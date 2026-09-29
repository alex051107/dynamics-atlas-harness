"""Optional remote tool server: the agent (headless Claude Code) stays local, mcp_server.py runs on a Longleaf node.

Switch: env REMOTE_TOOLS=1 (default off = local stdio server, unchanged). The MCP config's command becomes an ssh
call whose stdio carries the MCP protocol to remote_launch.sh; the run directory lives on Longleaf during the run
and is rsynced back to the same local path afterwards. Code and workspaces are pushed beforehand with
nmr_agent_work/sync_agent_remote.sh.

Env knobs: REMOTE_CORES (default 8), REMOTE_MEM (default 16G), NMR_SERVE_NODE (mode b: ssh into a held node),
NMR_REMOTE_HOST (default `longleaf`).
"""

from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

HOST = os.environ.get("NMR_REMOTE_HOST", "longleaf")
BASE = os.environ.get("NMR_REMOTE_ROOT", "") + "/agent_remote"  # remote root must be set via NMR_REMOTE_ROOT
LAUNCH = f"{BASE}/src/dynamics_atlas_harness/nmr_agent/remote_launch.sh"
# Files the local runner writes itself; never overwritten by the sync back.
RUNNER_OWNED = ("transcript.jsonl", "stderr.txt", "mcp_config.json", "system_prompt.txt", "user_prompt.txt",
                "summary.json", "result_usage.json", "runner.log")
MCP_STARTUP_TIMEOUT_MS = "300000"  # srun may queue; Claude Code's default MCP startup timeout is 30 s


def enabled() -> bool:
    return os.environ.get("REMOTE_TOOLS") == "1"


def remote_run_dir(run: Path) -> str:
    return f"{BASE}/runs/{run.name}"


def prepare(ws: Path, run: Path, workflow_file: str = "") -> None:
    """Check the workspace was synced, the remote run dir is fresh, and put the workflow copy there."""
    rrun = remote_run_dir(run)
    q = shlex.quote
    p = subprocess.run(["ssh", "-o", "BatchMode=yes", HOST,
                        f"test -d {q(BASE + '/ws/' + ws.name)} && ! test -e {q(rrun + '/actions.jsonl')} && mkdir -p {q(rrun)}"],
                       capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError(f"remote prepare failed (workspace not synced, or remote run dir already used): {p.stderr.strip()}")
    if workflow_file:
        subprocess.run(["rsync", "-a", workflow_file, f"{HOST}:{rrun}/workflow_used.md"], check=True, timeout=120)


def server_entry(ws: Path, run: Path, arm: str, block_bmrb: str, max_calls: int) -> dict:
    cores = os.environ.get("REMOTE_CORES", "8")
    mem = os.environ.get("REMOTE_MEM", "16G")
    env = {"NMR_REMOTE_ROOT": os.environ.get("NMR_REMOTE_ROOT", ""), "NMR_REMOTE_RUN_DIR": remote_run_dir(run), "DYNAMICS_ATLAS_POTENCI": f"{BASE}/POTENCI/potenci.py3",
           "NMR_AGENT_WORKFLOW_FILE": f"{remote_run_dir(run)}/workflow_used.md" if os.environ.get("NMR_AGENT_WORKFLOW_FILE") else ""}
    if os.environ.get("NMR_SERVE_NODE"):
        env["NMR_SERVE_NODE"] = os.environ["NMR_SERVE_NODE"]
    args = ["--workspace", f"{BASE}/ws/{ws.name}", "--run-dir", remote_run_dir(run), "--arm", arm,
            "--block-bmrb", block_bmrb, "--max-calls", str(max_calls)]
    remote_cmd = "env " + " ".join(f"{k}={shlex.quote(v)}" for k, v in env.items()) + \
        f" bash {LAUNCH} {cores} {mem} " + " ".join(shlex.quote(a) for a in args)
    return {"command": "ssh", "args": ["-T", "-o", "BatchMode=yes", "-o", "ServerAliveInterval=30",
                                       "-o", "ServerAliveCountMax=6", HOST, remote_cmd]}


def pull(run: Path) -> int:
    ex = [f"--exclude={n}" for n in RUNNER_OWNED]
    p = subprocess.run(["rsync", "-a", *ex, f"{HOST}:{remote_run_dir(run)}/", f"{run}/"], capture_output=True, text=True, timeout=600)
    return p.returncode
