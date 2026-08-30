import hashlib
import json
import unittest

from dynamics_atlas_harness.proposal_provenance_v1 import (
    CALLER_SUPPLIED_IN_MEMORY,
    RECORDED_PROPOSAL_REPLAY,
    ProposalProvenanceV1Error,
    build_proposal_provenance_v1,
)


def _expected_hash(value):
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class ProposalProvenanceV1Tests(unittest.TestCase):
    def test_recorded_receipt_hashes_json_and_marks_unavailable_metadata(self):
        visible_input = {"z": [3, 2, 1], "case_id": "CASE::ONE"}
        proposal = {"case_id": "CASE::ONE", "decision": "ABSTAIN_NO_ACTION"}
        evaluation = {
            "schema_version": "proposal-admission/v1",
            "proposal_status": "ADMISSIBLE_NONAUTHORITATIVE",
        }
        receipt = build_proposal_provenance_v1(
            role="PROFILER",
            mode=RECORDED_PROPOSAL_REPLAY,
            visible_input=visible_input,
            parsed_proposal=proposal,
            contract_evaluator="validate_test_proposal",
            contract_admission_evaluation=evaluation,
            source_path="evidence/recorded/proposal.json",
        )

        self.assertEqual(receipt["source_path"], "evidence/recorded/proposal.json")
        self.assertEqual(
            receipt["visible_input"]["canonical_sha256"], _expected_hash(visible_input)
        )
        self.assertEqual(
            receipt["parsed_proposal"]["canonical_sha256"], _expected_hash(proposal)
        )
        self.assertEqual(
            receipt["contract_admission_evaluation"]["canonical_sha256"],
            _expected_hash(evaluation),
        )
        self.assertEqual(
            receipt["contract_admission_evaluation"]["status"],
            "ADMISSIBLE_NONAUTHORITATIVE",
        )
        for metadata in ("provider", "model", "prompt", "raw_response"):
            self.assertEqual(receipt[metadata]["status"], "UNAVAILABLE_NOT_RECORDED")
        self.assertIsNone(receipt["recorded_timestamp"])
        self.assertIsNone(receipt["reported_cost"])
        self.assertEqual(
            receipt["answer_blindness_status"],
            "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED",
        )
        self.assertNotIn("/Users/", json.dumps(receipt, sort_keys=True))

    def test_caller_supplied_receipt_has_no_source_path(self):
        receipt = build_proposal_provenance_v1(
            role="PLANNER",
            mode=CALLER_SUPPLIED_IN_MEMORY,
            visible_input={"case_id": "CASE::ONE"},
            parsed_proposal={"case_id": "CASE::ONE"},
            contract_evaluator="validate_test_proposal",
            contract_admission_evaluation={"status": "ADMITTED"},
            source_path=None,
        )
        self.assertIsNone(receipt["source_path"])
        self.assertEqual(
            receipt["provider"]["status"],
            "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY",
        )

    def test_absolute_or_in_memory_source_path_is_rejected(self):
        common = {
            "role": "PROFILER",
            "visible_input": {"case_id": "CASE::ONE"},
            "parsed_proposal": {"case_id": "CASE::ONE"},
            "contract_evaluator": "validate_test_proposal",
            "contract_admission_evaluation": {"status": "ADMITTED"},
        }
        with self.assertRaisesRegex(
            ProposalProvenanceV1Error,
            "PROPOSAL_SOURCE_PATH_MUST_BE_REPOSITORY_RELATIVE",
        ):
            build_proposal_provenance_v1(
                **common,
                mode=RECORDED_PROPOSAL_REPLAY,
                source_path="/Users/example/proposal.json",
            )
        with self.assertRaisesRegex(
            ProposalProvenanceV1Error,
            "IN_MEMORY_PROPOSAL_MUST_NOT_HAVE_SOURCE_PATH",
        ):
            build_proposal_provenance_v1(
                **common,
                mode=CALLER_SUPPLIED_IN_MEMORY,
                source_path="proposal.json",
            )


if __name__ == "__main__":
    unittest.main()
