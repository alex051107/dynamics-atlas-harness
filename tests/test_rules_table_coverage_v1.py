import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).parents[1]
ARTIFACT_ROOT = REPO_ROOT / "research" / "rules_table_coverage_v1"
ALLOWED_LABELS = {
    "COVERED_EXACT",
    "COVERED_PARTIAL",
    "UNCOVERED_OBLIGATION",
    "OVERTRIGGERED_RULE",
    "WRONG_TARGET_SCOPE",
    "WRONG_DEPENDENCY",
    "WRONG_RESOLUTION_ROUTE",
    "CLAIM_CEILING_TOO_HIGH",
    "CLAIM_CEILING_TOO_LOW",
    "HUMAN_JUDGMENT_ONLY",
    "SOURCE_SPECIFIC_ONLY",
    "DATA_INSUFFICIENT",
}
EXPECTED_LABEL_COUNTS = {
    "COVERED_EXACT": 14,
    "COVERED_PARTIAL": 23,
    "HUMAN_JUDGMENT_ONLY": 2,
    "SOURCE_SPECIFIC_ONLY": 1,
}


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


class RulesTableCoverageV1ArtifactTests(unittest.TestCase):
    def test_frozen_source_first_coverage_artifacts_are_consistent(self):
        manifest = json.loads((ARTIFACT_ROOT / "manifest.json").read_text(encoding="utf-8"))
        repairs = json.loads((ARTIFACT_ROOT / "candidate_repairs.json").read_text(encoding="utf-8"))
        source_path = ARTIFACT_ROOT / "source_first_obligations.jsonl"
        coverage_path = ARTIFACT_ROOT / "rule_coverage_results.jsonl"
        matrix_path = ARTIFACT_ROOT / "coverage_matrix.csv"
        report = (ARTIFACT_ROOT / "REPORT.md").read_text(encoding="utf-8")

        self.assertEqual(manifest["post_merge_main_sha"], "86fc842f36002e57bcd71e6cb3fd90f9fed98d4b")
        self.assertEqual(manifest["post_merge_main_sha"], manifest["pr23_merge"]["merge_commit_sha"])
        self.assertEqual(manifest["pr23_merge"]["reviewed_head_sha"], "099faace269c4675d015a2e6fcc6c625725a55ac")
        self.assertEqual(
            manifest["bounded_review_repair"]["development_status"],
            "RULES_TABLE_PARTIALLY_COVERED_WITH_RECURRING_GAPS",
        )
        self.assertFalse(manifest["bounded_review_repair"]["pass_a_records_mutated"])
        self.assertEqual(manifest["frozen_corpus"]["challenge_unit_count"], 20)
        self.assertEqual(manifest["frozen_corpus"]["source_identity_count"], 15)
        self.assertEqual(manifest["source_hash_audit"]["status"], "PASS")
        self.assertEqual(manifest["source_hash_audit"]["verified_pdf_hashes"], 15)
        self.assertEqual(manifest["source_hash_audit"]["verified_derivative_hashes"], 15)

        source_bytes = source_path.read_bytes()
        self.assertEqual(
            hashlib.sha256(source_bytes).hexdigest(), manifest["pass_a_freeze"]["sha256"]
        )
        self.assertEqual(manifest["pass_a_freeze"]["status"], "FROZEN")
        self.assertTrue(manifest["pass_a_freeze"]["rules_baseline_loaded_after_freeze"])
        self.assertLess(
            manifest["pass_a_freeze"]["frozen_at_utc"],
            manifest["rules_baseline"]["loaded_at_utc"],
        )

        source_lines = [line for line in source_bytes.splitlines() if line]
        source_records = [json.loads(line) for line in source_lines]
        self.assertEqual([row["case_id"] for row in source_records], manifest["frozen_corpus"]["case_order"])
        self.assertEqual(len(source_records), 20)
        self.assertEqual(len({row["paper_id"] for row in source_records}), 15)
        source_record_hashes = manifest["pass_a_freeze"]["case_record_sha256"]
        forbidden_pass_a_tokens = re.compile(
            r"F0[1-7]R\d\d|COVERED_|WRONG_TARGET_SCOPE|WRONG_DEPENDENCY|"
            r"WRONG_RESOLUTION_ROUTE|CLAIM_CEILING_TOO_|candidate_repair|"
            r"applicability_binding|evaluation_contract|resolution_policy",
            re.IGNORECASE,
        )
        for raw_line, record in zip(source_lines, source_records, strict=True):
            self.assertEqual(record["pass"], "A")
            self.assertFalse(record["input_isolation"]["current_baseline_loaded"])
            self.assertFalse(record["input_isolation"]["prior_projection_loaded"])
            self.assertNotRegex(raw_line.decode("utf-8"), forbidden_pass_a_tokens)
            self.assertEqual(
                hashlib.sha256(raw_line).hexdigest(), source_record_hashes[record["case_id"]]
            )
            locator_ids = {locator["id"] for locator in record["exact_source_locators"]}
            self.assertTrue(locator_ids)
            for field in ("source_supported_facts", "relevant_source_objects"):
                for item in record[field]:
                    self.assertEqual(item["label"], "OBSERVED_SOURCE")
                    self.assertTrue(set(item["locator_ids"]).issubset(locator_ids))
                    self.assertTrue(item["locator_ids"])
            for item in record["mandatory_review_obligations"]:
                self.assertEqual(item["label"], "INFERENCE")
                self.assertTrue(set(item["basis_locator_ids"]).issubset(locator_ids))
                self.assertTrue(item["basis_locator_ids"])

        coverage_records = _jsonl(coverage_path)
        self.assertEqual([row["case_id"] for row in coverage_records], manifest["frozen_corpus"]["case_order"])
        self.assertEqual(len(coverage_records), 20)
        with matrix_path.open(encoding="utf-8") as handle:
            matrix_rows = list(csv.DictReader(handle))
        self.assertEqual(len(matrix_rows), 40)
        matrix_by_obligation = {
            (row["case_id"], row["obligation_id"]): row for row in matrix_rows
        }
        self.assertEqual(len(matrix_by_obligation), 40)

        labels = Counter()
        family_counts = Counter()
        candidate_count = 0
        for record in coverage_records:
            self.assertEqual(record["pass"], "B")
            self.assertEqual(record["pass_a_case_sha256"], source_record_hashes[record["case_id"]])
            case_repair_ids = {
                finding["candidate_repair_id"]
                for finding in record["overtrigger_findings"]
                if finding["candidate_repair_id"]
            }
            self.assertLessEqual(len(case_repair_ids), 1)
            for obligation in record["obligations"]:
                self.assertIn(obligation["coverage_label"], ALLOWED_LABELS)
                labels[obligation["coverage_label"]] += 1
                family_counts[obligation["matched_family"]] += 1
                matrix = matrix_by_obligation[(record["case_id"], obligation["obligation_id"])]
                self.assertEqual(matrix["coverage_label"], obligation["coverage_label"])
                self.assertEqual(matrix["matched_rule"], obligation["matched_rule"] or "")
                self.assertEqual(matrix["target_kind"], obligation["target_kind"] or "")
                expected_repair_id = obligation["candidate_repair_id"] or next(
                    iter(case_repair_ids), ""
                )
                self.assertEqual(matrix["candidate_repair_id"], expected_repair_id)
                if obligation["implementation_status"] == "CANDIDATE_MAP_ONLY":
                    candidate_count += 1
                    self.assertNotEqual(obligation["coverage_label"], "COVERED_EXACT")
                    self.assertIn("HUMAN", obligation["resolution_route"])

        self.assertEqual(sum(labels.values()), 40)
        self.assertEqual(dict(labels), EXPECTED_LABEL_COUNTS)
        self.assertEqual(
            dict(family_counts),
            {
                "F01_CLAIM_CONTRACT_AND_CEILING": 3,
                "F02_SYSTEM_CONSTRUCT_AND_CONDITION": 5,
                "F03_SOURCE_MEASUREMENT_SEMANTICS": 7,
                "F04_SOURCE_RELIABILITY_AND_UNCERTAINTY": 6,
                "F05_REPRESENTATION_SUPPORT_AND_FORWARD_BRIDGE": 9,
                "F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE": 6,
                "F07_IDENTIFIABILITY_AND_NEXT_ACTION": 4,
            },
        )
        self.assertEqual(candidate_count, 19)
        self.assertEqual(len(repairs["candidate_repairs"]), 1)
        self.assertFalse(repairs["canonical_mutation"])
        cr_001 = repairs["candidate_repairs"][0]
        self.assertEqual(cr_001["candidate_repair_id"], "CR-001")
        self.assertEqual(cr_001["disposition"], "DEFER")
        self.assertEqual(cr_001["status"], "SOURCE_OWNERSHIP_REVIEW_REQUIRED")
        self.assertEqual(
            cr_001["repair_layer_status"],
            "UNRESOLVED_SOURCE_ADMISSION_TYPING_VS_APPLICABILITY",
        )
        self.assertIn("source.case_evidence_scope == CLAIM_EVIDENCE", json.dumps(cr_001))
        self.assertEqual(len(cr_001["required_source_science_review"]), 3)

        c020 = next(record for record in coverage_records if record["case_id"] == "case_020")
        c020_o02 = next(
            obligation
            for obligation in c020["obligations"]
            if obligation["obligation_id"] == "case_020_o02"
        )
        self.assertEqual(c020_o02["coverage_label"], "HUMAN_JUDGMENT_ONLY")
        self.assertEqual(c020_o02["failure_layer"], "NO_GENERIC_RULE_DEFECT")
        self.assertIn("DEPENDENCY_QUESTION_NOT_YET_ESTABLISHED", c020_o02["dependency_finding"])
        self.assertEqual(c020_o02["resolution_route"], "HUMAN_OR_NEW_DATA")

        for relative_path, expected_hash in manifest["rules_baseline"]["file_hashes"].items():
            self.assertEqual(
                hashlib.sha256((ARTIFACT_ROOT / "frozen_rules_baseline" / relative_path).read_bytes()).hexdigest(), expected_hash
            )
        for forbidden in ("/Users/", "BEGIN PRIVATE KEY", "ghp_"):
            for artifact in ARTIFACT_ROOT.iterdir():
                if artifact.is_file():
                    self.assertNotIn(forbidden, artifact.read_text(encoding="utf-8"))

        for summary_line in (
            "| Challenge units | 20 |",
            "| Source identities | 15 |",
            "| Source-first mandatory obligations | 40 |",
            "| Deferred repair issues requiring layer decision | 1 |",
            "| `COVERED_EXACT` | 14 |",
            "| `COVERED_PARTIAL` | 23 |",
            "| `WRONG_DEPENDENCY` | 0 |",
            "| `HUMAN_JUDGMENT_ONLY` | 2 |",
            "| `SOURCE_SPECIFIC_ONLY` | 1 |",
        ):
            self.assertIn(summary_line, report)
