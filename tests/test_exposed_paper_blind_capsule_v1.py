import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from dynamics_atlas_harness import exposed_paper_blind_capsule_v1 as capsule
from dynamics_atlas_harness.exposed_paper_blind_capsule_v1 import (
    ADK_PUBLIC_CASE_ID,
    HSP90_PUBLIC_CASE_ID,
    ExposedPaperBlindCapsuleError,
    _ACTION_CARD_SPECS,
    _case_human_packet,
    _development_obligations,
    _execute_selected_actions,
    materialize_planner_input,
    run_exposed_paper_blind_capsule,
    run_hsp90_exact_control_regression,
    validate_planner_proposal,
)
from dynamics_atlas_harness.paper_blind_exposed_v1 import (
    project_admitted_proposal_to_rules_casegraph,
    validate_agent_proposal,
    verify_declared_asset_hashes,
)
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_v1 import evaluate_active_rules


REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1"
PUBLIC_ROOT = EVIDENCE_ROOT / "public"
PROFILER_ROOT = EVIDENCE_ROOT / "agent_runs" / "profiler"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _fresh_state(case_slug: str, case_id: str, *, declared_composition: bool = False):
    packet = PUBLIC_ROOT / f"{case_slug}_public_packet_v1.json"
    proposal = _load(PROFILER_ROOT / f"{case_slug}_proposal.json")
    if declared_composition:
        for source in proposal["proposed_case_facts"]["sources"]:
            source["sample_composition"] = "Declared test composition."
    rules = load_rules_v1_bundle(REPO_ROOT / "registries" / "rules_v1")
    casegraph = project_admitted_proposal_to_rules_casegraph(
        packet, validate_agent_proposal(packet, proposal)
    )
    results = evaluate_active_rules(case_graph=casegraph, **rules)
    return packet, proposal, results, _development_obligations(case_id, results)


