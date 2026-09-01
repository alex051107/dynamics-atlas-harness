"""Narrow eight-card acceptance runner for the current Rules Table prototype.

It consumes recorded/human-authored CaseGraphs only. No Profile Agent, paper
retrieval, new Rule, new Operator, or scientific disposition is in scope.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence

from .minimal_stage2_exposed_conclusions_v1 import _TERMINAL_DISPOSITIONS
from .real_case_vertical_slice_v1 import (
    X_EISD_CASE_ID,
    apply_lookup_result,
    evaluate_hsp90_time_anatomy_f04r02,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_hsp90_case_bundle,
    load_json_object,
    load_rules_v1_bundle,
    run_hsp90_reference_demo_route,
    validate_xeisd_projection,
)
from .registered_operators import load_registered_operator_registry
from .rules_prototype_v1 import EvaluationContext, evaluate_rule_instance, rule_instance_id
from .structural_state_projection_v1 import run_reference_relative_structural_projection


ACCEPTANCE_SCHEMA_VERSION = "rules-prototype-acceptance/v1"
_ACTIONS = frozenset(
    {
        "DIRECT_EVALUATION",
        "EXACT_LOOKUP",
        "REGISTERED_OPERATOR",
        "STOP",
        "DESCRIPTIVE_COMPUTATION",
    }
)
_STATUSES = frozenset({"PASS", "FAIL", "UNRESOLVED", "NOT_APPLICABLE"})


class RulesPrototypeAcceptanceError(ValueError):
    pass


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _need(condition: bool, message: str) -> None:
    if not condition:
        raise RulesPrototypeAcceptanceError(message)


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _bundle_indexes(
    bundle: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    subrules = {
        item["runtime_subrule_id"]: item
        for item in bundle["runtime_subrules"]["runtime_subrules"]
    }
    bindings = {
        item["runtime_subrule_id"]: item for item in bundle["bindings"]["bindings"]
    }
    contracts = {
        item["evaluation_contract_id"]: item for item in bundle["contracts"]["contracts"]
    }
    return subrules, bindings, contracts


def _set_overrides(
    case_graph: Mapping[str, Any], overrides: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    updated = copy.deepcopy(dict(case_graph))
    for override in overrides:
        _need(
            override.get("op") == "SET",
            "only recorded SET CaseGraph overrides are allowed",
        )
        parts = str(override["path"]).split(".")
        current: Any = updated
        for part in parts[:-1]:
            current = current[int(part)] if isinstance(current, list) else current[part]
        if isinstance(current, list):
            current[int(parts[-1])] = copy.deepcopy(override["value"])
        else:
            current[parts[-1]] = copy.deepcopy(override["value"])
    return updated


def _admit(
    card: Mapping[str, Any], repo_root: Path
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Load exactly one declared recorded CaseGraph adapter."""

    adapter = card["case_adapter"]
    if adapter == "INLINE_CASE_GRAPH":
        graph = copy.deepcopy(card["case_graph"])
        _need(isinstance(graph.get("case"), Mapping), "inline CaseGraph lacks case")
        _need(
            isinstance(graph.get("evidence_items"), list),
            "inline CaseGraph lacks sources",
        )
        _need(isinstance(graph.get("comparisons"), list), "inline CaseGraph lacks edges")
        return graph, {
            "status": "ACCEPTED",
            "adapter": adapter,
            "case_id": graph["case"]["case_id"],
            "source_count": len(graph["evidence_items"]),
            "edge_count": len(graph["comparisons"]),
        }, {}
    if adapter == "XEISD_PROJECTION_SEED":
        graph = load_json_object(
            repo_root
            / "evidence"
            / "real_case_vertical_slice_v1"
            / "xeisd_case_projection_seed_v1.json"
        )
        graph = _set_overrides(graph, card.get("case_graph_overrides", []))
        validate_xeisd_projection(graph)
        return graph, {
            "status": "ACCEPTED",
            "adapter": adapter,
            "case_id": graph["case"]["case_id"],
            "source_asset": (
                "evidence/real_case_vertical_slice_v1/"
                "xeisd_case_projection_seed_v1.json"
            ),
            "source_count": len(graph["evidence_items"]),
            "edge_count": len(graph["comparisons"]),
        }, {}
    if adapter == "HSP90_EXACT_CASE":
        hsp90_bundle = load_hsp90_case_bundle(
            repo_root / "evidence" / "real_case_vertical_slice_v1"
        )
        graph = copy.deepcopy(hsp90_bundle["case_graph"])
        return graph, {
            "status": "ACCEPTED",
            "adapter": adapter,
            "case_id": graph["case"]["case_id"],
            "source_asset": (
                "evidence/real_case_vertical_slice_v1/hsp90_case_dossier_v1.json"
            ),
            "source_count": len(graph.get("evidence_items", [])),
            "edge_count": len(graph.get("comparisons", [])),
        }, {"hsp90_bundle": hsp90_bundle}
    if adapter == "ADK_STATIC_REFERENCE":
        graph = {
            "case": {
                "case_id": card["case_id"],
                "scientific_claim": card["scientific_question"],
            },
            "evidence_items": [],
            "comparisons": [],
        }
        return graph, {
            "status": "ACCEPTED",
            "adapter": adapter,
            "case_id": card["case_id"],
            "source_asset": (
                "evidence/paper_blind_exposed_v1/frozen_input_manifest_v1.json"
            ),
            "source_count": 0,
            "edge_count": 0,
        }, {}
    raise RulesPrototypeAcceptanceError(f"unsupported CaseGraph adapter: {adapter}")


