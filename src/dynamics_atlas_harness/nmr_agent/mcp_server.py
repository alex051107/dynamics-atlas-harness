"""Stdio MCP server exposing the NMR analysis tools to a headless Claude Code session.

The same harness logic as the OpenRouter loop applies: tools act only on the sanitized
workspace, every call is logged with its purpose/expectation, research state is kept by
the harness, and (arm C) reflection checkpoints are attached to tool results and enforced.

Usage (from an MCP config):  python -m dynamics_atlas_harness.nmr_agent.mcp_server
    --workspace WS --run-dir RUN --arm C [--block-bmrb 52021,52023]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path

import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server

from .agent import Agent, RunConfig
from .tools import ANALYSIS_TOOLS


def build(ws: Path, run_dir: Path, arm: str, blocked: tuple[str, ...], result_chars: int, max_calls: int) -> Server:
    agent = Agent(ws, run_dir, RunConfig(arm=arm), blocked_bmrb=blocked)
    server = Server("nmr")
    counter = {"n": 0}
    call_lock = asyncio.Lock()

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [types.Tool(name=s["function"]["name"], description=s["function"]["description"],
                           inputSchema=s["function"]["parameters"]) for s in agent.specs]

    async def execute_call(name: str, arguments: dict) -> list[types.TextContent]:
        counter["n"] += 1
        t1 = time.time()
        over = counter["n"] > max_calls and name not in ("finish", "update_research_state", "propose_experiment")
        if over:
            result, is_err = {"error": "Tool-call budget exhausted. Call finish with your report now."}, True
        else:
            result, is_err = await asyncio.to_thread(agent._execute, name, arguments or {})
        if name in ANALYSIS_TOOLS and not is_err:
            agent.analysis_since_reflect += 1
        reason = agent._checkpoint_reason(name, result, is_err)
        full = json.dumps(result, ensure_ascii=False, default=str)
        text = full if len(full) <= result_chars else full[:result_chars] + f"... [truncated {len(full) - result_chars} chars]"
        if reason:
            agent.reflection_pending = True
            text += f"\n\nREFLECTION CHECKPOINT ({reason}). Your next call must be reflect."
        if counter["n"] == int(0.85 * max_calls):
            text += f"\n\nBudget note: {counter['n']} of {max_calls} tool calls used. Plan to finish soon."
        if name == "finish":
            text += "\n\nReport recorded. The analysis is closed; reply with the single word DONE."
        agent.log.write(json.dumps({"call": counter["n"], "tool": name, "args": arguments, "error": is_err,
                                    "checkpoint": reason, "seconds": round(time.time() - t1, 2),
                                    "result": result}, ensure_ascii=False, default=str) + "\n")
        agent.log.flush()
        (run_dir / "research_state.json").write_text(agent.state.render())
        (run_dir / "reflections.json").write_text(json.dumps(agent.state.reflections, indent=1, ensure_ascii=False))
        if agent.final_report is not None:
            (run_dir / "REPORT.md").write_text(agent.final_report)
        return [types.TextContent(type="text", text=text)]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        # Counters, reflection and research state belong to a single ordered run.
        async with call_lock:
            return await execute_call(name, arguments)

    return server


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--run-dir", required=True, type=Path)
    ap.add_argument("--arm", default="C", choices=["A", "B", "C", "C2", "W"])
    ap.add_argument("--block-bmrb", default="")
    ap.add_argument("--result-chars", type=int, default=6000)
    ap.add_argument("--max-calls", type=int, default=70)
    a = ap.parse_args()
    a.run_dir.mkdir(parents=True, exist_ok=True)
    server = build(a.workspace.resolve(), a.run_dir.resolve(), a.arm,
                   tuple(x for x in a.block_bmrb.split(",") if x), a.result_chars, a.max_calls)

    async def run() -> None:
        async with stdio_server() as (r, w):
            await server.run(r, w, server.create_initialization_options())

    asyncio.run(run())


if __name__ == "__main__":
    main()
