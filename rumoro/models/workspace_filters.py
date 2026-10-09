from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workspace_filters_subreddits import WorkspaceFiltersSubreddits


T = TypeVar("T", bound="WorkspaceFilters")


@_attrs_define
class WorkspaceFilters:
    """Matching rules for the whole workspace. A post they reject is never billed.

    Attributes:
        excluded_terms (list[str]): Posts that contain one of these terms are dropped, whichever keyword matched them.
            Terms follow the same phrase rule as a keyword, and `*` at either end is a wildcard. A common list is "hiring,
            job, careers".
        excluded_authors (list[str]): Authors ignored across all keywords, such as your own accounts, teammates or known
            spammers. Entries may be profile or post links, @handles, u/names, Bluesky DIDs or display names, and are saved
            in canonical form.
        excluded_repos (list[str]): Repositories to ignore, as owner/name or a github.com link (vercel/next.js,
            https://github.com/vercel/next.js). Their issues, pull requests and comments are dropped.
        subreddits (WorkspaceFiltersSubreddits): Applies to Reddit only.
        updated_at (None | str): When the filters were last changed. Null if never.
    """

    excluded_terms: list[str]
    excluded_authors: list[str]
    excluded_repos: list[str]
    subreddits: WorkspaceFiltersSubreddits
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_terms = self.excluded_terms

        excluded_authors = self.excluded_authors

        excluded_repos = self.excluded_repos

        subreddits = self.subreddits.to_dict()

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "excludedTerms": excluded_terms,
                "excludedAuthors": excluded_authors,
                "excludedRepos": excluded_repos,
                "subreddits": subreddits,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace_filters_subreddits import (
            WorkspaceFiltersSubreddits,
        )

        d = dict(src_dict)
        excluded_terms = cast(list[str], d.pop("excludedTerms"))

        excluded_authors = cast(list[str], d.pop("excludedAuthors"))

        excluded_repos = cast(list[str], d.pop("excludedRepos"))

        subreddits = WorkspaceFiltersSubreddits.from_dict(d.pop("subreddits"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        workspace_filters = cls(
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            excluded_repos=excluded_repos,
            subreddits=subreddits,
            updated_at=updated_at,
        )

        workspace_filters.additional_properties = d
        return workspace_filters

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
