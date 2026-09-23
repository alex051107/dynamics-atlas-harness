# FutureHouse Systems and Kosmos: Architecture Notes for the Harness

Read-only review of public GitHub source (Future-House org, all six repos on `main`, via `gh api`) and the Kosmos preprint (arXiv 2511.02824, HTML, two independent passes cross-checked for section numbers/quotes). Nothing cloned, installed, or run. Per repo: README + 2–3 source files, not full coverage.

## 1. Six systems

### finch — notebook agent
- Single agent edits/executes cells in a persistent Jupyter notebook via aviary `Tool`s until it calls a terminal `submit_answer` tool. (finch/blob/main/src/fhda/data_analysis_env.py)
- State = the live notebook object + action history + reward + `done`, exported as an aviary `Frame` for logging. (same file, `export_frame`)
- Runs in a bioinformatics Docker image; working dirs sync to GCS via a `DataRepo` push/pull so long runs survive restarts. (finch README; src/fhda/storage.py)
- Grading is internal: an LLM (`EvalAnswerMode.LLM`) compares the submitted answer to a reference inside the environment, not as an external check. (data_analysis_env.py)

### robin — multi-agent discovery pipeline
- Not one agent loop: a pipeline of `Step`s (prompt template + files) is submitted as named jobs to a hosted runtime ("Edison"); robin assembles prompts, it doesn't reason. (robin/blob/main/robin/multitrajectory_runner.py)
- Each step can fan out into N parallel task requests (e.g. tournament-style ranking), awaited together. (same file)
- Inter-step state is a plain results dict (task ids, responses, success rate) JSON-dumped after the run — no shared memory object. (same file)
- Evaluation: per-step task success rate, plus pairwise LLM-judged ranking of hypotheses into CSVs for human review. (README; same file)

### aviary — environment/gym library
- Canonical loop: `env.reset() -> (obs, tools)`, then `agent -> ToolRequestMessage -> env.step(action) -> (obs, reward, done, truncated)`, agent-agnostic. (aviary README; src/aviary/env.py)
- `Environment` is generic over a state type; tools live on the environment (not the agent) since they mutate its state; `exec_tool_calls` auto-splits valid/invalid calls. (src/aviary/env.py)
- Tool calls are typed pydantic models with JSON-schema arguments, so malformed calls are caught structurally. (src/aviary/tools/base.py)
- Aviary never runs agents or scores beyond the scalar reward from `env.step`; looping and scoring are pushed to ldp and to each environment. (env.py)

