"""Writes rumoro/_facade.py: one object over the generated client, one method per operation, grouped as the CLI's
noun:verb commands (packages/cli/src/naming.ts). Run after openapi-python-client has regenerated rumoro/."""

from __future__ import annotations

import enum
import importlib
import inspect
import json
import re
import sys
import typing
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
DOCUMENT = json.loads((ROOT.parent / "sdk" / "openapi.json").read_text())
SCHEMAS = DOCUMENT["components"]["schemas"]
# The generator's module for each operation: rumoro/api/<tag>/<operation>.py.
MODULES = {file.stem: f"{file.parent.name}.{file.stem}" for file in (ROOT / "rumoro" / "api").glob("*/*.py") if file.stem != "__init__"}

# The CLI's naming (packages/cli/src/naming.ts).
NAMED_VERBS = {
    "listPersonActivities": "activities", "logPersonActivity": "log-activity", "deletePersonActivity": "delete-activity",
    "listInvitations": "invitations", "createInvitation": "invite", "revokeInvitation": "revoke-invitation", "removeMember": "remove",
    "createTopUp": "top-up", "getInvoiceUrl": "invoice-url", "exportMentionsJson": "export-json",
}
SINGLETONS = {"company", "filters", "usage"}
# The order the groups are attached to the client in.
GROUP_ORDER = ["keywords", "mentions", "people", "segments", "alerts", "channels", "company", "analytics", "api-keys", "system",
               "filters", "views", "attention", "groups", "auth", "members", "usage", "billing"]


def command_name(operation_id: str, method: str, path: str) -> tuple[str, str]:
    segments = re.sub(r"^/v1/", "", path).split("/")
    noun = segments[0]
    if noun == "health":
        return "system", "health"
    if noun == "whoami":
        return "auth", "whoami"
    if operation_id in NAMED_VERBS:
        return noun, NAMED_VERBS[operation_id]
    rest = segments[1:]
    has_id = any(s.startswith("{") for s in rest)
    action = next((s for s in rest if not s.startswith("{")), None)
    if action is not None:
        verb = "export" if action == "export.csv" else action
    elif method == "get" and not has_id:
        verb = "search" if operation_id.startswith("search") else "get" if noun in SINGLETONS else "list"
    elif method == "post" and not has_id:
        verb = "create"
    elif method == "get":
        verb = "get"
    elif method == "patch":
        verb = "update"
    elif method == "delete":
        verb = "revoke" if operation_id.startswith("revoke") else "delete"
    else:
        verb = method
    return noun, verb


