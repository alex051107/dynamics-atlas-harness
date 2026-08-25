"""Dynamics Atlas typed evidence-routing and registered-operator harness."""

from .contracts import validate_case_profile
from .evaluation import build_evaluation_contract, evaluate_current_bundle
from .profile import validate_case_graph
from .providers import (
    ProfileProvider,
    ProposalProvider,
    RecordedCaseGraphProvider,
    RecordedProposalProvider,
)
from .runtime import run_resolution_stage

__all__ = [
    "ProfileProvider",
    "ProposalProvider",
    "RecordedCaseGraphProvider",
    "RecordedProposalProvider",
    "build_evaluation_contract",
    "evaluate_current_bundle",
    "run_resolution_stage",
    "validate_case_graph",
    "validate_case_profile",
]

__version__ = "0.2.0"
