from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_usage_breakdown_by import GetUsageBreakdownBy
from ...models.get_usage_breakdown_range import GetUsageBreakdownRange
from ...models.usage_breakdown import UsageBreakdown
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_by: str | Unset = UNSET
    if not isinstance(by, Unset):
        json_by = by.value

    params["by"] = json_by

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["month"] = month

    params["limit"] = limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UsageBreakdown | None:
    if response.status_code == 200:
        response_200 = UsageBreakdown.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | UsageBreakdown]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | UsageBreakdown]:
    """Get the usage breakdown

     Returns what the workspace used and was charged over a period, in US cents at list price. Each call
    groups rows by one `by` value, day, platform or keyword, and always includes the totals. `range`
    reads the past UTC days up to today (30d by default). `month` reads one calendar month (YYYY-MM),
    which is what you match against a bill or a per-client margin. Keyword-days come from the daily run
    and mention charges from billed matches. So a deleted keyword keeps its charges in the keyword rows
    (`keyword.removed`), while its mention counts show 0. Each keyword carries the same numbers for the
    current month as `stats.cost`. `totals.ledgerDebitCents` is what the balance has been debited so far
    for the period's days. Mentions settle the morning after, so a period ending today is below
    `totals.totalCents` by the unsettled ones, and a finished month differs only by cumulative rounding.
    Rows come in pages (`limit`, `offset`, `total`). A workspace can call this 30 times a minute across
    all its keys and tokens.

    Args:
        by (GetUsageBreakdownBy | Unset): How to group the rows. day gives one row per UTC day,
            then platform, keyword (the default, used to work out margins), or group (the cost of a
            client or campaign). Default: GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): How many UTC days back from today to read. One of
            7d, 30d or 90d, 30d by default. Ignored when you send `month`.
        month (str | Unset): A calendar month (YYYY-MM, UTC) to read instead of a range. It covers
            the month's first to last day, or up to today for the current month. A future month
            returns 400.
        limit (int | Unset): How many rows to return, from 1 to 500, 100 by default. Only
            by=keyword can need more than one page, since a period has at most 90 days and there are
            only a dozen platforms. Default: 100.
        offset (int | None | Unset): How many rows to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UsageBreakdown]
    """

    kwargs = _get_kwargs(
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | UsageBreakdown | None:
    """Get the usage breakdown

     Returns what the workspace used and was charged over a period, in US cents at list price. Each call
    groups rows by one `by` value, day, platform or keyword, and always includes the totals. `range`
    reads the past UTC days up to today (30d by default). `month` reads one calendar month (YYYY-MM),
    which is what you match against a bill or a per-client margin. Keyword-days come from the daily run
    and mention charges from billed matches. So a deleted keyword keeps its charges in the keyword rows
    (`keyword.removed`), while its mention counts show 0. Each keyword carries the same numbers for the
    current month as `stats.cost`. `totals.ledgerDebitCents` is what the balance has been debited so far
    for the period's days. Mentions settle the morning after, so a period ending today is below
    `totals.totalCents` by the unsettled ones, and a finished month differs only by cumulative rounding.
    Rows come in pages (`limit`, `offset`, `total`). A workspace can call this 30 times a minute across
    all its keys and tokens.

    Args:
        by (GetUsageBreakdownBy | Unset): How to group the rows. day gives one row per UTC day,
            then platform, keyword (the default, used to work out margins), or group (the cost of a
            client or campaign). Default: GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): How many UTC days back from today to read. One of
            7d, 30d or 90d, 30d by default. Ignored when you send `month`.
        month (str | Unset): A calendar month (YYYY-MM, UTC) to read instead of a range. It covers
            the month's first to last day, or up to today for the current month. A future month
            returns 400.
        limit (int | Unset): How many rows to return, from 1 to 500, 100 by default. Only
            by=keyword can need more than one page, since a period has at most 90 days and there are
            only a dozen platforms. Default: 100.
        offset (int | None | Unset): How many rows to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UsageBreakdown
    """

    return sync_detailed(
        client=client,
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | UsageBreakdown]:
    """Get the usage breakdown

     Returns what the workspace used and was charged over a period, in US cents at list price. Each call
    groups rows by one `by` value, day, platform or keyword, and always includes the totals. `range`
    reads the past UTC days up to today (30d by default). `month` reads one calendar month (YYYY-MM),
    which is what you match against a bill or a per-client margin. Keyword-days come from the daily run
    and mention charges from billed matches. So a deleted keyword keeps its charges in the keyword rows
    (`keyword.removed`), while its mention counts show 0. Each keyword carries the same numbers for the
    current month as `stats.cost`. `totals.ledgerDebitCents` is what the balance has been debited so far
    for the period's days. Mentions settle the morning after, so a period ending today is below
    `totals.totalCents` by the unsettled ones, and a finished month differs only by cumulative rounding.
    Rows come in pages (`limit`, `offset`, `total`). A workspace can call this 30 times a minute across
    all its keys and tokens.

    Args:
        by (GetUsageBreakdownBy | Unset): How to group the rows. day gives one row per UTC day,
            then platform, keyword (the default, used to work out margins), or group (the cost of a
            client or campaign). Default: GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): How many UTC days back from today to read. One of
            7d, 30d or 90d, 30d by default. Ignored when you send `month`.
        month (str | Unset): A calendar month (YYYY-MM, UTC) to read instead of a range. It covers
            the month's first to last day, or up to today for the current month. A future month
            returns 400.
        limit (int | Unset): How many rows to return, from 1 to 500, 100 by default. Only
            by=keyword can need more than one page, since a period has at most 90 days and there are
            only a dozen platforms. Default: 100.
        offset (int | None | Unset): How many rows to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UsageBreakdown]
    """

    kwargs = _get_kwargs(
        by=by,
        range_=range_,
        month=month,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    by: GetUsageBreakdownBy | Unset = GetUsageBreakdownBy.KEYWORD,
    range_: GetUsageBreakdownRange | Unset = UNSET,
    month: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | None | Unset = 0,
) -> ErrorResponse | UsageBreakdown | None:
    """Get the usage breakdown

     Returns what the workspace used and was charged over a period, in US cents at list price. Each call
    groups rows by one `by` value, day, platform or keyword, and always includes the totals. `range`
    reads the past UTC days up to today (30d by default). `month` reads one calendar month (YYYY-MM),
    which is what you match against a bill or a per-client margin. Keyword-days come from the daily run
    and mention charges from billed matches. So a deleted keyword keeps its charges in the keyword rows
    (`keyword.removed`), while its mention counts show 0. Each keyword carries the same numbers for the
    current month as `stats.cost`. `totals.ledgerDebitCents` is what the balance has been debited so far
    for the period's days. Mentions settle the morning after, so a period ending today is below
    `totals.totalCents` by the unsettled ones, and a finished month differs only by cumulative rounding.
    Rows come in pages (`limit`, `offset`, `total`). A workspace can call this 30 times a minute across
    all its keys and tokens.

    Args:
        by (GetUsageBreakdownBy | Unset): How to group the rows. day gives one row per UTC day,
            then platform, keyword (the default, used to work out margins), or group (the cost of a
            client or campaign). Default: GetUsageBreakdownBy.KEYWORD.
        range_ (GetUsageBreakdownRange | Unset): How many UTC days back from today to read. One of
            7d, 30d or 90d, 30d by default. Ignored when you send `month`.
        month (str | Unset): A calendar month (YYYY-MM, UTC) to read instead of a range. It covers
            the month's first to last day, or up to today for the current month. A future month
            returns 400.
        limit (int | Unset): How many rows to return, from 1 to 500, 100 by default. Only
            by=keyword can need more than one page, since a period has at most 90 days and there are
            only a dozen platforms. Default: 100.
        offset (int | None | Unset): How many rows to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UsageBreakdown
    """

    return (
        await asyncio_detailed(
            client=client,
            by=by,
            range_=range_,
            month=month,
            limit=limit,
            offset=offset,
        )
    ).parsed
