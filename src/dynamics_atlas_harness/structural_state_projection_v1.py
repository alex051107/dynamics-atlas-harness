"""Package-backed static reference-relative proximity descriptions.

This narrow adapter uses SciPy's rigid alignment implementation for a named sample
and named reference anchors. It reports geometry only; it does not assign a
population, kinetic state, pathway, free energy, mechanism, or Rule result.
"""

from __future__ import annotations

import importlib.metadata
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import numpy as np
from scipy.spatial.transform import Rotation


class StructuralStateProjectionError(ValueError):
    """Raised when a coordinate array or declared atom mapping is invalid."""


def _coordinates(path: Path) -> np.ndarray:
    try:
        coordinates = np.load(path, allow_pickle=False)
    except (OSError, ValueError) as error:
        raise StructuralStateProjectionError("COORDINATE_ARRAY_UNREADABLE") from error
    if coordinates.ndim != 2 or coordinates.shape[1] != 3 or coordinates.shape[0] < 3:
        raise StructuralStateProjectionError("COORDINATE_ARRAY_MUST_BE_N_BY_3")
    if not np.issubdtype(coordinates.dtype, np.number) or not np.isfinite(coordinates).all():
        raise StructuralStateProjectionError("COORDINATE_ARRAY_MUST_BE_FINITE_NUMERIC")
    return np.asarray(coordinates, dtype=np.float64)


def _indices(indices: Sequence[int], *, coordinate_count: int, label: str) -> np.ndarray:
    if not isinstance(indices, Sequence) or isinstance(indices, (str, bytes)) or len(indices) < 3:
        raise StructuralStateProjectionError(f"{label}_MUST_HAVE_AT_LEAST_THREE_INDICES")
    if any(not isinstance(index, int) or isinstance(index, bool) for index in indices):
        raise StructuralStateProjectionError(f"{label}_INDICES_MUST_BE_INTEGERS")
    if len(set(indices)) != len(indices) or min(indices) < 0 or max(indices) >= coordinate_count:
        raise StructuralStateProjectionError(f"{label}_INDICES_OUT_OF_RANGE")
    return np.asarray(indices, dtype=int)


def _aligned_rmsd(
    *, sample: np.ndarray, reference: np.ndarray, alignment_indices: np.ndarray, classification_indices: np.ndarray
) -> float:
    reference_core = reference[alignment_indices]
    sample_core = sample[alignment_indices]
    reference_center = np.mean(reference_core, axis=0)
    sample_center = np.mean(sample_core, axis=0)
    try:
        rotation, _ = Rotation.align_vectors(
            reference_core - reference_center,
            sample_core - sample_center,
        )
    except ValueError as error:
        raise StructuralStateProjectionError("SCIPY_RIGID_ALIGNMENT_FAILED") from error
    aligned_sample = rotation.apply(sample - sample_center) + reference_center
    residual = aligned_sample[classification_indices] - reference[classification_indices]
    return float(np.sqrt(np.mean(np.sum(residual * residual, axis=1))))


