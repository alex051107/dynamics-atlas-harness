"""Package-backed, group-preserving observable sampling descriptions.

This is a narrow development analysis adapter, not a Rule evaluator, Operator, or
equilibration detector. It uses PyMBAR's public timeseries estimator for each
trajectory independently and keeps declared trajectory/group identity intact.
"""

from __future__ import annotations

import importlib.metadata
import json
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import numpy as np
from pymbar import timeseries


class SamplingDiagnosticsError(ValueError):
    """Raised when a frozen observable or its identity manifest is invalid."""


def _read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise SamplingDiagnosticsError("GROUP_MANIFEST_MUST_BE_OBJECT")
    return value


def _finite_matrix(path: Path) -> np.ndarray:
    try:
        matrix = np.load(path, allow_pickle=False)
    except (OSError, ValueError) as error:
        raise SamplingDiagnosticsError("OBSERVABLE_ARRAY_UNREADABLE") from error
    if matrix.ndim != 2 or matrix.shape[0] < 1 or matrix.shape[1] < 2:
        raise SamplingDiagnosticsError("OBSERVABLE_ARRAY_MUST_BE_NONEMPTY_2D")
    if not np.issubdtype(matrix.dtype, np.number) or not np.isfinite(matrix).all():
        raise SamplingDiagnosticsError("OBSERVABLE_ARRAY_MUST_BE_FINITE_NUMERIC")
    return np.asarray(matrix, dtype=np.float64)


def _row_groups(path: Path, expected_rows: int) -> list[dict[str, str | int]]:
    manifest = _read_json(path)
    if manifest.get("schema_version") != "hsp90-trajectory-group-manifest/v1":
        raise SamplingDiagnosticsError("UNEXPECTED_GROUP_MANIFEST_SCHEMA")
    rows = manifest.get("rows")
    groups = manifest.get("groups")
    if not isinstance(rows, list) or not isinstance(groups, list):
        raise SamplingDiagnosticsError("GROUP_MANIFEST_ROWS_OR_GROUPS_INVALID")
    declared_group_ids = {
        group.get("group_id")
        for group in groups
        if isinstance(group, Mapping) and isinstance(group.get("group_id"), str)
    }
    if len(declared_group_ids) != len(groups) or not declared_group_ids:
        raise SamplingDiagnosticsError("GROUP_MANIFEST_GROUP_IDS_INVALID")
    if len(rows) != expected_rows:
        raise SamplingDiagnosticsError("TRAJECTORY_ID_COUNT_DOES_NOT_MATCH_OBSERVABLE_ROWS")

    normalized: list[dict[str, str | int]] = []
    seen_ids: set[str] = set()
    for expected_index, row in enumerate(rows):
        if not isinstance(row, Mapping) or set(row) != {"row_index", "trajectory_id", "group_id"}:
            raise SamplingDiagnosticsError("GROUP_MANIFEST_ROW_INVALID")
        row_index = row.get("row_index")
        trajectory_id = row.get("trajectory_id")
        group_id = row.get("group_id")
        if row_index != expected_index:
            raise SamplingDiagnosticsError("GROUP_MANIFEST_ROW_ORDER_INVALID")
        if not isinstance(trajectory_id, str) or not trajectory_id or trajectory_id in seen_ids:
            raise SamplingDiagnosticsError("GROUP_MANIFEST_TRAJECTORY_ID_INVALID")
        if not isinstance(group_id, str) or group_id not in declared_group_ids:
            raise SamplingDiagnosticsError("GROUP_MANIFEST_GROUP_ID_INVALID")
        seen_ids.add(trajectory_id)
        normalized.append(
            {"row_index": row_index, "trajectory_id": trajectory_id, "group_id": group_id}
        )
    return normalized


def _summary(values: Sequence[float]) -> dict[str, float | int]:
    array = np.asarray(values, dtype=np.float64)
    return {
        "trajectory_count": int(array.size),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "minimum": float(np.min(array)),
        "maximum": float(np.max(array)),
    }


