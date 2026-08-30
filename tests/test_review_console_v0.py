"""Behavioral checks for the bounded, static Delivery A review surface."""

from __future__ import annotations

import inspect
import json
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness import review_console_v0
from dynamics_atlas_harness.review_console_v0 import (
    REVIEW_DISPOSITIONS,
    build_source_science_review_workspace,
    render_review_console,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CAPSULE_ROOT = (
    REPO_ROOT
    / "evidence"
    / "paper_blind_exposed_v1"
    / "development_runs"
    / "exposed_paper_blind_scientific_decision_capsule_v1"
)
WORKSPACE = REPO_ROOT / "review" / "source_science_v1"
STATUS = REPO_ROOT / "governance" / "current_execution_status.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class SourceScienceReviewWorkspaceTests(unittest.TestCase):
    def test_workspace_covers_pending_scope_with_blank_named_reviewer_fields(self):
        source_index = _load(WORKSPACE / "source_passage_index.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        form = _load(WORKSPACE / "reviewer_form.json")
        schema = _load(WORKSPACE / "reviewer_form.schema.json")

        self.assertEqual(source_index["workspace_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(matrix["workspace_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(form["review_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(form["allowed_dispositions"], list(REVIEW_DISPOSITIONS))
        self.assertEqual(schema["properties"]["allowed_dispositions"]["const"], list(REVIEW_DISPOSITIONS))
        self.assertEqual(len(source_index["entries"]), 9)
        self.assertEqual(len(matrix["items"]), 9)
        self.assertEqual(len(form["items"]), 9)

        expected_families = {
            "F01_CLAIM_CONTRACT_AND_CEILING",
            "F02_SYSTEM_CONSTRUCT_AND_CONDITION",
            "F03_SOURCE_MEASUREMENT_SEMANTICS",
            "F04_SOURCE_RELIABILITY_AND_UNCERTAINTY",
            "F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE",
        }
        self.assertEqual({entry["family_id"] for entry in source_index["entries"]}, expected_families)
        reviewer_fields = {
            "reviewer_name",
            "reviewer_role",
            "review_date",
            "passage_checked",
            "rule_disposition",
            "case_application_disposition",
            "required_revision",
            "claim_ceiling",
            "notes",
        }
        for item in form["items"]:
            with self.subTest(item=item["review_item_id"]):
                self.assertEqual(set(item) - {"review_item_id"}, reviewer_fields)
                self.assertTrue(all(item[field] is None for field in reviewer_fields))

    def test_every_review_item_keeps_locator_contract_and_case_application_explicit(self):
        source_index = _load(WORKSPACE / "source_passage_index.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        entries_by_id = {entry["review_item_id"]: entry for entry in source_index["entries"]}

        for item in matrix["items"]:
            with self.subTest(item=item["review_item_id"]):
                entry = entries_by_id[item["review_item_id"]]
                self.assertTrue(entry["primary_source_locator"])
                self.assertTrue(entry["atomic_scientific_statement"])
                self.assertTrue(entry["proposed_reusable_review_question"])
                self.assertTrue(entry["forbidden_generalization"])
                predicate = item["exact_applicability_predicate"]
                self.assertTrue(predicate["binding_id"])
                self.assertIn("op", predicate["predicate"])
                self.assertTrue(item["required_evidence"])
                self.assertTrue(item["resolution_policy"]["resolution_policy_id"])
                self.assertTrue(item["evaluation_contract"]["evaluation_contract_id"])
                self.assertEqual(item["current_status"], "PENDING_DOMAIN_REVIEW")
                self.assertEqual(len(item["case_applications"]), 2)

        f04 = entries_by_id["NDSR-F04R02"]
        self.assertEqual(f04["primary_locator_status"], "CASE_BOUND_TRACEABILITY_MAPPING_PENDING")
        f04_matrix = next(item for item in matrix["items"] if item["review_item_id"] == "NDSR-F04R02")
        self.assertTrue(
            any(
                application["application_status"] == "SEPARATE_EXACT_CONTROL_REGRESSION_ONLY"
                and application["public_case_rule_effect"] == "NO_ACTIVE_RULE_EFFECT"
                for application in f04_matrix["case_applications"]
            )
        )

    def test_builder_reproduces_the_bounded_workspace_from_repository_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "source_science_v1"
            result = build_source_science_review_workspace(output_dir=target, capsule_root=CAPSULE_ROOT)
            self.assertEqual(result["status"], "PENDING_DOMAIN_REVIEW")
            self.assertEqual(result["review_item_count"], 9)
            self.assertEqual(result["case_count"], 2)
            for name in (
                "README.md",
                "reviewer_form.json",
                "reviewer_form.schema.json",
                "source_passage_index.json",
                "case_application_matrix.json",
            ):
                self.assertTrue((target / name).is_file(), name)
            self.assertEqual(
                _load(target / "source_passage_index.json"),
                _load(WORKSPACE / "source_passage_index.json"),
            )


class StaticReviewConsoleTests(unittest.TestCase):
    def test_console_renders_two_cases_and_preserves_evidence_lanes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = render_review_console(
                status_path=STATUS,
                capsule_root=CAPSULE_ROOT,
                review_workspace=WORKSPACE,
                output_dir=Path(temp_dir),
            )
            rendered = output_path.read_text(encoding="utf-8")

        self.assertIn("HSP90_NTD_EXPOSED_PAPER_BLIND_V1", rendered)
        self.assertIn("ADK_EXPOSED_PORTABILITY_V1", rendered)
        self.assertIn("DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT", rendered)
        self.assertIn("ACTIVE_RULE_EVIDENCE", rendered)
        self.assertIn("EXISTING_EXACT_CONTROL_REGRESSION", rendered)
        self.assertIn("No broad public-case active-Rule evidence is recorded", rendered)
        self.assertIn("No active RuleResult update.", rendered)
        self.assertIn("UNKNOWN / unresolved", rendered)
        self.assertIn("PENDING_DOMAIN_REVIEW", rendered)
        self.assertIn("https://www.rcsb.org/structure/1E4V", rendered)
        self.assertIn('href="https://www.rcsb.org/structure/1E4V"', rendered)

    def test_console_is_static_read_only_and_status_consistent(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = render_review_console(
                status_path=STATUS,
                capsule_root=CAPSULE_ROOT,
                review_workspace=WORKSPACE,
                output_dir=Path(temp_dir),
            )
            rendered = output_path.read_text(encoding="utf-8").lower()
        status = _load(STATUS)
        source = inspect.getsource(review_console_v0).lower()

        self.assertIn(status["next_allowed_action"]["action"].lower(), rendered)
        self.assertNotIn("<form", rendered)
        self.assertNotIn("<script", rendered)
        self.assertNotIn("fetch(", rendered)
        self.assertNotIn("api key", rendered)
        self.assertNotIn("subprocess", source)
        self.assertNotIn("sqlite", source)
        self.assertNotIn("requests", source)
        self.assertNotIn("urllib", source)
