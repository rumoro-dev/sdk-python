from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_breakdown_data_item_keyword_type_0 import (
        AnalyticsBreakdownDataItemKeywordType0,
    )
    from ..models.analytics_breakdown_data_item_person_type_0 import (
        AnalyticsBreakdownDataItemPersonType0,
    )
    from ..models.analytics_breakdown_data_item_previous_type_0 import (
        AnalyticsBreakdownDataItemPreviousType0,
    )
    from ..models.analytics_breakdown_data_item_sentiment import (
        AnalyticsBreakdownDataItemSentiment,
    )
    from ..models.analytics_breakdown_data_item_slot_type_0 import (
        AnalyticsBreakdownDataItemSlotType0,
    )


T = TypeVar("T", bound="AnalyticsBreakdownDataItem")


@_attrs_define
class AnalyticsBreakdownDataItem:
    """
    Attributes:
        key (str): What the row stands for. A platform name, keyword id, sentiment, intent or status, "weekday-hour"
            with by=hour, or a person key you should not parse.
        label (str): A name to display. The keyword's term or the person's name, or else the key.
        keyword (AnalyticsBreakdownDataItemKeywordType0 | None): Set only with by=keyword. Null otherwise.
        person (AnalyticsBreakdownDataItemPersonType0 | None): Set only with by=person. Null otherwise.
        slot (AnalyticsBreakdownDataItemSlotType0 | None): Weekday and hour in `timezone` when by=hour, otherwise null.
        matched (int): Matches in this row.
        relevant (int): How many of them scored 40 or more.
        share (float): The percentage of the window's matches that fall in this row, with one decimal. A mention can
            have several intents, so intent shares can total more than 100.
        sentiment (AnalyticsBreakdownDataItemSentiment): Sentiment split of the matched mentions.
        previous (AnalyticsBreakdownDataItemPreviousType0 | None): This row for the period just before the window. Null
            unless compare=true.
    """

    key: str
    label: str
    keyword: AnalyticsBreakdownDataItemKeywordType0 | None
    person: AnalyticsBreakdownDataItemPersonType0 | None
    slot: AnalyticsBreakdownDataItemSlotType0 | None
    matched: int
    relevant: int
    share: float
    sentiment: AnalyticsBreakdownDataItemSentiment
    previous: AnalyticsBreakdownDataItemPreviousType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_breakdown_data_item_keyword_type_0 import (
            AnalyticsBreakdownDataItemKeywordType0,
        )
        from ..models.analytics_breakdown_data_item_person_type_0 import (
            AnalyticsBreakdownDataItemPersonType0,
        )
        from ..models.analytics_breakdown_data_item_previous_type_0 import (
            AnalyticsBreakdownDataItemPreviousType0,
        )
        from ..models.analytics_breakdown_data_item_slot_type_0 import (
            AnalyticsBreakdownDataItemSlotType0,
        )

        key = self.key

        label = self.label

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, AnalyticsBreakdownDataItemKeywordType0):
            keyword = self.keyword.to_dict()
        else:
            keyword = self.keyword

        person: dict[str, Any] | None
        if isinstance(self.person, AnalyticsBreakdownDataItemPersonType0):
            person = self.person.to_dict()
        else:
            person = self.person

        slot: dict[str, Any] | None
        if isinstance(self.slot, AnalyticsBreakdownDataItemSlotType0):
            slot = self.slot.to_dict()
        else:
            slot = self.slot

        matched = self.matched

        relevant = self.relevant

        share = self.share

        sentiment = self.sentiment.to_dict()

        previous: dict[str, Any] | None
        if isinstance(self.previous, AnalyticsBreakdownDataItemPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "keyword": keyword,
                "person": person,
                "slot": slot,
                "matched": matched,
                "relevant": relevant,
                "share": share,
                "sentiment": sentiment,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_breakdown_data_item_keyword_type_0 import (
            AnalyticsBreakdownDataItemKeywordType0,
        )
        from ..models.analytics_breakdown_data_item_person_type_0 import (
            AnalyticsBreakdownDataItemPersonType0,
        )
        from ..models.analytics_breakdown_data_item_previous_type_0 import (
            AnalyticsBreakdownDataItemPreviousType0,
        )
        from ..models.analytics_breakdown_data_item_sentiment import (
            AnalyticsBreakdownDataItemSentiment,
        )
        from ..models.analytics_breakdown_data_item_slot_type_0 import (
            AnalyticsBreakdownDataItemSlotType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_keyword(
            data: object,
        ) -> AnalyticsBreakdownDataItemKeywordType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = AnalyticsBreakdownDataItemKeywordType0.from_dict(data)

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsBreakdownDataItemKeywordType0 | None, data)

        keyword = _parse_keyword(d.pop("keyword"))

        def _parse_person(data: object) -> AnalyticsBreakdownDataItemPersonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_type_0 = AnalyticsBreakdownDataItemPersonType0.from_dict(data)

                return person_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsBreakdownDataItemPersonType0 | None, data)

        person = _parse_person(d.pop("person"))

        def _parse_slot(data: object) -> AnalyticsBreakdownDataItemSlotType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slot_type_0 = AnalyticsBreakdownDataItemSlotType0.from_dict(data)

                return slot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsBreakdownDataItemSlotType0 | None, data)

        slot = _parse_slot(d.pop("slot"))

        matched = d.pop("matched")

        relevant = d.pop("relevant")

        share = d.pop("share")

        sentiment = AnalyticsBreakdownDataItemSentiment.from_dict(d.pop("sentiment"))

        def _parse_previous(
            data: object,
        ) -> AnalyticsBreakdownDataItemPreviousType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = AnalyticsBreakdownDataItemPreviousType0.from_dict(
                    data
                )

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsBreakdownDataItemPreviousType0 | None, data)

        previous = _parse_previous(d.pop("previous"))

        analytics_breakdown_data_item = cls(
            key=key,
            label=label,
            keyword=keyword,
            person=person,
            slot=slot,
            matched=matched,
            relevant=relevant,
            share=share,
            sentiment=sentiment,
            previous=previous,
        )

        analytics_breakdown_data_item.additional_properties = d
        return analytics_breakdown_data_item

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
