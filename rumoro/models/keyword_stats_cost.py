from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordStatsCost")


@_attrs_define
class KeywordStatsCost:
    """List-price cost this calendar month (UTC), equal to this keyword's row in GET /v1/usage/breakdown?month=<this
    month>. The ledger settles daily and can differ only by cumulative rounding.

        Attributes:
            keyword_days (int): Charged days this month. A day is charged when the keyword is unmuted at the daily run, so a
                new keyword shows 0 until tomorrow.
            keyword_cents (int): keywordDays at 500/30 cents each, which is $5 a month. Only the total is rounded.
            billable_mentions (int): Matches billed this month. A match counts when it is scored, which is the time the
                ledger settles by. So this can lag behind thisMonth while matches are still being scored, and a match that
                failed to score never counts.
            mention_cents (int): Those matches priced at $0.008 each, with the total rounded once.
            total_cents (int): keywordCents plus mentionCents. The keyword's cost this month in US cents.
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

        keyword_stats_cost = cls(
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            billable_mentions=billable_mentions,
            mention_cents=mention_cents,
            total_cents=total_cents,
        )

        keyword_stats_cost.additional_properties = d
        return keyword_stats_cost

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
