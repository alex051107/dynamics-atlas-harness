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
PR15_MERGED_DEVELOPMENT_CAUSAL_CAPSULE_COMMIT = "03ae77efdfaabeaebbf2cf8cae5a490c15241be1"
PR15_REVIEWED_IMPLEMENTATION_HEAD = "1c11b758388abe3e6023cfc714f172c203c15774"


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
            baseline["main_commit"],
            PR15_MERGED_DEVELOPMENT_CAUSAL_CAPSULE_COMMIT,
        )
        self.assertEqual(
            baseline["baseline_tag"],
            "post-pr15-merged-development-causal-capsule",
        )
        self.assertIn(
            "Verified literal GitHub main through merged PR #15",
            baseline["main_commit_semantics"],
        )
        self.assertIn(
            "Delivery A source-science workspace and static Review Console are an unmerged Draft surface",
            baseline["main_commit_semantics"],
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
        self.assertEqual(capsule["merge_commit"], PR15_MERGED_DEVELOPMENT_CAUSAL_CAPSULE_COMMIT)
        self.assertIn("status_snapshot_as_of", status)
        self.assertEqual(
            status["next_allowed_action"]["action"],
            "NAMED_HUMAN_DOMAIN_SOURCE_SCIENCE_REVIEW_F01_F02_F03_F04_F06",
        )
        self.assertEqual(
            status["next_allowed_action"]["authorization"],
            "RECORDED_USER_DIRECTION_DA-20260830-052",
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
        self.assertIn("STATIC_READ_ONLY_REVIEW_CONSOLE_V0_DRAFT", source_review["known_present"])
        self.assertIn("F04R02_CASE_BOUND_TRACEABILITY_MAPPING", source_review["known_unresolved"])
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
        self.assertIn("literal current `main` HEAD", document)

        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Current execution status", readme)
        self.assertIn("docs/CURRENT_EXECUTION_STATUS_ZH.md", readme)
        self.assertIn("Historical initial control-plane smoke v0.2", readme)

        baseline = (REPO_ROOT / "BASELINE.md").read_text(encoding="utf-8")
        self.assertIn("Historical initial baseline", baseline)
        self.assertIn("docs/CURRENT_EXECUTION_STATUS_ZH.md", baseline)
