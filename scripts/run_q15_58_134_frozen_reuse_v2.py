"""Read the admitted 58/134 source set with frozen Q15 functions and bindings.

Version 2 preserves v1 as the first replay.  It restores the previous
within-repetition-median sensitivity estimand and derives grouping exclusively
from the selected ZIP-member identity before consuming any APBS bytes.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import time
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any

import numpy as np

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


INTAKE = "q15_58_134_full_input_intake_v1"
PAIR = "58_134"
DIRECTORY_TO_CONDITION = {"58_134_apo": "apo", "58_134_1mM_SA": "holo"}
EXPECTED_GROUPS = {
    (directory, f"repetion_{number}")
    for directory in DIRECTORY_TO_CONDITION
    for number in (1, 2, 3)
}
EXPECTED_METADATA = {
    "timeResolution": "1.250000e-008",
    "arrivalWindow": "5.000000e-004",
    "minNeighbors": "15",
    "minPhotPerBurst": "50",
    "reductionMode": "0",
}
COUNT_FIELDS = ("F_Dexc_Dem", "F_Dexc_Aem", "F_Aexc_Aem")


def assignment_from_member_name(name: str) -> tuple[str, str]:
    """Return the declared archive directory and source repetition from identity."""
    parts = PurePosixPath(name).parts
    if len(parts) != 4 or parts[0] != "Figure3" or parts[1] not in DIRECTORY_TO_CONDITION:
        raise ValueError("UNEXPECTED_SELECTED_MEMBER_IDENTITY")
    directory, repetition = parts[1], parts[2]
    if (directory, repetition) not in EXPECTED_GROUPS:
        raise ValueError("UNEXPECTED_SELECTED_MEMBER_GROUP")
    return directory, repetition


def _identity(member: dict[str, Any]) -> dict[str, Any]:
    return {key: member[key] for key in ("name", "crc32", "expanded_bytes")}


def validate_admitted_member_map(
    selected_members: list[dict[str, Any]], combined_results: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], dict[tuple[str, str], dict[str, list[str]]]]:
    """Bind receipt fields to the selected central-directory member identities."""
    selected_by_name = {row["name"]: row for row in selected_members}
    combined_names = [item.get("member", {}).get("name") for item in combined_results]
    if len(selected_by_name) != len(selected_members) or len(set(combined_names)) != len(combined_names):
        raise ValueError("SELECTED_OR_RECEIPT_MEMBER_SET_NOT_UNIQUE")
    if set(selected_by_name) != set(combined_names):
        raise ValueError("SELECTED_OR_RECEIPT_MEMBER_SET_MISMATCH")
    grouped: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(lambda: {"apbs": [], "background": []})
    admitted_apbs = []
    for item in combined_results:
        if item.get("status") != "LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH":
            raise ValueError("UNVERIFIED_MEMBER")
        member = item["member"]
        name = member["name"]
        selected = selected_by_name[name]
        if _identity(member) != _identity(selected):
            raise ValueError("SELECTED_AND_RECEIPT_IDENTITY_MISMATCH")
        directory, repetition = assignment_from_member_name(name)
        if item.get("condition_directory") != directory or item.get("source_repetition") != repetition:
            raise ValueError("SOURCE_ASSIGNMENT_RECEIPT_MISMATCH")
        group = grouped[(directory, repetition)]
        if name.endswith("_apbs_alex.csv"):
            group["apbs"].append(name)
            admitted_apbs.append(dict(_identity(member), path=item["path"], directory=directory, repetition=repetition))
        elif name.endswith("bkg.csv"):
            group["background"].append(name)
        else:
            raise ValueError("UNEXPECTED_SELECTED_MEMBER_ROLE")
    if set(grouped) != EXPECTED_GROUPS or any(not values["apbs"] or len(values["background"]) != 1 for values in grouped.values()):
        raise ValueError("SIX_COMPLETE_SOURCE_GROUPS_REQUIRED")
    admitted_apbs.sort(key=lambda row: row["name"])
    if len(admitted_apbs) != 86:
        raise ValueError("EXPECTED_86_UNIQUE_APBS_MEMBERS")
    return admitted_apbs, grouped


def _load_csv(data: bytes) -> list[dict[str, str]]:
    lines = data.decode("utf-8").splitlines()
    try:
        marker = lines.index("DATA")
    except ValueError as exc:
        raise ValueError("APBS_DATA_MARKER_UNAVAILABLE") from exc
    metadata = dict(csv.reader(lines[1:marker]))
    rows = list(csv.DictReader(lines[marker + 1 :]))
    if not rows or set(COUNT_FIELDS + ("Len", "Tau")) - set(rows[0]):
        raise ValueError("APBS_REQUIRED_COLUMNS_UNAVAILABLE")
    if {key: metadata.get(key) for key in EXPECTED_METADATA} != EXPECTED_METADATA:
        raise ValueError("APBS_SOURCE_POLICY_METADATA_CHANGED")
    return rows


def direction_diagnostics(repetitions: list[dict[str, Any]], comparison: dict[str, Any]) -> dict[str, Any]:
    """Use the historical mean-of-within-repetition-medians sensitivity."""
    groups = {
        condition: sorted(
            [row for row in repetitions if row["condition"] == condition],
            key=lambda row: row["repetition"],
        )
        for condition in ("apo", "holo")
    }
    if any(len(rows) != 3 for rows in groups.values()):
        raise ValueError("THREE_SOURCE_REPETITIONS_REQUIRED")
    means = {condition: np.asarray([row["E"]["mean"] for row in rows], dtype=float) for condition, rows in groups.items()}
    medians = {condition: np.asarray([row["E"]["median"] for row in rows], dtype=float) for condition, rows in groups.items()}
    leave_one = [
        float(np.delete(means["holo"], drop_holo).mean() - np.delete(means["apo"], drop_apo).mean())
        for drop_holo in range(3)
        for drop_apo in range(3)
    ]
    return {
        "equal_repetition_mean_effect": float(comparison["holo_minus_apo_E"]),
        "equal_repetition_median_effect": float(medians["holo"].mean() - medians["apo"].mean()),
        "leave_one_per_condition_effects": leave_one,
        "leave_one_per_condition_range": [min(leave_one), max(leave_one)],
        "definition": "mean(within-repetition E.median) holo minus apo; retained from q15_pro19_verification_v1",
        "interpretation": "Existing equal-repetition direction sensitivity only; no added experiment, fit, confidence interval or structural inference.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task, output = args.task_root.resolve(), args.output.resolve()
    if output.exists():
        raise FileExistsError(f"REFUSING_TO_OVERWRITE:{output}")
    source_root = task / "outputs" / INTAKE
    receipt = json.loads((source_root / "retry1_receipt.json").read_text())
    quality = json.loads((source_root / "input_quality_report.json").read_text())
    selected = json.loads((source_root / "selected_members.json").read_text())
    if not receipt.get("source_admission_complete") or receipt.get("passed_members") != 92 or receipt.get("failed_members") != 0:
        raise ValueError("COMPLETE_92_MEMBER_RECEIPT_REQUIRED")
    if quality.get("source_admission") != "COMPLETE" or not quality.get("apbs", {}).get("matches_frozen_export_policy"):
        raise ValueError("FROZEN_EXPORT_POLICY_APPLICABILITY_UNAVAILABLE")
    if quality.get("frozen_policy") != q15.POLICY:
        raise ValueError("FROZEN_POLICY_CHANGED")
    admitted_apbs, assignment_groups = validate_admitted_member_map(selected, receipt["combined_results"])
    started = time.monotonic()
    workspace = task.parents[2]
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for member in admitted_apbs:
        relative = Path(member["path"])
        path = relative if relative.is_absolute() else workspace / relative
        if source_root not in path.resolve().parents:
            raise ValueError("SOURCE_MEMBER_PATH_OUTSIDE_ADMITTED_ROOT")
        data = path.read_bytes()
        q15.validate_member_bytes(data, member)
        rows = _load_csv(data)
        counts = np.asarray([[float(row[field]) for field in COUNT_FIELDS] for row in rows])
        duration = np.asarray([float(row["Tau"]) for row in rows])
        length = np.asarray([float(row["Len"]) for row in rows])
        if not np.array_equal(counts.sum(axis=1), length):
            raise ValueError("RAW_LENGTH_IDENTITY_FAILED")
        corrected = q15.correct(counts, duration)
        grouped[(member["directory"], member["repetition"])].append(
            {"rows": len(rows), "selected_E": corrected["E"][corrected["selected"]], "eligible": int(corrected["eligible"].sum()), "selected": int(corrected["selected"].sum())}
        )
    repetitions = []
    for (directory, repetition), files in sorted(grouped.items()):
        values = np.concatenate([record["selected_E"] for record in files])
        repetitions.append({
            "pair": PAIR, "condition": DIRECTORY_TO_CONDITION[directory], "repetition": repetition,
            "E": q15.summarize(values), "raw_bursts": sum(record["rows"] for record in files),
            "eligible_bursts": sum(record["eligible"] for record in files), "selected_bursts": sum(record["selected"] for record in files),
            "technical_segments": len(files),
        })
    comparison = q15.group_difference(repetitions)[PAIR]
    report = {
        "version": "q15-58-134-frozen-reuse/v2", "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_receipts": ["q15_58_134_full_input_intake_v1/retry1_receipt.json", "q15_58_134_full_input_intake_v1/input_quality_report.json"],
        "source_selection": {"pair": PAIR, "conditions": {"apo": "Figure3/58_134_apo", "holo": "Figure3/58_134_1mM_SA"}, "source_repetitions_per_condition": 3, "apbs_members": len(admitted_apbs), "background_members_used_for_recalculation": 0, "member_identity": [{key: value for key, value in row.items() if key in {"name", "crc32", "expanded_bytes"}} for row in admitted_apbs]},
        "source_assignment": {"derived_from": "selected ZIP-member identity", "groups": {"/".join(key): {role: sorted(value) for role, value in values.items()} for key, values in sorted(assignment_groups.items())}},
        "frozen_policy": q15.POLICY, "policy_applicability": quality["policy_applicability"],
        "repetitions": repetitions, "condition_comparisons": {PAIR: comparison}, "diagnostics": {PAIR: direction_diagnostics(repetitions, comparison)},
        "numerical_calculation": True, "rules_runs": 0, "fits": 0, "execution_seconds": round(time.monotonic() - started, 6),
        "claim_ceiling": "Corrected source ALEX efficiency comparison under the frozen shared policy; no absolute distance, protein state, saturation, population or full-Q15 inference.",
    }
    output.mkdir(parents=True)
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"pair": PAIR, "comparison": comparison, "diagnostics": report["diagnostics"][PAIR]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
