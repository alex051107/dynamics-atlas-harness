# FutureHouse agent-design research, pass 2 (narrow, code-located)

Commit SHAs pinned at fetch (2026-09-22): aviary `7167342`, ldp `7220ca1`, finch `aea66fd`, paper-qa `57e89f7`.

## 1. Future-House public repositories

Fetched via `gh api orgs/Future-House/repos` (15 public repos, 2026-09-22).

| Repo | What it is | Last push | Matters? |
|---|---|---|---|
| `paper-qa` | RAG answering questions from scientific PDFs with citations | 2026-09-22 | Yes — fullest tool-gated agent loop with re-injected status + evidence store. |
| `aviary` | "Language agent gym" — Environment/Message/Tool primitives shared org-wide | 2026-09-16 | Yes — base substrate (messages, tool schema, execution/error handling). |
| `ldp` | Modular agents/environments/optimizers framework, incl. `lmi` LLM client | 2026-09-21 | Yes — where agent *state* (history, hiding, sliding windows) is decided. |
| `finch` | Aviary-based data-analysis agent built around a Jupyter notebook | 2026-04-22 | Yes — closest analog to a stage card with a persistent, growing artifact. |
| `robin` | Multi-agent system automating a fixed scientific-discovery workflow | 2026-04-21 | Yes — closest analog to orchestration over fixed stages. |
| `BixBench` | Benchmark for LLM agents in comp. biology, on finch's notebook env | 2025-10-06 | Somewhat — benchmark-design precedent only. |
| `LAB-Bench` | Benchmark dataset for foundational biology-research capabilities | 2025-09-27 | Somewhat — task-design precedent only. |
| `ether0` | Scientific-reasoning model + dataset + RL rewards for chemistry | 2025-10-26 | Marginal — training artifact, not harness design. |
| `tutorial-series` | Notebook tutorials | 2026-07-28 | Marginal — onboarding examples. |
| `llm-client` | Archived. "Central LLM client for use by Aviary and PaperQA" | 2025-02-23 | Historical — deprecated for `lmi` inside `ldp` (Q4). |
| `LitQA` | Archived eval dataset of literature QA questions | 2024-12-18 | No — archived benchmark. |
| `WikiCrow` | No description; wiki-article generation app built on paper-qa | 2024-10-24 | No — downstream app. |
| `SWE-bench` | Fork of upstream SWE-bench | 2024-07-24 | No — not FH-authored design. |
| `trl` | FutureHouse fork of HuggingFace `trl` (RL training library) | 2026-06-22 | No — training infra fork. |
| `feathers` | Archived. Design system for FutureHouse web apps (TypeScript) | 2025-12-06 | No — UI, unrelated. |

Source: `gh api orgs/Future-House/repos`. `robin` internals: not verified this pass.

## 2. Incremental context: what the model sees each turn

**aviary.** `Environment.step` returns only the *new* observations for that turn, not history (`src/aviary/env.py:120`, abstract signature `async def step(self, action: Message) -> tuple[Messages, float, bool, bool]`). https://github.com/Future-House/aviary/blob/7167342915e656fba1d93af4a5f0549cb803cd76/src/aviary/env.py#L120

`DummyEnv.step` shows the pattern: `exec_tool_calls` returns only the tool-response messages for this action, and the environment appends them to its own internal state, while the caller (the agent) decides how to fold them into the prompt (`src/aviary/env.py:573-585`). `ToolResponseMessage`/`ToolRequestMessage` live in `src/aviary/tools/base.py:125` and `:150` (not `message.py`); `EnvStateMessage` is a plain `Message` subclass in `src/aviary/message.py:318`, deprecated in favor of an `info={"is_env_state": True}` flag "since this subclass is erased by `aviary.tools.base.MessagesAdapter` serialization." aviary is a pure delta/observation protocol — full-history bookkeeping is the *agent's* job.

