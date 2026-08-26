import copy
import json
import unittest
from pathlib import Path

from dynamics_atlas_harness.real_case_vertical_slice_v1 import (
    ExecutionEvidenceContext,
    HSP90_CASE_ID,
    HSP90_OPERATOR_ID,
    HSP90_RUNTIME_SUBRULE_ID,
    HSP90_SOURCE_ID,
    VerticalSliceError,
    evaluate_hsp90_time_anatomy_f04r02,
    load_hsp90_case_bundle,
    materialize_hsp90_conclusion_packet,
    resolve_hsp90_time_anatomy_obligation,
    validate_hsp90_conclusion_packet,
    validate_hsp90_operator_input_manifest,
    validate_hsp90_time_anatomy_outputs,
)
from dynamics_atlas_harness.registered_operators import (
    execute_hsp90_time_anatomy_adapter,
    load_registered_operator_registry,
)
from dynamics_atlas_harness.rules_prototype_v1 import rule_instance_id


REPO_ROOT = Path(__file__).parents[2]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
OUTPUT_ROOT = EVIDENCE_ROOT / "outputs" / "hsp90_b1_rule_to_operator"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


class Hsp90VerticalSliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = load_hsp90_case_bundle(EVIDENCE_ROOT)
        cls.registry = load_registered_operator_registry(
            REPO_ROOT / "config" / "registered_operators.json"
        )

    def test_b0_case_graph_emits_one_real_computable_f04_obligation(self):
        result = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
        )
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertEqual(
            result["rule_instance_id"],
            rule_instance_id(HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID),
        )
        self.assertEqual(result["family_id"], "F04_SOURCE_RELIABILITY_AND_UNCERTAINTY")
        self.assertEqual(
            result["reason_codes"],
            ["COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING"],
        )
        self.assertEqual(result["claim_effect"]["route"], "REGISTERED_OPERATOR")
        self.assertTrue(result["human_decision_gate_required"])

    def test_exact_route_requires_roster_pass_manifest_and_same_rule_instance(self):
        pre_rule = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
        )
        resolution = resolve_hsp90_time_anatomy_obligation(
            rule_result=pre_rule,
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            operator_registry=self.registry,
            input_manifest=self.bundle["input_manifest"],
            workspace_root=REPO_ROOT,
        )
        self.assertEqual(resolution["route"], "REGISTERED_OPERATOR")
        self.assertEqual(resolution["status"], "ROUTABLE")
        self.assertEqual(resolution["operator_id"], HSP90_OPERATOR_ID)
        self.assertEqual(
            resolution["affected_rule_instance_id"], pre_rule["rule_instance_id"]
        )

        canary_only = copy.deepcopy(self.registry)
        canary_only["operators"][HSP90_OPERATOR_ID]["status"] = "CANARY_PASS"
        canary_only["operators"][HSP90_OPERATOR_ID]["routable"] = False
        blocked = resolve_hsp90_time_anatomy_obligation(
            rule_result=pre_rule,
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            operator_registry=canary_only,
            input_manifest=self.bundle["input_manifest"],
            workspace_root=REPO_ROOT,
        )
        self.assertEqual(blocked["route"], "HUMAN_OR_NEW_DATA")
        self.assertEqual(
            blocked["reason_code"],
            "EXACT_HSP90_OPERATOR_NOT_ROSTER_PASS_AND_ROUTABLE",
        )

        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_HSP90_TIME_ANATOMY_HANDLER"):
            execute_hsp90_time_anatomy_adapter(
                spec=self.registry["operators"]["hsp90.directional_time_anatomy.v0"],
                workspace_root=REPO_ROOT.parent,
                output_dir=REPO_ROOT / "must_not_be_created",
            )

    def test_wrong_target_and_bad_manifest_fail_closed_without_execution(self):
        wrong_target = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
            target_id="different-md-source",
        )
        self.assertEqual(wrong_target["status"], "NOT_APPLICABLE")
        self.assertEqual(wrong_target["reason_codes"], ["WRONG_TARGET_ID"])

        bad_manifest = copy.deepcopy(self.bundle["input_manifest"])
        bad_manifest["fixed_inputs"]["route_predictions"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(VerticalSliceError, "hash mismatch"):
            validate_hsp90_operator_input_manifest(
                input_manifest=bad_manifest,
                operator_spec=self.registry["operators"][HSP90_OPERATOR_ID],
                workspace_root=REPO_ROOT,
            )

    def test_preseeded_or_mutated_context_cannot_fabricate_pass(self):
        expected_rule_id = rule_instance_id(
            HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
        )
        with self.assertRaises(TypeError):
            ExecutionEvidenceContext({expected_rule_id: {"contract_status": "PASS"}})

        context = ExecutionEvidenceContext()
        inspection_copy = context.evidence_results_by_rule_instance
        inspection_copy[expected_rule_id] = {"contract_status": "PASS"}
        result = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
            evidence_context=context,
        )
        self.assertEqual(result["status"], "UNRESOLVED")

    def test_casegraph_time_contract_must_match_the_exact_manifest(self):
        altered_case = copy.deepcopy(self.bundle["case_graph"])
        source = altered_case["evidence_items"][0]
        source["time_semantics"]["saved_stride_ns"] = 2
        source["time_anatomy_control"]["saved_stride_ns"] = 2
        with self.assertRaisesRegex(VerticalSliceError, "does not match the exact manifest"):
            evaluate_hsp90_time_anatomy_f04r02(
                case_graph=altered_case,
                rule_overlay=self.bundle["rule_overlay"],
                input_manifest=self.bundle["input_manifest"],
            )

    def test_forged_pass_rule_cannot_materialize_a_conclusion_packet(self):
        with self.assertRaisesRegex(VerticalSliceError, "exact re-evaluated RuleResult"):
            materialize_hsp90_conclusion_packet(
                case_graph=self.bundle["case_graph"],
                rule_overlay=self.bundle["rule_overlay"],
                input_manifest=self.bundle["input_manifest"],
                operator_registry=self.registry,
                workspace_root=REPO_ROOT,
                rule_result={
                    "status": "PASS",
                    "rule_instance_id": "forged-rule-instance",
                },
                operator_run=None,
                scenario_id="B1_FORGED_PASS",
            )

    def test_generated_operator_output_validates_and_changes_only_f04r02(self):
        self.assertTrue(
            OUTPUT_ROOT.is_dir(),
            "run scripts/run_hsp90_vertical_slice_v1.py before this artifact test",
        )
        pre = read_json(OUTPUT_ROOT / "pre_operator_rule_result.json")
        post = read_json(OUTPUT_ROOT / "post_operator_rule_result.json")
        receipt = read_json(OUTPUT_ROOT / "operator_run_receipt.json")
        evidence = read_json(OUTPUT_ROOT / "evidence_result.json")
        packet = read_json(OUTPUT_ROOT / "conclusion_packet.json")
        run = read_json(OUTPUT_ROOT / "run_receipt.json")

        self.assertEqual(pre["status"], "UNRESOLVED")
        self.assertEqual(post["status"], "PASS")
        self.assertEqual(pre["runtime_subrule_id"], HSP90_RUNTIME_SUBRULE_ID)
        self.assertEqual(post["runtime_subrule_id"], HSP90_RUNTIME_SUBRULE_ID)
        self.assertEqual(receipt["status"], "SUCCEEDED")
        self.assertEqual(evidence["contract_status"], "PASS")
        self.assertEqual(
            evidence["scientific_evaluation_status"], "PENDING_HUMAN_VALIDATION"
        )
        validation = validate_hsp90_time_anatomy_outputs(
            output_dir=OUTPUT_ROOT / "operator_outputs",
            input_manifest=self.bundle["input_manifest"],
        )
        validate_hsp90_conclusion_packet(packet)
        self.assertEqual(validation["status"], "PASS")
        self.assertEqual(validation["observed_counts"]["trajectory_time_anatomy_rows"], 120)
        self.assertEqual(packet["case_id"], HSP90_CASE_ID)
        self.assertEqual(packet["terminal_route"], "REGISTERED_OPERATOR")
        self.assertEqual(packet["terminal_disposition"], "SUPPORT_WITHIN_CEILING")
        self.assertEqual(packet["scientific_verdict"], "NOT_EMITTED_PROPOSAL_ONLY")
        self.assertFalse(packet["unsafe_claim_upgrade"])
        self.assertIn("transition rate", packet["claim_ceiling"].lower())
        self.assertEqual(run["unregistered_tool_calls"], 0)

    def test_execution_evidence_context_rejects_duplicate_and_preserves_human_gate(self):
        context = ExecutionEvidenceContext()
        operator_run = {
            "operator_run_receipt": read_json(OUTPUT_ROOT / "operator_run_receipt.json"),
            "evidence_result": read_json(OUTPUT_ROOT / "evidence_result.json"),
        }
        context.record_validated_operator_run(
            operator_run=operator_run,
            operator_registry=self.registry,
            input_manifest=self.bundle["input_manifest"],
            workspace_root=REPO_ROOT,
        )
        with self.assertRaisesRegex(VerticalSliceError, "duplicate"):
            context.record_validated_operator_run(
                operator_run=operator_run,
                operator_registry=self.registry,
                input_manifest=self.bundle["input_manifest"],
                workspace_root=REPO_ROOT,
            )
        reevaluated = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
            evidence_context=context,
        )
        packet = materialize_hsp90_conclusion_packet(
            case_graph=self.bundle["case_graph"],
            rule_overlay=self.bundle["rule_overlay"],
            input_manifest=self.bundle["input_manifest"],
            operator_registry=self.registry,
            workspace_root=REPO_ROOT,
            rule_result=reevaluated,
            operator_run=operator_run,
            scenario_id="B1_TEST_REEVALUATION",
        )
        self.assertEqual(reevaluated["status"], "PASS")
        self.assertTrue(packet["human_decision_gate_required"])
        self.assertIn("rate", packet["claim_ceiling"].lower())


if __name__ == "__main__":
    unittest.main()
