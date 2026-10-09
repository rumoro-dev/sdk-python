from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageSummaryKeywords")


@_attrs_define
class UsageSummaryKeywords:
    """Keyword counts compared with the balance.

    Attributes:
        active (int): Keywords that are not muted. These are charged each day.
        paused (int): Keywords paused because the balance ran out. A top-up resumes them.
        capped (int): Keywords that are not muted but reached their monthly mention cap. They are still charged each day
            and are not matched until the next month or until the cap is raised.
        limit (int): Keywords the workspace may run now. 0 if the balance can't cover one more keyword-day, otherwise
            the self-serve maximum.
        day_cents (int): Daily cost of the active keywords.
    """

    active: int
    paused: int
    capped: int
    limit: int
    day_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        paused = self.paused

        capped = self.capped

        limit = self.limit

        day_cents = self.day_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "paused": paused,
                "capped": capped,
                "limit": limit,
                "dayCents": day_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active")

        paused = d.pop("paused")

        capped = d.pop("capped")

        limit = d.pop("limit")

        day_cents = d.pop("dayCents")

        usage_summary_keywords = cls(
            active=active,
            paused=paused,
            capped=capped,
            limit=limit,
            day_cents=day_cents,
        )

        usage_summary_keywords.additional_properties = d
        return usage_summary_keywords

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
