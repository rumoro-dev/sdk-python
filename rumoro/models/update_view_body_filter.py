from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_view_body_filter_keyword_kinds_item import (
    UpdateViewBodyFilterKeywordKindsItem,
)
from ..models.update_view_body_filter_not_platforms_item import (
    UpdateViewBodyFilterNotPlatformsItem,
)
from ..models.update_view_body_filter_not_sentiments_item import (
    UpdateViewBodyFilterNotSentimentsItem,
)
from ..models.update_view_body_filter_platforms_item import (
    UpdateViewBodyFilterPlatformsItem,
)
from ..models.update_view_body_filter_sentiments_item import (
    UpdateViewBodyFilterSentimentsItem,
)
from ..models.update_view_body_filter_status import UpdateViewBodyFilterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_group import FilterGroup


T = TypeVar("T", bound="UpdateViewBodyFilter")


@_attrs_define
class UpdateViewBodyFilter:
    """Sets the full new filter.

    Attributes:
        q (str | Unset): Searches post text and author names.
        keyword_ids (list[str] | Unset): Keeps matches of these keywords only.
        not_keyword_ids (list[str] | Unset): Keyword ids to exclude.
        keyword_kinds (list[UpdateViewBodyFilterKeywordKindsItem] | Unset): Keyword kinds to keep, out of brand,
            competitor and topic.
        group_ids (list[str] | Unset): Limits to keywords from these groups (grp_...).
        not_group_ids (list[str] | Unset): Hides matches from keywords that belong to these groups.
        platforms (list[UpdateViewBodyFilterPlatformsItem] | Unset): Keeps posts from these platforms only.
        not_platforms (list[UpdateViewBodyFilterNotPlatformsItem] | Unset): Platforms to exclude.
        status (UpdateViewBodyFilterStatus | Unset): Keeps mentions with this status only (open, ignored or done).
        relevant (bool | Unset): Filter on the classifier's verdict. true keeps relevant mentions, false the rest.
        min_relevance (int | Unset): Minimum relevance score a mention needs.
        min_confidence (float | Unset): Keeps mentions whose classifier confidence is this value or higher.
        sentiments (list[UpdateViewBodyFilterSentimentsItem] | Unset): Keeps mentions with these sentiments only.
        not_sentiments (list[UpdateViewBodyFilterNotSentimentsItem] | Unset): Hides these sentiments. Unscored mentions
            stay.
        intents (list[str] | Unset): Keeps mentions tagged with one of these intents or topics.
        not_intents (list[str] | Unset): Hides mentions with these tags.
        automated (bool | Unset): true keeps posts that look machine-made. false keeps the others.
        languages (list[str] | Unset): Keeps posts in these languages only, as ISO 639-1 codes.
        not_languages (list[str] | Unset): Leaves out posts in these languages. Posts with an unknown language are kept.
        tags (list[str] | Unset): Keeps authors your workspace gave one of these tags.
        not_tags (list[str] | Unset): Leaves out authors with one of these tags.
        link_hosts (list[str] | Unset): Keeps posts that link to one of these hosts or its subdomains.
        not_link_hosts (list[str] | Unset): Leaves out posts that link to these hosts.
        min_followers (int | Unset): Keeps authors with this many followers or more. Unknown counts are left out.
        max_followers (int | Unset): Keeps authors with this many followers or fewer. Unknown counts are left out.
        is_reply (bool | Unset): true keeps replies and comments. false keeps posts that are not replies.
        exclude_authors (list[str] | Unset): Leaves out these authors, given as display names, handles or profile links.
        ratings (list[int] | Unset): Keeps reviews with one of these star ratings. Posts that are not reviews are left
            out.
        not_ratings (list[int] | Unset): Hides reviews with these star ratings. Other posts are not affected.
        min_likes (int | Unset): Keeps posts with this many likes (upvotes, reactions) or more, counted when the post
            was collected. Posts without a like count are left out.
        min_reposts (int | Unset): Keeps posts with this many reposts (shares, retweets) or more, counted when the post
            was collected. Posts without a repost count are left out.
        min_replies (int | Unset): Keeps posts with this many replies (comments) or more, counted when the post was
            collected. Posts without a reply count are left out.
        min_quotes (int | Unset): Keeps posts with this many quotes or more, counted when the post was collected. Posts
            without a quote count are left out.
        min_views (int | Unset): Keeps posts with this many views (plays) or more, counted when the post was collected.
            Posts without a view count are left out.
        min_bookmarks (int | Unset): Keeps posts with this many bookmarks (saves) or more, counted when the post was
            collected. Posts without a bookmark count are left out.
        any_of (list[FilterGroup] | Unset): Up to 10 OR'd groups (at least 1). A mention must meet every condition of
            some group, plus all other conditions, so the filter reads (other conditions) AND (group 1 OR group 2 ...).
            Groups take view filter fields (platforms, sentiments, intents, keywordKinds, the not lists and so on) but no
            nested anyOf.
    """

    q: str | Unset = UNSET
    keyword_ids: list[str] | Unset = UNSET
    not_keyword_ids: list[str] | Unset = UNSET
    keyword_kinds: list[UpdateViewBodyFilterKeywordKindsItem] | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    not_group_ids: list[str] | Unset = UNSET
    platforms: list[UpdateViewBodyFilterPlatformsItem] | Unset = UNSET
    not_platforms: list[UpdateViewBodyFilterNotPlatformsItem] | Unset = UNSET
    status: UpdateViewBodyFilterStatus | Unset = UNSET
    relevant: bool | Unset = UNSET
    min_relevance: int | Unset = UNSET
    min_confidence: float | Unset = UNSET
    sentiments: list[UpdateViewBodyFilterSentimentsItem] | Unset = UNSET
    not_sentiments: list[UpdateViewBodyFilterNotSentimentsItem] | Unset = UNSET
    intents: list[str] | Unset = UNSET
    not_intents: list[str] | Unset = UNSET
    automated: bool | Unset = UNSET
    languages: list[str] | Unset = UNSET
    not_languages: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    not_tags: list[str] | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    not_link_hosts: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    max_followers: int | Unset = UNSET
    is_reply: bool | Unset = UNSET
    exclude_authors: list[str] | Unset = UNSET
    ratings: list[int] | Unset = UNSET
    not_ratings: list[int] | Unset = UNSET
    min_likes: int | Unset = UNSET
    min_reposts: int | Unset = UNSET
    min_replies: int | Unset = UNSET
    min_quotes: int | Unset = UNSET
    min_views: int | Unset = UNSET
    min_bookmarks: int | Unset = UNSET
    any_of: list[FilterGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyword_ids, Unset):
            keyword_ids = self.keyword_ids

        not_keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_keyword_ids, Unset):
            not_keyword_ids = self.not_keyword_ids

        keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.keyword_kinds, Unset):
            keyword_kinds = []
            for keyword_kinds_item_data in self.keyword_kinds:
                keyword_kinds_item = keyword_kinds_item_data.value
                keyword_kinds.append(keyword_kinds_item)

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        not_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_group_ids, Unset):
            not_group_ids = self.not_group_ids

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        not_platforms: list[str] | Unset = UNSET
        if not isinstance(self.not_platforms, Unset):
            not_platforms = []
            for not_platforms_item_data in self.not_platforms:
                not_platforms_item = not_platforms_item_data.value
                not_platforms.append(not_platforms_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        relevant = self.relevant

        min_relevance = self.min_relevance

        min_confidence = self.min_confidence

        sentiments: list[str] | Unset = UNSET
        if not isinstance(self.sentiments, Unset):
            sentiments = []
            for sentiments_item_data in self.sentiments:
                sentiments_item = sentiments_item_data.value
                sentiments.append(sentiments_item)

        not_sentiments: list[str] | Unset = UNSET
        if not isinstance(self.not_sentiments, Unset):
            not_sentiments = []
            for not_sentiments_item_data in self.not_sentiments:
                not_sentiments_item = not_sentiments_item_data.value
                not_sentiments.append(not_sentiments_item)

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        not_intents: list[str] | Unset = UNSET
        if not isinstance(self.not_intents, Unset):
            not_intents = self.not_intents

        automated = self.automated

        languages: list[str] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        not_languages: list[str] | Unset = UNSET
        if not isinstance(self.not_languages, Unset):
            not_languages = self.not_languages

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        not_tags: list[str] | Unset = UNSET
        if not isinstance(self.not_tags, Unset):
            not_tags = self.not_tags

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        not_link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.not_link_hosts, Unset):
            not_link_hosts = self.not_link_hosts

        min_followers = self.min_followers

        max_followers = self.max_followers

        is_reply = self.is_reply

        exclude_authors: list[str] | Unset = UNSET
        if not isinstance(self.exclude_authors, Unset):
            exclude_authors = self.exclude_authors

        ratings: list[int] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings

        not_ratings: list[int] | Unset = UNSET
        if not isinstance(self.not_ratings, Unset):
            not_ratings = self.not_ratings

        min_likes = self.min_likes

        min_reposts = self.min_reposts

        min_replies = self.min_replies

        min_quotes = self.min_quotes

        min_views = self.min_views

        min_bookmarks = self.min_bookmarks

        any_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_of, Unset):
            any_of = []
            for any_of_item_data in self.any_of:
                any_of_item = any_of_item_data.to_dict()
                any_of.append(any_of_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if q is not UNSET:
            field_dict["q"] = q
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if not_keyword_ids is not UNSET:
            field_dict["notKeywordIds"] = not_keyword_ids
        if keyword_kinds is not UNSET:
            field_dict["keywordKinds"] = keyword_kinds
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if not_group_ids is not UNSET:
            field_dict["notGroupIds"] = not_group_ids
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if not_platforms is not UNSET:
            field_dict["notPlatforms"] = not_platforms
        if status is not UNSET:
            field_dict["status"] = status
        if relevant is not UNSET:
            field_dict["relevant"] = relevant
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if not_sentiments is not UNSET:
            field_dict["notSentiments"] = not_sentiments
        if intents is not UNSET:
            field_dict["intents"] = intents
        if not_intents is not UNSET:
            field_dict["notIntents"] = not_intents
        if automated is not UNSET:
            field_dict["automated"] = automated
        if languages is not UNSET:
            field_dict["languages"] = languages
        if not_languages is not UNSET:
            field_dict["notLanguages"] = not_languages
        if tags is not UNSET:
            field_dict["tags"] = tags
        if not_tags is not UNSET:
            field_dict["notTags"] = not_tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if not_link_hosts is not UNSET:
            field_dict["notLinkHosts"] = not_link_hosts
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if max_followers is not UNSET:
            field_dict["maxFollowers"] = max_followers
        if is_reply is not UNSET:
            field_dict["isReply"] = is_reply
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if not_ratings is not UNSET:
            field_dict["notRatings"] = not_ratings
        if min_likes is not UNSET:
            field_dict["minLikes"] = min_likes
        if min_reposts is not UNSET:
            field_dict["minReposts"] = min_reposts
        if min_replies is not UNSET:
            field_dict["minReplies"] = min_replies
        if min_quotes is not UNSET:
            field_dict["minQuotes"] = min_quotes
        if min_views is not UNSET:
            field_dict["minViews"] = min_views
        if min_bookmarks is not UNSET:
            field_dict["minBookmarks"] = min_bookmarks
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_group import FilterGroup

        d = dict(src_dict)
        q = d.pop("q", UNSET)

        keyword_ids = cast(list[str], d.pop("keywordIds", UNSET))

        not_keyword_ids = cast(list[str], d.pop("notKeywordIds", UNSET))

        _keyword_kinds = d.pop("keywordKinds", UNSET)
        keyword_kinds: list[UpdateViewBodyFilterKeywordKindsItem] | Unset = UNSET
        if _keyword_kinds is not UNSET:
            keyword_kinds = []
            for keyword_kinds_item_data in _keyword_kinds:
                keyword_kinds_item = UpdateViewBodyFilterKeywordKindsItem(
                    keyword_kinds_item_data
                )

                keyword_kinds.append(keyword_kinds_item)

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        not_group_ids = cast(list[str], d.pop("notGroupIds", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[UpdateViewBodyFilterPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = UpdateViewBodyFilterPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        _not_platforms = d.pop("notPlatforms", UNSET)
        not_platforms: list[UpdateViewBodyFilterNotPlatformsItem] | Unset = UNSET
        if _not_platforms is not UNSET:
            not_platforms = []
            for not_platforms_item_data in _not_platforms:
                not_platforms_item = UpdateViewBodyFilterNotPlatformsItem(
                    not_platforms_item_data
                )

                not_platforms.append(not_platforms_item)

        _status = d.pop("status", UNSET)
        status: UpdateViewBodyFilterStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateViewBodyFilterStatus(_status)

        relevant = d.pop("relevant", UNSET)

        min_relevance = d.pop("minRelevance", UNSET)

        min_confidence = d.pop("minConfidence", UNSET)

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[UpdateViewBodyFilterSentimentsItem] | Unset = UNSET
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = UpdateViewBodyFilterSentimentsItem(
                    sentiments_item_data
                )

                sentiments.append(sentiments_item)

        _not_sentiments = d.pop("notSentiments", UNSET)
        not_sentiments: list[UpdateViewBodyFilterNotSentimentsItem] | Unset = UNSET
        if _not_sentiments is not UNSET:
            not_sentiments = []
            for not_sentiments_item_data in _not_sentiments:
                not_sentiments_item = UpdateViewBodyFilterNotSentimentsItem(
                    not_sentiments_item_data
                )

                not_sentiments.append(not_sentiments_item)

        intents = cast(list[str], d.pop("intents", UNSET))

        not_intents = cast(list[str], d.pop("notIntents", UNSET))

        automated = d.pop("automated", UNSET)

        languages = cast(list[str], d.pop("languages", UNSET))

        not_languages = cast(list[str], d.pop("notLanguages", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        not_tags = cast(list[str], d.pop("notTags", UNSET))

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        not_link_hosts = cast(list[str], d.pop("notLinkHosts", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        max_followers = d.pop("maxFollowers", UNSET)

        is_reply = d.pop("isReply", UNSET)

        exclude_authors = cast(list[str], d.pop("excludeAuthors", UNSET))

        ratings = cast(list[int], d.pop("ratings", UNSET))

        not_ratings = cast(list[int], d.pop("notRatings", UNSET))

        min_likes = d.pop("minLikes", UNSET)

        min_reposts = d.pop("minReposts", UNSET)

        min_replies = d.pop("minReplies", UNSET)

        min_quotes = d.pop("minQuotes", UNSET)

        min_views = d.pop("minViews", UNSET)

        min_bookmarks = d.pop("minBookmarks", UNSET)

        _any_of = d.pop("anyOf", UNSET)
        any_of: list[FilterGroup] | Unset = UNSET
        if _any_of is not UNSET:
            any_of = []
            for any_of_item_data in _any_of:
                any_of_item = FilterGroup.from_dict(any_of_item_data)

                any_of.append(any_of_item)

        update_view_body_filter = cls(
            q=q,
            keyword_ids=keyword_ids,
            not_keyword_ids=not_keyword_ids,
            keyword_kinds=keyword_kinds,
            group_ids=group_ids,
            not_group_ids=not_group_ids,
            platforms=platforms,
            not_platforms=not_platforms,
            status=status,
            relevant=relevant,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            sentiments=sentiments,
            not_sentiments=not_sentiments,
            intents=intents,
            not_intents=not_intents,
            automated=automated,
            languages=languages,
            not_languages=not_languages,
            tags=tags,
            not_tags=not_tags,
            link_hosts=link_hosts,
            not_link_hosts=not_link_hosts,
            min_followers=min_followers,
            max_followers=max_followers,
            is_reply=is_reply,
            exclude_authors=exclude_authors,
            ratings=ratings,
            not_ratings=not_ratings,
            min_likes=min_likes,
            min_reposts=min_reposts,
            min_replies=min_replies,
            min_quotes=min_quotes,
            min_views=min_views,
            min_bookmarks=min_bookmarks,
            any_of=any_of,
        )

        update_view_body_filter.additional_properties = d
        return update_view_body_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
