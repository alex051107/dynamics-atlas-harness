"""Versioned scientific OperatorSpecs and a narrow existing-analysis adapter."""

from __future__ import annotations

import contextlib
import importlib.metadata
import importlib.util
import io
import json
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .workspace import resolve_workspace_asset


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _validate_operator_lifecycle(operator_id: str, spec: Mapping[str, Any]) -> None:
    status = spec.get("status")
    routable = spec.get("routable")
    if status != "ROSTER_PASS":
        if routable is not False:
            raise ValueError(
                f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:NON_ROSTER_ROUTABLE"
            )
        return

    if routable is not True:
        raise ValueError(
            f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:ROSTER_NOT_ROUTABLE"
        )
    if "promotion_blockers" in spec and spec["promotion_blockers"] != []:
        raise ValueError(
            f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:ROSTER_PROMOTION_BLOCKERS_PRESENT"
        )
    if not isinstance(spec.get("output_contract"), str) or not spec[
        "output_contract"
    ].strip():
        raise ValueError(
            f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:ROSTER_MISSING_OUTPUT_CONTRACT"
        )
    route_match = spec.get("route_match")
    if not isinstance(route_match, Mapping) or not route_match:
        raise ValueError(
            f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:ROSTER_MISSING_ROUTE_MATCH"
        )
    if not isinstance(spec.get("claim_ceiling"), str) or not spec[
        "claim_ceiling"
    ].strip():
        raise ValueError(
            f"INVALID_OPERATOR_LIFECYCLE:{operator_id}:ROSTER_MISSING_CLAIM_CEILING"
        )


def load_registered_operator_registry(path: Path) -> dict[str, Any]:
    registry = _read_json(path)
    if registry.get("schema_version") != "scientific-operator-registry/v0.2":
        raise ValueError("INVALID_REGISTERED_OPERATOR_SCHEMA")
    if not isinstance(registry.get("registry_id"), str):
        raise ValueError("MISSING_REGISTERED_OPERATOR_REGISTRY_ID")
    operators = registry.get("operators")
    if not isinstance(operators, Mapping):
        raise ValueError("INVALID_REGISTERED_OPERATOR_ENTRIES")
    for operator_id, spec in operators.items():
        if not isinstance(spec, Mapping):
            raise ValueError(f"INVALID_REGISTERED_OPERATOR_SPEC:{operator_id}")
        _validate_operator_lifecycle(str(operator_id), spec)
    return registry


def _package_version(package: str) -> str | None:
    if importlib.util.find_spec(package) is None:
        return None
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "AVAILABLE_VERSION_UNKNOWN"


def probe_operator(spec: Mapping[str, Any], workspace_root: Path) -> dict[str, Any]:
    reasons: list[str] = []
    packages: dict[str, str | None] = {}
    for package in spec.get("runtime", {}).get("required_python_packages", []):
        version = _package_version(str(package))
        packages[str(package)] = version
        if version is None:
            reasons.append(f"PYTHON_PACKAGE_UNAVAILABLE:{package}")

    paths: dict[str, str] = {}
    implementation_ref = spec.get("implementation_ref")
    if isinstance(implementation_ref, str):
        try:
            path = resolve_workspace_asset(workspace_root, implementation_ref)
        except ValueError as exc:
            reasons.append(str(exc))
        else:
            paths["implementation_ref"] = str(path)
    else:
        reasons.append("MISSING_IMPLEMENTATION_REF")

    fixed_inputs = spec.get("fixed_inputs", {})
    if not isinstance(fixed_inputs, Mapping):
        reasons.append("INVALID_FIXED_INPUTS")
    else:
        for name, relative_path in fixed_inputs.items():
            if not isinstance(relative_path, str):
                reasons.append(f"INVALID_FIXED_INPUT:{name}")
                continue
            try:
                path = resolve_workspace_asset(workspace_root, relative_path)
            except ValueError as exc:
                reasons.append(f"{name}:{exc}")
            else:
                paths[str(name)] = str(path)

    if spec.get("status") == "REGISTERED_BLOCKED":
        reasons.extend(
            f"DECLARED_BLOCKER:{item}"
            for item in spec.get("blockers", [])
            if isinstance(item, str)
        )
    return {
        "schema_version": "operator-runtime-probe/v0.1",
        "operator_id": spec.get("operator_id"),
        "status": "AVAILABLE" if not reasons else "BLOCKED",
        "reason_codes": reasons,
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "packages": packages,
        "resolved_paths": paths,
    }


def summarize_registered_operators(
    registry: Mapping[str, Any], workspace_root: Path
) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for operator_id, spec in registry.get("operators", {}).items():
        if not isinstance(spec, Mapping):
            continue
        probe = probe_operator(spec, workspace_root)
        summaries.append(
            {
                "operator_id": operator_id,
                "version": spec.get("version"),
                "declared_status": spec.get("status"),
                "runtime_status": probe["status"],
                "skill_ref": spec.get("skill_ref"),
                "capability": spec.get("capability"),
                "route_match": spec.get("route_match"),
                "claim_ceiling": spec.get("claim_ceiling"),
            }
        )
    return summaries