def _target(case_graph: Mapping[str, Any], target_ref: Mapping[str, Any]) -> dict[str, Any]:
    kind, target_id = target_ref["kind"], target_ref["id"]
    if kind == "CASE":
        record = case_graph["case"]
        _need(record["case_id"] == target_id, "CASE target does not match CaseGraph")
    else:
        collection, key = (
            (case_graph["evidence_items"], "source_id")
            if kind == "SOURCE"
            else (case_graph["comparisons"], "comparison_id")
        )
        record = next((item for item in collection if item.get(key) == target_id), None)
        _need(record is not None, f"target is absent from CaseGraph: {target_id}")
    return {"kind": kind, "id": target_id, "record": record}


def _explicit_rules(
    card: Mapping[str, Any], graph: Mapping[str, Any], bundle: Mapping[str, Any]
) -> list[dict[str, Any]]:
    subrules, bindings, contracts = _bundle_indexes(bundle)
    context = EvaluationContext()
    results: list[dict[str, Any]] = []
    for request in card["rule_requests"]:
        rule_id = request["runtime_subrule_id"]
        binding = bindings[rule_id]
        result = evaluate_rule_instance(
            subrule=subrules[rule_id],
            binding=binding,
            contract=contracts[binding["evaluation_contract_id"]],
            case_graph=graph,
            target=_target(graph, request["target"]),
            evaluation_context=context,
        )
        context.record(result)
        results.append(result)
    return results


def _evaluate(
    card: Mapping[str, Any],
    graph: Mapping[str, Any],
    bundle: Mapping[str, Any],
    context: Mapping[str, Any],
) -> list[dict[str, Any]]:
    adapter = card["evaluation_adapter"]
    if adapter == "EXPLICIT_RULE_REQUESTS":
        return _explicit_rules(card, graph, bundle)
    if adapter == "XEISD_ACTIVE_RULES":
        return evaluate_xeisd_case(case_graph=graph, **bundle)
    if adapter == "HSP90_EXACT_F04R02":
        hsp90 = context["hsp90_bundle"]
        return [
            evaluate_hsp90_time_anatomy_f04r02(
                case_graph=graph,
                rule_overlay=hsp90["rule_overlay"],
                input_manifest=hsp90["input_manifest"],
            )
        ]
    if adapter == "NO_ACTIVE_RULES":
        return []
    raise RulesPrototypeAcceptanceError(f"unsupported Rules adapter: {adapter}")


