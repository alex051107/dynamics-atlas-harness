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
_PREDICATE_OPS = frozenset(
    {"EQ", "IN", "EXISTS", "ALL", "ANY", "NOT", "PRIOR_RESULT_STATUS"}
)
_ITERATION_OPS = frozenset({"FOR_EACH_SOURCE", "FOR_EACH_EDGE"})
_TRUE = "TRUE"
_FALSE = "FALSE"
_UNKNOWN = "UNKNOWN"
_STORED_RULE_RESULT_STATUSES = frozenset({"PASS", "FAIL", "UNRESOLVED", "NOT_APPLICABLE"})

# These are deliberately explicit PR1B phases, not a dependency graph or a
# general workflow scheduler. F06R02 declares only the producer results below.
_PR1B_PREREQUISITE_SUBRULE_IDS = (
    "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
    "F02R02_EDGE_CONDITION_COMPATIBILITY",
    "F03R01_SOURCE_NATIVE_MEASUREMENT",
)
_PR1B_CONTEXT_PRODUCER_SUBRULE_IDS = frozenset(
    {
        "F02R02_EDGE_CONDITION_COMPATIBILITY",
        "F03R01_SOURCE_NATIVE_MEASUREMENT",
    }
)
_PR1B_REPLAY_SUBRULE_IDS = (
    "F01R01_CASE_CLAIM_DECLARATION",
    "F01R02_CASE_REQUESTED_WORDING_SCOPE",
    "F06R01_SOURCE_EVIDENCE_ROLE",
    "F06R02_EDGE_COMPARABILITY",
    "F06R03_EDGE_VALIDATION_INDEPENDENCE",
)


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


def rule_instance_id(
    runtime_subrule_id: str,
    target_kind: str | None,
    target_id: Any,
) -> str:
    """Return the stable identifier used for one post-evaluation RuleResult."""

    return f"{runtime_subrule_id}::{target_kind or 'UNKNOWN'}::{target_id or 'UNKNOWN'}"


class EvaluationContext:
    """Proposal-local post-evaluation state that is deliberately outside CaseGraph.

    The scientific CaseGraph remains a record of CASE, SOURCE, and EDGE facts.
    Prior RuleResults are keyed separately by stable RuleInstance ID so dependency
    wiring cannot be mistaken for a scientific source or edge attribute. PR1B stores
    only the F02R02/F03R01 producer results needed for its explicit F06 replay.
    """

    def __init__(self, rule_results_by_instance: Mapping[str, Any] | None = None):
        if rule_results_by_instance is None:
            rule_results_by_instance = {}
        if not isinstance(rule_results_by_instance, Mapping):
            raise RulePrototypeError("EvaluationContext rule_results_by_instance must be a mapping")
        self.rule_results_by_instance = dict(rule_results_by_instance)

    @classmethod
    def from_mapping(
        cls,
        value: "EvaluationContext | Mapping[str, Any] | None",
    ) -> "EvaluationContext":
        if value is None:
            return cls()
        if isinstance(value, cls):
            return value
        if not isinstance(value, Mapping):
            raise RulePrototypeError("evaluation_context must be a mapping or EvaluationContext")
        return cls(value.get("rule_results_by_instance", {}))

    def status_for(
        self,
        *,
        runtime_subrule_id: str,
        target_kind: str,
        target_id: str,
    ) -> str:
        """Return a prior RuleResult status, or NOT_RUN when no result exists."""

        record = self.rule_results_by_instance.get(
            rule_instance_id(runtime_subrule_id, target_kind, target_id)
        )
        status = record.get("status") if isinstance(record, Mapping) else record
        return status if isinstance(status, str) and status else "NOT_RUN"

    def record(self, result: Mapping[str, Any]) -> None:
        """Store one validated RuleResult without allowing fallback-ID collisions.

        This deliberately stores a narrow identity-and-status record rather than an
        arbitrary caller object. ``NOT_RUN`` is a lookup sentinel and may not be
        stored. Callers must use a fresh context for a replay: an existing RuleResult
        with the same stable ID is rejected rather than silently overwritten.
        """

        if not isinstance(result, Mapping):
            raise RulePrototypeError("EvaluationContext.record requires a RuleResult mapping")
        runtime_subrule_id = result.get("runtime_subrule_id")
        target = result.get("target")
        if not isinstance(runtime_subrule_id, str) or not runtime_subrule_id.strip():
            raise RulePrototypeError("RuleResult runtime_subrule_id must be a nonempty string")
        if not isinstance(target, Mapping):
            raise RulePrototypeError("RuleResult target must be a mapping")
        target_kind = target.get("kind")
        target_id = target.get("id")
        if target_kind not in {"CASE", "SOURCE", "EDGE"}:
            raise RulePrototypeError("RuleResult target.kind must be CASE, SOURCE, or EDGE")
        if not isinstance(target_id, str) or not target_id.strip() or target_id == "UNKNOWN":
            raise RulePrototypeError("RuleResult target.id must be a nonempty, non-UNKNOWN string")
        expected_rule_instance_id = rule_instance_id(
            runtime_subrule_id, target_kind, target_id
        )
        supplied_rule_instance_id = result.get("rule_instance_id")
        if "::UNKNOWN" in expected_rule_instance_id or "::UNKNOWN" in str(
            supplied_rule_instance_id
        ):
            raise RulePrototypeError("RuleResult IDs may not use the UNKNOWN fallback")
        if supplied_rule_instance_id != expected_rule_instance_id:
            raise RulePrototypeError("RuleResult rule_instance_id does not match its identity")
        status = result.get("status")
        if status not in _STORED_RULE_RESULT_STATUSES:
            raise RulePrototypeError(
                "EvaluationContext may store only emitted RuleResult statuses"
            )
        if expected_rule_instance_id in self.rule_results_by_instance:
            raise RulePrototypeError("EvaluationContext refuses duplicate RuleResult IDs")
        self.rule_results_by_instance[expected_rule_instance_id] = {
            "rule_instance_id": expected_rule_instance_id,
            "runtime_subrule_id": runtime_subrule_id,
            "target": {"kind": target_kind, "id": target_id},
            "status": status,
        }


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


