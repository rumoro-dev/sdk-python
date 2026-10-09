from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_attention_response_200 import ListAttentionResponse200
from ...models.list_attention_status import ListAttentionStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["kind"] = kind

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/attention",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListAttentionResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAttentionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ListAttentionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAttentionResponse200]:
    """List attention items

     Lists items that need a person, latest first. Kinds are mention.spike (a keyword's mentions jumped
    in the last hour), sentiment.negative_spike (its 24-hour negative share jumped), keyword.noisy (it
    turned noisy) and channel.failing (a channel's recent sends all failed). Checks run hourly. Items
    open when the condition starts and resolve when it ends. Open items are the default, and
    `status=all` adds the history. Opening an item also sends an account event of the same name to
    subscribed webhook, Slack, email and Telegram channels.

    Args:
        status (ListAttentionStatus | Unset): Which items to list. Defaults to open. Default:
            ListAttentionStatus.OPEN.
        kind (str | Unset): Filters by kind. Send a comma-separated list such as
            mention.spike,keyword.noisy.
        limit (int | Unset): How many items to return, latest first. 50 by default and 100 at
            most. Default: 50.
        cursor (str | Unset): Pass the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAttentionResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAttentionResponse200 | None:
    """List attention items

     Lists items that need a person, latest first. Kinds are mention.spike (a keyword's mentions jumped
    in the last hour), sentiment.negative_spike (its 24-hour negative share jumped), keyword.noisy (it
    turned noisy) and channel.failing (a channel's recent sends all failed). Checks run hourly. Items
    open when the condition starts and resolve when it ends. Open items are the default, and
    `status=all` adds the history. Opening an item also sends an account event of the same name to
    subscribed webhook, Slack, email and Telegram channels.

    Args:
        status (ListAttentionStatus | Unset): Which items to list. Defaults to open. Default:
            ListAttentionStatus.OPEN.
        kind (str | Unset): Filters by kind. Send a comma-separated list such as
            mention.spike,keyword.noisy.
        limit (int | Unset): How many items to return, latest first. 50 by default and 100 at
            most. Default: 50.
        cursor (str | Unset): Pass the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAttentionResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | ListAttentionResponse200]:
    """List attention items

     Lists items that need a person, latest first. Kinds are mention.spike (a keyword's mentions jumped
    in the last hour), sentiment.negative_spike (its 24-hour negative share jumped), keyword.noisy (it
    turned noisy) and channel.failing (a channel's recent sends all failed). Checks run hourly. Items
    open when the condition starts and resolve when it ends. Open items are the default, and
    `status=all` adds the history. Opening an item also sends an account event of the same name to
    subscribed webhook, Slack, email and Telegram channels.

    Args:
        status (ListAttentionStatus | Unset): Which items to list. Defaults to open. Default:
            ListAttentionStatus.OPEN.
        kind (str | Unset): Filters by kind. Send a comma-separated list such as
            mention.spike,keyword.noisy.
        limit (int | Unset): How many items to return, latest first. 50 by default and 100 at
            most. Default: 50.
        cursor (str | Unset): Pass the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListAttentionResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: ListAttentionStatus | Unset = ListAttentionStatus.OPEN,
    kind: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | ListAttentionResponse200 | None:
    """List attention items

     Lists items that need a person, latest first. Kinds are mention.spike (a keyword's mentions jumped
    in the last hour), sentiment.negative_spike (its 24-hour negative share jumped), keyword.noisy (it
    turned noisy) and channel.failing (a channel's recent sends all failed). Checks run hourly. Items
    open when the condition starts and resolve when it ends. Open items are the default, and
    `status=all` adds the history. Opening an item also sends an account event of the same name to
    subscribed webhook, Slack, email and Telegram channels.

    Args:
        status (ListAttentionStatus | Unset): Which items to list. Defaults to open. Default:
            ListAttentionStatus.OPEN.
        kind (str | Unset): Filters by kind. Send a comma-separated list such as
            mention.spike,keyword.noisy.
        limit (int | Unset): How many items to return, latest first. 50 by default and 100 at
            most. Default: 50.
        cursor (str | Unset): Pass the previous page's nextCursor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListAttentionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            kind=kind,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
