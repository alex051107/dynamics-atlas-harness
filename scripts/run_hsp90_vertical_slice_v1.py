#!/usr/bin/env python3
"""Run the one exposed HSP90 Rule-to-Operator vertical slice exactly once.

The script has no Agent, network, generic scheduler, or broad Operator discovery
path. It starts from the case-bound F04R02 obligation, matches one pre-registered
Operator against one exact manifest, and writes a receipt, EvidenceResult,
reevaluation, and bounded ConclusionPacket.
"""

from __future__ import annotations

import json
from pathlib import Path

from dynamics_atlas_harness.real_case_vertical_slice_v1 import (
    ExecutionEvidenceContext,
    evaluate_hsp90_time_anatomy_f04r02,
    load_hsp90_case_bundle,
    materialize_hsp90_conclusion_packet,
    resolve_hsp90_time_anatomy_obligation,
    run_hsp90_case_bound_operator,
)
from dynamics_atlas_harness.registered_operators import load_registered_operator_registry


REPO_ROOT = Path(__file__).parents[1]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
OUTPUT_ROOT = EVIDENCE_ROOT / "outputs" / "hsp90_b1_rule_to_operator"


def main() -> None:
    if OUTPUT_ROOT.exists():
        raise SystemExit(
            f"refusing to overwrite frozen HSP90 vertical-slice output: {OUTPUT_ROOT}"
        )
    bundle = load_hsp90_case_bundle(EVIDENCE_ROOT)
    registry = load_registered_operator_registry(
        REPO_ROOT / "config" / "registered_operators.json"
    )
    pre_rule = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
    )
    resolution = resolve_hsp90_time_anatomy_obligation(
        rule_result=pre_rule,
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        operator_registry=registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=REPO_ROOT,
    )

    # Freeze a new receipt directory before the adapter runs; a failed execution is
    # still an auditable Case-B outcome rather than an unrecorded exception.
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=False)
    operator_output_dir = OUTPUT_ROOT / "operator_outputs"
    operator_run = run_hsp90_case_bound_operator(
        resolution=resolution,
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        operator_registry=registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=REPO_ROOT,
        output_dir=operator_output_dir,
        request_id="B1_EXACT_HSP90_RULE_TO_OPERATOR",
    )
    context = ExecutionEvidenceContext()
    context.record_validated_operator_run(
        operator_run=operator_run,
        operator_registry=registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=REPO_ROOT,
    )
    post_rule = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
        evidence_context=context,
    )
    packet = materialize_hsp90_conclusion_packet(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
        operator_registry=registry,
        workspace_root=REPO_ROOT,
        rule_result=post_rule,
        operator_run=operator_run,
        scenario_id="B1_EXACT_HSP90_RULE_TO_OPERATOR",
    )

    # Do not write through helper before the Operator's own output directory exists.
    for name, payload in (
        ("pre_operator_rule_result.json", pre_rule),
        ("resolution_route.json", resolution),
        ("operator_run_receipt.json", operator_run["operator_run_receipt"]),
        ("evidence_result.json", operator_run["evidence_result"]),
        ("post_operator_rule_result.json", post_rule),
        ("conclusion_packet.json", packet),
    ):
        (OUTPUT_ROOT / name).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    (OUTPUT_ROOT / "run_receipt.json").write_text(
        json.dumps(
            {
                "run_kind": "EXPOSED_HSP90_RULE_TO_OPERATOR_VERTICAL_SLICE_V1_ALPHA",
                "case_id": bundle["case_graph"]["case"]["case_id"],
                "network_accessed": False,
                "live_agent_run": False,
                "unregistered_tool_calls": 0,
                "pre_operator_rule_status": pre_rule["status"],
                "post_operator_rule_status": post_rule["status"],
                "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
                "operator_scope": resolution["operator_scope"],
                "route_disposition": packet["route_disposition"],
                "scientific_disposition": "NOT_EVALUATED",
                "boundary": "One exact case-bound registered Operator execution. The result is same-packet and subject to the HumanDecisionGate; it emits a route-contract outcome, not a scientific disposition."
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
