"""Behavioral checks for the bounded static review workspace/workbench."""

from __future__ import annotations

import inspect
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from dynamics_atlas_harness import review_console_v0
from dynamics_atlas_harness.review_console_v0 import (
    POSITIVE_REVIEW_DISPOSITIONS,
    REVIEW_DISPOSITIONS,
    ReviewConsoleError,
    _render_main,
    build_source_science_review_workspace,
    render_review_console,
    validate_source_science_review_form,
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
LIVE_EVIDENCE_ROOT = (
    REPO_ROOT
    / "evidence/live_agent_common_flows_v1/development_runs/"
    "authorized_planner_from_frozen_hsp90_minimax_repair1_20260830/trial-1"
)
RECORDED_EVIDENCE_ROOT = (
    REPO_ROOT
    / "evidence/live_agent_common_flows_v1/development_runs/"
    "authorized_campaign_live_20260830/recorded_replay/hsp90"
)
COMMON_FLOW_MATRIX = (
    REPO_ROOT
    / "evidence/common_flow_scenarios_v1/development_runs/"
    "common_flow_scenarios_v1/common_flow_matrix.json"
)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _complete_identity(item: dict) -> None:
    item.update(
        {
            "reviewer_name": "Named Domain Reviewer",
            "reviewer_role": "Domain scientist",
            "review_date": "2026-08-30",
            "passage_checked": "Primary passage and case-bound artifacts checked.",
            "allowed_scope": "Only the exact recorded reusable question and keyed cases.",
            "claim_ceiling": "No scientific support or runtime activation.",
            "supporting_note": "Disposition is limited to the named evidence and scope.",
        }
    )


class SourceScienceReviewWorkspaceTests(unittest.TestCase):
    def test_workspace_has_nine_blank_matrix_keyed_draft_items_and_canonical_authority(self):
        source_index = _load(WORKSPACE / "source_passage_index.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        form = _load(WORKSPACE / "reviewer_form.json")
        schema = _load(WORKSPACE / "reviewer_form.schema.json")

        self.assertEqual(source_index["workspace_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(matrix["workspace_status"], "PENDING_DOMAIN_REVIEW")
        self.assertEqual(form["review_status"], "DRAFT")
        self.assertEqual(form["allowed_dispositions"], list(REVIEW_DISPOSITIONS))
        self.assertEqual(schema["properties"]["allowed_dispositions"]["const"], list(REVIEW_DISPOSITIONS))
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(form)
        validate_source_science_review_form(form, matrix)
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
        for entry in source_index["entries"]:
            with self.subTest(entry=entry["review_item_id"]):
                self.assertTrue(entry["scientific_question"])
                self.assertTrue(entry["claim_effect_summary"])
                self.assertTrue(entry["implementation_status"])
                self.assertEqual(
                    entry["runtime_subrules_registry_status"],
                    "PROPOSAL_ONLY_NOT_RUNTIME_ACTIVE",
                )
                self.assertEqual(
                    entry["family_overlay_registry_status"],
                    "PROPOSAL_ONLY_NOT_RUNTIME_ACTIVE",
                )
                self.assertEqual(
                    entry["family_overlay"]["source_grounding_decision"],
                    "PENDING_DOMAIN_REVIEW",
                )
                self.assertIn(entry["family_overlay"]["runtime_readiness"], {"NOT_READY", "DEFER"})
                self.assertTrue(entry["passage_kind"])
                self.assertTrue(entry["source_packet_status"])

        form_by_id = {item["review_item_id"]: item for item in form["items"]}
        matrix_by_id = {item["review_item_id"]: item for item in matrix["items"]}
        nullable_fields = {
            "reviewer_name",
            "reviewer_role",
            "review_date",
            "passage_checked",
            "rule_disposition",
            "required_revision",
            "allowed_scope",
            "claim_ceiling",
            "supporting_note",
        }
        for item_id, item in form_by_id.items():
            with self.subTest(item=item_id):
                self.assertTrue(all(item[field] is None for field in nullable_fields))
                self.assertEqual(len(item["case_application_dispositions"]), 2)
                expected_apps = matrix_by_id[item_id]["case_applications"]
                self.assertEqual(
                    {record["case_id"] for record in item["case_application_dispositions"]},
                    {application["case_id"] for application in expected_apps},
                )
                self.assertTrue(
                    all(record["disposition"] is None for record in item["case_application_dispositions"])
                )
                self.assertTrue(
                    all("rule_instance_ids" in record["reviewed_target"] for record in item["case_application_dispositions"])
                )

        f04 = next(entry for entry in source_index["entries"] if entry["review_item_id"] == "NDSR-F04R02")
        self.assertEqual(f04["source_packet_status"], "PENDING_SOURCE_TRACEABILITY_MAPPING")
        self.assertEqual(f04["primary_locator_status"], "CASE_BOUND_TRACEABILITY_MAPPING_PENDING")
        self.assertIn("mapping remains DATA_INSUFFICIENT", f04["traceability_note"])
        self.assertEqual(f04["runtime_subrule_origin"], "CASE_BOUND_OVERLAY_NOT_RUNTIME_SUBRULES_V1_MEMBER")

    def test_builder_reproduces_workspace_from_repository_inputs(self):
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
                self.assertEqual((target / name).read_bytes(), (WORKSPACE / name).read_bytes())

    def test_incomplete_positive_and_completed_draft_are_rejected(self):
        form = _load(WORKSPACE / "reviewer_form.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        schema = _load(WORKSPACE / "reviewer_form.schema.json")

        incomplete = deepcopy(form)
        incomplete["items"][0]["rule_disposition"] = POSITIVE_REVIEW_DISPOSITIONS[0]
        self.assertTrue(list(Draft202012Validator(schema).iter_errors(incomplete)))
        with self.assertRaisesRegex(ReviewConsoleError, "COMPLETED_REVIEW_FIELD_REQUIRED"):
            validate_source_science_review_form(incomplete, matrix)

        completed = deepcopy(form)
        completed["review_status"] = "COMPLETED"
        self.assertTrue(list(Draft202012Validator(schema).iter_errors(completed)))
        with self.assertRaisesRegex(ReviewConsoleError, "COMPLETED_REVIEW_FIELD_REQUIRED"):
            validate_source_science_review_form(completed, matrix)

    def test_f04_positive_disposition_is_blocked_while_traceability_pending(self):
        form = _load(WORKSPACE / "reviewer_form.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        schema = _load(WORKSPACE / "reviewer_form.schema.json")
        f04 = next(item for item in form["items"] if item["review_item_id"] == "NDSR-F04R02")
        _complete_identity(f04)
        f04["rule_disposition"] = "APPROVE_AS_WRITTEN"

        self.assertTrue(list(Draft202012Validator(schema).iter_errors(form)))
        with self.assertRaisesRegex(ReviewConsoleError, "F04_POSITIVE_DISPOSITION_BLOCKED"):
            validate_source_science_review_form(form, matrix)

    def test_bounded_revision_requires_text_in_schema_and_python_validator(self):
        form = _load(WORKSPACE / "reviewer_form.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")
        schema = _load(WORKSPACE / "reviewer_form.schema.json")

        for disposition_scope in ("rule", "case"):
            with self.subTest(disposition_scope=disposition_scope):
                bounded = deepcopy(form)
                item = bounded["items"][0]
                _complete_identity(item)
                if disposition_scope == "rule":
                    item["rule_disposition"] = "APPROVE_WITH_BOUNDED_REVISION"
                else:
                    item["case_application_dispositions"][0][
                        "disposition"
                    ] = "APPROVE_WITH_BOUNDED_REVISION"
                self.assertTrue(list(Draft202012Validator(schema).iter_errors(bounded)))
                with self.assertRaisesRegex(
                    ReviewConsoleError, "BOUNDED_REVISION_TEXT_REQUIRED"
                ):
                    validate_source_science_review_form(bounded, matrix)

                item["required_revision"] = "Use only the exact bounded wording."
                Draft202012Validator(schema).validate(bounded)
                validate_source_science_review_form(bounded, matrix)

    def test_unknown_missing_case_coverage_and_mismatched_rule_ids_are_rejected(self):
        form = _load(WORKSPACE / "reviewer_form.json")
        matrix = _load(WORKSPACE / "case_application_matrix.json")

        missing_case = deepcopy(form)
        missing_case["items"][0]["case_application_dispositions"].pop()
        with self.assertRaisesRegex(ReviewConsoleError, "CASE_DISPOSITION_COVERAGE_MISMATCH"):
            validate_source_science_review_form(missing_case, matrix)

        unknown_item = deepcopy(form)
        unknown = deepcopy(unknown_item["items"][0])
        unknown["review_item_id"] = "UNKNOWN_REVIEW_ITEM"
        unknown_item["items"].append(unknown)
        with self.assertRaisesRegex(ReviewConsoleError, "FORM_REVIEW_ITEM_UNKNOWN"):
            validate_source_science_review_form(unknown_item, matrix)

        mismatched_rule = deepcopy(form)
        mismatched_rule["items"][0]["case_application_dispositions"][0]["reviewed_target"][
            "rule_instance_ids"
        ] = ["MISMATCHED_RULE_INSTANCE"]
        with self.assertRaisesRegex(ReviewConsoleError, "CASE_DISPOSITION_RULE_INSTANCE_MISMATCH"):
            validate_source_science_review_form(mismatched_rule, matrix)


class StaticReviewConsoleTests(unittest.TestCase):
    def test_committed_live_and_recorded_roots_render_as_one_comparison_workbench(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = render_review_console(
                status_path=STATUS,
                case_roots=[RECORDED_EVIDENCE_ROOT, LIVE_EVIDENCE_ROOT],
                capsule_root=CAPSULE_ROOT,
                review_workspace=WORKSPACE,
                scenario_matrix_path=COMMON_FLOW_MATRIX,
                output_dir=Path(temp_dir),
            )
            rendered = output_path.read_text(encoding="utf-8")

        self.assertIn("RECORDED_PROPOSAL_REPLAY", rendered)
        self.assertIn("LIVE_OPENROUTER_PROPOSAL", rendered)
        self.assertIn("LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE", rendered)
        self.assertIn("DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE", rendered)
        self.assertIn("LIVE_AGENT_DECISION_CLOSURE_V1_COMPLETE", rendered)
        self.assertIn("RECORDED_PROFILE_LIVE_PLANNER", rendered)
        self.assertIn(
            "PAIRED_CARD_PRESENT_VERSUS_CARD_REMOVED_COUNTERFACTUAL", rendered
        )
        self.assertIn("minimax/minimax-m2.5", rendered)
        self.assertIn("StreamLake", rendered)
        self.assertIn('"prompt_tokens"', rendered.replace("&quot;", '"'))
        self.assertIn("0.145264010", rendered)
        self.assertIn("AUTHORIZED_EXACTLY_ONE_SELECTED_CARD", rendered)
        self.assertIn("DESCRIPTIVE_ANALYSIS_ONLY", rendered)
        self.assertIn(
            "No broad public-case ACTIVE_RULE_EVIDENCE is recorded. "
            "No active RuleResult update.",
            rendered,
        )
        self.assertIn("NOT_CALCULATED_BY_CASE_RUNNER", rendered)
        self.assertIn("T1_SUPPORT_SYNTHETIC_CONTRACT_BEHAVIOR_ONLY", rendered)
        self.assertIn("NOT_LIVE_AGENT_COMMON_FLOW_COVERAGE", rendered)

    def test_console_renders_common_flow_matrix_with_fresh_run(self):
        from dynamics_atlas_harness.case_runner_v1 import run_case_v1
        from dynamics_atlas_harness.common_flow_scenarios_v1 import (
            run_common_flow_scenario_suite,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            run_root = temp_root / "run-hsp90"
            suite_root = temp_root / "scenario-suite"
            output_dir = temp_root / "workbench"
            run_case_v1(case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1", output_dir=run_root)
            run_common_flow_scenario_suite(output_dir=suite_root)
            output_path = render_review_console(
                status_path=STATUS,
                case_roots=[run_root],
                capsule_root=CAPSULE_ROOT,
                review_workspace=WORKSPACE,
                scenario_matrix_path=suite_root / "common_flow_matrix.json",
                output_dir=output_dir,
            )
            rendered = output_path.read_text(encoding="utf-8")

        self.assertIn("COMMON FLOW SCENARIO MATRIX", rendered)
        self.assertIn("A_DIRECT_EVALUATION_XEISD_A1", rendered)
        self.assertIn("B_NARROW_LOOKUP_XEISD_RANDOM_COMPOSITION", rendered)
        self.assertIn("C_REGISTERED_COMPUTATION_HSP90_EXACT_CONTROL", rendered)
        self.assertIn("D_EXPLICIT_STOP_XEISD_MISSING_COMPOSITION", rendered)
        self.assertIn("SUPPORT_WITHIN_CEILING", rendered)
        self.assertIn("CANNOT_SUPPORT_REQUESTED_CLAIM", rendered)
        self.assertIn("ABSTAIN_OR_HUMAN_REVIEW", rendered)

    def test_console_renders_fresh_hsp90_and_adk_case_runner_roots(self):
        from dynamics_atlas_harness.case_runner_v1 import run_case_v1

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            hsp90_root = temp_root / "run-hsp90"
            adk_root = temp_root / "run-adk"
            output_dir = temp_root / "review-console"
            run_case_v1(
                case_id="HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
                output_dir=hsp90_root,
            )
            run_case_v1(
                case_id="ADK_EXPOSED_PORTABILITY_V1",
                output_dir=adk_root,
            )

            result = _render_main(
                [
                    "--status",
                    str(STATUS),
                    "--case-root",
                    str(hsp90_root),
                    "--case-root",
                    str(adk_root),
                    "--review-workspace",
                    str(WORKSPACE),
                    "--output-dir",
                    str(output_dir),
                ]
            )
            rendered = (output_dir / "index.html").read_text(encoding="utf-8")

        self.assertEqual(result, 0)
        self.assertEqual(rendered.count("CASE_RUNNER_V1_RUN"), 2)
        self.assertIn("HSP90_NTD_EXPOSED_PAPER_BLIND_V1", rendered)
        self.assertIn("ADK_EXPOSED_PORTABILITY_V1", rendered)
        self.assertGreaterEqual(rendered.count("NOT_CALCULATED_BY_CASE_RUNNER"), 2)
        self.assertEqual(rendered.count('<article class="evidence-card">'), 2)
        self.assertEqual(
            rendered.count(
                "No broad public-case ACTIVE_RULE_EVIDENCE is recorded. "
                "No active RuleResult update."
            ),
            2,
        )
        self.assertNotIn("active-evidence-card", rendered)
        self.assertEqual(
            rendered.count(
                '<code>CONCLUSION_PACKET</code><span class="badge badge-unavailable">'
                "UNAVAILABLE</span>"
            ),
            2,
        )

    def test_console_has_four_views_two_cases_unknown_integrity_state_and_evidence_lanes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            output_path = render_review_console(
                status_path=STATUS,
                capsule_root=CAPSULE_ROOT,
                review_workspace=WORKSPACE,
                output_dir=output_dir,
            )
            rendered = output_path.read_text(encoding="utf-8")
            self.assertTrue((output_dir / "reviewer_form.json").is_file())
            self.assertTrue((output_dir / "reviewer_form.schema.json").is_file())
            self.assertEqual(
                (output_dir / "reviewer_form.json").read_bytes(),
                (WORKSPACE / "reviewer_form.json").read_bytes(),
            )

        self.assertEqual(rendered.count("PRIMARY VIEW "), 4)
        self.assertIn("Case Overview", rendered)
        self.assertIn("Source → Rule → Evidence Trace", rendered)
        self.assertIn("Conclusion and Provenance", rendered)
        self.assertIn("Human Review", rendered)
        self.assertIn("HSP90_NTD_EXPOSED_PAPER_BLIND_V1", rendered)
        self.assertIn("ADK_EXPOSED_PORTABILITY_V1", rendered)
        self.assertIn("AGENT_PROPOSAL", rendered)
        self.assertIn("PLATFORM_ADMITTED_FACT", rendered)
        self.assertIn("RULE_RESULT", rendered)
        self.assertIn("DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT", rendered)
        self.assertIn("ACTIVE_RULE_EVIDENCE", rendered)
        self.assertIn("EXISTING_EXACT_CONTROL_REGRESSION", rendered)
        self.assertIn("CONCLUSION_PACKET", rendered)
        self.assertIn("HUMAN_REVIEW", rendered)
        self.assertIn("UNKNOWN / unresolved", rendered)
        self.assertIn("INTEGRITY_ERROR_EXAMPLE", rendered)
        self.assertIn("REQUIRED_ARTIFACT_MISSING", rendered)
        self.assertIn("Passage kind", rendered)
        self.assertIn("Source packet status", rendered)
        self.assertIn("Traceability note", rendered)
        self.assertIn("PENDING_SOURCE_TRACEABILITY_MAPPING", rendered)
        self.assertIn("PROPOSAL_ONLY_NOT_RUNTIME_ACTIVE", rendered)
        self.assertIn("ADVISORY_RECONCILIATION_NOT_OFFICIAL_DISPOSITION", rendered)
        self.assertIn("ADVISORY_COMPLETE_OFFICIAL_DOMAIN_REVIEW_PENDING", rendered)
        self.assertIn("OFFICIAL_REVIEW_TEMPLATE_BLANK", rendered)
        self.assertIn('href="reviewer_form.json"', rendered)
        self.assertIn('href="reviewer_form.schema.json"', rendered)
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
        self.assertNotIn("import requests", source)
        self.assertNotIn("urllib", source)


if __name__ == "__main__":
    unittest.main()
