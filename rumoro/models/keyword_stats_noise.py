from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordStatsNoise")


@_attrs_define
class KeywordStatsNoise:
    """Relevance of the scored matches from the past 14 days. A keyword you narrow today drops the flag within two weeks.

    Attributes:
        scored (int): How many of the last 14 days' matches are scored.
        relevant (int): How many of them were scored relevant.
        noisy (bool): True when the past 14 days have 20 or more scored matches and fewer than 30% are relevant. Narrow
            the keyword with required terms, excluded terms or context, because every match is billed, relevant or not.
    """

    scored: int
    relevant: int
    noisy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scored = self.scored

        relevant = self.relevant

        noisy = self.noisy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scored": scored,
                "relevant": relevant,
                "noisy": noisy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scored = d.pop("scored")

        relevant = d.pop("relevant")

        noisy = d.pop("noisy")

        keyword_stats_noise = cls(
            scored=scored,
            relevant=relevant,
            noisy=noisy,
        )

        keyword_stats_noise.additional_properties = d
        return keyword_stats_noise

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
