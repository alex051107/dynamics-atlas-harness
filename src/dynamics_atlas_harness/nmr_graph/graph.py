"""The LangGraph: analyze (create_agent tool loop) -> review -> conditional edge back to analyze."""

from __future__ import annotations

import json
import operator
from pathlib import Path
from typing import Annotated, Any, TypedDict

from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_core.messages import AnyMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

from .review import (collect_action_log, collect_fit_inventory, feedback_text, parse_verdict, read_report, review_messages)

MODEL_CALL_SLACK = 15


class GraphState(TypedDict, total=False):
    messages: Annotated[list[AnyMessage], add_messages]
    review_round: int                                   # number of returns to the analysis node so far
    review_feedback: Annotated[list[dict], operator.add]  # one entry per review call
    end_reason: str


def recursion_limit(max_tool_calls: int, max_review_rounds: int) -> int:
    per_round = 2 * (max_tool_calls + MODEL_CALL_SLACK)
    return per_round * (max_review_rounds + 1) + 50


def build_graph(model, tools: list, system_prompt: str, run_dir: Path, *, review_prompt: str | None = None,
                review_model=None, workspace: Path | None = None, max_review_rounds: int = 2,
                max_tool_calls: int = 70):
    """Compile the graph. `review_prompt=None` builds the analysis-only graph (no review node)."""
    run_dir = Path(run_dir)
    analyst = create_agent(
        model, tools=tools, system_prompt=system_prompt,
        middleware=[ModelCallLimitMiddleware(run_limit=max_tool_calls + MODEL_CALL_SLACK, exit_behavior="end")])
    g = StateGraph(GraphState)
    g.add_node("analyze", analyst)
    g.add_edge(START, "analyze")

    def report_for(state) -> str | None:
        return read_report(run_dir, state["messages"])

    def closing_reason(state, default: str) -> str:
        if report_for(state) is None:
            last = state["messages"][-1] if state["messages"] else None
            text = last.content if last is not None and isinstance(last.content, str) else ""
            return "model_call_limit" if text.startswith("Model call limits exceeded") else "ended_without_finish"
        return default

    if review_prompt is None:
        def close(state: GraphState) -> dict:
            return {"end_reason": closing_reason(state, "finished")}
        g.add_node("close", close)
        g.add_edge("analyze", "close")
        g.add_edge("close", END)
        return g.compile(checkpointer=InMemorySaver())

    rmodel = review_model or model

    async def review(state: GraphState) -> dict:
        report = report_for(state)
        if report is None:
            return {"end_reason": closing_reason(state, "ended_without_finish")}
        rnd = state.get("review_round", 0)
        inventory = collect_fit_inventory(run_dir, report, workspace)
        raw, error = "", None
        try:
            resp = await rmodel.ainvoke(review_messages(review_prompt, report, inventory, collect_action_log(run_dir)))
            raw = resp.content if isinstance(resp.content, str) else json.dumps(resp.content)
        except Exception as e:  # a failed review call must not discard the finished analysis
            error = f"{type(e).__name__}: {e}"
        verdict = parse_verdict(raw) if not error else None
        entry: dict[str, Any] = {"round": rnd + 1, "verdict": verdict["verdict"] if verdict else None,
                                 "findings": verdict["findings"] if verdict else [],
                                 "required_actions": verdict["required_actions"] if verdict else [],
                                 "inventory_summary": {k: inventory[k] for k in
                                                       ("n_fits", "uncited_fit_ids", "cited_but_missing", "flagged_fit_ids", "fits_by_data_type")},
                                 "raw_response": raw, "error": error}
        if verdict is None:
            entry["note"] = "review reply unusable; run closed without a return to analysis"
            return {"review_feedback": [entry], "end_reason": "review_unusable"}
        if verdict["verdict"] == "pass":
            return {"review_feedback": [entry], "end_reason": "review_passed"}
        if rnd >= max_review_rounds:
            return {"review_feedback": [entry], "end_reason": "review_round_limit"}
        return {"review_feedback": [entry], "review_round": rnd + 1, "end_reason": "",
                "messages": [HumanMessage(content=feedback_text(rnd + 1, max_review_rounds, verdict["required_actions"]))]}

    def route(state: GraphState) -> str:
        return "analyze" if not state.get("end_reason") else END

    g.add_node("review", review)
    g.add_edge("analyze", "review")
    g.add_conditional_edges("review", route, {"analyze": "analyze", END: END})
    return g.compile(checkpointer=InMemorySaver())
