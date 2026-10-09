from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdownDataItemGroupType0")


@_attrs_define
class UsageBreakdownDataItemGroupType0:
    """Set only with by=group. Null otherwise.

    Attributes:
        id (str): The group's id. It is "none" for keyword-days charged before groups existed when the keyword has since
            been deleted.
        name (str): Current group name, or "Deleted group" or "No group".
        removed (bool): True when the group was deleted later.
    """

    id: str
    name: str
    removed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        removed = d.pop("removed")

        usage_breakdown_data_item_group_type_0 = cls(
            id=id,
            name=name,
            removed=removed,
        )

        usage_breakdown_data_item_group_type_0.additional_properties = d
        return usage_breakdown_data_item_group_type_0

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