class ExposedPaperBlindCapsuleV1Tests(unittest.TestCase):
    def test_fresh_rule_state_materializes_planner_input_and_removes_resolved_rule(self):
        packet, _, baseline_results, baseline_items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        _, _, declared_results, declared_items = _fresh_state(
            "hsp90", HSP90_PUBLIC_CASE_ID, declared_composition=True
        )
        baseline = materialize_planner_input(
            case_id=HSP90_PUBLIC_CASE_ID,
            active_rule_results=baseline_results,
            development_items=baseline_items,
            action_card_specs=_ACTION_CARD_SPECS,
            asset_verification=verify_declared_asset_hashes(packet),
        )
        declared = materialize_planner_input(
            case_id=HSP90_PUBLIC_CASE_ID,
            active_rule_results=declared_results,
            development_items=declared_items,
            action_card_specs=_ACTION_CARD_SPECS,
            asset_verification=verify_declared_asset_hashes(packet),
        )
        composition_ref = (
            "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::"
            "HSP90_NMR_METHODS_RESULTS"
        )
        self.assertIn(composition_ref, {item["ref"] for item in baseline["unresolved_items"]})
        self.assertNotIn(composition_ref, {item["ref"] for item in declared["unresolved_items"]})

    def test_stale_planner_references_are_not_materialized_or_accepted(self):
        packet, _, results, items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        stale_card = dict(_ACTION_CARD_SPECS[0])
        stale_card["addresses_ref"] = "F06R02_EDGE_COMPARABILITY::EDGE::HSP90_NMR_MD_CONFORMATIONAL_RELATION"
        planner_input = materialize_planner_input(
            case_id=HSP90_PUBLIC_CASE_ID,
            active_rule_results=results,
            development_items=items,
            action_card_specs=(stale_card,),
            asset_verification=verify_declared_asset_hashes(packet),
        )
        self.assertEqual(planner_input["legal_action_cards"], [])
        self.assertNotIn(stale_card["addresses_ref"], {item["ref"] for item in planner_input["unresolved_items"]})
        self.assertFalse((EVIDENCE_ROOT / "agent_runs" / "planner" / "hsp90_action_input.json").exists())
        self.assertFalse((EVIDENCE_ROOT / "agent_runs" / "planner" / "adk_action_input.json").exists())
        adk_packet, _, adk_results, adk_items = _fresh_state("adk", ADK_PUBLIC_CASE_ID)
        adk_stale = dict(_ACTION_CARD_SPECS[1])
        adk_stale["addresses_ref"] = "F02R02_EDGE_CONDITION_COMPATIBILITY::EDGE::ADK_G10V_TO_CLOSED_REFERENCE"
        adk_input = materialize_planner_input(
            case_id=ADK_PUBLIC_CASE_ID,
            active_rule_results=adk_results,
            development_items=adk_items,
            action_card_specs=(adk_stale,),
            asset_verification=verify_declared_asset_hashes(adk_packet),
        )
        self.assertEqual(adk_input["legal_action_cards"], [])
        self.assertNotIn(adk_stale["addresses_ref"], {item["ref"] for item in adk_input["unresolved_items"]})

    def test_card_requires_unresolved_address_correct_case_and_assets(self):
        packet, _, results, items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        passed_ref = next(item["rule_instance_id"] for item in results if item["status"] == "PASS")
        passed_card = dict(_ACTION_CARD_SPECS[0])
        passed_card["card_id"] = "PASSED_REF_CARD"
        passed_card["addresses_ref"] = passed_ref
        missing_asset_card = dict(_ACTION_CARD_SPECS[0])
        missing_asset_card["card_id"] = "MISSING_ASSET_CARD"
        missing_asset_card["required_asset_ids"] = ("NOT_IN_FROZEN_MANIFEST",)
        wrong_case = dict(_ACTION_CARD_SPECS[1])
        planner_input = materialize_planner_input(
            case_id=HSP90_PUBLIC_CASE_ID,
            active_rule_results=results,
            development_items=items,
            action_card_specs=(passed_card, missing_asset_card, wrong_case),
            asset_verification=verify_declared_asset_hashes(packet),
        )
        self.assertEqual(planner_input["legal_action_cards"], [])
        with self.assertRaisesRegex(ExposedPaperBlindCapsuleError, "PLANNER_SELECTED_ILLEGAL_CARD"):
            validate_planner_proposal(
                planner_input,
                {
                    "case_id": HSP90_PUBLIC_CASE_ID,
                    "decision": "SELECT_ACTIONS",
                    "selected_card_ids": ["PASSED_REF_CARD"],
                    "rationales": {"PASSED_REF_CARD": "stale"},
                },
            )

    def test_selection_controls_only_public_action_and_exact_control_is_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_exposed_paper_blind_capsule(
                output_root=Path(tmp) / "run", include_exact_hsp90_control_regression=False
            )
            hsp90 = result["cases"][HSP90_PUBLIC_CASE_ID]["selected_execution"]
            adk = result["cases"][ADK_PUBLIC_CASE_ID]["selected_execution"]
            self.assertEqual(
                hsp90["selected_card_ids"], ["HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1"]
            )
            self.assertEqual(
                adk["selected_card_ids"],
                ["ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1"],
            )
            self.assertFalse(
                (Path(result["output_root"]) / "hsp90" / "existing_exact_hsp90_control_regression").exists()
            )
            control = run_hsp90_exact_control_regression(output_root=Path(tmp) / "control")
            self.assertEqual(control["sidecar_kind"], "EXISTING_EXACT_CONTROL_REGRESSION")
            self.assertEqual(control["public_case_rule_effect"], "NO_ACTIVE_RULE_EFFECT")
            self.assertEqual(control["exact_control_rule_effect"], "ACTIVE_RULE_EFFECT")

    def test_abstention_executes_no_action_or_control_receipt(self):
        abstain = {
            "case_id": HSP90_PUBLIC_CASE_ID,
            "decision": "ABSTAIN_NO_ACTION",
            "selected_card_ids": [],
            "rationales": {},
        }
        with tempfile.TemporaryDirectory() as tmp:
            result = run_exposed_paper_blind_capsule(
                output_root=Path(tmp) / "run",
                planner_proposal_overrides={HSP90_PUBLIC_CASE_ID: abstain},
                include_exact_hsp90_control_regression=False,
            )
            hsp90 = result["cases"][HSP90_PUBLIC_CASE_ID]
            self.assertEqual(hsp90["selected_execution"]["execution_status"], "NO_ACTION_SELECTED")
            self.assertEqual(hsp90["selected_execution"]["evidence_results"], [])
            self.assertEqual(
                hsp90["human_decision_packet"]["existing_exact_hsp90_control_regression"]["status"],
                "NOT_RUN_IN_THIS_CAPSULE_INVOCATION",
            )

    def test_illegal_cross_case_selection_fails_before_action_output(self):
        illegal = {
            "case_id": HSP90_PUBLIC_CASE_ID,
            "decision": "SELECT_ACTIONS",
            "selected_card_ids": ["ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1"],
            "rationales": {"ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1": "wrong case"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "run"
            with self.assertRaisesRegex(ExposedPaperBlindCapsuleError, "PLANNER_SELECTED_ILLEGAL_CARD"):
                run_exposed_paper_blind_capsule(
                    output_root=root,
                    planner_proposal_overrides={HSP90_PUBLIC_CASE_ID: illegal},
                    include_exact_hsp90_control_regression=False,
                )
            self.assertFalse((root / "hsp90" / "arm_c_selected_public_actions.json").exists())
            self.assertFalse((root / "hsp90" / "existing_exact_hsp90_control_regression").exists())

    def test_descriptive_adapter_cannot_forge_active_rule_effect(self):
        packet, _, results, items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        planner_input = materialize_planner_input(
            case_id=HSP90_PUBLIC_CASE_ID,
            active_rule_results=results,
            development_items=items,
            action_card_specs=_ACTION_CARD_SPECS,
            asset_verification=verify_declared_asset_hashes(packet),
        )
        admission = validate_planner_proposal(
            planner_input,
            {
                "case_id": HSP90_PUBLIC_CASE_ID,
                "decision": "SELECT_ACTIONS",
                "selected_card_ids": ["HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1"],
                "rationales": {"HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1": "test"},
            },
        )
        with patch.dict(
            capsule._CARD_EXECUTORS,
            {"HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1": lambda: {"rule_effect": "ACTIVE_RULE_EFFECT"}},
        ):
            with self.assertRaisesRegex(
                ExposedPaperBlindCapsuleError, "DESCRIPTIVE_RESULT_ATTEMPTED_ACTIVE_RULE_EFFECT"
            ):
                _execute_selected_actions(
                    case_id=HSP90_PUBLIC_CASE_ID,
                    planner_input=planner_input,
                    planner_admission=admission,
                )

    def test_gap_taxonomy_distinguishes_source_contract_bridge_and_new_data(self):
        _, _, _, hsp90_items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        by_ref = {item.get("rule_instance_id", item.get("development_obligation_ref")): item for item in hsp90_items}
        self.assertEqual(
            by_ref[
                "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::HSP90_NMR_METHODS_RESULTS"
            ]["gap_type"],
            "SOURCE_FACT_MISSING",
        )
        self.assertEqual(
            by_ref["F06R01_SOURCE_EVIDENCE_ROLE::SOURCE::HSP90_NMR_METHODS_RESULTS"]["gap_type"],
            "SOURCE_FACT_MISSING",
        )
        self.assertEqual(
            by_ref["F06R01_SOURCE_EVIDENCE_ROLE::SOURCE::HSP90_NMR_METHODS_RESULTS"]["reason_codes"],
            ["SOURCE_PROPOSED_LINEAGE_REQUIRES_VERIFICATION"],
        )
        self.assertEqual(
            by_ref["HSP90_DEV_OBL_NMR_MD_FORWARD_BRIDGE"]["gap_type"],
            "METHOD_OR_FORWARD_BRIDGE_MISSING",
        )
        self.assertEqual(
            by_ref["HSP90_DEV_OBL_CANDIDATE_F04_F05_F07_LIFECYCLE"]["gap_type"],
            "EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING",
        )
        _, _, _, adk_items = _fresh_state("adk", ADK_PUBLIC_CASE_ID)
        adk_by_ref = {item.get("rule_instance_id", item.get("development_obligation_ref")): item for item in adk_items}
        self.assertEqual(adk_by_ref["ADK_DEV_OBL_DYNAMIC_COVERAGE"]["gap_type"], "NEW_DATA_REQUIRED")

    def test_human_packet_has_no_order_derived_first_blocker(self):
        _, _, results, items = _fresh_state("hsp90", HSP90_PUBLIC_CASE_ID)
        arm = {"rule_results": results, "projected_casegraph": {"case": {"scientific_claim": "test"}}}
        first = _case_human_packet(
            case_id=HSP90_PUBLIC_CASE_ID,
            agent_rule_arm=arm,
            development_obligations=items,
            selected_execution={"evidence_results": []},
            comparison={},
            exact_hsp90_control_regression=None,
        )
        arm["rule_results"] = list(reversed(results))
        second = _case_human_packet(
            case_id=HSP90_PUBLIC_CASE_ID,
            agent_rule_arm=arm,
            development_obligations=list(reversed(items)),
            selected_execution={"evidence_results": []},
            comparison={},
            exact_hsp90_control_regression=None,
        )
        self.assertNotIn("first_blocking_rule_instance", first)
        self.assertEqual(first["blocking_unresolved_rule_instances"], second["blocking_unresolved_rule_instances"])
        self.assertEqual(first["resolution_options"], second["resolution_options"])

    def test_comparison_and_provenance_do_not_claim_agent_accuracy_or_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_exposed_paper_blind_capsule(
                output_root=Path(tmp) / "run", include_exact_hsp90_control_regression=False
            )
            hsp90 = result["cases"][HSP90_PUBLIC_CASE_ID]
            comparison = hsp90["human_decision_packet"]["development_reference_comparison"]
            self.assertIn("BOUNDARY_CONSISTENCY", comparison)
            self.assertIn("AGENT_AUTHORED_CONTENT_ASSESSMENT", comparison)
            self.assertNotIn("precision", json.dumps(comparison))
            self.assertNotIn("recall", json.dumps(comparison))
            provenance = _load(Path(result["output_root"]) / "hsp90" / "profiler_proposal_provenance.json")
            self.assertEqual(provenance["provenance_status"], "RECORDED_PROPOSAL_REPLAY_ONLY")
            self.assertEqual(provenance["answer_blindness_status"], "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED")
            self.assertFalse(provenance["filesystem_isolation_technically_enforced"])

    def test_scientific_semantics_preserve_groups_static_scope_and_no_active_rule_effect(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_exposed_paper_blind_capsule(
                output_root=Path(tmp) / "run", include_exact_hsp90_control_regression=False
            )
        hsp90 = result["cases"][HSP90_PUBLIC_CASE_ID]["selected_execution"]["evidence_results"][0]["descriptive_result"]
        self.assertEqual(hsp90["capability_kind"], "GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION")
        self.assertEqual(hsp90["row_count"], 40)
        self.assertEqual(
            {item["group_id"]: item["trajectory_count"] for item in hsp90["within_group_summaries"]},
            {"R46A_ES": 20, "R60A_GS": 20},
        )
        self.assertIn("does not establish global sampling adequacy", hsp90["limitation"])
        self.assertEqual(hsp90["rule_effect"], "NO_ACTIVE_RULE_EFFECT")
        adk = result["cases"][ADK_PUBLIC_CASE_ID]["selected_execution"]["evidence_results"][0]["descriptive_result"]
        self.assertEqual(adk["capability_kind"], "STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION")
        self.assertEqual(len(adk["reference_distances"]), 2)
        self.assertEqual(adk["rule_effect"], "NO_ACTIVE_RULE_EFFECT")
        self.assertIn("portability", adk["forbidden_claims"])


if __name__ == "__main__":
    unittest.main()
