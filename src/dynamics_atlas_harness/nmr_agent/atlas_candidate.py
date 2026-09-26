"""Minimal candidate contract; shape and evidence links are not domain acceptance."""
import re
from pathlib import Path

REQUIRED_TEXT = (
    "protein", "construct_and_variant", "conditions", "bound_ligands", "major_state",
    "alternative_state", "kinetic_model", "exchange_parameters", "residues_and_regions",
    "structural_identity_evidence", "controls_and_artefact_checks", "functional_relevance",
    "cannot_be_supported", "evidence_type", "proposed_tier", "provenance",
)


def validate(entries, observation_dir: Path) -> list[str]:
    if not isinstance(entries, list):
        return ["atlas_entries must be an array (empty if no state record is supported)"]
    errors = []
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {i} must be an object")
            continue
        for key in REQUIRED_TEXT:
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                errors.append(f"entry {i}: {key} needs a nonempty value, or an explicit unknown/unsupported statement")
        if entry.get("proposed_tier") not in ("strong", "weak", "candidate", "not_included"):
            errors.append(f"entry {i}: invalid proposed_tier")
        ids = entry.get("source_observations")
        if not isinstance(ids, list) or not ids:
            errors.append(f"entry {i}: source_observations must name issued observation ids")
        else:
            for oid in ids:
                if not isinstance(oid, str) or not re.fullmatch(r"O\d{6}", oid) or not (observation_dir / f"{oid}.json").is_file():
                    errors.append(f"entry {i}: unknown observation id {oid!r}")
    return errors
