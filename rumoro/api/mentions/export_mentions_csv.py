import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.export_mentions_csv_keyword_kinds_item import (
    ExportMentionsCsvKeywordKindsItem,
)
from ...models.export_mentions_csv_not_platforms_item import (
    ExportMentionsCsvNotPlatformsItem,
)
from ...models.export_mentions_csv_not_sentiments_item import (
    ExportMentionsCsvNotSentimentsItem,
)
from ...models.export_mentions_csv_platform import ExportMentionsCsvPlatform
from ...models.export_mentions_csv_platforms_item import ExportMentionsCsvPlatformsItem
from ...models.export_mentions_csv_sentiment import ExportMentionsCsvSentiment
from ...models.export_mentions_csv_sentiments_item import (
    ExportMentionsCsvSentimentsItem,
)
from ...models.export_mentions_csv_status import ExportMentionsCsvStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keyword_id: str | Unset = UNSET,
    platform: ExportMentionsCsvPlatform | Unset = UNSET,
    status: ExportMentionsCsvStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: ExportMentionsCsvSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    keyword_kinds: list[ExportMentionsCsvKeywordKindsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[ExportMentionsCsvPlatformsItem] | Unset = UNSET,
    not_platforms: list[ExportMentionsCsvNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[ExportMentionsCsvSentimentsItem] | Unset = UNSET,
    not_sentiments: list[ExportMentionsCsvNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    ratings: list[int] | Unset = UNSET,
    not_ratings: list[int] | Unset = UNSET,
    min_likes: int | None | Unset = UNSET,
    min_reposts: int | None | Unset = UNSET,
    min_replies: int | None | Unset = UNSET,
    min_quotes: int | None | Unset = UNSET,
    min_views: int | None | Unset = UNSET,
    min_bookmarks: int | None | Unset = UNSET,
    any_of: str | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keywordId"] = keyword_id

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["relevant"] = relevant

    json_sentiment: str | Unset = UNSET
    if not isinstance(sentiment, Unset):
        json_sentiment = sentiment.value

    params["sentiment"] = json_sentiment

    params["intent"] = intent

    params["automated"] = automated

    params["personId"] = person_id

    params["includeMuted"] = include_muted

    params["assigneeId"] = assignee_id

    params["snoozed"] = snoozed

    json_exclude_authors: list[str] | None | Unset
    if isinstance(exclude_authors, Unset):
        json_exclude_authors = UNSET
    elif isinstance(exclude_authors, list):
        json_exclude_authors = exclude_authors

    else:
        json_exclude_authors = exclude_authors
    params["excludeAuthors"] = json_exclude_authors

    json_min_relevance: int | None | Unset
    if isinstance(min_relevance, Unset):
        json_min_relevance = UNSET
    else:
        json_min_relevance = min_relevance
    params["minRelevance"] = json_min_relevance

    json_min_confidence: float | None | Unset
    if isinstance(min_confidence, Unset):
        json_min_confidence = UNSET
    else:
        json_min_confidence = min_confidence
    params["minConfidence"] = json_min_confidence

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

    params["isReply"] = is_reply

    params["alertId"] = alert_id

    params["viewId"] = view_id

    json_keyword_kinds: list[str] | Unset = UNSET
    if not isinstance(keyword_kinds, Unset):
        json_keyword_kinds = []
        for keyword_kinds_item_data in keyword_kinds:
            keyword_kinds_item = keyword_kinds_item_data.value
            json_keyword_kinds.append(keyword_kinds_item)

    params["keywordKinds"] = json_keyword_kinds

    json_tags: list[str] | None | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    elif isinstance(tags, list):
        json_tags = tags

    else:
        json_tags = tags
    params["tags"] = json_tags

    json_link_hosts: list[str] | None | Unset
    if isinstance(link_hosts, Unset):
        json_link_hosts = UNSET
    elif isinstance(link_hosts, list):
        json_link_hosts = link_hosts

    else:
        json_link_hosts = link_hosts
    params["linkHosts"] = json_link_hosts

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    json_keyword_ids: list[str] | None | Unset
    if isinstance(keyword_ids, Unset):
        json_keyword_ids = UNSET
    elif isinstance(keyword_ids, list):
        json_keyword_ids = keyword_ids

    else:
        json_keyword_ids = keyword_ids
    params["keywordIds"] = json_keyword_ids

    json_group_ids: list[str] | None | Unset
    if isinstance(group_ids, Unset):
        json_group_ids = UNSET
    elif isinstance(group_ids, list):
        json_group_ids = group_ids

    else:
        json_group_ids = group_ids
    params["groupIds"] = json_group_ids

    json_not_group_ids: list[str] | None | Unset
    if isinstance(not_group_ids, Unset):
        json_not_group_ids = UNSET
    elif isinstance(not_group_ids, list):
        json_not_group_ids = not_group_ids

    else:
        json_not_group_ids = not_group_ids
    params["notGroupIds"] = json_not_group_ids

    json_not_keyword_ids: list[str] | None | Unset
    if isinstance(not_keyword_ids, Unset):
        json_not_keyword_ids = UNSET
    elif isinstance(not_keyword_ids, list):
        json_not_keyword_ids = not_keyword_ids

    else:
        json_not_keyword_ids = not_keyword_ids
    params["notKeywordIds"] = json_not_keyword_ids

    json_sentiments: list[str] | Unset = UNSET
    if not isinstance(sentiments, Unset):
        json_sentiments = []
        for sentiments_item_data in sentiments:
            sentiments_item = sentiments_item_data.value
            json_sentiments.append(sentiments_item)

    params["sentiments"] = json_sentiments

    json_not_sentiments: list[str] | Unset = UNSET
    if not isinstance(not_sentiments, Unset):
        json_not_sentiments = []
        for not_sentiments_item_data in not_sentiments:
            not_sentiments_item = not_sentiments_item_data.value
            json_not_sentiments.append(not_sentiments_item)

    params["notSentiments"] = json_not_sentiments

    json_intents: list[str] | None | Unset
    if isinstance(intents, Unset):
        json_intents = UNSET
    elif isinstance(intents, list):
        json_intents = intents

    else:
        json_intents = intents
    params["intents"] = json_intents

    json_not_intents: list[str] | None | Unset
    if isinstance(not_intents, Unset):
        json_not_intents = UNSET
    elif isinstance(not_intents, list):
        json_not_intents = not_intents

    else:
        json_not_intents = not_intents
    params["notIntents"] = json_not_intents

    json_not_link_hosts: list[str] | None | Unset
    if isinstance(not_link_hosts, Unset):
        json_not_link_hosts = UNSET
    elif isinstance(not_link_hosts, list):
        json_not_link_hosts = not_link_hosts

    else:
        json_not_link_hosts = not_link_hosts
    params["notLinkHosts"] = json_not_link_hosts

    json_not_tags: list[str] | None | Unset
    if isinstance(not_tags, Unset):
        json_not_tags = UNSET
    elif isinstance(not_tags, list):
        json_not_tags = not_tags

    else:
        json_not_tags = not_tags
    params["notTags"] = json_not_tags

    json_languages: list[str] | Unset = UNSET
    if not isinstance(languages, Unset):
        json_languages = languages

    params["languages"] = json_languages

    json_not_languages: list[str] | Unset = UNSET
    if not isinstance(not_languages, Unset):
        json_not_languages = not_languages

    params["notLanguages"] = json_not_languages

    json_ratings: list[int] | Unset = UNSET
    if not isinstance(ratings, Unset):
        json_ratings = ratings

    params["ratings"] = json_ratings

    json_not_ratings: list[int] | Unset = UNSET
    if not isinstance(not_ratings, Unset):
        json_not_ratings = not_ratings

    params["notRatings"] = json_not_ratings

    json_min_likes: int | None | Unset
    if isinstance(min_likes, Unset):
        json_min_likes = UNSET
    else:
        json_min_likes = min_likes
    params["minLikes"] = json_min_likes

    json_min_reposts: int | None | Unset
    if isinstance(min_reposts, Unset):
        json_min_reposts = UNSET
    else:
        json_min_reposts = min_reposts
    params["minReposts"] = json_min_reposts

    json_min_replies: int | None | Unset
    if isinstance(min_replies, Unset):
        json_min_replies = UNSET
    else:
        json_min_replies = min_replies
    params["minReplies"] = json_min_replies

    json_min_quotes: int | None | Unset
    if isinstance(min_quotes, Unset):
        json_min_quotes = UNSET
    else:
        json_min_quotes = min_quotes
    params["minQuotes"] = json_min_quotes

    json_min_views: int | None | Unset
    if isinstance(min_views, Unset):
        json_min_views = UNSET
    else:
        json_min_views = min_views
    params["minViews"] = json_min_views

    json_min_bookmarks: int | None | Unset
    if isinstance(min_bookmarks, Unset):
        json_min_bookmarks = UNSET
    else:
        json_min_bookmarks = min_bookmarks
    params["minBookmarks"] = json_min_bookmarks

    params["anyOf"] = any_of

    params["q"] = q

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mentions/export.csv",
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
    keyword_id: str | Unset = UNSET,
    platform: ExportMentionsCsvPlatform | Unset = UNSET,
    status: ExportMentionsCsvStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: ExportMentionsCsvSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    keyword_kinds: list[ExportMentionsCsvKeywordKindsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[ExportMentionsCsvPlatformsItem] | Unset = UNSET,
    not_platforms: list[ExportMentionsCsvNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[ExportMentionsCsvSentimentsItem] | Unset = UNSET,
    not_sentiments: list[ExportMentionsCsvNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    ratings: list[int] | Unset = UNSET,
    not_ratings: list[int] | Unset = UNSET,
    min_likes: int | None | Unset = UNSET,
    min_reposts: int | None | Unset = UNSET,
    min_replies: int | None | Unset = UNSET,
    min_quotes: int | None | Unset = UNSET,
    min_views: int | None | Unset = UNSET,
    min_bookmarks: int | None | Unset = UNSET,
    any_of: str | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Export mentions as CSV

     Returns as CSV the mentions GET /v1/mentions lists for the same filters. Rows are ordered by match
    time, latest first, which is the order they reached your feed and can differ from the post date. The
    columns are id, published_at, platform, keyword, author, author_url, author_followers, relevance,
    sentiment, intents (separated by |), language, confidence, status, relevant, delivered, url, links
    (separated by |), text (the first 1,000 characters), group, group_external_id, rating and app_id
    (reviews only), and title and image_url (on platforms that have them). The file holds at most 10,000
    rows, and the X-Mentions-Truncated header tells you when rows were cut. Each workspace can export 6
    times a minute, and a 429 includes Retry-After.

    Args:
        keyword_id (str | Unset): Only this keyword's matches.
        platform (ExportMentionsCsvPlatform | Unset): Only this platform's posts.
        status (ExportMentionsCsvStatus | Unset): Keeps mentions with this status only. Leave it
            out for all statuses.
        relevant (bool | Unset): true keeps mentions the classifier scored relevant. false keeps
            the others, including unscored ones.
        sentiment (ExportMentionsCsvSentiment | Unset): Keeps mentions with this sentiment only.
        intent (str | Unset): Returns only mentions with this tag. One of bug_report, buy_intent,
            churn_intent, comparison, complaint, event, feedback, hiring, industry_insight, launch,
            praise, pricing, promotional, question and testimonial.
        automated (bool | Unset): true keeps mentions that look machine-made, such as bot
            accounts, scheduled or template posts and AI-written text. false keeps the others,
            including mentions scored before this flag existed. Leave it out for all.
        person_id (str | Unset): Keeps mentions by this person (an id from /v1/people), including
            merged accounts. Turns on includeMuted.
        include_muted (bool | Unset): true also returns mentions by muted people, which are hidden
            by default.
        assignee_id (str | Unset): Member user id. Returns only mentions assigned to them.
        snoozed (bool | Unset): true shows only snoozed mentions, which are otherwise hidden until
            they wake.
        exclude_authors (list[str] | None | Unset): Leaves out these authors, given as display
            names, handles or profile links. Repeat the parameter or send one value with commas.
        min_relevance (int | None | Unset): Keeps mentions with this relevance score or higher.
            Unscored mentions are left out.
        min_confidence (float | None | Unset): Minimum classifier confidence, 0 to 1. Mentions
            with no confidence are dropped.
        min_followers (int | None | Unset): Sends only posts by authors with this many followers
            or more. Unknown counts are left out.
        max_followers (int | None | Unset): Keeps posts by authors with this many followers or
            fewer. Unknown counts are left out.
        is_reply (bool | Unset): true keeps replies and comments, meaning posts that answer
            another post. false keeps posts that are not replies. Leave it out for both.
        alert_id (str | Unset): Adds an alert rule's filter (an id from GET /v1/alerts) to the
            other filters. You get the mentions the rule would send, useful for a preview or an export
            in feed form. An unknown id returns 404.
        view_id (str | Unset): Adds a saved view's filter (an id from GET /v1/views) to the other
            filters, with every condition joined by AND. You get exactly what the view shows. An
            unknown id returns 404.
        keyword_kinds (list[ExportMentionsCsvKeywordKindsItem] | Unset): Keeps matches of keywords
            of these kinds only (brand, competitor, topic). Repeat the parameter or separate values
            with commas.
        tags (list[str] | None | Unset): Keeps authors your workspace gave one of these tags,
            matched exactly and by case. Repeat the parameter or separate values with commas.
        link_hosts (list[str] | None | Unset): Keeps posts that link to one of these hosts or its
            subdomains, so slack.com also matches api.slack.com. Repeat the parameter or separate
            values with commas.
        platforms (list[ExportMentionsCsvPlatformsItem] | Unset): Keeps posts from these platforms
            only.
        not_platforms (list[ExportMentionsCsvNotPlatformsItem] | Unset): Platforms to exclude.
        keyword_ids (list[str] | None | Unset): Keeps matches of these keywords only.
        group_ids (list[str] | None | Unset): Keeps matches of keywords in these groups only
            (grp_...). Repeat the parameter or separate values with commas.
        not_group_ids (list[str] | None | Unset): Hides matches from keywords that belong to these
            groups.
        not_keyword_ids (list[str] | None | Unset): Keyword ids to exclude.
        sentiments (list[ExportMentionsCsvSentimentsItem] | Unset): Keeps mentions with these
            sentiments only.
        not_sentiments (list[ExportMentionsCsvNotSentimentsItem] | Unset): Leaves out these
            sentiments. Mentions not scored yet are kept.
        intents (list[str] | None | Unset): Keeps mentions tagged with one of these intents or
            topics.
        not_intents (list[str] | None | Unset): Intent or topic tags to exclude.
        not_link_hosts (list[str] | None | Unset): Leaves out posts that link to these hosts or
            their subdomains.
        not_tags (list[str] | None | Unset): Leaves out authors your workspace gave one of these
            tags.
        languages (list[str] | Unset): Sends only posts in these languages, as ISO 639-1 codes
            such as en, es or de. Posts with an unknown language are left out.
        not_languages (list[str] | Unset): Leaves out posts in these languages. Posts with an
            unknown language are kept.
        ratings (list[int] | Unset): Keeps reviews with one of these star ratings, from 1 to 5.
            Use ratings=1,2 for the unhappy ones. Posts that are not reviews are left out.
        not_ratings (list[int] | Unset): Star ratings (1 to 5) to hide, such as notRatings=5.
            Other posts are unaffected.
        min_likes (int | None | Unset): Keeps posts with this many likes (upvotes, reactions) or
            more, counted when the post was collected. Posts without a like count are left out.
        min_reposts (int | None | Unset): Keeps posts with this many reposts (shares, retweets) or
            more, counted when the post was collected. Posts without a repost count are left out.
        min_replies (int | None | Unset): Keeps posts with this many replies (comments) or more,
            counted when the post was collected. Posts without a reply count are left out.
        min_quotes (int | None | Unset): Keeps posts with this many quotes or more, counted when
            the post was collected. Posts without a quote count are left out.
        min_views (int | None | Unset): Keeps posts with this many views (plays) or more, counted
            when the post was collected. Posts without a view count are left out.
        min_bookmarks (int | None | Unset): Keeps posts with this many bookmarks (saves) or more,
            counted when the post was collected. Posts without a bookmark count are left out.
        any_of (str | Unset): Groups of conditions joined by OR, as URL-encoded JSON. For example
            [{"platforms":["github"],"intents":["bug_report"]},{"sentiments":["negative"]}] means "bug
            reports on GitHub, or anything negative". A group uses the fields of a view filter, where
            a list matches any value, a not list matches none, and all conditions are joined by AND. A
            mention passes when one group matches, and the other filters here still apply. Send 1 to
            10 groups, none empty and none nested.
        q (str | Unset): Searches post text and author names.
        since (datetime.datetime | Unset): Keeps posts published at this time or later, as ISO
            8601 or epoch ms.
        until (datetime.datetime | Unset): Keeps posts published at this time or earlier, as ISO
            8601 or epoch ms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        view_id=view_id,
        keyword_kinds=keyword_kinds,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        ratings=ratings,
        not_ratings=not_ratings,
        min_likes=min_likes,
        min_reposts=min_reposts,
        min_replies=min_replies,
        min_quotes=min_quotes,
        min_views=min_views,
        min_bookmarks=min_bookmarks,
        any_of=any_of,
        q=q,
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: ExportMentionsCsvPlatform | Unset = UNSET,
    status: ExportMentionsCsvStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: ExportMentionsCsvSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    keyword_kinds: list[ExportMentionsCsvKeywordKindsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[ExportMentionsCsvPlatformsItem] | Unset = UNSET,
    not_platforms: list[ExportMentionsCsvNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[ExportMentionsCsvSentimentsItem] | Unset = UNSET,
    not_sentiments: list[ExportMentionsCsvNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    ratings: list[int] | Unset = UNSET,
    not_ratings: list[int] | Unset = UNSET,
    min_likes: int | None | Unset = UNSET,
    min_reposts: int | None | Unset = UNSET,
    min_replies: int | None | Unset = UNSET,
    min_quotes: int | None | Unset = UNSET,
    min_views: int | None | Unset = UNSET,
    min_bookmarks: int | None | Unset = UNSET,
    any_of: str | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Export mentions as CSV

     Returns as CSV the mentions GET /v1/mentions lists for the same filters. Rows are ordered by match
    time, latest first, which is the order they reached your feed and can differ from the post date. The
    columns are id, published_at, platform, keyword, author, author_url, author_followers, relevance,
    sentiment, intents (separated by |), language, confidence, status, relevant, delivered, url, links
    (separated by |), text (the first 1,000 characters), group, group_external_id, rating and app_id
    (reviews only), and title and image_url (on platforms that have them). The file holds at most 10,000
    rows, and the X-Mentions-Truncated header tells you when rows were cut. Each workspace can export 6
    times a minute, and a 429 includes Retry-After.

    Args:
        keyword_id (str | Unset): Only this keyword's matches.
        platform (ExportMentionsCsvPlatform | Unset): Only this platform's posts.
        status (ExportMentionsCsvStatus | Unset): Keeps mentions with this status only. Leave it
            out for all statuses.
        relevant (bool | Unset): true keeps mentions the classifier scored relevant. false keeps
            the others, including unscored ones.
        sentiment (ExportMentionsCsvSentiment | Unset): Keeps mentions with this sentiment only.
        intent (str | Unset): Returns only mentions with this tag. One of bug_report, buy_intent,
            churn_intent, comparison, complaint, event, feedback, hiring, industry_insight, launch,
            praise, pricing, promotional, question and testimonial.
        automated (bool | Unset): true keeps mentions that look machine-made, such as bot
            accounts, scheduled or template posts and AI-written text. false keeps the others,
            including mentions scored before this flag existed. Leave it out for all.
        person_id (str | Unset): Keeps mentions by this person (an id from /v1/people), including
            merged accounts. Turns on includeMuted.
        include_muted (bool | Unset): true also returns mentions by muted people, which are hidden
            by default.
        assignee_id (str | Unset): Member user id. Returns only mentions assigned to them.
        snoozed (bool | Unset): true shows only snoozed mentions, which are otherwise hidden until
            they wake.
        exclude_authors (list[str] | None | Unset): Leaves out these authors, given as display
            names, handles or profile links. Repeat the parameter or send one value with commas.
        min_relevance (int | None | Unset): Keeps mentions with this relevance score or higher.
            Unscored mentions are left out.
        min_confidence (float | None | Unset): Minimum classifier confidence, 0 to 1. Mentions
            with no confidence are dropped.
        min_followers (int | None | Unset): Sends only posts by authors with this many followers
            or more. Unknown counts are left out.
        max_followers (int | None | Unset): Keeps posts by authors with this many followers or
            fewer. Unknown counts are left out.
        is_reply (bool | Unset): true keeps replies and comments, meaning posts that answer
            another post. false keeps posts that are not replies. Leave it out for both.
        alert_id (str | Unset): Adds an alert rule's filter (an id from GET /v1/alerts) to the
            other filters. You get the mentions the rule would send, useful for a preview or an export
            in feed form. An unknown id returns 404.
        view_id (str | Unset): Adds a saved view's filter (an id from GET /v1/views) to the other
            filters, with every condition joined by AND. You get exactly what the view shows. An
            unknown id returns 404.
        keyword_kinds (list[ExportMentionsCsvKeywordKindsItem] | Unset): Keeps matches of keywords
            of these kinds only (brand, competitor, topic). Repeat the parameter or separate values
            with commas.
        tags (list[str] | None | Unset): Keeps authors your workspace gave one of these tags,
            matched exactly and by case. Repeat the parameter or separate values with commas.
        link_hosts (list[str] | None | Unset): Keeps posts that link to one of these hosts or its
            subdomains, so slack.com also matches api.slack.com. Repeat the parameter or separate
            values with commas.
        platforms (list[ExportMentionsCsvPlatformsItem] | Unset): Keeps posts from these platforms
            only.
        not_platforms (list[ExportMentionsCsvNotPlatformsItem] | Unset): Platforms to exclude.
        keyword_ids (list[str] | None | Unset): Keeps matches of these keywords only.
        group_ids (list[str] | None | Unset): Keeps matches of keywords in these groups only
            (grp_...). Repeat the parameter or separate values with commas.
        not_group_ids (list[str] | None | Unset): Hides matches from keywords that belong to these
            groups.
        not_keyword_ids (list[str] | None | Unset): Keyword ids to exclude.
        sentiments (list[ExportMentionsCsvSentimentsItem] | Unset): Keeps mentions with these
            sentiments only.
        not_sentiments (list[ExportMentionsCsvNotSentimentsItem] | Unset): Leaves out these
            sentiments. Mentions not scored yet are kept.
        intents (list[str] | None | Unset): Keeps mentions tagged with one of these intents or
            topics.
        not_intents (list[str] | None | Unset): Intent or topic tags to exclude.
        not_link_hosts (list[str] | None | Unset): Leaves out posts that link to these hosts or
            their subdomains.
        not_tags (list[str] | None | Unset): Leaves out authors your workspace gave one of these
            tags.
        languages (list[str] | Unset): Sends only posts in these languages, as ISO 639-1 codes
            such as en, es or de. Posts with an unknown language are left out.
        not_languages (list[str] | Unset): Leaves out posts in these languages. Posts with an
            unknown language are kept.
        ratings (list[int] | Unset): Keeps reviews with one of these star ratings, from 1 to 5.
            Use ratings=1,2 for the unhappy ones. Posts that are not reviews are left out.
        not_ratings (list[int] | Unset): Star ratings (1 to 5) to hide, such as notRatings=5.
            Other posts are unaffected.
        min_likes (int | None | Unset): Keeps posts with this many likes (upvotes, reactions) or
            more, counted when the post was collected. Posts without a like count are left out.
        min_reposts (int | None | Unset): Keeps posts with this many reposts (shares, retweets) or
            more, counted when the post was collected. Posts without a repost count are left out.
        min_replies (int | None | Unset): Keeps posts with this many replies (comments) or more,
            counted when the post was collected. Posts without a reply count are left out.
        min_quotes (int | None | Unset): Keeps posts with this many quotes or more, counted when
            the post was collected. Posts without a quote count are left out.
        min_views (int | None | Unset): Keeps posts with this many views (plays) or more, counted
            when the post was collected. Posts without a view count are left out.
        min_bookmarks (int | None | Unset): Keeps posts with this many bookmarks (saves) or more,
            counted when the post was collected. Posts without a bookmark count are left out.
        any_of (str | Unset): Groups of conditions joined by OR, as URL-encoded JSON. For example
            [{"platforms":["github"],"intents":["bug_report"]},{"sentiments":["negative"]}] means "bug
            reports on GitHub, or anything negative". A group uses the fields of a view filter, where
            a list matches any value, a not list matches none, and all conditions are joined by AND. A
            mention passes when one group matches, and the other filters here still apply. Send 1 to
            10 groups, none empty and none nested.
        q (str | Unset): Searches post text and author names.
        since (datetime.datetime | Unset): Keeps posts published at this time or later, as ISO
            8601 or epoch ms.
        until (datetime.datetime | Unset): Keeps posts published at this time or earlier, as ISO
            8601 or epoch ms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return sync_detailed(
        client=client,
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        view_id=view_id,
        keyword_kinds=keyword_kinds,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        ratings=ratings,
        not_ratings=not_ratings,
        min_likes=min_likes,
        min_reposts=min_reposts,
        min_replies=min_replies,
        min_quotes=min_quotes,
        min_views=min_views,
        min_bookmarks=min_bookmarks,
        any_of=any_of,
        q=q,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: ExportMentionsCsvPlatform | Unset = UNSET,
    status: ExportMentionsCsvStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: ExportMentionsCsvSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    keyword_kinds: list[ExportMentionsCsvKeywordKindsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[ExportMentionsCsvPlatformsItem] | Unset = UNSET,
    not_platforms: list[ExportMentionsCsvNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[ExportMentionsCsvSentimentsItem] | Unset = UNSET,
    not_sentiments: list[ExportMentionsCsvNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    ratings: list[int] | Unset = UNSET,
    not_ratings: list[int] | Unset = UNSET,
    min_likes: int | None | Unset = UNSET,
    min_reposts: int | None | Unset = UNSET,
    min_replies: int | None | Unset = UNSET,
    min_quotes: int | None | Unset = UNSET,
    min_views: int | None | Unset = UNSET,
    min_bookmarks: int | None | Unset = UNSET,
    any_of: str | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Export mentions as CSV

     Returns as CSV the mentions GET /v1/mentions lists for the same filters. Rows are ordered by match
    time, latest first, which is the order they reached your feed and can differ from the post date. The
    columns are id, published_at, platform, keyword, author, author_url, author_followers, relevance,
    sentiment, intents (separated by |), language, confidence, status, relevant, delivered, url, links
    (separated by |), text (the first 1,000 characters), group, group_external_id, rating and app_id
    (reviews only), and title and image_url (on platforms that have them). The file holds at most 10,000
    rows, and the X-Mentions-Truncated header tells you when rows were cut. Each workspace can export 6
    times a minute, and a 429 includes Retry-After.

    Args:
        keyword_id (str | Unset): Only this keyword's matches.
        platform (ExportMentionsCsvPlatform | Unset): Only this platform's posts.
        status (ExportMentionsCsvStatus | Unset): Keeps mentions with this status only. Leave it
            out for all statuses.
        relevant (bool | Unset): true keeps mentions the classifier scored relevant. false keeps
            the others, including unscored ones.
        sentiment (ExportMentionsCsvSentiment | Unset): Keeps mentions with this sentiment only.
        intent (str | Unset): Returns only mentions with this tag. One of bug_report, buy_intent,
            churn_intent, comparison, complaint, event, feedback, hiring, industry_insight, launch,
            praise, pricing, promotional, question and testimonial.
        automated (bool | Unset): true keeps mentions that look machine-made, such as bot
            accounts, scheduled or template posts and AI-written text. false keeps the others,
            including mentions scored before this flag existed. Leave it out for all.
        person_id (str | Unset): Keeps mentions by this person (an id from /v1/people), including
            merged accounts. Turns on includeMuted.
        include_muted (bool | Unset): true also returns mentions by muted people, which are hidden
            by default.
        assignee_id (str | Unset): Member user id. Returns only mentions assigned to them.
        snoozed (bool | Unset): true shows only snoozed mentions, which are otherwise hidden until
            they wake.
        exclude_authors (list[str] | None | Unset): Leaves out these authors, given as display
            names, handles or profile links. Repeat the parameter or send one value with commas.
        min_relevance (int | None | Unset): Keeps mentions with this relevance score or higher.
            Unscored mentions are left out.
        min_confidence (float | None | Unset): Minimum classifier confidence, 0 to 1. Mentions
            with no confidence are dropped.
        min_followers (int | None | Unset): Sends only posts by authors with this many followers
            or more. Unknown counts are left out.
        max_followers (int | None | Unset): Keeps posts by authors with this many followers or
            fewer. Unknown counts are left out.
        is_reply (bool | Unset): true keeps replies and comments, meaning posts that answer
            another post. false keeps posts that are not replies. Leave it out for both.
        alert_id (str | Unset): Adds an alert rule's filter (an id from GET /v1/alerts) to the
            other filters. You get the mentions the rule would send, useful for a preview or an export
            in feed form. An unknown id returns 404.
        view_id (str | Unset): Adds a saved view's filter (an id from GET /v1/views) to the other
            filters, with every condition joined by AND. You get exactly what the view shows. An
            unknown id returns 404.
        keyword_kinds (list[ExportMentionsCsvKeywordKindsItem] | Unset): Keeps matches of keywords
            of these kinds only (brand, competitor, topic). Repeat the parameter or separate values
            with commas.
        tags (list[str] | None | Unset): Keeps authors your workspace gave one of these tags,
            matched exactly and by case. Repeat the parameter or separate values with commas.
        link_hosts (list[str] | None | Unset): Keeps posts that link to one of these hosts or its
            subdomains, so slack.com also matches api.slack.com. Repeat the parameter or separate
            values with commas.
        platforms (list[ExportMentionsCsvPlatformsItem] | Unset): Keeps posts from these platforms
            only.
        not_platforms (list[ExportMentionsCsvNotPlatformsItem] | Unset): Platforms to exclude.
        keyword_ids (list[str] | None | Unset): Keeps matches of these keywords only.
        group_ids (list[str] | None | Unset): Keeps matches of keywords in these groups only
            (grp_...). Repeat the parameter or separate values with commas.
        not_group_ids (list[str] | None | Unset): Hides matches from keywords that belong to these
            groups.
        not_keyword_ids (list[str] | None | Unset): Keyword ids to exclude.
        sentiments (list[ExportMentionsCsvSentimentsItem] | Unset): Keeps mentions with these
            sentiments only.
        not_sentiments (list[ExportMentionsCsvNotSentimentsItem] | Unset): Leaves out these
            sentiments. Mentions not scored yet are kept.
        intents (list[str] | None | Unset): Keeps mentions tagged with one of these intents or
            topics.
        not_intents (list[str] | None | Unset): Intent or topic tags to exclude.
        not_link_hosts (list[str] | None | Unset): Leaves out posts that link to these hosts or
            their subdomains.
        not_tags (list[str] | None | Unset): Leaves out authors your workspace gave one of these
            tags.
        languages (list[str] | Unset): Sends only posts in these languages, as ISO 639-1 codes
            such as en, es or de. Posts with an unknown language are left out.
        not_languages (list[str] | Unset): Leaves out posts in these languages. Posts with an
            unknown language are kept.
        ratings (list[int] | Unset): Keeps reviews with one of these star ratings, from 1 to 5.
            Use ratings=1,2 for the unhappy ones. Posts that are not reviews are left out.
        not_ratings (list[int] | Unset): Star ratings (1 to 5) to hide, such as notRatings=5.
            Other posts are unaffected.
        min_likes (int | None | Unset): Keeps posts with this many likes (upvotes, reactions) or
            more, counted when the post was collected. Posts without a like count are left out.
        min_reposts (int | None | Unset): Keeps posts with this many reposts (shares, retweets) or
            more, counted when the post was collected. Posts without a repost count are left out.
        min_replies (int | None | Unset): Keeps posts with this many replies (comments) or more,
            counted when the post was collected. Posts without a reply count are left out.
        min_quotes (int | None | Unset): Keeps posts with this many quotes or more, counted when
            the post was collected. Posts without a quote count are left out.
        min_views (int | None | Unset): Keeps posts with this many views (plays) or more, counted
            when the post was collected. Posts without a view count are left out.
        min_bookmarks (int | None | Unset): Keeps posts with this many bookmarks (saves) or more,
            counted when the post was collected. Posts without a bookmark count are left out.
        any_of (str | Unset): Groups of conditions joined by OR, as URL-encoded JSON. For example
            [{"platforms":["github"],"intents":["bug_report"]},{"sentiments":["negative"]}] means "bug
            reports on GitHub, or anything negative". A group uses the fields of a view filter, where
            a list matches any value, a not list matches none, and all conditions are joined by AND. A
            mention passes when one group matches, and the other filters here still apply. Send 1 to
            10 groups, none empty and none nested.
        q (str | Unset): Searches post text and author names.
        since (datetime.datetime | Unset): Keeps posts published at this time or later, as ISO
            8601 or epoch ms.
        until (datetime.datetime | Unset): Keeps posts published at this time or earlier, as ISO
            8601 or epoch ms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        keyword_id=keyword_id,
        platform=platform,
        status=status,
        relevant=relevant,
        sentiment=sentiment,
        intent=intent,
        automated=automated,
        person_id=person_id,
        include_muted=include_muted,
        assignee_id=assignee_id,
        snoozed=snoozed,
        exclude_authors=exclude_authors,
        min_relevance=min_relevance,
        min_confidence=min_confidence,
        min_followers=min_followers,
        max_followers=max_followers,
        is_reply=is_reply,
        alert_id=alert_id,
        view_id=view_id,
        keyword_kinds=keyword_kinds,
        tags=tags,
        link_hosts=link_hosts,
        platforms=platforms,
        not_platforms=not_platforms,
        keyword_ids=keyword_ids,
        group_ids=group_ids,
        not_group_ids=not_group_ids,
        not_keyword_ids=not_keyword_ids,
        sentiments=sentiments,
        not_sentiments=not_sentiments,
        intents=intents,
        not_intents=not_intents,
        not_link_hosts=not_link_hosts,
        not_tags=not_tags,
        languages=languages,
        not_languages=not_languages,
        ratings=ratings,
        not_ratings=not_ratings,
        min_likes=min_likes,
        min_reposts=min_reposts,
        min_replies=min_replies,
        min_quotes=min_quotes,
        min_views=min_views,
        min_bookmarks=min_bookmarks,
        any_of=any_of,
        q=q,
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword_id: str | Unset = UNSET,
    platform: ExportMentionsCsvPlatform | Unset = UNSET,
    status: ExportMentionsCsvStatus | Unset = UNSET,
    relevant: bool | Unset = UNSET,
    sentiment: ExportMentionsCsvSentiment | Unset = UNSET,
    intent: str | Unset = UNSET,
    automated: bool | Unset = UNSET,
    person_id: str | Unset = UNSET,
    include_muted: bool | Unset = UNSET,
    assignee_id: str | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    exclude_authors: list[str] | None | Unset = UNSET,
    min_relevance: int | None | Unset = UNSET,
    min_confidence: float | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    is_reply: bool | Unset = UNSET,
    alert_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    keyword_kinds: list[ExportMentionsCsvKeywordKindsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    platforms: list[ExportMentionsCsvPlatformsItem] | Unset = UNSET,
    not_platforms: list[ExportMentionsCsvNotPlatformsItem] | Unset = UNSET,
    keyword_ids: list[str] | None | Unset = UNSET,
    group_ids: list[str] | None | Unset = UNSET,
    not_group_ids: list[str] | None | Unset = UNSET,
    not_keyword_ids: list[str] | None | Unset = UNSET,
    sentiments: list[ExportMentionsCsvSentimentsItem] | Unset = UNSET,
    not_sentiments: list[ExportMentionsCsvNotSentimentsItem] | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    not_link_hosts: list[str] | None | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    languages: list[str] | Unset = UNSET,
    not_languages: list[str] | Unset = UNSET,
    ratings: list[int] | Unset = UNSET,
    not_ratings: list[int] | Unset = UNSET,
    min_likes: int | None | Unset = UNSET,
    min_reposts: int | None | Unset = UNSET,
    min_replies: int | None | Unset = UNSET,
    min_quotes: int | None | Unset = UNSET,
    min_views: int | None | Unset = UNSET,
    min_bookmarks: int | None | Unset = UNSET,
    any_of: str | Unset = UNSET,
    q: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Export mentions as CSV

     Returns as CSV the mentions GET /v1/mentions lists for the same filters. Rows are ordered by match
    time, latest first, which is the order they reached your feed and can differ from the post date. The
    columns are id, published_at, platform, keyword, author, author_url, author_followers, relevance,
    sentiment, intents (separated by |), language, confidence, status, relevant, delivered, url, links
    (separated by |), text (the first 1,000 characters), group, group_external_id, rating and app_id
    (reviews only), and title and image_url (on platforms that have them). The file holds at most 10,000
    rows, and the X-Mentions-Truncated header tells you when rows were cut. Each workspace can export 6
    times a minute, and a 429 includes Retry-After.

    Args:
        keyword_id (str | Unset): Only this keyword's matches.
        platform (ExportMentionsCsvPlatform | Unset): Only this platform's posts.
        status (ExportMentionsCsvStatus | Unset): Keeps mentions with this status only. Leave it
            out for all statuses.
        relevant (bool | Unset): true keeps mentions the classifier scored relevant. false keeps
            the others, including unscored ones.
        sentiment (ExportMentionsCsvSentiment | Unset): Keeps mentions with this sentiment only.
        intent (str | Unset): Returns only mentions with this tag. One of bug_report, buy_intent,
            churn_intent, comparison, complaint, event, feedback, hiring, industry_insight, launch,
            praise, pricing, promotional, question and testimonial.
        automated (bool | Unset): true keeps mentions that look machine-made, such as bot
            accounts, scheduled or template posts and AI-written text. false keeps the others,
            including mentions scored before this flag existed. Leave it out for all.
        person_id (str | Unset): Keeps mentions by this person (an id from /v1/people), including
            merged accounts. Turns on includeMuted.
        include_muted (bool | Unset): true also returns mentions by muted people, which are hidden
            by default.
        assignee_id (str | Unset): Member user id. Returns only mentions assigned to them.
        snoozed (bool | Unset): true shows only snoozed mentions, which are otherwise hidden until
            they wake.
        exclude_authors (list[str] | None | Unset): Leaves out these authors, given as display
            names, handles or profile links. Repeat the parameter or send one value with commas.
        min_relevance (int | None | Unset): Keeps mentions with this relevance score or higher.
            Unscored mentions are left out.
        min_confidence (float | None | Unset): Minimum classifier confidence, 0 to 1. Mentions
            with no confidence are dropped.
        min_followers (int | None | Unset): Sends only posts by authors with this many followers
            or more. Unknown counts are left out.
        max_followers (int | None | Unset): Keeps posts by authors with this many followers or
            fewer. Unknown counts are left out.
        is_reply (bool | Unset): true keeps replies and comments, meaning posts that answer
            another post. false keeps posts that are not replies. Leave it out for both.
        alert_id (str | Unset): Adds an alert rule's filter (an id from GET /v1/alerts) to the
            other filters. You get the mentions the rule would send, useful for a preview or an export
            in feed form. An unknown id returns 404.
        view_id (str | Unset): Adds a saved view's filter (an id from GET /v1/views) to the other
            filters, with every condition joined by AND. You get exactly what the view shows. An
            unknown id returns 404.
        keyword_kinds (list[ExportMentionsCsvKeywordKindsItem] | Unset): Keeps matches of keywords
            of these kinds only (brand, competitor, topic). Repeat the parameter or separate values
            with commas.
        tags (list[str] | None | Unset): Keeps authors your workspace gave one of these tags,
            matched exactly and by case. Repeat the parameter or separate values with commas.
        link_hosts (list[str] | None | Unset): Keeps posts that link to one of these hosts or its
            subdomains, so slack.com also matches api.slack.com. Repeat the parameter or separate
            values with commas.
        platforms (list[ExportMentionsCsvPlatformsItem] | Unset): Keeps posts from these platforms
            only.
        not_platforms (list[ExportMentionsCsvNotPlatformsItem] | Unset): Platforms to exclude.
        keyword_ids (list[str] | None | Unset): Keeps matches of these keywords only.
        group_ids (list[str] | None | Unset): Keeps matches of keywords in these groups only
            (grp_...). Repeat the parameter or separate values with commas.
        not_group_ids (list[str] | None | Unset): Hides matches from keywords that belong to these
            groups.
        not_keyword_ids (list[str] | None | Unset): Keyword ids to exclude.
        sentiments (list[ExportMentionsCsvSentimentsItem] | Unset): Keeps mentions with these
            sentiments only.
        not_sentiments (list[ExportMentionsCsvNotSentimentsItem] | Unset): Leaves out these
            sentiments. Mentions not scored yet are kept.
        intents (list[str] | None | Unset): Keeps mentions tagged with one of these intents or
            topics.
        not_intents (list[str] | None | Unset): Intent or topic tags to exclude.
        not_link_hosts (list[str] | None | Unset): Leaves out posts that link to these hosts or
            their subdomains.
        not_tags (list[str] | None | Unset): Leaves out authors your workspace gave one of these
            tags.
        languages (list[str] | Unset): Sends only posts in these languages, as ISO 639-1 codes
            such as en, es or de. Posts with an unknown language are left out.
        not_languages (list[str] | Unset): Leaves out posts in these languages. Posts with an
            unknown language are kept.
        ratings (list[int] | Unset): Keeps reviews with one of these star ratings, from 1 to 5.
            Use ratings=1,2 for the unhappy ones. Posts that are not reviews are left out.
        not_ratings (list[int] | Unset): Star ratings (1 to 5) to hide, such as notRatings=5.
            Other posts are unaffected.
        min_likes (int | None | Unset): Keeps posts with this many likes (upvotes, reactions) or
            more, counted when the post was collected. Posts without a like count are left out.
        min_reposts (int | None | Unset): Keeps posts with this many reposts (shares, retweets) or
            more, counted when the post was collected. Posts without a repost count are left out.
        min_replies (int | None | Unset): Keeps posts with this many replies (comments) or more,
            counted when the post was collected. Posts without a reply count are left out.
        min_quotes (int | None | Unset): Keeps posts with this many quotes or more, counted when
            the post was collected. Posts without a quote count are left out.
        min_views (int | None | Unset): Keeps posts with this many views (plays) or more, counted
            when the post was collected. Posts without a view count are left out.
        min_bookmarks (int | None | Unset): Keeps posts with this many bookmarks (saves) or more,
            counted when the post was collected. Posts without a bookmark count are left out.
        any_of (str | Unset): Groups of conditions joined by OR, as URL-encoded JSON. For example
            [{"platforms":["github"],"intents":["bug_report"]},{"sentiments":["negative"]}] means "bug
            reports on GitHub, or anything negative". A group uses the fields of a view filter, where
            a list matches any value, a not list matches none, and all conditions are joined by AND. A
            mention passes when one group matches, and the other filters here still apply. Send 1 to
            10 groups, none empty and none nested.
        q (str | Unset): Searches post text and author names.
        since (datetime.datetime | Unset): Keeps posts published at this time or later, as ISO
            8601 or epoch ms.
        until (datetime.datetime | Unset): Keeps posts published at this time or earlier, as ISO
            8601 or epoch ms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword_id=keyword_id,
            platform=platform,
            status=status,
            relevant=relevant,
            sentiment=sentiment,
            intent=intent,
            automated=automated,
            person_id=person_id,
            include_muted=include_muted,
            assignee_id=assignee_id,
            snoozed=snoozed,
            exclude_authors=exclude_authors,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            min_followers=min_followers,
            max_followers=max_followers,
            is_reply=is_reply,
            alert_id=alert_id,
            view_id=view_id,
            keyword_kinds=keyword_kinds,
            tags=tags,
            link_hosts=link_hosts,
            platforms=platforms,
            not_platforms=not_platforms,
            keyword_ids=keyword_ids,
            group_ids=group_ids,
            not_group_ids=not_group_ids,
            not_keyword_ids=not_keyword_ids,
            sentiments=sentiments,
            not_sentiments=not_sentiments,
            intents=intents,
            not_intents=not_intents,
            not_link_hosts=not_link_hosts,
            not_tags=not_tags,
            languages=languages,
            not_languages=not_languages,
            ratings=ratings,
            not_ratings=not_ratings,
            min_likes=min_likes,
            min_reposts=min_reposts,
            min_replies=min_replies,
            min_quotes=min_quotes,
            min_views=min_views,
            min_bookmarks=min_bookmarks,
            any_of=any_of,
            q=q,
            since=since,
            until=until,
        )
    ).parsed
