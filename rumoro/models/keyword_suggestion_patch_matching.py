from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_matching_required_mode import (
    KeywordSuggestionPatchMatchingRequiredMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchMatching")


@_attrs_define
class KeywordSuggestionPatchMatching:
    """Fields you leave out stay as they are. An empty list clears a field.

    Attributes:
        required_terms (list[str] | Unset): Terms the post must contain as well. requiredMode says whether one or all of
            them must appear. An empty list sets no requirement.
        required_mode (KeywordSuggestionPatchMatchingRequiredMode | Unset): any needs one of the required terms in the
            post. all needs every one.
        excluded_terms (list[str] | Unset): Posts that contain one of these terms are dropped. Put `*` at the start or
            end of a term as a wildcard, so deploy* matches deployment and *bot matches nightlybot.
        excluded_authors (list[str] | Unset): Authors whose posts this keyword ignores. Each entry is a profile or post
            link, @handle, u/name, Bluesky DID or display name. Entries are normalized the same way as an alert's muted
            authors.
        case_sensitive (bool | Unset): When true, the term only matches in the exact case you typed, so RAG never
            matches rag. Defaults to false.
    """

    required_terms: list[str] | Unset = UNSET
    required_mode: KeywordSuggestionPatchMatchingRequiredMode | Unset = UNSET
    excluded_terms: list[str] | Unset = UNSET
    excluded_authors: list[str] | Unset = UNSET
    case_sensitive: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_terms: list[str] | Unset = UNSET
        if not isinstance(self.required_terms, Unset):
            required_terms = self.required_terms

        required_mode: str | Unset = UNSET
        if not isinstance(self.required_mode, Unset):
            required_mode = self.required_mode.value

        excluded_terms: list[str] | Unset = UNSET
        if not isinstance(self.excluded_terms, Unset):
            excluded_terms = self.excluded_terms

        excluded_authors: list[str] | Unset = UNSET
        if not isinstance(self.excluded_authors, Unset):
            excluded_authors = self.excluded_authors

        case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_terms is not UNSET:
            field_dict["requiredTerms"] = required_terms
        if required_mode is not UNSET:
            field_dict["requiredMode"] = required_mode
        if excluded_terms is not UNSET:
            field_dict["excludedTerms"] = excluded_terms
        if excluded_authors is not UNSET:
            field_dict["excludedAuthors"] = excluded_authors
        if case_sensitive is not UNSET:
            field_dict["caseSensitive"] = case_sensitive

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms", UNSET))

        _required_mode = d.pop("requiredMode", UNSET)
        required_mode: KeywordSuggestionPatchMatchingRequiredMode | Unset
        if isinstance(_required_mode, Unset):
            required_mode = UNSET
        else:
            required_mode = KeywordSuggestionPatchMatchingRequiredMode(_required_mode)

        excluded_terms = cast(list[str], d.pop("excludedTerms", UNSET))

        excluded_authors = cast(list[str], d.pop("excludedAuthors", UNSET))

        case_sensitive = d.pop("caseSensitive", UNSET)

        keyword_suggestion_patch_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            case_sensitive=case_sensitive,
        )

        keyword_suggestion_patch_matching.additional_properties = d
        return keyword_suggestion_patch_matching

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
