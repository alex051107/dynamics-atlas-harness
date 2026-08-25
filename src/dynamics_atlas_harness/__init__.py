"""Dynamics Atlas minimal profile/operator bridge."""

from .contracts import validate_case_profile
from .providers import ProposalProvider, RecordedProposalProvider
from .runtime import run_resolution_stage

__all__ = [
    "ProposalProvider",
    "RecordedProposalProvider",
    "run_resolution_stage",
    "validate_case_profile",
]

__version__ = "0.1.0"
