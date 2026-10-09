from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_source_platform import ReviewSourcePlatform

T = TypeVar("T", bound="ReviewSource")


@_attrs_define
class ReviewSource:
    """
    Attributes:
        platform (ReviewSourcePlatform): Where the reviews come from. appstore is the Apple App Store, googleplay is
            Google Play, trustpilot is a company's Trustpilot page and googlemaps is the Google reviews of a place.
        id (str): The platform's own id. An App Store app id, a Google Play package name, a Trustpilot domain, or a
            Google Place ID or cid.
        url (str): URL of the review page, such as an app's store listing, a company's Trustpilot page or a place on
            Google Maps.
        countries (list[str]): Two-letter storefront codes, lowercase. Empty for Trustpilot and Google Maps.
        language (None | str): The review language on Google Play. Null on other platforms.
        connected_at (str): When the keyword began collecting reviews from this page.
    """

    platform: ReviewSourcePlatform
    id: str
    url: str
    countries: list[str]
    language: None | str
    connected_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        id = self.id

        url = self.url

        countries = self.countries

        language: None | str
        language = self.language

        connected_at = self.connected_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "id": id,
                "url": url,
                "countries": countries,
                "language": language,
                "connectedAt": connected_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = ReviewSourcePlatform(d.pop("platform"))

        id = d.pop("id")

        url = d.pop("url")

        countries = cast(list[str], d.pop("countries"))

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        connected_at = d.pop("connectedAt")

        review_source = cls(
            platform=platform,
            id=id,
            url=url,
            countries=countries,
            language=language,
            connected_at=connected_at,
        )

        review_source.additional_properties = d
        return review_source

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
