from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reviews_report_totals_distribution import (
        ReviewsReportTotalsDistribution,
    )


T = TypeVar("T", bound="ReviewsReportTotals")


@_attrs_define
class ReviewsReportTotals:
    """
    Attributes:
        reviews (int): Reviews published in the window, counting each review once across keywords.
        average_rating (float | None): The average star rating with one decimal. Null when there are no reviews.
        distribution (ReviewsReportTotalsDistribution): How many reviews have each star rating.
        responded (int): Reviews with a reply from the owner or developer. The App Store feed has no replies.
        open_negative (int): Reviews of 1 or 2 stars still open in triage.
    """

    reviews: int
    average_rating: float | None
    distribution: ReviewsReportTotalsDistribution
    responded: int
    open_negative: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviews = self.reviews

        average_rating: float | None
        average_rating = self.average_rating

        distribution = self.distribution.to_dict()

        responded = self.responded

        open_negative = self.open_negative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviews": reviews,
                "averageRating": average_rating,
                "distribution": distribution,
                "responded": responded,
                "openNegative": open_negative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reviews_report_totals_distribution import (
            ReviewsReportTotalsDistribution,
        )

        d = dict(src_dict)
        reviews = d.pop("reviews")

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("averageRating"))

        distribution = ReviewsReportTotalsDistribution.from_dict(d.pop("distribution"))

        responded = d.pop("responded")

        open_negative = d.pop("openNegative")

        reviews_report_totals = cls(
            reviews=reviews,
            average_rating=average_rating,
            distribution=distribution,
            responded=responded,
            open_negative=open_negative,
        )

        reviews_report_totals.additional_properties = d
        return reviews_report_totals

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