def _prior_result_target(
    expression: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
) -> tuple[str, str] | None:
    selector = expression.get("target_selector")
    if selector == "CURRENT_EDGE":
        if target.get("kind") != "EDGE":
            raise RulePrototypeError("CURRENT_EDGE prior-result selector requires an EDGE target")
        target_id = target.get("id")
        target_kind = "EDGE"
    elif selector == "EDGE_LEFT_SOURCE":
        target_id = resolve_path(case_graph, target, "edge.left_source_id")
        target_kind = "SOURCE"
    elif selector == "EDGE_RIGHT_SOURCE":
        target_id = resolve_path(case_graph, target, "edge.right_source_id")
        target_kind = "SOURCE"
    else:
        raise RulePrototypeError(f"unknown prior-result target selector: {selector!r}")

    if not isinstance(target_id, str) or not target_id:
        return None
    return target_kind, target_id


def _prior_result_status(
    expression: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    evaluation_context: EvaluationContext,
) -> str:
    runtime_subrule_id = expression.get("runtime_subrule_id")
    if not isinstance(runtime_subrule_id, str) or not runtime_subrule_id:
        raise RulePrototypeError("PRIOR_RESULT_STATUS requires a runtime_subrule_id")
    prior_target = _prior_result_target(expression, case_graph, target)
    if prior_target is None:
        return "NOT_RUN"
    target_kind, target_id = prior_target
    return evaluation_context.status_for(
        runtime_subrule_id=runtime_subrule_id,
        target_kind=target_kind,
        target_id=target_id,
    )


def evaluate_predicate(
    expression: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
) -> bool:
    """Evaluate the compact, explicit binding grammar."""

    op = expression.get("op")
    if op not in _PREDICATE_OPS:
        raise RulePrototypeError(f"undefined predicate primitive: {op!r}")
    context = EvaluationContext.from_mapping(evaluation_context)

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
    if op == "PRIOR_RESULT_STATUS":
        values = expression.get("values")
        if not isinstance(values, list):
            raise RulePrototypeError("PRIOR_RESULT_STATUS requires a values list")
        return _prior_result_status(expression, case_graph, target, context) in values
    if op == "NOT":
        argument = expression.get("arg")
        if not isinstance(argument, Mapping):
            raise RulePrototypeError("NOT requires an arg object")
        return not evaluate_predicate(argument, case_graph, target, context)

    arguments = expression.get("args")
    if not isinstance(arguments, list) or not arguments:
        raise RulePrototypeError(f"{op} requires a nonempty args list")
    if not all(isinstance(argument, Mapping) for argument in arguments):
        raise RulePrototypeError(f"{op} arguments must be objects")
    outcomes = [
        evaluate_predicate(argument, case_graph, target, context) for argument in arguments
    ]
    return all(outcomes) if op == "ALL" else any(outcomes)


