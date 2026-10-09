from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_post_platform import MentionPostPlatform

if TYPE_CHECKING:
    from ..models.mention_post_engagement_type_0 import MentionPostEngagementType0
    from ..models.mention_post_reply_to_type_0 import MentionPostReplyToType0


T = TypeVar("T", bound="MentionPost")


@_attrs_define
class MentionPost:
    """
    Attributes:
        platform (MentionPostPlatform): The platform. Review platforms are appstore, googleplay, trustpilot and
            googlemaps (a place's Google reviews).
        url (str): A stable link to the post.
        text (str): The title and body, cut to 8 KB when the post is collected.
        title (None | str): The post's title on platforms that have titles, such as Hacker News stories, Reddit threads,
            GitHub issues and pull requests, Stack Overflow questions, DEV articles, YouTube videos, news articles and
            reviews with a title. Null on platforms without titles (X, Bluesky, LinkedIn) and for posts collected before
            October 2026.
        image_url (None | str): Preview image sent by the platform, or null. Examples are YouTube thumbnails, DEV
            covers, news sharing images and Bluesky images or link cards.
        links (list[str]): Up to 20 links found in the post, in the order they appear. Empty when there are none and for
            posts collected before September 2026.
        published_at (str): When the post went live on the platform.
        engagement (MentionPostEngagementType0 | None): Engagement numbers as the platform gave them when the post was
            collected, often a few minutes after it was written. A number the platform lacks is null. The whole object is
            null on platforms that report none and for posts collected before September 2026. X reports all six.
        reply_to (MentionPostReplyToType0 | None): The post being replied to, on X and Bluesky. Null when the post is
            not a reply.
    """

    platform: MentionPostPlatform
    url: str
    text: str
    title: None | str
    image_url: None | str
    links: list[str]
    published_at: str
    engagement: MentionPostEngagementType0 | None
    reply_to: MentionPostReplyToType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_post_engagement_type_0 import (
            MentionPostEngagementType0,
        )
        from ..models.mention_post_reply_to_type_0 import (
            MentionPostReplyToType0,
        )

        platform = self.platform.value

        url = self.url

        text = self.text

        title: None | str
        title = self.title

        image_url: None | str
        image_url = self.image_url

        links = self.links

        published_at = self.published_at

        engagement: dict[str, Any] | None
        if isinstance(self.engagement, MentionPostEngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        reply_to: dict[str, Any] | None
        if isinstance(self.reply_to, MentionPostReplyToType0):
            reply_to = self.reply_to.to_dict()
        else:
            reply_to = self.reply_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "url": url,
                "text": text,
                "title": title,
                "imageUrl": image_url,
                "links": links,
                "publishedAt": published_at,
                "engagement": engagement,
                "replyTo": reply_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_post_engagement_type_0 import (
            MentionPostEngagementType0,
        )
        from ..models.mention_post_reply_to_type_0 import (
            MentionPostReplyToType0,
        )

        d = dict(src_dict)
        platform = MentionPostPlatform(d.pop("platform"))

        url = d.pop("url")

        text = d.pop("text")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        links = cast(list[str], d.pop("links"))

        published_at = d.pop("publishedAt")

        def _parse_engagement(data: object) -> MentionPostEngagementType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = MentionPostEngagementType0.from_dict(data)

                return engagement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionPostEngagementType0 | None, data)

        engagement = _parse_engagement(d.pop("engagement"))

        def _parse_reply_to(data: object) -> MentionPostReplyToType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_to_type_0 = MentionPostReplyToType0.from_dict(data)

                return reply_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionPostReplyToType0 | None, data)

        reply_to = _parse_reply_to(d.pop("replyTo"))

        mention_post = cls(
            platform=platform,
            url=url,
            text=text,
            title=title,
            image_url=image_url,
            links=links,
            published_at=published_at,
            engagement=engagement,
            reply_to=reply_to,
        )

        mention_post.additional_properties = d
        return mention_post

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
