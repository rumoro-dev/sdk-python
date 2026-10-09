"""The facade against a mock transport: requests as the API reads them, answers as models, errors as RumoroError."""

from __future__ import annotations

import inspect
import json
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from rumoro import AsyncRumoro, Rumoro, RumoroError

KEY = "ref_0123abcd-0000-4000-8000-000000000000_" + "A" * 43
WHOAMI = {"workspace": {"id": "org_1", "name": "Acme"}, "auth": {"kind": "api_key", "scope": "write", "apiKeyId": "key_1", "expiresAt": None}, "user": None}


def recorded(answer):
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return answer(request)

    return requests, httpx.MockTransport(handler)


def methods(client) -> dict[str, list[str]]:
    groups = {name: value for name, value in vars(client).items() if name != "client"}
    return {name: [m for m, _ in inspect.getmembers(group, inspect.ismethod) if not m.startswith("_")] for name, group in groups.items()}


def test_one_method_per_operation_in_eighteen_groups():
    sync, asynchronous = methods(Rumoro(KEY)), methods(AsyncRumoro(KEY))
    assert sum(len(names) for names in sync.values()) == 80
    assert len(sync) == 18
    assert sync == asynchronous
    assert sync["mentions"] == ["export", "export_json", "get", "search", "update"]
    assert sync["channels"] == ["create", "delete", "deliveries", "get", "list", "rotate_secret", "test", "update"]


def test_requests_key_base_url_enums_instants_and_bodies():
    requests, transport = recorded(lambda request: httpx.Response(200, json={"data": [], "total": 0, "truncated": False}))
    rumoro = Rumoro(KEY, base_url="http://127.0.0.1:3000/api/", headers={"x-request-id": "py-request-0001"}, httpx_args={"transport": transport})
    rumoro.keywords.list(kind=["brand", "topic"], limit=5)
    rumoro.mentions.export_json(since=1_700_000_000_000, platforms=["x"])
    first, second = requests
    assert str(first.url).startswith("http://127.0.0.1:3000/api/v1/keywords?")
    assert first.headers["authorization"] == f"Bearer {KEY}"
    assert first.headers["x-request-id"] == "py-request-0001"
    assert parse_qs(urlsplit(str(first.url)).query) == {"kind": ["brand", "topic"], "limit": ["5"], "sort": ["newest"], "offset": ["0"]}
    query = parse_qs(urlsplit(str(second.url)).query)
    assert query["since"] == ["2023-11-14T22:13:20+00:00"]
    assert query["platforms"] == ["x"]


def test_coerced_lists_the_generated_code_leaves_raw():
    # The generated code expects enum members for these two (`.value`), so the facade coerces plain strings first.
    requests, transport = recorded(lambda request: httpx.Response(200, json={"data": [], "truncated": False}) if "mentions" in request.url.path
                                   else httpx.Response(200, text="handle\n", headers={"content-type": "text/csv"}))
    rumoro = Rumoro(KEY, httpx_args={"transport": transport})
    rumoro.mentions.export_json(not_sentiments=["negative"])
    assert rumoro.people.export(never_keyword_kinds=["competitor"]) == "handle\n"
    assert parse_qs(urlsplit(str(requests[0].url)).query)["notSentiments"] == ["negative"]
    assert parse_qs(urlsplit(str(requests[1].url)).query)["neverKeywordKinds"] == ["competitor"]


def test_bodies_as_dict_kwargs_or_a_kind_dict_and_answers_as_models():
    def answer(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/whoami":
            return httpx.Response(200, json=WHOAMI)
        if request.url.path == "/v1/channels":
            # Only the request body matters here; the live run parses real channels.
            return httpx.Response(400, json={"error": {"code": "validation_error", "message": "url: Invalid URL"}})
        return httpx.Response(204)

    requests, transport = recorded(answer)
    rumoro = Rumoro(KEY, httpx_args={"transport": transport})
    assert rumoro.auth.whoami().workspace.name == "Acme"
    with pytest.raises(RumoroError, match="validation_error"):
        rumoro.channels.create(kind="webhook", url="https://example.com/hook")
    assert json.loads(requests[1].content) == {"kind": "webhook", "url": "https://example.com/hook"}
    with pytest.raises(ValueError, match="kind must be one of: slack, email, webhook"):
        rumoro.channels.create({"kind": "pager"})
    assert rumoro.alerts.delete("feed_1") is None


def test_errors_raise_rumoro_error_with_status_and_code():
    _, transport = recorded(lambda request: httpx.Response(409, json={"error": {"code": "duplicate_keyword", "message": "Already tracked", "requestId": "req_1"}}))
    rumoro = Rumoro(KEY, httpx_args={"transport": transport})
    with pytest.raises(RumoroError) as raised:
        rumoro.keywords.create(term="acme", kind="brand")
    assert (raised.value.status, raised.value.code, raised.value.message) == (409, "duplicate_keyword", "Already tracked")
    assert str(raised.value) == "duplicate_keyword: Already tracked (HTTP 409)"


def test_undeclared_statuses_keep_the_api_code():
    # createKeyword declares no 400 and searchMentions no 429; the code still comes from the envelope (October 4).
    answers = iter([
        httpx.Response(400, json={"error": {"code": "validation_error", "message": "term: too short"}}),
        httpx.Response(429, json={"error": {"code": "rate_limited", "message": "wait", "retryAfterSeconds": 8}}),
        httpx.Response(502, text="<html>Bad gateway</html>"),
    ])
    _, transport = recorded(lambda request: next(answers))
    rumoro = Rumoro(KEY, httpx_args={"transport": transport})
    for call, expected in [(lambda: rumoro.keywords.create(term="a", kind="brand"), (400, "validation_error")),
                           (lambda: rumoro.mentions.search(limit=1), (429, "rate_limited")),
                           (lambda: rumoro.mentions.search(limit=1), (502, "http_502"))]:
        with pytest.raises(RumoroError) as raised:
            call()
        assert (raised.value.status, raised.value.code) == expected


async def test_async_client_mirrors_the_calls():
    requests, transport = recorded(lambda request: httpx.Response(200, json=WHOAMI))
    async with AsyncRumoro(KEY, httpx_args={"transport": transport}) as rumoro:
        assert (await rumoro.auth.whoami()).workspace.name == "Acme"
    assert requests[0].headers["authorization"] == f"Bearer {KEY}"
