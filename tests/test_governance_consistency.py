"""Focused checks for the post-PR0 governance handoff.

These tests deliberately validate repository-owned facts only. Live GitHub state is
verified separately immediately before merge.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_AFTER_PR0 = "c9d115b937ece52eba4c42613dc5877839348851"


def load_json(relative_path: str) -> dict:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def work_item(status: dict, role: str) -> dict:
    return next(item for item in status["work_items"] if item["role"] == role)


class GovernanceConsistencyTests(unittest.TestCase):
    def test_post_pr0_handoff_is_explicit(self) -> None:
        status = load_json("governance/current_execution_status.json")
        plan = load_json("governance/frozen_execution_plan_v1_0.json")

        self.assertEqual(status["repository_baseline"]["main_commit"], MAIN_AFTER_PR0)
        self.assertEqual(
            work_item(status, "ISOLATED_FROZEN_PLAN_PR0")["state"],
            "MERGED_MAIN_READBACK_PASS",
        )
        self.assertEqual(
            work_item(status, "FROZEN_PLAN_GOVERNANCE")["state"],
            "SYNCHRONIZED_TO_MERGED_PR0_MAIN_PENDING_FOCUSED_CONSISTENCY_TEST_AND_PUSH",
        )
        self.assertEqual(
            status["next_allowed_action"]["action"],
            "COMPLETE_GATE0B_GOVERNANCE_SYNC_AND_MERGE",
        )
        self.assertEqual(
            status["next_allowed_action"]["merge_authority"],
            "USER_DECISION_DA-20260825-025",
        )
        self.assertEqual(
            next(
                stage for stage in status["stages"] if stage["stage"] == "PR1_RULES_PROTOTYPE_V1"
            )["status"],
            "FIRST_DRAFT_AUTHORIZED_AFTER_GOVERNANCE_MERGE",
        )
        self.assertEqual(
            plan["current_authorization"]["next_allowed_action"],
            "COMPLETE_GATE0B_GOVERNANCE_SYNC_AND_MERGE",
        )
        self.assertIn(
            "CREATE_REVISED_PR1_FIRST_DRAFT_AFTER_GOVERNANCE_MERGE",
            plan["current_authorization"]["allowed_actions"],
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
