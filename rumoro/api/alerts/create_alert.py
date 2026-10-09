from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert import Alert
from ...models.create_alert_body import CreateAlertBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAlertBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alerts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Alert | ErrorResponse | None:
    if response.status_code == 201:
        response_201 = Alert.from_dict(response.json())

        return response_201

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
) -> Response[Alert | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAlertBody,
) -> Response[Alert | ErrorResponse]:
    """Create an alert

     Creates an alert, which pairs a filter with one or more channels. instant mode sends each matching
    mention as it arrives. hourly sends a digest of the previous full UTC hour at five past, skips hours
    with no mention above the rule's minimum, takes no schedule and works with Slack, Telegram and
    webhook channels only. daily sends one digest at schedule.hour in schedule.timezone. weekly sends
    one a week on schedule.weekday, from 0 for Sunday to 6 for Saturday. filter.anyOf adds OR logic with
    groups of mention-list conditions. At least one group must match, as well as the rest of the filter.

    Args:
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateAlertBody,
) -> Alert | ErrorResponse | None:
    """Create an alert

     Creates an alert, which pairs a filter with one or more channels. instant mode sends each matching
    mention as it arrives. hourly sends a digest of the previous full UTC hour at five past, skips hours
    with no mention above the rule's minimum, takes no schedule and works with Slack, Telegram and
    webhook channels only. daily sends one digest at schedule.hour in schedule.timezone. weekly sends
    one a week on schedule.weekday, from 0 for Sunday to 6 for Saturday. filter.anyOf adds OR logic with
    groups of mention-list conditions. At least one group must match, as well as the rest of the filter.

    Args:
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAlertBody,
) -> Response[Alert | ErrorResponse]:
    """Create an alert

     Creates an alert, which pairs a filter with one or more channels. instant mode sends each matching
    mention as it arrives. hourly sends a digest of the previous full UTC hour at five past, skips hours
    with no mention above the rule's minimum, takes no schedule and works with Slack, Telegram and
    webhook channels only. daily sends one digest at schedule.hour in schedule.timezone. weekly sends
    one a week on schedule.weekday, from 0 for Sunday to 6 for Saturday. filter.anyOf adds OR logic with
    groups of mention-list conditions. At least one group must match, as well as the rest of the filter.

    Args:
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateAlertBody,
) -> Alert | ErrorResponse | None:
    """Create an alert

     Creates an alert, which pairs a filter with one or more channels. instant mode sends each matching
    mention as it arrives. hourly sends a digest of the previous full UTC hour at five past, skips hours
    with no mention above the rule's minimum, takes no schedule and works with Slack, Telegram and
    webhook channels only. daily sends one digest at schedule.hour in schedule.timezone. weekly sends
    one a week on schedule.weekday, from 0 for Sunday to 6 for Saturday. filter.anyOf adds OR logic with
    groups of mention-list conditions. At least one group must match, as well as the rest of the filter.

    Args:
        body (CreateAlertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