**ldp.** `SimpleAgentState` (`src/ldp/agent/simple_agent.py:27`) is the accumulator: each turn, `get_next_state` appends new observations to `self.messages` and the *whole* list is sent to the LLM (`get_asv`, line 168-183: `result = await self._llm_call_op(..., msgs=messages, ...)`). Context growth is controlled by three opt-in flags on the same class (lines 36-47): `hide_old_env_states` (replaces old `EnvStateMessage`s with a fixed placeholder `HiddenEnvStateMessage` = `"[Previous environment state - hidden]"`), `hide_old_action_content` (nulls old `ToolRequestMessage.content`), and `sliding_window` (keeps only the last N transition "blocks," collapsing older ones behind a `"[Previous messages - hidden]"` marker, lines 78-89). `ReActAgent` (`src/ldp/agent/react_agent.py:40`) carries the identical three flags. ldp defaults to **full resend**, with hiding/windowing as opt-outs — the inverse of a diff-based protocol.
https://github.com/Future-House/ldp/blob/7220ca1e06292b856b1a3f1fe2c94170bc933055/src/ldp/agent/simple_agent.py#L36-L109

**finch (notebook env).** The whole notebook is re-sent every step, not a diff. `get_env_state_msg` (`src/fhda/notebook_env.py:341-352`) renders **all** current cells (`self.state.cells`) to Markdown on every call:
```python
def get_env_state_msg(self) -> EnvStateMessage:
    md_notebook, notebook_images = utils.view_notebook(cells=self.state.cells, ...)
    return EnvStateMessage.create_message(
        text=f"Markdown representation of notebook contents ({nb_path}):\n\n{md_notebook}", ...)
```
`step()` (lines 171-185) appends that full render after every tool call: `obs = [*obs, self.get_env_state_msg()]`. Individual tools (e.g. `edit_cell`, line 215) return only a short confirmation string, but the environment bolts on a full-notebook snapshot regardless — this is why ldp's `hide_old_env_states` exists: it hides *previous* full-notebook dumps, keeping only the latest.
https://github.com/Future-House/finch/blob/aea66fdf2dd2be827727de50a73cae60dff59972/src/fhda/notebook_env.py#L341-L352

**paper-qa.** A short status string is recomputed and appended to nearly every tool's return value, not to the whole message list. `EnvironmentState.status`, a computed property (`src/paperqa/agents/tools.py:68-73`), is built by `default_status` (lines 37-44):
```python
def make_status(total_paper_count, relevant_paper_count, evidence_count, cost) -> str:
    return (f"Status: Paper Count={total_paper_count} | Relevant Papers={relevant_paper_count}"
            f" | Current Evidence={evidence_count} | Current Cost=${cost:.4f}")
```
`gather_evidence` returns `f"Added {n} pieces of evidence...\n\n" + status` (line 311); `gen_answer` returns `f"{answer} | {status}"` (line 372); `Complete.complete` returns `f"{...} | {state.status}"` (line 440). The evidence store is never dumped in full — only its *count* and a per-call top-N excerpt (`gather_evidence`, lines 280-299). Full evidence lives in `state.session.contexts`, off the message thread.
https://github.com/Future-House/paper-qa/blob/57e89f7223b0960d5ee5ea048c69e3c47e088572/src/paperqa/agents/tools.py#L27-L44

## 3. Tools: definition, validation, error surfacing

`Tool.from_function` (`src/aviary/tools/base.py:398-467`) uses `docstring_parser.parse` to read the function's docstring, raises `ValueError` if the docstring or any parameter description is missing (lines 411-412, 429-430; opt-out via `allow_empty_param_descriptions`), builds a throwaway Pydantic model from the signature (`create_model`, line 450) and calls `.model_json_schema()` for the JSON Schema (line 451). `state`/`tool_call_id` params are stripped from the LLM-facing schema (injected server-side, line 417-419).
https://github.com/Future-House/aviary/blob/7167342915e656fba1d93af4a5f0549cb803cd76/src/aviary/tools/base.py#L398-L467

