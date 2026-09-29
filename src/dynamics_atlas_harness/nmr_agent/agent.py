"""The analysis loop: model proposes a tool call -> harness executes it on real data ->
result (and, in arm C, a reflection checkpoint) goes back -> repeat until finish or budget.

Transport: OpenRouter chat completions with native tool calling. The returned model id,
provider, token usage and cost of every call are logged. Credentials come from the
environment (see `with-openrouter`); nothing is written to disk.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import traceback
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .prompts import (FINISH_GATE_INSTRUCTION, REFLECT_TOOL, WORKFLOW_CHECKPOINT_FULL, WORKFLOW_CHECKPOINT_REMINDER,
                      system_prompt, workflow_file)
from .tools import ANALYSIS_TOOLS, ToolBox, tool_specs

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


@dataclass
class RunConfig:
    arm: str = "C"
    model: str = "anthropic/claude-opus-5.5"
    max_turns: int = 40
    max_cost_usd: float = 1.0
    max_tokens: int = 6000
    tool_result_chars: int = 4000
    keep_recent_tool_results: int = 8
    trim_threshold_chars: int = 60000
    reflect_every: int = 4          # arm C: periodic checkpoint after this many analysis actions
    temperature: float | None = None


@dataclass
class ResearchState:
    facts: list[str] = field(default_factory=list)
    hypotheses: dict[str, dict[str, Any]] = field(default_factory=dict)
    open_questions: list[str] = field(default_factory=list)
    plan: list[str] = field(default_factory=list)
    retracted: list[str] = field(default_factory=list)
    proposed_experiments: list[dict[str, str]] = field(default_factory=list)
    reflections: list[dict[str, Any]] = field(default_factory=list)

    def update(self, args: dict[str, Any]) -> dict[str, Any]:
        for f in args.get("facts", []) or []:
            if f not in self.facts:
                self.facts.append(f)
        for h in args.get("hypotheses", []) or []:
            hid = h.get("id") or f"H{len(self.hypotheses) + 1}"
            cur = self.hypotheses.setdefault(hid, {"statement": "", "status": "open", "for": [], "against": []})
            for k in ("statement", "status"):
                if h.get(k):
                    cur[k] = h[k]
            for k in ("for", "against"):
                for item in h.get(k, []) or []:
                    if item not in cur[k]:
                        cur[k].append(item)
        if args.get("open_questions") is not None:
            self.open_questions = list(args["open_questions"])
        if args.get("plan") is not None:
            self.plan = list(args["plan"])
        for r in args.get("retracted", []) or []:
            self.retracted.append(r)
        return {"ok": True, "n_facts": len(self.facts), "hypotheses": {k: v["status"] for k, v in self.hypotheses.items()}}

    def render(self) -> str:
        return json.dumps({"facts": self.facts, "hypotheses": self.hypotheses, "open_questions": self.open_questions,
                           "plan": self.plan, "retracted": self.retracted,
                           "proposed_experiments": self.proposed_experiments}, ensure_ascii=False, indent=1)


def call_openrouter(messages: list[dict[str, Any]], tools: list[dict[str, Any]], cfg: RunConfig) -> dict[str, Any]:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY not set (run under with-openrouter)")
    body: dict[str, Any] = {"model": cfg.model, "messages": messages, "tools": tools, "max_tokens": cfg.max_tokens,
                            "usage": {"include": True}}
    if cfg.temperature is not None:
        body["temperature"] = cfg.temperature
    req = urllib.request.Request(OPENROUTER_URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                          "X-Title": "dynamics-atlas-nmr-agent-v0"})
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read()[:500]!r}"
            if e.code in (400, 401, 402, 403):
                break
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = repr(e)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"OpenRouter call failed: {last_err}")


def _cache_mark(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Copy messages, marking the system prompt and the last message as Anthropic cache breakpoints."""
    out = []
    for i, m in enumerate(messages):
        m2 = dict(m)
        if (i == 0 or i == len(messages) - 1) and isinstance(m2.get("content"), str) and m2["role"] in ("system", "user", "tool"):
            m2["content"] = [{"type": "text", "text": m2["content"], "cache_control": {"type": "ephemeral"}}]
        out.append(m2)
    return out


