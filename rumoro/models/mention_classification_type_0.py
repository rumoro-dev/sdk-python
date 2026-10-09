from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_classification_type_0_sentiment import (
    MentionClassificationType0Sentiment,
)

if TYPE_CHECKING:
    from ..models.mention_classification_type_0_feedback_type_0 import (
        MentionClassificationType0FeedbackType0,
    )


T = TypeVar("T", bound="MentionClassificationType0")


@_attrs_define
class MentionClassificationType0:
    """The classifier's result with your feedback applied. Null while the post waits to be classified.

    Attributes:
        relevance (int | None): Score out of 100, or null if classification failed.
        sentiment (MentionClassificationType0Sentiment): The sentiment the classifier assigned.
        intents (list[str]): Tags for intent and topic. The values are buy_intent, question, complaint, praise,
            comparison, churn_intent (moving away from the keyword), bug_report, pricing, hiring, event, promotional,
            testimonial (a user recommending it from experience), industry_insight (analysis or numbers about the market),
            launch (a new product or feature announced) and feedback (an idea or request for it).
        automated (bool): A label for posts that look machine-made. Examples are bot or app accounts, scheduled or
            template posts and obvious AI summaries. Such mentions are kept, delivered and billed as usual. false until
            judged.
        language (None | str): ISO 639-1 code (en, es, de) of the post's language. Null if unknown or scored before
            languages were stored.
        confidence (float | None): The classifier's confidence in its relevance score, from 0 to 1. Null when the
            fallback model scored the post, or when it was scored before confidence was stored.
        uncertain (bool): True when a person should check the score, because confidence is below 0.4 or the model that
            wrote the note disagreed with it. It is a hint for reviewers and never hides a mention.
        note (None | str): A sentence from the classifier on why it gave this score.
        failed (bool): Set when the model failed to score the post. Such posts remain in the feed and cost nothing.
        feedback (MentionClassificationType0FeedbackType0 | None): Feedback from your team, or null. Judging relevance
            sets `relevance` to 100 or 0 and updates `relevant` to match. A new sentiment replaces `sentiment`. Lists,
            filters, digests and reports all use the corrected values.
    """

    relevance: int | None
    sentiment: MentionClassificationType0Sentiment
    intents: list[str]
    automated: bool
    language: None | str
    confidence: float | None
    uncertain: bool
    note: None | str
    failed: bool
    feedback: MentionClassificationType0FeedbackType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_classification_type_0_feedback_type_0 import (
            MentionClassificationType0FeedbackType0,
        )

        relevance: int | None
        relevance = self.relevance

        sentiment = self.sentiment.value

        intents = self.intents

        automated = self.automated

        language: None | str
        language = self.language

        confidence: float | None
        confidence = self.confidence

        uncertain = self.uncertain

        note: None | str
        note = self.note

        failed = self.failed

        feedback: dict[str, Any] | None
        if isinstance(self.feedback, MentionClassificationType0FeedbackType0):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relevance": relevance,
                "sentiment": sentiment,
                "intents": intents,
                "automated": automated,
                "language": language,
                "confidence": confidence,
                "uncertain": uncertain,
                "note": note,
                "failed": failed,
                "feedback": feedback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_classification_type_0_feedback_type_0 import (
            MentionClassificationType0FeedbackType0,
        )

        d = dict(src_dict)

        def _parse_relevance(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        relevance = _parse_relevance(d.pop("relevance"))

        sentiment = MentionClassificationType0Sentiment(d.pop("sentiment"))

        intents = cast(list[str], d.pop("intents"))

        automated = d.pop("automated")

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        def _parse_confidence(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        confidence = _parse_confidence(d.pop("confidence"))

        uncertain = d.pop("uncertain")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        failed = d.pop("failed")

        def _parse_feedback(
            data: object,
        ) -> MentionClassificationType0FeedbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = MentionClassificationType0FeedbackType0.from_dict(
                    data
                )

                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionClassificationType0FeedbackType0 | None, data)

        feedback = _parse_feedback(d.pop("feedback"))

        mention_classification_type_0 = cls(
            relevance=relevance,
            sentiment=sentiment,
            intents=intents,
            automated=automated,
            language=language,
            confidence=confidence,
            uncertain=uncertain,
            note=note,
            failed=failed,
            feedback=feedback,
        )

        mention_classification_type_0.additional_properties = d
        return mention_classification_type_0

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