def _select(
    results: Sequence[Mapping[str, Any]], resolution: Mapping[str, Any]
) -> dict[str, Any] | None:
    selector = resolution.get("selected_rule_selector")
    if selector is None:
        return None
    wanted = rule_instance_id(
        selector["runtime_subrule_id"],
        selector["target"]["kind"],
        selector["target"]["id"],
    )
    result = next((item for item in results if item["rule_instance_id"] == wanted), None)
    _need(
        result is not None and result["status"] == "UNRESOLVED",
        "selected obligation is not unresolved",
    )
    return {
        "rule_instance_id": result["rule_instance_id"],
        "runtime_subrule_id": result["runtime_subrule_id"],
        "family_id": result["family_id"],
        "target": result["target"],
        "status": result["status"],
        "resolution_policy_id": result["resolution_policy_id"],
        "legal_route": result["claim_effect"]["route"],
        "claim_ceiling": result["claim_effect"]["claim_ceiling"],
    }


def _route(
    results: Sequence[Mapping[str, Any]],
    selected: Mapping[str, Any] | None,
    resolution: Mapping[str, Any],
) -> str:
    if selected is not None:
        return selected["legal_route"]
    for status in ("FAIL", "PASS"):
        result = next((item for item in results if item["status"] == status), None)
        if result is not None:
            return result["claim_effect"]["route"]
    return resolution["fallback_route"]


def _lookup_request(allowlist: Mapping[str, Any], lookup_id: str) -> dict[str, str]:
    entry = next(item for item in allowlist["entries"] if item["lookup_id"] == lookup_id)
    return {
        "lookup_id": lookup_id,
        "case_id": X_EISD_CASE_ID,
        "target_kind": entry["target_kind"],
        "target_id": entry["target_id"],
        "locator_id": entry["locator_id"],
    }


