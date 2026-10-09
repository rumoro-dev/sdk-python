from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthSample")


@_attrs_define
class KeywordHealthSample:
    """The posts used for noiseTerms, noiseAuthors and the effects. Only posts the keyword's current rules accept count,
    not ones an older rule let in. Review platforms match by app rather than text and are left out.

        Attributes:
            noise (int): Noise posts that were read, up to 200 of the newest in the window or since stats.judgedSince, from
                platforms matched by text. Zero when fewer than 20 matches were scored since a change.
            relevant (int): Relevant posts that were read, chosen the same way.
    """

    noise: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        noise = self.noise

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noise": noise,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        noise = d.pop("noise")

        relevant = d.pop("relevant")

        keyword_health_sample = cls(
            noise=noise,
            relevant=relevant,
        )

        keyword_health_sample.additional_properties = d
        return keyword_health_sample

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
