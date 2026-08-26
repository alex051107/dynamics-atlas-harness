#!/usr/bin/env python3
"""Generate the fixed exposed X-EISD vertical-slice receipts.

The output location is intentionally fixed inside this repository. The script has no
network, Operator, Agent, or generic scheduler path.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

from dynamics_atlas_harness.real_case_vertical_slice_v1 import (
    X_EISD_CASE_ID,
    apply_lookup_result,
    derive_declaration_attestations,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_json_object,
    load_rules_v1_bundle,
    materialize_xeisd_conclusion_packet,
)


REPO_ROOT = Path(__file__).parents[1]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
OUTPUT_ROOT = EVIDENCE_ROOT / "outputs"


def write_json(name: str, payload: object) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    (OUTPUT_ROOT / name).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def request_for(allowlist: dict, lookup_id: str) -> dict:
    entry = next(item for item in allowlist["entries"] if item["lookup_id"] == lookup_id)
    return {
        "lookup_id": lookup_id,
        "case_id": X_EISD_CASE_ID,
        "target_kind": entry["target_kind"],
        "target_id": entry["target_id"],
        "locator_id": entry["locator_id"],
    }


def main() -> None:
    seed = load_json_object(EVIDENCE_ROOT / "xeisd_case_projection_seed_v1.json")
    allowlist = load_json_object(EVIDENCE_ROOT / "xeisd_source_lookup_allowlist_v1.json")
    bundle = load_rules_v1_bundle(REPO_ROOT / "registries" / "rules_v1")

    a1_graph = copy.deepcopy(seed)
    a1_lookups = []
    for lookup_id in (
        "XEI-LOOKUP-RANDOM-DECLARATIONS",
        "XEI-LOOKUP-JCOUPLING-DECLARATIONS",
        "XEI-LOOKUP-RANDOM-JCOUPLING-EDGE",
    ):
        result = execute_exact_source_lookup(
            allowlist=allowlist,
            request=request_for(allowlist, lookup_id),
            workspace_root=REPO_ROOT,
        )
        a1_lookups.append(result)
        a1_graph = apply_lookup_result(case_graph=a1_graph, lookup_result=result)
    a1_graph = derive_declaration_attestations(
        case_graph=a1_graph, lookup_results=a1_lookups
    )
    a1_results = evaluate_xeisd_case(case_graph=a1_graph, **bundle)
    a1_packet = materialize_xeisd_conclusion_packet(
        case_graph=a1_graph,
        rule_results=a1_results,
        lookup_results=a1_lookups,
        scenario_id="A1_COMPLETE_LOOKUP_THEN_DIRECT",
    )

    a2_graph = copy.deepcopy(a1_graph)
    a2_graph["evidence_items"][0].pop("sample_composition")
    a2_results = evaluate_xeisd_case(case_graph=a2_graph, **bundle)
    a2_lookup = execute_exact_source_lookup(
        allowlist=allowlist,
        request={
            "lookup_id": "XEI-LOOKUP-MISSING-COMPOSITION",
            "case_id": X_EISD_CASE_ID,
            "target_kind": "SOURCE",
            "target_id": "xeisd_random_candidate_pool",
            "locator_id": "XEI-M04",
        },
        workspace_root=REPO_ROOT,
    )
    a2_packet = materialize_xeisd_conclusion_packet(
        case_graph=a2_graph,
        rule_results=a2_results,
        lookup_results=[a2_lookup],
        scenario_id="A2_MISSING_COMPOSITION",
    )

    a3_graph = copy.deepcopy(a1_graph)
    a3_graph["comparisons"][0]["condition_relation"] = "MISMATCH"
    a3_results = evaluate_xeisd_case(case_graph=a3_graph, **bundle)
    a3_packet = materialize_xeisd_conclusion_packet(
        case_graph=a3_graph,
        rule_results=a3_results,
        lookup_results=a1_lookups,
        scenario_id="A3_EXPLICIT_CONDITION_MISMATCH",
    )

    write_json("xeisd_a1_complete_casegraph.json", a1_graph)
    write_json("xeisd_a1_lookup_receipts.json", a1_lookups)
    write_json("xeisd_a1_conclusion_packet.json", a1_packet)
    write_json("xeisd_a2_conclusion_packet.json", a2_packet)
    write_json("xeisd_a3_conclusion_packet.json", a3_packet)
    write_json(
        "run_receipt.json",
        {
            "run_kind": "EXPOSED_X_EISD_VERTICAL_SLICE_V1_ALPHA",
            "case_id": X_EISD_CASE_ID,
            "network_accessed": False,
            "operator_results": [],
            "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
            "scientific_disposition": "NOT_EVALUATED",
            "lookup_kind": "EXACT_REVIEW_DERIVATIVE_ATTESTATION",
            "route_dispositions": {
                "A1": a1_packet["route_disposition"],
                "A2": a2_packet["route_disposition"],
                "A3": a3_packet["route_disposition"],
            },
            "boundary": "Exact predeclared review-derivative attestation receipts. No free-text source extraction, source-science validation, scientific disposition, registered Operator, or Agent run occurred."
        },
    )


if __name__ == "__main__":
    main()
