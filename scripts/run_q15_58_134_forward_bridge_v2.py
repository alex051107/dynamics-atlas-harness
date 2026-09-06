"""Run F05R02 only from the verified v2 58/134 producer report."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path, PurePosixPath
from typing import Any

import numpy as np

from dynamics_atlas_harness import forward_bridge_use_v1 as bridge
from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


PAIR = "58_134"
INTAKE = "q15_58_134_full_input_intake_v1"
READER_DIR = "q15_58_134_frozen_reuse_v2"
DIRECTORIES = {"58_134_apo": "apo", "58_134_1mM_SA": "holo"}


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def _identity(member: dict[str, Any]) -> dict[str, Any]:
    return {key: member[key] for key in ("name", "crc32", "expanded_bytes")}


def _assignment(name: str) -> tuple[str, str]:
    parts = PurePosixPath(name).parts
    if len(parts) != 4 or parts[0] != "Figure3" or parts[1] not in DIRECTORIES:
        raise ValueError("UNEXPECTED_SELECTED_MEMBER_IDENTITY")
    return parts[1], parts[2]


def expected_source_map(task: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, list[str]]]]:
    root = task / "outputs" / INTAKE
    selected = _load(root / "selected_members.json")
    receipt = _load(root / "retry1_receipt.json")
    if not receipt.get("source_admission_complete") or receipt.get("passed_members") != 92:
        raise ValueError("COMPLETE_SOURCE_RECEIPT_REQUIRED")
    selected_by_name = {row["name"]: row for row in selected}
    items = receipt["combined_results"]
    names = [item.get("member", {}).get("name") for item in items]
    if len(selected_by_name) != len(selected) or len(names) != len(set(names)) or set(selected_by_name) != set(names):
        raise ValueError("SELECTED_OR_RECEIPT_MEMBER_SET_MISMATCH")
    apbs: list[dict[str, Any]] = []
    groups: dict[str, dict[str, list[str]]] = {}
    for item in items:
        member, name = item["member"], item["member"]["name"]
        if item.get("status") != "LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH" or _identity(member) != _identity(selected_by_name[name]):
            raise ValueError("SOURCE_RECEIPT_IDENTITY_UNAVAILABLE")
        directory, repetition = _assignment(name)
        if item.get("condition_directory") != directory or item.get("source_repetition") != repetition:
            raise ValueError("SOURCE_ASSIGNMENT_RECEIPT_MISMATCH")
        key = f"{directory}/{repetition}"
        groups.setdefault(key, {"apbs": [], "background": []})
        if name.endswith("_apbs_alex.csv"):
            groups[key]["apbs"].append(name)
            apbs.append(_identity(member))
        elif name.endswith("bkg.csv"):
            groups[key]["background"].append(name)
        else:
            raise ValueError("UNEXPECTED_SELECTED_MEMBER_ROLE")
    if len(apbs) != 86 or any(not item["apbs"] or len(item["background"]) != 1 for item in groups.values()) or len(groups) != 6:
        raise ValueError("COMPLETE_APBS_SOURCE_MAP_REQUIRED")
    return sorted(apbs, key=lambda row: row["name"]), {key: {role: sorted(names) for role, names in value.items()} for key, value in sorted(groups.items())}


def _diagnostics(repetitions: list[dict[str, Any]], comparison: dict[str, Any]) -> dict[str, Any]:
    groups = {condition: sorted([row for row in repetitions if row["condition"] == condition], key=lambda row: row["repetition"]) for condition in ("apo", "holo")}
    if any(len(rows) != 3 for rows in groups.values()):
        raise ValueError("THREE_SOURCE_REPETITIONS_REQUIRED")
    means = {condition: np.asarray([row["E"]["mean"] for row in rows], dtype=float) for condition, rows in groups.items()}
    medians = {condition: np.asarray([row["E"]["median"] for row in rows], dtype=float) for condition, rows in groups.items()}
    leave = [float(np.delete(means["holo"], i).mean() - np.delete(means["apo"], j).mean()) for i in range(3) for j in range(3)]
    return {
        "equal_repetition_mean_effect": float(comparison["holo_minus_apo_E"]),
        "equal_repetition_median_effect": float(medians["holo"].mean() - medians["apo"].mean()),
        "leave_one_per_condition_effects": leave,
        "leave_one_per_condition_range": [min(leave), max(leave)],
        "definition": "mean(within-repetition E.median) holo minus apo; retained from q15_pro19_verification_v1",
        "interpretation": "Existing equal-repetition direction sensitivity only; no added experiment, fit, confidence interval or structural inference.",
    }


def validate_producer_report(report: dict[str, Any], expected_members: list[dict[str, Any]], expected_groups: dict[str, dict[str, list[str]]]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Rebuild every bridge input from a producer report instead of trusting fields."""
    if report.get("version") != "q15-58-134-frozen-reuse/v2" or report.get("frozen_policy") != q15.POLICY:
        raise ValueError("FROZEN_READER_REPORT_OR_POLICY_UNAVAILABLE")
    selection = report.get("source_selection", {})
    if selection.get("pair") != PAIR or selection.get("member_identity") != expected_members or selection.get("apbs_members") != len(expected_members):
        raise ValueError("PRODUCER_MEMBER_IDENTITY_MISMATCH")
    if report.get("source_assignment", {}).get("groups") != expected_groups:
        raise ValueError("PRODUCER_SOURCE_ASSIGNMENT_MISMATCH")
    if report.get("source_receipts") != ["q15_58_134_full_input_intake_v1/retry1_receipt.json", "q15_58_134_full_input_intake_v1/input_quality_report.json"]:
        raise ValueError("PRODUCER_SOURCE_RECEIPT_MISMATCH")
    repetitions = report.get("repetitions")
    if not isinstance(repetitions, list) or len(repetitions) != 6 or any(row.get("pair") != PAIR for row in repetitions):
        raise ValueError("PRODUCER_REPETITION_SUMMARY_UNAVAILABLE")
    rebuilt_comparison = q15.group_difference(repetitions)[PAIR]
    if report.get("condition_comparisons") != {PAIR: rebuilt_comparison}:
        raise ValueError("PRODUCER_COMPARISON_MISMATCH")
    rebuilt_diagnostics = _diagnostics(repetitions, rebuilt_comparison)
    if report.get("diagnostics") != {PAIR: rebuilt_diagnostics}:
        raise ValueError("PRODUCER_DIAGNOSTIC_MISMATCH")
    return rebuilt_comparison, rebuilt_diagnostics


