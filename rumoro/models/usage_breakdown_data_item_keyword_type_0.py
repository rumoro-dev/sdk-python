from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdownDataItemKeywordType0")


@_attrs_define
class UsageBreakdownDataItemKeywordType0:
    """Set only with by=keyword. Null otherwise.

    Attributes:
        id (str): The keyword's id (kw_...). Deleted keywords keep their id here.
        term (str): The term when it was last charged, or its current term.
        removed (bool): The keyword was deleted later. Charges remain, but its mentions are gone, so mention counts are
            0.
    """

    id: str
    term: str
    removed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        removed = d.pop("removed")

        usage_breakdown_data_item_keyword_type_0 = cls(
            id=id,
            term=term,
            removed=removed,
        )

        usage_breakdown_data_item_keyword_type_0.additional_properties = d
        return usage_breakdown_data_item_keyword_type_0

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
