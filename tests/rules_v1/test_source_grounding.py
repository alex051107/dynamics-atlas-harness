import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parents[2]
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
EVIDENCE_PATH = REPO_ROOT / "evidence" / "rules_v1" / "source_evidence_packets_v1.jsonl"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


class SourceGroundingTests(unittest.TestCase):
    def test_all_active_subrules_have_review_bounded_derivative_packets(self):
        subrules = read_json(RULES_ROOT / "runtime_subrules_v1.json")["runtime_subrules"]
        packets = read_jsonl(EVIDENCE_PATH)
        packet_by_id = {packet["evidence_packet_id"]: packet for packet in packets}

        self.assertEqual(len(packets), len(packet_by_id))
        active = [
            subrule
            for subrule in subrules
            if subrule["implementation_status"] == "COMPLETE_DRAFT"
        ]
        self.assertEqual(len(active), 8)
        locator_reviewed_packet_ids = {
            "SEP-F01-CLAIM-CONTRACT",
            "SEP-F02-CONSTRUCT",
            "SEP-F02-CONDITION",
            "SEP-F03-MEASUREMENT",
        }
        for subrule in active:
            with self.subTest(subrule=subrule["runtime_subrule_id"]):
                self.assertTrue(subrule["required_evidence_packet_ids"])
                for packet_id in subrule["required_evidence_packet_ids"]:
                    packet = packet_by_id[packet_id]
                    expected_status = (
                        "LOCATOR_REVIEWED_FOR_PROPOSED_CONTROL_LOGIC"
                        if packet_id in locator_reviewed_packet_ids
                        else "PENDING"
                    )
                    self.assertEqual(packet["human_review_status"], expected_status)
                    if packet_id in locator_reviewed_packet_ids:
                        self.assertIn("review_disposition_scope", packet)
                        self.assertIn("only", packet["review_disposition_scope"].lower())
                    self.assertEqual(
                        packet["derivative_kind"],
                        "UPSTREAM_REVIEW_DERIVATIVE_NOT_PRIMARY_VERBATIM",
                    )
                    self.assertTrue(packet["source_locator"])
                    self.assertTrue(packet["atomic_paper_statement"])
                    self.assertTrue(packet["forbidden_generalization"])

    def test_runtime_registry_references_packets_without_copying_source_passages(self):
        registry_text = (RULES_ROOT / "runtime_subrules_v1.json").read_text(encoding="utf-8")
        self.assertNotIn("short_passage", registry_text)
        self.assertNotIn("atomic_paper_statement", registry_text)
        self.assertNotIn("proposed_reusable_use", registry_text)

    def test_source_packet_schema_declares_the_review_boundary(self):
        schema = read_json(
            REPO_ROOT / "schemas" / "rules_v1" / "source_evidence_packet.schema.json"
        )
        required = set(schema["required"])
        self.assertTrue(
            {
                "source_locator",
                "short_passage",
                "atomic_paper_statement",
                "proposed_reusable_use",
                "forbidden_generalization",
                "human_review_status",
            }.issubset(required)
        )
        self.assertEqual(
            schema["properties"]["human_review_status"]["enum"],
            ["PENDING", "LOCATOR_REVIEWED_FOR_PROPOSED_CONTROL_LOGIC"],
        )


if __name__ == "__main__":
    unittest.main()