def _evaluate_predicate_for_fail_scan(
    expression: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
) -> str:
    """Evaluate a fatal-failure predicate without treating missing facts as FALSE.

    This three-valued scan is used only before generic missing-evidence handling.
    It permits a known fatal contradiction in an ``ANY`` condition to win even if a
    different field is missing, while a failure that itself depends on missing
    evidence remains UNKNOWN and therefore cannot fabricate a FAIL outcome.
    """

    op = expression.get("op")
    if op not in _PREDICATE_OPS:
        raise RulePrototypeError(f"undefined predicate primitive: {op!r}")
    context = EvaluationContext.from_mapping(evaluation_context)

    if op == "EXISTS":
        return (
            _TRUE
            if _is_present(resolve_path(case_graph, target, str(expression["path"])))
            else _UNKNOWN
        )
    if op == "EQ":
        value = resolve_path(case_graph, target, str(expression["path"]))
        if not _is_present(value):
            return _UNKNOWN
        return _TRUE if value == expression.get("value") else _FALSE
    if op == "IN":
        values_path = expression.get("values_path")
        values = (
            resolve_path(case_graph, target, str(values_path))
            if values_path is not None
            else expression.get("values")
        )
        value = resolve_path(case_graph, target, str(expression["path"]))
        if not _is_present(value) or values is _MISSING or values is None:
            return _UNKNOWN
        if not isinstance(values, list):
            raise RulePrototypeError("IN requires a values list or values_path resolving to a list")
        return _TRUE if value in values else _FALSE
    if op == "PRIOR_RESULT_STATUS":
        values = expression.get("values")
        if not isinstance(values, list):
            raise RulePrototypeError("PRIOR_RESULT_STATUS requires a values list")
        return (
            _TRUE
            if _prior_result_status(expression, case_graph, target, context) in values
            else _FALSE
        )
    if op == "NOT":
        argument = expression.get("arg")
        if not isinstance(argument, Mapping):
            raise RulePrototypeError("NOT requires an arg object")
        outcome = _evaluate_predicate_for_fail_scan(argument, case_graph, target, context)
        if outcome == _UNKNOWN:
            return _UNKNOWN
        return _FALSE if outcome == _TRUE else _TRUE

    arguments = expression.get("args")
    if not isinstance(arguments, list) or not arguments:
        raise RulePrototypeError(f"{op} requires a nonempty args list")
    if not all(isinstance(argument, Mapping) for argument in arguments):
        raise RulePrototypeError(f"{op} arguments must be objects")
    outcomes = [
        _evaluate_predicate_for_fail_scan(argument, case_graph, target, context)
        for argument in arguments
    ]
    if op == "ALL":
        if _FALSE in outcomes:
            return _FALSE
        return _TRUE if all(outcome == _TRUE for outcome in outcomes) else _UNKNOWN
    if _TRUE in outcomes:
        return _TRUE
    return _FALSE if all(outcome == _FALSE for outcome in outcomes) else _UNKNOWN


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
        "rule_instance_id": rule_instance_id(
            subrule["runtime_subrule_id"],
            target.get("kind"),
            target.get("id"),
        ),
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
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
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
        if evaluate_predicate(condition, case_graph, target, evaluation_context):
            return str(entry.get("reason_code", "CONTRACT_CONDITION_MATCHED"))
    return None


def _first_known_fatal_reason(
    *,
    conditions: Any,
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
) -> str | None:
    """Return a confirmed fatal failure without converting missing facts to FAIL."""

    if not isinstance(conditions, list):
        raise RulePrototypeError("contract fail_conditions must be a list")
    for entry in conditions:
        if not isinstance(entry, Mapping):
            raise RulePrototypeError("contract fail_conditions entries must be objects")
        condition = entry.get("condition")
        if not isinstance(condition, Mapping):
            raise RulePrototypeError(
                "contract fail_conditions entries must include a condition object"
            )
        if (
            _evaluate_predicate_for_fail_scan(
                condition, case_graph, target, evaluation_context
            )
            == _TRUE
        ):
            return str(entry.get("reason_code", "CONTRACT_CONDITION_MATCHED"))
    return None


