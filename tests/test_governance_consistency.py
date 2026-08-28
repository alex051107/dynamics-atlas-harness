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
MAIN_AFTER_PR10 = "00faf6f0d2f8916878dd37b57c2018dbfbd45020"


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

        self.assertEqual(status["repository_baseline"]["main_commit"], MAIN_AFTER_PR10)
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
        self.assertEqual(
            status["next_allowed_action"]["action"],
            "NAMED_HUMAN_DOMAIN_SOURCE_SCIENCE_REVIEW_F01_F02_F03_F04_F06",
        )
        self.assertEqual(
            live_agent["observed_result"]["result"],
            "SAFE_BUT_CAPABILITY_REJECTED_NO_TYPED_CONTRACT_PASS",
        )
        self.assertEqual(
            next(stage for stage in status["stages"] if stage["stage"] == "NAMED_SOURCE_SCIENCE_REVIEW")["status"],
            "PENDING_DOMAIN_REVIEW",
        )
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

    def test_pr_template_carries_open_ended_reviewer_context(self) -> None:
        template = (REPO_ROOT / ".github" / "pull_request_template.md").read_text(
            encoding="utf-8"
        )
        for required_text in (
            "## Codex review brief",
            "Original objective:",
            "Why this is the smallest authorized action now:",
            "Actual behavioral change:",
            "Deliberately excluded work:",
            "Known limits and next authorized action:",
            "Open review invitation:",
            "Frozen Plan semantic milestone:",
            "GitHub delivery PR number:",
            "## Advisory review handback",
            "Review request exact head:",
            "Reviewer transport state:",
            "Accepted findings and verification evidence:",
            "Rejected findings and contrary evidence:",
            "Deferred findings and reason:",
            "REVIEW_NOT_DELIVERED",
        ):
            with self.subTest(required_text=required_text):
                self.assertIn(required_text, template)

        document = (REPO_ROOT / "docs" / "CURRENT_EXECUTION_STATUS_ZH.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("GitHub PR 编号只是 delivery ID", document)
        self.assertIn("Frozen Plan 的 `PR 8`", document)
