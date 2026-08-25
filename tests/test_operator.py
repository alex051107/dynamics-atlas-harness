import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.operators import load_operator_registry
from dynamics_atlas_harness.providers import RecordedProposalProvider
from dynamics_atlas_harness.runtime import run_resolution_stage


ROOT = Path(__file__).parents[1]
FIXTURES = Path(__file__).parent / "fixtures"


def load(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def obligation():
    return load("recorded_selector_output.json")["obligations"][0]


class OperatorBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = load_operator_registry(ROOT / "config" / "operators.json")

    def run_proposal(self, proposal):
        return run_resolution_stage(
            obligation(),
            RecordedProposalProvider(proposal),
            self.registry,
            FIXTURES,
            request_id="test-request",
        )

    def test_read_only_fixture_operator_succeeds_and_requires_human_review(self):
        artifacts = self.run_proposal(load("recorded_resolution_proposal.json"))
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "SUCCEEDED")
        self.assertEqual(artifacts["evidence_result"]["status"], "OBSERVED")
        self.assertEqual(
            artifacts["review_packet"]["review_status"], "HUMAN_REVIEW_REQUIRED"
        )
        self.assertNotIn("verdict", artifacts["evidence_result"])

    def test_missing_source_prerequisite_abstains(self):
        proposal = load("recorded_resolution_proposal.json")
        proposal["operator_inputs"]["source_path"] = "missing.json"
        artifacts = self.run_proposal(proposal)
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertIn("SOURCE_PATH_NOT_FOUND", artifacts["operator_run_receipt"]["reason_codes"])

    def test_blocked_mdanalysis_profile_does_not_execute(self):
        proposal = load("recorded_resolution_proposal.json")
        proposal["operator_id"] = "trajectory.structural_state_projection.v1"
        artifacts = self.run_proposal(proposal)
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertIn("OPERATOR_NOT_READY", artifacts["operator_run_receipt"]["reason_codes"])

    def test_unregistered_operator_abstains(self):
        proposal = load("recorded_resolution_proposal.json")
        proposal["operator_id"] = "unknown.operator"
        artifacts = self.run_proposal(proposal)
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertEqual(artifacts["operator_run_receipt"]["reason_codes"], ["UNREGISTERED_OPERATOR"])

    def test_source_path_cannot_escape_allowed_root(self):
        proposal = load("recorded_resolution_proposal.json")
        proposal["operator_inputs"]["source_path"] = "../outside.json"
        artifacts = self.run_proposal(proposal)
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertIn(
            "SOURCE_PATH_OUTSIDE_ALLOWED_ROOT",
            artifacts["operator_run_receipt"]["reason_codes"],
        )

    def test_answer_bearing_source_is_rejected_before_pointer_lookup(self):
        proposal = load("recorded_resolution_proposal.json")
        proposal["operator_inputs"]["source_path"] = "source_with_reference_answer.json"
        proposal["operator_inputs"]["json_pointer"] = "/reference_answer"
        artifacts = self.run_proposal(proposal)
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertIn(
            "ANSWER_BEARING_SOURCE",
            artifacts["operator_run_receipt"]["reason_codes"],
        )

    def test_non_object_provider_output_abstains(self):
        class BadProvider:
            provider_id = "bad-provider"

            def propose(self, bounded_view):
                return None

        artifacts = run_resolution_stage(
            obligation(), BadProvider(), self.registry, FIXTURES, request_id="bad-output"
        )
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertIn(
            "PROVIDER_OUTPUT_NOT_OBJECT",
            artifacts["operator_run_receipt"]["reason_codes"],
        )

    def test_provider_exception_abstains_without_error_text(self):
        class RaisingProvider:
            provider_id = "raising-provider"

            def propose(self, bounded_view):
                raise RuntimeError("sensitive detail")

        artifacts = run_resolution_stage(
            obligation(), RaisingProvider(), self.registry, FIXTURES, request_id="provider-error"
        )
        self.assertEqual(artifacts["operator_run_receipt"]["status"], "ABSTAINED")
        self.assertEqual(
            artifacts["operator_run_receipt"]["reason_codes"],
            ["PROVIDER_ERROR:RuntimeError"],
        )


if __name__ == "__main__":
    unittest.main()
