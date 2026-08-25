import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import main


ROOT = Path(__file__).parents[1]
FIXTURES = Path(__file__).parent / "fixtures"


class EndToEndTests(unittest.TestCase):
    def test_recorded_provider_vertical_slice_writes_review_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "run"
            code = main(
                [
                    "run-fixture",
                    "--profile-proposal",
                    str(FIXTURES / "case_profile_valid.json"),
                    "--selector-output",
                    str(FIXTURES / "recorded_selector_output.json"),
                    "--resolution-proposal",
                    str(FIXTURES / "subagent_resolution_proposal.json"),
                    "--output-dir",
                    str(output),
                ]
            )
            self.assertEqual(code, 0)
            review = json.loads((output / "review_packet.json").read_text(encoding="utf-8"))
            self.assertEqual(review["review_status"], "HUMAN_REVIEW_REQUIRED")
            self.assertEqual(review["workflow_status"], "EVIDENCE_OBSERVED")
            self.assertEqual(review["proposal_provider_id"], "recorded-codex-subagent")
            profile = json.loads(
                (output / "profile_admission.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                profile["method_profile_registry_id"],
                "dynamics-atlas-method-profiles/v0.1-empty",
            )
            self.assertEqual(
                json.loads(
                    (output / "selector_admission.json").read_text(encoding="utf-8")
                )["status"],
                "ACCEPTED",
            )
            self.assertTrue((output / "operator_run_receipt.json").is_file())
            self.assertTrue((output / "evidence_result.json").is_file())

    def test_mismatched_selector_case_stops_before_provider(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            selector = json.loads(
                (FIXTURES / "recorded_selector_output.json").read_text(encoding="utf-8")
            )
            selector["case_id"] = "different-case"
            selector_path = temp_root / "selector.json"
            selector_path.write_text(json.dumps(selector), encoding="utf-8")
            output = temp_root / "run"
            code = main(
                [
                    "run-fixture",
                    "--profile-proposal",
                    str(FIXTURES / "case_profile_valid.json"),
                    "--selector-output",
                    str(selector_path),
                    "--resolution-proposal",
                    str(FIXTURES / "subagent_resolution_proposal.json"),
                    "--output-dir",
                    str(output),
                ]
            )
            self.assertEqual(code, 0)
            admission = json.loads(
                (output / "selector_admission.json").read_text(encoding="utf-8")
            )
            self.assertEqual(admission["status"], "ABSTAINED")
            self.assertEqual(admission["reason_codes"], ["CASE_ID_MISMATCH"])
            self.assertFalse((output / "operator_run_receipt.json").exists())


if __name__ == "__main__":
    unittest.main()
