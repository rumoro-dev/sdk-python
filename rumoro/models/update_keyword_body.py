from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_keyword_body_kind import UpdateKeywordBodyKind
from ..models.update_keyword_body_platforms_type_0_item import (
    UpdateKeywordBodyPlatformsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_keyword_body_cap_type_0 import UpdateKeywordBodyCapType0
    from ..models.update_keyword_body_matching import UpdateKeywordBodyMatching
    from ..models.update_keyword_body_review_sources_item import (
        UpdateKeywordBodyReviewSourcesItem,
    )


T = TypeVar("T", bound="UpdateKeywordBody")


@_attrs_define
class UpdateKeywordBody:
    """Fields you leave out stay as they are.

    Attributes:
        kind (UpdateKeywordBodyKind | Unset): New kind (brand, competitor or topic).
        muted (bool | Unset): Muting stops polling and matching. Existing mentions are kept.
        platforms (list[UpdateKeywordBodyPlatformsType0Item] | None | Unset): Sets a new platform list. Null means all
            platforms. An empty list means none, which works when the keyword has reviewSources and only collects reviews.
        context (None | str | Unset): Up to 300 characters the classifier reads for this keyword only, in addition to
            the company profile or the group's description. Say what the term means for you and what to ignore, for example
            "Driftwood is our deploy tool, not beach wood." Null clears it.
        matching (UpdateKeywordBodyMatching | Unset): Fields you leave out stay as they are. An empty list clears a
            field.
        cap (None | Unset | UpdateKeywordBodyCapType0): Sets a new monthly mention cap, or null for no cap. A cap above
            this month's count resumes a capped keyword right away. A cap at or below the count pauses it.
        group_id (str | Unset): Target group (grp_...). 409 if it already has this term.
        review_sources (list[UpdateKeywordBodyReviewSourcesItem] | Unset): Sets a new list of review pages for this
            keyword. An empty list disconnects them all, and their reviews are kept. A page or country you add gets the free
            30-day look-back. Pages already listed are unchanged.
    """

    kind: UpdateKeywordBodyKind | Unset = UNSET
    muted: bool | Unset = UNSET
    platforms: list[UpdateKeywordBodyPlatformsType0Item] | None | Unset = UNSET
    context: None | str | Unset = UNSET
    matching: UpdateKeywordBodyMatching | Unset = UNSET
    cap: None | Unset | UpdateKeywordBodyCapType0 = UNSET
    group_id: str | Unset = UNSET
    review_sources: list[UpdateKeywordBodyReviewSourcesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_keyword_body_cap_type_0 import (
            UpdateKeywordBodyCapType0,
        )

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        muted = self.muted

        platforms: list[str] | None | Unset
        if isinstance(self.platforms, Unset):
            platforms = UNSET
        elif isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        matching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching, Unset):
            matching = self.matching.to_dict()

        cap: dict[str, Any] | None | Unset
        if isinstance(self.cap, Unset):
            cap = UNSET
        elif isinstance(self.cap, UpdateKeywordBodyCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        group_id = self.group_id

        review_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.review_sources, Unset):
            review_sources = []
            for review_sources_item_data in self.review_sources:
                review_sources_item = review_sources_item_data.to_dict()
                review_sources.append(review_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if muted is not UNSET:
            field_dict["muted"] = muted
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if context is not UNSET:
            field_dict["context"] = context
        if matching is not UNSET:
            field_dict["matching"] = matching
        if cap is not UNSET:
            field_dict["cap"] = cap
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if review_sources is not UNSET:
            field_dict["reviewSources"] = review_sources

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_keyword_body_cap_type_0 import (
            UpdateKeywordBodyCapType0,
        )
        from ..models.update_keyword_body_matching import (
            UpdateKeywordBodyMatching,
        )
        from ..models.update_keyword_body_review_sources_item import (
            UpdateKeywordBodyReviewSourcesItem,
        )

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: UpdateKeywordBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = UpdateKeywordBodyKind(_kind)

        muted = d.pop("muted", UNSET)

        def _parse_platforms(
            data: object,
        ) -> list[UpdateKeywordBodyPlatformsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = UpdateKeywordBodyPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateKeywordBodyPlatformsType0Item] | None | Unset, data)

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _matching = d.pop("matching", UNSET)
        matching: UpdateKeywordBodyMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = UpdateKeywordBodyMatching.from_dict(_matching)

        def _parse_cap(data: object) -> None | Unset | UpdateKeywordBodyCapType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = UpdateKeywordBodyCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateKeywordBodyCapType0, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        group_id = d.pop("groupId", UNSET)

        _review_sources = d.pop("reviewSources", UNSET)
        review_sources: list[UpdateKeywordBodyReviewSourcesItem] | Unset = UNSET
        if _review_sources is not UNSET:
            review_sources = []
            for review_sources_item_data in _review_sources:
                review_sources_item = UpdateKeywordBodyReviewSourcesItem.from_dict(
                    review_sources_item_data
                )

                review_sources.append(review_sources_item)

        update_keyword_body = cls(
            kind=kind,
            muted=muted,
            platforms=platforms,
            context=context,
            matching=matching,
            cap=cap,
            group_id=group_id,
            review_sources=review_sources,
        )

        update_keyword_body.additional_properties = d
        return update_keyword_body

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