def run_reference_relative_structural_projection(
    *,
    sample_id: str,
    sample_coordinate_path: str | Path,
    reference_coordinate_paths: Mapping[str, str | Path],
    residue_positions: Sequence[int],
    alignment_positions: Sequence[int],
    classification_positions: Sequence[int],
    ambiguity_tolerance_angstrom: float = 0.001,
) -> dict[str, Any]:
    """Describe one non-reference structure's rigidly aligned anchor proximity."""

    if not isinstance(sample_id, str) or not sample_id.strip():
        raise StructuralStateProjectionError("SAMPLE_ID_INVALID")
    if not isinstance(reference_coordinate_paths, Mapping) or len(reference_coordinate_paths) < 2:
        raise StructuralStateProjectionError("AT_LEAST_TWO_REFERENCES_REQUIRED")
    if not isinstance(ambiguity_tolerance_angstrom, (int, float)) or ambiguity_tolerance_angstrom < 0:
        raise StructuralStateProjectionError("AMBIGUITY_TOLERANCE_INVALID")
    sample_path = Path(sample_coordinate_path).resolve()
    sample = _coordinates(sample_path)
    references = {
        reference_id: _coordinates(Path(path).resolve())
        for reference_id, path in reference_coordinate_paths.items()
    }
    if any(sample_path == Path(path).resolve() for path in reference_coordinate_paths.values()):
        raise StructuralStateProjectionError("SAMPLE_MUST_NOT_BE_REFERENCE_ASSET")
    if any(np.array_equal(sample, reference) for reference in references.values()):
        raise StructuralStateProjectionError("SAMPLE_MUST_NOT_MATCH_REFERENCE_COORDINATES")
    if any(not isinstance(reference_id, str) or not reference_id.strip() for reference_id in references):
        raise StructuralStateProjectionError("REFERENCE_ID_INVALID")
    if any(reference.shape != sample.shape for reference in references.values()):
        raise StructuralStateProjectionError("REFERENCE_COORDINATE_SHAPE_MISMATCH")
    if len(residue_positions) != sample.shape[0]:
        raise StructuralStateProjectionError("RESIDUE_MAPPING_LENGTH_MISMATCH")
    if list(residue_positions) != list(range(1, sample.shape[0] + 1)):
        raise StructuralStateProjectionError("RESIDUE_MAPPING_MUST_BE_ORDERED_CHAIN_A_CA")
    alignment_indices = _indices(
        alignment_positions, coordinate_count=sample.shape[0], label="ALIGNMENT"
    )
    classification_indices = _indices(
        classification_positions, coordinate_count=sample.shape[0], label="CLASSIFICATION"
    )

    distances = [
        {
            "reference_id": reference_id,
            "aligned_rmsd_angstrom": _aligned_rmsd(
                sample=sample,
                reference=references[reference_id],
                alignment_indices=alignment_indices,
                classification_indices=classification_indices,
            ),
        }
        for reference_id in sorted(references)
    ]
    distances.sort(key=lambda item: (item["aligned_rmsd_angstrom"], item["reference_id"]))
    nearest = distances[0]
    second = distances[1]
    distance_gap = float(second["aligned_rmsd_angstrom"] - nearest["aligned_rmsd_angstrom"])
    ambiguous = distance_gap <= float(ambiguity_tolerance_angstrom)

    return {
        "schema_version": "static-reference-relative-proximity-description/v1",
        "development_status": "DESCRIPTIVE_DEVELOPMENT_ONLY",
        "capability_kind": "STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION",
        "sample_id": sample_id.strip(),
        "sample_kind": "NONREFERENCE_STATIC_COORDINATE_SAMPLE",
        "method_provenance": {
            "package": "scipy",
            "package_version": importlib.metadata.version("scipy"),
            "function": "scipy.spatial.transform.Rotation.align_vectors",
            "parameters": {
                "rigid_alignment": "proper_rotation_plus_translation",
                "ambiguity_tolerance_angstrom": float(ambiguity_tolerance_angstrom),
            },
        },
        "atom_residue_mapping": {
            "selection": "Chain A C-alpha",
            "residue_positions": list(residue_positions),
            "mapping_rule": "Position i maps among the three frozen Chain A C-alpha arrays at residue position i+1.",
        },
        "alignment_core": {"residue_positions": [int(index) + 1 for index in alignment_indices]},
        "classification_region": {
            "residue_positions": [int(index) + 1 for index in classification_indices]
        },
        "reference_distances": distances,
        "nearest_reference_geometry": {
            "status": "AMBIGUOUS_REFERENCE_PROXIMITY" if ambiguous else "CLOSER_TO_REFERENCE",
            "reference_id": None if ambiguous else nearest["reference_id"],
            "distance_gap_to_second_reference_angstrom": distance_gap,
        },
        "rule_effect": "NO_ACTIVE_RULE_EFFECT",
        "claim_ceiling": "Whole-chain rigid-alignment reference-relative proximity for one static non-reference sample.",
        "forbidden_claims": [
            "state population",
            "transition rate",
            "free energy",
            "mechanism",
            "pathway",
            "wild-type equivalence",
            "portability",
        ],
    }
