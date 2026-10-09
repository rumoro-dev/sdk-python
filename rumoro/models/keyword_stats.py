from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_stats_health import KeywordStatsHealth

if TYPE_CHECKING:
    from ..models.keyword_stats_cost import KeywordStatsCost
    from ..models.keyword_stats_feedback import KeywordStatsFeedback
    from ..models.keyword_stats_noise import KeywordStatsNoise


T = TypeVar("T", bound="KeywordStats")


@_attrs_define
class KeywordStats:
    """Counted from this workspace's matches only.

    Attributes:
        mentions (int): All matches so far, relevant or not. Billing counts this number.
        relevant (int): Matches whose relevance score reached the threshold.
        last7d (int): Matches with a post date in the past 7 days.
        this_month (int): Matches recorded in the current calendar month (UTC). The cap is checked against this count.
        last_mention_at (None | str): Time of the latest matched post. Null before the first match.
        feedback (KeywordStatsFeedback): Your team's relevance marks, set with PATCH /v1/mentions/{id}.
        noise (KeywordStatsNoise): Relevance of the scored matches from the past 14 days. A keyword you narrow today
            drops the flag within two weeks.
        health (KeywordStatsHealth): Health over the 14 days `noise` covers, by the same rule as GET
            /v1/keywords/{id}/health. The first that applies wins. paused (muted), capped (at its cap), noisy (20+ scored
            matches, under 30% relevant), new (under 7 days old, or changed in the last 7 days with under 20 scored since),
            quiet (7+ days, nothing relevant), otherwise healthy. After a change to matching rules, platforms or context, or
            an unmute, within the 14 days, only later matches count, while `noise` keeps all 14 days. The endpoint defaults
            to 30 days, so the two can differ, and it explains why and what to change.
        cost (KeywordStatsCost): List-price cost this calendar month (UTC), equal to this keyword's row in GET
            /v1/usage/breakdown?month=<this month>. The ledger settles daily and can differ only by cumulative rounding.
    """

    mentions: int
    relevant: int
    last7d: int
    this_month: int
    last_mention_at: None | str
    feedback: KeywordStatsFeedback
    noise: KeywordStatsNoise
    health: KeywordStatsHealth
    cost: KeywordStatsCost
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        relevant = self.relevant

        last7d = self.last7d

        this_month = self.this_month

        last_mention_at: None | str
        last_mention_at = self.last_mention_at

        feedback = self.feedback.to_dict()

        noise = self.noise.to_dict()

        health = self.health.value

        cost = self.cost.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "relevant": relevant,
                "last7d": last7d,
                "thisMonth": this_month,
                "lastMentionAt": last_mention_at,
                "feedback": feedback,
                "noise": noise,
                "health": health,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_stats_cost import KeywordStatsCost
        from ..models.keyword_stats_feedback import (
            KeywordStatsFeedback,
        )
        from ..models.keyword_stats_noise import KeywordStatsNoise

        d = dict(src_dict)
        mentions = d.pop("mentions")

        relevant = d.pop("relevant")

        last7d = d.pop("last7d")

        this_month = d.pop("thisMonth")

        def _parse_last_mention_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_mention_at = _parse_last_mention_at(d.pop("lastMentionAt"))

        feedback = KeywordStatsFeedback.from_dict(d.pop("feedback"))

        noise = KeywordStatsNoise.from_dict(d.pop("noise"))

        health = KeywordStatsHealth(d.pop("health"))

        cost = KeywordStatsCost.from_dict(d.pop("cost"))

        keyword_stats = cls(
            mentions=mentions,
            relevant=relevant,
            last7d=last7d,
            this_month=this_month,
            last_mention_at=last_mention_at,
            feedback=feedback,
            noise=noise,
            health=health,
            cost=cost,
        )

        keyword_stats.additional_properties = d
        return keyword_stats

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
