from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reviews_report_window_bucket import ReviewsReportWindowBucket

T = TypeVar("T", bound="ReviewsReportWindow")


@_attrs_define
class ReviewsReportWindow:
    """Start and end of the period.

    Attributes:
        from_ (str): The first day included.
        to (str): The last day included.
        days (int): How many days the window spans.
        timezone (str): The IANA time zone used to split the days.
        bucket (ReviewsReportWindowBucket): The step of each page's series. Days for windows up to 90 days and weeks
            beyond, unless you ask for one.
    """

    from_: str
    to: str
    days: int
    timezone: str
    bucket: ReviewsReportWindowBucket
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        days = self.days

        timezone = self.timezone

        bucket = self.bucket.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "days": days,
                "timezone": timezone,
                "bucket": bucket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        days = d.pop("days")

        timezone = d.pop("timezone")

        bucket = ReviewsReportWindowBucket(d.pop("bucket"))

        reviews_report_window = cls(
            from_=from_,
            to=to,
            days=days,
            timezone=timezone,
            bucket=bucket,
        )

        reviews_report_window.additional_properties = d
        return reviews_report_window

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
