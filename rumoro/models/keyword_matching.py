from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_matching_required_mode import KeywordMatchingRequiredMode

T = TypeVar("T", bound="KeywordMatching")


@_attrs_define
class KeywordMatching:
    """Rules a post must pass before it is stored as a mention. A post they reject is never billed.

    Attributes:
        required_terms (list[str]): Terms the post must contain as well. requiredMode says whether one or all of them
            must appear. An empty list sets no requirement.
        required_mode (KeywordMatchingRequiredMode): any needs one of the required terms in the post. all needs every
            one.
        excluded_terms (list[str]): Posts that contain one of these terms are dropped. Put `*` at the start or end of a
            term as a wildcard, so deploy* matches deployment and *bot matches nightlybot.
        excluded_authors (list[str]): Authors whose posts this keyword ignores. Each entry is a profile or post link,
            @handle, u/name, Bluesky DID or display name. Entries are normalized the same way as an alert's muted authors.
        case_sensitive (bool): When true, the term only matches in the exact case you typed, so RAG never matches rag.
            Defaults to false.
    """

    required_terms: list[str]
    required_mode: KeywordMatchingRequiredMode
    excluded_terms: list[str]
    excluded_authors: list[str]
    case_sensitive: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_terms = self.required_terms

        required_mode = self.required_mode.value

        excluded_terms = self.excluded_terms

        excluded_authors = self.excluded_authors

        case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requiredTerms": required_terms,
                "requiredMode": required_mode,
                "excludedTerms": excluded_terms,
                "excludedAuthors": excluded_authors,
                "caseSensitive": case_sensitive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms"))

        required_mode = KeywordMatchingRequiredMode(d.pop("requiredMode"))

        excluded_terms = cast(list[str], d.pop("excludedTerms"))

        excluded_authors = cast(list[str], d.pop("excludedAuthors"))

        case_sensitive = d.pop("caseSensitive")

        keyword_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            case_sensitive=case_sensitive,
        )

        keyword_matching.additional_properties = d
        return keyword_matching

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
