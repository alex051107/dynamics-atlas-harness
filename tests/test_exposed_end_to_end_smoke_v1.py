"""Behavioral checks for the bounded paper-question-to-human-review smoke path."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import main
from dynamics_atlas_harness.exposed_end_to_end_smoke_v1 import (
    ExposedEndToEndSmokeError,
    _bind_authorized_proposal,
    _execute_exact_bound_routes,
    materialize_and_bind_exposed_case,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ExposedEndToEndSmokeV1Tests(unittest.TestCase):
    def test_command_connects_existing_paper_question_agent_routes_tools_and_human_packet(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            self.assertEqual(main(["run-smoke", "--output-dir", str(output_dir)]), 0)

            question = read_json(output_dir / "inputs/xeisd_paper_question.json")
            xeisd_binding = read_json(output_dir / "tracks/xeisd_route_binding.json")
            hsp90_binding = read_json(output_dir / "tracks/hsp90_route_binding.json")
            xeisd_pre_agent_rules = read_json(
                output_dir / "rules/xeisd_pre_agent_rule_selection.json"
            )
            hsp90_pre_agent_rules = read_json(
                output_dir / "rules/hsp90_pre_agent_rule_selection.json"
            )
            human = read_json(output_dir / "human_decision_packet.json")
            summary = read_json(output_dir / "run_summary.json")
            manifest = read_json(output_dir / "run_manifest.json")
            execution = read_json(output_dir / "bound_execution/execution_manifest.json")

            self.assertEqual(question["paper_identity"]["doi"], "10.1038/s42004-020-0323-0")
            self.assertEqual(question["case_id"], xeisd_binding["case_id"])
            self.assertTrue(
                all(
                    result["status"] == "UNRESOLVED"
                    for result in xeisd_pre_agent_rules["rule_results"]
                    if result["rule_instance_id"] in xeisd_binding["selected_rule_instance_ids"]
                )
            )
            self.assertEqual(
                xeisd_pre_agent_rules["case_graph_admission"]["status"], "PASS"
            )
            self.assertEqual(
                hsp90_pre_agent_rules["case_graph_admission"]["status"], "PASS"
            )
            self.assertEqual(hsp90_pre_agent_rules["rule_results"][0]["status"], "UNRESOLVED")
            self.assertEqual(
                xeisd_binding["selected_track"],
                "EXACT_REVIEW_DERIVATIVE_ATTESTATION_THEN_DIRECT_EVALUATION",
            )
            self.assertEqual(
                hsp90_binding["selected_track"],
                "EXACT_CASE_BOUND_REGISTERED_OPERATOR_THEN_RULE_REEVALUATION",
            )
            self.assertEqual(
                read_json(output_dir / "agent/xeisd/evaluation.json")[
                    "sealed_reference_and_authorization_view"
                ]["status"],
                "PASS",
            )
            self.assertEqual(
                read_json(output_dir / "agent/hsp90/evaluation.json")[
                    "sealed_reference_and_authorization_view"
                ]["deterministic_authorization"]["status"],
                "AUTHORIZED_NO_EXECUTION",
            )
            self.assertEqual(
                read_json(output_dir / "bound_execution/routes/hsp90_b1/evidence_result.json")[
                    "contract_status"
                ],
                "PASS",
            )
            self.assertEqual(
                read_json(output_dir / "bound_execution/routes/hsp90_b1/post_operator_rule_result.json")[
                    "status"
                ],
                "PASS",
            )
            self.assertEqual(human["system_recommendation"], "ABSTAIN_OR_HUMAN_REVIEW")
            self.assertEqual(human["scientific_disposition"], "NOT_EVALUATED")
            self.assertEqual(summary["scientific_support_packets"], 0)
            self.assertEqual(summary["source_science_review_status"], "PENDING_DOMAIN_REVIEW")
            self.assertEqual(manifest["live_model_calls"], 0)
            self.assertFalse(manifest["external_network_accessed"])
            self.assertEqual(
                [track["case_key"] for track in execution["executed_tracks"]],
                ["xeisd", "hsp90"],
            )
            self.assertEqual(
                execution["deliberately_unexecuted_reference_scenarios"],
                ["XEISD_A2_MISSING_COMPOSITION", "XEISD_A3_EXPLICIT_CONDITION_MISMATCH"],
            )
            self.assertFalse((output_dir / "bound_execution/routes/xeisd_a2").exists())
            self.assertFalse((output_dir / "bound_execution/routes/xeisd_a3").exists())

    def test_bind_rejects_card_target_mismatch_before_reference_tools_run(self):
        artifacts = materialize_and_bind_exposed_case(case_key="xeisd", repo_root=REPO_ROOT)
        altered = copy.deepcopy(artifacts["materialization"])
        altered["canonical_proposal"]["proposed_actions"][0]["target_rule_instance_id"] = "wrong-rule"
        with self.assertRaisesRegex(
            ExposedEndToEndSmokeError, "PLANNER_CARD_TARGETS_DO_NOT_MATCH_SELECTED_RULES"
        ):
            _bind_authorized_proposal(
                case_key="xeisd",
                packet=artifacts["planner_packet"],
                pre_agent_rule_selection=artifacts["pre_agent_rule_selection"],
                materialization=altered,
                evaluation=artifacts["evaluation"],
            )

    def test_invalid_bound_track_produces_no_operator_receipt(self):
        bindings = {
            case_key: materialize_and_bind_exposed_case(
                case_key=case_key, repo_root=REPO_ROOT
            )["route_binding"]
            for case_key in ("xeisd", "hsp90")
        }
        bindings["hsp90"]["selected_track"] = "UNAUTHORIZED_TRACK"
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            with self.assertRaisesRegex(
                ExposedEndToEndSmokeError, "HSP90_BOUND_TRACK_NOT_EXECUTABLE"
            ):
                _execute_exact_bound_routes(
                    repo_root=REPO_ROOT,
                    output_dir=output_dir,
                    bindings=bindings,
                )
            self.assertFalse((output_dir / "bound_execution").exists())
            self.assertFalse(
                (
                    output_dir
                    / "bound_execution/routes/hsp90_b1/operator_run_receipt.json"
                ).exists()
            )

    def test_nonempty_output_is_rejected_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            output_dir.mkdir()
            sentinel = output_dir / "keep.txt"
            sentinel.write_text("preserve", encoding="utf-8")
            with self.assertRaisesRegex(ExposedEndToEndSmokeError, "OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY"):
                main(["run-smoke", "--output-dir", str(output_dir)])
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")


if __name__ == "__main__":
    unittest.main()
