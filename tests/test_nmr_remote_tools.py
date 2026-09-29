"""REMOTE_TOOLS switch: default keeps the local stdio MCP server; =1 swaps in the ssh/Longleaf launch."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from dynamics_atlas_harness.nmr_agent import claude_runner, remote_tools


def run_runner(env: dict, tmp: Path):
    ws = tmp / "ws"
    ws.mkdir()
    (ws / "TASK.md").write_text("task")
    run = tmp / "runs" / "R1"
    argv = ["claude_runner", "--workspace", str(ws), "--run-dir", str(run), "--arm", "A", "--claude-bin", "/bin/true",
            "--cwd", str(tmp / "cwd"), "--max-calls", "8", "--block-bmrb", "1,2"]
    proc = MagicMock()
    proc.wait.return_value = 0
    with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv), \
            patch.object(claude_runner.subprocess, "Popen", return_value=proc) as popen, \
            patch.object(remote_tools, "prepare") as prep, patch.object(remote_tools, "pull", return_value=0) as pull:
        if "REMOTE_TOOLS" not in env:
            os.environ.pop("REMOTE_TOOLS", None)
        claude_runner.main()
    return json.loads((run / "mcp_config.json").read_text())["mcpServers"]["nmr"], popen, prep, pull, ws, run


class RemoteSwitch(unittest.TestCase):
    def test_default_is_local_and_unchanged(self):
        with tempfile.TemporaryDirectory() as d, patch("builtins.print"):
            nmr, popen, prep, pull, ws, run = run_runner({}, Path(d))
        self.assertEqual(nmr["command"], sys.executable)
        self.assertEqual(nmr["args"][:2], ["-m", "dynamics_atlas_harness.nmr_agent.mcp_server"])
        self.assertEqual(nmr["args"][nmr["args"].index("--workspace") + 1], str(ws.resolve()))
        self.assertEqual(nmr["args"][nmr["args"].index("--run-dir") + 1], str(run.resolve()))
        self.assertEqual(nmr["env"]["OMP_NUM_THREADS"], "2")
        self.assertEqual(sorted(nmr["env"]), sorted(["PYTHONPATH", "PYTHONWARNINGS", "DYNAMICS_ATLAS_POTENCI", "NMR_AGENT_WORKFLOW_FILE",
                                                     "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"]))
        prep.assert_not_called()
        pull.assert_not_called()
        self.assertIsNone(popen.call_args.kwargs.get("env"))

    def test_remote_zero_is_local(self):
        with tempfile.TemporaryDirectory() as d, patch("builtins.print"):
            nmr, _, prep, pull, *_ = run_runner({"REMOTE_TOOLS": "0"}, Path(d))
        self.assertEqual(nmr["command"], sys.executable)
        prep.assert_not_called()
        pull.assert_not_called()

    def test_remote_uses_ssh_and_remote_run_dir(self):
        with tempfile.TemporaryDirectory() as d, patch("builtins.print"):
            nmr, popen, prep, pull, ws, run = run_runner({"REMOTE_TOOLS": "1", "REMOTE_CORES": "4"}, Path(d))
        self.assertEqual(nmr["command"], "ssh")
        cmd = nmr["args"][-1]
        self.assertIn(f"{remote_tools.BASE}/runs/R1", cmd)
        self.assertIn(f"{remote_tools.BASE}/ws/ws", cmd)
        self.assertIn("remote_launch.sh 4 16G", cmd)
        self.assertNotIn(str(ws), cmd)
        prep.assert_called_once()
        pull.assert_called_once()
        self.assertEqual(popen.call_args.kwargs["env"]["MCP_TIMEOUT"], remote_tools.MCP_STARTUP_TIMEOUT_MS)


if __name__ == "__main__":
    unittest.main()