class Agent:
    def __init__(self, workspace: Path, run_dir: Path, cfg: RunConfig, blocked_bmrb: tuple[str, ...] = ()):
        self.ws = workspace
        self.run_dir = run_dir
        self.cfg = cfg
        run_dir.mkdir(parents=True, exist_ok=True)
        if cfg.arm == "S":
            workflow_file()     # fail before the run starts if the checkpoint workflow is missing
        self.tools = ToolBox(workspace, run_dir, blocked_bmrb_ids=blocked_bmrb, per_experiment_chi2=(cfg.arm == "S"))
        policy_path = workspace / "tool_policy.json"
        policy = json.loads(policy_path.read_text()) if policy_path.exists() else {}
        self.tools.allow_bmrb = policy.get("allow_network_bmrb", True)
        self.state = ResearchState()
        self.specs = tool_specs() + ([REFLECT_TOOL] if cfg.arm.startswith("C") or cfg.arm == "S" else [])
        if policy.get("allowed_tools") is not None:
            self.specs = [s for s in self.specs if s["function"]["name"] in policy["allowed_tools"]]
        self.allowed_tools = {s["function"]["name"] for s in self.specs}
        self.observation_dir = run_dir / "observations"
        self.observation_dir.mkdir(exist_ok=True)
        self.observation_n = max((int(p.stem[1:]) for p in self.observation_dir.glob("O*.json")), default=0)
        self.messages: list[dict[str, Any]] = [
            {"role": "system", "content": system_prompt(cfg.arm)},
            {"role": "user", "content": (workspace / "TASK.md").read_text()
             + "\n\nStart by calling inventory. Work until you can answer the questions, then call finish."},
        ]
        self.cost = 0.0
        self.turn = 0
        self.resumed_from = None
        self.analysis_since_reflect = 0
        self.reflection_pending = False
        self.final_report: str | None = None
        self._workflow_flag = run_dir / "workflow_attached.flag"     # arm S: full workflow already shown at a checkpoint
        self._finish_gate_file = run_dir / "finish_checklist.json"   # arm S: first finish call already answered with a checklist
        if (run_dir / "messages.json").exists():
            self._resume()
        self.log = (run_dir / "actions.jsonl").open("a")
        self.calls = (run_dir / "model_calls.jsonl").open("a")

    # ------------------------------------------------------------------
    def _resume(self) -> None:
        """Continue a stopped run from its saved messages, research state and cost."""
        self.messages = json.loads((self.run_dir / "messages.json").read_text())
        st = json.loads((self.run_dir / "research_state.json").read_text())
        for k in ("facts", "hypotheses", "open_questions", "plan", "retracted", "proposed_experiments"):
            setattr(self.state, k, st.get(k, getattr(self.state, k)))
        if (self.run_dir / "reflections.json").exists():
            self.state.reflections = json.loads((self.run_dir / "reflections.json").read_text())
        prev = json.loads((self.run_dir / "summary.json").read_text())
        self.cost = float(prev.get("cost_usd", 0.0))
        self.turn = int(prev.get("turns", 0))
        self.resumed_from = prev
        # a dangling assistant tool call without results cannot be sent back; drop it
        while self.messages and self.messages[-1]["role"] == "assistant" and self.messages[-1].get("tool_calls"):
            self.messages.pop()
        note = (self.run_dir / "operator_note.txt")
        if note.exists():
            self.messages.append({"role": "user", "content": note.read_text()})

    def _trim(self) -> None:
        """Trim old tool outputs in one batch once they exceed a size budget.

        Rewriting history invalidates the prompt cache from that point on, so trimming happens
        rarely and all at once instead of one message per turn.
        """
        idx = [i for i, m in enumerate(self.messages) if m["role"] == "tool"
               and isinstance(m["content"], str) and not m["content"].startswith("[trimmed")]
        live = sum(len(self.messages[i]["content"]) for i in idx)
        if live <= self.cfg.trim_threshold_chars:
            return
        for i in idx[:-self.cfg.keep_recent_tool_results]:
            import re
            match = re.search(r'"observation_id"\s*:\s*"(O\d{6})"', self.messages[i]["content"])
            source = f"read_result(observation_id='{match.group(1)}')" if match else "legacy run logs (no observation id)"
            self.messages[i]["content"] = f"[trimmed: older tool output; full text retained. Retrieve via {source}.]"
        self.messages.append({"role": "user", "content": "Context note: older tool outputs were trimmed. Current research state:\n" + self.state.render()})

    def _execute(self, name: str, args: dict[str, Any]) -> tuple[Any, bool]:
        if name not in self.allowed_tools:
            result, is_err = {"error": "tool not allowed by this run's policy"}, True
        else:
            result, is_err = self._execute_impl(name, args)
        self.observation_n += 1
        oid = f"O{self.observation_n:06d}"
        result = {"observation_id": oid, **(result if isinstance(result, dict) else {"value": result})}
        (self.observation_dir / (oid + ".json")).write_text(json.dumps(
            {"tool": name, "args": args, "error": is_err, "result": result}, ensure_ascii=False, default=str))
        return result, is_err

    def _execute_impl(self, name: str, args: dict[str, Any]) -> tuple[Any, bool]:
        if name == "get_research_state":
            return {"origin": "model_authored_notes", "state": json.loads(self.state.render())}, False
        if self.reflection_pending and name != "reflect" and name in ANALYSIS_TOOLS:
            return {"error": "REFLECTION CHECKPOINT pending: call reflect before the next analysis."}, True
        if name == "reflect":
            self.state.reflections.append(args | {"turn": self.turn})
            self.reflection_pending = False
            self.analysis_since_reflect = 0
            return {"ok": True, "recorded": True}, False
        if name == "update_research_state":
            return self.state.update(args), False
        if name == "propose_experiment":
            self.state.proposed_experiments.append(args)
            return {"ok": True, "n_proposed": len(self.state.proposed_experiments)}, False
        if name == "finish":
            if self.cfg.arm == "S" and not self._finish_gate_file.exists():
                return self._finish_gate(), False
            from .atlas_candidate import validate
            problems = validate(args.get("atlas_entries"), self.observation_dir)
            if not isinstance(args.get("report"), str) or not args["report"].strip():
                problems.append("report must not be empty")
            if problems:
                return {"error": "incomplete candidate record", "problems": problems}, True
            self.final_report = args.get("report", "")
            self.atlas_entries = args.get("atlas_entries")
            (self.run_dir / "ATLAS_ENTRIES.json").write_text(json.dumps(self.atlas_entries, indent=1, ensure_ascii=False))
            (self.run_dir / "ATLAS_VALIDATION.json").write_text(json.dumps({
                "shape_and_links_checked": True, "domain_review": "pending", "status": "candidate_only",
                "database_import_performed": False,
                "limit": "Observation existence does not establish that a scientific claim follows from it; Gina must review."}, indent=2))
            return {"ok": True}, False
        fn = getattr(self.tools, name, None)
        if fn is None or name.startswith("_"):
            return {"error": f"unknown tool {name}"}, True
        try:
            return fn(**args), False
        except Exception as e:  # tool errors go back to the model as observations
            return {"error": f"{type(e).__name__}: {e}"}, True

    def _finish_gate(self) -> dict[str, Any]:
        """Arm S: the first finish call returns a checklist instead of closing the run. No judgement of content."""
        flagged = [{"fit_id": fid, "flags": list(fit["flags"])} for fid, fit in sorted(self.tools.fits.items())
                   if isinstance(fit, dict) and fit.get("flags")]
        kept = [{"reflection_no": i + 1, "turn": r.get("turn"), "discrepancy": r.get("discrepancy"), "next_action": r.get("next_action")}
                for i, r in enumerate(self.state.reflections)
                if r.get("decision") == "keep_plan"
                and str(r.get("discrepancy", "")).strip().rstrip(".").strip().lower() not in ("", "none")]
        gate = {"finish_check": FINISH_GATE_INSTRUCTION, "fits_with_flags": flagged, "kept_plan_despite_discrepancy": kept}
        self._finish_gate_file.write_text(json.dumps(gate, indent=1, ensure_ascii=False))
        return gate

    def checkpoint_suffix(self, reason: str) -> str:
        """Text appended to a tool result that opens a reflection checkpoint (arm S also attaches the workflow)."""
        text = f"\n\nREFLECTION CHECKPOINT ({reason}). Your next call must be reflect."
        if self.cfg.arm == "S":
            if self._workflow_flag.exists():
                text += WORKFLOW_CHECKPOINT_REMINDER
            else:
                text += WORKFLOW_CHECKPOINT_FULL.format(text=workflow_file().read_text())
                self._workflow_flag.write_text("attached\n")
        return text

    def _checkpoint_reason(self, name: str, result: Any, is_err: bool) -> str | None:
        if not (self.cfg.arm.startswith("C") or self.cfg.arm == "S") or name not in ANALYSIS_TOOLS:
            return None
        if is_err:
            return "the tool returned an error"
        if isinstance(result, dict) and result.get("flags"):
            return "the fit raised flags: " + "; ".join(result["flags"])
        if self.analysis_since_reflect >= self.cfg.reflect_every:
            return f"{self.analysis_since_reflect} analyses since the last reflection"
        return None

    def run(self) -> dict[str, Any]:
        t0 = time.time()
        stop_reason = "max_turns"
        warned = False
        while self.turn < self.cfg.max_turns:
            (self.run_dir / "messages.json").write_text(json.dumps(self.messages, ensure_ascii=False))
            self.turn += 1
            if not warned and (self.cost > 0.8 * self.cfg.max_cost_usd or self.turn >= self.cfg.max_turns - 3):
                self.messages.append({"role": "user", "content": "Budget nearly exhausted. Finish the current step and call finish with your report now."})
                warned = True
            self._trim()
            try:
                resp = call_openrouter(_cache_mark(self.messages), self.specs, self.cfg)
            except Exception as e:
                stop_reason = f"transport_error: {e}"
                break
            usage = resp.get("usage", {}) or {}
            self.cost += float(usage.get("cost") or 0.0)
            choice = resp["choices"][0]
            msg = choice["message"]
            self.calls.write(json.dumps({"turn": self.turn, "model": resp.get("model"), "provider": resp.get("provider"),
                                         "usage": usage, "finish_reason": choice.get("finish_reason"),
                                         "content": msg.get("content"), "tool_calls": msg.get("tool_calls")}, ensure_ascii=False) + "\n")
            self.calls.flush()
            assistant = {"role": "assistant", "content": msg.get("content") or ""}
            if msg.get("tool_calls"):
                assistant["tool_calls"] = msg["tool_calls"]
            self.messages.append(assistant)
            if not msg.get("tool_calls"):
                self.messages.append({"role": "user", "content": "Continue by calling a tool (call finish when done)."})
                continue
            for tc in msg["tool_calls"]:
                name = tc["function"]["name"]
                try:
                    args = json.loads(tc["function"].get("arguments") or "{}")
                except json.JSONDecodeError:
                    args = {}
                t1 = time.time()
                result, is_err = self._execute(name, args)
                if name in ANALYSIS_TOOLS and not is_err:
                    self.analysis_since_reflect += 1
                reason = self._checkpoint_reason(name, result, is_err)
                text = json.dumps(result, ensure_ascii=False, default=str)
                full = text
                if len(text) > self.cfg.tool_result_chars:
                    text = text[: self.cfg.tool_result_chars] + f"... [truncated {len(full) - self.cfg.tool_result_chars} chars]"
                if reason:
                    self.reflection_pending = True
                    text += self.checkpoint_suffix(reason)
                self.messages.append({"role": "tool", "tool_call_id": tc["id"], "content": text})
                self.log.write(json.dumps({"turn": self.turn, "tool": name, "args": args, "error": is_err,
                                           "checkpoint": reason, "seconds": round(time.time() - t1, 2),
                                           "result": json.loads(full) if full.startswith("{") else full},
                                          ensure_ascii=False, default=str) + "\n")
                self.log.flush()
            (self.run_dir / "research_state.json").write_text(self.state.render())
            if self.final_report is not None:
                stop_reason = "finish"
                break
            if self.cost > self.cfg.max_cost_usd:
                stop_reason = "budget"
                break
        summary = {"resumed_from": self.resumed_from, "arm": self.cfg.arm, "model_requested": self.cfg.model, "turns": self.turn, "cost_usd": round(self.cost, 5),
                   "stop_reason": stop_reason, "seconds": round(time.time() - t0, 1),
                   "n_reflections": len(self.state.reflections), "finished": self.final_report is not None}
        (self.run_dir / "summary.json").write_text(json.dumps(summary, indent=1))
        (self.run_dir / "research_state.json").write_text(self.state.render())
        (self.run_dir / "reflections.json").write_text(json.dumps(self.state.reflections, indent=1, ensure_ascii=False))
        (self.run_dir / "messages.json").write_text(json.dumps(self.messages, indent=1, ensure_ascii=False))
        if self.final_report is not None:
            (self.run_dir / "REPORT.md").write_text(self.final_report)
        return summary


def main() -> None:
    ap = argparse.ArgumentParser(description="Run the NMR analysis agent on a sanitized workspace.")
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--run-dir", required=True, type=Path)
    ap.add_argument("--arm", default="C", choices=["A", "B", "C", "C2", "W", "S"])
    ap.add_argument("--model", default="anthropic/claude-opus-5.5")
    ap.add_argument("--max-turns", type=int, default=40)
    ap.add_argument("--max-cost", type=float, default=1.0)
    ap.add_argument("--block-bmrb", default="", help="comma-separated BMRB ids withheld from the solver")
    a = ap.parse_args()
    cfg = RunConfig(arm=a.arm, model=a.model, max_turns=a.max_turns, max_cost_usd=a.max_cost)
    agent = Agent(a.workspace, a.run_dir, cfg, blocked_bmrb=tuple(x for x in a.block_bmrb.split(",") if x))
    try:
        print(json.dumps(agent.run(), indent=1))
    except Exception:
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
