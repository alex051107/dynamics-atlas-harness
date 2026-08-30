import json
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from dynamics_atlas_harness import cli
from dynamics_atlas_harness.openrouter_proposal_transport_v1 import canonical_json_sha256
from dynamics_atlas_harness import openrouter_profiler_sweep_v1 as older_live_profiler
from dynamics_atlas_harness import openrouter_proposal_transport_v1  # noqa: F401


REPO_ROOT = Path(__file__).resolve().parents[1]
HSP90_CASE_ID = "HSP90_NTD_EXPOSED_PAPER_BLIND_V1"


class CaseCliV1Tests(unittest.TestCase):
    def test_cli_import_and_parser_do_not_load_optional_case_runtime(self):
        script = r'''
import builtins
import sys

real_import = builtins.__import__
blocked_roots = {"numpy", "scipy", "pymbar"}
blocked_modules = {
    "case_runner_v1",
    "exposed_paper_blind_capsule_v1",
    "sampling_diagnostics_v1",
    "structural_state_projection_v1",
}

def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
    if name.split(".", 1)[0] in blocked_roots or name.split(".")[-1] in blocked_modules:
        raise AssertionError("optional case runtime imported during core CLI parsing: " + name)
    return real_import(name, globals, locals, fromlist, level)

builtins.__import__ = guarded_import
from dynamics_atlas_harness import cli
args = cli.build_parser().parse_args([
    "run-case",
    "--case-id",
    "HSP90_NTD_EXPOSED_PAPER_BLIND_V1",
    "--output-dir",
    "/tmp/not-executed",
])
assert args.handler.__name__ == "run_case"
assert "dynamics_atlas_harness.case_runner_v1" not in sys.modules
'''
        completed = subprocess.run(
            [sys.executable, "-c", script],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_recorded_run_case_never_reads_key_or_calls_older_live_transport(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "case-output"
            with (
                patch.object(
                    older_live_profiler,
                    "read_openrouter_api_key",
                    side_effect=AssertionError("credential reader must remain unused"),
                ) as key_reader,
                patch.object(
                    older_live_profiler.OpenRouterProfilerJsonClient,
                    "call",
                    side_effect=AssertionError("live transport must remain unused"),
                ) as transport,
            ):
                status = cli.main(
                    [
                        "run-case",
                        "--case-id",
                        HSP90_CASE_ID,
                        "--output-dir",
                        str(output_dir),
                    ]
                )

            self.assertEqual(status, 0)
            key_reader.assert_not_called()
            transport.assert_not_called()
            manifest = json.loads(
                (output_dir / "case_run_manifest_v1.json").read_text(encoding="utf-8")
            )
            self.assertFalse(manifest["network_accessed"])
            self.assertFalse(manifest["credentials_accessed"])
            self.assertEqual(
                manifest["proposal_provenance"]["profiler"]["mode"],
                "RECORDED_PROPOSAL_REPLAY",
            )

    def test_canonical_run_agent_case_is_recorded_and_no_network_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "canonical-recorded"
            status = cli.main(
                [
                    "run-agent-case",
                    "--case-id",
                    HSP90_CASE_ID,
                    "--output-dir",
                    str(output_dir),
                ]
            )
            manifest = json.loads(
                (output_dir / "case_run_manifest_v1.json").read_text(encoding="utf-8")
            )
        self.assertEqual(status, 0)
        self.assertEqual(manifest["agent_mode"], "RECORDED_OR_IN_MEMORY")
        self.assertFalse(manifest["network_accessed"])
        self.assertFalse(manifest["credentials_accessed"])
        self.assertFalse(manifest["external_model_transport"])

    def test_completed_campaign_live_cli_entries_refuse_before_credential_or_runtime(self):
        config_path = (
            REPO_ROOT
            / "agent_experiments/live_agent_common_flows_v1/config/live_agent_common_flows_v1.json"
        )
        config = json.loads(config_path.read_text(encoding="utf-8"))
        campaign_runtime = Mock(
            side_effect=AssertionError("live campaign runtime must remain unused")
        )
        fake_live_runtime = types.ModuleType(
            "dynamics_atlas_harness.live_agent_common_flows_v1"
        )
        fake_live_runtime.load_campaign_config = Mock(return_value=config)
        fake_live_runtime.require_live_agent_campaign_open = Mock(
            side_effect=ValueError(cli.LIVE_AGENT_CAMPAIGN_CLOSED_ERROR)
        )
        fake_live_runtime._model_entry = Mock()
        fake_live_runtime.run_live_agent_case = Mock(
            side_effect=AssertionError("live case runtime must remain unused")
        )
        fake_live_runtime.run_live_agent_campaign = campaign_runtime
        live_entry_points = (
            [
                "run-agent-case",
                "--case-id",
                HSP90_CASE_ID,
                "--output-dir",
                "/tmp/closed-live-agent-case-not-created",
                "--agent-mode",
                "live-openrouter",
            ],
            [
                "run-agent-campaign",
                "--output-dir",
                "/tmp/closed-live-agent-campaign-not-created",
            ],
        )
        with (
            patch.dict(
                sys.modules,
                {
                    "dynamics_atlas_harness.live_agent_common_flows_v1": fake_live_runtime
                },
            ),
            patch(
                "dynamics_atlas_harness.openrouter_proposal_transport_v1.read_openrouter_credential",
                side_effect=AssertionError("credential reader must remain unused"),
            ) as credential_reader,
            patch.object(
                cli,
                "_open_live_agent_campaign_budget",
                side_effect=AssertionError("budget ledger must remain unopened"),
            ) as budget_opener,
        ):
            for argv in live_entry_points:
                with self.subTest(command=argv[0]):
                    with self.assertRaises(ValueError) as caught:
                        cli.main(argv)
                    self.assertEqual(
                        str(caught.exception),
                        cli.LIVE_AGENT_CAMPAIGN_CLOSED_ERROR,
                    )

        credential_reader.assert_not_called()
        budget_opener.assert_not_called()
        campaign_runtime.assert_not_called()
        self.assertEqual(
            fake_live_runtime.require_live_agent_campaign_open.call_count, 2
        )

    def test_closed_campaign_config_is_bound_to_completion_receipt(self):
        config_path = (
            REPO_ROOT
            / "agent_experiments/live_agent_common_flows_v1/config/live_agent_common_flows_v1.json"
        )
        config = json.loads(config_path.read_text(encoding="utf-8"))
        receipt_path = REPO_ROOT / config["completion_receipt_path"]
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))

        self.assertEqual(
            config["execution_status"],
            cli.LIVE_AGENT_CAMPAIGN_CLOSED_STATUS,
        )
        self.assertEqual(config["planner_schema_repairs_used"], 1)
        self.assertEqual(config["prompt_repairs_used"], 1)
        self.assertIn(
            "DETERMINISTIC_VALIDATE_PLANNER_PROPOSAL_PRESERVES_SELECT_OR_ABSTAIN_SEMANTICS",
            config["planner_schema_repair_description"],
        )
        self.assertEqual(receipt["campaign_id"], config["campaign_id"])
        self.assertEqual(receipt["campaign_state"], cli.LIVE_AGENT_CAMPAIGN_CLOSED_STATUS)
        self.assertEqual(
            receipt["maximum_authorized_completed_calls"],
            config["max_completed_calls"],
        )
        self.assertLessEqual(
            receipt["completed_api_calls"],
            receipt["maximum_authorized_completed_calls"],
        )
        self.assertEqual(
            receipt["maximum_authorized_cost_usd"],
            config["budget_usd"],
        )
        self.assertEqual(
            canonical_json_sha256(receipt),
            config["completion_receipt_sha256"],
        )
        self.assertTrue(config["budget_ledger_path"].startswith("local/"))


if __name__ == "__main__":
    unittest.main()