Argument validation happens at deserialization: `ToolCallFunction.deserialize_args` (lines 57-76) tries `json.loads` on the raw arguments string; on failure it relabels the call `name = "INVALID"` (`INVALID_TOOL_NAME`, line 50) rather than raising. `Environment.filter_invalid_tool_calls` (`src/aviary/env.py:161-193`) splits a request into valid/invalid subsets against `self.tools`, and `exec_tool_calls` turns each invalid call into `ToolResponseMessage(..., content=f"Invalid tool call: {tool_call.function.name}")` (lines 336-343) — the model is told which call failed, not why, via the same tool-result channel it expects.

Runtime exceptions in a tool function are caught the same way when `handle_tool_exc=True`: `env.py:284-307` wraps it as `content=f"Encountered exception during tool call: {format_exc(tool_exc)}"`, returning a normal `ToolResponseMessage` rather than propagating.
https://github.com/Future-House/aviary/blob/7167342915e656fba1d93af4a5f0549cb803cd76/src/aviary/env.py#L284-L343

**paper-qa's precondition gate is a hard check on `gather_evidence`, not on `gen_answer`.** `GatherEvidence.gather_evidence` (`src/paperqa/agents/tools.py:225-241`) raises `EmptyDocsError("Not gathering evidence due to having no papers.")` when `state.docs.docs` is empty. `GenerateAnswer.gen_answer` (lines 323-372) has **no code-level gate** — "at least five pieces of evidence" is only a docstring instruction (line 328), a soft/prompted precondition, unenforced. The raised `EmptyDocsError` is caught by aviary's `exec_tool_calls` because `PaperQAEnvironment.step` passes `handle_tool_exc=True` (`src/paperqa/agents/env.py:309-329`), reaching the model as an ordinary tool-result message.
https://github.com/Future-House/paper-qa/blob/57e89f7223b0960d5ee5ea048c69e3c47e088572/src/paperqa/agents/tools.py#L225-L241

## 4. Model access: LiteLLM, own client, or LangChain

All four libraries call models through an FH-owned wrapper around **LiteLLM**, not LangChain. `ToolRequestMessage`/`ToolResponseMessage`/`Parameters` carry the comment "Matching LiteLLM structure" (`src/aviary/tools/base.py:127, 157, 201`). The wrapper is `lmi` (PyPI `fhlmi`), living inside `ldp` at `packages/lmi/src/lmi/`, not its own repo. `LiteLLMModel` (`packages/lmi/src/lmi/llms.py:995`) calls `litellm.acompletion` directly (line 1291: `completions = await track_costs(litellm.acompletion)(**call_kwargs)`); `paperqa/agents/env.py:18` and `agents/tools.py:14` both import `LiteLLMModel`/`EmbeddingModel` from `lmi`. finch's `pyproject.toml` depends on `fhaviary`, `ldp`, and, as a stated exception, the raw `anthropic` SDK — inline comment: "this is necessary for tortoise, remove in favor of LMI when it works with search" — one deliberate, flagged-temporary bypass of the wrapper.
https://github.com/Future-House/ldp/blob/7220ca1e06292b856b1a3f1fe2c94170bc933055/packages/lmi/src/lmi/llms.py

**paper-qa did depend on LangChain, twice over, and removed it in two separate steps.** PR #223 ("[WIP] Version 4 with better open source model support and no langchain," merged 2024-01-22, commit `3cb16f2`) removed LangChain from the *LLM-calling* layer — checklist includes "Remove Langchain" and "Get langchain vector store adapter" (a partial, optional carry-over). PR #358 ("`aviary` and `ldp` for agents over `langchain`," merged 2024-09-11, commit `b9b9c224f`) then removed LangChain from the *agent/tool-orchestration* layer that still used it: "Incorporates `aviary` as required and `ldp` as opt-in, drops `langchain` ... Implements `agents.env` for an aviary `Environment`." The current `pyproject.toml` on `main` has zero `langchain` references (checked directly). The archived `llm-client` README states: "the `llmclient` repository is now deprecated. We have migrated all development and maintenance to a new package, `lmi`, which is part of the `ldp` repository."
https://github.com/Future-House/paper-qa/pull/358 · https://github.com/Future-House/paper-qa/pull/223 · https://github.com/Future-House/llm-client/blob/main/README.md

