import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.export_people_csv_keyword_kinds_item import (
    ExportPeopleCsvKeywordKindsItem,
)
from ...models.export_people_csv_never_keyword_kinds_item import (
    ExportPeopleCsvNeverKeywordKindsItem,
)
from ...models.export_people_csv_not_platforms_item import (
    ExportPeopleCsvNotPlatformsItem,
)
from ...models.export_people_csv_platform import ExportPeopleCsvPlatform
from ...models.export_people_csv_platforms_item import ExportPeopleCsvPlatformsItem
from ...models.export_people_csv_sort import ExportPeopleCsvSort
from ...models.export_people_csv_stages_item import ExportPeopleCsvStagesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    handle: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    automated: bool | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params["q"] = q

    params["handle"] = handle

    params["tag"] = tag

    params["muted"] = muted

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["segmentId"] = segment_id

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    json_tags: list[str] | None | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    elif isinstance(tags, list):
        json_tags = tags

    else:
        json_tags = tags
    params["tags"] = json_tags

    json_min_followers: int | None | Unset
    if isinstance(min_followers, Unset):
        json_min_followers = UNSET
    else:
        json_min_followers = min_followers
    params["minFollowers"] = json_min_followers

    json_max_followers: int | None | Unset
    if isinstance(max_followers, Unset):
        json_max_followers = UNSET
    else:
        json_max_followers = max_followers
    params["maxFollowers"] = json_max_followers

    params["minMentions"] = min_mentions

    params["minNegative"] = min_negative

    json_intents: list[str] | None | Unset
    if isinstance(intents, Unset):
        json_intents = UNSET
    elif isinstance(intents, list):
        json_intents = intents

    else:
        json_intents = intents
    params["intents"] = json_intents

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    json_not_tags: list[str] | None | Unset
    if isinstance(not_tags, Unset):
        json_not_tags = UNSET
    elif isinstance(not_tags, list):
        json_not_tags = not_tags

    else:
        json_not_tags = not_tags
    params["notTags"] = json_not_tags

    json_not_intents: list[str] | None | Unset
    if isinstance(not_intents, Unset):
        json_not_intents = UNSET
    elif isinstance(not_intents, list):
        json_not_intents = not_intents

    else:
        json_not_intents = not_intents
    params["notIntents"] = json_not_intents

    json_keyword_kinds: list[str] | Unset = UNSET
    if not isinstance(keyword_kinds, Unset):
        json_keyword_kinds = []
        for keyword_kinds_item_data in keyword_kinds:
            keyword_kinds_item = keyword_kinds_item_data.value
            json_keyword_kinds.append(keyword_kinds_item)

    params["keywordKinds"] = json_keyword_kinds

    json_never_keyword_kinds: list[str] | Unset = UNSET
    if not isinstance(never_keyword_kinds, Unset):
        json_never_keyword_kinds = []
        for never_keyword_kinds_item_data in never_keyword_kinds:
            never_keyword_kinds_item = never_keyword_kinds_item_data.value
            json_never_keyword_kinds.append(never_keyword_kinds_item)

    params["neverKeywordKinds"] = json_never_keyword_kinds

    params["newSinceDays"] = new_since_days

    json_link_hosts: list[str] | None | Unset
    if isinstance(link_hosts, Unset):
        json_link_hosts = UNSET
    elif isinstance(link_hosts, list):
        json_link_hosts = link_hosts

    else:
        json_link_hosts = link_hosts
    params["linkHosts"] = json_link_hosts

    json_stages: list[str] | Unset = UNSET
    if not isinstance(stages, Unset):
        json_stages = []
        for stages_item_data in stages:
            stages_item = stages_item_data.value
            json_stages.append(stages_item)

    params["stages"] = json_stages

    params["automated"] = automated

    json_owner_ids: list[str] | None | Unset
    if isinstance(owner_ids, Unset):
        json_owner_ids = UNSET
    elif isinstance(owner_ids, list):
        json_owner_ids = owner_ids

    else:
        json_owner_ids = owner_ids
    params["ownerIds"] = json_owner_ids

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/people/export.csv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
) -> Response[ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    handle: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    automated: bool | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> Response[ErrorResponse | str]:
    """Export people as CSV

     Returns as CSV the people GET /v1/people lists for the same filters, segmentId included. Each row is
    one person with handle, followers, email, website, company, location and tags, then outreach stage,
    owner and last contacted. The file holds at most 5,000 people. Each workspace can export 6 times a
    minute, and a 429 includes Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): Only people with a profile on this platform.
        q (str | Unset): Searches the display name, handle and profile link, ignoring case.
        handle (str | Unset): Looks up a person by one of their accounts, given as a handle (@sam,
            u/sam, sam) or a profile or post link (https://x.com/sam). The match is exact but ignores
            case, and covers merged accounts. Add platform to pick one platform. A link already tells
            which platform it is.
        tag (str | Unset): Keeps people with this tag, matched exactly and by case.
        muted (bool | Unset): true keeps muted people and false people who are not muted. Leave it
            out for everyone.
        since (datetime.datetime | Unset): A time in ISO 8601 or epoch ms. Keeps people first
            matched then or later.
        segment_id (str | Unset): Adds a saved segment's filter to all other filters here. An
            unknown id returns 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): Keeps people who have an account
            on one of these platforms. Repeat the parameter or separate values with commas.
        tags (list[str] | None | Unset): Keeps people with one of these tags. Repeat the parameter
            or separate values with commas.
        min_followers (int | None | Unset): This many followers or more. People with an unknown
            count are left out.
        max_followers (int | None | Unset): Keeps people with this many followers or fewer.
        min_mentions (int | Unset): Minimum number of matched mentions.
        min_negative (int | Unset): Minimum number of negative mentions.
        intents (list[str] | None | Unset): Has a mention tagged with one of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Leaves out people with an
            account on these platforms. Repeat the parameter or separate values with commas.
        not_tags (list[str] | None | Unset): Leaves out people with one of these tags. Repeat the
            parameter or separate values with commas.
        not_intents (list[str] | None | Unset): Leaves out people whose mentions have one of these
            intents. Repeat the parameter or separate values with commas.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Only people with a mention
            of these keyword kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Excludes people
            who mentioned these keyword kinds.
        new_since_days (int | Unset): People first seen in the past this many days.
        link_hosts (list[str] | None | Unset): Keeps people with a mention that links to one of
            these hosts or its subdomains. Repeat the parameter or separate values with commas.
        stages (list[ExportPeopleCsvStagesItem] | Unset): Keeps people at one of these outreach
            stages. Repeat the parameter or separate values with commas.
        automated (bool | Unset): true keeps people whose matched posts are mostly machine-made,
            such as bots. false keeps the others. Leave it out for everyone.
        owner_ids (list[str] | None | Unset): Keeps people owned by one of these members, by user
            id. Use `none` for people without an owner. Repeat the parameter or separate values with
            commas.
        sort (ExportPeopleCsvSort | Unset): mentions puts the most matches first. recent puts the
            most recently seen first. reach puts the most followers first, with unknown counts at the
            end. new puts people seen for the first time most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        platform=platform,
        q=q,
        handle=handle,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        automated=automated,
        owner_ids=owner_ids,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    handle: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    automated: bool | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> ErrorResponse | str | None:
    """Export people as CSV

     Returns as CSV the people GET /v1/people lists for the same filters, segmentId included. Each row is
    one person with handle, followers, email, website, company, location and tags, then outreach stage,
    owner and last contacted. The file holds at most 5,000 people. Each workspace can export 6 times a
    minute, and a 429 includes Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): Only people with a profile on this platform.
        q (str | Unset): Searches the display name, handle and profile link, ignoring case.
        handle (str | Unset): Looks up a person by one of their accounts, given as a handle (@sam,
            u/sam, sam) or a profile or post link (https://x.com/sam). The match is exact but ignores
            case, and covers merged accounts. Add platform to pick one platform. A link already tells
            which platform it is.
        tag (str | Unset): Keeps people with this tag, matched exactly and by case.
        muted (bool | Unset): true keeps muted people and false people who are not muted. Leave it
            out for everyone.
        since (datetime.datetime | Unset): A time in ISO 8601 or epoch ms. Keeps people first
            matched then or later.
        segment_id (str | Unset): Adds a saved segment's filter to all other filters here. An
            unknown id returns 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): Keeps people who have an account
            on one of these platforms. Repeat the parameter or separate values with commas.
        tags (list[str] | None | Unset): Keeps people with one of these tags. Repeat the parameter
            or separate values with commas.
        min_followers (int | None | Unset): This many followers or more. People with an unknown
            count are left out.
        max_followers (int | None | Unset): Keeps people with this many followers or fewer.
        min_mentions (int | Unset): Minimum number of matched mentions.
        min_negative (int | Unset): Minimum number of negative mentions.
        intents (list[str] | None | Unset): Has a mention tagged with one of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Leaves out people with an
            account on these platforms. Repeat the parameter or separate values with commas.
        not_tags (list[str] | None | Unset): Leaves out people with one of these tags. Repeat the
            parameter or separate values with commas.
        not_intents (list[str] | None | Unset): Leaves out people whose mentions have one of these
            intents. Repeat the parameter or separate values with commas.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Only people with a mention
            of these keyword kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Excludes people
            who mentioned these keyword kinds.
        new_since_days (int | Unset): People first seen in the past this many days.
        link_hosts (list[str] | None | Unset): Keeps people with a mention that links to one of
            these hosts or its subdomains. Repeat the parameter or separate values with commas.
        stages (list[ExportPeopleCsvStagesItem] | Unset): Keeps people at one of these outreach
            stages. Repeat the parameter or separate values with commas.
        automated (bool | Unset): true keeps people whose matched posts are mostly machine-made,
            such as bots. false keeps the others. Leave it out for everyone.
        owner_ids (list[str] | None | Unset): Keeps people owned by one of these members, by user
            id. Use `none` for people without an owner. Repeat the parameter or separate values with
            commas.
        sort (ExportPeopleCsvSort | Unset): mentions puts the most matches first. recent puts the
            most recently seen first. reach puts the most followers first, with unknown counts at the
            end. new puts people seen for the first time most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return sync_detailed(
        client=client,
        platform=platform,
        q=q,
        handle=handle,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        automated=automated,
        owner_ids=owner_ids,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    handle: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    automated: bool | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> Response[ErrorResponse | str]:
    """Export people as CSV

     Returns as CSV the people GET /v1/people lists for the same filters, segmentId included. Each row is
    one person with handle, followers, email, website, company, location and tags, then outreach stage,
    owner and last contacted. The file holds at most 5,000 people. Each workspace can export 6 times a
    minute, and a 429 includes Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): Only people with a profile on this platform.
        q (str | Unset): Searches the display name, handle and profile link, ignoring case.
        handle (str | Unset): Looks up a person by one of their accounts, given as a handle (@sam,
            u/sam, sam) or a profile or post link (https://x.com/sam). The match is exact but ignores
            case, and covers merged accounts. Add platform to pick one platform. A link already tells
            which platform it is.
        tag (str | Unset): Keeps people with this tag, matched exactly and by case.
        muted (bool | Unset): true keeps muted people and false people who are not muted. Leave it
            out for everyone.
        since (datetime.datetime | Unset): A time in ISO 8601 or epoch ms. Keeps people first
            matched then or later.
        segment_id (str | Unset): Adds a saved segment's filter to all other filters here. An
            unknown id returns 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): Keeps people who have an account
            on one of these platforms. Repeat the parameter or separate values with commas.
        tags (list[str] | None | Unset): Keeps people with one of these tags. Repeat the parameter
            or separate values with commas.
        min_followers (int | None | Unset): This many followers or more. People with an unknown
            count are left out.
        max_followers (int | None | Unset): Keeps people with this many followers or fewer.
        min_mentions (int | Unset): Minimum number of matched mentions.
        min_negative (int | Unset): Minimum number of negative mentions.
        intents (list[str] | None | Unset): Has a mention tagged with one of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Leaves out people with an
            account on these platforms. Repeat the parameter or separate values with commas.
        not_tags (list[str] | None | Unset): Leaves out people with one of these tags. Repeat the
            parameter or separate values with commas.
        not_intents (list[str] | None | Unset): Leaves out people whose mentions have one of these
            intents. Repeat the parameter or separate values with commas.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Only people with a mention
            of these keyword kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Excludes people
            who mentioned these keyword kinds.
        new_since_days (int | Unset): People first seen in the past this many days.
        link_hosts (list[str] | None | Unset): Keeps people with a mention that links to one of
            these hosts or its subdomains. Repeat the parameter or separate values with commas.
        stages (list[ExportPeopleCsvStagesItem] | Unset): Keeps people at one of these outreach
            stages. Repeat the parameter or separate values with commas.
        automated (bool | Unset): true keeps people whose matched posts are mostly machine-made,
            such as bots. false keeps the others. Leave it out for everyone.
        owner_ids (list[str] | None | Unset): Keeps people owned by one of these members, by user
            id. Use `none` for people without an owner. Repeat the parameter or separate values with
            commas.
        sort (ExportPeopleCsvSort | Unset): mentions puts the most matches first. recent puts the
            most recently seen first. reach puts the most followers first, with unknown counts at the
            end. new puts people seen for the first time most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        platform=platform,
        q=q,
        handle=handle,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        automated=automated,
        owner_ids=owner_ids,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    handle: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    automated: bool | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> ErrorResponse | str | None:
    """Export people as CSV

     Returns as CSV the people GET /v1/people lists for the same filters, segmentId included. Each row is
    one person with handle, followers, email, website, company, location and tags, then outreach stage,
    owner and last contacted. The file holds at most 5,000 people. Each workspace can export 6 times a
    minute, and a 429 includes Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): Only people with a profile on this platform.
        q (str | Unset): Searches the display name, handle and profile link, ignoring case.
        handle (str | Unset): Looks up a person by one of their accounts, given as a handle (@sam,
            u/sam, sam) or a profile or post link (https://x.com/sam). The match is exact but ignores
            case, and covers merged accounts. Add platform to pick one platform. A link already tells
            which platform it is.
        tag (str | Unset): Keeps people with this tag, matched exactly and by case.
        muted (bool | Unset): true keeps muted people and false people who are not muted. Leave it
            out for everyone.
        since (datetime.datetime | Unset): A time in ISO 8601 or epoch ms. Keeps people first
            matched then or later.
        segment_id (str | Unset): Adds a saved segment's filter to all other filters here. An
            unknown id returns 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): Keeps people who have an account
            on one of these platforms. Repeat the parameter or separate values with commas.
        tags (list[str] | None | Unset): Keeps people with one of these tags. Repeat the parameter
            or separate values with commas.
        min_followers (int | None | Unset): This many followers or more. People with an unknown
            count are left out.
        max_followers (int | None | Unset): Keeps people with this many followers or fewer.
        min_mentions (int | Unset): Minimum number of matched mentions.
        min_negative (int | Unset): Minimum number of negative mentions.
        intents (list[str] | None | Unset): Has a mention tagged with one of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Leaves out people with an
            account on these platforms. Repeat the parameter or separate values with commas.
        not_tags (list[str] | None | Unset): Leaves out people with one of these tags. Repeat the
            parameter or separate values with commas.
        not_intents (list[str] | None | Unset): Leaves out people whose mentions have one of these
            intents. Repeat the parameter or separate values with commas.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Only people with a mention
            of these keyword kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Excludes people
            who mentioned these keyword kinds.
        new_since_days (int | Unset): People first seen in the past this many days.
        link_hosts (list[str] | None | Unset): Keeps people with a mention that links to one of
            these hosts or its subdomains. Repeat the parameter or separate values with commas.
        stages (list[ExportPeopleCsvStagesItem] | Unset): Keeps people at one of these outreach
            stages. Repeat the parameter or separate values with commas.
        automated (bool | Unset): true keeps people whose matched posts are mostly machine-made,
            such as bots. false keeps the others. Leave it out for everyone.
        owner_ids (list[str] | None | Unset): Keeps people owned by one of these members, by user
            id. Use `none` for people without an owner. Repeat the parameter or separate values with
            commas.
        sort (ExportPeopleCsvSort | Unset): mentions puts the most matches first. recent puts the
            most recently seen first. reach puts the most followers first, with unknown counts at the
            end. new puts people seen for the first time most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            q=q,
            handle=handle,
            tag=tag,
            muted=muted,
            since=since,
            segment_id=segment_id,
            platforms=platforms,
            tags=tags,
            min_followers=min_followers,
            max_followers=max_followers,
            min_mentions=min_mentions,
            min_negative=min_negative,
            intents=intents,
            not_platforms=not_platforms,
            not_tags=not_tags,
            not_intents=not_intents,
            keyword_kinds=keyword_kinds,
            never_keyword_kinds=never_keyword_kinds,
            new_since_days=new_since_days,
            link_hosts=link_hosts,
            stages=stages,
            automated=automated,
            owner_ids=owner_ids,
            sort=sort,
        )
    ).parsed
