import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parents[2]
ADVISORY_PATH = (
    REPO_ROOT
    / "evidence"
    / "source_science_advisory_v1"
    / "advisory_reconciliation.json"
)
RUNTIME_SUBRULES_PATH = REPO_ROOT / "registries" / "rules_v1" / "runtime_subrules_v1.json"
F04_OVERLAY_PATH = (
    REPO_ROOT
    / "evidence"
    / "real_case_vertical_slice_v1"
    / "hsp90_f04r02_rule_overlay_v1.json"
)


class SourceScienceAdvisoryV1Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(ADVISORY_PATH.read_text(encoding="utf-8"))

    def test_all_nine_h1_items_are_advisory_only_and_reviewer_ready(self):
        expected_ids = {
            "NDSR-F01R01",
            "NDSR-F01R02",
            "NDSR-F02R01",
            "NDSR-F02R02",
            "NDSR-F03R01",
            "NDSR-F04R02",
            "NDSR-F06R01",
            "NDSR-F06R02",
            "NDSR-F06R03",
        }
        records = self.packet["records"]
        self.assertEqual({record["review_item_id"] for record in records}, expected_ids)
        self.assertEqual(len(records), 9)
        self.assertEqual(
            self.packet["official_review"],
            {
                "reviewer_identity": None,
                "reviewer_role": None,
                "review_date": None,
                "official_disposition": None,
                "official_note": None,
            },
        )
        allowed = set(self.packet["allowed_advisory_dispositions"])
        self.assertEqual(
            allowed,
            {
                "ADVISORY_APPROVE_AS_WRITTEN",
                "ADVISORY_APPROVE_WITH_BOUNDED_REVISION",
                "ADVISORY_REJECT_OR_DEFER",
                "DATA_INSUFFICIENT",
            },
        )
        for record in records:
            with self.subTest(review_item_id=record["review_item_id"]):
                self.assertTrue(record["exact_source_locator_checked"])
                self.assertTrue(record["atomic_source_supported_statement"])
                self.assertEqual(
                    record["current_repository_interpretation"]["classification"],
                    "PROJECT_INTERPRETATION",
                )
                self.assertEqual(set(record["hsp90_adk_application"]), {"ADK", "HSP90"})
                self.assertIn(
                    record["reconciliation"]["result"],
                    {"AGREEMENT", "MISMATCH", "DATA_INSUFFICIENT"},
                )
                self.assertIn(record["advisory_disposition"], allowed)
                self.assertTrue(record["smallest_bounded_repair"]["repair"])
                self.assertTrue(record["unresolved_human_question"])
                self.assertEqual(record["authoritative_effect"], "NONE")

    def test_advisory_uses_canonical_subrules_and_repository_safe_locators(self):
        runtime = json.loads(RUNTIME_SUBRULES_PATH.read_text(encoding="utf-8"))
        canonical_ids = {
            item["runtime_subrule_id"] for item in runtime["runtime_subrules"]
        }
        f04_overlay = json.loads(F04_OVERLAY_PATH.read_text(encoding="utf-8"))
        canonical_ids.add(f04_overlay["runtime_subrule"]["runtime_subrule_id"])
        serialized = json.dumps(self.packet, sort_keys=True)
        self.assertNotIn("/Users/", serialized)
        self.assertNotIn("/home/", serialized)
        for record in self.packet["records"]:
            self.assertIn(record["runtime_subrule_id"], canonical_ids)

        f04 = next(
            record
            for record in self.packet["records"]
            if record["review_item_id"] == "NDSR-F04R02"
        )
        self.assertEqual(f04["reconciliation"]["result"], "DATA_INSUFFICIENT")
        self.assertEqual(f04["advisory_disposition"], "DATA_INSUFFICIENT")
        self.assertEqual(f04["smallest_bounded_repair"]["status"], "BLOCKED_HUMAN")
        self.assertEqual(
            self.packet["global_result"]["official_source_science_status"],
            "PENDING_DOMAIN_REVIEW",
        )
        self.assertEqual(
            self.packet["global_result"]["broad_same_rule_closure"],
            "BLOCKED_BROAD_CLOSURE",
        )


if __name__ == "__main__":
    unittest.main()
