from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_outreach_stage import PersonOutreachStage

if TYPE_CHECKING:
    from ..models.person_outreach_owner_type_0 import PersonOutreachOwnerType0


T = TypeVar("T", bound="PersonOutreach")


@_attrs_define
class PersonOutreach:
    """Your outreach to this person. Logging the first activity makes the member who reached out the owner, if there was
    none, and moves not_contacted to contacted.

        Attributes:
            owner (None | PersonOutreachOwnerType0): The teammate responsible for this contact. Null when no one is, or when
                that member has left the workspace.
            stage (PersonOutreachStage): The outreach stage your team has reached with this person.
            last_contacted_at (None | str): Time of the latest logged activity. Null when no contact was logged.
    """

    owner: None | PersonOutreachOwnerType0
    stage: PersonOutreachStage
    last_contacted_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.person_outreach_owner_type_0 import (
            PersonOutreachOwnerType0,
        )

        owner: dict[str, Any] | None
        if isinstance(self.owner, PersonOutreachOwnerType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        stage = self.stage.value

        last_contacted_at: None | str
        last_contacted_at = self.last_contacted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "stage": stage,
                "lastContactedAt": last_contacted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.person_outreach_owner_type_0 import (
            PersonOutreachOwnerType0,
        )

        d = dict(src_dict)

        def _parse_owner(data: object) -> None | PersonOutreachOwnerType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_type_0 = PersonOutreachOwnerType0.from_dict(data)

                return owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonOutreachOwnerType0, data)

        owner = _parse_owner(d.pop("owner"))

        stage = PersonOutreachStage(d.pop("stage"))

        def _parse_last_contacted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_contacted_at = _parse_last_contacted_at(d.pop("lastContactedAt"))

        person_outreach = cls(
            owner=owner,
            stage=stage,
            last_contacted_at=last_contacted_at,
        )

        person_outreach.additional_properties = d
        return person_outreach

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