## 5. LangGraph today (official docs, docs.langchain.com)

**StateGraph and reducers.** A graph is built from a state schema (`TypedDict`/Pydantic) and executes in discrete "super-steps." Each state key has an independent reducer: unannotated keys default to overwrite-on-update; a key annotated `Annotated[list, operator.add]` (or the prebuilt `add_messages` for chat histories) accumulates instead. Nodes return *partial* updates; LangGraph applies each key's reducer to merge them into running state. https://docs.langchain.com/oss/python/langgraph/graph-api

**Checkpointers and durable execution.** A checkpointer snapshots the full graph state after every super-step, keyed by a `thread_id`; production options are `PostgresSaver`/`AsyncPostgresSaver` and `SqliteSaver` (local), with `InMemorySaver` for tests only. Re-invoking a graph with the same `thread_id` resumes from the last checkpoint after a crash instead of restarting. https://docs.langchain.com/oss/python/langgraph/persistence

**Interrupts for human-in-the-loop.** Calling `interrupt(value)` inside a node halts the graph and surfaces `value` to the caller; this requires a checkpointer, since state at that exact point is persisted for later resume. A human resumes with `Command(resume=<value>)` against the same `thread_id`; that value becomes `interrupt()`'s return inside the node, which re-executes from its top on resume. https://docs.langchain.com/oss/python/langgraph/interrupts

**Message history management.** Short-term memory is checkpointed thread state — "state is persisted to a database (or memory) using a checkpointer so the thread can be resumed at any time." Two built-in mitigations for context growth: `trim_messages` drops older messages by token or message count before a model call (only the copy sent to the model shrinks, not the stored state), and `SummarizationMiddleware` replaces older spans with a running summary while keeping recent turns verbatim. https://docs.langchain.com/oss/python/langchain/short-term-memory

## What this means for a stage-card harness

- **ADOPT** — Delta-shaped `step()` return (aviary): a stage should emit only what changed this turn; the harness's own accumulator, not the stage function, owns history.
- **ADOPT** — A single re-injected status line (paper-qa's `EnvironmentState.status`) per tool result: cheap, always-fresh orientation (counts/cost/stage) without resending large state.
- **ADOPT** — Hard-raise-then-catch-into-message for precondition failures (paper-qa's `EmptyDocsError` + aviary's `handle_tool_exc=True`): keeps the check as real code, not a docstring hint, while still returning a recoverable tool message.
- **ADAPT** — ldp's `hide_old_env_states`/`sliding_window`: worth copying for a full-artifact stage card, but gate it per stage, since some stages need the full prior artifact and some don't.
- **ADAPT** — Docstring-to-schema tool definition (`Tool.from_function`): good ergonomics, but "docstring is source of truth" is risky for a governed harness — pair it with the project's own schema validation.
- **SKIP** — finch's "re-render the entire notebook every step": fine at finch's scale, but for larger stage-card artifacts this is exactly what `hide_old_env_states` exists to patch over; a diff/section-scoped update is not verified in any of these repos.
- **SKIP** — LangChain: paper-qa's history shows removing it twice (LLM layer 2024-01, agent layer 2024-09) for a thin LiteLLM wrapper; adopting it now reproduces a path FutureHouse already walked back.
- **ADAPT** — LangGraph's interrupt()+checkpointer for human-approval points between stage cards: matches "human reviewer owns claim upgrades," but needs LangGraph's Postgres/Sqlite persistence — fit with the file-based state model is not verified.
