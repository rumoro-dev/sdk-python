from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_mode import AlertMode

if TYPE_CHECKING:
    from ..models.alert_channels_item import AlertChannelsItem
    from ..models.alert_filter import AlertFilter
    from ..models.alert_schedule_type_0 import AlertScheduleType0
    from ..models.alert_stats import AlertStats


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        id (str): The alert's id (feed_...).
        name (str):
        enabled (bool):
        mode (AlertMode): instant sends each matching mention as it arrives. hourly sends a digest of the previous full
            UTC hour at five past the hour, so the hour's last mentions are scored. It skips hours with no mention at or
            above the rule's relevance minimum, and works with Slack, Telegram and webhook channels only. daily sends one
            digest at the scheduled local time. weekly sends one digest a week on schedule.weekday.
        filter_ (AlertFilter):
        schedule (AlertScheduleType0 | None): Null for instant and hourly alerts, which have no schedule.
        event (str): The event name sent in webhook payloads. Unless you set one, it is the default for the mode.
        channels (list[AlertChannelsItem]): The channels the alert sends to.
        stats (AlertStats): Counted from this workspace's deliveries.
        created_at (str): UTC time in ISO 8601.
    """

    id: str
    name: str
    enabled: bool
    mode: AlertMode
    filter_: AlertFilter
    schedule: AlertScheduleType0 | None
    event: str
    channels: list[AlertChannelsItem]
    stats: AlertStats
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_schedule_type_0 import AlertScheduleType0

        id = self.id

        name = self.name

        enabled = self.enabled

        mode = self.mode.value

        filter_ = self.filter_.to_dict()

        schedule: dict[str, Any] | None
        if isinstance(self.schedule, AlertScheduleType0):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

        event = self.event

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        stats = self.stats.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "mode": mode,
                "filter": filter_,
                "schedule": schedule,
                "event": event,
                "channels": channels,
                "stats": stats,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_channels_item import AlertChannelsItem
        from ..models.alert_filter import AlertFilter
        from ..models.alert_schedule_type_0 import AlertScheduleType0
        from ..models.alert_stats import AlertStats

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        mode = AlertMode(d.pop("mode"))

        filter_ = AlertFilter.from_dict(d.pop("filter"))

        def _parse_schedule(data: object) -> AlertScheduleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = AlertScheduleType0.from_dict(data)

                return schedule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertScheduleType0 | None, data)

        schedule = _parse_schedule(d.pop("schedule"))

        event = d.pop("event")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = AlertChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        stats = AlertStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        alert = cls(
            id=id,
            name=name,
            enabled=enabled,
            mode=mode,
            filter_=filter_,
            schedule=schedule,
            event=event,
            channels=channels,
            stats=stats,
            created_at=created_at,
        )

        alert.additional_properties = d
        return alert

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
