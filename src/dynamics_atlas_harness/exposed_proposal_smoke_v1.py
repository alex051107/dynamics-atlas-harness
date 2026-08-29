"""Answer-blind proposal materialization for the exposed development smoke test.

This adapter owns only fixture loading and card-selection materialization.  It does
not call a model, inspect sealed references, select Rules, or execute an action.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .live_agent_exposed_v1 import materialize_planner_card_selection


EXPOSED_CASES = ("xeisd", "hsp90")
_RECORDED_RUN = "qwen2_5_1_5b_20260826_prompt_remediation1"


class ExposedProposalSmokeError(ValueError):
    """Raised when a committed smoke-test fixture cannot be admitted."""


def _json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExposedProposalSmokeError(f"cannot read JSON fixture {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ExposedProposalSmokeError(f"fixture must be a JSON object: {path}")
    return value


def load_exposed_planner_fixtures(
    case_key: str, *, experiment_root: Path
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Load one model-visible packet and its recorded card-only response."""

    if case_key not in EXPOSED_CASES:
        raise ExposedProposalSmokeError(f"unsupported exposed case: {case_key}")
    packet = _json_object(experiment_root / "workspaces" / f"{case_key}_planner" / "input.json")
    selection = _json_object(
        experiment_root
        / "recorded"
        / _RECORDED_RUN
        / f"{case_key}_planner"
        / "raw_response.txt"
    )
    return packet, selection


def materialize_exposed_planner_proposal(
    case_key: str, *, experiment_root: Path
) -> dict[str, Any]:
    """Return the existing platform-owned, non-authoritative proposal receipt."""

    packet, recorded_selection = load_exposed_planner_fixtures(
        case_key, experiment_root=experiment_root
    )
    # The committed historical response is a proposal-shaped object.  Keep only
    # its card IDs and rationales at this boundary; platform-owned fields must not
    # be trusted from the recorded response.
    if (
        recorded_selection.get("execution_requested") is not False
        or recorded_selection.get("scientific_disposition") != "NOT_EVALUATED"
    ):
        raise ExposedProposalSmokeError("recorded response contains an escalation")
    actions = recorded_selection.get("proposed_actions")
    if not isinstance(actions, list) or not actions:
        raise ExposedProposalSmokeError("recorded response lacks proposed actions")
    selection = {"selected_card_ids": [], "rationales": {}}
    for action in actions:
        if not isinstance(action, dict):
            raise ExposedProposalSmokeError("recorded action must be an object")
        card_id = action.get("card_id")
        rationale = action.get("rationale")
        if not isinstance(card_id, str) or not isinstance(rationale, str):
            raise ExposedProposalSmokeError("recorded action lacks card selection fields")
        selection["selected_card_ids"].append(card_id)
        selection["rationales"][card_id] = rationale
    return materialize_planner_card_selection(selection, packet)
