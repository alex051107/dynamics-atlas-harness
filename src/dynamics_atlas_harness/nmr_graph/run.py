"""Run one NMR analysis through the LangGraph framework.

python -m dynamics_atlas_harness.nmr_graph.run --workspace WS --run-dir RUN --config CONFIG.yaml [--max-calls N]

The API key is read from the environment variable named in the config (run under `with-deepseek`); it is
never written to disk. Run directory: the NMR tool server's own files (REPORT.md, actions.jsonl, fits/,
observations/, research_state.json) plus system_prompt.txt, user_prompt.txt, config_resolved.json,
messages.json, review_log.json, consult_log.jsonl, model_usage.jsonl and summary.json.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, messages_to_dict
from langchain_core.tools import StructuredTool

from ..nmr_agent.prompts import system_prompt as nmr_base_prompt
from .config import GraphConfig, config_dict, file_hashes, load_config
from .consult import make_consult_tools
from .graph import build_graph, recursion_limit
from .usage import UsageTracker

CONSULT_HINT = ("\n\nA file of method experience (consult_methods) and a file of stuck-point cases (consult_cases) "
                "are available to query.")
TOOL_NOTE = "\n\nYour NMR tools come from the MCP server 'nmr'. You have no other file, shell or web access."


def build_system_prompt(cfg: GraphConfig) -> str:
    parts = [nmr_base_prompt(cfg.arm)] if cfg.include_base_prompt else []
    for p in cfg.prompt_files:
        parts.append(Path(p).read_text().strip())      # a missing layer file fails the run before any model call
    text = "\n\n".join(x for x in parts if x)
    if cfg.enable_consult_tools:
        text += CONSULT_HINT
    return text + TOOL_NOTE


def _text(content: Any) -> str:
    if isinstance(content, str):
        return content
    return "".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content or [])


def as_text_tool(t) -> StructuredTool:
    """MCP adapter tools return a list of content blocks; the chat endpoint wants tool messages as plain strings."""
    async def run(**kwargs):
        out = await t.coroutine(**kwargs)
        return _text(out[0] if isinstance(out, tuple) else out)
    return StructuredTool(name=t.name, description=t.description, args_schema=t.args_schema,
                          coroutine=run, response_format="content")


def server_connection(cfg: GraphConfig, workspace: Path, run_dir: Path) -> dict[str, Any]:
    src = Path(__file__).resolve().parents[2]
    env = {"PYTHONPATH": str(src), "PYTHONWARNINGS": "ignore",
           "DYNAMICS_ATLAS_POTENCI": os.environ.get("DYNAMICS_ATLAS_POTENCI", ""),
           "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2", "MKL_NUM_THREADS": "2", "VECLIB_MAXIMUM_THREADS": "2"}
    return {"transport": "stdio", "command": sys.executable, "env": env, "args": [
        "-m", "dynamics_atlas_harness.nmr_agent.mcp_server", "--workspace", str(workspace), "--run-dir", str(run_dir),
        "--arm", cfg.arm, "--block-bmrb", ",".join(cfg.block_bmrb), "--result-chars", str(cfg.result_chars),
        "--max-calls", str(cfg.max_tool_calls)]}


def make_model(cfg: GraphConfig, tracker: UsageTracker):
    from langchain_openai import ChatOpenAI
    key = os.environ.get(cfg.api_key_env)
    if not key:
        raise RuntimeError(f"{cfg.api_key_env} is not set (run under with-deepseek)")
    kw: dict[str, Any] = {}
    if cfg.max_tokens:
        kw["max_tokens"] = cfg.max_tokens
    if cfg.temperature is not None:
        kw["temperature"] = cfg.temperature
    return ChatOpenAI(model=cfg.model, base_url=cfg.base_url, api_key=key, callbacks=[tracker],
                      max_retries=8, timeout=600, **kw)


async def run_graph(cfg: GraphConfig, workspace: Path, run_dir: Path, model, tracker: UsageTracker,
                    task_text: str | None = None, mcp_tools_override: list | None = None) -> dict[str, Any]:
    """Wire tools + prompts into the graph, run it, write the run-directory records. Returns summary dict."""
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain_mcp_adapters.tools import load_mcp_tools
    t0 = time.time()
    run_dir.mkdir(parents=True, exist_ok=True)
    if (run_dir / "summary.json").exists():
        raise FileExistsError("run directory already has a summary.json; choose a new run identity")
    sp = build_system_prompt(cfg)
    review_prompt = None
    if cfg.enable_review:
        if not cfg.review_prompt_file:
            raise ValueError("enable_review needs review_prompt_file")
        review_prompt = Path(cfg.review_prompt_file).read_text()
    task = task_text or ((workspace / "TASK.md").read_text()
                         + "\n\nStart by calling inventory. Work until you can answer the questions, then call finish.")
    (run_dir / "system_prompt.txt").write_text(sp)
    (run_dir / "user_prompt.txt").write_text(task)
    (run_dir / "config_resolved.json").write_text(json.dumps(config_dict(cfg), indent=1))
    consult_tools = (make_consult_tools(cfg.methods_file, cfg.cases_file, cfg.consult_top_k, cfg.consult_max_chars,
                                        run_dir / "consult_log.jsonl") if cfg.enable_consult_tools else [])
    result: dict[str, Any] = {}
    error = None

    async def go(nmr_tools: list) -> None:
        graph = build_graph(model, [*nmr_tools, *consult_tools], sp, run_dir, review_prompt=review_prompt,
                            workspace=workspace, max_review_rounds=cfg.max_review_rounds,
                            max_tool_calls=cfg.max_tool_calls)
        conf = {"configurable": {"thread_id": run_dir.name},
                "recursion_limit": recursion_limit(cfg.max_tool_calls, cfg.max_review_rounds)}
        result.update(await graph.ainvoke({"messages": [HumanMessage(content=task)], "review_round": 0}, conf))

    try:
        if mcp_tools_override is not None:
            await go(mcp_tools_override)
        else:
            client = MultiServerMCPClient({"nmr": server_connection(cfg, workspace, run_dir)})
            async with client.session("nmr") as session:      # one persistent server process for the whole run
                await go([as_text_tool(t) for t in await load_mcp_tools(session)])
    except Exception as e:
        error = f"{type(e).__name__}: {e}"
        leaves: list[str] = []

        def walk(x: BaseException) -> None:          # anyio TaskGroup wraps the real failure in an ExceptionGroup
            if isinstance(x, BaseExceptionGroup):
                for y in x.exceptions:
                    walk(y)
            else:
                leaves.append(f"{type(x).__name__}: {str(x)[:500]}")
        walk(e)
        if leaves and leaves != [error]:
            error += " | leaf: " + " ; ".join(leaves)
    msgs = result.get("messages", [])
    (run_dir / "messages.json").write_text(json.dumps(messages_to_dict(msgs), ensure_ascii=False, indent=1, default=str))
    reviews = result.get("review_feedback", [])
    (run_dir / "review_log.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=1))
    with (run_dir / "model_usage.jsonl").open("w") as f:
        for c in tracker.calls:
            f.write(json.dumps(c) + "\n")
    n_tool_calls = sum(1 for _ in (run_dir / "actions.jsonl").open()) if (run_dir / "actions.jsonl").exists() else 0
    summary = {"config": cfg.name, "arm": cfg.arm, "model_requested": cfg.model, "base_url": cfg.base_url,
               **tracker.summary(), "review_enabled": cfg.enable_review, "review_rounds": result.get("review_round", 0),
               "review_calls": len(reviews), "end_reason": "error" if error else result.get("end_reason"),
               "error": error, "finished": (run_dir / "REPORT.md").exists(), "nmr_tool_calls": n_tool_calls,
               "max_tool_calls": cfg.max_tool_calls, "seconds": round(time.time() - t0, 1),
               "files_sha256": file_hashes(cfg), "python": sys.executable}
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=1))
    return summary


def main() -> None:
    ap = argparse.ArgumentParser(description="Run the NMR analysis LangGraph on a sanitized workspace.")
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--run-dir", required=True, type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--max-calls", type=int, help="override max_tool_calls of the config")
    ap.add_argument("--block-bmrb", help="comma-separated BMRB ids withheld from the solver (override)")
    a = ap.parse_args()
    cfg = load_config(a.config)
    if a.max_calls is not None:
        cfg.max_tool_calls = a.max_calls
    if a.block_bmrb is not None:
        cfg.block_bmrb = [x for x in a.block_bmrb.split(",") if x]
    tracker = UsageTracker()
    summary = asyncio.run(run_graph(cfg, a.workspace.resolve(), a.run_dir.resolve(), make_model(cfg, tracker), tracker))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