def _run_hsp90_time_anatomy(
    *,
    spec: Mapping[str, Any],
    probe: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    paths = probe["resolved_paths"]
    implementation_path = Path(paths["implementation_ref"])
    module_spec = importlib.util.spec_from_file_location(
        "dynamics_atlas_registered_hsp90_time_anatomy_v0", implementation_path
    )
    if module_spec is None or module_spec.loader is None:
        raise ValueError("OPERATOR_MODULE_LOAD_FAILED")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    output_dir.mkdir(parents=True, exist_ok=False)
    module.FRAMES = Path(paths["frame_state_assignments"])
    module.ROUTES = Path(paths["route_predictions"])
    module.SOURCE = module.FRAMES.parent
    module.OUT = output_dir
    parameters = spec.get("fixed_parameters", {})
    module.PERSISTENCE_FRAMES = list(parameters["persistence_saved_frames"])

    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        module.main()
    missing = [
        name for name in spec.get("expected_outputs", []) if not (output_dir / name).is_file()
    ]
    if missing:
        raise ValueError("OPERATOR_OUTPUT_MISSING:" + ",".join(missing))
    result = _read_json(output_dir / "results_summary.json")
    return {
        "result": result,
        "stdout_tail": captured.getvalue()[-2000:],
        "output_files": sorted(path.name for path in output_dir.iterdir() if path.is_file()),
    }


def execute_hsp90_time_anatomy_adapter(
    *,
    spec: Mapping[str, Any],
    workspace_root: Path,
    output_dir: Path,
) -> dict[str, Any]:
    """Run the existing HSP90 implementation after an exact caller-side binding.

    This is intentionally a narrow implementation adapter, not a generic Operator
    router.  The caller owns the case, RuleInstance, manifest, and output-contract
    checks; this function only probes the registered implementation and invokes the
    frozen standard-library script with the registered fixed inputs and parameters.
    """

    if spec.get("handler") != "case_bound_hsp90_time_anatomy_v1":
        raise ValueError("UNSUPPORTED_HSP90_TIME_ANATOMY_HANDLER")
    probe = probe_operator(spec, workspace_root)
    reason_codes = probe["reason_codes"]
    if reason_codes:
        raise ValueError("OPERATOR_RUNTIME_PROBE_FAILED:" + ",".join(reason_codes))
    return _run_hsp90_time_anatomy(spec=spec, probe=probe, output_dir=output_dir)


def run_registered_operator_canary(
    *,
    registry: Mapping[str, Any],
    operator_id: str,
    workspace_root: Path,
    output_dir: Path,
    request_id: str,
) -> dict[str, dict[str, Any]]:
    operators = registry.get("operators", {})
    spec = operators.get(operator_id) if isinstance(operators, Mapping) else None
    if not isinstance(spec, Mapping):
        reason_codes = ["UNREGISTERED_OPERATOR"]
        probe: dict[str, Any] | None = None
    else:
        probe = probe_operator(spec, workspace_root)
        reason_codes = list(probe["reason_codes"])

    if spec is None or reason_codes:
        receipt = {
            "schema_version": "operator-run-receipt/v0.2",
            "request_id": request_id,
            "operator_id": operator_id,
            "status": "BLOCKED",
            "reason_codes": reason_codes,
            "runtime_probe": probe,
            "operator_registry_id": registry.get("registry_id"),
        }
        return {
            "operator_run_receipt": receipt,
            "evidence_result": {
                "schema_version": "evidence-result/v0.2",
                "status": "NOT_PRODUCED",
                "evaluation_status": "NOT_EVALUATED",
                "reason_codes": reason_codes,
            },
        }

    handler = spec.get("handler")
    if handler != "existing_hsp90_time_anatomy_v0":
        raise ValueError("UNSUPPORTED_REGISTERED_OPERATOR_HANDLER")
    payload = _run_hsp90_time_anatomy(spec=spec, probe=probe, output_dir=output_dir)
    receipt = {
        "schema_version": "operator-run-receipt/v0.2",
        "request_id": request_id,
        "operator_id": operator_id,
        "operator_version": spec.get("version"),
        "operator_registry_id": registry.get("registry_id"),
        "status": "SUCCEEDED",
        "reason_codes": [],
        "skill_ref": spec.get("skill_ref"),
        "implementation_ref": spec.get("implementation_ref"),
        "runtime_probe": probe,
        "fixed_inputs": spec.get("fixed_inputs"),
        "fixed_parameters": spec.get("fixed_parameters"),
        "output_contract": spec.get("output_contract"),
        "output_files": payload["output_files"],
        "stdout_tail": payload["stdout_tail"],
    }
    evidence = {
        "schema_version": "evidence-result/v0.2",
        "status": "OBSERVED",
        "evaluation_status": "PENDING_HUMAN_VALIDATION",
        "operator_id": operator_id,
        "operator_version": spec.get("version"),
        "result": payload["result"],
        "claim_ceiling": spec.get("claim_ceiling"),
        "forbidden_claims": spec.get("forbidden_claims", []),
    }
    return {"operator_run_receipt": receipt, "evidence_result": evidence}