def snake(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def ident(name: str) -> str:
    return name.replace("-", "_")


def class_name(group: str) -> str:
    return "".join(part.capitalize() for part in re.split(r"[-_]", group))


def resolve(schema: dict) -> dict:
    return SCHEMAS[schema["$ref"].split("/")[-1]] if "$ref" in schema else schema


def members(hint: typing.Any) -> list:
    return list(typing.get_args(hint)) if typing.get_origin(hint) in (typing.Union, getattr(__import__("types"), "UnionType")) else [hint]


def model_name(hint: typing.Any) -> str:
    useful = [item for item in members(hint) if item is not type(None) and getattr(item, "__name__", "") != "ErrorResponse"]
    if len(useful) == 1 and useful[0] is str:
        return "str"
    if len(useful) == 1 and inspect.isclass(useful[0]) and useful[0].__module__.startswith("rumoro.models"):
        return f"_m.{useful[0].__name__}"
    return "Any"


def coercion(hint: typing.Any) -> str | None:
    for item in members(hint):
        if inspect.isclass(item) and issubclass(item, enum.Enum):
            return f"(_enum, _m.{item.__name__})"
        if typing.get_origin(item) is list:
            (inner,) = typing.get_args(item)
            if inspect.isclass(inner) and issubclass(inner, enum.Enum):
                return f"(_enum_list, _m.{inner.__name__})"
        if item is datetime:
            return "(_instant, None)"
    return None


def operations():
    for path, methods in DOCUMENT["paths"].items():
        for method, operation in methods.items():
            yield path, method, operation


def method_source(path: str, method: str, operation: dict, asynchronous: bool) -> tuple[str, str]:
    operation_id = operation["operationId"]
    group, verb = command_name(operation_id, method, path)
    module_path = MODULES[snake(operation_id)]
    module = importlib.import_module(f"rumoro.api.{module_path}")
    signature = inspect.signature(module.sync_detailed)
    hints = typing.get_type_hints(module.sync_detailed)
    positional = [name for name, p in signature.parameters.items() if p.kind is p.POSITIONAL_OR_KEYWORD]
    keyword = [name for name, p in signature.parameters.items() if p.kind is p.KEYWORD_ONLY and name not in ("client", "body")]
    query = [p for p in operation.get("parameters", []) if p["in"] == "query"]
    assert len(query) == len(keyword), (operation_id, keyword)
    json_body = operation.get("requestBody", {}).get("content", {}).get("application/json")

    args = ["self", *(f"{name}: str" for name in positional)]
    body_arg = ""
    if json_body:
        schema = resolve(json_body["schema"])
        if "oneOf" in schema:
            variants = [item["$ref"].split("/")[-1] for item in schema["oneOf"]]
            types = " | ".join(f"_m.{name}" for name in variants)
            kinds = ", ".join(f'"{resolve({"$ref": f"#/components/schemas/{name}"})["properties"]["kind"]["enum"][0]}": _m.{name}' for name in variants)
            target = "{" + kinds + "}"
        else:
            types = model_name(hints["body"])
            target = types
        args.append(f"body: dict[str, Any] | {types} | None = None")
        args.append("**fields: Any")
        body_arg = f", body=_body({target}, body, fields)"
    elif query:
        args.append("**params: Any")
    returns = model_name(typing.get_type_hints(module.sync)["return"])

    doc = [operation.get("summary", operation_id)]
    if operation.get("description"):
        doc += ["", operation["description"]]
    if query:
        doc += ["", "Keyword arguments (query):"]
        doc += [f"  {name}: {(p.get('description') or p['schema'].get('description') or '')}".rstrip() if (p.get("description") or p["schema"].get("description")) else f"  {name}:"
                for name, p in zip(keyword, query)]
    if json_body:
        schema = resolve(json_body["schema"])
        if "oneOf" in schema:
            fields, required = {}, set()
            for item in schema["oneOf"]:
                for name, prop in resolve(item).get("properties", {}).items():
                    fields.setdefault(name, prop)
        else:
            fields, required = schema.get("properties", {}), set(schema.get("required", []))
        kinds = [resolve(item)["properties"]["kind"]["enum"][0] for item in schema.get("oneOf", [])]
        doc += ["", f"Body: a dict with `kind` ({', '.join(kinds)}) or a model; fields may also be passed as keyword arguments:" if kinds
                else "Body: a dict, a model, or the fields as keyword arguments:"]
        for name, prop in fields.items():
            text = resolve(prop).get("description") if "$ref" in prop else prop.get("description")
            label = f"{name} (required)" if name in required else name
            doc.append(f"  {label}: {text}" if text else f"  {label}:")
    docstring = "\n        ".join(doc).replace("\n        \n", "\n\n")

    table = [(name, coercion(hints[name])) for name in keyword]
    table = [f'"{name}": {value}' for name, value in table if value]
    lines = [f"    {'async ' if asynchronous else ''}def {ident(verb)}({', '.join(args)}) -> {returns}:", f'        """{docstring}"""']
    if table:
        lines.append(f"        _coerce(params, {{{', '.join(table)}}})")
    call_args = ", ".join([*positional, "client=self._client"]) + body_arg + (", **params" if query and not json_body else "")
    call = f"{'await ' if asynchronous else ''}_ops.{module_path}.{'asyncio_detailed' if asynchronous else 'sync_detailed'}({call_args})"
    lines.append(f"        return _result({call})")
    return group, verb, "\n".join(lines), module_path


def group_classes(asynchronous: bool) -> tuple[list[str], set[str]]:
    groups: dict[str, list[tuple[str, str]]] = {}
    modules = set()
    for path, method, operation in operations():
        group, verb, source, module_path = method_source(path, method, operation, asynchronous)
        groups.setdefault(group, []).append((ident(verb), source))
        modules.add(module_path)
    ordered = [g for g in GROUP_ORDER if g in groups] + [g for g in groups if g not in GROUP_ORDER]
    classes = []
    for group in ordered:
        methods = sorted(groups[group])
        name = f"_{'Async' if asynchronous else ''}{class_name(group)}"
        head = [f"class {name}:", f'    """{group}: {", ".join(verb for verb, _ in methods)}."""', "",
                "    def __init__(self, client: AuthenticatedClient) -> None:", "        self._client = client"]
        classes.append("\n".join(head) + "\n\n" + "\n\n".join(source for _, source in methods) + "\n")
    return [ordered, classes], modules


HEADER = '''"""Convenience layer over the generated client: one object, one call per endpoint.

Generated by scripts/generate_facade.py from the OpenAPI document; do not edit.
Groups and method names follow the CLI's noun:verb rule.
"""

from __future__ import annotations

import datetime as _dt
import json
from typing import Any

import httpx

from . import api as _ops  # noqa: F401
from . import models as _m
from .client import AuthenticatedClient
from .types import UNSET, Response

DEFAULT_BASE_URL = "https://api.rumoro.dev"


class RumoroError(Exception):
    """A non-2xx answer: the HTTP `status`, the API's stable `code`, and its `message`."""

    def __init__(self, status: int, code: str, message: str) -> None:
        super().__init__(f"{code}: {message} (HTTP {status})")
        self.status = status
        self.code = code
        self.message = message


def _result(response: Response[Any]) -> Any:
    status = int(response.status_code)
    if 200 <= status < 300:
        return response.parsed
    parsed = response.parsed
    if isinstance(parsed, _m.ErrorResponse):
        raise RumoroError(status, parsed.error.code, parsed.error.message)
    # A status the operation doesn't declare (a 400 or 429 on most calls) is not parsed, but the body is the same envelope.
    try:
        error = json.loads(response.content)["error"]
        if isinstance(error["code"], str) and isinstance(error["message"], str):
            raise RumoroError(status, error["code"], error["message"])
    except (ValueError, KeyError, TypeError):
        pass
    raise RumoroError(status, f"http_{status}", response.content[:300].decode(errors="replace"))


def _enum(cls: type, value: Any) -> Any:
    if value is UNSET or value is None or isinstance(value, cls):
        return value
    return cls(value)


def _enum_list(cls: type, values: Any) -> Any:
    if values is UNSET or values is None:
        return values
    return [_enum(cls, v) for v in values]


def _instant(_cls: Any, value: Any) -> Any:
    if value is UNSET or value is None or isinstance(value, _dt.datetime):
        return value
    if isinstance(value, (int, float)):
        return _dt.datetime.fromtimestamp(value / 1000, tz=_dt.timezone.utc)
    if isinstance(value, _dt.date):
        return _dt.datetime(value.year, value.month, value.day, tzinfo=_dt.timezone.utc)
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = _dt.datetime.fromisoformat(text)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=_dt.timezone.utc)


def _coerce(params: dict[str, Any], table: dict[str, tuple[Any, Any]]) -> None:
    for name, (fn, cls) in table.items():
        if name in params:
            params[name] = fn(cls, params[name])


def _body(target: Any, body: Any, fields: dict[str, Any]) -> Any:
    data = body if body is not None else fields
    if not isinstance(data, dict):
        return data
    if isinstance(target, dict):
        kind = data.get("kind")
        cls = target.get(kind)
        if cls is None:
            raise ValueError(f"kind must be one of: {', '.join(target)}")
        return cls.from_dict(data)
    return target.from_dict(data)
'''


def client_class(name: str, ordered: list[str], asynchronous: bool) -> str:
    usage = "mentions = await client.mentions.search(platform=\"hackernews\", relevant=True)" if asynchronous \
        else "mentions = client.mentions.search(platform=\"hackernews\", relevant=True)"
    attach = "\n".join(f"        self.{ident(group)} = _{'Async' if asynchronous else ''}{class_name(group)}(self.client)" for group in ordered)
    enter = (f'    async def __aenter__(self) -> "{name}":\n        await self.client.__aenter__()\n        return self\n\n'
             f"    async def __aexit__(self, *args: Any) -> None:\n        await self.client.__aexit__(*args)") if asynchronous else \
            (f'    def __enter__(self) -> "{name}":\n        self.client.__enter__()\n        return self\n\n'
             f"    def __exit__(self, *args: Any) -> None:\n        self.client.__exit__(*args)")
    return f'''class {name}:
    """The Rumoro API{", awaitable" if asynchronous else ""}: one object, one call per endpoint, grouped by resource.

    client = {name}(api_key)
    {usage}

    Every call returns the parsed response (the generated model, a str for CSV
    exports, None for a 204) or raises RumoroError with the API's status, code
    and message. Enum-valued arguments take plain strings, instants take a
    datetime, an ISO 8601 string or epoch milliseconds, bodies take a dict, a
    model, or their fields as keyword arguments. `client` is the underlying
    AuthenticatedClient for anything the facade does not cover.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | None = 30.0,
        headers: dict[str, str] | None = None,
        httpx_args: dict[str, Any] | None = None,
    ) -> None:
        self.client = AuthenticatedClient(
            base_url=base_url.rstrip("/"),
            token=api_key,
            prefix="Bearer",
            headers=headers or {{}},
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
            httpx_args=httpx_args or {{}},
        )
{attach}

{enter}
'''


def main() -> None:
    (ordered, sync_classes), modules = group_classes(False)
    (_, async_classes), _ = group_classes(True)
    imports = "\n".join(f"import rumoro.api.{module}  # noqa: F401" for module in sorted(modules))
    text = (HEADER + "\n\n\n" + imports + "\n\n\n" + "\n".join(sync_classes) + "\n" + "\n".join(async_classes) + "\n"
            + client_class("Rumoro", ordered, False) + "\n" + client_class("AsyncRumoro", ordered, True))
    (ROOT / "rumoro" / "_facade.py").write_text(text)
    (ROOT / "rumoro" / "__init__.py").write_text('''"""A client library for accessing Rumoro API"""

from ._facade import DEFAULT_BASE_URL, AsyncRumoro, Rumoro, RumoroError
from .client import AuthenticatedClient, Client

__all__ = (
    "DEFAULT_BASE_URL",
    "AsyncRumoro",
    "AuthenticatedClient",
    "Client",
    "Rumoro",
    "RumoroError",
)
''')
    print(f"{len(modules)} operations in {len(ordered)} groups")


if __name__ == "__main__":
    main()
