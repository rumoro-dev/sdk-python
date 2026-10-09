from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGroupBody")


@_attrs_define
class CreateGroupBody:
    """
    Attributes:
        name (str): The group's name, such as a client, campaign or product. Must be unique in the workspace.
        external_id (None | str | Unset): An id from your own system, such as a client id. Must be unique in the
            workspace. Find the group with GET /v1/groups?externalId=.
        context (None | str | Unset): Up to 4000 characters the classifier treats as "the company" for this group's
            keywords. It fully replaces the workspace profile, including its relevance guidelines and competitors. Describe
            the business, what it sells and to whom, what it is not, and any rule for this group, such as "ignore job
            posts". With one group per client, use the client's description. Null means the workspace profile is used.
    """

    name: str
    external_id: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        create_group_body = cls(
            name=name,
            external_id=external_id,
            context=context,
        )

        create_group_body.additional_properties = d
        return create_group_body

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
