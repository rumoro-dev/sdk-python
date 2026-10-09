from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_body_filter_platforms_item import (
    UpdateAlertBodyFilterPlatformsItem,
)
from ..models.update_alert_body_filter_sentiments_item import (
    UpdateAlertBodyFilterSentimentsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_group import FilterGroup


T = TypeVar("T", bound="UpdateAlertBodyFilter")


@_attrs_define
class UpdateAlertBodyFilter:
    """Sets the full new filter.

    Attributes:
        keyword_ids (list[str] | Unset): Limits the rule to these keywords.
        group_ids (list[str] | Unset): Limits the rule to keywords in these groups (grp_...), for example one rule for
            each client.
        platforms (list[UpdateAlertBodyFilterPlatformsItem] | Unset): Limits the rule to posts from these platforms.
        min_relevance (int | Unset): The lowest relevance score the rule sends. Without it, only relevant mentions are
            sent, meaning a score of 40 or more. A lower value, down to 0, also sends matches the classifier rated as noise.
            A higher value sends fewer. Email channels always use 40, whatever the rule says. Mentions without a score are
            never sent.
        min_confidence (float | Unset): Sends only mentions whose classifier confidence is this value or higher, from 0
            to 1. Mentions without a confidence are left out.
        sentiments (list[UpdateAlertBodyFilterSentimentsItem] | Unset): Keeps mentions with these sentiments only.
        intents (list[str] | Unset): Sends only mentions with one or more of these intent or topic tags.
        exclude_authors (list[str] | Unset): Leaves out these authors, given as display names, handles or profile links.
        min_followers (int | Unset): Sends only posts by authors with this many followers or more. Unknown counts are
            left out.
        tags (list[str] | Unset): Keeps authors your workspace gave one of these tags.
        link_hosts (list[str] | Unset): Sends only posts that link to one of these hosts or its subdomains, so slack.com
            also matches api.slack.com. Posts without links are left out.
        languages (list[str] | Unset): Sends only posts in these languages, as ISO 639-1 codes such as en, es or de.
            Posts with an unknown language are left out.
        automated (bool | Unset): true sends only posts that look machine-made, such as bot or template posts. false
            sends only the others. Leave it out to send both.
        ratings (list[int] | Unset): Sends only reviews with one of these star ratings, from 1 to 5. Use [1, 2] for the
            unhappy ones. Posts that are not reviews are left out.
        not_ratings (list[int] | Unset): Star ratings (1 to 5) to skip, such as [5]. Other posts still go out.
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

    keyword_ids: list[str] | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    platforms: list[UpdateAlertBodyFilterPlatformsItem] | Unset = UNSET
    min_relevance: int | Unset = UNSET
    min_confidence: float | Unset = UNSET
    sentiments: list[UpdateAlertBodyFilterSentimentsItem] | Unset = UNSET
    intents: list[str] | Unset = UNSET
    exclude_authors: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    languages: list[str] | Unset = UNSET
    automated: bool | Unset = UNSET
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
        keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyword_ids, Unset):
            keyword_ids = self.keyword_ids

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        min_relevance = self.min_relevance

        min_confidence = self.min_confidence

        sentiments: list[str] | Unset = UNSET
        if not isinstance(self.sentiments, Unset):
            sentiments = []
            for sentiments_item_data in self.sentiments:
                sentiments_item = sentiments_item_data.value
                sentiments.append(sentiments_item)

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        exclude_authors: list[str] | Unset = UNSET
        if not isinstance(self.exclude_authors, Unset):
            exclude_authors = self.exclude_authors

        min_followers = self.min_followers

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        languages: list[str] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        automated = self.automated

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
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if intents is not UNSET:
            field_dict["intents"] = intents
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if languages is not UNSET:
            field_dict["languages"] = languages
        if automated is not UNSET:
            field_dict["automated"] = automated
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
        keyword_ids = cast(list[str], d.pop("keywordIds", UNSET))

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[UpdateAlertBodyFilterPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = UpdateAlertBodyFilterPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        min_relevance = d.pop("minRelevance", UNSET)

        min_confidence = d.pop("minConfidence", UNSET)

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[UpdateAlertBodyFilterSentimentsItem] | Unset = UNSET
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = UpdateAlertBodyFilterSentimentsItem(
                    sentiments_item_data
                )

                sentiments.append(sentiments_item)

        intents = cast(list[str], d.pop("intents", UNSET))

        exclude_authors = cast(list[str], d.pop("excludeAuthors", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        languages = cast(list[str], d.pop("languages", UNSET))

        automated = d.pop("automated", UNSET)

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

        update_alert_body_filter = cls(
            keyword_ids=keyword_ids,
            group_ids=group_ids,
            platforms=platforms,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            sentiments=sentiments,
            intents=intents,
            exclude_authors=exclude_authors,
            min_followers=min_followers,
            tags=tags,
            link_hosts=link_hosts,
            languages=languages,
            automated=automated,
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

        update_alert_body_filter.additional_properties = d
        return update_alert_body_filter

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
