"""Command-line entry point for the exposed fixture slice."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal
from pathlib import Path
from typing import Any

from .evaluation import build_evaluation_contract, evaluate_current_bundle
from .operators import load_method_profile_registry, load_operator_registry
from .profile import build_profile_request, validate_case_graph
from .providers import RecordedCaseGraphProvider, RecordedProposalProvider
from .registered_operators import (
    load_registered_operator_registry,
    run_registered_operator_canary,
    summarize_registered_operators,
)
from .runplan import build_run_plan
from .runtime import admit_profile, run_resolution_stage
from .workspace import (
    load_workspace_asset_registry,
    resolve_bundle,
    run_existing_selector,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
LIVE_AGENT_CAMPAIGN_CONFIG_PATH = (
    REPO_ROOT
    / "agent_experiments"
    / "live_agent_common_flows_v1"
    / "config"
    / "live_agent_common_flows_v1.json"
)
LIVE_AGENT_CAMPAIGN_CLOSED_STATUS = "CLOSED_FROZEN"
LIVE_AGENT_CAMPAIGN_OPEN_STATUS = "AUTHORIZED_FOR_LIVE_CALLS"
LIVE_AGENT_CAMPAIGN_CLOSED_ERROR = (
    "LIVE_AGENT_CAMPAIGN_CLOSED_REQUIRES_NEW_AUTHORIZATION"
)
OPERATOR_REGISTRY_PATH = REPO_ROOT / "config" / "operators.json"
METHOD_PROFILE_REGISTRY_PATH = REPO_ROOT / "config" / "method_profiles.json"
FIXTURE_ALLOWED_ROOT = REPO_ROOT / "tests" / "fixtures"
WORKSPACE_ASSET_REGISTRY_PATH = REPO_ROOT / "config" / "workspace_assets.json"
REGISTERED_OPERATOR_REGISTRY_PATH = REPO_ROOT / "config" / "registered_operators.json"
PROFILE_PROMPT_PATH = REPO_ROOT / "prompts" / "profile_case_v1.md"


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(value, sort_keys=True) + "\n" for value in values),
        encoding="utf-8",
    )


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


def run_prototype(args: argparse.Namespace) -> int:
    """Run the target-architecture development slice against existing assets."""

    output_dir = Path(args.output_dir).resolve()
    _prepare_output_dir(output_dir)
    workspace_root = Path(args.workspace_root).resolve()
    traces: list[dict[str, Any]] = []

    asset_registry = load_workspace_asset_registry(WORKSPACE_ASSET_REGISTRY_PATH)
    bundle = resolve_bundle(asset_registry, workspace_root, args.bundle_id)
    source_case_graph = _read_json(bundle["example_case_graph"])
    case = source_case_graph["case"]
    data_manifest = [
        {
            "source_id": source.get("source_id"),
            "method_id": source.get("method_id"),
            "source_locator": source.get("source_locator"),
        }
        for source in source_case_graph.get("evidence_items", [])
    ]
    profile_request = build_profile_request(
        request_id=f"{args.run_id}-profile",
        question=str(case.get("scientific_claim")),
        data_manifest=data_manifest,
        prompt_ref="prompts/profile_case_v1.md",
        prompt_version="0.1",
    )
    provider = RecordedCaseGraphProvider(
        source_case_graph, provider_id="recorded-existing-rich-case-graph"
    )
    proposal = provider.propose_profile(profile_request)
    proposal_path = output_dir / "profile" / "case_graph_proposal.json"
    _write_json(output_dir / "profile" / "profile_request.json", profile_request)
    _write_json(proposal_path, proposal)
    admission = validate_case_graph(proposal, bundle["profile_schema"])
    _write_json(output_dir / "profile" / "case_graph_admission.json", admission.to_dict())
    traces.append(
        {
            "event": "PROFILE_VALIDATED",
            "status": admission.status,
            "provider_id": provider.provider_id,
            "artifact": "profile/case_graph_admission.json",
        }
    )
    if not admission.selector_access_allowed:
        _write_jsonl(output_dir / "trace.jsonl", traces)
        _write_json(
            output_dir / "run_summary.json",
            {
                "schema_version": "target-architecture-run-summary/v0.1",
                "run_id": args.run_id,
                "status": "PROFILE_BLOCKED",
                "reason_codes": list(admission.reason_codes),
            },
        )
        return 0

    rules_dir = output_dir / "rules"
    selector_artifacts = run_existing_selector(
        bundle=bundle,
        case_graph_path=proposal_path,
        output_path=rules_dir / "selector_output.json",
        receipt_path=rules_dir / "selector_native_receipt.json",
        run_id=f"{args.run_id}-selector",
    )
    selector_output = selector_artifacts["selector_output"]
    _write_json(rules_dir / "selector_adapter_receipt.json", selector_artifacts["adapter_receipt"])
    traces.append(
        {
            "event": "RULES_SELECTED",
            "status": "SUCCEEDED",
            "obligation_count": len(selector_output.get("obligations", [])),
            "unresolved_input_count": len(selector_output.get("unresolved_inputs", [])),
            "artifact": "rules/selector_output.json",
        }
    )

    contract = build_evaluation_contract(proposal, selector_output)
    evaluation = evaluate_current_bundle(
        contract=contract,
        selector_output=selector_output,
        evidence_results=[],
    )
    _write_json(output_dir / "evaluation" / "evaluation_contract.json", contract)
    _write_json(output_dir / "evaluation" / "current_bundle_evaluation.json", evaluation)
    traces.append(
        {
            "event": "CURRENT_BUNDLE_EVALUATED",
            "status": evaluation["branch"],
            "gap_count": evaluation["gap_count"],
            "artifact": "evaluation/current_bundle_evaluation.json",
        }
    )

    operator_registry = load_registered_operator_registry(REGISTERED_OPERATOR_REGISTRY_PATH)
    summaries = summarize_registered_operators(operator_registry, workspace_root)
    _write_json(
        output_dir / "operators" / "registry_snapshot.json",
        {
            "schema_version": "operator-registry-runtime-view/v0.1",
            "registry_id": operator_registry["registry_id"],
            "operators": summaries,
        },
    )

    plan: dict[str, Any] | None = None
    if evaluation["branch"] == "RUN_PLAN_REQUIRED":
        plan = build_run_plan(
            run_id=f"{args.run_id}-plan",
            case_graph=proposal,
            evaluation=evaluation,
            operator_registry=operator_registry,
        )
        _write_json(output_dir / "run_plan.json", plan)
        traces.append(
            {
                "event": "RUN_PLAN_PERSISTED",
                "status": plan["status"],
                "blocked_gap_count": plan["blocked_gap_count"],
                "artifact": "run_plan.json",
            }
        )
    else:
        _write_json(output_dir / "direct_bounded_result.json", evaluation)
        traces.append(
            {
                "event": "DIRECT_BOUNDED_RESULT",
                "status": evaluation["bundle_status"],
                "artifact": "direct_bounded_result.json",
            }
        )

    canary_status = "NOT_REQUESTED"
    if args.canary_operator_id:
        canary_root = output_dir / "operator_canary"
        canary_artifacts = run_registered_operator_canary(
            registry=operator_registry,
            operator_id=args.canary_operator_id,
            workspace_root=workspace_root,
            output_dir=canary_root / "payload",
            request_id=f"{args.run_id}-operator-canary",
        )
        for name, artifact in canary_artifacts.items():
            _write_json(canary_root / f"{name}.json", artifact)
        canary_status = canary_artifacts["operator_run_receipt"]["status"]
        traces.append(
            {
                "event": "REGISTERED_OPERATOR_CANARY",
                "status": canary_status,
                "operator_id": args.canary_operator_id,
                "artifact": "operator_canary/operator_run_receipt.json",
            }
        )

    case_flow_status = (
        "DIRECT_BOUNDED_RESULT"
        if plan is None
        else f"RUN_PLAN_{plan['status']}"
    )
    routed_operator_count = 0
    if plan is not None:
        routed_operator_count = sum(
            1
            for node in plan["nodes"]
            if node.get("node_type") == "RESOLVE_GAP" and node.get("operator_id")
        )
    summary = {
        "schema_version": "target-architecture-run-summary/v0.1",
        "run_id": args.run_id,
        "status": "LOCAL_VERTICAL_SLICE_EXECUTED_WITH_BLOCKED_CASE_ROUTE"
        if plan is not None and plan["status"] == "BLOCKED"
        else "LOCAL_VERTICAL_SLICE_EXECUTED",
        "case_id": admission.case_id,
        "profile_status": admission.status,
        "rules_selector": "EXISTING_SELECTOR_INVOKED",
        "obligation_count": len(selector_output.get("obligations", [])),
        "unresolved_input_count": len(selector_output.get("unresolved_inputs", [])),
        "evaluation_branch": evaluation["branch"],
        "case_flow_status": case_flow_status,
        "case_gap_resolution_operator_count": routed_operator_count,
        "registered_operator_canary_status": canary_status,
        "operator_canary_relation": "INDEPENDENT_REGISTRY_CANARY_NOT_ROUTED_FROM_CASE_PLAN"
        if args.canary_operator_id
        else "NOT_APPLICABLE",
        "request_validate_commit": "FUTURE_FEATURE",
        "semantic_correctness": "NOT_EVALUATED",
        "scientific_final_authority": "HUMAN_REVIEW_REQUIRED",
        "claim_ceiling": "Local development architecture behavior only.",
    }
    traces.append(
        {
            "event": "HUMAN_REVIEW_BOUNDARY",
            "status": "REQUIRED",
            "artifact": "run_summary.json",
        }
    )
    _write_jsonl(output_dir / "trace.jsonl", traces)
    _write_json(output_dir / "run_summary.json", summary)
    return 0


def run_demo(args: argparse.Namespace) -> int:
    """Rerun the fixed exposed-development reference artifacts into fresh output."""

    from .runnable_reference_demo_v1 import run_reference_demo

    run_reference_demo(output_dir=Path(args.output_dir))
    return 0


def run_smoke(args: argparse.Namespace) -> int:
    """Run the fixed paper-question-to-human-review exposed-development smoke test."""

    from .exposed_end_to_end_smoke_v1 import run_exposed_end_to_end_smoke

    run_exposed_end_to_end_smoke(output_dir=Path(args.output_dir))
    return 0


def run_prototype_acceptance(args: argparse.Namespace) -> int:
    """Run the fixed no-Agent Rules Prototype acceptance suite."""

    from .rules_prototype_acceptance_v1 import run_and_write_acceptance_suite

    run_and_write_acceptance_suite(
        repo_root=Path(args.repo_root),
        artifacts_dir=Path(args.artifacts_dir),
    )
    return 0


def run_case(args: argparse.Namespace) -> int:
    """Run one exact registered exposed-development case by recorded replay."""

    # The case runner imports the optional scientific capsule.  Keeping this
    # import inside the handler lets the core CLI and parser load without NumPy,
    # SciPy, or PyMBAR when another command is being used.
    from .case_runner_v1 import run_case_v1

    run_case_v1(case_id=args.case_id, output_dir=Path(args.output_dir))
    return 0


def _open_live_agent_campaign_budget(
    config: dict[str, Any],
    *,
    requested_cap: Decimal | None = None,
):
    """Open the one persisted ledger shared by every live CLI entry point."""

    from .live_agent_common_flows_v1 import campaign_budget_ledger_path
    from .openrouter_proposal_transport_v1 import OpenRouterBudgetLedger

    frozen_cap = Decimal(str(config["budget_usd"]))
    if requested_cap is not None and requested_cap != frozen_cap:
        raise ValueError("LIVE_AGENT_BUDGET_MUST_MATCH_FROZEN_CAMPAIGN_CAP")
    return OpenRouterBudgetLedger(
        cap_usd=frozen_cap,
        max_completed_calls=int(config["max_completed_calls"]),
        max_attempts_per_cell=int(config["max_attempts_per_exact_role_case_model"]),
        campaign_id=str(config["campaign_id"]),
        state_path=campaign_budget_ledger_path(config),
    )


def _require_live_agent_campaign_open(config: dict[str, Any]) -> None:
    """Reuse the runtime guard so CLI and Python APIs cannot drift."""

    from .live_agent_common_flows_v1 import require_live_agent_campaign_open

    require_live_agent_campaign_open(config)


def run_agent_case(args: argparse.Namespace) -> int:
    """Run the canonical recorded-default or explicit live proposal path."""

    if args.agent_mode == "recorded":
        from .case_runner_v1 import run_case_v1

        run_case_v1(case_id=args.case_id, output_dir=Path(args.output_dir))
        return 0

    from .live_agent_common_flows_v1 import (
        _model_entry,
        load_campaign_config,
        run_live_agent_case,
    )
    from .openrouter_proposal_transport_v1 import (
        OpenRouterProposalClient,
        read_openrouter_credential,
    )

    config = load_campaign_config(Path(args.campaign_config))
    _require_live_agent_campaign_open(config)
    cap = Decimal(args.budget_usd) if args.budget_usd is not None else None
    _model_entry(config, args.model_profile)
    credential = read_openrouter_credential(repo_root=REPO_ROOT)
    client = OpenRouterProposalClient(
        credential=credential,
        budget=_open_live_agent_campaign_budget(config, requested_cap=cap),
    )
    result = run_live_agent_case(
        case_id=args.case_id,
        output_dir=Path(args.output_dir),
        model_profile=args.model_profile,
        client=client,
        config=config,
    )
    return 0 if result["status"] == "SUCCEEDED" else 2


def run_agent_campaign(args: argparse.Namespace) -> int:
    """Run the frozen OpenRouter development matrix within the authorized cap."""

    from .live_agent_common_flows_v1 import (
        load_campaign_config,
        run_live_agent_campaign,
    )

    config = load_campaign_config(Path(args.campaign_config))
    _require_live_agent_campaign_open(config)
    budget = _open_live_agent_campaign_budget(config)
    manifest = run_live_agent_campaign(
        output_dir=Path(args.output_dir),
        budget=budget,
        config=config,
    )
    return 2 if manifest["status"] == "LIVE_CALL_BLOCKED_MISSING_CREDENTIAL" else 0


def run_scenario_suite(args: argparse.Namespace) -> int:
    """Run the deterministic four-route, three-terminal engineering suite."""

    from .common_flow_scenarios_v1 import run_common_flow_scenario_suite

    run_common_flow_scenario_suite(output_dir=Path(args.output_dir))
    return 0


def build_workbench(args: argparse.Namespace) -> int:
    """Render CaseView-compatible roots and an optional scenario matrix."""

    from .review_console_v0 import (
        DEFAULT_CAPSULE_ROOT,
        DEFAULT_REVIEW_WORKSPACE,
        render_review_console,
    )

    render_review_console(
        status_path=Path(args.status),
        capsule_root=Path(args.capsule_root) if args.capsule_root else DEFAULT_CAPSULE_ROOT,
        case_roots=[Path(path) for path in args.artifact_roots]
        if args.artifact_roots
        else None,
        review_workspace=Path(args.review_workspace)
        if args.review_workspace
        else DEFAULT_REVIEW_WORKSPACE,
        scenario_matrix_path=(
            Path(args.scenario_matrix) if args.scenario_matrix else None
        ),
        output_dir=Path(args.output_dir),
    )
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
    prototype_parser = subparsers.add_parser("run-prototype")
    prototype_parser.add_argument("--workspace-root", required=True)
    prototype_parser.add_argument("--output-dir", required=True)
    prototype_parser.add_argument("--run-id", default="target-architecture-prototype-001")
    prototype_parser.add_argument(
        "--bundle-id", default="protein_dynamics_rules_v0_3"
    )
    prototype_parser.add_argument(
        "--canary-operator-id",
        default=None,
        help="Run one independent registry canary explicitly; it is never part of case routing.",
    )
    prototype_parser.set_defaults(handler=run_prototype)
    demo_parser = subparsers.add_parser(
        "run-demo",
        help="Rerun the fixed X-EISD/HSP90 exposed-development reference demo.",
    )
    demo_parser.add_argument(
        "--output-dir",
        required=True,
        help="A new or empty directory for fresh demo artifacts.",
    )
    demo_parser.set_defaults(handler=run_demo)
    smoke_parser = subparsers.add_parser(
        "run-smoke",
        help="Run the exact X-EISD paper question plus HSP90 operator exposed-development smoke test.",
    )
    smoke_parser.add_argument(
        "--output-dir",
        required=True,
        help="A new or empty directory for fresh smoke-test artifacts.",
    )
    smoke_parser.set_defaults(handler=run_smoke)
    acceptance_parser = subparsers.add_parser(
        "run-prototype-acceptance",
        help="Run the eight recorded CaseGraph Rules Prototype acceptance tests.",
    )
    acceptance_parser.add_argument(
        "--repo-root",
        default=str(REPO_ROOT),
        help="Harness repository root containing frozen inputs and Rule registries.",
    )
    acceptance_parser.add_argument(
        "--artifacts-dir",
        default=str(REPO_ROOT / "research" / "rules_prototype_acceptance_v1"),
        help="Directory containing cases.jsonl and receiving the three generated artifacts.",
    )
    acceptance_parser.set_defaults(handler=run_prototype_acceptance)
    case_parser = subparsers.add_parser(
        "run-case",
        help="Run one exact registered exposed-development case by recorded proposal replay.",
    )
    case_parser.add_argument(
        "--case-id",
        required=True,
        help="Exact case ID from the exposed-development case registry.",
    )
    case_parser.add_argument(
        "--output-dir",
        required=True,
        help="A new or empty directory for fresh case artifacts.",
    )
    case_parser.set_defaults(handler=run_case)
    agent_case_parser = subparsers.add_parser(
        "run-agent-case",
        help=(
            "Canonical exposed-case path. Recorded replay is the no-network default; "
            "live OpenRouter must be selected explicitly."
        ),
    )
    agent_case_parser.add_argument("--case-id", required=True)
    agent_case_parser.add_argument("--output-dir", required=True)
    agent_case_parser.add_argument(
        "--agent-mode",
        choices=("recorded", "live-openrouter"),
        default="recorded",
    )
    agent_case_parser.add_argument(
        "--model-profile",
        default="luna",
        help="Exact profile ID frozen in the selected campaign config; ignored in recorded mode.",
    )
    agent_case_parser.add_argument(
        "--campaign-config",
        default=str(LIVE_AGENT_CAMPAIGN_CONFIG_PATH),
        help="Explicit campaign config; the config owns campaign ID, budget, ledger, and model profiles.",
    )
    agent_case_parser.add_argument(
        "--budget-usd",
        default=None,
        help="Optional live-only cap assertion; when omitted, use the frozen config cap.",
    )
    agent_case_parser.set_defaults(handler=run_agent_case)
    campaign_parser = subparsers.add_parser(
        "run-agent-campaign",
        help="Run the explicitly selected frozen OpenRouter campaign.",
    )
    campaign_parser.add_argument("--output-dir", required=True)
    campaign_parser.add_argument(
        "--campaign-config",
        default=str(LIVE_AGENT_CAMPAIGN_CONFIG_PATH),
    )
    campaign_parser.set_defaults(handler=run_agent_campaign)
    scenario_parser = subparsers.add_parser(
        "run-scenario-suite",
        help="Run the deterministic direct/lookup/computation/stop scenarios.",
    )
    scenario_parser.add_argument("--output-dir", required=True)
    scenario_parser.set_defaults(handler=run_scenario_suite)
    workbench_parser = subparsers.add_parser(
        "build-workbench",
        help="Render a static read-only workbench from case/run roots.",
    )
    workbench_parser.add_argument("--status", required=True)
    workbench_parser.add_argument("--artifact-root", dest="artifact_roots", action="append")
    workbench_parser.add_argument("--scenario-matrix")
    workbench_parser.add_argument("--capsule-root")
    workbench_parser.add_argument("--review-workspace")
    workbench_parser.add_argument("--output-dir", required=True)
    workbench_parser.set_defaults(handler=build_workbench)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
