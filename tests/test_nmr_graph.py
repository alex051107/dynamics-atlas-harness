import asyncio
import json
import tempfile
import unittest
from pathlib import Path

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.tools import StructuredTool

from dynamics_atlas_harness.nmr_graph import consult, review
from dynamics_atlas_harness.nmr_graph.config import GraphConfig, load_config
from dynamics_atlas_harness.nmr_graph.run import build_system_prompt, run_graph
from dynamics_atlas_harness.nmr_graph.usage import UsageTracker

CONFIGS = Path(consult.__file__).parent / "configs"


class Scripted(BaseChatModel):
    """Replays a fixed list of AIMessages; records the messages it was shown."""
    script: list
    seen: list = []
    idx: int = 0

    @property
    def _llm_type(self) -> str:
        return "scripted"

    def bind_tools(self, tools, **kw):
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kw):
        self.seen.append(list(messages))
        m = self.script[min(self.idx, len(self.script) - 1)]
        self.idx += 1
        return ChatResult(generations=[ChatGeneration(message=m)])


def call(name, args, i):
    return AIMessage(content="", tool_calls=[{"name": name, "args": args, "id": f"c{name}{i}"}])


def fake_tools(run_dir: Path):
    def fit(experiments: list[str]) -> str:
        n = len(list((run_dir / "fits").glob("F*.json"))) + 1
        (run_dir / "fits").mkdir(exist_ok=True)
        (run_dir / "fits" / f"F{n}.json").write_text(json.dumps(
            {"fit_id": f"F{n}", "model": "two_state", "mode": "global", "experiments": experiments,
             "per_residue": {"A1": {}}, "flags": ["reduced chi2 too high"] if n == 2 else [], "reduced_chi2": 1.0}))
        return f"fit F{n}"

    def finish(report: str, atlas_entries: list) -> str:
        (run_dir / "REPORT.md").write_text(report)
        return "Report recorded. Reply DONE."
    return [StructuredTool.from_function(fit, name="fit_exchange", description="fit"),
            StructuredTool.from_function(finish, name="finish", description="finish")]


def analysis_script(reports: list[str], extra_first=()):
    s = [*extra_first, call("fit_exchange", {"experiments": ["cpmg_15N_600MHz"]}, 1), call("fit_exchange", {"experiments": ["cest_15N_B1_10Hz"]}, 2)]
    for i, r in enumerate(reports):
        s += [call("finish", {"report": r, "atlas_entries": []}, i), AIMessage(content="DONE")]
    return s


def verdict(v, actions=()):
    return AIMessage(content=json.dumps({"verdict": v, "findings": [], "required_actions": list(actions)}))


class GraphRuns(unittest.TestCase):
    def run_it(self, cfg, analysis, reviewer=None, tools_extra=()):
        d = Path(tempfile.mkdtemp())
        ws = d / "ws"
        ws.mkdir()
        (ws / "TASK.md").write_text("task")
        run = d / "run"
        run.mkdir()
        tracker = UsageTracker()
        model = Scripted(script=analysis, seen=[])
        if reviewer is not None:
            from dynamics_atlas_harness.nmr_graph import graph as g
            orig = g.build_graph
            rmodel = Scripted(script=reviewer, seen=[])
            import dynamics_atlas_harness.nmr_graph.run as r
            r.build_graph = lambda *a, **k: orig(*a, **{**k, "review_model": rmodel})
            self.addCleanup(setattr, r, "build_graph", orig)
            self.rmodel = rmodel
        summary = asyncio.run(run_graph(cfg, ws, run, model, tracker, mcp_tools_override=[*fake_tools(run)]))
        return summary, run, model

    def cfg(self, **kw):
        return GraphConfig(review_prompt_file=str(CONFIGS.parent / "content/layer4_reviewer.md"), enable_review=True, **kw)

    def test_review_passes(self):
        s, run, _ = self.run_it(self.cfg(), analysis_script(["Result from F1 and F2."]), [verdict("pass")])
        self.assertEqual((s["end_reason"], s["review_rounds"], s["review_calls"]), ("review_passed", 0, 1))
        self.assertTrue((run / "REPORT.md").exists())
        log = json.loads((run / "review_log.json").read_text())
        self.assertEqual(log[0]["verdict"], "pass")
        # the reviewer saw the report and the program-built inventory
        shown = self.rmodel.seen[0][1].content
        self.assertIn("Result from F1 and F2.", shown)
        self.assertIn('"uncited_fit_ids": []', shown)

    def test_review_returns_then_passes(self):
        s, run, model = self.run_it(self.cfg(), analysis_script(["v1 F1", "v2 F1 F2 with test"]),
                                    [verdict("revise", ["Mention F2"]), verdict("pass")])
        self.assertEqual((s["end_reason"], s["review_rounds"], s["review_calls"]), ("review_passed", 1, 2))
        self.assertEqual((run / "REPORT.md").read_text(), "v2 F1 F2 with test")
        feedback = [m for m in model.seen[-1] if isinstance(m, HumanMessage) and "Independent review" in m.content]
        self.assertEqual(len(feedback), 1)
        self.assertIn("Mention F2", feedback[0].content)

    def test_two_returns_then_forced_end(self):
        s, run, _ = self.run_it(self.cfg(max_review_rounds=2), analysis_script(["a", "b", "c"]),
                                [verdict("revise", ["do x"])])
        self.assertEqual((s["end_reason"], s["review_rounds"], s["review_calls"]), ("review_round_limit", 2, 3))
        self.assertEqual((run / "REPORT.md").read_text(), "c")

    def test_unusable_review_reply_closes_without_return(self):
        s, _, _ = self.run_it(self.cfg(), analysis_script(["a"]), [AIMessage(content="not json")])
        self.assertEqual((s["end_reason"], s["review_rounds"]), ("review_unusable", 0))

    def test_no_review_node(self):
        cfg = GraphConfig(enable_review=False)
        s, run, _ = self.run_it(cfg, analysis_script(["only report"]))
        self.assertEqual((s["end_reason"], s["review_calls"]), ("finished", 0))
        self.assertEqual(json.loads((run / "review_log.json").read_text()), [])

    def test_analysis_without_finish(self):
        s, _, _ = self.run_it(self.cfg(), [AIMessage(content="I give up")], [verdict("pass")])
        self.assertEqual((s["end_reason"], s["review_calls"]), ("ended_without_finish", 0))

    def test_consult_tool_called_inside_graph(self):
        d = Path(tempfile.mkdtemp())
        m = d / "m.md"
        m.write_text("# Bootstrap\nuncertainty by bootstrap\n\n# Signs\nsign of dw from CEST dip\n")
        cfg = GraphConfig(enable_review=False, enable_consult_tools=True, methods_file=str(m), cases_file=str(d / "missing.md"))
        script = [call("consult_methods", {"query": "sign of dw"}, 0), call("consult_cases", {"query": "anything"}, 1),
                  call("finish", {"report": "r", "atlas_entries": []}, 2), AIMessage(content="DONE")]
        s, run, model = self.run_it(cfg, script)
        self.assertEqual(s["end_reason"], "finished")
        log = [json.loads(x) for x in (run / "consult_log.jsonl").read_text().splitlines()]
        self.assertEqual([(x["tool"], x["empty"]) for x in log], [("consult_methods", False), ("consult_cases", True)])
        tool_msgs = [x.content for x in model.seen[-1] if x.type == "tool"]
        self.assertIn("CEST dip", tool_msgs[0])
        self.assertIn("无可用内容", tool_msgs[1])


