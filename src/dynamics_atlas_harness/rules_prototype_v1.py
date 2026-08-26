"""Proposal-only deterministic evaluator for the revised Rules Prototype v1.

This module is intentionally not imported by the active v0.3 selector or runtime.
It evaluates explicit Draft fixtures so reviewers can inspect binding behavior before
any scientific rule is activated.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any


class RulePrototypeError(ValueError):
    """Raised when a Draft registry uses an undefined grammar form."""


_MISSING = object()
_PREDICATE_OPS = frozenset({"EQ", "IN", "EXISTS", "ALL", "ANY", "NOT"})
_ITERATION_OPS = frozenset({"FOR_EACH_SOURCE", "FOR_EACH_EDGE"})


def load_json(path: Path) -> dict[str, Any]:
    import json

    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise RulePrototypeError(f"registry must be a JSON object: {path}")
    return value


def _is_present(value: Any) -> bool:
    return value is not _MISSING and value is not None and value != "" and value != []


def _walk(value: Any, parts: Iterable[str]) -> Any:
    current = value
    for part in parts:
        if not isinstance(current, Mapping) or part not in current:
            return _MISSING
        current = current[part]
    return current


def resolve_path(
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    path: str,
) -> Any:
    """Resolve a canonical CASE, SOURCE, EDGE, or target path for one instance."""

    root, separator, remainder = path.partition(".")
    if not separator:
        raise RulePrototypeError(f"canonical path must include a root: {path}")
    if root == "case":
        value = case_graph.get("case", _MISSING)
    elif root == "source":
        value = target.get("record", _MISSING) if target.get("kind") == "SOURCE" else _MISSING
    elif root == "edge":
        value = target.get("record", _MISSING) if target.get("kind") == "EDGE" else _MISSING
    elif root == "target":
        value = target
    else:
        raise RulePrototypeError(f"unknown canonical path root: {root}")
    return _walk(value, remainder.split("."))


def evaluate_predicate(
    expression: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
) -> bool:
    """Evaluate the compact, explicit binding grammar."""

    op = expression.get("op")
    if op not in _PREDICATE_OPS:
        raise RulePrototypeError(f"undefined predicate primitive: {op!r}")

    if op == "EXISTS":
        return _is_present(resolve_path(case_graph, target, str(expression["path"])))
    if op == "EQ":
        return resolve_path(case_graph, target, str(expression["path"])) == expression.get("value")
    if op == "IN":
        values_path = expression.get("values_path")
        values = (
            resolve_path(case_graph, target, str(values_path))
            if values_path is not None
            else expression.get("values")
        )
        if not isinstance(values, list):
            raise RulePrototypeError("IN requires a values list or values_path resolving to a list")
        return resolve_path(case_graph, target, str(expression["path"])) in values
    if op == "NOT":
        argument = expression.get("arg")
        if not isinstance(argument, Mapping):
            raise RulePrototypeError("NOT requires an arg object")
        return not evaluate_predicate(argument, case_graph, target)

    arguments = expression.get("args")
    if not isinstance(arguments, list) or not arguments:
        raise RulePrototypeError(f"{op} requires a nonempty args list")
    if not all(isinstance(argument, Mapping) for argument in arguments):
        raise RulePrototypeError(f"{op} arguments must be objects")
    outcomes = [
        evaluate_predicate(argument, case_graph, target) for argument in arguments
    ]
    return all(outcomes) if op == "ALL" else any(outcomes)


def expand_targets(
    binding: Mapping[str, Any],
    case_graph: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Create deterministic CASE, SOURCE, or EDGE target references."""

    target_kind = binding.get("target_kind")
    iteration = binding.get("iteration")
    if target_kind == "CASE":
        if iteration is not None:
            raise RulePrototypeError("CASE binding must not declare an iteration primitive")
        case = case_graph.get("case", {})
        return [{"kind": "CASE", "id": case.get("case_id"), "record": case}]

    expected_op = {
        "SOURCE": "FOR_EACH_SOURCE",
        "EDGE": "FOR_EACH_EDGE",
    }.get(target_kind)
    if expected_op is None:
        raise RulePrototypeError(f"unknown binding target kind: {target_kind!r}")
    if not isinstance(iteration, Mapping) or iteration.get("op") != expected_op:
        raise RulePrototypeError(
            f"{target_kind} binding must use the {expected_op} iteration primitive"
        )
    if iteration.get("op") not in _ITERATION_OPS:
        raise RulePrototypeError(f"undefined iteration primitive: {iteration.get('op')!r}")
    collection_name = "evidence_items" if target_kind == "SOURCE" else "comparisons"
    id_name = "source_id" if target_kind == "SOURCE" else "comparison_id"
    collection = case_graph.get(collection_name, [])
    if not isinstance(collection, list):
        raise RulePrototypeError(f"{collection_name} must be a list")
    return [
        {"kind": target_kind, "id": record.get(id_name), "record": record}
        for record in collection
        if isinstance(record, Mapping)
    ]


