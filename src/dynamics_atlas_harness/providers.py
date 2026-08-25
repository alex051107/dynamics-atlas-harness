"""Provider-neutral proposal interface."""

from __future__ import annotations

import copy
from collections.abc import Mapping
from typing import Any, Protocol


class ProposalProvider(Protocol):
    """A provider proposes; it never authorizes or executes."""

    provider_id: str

    def propose(self, bounded_view: Mapping[str, Any]) -> dict[str, Any]: ...


class RecordedProposalProvider:
    """Replay a stored proposal through the same interface as a later model."""

    def __init__(self, proposal: Mapping[str, Any], provider_id: str = "recorded-fixture"):
        self.provider_id = provider_id
        self._proposal = copy.deepcopy(dict(proposal))

    def propose(self, bounded_view: Mapping[str, Any]) -> dict[str, Any]:
        del bounded_view
        return copy.deepcopy(self._proposal)
