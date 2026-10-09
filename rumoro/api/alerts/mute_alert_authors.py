from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert import Alert
from ...models.error_response import ErrorResponse
from ...models.mute_alert_authors_body import MuteAlertAuthorsBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: MuteAlertAuthorsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alerts/{id}/mute".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Alert | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = Alert.from_dict(response.json())

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: MuteAlertAuthorsBody,
) -> Response[Alert | ErrorResponse]:
    """Mute authors

     Adds authors to the alert's muted list and leaves the rest of its filter alone. Links are handled as
    in the dashboard, so a post link mutes its author, twitter.com turns into x.com and a Hacker News
    profile keeps its id. Authors who are already muted are skipped, so retrying is safe. An entry that
    is not a person, such as a subreddit or a story, fails the request and the error names it.

    Args:
        id (str): The alert's id (feed_...). Example: feed_abc123.
        body (MuteAlertAuthorsBody): The authors to add to the alert's muted list, or take off it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: MuteAlertAuthorsBody,
) -> Alert | ErrorResponse | None:
    """Mute authors

     Adds authors to the alert's muted list and leaves the rest of its filter alone. Links are handled as
    in the dashboard, so a post link mutes its author, twitter.com turns into x.com and a Hacker News
    profile keeps its id. Authors who are already muted are skipped, so retrying is safe. An entry that
    is not a person, such as a subreddit or a story, fails the request and the error names it.

    Args:
        id (str): The alert's id (feed_...). Example: feed_abc123.
        body (MuteAlertAuthorsBody): The authors to add to the alert's muted list, or take off it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: MuteAlertAuthorsBody,
) -> Response[Alert | ErrorResponse]:
    """Mute authors

     Adds authors to the alert's muted list and leaves the rest of its filter alone. Links are handled as
    in the dashboard, so a post link mutes its author, twitter.com turns into x.com and a Hacker News
    profile keeps its id. Authors who are already muted are skipped, so retrying is safe. An entry that
    is not a person, such as a subreddit or a story, fails the request and the error names it.

    Args:
        id (str): The alert's id (feed_...). Example: feed_abc123.
        body (MuteAlertAuthorsBody): The authors to add to the alert's muted list, or take off it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: MuteAlertAuthorsBody,
) -> Alert | ErrorResponse | None:
    """Mute authors

     Adds authors to the alert's muted list and leaves the rest of its filter alone. Links are handled as
    in the dashboard, so a post link mutes its author, twitter.com turns into x.com and a Hacker News
    profile keeps its id. Authors who are already muted are skipped, so retrying is safe. An entry that
    is not a person, such as a subreddit or a story, fails the request and the error names it.

    Args:
        id (str): The alert's id (feed_...). Example: feed_abc123.
        body (MuteAlertAuthorsBody): The authors to add to the alert's muted list, or take off it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
