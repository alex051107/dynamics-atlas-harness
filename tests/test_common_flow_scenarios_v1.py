"""Behavioral tests for the deterministic common-flow scenario suite."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.common_flow_scenarios_v1 import (
    CANNOT_SUPPORT_SCENARIO_ID,
    COMPUTATION_SCENARIO_ID,
    DIRECT_SCENARIO_ID,
    LOOKUP_SCENARIO_ID,
    STOP_SCENARIO_ID,
    SYNTHETIC_SUPPORT_SCENARIO_ID,
    run_common_flow_scenario_suite,
)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class CommonFlowScenarioSuiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary_directory = tempfile.TemporaryDirectory()
        cls.output_dir = Path(cls._temporary_directory.name) / "scenario-suite"
        cls.result = run_common_flow_scenario_suite(output_dir=cls.output_dir)
        cls.manifest = read_json(cls.output_dir / "scenario_suite_manifest.json")
        cls.matrix = read_json(cls.output_dir / "common_flow_matrix.json")
        cls.rows = {
            row["scenario_id"]: row for row in cls.matrix["scenarios"]
        }

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary_directory.cleanup()

    def test_four_routes_and_three_terminal_behaviors_are_materialized(self):
        self.assertEqual(
            list(self.rows),
            [
                DIRECT_SCENARIO_ID,
                LOOKUP_SCENARIO_ID,
                COMPUTATION_SCENARIO_ID,
                STOP_SCENARIO_ID,
                SYNTHETIC_SUPPORT_SCENARIO_ID,
                CANNOT_SUPPORT_SCENARIO_ID,
            ],
        )
        self.assertEqual(
            {
                self.rows[scenario_id]["expected_route_family"]
                for scenario_id in (
                    DIRECT_SCENARIO_ID,
                    LOOKUP_SCENARIO_ID,
                    COMPUTATION_SCENARIO_ID,
                    STOP_SCENARIO_ID,
                )
            },
            {
                "DIRECT_EVALUATION",
                "NARROW_LOOKUP",
                "REGISTERED_COMPUTATION",
                "EXPLICIT_STOP",
            },
        )
        self.assertEqual(
            {row["terminal_reducer_state"] for row in self.rows.values()},
            {
                "SUPPORT_WITHIN_CEILING",
                "CANNOT_SUPPORT_REQUESTED_CLAIM",
                "ABSTAIN_OR_HUMAN_REVIEW",
            },
        )
        self.assertEqual(
            self.rows[DIRECT_SCENARIO_ID]["actual_route"], "DIRECT_EVALUATION"
        )
        self.assertEqual(
            self.rows[STOP_SCENARIO_ID]["actual_route"], "HUMAN_OR_NEW_DATA"
        )

    def test_narrow_lookup_records_exact_same_target_rule_and_all_dependency_diffs(self):
        row = self.rows[LOOKUP_SCENARIO_ID]
        target_rule_id = row["affected_rule_instance"]
        self.assertEqual(row["before_rule_result"]["rule_instance_id"], target_rule_id)
        self.assertEqual(row["after_rule_result"]["rule_instance_id"], target_rule_id)
        self.assertEqual(row["before_rule_result"]["status"], "UNRESOLVED")
        self.assertEqual(row["after_rule_result"]["status"], "PASS")
        self.assertEqual(row["action_count"], 1)
        self.assertEqual(row["evidence_result_class"], "SOURCE_LOOKUP_RESULT")

        transition_path = next(
            self.output_dir / path
            for path in row["artifact_paths"]
            if path.endswith("rule_transition.json")
        )
        transition = read_json(transition_path)
        self.assertEqual(transition["affected_rule_instance_id"], target_rule_id)
        self.assertIn(
            target_rule_id,
            {
                item["rule_instance_id"]
                for item in transition["all_changed_rule_statuses"]
            },
        )
        lookup_result = read_json(
            self.output_dir
            / f"scenarios/{LOOKUP_SCENARIO_ID}/lookup_result.json"
        )
        self.assertEqual(lookup_result["status"], "FOUND")
        self.assertEqual(lookup_result["route"], "SOURCE_LOOKUP")
        self.assertIn("fixture_sha256", lookup_result)

    def test_registered_computation_is_exact_control_same_rule_and_not_broad_closure(self):
        row = self.rows[COMPUTATION_SCENARIO_ID]
        self.assertEqual(row["before_rule_result"]["status"], "UNRESOLVED")
        self.assertEqual(row["after_rule_result"]["status"], "PASS")
        self.assertEqual(
            row["before_rule_result"]["rule_instance_id"],
            row["affected_rule_instance"],
        )
        self.assertEqual(
            row["after_rule_result"]["rule_instance_id"],
            row["affected_rule_instance"],
        )
        self.assertEqual(row["evidence_result_class"], "OPERATOR_EVIDENCE_RESULT")
        self.assertTrue(row["claim_ceiling"].startswith("EXACT_CONTROL_ONLY:"))
        self.assertEqual(
            row["terminal_reducer_state"], "ABSTAIN_OR_HUMAN_REVIEW"
        )
        evidence = read_json(
            self.output_dir
            / f"scenarios/{COMPUTATION_SCENARIO_ID}/evidence_result.json"
        )
        self.assertEqual(evidence["affected_rule_instance_id"], row["affected_rule_instance"])
        self.assertEqual(evidence["contract_status"], "PASS")
        self.assertEqual(
            evidence["scientific_evaluation_status"], "PENDING_HUMAN_VALIDATION"
        )
        self.assertEqual(
            self.manifest["hsp90_broad_closure_status"],
            "NOT_ESTABLISHED_EXACT_CONTROL_ONLY",
        )

    def test_explicit_stop_preserves_unresolved_rule_and_runs_no_unauthorized_analysis(self):
        row = self.rows[STOP_SCENARIO_ID]
        self.assertEqual(row["before_rule_result"]["status"], "UNRESOLVED")
        self.assertEqual(row["after_rule_result"]["status"], "UNRESOLVED")
        stop_receipt = read_json(
            self.output_dir / f"scenarios/{STOP_SCENARIO_ID}/stop_receipt.json"
        )
        self.assertEqual(stop_receipt["lookup_status"], "NOT_FOUND")
        self.assertEqual(stop_receipt["route"], "HUMAN_OR_NEW_DATA")
        self.assertEqual(stop_receipt["authorized_lookup_actions"], 1)
        self.assertEqual(stop_receipt["unauthorized_analysis_actions"], 0)
        self.assertEqual(stop_receipt["unregistered_tool_calls"], 0)
        self.assertFalse(stop_receipt["network_accessed"])

    def test_support_is_synthetic_only_and_real_authority_is_not_upgraded(self):
        row = self.rows[SYNTHETIC_SUPPORT_SCENARIO_ID]
        self.assertEqual(row["terminal_reducer_state"], "SUPPORT_WITHIN_CEILING")
        self.assertEqual(
            row["authority_status"], "SYNTHETIC_CONTRACT_BEHAVIOR_ONLY"
        )
        self.assertTrue(
            row["claim_ceiling"].startswith("SYNTHETIC_CONTRACT_BEHAVIOR_ONLY:")
        )
        authority_receipt = read_json(
            self.output_dir
            / f"scenarios/{SYNTHETIC_SUPPORT_SCENARIO_ID}/authority_receipt.json"
        )
        self.assertEqual(
            authority_receipt["source_grounding_authority"],
            "SYNTHETIC_OVERRIDE_NOT_REPOSITORY_STATUS",
        )
        self.assertEqual(authority_receipt["real_scientific_support_packets"], 0)
        self.assertFalse(authority_receipt["scientific_claim_upgrade"])
        self.assertEqual(self.manifest["real_scientific_support_packets"], 0)
        self.assertEqual(self.manifest["synthetic_contract_support_packets"], 1)
        self.assertEqual(
            self.manifest["source_science_review_status"], "PENDING_DOMAIN_REVIEW"
        )

    def test_explicit_mismatch_uses_existing_reducer_cannot_support_branch(self):
        row = self.rows[CANNOT_SUPPORT_SCENARIO_ID]
        self.assertEqual(
            row["terminal_reducer_state"], "CANNOT_SUPPORT_REQUESTED_CLAIM"
        )
        stage2 = read_json(
            self.output_dir
            / f"scenarios/{CANNOT_SUPPORT_SCENARIO_ID}/stage2_conclusion_packet.json"
        )
        self.assertEqual(stage2["route_disposition"], "RELATION_BLOCKED")
        self.assertEqual(stage2["first_failed_dependency"]["status"], "FAIL")
        self.assertFalse(stage2["unsafe_claim_upgrade"])
        self.assertIn("cross-source relation", stage2["current_claim_ceiling"])

    def test_manifest_and_matrix_use_relative_existing_deterministic_artifact_paths(self):
        self.assertFalse(self.manifest["network_accessed"])
        self.assertEqual(self.manifest["model_calls"], 0)
        self.assertEqual(self.manifest["credential_reads"], 0)
        self.assertEqual(self.manifest["external_spend"], 0.0)
        self.assertEqual(
            self.result["matrix"]["scenarios"], self.matrix["scenarios"]
        )
        for row in self.matrix["scenarios"]:
            self.assertEqual(row["actual_cost"], 0.0)
            self.assertEqual(row["result_status"], "SUCCEEDED")
            for relative_path in row["artifact_paths"]:
                path = Path(relative_path)
                self.assertFalse(path.is_absolute())
                self.assertNotIn("..", path.parts)
                self.assertTrue((self.output_dir / path).is_file(), relative_path)

    def test_nonempty_output_directory_is_rejected_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "nonempty"
            output_dir.mkdir()
            sentinel = output_dir / "keep.txt"
            sentinel.write_text("preserve", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY"):
                run_common_flow_scenario_suite(output_dir=output_dir)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
            self.assertEqual(list(output_dir.iterdir()), [sentinel])


if __name__ == "__main__":
    unittest.main()