class Consult(unittest.TestCase):
    def test_ranking_and_missing_file(self):
        d = Path(tempfile.mkdtemp())
        f = d / "x.md"
        f.write_text("# One\nresidue selection and global fits\n\n# Two\nchemical shift reference comparison\n\n# Three\nunrelated words here\n")
        out = consult.consult(str(f), "which reference for chemical shift", 1, 500)
        self.assertIn("Two", out)
        self.assertNotIn("One", out)
        self.assertEqual(consult.consult(str(f), "zzz qqq", 3, 500), consult.NO_MATCH)
        self.assertEqual(consult.consult(str(d / "none.md"), "x", 3, 500), consult.NO_CONTENT)
        self.assertEqual(consult.consult(None, "x", 3, 500), consult.NO_CONTENT)

    def test_blank_line_split_without_headings(self):
        segs = consult.split_segments("alpha beta\n\ngamma delta\n\nepsilon")
        self.assertEqual(len(segs), 3)


class Inventory(unittest.TestCase):
    def test_uncited_cited_missing_and_types(self):
        d = Path(tempfile.mkdtemp())
        (d / "fits").mkdir()
        (d / "observations").mkdir()
        for n, exps in ((1, ["cpmg_15N_600MHz"]), (2, ["cest_15N_600MHz_B1_10Hz"]), (3, ["cpmg_15N_600MHz", "cest_15N_600MHz_B1_10Hz"])):
            (d / "fits" / f"F{n}.json").write_text(json.dumps({"fit_id": f"F{n}", "experiments": exps, "flags": ["x"] if n == 3 else [], "per_residue": {}}))
        (d / "observations" / "O000007.json").write_text(json.dumps({"tool": "fit_exchange", "error": False, "result": {"fit_id": "F2"}}))
        inv = review.collect_fit_inventory(d, "We used F1 and O000007 and F009; residue F130 shifts.")
        self.assertEqual(inv["uncited_fit_ids"], ["F3"])          # F2 counts as cited through its observation
        self.assertEqual(inv["cited_but_missing"], ["F009"])
        self.assertEqual(inv["flagged_fit_ids"], ["F3"])
        self.assertEqual(inv["fits_by_data_type"], {"cpmg": ["F1"], "cest": ["F2"], "mixed": ["F3"]})

    def test_parse_verdict(self):
        self.assertEqual(review.parse_verdict('text {"verdict":"pass"} tail')["verdict"], "pass")
        self.assertEqual(review.parse_verdict('{"verdict":"revise","required_actions":[]}')["verdict"], "pass")
        self.assertIsNone(review.parse_verdict("nothing"))


class Configs(unittest.TestCase):
    def test_presets(self):
        a, w1, nr = (load_config(CONFIGS / f"{n}.yaml") for n in ("A", "W1", "W1_noreview"))
        self.assertEqual((a.enable_consult_tools, a.enable_review, a.prompt_files), (False, False, []))
        self.assertEqual((w1.enable_consult_tools, w1.enable_review, len(w1.prompt_files)), (True, True, 2))
        self.assertEqual((nr.enable_consult_tools, nr.enable_review), (True, False))
        for c in (w1, nr):
            self.assertTrue(all(Path(p).is_file() for p in c.prompt_files))
        self.assertIn("consult_methods", build_system_prompt(w1))
        self.assertNotIn("consult_methods", build_system_prompt(a))
        from dynamics_atlas_harness.nmr_agent.prompts import BASE
        self.assertTrue(build_system_prompt(a).startswith(BASE))


if __name__ == "__main__":
    unittest.main()
