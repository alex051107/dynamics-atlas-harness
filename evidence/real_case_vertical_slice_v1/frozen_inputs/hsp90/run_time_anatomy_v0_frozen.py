#!/usr/bin/env python3
"""Catalogue raw two-readout directional blocks in the frozen HSP90 packet.

The script records operational departure/return candidates. It does not build a
kinetic model or infer an NMR-core state transition.
"""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TASK = ROOT
SOURCE = ROOT
FRAMES = SOURCE / "frame_state_assignments.tsv"
ROUTES = SOURCE / "route_predictions.tsv"
OUT = TASK / "outputs"
PERSISTENCE_FRAMES = [5, 20, 50]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def label(row: dict) -> str:
    """Existing zero-sign rule; mixed signs are explicitly not a consensus state."""
    geometry = float(row["geometry_delta_A"])
    contact = float(row["contact_margin_A"])
    if geometry > 0 and contact > 0:
        return "OPEN_CONSENSUS"
    if geometry < 0 and contact < 0:
        return "CLOSED_CONSENSUS"
    return "READOUT_CONFLICT"


def median_route(rows: list[dict]) -> str:
    """Display-only 50-ns bin summary using the same unoptimized zero signs."""
    geometry = statistics.median(float(row["geometry_delta_A"]) for row in rows)
    contact = statistics.median(float(row["contact_margin_A"]) for row in rows)
    if geometry > 0 and contact > 0:
        return "OPEN_CONSENSUS"
    if geometry < 0 and contact < 0:
        return "CLOSED_CONSENSUS"
    return "READOUT_CONFLICT"


def contiguous_runs(labels: list[str]) -> list[dict]:
    runs: list[dict] = []
    start = 0
    current = labels[0]
    for index, value in enumerate(labels[1:], start=1):
        if value != current:
            runs.append({"label": current, "start_index": start, "end_index": index - 1,
                         "length_frames": index - start})
            start, current = index, value
    runs.append({"label": current, "start_index": start, "end_index": len(labels) - 1,
                 "length_frames": len(labels) - start})
    return runs


def opposite(label_value: str) -> str:
    return "CLOSED_CONSENSUS" if label_value == "OPEN_CONSENSUS" else "OPEN_CONSENSUS"


def read_lineage() -> dict[str, str]:
    with ROUTES.open(newline="") as handle:
        return {row["trajectory"]: row["seed_lineage"] for row in csv.DictReader(handle, delimiter="\t")}


def write_tsv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    lineage = read_lineage()
    frames: dict[str, list[dict]] = defaultdict(list)
    with FRAMES.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            frames[row["trajectory"]].append(row)

    block_rows: list[dict] = []
    trajectory_rows: list[dict] = []
    bin_rows: list[dict] = []
    for trajectory, rows in sorted(frames.items()):
        rows = sorted(rows, key=lambda row: float(row["time_ns"]))
        if len(rows) != 1001:
            raise ValueError(f"{trajectory}: expected 1001 saved frames, observed {len(rows)}")
        labels = [label(row) for row in rows]
        runs = contiguous_runs(labels)
        for start in range(0, len(rows), 50):
            subset = rows[start:min(start + 50, len(rows))]
            bin_rows.append({
                "trajectory": trajectory,
                "seed_lineage": lineage[trajectory],
                "bin_index": start // 50 + 1,
                "start_time_ns": float(subset[0]["time_ns"]),
                "end_time_ns": float(subset[-1]["time_ns"]),
                "n_saved_frames": len(subset),
                "bin_route": median_route(subset),
            })
        for run in runs:
            block_rows.append({
                "trajectory": trajectory,
                "seed_lineage": lineage[trajectory],
                "label": run["label"],
                "start_time_ns": float(rows[run["start_index"]]["time_ns"]),
                "end_time_ns": float(rows[run["end_index"]]["time_ns"]),
                "length_saved_frames": run["length_frames"],
                "length_ns": run["length_frames"],
            })
        for horizon in PERSISTENCE_FRAMES:
            persistent = [run for run in runs if run["label"] != "READOUT_CONFLICT" and run["length_frames"] >= horizon]
            start = persistent[0] if persistent else None
            departure = None
            returned = None
            if start:
                for run in persistent[1:]:
                    if departure is None and run["label"] == opposite(start["label"]):
                        departure = run
                    elif departure is not None and run["label"] == start["label"]:
                        returned = run
                        break
            trajectory_rows.append({
                "trajectory": trajectory,
                "seed_lineage": lineage[trajectory],
                "persistence_saved_frames": horizon,
                "persistence_ns": horizon,
                "first_persistent_direction": start["label"] if start else "NO_PERSISTENT_CONSENSUS",
                "first_persistent_start_ns": float(rows[start["start_index"]]["time_ns"]) if start else "",
                "opposite_direction_departure_candidate": bool(departure),
                "opposite_departure_start_ns": float(rows[departure["start_index"]]["time_ns"]) if departure else "",
                "return_candidate": bool(returned),
                "return_start_ns": float(rows[returned["start_index"]]["time_ns"]) if returned else "",
                "strict_core_frames": sum(row["state_core"] != "U" for row in rows),
            })

    write_tsv(OUT / "directional_runs.tsv", block_rows)
    write_tsv(OUT / "trajectory_time_anatomy.tsv", trajectory_rows)
    write_tsv(OUT / "trajectory_time_bins_50ns.tsv", bin_rows)
    summary: dict[str, dict] = {}
    for horizon in PERSISTENCE_FRAMES:
        subset = [row for row in trajectory_rows if row["persistence_saved_frames"] == horizon]
        by_lineage = {}
        for name in sorted({row["seed_lineage"] for row in subset}):
            rows = [row for row in subset if row["seed_lineage"] == name]
            by_lineage[name] = {
                "n_trajectories": len(rows),
                "opposite_departure_candidate_n": sum(row["opposite_direction_departure_candidate"] for row in rows),
                "return_candidate_n": sum(row["return_candidate"] for row in rows),
            }
        summary[str(horizon)] = {
            "n_trajectories": len(subset),
            "opposite_departure_candidate_n": sum(row["opposite_direction_departure_candidate"] for row in subset),
            "return_candidate_n": sum(row["return_candidate"] for row in subset),
            "strict_core_frame_count_total": sum(row["strict_core_frames"] for row in subset),
            "by_seed_lineage": by_lineage,
        }
    result = {
        "task": "dynamics_atlas_hsp90_time_anatomy_v0_20260730",
        "evidence_level": "v0_same_packet_diagnostic",
        "inputs": {
            "frame_state_assignments.tsv": {"sha256": sha256(FRAMES)},
            "route_predictions.tsv": {"sha256": sha256(ROUTES)},
        },
        "statistical_unit": "trajectory (n=40); frame runs are within-trajectory descriptive objects",
        "persistence_grid_saved_frames": PERSISTENCE_FRAMES,
        "display_bin": "50 saved frames (about 50 ns; the last bin has 51 frames)",
        "summary": summary,
        "allowed_wording": "Describes persistent two-readout directional departure and return candidates under an explicit horizon grid.",
        "forbidden_wording": "Does not estimate a transition rate, equilibrium, population, free energy, complete pathway, mechanism, or mutation effect.",
    }
    (OUT / "results_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
