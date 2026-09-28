# NMR 工具合同 v1（Opus 案例线 → Codex 架构线）

由 `tool_specs()` 自动生成（`dynamics-atlas-harness-nmr-agent-v0/src/dynamics_atlas_harness/nmr_agent/tools.py`），2026-09-26。
工具共 19 个（含仅 C 组可用的 reflect）。标记“分析类”的工具必须带 `purpose` 与 `expectation`，并计入反思检查点。

| 工具 | 分析类 | 必填参数 | 全部参数 | 说明 |
|---|---|---|---|---|
| `inventory` |  |  |  | List variants, experiments (kind, field, delays, B1, residue counts) and other files in the workspace. |
| `read_text` |  | path | path, max_chars, offset | Read a workspace text file in pages; use next_offset to continue. |
| `read_result` |  | observation_id | observation_id, offset | Retrieve a full earlier tool observation by its issued id, in pages. Results remain available after truncation. |
| `get_research_state` |  |  |  | Retrieve the current model-authored research notes, including withdrawals. These notes are not new tool evidence. |
| `compare_references` | 是 | reference_ids, purpose, expectation | reference_ids, residues, regions, variant, fit_id, dw_key, pH, temperature_K, ionic_strength_M, purpose, expectation | Compare minor-state 15N shifts (ground + signed dw from one of your fits) with several reference sets on exactly the same residue intersection. Returns signed r |
| `screen_dispersion` | 是 | variant, experiment, purpose, expectation | variant, experiment, purpose, expectation | Per-residue screen of one experiment: CPMG -> dR2 (low minus high nu_CPMG) with z-score; CEST -> depth and offset of the strongest dip away from the major-state |
| `show_profile` | 是 | variant, experiment, residue, purpose, expectation | variant, experiment, residue, purpose, expectation | Return the numeric profile of one residue (CPMG: nu_CPMG vs R2eff; CEST: ppm vs normalised intensity). |
| `fit_exchange` | 是 | variant, residues, purpose, expectation | variant, residues, experiments, mode, kex0, pb0, dw_init, fix, model, groups, kex2_0, pc0, dw2_init, purpose, expectation | Fit an exchange model (numerical Bloch-McConnell) to chosen residues and experiments. Two-state: mode='global' shares kex and pb; mode='per_residue' fits them p |
| `cest_sign_scan` | 是 | variant, residues, kex, pb, purpose, expectation | variant, residues, kex, pb, dw_abs, purpose, expectation | For each residue, refit its CEST profile (kex/pb fixed) from several starting /dw/ of both signs and report the best dw and whether the sign is determined. |
| `bootstrap_global` | 是 | variant, residues, purpose, expectation | variant, residues, experiments, n_boot, kex0, pb0, dw_init, purpose, expectation | Residue-resampling bootstrap of the global kex and pb (5-50 replicates, each a full refit, run in parallel; typically a few seconds to a minute in total). |
| `bmrb_search` | 是 | term, purpose, expectation | term, purpose, expectation | Search BMRB by free text; returns entry IDs only. |
| `bmrb_entry` | 是 | entry_id, purpose, expectation | entry_id, atoms, purpose, expectation | Get one BMRB entry's molecular system, sample conditions and assigned shifts for chosen atoms (default N, H). |
| `python` | 是 | code, purpose, expectation | code, purpose, expectation | Run a Python script (numpy, scipy, pandas available; workspace is read-only cwd; fitting library imports as `exchange`). Full output is retained under its obser |
| `update_research_state` |  |  | facts, hypotheses, open_questions, plan, retracted | Record durable research state: facts about the sample, hypotheses with evidence for/against, open questions, current plan. Only what you write here survives con |
| `propose_experiment` |  | description, question_it_resolves | description, question_it_resolves | Record a new measurement you would recommend (not executed). |
| `reference_shifts` | 是 | action, purpose, expectation | action, name, variant, atoms, pH, temperature_K, ionic_strength_M, purpose, expectation | List available reference chemical-shift sets and predictors (action='list'), or fetch one (action='get', name, variant, atoms). |
| `pdb_ligand_distances` | 是 | pdb_id, purpose, expectation | pdb_id, ligand, ligand_atoms, atom, chain, purpose, expectation | From a PDB entry (RCSB, coordinates only), list ligands, or compute each residue's backbone-atom distance to the nearest atom of a chosen ligand (optionally spe |
| `finish` |  | report, atlas_entries | report, atlas_entries | End the analysis. Submit (1) the report (markdown): direct answers, numbers with uncertainties, the evidence behind each conclusion (cite fit ids / tool results |
| `reflect` |  | expected, observed, discrepancy, suspects, decision, next_action | expected, observed, discrepancy, suspects, decision, next_action | Compare expectation with observation after a checkpoint and decide how the plan changes. |

## 运行目录与记录格式（以 `<local-work>/runs/V3_C21_r3/` 为样例）

- `actions.jsonl`：每行一次工具调用，键 = ['call', 'tool', 'args', 'error', 'checkpoint', 'seconds', 'result']。MCP 运行器用 `call` 计数；OpenRouter 循环用 `turn`。
- `observations/O000001.json …`：每次调用的完整结果，键 = ['tool', 'args', 'error', 'result']；工具返回里带 `observation_id`，可用 `read_result` 分页回读。
- `fits/F001.json …`：拟合摘要（global、global_err、per_residue、chi2、aic、bic、flags、notes、model、groups、experiments）。
- `research_state.json`：键 = ['facts', 'hypotheses', 'open_questions', 'plan', 'retracted', 'proposed_experiments']；只能由 `update_research_state` / `propose_experiment` 改写，`reflections.json` 另存。
- `ATLAS_ENTRIES.json`：候选条目列表，字段 = ['protein', 'construct_and_variant', 'bound_ligands', 'conditions', 'major_state', 'alternative_state', 'exchange_parameters', 'kinetic_model', 'residues_and_regions', 'evidence_type', 'structural_identity_evidence', 'controls_and_artefact_checks', 'functional_relevance', 'cannot_be_supported', 'proposed_tier', 'provenance']。`proposed_tier` 只是提议。
- `REPORT.md`、`summary.json`（模型标识、调用数、名义成本）、`transcript.jsonl`（无头会话流）、`system_prompt.txt`、`user_prompt.txt`、`mcp_config.json`。

## 启动命令

```bash
PYTHONPATH=src python3 -m dynamics_atlas_harness.nmr_agent.claude_runner \
  --workspace <local-work>/kras_ws_v3 --run-dir <local-work>/runs/<RUN> \
  --arm A|B|C|C2 --model claude-opus-5-5 --max-calls 70 --block-bmrb 52021,52023,52024
```

隔离开关（`claude_runner.py`）：`--tools "" --setting-sources "" --disable-slash-commands --strict-mcp-config --allowedTools mcp__nmr --no-session-persistence`，中性 cwd `/tmp/nmr_solver/<run>`，使用桌面 App 自带的 Claude Code 2.1.281（2.1.268 不支持 Opus 5.5）。python 工具在 `sandbox-exec` 下运行：拒绝读 /Users（工作区与临时目录除外）、拒绝网络与写工作区。

## 工作区布局（v3）

`<variant>/experiments.json`（实验参数与残基清单）、`<variant>/data/<experiment>/<residue>.txt`、`ground_state_shifts.json`、`measured_R1.json`、`sequence.json`、`references/*.json`、`hsqc_minus_hmqc_*.txt`；对照样品为 `<variant>_GDP/`；`relaxation_15N_850MHz/*.csv`；`TASK.md`；`lib/`（exchange.py、multistate.py，供沙箱 python 导入）。泄露审计写在工作区外：`<workspace>_LEAK_AUDIT.json`。
