"""Use the common F05R02 bridge once for an admitted 58/134 frozen result."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path

from dynamics_atlas_harness import forward_bridge_use_v1 as bridge
from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


PAIR = "58_134"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text())


def _source_record() -> dict[str, object]:
    return {
        "source_id": "Q15_APBS_58_134",
        "case_evidence_scope": "CLAIM_EVIDENCE",
        "evidence_role": "FIT_TARGET",
        "source_locator": "Peter2022 DOI10.1038/s41467-022-31945-6; Zenodo6683587 Figure3/58_134_apo and Figure3/58_134_1mM_SA; CRC-admitted APBS members; SI Table2 rows1-2.",
        "data_lineage_status": "AGENT_PROPOSED_UNVERIFIED",
        "construct_and_condition": "HiSiaP labeled at 58_134; source-labelled apo and 1mM_SA groups, three repetitions per condition.",
        "sample_composition": "AlexaFluor555/AlexaFluor647 double labels; frozen shared calibration is conditionally applicable.",
        "sample_system_composition_declaration_status": "DECLARED",
        "native_observable": "CRC-admitted APBS photon-count exports AA, DD, DA and burst duration; frozen correction is applied once after source identity validation.",
        "estimand": "Conditional fluorescence efficiency direction under declared correction, compared only with an efficiency-weighted FPS reference direction.",
        "time_semantics": {"kind": "DIFFUSING_SINGLE_MOLECULE_BURSTS"},
        "spatial_support": "Two labeling positions 58_134; not C-alpha geometry or a direct population measurement.",
        "unit_or_aggregation": "Technical segments are pooled only within each of three source-labelled repetitions per condition; repetitions are equally summarized.",
        "native_measurement_declaration_status": "DECLARED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--comparison", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task = args.task_root.resolve()
    comparison_path = args.comparison.resolve()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"REFUSING_TO_OVERWRITE:{output}")
    comparison = _load(comparison_path)
    if comparison.get("version") != "q15-58-134-frozen-reuse/v1" or comparison.get("frozen_policy") != q15.POLICY:
        raise ValueError("FROZEN_READER_REPORT_OR_POLICY_UNAVAILABLE")
    source = _source_record()
    reference = _load(Path(__file__).resolve().parents[1] / "research" / "paper_result_reproduction_screen_v1" / "q15_full_table2_reference_admission_v1.json")
    if reference.get("forward_distance_semantics") != "FRET_EFFICIENCY_AVERAGED_MODEL_DISTANCE":
        raise ValueError("REFERENCE_SEMANTICS_INCOMPATIBLE")
    values = reference["pairs"][PAIR]["FRET_sim"]
    direction = comparison["condition_comparisons"][PAIR]
    diagnostics = comparison["diagnostics"][PAIR]
    scope = {
        "source_id": source["source_id"],
        "model_id": "author-FPS-open-closed-reference",
        "observable": "FRET_E",
        "probe": "AF555_AF647_58_134",
        "condition": "apo:1mM_SA_archive_label",
        "unit": "dimensionless_efficiency",
        "aggregation": "equal_repetition_mean_E_vs_efficiency_weighted_reference_R",
        "target_support": "apo:holo",
    }
    value = {
        "scope": scope,
        "method_id": "efficiency_weighted_reference_direction_v1",
        "data": {
            "reference_definition": "EFFICIENCY_WEIGHTED_DISTANCE",
            "observed_change": direction["holo_minus_apo_E"],
            "reference_apo": values["apo"],
            "reference_holo": values["holo"],
            "direction_checks": [
                diagnostics["equal_repetition_median_effect"],
                *diagnostics["leave_one_per_condition_effects"],
            ],
        },
    }
    use = {
        "contract": bridge.CONTRACT,
        "use_id": "reference-58_134",
        "scope": scope,
        "method_id": value["method_id"],
        "input_ref": "input-reference-58_134",
        "requested_use": "MODEL_OBSERVATION_COMPARISON",
    }
    context = {
        "inputs": {use["input_ref"]: value},
        "admissions": {
            use["input_ref"]: {
                "input_digest": bridge.digest(value),
                "source_receipts": [
                    "q15_58_134_full_input_intake_v1/retry1_receipt.json",
                    "q15_58_134_full_input_intake_v1/input_quality_report.json",
                    "q15-58-134-frozen-reuse/v1/report.json",
                    "q15_full_table2_reference_admission_v1.json",
                ],
                "method_basis": reference["locator"] + "; existing frozen Q15 correction and stable-probe reference hypothesis; no mean-distance conversion.",
                "conditional_assumptions": [
                    "stable-probe reference hypothesis",
                    "efficiency-weighted reference output, not mean distance",
                    "shared frozen calibration remains conditionally applicable",
                ],
                "authority_binding": {
                    "source_id": source["source_id"],
                    "source_version": "Peter2022 Figure3 selected 58/134 members and SI Table2 rows1-2",
                    "measurement_version": "q15-58-134-frozen-reuse/v1",
                    "relationship_to_graph": "LATER_ADMITTED_SOURCE_FOR_CURRENT_USE",
                    "relevant_contradictions": [],
                },
                "role": "NEW_DERIVED_INPUT_ADMISSION_FROM_PRIOR_SOURCES_NOT_SCIENTIFIC_APPROVAL",
            }
        },
    }
    graph = {
        "case": {
            "case_id": "development-q15-58-134-local-direction",
            "intake_kind": "SCIENTIFIC_CLAIM_REVIEW",
            "scientific_claim": "For the admitted 58/134 source exports, does the frozen efficiency direction agree with the published efficiency-weighted FPS reference direction?",
            "requested_claim_level": "LOCAL_MODEL_OBSERVATION_DIRECTION",
            "intended_use": "DEVELOPMENT_REPLAY",
            "observability_target": {"event_signature": "Admitted source-derived local direction check", "target_time_scale": "SOURCE_DECLARED", "target_spatial_scale": "TWO_FLUOROPHORE_LABEL_POSITIONS"},
            "claim_contract": {
                "internal_consistency": "CONSISTENT",
                "declared_request_scope": ["LOCAL_MODEL_OBSERVATION_DIRECTION"],
                "forbidden_upgrades": ["BIOLOGICAL_ACTIVITY", "BACKBONE_DISTANCE_AS_PROBE_DISTANCE", "STRUCTURAL_POPULATION", "FULL_Q15_ANSWER"],
            },
        },
        "evidence_items": [source],
        "comparisons": [],
        "projection_boundary": "One newly admitted source use under frozen F05R02; it has no whole-question verdict.",
        "forward_bridge_uses": [use],
    }
    root = Path(__file__).resolve().parents[1]
    runtime = _load(root / "registries" / "rules_v1" / "runtime_subrules_v1.json")
    bindings = _load(root / "registries" / "rules_v1" / "applicability_bindings_v1.json")
    contracts = _load(root / "registries" / "rules_v1" / "evaluation_contracts_v1.json")
    kwargs = {"case_graph": graph, "runtime_subrules": runtime, "bindings": bindings, "contracts": contracts}
    off = bridge.run_checks(**kwargs, context=context, enabled=False)
    on = bridge.run_checks(**kwargs, context=context, enabled=True)
    reentry_context = copy.deepcopy(context)
    reentry_context["evidence"] = on["evidence"]
    reentry = bridge.run_checks(**kwargs, context=reentry_context, enabled=True)
    def chosen(result: dict[str, object]) -> dict[str, object]:
        return next(row for row in result["after"] if row.get("use_id") == use["use_id"])
    off_row, on_row, reentry_row = chosen(off), chosen(on), chosen(reentry)
    if off_row.get("reason") != "REQUESTED_USE_NUMERICAL_CHECK_MISSING" or off["operator_calls"]:
        raise ValueError("OFF_PATH_DID_NOT_PRESERVE_REGISTERED_OPERATOR")
    if len(on["operator_calls"]) != 1 or not on_row.get("check_completed") or reentry["operator_calls"]:
        raise ValueError("RULES_REENTRY_NOT_REPRODUCIBLE")
    output.mkdir(parents=True)
    for name, payload in (("casegraph", graph), ("admission", context), ("off", off), ("on", on), ("reentry", reentry)):
        (output / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    report = {
        "version": "q15-58-134-forward-bridge/v1",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "comparison_report": str(comparison_path),
        "rule_instance_id": on_row["rule_instance_id"],
        "operator": bridge.RULE_ID,
        "method_id": value["method_id"],
        "off": {key: off_row.get(key) for key in ("status", "route", "reason", "check_completed")},
        "on": {key: on_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support", "numerical", "allowed_conclusion", "claim_ceiling", "conditional_assumptions")},
        "reentry": {key: reentry_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support")},
        "operator_calls": {"off": len(off["operator_calls"]), "on": len(on["operator_calls"]), "reentry": len(reentry["operator_calls"])},
        "new_fits": 0,
        "full_question_count_change": 0,
        "claim_ceiling": "One conditional local 58/134 model-observation direction relation, not a protein-state, activity, absolute-distance, full-Q15 or accuracy conclusion.",
    }
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