### ldp — agent/rollout framework
- `Agent` = two methods, `init_state(tools)` and `get_asv(state, obs) -> (action, new_state, value)`, decoupled from `Environment.step` so agents/environments compose freely. (ldp README)
- `RolloutManager.sample_trajectories` runs rollouts concurrently (`asyncio.wait(FIRST_COMPLETED)`), respawning environments to hit a step budget rather than a fixed episode count. (ldp/blob/main/src/ldp/alg/rollout.py)
- History = a `Trajectory` of `Transition`s, serializable to JSONL; agent memory (e.g. ReAct's message history) is a separate `SimpleAgentState`, distinct from env state. (rollout.py; src/ldp/agent/react_agent.py)
- A stochastic computation graph (`compute_graph`, `LLMCallOp`) wraps each sub-step for later optimization — opt-in, not required. (README)

### paper-qa — literature RAG agent
- `run_agent()` dispatches to one of three interchangeable loops — fixed-order "fake" agent, aviary `ToolSelector` agent, or ldp agent — chosen by a settings flag alone. (paper-qa/blob/main/src/paperqa/agents/main.py)
- Four tools: `paper_search`, `gather_evidence`, `generate_answer`, `complete`; each docstring is the LLM-visible schema and states its own preconditions. (src/paperqa/agents/tools.py)
- State bundles the doc store + a `PQASession` (answer, contexts, cost, tool history); a short computed `status` string is re-injected each step instead of full state. (agents/tools.py)
- A hard timeout forces early termination into "just answer"; tool history is checked so an answer never returns without `generate_answer` having run. (agents/main.py, `_run_with_timeout_failure`)
- Outcome is a typed `AgentStatus` enum (SUCCESS/UNSURE/TRUNCATED/FAIL); answers carry grounded in-text citations by construction. (agents/main.py)

### BixBench — bioinformatics agent benchmark
- `TrajectoryGenerator` pulls dataset "capsules" from Hugging Face, builds one finch `DataAnalysisEnv` per question, runs them via ldp's `RolloutManager` — BixBench is finch's benchmark harness, not a separate agent. (BixBench/blob/main/bixbench/generate_trajectories.py)
- Every trajectory is stored twice: flat JSON summary for fast analysis, full ldp `Trajectory` as JSONL for replay. (same file, `store_trajectory`)
- `GradingFunction` supports exact/partial string match, numeric-range match, and LLM-judge match, returning a typed `GradeResult(grade, correct, refusal)`; MCQ adds an explicit refusal option. (bixbench/graders.py)
- Final scores use majority vote over k=5 replicas, with ablations for image input and refusal option. (README)

## 2. Kosmos structured world model (arXiv 2511.02824)

Read via arxiv.org/html/2511.02824, two independent passes. Kosmos's code is not public — this reports what the paper states, not a source review.

- Defined functionally, not as a schema: "Kosmos shares and synthesizes information among these agents by continuously updating a structured world model" (Sec. 2.1). No field-level structure appears in the text read.
- Stated coherence mechanism for long runs: lets Kosmos "coherently pursue the specified objective over 200 agent rollouts" (Sec. 2.1). Per run: 166 data-analysis rollouts (42,000 LOC) + 36 literature rollouts (1,500 papers), cycles up to 12 hours; discoveries traced to cycles 5, 10, 20 (Sec. 2.1).
- Two agent types split work per cycle — parallel data-analysis and literature-search instances — reading next tasks from the world model: "Kosmos then queries the world model to propose literature search and data analysis tasks" (Sec. 2.1). No retrieval mechanism or schema is given beyond this sentence.
- Traceability is a stated rule: "Each statement and figure in the report cites either a publication found by the literature search agent or a Jupyter notebook created by the data analysis agent" (Sec. 2.1); figures link to hosted trajectories on platform.edisonscientific.com.
- Accuracy evaluation: 102 statements from 3 reports, judged supported/refuted by blinded expert scientists — "the original code or cited paper(s) supporting the statements were not made available to the evaluating scientist" (Sec. 4.1.1).
- Results (confirmed in both passes): "79.4% of the statements in the report were accurate" — 85.5% data-analysis, 82.1% literature-review, 57.9% synthesis/interpretation (Sec. 4.1.1). A first-pass-only, unverified finding attributed the interpretation gap to conflating statistical significance with scientific value (Sec. 3.2 per that read) — lower confidence than the numbers above.
- No code, weight, or dataset release statement appears in the text read; only public artifacts are hosted trajectory links and the affiliation "Edison Scientific Inc." Kosmos is not shown to be open source.

## 3. Design takeaways for our harness

Our setting: a single analysis agent on stage cards (goal, inputs, routine move, done criteria, stuck signal, ordered follow-ups, fallback claim, claim limit), sandboxed notebook execution, an evidence ledger with provenance, a drift judge, human review at chosen stages, output = a database of annotated states.

1. **ADOPT** — split agent from environment/tools/state as aviary does (`Environment` owns tools + typed state). Keeps our executor swappable, state independently serializable for the ledger. (aviary `env.py`)
2. **ADOPT** — paper-qa's compact re-injected `status` string as what the agent sees each step, not the full ledger. Fits a stage card's "done criteria" check. (paperqa `agents/tools.py`)
3. **ADOPT** — paper-qa's timeout-then-forced-answer as the literal implementation of our "fallback claim" field: every run ends with something citable. (paperqa `agents/main.py`)
4. **ADOPT** — BixBench/finch's dual storage (flat JSON + full JSONL) as the evidence-ledger pattern: cheap to query, fully replayable. (BixBench `generate_trajectories.py`)
5. **ADOPT** — BixBench's typed grade result with a distinct refusal category. Ready-made implementation of our ABSTAIN/NOT_COMPARABLE discipline. (BixBench `graders.py`)
6. **ADAPT** — ldp's concurrency pattern (respawn-to-budget) for running stage cards across many cases under one shared budget; skip its optimizer/gradient machinery, we don't need it. (ldp `alg/rollout.py`)
7. **ADAPT** — Kosmos's world-model-as-task-proposer for our "ordered follow-up analyses": the read/write-scratchpad pattern is sound, but its schema is undocumented, so only the pattern transfers. (Kosmos Sec. 2.1; inference)
8. **ADOPT** — Kosmos's rule that every statement cites a trajectory, notebook, or paper — independent confirmation from a frontier lab that a claim-source-map default is correct. (Kosmos Sec. 2.1)
9. **ADOPT with caution** — Kosmos's blinded-evaluator audit as our human-review design; its interpretation-statement weak point (57.9% vs. 85.5%) argues for routing "interpretation" stage cards to human review more often. (Kosmos Sec. 4.1.1)
10. **SKIP** — robin's dispatch-to-hosted-platform orchestration. Robin and Kosmos both route through the same proprietary "Edison Scientific" platform; the real agent-loop code for both is outside the public repo, so this teaches us nothing about loop design. (robin `multitrajectory_runner.py`; Kosmos author affiliations)