def evaluate_rule_instance(
    *,
    subrule: Mapping[str, Any],
    binding: Mapping[str, Any],
    contract: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    target: Mapping[str, Any],
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluate one already-targeted Draft RuleInstance with fail-closed outcomes.

    A confirmed failure blocks the RuleInstance even if another field remains
    unresolved. Otherwise an explicit unresolved condition wins. PASS requires a
    matching frozen pass condition; every unmatched state defaults to UNRESOLVED.
    """

    context = EvaluationContext.from_mapping(evaluation_context)
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
    if not evaluate_predicate(applicability, case_graph, target, context):
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

    fatal_failure_reason = _first_known_fatal_reason(
        conditions=contract.get("fail_conditions"),
        case_graph=case_graph,
        target=target,
        evaluation_context=context,
    )

    required_paths = binding.get("required_evidence_paths")
    if not isinstance(required_paths, list):
        raise RulePrototypeError("binding required_evidence_paths must be a list")
    missing_paths = [
        path
        for path in required_paths
        if not _is_present(resolve_path(case_graph, target, str(path)))
    ]
    if fatal_failure_reason is not None:
        return _result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            target=target,
            status="FAIL",
            applicability_status="MATCHED",
            reason_codes=[fatal_failure_reason],
            missing_paths=missing_paths,
        )
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
        evaluation_context=context,
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
        evaluation_context=context,
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
        evaluation_context=context,
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
    evaluation_context: EvaluationContext | Mapping[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Run the explicit PR1B prerequisite phase and its one F06 replay.

    Phase one evaluates F02R01, F02R02, and F03R01. Only the F02R02 and F03R01
    outputs are stored because F06R02 names them as dependencies. Phase two replays
    the F01/F06 Draft slice against that fresh proposal-local context. This is not a
    general dependency scheduler and does not store F06 or terminal conclusions.
    """

    subrule_by_id = {
        item["runtime_subrule_id"]: item
        for item in runtime_subrules.get("runtime_subrules", [])
    }
    contract_by_id = {
        item["evaluation_contract_id"]: item for item in contracts.get("contracts", [])
    }
    binding_by_subrule_id = {
        item["runtime_subrule_id"]: item for item in bindings.get("bindings", [])
    }
    planned_subrule_ids = set(_PR1B_PREREQUISITE_SUBRULE_IDS) | set(
        _PR1B_REPLAY_SUBRULE_IDS
    )
    unplanned_complete_drafts = {
        runtime_subrule_id
        for runtime_subrule_id, subrule in subrule_by_id.items()
        if subrule.get("implementation_status") == "COMPLETE_DRAFT"
        and runtime_subrule_id not in planned_subrule_ids
    }
    if unplanned_complete_drafts:
        raise RulePrototypeError(
            "PR1B evaluator has no explicit phase for complete Draft sub-rules: "
            + ", ".join(sorted(unplanned_complete_drafts))
        )

    context = EvaluationContext.from_mapping(evaluation_context)
    if context.rule_results_by_instance:
        raise RulePrototypeError(
            "PR1B active replay requires a fresh empty EvaluationContext"
        )
    results: list[dict[str, Any]] = []

    for phase_subrule_ids in (
        _PR1B_PREREQUISITE_SUBRULE_IDS,
        _PR1B_REPLAY_SUBRULE_IDS,
    ):
        for runtime_subrule_id in phase_subrule_ids:
            subrule = subrule_by_id.get(runtime_subrule_id)
            binding = binding_by_subrule_id.get(runtime_subrule_id)
            if subrule is None or binding is None:
                raise RulePrototypeError(
                    f"PR1B evaluator cannot resolve configured sub-rule: {runtime_subrule_id}"
                )
            if subrule.get("implementation_status") != "COMPLETE_DRAFT":
                raise RulePrototypeError(
                    f"PR1B evaluator requires a complete Draft sub-rule: {runtime_subrule_id}"
                )
            contract = contract_by_id.get(binding["evaluation_contract_id"])
            if contract is None:
                raise RulePrototypeError(
                    f"PR1B evaluator cannot resolve contract for: {runtime_subrule_id}"
                )
            for target in expand_targets(binding, case_graph):
                result = evaluate_rule_instance(
                    subrule=subrule,
                    binding=binding,
                    contract=contract,
                    case_graph=case_graph,
                    target=target,
                    evaluation_context=context,
                )
                results.append(result)
                if runtime_subrule_id in _PR1B_CONTEXT_PRODUCER_SUBRULE_IDS:
                    context.record(result)
    return results
