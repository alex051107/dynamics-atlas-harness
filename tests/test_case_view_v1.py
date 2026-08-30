"""Behavioral checks for the artifact-only CaseView read model."""

from __future__ import annotations

import json
import hashlib
import shutil
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.case_view_v1 import (
    CaseViewIntegrityError,
    build_case_view,
)
from dynamics_atlas_harness.paper_blind_exposed_v1 import validate_agent_proposal
from dynamics_atlas_harness.proposal_provenance_v1 import (
    CALLER_SUPPLIED_IN_MEMORY,
    build_proposal_provenance_v1,
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


def _canonical_sha256(value) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


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
        case_id = "HSP90_NTD_EXPOSED_PAPER_BLIND_V1"
        public_packet_path = (
            REPO_ROOT
            / "evidence"
            / "paper_blind_exposed_v1"
            / "public"
            / "hsp90_public_packet_v1.json"
        )
        profile_proposal_path = (
            REPO_ROOT
            / "evidence"
            / "paper_blind_exposed_v1"
            / "agent_runs"
            / "profiler"
            / "hsp90_proposal.json"
        )
        public_packet = json.loads(public_packet_path.read_text(encoding="utf-8"))
        profile_proposal = json.loads(profile_proposal_path.read_text(encoding="utf-8"))
        profiler_visible_input = {
            "schema_version": "paper-blind-agent-visible-input/v1",
            **{
                field: public_packet[field]
                for field in (
                    "packet_id",
                    "case_id",
                    "research_question",
                    "source_materials",
                    "data_assets",
                    "agent_proposal_schema",
                )
            },
        }
        planner_proposal = {
            "case_id": case_id,
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
            "rationales": {"SYNTH_DESCRIPTIVE_CARD": "Exercise the test-only card."},
        }
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
            "admission": validate_agent_proposal(public_packet_path, profile_proposal),
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
            "schema_version": "paper-blind-planner-proposal-admission/v2",
            "proposal_status": "ADMISSIBLE_CARD_SELECTION_ONLY",
            "case_id": case_id,
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
            "rationales": {"SYNTH_DESCRIPTIVE_CARD": "Exercise the test-only card."},
            "execution_authorization": "AUTHORIZED_EXACT_SELECTED_CAPSULE_ACTIONS_ONLY",
            "scientific_disposition": "NOT_EVALUATED",
        }
        authorization = {
            "schema_version": "case-runner-authorization/v1",
            "case_id": case_id,
            "status": "AUTHORIZED_EXACTLY_ONE_SELECTED_CARD",
            "selected_card_ids": ["SYNTH_DESCRIPTIVE_CARD"],
            "executed_action_count": 1,
        }
        execution = {
            "execution_status": "SELECTED_ACTIONS_EXECUTED",
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
        def proposal_provenance(role, visible_input, proposal, evaluation):
            return build_proposal_provenance_v1(
                role=role,
                mode=CALLER_SUPPLIED_IN_MEMORY,
                visible_input=visible_input,
                parsed_proposal=proposal,
                contract_evaluator=(
                    "validate_agent_proposal"
                    if role == "PROFILER"
                    else "validate_planner_proposal"
                ),
                contract_admission_evaluation=evaluation,
                source_path=None,
            )

        profiler_provenance = proposal_provenance(
            "PROFILER", profiler_visible_input, profile_proposal, fresh["admission"]
        )
        planner_provenance = proposal_provenance(
            "PLANNER", planner_input, planner_proposal, planner_admission
        )
        artifact_paths = [
            "inputs/public_case_packet.json",
            "inputs/profiler_visible_input.json",
            "inputs/profile_proposal.json",
            "inputs/planner_proposal.json",
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
            "run_scope": "EXPOSED_DEVELOPMENT_ONLY",
            "research_question": public_packet["research_question"],
            "claim_boundary": public_packet["platform_authority_envelope"][
                "claim_boundary"
            ],
            "input_provenance": {
                "public_case_packet": (
                    "evidence/paper_blind_exposed_v1/public/hsp90_public_packet_v1.json"
                ),
                "profile_proposal": None,
                "planner_proposal": None,
                "profile_mode": "CALLER_SUPPLIED_IN_MEMORY",
                "planner_mode": "CALLER_SUPPLIED_IN_MEMORY",
                "snapshot_artifacts": {
                    "public_case_packet": {
                        "path": "inputs/public_case_packet.json",
                        "canonical_sha256": _canonical_sha256(public_packet),
                    },
                    "profiler_visible_input": {
                        "path": "inputs/profiler_visible_input.json",
                        "canonical_sha256": _canonical_sha256(profiler_visible_input),
                    },
                    "profile_proposal": {
                        "path": "inputs/profile_proposal.json",
                        "canonical_sha256": _canonical_sha256(profile_proposal),
                    },
                    "planner_proposal": {
                        "path": "inputs/planner_proposal.json",
                        "canonical_sha256": _canonical_sha256(planner_proposal),
                    },
                    "planner_visible_input": {
                        "path": "planner_visible_input.json",
                        "canonical_sha256": _canonical_sha256(planner_input),
                    },
                },
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
            "network_accessed": False,
            "credentials_accessed": False,
            "external_model_transport": False,
            "artifact_paths": artifact_paths,
            "boundary": (
                "This runner records deterministic exposed-development behavior only. "
                "It does not compute a terminal verdict, source-science approval, broad "
                "HSP90 closure, ADK dynamics portability, or Agent effectiveness."
            ),
        }
        for name, value in (
            ("inputs/public_case_packet.json", public_packet),
            ("inputs/profiler_visible_input.json", profiler_visible_input),
            ("inputs/profile_proposal.json", profile_proposal),
            ("inputs/planner_proposal.json", planner_proposal),
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

    def test_run_rejects_changed_rule_without_link_and_tampered_identity(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "changed")
            reevaluation_path = root / "rule_reevaluation.json"
            reevaluation = json.loads(reevaluation_path.read_text(encoding="utf-8"))
            reevaluation["after_rule_results"][0]["status"] = "PASS"
            _write_json(reevaluation_path, reevaluation)
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["rule_reevaluation"] = reevaluation
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "REEVALUATED_RULE_CHANGE_SET_MISMATCH"
            ):
                build_case_view(root)

        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "identity")
            reevaluation_path = root / "rule_reevaluation.json"
            reevaluation = json.loads(reevaluation_path.read_text(encoding="utf-8"))
            reevaluation["after_rule_results"][0]["target"]["id"] = "TAMPERED_SOURCE"
            _write_json(reevaluation_path, reevaluation)
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["rule_reevaluation"] = reevaluation
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(CaseViewIntegrityError, "RULE_INSTANCE_IDENTITY_CHANGED"):
                build_case_view(root)

    def test_run_rejects_stale_proposal_receipt_hashes_and_source_path(self):
        mutations = (
            ("visible_input", "canonical_sha256", "STALE_PROPOSAL_RECEIPT_HASH"),
            ("parsed_proposal", "canonical_sha256", "STALE_PROPOSAL_RECEIPT_HASH"),
            (
                "contract_admission_evaluation",
                "canonical_sha256",
                "STALE_PROPOSAL_RECEIPT_HASH",
            ),
        )
        for field, key, expected_error in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp_dir:
                root = self._build_run_root(Path(temp_dir) / "run")
                receipt_path = root / "profiler_proposal_provenance.json"
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                receipt[field][key] = "0" * 64
                _write_json(receipt_path, receipt)
                manifest_path = root / "case_run_manifest_v1.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest["proposal_provenance"]["profiler"] = receipt
                _write_json(manifest_path, manifest)
                with self.assertRaisesRegex(CaseViewIntegrityError, expected_error):
                    build_case_view(root)

        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            receipt_path = root / "profiler_proposal_provenance.json"
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["source_path"] = "tampered/proposal.json"
            _write_json(receipt_path, receipt)
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["proposal_provenance"]["profiler"] = receipt
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "PROPOSAL_RECEIPT_SOURCE_PATH_MISMATCH"
            ):
                build_case_view(root)

    def test_run_rejects_unclassified_evidence_instead_of_promoting_it(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            execution_path = root / "selected_action_execution.json"
            execution = json.loads(execution_path.read_text(encoding="utf-8"))
            unclassified = {
                "case_id": execution["case_id"],
                "card_id": execution["selected_card_ids"][0],
                "evidence_result_id": "UNKNOWN_EFFECT_EVIDENCE",
            }
            execution["evidence_results"] = [unclassified]
            _write_json(execution_path, execution)
            _write_json(
                root
                / "actions"
                / execution["selected_card_ids"][0]
                / "evidence_result.json",
                unclassified,
            )
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["action_execution"] = execution
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "EVIDENCE_EFFECT_CLASSIFICATION_UNKNOWN"
            ):
                build_case_view(root)

    def test_run_rejects_authorization_not_reconciled_to_admission_and_execution(self):
        mutations = (
            ("status", "DENIED"),
            ("selected_card_ids", ["NOT_AUTHORIZED_CARD"]),
            ("executed_action_count", 0),
        )
        for field, value in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp_dir:
                root = self._build_run_root(Path(temp_dir) / "run")
                authorization_path = root / "planner_authorization.json"
                authorization = json.loads(authorization_path.read_text(encoding="utf-8"))
                authorization[field] = value
                _write_json(authorization_path, authorization)
                manifest_path = root / "case_run_manifest_v1.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest["authorization"] = authorization
                _write_json(manifest_path, manifest)
                with self.assertRaisesRegex(CaseViewIntegrityError, "AUTHORIZATION_"):
                    build_case_view(root)

    def test_run_rejects_manifest_question_or_claim_ceiling_not_in_public_packet(self):
        mutations = (
            ("research_question", "Forged question", "PUBLIC_PACKET_QUESTION_MISMATCH"),
            (
                "claim_boundary",
                {"allowed": "Forged elevated scientific claim"},
                "PUBLIC_PACKET_CLAIM_BOUNDARY_MISMATCH",
            ),
        )
        for field, value, expected_error in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp_dir:
                root = self._build_run_root(Path(temp_dir) / "run")
                manifest_path = root / "case_run_manifest_v1.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest[field] = value
                _write_json(manifest_path, manifest)
                with self.assertRaisesRegex(CaseViewIntegrityError, expected_error):
                    build_case_view(root)

    def test_run_rejects_forged_packet_claim_chain_when_source_anchor_is_removed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            packet_path = root / "inputs" / "public_case_packet.json"
            packet = json.loads(packet_path.read_text(encoding="utf-8"))
            packet["research_question"] = "Forged elevated question"
            packet["platform_authority_envelope"]["claim_boundary"] = {
                "allowed": "FORGED_BROAD_SCIENTIFIC_SUPPORT"
            }
            _write_json(packet_path, packet)

            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["research_question"] = packet["research_question"]
            manifest["claim_boundary"] = packet["platform_authority_envelope"][
                "claim_boundary"
            ]
            manifest["input_provenance"]["public_case_packet"] = None
            manifest["input_provenance"]["snapshot_artifacts"]["public_case_packet"][
                "canonical_sha256"
            ] = _canonical_sha256(packet)
            _write_json(manifest_path, manifest)

            with self.assertRaisesRegex(
                CaseViewIntegrityError, "REPOSITORY_PUBLIC_PACKET_SOURCE_REQUIRED"
            ):
                build_case_view(root)

    def test_run_rejects_non_runner_terminal_review_and_transport_state(self):
        mutations = (
            ("schema_version", "forged-run/v1"),
            ("run_scope", "PRODUCTION"),
            ("terminal_scientific_state", "FORGED_SCIENTIFIC_SUPPORT"),
            ("scientific_disposition", "SUPPORTED"),
            ("source_science_review_status", "APPROVED_BY_NAMED_REVIEWER"),
            ("network_accessed", True),
            ("credentials_accessed", True),
            ("external_model_transport", True),
            ("boundary", "Forged unrestricted scientific result."),
        )
        for field, value in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp_dir:
                root = self._build_run_root(Path(temp_dir) / "run")
                manifest_path = root / "case_run_manifest_v1.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest[field] = value
                _write_json(manifest_path, manifest)
                with self.assertRaisesRegex(
                    CaseViewIntegrityError,
                    f"CASE_RUNNER_MANIFEST_INVARIANT_MISMATCH:{field}",
                ):
                    build_case_view(root)

    def test_run_rejects_recorded_proposal_diverging_from_repository_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            profile = manifest["proposal_provenance"]["profiler"]
            profile_source = (
                "evidence/paper_blind_exposed_v1/agent_runs/profiler/adk_proposal.json"
            )
            manifest["input_provenance"]["profile_mode"] = "RECORDED_PROPOSAL_REPLAY"
            manifest["input_provenance"]["profile_proposal"] = profile_source
            profiler_visible_input = json.loads(
                (root / "inputs" / "profiler_visible_input.json").read_text(encoding="utf-8")
            )
            profile = build_proposal_provenance_v1(
                role="PROFILER",
                mode="RECORDED_PROPOSAL_REPLAY",
                visible_input=profiler_visible_input,
                parsed_proposal=json.loads(
                    (root / "inputs" / "profile_proposal.json").read_text(encoding="utf-8")
                ),
                contract_evaluator="validate_agent_proposal",
                contract_admission_evaluation=manifest["fresh_rule_state"]["admission"],
                source_path=profile_source,
            )
            manifest["proposal_provenance"]["profiler"] = profile
            _write_json(root / "profiler_proposal_provenance.json", profile)
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "REPOSITORY_SOURCE_SNAPSHOT_MISMATCH"
            ):
                build_case_view(root)

    def test_run_rejects_profiler_input_not_derived_from_public_packet(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            visible_path = root / "inputs" / "profiler_visible_input.json"
            visible = json.loads(visible_path.read_text(encoding="utf-8"))
            visible["research_question"] = "Forged Profiler-visible question"
            _write_json(visible_path, visible)

            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["input_provenance"]["snapshot_artifacts"][
                "profiler_visible_input"
            ]["canonical_sha256"] = _canonical_sha256(visible)
            profile = json.loads(
                (root / "inputs" / "profile_proposal.json").read_text(encoding="utf-8")
            )
            receipt = build_proposal_provenance_v1(
                role="PROFILER",
                mode=CALLER_SUPPLIED_IN_MEMORY,
                visible_input=visible,
                parsed_proposal=profile,
                contract_evaluator="validate_agent_proposal",
                contract_admission_evaluation=manifest["fresh_rule_state"]["admission"],
                source_path=None,
            )
            manifest["proposal_provenance"]["profiler"] = receipt
            _write_json(root / "profiler_proposal_provenance.json", receipt)
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "PROFILER_VISIBLE_INPUT_PUBLIC_PACKET_MISMATCH"
            ):
                build_case_view(root)

    def test_run_rejects_planner_admission_not_derived_from_proposal(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._build_run_root(Path(temp_dir) / "run")
            manifest_path = root / "case_run_manifest_v1.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            admission = manifest["planner_admission"]
            admission["scientific_disposition"] = "SUPPORTED"
            proposal = json.loads(
                (root / "inputs" / "planner_proposal.json").read_text(encoding="utf-8")
            )
            receipt = build_proposal_provenance_v1(
                role="PLANNER",
                mode=CALLER_SUPPLIED_IN_MEMORY,
                visible_input=manifest["planner_visible_input"],
                parsed_proposal=proposal,
                contract_evaluator="validate_planner_proposal",
                contract_admission_evaluation=admission,
                source_path=None,
            )
            manifest["proposal_provenance"]["planner"] = receipt
            _write_json(root / "planner_proposal_provenance.json", receipt)
            _write_json(manifest_path, manifest)
            with self.assertRaisesRegex(
                CaseViewIntegrityError, "PLANNER_ADMISSION_PROPOSAL_MISMATCH"
            ):
                build_case_view(root)


if __name__ == "__main__":
    unittest.main()
