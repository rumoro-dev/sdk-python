from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_share_of_voice_platforms_item import GetShareOfVoicePlatformsItem
from ...models.get_share_of_voice_range import GetShareOfVoiceRange
from ...models.share_of_voice import ShareOfVoice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    range_: GetShareOfVoiceRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetShareOfVoicePlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["from"] = from_

    params["to"] = to

    json_keyword_ids: list[str] | None | Unset
    if isinstance(keyword_ids, Unset):
        json_keyword_ids = UNSET
    elif isinstance(keyword_ids, list):
        json_keyword_ids = keyword_ids

    else:
        json_keyword_ids = keyword_ids
    params["keywordIds"] = json_keyword_ids

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    params["compare"] = compare

    params["timezone"] = timezone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/share-of-voice",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ShareOfVoice | None:
    if response.status_code == 200:
        response_200 = ShareOfVoice.from_dict(response.json())

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
) -> Response[ErrorResponse | ShareOfVoice]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetShareOfVoiceRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetShareOfVoicePlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Response[ErrorResponse | ShareOfVoice]:
    """Get share of voice

     Returns each keyword with matches in the period, its counts and its share of all brand and
    competitor matches. Topic keywords are counted but not part of the split. Pick the period with
    `range` (7d, 30d, 90d or 365d up to today) or with `from` and `to`. Days follow `timezone`, UTC by
    default. `keywordIds` and `platforms` narrow the data, and `compare=true` adds the equally long
    period just before. Dates are publish dates.

    Args:
        range_ (GetShareOfVoiceRange | Unset): A preset period up to today, 30d by default.
            Ignored when you send from or to.
        from_ (str | Unset): Start date in `timezone`, as YYYY-MM-DD. That day is included.
        to (str | Unset): End date in `timezone`, as YYYY-MM-DD, included. Defaults to today.
        keyword_ids (list[str] | None | Unset): Keeps these keyword ids only. Repeat the parameter
            or separate values with commas. Leave it out for all keywords.
        platforms (list[GetShareOfVoicePlatformsItem] | Unset): Keeps these platforms only. Repeat
            the parameter or separate values with commas. Leave it out for all platforms.
        compare (bool | Unset): true adds the equally long period just before as `previous`.
        timezone (str | Unset): The IANA time zone used to split days, such as America/New_York.
            Defaults to UTC. The zone's offset at the end of the period is used for the whole period.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ShareOfVoice]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    range_: GetShareOfVoiceRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetShareOfVoicePlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> ErrorResponse | ShareOfVoice | None:
    """Get share of voice

     Returns each keyword with matches in the period, its counts and its share of all brand and
    competitor matches. Topic keywords are counted but not part of the split. Pick the period with
    `range` (7d, 30d, 90d or 365d up to today) or with `from` and `to`. Days follow `timezone`, UTC by
    default. `keywordIds` and `platforms` narrow the data, and `compare=true` adds the equally long
    period just before. Dates are publish dates.

    Args:
        range_ (GetShareOfVoiceRange | Unset): A preset period up to today, 30d by default.
            Ignored when you send from or to.
        from_ (str | Unset): Start date in `timezone`, as YYYY-MM-DD. That day is included.
        to (str | Unset): End date in `timezone`, as YYYY-MM-DD, included. Defaults to today.
        keyword_ids (list[str] | None | Unset): Keeps these keyword ids only. Repeat the parameter
            or separate values with commas. Leave it out for all keywords.
        platforms (list[GetShareOfVoicePlatformsItem] | Unset): Keeps these platforms only. Repeat
            the parameter or separate values with commas. Leave it out for all platforms.
        compare (bool | Unset): true adds the equally long period just before as `previous`.
        timezone (str | Unset): The IANA time zone used to split days, such as America/New_York.
            Defaults to UTC. The zone's offset at the end of the period is used for the whole period.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ShareOfVoice
    """

    return sync_detailed(
        client=client,
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    range_: GetShareOfVoiceRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetShareOfVoicePlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> Response[ErrorResponse | ShareOfVoice]:
    """Get share of voice

     Returns each keyword with matches in the period, its counts and its share of all brand and
    competitor matches. Topic keywords are counted but not part of the split. Pick the period with
    `range` (7d, 30d, 90d or 365d up to today) or with `from` and `to`. Days follow `timezone`, UTC by
    default. `keywordIds` and `platforms` narrow the data, and `compare=true` adds the equally long
    period just before. Dates are publish dates.

    Args:
        range_ (GetShareOfVoiceRange | Unset): A preset period up to today, 30d by default.
            Ignored when you send from or to.
        from_ (str | Unset): Start date in `timezone`, as YYYY-MM-DD. That day is included.
        to (str | Unset): End date in `timezone`, as YYYY-MM-DD, included. Defaults to today.
        keyword_ids (list[str] | None | Unset): Keeps these keyword ids only. Repeat the parameter
            or separate values with commas. Leave it out for all keywords.
        platforms (list[GetShareOfVoicePlatformsItem] | Unset): Keeps these platforms only. Repeat
            the parameter or separate values with commas. Leave it out for all platforms.
        compare (bool | Unset): true adds the equally long period just before as `previous`.
        timezone (str | Unset): The IANA time zone used to split days, such as America/New_York.
            Defaults to UTC. The zone's offset at the end of the period is used for the whole period.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ShareOfVoice]
    """

    kwargs = _get_kwargs(
        range_=range_,
        from_=from_,
        to=to,
        keyword_ids=keyword_ids,
        platforms=platforms,
        compare=compare,
        timezone=timezone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    range_: GetShareOfVoiceRange | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    platforms: list[GetShareOfVoicePlatformsItem] | Unset = UNSET,
    compare: bool | Unset = UNSET,
    timezone: str | Unset = UNSET,
) -> ErrorResponse | ShareOfVoice | None:
    """Get share of voice

     Returns each keyword with matches in the period, its counts and its share of all brand and
    competitor matches. Topic keywords are counted but not part of the split. Pick the period with
    `range` (7d, 30d, 90d or 365d up to today) or with `from` and `to`. Days follow `timezone`, UTC by
    default. `keywordIds` and `platforms` narrow the data, and `compare=true` adds the equally long
    period just before. Dates are publish dates.

    Args:
        range_ (GetShareOfVoiceRange | Unset): A preset period up to today, 30d by default.
            Ignored when you send from or to.
        from_ (str | Unset): Start date in `timezone`, as YYYY-MM-DD. That day is included.
        to (str | Unset): End date in `timezone`, as YYYY-MM-DD, included. Defaults to today.
        keyword_ids (list[str] | None | Unset): Keeps these keyword ids only. Repeat the parameter
            or separate values with commas. Leave it out for all keywords.
        platforms (list[GetShareOfVoicePlatformsItem] | Unset): Keeps these platforms only. Repeat
            the parameter or separate values with commas. Leave it out for all platforms.
        compare (bool | Unset): true adds the equally long period just before as `previous`.
        timezone (str | Unset): The IANA time zone used to split days, such as America/New_York.
            Defaults to UTC. The zone's offset at the end of the period is used for the whole period.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ShareOfVoice
    """

    return (
        await asyncio_detailed(
            client=client,
            range_=range_,
            from_=from_,
            to=to,
            keyword_ids=keyword_ids,
            platforms=platforms,
            compare=compare,
            timezone=timezone,
        )
    ).parsed
