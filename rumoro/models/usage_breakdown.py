from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_breakdown_by import UsageBreakdownBy
from ..models.usage_breakdown_currency import UsageBreakdownCurrency

if TYPE_CHECKING:
    from ..models.usage_breakdown_data_item import UsageBreakdownDataItem
    from ..models.usage_breakdown_totals import UsageBreakdownTotals
    from ..models.usage_breakdown_window import UsageBreakdownWindow


T = TypeVar("T", bound="UsageBreakdown")


@_attrs_define
class UsageBreakdown:
    """
    Attributes:
        window (UsageBreakdownWindow): Report range in UTC days.
        by (UsageBreakdownBy): Grouping used for the rows.
        currency (UsageBreakdownCurrency): All amounts are in US cents.
        totals (UsageBreakdownTotals): Totals for the whole window. They are the same whatever `by` is.
        data (list[UsageBreakdownDataItem]): With by=day the rows are in date order. With by=platform and by=keyword the
            most expensive come first, then those with the most matches, deleted keywords included.
        total (int): The number of rows before `limit` and `offset` are applied.
    """

    window: UsageBreakdownWindow
    by: UsageBreakdownBy
    currency: UsageBreakdownCurrency
    totals: UsageBreakdownTotals
    data: list[UsageBreakdownDataItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window = self.window.to_dict()

        by = self.by.value

        currency = self.currency.value

        totals = self.totals.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "by": by,
                "currency": currency,
                "totals": totals,
                "data": data,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_breakdown_data_item import (
            UsageBreakdownDataItem,
        )
        from ..models.usage_breakdown_totals import (
            UsageBreakdownTotals,
        )
        from ..models.usage_breakdown_window import (
            UsageBreakdownWindow,
        )

        d = dict(src_dict)
        window = UsageBreakdownWindow.from_dict(d.pop("window"))

        by = UsageBreakdownBy(d.pop("by"))

        currency = UsageBreakdownCurrency(d.pop("currency"))

        totals = UsageBreakdownTotals.from_dict(d.pop("totals"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = UsageBreakdownDataItem.from_dict(data_item_data)

            data.append(data_item)

        total = d.pop("total")

        usage_breakdown = cls(
            window=window,
            by=by,
            currency=currency,
            totals=totals,
            data=data,
            total=total,
        )

        usage_breakdown.additional_properties = d
        return usage_breakdown

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
