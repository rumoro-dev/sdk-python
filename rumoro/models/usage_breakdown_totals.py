from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdownTotals")


@_attrs_define
class UsageBreakdownTotals:
    """Totals for the whole window. They are the same whatever `by` is.

    Attributes:
        keyword_days (int): Sum of keyword-days over the window.
        keyword_cents (int): Those keyword-days priced at $5 a month (500/30 cents a day), with the total rounded once.
        matched_mentions (int): Match count for the window, relevant or not.
        billable_mentions (int): Matches billed in the window that fall in this row. Every scored match is billed,
            relevant or not.
        mention_cents (int): Those mentions priced at $0.008 each, with the total rounded once.
        total_cents (int): keywordCents plus mentionCents.
        unclassified_mentions (int): Matches whose classification failed. They are never charged.
        ledger_debit_cents (int): Debits recorded so far for the window's days, each on its settlement day. Mentions
            settle the next morning, so a window ending today trails totalCents by today's mentions, plus yesterday's before
            the 00:05 UTC run. A closed month differs only by cumulative rounding.
        unattributed_billable (int): Billed mentions whose match was removed with a deleted keyword, so they belong to
            no platform or keyword row. They were still charged.
    """

    keyword_days: int
    keyword_cents: int
    matched_mentions: int
    billable_mentions: int
    mention_cents: int
    total_cents: int
    unclassified_mentions: int
    ledger_debit_cents: int
    unattributed_billable: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        matched_mentions = self.matched_mentions

        billable_mentions = self.billable_mentions

        mention_cents = self.mention_cents

        total_cents = self.total_cents

        unclassified_mentions = self.unclassified_mentions

        ledger_debit_cents = self.ledger_debit_cents

        unattributed_billable = self.unattributed_billable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "matchedMentions": matched_mentions,
                "billableMentions": billable_mentions,
                "mentionCents": mention_cents,
                "totalCents": total_cents,
                "unclassifiedMentions": unclassified_mentions,
                "ledgerDebitCents": ledger_debit_cents,
                "unattributedBillable": unattributed_billable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_days = d.pop("keywordDays")

        keyword_cents = d.pop("keywordCents")

        matched_mentions = d.pop("matchedMentions")

        billable_mentions = d.pop("billableMentions")

        mention_cents = d.pop("mentionCents")

        total_cents = d.pop("totalCents")

        unclassified_mentions = d.pop("unclassifiedMentions")

        ledger_debit_cents = d.pop("ledgerDebitCents")

        unattributed_billable = d.pop("unattributedBillable")

        usage_breakdown_totals = cls(
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            matched_mentions=matched_mentions,
            billable_mentions=billable_mentions,
            mention_cents=mention_cents,
            total_cents=total_cents,
            unclassified_mentions=unclassified_mentions,
            ledger_debit_cents=ledger_debit_cents,
            unattributed_billable=unattributed_billable,
        )

        usage_breakdown_totals.additional_properties = d
        return usage_breakdown_totals

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
