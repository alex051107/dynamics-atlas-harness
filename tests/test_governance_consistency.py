"""Focused checks for repository-owned current execution status.

The frozen execution plan remains historical. Current authorization lives in the
machine-readable status overlay and the append-only deviation record.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ENGINEERING_INTEGRATION_BASE_COMMIT = "03ae77efdfaabeaebbf2cf8cae5a490c15241be1"
PR15_REVIEWED_IMPLEMENTATION_HEAD = "1c11b758388abe3e6023cfc714f172c203c15774"
BOUNDED_ENGINEERING_IMPLEMENTATION_BASELINE = "522fe7e2f07a5b08d0b2b73e5aa13bf7c609cdba"


def load_json(relative_path: str) -> dict:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def work_item(status: dict, role: str) -> dict:
    return next(item for item in status["work_items"] if item["role"] == role)


class GovernanceConsistencyTests(unittest.TestCase):
    def test_current_status_records_merged_baseline_and_bounded_slice_result(self) -> None:
        status = load_json("governance/current_execution_status.json")
        deviations = [
            json.loads(line)
            for line in (REPO_ROOT / "governance/deviations.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        baseline = status["repository_baseline"]
        self.assertEqual(
            baseline["bounded_engineering_integration_base_commit"],
            ENGINEERING_INTEGRATION_BASE_COMMIT,
        )
        self.assertEqual(
            baseline["baseline_tag"],
            "bounded-engineering-integration-baseline-v1",
        )
        self.assertIn(
            "not a live assertion about current main, delivery head, merge state, or CI result",
            baseline["baseline_semantics"],
        )
        self.assertEqual(
            baseline["delivery_state_authority"],
            "GITHUB_PR_METADATA_AUTHORITATIVE_FOR_DELIVERY_STATE",
        )
        self.assertEqual(
            work_item(status, "NO_AGENT_MILESTONE_A")["state"].split("_")[0:2],
            ["MERGED", "PASS"],
        )
        live_agent = work_item(status, "LIVE_AGENT_EXPOSED_CASES_V1")
        self.assertEqual(
            live_agent["state"],
            "MERGED_CONTRACT_FAILURE_BASELINE_SAFE_BUT_CAPABILITY_REJECTED",
        )
        self.assertEqual(live_agent["authorization"], "USER_DECISION_DA-20260826-032")
        consolidation = work_item(status, "DELIVERY_CONSOLIDATION_20260829")
        self.assertEqual(consolidation["state"], "PR12_PR13_PR14_MERGED_CLEAN_CI")
        self.assertEqual(
            consolidation["merge_commits"]["PR14"],
            "4028cc4be02465e0e19b5c733aa335b23618c4b5",
        )
        capsule = work_item(status, "EXPOSED_PAPER_BLIND_SCIENTIFIC_DECISION_CAPSULE_V1")
        self.assertEqual(
            capsule["state"],
            "MERGED_DEVELOPMENT_CAUSAL_CAPSULE",
        )
        self.assertEqual(
            capsule["reviewed_implementation_head"],
            PR15_REVIEWED_IMPLEMENTATION_HEAD,
        )
        self.assertEqual(capsule["delivery_pr_number"], 15)
        self.assertEqual(capsule["merge_commit"], ENGINEERING_INTEGRATION_BASE_COMMIT)
        self.assertIn("status_snapshot_as_of", status)
        self.assertEqual(
            status["next_allowed_action"]["action"],
            "LIVE_AGENT_DECISION_CLOSURE_V1_XEISD_EXACT_LOOKUP_OR_EXACT_HSP90_CONTROL_FALLBACK",
        )
        self.assertEqual(
            status["next_allowed_action"]["authorization"],
            "RECORDED_USER_DIRECTION_DA-20260830-056",
        )
        boundary = status["current_delivery_boundary"]
        self.assertEqual(
            boundary["completion_states"],
            [
                "LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE",
                "DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE",
                "LIVE_AGENT_DECISION_CLOSURE_NOT_YET_ESTABLISHED",
            ],
        )
        self.assertEqual(
            boundary["profiler"]["full_annotation_envelope"],
            "FULL_ANNOTATION_ENVELOPE_FAIL",
        )
        self.assertEqual(
            boundary["planner"]["decision_surface"],
            "ONE_LEGAL_CARD_VERSUS_ABSTAIN",
        )
        self.assertEqual(
            boundary["common_flows"]["agent_mode"],
            "NO_AGENT_DETERMINISTIC_SCENARIO",
        )
        self.assertEqual(
            live_agent["observed_result"]["result"],
            "SAFE_BUT_CAPABILITY_REJECTED_NO_TYPED_CONTRACT_PASS",
        )
        self.assertEqual(
            next(stage for stage in status["stages"] if stage["stage"] == "NAMED_SOURCE_SCIENCE_REVIEW")["status"],
            "PENDING_DOMAIN_REVIEW",
        )
        source_review = next(
            stage for stage in status["stages"] if stage["stage"] == "NAMED_SOURCE_SCIENCE_REVIEW"
        )
        self.assertIn("SOURCE_SCIENCE_REVIEW_WORKSPACE_V1_DRAFT", source_review["known_present"])
        self.assertIn(
            "NINE_ITEM_AUTOMATED_ADVISORY_RECONCILIATION",
            source_review["known_present"],
        )
        self.assertIn(
            "FOUR_VIEW_STATIC_READ_ONLY_REVIEW_WORKBENCH_V1_DRAFT",
            source_review["known_present"],
        )
        self.assertIn("F04R02_CASE_BOUND_TRACEABILITY_MAPPING", source_review["known_unresolved"])
        workbench = work_item(status, "AUTONOMOUS_ENGINEERING_WORKBENCH_V1")
        self.assertEqual(workbench["base_commit"], ENGINEERING_INTEGRATION_BASE_COMMIT)
        self.assertEqual(
            workbench["bounded_engineering_integration_baseline"],
            BOUNDED_ENGINEERING_IMPLEMENTATION_BASELINE,
        )
        self.assertEqual(workbench["state"], "BOUNDED_ENGINEERING_INTEGRATION_BASELINE_V1")
        self.assertEqual(
            workbench["observed_result"]["official_source_science_status"],
            "PENDING_DOMAIN_REVIEW",
        )
        self.assertEqual(
            workbench["observed_result"]["broad_same_rule_closure"],
            "BLOCKED_BROAD_CLOSURE",
        )
        self.assertEqual(workbench["observed_result"]["f04_traceability"], "DATA_INSUFFICIENT")
        self.assertFalse(
            workbench["observed_result"]["terminal_scientific_state_calculated_by_runner"]
        )
        self.assertEqual(
            workbench["observed_result"]["runner_terminal_state"],
            "NOT_CALCULATED_BY_CASE_RUNNER",
        )
        self.assertIn(
            "DYNAMIC_PORTABILITY_NOT_EVALUATED",
            workbench["observed_result"]["adk_boundary"],
        )
        self.assertEqual(
            workbench["observed_result"]["delivery_state_authority"],
            "GITHUB_PR_METADATA_AUTHORITATIVE_FOR_DELIVERY_STATE",
        )
        workbench_stage = next(
            stage for stage in status["stages"] if stage["stage"] == "AUTONOMOUS_ENGINEERING_WORKBENCH_V1"
        )
        self.assertEqual(workbench_stage["status"], "BOUNDED_ENGINEERING_INTEGRATION_BASELINE_V1")
        for unresolved in (
            "NAMED_SOURCE_SCIENCE_REVIEW",
            "BROAD_SAME_RULE_CLOSURE",
            "RUNNER_GENERATED_CONCLUSION_PACKET",
            "ADK_DYNAMIC_PORTABILITY",
            "LIVE_AGENT_EXECUTION",
            "HELD_OUT_RESULT",
        ):
            with self.subTest(unresolved=unresolved):
                self.assertIn(unresolved, workbench_stage["known_unresolved"])
        serialized_status = json.dumps(status, sort_keys=True).upper()
        self.assertNotRegex(
            serialized_status,
            r"EXACT_FINAL_HEAD|FINAL_DELIVERY_HEAD|GITHUB_CI_PENDING|CI_PENDING|FINAL_CI_MATRIX",
        )
        self.assertNotIn("FULL_CHAIN", serialized_status)
        self.assertIn("NO_AGENT_DETERMINISTIC_SCENARIO", status["claim_ceiling"])
        self.assertEqual(
            next(stage for stage in status["stages"] if stage["stage"] == "ADK_PORTABILITY")["status"],
            "NOT_AUTHORIZED",
        )
        authorization = next(
            record
            for record in deviations
            if record.get("decision_id") == "DA-20260826-032"
        )
        self.assertEqual(authorization["status"], "ACTIVE")
        self.assertIn("RULES_EXPANSION", authorization["forbidden"])
        sequence_reconciliation = next(
            record
            for record in deviations
            if record.get("deviation_id") == "DA-DEV-20260828-003"
        )
        self.assertEqual(
            sequence_reconciliation["status"],
            "RECORDED_NO_FURTHER_EXPANSION_AUTHORIZED",
        )

    def test_governance_records_are_portable_and_document_links_resolve(self) -> None:
        repository_records = (
            "governance/current_execution_status.json",
            "governance/frozen_execution_plan_v1_0.json",
            "governance/deviations.jsonl",
        )
        for relative_path in repository_records:
            contents = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            self.assertNotRegex(contents, r"(?:/Users/|/private/|file://)")

        document_path = REPO_ROOT / "docs/CURRENT_EXECUTION_STATUS_ZH.md"
        document = document_path.read_text(encoding="utf-8")
        self.assertNotIn("../../autoresearch", document)
        self.assertNotRegex(document, r"(?:/Users/|/private/|file://)")

        for target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", document):
            if re.match(r"[a-z][a-z0-9+.-]*://", target, re.IGNORECASE):
                continue
            self.assertTrue(
                (document_path.parent / target).resolve().is_file(),
                f"broken repository-relative link: {target}",
            )

    def test_pr_template_keeps_minimal_open_ended_reviewer_context(self) -> None:
        template = (REPO_ROOT / ".github" / "pull_request_template.md").read_text(
            encoding="utf-8"
        )
        for required_text in (
            "## Review context",
            "Original objective and why now:",
            "Actual behavioral change:",
            "Focused validation:",
            "Deliberately excluded work:",
            "Open review invitation:",
            "Frozen Plan semantic milestone:",
            "GitHub delivery PR number:",
        ):
            with self.subTest(required_text=required_text):
                self.assertIn(required_text, template)
        self.assertNotIn("Advisory review handback", template)

        document = (REPO_ROOT / "docs" / "CURRENT_EXECUTION_STATUS_ZH.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("GitHub PR 编号只是 delivery ID", document)
        self.assertIn("Frozen Plan 的 `PR 8`", document)
        self.assertIn("只有具名 human/domain review 或具名 project-owner", document)
        self.assertIn("development/runtime baseline commit", document)
        self.assertIn("literal `main`", document)
        self.assertIn("engineering workbench v1", document)
        self.assertIn("recorded-replay evidence execution and inspection path", document)
        self.assertIn("GITHUB_PR_METADATA_AUTHORITATIVE_FOR_DELIVERY_STATE", document)
        self.assertIn("internal adversarial subagent review passes", document)

        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Current execution status", readme)
        self.assertIn("docs/CURRENT_EXECUTION_STATUS_ZH.md", readme)
        self.assertIn("Historical initial control-plane smoke v0.2", readme)
        self.assertIn("recorded-replay evidence execution and inspection path", readme)
        self.assertIn("GitHub PR merge-ref CI", readme)

        completion = (REPO_ROOT / "docs" / "ENGINEERING_V1_COMPLETION.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "## Implemented recorded-replay evidence execution and inspection path",
            completion,
        )
        self.assertIn("Decision: `BOUNDED_ENGINEERING_WORKBENCH_V1_COMPLETE`", completion)
        self.assertIn("--case-root /tmp/dynamics-atlas-hsp90-engineering-v1", completion)
        self.assertIn("--case-root /tmp/dynamics-atlas-adk-engineering-v1", completion)
        self.assertIn("internal adversarial subagent review passes", completion)
        self.assertIn(
            "GitHub PR checks validate a PR merge ref, not a direct checkout",
            completion,
        )
        self.assertNotIn("## Implemented end-to-end path", completion)
        self.assertNotIn("Final delivery head:", completion)
        self.assertIn("--case-root /tmp/dynamics-atlas-hsp90-engineering-v1", readme)
        self.assertIn("--case-root /tmp/dynamics-atlas-adk-engineering-v1", readme)

        baseline = (REPO_ROOT / "BASELINE.md").read_text(encoding="utf-8")
        self.assertIn("Historical initial baseline", baseline)
        self.assertIn("docs/CURRENT_EXECUTION_STATUS_ZH.md", baseline)