def _result(
    *,
    subrule: Mapping[str, Any],
    binding: Mapping[str, Any],
    contract: Mapping[str, Any],
    target: Mapping[str, Any],
    status: str,
    applicability_status: str,
    reason_codes: list[str],
    missing_paths: list[str],
) -> dict[str, Any]:
    effect = contract["result_effects"][status]
    return {
        "schema_version": "rules-prototype-rule-result/v1",
        "runtime_subrule_id": subrule["runtime_subrule_id"],
        "family_id": subrule["family_id"],
        "target": {"kind": target.get("kind"), "id": target.get("id")},
        "applicability_status": applicability_status,
        "status": status,
        "reason_codes": reason_codes,
        "missing_paths": missing_paths,
        "resolution_policy_id": binding["resolution_policy_id"],
        "evaluation_contract_id": contract["evaluation_contract_id"],
        "claim_effect": effect,
        "scientific_verdict": "NOT_EMITTED_IN_PR1",
        "human_decision_gate_required": True,
        "human_decision_gate_id": contract["human_decision_gate_id"],
    }


def _first_matching_reason(
    *,
    conditions: Any,
    condition_set_name: str,
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
) -> str | None:
    """Return the first matching reason from one explicit contract condition set."""

    if not isinstance(conditions, list):
        raise RulePrototypeError(f"contract {condition_set_name} must be a list")
    for entry in conditions:
        if not isinstance(entry, Mapping):
            raise RulePrototypeError(
                f"contract {condition_set_name} entries must be objects"
            )
        condition = entry.get("condition")
        if not isinstance(condition, Mapping):
            raise RulePrototypeError(
                f"contract {condition_set_name} entries must include a condition object"
            )
        if evaluate_predicate(condition, case_graph, target):
            return str(entry.get("reason_code", "CONTRACT_CONDITION_MATCHED"))
    return None


def evaluate_rule_instance(
    *,
    subrule: Mapping[str, Any],
    binding: Mapping[str, Any],
    contract: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
) -> dict[str, Any]:
    """Evaluate one already-targeted Draft RuleInstance with fail-closed outcomes.

    A confirmed failure blocks the RuleInstance even if another field remains
    unresolved. Otherwise an explicit unresolved condition wins. PASS requires a
    matching frozen pass condition; every unmatched state defaults to UNRESOLVED.
    """

    if target.get("kind") != subrule.get("target_kind") or target.get("kind") != binding.get(
        "target_kind"
    ):
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="NOT_APPLICABLE",
            applicability_status="WRONG_TARGET",
            reason_codes=["WRONG_TARGET_KIND"],
            missing_paths=[],
        )

    applicability = binding.get("applicability")
    if not isinstance(applicability, Mapping):
        raise RulePrototypeError("binding applicability must be a grammar object")
    if not evaluate_predicate(applicability, case_graph, target):
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="NOT_APPLICABLE",
            applicability_status="NOT_MATCHED",
            reason_codes=["APPLICABILITY_PREDICATE_FALSE"],
            missing_paths=[],
        )

    required_paths = binding.get("required_evidence_paths")
    if not isinstance(required_paths, list):
        raise RulePrototypeError("binding required_evidence_paths must be a list")
    missing_paths = [
        path
        for path in required_paths
        if not _is_present(resolve_path(case_graph, target, str(path)))
    ]
    if missing_paths:
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="UNRESOLVED",
            applicability_status="MATCHED",
            reason_codes=["REQUIRED_EVIDENCE_MISSING"],
            missing_paths=missing_paths,
        )

    failure_reason = _first_matching_reason(
        conditions=contract.get("fail_conditions"),
        condition_set_name="fail_conditions",
        case_graph=case_graph,
        target=target,
    )
    if failure_reason is not None:
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="FAIL",
            applicability_status="MATCHED",
            reason_codes=[failure_reason],
            missing_paths=[],
        )

    unresolved_reason = _first_matching_reason(
        conditions=contract.get("unresolved_conditions"),
        condition_set_name="unresolved_conditions",
        case_graph=case_graph,
        target=target,
    )
    if unresolved_reason is not None:
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="UNRESOLVED",
            applicability_status="MATCHED",
            reason_codes=[unresolved_reason],
            missing_paths=[],
        )

    pass_reason = _first_matching_reason(
        conditions=contract.get("pass_conditions"),
        condition_set_name="pass_conditions",
        case_graph=case_graph,
        target=target,
    )
    if pass_reason is not None:
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="PASS",
            applicability_status="MATCHED",
            reason_codes=[pass_reason],
            missing_paths=[],
        )

    return _result(
        subrule=subrule,
        binding=binding,
        contract=contract,
        target=target,
        status="UNRESOLVED",
        applicability_status="MATCHED",
        reason_codes=["NO_EXPLICIT_CONTRACT_OUTCOME"],
        missing_paths=[],
    )


def evaluate_active_rules(
    *,
    case_graph: Mapping[str, Any],
    runtime_subrules: Mapping[str, Any],
    bindings: Mapping[str, Any],
    contracts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Evaluate only the F01/F06 Draft slice; candidate-map rules are not executed."""

    subrule_by_id = {
        item["runtime_subrule_id"]: item
        for item in runtime_subrules.get("runtime_subrules", [])
    }
    contract_by_id = {
        item["evaluation_contract_id"]: item for item in contracts.get("contracts", [])
    }
    results: list[dict[str, Any]] = []
    for binding in bindings.get("bindings", []):
        subrule = subrule_by_id[binding["runtime_subrule_id"]]
        if subrule.get("implementation_status") != "COMPLETE_DRAFT":
            continue
        contract = contract_by_id[binding["evaluation_contract_id"]]
        for target in expand_targets(binding, case_graph):
            results.append(
                evaluate_rule_instance(
                    subrule=subrule,
                    binding=binding,
                    contract=contract,
                    case_graph=case_graph,
                    target=target,
                )
            )
    return results