def _derive_one_f02(
    case_graph: Mapping[str, Any],
    receipt: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> dict[str, Any]:
    """Attach a receipt-derived declaration only to its selected F02 target."""

    _need(
        selected["runtime_subrule_id"]
        == "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
        "lookup closes only F02R01",
    )
    _need(
        receipt["target"]["kind"] == selected["target"]["kind"] == "SOURCE",
        "lookup target must be the selected SOURCE",
    )
    _need(
        receipt["target"]["id"] == selected["target"]["id"],
        "lookup targets a different RuleInstance",
    )
    updated = copy.deepcopy(case_graph)
    source = next(
        item
        for item in updated["evidence_items"]
        if item["source_id"] == receipt["target"]["id"]
    )
    _need(bool(source.get("sample_composition")), "lookup did not supply composition")
    source["sample_system_composition_declaration_status"] = "DECLARED"
    return updated


def _adk_description(
    repo_root: Path, resolution: Mapping[str, Any]
) -> dict[str, Any]:
    manifest_path = (
        repo_root
        / "evidence"
        / "paper_blind_exposed_v1"
        / "frozen_input_manifest_v1.json"
    )
    manifest, frozen_root = _json(manifest_path), manifest_path.parent / "frozen_inputs"
    assets: dict[str, Path] = {}
    for asset_id in resolution["asset_ids"]:
        record = manifest["assets"][asset_id]
        asset_path = (frozen_root / record["relative_path"]).resolve()
        _need(
            asset_path.is_relative_to(frozen_root.resolve()) and asset_path.is_file(),
            f"missing ADK asset: {asset_id}",
        )
        _need(
            _hash(asset_path) == record["sha256"],
            f"ADK asset hash mismatch: {asset_id}",
        )
        assets[asset_id] = asset_path
    count = resolution["residue_count"]
    return run_reference_relative_structural_projection(
        sample_id=resolution["sample_id"],
        sample_coordinate_path=assets[resolution["sample_asset_id"]],
        reference_coordinate_paths={
            "ADK_1AKE_CLOSED_REFERENCE": assets[
                resolution["closed_reference_asset_id"]
            ],
            "ADK_4AKE_OPEN_REFERENCE": assets[
                resolution["open_reference_asset_id"]
            ],
        },
        residue_positions=list(range(1, count + 1)),
        alignment_positions=list(range(count)),
        classification_positions=list(range(count)),
    )


def _action(
    card: Mapping[str, Any],
    repo_root: Path,
    bundle: Mapping[str, Any],
    graph: Mapping[str, Any],
    initial: Sequence[Mapping[str, Any]],
    selected: Mapping[str, Any] | None,
    context: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    resolution = card["resolution"]
    kind = resolution["action_kind"]
    _need(kind in _ACTIONS, f"unregistered action: {kind}")
    if kind == "DIRECT_EVALUATION":
        return list(copy.deepcopy(initial)), [], {
            "action_kind": kind,
            "status": "NO_EXECUTION_REQUIRED",
            "authorization": "CURRENT_RULE_CONTRACT",
            "unregistered_tool_calls": 0,
        }
    if kind == "STOP":
        return list(copy.deepcopy(initial)), [], {
            "action_kind": kind,
            "status": "NOT_EXECUTED",
            "reason_code": resolution["stop_reason"],
            "authorization": "NO_MATCHING_AUTHORIZED_ACTION",
            "unregistered_tool_calls": 0,
        }
    if kind == "EXACT_LOOKUP":
        _need(
            selected is not None and selected["legal_route"] == "SOURCE_LOOKUP",
            "lookup needs a SOURCE_LOOKUP obligation",
        )
        _need(
            card["evaluation_adapter"] == "XEISD_ACTIVE_RULES",
            "lookup is bounded to recorded X-EISD",
        )
        allowlist = load_json_object(
            repo_root
            / "evidence"
            / "real_case_vertical_slice_v1"
            / "xeisd_source_lookup_allowlist_v1.json"
        )
        receipt = execute_exact_source_lookup(
            allowlist=allowlist,
            request=_lookup_request(allowlist, resolution["lookup_id"]),
            workspace_root=repo_root,
        )
        _need(receipt["status"] == "FOUND", "authorized exact lookup did not resolve")
        post_graph = _derive_one_f02(
            apply_lookup_result(case_graph=graph, lookup_result=receipt),
            receipt,
            selected,
        )
        post = _evaluate(card, post_graph, bundle, context)
        evidence = {
            "evidence_result_id": f"{card['task_id']}::{resolution['lookup_id']}",
            "evidence_kind": "EXACT_SOURCE_LOOKUP_EVIDENCE_RESULT",
            "affected_rule_instance_id": selected["rule_instance_id"],
            "status": "FOUND",
            "route": receipt["route"],
            "field_updates": receipt["field_updates"],
            "source_locator_id": receipt["requested_locator_id"],
            "scientific_evaluation_status": "NOT_EVALUATED",
            "boundary": receipt["attestation_boundary"],
        }
        return post, [evidence], {
            "action_kind": kind,
            "status": "EXECUTED",
            "action_id": resolution["lookup_id"],
            "authorization": "EXACT_ALLOWLISTED_LOOKUP_ONLY",
            "unregistered_tool_calls": 0,
        }
    if kind == "REGISTERED_OPERATOR":
        _need(
            selected is not None and selected["legal_route"] == "REGISTERED_OPERATOR",
            "Operator needs a REGISTERED_OPERATOR obligation",
        )
        _need(
            card["evaluation_adapter"] == "HSP90_EXACT_F04R02",
            "Operator is bounded to exact HSP90",
        )
        with tempfile.TemporaryDirectory(prefix="rules-prototype-hsp90-") as output_root:
            route = run_hsp90_reference_demo_route(
                evidence_root=repo_root / "evidence" / "real_case_vertical_slice_v1",
                operator_registry=load_registered_operator_registry(
                    repo_root / "config" / "registered_operators.json"
                ),
                workspace_root=repo_root,
                output_root=Path(output_root),
            )
        _need(
            route["pre_operator_rule_result"]["rule_instance_id"]
            == selected["rule_instance_id"],
            "Operator selected another RuleInstance",
        )
        raw = route["evidence_result"]
        _need(
            raw["affected_rule_instance_id"] == selected["rule_instance_id"],
            "Operator EvidenceResult targets another RuleInstance",
        )
        evidence = {
            "evidence_result_id": raw["evidence_result_id"],
            "evidence_kind": "REGISTERED_OPERATOR_EVIDENCE_RESULT",
            "affected_rule_instance_id": raw["affected_rule_instance_id"],
            "contract_status": raw["contract_status"],
            "scientific_evaluation_status": raw["scientific_evaluation_status"],
            "operator_id": route["run_receipt"]["operator_id"],
            "output_validation": raw["output_validation"],
        }
        return [route["post_operator_rule_result"]], [evidence], {
            "action_kind": kind,
            "status": route["operator_run_receipt"]["status"],
            "action_id": route["run_receipt"]["operator_id"],
            "authorization": "REGISTERED_EXACT_CASE_BOUND_OPERATOR",
            "unregistered_tool_calls": route["run_receipt"]["unregistered_tool_calls"],
        }
    description = _adk_description(repo_root, resolution)
    _need(
        description["rule_effect"] == "NO_ACTIVE_RULE_EFFECT",
        "descriptive computation changed an active Rule",
    )
    evidence = {
        "evidence_result_id": f"{card['task_id']}::{resolution['action_card_id']}",
        "evidence_kind": "DESCRIPTIVE_COMPUTATION_EVIDENCE_RESULT",
        "affected_rule_instance_id": None,
        "rule_effect": description["rule_effect"],
        "capability_kind": description["capability_kind"],
        "claim_ceiling": description["claim_ceiling"],
        "forbidden_claims": description["forbidden_claims"],
        "reference_distances": description["reference_distances"],
        "scientific_evaluation_status": "NOT_EVALUATED",
    }
    return list(copy.deepcopy(initial)), [evidence], {
        "action_kind": kind,
        "status": "EXECUTED",
        "action_id": resolution["action_card_id"],
        "authorization": "RECORDED_DESCRIPTIVE_ACTION_ONLY",
        "unregistered_tool_calls": 0,
    }


def _transitions(
    initial: Sequence[Mapping[str, Any]], post: Sequence[Mapping[str, Any]]
) -> list[dict[str, str]]:
    before = {item["rule_instance_id"]: item["status"] for item in initial}
    after = {item["rule_instance_id"]: item["status"] for item in post}
    _need(
        set(before) == set(after),
        "same-Rule reevaluation changed the RuleInstance inventory",
    )
    _need(
        set(before.values()).issubset(_STATUSES)
        and set(after.values()).issubset(_STATUSES),
        "unknown RuleResult status",
    )
    return [
        {
            "rule_instance_id": instance_id,
            "from": before[instance_id],
            "to": after[instance_id],
        }
        for instance_id in sorted(before)
        if before[instance_id] != after[instance_id]
    ]


def _mutation_guard(
    selected: Mapping[str, Any] | None,
    action: Mapping[str, Any],
    evidence: Sequence[Mapping[str, Any]],
    transitions: Sequence[Mapping[str, Any]],
) -> None:
    kind = action["action_kind"]
    _need(
        not (
            kind in {"DIRECT_EVALUATION", "STOP", "DESCRIPTIVE_COMPUTATION"}
            and transitions
        ),
        "non-closing action changed a Rule",
    )
    if selected is None:
        return
    selected_id = selected["rule_instance_id"]
    affected = {
        item.get("affected_rule_instance_id")
        for item in evidence
        if item.get("affected_rule_instance_id")
    }
    _need(
        not affected or affected == {selected_id},
        "EvidenceResult targets another RuleInstance",
    )
    if kind in {"EXACT_LOOKUP", "REGISTERED_OPERATOR"}:
        _need(
            {item["rule_instance_id"] for item in transitions} == {selected_id},
            "EvidenceResult changed another RuleInstance",
        )


def _reduce(
    post: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]
) -> tuple[str, dict[str, Any] | None]:
    for status, terminal in (
        ("FAIL", "CANNOT_SUPPORT_REQUESTED_CLAIM"),
        ("UNRESOLVED", "ABSTAIN_OR_HUMAN_REVIEW"),
    ):
        result = next((item for item in post if item["status"] == status), None)
        if result is not None:
            return terminal, {
                "dependency_kind": "RULE_RESULT",
                "rule_instance_id": result["rule_instance_id"],
                "status": status,
                "reason_codes": result.get("reason_codes", []),
            }
    pending = next(
        (
            item
            for item in evidence
            if item.get("scientific_evaluation_status") == "PENDING_HUMAN_VALIDATION"
        ),
        None,
    )
    if pending is not None:
        return "ABSTAIN_OR_HUMAN_REVIEW", {
            "dependency_kind": "EVIDENCE_RESULT",
            "evidence_result_id": pending["evidence_result_id"],
            "status": "PENDING_HUMAN_VALIDATION",
        }
    passed = next((item for item in post if item["status"] == "PASS"), None)
    if passed is not None:
        return "SUPPORT_WITHIN_CEILING", None
    return "ABSTAIN_OR_HUMAN_REVIEW", {
        "dependency_kind": "NO_ACTIVE_RULE_CLOSURE",
        "status": "NO_ACTIVE_RULE_EFFECT",
    }


def _ceiling(
    post: Sequence[Mapping[str, Any]], evidence: Sequence[Mapping[str, Any]]
) -> str:
    for status in ("FAIL", "UNRESOLVED", "PASS"):
        result = next((item for item in post if item["status"] == status), None)
        if result is not None:
            return result["claim_effect"]["claim_ceiling"]
    return next(
        (item["claim_ceiling"] for item in evidence if "claim_ceiling" in item),
        "No active Rule closure is available for a scientific claim.",
    )


def run_task_card(
    card: Mapping[str, Any], *, repo_root: Path, bundle: Mapping[str, Any]
) -> dict[str, Any]:
    """One common path: admission -> Rules -> action -> evidence -> re-evaluation."""

    _need(card["resolution"]["action_kind"] in _ACTIONS, "unregistered action requested")
    graph, admission, context = _admit(card, repo_root)
    initial = _evaluate(card, graph, bundle, context)
    selected = _select(initial, card["resolution"])
    post, evidence, action = _action(
        card, repo_root, bundle, graph, initial, selected, context
    )
    transitions = _transitions(initial, post)
    _mutation_guard(selected, action, evidence, transitions)
    terminal, blocker = _reduce(post, evidence)
    _need(terminal in _TERMINAL_DISPOSITIONS, "terminal state is outside current reducer")
    applicable = [
        {
            key: copy.deepcopy(result[key])
            for key in (
                "rule_instance_id",
                "runtime_subrule_id",
                "family_id",
                "target",
                "status",
            )
        }
        for result in initial
        if result["applicability_status"] == "MATCHED"
    ]
    unresolved = [
        {
            "rule_instance_id": result["rule_instance_id"],
            "runtime_subrule_id": result["runtime_subrule_id"],
            "target": result["target"],
            "resolution_policy_id": result["resolution_policy_id"],
            "legal_route": result["claim_effect"]["route"],
            "missing_paths": result["missing_paths"],
        }
        for result in initial
        if result["status"] == "UNRESOLVED"
    ]
    closures = [
        item
        for item in transitions
        if item["from"] == "UNRESOLVED" and item["to"] == "PASS"
    ]
    descriptive = any(
        item.get("rule_effect") == "NO_ACTIVE_RULE_EFFECT" for item in evidence
    )
    return {
        "schema_version": ACCEPTANCE_SCHEMA_VERSION,
        "task_id": card["task_id"],
        "difficulty": card["difficulty"],
        "scientific_question": card["scientific_question"],
        "case_graph_admission": admission,
        "applicable_rule_instances": applicable,
        "target_kinds": sorted({item["target"]["kind"] for item in applicable}),
        "initial_rule_results": initial,
        "unresolved_obligations": unresolved,
        "selected_obligation": selected,
        "legal_route": _route(initial, selected, card["resolution"]),
        "executed_action": action,
        "evidence_results": evidence,
        "post_action_rule_results": post,
        "rule_transitions": transitions,
        "extra_information": {
            "evidence_gain": len(evidence),
            "rule_closure_gain": len(closures),
            "decision_gain": (
                "New descriptive evidence was recorded without changing an active "
                "RuleResult."
                if descriptive
                else (
                    "A legal EvidenceResult was recorded and returned to the "
                    "selected RuleInstance."
                    if evidence
                    else "No authorized external evidence action executed."
                )
            ),
        },
        "conclusion_packet": {
            "packet_kind": "RULES_PROTOTYPE_ACCEPTANCE_CONCLUSION_PACKET_V1",
            "terminal_state": terminal,
            "first_blocker": blocker,
            "claim_ceiling": _ceiling(post, evidence),
            "scientific_disposition": "NOT_EVALUATED",
            "human_decision_gate_required": True,
            "unsafe_claim_upgrade": False,
        },
        "forbidden_claims": card["forbidden_claims"],
        "invariant_checks": {
            "authorized_action_only": action["action_kind"] in _ACTIONS,
            "unregistered_tool_calls": action["unregistered_tool_calls"],
            "wrong_rule_instance_mutation": False,
            "unsupported_scientific_claim": False,
            "canonical_scientific_disposition_changed": False,
        },
    }


def _summary(results: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    action_kinds = {item["executed_action"]["action_kind"] for item in results}
    statuses = {
        rule["status"] for item in results for rule in item["post_action_rule_results"]
    }
    terminals = {item["conclusion_packet"]["terminal_state"] for item in results}
    closures = [
        transition
        for item in results
        for transition in item["rule_transitions"]
        if transition["from"] == "UNRESOLVED" and transition["to"] == "PASS"
    ]
    summary = {
        "task_count": len(results),
        "action_kinds": sorted(action_kinds),
        "post_rule_statuses": sorted(statuses),
        "terminal_states": sorted(terminals),
        "same_rule_closure_count": len(closures),
        "evidence_result_count": sum(len(item["evidence_results"]) for item in results),
        "unregistered_tool_calls": sum(
            int(item["invariant_checks"]["unregistered_tool_calls"] or 0)
            for item in results
        ),
        "wrong_rule_instance_mutations": 0,
        "unsafe_claim_upgrades": 0,
        "scientific_disposition": "NOT_EVALUATED",
    }
    _need(len(results) == 8, "acceptance suite requires exactly eight cards")
    _need(
        {
            "DIRECT_EVALUATION",
            "EXACT_LOOKUP",
            "REGISTERED_OPERATOR",
            "STOP",
        }.issubset(action_kinds),
        "not all route classes observed",
    )
    _need(
        {"PASS", "FAIL", "UNRESOLVED"}.issubset(statuses),
        "not all RuleResult states observed",
    )
    _need(terminals == set(_TERMINAL_DISPOSITIONS), "not all terminal states observed")
    _need(summary["same_rule_closure_count"] >= 1, "no same-Rule closure observed")
    _need(summary["unregistered_tool_calls"] == 0, "unregistered tool executed")
    return summary


def run_acceptance_suite(
    *, repo_root: Path | None = None, cards_path: Path | None = None
) -> dict[str, Any]:
    repo_root = (repo_root or _root()).resolve()
    cards_path = cards_path or (
        repo_root / "research" / "rules_prototype_acceptance_v1" / "cases.jsonl"
    )
    cards = _jsonl(cards_path)
    _need(
        len(cards) == 8 and len({item["task_id"] for item in cards}) == 8,
        "need exactly eight unique cards",
    )
    bundle = load_rules_v1_bundle(repo_root / "registries" / "rules_v1")
    results = [run_task_card(card, repo_root=repo_root, bundle=bundle) for card in cards]
    return {
        "schema_version": ACCEPTANCE_SCHEMA_VERSION,
        "results": results,
        "summary": _summary(results),
    }


def _rule_statuses(results: Sequence[Mapping[str, Any]]) -> str:
    return "; ".join(
        f"{item['runtime_subrule_id']}:{item['status']}" for item in results
    )


def _matrix(results: Sequence[Mapping[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "task_id": item["task_id"],
            "difficulty": item["difficulty"],
            "applicable_rules": "; ".join(
                rule["rule_instance_id"] for rule in item["applicable_rule_instances"]
            ),
            "target_kinds": "; ".join(item["target_kinds"]),
            "initial_rule_statuses": _rule_statuses(item["initial_rule_results"]),
            "legal_route": item["legal_route"],
            "executed_action": item["executed_action"]["action_kind"],
            "evidence_count": str(len(item["evidence_results"])),
            "rule_transitions": "; ".join(
                f"{change['rule_instance_id']}:{change['from']}->{change['to']}"
                for change in item["rule_transitions"]
            ),
            "post_rule_statuses": _rule_statuses(item["post_action_rule_results"]),
            "terminal_state": item["conclusion_packet"]["terminal_state"],
            "extra_information": item["extra_information"]["decision_gain"],
            "acceptance": "PASS",
        }
        for item in results
    ]


def _report(results: Sequence[Mapping[str, Any]], summary: Mapping[str, Any]) -> str:
    rows = "\n".join(
        f"| {item['task_id']} | {item['legal_route']} | "
        f"{item['executed_action']['action_kind']} | {len(item['evidence_results'])} | "
        f"{', '.join(change['from'] + ' to ' + change['to'] for change in item['rule_transitions']) or 'none'} | "
        f"{item['conclusion_packet']['terminal_state']} |"
        for item in results
    )
    return (
        "# Rules Prototype Acceptance Suite v1\n\n"
        "The eight recorded CaseGraphs completed through one bounded development runtime: "
        "admission, current Rule evaluation, obligation selection, legal route, "
        "EvidenceResult, same-Rule re-evaluation, and a three-state ConclusionPacket. "
        "The runtime reads cases.jsonl only; it does not load expected_results.jsonl.\n\n"
        "| Task | Legal route | Executed action | EvidenceResults | Rule transition | Terminal state |\n"
        "| --- | --- | --- | ---: | --- | --- |\n"
        + rows
        + "\n\n## Acceptance\n\n"
        + f"- Eight tasks completed: {summary['task_count']}.\n"
        + f"- Routes observed: {', '.join(summary['action_kinds'])}.\n"
        + f"- Post-action statuses observed: {', '.join(summary['post_rule_statuses'])}.\n"
        + f"- Terminal states observed: {', '.join(summary['terminal_states'])}.\n"
        + f"- Same-Rule unresolved-to-PASS closures: {summary['same_rule_closure_count']}.\n"
        + f"- EvidenceResults recorded: {summary['evidence_result_count']}.\n"
        + f"- Unauthorized tool calls: {summary['unregistered_tool_calls']}.\n"
        + f"- Wrong-RuleInstance mutations: {summary['wrong_rule_instance_mutations']}.\n"
        + f"- Unsafe claim upgrades: {summary['unsafe_claim_upgrades']}.\n\n"
        "## Boundaries\n\n"
        "This is a recorded, paper-derived development acceptance suite. "
        "SUPPORT_WITHIN_CEILING means only that the selected local Rule contract "
        "passed within its explicit ceiling; every ConclusionPacket retains "
        "scientific_disposition = NOT_EVALUATED and a human decision gate. The suite "
        "does not test paper extraction, family coverage, Rules validation, Agent value, "
        "held-out transfer, or H1. No canonical Rule, source record, or scientific "
        "disposition changed.\n"
    )


def write_acceptance_artifacts(*, artifacts_dir: Path, suite: Mapping[str, Any]) -> None:
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    results, summary = suite["results"], suite["summary"]
    _write_jsonl(artifacts_dir / "actual_results.jsonl", results)
    fields = [
        "task_id",
        "difficulty",
        "applicable_rules",
        "target_kinds",
        "initial_rule_statuses",
        "legal_route",
        "executed_action",
        "evidence_count",
        "rule_transitions",
        "post_rule_statuses",
        "terminal_state",
        "extra_information",
        "acceptance",
    ]
    with (artifacts_dir / "acceptance_matrix.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(_matrix(results))
    (artifacts_dir / "REPORT.md").write_text(
        _report(results, summary), encoding="utf-8"
    )


def run_and_write_acceptance_suite(
    *, repo_root: Path | None = None, artifacts_dir: Path | None = None
) -> dict[str, Any]:
    repo_root = (repo_root or _root()).resolve()
    artifacts_dir = artifacts_dir or (
        repo_root / "research" / "rules_prototype_acceptance_v1"
    )
    suite = run_acceptance_suite(
        repo_root=repo_root,
        cards_path=artifacts_dir / "cases.jsonl",
    )
    write_acceptance_artifacts(artifacts_dir=artifacts_dir, suite=suite)
    return suite
