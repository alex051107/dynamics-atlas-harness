"""Behavioral checks for the artifact-only CaseView read model."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.case_view_v1 import (
    CaseViewIntegrityError,
    build_case_view,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CAPSULE_ROOT = (
    REPO_ROOT
    / "evidence"
    / "paper_blind_exposed_v1"
    / "development_runs"
    / "exposed_paper_blind_scientific_decision_capsule_v1"
)


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _all_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _all_strings(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _all_strings(item)


class RecordedCapsuleCaseViewTests(unittest.TestCase):
    def test_hsp90_and_adk_project_without_collapsing_evidence_lanes_or_unknown(self):
        hsp90 = build_case_view(CAPSULE_ROOT / "hsp90")
        adk = build_case_view(CAPSULE_ROOT / "adk")

        self.assertEqual(hsp90.case_id, "HSP90_NTD_EXPOSED_PAPER_BLIND_V1")
        self.assertEqual(adk.case_id, "ADK_EXPOSED_PORTABILITY_V1")
        self.assertEqual(hsp90.integrity_status, "PASS")
        self.assertEqual(adk.integrity_status, "PASS")
        self.assertTrue(hsp90.descriptive_evidence_no_active_rule_effect)
        self.assertTrue(adk.descriptive_evidence_no_active_rule_effect)
        self.assertEqual(hsp90.active_rule_evidence, [])
        self.assertEqual(adk.active_rule_evidence, [])
        self.assertEqual(
            hsp90.exact_control_regression["exact_control_rule_effect"],
            "ACTIVE_RULE_EFFECT",
        )
        self.assertEqual(adk.exact_control_regression["availability"], "UNAVAILABLE")
        self.assertEqual(hsp90.conclusion_packet["kind"], "CONCLUSION_PACKET")
        self.assertIn("UNKNOWN", set(_all_strings(hsp90.to_dict())))

    def _copied_hsp90(self, temp_dir: str) -> Path:
        target = Path(temp_dir) / "hsp90"
        shutil.copytree(CAPSULE_ROOT / "hsp90", target)
        return target

    def test_required_missing_and_malformed_artifacts_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = self._copied_hsp90(temp_dir)
            (missing / "planner_visible_input.json").unlink()
            with self.assertRaisesRegex(CaseViewIntegrityError, "REQUIRED_ARTIFACT_MISSING"):
                build_case_view(missing)

        with tempfile.TemporaryDirectory() as temp_dir:
            malformed = self._copied_hsp90(temp_dir)
            (malformed / "planner_visible_input.json").write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(CaseViewIntegrityError, "ARTIFACT_MALFORMED"):
                build_case_view(malformed)

    def test_cross_case_receipt_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = self._copied_hsp90(temp_dir)
            receipt_path = target / "asset_identity_verification.json"
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["case_id"] = "ADK_EXPOSED_PORTABILITY_V1"
            _write_json(receipt_path, receipt)
            with self.assertRaisesRegex(CaseViewIntegrityError, "CROSS_CASE_ARTIFACT"):
                build_case_view(target)

    def test_stale_proposal_reference_hash_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = self._copied_hsp90(temp_dir)
            receipt_path = target / "planner_proposal_provenance.json"
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["recorded_proposal_sha256"] = "0" * 64
            _write_json(receipt_path, receipt)
            with self.assertRaisesRegex(CaseViewIntegrityError, "STALE_ARTIFACT_REFERENCE_HASH"):
                build_case_view(target)


class CaseRunnerArtifactViewTests(unittest.TestCase):
    def _build_run_root(self, root: Path) -> Path:
        case_id = "SYNTHETIC_EXPOSED_DEVELOPMENT_CASE"
        rule = {
            "rule_instance_id": "F02R01::SOURCE::SYNTH_SOURCE",
            "runtime_subrule_id": "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
            "status": "UNKNOWN",
            "reason_codes": ["SOURCE_CONTEXT_UNKNOWN"],
            "target": {"kind": "SOURCE", "id": "SYNTH_SOURCE"},
        }
        evidence = {
            "case_id": case_id,
            "card_id": "SYNTH_DESCRIPTIVE_CARD",
            "action_kind": "DESCRIPTIVE_ANALYSIS_ONLY",
            "rule_effect": "NO_ACTIVE_RULE_EFFECT",
            "active_rule_effect": None,
            "affected_rule_instance_id": None,
            "descriptive_result": {
                "rule_effect": "NO_ACTIVE_RULE_EFFECT",
                "capability_kind": "SYNTHETIC_DESCRIPTION",
                "claim_ceiling": "Fixture-only descriptive output.",
            },
        }
        fresh = {
            "admission": {
                "proposal": {"case_id": case_id, "proposed_case_facts": {"unknown": "UNKNOWN"}},
                "proposal_status": "ADMISSIBLE_NONAUTHORITATIVE",
            },
            "projected_casegraph": {"case": {"case_id": case_id}},
            "rule_results": [rule],
            "development_obligations": [{"ref": rule["rule_instance_id"], "status": "UNKNOWN"}],
            "asset_verification": {},
        }
        planner_input = {
            "case_id": case_id,
            "legal_action_cards": [
                {"case_id": case_id, "card_id": "SYNTH_DESCRIPTIVE_CARD"}
            ],
            "unresolved_items": [{"ref": rule["rule_instance_id"], "status": "UNKNOWN"}],
        }
        planner_admission = {
            "case_id": case_id,
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
        }
        authorization = {
            "case_id": case_id,
            "status": "AUTHORIZED_EXACTLY_ONE_SELECTED_CARD",
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
        }
        execution = {
            "case_id": case_id,
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
            "evidence_results": [evidence],
        }
        reevaluation = {
            "case_id": case_id,
            "before_rule_results": [rule],
            "after_rule_results": [rule],
            "reevaluated_rule_instance_ids": [],
            "evidence_links": [],
        }
        profiler_provenance = {
            "schema_version": "dynamics-atlas-proposal-provenance/v1",
            "case_id": case_id,
            "role": "PROFILER",
            "mode": "CALLER_SUPPLIED_IN_MEMORY",
        }
        planner_provenance = {
            "schema_version": "dynamics-atlas-proposal-provenance/v1",
            "case_id": case_id,
            "role": "PLANNER",
            "mode": "CALLER_SUPPLIED_IN_MEMORY",
        }
        artifact_paths = [
            "profiler_proposal_provenance.json",
            "planner_proposal_provenance.json",
            "fresh_rule_state.json",
            "planner_visible_input.json",
            "planner_authorization.json",
            "selected_action_execution.json",
            "rule_reevaluation.json",
            "actions/SYNTH_DESCRIPTIVE_CARD/evidence_result.json",
            "case_run_manifest_v1.json",
        ]
        manifest = {
            "schema_version": "dynamics-atlas-case-run/v1",
            "case_id": case_id,
            "research_question": "Keep UNKNOWN explicit?",
            "claim_boundary": {"allowed": "fixture description only"},
            "input_provenance": {
                "public_case_packet": None,
                "profile_proposal": None,
                "planner_proposal": None,
            },
            "proposal_provenance": {
                "profiler": profiler_provenance,
                "planner": planner_provenance,
            },
            "fresh_rule_state": fresh,
            "planner_visible_input": planner_input,
            "planner_admission": planner_admission,
            "authorization": authorization,
            "action_execution": execution,
            "rule_reevaluation": reevaluation,
            "terminal_scientific_state": "NOT_CALCULATED_BY_CASE_RUNNER",
            "scientific_disposition": "NOT_EVALUATED",
            "source_science_review_status": "PENDING_DOMAIN_REVIEW",
            "artifact_paths": artifact_paths,
            "boundary": "Synthetic run fixture; no terminal scientific state is calculated.",
        }
        for name, value in (
            ("profiler_proposal_provenance.json", profiler_provenance),
            ("planner_proposal_provenance.json", planner_provenance),
            ("fresh_rule_state.json", fresh),
            ("planner_visible_input.json", planner_input),
            ("planner_authorization.json", authorization),
            ("selected_action_execution.json", execution),
            ("rule_reevaluation.json", reevaluation),
            ("actions/SYNTH_DESCRIPTIVE_CARD/evidence_result.json", evidence),
            ("case_run_manifest_v1.json", manifest),
        ):
            _write_json(root / name, value)
        return root

    def test_run_projection_keeps_optional_absence_and_terminal_noncalculation_explicit(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            view = build_case_view(self._build_run_root(Path(temp_dir) / "run"))

        self.assertEqual(view.artifact_kind, "CASE_RUNNER_V1_RUN")
        self.assertEqual(view.terminal_scientific_state, "NOT_CALCULATED_BY_CASE_RUNNER")
        self.assertEqual(view.conclusion_packet["availability"], "UNAVAILABLE")
        self.assertEqual(view.exact_control_regression["availability"], "UNAVAILABLE")
        self.assertEqual(len(view.descriptive_evidence_no_active_rule_effect), 1)
        self.assertEqual(view.active_rule_evidence, [])
        self.assertEqual(view.rule_results[0]["status"], "UNKNOWN")

    def test_run_rejects_mismatched_rule_instance_link(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            reevaluation_path = root / "rule_reevaluation.json"
            reevaluation = json.loads(reevaluation_path.read_text(encoding="utf-8"))
            reevaluation["evidence_links"] = [
                {
                    "affected_rule_instance_id": "UNKNOWN_RULE_INSTANCE",
                    "evidence_result_id": "E1",
                }
            ]
            _write_json(reevaluation_path, reevaluation)
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["rule_reevaluation"] = reevaluation
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(CaseViewIntegrityError, "STALE_RULE_RESULT_LINK"):
                build_case_view(root)


if __name__ == "__main__":
    unittest.main()
