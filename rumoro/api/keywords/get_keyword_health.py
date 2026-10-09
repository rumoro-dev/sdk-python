from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_keyword_health_range import GetKeywordHealthRange
from ...models.keyword_health import KeywordHealth
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["ai"] = ai

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/keywords/{id}/health".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | KeywordHealth | None:
    if response.status_code == 200:
        response_200 = KeywordHealth.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | KeywordHealth]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> Response[ErrorResponse | KeywordHealth]:
    """Check a keyword's health

     Checks whether the keyword earns its cost over `range` (default 30d). Returns a status (healthy,
    noisy, quiet, capped, paused or new) with plain-word reasons, numbers by platform and week, cost,
    the words and authors behind the noise, and suggestions. Send a suggestion's `patch` unchanged to
    PATCH /v1/keywords/{id}. Its effect comes from replaying the matcher's rules on the window's posts.
    `ai=true` adds a model-written context (cached a day, up to 20 model calls an hour per workspace).
    Read only and never billed. Reports are cached 5 minutes and rebuilt after a keyword change. Up to
    30 reads a minute per workspace.

    Args:
        id (str): The keyword's id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): How many UTC days back from today to read, by
            match time. One of 7d, 30d or 90d, 30d by default.
        ai (bool | Unset): true also asks a language model to rewrite the context. The answer is
            cached for a day per keyword and window, with at most 20 model calls an hour per
            workspace. With the default false, all suggestions come from the rules only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordHealth]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        ai=ai,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> ErrorResponse | KeywordHealth | None:
    """Check a keyword's health

     Checks whether the keyword earns its cost over `range` (default 30d). Returns a status (healthy,
    noisy, quiet, capped, paused or new) with plain-word reasons, numbers by platform and week, cost,
    the words and authors behind the noise, and suggestions. Send a suggestion's `patch` unchanged to
    PATCH /v1/keywords/{id}. Its effect comes from replaying the matcher's rules on the window's posts.
    `ai=true` adds a model-written context (cached a day, up to 20 model calls an hour per workspace).
    Read only and never billed. Reports are cached 5 minutes and rebuilt after a keyword change. Up to
    30 reads a minute per workspace.

    Args:
        id (str): The keyword's id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): How many UTC days back from today to read, by
            match time. One of 7d, 30d or 90d, 30d by default.
        ai (bool | Unset): true also asks a language model to rewrite the context. The answer is
            cached for a day per keyword and window, with at most 20 model calls an hour per
            workspace. With the default false, all suggestions come from the rules only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordHealth
    """

    return sync_detailed(
        id=id,
        client=client,
        range_=range_,
        ai=ai,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> Response[ErrorResponse | KeywordHealth]:
    """Check a keyword's health

     Checks whether the keyword earns its cost over `range` (default 30d). Returns a status (healthy,
    noisy, quiet, capped, paused or new) with plain-word reasons, numbers by platform and week, cost,
    the words and authors behind the noise, and suggestions. Send a suggestion's `patch` unchanged to
    PATCH /v1/keywords/{id}. Its effect comes from replaying the matcher's rules on the window's posts.
    `ai=true` adds a model-written context (cached a day, up to 20 model calls an hour per workspace).
    Read only and never billed. Reports are cached 5 minutes and rebuilt after a keyword change. Up to
    30 reads a minute per workspace.

    Args:
        id (str): The keyword's id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): How many UTC days back from today to read, by
            match time. One of 7d, 30d or 90d, 30d by default.
        ai (bool | Unset): true also asks a language model to rewrite the context. The answer is
            cached for a day per keyword and window, with at most 20 model calls an hour per
            workspace. With the default false, all suggestions come from the rules only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | KeywordHealth]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        ai=ai,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: GetKeywordHealthRange | Unset = UNSET,
    ai: bool | Unset = UNSET,
) -> ErrorResponse | KeywordHealth | None:
    """Check a keyword's health

     Checks whether the keyword earns its cost over `range` (default 30d). Returns a status (healthy,
    noisy, quiet, capped, paused or new) with plain-word reasons, numbers by platform and week, cost,
    the words and authors behind the noise, and suggestions. Send a suggestion's `patch` unchanged to
    PATCH /v1/keywords/{id}. Its effect comes from replaying the matcher's rules on the window's posts.
    `ai=true` adds a model-written context (cached a day, up to 20 model calls an hour per workspace).
    Read only and never billed. Reports are cached 5 minutes and rebuilt after a keyword change. Up to
    30 reads a minute per workspace.

    Args:
        id (str): The keyword's id (kw_...). Example: kw_abc123.
        range_ (GetKeywordHealthRange | Unset): How many UTC days back from today to read, by
            match time. One of 7d, 30d or 90d, 30d by default.
        ai (bool | Unset): true also asks a language model to rewrite the context. The answer is
            cached for a day per keyword and window, with at most 20 model calls an hour per
            workspace. With the default false, all suggestions come from the rules only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | KeywordHealth
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            range_=range_,
            ai=ai,
        )
    ).parsed
