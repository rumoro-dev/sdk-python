from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_health_status import KeywordHealthStatus

if TYPE_CHECKING:
    from ..models.keyword_health_ai import KeywordHealthAi
    from ..models.keyword_health_keyword import KeywordHealthKeyword
    from ..models.keyword_health_noise_authors_item import KeywordHealthNoiseAuthorsItem
    from ..models.keyword_health_noise_terms_item import KeywordHealthNoiseTermsItem
    from ..models.keyword_health_sample import KeywordHealthSample
    from ..models.keyword_health_stats import KeywordHealthStats
    from ..models.keyword_health_window import KeywordHealthWindow
    from ..models.keyword_suggestion import KeywordSuggestion


T = TypeVar("T", bound="KeywordHealth")


@_attrs_define
class KeywordHealth:
    """
    Attributes:
        keyword (KeywordHealthKeyword): The keyword this report covers.
        window (KeywordHealthWindow): The days the report covers, in UTC and by match time.
        status (KeywordHealthStatus): The first that applies wins. paused when you, the wallet or the noise brake muted
            it. capped at the monthly mention cap. noisy with 20+ scored matches in the window and under 30% relevant. new
            when under 7 days old, or changed in the last 7 days with under 20 scored matches since. quiet when 7+ days old
            with nothing relevant in the window. Otherwise healthy. After a rules, platforms or context change, or an
            unmute, inside the window, only later matches count (stats.judgedSince).
        reasons (list[str]): Plain-word explanation, status first.
        stats (KeywordHealthStats): Based on this keyword's matches in the window.
        sample (KeywordHealthSample): The posts used for noiseTerms, noiseAuthors and the effects. Only posts the
            keyword's current rules accept count, not ones an older rule let in. Review platforms match by app rather than
            text and are left out.
        noise_terms (list[KeywordHealthNoiseTermsItem]): Up to 10 words or phrases that show up far more in noise than
            in relevant posts, strongest first. Words of the keyword itself are skipped.
        noise_authors (list[KeywordHealthNoiseAuthorsItem]): Authors in the sample with no relevant post and 3 or more
            noise posts.
        suggestions (list[KeywordSuggestion]): Suggested noise fixes, each a body for PATCH /v1/keywords/{id}. The list
            is empty if no fix helps, or if fewer than 20 matches were scored after the last change. A reason explains
            which.
        ai (KeywordHealthAi): The optional part of the report written by a language model.
        generated_at (str): When the report was built. Reports are cached for 5 minutes, and changing the keyword builds
            a new one.
    """

    keyword: KeywordHealthKeyword
    window: KeywordHealthWindow
    status: KeywordHealthStatus
    reasons: list[str]
    stats: KeywordHealthStats
    sample: KeywordHealthSample
    noise_terms: list[KeywordHealthNoiseTermsItem]
    noise_authors: list[KeywordHealthNoiseAuthorsItem]
    suggestions: list[KeywordSuggestion]
    ai: KeywordHealthAi
    generated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword.to_dict()

        window = self.window.to_dict()

        status = self.status.value

        reasons = self.reasons

        stats = self.stats.to_dict()

        sample = self.sample.to_dict()

        noise_terms = []
        for noise_terms_item_data in self.noise_terms:
            noise_terms_item = noise_terms_item_data.to_dict()
            noise_terms.append(noise_terms_item)

        noise_authors = []
        for noise_authors_item_data in self.noise_authors:
            noise_authors_item = noise_authors_item_data.to_dict()
            noise_authors.append(noise_authors_item)

        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        ai = self.ai.to_dict()

        generated_at = self.generated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyword": keyword,
                "window": window,
                "status": status,
                "reasons": reasons,
                "stats": stats,
                "sample": sample,
                "noiseTerms": noise_terms,
                "noiseAuthors": noise_authors,
                "suggestions": suggestions,
                "ai": ai,
                "generatedAt": generated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_health_ai import KeywordHealthAi
        from ..models.keyword_health_keyword import (
            KeywordHealthKeyword,
        )
        from ..models.keyword_health_noise_authors_item import (
            KeywordHealthNoiseAuthorsItem,
        )
        from ..models.keyword_health_noise_terms_item import (
            KeywordHealthNoiseTermsItem,
        )
        from ..models.keyword_health_sample import KeywordHealthSample
        from ..models.keyword_health_stats import KeywordHealthStats
        from ..models.keyword_health_window import KeywordHealthWindow
        from ..models.keyword_suggestion import KeywordSuggestion

        d = dict(src_dict)
        keyword = KeywordHealthKeyword.from_dict(d.pop("keyword"))

        window = KeywordHealthWindow.from_dict(d.pop("window"))

        status = KeywordHealthStatus(d.pop("status"))

        reasons = cast(list[str], d.pop("reasons"))

        stats = KeywordHealthStats.from_dict(d.pop("stats"))

        sample = KeywordHealthSample.from_dict(d.pop("sample"))

        noise_terms = []
        _noise_terms = d.pop("noiseTerms")
        for noise_terms_item_data in _noise_terms:
            noise_terms_item = KeywordHealthNoiseTermsItem.from_dict(
                noise_terms_item_data
            )

            noise_terms.append(noise_terms_item)

        noise_authors = []
        _noise_authors = d.pop("noiseAuthors")
        for noise_authors_item_data in _noise_authors:
            noise_authors_item = KeywordHealthNoiseAuthorsItem.from_dict(
                noise_authors_item_data
            )

            noise_authors.append(noise_authors_item)

        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = KeywordSuggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        ai = KeywordHealthAi.from_dict(d.pop("ai"))

        generated_at = d.pop("generatedAt")

        keyword_health = cls(
            keyword=keyword,
            window=window,
            status=status,
            reasons=reasons,
            stats=stats,
            sample=sample,
            noise_terms=noise_terms,
            noise_authors=noise_authors,
            suggestions=suggestions,
            ai=ai,
            generated_at=generated_at,
        )

        keyword_health.additional_properties = d
        return keyword_health

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
