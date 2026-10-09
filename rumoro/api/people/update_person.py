from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.person import Person
from ...models.update_person_body import UpdatePersonBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdatePersonBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/people/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Person | None:
    if response.status_code == 200:
        response_200 = Person.from_dict(response.json())

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
) -> Response[ErrorResponse | Person]:
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
    body: UpdatePersonBody,
) -> Response[ErrorResponse | Person]:
    """Update a person

     Changes your workspace's tags, notes and mute for the person, and the outreach owner and stage. The
    owner must be a workspace member, and null removes it. Muting hides their posts from your feed and
    all channels. Collection and billing do not change.

    Args:
        id (str): The person's id (aut_...). Example: aut_abc123.
        body (UpdatePersonBody): Fields you leave out stay as they are.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Person]
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
    body: UpdatePersonBody,
) -> ErrorResponse | Person | None:
    """Update a person

     Changes your workspace's tags, notes and mute for the person, and the outreach owner and stage. The
    owner must be a workspace member, and null removes it. Muting hides their posts from your feed and
    all channels. Collection and billing do not change.

    Args:
        id (str): The person's id (aut_...). Example: aut_abc123.
        body (UpdatePersonBody): Fields you leave out stay as they are.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Person
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
    body: UpdatePersonBody,
) -> Response[ErrorResponse | Person]:
    """Update a person

     Changes your workspace's tags, notes and mute for the person, and the outreach owner and stage. The
    owner must be a workspace member, and null removes it. Muting hides their posts from your feed and
    all channels. Collection and billing do not change.

    Args:
        id (str): The person's id (aut_...). Example: aut_abc123.
        body (UpdatePersonBody): Fields you leave out stay as they are.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Person]
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
    body: UpdatePersonBody,
) -> ErrorResponse | Person | None:
    """Update a person

     Changes your workspace's tags, notes and mute for the person, and the outreach owner and stage. The
    owner must be a workspace member, and null removes it. Muting hides their posts from your feed and
    all channels. Collection and billing do not change.

    Args:
        id (str): The person's id (aut_...). Example: aut_abc123.
        body (UpdatePersonBody): Fields you leave out stay as they are.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Person
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
