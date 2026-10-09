from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthStatsCost")


@_attrs_define
class KeywordHealthStatsCost:
    """List-price cost of this keyword in the window.

    Attributes:
        keyword_days (int): Charged days in the window.
        keyword_cents (int): What keywordDays cost at the keyword rate.
        billable_mentions (int): Billed matches in the window, dated by scoring time.
        mention_cents (int): What billableMentions cost at the mention rate.
        total_cents (int): keywordCents plus mentionCents, equal to this keyword's GET /v1/usage/breakdown row for that
            range.
    """

    keyword_days: int
    keyword_cents: int
    billable_mentions: int
    mention_cents: int
    total_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        billable_mentions = self.billable_mentions

        mention_cents = self.mention_cents

        total_cents = self.total_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "billableMentions": billable_mentions,
                "mentionCents": mention_cents,
                "totalCents": total_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_days = d.pop("keywordDays")

        keyword_cents = d.pop("keywordCents")

        billable_mentions = d.pop("billableMentions")

        mention_cents = d.pop("mentionCents")

        total_cents = d.pop("totalCents")

        keyword_health_stats_cost = cls(
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            billable_mentions=billable_mentions,
            mention_cents=mention_cents,
            total_cents=total_cents,
        )

        keyword_health_stats_cost.additional_properties = d
        return keyword_health_stats_cost

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
