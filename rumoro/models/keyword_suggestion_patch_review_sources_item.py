from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_review_sources_item_platform import (
    KeywordSuggestionPatchReviewSourcesItemPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchReviewSourcesItem")


@_attrs_define
class KeywordSuggestionPatchReviewSourcesItem:
    """A review page, by link or by platform and id. Its reviews become this keyword's mentions.

    Attributes:
        url (str | Unset): Review page link, or send platform and id instead. Accepts App Store and Google Play app
            links (https://apps.apple.com/us/app/slack/id618783545,
            https://play.google.com/store/apps/details?id=com.Slack), Trustpilot pages
            (https://www.trustpilot.com/review/slack.com) and Google Maps places (full or maps.app.goo.gl link).
        platform (KeywordSuggestionPatchReviewSourcesItemPlatform | Unset): Where the reviews come from. appstore is the
            Apple App Store, googleplay is Google Play, trustpilot is a company's Trustpilot page and googlemaps is the
            Google reviews of a place.
        id (str | Unset): The platform's own id. On the App Store it is the number after "id" in the link, on Google
            Play the package name, on Trustpilot the company's domain (slack.com) and on Google Maps a Place ID (ChIJ...).
        countries (list[str] | Unset): For App Store and Google Play. Up to 20 storefronts to read, as two-letter codes.
            Without it, the storefront in the link is used, or us. Each storefront adds one poll a day, and a review found
            in two storefronts is still one mention. Trustpilot and Google Maps have a single page and take no countries.
        language (str | Unset): For Google Play. The review language to read, such as en, es, de or pt-BR, since Google
            Play returns one language at a time. Without it, the link's hl is used, or en.
    """

    url: str | Unset = UNSET
    platform: KeywordSuggestionPatchReviewSourcesItemPlatform | Unset = UNSET
    id: str | Unset = UNSET
    countries: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        id = self.id

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if platform is not UNSET:
            field_dict["platform"] = platform
        if id is not UNSET:
            field_dict["id"] = id
        if countries is not UNSET:
            field_dict["countries"] = countries
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: KeywordSuggestionPatchReviewSourcesItemPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = KeywordSuggestionPatchReviewSourcesItemPlatform(_platform)

        id = d.pop("id", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        language = d.pop("language", UNSET)

        keyword_suggestion_patch_review_sources_item = cls(
            url=url,
            platform=platform,
            id=id,
            countries=countries,
            language=language,
        )

        keyword_suggestion_patch_review_sources_item.additional_properties = d
        return keyword_suggestion_patch_review_sources_item

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