def run_grouped_observable_sampling_diagnostics(
    *,
    observable_path: str | Path,
    trajectory_group_manifest_path: str | Path,
    observable_id: str,
    analysis_window_label: str,
) -> dict[str, Any]:
    """Describe trajectory-local autocorrelation and effective sample size.

    The result is intentionally descriptive. It never asserts global equilibration,
    population convergence, inter-group biological differences, or a Rule outcome.
    """

    matrix = _finite_matrix(Path(observable_path))
    row_groups = _row_groups(Path(trajectory_group_manifest_path), matrix.shape[0])
    per_trajectory: list[dict[str, Any]] = []
    values_by_group: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for row, identity in zip(matrix, row_groups, strict=True):
        try:
            inefficiency = float(timeseries.statistical_inefficiency(row))
        except Exception as error:  # PyMBAR documents estimator preconditions at runtime.
            raise SamplingDiagnosticsError("PYMBAR_STATISTICAL_INEFFICIENCY_FAILED") from error
        if not np.isfinite(inefficiency) or inefficiency < 1.0:
            inefficiency = 1.0
        record = {
            "trajectory_id": identity["trajectory_id"],
            "group_id": identity["group_id"],
            "frame_count": int(row.size),
            "observable_mean": float(np.mean(row)),
            "observable_standard_deviation": float(np.std(row)),
            "observed_window_minimum": float(np.min(row)),
            "observed_window_maximum": float(np.max(row)),
            "statistical_inefficiency": inefficiency,
            "effective_sample_size": float(row.size / inefficiency),
        }
        per_trajectory.append(record)
        values_by_group[str(identity["group_id"])].append(record)

    groups: list[dict[str, Any]] = []
    for group_id in sorted(values_by_group):
        records = values_by_group[group_id]
        groups.append(
            {
                "group_id": group_id,
                "trajectory_count": len(records),
                "observable_mean_summary": _summary(
                    [float(item["observable_mean"]) for item in records]
                ),
                "effective_sample_size_summary": _summary(
                    [float(item["effective_sample_size"]) for item in records]
                ),
                "statistical_inefficiency_summary": _summary(
                    [float(item["statistical_inefficiency"]) for item in records]
                ),
            }
        )

    between_group: list[dict[str, Any]] = []
    sorted_group_ids = sorted(values_by_group)
    for left_index, left_group_id in enumerate(sorted_group_ids):
        for right_group_id in sorted_group_ids[left_index + 1 :]:
            left_means = [float(item["observable_mean"]) for item in values_by_group[left_group_id]]
            right_means = [float(item["observable_mean"]) for item in values_by_group[right_group_id]]
            between_group.append(
                {
                    "left_group_id": left_group_id,
                    "right_group_id": right_group_id,
                    "difference_of_trajectory_mean_observable": float(
                        np.mean(right_means) - np.mean(left_means)
                    ),
                    "interpretation_boundary": (
                        "A descriptive difference of row-level means only; no biological "
                        "group effect, population, or convergence claim is emitted."
                    ),
                }
            )

    return {
        "schema_version": "grouped-observable-sampling-diagnostics/v1",
        "development_status": "DESCRIPTIVE_DEVELOPMENT_ONLY",
        "observable_id": observable_id,
        "analysis_window_label": analysis_window_label,
        "method_provenance": {
            "package": "pymbar",
            "package_version": importlib.metadata.version("pymbar"),
            "function": "pymbar.timeseries.statistical_inefficiency",
            "parameters": {"per_trajectory": True, "equilibration_detection": "NOT_RUN"},
        },
        "statistical_unit": "TRAJECTORY",
        "frame_dependence": "CORRELATED_WITHIN_TRAJECTORY",
        "row_count": int(matrix.shape[0]),
        "frames_per_trajectory": int(matrix.shape[1]),
        "per_trajectory": per_trajectory,
        "within_group_summaries": groups,
        "between_group_descriptions": between_group,
        "rule_effect": "NO_RULE_RESULT_EMITTED",
        "claim_ceiling": (
            "Observable-specific descriptive autocorrelation and effective-sample-size "
            "estimates within the supplied window only."
        ),
        "forbidden_claims": [
            "simulation globally equilibrated",
            "equilibrium population",
            "kinetic rate",
            "free energy",
            "mechanism",
            "biological group effect",
        ],
    }
