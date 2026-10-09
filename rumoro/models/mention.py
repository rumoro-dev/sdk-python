from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_status import MentionStatus

if TYPE_CHECKING:
    from ..models.mention_author_type_0 import MentionAuthorType0
    from ..models.mention_classification_type_0 import MentionClassificationType0
    from ..models.mention_keyword import MentionKeyword
    from ..models.mention_post import MentionPost
    from ..models.mention_review_type_0 import MentionReviewType0
    from ..models.mention_triage import MentionTriage


T = TypeVar("T", bound="Mention")


@_attrs_define
class Mention:
    """
    Attributes:
        id (str): The mention's id (mm_...). A mention is one post matched to one keyword, so a post that matches two
            keywords has two ids.
        status (MentionStatus): open means no one has handled it. ignored means you hid it from the feed and channels.
            done means it was handled.
        relevant (bool): True when the classifier's relevance score is 40 or more, the delivery threshold.
        delivered (bool): true once any channel of yours received it.
        priority (float): How much the mention deserves attention, with one decimal, worked out when you read it. It
            adds half the relevance, points for the author's followers (8 when unknown) and points for the strongest intent
            (from 20 for buy intent down to 5 for praise). It then takes off 2 points per day of age, at most 20.
        keyword (MentionKeyword): The keyword the post matched, with its group.
        post (MentionPost):
        author (MentionAuthorType0 | None): The author of the post. Null when the platform gave no author.
        review (MentionReviewType0 | None): Details of an app store review. Null for any other post. The stars set the
            sentiment, with 4 and 5 positive, 3 neutral, and 1 and 2 negative. A review always counts as relevant, because
            you picked the app.
        classification (MentionClassificationType0 | None): The classifier's result with your feedback applied. Null
            while the post waits to be classified.
        triage (MentionTriage):
        created_at (str): When the match was stored. The feed is sorted by this by default.
    """

    id: str
    status: MentionStatus
    relevant: bool
    delivered: bool
    priority: float
    keyword: MentionKeyword
    post: MentionPost
    author: MentionAuthorType0 | None
    review: MentionReviewType0 | None
    classification: MentionClassificationType0 | None
    triage: MentionTriage
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_author_type_0 import MentionAuthorType0
        from ..models.mention_classification_type_0 import (
            MentionClassificationType0,
        )
        from ..models.mention_review_type_0 import MentionReviewType0

        id = self.id

        status = self.status.value

        relevant = self.relevant

        delivered = self.delivered

        priority = self.priority

        keyword = self.keyword.to_dict()

        post = self.post.to_dict()

        author: dict[str, Any] | None
        if isinstance(self.author, MentionAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        review: dict[str, Any] | None
        if isinstance(self.review, MentionReviewType0):
            review = self.review.to_dict()
        else:
            review = self.review

        classification: dict[str, Any] | None
        if isinstance(self.classification, MentionClassificationType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        triage = self.triage.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "relevant": relevant,
                "delivered": delivered,
                "priority": priority,
                "keyword": keyword,
                "post": post,
                "author": author,
                "review": review,
                "classification": classification,
                "triage": triage,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_author_type_0 import MentionAuthorType0
        from ..models.mention_classification_type_0 import (
            MentionClassificationType0,
        )
        from ..models.mention_keyword import MentionKeyword
        from ..models.mention_post import MentionPost
        from ..models.mention_review_type_0 import MentionReviewType0
        from ..models.mention_triage import MentionTriage

        d = dict(src_dict)
        id = d.pop("id")

        status = MentionStatus(d.pop("status"))

        relevant = d.pop("relevant")

        delivered = d.pop("delivered")

        priority = d.pop("priority")

        keyword = MentionKeyword.from_dict(d.pop("keyword"))

        post = MentionPost.from_dict(d.pop("post"))

        def _parse_author(data: object) -> MentionAuthorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = MentionAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionAuthorType0 | None, data)

        author = _parse_author(d.pop("author"))

        def _parse_review(data: object) -> MentionReviewType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                review_type_0 = MentionReviewType0.from_dict(data)

                return review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionReviewType0 | None, data)

        review = _parse_review(d.pop("review"))

        def _parse_classification(data: object) -> MentionClassificationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                classification_type_0 = MentionClassificationType0.from_dict(data)

                return classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionClassificationType0 | None, data)

        classification = _parse_classification(d.pop("classification"))

        triage = MentionTriage.from_dict(d.pop("triage"))

        created_at = d.pop("createdAt")

        mention = cls(
            id=id,
            status=status,
            relevant=relevant,
            delivered=delivered,
            priority=priority,
            keyword=keyword,
            post=post,
            author=author,
            review=review,
            classification=classification,
            triage=triage,
            created_at=created_at,
        )

        mention.additional_properties = d
        return mention

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
