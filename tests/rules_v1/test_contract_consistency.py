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
            5,
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

        for policy in policies:
            self.assertIsInstance(policy["operator_route_allowed"], bool)
            self.assertTrue(set(policy["allowed_routes"]).issubset(action_ids))

    def test_human_gate_is_separate_from_scientific_evaluation(self):
        gate = read_json("human_decision_gates_v1.json")["gates"][0]
        self.assertEqual(gate["status"], "PENDING_HUMAN_SCIENTIFIC_REVIEW")
        self.assertEqual(gate["allowed_decisions"], ["APPROVE", "REVISE", "REJECT", "DEFER"])
        self.assertIn("rule_status", gate["does_not_control"])
        self.assertIn("scientific_claim_ceiling", gate["does_not_control"])

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
