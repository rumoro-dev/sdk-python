from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_breakdown_data_item_group_type_0 import (
        UsageBreakdownDataItemGroupType0,
    )
    from ..models.usage_breakdown_data_item_keyword_type_0 import (
        UsageBreakdownDataItemKeywordType0,
    )


T = TypeVar("T", bound="UsageBreakdownDataItem")


@_attrs_define
class UsageBreakdownDataItem:
    """
    Attributes:
        key (str): What the row stands for. A UTC day (YYYY-MM-DD) with by=day, a platform with by=platform, a keyword
            id with by=keyword and a group id with by=group.
        label (str): A name to display. The keyword's term or the group's name, or else the key.
        keyword (None | UsageBreakdownDataItemKeywordType0): Set only with by=keyword. Null otherwise.
        group (None | UsageBreakdownDataItemGroupType0): Set only with by=group. Null otherwise.
        keyword_days (int | None): Keyword-days charged in this row by the daily run. Null with by=platform, since a
            keyword-day has no platform, and for days before the first recorded run, where the count is unknown rather than
            zero. A keyword row only counts recorded days, so before window.keywordDaysFrom it is a minimum, not zero.
        keyword_cents (int): Those keyword-days priced at $5 a month (500/30 cents a day), with the total rounded once.
        matched_mentions (int): Match count for the window, relevant or not.
        billable_mentions (int): Matches billed in the window that fall in this row. Every scored match is billed,
            relevant or not.
        mention_cents (int): Those mentions priced at $0.008 each, with the total rounded once.
        total_cents (int): keywordCents plus mentionCents.
    """

    key: str
    label: str
    keyword: None | UsageBreakdownDataItemKeywordType0
    group: None | UsageBreakdownDataItemGroupType0
    keyword_days: int | None
    keyword_cents: int
    matched_mentions: int
    billable_mentions: int
    mention_cents: int
    total_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_breakdown_data_item_group_type_0 import (
            UsageBreakdownDataItemGroupType0,
        )
        from ..models.usage_breakdown_data_item_keyword_type_0 import (
            UsageBreakdownDataItemKeywordType0,
        )

        key = self.key

        label = self.label

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, UsageBreakdownDataItemKeywordType0):
            keyword = self.keyword.to_dict()
        else:
            keyword = self.keyword

        group: dict[str, Any] | None
        if isinstance(self.group, UsageBreakdownDataItemGroupType0):
            group = self.group.to_dict()
        else:
            group = self.group

        keyword_days: int | None
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        matched_mentions = self.matched_mentions

        billable_mentions = self.billable_mentions

        mention_cents = self.mention_cents

        total_cents = self.total_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "keyword": keyword,
                "group": group,
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "matchedMentions": matched_mentions,
                "billableMentions": billable_mentions,
                "mentionCents": mention_cents,
                "totalCents": total_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_breakdown_data_item_group_type_0 import (
            UsageBreakdownDataItemGroupType0,
        )
        from ..models.usage_breakdown_data_item_keyword_type_0 import (
            UsageBreakdownDataItemKeywordType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_keyword(data: object) -> None | UsageBreakdownDataItemKeywordType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = UsageBreakdownDataItemKeywordType0.from_dict(data)

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UsageBreakdownDataItemKeywordType0, data)

        keyword = _parse_keyword(d.pop("keyword"))

        def _parse_group(data: object) -> None | UsageBreakdownDataItemGroupType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_0 = UsageBreakdownDataItemGroupType0.from_dict(data)

                return group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UsageBreakdownDataItemGroupType0, data)

        group = _parse_group(d.pop("group"))

        def _parse_keyword_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        keyword_days = _parse_keyword_days(d.pop("keywordDays"))

        keyword_cents = d.pop("keywordCents")

        matched_mentions = d.pop("matchedMentions")

        billable_mentions = d.pop("billableMentions")

        mention_cents = d.pop("mentionCents")

        total_cents = d.pop("totalCents")

        usage_breakdown_data_item = cls(
            key=key,
            label=label,
            keyword=keyword,
            group=group,
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            matched_mentions=matched_mentions,
            billable_mentions=billable_mentions,
            mention_cents=mention_cents,
            total_cents=total_cents,
        )

        usage_breakdown_data_item.additional_properties = d
        return usage_breakdown_data_item

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
