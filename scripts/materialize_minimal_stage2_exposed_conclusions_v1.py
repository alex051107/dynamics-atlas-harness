#!/usr/bin/env python3
"""Materialize Stage-2 packets from frozen exposed route artifacts only.

This script never calls a model, lookup, or Operator.  It reads the immutable PR #6
route packets and writes a separate, non-overwriting Stage-2 evidence bundle.
"""

from __future__ import annotations

import json
from pathlib import Path

from dynamics_atlas_harness.minimal_stage2_exposed_conclusions_v1 import (
    materialize_stage2_conclusion_packet,
    source_grounding_by_family,
)
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_json_object


REPO_ROOT = Path(__file__).parents[1]
OUTPUT_ROOT = REPO_ROOT / "evidence" / "minimal_stage2_exposed_conclusions_v1" / "outputs"
FAMILY_OVERLAY_PATH = REPO_ROOT / "registries" / "rules_v1" / "family_overlay_v1.json"

SCENARIOS = (
    (
        "XEISD_A1_COMPLETE_METADATA",
        "xeisd_a1_complete_stage2_conclusion_packet.json",
        "evidence/real_case_vertical_slice_v1/outputs/xeisd_a1_conclusion_packet.json",
    ),
    (
        "XEISD_A2_MISSING_COMPOSITION",
        "xeisd_a2_missing_composition_stage2_conclusion_packet.json",
        "evidence/real_case_vertical_slice_v1/outputs/xeisd_a2_conclusion_packet.json",
    ),
    (
        "XEISD_A3_EXPLICIT_CONDITION_MISMATCH",
        "xeisd_a3_condition_mismatch_stage2_conclusion_packet.json",
        "evidence/real_case_vertical_slice_v1/outputs/xeisd_a3_conclusion_packet.json",
    ),
    (
        "HSP90_B1_OPERATOR_CONTRACT_PASS",
        "hsp90_b1_operator_contract_stage2_conclusion_packet.json",
        "evidence/real_case_vertical_slice_v1/outputs/hsp90_b1_rule_to_operator/conclusion_packet.json",
    ),
)


def _write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    if OUTPUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing Stage-2 evidence: {OUTPUT_ROOT}")
    source_grounding = source_grounding_by_family(load_json_object(FAMILY_OVERLAY_PATH))
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=False)

    terminal_dispositions: dict[str, str] = {}
    for scenario_id, output_name, route_relative_path in SCENARIOS:
        route_packet = load_json_object(REPO_ROOT / route_relative_path)
        packet = materialize_stage2_conclusion_packet(
            route_packet=route_packet,
            source_grounding=source_grounding,
            scenario_id=scenario_id,
            route_artifact_path=route_relative_path,
        )
        _write_json(OUTPUT_ROOT / output_name, packet)
        terminal_dispositions[scenario_id] = packet["terminal_disposition"]

    _write_json(
        OUTPUT_ROOT / "run_receipt.json",
        {
            "run_kind": "MINIMAL_STAGE2_EXPOSED_CONCLUSIONS_V1",
            "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
            "input_family_overlay": "registries/rules_v1/family_overlay_v1.json",
            "input_route_artifacts": [entry[2] for entry in SCENARIOS],
            "terminal_dispositions": terminal_dispositions,
            "network_accessed": False,
            "model_calls": 0,
            "lookup_calls": 0,
            "operator_calls": 0,
            "scientific_claim_upgrade": False,
            "boundary": "A deterministic reduction over frozen exposed route artifacts. Source-grounding decisions remain PENDING_DOMAIN_REVIEW, and every packet retains human final authority.",
        },
    )


if __name__ == "__main__":
    main()
