import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from dynamics_atlas_harness import cli
from dynamics_atlas_harness import openrouter_profiler_sweep_v1 as older_live_profiler


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


if __name__ == "__main__":
    unittest.main()
