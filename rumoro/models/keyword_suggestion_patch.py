from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_kind import KeywordSuggestionPatchKind
from ..models.keyword_suggestion_patch_platforms_type_0_item import (
    KeywordSuggestionPatchPlatformsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_suggestion_patch_cap_type_0 import (
        KeywordSuggestionPatchCapType0,
    )
    from ..models.keyword_suggestion_patch_matching import (
        KeywordSuggestionPatchMatching,
    )
    from ..models.keyword_suggestion_patch_review_sources_item import (
        KeywordSuggestionPatchReviewSourcesItem,
    )


T = TypeVar("T", bound="KeywordSuggestionPatch")


@_attrs_define
class KeywordSuggestionPatch:
    """Send this body unchanged to PATCH /v1/keywords/{id} to apply the suggestion. Lists hold the full new list, with the
    current entries included.

        Attributes:
            kind (KeywordSuggestionPatchKind | Unset): New kind (brand, competitor or topic).
            muted (bool | Unset): Muting stops polling and matching. Existing mentions are kept.
            platforms (list[KeywordSuggestionPatchPlatformsType0Item] | None | Unset): Sets a new platform list. Null means
                all platforms. An empty list means none, which works when the keyword has reviewSources and only collects
                reviews.
            context (None | str | Unset): Up to 300 characters the classifier reads for this keyword only, in addition to
                the company profile or the group's description. Say what the term means for you and what to ignore, for example
                "Driftwood is our deploy tool, not beach wood." Null clears it.
            matching (KeywordSuggestionPatchMatching | Unset): Fields you leave out stay as they are. An empty list clears a
                field.
            cap (KeywordSuggestionPatchCapType0 | None | Unset): Sets a new monthly mention cap, or null for no cap. A cap
                above this month's count resumes a capped keyword right away. A cap at or below the count pauses it.
            group_id (str | Unset): Target group (grp_...). 409 if it already has this term.
            review_sources (list[KeywordSuggestionPatchReviewSourcesItem] | Unset): Sets a new list of review pages for this
                keyword. An empty list disconnects them all, and their reviews are kept. A page or country you add gets the free
                30-day look-back. Pages already listed are unchanged.
    """

    kind: KeywordSuggestionPatchKind | Unset = UNSET
    muted: bool | Unset = UNSET
    platforms: list[KeywordSuggestionPatchPlatformsType0Item] | None | Unset = UNSET
    context: None | str | Unset = UNSET
    matching: KeywordSuggestionPatchMatching | Unset = UNSET
    cap: KeywordSuggestionPatchCapType0 | None | Unset = UNSET
    group_id: str | Unset = UNSET
    review_sources: list[KeywordSuggestionPatchReviewSourcesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_suggestion_patch_cap_type_0 import (
            KeywordSuggestionPatchCapType0,
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
        elif isinstance(self.cap, KeywordSuggestionPatchCapType0):
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
        from ..models.keyword_suggestion_patch_cap_type_0 import (
            KeywordSuggestionPatchCapType0,
        )
        from ..models.keyword_suggestion_patch_matching import (
            KeywordSuggestionPatchMatching,
        )
        from ..models.keyword_suggestion_patch_review_sources_item import (
            KeywordSuggestionPatchReviewSourcesItem,
        )

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: KeywordSuggestionPatchKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = KeywordSuggestionPatchKind(_kind)

        muted = d.pop("muted", UNSET)

        def _parse_platforms(
            data: object,
        ) -> list[KeywordSuggestionPatchPlatformsType0Item] | None | Unset:
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
                    platforms_type_0_item = KeywordSuggestionPatchPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[KeywordSuggestionPatchPlatformsType0Item] | None | Unset, data
            )

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _matching = d.pop("matching", UNSET)
        matching: KeywordSuggestionPatchMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = KeywordSuggestionPatchMatching.from_dict(_matching)

        def _parse_cap(data: object) -> KeywordSuggestionPatchCapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = KeywordSuggestionPatchCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordSuggestionPatchCapType0 | None | Unset, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        group_id = d.pop("groupId", UNSET)

        _review_sources = d.pop("reviewSources", UNSET)
        review_sources: list[KeywordSuggestionPatchReviewSourcesItem] | Unset = UNSET
        if _review_sources is not UNSET:
            review_sources = []
            for review_sources_item_data in _review_sources:
                review_sources_item = KeywordSuggestionPatchReviewSourcesItem.from_dict(
                    review_sources_item_data
                )

                review_sources.append(review_sources_item)

        keyword_suggestion_patch = cls(
            kind=kind,
            muted=muted,
            platforms=platforms,
            context=context,
            matching=matching,
            cap=cap,
            group_id=group_id,
            review_sources=review_sources,
        )

        keyword_suggestion_patch.additional_properties = d
        return keyword_suggestion_patch

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
