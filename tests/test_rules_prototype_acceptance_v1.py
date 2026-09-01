import csv
import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.rules_prototype_acceptance_v1 import (
    run_acceptance_suite,
    write_acceptance_artifacts,
)


REPO_ROOT = Path(__file__).parents[1]
ARTIFACT_ROOT = REPO_ROOT / "research" / "rules_prototype_acceptance_v1"


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def status_by_rule_instance(results):
    return {result["rule_instance_id"]: result["status"] for result in results}


class RulesPrototypeAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = {
            row["task_id"]: row for row in read_jsonl(ARTIFACT_ROOT / "expected_results.jsonl")
        }
        cls.suite = run_acceptance_suite(repo_root=REPO_ROOT)
        cls.actual = {row["task_id"]: row for row in cls.suite["results"]}

    def test_all_eight_cards_match_their_independent_expected_results(self):
        self.assertEqual(set(self.actual), set(self.expected))
        self.assertEqual(len(self.actual), 8)
        for task_id, expected in self.expected.items():
            with self.subTest(task_id=task_id):
                actual = self.actual[task_id]
                self.assertEqual(
                    [item["rule_instance_id"] for item in actual["applicable_rule_instances"]
                     if item["rule_instance_id"] in expected["expected_applicable_rule_instance_ids"]],
                    expected["expected_applicable_rule_instance_ids"],
                )
                self.assertEqual(actual["target_kinds"], expected["expected_target_kinds"])
                self.assertEqual(actual["legal_route"], expected["expected_legal_route"])
                self.assertEqual(
                    actual["executed_action"]["action_kind"],
                    expected["expected_executed_action"],
                )
                self.assertEqual(len(actual["evidence_results"]), expected["expected_evidence_count"])
                initial_statuses = status_by_rule_instance(actual["initial_rule_results"])
                post_statuses = status_by_rule_instance(actual["post_action_rule_results"])
                for rule_instance_id, expected_status in expected["expected_initial_statuses"].items():
                    self.assertEqual(initial_statuses[rule_instance_id], expected_status)
                for rule_instance_id, expected_status in expected["expected_post_statuses"].items():
                    self.assertEqual(post_statuses[rule_instance_id], expected_status)
                self.assertEqual(actual["rule_transitions"], expected["expected_transitions"])
                self.assertEqual(
                    actual["conclusion_packet"]["terminal_state"],
                    expected["expected_terminal_state"],
                )

    def test_common_runtime_preserves_route_and_claim_boundaries(self):
        summary = self.suite["summary"]
        self.assertEqual(summary["task_count"], 8)
        self.assertTrue(
            {"DIRECT_EVALUATION", "EXACT_LOOKUP", "REGISTERED_OPERATOR", "STOP"}.issubset(
                set(summary["action_kinds"])
            )
        )
        self.assertTrue({"PASS", "FAIL", "UNRESOLVED"}.issubset(summary["post_rule_statuses"]))
        self.assertEqual(
            set(summary["terminal_states"]),
            {
                "SUPPORT_WITHIN_CEILING",
                "CANNOT_SUPPORT_REQUESTED_CLAIM",
                "ABSTAIN_OR_HUMAN_REVIEW",
            },
        )
        self.assertGreaterEqual(summary["same_rule_closure_count"], 1)
        self.assertEqual(summary["unregistered_tool_calls"], 0)
        self.assertEqual(summary["wrong_rule_instance_mutations"], 0)
        self.assertEqual(summary["unsafe_claim_upgrades"], 0)
        for actual in self.actual.values():
            self.assertEqual(actual["conclusion_packet"]["scientific_disposition"], "NOT_EVALUATED")
            self.assertTrue(actual["conclusion_packet"]["human_decision_gate_required"])
            self.assertFalse(actual["conclusion_packet"]["unsafe_claim_upgrade"])

    def test_generated_artifacts_are_reconstructable_from_cases_only(self):
        with tempfile.TemporaryDirectory(prefix="rules-prototype-acceptance-") as temp_dir:
            output_root = Path(temp_dir)
            write_acceptance_artifacts(artifacts_dir=output_root, suite=self.suite)
            actual_rows = read_jsonl(output_root / "actual_results.jsonl")
            self.assertEqual([row["task_id"] for row in actual_rows], list(self.actual))
            with (output_root / "acceptance_matrix.csv").open(encoding="utf-8") as handle:
                matrix = list(csv.DictReader(handle))
            self.assertEqual(len(matrix), 8)
            self.assertTrue(all(row["acceptance"] == "PASS" for row in matrix))
            report = (output_root / "REPORT.md").read_text(encoding="utf-8")
            self.assertIn("does not load expected_results.jsonl", report)
            self.assertIn("scientific_disposition = NOT_EVALUATED", report)


if __name__ == "__main__":
    unittest.main()
