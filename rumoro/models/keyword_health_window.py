from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthWindow")


@_attrs_define
class KeywordHealthWindow:
    """The days the report covers, in UTC and by match time.

    Attributes:
        from_ (str): Start date (UTC, YYYY-MM-DD), included.
        to (str): The last day included, which is today.
        days (int): How many days the window spans.
    """

    from_: str
    to: str
    days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        days = self.days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        days = d.pop("days")

        keyword_health_window = cls(
            from_=from_,
            to=to,
            days=days,
        )

        keyword_health_window.additional_properties = d
        return keyword_health_window

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
