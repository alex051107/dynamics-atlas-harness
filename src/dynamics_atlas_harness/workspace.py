"""Read-only adapter to the existing Rules Table selector assets."""

from __future__ import annotations

import json
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_workspace_asset_registry(path: Path) -> dict[str, Any]:
    registry = _read_json(path)
    if registry.get("schema_version") != "workspace-asset-registry/v0.1":
        raise ValueError("INVALID_WORKSPACE_ASSET_REGISTRY")
    bundles = registry.get("bundles")
    if not isinstance(bundles, Mapping):
        raise ValueError("INVALID_WORKSPACE_ASSET_BUNDLES")
    return registry


def resolve_workspace_asset(workspace_root: Path, relative_path: str) -> Path:
    root = workspace_root.resolve()
    candidate = (root / relative_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError("WORKSPACE_ASSET_OUTSIDE_ROOT") from exc
    if not candidate.is_file():
        raise ValueError(f"WORKSPACE_ASSET_NOT_FOUND:{relative_path}")
    return candidate


def resolve_bundle(
    registry: Mapping[str, Any], workspace_root: Path, bundle_id: str
) -> dict[str, Path]:
    bundles = registry.get("bundles")
    bundle = bundles.get(bundle_id) if isinstance(bundles, Mapping) else None
    if not isinstance(bundle, Mapping):
        raise ValueError("UNKNOWN_WORKSPACE_ASSET_BUNDLE")
    required = (
        "profile_schema",
        "selector_entrypoint",
        "rule_registry",
        "typed_bindings",
        "compiled_rule_index",
        "method_scope",
        "example_case_graph",
    )
    result: dict[str, Path] = {}
    for field in required:
        value = bundle.get(field)
        if not isinstance(value, str) or not value:
            raise ValueError(f"MISSING_WORKSPACE_ASSET:{field}")
        result[field] = resolve_workspace_asset(workspace_root, value)
    return result


def run_existing_selector(
    *,
    bundle: Mapping[str, Path],
    case_graph_path: Path,
    output_path: Path,
    receipt_path: Path,
    run_id: str,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Invoke the existing selector without copying or mutating Rules assets."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(bundle["selector_entrypoint"]),
        "--input",
        str(case_graph_path),
        "--output",
        str(output_path),
        "--receipt",
        str(receipt_path),
        "--run-id",
        run_id,
        "--index",
        str(bundle["compiled_rule_index"]),
        "--method-scope",
        str(bundle["method_scope"]),
    ]
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    adapter_receipt = {
        "schema_version": "rules-selector-adapter-receipt/v0.1",
        "run_id": run_id,
        "status": "SUCCEEDED" if completed.returncode == 0 else "FAILED",
        "return_code": completed.returncode,
        "selector_entrypoint": str(bundle["selector_entrypoint"]),
        "rule_registry": str(bundle["rule_registry"]),
        "typed_bindings": str(bundle["typed_bindings"]),
        "compiled_rule_index": str(bundle["compiled_rule_index"]),
        "method_scope": str(bundle["method_scope"]),
        "case_graph_path": str(case_graph_path),
        "stdout_tail": completed.stdout[-2000:],
        "stderr_tail": completed.stderr[-2000:],
        "authority": "EXISTING_SELECTOR_REVIEW_OBLIGATIONS_ONLY",
    }
    if completed.returncode != 0:
        raise RuntimeError(json.dumps(adapter_receipt, sort_keys=True))
    result = _read_json(output_path)
    adapter_receipt["obligation_count"] = len(result.get("obligations", []))
    adapter_receipt["unresolved_input_count"] = len(result.get("unresolved_inputs", []))
    return {"selector_output": result, "adapter_receipt": adapter_receipt}
