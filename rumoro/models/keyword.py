from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_kind import KeywordKind
from ..models.keyword_platforms_type_0_item import KeywordPlatformsType0Item

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef
    from ..models.keyword_cap_type_0 import KeywordCapType0
    from ..models.keyword_matching import KeywordMatching
    from ..models.keyword_polling_item import KeywordPollingItem
    from ..models.keyword_stats import KeywordStats
    from ..models.review_source import ReviewSource


T = TypeVar("T", bound="Keyword")


@_attrs_define
class Keyword:
    """
    Attributes:
        id (str): The keyword's id (kw_...).
        term (str):
        kind (KeywordKind):
        muted (bool): True when the keyword is neither polled nor matched. You, the wallet (pausedForBalance) or the
            noise brake (pausedForNoise) can mute it. Reaching the mention cap does not mute it (pausedForCap).
        paused_for_balance (bool): Muted because the balance ran out. A top-up resumes it. Unmuting it yourself also
            needs balance.
        paused_for_noise (bool): Set when the noise brake muted the keyword. That happens on welcome credit once 20 or
            more matches are scored and under 30% are relevant. Unmuting it, or changing its required or excluded terms,
            platforms or context, resumes it when the balance covers another day. A top-up alone does not.
        paused_for_cap (bool): Hit its monthly mention cap. Matching resumes on the 1st (UTC) or when you raise the cap.
            The keyword isn't muted and is still charged daily.
        cap (KeywordCapType0 | None): Monthly limit on matched mentions. Null means none.
        group (GroupRef): The keyword's group.
        platforms (list[KeywordPlatformsType0Item] | None): The platforms searched for the term. Null means all of them.
            An empty list means none, and the keyword only collects reviews.
        review_sources (list[ReviewSource]): The review pages the keyword reads, such as App Store and Google Play apps,
            Trustpilot pages and Google Maps places. Empty when there are none.
        context (None | str): Up to 300 characters the classifier reads for this keyword only, in addition to the
            company profile or the group's description. Say what the term means for you and what to ignore, for example
            "Driftwood is our deploy tool, not beach wood." Null clears it.
        matching (KeywordMatching): Rules a post must pass before it is stored as a mention. A post they reject is never
            billed.
        stats (KeywordStats): Counted from this workspace's matches only.
        polling (list[KeywordPollingItem]): Polling status for each platform that is polled on a schedule. Live feeds
            such as Bluesky are not listed.
        created_at (str): UTC time in ISO 8601.
    """

    id: str
    term: str
    kind: KeywordKind
    muted: bool
    paused_for_balance: bool
    paused_for_noise: bool
    paused_for_cap: bool
    cap: KeywordCapType0 | None
    group: GroupRef
    platforms: list[KeywordPlatformsType0Item] | None
    review_sources: list[ReviewSource]
    context: None | str
    matching: KeywordMatching
    stats: KeywordStats
    polling: list[KeywordPollingItem]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_cap_type_0 import KeywordCapType0

        id = self.id

        term = self.term

        kind = self.kind.value

        muted = self.muted

        paused_for_balance = self.paused_for_balance

        paused_for_noise = self.paused_for_noise

        paused_for_cap = self.paused_for_cap

        cap: dict[str, Any] | None
        if isinstance(self.cap, KeywordCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        group = self.group.to_dict()

        platforms: list[str] | None
        if isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        review_sources = []
        for review_sources_item_data in self.review_sources:
            review_sources_item = review_sources_item_data.to_dict()
            review_sources.append(review_sources_item)

        context: None | str
        context = self.context

        matching = self.matching.to_dict()

        stats = self.stats.to_dict()

        polling = []
        for polling_item_data in self.polling:
            polling_item = polling_item_data.to_dict()
            polling.append(polling_item)

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "kind": kind,
                "muted": muted,
                "pausedForBalance": paused_for_balance,
                "pausedForNoise": paused_for_noise,
                "pausedForCap": paused_for_cap,
                "cap": cap,
                "group": group,
                "platforms": platforms,
                "reviewSources": review_sources,
                "context": context,
                "matching": matching,
                "stats": stats,
                "polling": polling,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_ref import GroupRef
        from ..models.keyword_cap_type_0 import KeywordCapType0
        from ..models.keyword_matching import KeywordMatching
        from ..models.keyword_polling_item import KeywordPollingItem
        from ..models.keyword_stats import KeywordStats
        from ..models.review_source import ReviewSource

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = KeywordKind(d.pop("kind"))

        muted = d.pop("muted")

        paused_for_balance = d.pop("pausedForBalance")

        paused_for_noise = d.pop("pausedForNoise")

        paused_for_cap = d.pop("pausedForCap")

        def _parse_cap(data: object) -> KeywordCapType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = KeywordCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordCapType0 | None, data)

        cap = _parse_cap(d.pop("cap"))

        group = GroupRef.from_dict(d.pop("group"))

        def _parse_platforms(data: object) -> list[KeywordPlatformsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = KeywordPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordPlatformsType0Item] | None, data)

        platforms = _parse_platforms(d.pop("platforms"))

        review_sources = []
        _review_sources = d.pop("reviewSources")
        for review_sources_item_data in _review_sources:
            review_sources_item = ReviewSource.from_dict(review_sources_item_data)

            review_sources.append(review_sources_item)

        def _parse_context(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        context = _parse_context(d.pop("context"))

        matching = KeywordMatching.from_dict(d.pop("matching"))

        stats = KeywordStats.from_dict(d.pop("stats"))

        polling = []
        _polling = d.pop("polling")
        for polling_item_data in _polling:
            polling_item = KeywordPollingItem.from_dict(polling_item_data)

            polling.append(polling_item)

        created_at = d.pop("createdAt")

        keyword = cls(
            id=id,
            term=term,
            kind=kind,
            muted=muted,
            paused_for_balance=paused_for_balance,
            paused_for_noise=paused_for_noise,
            paused_for_cap=paused_for_cap,
            cap=cap,
            group=group,
            platforms=platforms,
            review_sources=review_sources,
            context=context,
            matching=matching,
            stats=stats,
            polling=polling,
            created_at=created_at,
        )

        keyword.additional_properties = d
        return keyword

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
