import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parents[2]
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
METHODOLOGY_ROOT = REPO_ROOT / "methodology"


def read_json(name):
    return json.loads((RULES_ROOT / name).read_text(encoding="utf-8"))


class ContractConsistencyTests(unittest.TestCase):
    def test_seven_families_and_twelve_single_target_subrules_resolve(self):
        overlay = read_json("family_overlay_v1.json")
        methodology = json.loads(
            (METHODOLOGY_ROOT / "methodology_map_v1.json").read_text(encoding="utf-8")
        )
        subrules = read_json("runtime_subrules_v1.json")["runtime_subrules"]
        bindings = read_json("applicability_bindings_v1.json")["bindings"]
        contracts = read_json("evaluation_contracts_v1.json")["contracts"]
        policies = read_json("resolution_policies_v1.json")["policies"]
        gates = read_json("human_decision_gates_v1.json")["gates"]
        actions = read_json("action_vocabulary_v1.json")

        self.assertEqual(len(overlay["families"]), 7)
        self.assertEqual(len(methodology["human_facing_families"]), 7)
        self.assertEqual(
            {family["family_id"] for family in methodology["human_facing_families"]},
            {family["family_id"] for family in overlay["families"]},
        )
        self.assertEqual(len(subrules), 12)
        self.assertEqual(
            {subrule["target_kind"] for subrule in subrules}, {"CASE", "SOURCE", "EDGE"}
        )
        self.assertEqual(
            sum(subrule["implementation_status"] == "COMPLETE_DRAFT" for subrule in subrules),
            8,
        )

        binding_by_subrule = {binding["runtime_subrule_id"]: binding for binding in bindings}
        contract_by_subrule = {
            contract["runtime_subrule_id"]: contract for contract in contracts
        }
        policy_ids = {policy["resolution_policy_id"] for policy in policies}
        gate_ids = {gate["human_decision_gate_id"] for gate in gates}
        action_ids = {route["route"] for route in actions["routes"]}

        self.assertEqual(
            action_ids,
            {"DIRECT_EVALUATION", "SOURCE_LOOKUP", "REGISTERED_OPERATOR", "HUMAN_OR_NEW_DATA"},
        )
        for subrule in subrules:
            with self.subTest(subrule=subrule["runtime_subrule_id"]):
                binding = binding_by_subrule[subrule["runtime_subrule_id"]]
                contract = contract_by_subrule[subrule["runtime_subrule_id"]]
                self.assertEqual(binding["target_kind"], subrule["target_kind"])
                self.assertEqual(contract["target_kind"], subrule["target_kind"])
                self.assertIn(binding["resolution_policy_id"], policy_ids)
                self.assertIn(contract["human_decision_gate_id"], gate_ids)
                self.assertNotIn(
                    "human_decision",
                    json.dumps(binding["required_evidence_paths"]),
                )
                self.assertNotIn(
                    "human_decision",
                    json.dumps(contract["fail_conditions"]),
                )
                self.assertNotIn(
                    "human_decision",
                    json.dumps(contract["pass_conditions"]),
                )
                self.assertNotIn(
                    "human_decision",
                    json.dumps(contract["unresolved_conditions"]),
                )

        for policy in policies:
            self.assertIsInstance(policy["operator_route_allowed"], bool)
            self.assertTrue(set(policy["allowed_routes"]).issubset(action_ids))

    def test_contracts_are_explicit_and_fail_closed(self):
        contracts = read_json("evaluation_contracts_v1.json")["contracts"]
        for contract in contracts:
            with self.subTest(contract=contract["evaluation_contract_id"]):
                for field in ("pass_conditions", "fail_conditions", "unresolved_conditions"):
                    self.assertIsInstance(contract[field], list)
                    for entry in contract[field]:
                        self.assertTrue(entry["reason_code"])
                        self.assertIn("condition", entry)
                self.assertNotIn("edge.prerequisite_rule_results", json.dumps(contract))
                if contract["implementation_status"] == "COMPLETE_DRAFT":
                    self.assertTrue(contract["pass_conditions"])
                    self.assertTrue(contract["fail_conditions"])
                    self.assertTrue(contract["unresolved_conditions"])

        f06r02 = next(
            contract
            for contract in contracts
            if contract["runtime_subrule_id"] == "F06R02_EDGE_COMPARABILITY"
        )
        f02r02 = next(
            contract
            for contract in contracts
            if contract["runtime_subrule_id"] == "F02R02_EDGE_CONDITION_COMPATIBILITY"
        )
        f06r03 = next(
            contract
            for contract in contracts
            if contract["runtime_subrule_id"] == "F06R03_EDGE_VALIDATION_INDEPENDENCE"
        )
        self.assertIn("PRIOR_RESULT_STATUS", json.dumps(f06r02))
        self.assertIn(
            "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION", json.dumps(f02r02)
        )
        self.assertIn("EDGE_LEFT_SOURCE", json.dumps(f02r02))
        self.assertIn("EDGE_RIGHT_SOURCE", json.dumps(f02r02))
        self.assertNotIn("condition_relation", json.dumps(f06r03))
        self.assertNotIn("F02R02_EDGE_CONDITION_COMPATIBILITY", json.dumps(f06r03))
        self.assertNotIn("F03R01_SOURCE_NATIVE_MEASUREMENT", json.dumps(f06r03))

    def test_human_gate_separates_architecture_source_grounding_and_runtime_readiness(self):
        gates = {
            gate["human_decision_gate_id"]: gate
            for gate in read_json("human_decision_gates_v1.json")["gates"]
        }
        architecture = gates["HDG-RULES-V1-SCIENTIFIC-REVIEW"]
        source_science = gates["HDG-RULES-V1-SOURCE-SCIENCE-REVIEW"]
        self.assertEqual(architecture["gate_role"], "ARCHITECTURE_AND_RUNTIME_READINESS")
        self.assertEqual(
            architecture["review_dimensions"]["architecture_decision"]["allowed_decisions"],
            ["APPROVE", "REVISE", "REJECT", "DEFER"],
        )
        self.assertEqual(
            architecture["review_dimensions"]["runtime_readiness"]["allowed_decisions"],
            ["READY_FOR_NEXT_DRAFT", "NOT_READY", "DEFER"],
        )
        self.assertEqual(
            source_science["review_dimensions"]["source_grounding_decision"]["allowed_decisions"],
            ["VERIFIED", "PENDING_DOMAIN_REVIEW", "REJECTED"],
        )
        self.assertIn("rule_status", architecture["does_not_control"])
        self.assertIn("scientific_claim_ceiling", architecture["does_not_control"])

    def test_family_overlay_records_three_review_dimensions(self):
        families = read_json("family_overlay_v1.json")["families"]
        for family in families:
            with self.subTest(family=family["family_id"]):
                self.assertIn(
                    family["architecture_decision"], {"APPROVE", "REVISE", "REJECT", "DEFER"}
                )
                self.assertEqual(family["source_grounding_decision"], "PENDING_DOMAIN_REVIEW")
                self.assertIn(
                    family["runtime_readiness"],
                    {"READY_FOR_NEXT_DRAFT", "NOT_READY", "DEFER"},
                )

    def test_source_lookup_is_declared_only_in_this_draft(self):
        actions = {
            item["route"]: item
            for item in read_json("action_vocabulary_v1.json")["routes"]
        }
        lookup = actions["SOURCE_LOOKUP"]
        self.assertFalse(lookup["execution_allowed_in_pr1"])
        self.assertEqual(lookup["implementation_status"], "DECLARED_ONLY_NO_EXECUTOR_IN_PR1")

    def test_coverage_gap_register_is_candidate_only(self):
        records = [
            json.loads(line)
            for line in (METHODOLOGY_ROOT / "coverage_gap_register_v1.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line
        ]
        self.assertEqual(len(records), 4)
        self.assertTrue(
            all(record["status"].startswith("CANDIDATE_") for record in records)
        )
        self.assertTrue(
            all("forbidden_upgrade" in record for record in records)
        )


if __name__ == "__main__":
    unittest.main()
