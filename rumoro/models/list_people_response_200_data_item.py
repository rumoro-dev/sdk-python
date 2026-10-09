from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_people_response_200_data_item_platform import (
    ListPeopleResponse200DataItemPlatform,
)

if TYPE_CHECKING:
    from ..models.list_people_response_200_data_item_accounts_item import (
        ListPeopleResponse200DataItemAccountsItem,
    )
    from ..models.list_people_response_200_data_item_annotations import (
        ListPeopleResponse200DataItemAnnotations,
    )
    from ..models.list_people_response_200_data_item_outreach import (
        ListPeopleResponse200DataItemOutreach,
    )
    from ..models.list_people_response_200_data_item_profile_type_0 import (
        ListPeopleResponse200DataItemProfileType0,
    )
    from ..models.list_people_response_200_data_item_reach import (
        ListPeopleResponse200DataItemReach,
    )
    from ..models.list_people_response_200_data_item_stats import (
        ListPeopleResponse200DataItemStats,
    )


T = TypeVar("T", bound="ListPeopleResponse200DataItem")


@_attrs_define
class ListPeopleResponse200DataItem:
    """
    Attributes:
        id (str): The person's id (aut_...), which is the id of their main account. An account merged into a person
            leads to that person.
        platform (ListPeopleResponse200DataItemPlatform): The main account's platform. See `accounts` for all of them.
        name (None | str): The name shown on their latest post. Null if the platform has none.
        handle (None | str): The main account's handle, written the platform's way.
        url (None | str): Link to the main account's profile.
        avatar_url (None | str):
        accounts (list[ListPeopleResponse200DataItemAccountsItem]): All accounts this workspace counts as this person,
            starting with the main one.
        reach (ListPeopleResponse200DataItemReach): Counts from the platform, taken from their latest post. Null where a
            platform lacks the number.
        profile (ListPeopleResponse200DataItemProfileType0 | None): Details from the public profile. Null until the
            profile is fetched.
        stats (ListPeopleResponse200DataItemStats): Counted from this workspace's matches only.
        annotations (ListPeopleResponse200DataItemAnnotations): Notes and tags your workspace added to the person.
        outreach (ListPeopleResponse200DataItemOutreach): Your outreach to this person. Logging the first activity makes
            the member who reached out the owner, if there was none, and moves not_contacted to contacted.
    """

    id: str
    platform: ListPeopleResponse200DataItemPlatform
    name: None | str
    handle: None | str
    url: None | str
    avatar_url: None | str
    accounts: list[ListPeopleResponse200DataItemAccountsItem]
    reach: ListPeopleResponse200DataItemReach
    profile: ListPeopleResponse200DataItemProfileType0 | None
    stats: ListPeopleResponse200DataItemStats
    annotations: ListPeopleResponse200DataItemAnnotations
    outreach: ListPeopleResponse200DataItemOutreach
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_people_response_200_data_item_profile_type_0 import (
            ListPeopleResponse200DataItemProfileType0,
        )

        id = self.id

        platform = self.platform.value

        name: None | str
        name = self.name

        handle: None | str
        handle = self.handle

        url: None | str
        url = self.url

        avatar_url: None | str
        avatar_url = self.avatar_url

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        reach = self.reach.to_dict()

        profile: dict[str, Any] | None
        if isinstance(self.profile, ListPeopleResponse200DataItemProfileType0):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        stats = self.stats.to_dict()

        annotations = self.annotations.to_dict()

        outreach = self.outreach.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "name": name,
                "handle": handle,
                "url": url,
                "avatarUrl": avatar_url,
                "accounts": accounts,
                "reach": reach,
                "profile": profile,
                "stats": stats,
                "annotations": annotations,
                "outreach": outreach,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_people_response_200_data_item_accounts_item import (
            ListPeopleResponse200DataItemAccountsItem,
        )
        from ..models.list_people_response_200_data_item_annotations import (
            ListPeopleResponse200DataItemAnnotations,
        )
        from ..models.list_people_response_200_data_item_outreach import (
            ListPeopleResponse200DataItemOutreach,
        )
        from ..models.list_people_response_200_data_item_profile_type_0 import (
            ListPeopleResponse200DataItemProfileType0,
        )
        from ..models.list_people_response_200_data_item_reach import (
            ListPeopleResponse200DataItemReach,
        )
        from ..models.list_people_response_200_data_item_stats import (
            ListPeopleResponse200DataItemStats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        platform = ListPeopleResponse200DataItemPlatform(d.pop("platform"))

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

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = ListPeopleResponse200DataItemAccountsItem.from_dict(
                accounts_item_data
            )

            accounts.append(accounts_item)

        reach = ListPeopleResponse200DataItemReach.from_dict(d.pop("reach"))

        def _parse_profile(
            data: object,
        ) -> ListPeopleResponse200DataItemProfileType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_0 = ListPeopleResponse200DataItemProfileType0.from_dict(
                    data
                )

                return profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPeopleResponse200DataItemProfileType0 | None, data)

        profile = _parse_profile(d.pop("profile"))

        stats = ListPeopleResponse200DataItemStats.from_dict(d.pop("stats"))

        annotations = ListPeopleResponse200DataItemAnnotations.from_dict(
            d.pop("annotations")
        )

        outreach = ListPeopleResponse200DataItemOutreach.from_dict(d.pop("outreach"))

        list_people_response_200_data_item = cls(
            id=id,
            platform=platform,
            name=name,
            handle=handle,
            url=url,
            avatar_url=avatar_url,
            accounts=accounts,
            reach=reach,
            profile=profile,
            stats=stats,
            annotations=annotations,
            outreach=outreach,
        )

        list_people_response_200_data_item.additional_properties = d
        return list_people_response_200_data_item

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
