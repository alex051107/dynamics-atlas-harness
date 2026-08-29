import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.exposed_paper_blind_capsule_v1 import (
    ExposedPaperBlindCapsuleError,
    run_exposed_paper_blind_capsule,
    validate_planner_proposal,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNER_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1" / "agent_runs" / "planner"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ExposedPaperBlindCapsuleV1Tests(unittest.TestCase):
    def test_full_capsule_is_answer_blind_and_fail_closed_for_science(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_exposed_paper_blind_capsule(output_root=Path(tmp) / "run")
            run_root = Path(result["output_root"])
            summary = result["summary"]
            self.assertEqual(summary["unsupported_support_packets"], 0)
            self.assertEqual(summary["scientific_disposition"], "NOT_EVALUATED")
            self.assertFalse(summary["dhfr_accessed"])
            self.assertFalse(summary["external_model_transport"])

            for slug in ("hsp90", "adk"):
                visible = _load(run_root / slug / "agent_visible_input.json")
                self.assertNotIn("platform_authority_envelope", visible)
                self.assertNotIn("hidden_reference_boundary", visible)
                self.assertNotIn("claim_boundary", json.dumps(visible))
                human_packet = _load(run_root / slug / "human_decision_packet.json")
                self.assertEqual(human_packet["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")
                self.assertEqual(human_packet["scientific_disposition"], "NOT_EVALUATED")
                self.assertEqual(human_packet["source_science_review_status"], "PENDING_DOMAIN_REVIEW")

            hsp90_full = _load(run_root / "hsp90" / "arm_c_full_harness.json")
            sampling = hsp90_full["evidence_results"]["sampling_description"]
            self.assertEqual(sampling["row_count"], 40)
            self.assertEqual(
                {item["group_id"]: item["trajectory_count"] for item in sampling["within_group_summaries"]},
                {"R46A_ES": 20, "R60A_GS": 20},
            )
            exact = hsp90_full["evidence_results"]["exact_hsp90_control"]
            self.assertEqual(exact["pre_operator_rule_result"]["status"], "UNRESOLVED")
            self.assertEqual(exact["post_operator_rule_result"]["status"], "PASS")
            self.assertEqual(
                exact["pre_operator_rule_result"]["rule_instance_id"],
                exact["post_operator_rule_result"]["rule_instance_id"],
            )

            adk_full = _load(run_root / "adk" / "arm_c_full_harness.json")
            projection = adk_full["evidence_results"]["reference_relative_projection"]
            self.assertEqual(projection["sample_kind"], "NONREFERENCE_STATIC_COORDINATE_SAMPLE")
            self.assertEqual(projection["rule_effect"], "NO_RULE_RESULT_EMITTED")

    def test_invalid_planner_selection_cannot_authorize_an_action(self):
        planner_input = _load(PLANNER_ROOT / "adk_action_input.json")
        invalid = {
            "case_id": "ADK_EXPOSED_PORTABILITY_V1",
            "selected_card_ids": ["INVENTED_OPERATOR_ROUTE"],
            "rationales": {"INVENTED_OPERATOR_ROUTE": "not legal"},
        }
        with self.assertRaisesRegex(ExposedPaperBlindCapsuleError, "PLANNER_SELECTED_ILLEGAL_CARD"):
            validate_planner_proposal(
                planner_input,
                invalid,
                required_cards=("ADK_NONREFERENCE_REFERENCE_PROJECTION_V1",),
            )


if __name__ == "__main__":
    unittest.main()
