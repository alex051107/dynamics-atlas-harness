import copy
import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.rules_prototype_v1 import (
    EvaluationContext,
    RulePrototypeError,
    evaluate_active_rules,
    evaluate_rule_instance,
    rule_instance_id,
)


REPO_ROOT = Path(__file__).parents[2]
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
FIXTURES = Path(__file__).parent / "fixtures"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def target_from_reference(case_graph, reference):
    kind = reference["kind"]
    if kind == "CASE":
        return {"kind": "CASE", "id": case_graph["case"]["case_id"], "record": case_graph["case"]}
    collection = "evidence_items" if kind == "SOURCE" else "comparisons"
    key = "source_id" if kind == "SOURCE" else "comparison_id"
    record = next(item for item in case_graph[collection] if item[key] == reference["id"])
    return {"kind": kind, "id": reference["id"], "record": record}


def apply_mutation(case_graph, target, mutation):
    root, _, remainder = mutation["path"].partition(".")
    container = case_graph["case"] if root == "case" else target["record"]
    parts = remainder.split(".")
    for part in parts[:-1]:
        container = container[part]
    if mutation["op"] == "SET":
        container[parts[-1]] = mutation["value"]
    elif mutation["op"] == "DELETE":
        container.pop(parts[-1], None)
    else:
        raise AssertionError(f"unknown fixture mutation: {mutation['op']}")


def apply_context_mutation(evaluation_context, mutation):
    container = evaluation_context
    parts = mutation["path"].split(".")
    for part in parts[:-1]:
        container = container[part]
    if mutation["op"] == "SET":
        container[parts[-1]] = mutation["value"]
    elif mutation["op"] == "DELETE":
        container.pop(parts[-1], None)
    else:
        raise AssertionError(f"unknown evaluation-context mutation: {mutation['op']}")


class BindingBehaviorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subrules = {
            item["runtime_subrule_id"]: item
            for item in read_json(RULES_ROOT / "runtime_subrules_v1.json")["runtime_subrules"]
        }
        cls.bindings = {
            item["runtime_subrule_id"]: item
            for item in read_json(RULES_ROOT / "applicability_bindings_v1.json")["bindings"]
        }
        cls.contracts = {
            item["runtime_subrule_id"]: item
            for item in read_json(RULES_ROOT / "evaluation_contracts_v1.json")["contracts"]
        }
        cls.base_case = read_json(FIXTURES / "f01_f06_positive_casegraph.json")
        cls.evaluation_context = read_json(FIXTURES / "f01_f06_evaluation_context.json")
        cls.matrix = read_json(FIXTURES / "f01_f06_behavioral_matrix.json")

    def test_fixture_runner_exercises_all_required_behavior_classes(self):
        categories = {scenario["category"] for scenario in self.matrix["scenarios"]}
        self.assertTrue(
            {
                "positive",
                "one_field_negative",
                "missing_evidence",
                "wrong_target",
                "conflict",
                "request_scope",
                "unknown_status",
                "dependency",
            }.issubset(categories),
        )
        required_ids = {
            "F01R01_CASE_CLAIM_DECLARATION",
            "F01R02_CASE_REQUESTED_WORDING_SCOPE",
            "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
            "F02R02_EDGE_CONDITION_COMPATIBILITY",
            "F03R01_SOURCE_NATIVE_MEASUREMENT",
            "F06R01_SOURCE_EVIDENCE_ROLE",
            "F06R02_EDGE_COMPARABILITY",
            "F06R03_EDGE_VALIDATION_INDEPENDENCE",
        }
        for runtime_subrule_id in required_ids:
            seen = {
                scenario["category"]
                for scenario in self.matrix["scenarios"]
                if scenario["runtime_subrule_id"] == runtime_subrule_id
            }
            self.assertTrue(
                {"positive", "one_field_negative", "missing_evidence", "wrong_target", "conflict"}.issubset(seen)
            )

        for scenario in self.matrix["scenarios"]:
            with self.subTest(scenario=scenario["scenario_id"]):
                case_graph = copy.deepcopy(self.base_case)
                evaluation_context = copy.deepcopy(self.evaluation_context)
                target = target_from_reference(case_graph, scenario["target_ref"])
                for mutation in scenario["mutations"]:
                    apply_mutation(case_graph, target, mutation)
                for mutation in scenario.get("evaluation_context_mutations", []):
                    apply_context_mutation(evaluation_context, mutation)
                if "target_override" in scenario:
                    target = target_from_reference(case_graph, scenario["target_override"])
                result = evaluate_rule_instance(
                    subrule=self.subrules[scenario["runtime_subrule_id"]],
                    binding=self.bindings[scenario["runtime_subrule_id"]],
                    contract=self.contracts[scenario["runtime_subrule_id"]],
                    case_graph=case_graph,
                    target=target,
                    evaluation_context=evaluation_context,
                )
                self.assertEqual(result["status"], scenario["expected"]["status"])
                self.assertEqual(
                    result["applicability_status"],
                    scenario["expected"]["applicability_status"],
                )
                self.assertEqual(result["scientific_verdict"], "NOT_EMITTED_IN_PR1")
                self.assertTrue(result["human_decision_gate_required"])
                if "decision_class" in scenario["expected"]:
                    self.assertEqual(
                        result["claim_effect"]["decision_class"],
                        scenario["expected"]["decision_class"],
                    )
                if "route" in scenario["expected"]:
                    self.assertEqual(
                        result["claim_effect"]["route"], scenario["expected"]["route"]
                    )

    def test_active_slice_runs_fresh_draft_prerequisites_before_f06_replay(self):
        context = EvaluationContext()
        results = evaluate_active_rules(
            case_graph=self.base_case,
            runtime_subrules={"runtime_subrules": list(self.subrules.values())},
            bindings={"bindings": list(self.bindings.values())},
            contracts={"contracts": list(self.contracts.values())},
            evaluation_context=context,
        )
        self.assertEqual(len(results), 11)
        self.assertEqual(
            {result["family_id"] for result in results},
            {
                "F01_CLAIM_CONTRACT_AND_CEILING",
                "F02_SYSTEM_CONSTRUCT_AND_CONDITION",
                "F03_SOURCE_MEASUREMENT_SEMANTICS",
                "F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE",
            },
        )
        self.assertTrue(all(result["status"] == "PASS" for result in results))
        self.assertTrue(
            all(result["claim_effect"]["route"] != "REGISTERED_OPERATOR" for result in results)
        )
        self.assertTrue(
            all(
                result["rule_instance_id"]
                == rule_instance_id(
                    result["runtime_subrule_id"],
                    result["target"]["kind"],
                    result["target"]["id"],
                )
                for result in results
            )
        )
        self.assertEqual(len(context.rule_results_by_instance), 5)
        self.assertEqual(
            context.status_for(
                runtime_subrule_id="F02R02_EDGE_CONDITION_COMPATIBILITY",
                target_kind="EDGE",
                target_id="edge-construction-validation",
            ),
            "PASS",
        )
        for source_id in ("source-construction", "source-held-out"):
            self.assertEqual(
                context.status_for(
                    runtime_subrule_id="F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                    target_kind="SOURCE",
                    target_id=source_id,
                ),
                "PASS",
            )
            self.assertEqual(
                context.status_for(
                    runtime_subrule_id="F03R01_SOURCE_NATIVE_MEASUREMENT",
                    target_kind="SOURCE",
                    target_id=source_id,
                ),
                "PASS",
            )
        self.assertNotIn("prerequisite_rule_results", json.dumps(self.base_case))

        missing_measurement = copy.deepcopy(self.base_case)
        missing_measurement["evidence_items"][0].pop("estimand")
        missing_replay = evaluate_active_rules(
            case_graph=missing_measurement,
            runtime_subrules={"runtime_subrules": list(self.subrules.values())},
            bindings={"bindings": list(self.bindings.values())},
            contracts={"contracts": list(self.contracts.values())},
        )
        missing_by_instance = {
            result["rule_instance_id"]: result for result in missing_replay
        }
        self.assertEqual(
            missing_by_instance[
                rule_instance_id(
                    "F03R01_SOURCE_NATIVE_MEASUREMENT",
                    "SOURCE",
                    "source-construction",
                )
            ]["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            missing_by_instance[
                rule_instance_id(
                    "F06R02_EDGE_COMPARABILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            missing_by_instance[
                rule_instance_id(
                    "F06R03_EDGE_VALIDATION_INDEPENDENCE",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "PASS",
        )

        independent_but_noncomparable = copy.deepcopy(self.base_case)
        independent_but_noncomparable["comparisons"][0]["condition_relation"] = "MISMATCH"
        replay_results = evaluate_active_rules(
            case_graph=independent_but_noncomparable,
            runtime_subrules={"runtime_subrules": list(self.subrules.values())},
            bindings={"bindings": list(self.bindings.values())},
            contracts={"contracts": list(self.contracts.values())},
        )
        replay_by_instance = {result["rule_instance_id"]: result for result in replay_results}
        self.assertEqual(
            replay_by_instance[
                rule_instance_id(
                    "F02R02_EDGE_CONDITION_COMPATIBILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "FAIL",
        )
        self.assertEqual(
            replay_by_instance[
                rule_instance_id(
                    "F06R02_EDGE_COMPARABILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "FAIL",
        )
        self.assertEqual(
            replay_by_instance[
                rule_instance_id(
                    "F06R03_EDGE_VALIDATION_INDEPENDENCE",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "PASS",
        )

        f02r01_unresolved = copy.deepcopy(self.base_case)
        f02r01_unresolved["evidence_items"][0].pop("sample_composition")
        f02r01_replay = evaluate_active_rules(
            case_graph=f02r01_unresolved,
            runtime_subrules={"runtime_subrules": list(self.subrules.values())},
            bindings={"bindings": list(self.bindings.values())},
            contracts={"contracts": list(self.contracts.values())},
        )
        f02r01_by_instance = {
            result["rule_instance_id"]: result for result in f02r01_replay
        }
        self.assertEqual(
            f02r01_by_instance[
                rule_instance_id(
                    "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                    "SOURCE",
                    "source-construction",
                )
            ]["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            f02r01_by_instance[
                rule_instance_id(
                    "F02R02_EDGE_CONDITION_COMPATIBILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            f02r01_by_instance[
                rule_instance_id(
                    "F06R02_EDGE_COMPARABILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "UNRESOLVED",
        )

        contradicted_f02r01 = copy.deepcopy(self.base_case)
        contradicted_f02r01["evidence_items"][0][
            "sample_system_composition_declaration_status"
        ] = "CONTRADICTED"
        contradicted_replay = evaluate_active_rules(
            case_graph=contradicted_f02r01,
            runtime_subrules={"runtime_subrules": list(self.subrules.values())},
            bindings={"bindings": list(self.bindings.values())},
            contracts={"contracts": list(self.contracts.values())},
        )
        contradicted_by_instance = {
            result["rule_instance_id"]: result for result in contradicted_replay
        }
        self.assertEqual(
            contradicted_by_instance[
                rule_instance_id(
                    "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
                    "SOURCE",
                    "source-construction",
                )
            ]["status"],
            "FAIL",
        )
        self.assertEqual(
            contradicted_by_instance[
                rule_instance_id(
                    "F02R02_EDGE_CONDITION_COMPATIBILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "UNRESOLVED",
        )
        self.assertEqual(
            contradicted_by_instance[
                rule_instance_id(
                    "F06R02_EDGE_COMPARABILITY",
                    "EDGE",
                    "edge-construction-validation",
                )
            ]["status"],
            "UNRESOLVED",
        )

    def test_evaluation_context_rejects_fallback_and_duplicate_rule_result_ids(self):
        result = {
            "runtime_subrule_id": "F03R01_SOURCE_NATIVE_MEASUREMENT",
            "target": {"kind": "SOURCE", "id": "source-record-1"},
            "rule_instance_id": rule_instance_id(
                "F03R01_SOURCE_NATIVE_MEASUREMENT", "SOURCE", "source-record-1"
            ),
            "status": "PASS",
        }
        context = EvaluationContext()
        context.record(result)
        self.assertEqual(
            context.status_for(
                runtime_subrule_id="F03R01_SOURCE_NATIVE_MEASUREMENT",
                target_kind="SOURCE",
                target_id="source-record-1",
            ),
            "PASS",
        )
        with self.assertRaisesRegex(RulePrototypeError, "duplicate"):
            context.record(result)

        unknown_target = copy.deepcopy(result)
        unknown_target["target"]["id"] = "UNKNOWN"
        unknown_target["rule_instance_id"] = rule_instance_id(
            "F03R01_SOURCE_NATIVE_MEASUREMENT", "SOURCE", "UNKNOWN"
        )
        with self.assertRaisesRegex(RulePrototypeError, "nonempty, non-UNKNOWN"):
            EvaluationContext().record(unknown_target)

        mismatched_id = copy.deepcopy(result)
        mismatched_id["rule_instance_id"] = "F03R01_SOURCE_NATIVE_MEASUREMENT::SOURCE::other"
        with self.assertRaisesRegex(RulePrototypeError, "does not match"):
            EvaluationContext().record(mismatched_id)

        not_run = copy.deepcopy(result)
        not_run["status"] = "NOT_RUN"
        with self.assertRaisesRegex(RulePrototypeError, "emitted RuleResult statuses"):
            EvaluationContext().record(not_run)

        phantom_case = copy.deepcopy(self.base_case)
        phantom_case["comparisons"][0]["right_source_id"] = "phantom-source"
        preseeded = EvaluationContext(
            {
                rule_instance_id(
                    "F03R01_SOURCE_NATIVE_MEASUREMENT",
                    "SOURCE",
                    "phantom-source",
                ): {"status": "PASS"}
            }
        )
        with self.assertRaisesRegex(RulePrototypeError, "fresh empty"):
            evaluate_active_rules(
                case_graph=phantom_case,
                runtime_subrules={"runtime_subrules": list(self.subrules.values())},
                bindings={"bindings": list(self.bindings.values())},
                contracts={"contracts": list(self.contracts.values())},
                evaluation_context=preseeded,
            )


if __name__ == "__main__":
    unittest.main()
