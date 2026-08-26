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
MAIN_AFTER_NO_AGENT_MILESTONE = "dd189362c4186f256e1ebe3cf2e068cdcbd6f733"


def load_json(relative_path: str) -> dict:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


def work_item(status: dict, role: str) -> dict:
    return next(item for item in status["work_items"] if item["role"] == role)


class GovernanceConsistencyTests(unittest.TestCase):
    def test_current_status_records_merged_baseline_and_authorized_slice(self) -> None:
        status = load_json("governance/current_execution_status.json")
        deviations = [
            json.loads(line)
            for line in (REPO_ROOT / "governance/deviations.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        self.assertEqual(status["repository_baseline"]["main_commit"], MAIN_AFTER_NO_AGENT_MILESTONE)
        self.assertEqual(
            work_item(status, "NO_AGENT_MILESTONE_A")["state"].split("_")[0:2],
            ["MERGED", "PASS"],
        )
        live_agent = work_item(status, "LIVE_AGENT_EXPOSED_CASES_V1")
        self.assertEqual(live_agent["state"], "HUMAN_AUTHORIZED_NOT_STARTED")
        self.assertEqual(live_agent["authorization"], "USER_DECISION_DA-20260826-032")
        self.assertEqual(status["next_allowed_action"]["action"], "CREATE_FEATURE_LIVE_AGENT_EXPOSED_CASES_V1")
        self.assertEqual(
            next(stage for stage in status["stages"] if stage["stage"] == "STAGE2_ADK_HELD_OUT")["status"],
            "NOT_AUTHORIZED",
        )
        authorization = next(
            record
            for record in deviations
            if record.get("decision_id") == "DA-20260826-032"
        )
        self.assertEqual(authorization["status"], "ACTIVE")
        self.assertIn("RULES_EXPANSION", authorization["forbidden"])

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
