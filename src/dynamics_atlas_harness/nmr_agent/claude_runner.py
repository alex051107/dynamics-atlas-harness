"""Run one solver session with headless Claude Code, using only the NMR MCP tools.

Isolation: all built-in tools disabled (no file, shell or web access), no settings
sources (no CLAUDE.md, memory or hooks), skills disabled, only the `nmr` MCP server,
neutral empty working directory. The transcript (stream-json) is kept; the model id and
notional cost are read from it.
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

from . import remote_tools
from .prompts import WORKFLOW_ENV, system_prompt, workflow_file_info

TOOL_NOTE = ("\n\nYour tools come from the MCP server 'nmr' (names appear as mcp__nmr__<tool>). "
             "You have no other file, shell or web access.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--run-dir", required=True, type=Path)
    ap.add_argument("--arm", default="C", choices=["A", "B", "C", "C2", "W", "S"])
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--block-bmrb", default="")
    ap.add_argument("--max-calls", type=int, default=70)
    ap.add_argument("--prompt-file", type=Path, help="Frozen experimental system prompt override")
    ap.add_argument("--timeout-s", type=int, default=3600)
    ap.add_argument("--cwd", type=Path, default=Path("/tmp/nmr_solver"))
    ap.add_argument("--claude-bin", default=os.environ.get("CLAUDE_BIN") or str(Path.home() / "Library/Application Support/Claude/claude-code/2.1.281/claude.app/Contents/MacOS/claude"))
    a = ap.parse_args()
    run = a.run_dir.resolve()
    if (run / "transcript.jsonl").exists():
        raise FileExistsError("run directory already contains a transcript; choose a new run identity")
    run.mkdir(parents=True, exist_ok=True)
    cwd = a.cwd / run.name
    cwd.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parents[2]
    wf_info = workflow_file_info() if a.arm in ("W", "S") and not a.prompt_file else {}
    remote = remote_tools.enabled()  # REMOTE_TOOLS=1: tool server runs on Longleaf (default: local)
    if remote:
        remote_tools.prepare(a.workspace.resolve(), run, os.environ.get(WORKFLOW_ENV, ""))
    mcp_cfg = {"mcpServers": {"nmr": {"command": sys.executable, "args": [
        "-m", "dynamics_atlas_harness.nmr_agent.mcp_server", "--workspace", str(a.workspace.resolve()),
        "--run-dir", str(run), "--arm", a.arm, "--block-bmrb", a.block_bmrb, "--max-calls", str(a.max_calls)],
        "env": {"PYTHONPATH": str(src), "PYTHONWARNINGS": "ignore", "DYNAMICS_ATLAS_POTENCI": os.environ.get("DYNAMICS_ATLAS_POTENCI", ""), WORKFLOW_ENV: os.environ.get(WORKFLOW_ENV, ""), "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2", "MKL_NUM_THREADS": "2", "VECLIB_MAXIMUM_THREADS": "2"}}}}
    if remote:
        mcp_cfg = {"mcpServers": {"nmr": remote_tools.server_entry(a.workspace.resolve(), run, a.arm, a.block_bmrb, a.max_calls)}}
    (run / "mcp_config.json").write_text(json.dumps(mcp_cfg, indent=1))
    sp = (a.prompt_file.read_text() if a.prompt_file else system_prompt(a.arm)) + TOOL_NOTE
    (run / "system_prompt.txt").write_text(sp)
    task = (a.workspace / "TASK.md").read_text() + "\n\nStart by calling inventory. Work until you can answer the questions, then call finish."
    (run / "user_prompt.txt").write_text(task)
    cmd = [a.claude_bin, "-p", task, "--model", a.model, "--tools", "", "--setting-sources", "", "--disable-slash-commands",
           "--strict-mcp-config", "--mcp-config", str(run / "mcp_config.json"), "--allowedTools", "mcp__nmr",
           "--system-prompt-file", str(run / "system_prompt.txt"), "--no-session-persistence",
           "--output-format", "stream-json", "--verbose"]
    t0 = time.time()
    timed_out = False
    with (run / "transcript.jsonl").open("w") as out, (run / "stderr.txt").open("w") as err:
        cenv = {**os.environ, "MCP_TIMEOUT": remote_tools.MCP_STARTUP_TIMEOUT_MS} if remote else None
        proc = subprocess.Popen(cmd, cwd=cwd, stdout=out, stderr=err, stdin=subprocess.DEVNULL, start_new_session=True, env=cenv)
        try:
            rc = proc.wait(timeout=a.timeout_s)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                rc = proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                rc = proc.wait()
    pull_rc = remote_tools.pull(run) if remote else None  # bring observations/fits/REPORT back before counting
    models, cost, turns, result = set(), None, None, None
    for line in (run / "transcript.jsonl").read_text().splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "assistant":
            m = d.get("message", {}).get("model")
            if m:
                models.add(m)
        if d.get("type") == "result":
            cost, turns, result = d.get("total_cost_usd"), d.get("num_turns"), d.get("subtype")
            (run / "result_usage.json").write_text(json.dumps({k: d.get(k) for k in ("usage", "modelUsage", "total_cost_usd", "num_turns", "duration_ms")}, indent=1))
    n_calls = sum(1 for _ in (run / "actions.jsonl").open()) if (run / "actions.jsonl").exists() else 0
    summary = {"transport": "claude-code-headless (subscription)", "arm": a.arm, "model_requested": a.model,
               "models_returned": sorted(models), "notional_cost_usd": cost, "num_turns": turns, "tool_calls": n_calls,
               "result": result, "returncode": rc, "finished": (run / "REPORT.md").exists(),
               "seconds": round(time.time() - t0, 1), "claude_bin": a.claude_bin, "block_bmrb": a.block_bmrb, "max_calls": a.max_calls, "isolation_flags": cmd[3:]}
    summary["timed_out"] = timed_out
    summary.update(wf_info)
    summary["python"] = sys.executable
    if remote:
        nf = run / "remote_node.txt"
        summary["remote_tools"] = {"node_info": nf.read_text().strip() if nf.exists() else None, "sync_back_rc": pull_rc}
    (run / "summary.json").write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
