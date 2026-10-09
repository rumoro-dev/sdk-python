from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_keywords_kind_item import ListKeywordsKindItem
from ...models.list_keywords_platform_item import ListKeywordsPlatformItem
from ...models.list_keywords_response_200 import ListKeywordsResponse200
from ...models.list_keywords_sort import ListKeywordsSort
from ...models.list_keywords_status_item import ListKeywordsStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    json_group_id: list[str] | None | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    elif isinstance(group_id, list):
        json_group_id = group_id

    else:
        json_group_id = group_id
    params["groupId"] = json_group_id

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item = kind_item_data.value
            json_kind.append(kind_item)

    params["kind"] = json_kind

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_platform: list[str] | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = []
        for platform_item_data in platform:
            platform_item = platform_item_data.value
            json_platform.append(platform_item)

    params["platform"] = json_platform

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

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
        "url": "/v1/keywords",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ListKeywordsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListKeywordsResponse200.from_dict(response.json())

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
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     Returns the workspace's keywords with their match counts and polling status. With no parameters you
    get all keywords, latest first. `q` searches the term and context. `kind`, `status` and `platform`
    filter the list, `sort` orders it, and `limit` and `offset` page through it. `total` is the number
    of matching keywords before paging.

    Args:
        q (str | Unset): Case-insensitive search in the term and context.
        group_id (list[str] | None | Unset): Keeps keywords in these groups only (grp_...). Repeat
            the parameter or separate values with commas.
        kind (list[ListKeywordsKindItem] | Unset): Keeps keywords of these kinds only (brand,
            competitor, topic). Repeat the parameter or separate values with commas.
        status (list[ListKeywordsStatusItem] | Unset): Keeps keywords in these states only
            (active, muted, paused, capped). Repeat the parameter or separate values with commas.
        platform (list[ListKeywordsPlatformItem] | Unset): Keeps keywords that run on one of these
            platforms. That means the term is searched there, which is every platform when platforms
            is null. For appstore and googleplay it means an app from that store is in reviewSources.
            Repeat the parameter or separate values with commas.
        sort (ListKeywordsSort | Unset): newest puts the latest created first and oldest the
            earliest. term sorts A to Z. mentions puts the most matches first and relevant the most
            relevant matches. recent puts the most matches of the past 7 days first. lastMention puts
            the latest matched post first, with keywords that have none at the end. Default:
            ListKeywordsSort.NEWEST.
        limit (int | Unset): How many to return, from 1 to 500. Leave it out to get all keywords
            after `offset`.
        offset (int | None | Unset): How many keywords to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListKeywordsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
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
    q: str | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     Returns the workspace's keywords with their match counts and polling status. With no parameters you
    get all keywords, latest first. `q` searches the term and context. `kind`, `status` and `platform`
    filter the list, `sort` orders it, and `limit` and `offset` page through it. `total` is the number
    of matching keywords before paging.

    Args:
        q (str | Unset): Case-insensitive search in the term and context.
        group_id (list[str] | None | Unset): Keeps keywords in these groups only (grp_...). Repeat
            the parameter or separate values with commas.
        kind (list[ListKeywordsKindItem] | Unset): Keeps keywords of these kinds only (brand,
            competitor, topic). Repeat the parameter or separate values with commas.
        status (list[ListKeywordsStatusItem] | Unset): Keeps keywords in these states only
            (active, muted, paused, capped). Repeat the parameter or separate values with commas.
        platform (list[ListKeywordsPlatformItem] | Unset): Keeps keywords that run on one of these
            platforms. That means the term is searched there, which is every platform when platforms
            is null. For appstore and googleplay it means an app from that store is in reviewSources.
            Repeat the parameter or separate values with commas.
        sort (ListKeywordsSort | Unset): newest puts the latest created first and oldest the
            earliest. term sorts A to Z. mentions puts the most matches first and relevant the most
            relevant matches. recent puts the most matches of the past 7 days first. lastMention puts
            the latest matched post first, with keywords that have none at the end. Default:
            ListKeywordsSort.NEWEST.
        limit (int | Unset): How many to return, from 1 to 500. Leave it out to get all keywords
            after `offset`.
        offset (int | None | Unset): How many keywords to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListKeywordsResponse200
    """

    return sync_detailed(
        client=client,
        q=q,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> Response[ErrorResponse | ListKeywordsResponse200]:
    """List keywords

     Returns the workspace's keywords with their match counts and polling status. With no parameters you
    get all keywords, latest first. `q` searches the term and context. `kind`, `status` and `platform`
    filter the list, `sort` orders it, and `limit` and `offset` page through it. `total` is the number
    of matching keywords before paging.

    Args:
        q (str | Unset): Case-insensitive search in the term and context.
        group_id (list[str] | None | Unset): Keeps keywords in these groups only (grp_...). Repeat
            the parameter or separate values with commas.
        kind (list[ListKeywordsKindItem] | Unset): Keeps keywords of these kinds only (brand,
            competitor, topic). Repeat the parameter or separate values with commas.
        status (list[ListKeywordsStatusItem] | Unset): Keeps keywords in these states only
            (active, muted, paused, capped). Repeat the parameter or separate values with commas.
        platform (list[ListKeywordsPlatformItem] | Unset): Keeps keywords that run on one of these
            platforms. That means the term is searched there, which is every platform when platforms
            is null. For appstore and googleplay it means an app from that store is in reviewSources.
            Repeat the parameter or separate values with commas.
        sort (ListKeywordsSort | Unset): newest puts the latest created first and oldest the
            earliest. term sorts A to Z. mentions puts the most matches first and relevant the most
            relevant matches. recent puts the most matches of the past 7 days first. lastMention puts
            the latest matched post first, with keywords that have none at the end. Default:
            ListKeywordsSort.NEWEST.
        limit (int | Unset): How many to return, from 1 to 500. Leave it out to get all keywords
            after `offset`.
        offset (int | None | Unset): How many keywords to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListKeywordsResponse200]
    """

    kwargs = _get_kwargs(
        q=q,
        group_id=group_id,
        kind=kind,
        status=status,
        platform=platform,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    group_id: list[str] | None | Unset = UNSET,
    kind: list[ListKeywordsKindItem] | Unset = UNSET,
    status: list[ListKeywordsStatusItem] | Unset = UNSET,
    platform: list[ListKeywordsPlatformItem] | Unset = UNSET,
    sort: ListKeywordsSort | Unset = ListKeywordsSort.NEWEST,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = 0,
) -> ErrorResponse | ListKeywordsResponse200 | None:
    """List keywords

     Returns the workspace's keywords with their match counts and polling status. With no parameters you
    get all keywords, latest first. `q` searches the term and context. `kind`, `status` and `platform`
    filter the list, `sort` orders it, and `limit` and `offset` page through it. `total` is the number
    of matching keywords before paging.

    Args:
        q (str | Unset): Case-insensitive search in the term and context.
        group_id (list[str] | None | Unset): Keeps keywords in these groups only (grp_...). Repeat
            the parameter or separate values with commas.
        kind (list[ListKeywordsKindItem] | Unset): Keeps keywords of these kinds only (brand,
            competitor, topic). Repeat the parameter or separate values with commas.
        status (list[ListKeywordsStatusItem] | Unset): Keeps keywords in these states only
            (active, muted, paused, capped). Repeat the parameter or separate values with commas.
        platform (list[ListKeywordsPlatformItem] | Unset): Keeps keywords that run on one of these
            platforms. That means the term is searched there, which is every platform when platforms
            is null. For appstore and googleplay it means an app from that store is in reviewSources.
            Repeat the parameter or separate values with commas.
        sort (ListKeywordsSort | Unset): newest puts the latest created first and oldest the
            earliest. term sorts A to Z. mentions puts the most matches first and relevant the most
            relevant matches. recent puts the most matches of the past 7 days first. lastMention puts
            the latest matched post first, with keywords that have none at the end. Default:
            ListKeywordsSort.NEWEST.
        limit (int | Unset): How many to return, from 1 to 500. Leave it out to get all keywords
            after `offset`.
        offset (int | None | Unset): How many keywords to skip. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListKeywordsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            group_id=group_id,
            kind=kind,
            status=status,
            platform=platform,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
