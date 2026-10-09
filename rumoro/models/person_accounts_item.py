from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_accounts_item_platform import PersonAccountsItemPlatform

T = TypeVar("T", bound="PersonAccountsItem")


@_attrs_define
class PersonAccountsItem:
    """
    Attributes:
        id (str): The account's id (aut_...). The main account's id is the person's id.
        platform (PersonAccountsItemPlatform): The platform. Review platforms are appstore, googleplay, trustpilot and
            googlemaps (a place's Google reviews).
        name (None | str): The name shown on the platform.
        handle (None | str): The handle taken from the profile link, written the platform's way.
        url (None | str): Link to the profile.
    """

    id: str
    platform: PersonAccountsItemPlatform
    name: None | str
    handle: None | str
    url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform = self.platform.value

        name: None | str
        name = self.name

        handle: None | str
        handle = self.handle

        url: None | str
        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "name": name,
                "handle": handle,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        platform = PersonAccountsItemPlatform(d.pop("platform"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        handle = _parse_handle(d.pop("handle"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        person_accounts_item = cls(
            id=id,
            platform=platform,
            name=name,
            handle=handle,
            url=url,
        )

        person_accounts_item.additional_properties = d
        return person_accounts_item

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
