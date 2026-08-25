"""Allowlisted, read-only operator resolution and execution."""

from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .contracts import find_forbidden_answer_paths


def load_operator_registry(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        registry = json.load(handle)
    if registry.get("schema_version") != "scientific-operator-registry/v0.1":
        raise ValueError("INVALID_OPERATOR_REGISTRY_SCHEMA")
    if not isinstance(registry.get("registry_id"), str) or not registry["registry_id"].strip():
        raise ValueError("MISSING_OPERATOR_REGISTRY_ID")
    operators = registry.get("operators")
    if not isinstance(operators, dict):
        raise ValueError("INVALID_OPERATOR_REGISTRY_ENTRIES")
    return registry


def load_method_profile_registry(path: Path) -> tuple[str, frozenset[str]]:
    """Load only explicitly human-approved method profiles from a durable registry."""

    with path.open(encoding="utf-8") as handle:
        registry = json.load(handle)
    if registry.get("schema_version") != "method-profile-registry/v0.1":
        raise ValueError("INVALID_METHOD_PROFILE_REGISTRY_SCHEMA")
    registry_id = registry.get("registry_id")
    profiles = registry.get("profiles")
    if not isinstance(registry_id, str) or not registry_id.strip():
        raise ValueError("MISSING_METHOD_PROFILE_REGISTRY_ID")
    if not isinstance(profiles, Mapping):
        raise ValueError("INVALID_METHOD_PROFILE_REGISTRY_ENTRIES")
    approved: set[str] = set()
    for profile_id, profile in profiles.items():
        if not isinstance(profile_id, str) or not isinstance(profile, Mapping):
            raise ValueError("INVALID_METHOD_PROFILE_ENTRY")
        if profile.get("status") == "HUMAN_APPROVED":
            approval = profile.get("approval")
            if not isinstance(approval, Mapping) or not all(
                isinstance(approval.get(field), str) and approval.get(field, "").strip()
                for field in ("reviewer", "approved_at", "source_artifact")
            ):
                raise ValueError(f"INCOMPLETE_METHOD_PROFILE_APPROVAL:{profile_id}")
            approved.add(profile_id)
    return registry_id, frozenset(approved)


def operator_summary(registry: Mapping[str, Any]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for operator_id, spec in registry.get("operators", {}).items():
        if not isinstance(spec, Mapping):
            continue
        summaries.append(
            {
                "operator_id": operator_id,
                "version": spec.get("version"),
                "status": spec.get("status"),
                "resolves_obligation_types": spec.get("resolves_obligation_types", []),
            }
        )
    return summaries


def resolve_operator(
    registry: Mapping[str, Any], operator_id: str, obligation_type: str
) -> tuple[dict[str, Any] | None, list[str]]:
    operators = registry.get("operators")
    if not isinstance(operators, Mapping):
        return None, ["INVALID_OPERATOR_REGISTRY_ENTRIES"]
    spec = operators.get(operator_id)
    if not isinstance(spec, Mapping):
        return None, ["UNREGISTERED_OPERATOR"]
    resolved = dict(spec)
    if resolved.get("status") != "SOFTWARE_CANARY_PASS":
        reasons = ["OPERATOR_NOT_READY"]
        blockers = resolved.get("blockers", [])
        if isinstance(blockers, list):
            reasons.extend(f"BLOCKER:{item}" for item in blockers if isinstance(item, str))
        return resolved, reasons
    allowed_types = resolved.get("resolves_obligation_types")
    if not isinstance(allowed_types, list) or obligation_type not in allowed_types:
        return resolved, ["OBLIGATION_TYPE_NOT_ALLOWED_FOR_OPERATOR"]
    if resolved.get("handler") != "json_pointer_lookup":
        return resolved, ["UNSUPPORTED_OPERATOR_HANDLER"]
    return resolved, []


def _resolve_allowed_json_path(allowed_root: Path, source_path: str) -> Path:
    root = allowed_root.resolve()
    candidate = (root / source_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError("SOURCE_PATH_OUTSIDE_ALLOWED_ROOT") from exc
    if candidate.suffix.lower() != ".json":
        raise ValueError("SOURCE_PATH_NOT_JSON")
    if not candidate.is_file():
        raise ValueError("SOURCE_PATH_NOT_FOUND")
    return candidate


def _json_pointer(value: Any, pointer: str) -> Any:
    if pointer == "":
        return value
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("INVALID_JSON_POINTER")
    current = value
    for raw_token in pointer[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            try:
                current = current[int(token)]
            except (ValueError, IndexError) as exc:
                raise ValueError("JSON_POINTER_NOT_FOUND") from exc
        elif isinstance(current, Mapping) and token in current:
            current = current[token]
        else:
            raise ValueError("JSON_POINTER_NOT_FOUND")
    return current


def execute_operator(
    spec: Mapping[str, Any], operator_inputs: Mapping[str, Any], allowed_root: Path
) -> dict[str, Any]:
    required = spec.get("required_inputs")
    if not isinstance(required, list):
        raise ValueError("INVALID_OPERATOR_REQUIRED_INPUTS")
    missing = [field for field in required if field not in operator_inputs]
    if missing:
        raise ValueError("MISSING_OPERATOR_INPUT:" + ",".join(sorted(missing)))
    if spec.get("handler") != "json_pointer_lookup":
        raise ValueError("UNSUPPORTED_OPERATOR_HANDLER")
    source_path = operator_inputs.get("source_path")
    pointer = operator_inputs.get("json_pointer")
    if not isinstance(source_path, str):
        raise ValueError("INVALID_SOURCE_PATH")
    if not isinstance(pointer, str):
        raise ValueError("INVALID_JSON_POINTER")
    resolved_path = _resolve_allowed_json_path(allowed_root, source_path)
    with resolved_path.open(encoding="utf-8") as handle:
        source = json.load(handle)
    forbidden_source_paths = find_forbidden_answer_paths(source)
    if forbidden_source_paths:
        raise ValueError("ANSWER_BEARING_SOURCE")
    value = _json_pointer(source, pointer)
    forbidden_paths = find_forbidden_answer_paths(value)
    if forbidden_paths:
        raise ValueError("ANSWER_BEARING_OPERATOR_OUTPUT")
    return {
        "observed_value": value,
        "source_path": source_path,
        "json_pointer": pointer,
    }