def _source_record() -> dict[str, Any]:
    return {
        "source_id": "Q15_APBS_58_134", "case_evidence_scope": "CLAIM_EVIDENCE", "evidence_role": "FIT_TARGET",
        "source_locator": "Peter2022 DOI10.1038/s41467-022-31945-6; Zenodo6683587 Figure3/58_134_apo and Figure3/58_134_1mM_SA; CRC-admitted APBS members; SI Table2 rows1-2.",
        "data_lineage_status": "AGENT_PROPOSED_UNVERIFIED", "construct_and_condition": "HiSiaP labeled at 58_134; source-labelled apo and 1mM_SA groups, three repetitions per condition.",
        "sample_composition": "AlexaFluor555/AlexaFluor647 double labels; frozen shared calibration is conditionally applicable.", "sample_system_composition_declaration_status": "DECLARED",
        "native_observable": "CRC-admitted APBS photon-count exports AA, DD, DA and burst duration; frozen correction is applied once after source identity validation.",
        "estimand": "Conditional fluorescence efficiency direction under declared correction, compared only with an efficiency-weighted FPS reference direction.",
        "time_semantics": {"kind": "DIFFUSING_SINGLE_MOLECULE_BURSTS"}, "spatial_support": "Two labeling positions 58_134; not C-alpha geometry or a direct population measurement.",
        "unit_or_aggregation": "Technical segments are pooled only within each of three source-labelled repetitions per condition; repetitions are equally summarized.", "native_measurement_declaration_status": "DECLARED",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--comparison", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task, comparison_path, output = args.task_root.resolve(), args.comparison.resolve(), args.output.resolve()
    expected_path = task / "outputs" / READER_DIR / "report.json"
    if comparison_path != expected_path or output.exists():
        raise ValueError("EXPECTED_V2_PRODUCER_PATH_REQUIRED" if comparison_path != expected_path else f"REFUSING_TO_OVERWRITE:{output}")
    expected_members, expected_groups = expected_source_map(task)
    report = _load(comparison_path)
    direction, diagnostics = validate_producer_report(report, expected_members, expected_groups)
    root = Path(__file__).resolve().parents[1]
    reference = _load(root / "research" / "paper_result_reproduction_screen_v1" / "q15_full_table2_reference_admission_v1.json")
    if reference.get("forward_distance_semantics") != "FRET_EFFICIENCY_AVERAGED_MODEL_DISTANCE":
        raise ValueError("REFERENCE_SEMANTICS_INCOMPATIBLE")
    source = _source_record()
    scope = {"source_id": source["source_id"], "model_id": "author-FPS-open-closed-reference", "observable": "FRET_E", "probe": "AF555_AF647_58_134", "condition": "apo:1mM_SA_archive_label", "unit": "dimensionless_efficiency", "aggregation": "equal_repetition_mean_E_vs_efficiency_weighted_reference_R", "target_support": "apo:holo"}
    value = {"scope": scope, "method_id": "efficiency_weighted_reference_direction_v1", "data": {"reference_definition": "EFFICIENCY_WEIGHTED_DISTANCE", "observed_change": direction["holo_minus_apo_E"], "reference_apo": reference["pairs"][PAIR]["FRET_sim"]["apo"], "reference_holo": reference["pairs"][PAIR]["FRET_sim"]["holo"], "direction_checks": [diagnostics["equal_repetition_median_effect"], *diagnostics["leave_one_per_condition_effects"]]}}
    use = {"contract": bridge.CONTRACT, "use_id": "reference-58_134-v2", "scope": scope, "method_id": value["method_id"], "input_ref": "input-reference-58_134-v2", "requested_use": "MODEL_OBSERVATION_COMPARISON"}
    context = {"inputs": {use["input_ref"]: value}, "admissions": {use["input_ref"]: {"input_digest": bridge.digest(value), "source_receipts": ["q15_58_134_full_input_intake_v1/retry1_receipt.json", "q15_58_134_full_input_intake_v1/input_quality_report.json", "q15-58-134-frozen-reuse/v2/report.json", "q15_full_table2_reference_admission_v1.json"], "method_basis": reference["locator"] + "; existing frozen Q15 correction and stable-probe reference hypothesis; no mean-distance conversion.", "conditional_assumptions": ["stable-probe reference hypothesis", "efficiency-weighted reference output, not mean distance", "shared frozen calibration remains conditionally applicable"], "authority_binding": {"source_id": source["source_id"], "source_version": "Peter2022 Figure3 selected 58/134 members and SI Table2 rows1-2", "measurement_version": "q15-58-134-frozen-reuse/v2", "relationship_to_graph": "LATER_ADMITTED_SOURCE_FOR_CURRENT_USE", "relevant_contradictions": []}, "role": "NEW_DERIVED_INPUT_ADMISSION_FROM_PRIOR_SOURCES_NOT_SCIENTIFIC_APPROVAL"}}}
    graph = {"case": {"case_id": "development-q15-58-134-local-direction-v2", "intake_kind": "SCIENTIFIC_CLAIM_REVIEW", "scientific_claim": "For the admitted 58/134 source exports, does the frozen efficiency direction agree with the published efficiency-weighted FPS reference direction?", "requested_claim_level": "LOCAL_MODEL_OBSERVATION_DIRECTION", "intended_use": "DEVELOPMENT_REPLAY", "observability_target": {"event_signature": "Admitted source-derived local direction check", "target_time_scale": "SOURCE_DECLARED", "target_spatial_scale": "TWO_FLUOROPHORE_LABEL_POSITIONS"}, "claim_contract": {"internal_consistency": "CONSISTENT", "declared_request_scope": ["LOCAL_MODEL_OBSERVATION_DIRECTION"], "forbidden_upgrades": ["BIOLOGICAL_ACTIVITY", "BACKBONE_DISTANCE_AS_PROBE_DISTANCE", "STRUCTURAL_POPULATION", "FULL_Q15_ANSWER"]}}, "evidence_items": [source], "comparisons": [], "projection_boundary": "One v2 source-bound use under frozen F05R02; it has no whole-question verdict.", "forward_bridge_uses": [use]}
    kwargs = {"case_graph": graph, "runtime_subrules": _load(root / "registries/rules_v1/runtime_subrules_v1.json"), "bindings": _load(root / "registries/rules_v1/applicability_bindings_v1.json"), "contracts": _load(root / "registries/rules_v1/evaluation_contracts_v1.json")}
    off = bridge.run_checks(**kwargs, context=context, enabled=False)
    on = bridge.run_checks(**kwargs, context=context, enabled=True)
    reentry_context = copy.deepcopy(context); reentry_context["evidence"] = on["evidence"]
    reentry = bridge.run_checks(**kwargs, context=reentry_context, enabled=True)
    pick = lambda result: next(row for row in result["after"] if row.get("use_id") == use["use_id"])
    off_row, on_row, reentry_row = pick(off), pick(on), pick(reentry)
    if off_row.get("reason") != "REQUESTED_USE_NUMERICAL_CHECK_MISSING" or off["operator_calls"] or len(on["operator_calls"]) != 1 or not on_row.get("check_completed") or reentry["operator_calls"]:
        raise ValueError("RULES_REENTRY_NOT_REPRODUCIBLE")
    output.mkdir(parents=True)
    for name, payload in (("casegraph", graph), ("admission", context), ("off", off), ("on", on), ("reentry", reentry)):
        (output / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    result = {"version": "q15-58-134-forward-bridge/v2", "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(), "comparison_report": str(comparison_path), "rule_instance_id": on_row["rule_instance_id"], "operator": bridge.RULE_ID, "method_id": value["method_id"], "producer_reconstructed": True, "off": {key: off_row.get(key) for key in ("status", "route", "reason", "check_completed")}, "on": {key: on_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support", "numerical", "allowed_conclusion", "claim_ceiling", "conditional_assumptions")}, "reentry": {key: reentry_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support")}, "operator_calls": {"off": len(off["operator_calls"]), "on": len(on["operator_calls"]), "reentry": len(reentry["operator_calls"])}, "new_fits": 0, "full_question_count_change": 0, "claim_ceiling": "One conditional local 58/134 model-observation direction relation, not a protein-state, activity, absolute-distance, full-Q15 or accuracy conclusion."}
    (output / "report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
