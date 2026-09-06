"""Read one admitted 58/134 source set with the frozen Q15 functions only.

This is deliberately a narrow research-side reader: it accepts only the six
already-admitted source-labelled groups and reuses the existing APBS correction,
summary and equal-repetition comparison functions.  It does not replace shared
backgrounds with per-repetition exports, fit a model, or make a structural claim.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


INTAKE = "q15_58_134_full_input_intake_v1"
PAIR = "58_134"
EXPECTED_GROUPS = {
    (condition, f"repetion_{number}")
    for condition in ("58_134_apo", "58_134_1mM_SA")
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


def _load_csv(data: bytes) -> tuple[dict[str, str], list[dict[str, str]]]:
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
    return metadata, rows


def _direction_diagnostics(comparison: dict[str, object]) -> dict[str, object]:
    apo = np.asarray(comparison["apo_repetition_means"], dtype=float)
    holo = np.asarray(comparison["holo_repetition_means"], dtype=float)
    effect = float(comparison["holo_minus_apo_E"])
    leave_one = [
        float(np.delete(holo, drop_holo).mean() - np.delete(apo, drop_apo).mean())
        for drop_holo in range(3)
        for drop_apo in range(3)
    ]
    return {
        "equal_repetition_mean_effect": effect,
        "equal_repetition_median_effect": float(np.median(holo) - np.median(apo)),
        "leave_one_per_condition_effects": leave_one,
        "leave_one_per_condition_range": [min(leave_one), max(leave_one)],
        "interpretation": "Existing equal-repetition direction sensitivity only; no added experiment, fit, confidence interval or structural inference.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task = args.task_root.resolve()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"REFUSING_TO_OVERWRITE:{output}")

    source_root = task / "outputs" / INTAKE
    receipt = json.loads((source_root / "retry1_receipt.json").read_text())
    quality = json.loads((source_root / "input_quality_report.json").read_text())
    if not receipt.get("source_admission_complete") or receipt.get("passed_members") != 92 or receipt.get("failed_members") != 0:
        raise ValueError("COMPLETE_92_MEMBER_RECEIPT_REQUIRED")
    if quality.get("source_admission") != "COMPLETE" or not quality.get("apbs", {}).get("matches_frozen_export_policy"):
        raise ValueError("FROZEN_EXPORT_POLICY_APPLICABILITY_UNAVAILABLE")
    if quality.get("frozen_policy") != q15.POLICY:
        raise ValueError("FROZEN_POLICY_CHANGED")

    started = time.monotonic()
    workspace = task.parents[2]
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    member_manifest = []
    for item in receipt["combined_results"]:
        if item.get("status") != "LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH":
            raise ValueError("UNVERIFIED_MEMBER")
        member = item["member"]
        name = member["name"]
        if not name.endswith("_apbs_alex.csv"):
            continue
        key = (item["condition_directory"], item["source_repetition"])
        if key not in EXPECTED_GROUPS:
            raise ValueError("UNEXPECTED_SOURCE_GROUP")
        relative = Path(item["path"])
        path = relative if relative.is_absolute() else workspace / relative
        if source_root not in path.resolve().parents:
            raise ValueError("SOURCE_MEMBER_PATH_OUTSIDE_ADMITTED_ROOT")
        data = path.read_bytes()
        q15.validate_member_bytes(data, member)
        _, rows = _load_csv(data)
        counts = np.asarray([[float(row[field]) for field in COUNT_FIELDS] for row in rows])
        duration = np.asarray([float(row["Tau"]) for row in rows])
        length = np.asarray([float(row["Len"]) for row in rows])
        if not np.array_equal(counts.sum(axis=1), length):
            raise ValueError("RAW_LENGTH_IDENTITY_FAILED")
        corrected = q15.correct(counts, duration)
        grouped[key].append(
            {
                "name": name,
                "rows": len(rows),
                "selected_E": corrected["E"][corrected["selected"]],
                "eligible": int(corrected["eligible"].sum()),
                "selected": int(corrected["selected"].sum()),
                "member": {
                    "name": name,
                    "crc32": member["crc32"],
                    "expanded_bytes": member["expanded_bytes"],
                },
            }
        )

    if set(grouped) != EXPECTED_GROUPS or sum(len(value) for value in grouped.values()) != 86:
        raise ValueError("EXPECTED_86_APBS_MEMBERS_IN_SIX_GROUPS")
    repetitions = []
    for (directory, repetition), files in sorted(grouped.items()):
        values = np.concatenate([record["selected_E"] for record in files])
        condition = "apo" if directory == "58_134_apo" else "holo"
        repetitions.append(
            {
                "pair": PAIR,
                "condition": condition,
                "repetition": repetition,
                "E": q15.summarize(values),
                "raw_bursts": sum(record["rows"] for record in files),
                "eligible_bursts": sum(record["eligible"] for record in files),
                "selected_bursts": sum(record["selected"] for record in files),
                "technical_segments": len(files),
            }
        )
        member_manifest.extend(record["member"] for record in files)
    comparison = q15.group_difference(repetitions)[PAIR]
    report = {
        "version": "q15-58-134-frozen-reuse/v1",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_receipts": [
            "q15_58_134_full_input_intake_v1/retry1_receipt.json",
            "q15_58_134_full_input_intake_v1/input_quality_report.json",
        ],
        "source_selection": {
            "pair": PAIR,
            "conditions": {"apo": "Figure3/58_134_apo", "holo": "Figure3/58_134_1mM_SA"},
            "source_repetitions_per_condition": 3,
            "apbs_members": len(member_manifest),
            "background_members_used_for_recalculation": 0,
            "member_identity": member_manifest,
        },
        "frozen_policy": q15.POLICY,
        "policy_applicability": quality["policy_applicability"],
        "repetitions": repetitions,
        "condition_comparisons": {PAIR: comparison},
        "diagnostics": {PAIR: _direction_diagnostics(comparison)},
        "numerical_calculation": True,
        "rules_runs": 0,
        "fits": 0,
        "execution_seconds": round(time.monotonic() - started, 6),
        "claim_ceiling": "Corrected source ALEX efficiency comparison under the frozen shared policy; no absolute distance, protein state, saturation, population or full-Q15 inference.",
    }
    output.mkdir(parents=True)
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"pair": PAIR, "comparison": comparison, "diagnostics": report["diagnostics"][PAIR]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
