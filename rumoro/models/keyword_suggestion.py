from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_source import KeywordSuggestionSource
from ..models.keyword_suggestion_type import KeywordSuggestionType

if TYPE_CHECKING:
    from ..models.keyword_suggestion_effect_type_0 import KeywordSuggestionEffectType0
    from ..models.keyword_suggestion_patch import KeywordSuggestionPatch


T = TypeVar("T", bound="KeywordSuggestion")


@_attrs_define
class KeywordSuggestion:
    """
    Attributes:
        type_ (KeywordSuggestionType): What the suggestion changes. The excluded_* types add to the matching rules,
            required_terms swaps the required list, platforms drops the platforms that bring nearly only noise, and context
            rewrites the classifier's sentence.
        values (list[str]): The terms or authors to add, the platforms to remove, or the new context.
        why (str): Why, and what the change would have done, in plain words.
        patch (KeywordSuggestionPatch): Send this body unchanged to PATCH /v1/keywords/{id} to apply the suggestion.
            Lists hold the full new list, with the current entries included.
        effect (KeywordSuggestionEffectType0 | None): The result of replaying the change on the window's matches with
            the matcher's rules. Null for context suggestions, which alter scores rather than matches.
        source (KeywordSuggestionSource): rules means it was computed from the posts in the window. ai means a language
            model wrote it (with ai=true).
    """

    type_: KeywordSuggestionType
    values: list[str]
    why: str
    patch: KeywordSuggestionPatch
    effect: KeywordSuggestionEffectType0 | None
    source: KeywordSuggestionSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_suggestion_effect_type_0 import (
            KeywordSuggestionEffectType0,
        )

        type_ = self.type_.value

        values = self.values

        why = self.why

        patch = self.patch.to_dict()

        effect: dict[str, Any] | None
        if isinstance(self.effect, KeywordSuggestionEffectType0):
            effect = self.effect.to_dict()
        else:
            effect = self.effect

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "values": values,
                "why": why,
                "patch": patch,
                "effect": effect,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_suggestion_effect_type_0 import (
            KeywordSuggestionEffectType0,
        )
        from ..models.keyword_suggestion_patch import (
            KeywordSuggestionPatch,
        )

        d = dict(src_dict)
        type_ = KeywordSuggestionType(d.pop("type"))

        values = cast(list[str], d.pop("values"))

        why = d.pop("why")

        patch = KeywordSuggestionPatch.from_dict(d.pop("patch"))

        def _parse_effect(data: object) -> KeywordSuggestionEffectType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effect_type_0 = KeywordSuggestionEffectType0.from_dict(data)

                return effect_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordSuggestionEffectType0 | None, data)

        effect = _parse_effect(d.pop("effect"))

        source = KeywordSuggestionSource(d.pop("source"))

        keyword_suggestion = cls(
            type_=type_,
            values=values,
            why=why,
            patch=patch,
            effect=effect,
            source=source,
        )

        keyword_suggestion.additional_properties = d
        return keyword_suggestion

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
