"""Command-line entry point for the exposed fixture slice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .operators import load_method_profile_registry, load_operator_registry
from .providers import RecordedProposalProvider
from .runtime import admit_profile, run_resolution_stage


REPO_ROOT = Path(__file__).resolve().parents[2]
OPERATOR_REGISTRY_PATH = REPO_ROOT / "config" / "operators.json"
METHOD_PROFILE_REGISTRY_PATH = REPO_ROOT / "config" / "method_profiles.json"
FIXTURE_ALLOWED_ROOT = REPO_ROOT / "tests" / "fixtures"


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _prepare_output_dir(path: Path) -> None:
    if path.exists() and (not path.is_dir() or any(path.iterdir())):
        raise ValueError("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    path.mkdir(parents=True, exist_ok=True)


def run_fixture(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir).resolve()
    _prepare_output_dir(output_dir)

    profile = _read_json(Path(args.profile_proposal))
    method_registry_id, approved_profiles = load_method_profile_registry(
        METHOD_PROFILE_REGISTRY_PATH
    )
    admission = admit_profile(
        profile,
        approved_profiles,
        method_profile_registry_id=method_registry_id,
    )
    _write_json(output_dir / "profile_admission.json", admission.to_dict())
    if not admission.selector_access_allowed:
        return 0

    # The recorded selector output is deliberately opened only after admission.
    selector_output = _read_json(Path(args.selector_output))
    if selector_output.get("schema_version") != "recorded-selector-output/v0.1":
        raise ValueError("INVALID_RECORDED_SELECTOR_OUTPUT")
    selector_case_id = selector_output.get("case_id")
    selector_admission = {
        "schema_version": "selector-admission/v0.1",
        "profile_case_id": admission.case_id,
        "selector_case_id": selector_case_id,
        "status": "ACCEPTED" if selector_case_id == admission.case_id else "ABSTAINED",
        "reason_codes": [] if selector_case_id == admission.case_id else ["CASE_ID_MISMATCH"],
    }
    _write_json(output_dir / "selector_admission.json", selector_admission)
    if selector_case_id != admission.case_id:
        return 0
    obligations = selector_output.get("obligations")
    if not isinstance(obligations, list) or len(obligations) != 1:
        raise ValueError("PROTOTYPE_REQUIRES_EXACTLY_ONE_SELECTED_OBLIGATION")

    proposal = _read_json(Path(args.resolution_proposal))
    provider = RecordedProposalProvider(proposal, provider_id="recorded-codex-subagent")
    registry = load_operator_registry(OPERATOR_REGISTRY_PATH)
    artifacts = run_resolution_stage(
        obligations[0],
        provider,
        registry,
        FIXTURE_ALLOWED_ROOT,
        request_id=args.request_id,
    )
    for name, artifact in artifacts.items():
        _write_json(output_dir / f"{name}.json", artifact)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run-fixture")
    run_parser.add_argument("--profile-proposal", required=True)
    run_parser.add_argument("--selector-output", required=True)
    run_parser.add_argument("--resolution-proposal", required=True)
    run_parser.add_argument("--output-dir", required=True)
    run_parser.add_argument("--request-id", default="fixture-request-001")
    run_parser.set_defaults(handler=run_fixture)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.handler(args))
