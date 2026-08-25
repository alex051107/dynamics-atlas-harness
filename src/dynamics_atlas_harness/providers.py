"""Provider-neutral proposal interface."""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any, Protocol


class ProposalProvider(Protocol):
    """A provider proposes; it never authorizes or executes."""

    provider_id: str

    def propose(self, bounded_view: Mapping[str, Any]) -> dict[str, Any]: ...


class ProfileProvider(Protocol):
    """A provider may propose a rich CaseGraph, but cannot canonicalize it."""

    provider_id: str

    def propose_profile(self, request_view: Mapping[str, Any]) -> dict[str, Any]: ...


class RecordedProposalProvider:
    """Replay a stored proposal through the same interface as a later model."""

    def __init__(self, proposal: Mapping[str, Any], provider_id: str = "recorded-fixture"):
        self.provider_id = provider_id
        self._proposal = copy.deepcopy(dict(proposal))

    def propose(self, bounded_view: Mapping[str, Any]) -> dict[str, Any]:
        del bounded_view
        return copy.deepcopy(self._proposal)


class RecordedCaseGraphProvider:
    """Replay a source-grounded CaseGraph through the future model boundary."""

    def __init__(
        self, proposal: Mapping[str, Any], provider_id: str = "recorded-rich-case-graph"
    ):
        self.provider_id = provider_id
        self._proposal = copy.deepcopy(dict(proposal))

    def propose_profile(self, request_view: Mapping[str, Any]) -> dict[str, Any]:
        if request_view.get("authority") != "PROPOSE_CASE_GRAPH_ONLY":
            raise ValueError("INVALID_PROFILE_REQUEST_AUTHORITY")
        return copy.deepcopy(self._proposal)
