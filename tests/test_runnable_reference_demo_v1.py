"""Behavioral checks for the narrow clean-checkout reference demo."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from dynamics_atlas_harness.cli import main


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class RunnableReferenceDemoTests(unittest.TestCase):
    def test_module_command_materializes_fresh_routes_and_bounded_stage2_packets(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            self.assertEqual(main(["run-demo", "--output-dir", str(output_dir)]), 0)

            summary = read_json(output_dir / "run_summary.json")
            self.assertEqual(summary["status"], "SUCCEEDED")
            self.assertEqual(summary["scientific_support_packets"], 0)
            self.assertEqual(
                summary["terminal_dispositions"],
                {
                    "HSP90_B1_OPERATOR_CONTRACT_PASS": "ABSTAIN_OR_HUMAN_REVIEW",
                    "XEISD_A1_COMPLETE_METADATA": "ABSTAIN_OR_HUMAN_REVIEW",
                    "XEISD_A2_MISSING_COMPOSITION": "ABSTAIN_OR_HUMAN_REVIEW",
                    "XEISD_A3_EXPLICIT_CONDITION_MISMATCH": "CANNOT_SUPPORT_REQUESTED_CLAIM",
                },
            )
            self.assertTrue((output_dir / "report.md").is_file())
            self.assertTrue((output_dir / "routes/xeisd_a1/conclusion_packet.json").is_file())
            self.assertTrue((output_dir / "routes/xeisd_a2/conclusion_packet.json").is_file())
            self.assertTrue((output_dir / "routes/xeisd_a3/conclusion_packet.json").is_file())
            self.assertTrue((output_dir / "routes/hsp90_b1/conclusion_packet.json").is_file())
            self.assertTrue(
                (output_dir / "routes/hsp90_b1/operator_outputs/results_summary.json").is_file()
            )

            hsp90_receipt = read_json(output_dir / "routes/hsp90_b1/operator_run_receipt.json")
            hsp90_evidence = read_json(output_dir / "routes/hsp90_b1/evidence_result.json")
            self.assertEqual(hsp90_receipt["output_directory"], "routes/hsp90_b1/operator_outputs")
            self.assertEqual(hsp90_evidence["contract_status"], "PASS")
            self.assertEqual(
                hsp90_evidence["scientific_evaluation_status"], "PENDING_HUMAN_VALIDATION"
            )
            hsp90_stage2 = read_json(
                output_dir / "stage2/hsp90_b1_operator_contract_stage2_conclusion_packet.json"
            )
            self.assertEqual(hsp90_stage2["route_artifact"]["path"], "routes/hsp90_b1/conclusion_packet.json")
            self.assertEqual(hsp90_stage2["terminal_disposition"], "ABSTAIN_OR_HUMAN_REVIEW")

    def test_manifest_records_local_only_execution_and_frozen_input_identity(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            self.assertEqual(main(["run-demo", "--output-dir", str(output_dir)]), 0)
            manifest = read_json(output_dir / "run_manifest.json")

            self.assertFalse(manifest["network_accessed"])
            self.assertEqual(manifest["model_calls"], 0)
            self.assertEqual(manifest["credential_reads"], 0)
            self.assertEqual(manifest["external_spend"], 0)
            self.assertEqual(
                manifest["scientific_disposition"], "NOT_EVALUATED"
            )
            self.assertEqual(
                manifest["input_identities"]["xeisd_exact_review_derivative"]["sha256"],
                "fa5e3c99adadb18b6387c774dd1bd9d8b6f82663d4f3f6b63acfd3ad88829c99",
            )
            self.assertEqual(
                manifest["input_identities"]["hsp90_manifest_receipt"]["manifest_id"],
                "hsp90-directional-time-anatomy-inputs/v1-alpha",
            )

    def test_nonempty_output_directory_is_rejected_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "output"
            output_dir.mkdir()
            sentinel = output_dir / "keep.txt"
            sentinel.write_text("preserve this", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY"):
                main(["run-demo", "--output-dir", str(output_dir)])
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve this")
            self.assertFalse((output_dir / "run_summary.json").exists())

    def test_mutated_hash_bound_lookup_fixture_fails_in_an_isolated_checkout(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            checkout = Path(temporary_directory) / "checkout"
            shutil.copytree(
                REPO_ROOT,
                checkout,
                ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv", "*.pyc"),
            )
            fixture = (
                checkout
                / "evidence/real_case_vertical_slice_v1/frozen_inputs/xeisd"
                / "exact_review_derivative_excerpt_v1.json"
            )
            fixture.write_text(fixture.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            environment = dict(os.environ)
            environment["PYTHONPATH"] = str(checkout / "src")
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "dynamics_atlas_harness",
                    "run-demo",
                    "--output-dir",
                    str(checkout / "demo-output"),
                ],
                cwd=checkout,
                env=environment,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("X_EISD_REFERENCE_LOOKUP_FAILED", completed.stderr)
            self.assertIn("FIXTURE_HASH_MISMATCH", completed.stderr)


if __name__ == "__main__":
    unittest.main()
