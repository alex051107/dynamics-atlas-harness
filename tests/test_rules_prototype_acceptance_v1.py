import copy
import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import main as cli_main
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_acceptance_v1 import (
    RulesPrototypeAcceptanceError,
    _mutation_guard,
    compare_suite_to_expected,
    run_acceptance_suite,
    run_task_card,
    write_acceptance_artifacts,
)


REPO_ROOT = Path(__file__).parents[1]
ARTIFACT_ROOT = REPO_ROOT / "research" / "rules_prototype_acceptance_v1"
GENERATED_ARTIFACTS = (
    "actual_results.jsonl",
    "acceptance_matrix.csv",
    "REPORT.md",
)


def read_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]


def read_matrix(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


class RulesPrototypeAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = read_jsonl(ARTIFACT_ROOT / "cases.jsonl")
        cls.expected = {
            row["task_id"]: row
            for row in read_jsonl(ARTIFACT_ROOT / "expected_results.jsonl")
        }
        cls.suite = run_acceptance_suite(repo_root=REPO_ROOT)
        cls.actual = {row["task_id"]: row for row in cls.suite["results"]}
        cls.comparison = compare_suite_to_expected(
            suite=cls.suite,
            expected_results_path=ARTIFACT_ROOT / "expected_results.jsonl",
        )

    def test_all_eight_cards_match_their_predeclared_expected_results(self):
        self.assertEqual(self.comparison["acceptance"], "PASS")
        self.assertEqual(self.comparison["task_count"], 8)
        self.assertEqual(self.comparison["passing_task_count"], 8)
        self.assertEqual(self.comparison["mismatch_count"], 0)
        self.assertEqual(set(self.actual), set(self.expected))
        self.assertEqual(
            {item["acceptance"] for item in self.comparison["task_results"]}, {"PASS"}
        )

    def test_common_driver_preserves_bounded_route_and_claim_contracts(self):
        summary = self.suite["summary"]
        self.assertEqual(summary["task_count"], 8)
        self.assertTrue(
            {"DIRECT_EVALUATION", "EXACT_LOOKUP", "REGISTERED_OPERATOR", "STOP"}.issubset(
                set(summary["action_kinds"])
            )
        )
        self.assertTrue(
            {"PASS", "FAIL", "UNRESOLVED"}.issubset(summary["post_rule_statuses"])
        )
        self.assertEqual(
            set(summary["terminal_states"]),
            {
                "SUPPORT_WITHIN_CEILING",
                "CANNOT_SUPPORT_REQUESTED_CLAIM",
                "ABSTAIN_OR_HUMAN_REVIEW",
            },
        )
        self.assertGreaterEqual(summary["same_rule_closure_count"], 1)
        self.assertEqual(summary["unregistered_tool_calls"], 0)
        self.assertEqual(summary["mutation_guard_pass_count"], 8)
        self.assertEqual(self.comparison["claim_ceiling_checks_passed"], 8)
        for actual in self.actual.values():
            packet = actual["conclusion_packet"]
            self.assertEqual(packet["scientific_disposition"], "NOT_EVALUATED")
            self.assertTrue(packet["human_decision_gate_required"])
            self.assertIn(packet["claim_ceiling_source"]["kind"], {"RULE_CONTRACT", "EVIDENCE_RESULT"})

    def test_expected_terminal_mismatch_fails_cli_and_matrix_row(self):
        with tempfile.TemporaryDirectory(prefix="rules-prototype-cli-mismatch-") as temp_dir:
            artifacts = Path(temp_dir)
            for name in ("cases.jsonl", "expected_results.jsonl"):
                shutil.copy2(ARTIFACT_ROOT / name, artifacts / name)
            expected_rows = read_jsonl(artifacts / "expected_results.jsonl")
            expected_rows[0]["expected_terminal_state"] = "ABSTAIN_OR_HUMAN_REVIEW"
            (artifacts / "expected_results.jsonl").write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in expected_rows),
                encoding="utf-8",
            )
            exit_code = cli_main(
                [
                    "run-prototype-acceptance",
                    "--repo-root",
                    str(REPO_ROOT),
                    "--artifacts-dir",
                    str(artifacts),
                ]
            )
            self.assertEqual(exit_code, 1)
            matrix_by_task = {
                row["task_id"]: row for row in read_matrix(artifacts / "acceptance_matrix.csv")
            }
            self.assertEqual(
                matrix_by_task["T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"]["acceptance"],
                "FAIL",
            )
            self.assertIn(
                "TERMINAL_STATE_MISMATCH",
                matrix_by_task["T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"][
                    "mismatch_codes"
                ],
            )

    def test_extra_blocking_rule_instance_fails_exact_inventory_comparison(self):
        mutated = copy.deepcopy(self.suite)
        task = next(
            item
            for item in mutated["results"]
            if item["task_id"] == "T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"
        )
        injected = copy.deepcopy(task["initial_rule_results"][0])
        injected["rule_instance_id"] = "INJECTED_BLOCKING_RULE::SOURCE::t1_nmr_source"
        injected["runtime_subrule_id"] = "INJECTED_BLOCKING_RULE"
        injected["status"] = "FAIL"
        task["initial_rule_results"].append(copy.deepcopy(injected))
        task["post_action_rule_results"].append(copy.deepcopy(injected))
        task["applicable_rule_instances"].append(
            {
                "rule_instance_id": injected["rule_instance_id"],
                "runtime_subrule_id": injected["runtime_subrule_id"],
                "family_id": "INJECTED",
                "target": {"kind": "SOURCE", "id": "t1_nmr_source"},
                "status": "FAIL",
            }
        )
        comparison = compare_suite_to_expected(
            suite=mutated,
            expected_results_path=ARTIFACT_ROOT / "expected_results.jsonl",
        )
        t1 = next(
            item
            for item in comparison["task_results"]
            if item["task_id"] == "T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"
        )
        self.assertEqual(comparison["acceptance"], "FAIL")
        self.assertEqual(t1["acceptance"], "FAIL")
        self.assertIn(
            "APPLICABLE_RULE_INVENTORY_MISMATCH",
            {item["code"] for item in t1["mismatches"]},
        )

    def test_stop_with_an_authorized_lookup_fails_closed(self):
        card = copy.deepcopy(
            next(item for item in self.cards if item["task_id"] == "T5_XEISD_EXACT_LOOKUP_AVAILABLE")
        )
        card["resolution"]["action_kind"] = "STOP"
        card["resolution"]["stop_reason"] = "TEST_ONLY_STOP"
        bundle = load_rules_v1_bundle(REPO_ROOT / "registries" / "rules_v1")
        with self.assertRaisesRegex(
            RulesPrototypeAcceptanceError,
            "STOP requested despite an authorized action",
        ):
            run_task_card(card, repo_root=REPO_ROOT, bundle=bundle)

    def test_evidence_result_for_another_rule_instance_fails_closed(self):
        selected = self.actual["T5_XEISD_EXACT_LOOKUP_AVAILABLE"]["selected_obligation"]
        with self.assertRaisesRegex(
            RulesPrototypeAcceptanceError,
            "EvidenceResult targets another RuleInstance",
        ):
            _mutation_guard(
                selected,
                {"action_kind": "EXACT_LOOKUP"},
                [{"affected_rule_instance_id": "INJECTED::SOURCE::other"}],
                [{"rule_instance_id": selected["rule_instance_id"]}],
            )

    def test_modified_conclusion_claim_ceiling_fails_comparison(self):
        mutated = copy.deepcopy(self.suite)
        task = next(
            item
            for item in mutated["results"]
            if item["task_id"] == "T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"
        )
        task["conclusion_packet"]["claim_ceiling"] = "UNAUTHORIZED_CLAIM_CEILING"
        comparison = compare_suite_to_expected(
            suite=mutated,
            expected_results_path=ARTIFACT_ROOT / "expected_results.jsonl",
        )
        t1 = next(
            item
            for item in comparison["task_results"]
            if item["task_id"] == "T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION"
        )
        self.assertEqual(t1["acceptance"], "FAIL")
        self.assertIn(
            "CLAIM_CEILING_PACKET_VALUE_MISMATCH",
            {item["code"] for item in t1["mismatches"]},
        )
        self.assertIn(
            "CLAIM_CEILING_MISMATCH",
            {item["code"] for item in t1["mismatches"]},
        )

    def test_committed_generated_artifacts_reconstruct_byte_for_byte(self):
        with tempfile.TemporaryDirectory(prefix="rules-prototype-reconstruct-") as temp_dir:
            output_root = Path(temp_dir)
            write_acceptance_artifacts(
                artifacts_dir=output_root,
                suite=self.suite,
                comparison=self.comparison,
            )
            for name in GENERATED_ARTIFACTS:
                with self.subTest(artifact=name):
                    self.assertEqual(
                        (output_root / name).read_bytes(),
                        (ARTIFACT_ROOT / name).read_bytes(),
                    )
            report = (output_root / "REPORT.md").read_text(encoding="utf-8")
            self.assertIn("Comparator verdict: PASS", report)
            self.assertIn("four synthetic contract fixtures", report)
            self.assertIn("DESCRIPTIVE_NO_ACTIVE_RULE_CONTROL", report)

    def test_generated_descriptive_floats_are_canonicalized_for_artifacts(self):
        with tempfile.TemporaryDirectory(prefix="rules-prototype-float-artifact-") as temp_dir:
            output_root = Path(temp_dir)
            write_acceptance_artifacts(
                artifacts_dir=output_root,
                suite=self.suite,
                comparison=self.comparison,
            )
            generated_t8 = next(
                item
                for item in read_jsonl(output_root / "actual_results.jsonl")
                if item["task_id"] == "T8_ADK_BOUNDED_STRUCTURAL_COMPUTATION"
            )
            runtime_t8 = self.actual["T8_ADK_BOUNDED_STRUCTURAL_COMPUTATION"]
            generated = generated_t8["evidence_results"][0]["reference_distances"]
            runtime = runtime_t8["evidence_results"][0]["reference_distances"]
            self.assertEqual(
                [item["aligned_rmsd_angstrom"] for item in generated],
                [round(item["aligned_rmsd_angstrom"], 12) for item in runtime],
            )


if __name__ == "__main__":
    unittest.main()
