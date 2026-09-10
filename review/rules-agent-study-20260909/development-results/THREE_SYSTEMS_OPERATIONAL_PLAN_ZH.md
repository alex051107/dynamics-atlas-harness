> **SUPERSEDED 2026-09-09 (v1 → v2)** → 见 `HSP90_FIRST_ROUND_PLAN_V2_ZH.md`。Pro 审查见 `PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md`。本文保留为记录。

# 三体系操作计划：建系统 → 跑 HSP90 → 结果包交 Pro → 第二、第三体系

Dynamics Atlas · 2026-09-09 · 供 Codex 逐步执行、GPT Pro 审查结果 · 版本 v1

> 本文替代同目录的 `THREE_SYSTEMS_ANTI_DRIFT_PLAN_ZH.md` 与 `CODEX_EXECUTION_PLAN_RULES_HARNESS_HSP90_V1_ZH.md`；两者保留为草稿记录。
> 路径约定：`WS` = 本地工作区根目录（`dynamics-atlas-harness` 仓库的上级目录，不在 git 内）；`HARNESS` = `WS/dynamics-atlas-harness`；`TASK0` = `WS/autoresearch/tasks/dynamics_atlas_rules_incremental_value_protocol_20260909`。

## 0. 一页摘要

**要交出的东西：**

1. 一个能跑的系统：Agent 从论文和数据里产出结构化元数据档 → 已有的确定性 Rules 选择器给出审查义务 → 义务进入 Agent 分析、对主张的检查和评分依据 → Agent 在沙箱里做分析并按协议提交答案 → 每个数字由冻结脚本复算。代码在 harness 仓库分支 `feature/luna-runtime-v1`，离线测试全过，附 `REPLAY.md`。
2. 三个体系（HSP90、E. coli DHFR、ADK，Soojung 8 月 24 日点名）各一份科学表征：答案、与文献结论的逐主张比对、复算状态、Agent 单独 vs Agent+Rules 系统的具体差异。
3. 三个结果包，每个体系完成后交 GPT Pro 审查一次；Pro 的意见按条处置并记录。

**审查方式：** 不等领域专家。每阶段产出的结果包由 Pro 审；Pro 能指出错误、遗漏和过强结论，我们修一次并记录处置。Pro 审查不构成领域批准，所有结论保持"开发暴露、Pro 审过、未经领域确认"标签——这是 `PROJECT_MEMORY.md` 的永久边界，不是流程选项。

**PM 只做三件事，一次签完（§1）。** 其余全部由 Codex 执行、Pro 审查。

**顺序：** 建系统（3 天）→ HSP90 四站（5 天）→ Pro 审查包 #1 → ADK/DHFR 只读盘点并按规则选一个（2 天）→ 第二体系四站（5 天）→ Pro 审查包 #2 → 第三体系（5 天）→ Pro 审查包 #3 → 三体系汇总。约六周，模型费用 ≤ $1.50（账户余 $3.95）。

**不做：** 不换模型、不充值、不跑新 MD、不改 33 条注册表、不新建题库、不做四来源 24 份比较、不并行开两个体系、不声称 held-out。

## 1. PM 一次性授权清单 **[开工前签]**

| 项 | 内容 | 为什么绕不开 |
|---|---|---|
| 1 | 模型费用上限 **$1.50**（三体系合计，含元数据档起草）；出现 `UNKNOWN_CHARGE.json` 即停 | `CLAUDE.md` 手动门：live model calls |
| 2 | 在运行 shell 中提供 `OPENROUTER_API_KEY`（Codex 不从任何文件读 key） | 凭证 |
| 3 | 允许 `feature/luna-runtime-v1` 分支 commit / push / 开 Draft PR；`runs/`、案例数据、凭证不入库 | `CLAUDE.md` 手动门：git push |
| 4 | 允许为 S1/S2 只读下载公开数据（PDB、BMRB、Zenodo、ATLAS/mdCATH 条目），每体系 ≤ 2 GB，不跑新模拟 | STATUS 记录"DHFR action not authorized" |
| 5 | 允许把 `MD_TRAJECTORY` 最小方法档作为**开发 proposal**送入选择器（不修改正式 method scope 文件）；标签 `DEVELOPMENT_PROPOSAL_NOT_HUMAN_REVIEWED` | 8/24 计划要求人审；本轮改为 Pro 审 |

签字方式：PM 回复"授权 1–5"，Codex 写入 Decision Log 一条，开工。

## 2. 要建成的系统

```text
案例包 /source（论文 MD、数据、清单、公开事实、检查范围）
   │
   ├─ stage profile ── Luna 读 /source，按 v0.3 schema 提交 metadata_profile_v0_3.json
   │                    └─ jsonschema 校验，不过给一次修订，两次不过 → profile_rejected.json 停
   │
   ├─ rules_bridge ─── 调上游选择器 select_review_obligations.py（只读）
   │                    └─ review_obligations.json（DRAFT_REVIEW_PLAN：obligations[], unresolved_inputs[]）
   │                         ├─ render_active_rules.py → ACTIVE_RULES_<case>.md（每条带 rule_id，B 组读）
   │                         ├─ derive_public_facts.py → PUBLIC_FACTS.json（C 组检查的对象）
   │                         └─ render_rubric.py     → hidden/grading_rubric.md（评分依据模板）
   │
   ├─ stage analysis ─ Luna 在 Docker 沙箱里读、算、看图、submit（A 组无规则文本，B 组附 ACTIVE_RULES）
   │                    └─ answer.md / draft_*.json / receipt.json / events.jsonl
   │
   ├─ audit ────────── audit_answers.py：每个带数值的主张回到确定性产物复算 → source_check.json
   │
   └─ compare ──────── compare_to_literature.py：主张 × 文献结论 → comparison_table.csv
```

组件与现有代码的对应：

| 组件 | 现有位置 | 新位置 | 改动 |
|---|---|---|---|
| 运行器 | `TASK0/runtime/agent_run.py`（146 行）、`container_tools.py`、`finite_checks.py`、`common_prompt.txt`、`C_POLICY.txt`、`check_model.py`、`preflight.py`、3 个 `test_*.py` | `HARNESS/agent_experiments/luna_runtime_v1/` | 凭证改环境变量；加 `--stage profile|analysis`；加 `submit_profile` 工具；挂载前断言无 `hidden/` |
| 选择器 | `WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/scripts/select_review_obligations.py`（431 行） | 不动，只调 | 无 |
| 选择器合约 | 同任务 `outputs/contracts/protein_dynamics_metadata_contract_v0_3_candidate.json`、`review_obligation_selector_output_v1.json`、`outputs/selector_sidecar/rule_selector_index_v0_1.json`、`protein_dynamics_method_scope_v1.json` | 不动，只读 | 无 |
| 规则注册表 | `WS/autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/ruleset/v0_1/rule_registry.tsv`（33 行；列含 `rule_id, paper_id, source_locator, rule_class, gate_path, proposed_project_rule, required_fields, validation_route, abstain_route, transfer_scope`） | 不动，只读 | 无 |
| 编译索引/绑定 | `WS/autoresearch/tasks/dynamics_atlas_cryoem_modality_predicate_repair_20260823/outputs/contracts/compiled_registry_rule_index_v0_3.json`、`registry_bound_typed_bindings_v0_3.json` | 不动 | 无 |
| 桥接脚本 | 无 | `luna_runtime_v1/rules_bridge.py`、`render_active_rules.py`、`derive_public_facts.py`、`render_rubric.py` | 新写 |
| 审计/比对 | `TASK0/outputs/q05_development_source_check.json` 是手工版 | `luna_runtime_v1/audit_answers.py`、`compare_to_literature.py` | 新写，通用化 |
| 案例包 schema | 无 | `luna_runtime_v1/case_package_v1.schema.json`、`validate_case_package.py` | 新写 |
| 容器镜像 | `sha256:d99fa29f…`（含 numpy/pandas/scipy/matplotlib/pillow/sklearn/fitz，DA-20260909-005 已批四项依赖） | 不动 | 无 |

## 3. 阶段 A：建系统（Codex，3 天）

每步格式：**输入 → 动作 → 输出 → 完成标准 → 停止条件**。

### A1 建任务与回执

- 输入：`WS/autoresearch/templates/DYNAMICS_ATLAS_TASK_CONTEXT_RECEIPT_TEMPLATE.md`
- 动作：
  ```bash
  cd "$WS"
  python3 autoresearch/scripts/init_task.py --task-id dynamics_atlas_three_systems_v1_20260910 --goal "建 Rules 回路系统，HSP90/第二/第三体系四站，结果包交 Pro"
  # 填 state/context_receipt.md；task_spec.md 第一行加：anchor: system=ALL station=BUILD
  python3 autoresearch/scripts/validate_dynamics_atlas_context_receipt.py --task-id dynamics_atlas_three_systems_v1_20260910
  ```
- 输出：`WS/autoresearch/tasks/dynamics_atlas_three_systems_v1_20260910/`（下称 `TASK1`）
- 完成：验证器 PASS
- 停止：不 PASS 不进 A2

### A2 分支与搬运

- 输入：`TASK0/runtime/*`
- 动作：
  ```bash
  cd "$HARNESS" && git fetch origin && git worktree add ../dynamics-atlas-harness-luna-runtime-v1 -b feature/luna-runtime-v1 origin/main
  mkdir -p ../dynamics-atlas-harness-luna-runtime-v1/agent_experiments/luna_runtime_v1
  cp "$TASK0"/runtime/{agent_run.py,container_tools.py,finite_checks.py,common_prompt.txt,C_POLICY.txt,check_model.py,preflight.py,test_runner_offline.py,test_submission_maintenance_offline.py} ../dynamics-atlas-harness-luna-runtime-v1/agent_experiments/luna_runtime_v1/
  printf 'Frozen 2026-09-09 development copy. Live code: dynamics-atlas-harness/agent_experiments/luna_runtime_v1/\n' > "$TASK0/runtime/FROZEN_SEE_HARNESS.md"
  ```
  `ACTIVE_RULES_ZH.md`（七段手写规则）不搬。
- 输出：`HARNESS-luna/agent_experiments/luna_runtime_v1/`（下称 `RT`）
- 完成：`PYTHONPATH=$RT python3 -m unittest discover -s $RT -p 'test_*.py'` 通过；`python3 $RT/finite_checks.py` 打印 PASS
- 停止：测试失败修一次，再失败写失败账本

### A3 凭证只读环境变量

- 输入：`RT/agent_run.py` 第 `credential()` 函数（现从 `~/.codex/sessions/2026/08/30/rollout-*.jsonl` 正则抠 key）
- 动作：改为 `os.environ["OPENROUTER_API_KEY"]`，缺失抛 `RuntimeError`；保留 `/api/v1/key` 余额预检 `limit_remaining > 0.08`；写 `RT/test_credential_env_only.py`：未设变量必抛错；设了假值时 `Path.read_text` 不被调用
- 输出：改后的 `agent_run.py`、新测试
- 完成：新测试通过；`grep -rn "codex/sessions" $RT` 为空
- 停止：同 A2

### A4 案例包 schema 与验证器

- 输入：现有两个案例包 `TASK0/cases/Q05`、`TASK0/cases/T4L` 的文件结构
- 动作：写 `RT/case_package_v1.schema.json` 与 `RT/validate_case_package.py`。必含文件：

  | 文件 | 要求 |
  |---|---|
  | `QUESTION.txt` | 非空；不含"请用 X 方法" |
  | `SOURCE_INVENTORY.json` | `files[]`、`source_policy`、`missing`、**新增** `provenance[]`：每个数据文件的 `origin_task`、`origin_path`、`sha256` |
  | `PUBLIC_FACTS.json` | 列表；为空时 `CHECK_SCOPE.txt` 必含字串 `NO_MATCHABLE_RELATION` |
  | `CHECK_SCOPE.txt` | 非空 |
  | `method_sources/SOURCE_MAP.txt` | 非空 |
  | `metadata_profile_v0_3.json` | 阶段 B 起必含；合 v0.3 schema |
  | `hidden/grading_rubric.md`、`hidden/reference_values.json` | 存在；**不挂载** |

  `agent_run.py` 在 `docker run` 前断言 `/source` 挂载源目录下不存在 `hidden`（用 `--exclude`-式的分离目录：案例包 = `cases/<case>/public/` 挂载 + `cases/<case>/hidden/` 不挂载）。
- 输出：schema、验证器、对 Q05/T4L 的验证报告 `TASK1/outputs/legacy_case_validation.json`（只记录，不改历史案例）
- 完成：验证器对一个新建的最小合法案例包返回 0；对缺 `hidden/` 的返回非 0
- 停止：同 A2

### A5 桥接：元数据档 → 义务

- 输入：上游样例 `WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/outputs/case_inputs/selector_repair/lincoff_2020_xeisd_metadata_v0_3.json`
- 动作：写 `RT/rules_bridge.py`：
  ```bash
  python3 "$WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/scripts/select_review_obligations.py" \
    --input cases/<case>/public/metadata_profile_v0_3.json \
    --output cases/<case>/review_obligations.json \
    --receipt cases/<case>/review_obligations_receipt.json \
    --run-id <case>_<utcstamp>
  ```
  路径从 `HARNESS/config/workspace_assets.json` 的 `bundles.protein_dynamics_rules_v0_3.selector_entrypoint` 读；`jsonschema` 失败时把错误写入 receipt 并返回非 0。
- 输出：`review_obligations.json`（字段：`contract_version, run, case_id, output_kind, authority_boundary, obligations[], unresolved_inputs[]`）
- 完成：对 lincoff 样例运行成功，`obligations` 非空
- 停止：同 A2

### A6 义务 → 规则文本 / 公开事实 / 评分模板

- 输入：`review_obligations.json`、`rule_registry.tsv`
- 动作：
  - `render_active_rules.py`：每条 obligation 查注册表 `rule_id` → 输出 `cases/<case>/public/ACTIVE_RULES.md`，每条格式 `**[<rule_id>]** <proposed_project_rule>　必填：<required_fields>　弃权路线：<abstain_route>`。查不到 `rule_id` 的 obligation 写入 `unmapped_obligations.json`，不渲染。
  - `derive_public_facts.py`：从 `metadata_profile_v0_3.json` 的 `evidence_items[].evidence_role ∈ {FITTING, CALIBRATION}` 与 `comparisons[]` 生成 `used_in_fitting` 关系（`result_id, observation_subset, analysis_id, locator`）；从 `time_semantics` 为 `UNORDERED` 且无动力学模型的来源生成 `exclusive_analysis_basis`。输出 `public/PUBLIC_FACTS.json`；为空则在 `CHECK_SCOPE.txt` 写 `NO_MATCHABLE_RELATION`。
  - `render_rubric.py`：每条 obligation 生成一段"正确答案必须区分 / 过强结论 / 合理弃权"，输出 `hidden/grading_rubric.template.md`。
  - 把 `TASK0/runtime/ACTIVE_RULES_ZH.md` 七条逐条对照 33 条注册表 → `TASK1/outputs/seven_rules_registry_mapping.tsv`（列：`hand_rule_no, matched_rule_id_or_NONE, match_basis`）。对不上的进 `candidate_rules_from_20260909.tsv`，不入库。
- 输出：四个脚本 + 映射表
- 完成：`RT/test_rules_bridge_offline.py` 对 lincoff 样例断言：ACTIVE_RULES 每条有 `rule_id`；PUBLIC_FACTS 合 schema；rubric 段数 = obligations 数
- 停止：同 A2

### A7 两阶段运行

- 输入：`RT/agent_run.py`
- 动作：加 `--stage {profile,analysis}`：
  - `profile`：用户提示 = "读 /source，按 /source/metadata_profile_v0_3.schema.json 产出元数据档，用 `submit_profile` 提交"；新工具 `submit_profile(profile: object)`；主进程 `jsonschema` 校验，不过返回错误允许一次修订，两次不过写 `profile_rejected.json` 并 `status=PROFILE_REJECTED`；通过写 `public/metadata_profile_v0_3.json`（若已有则写 `metadata_profile_v0_3.<arm>.json` 供对照）。预算：15 次工具、60000 输入 token、8 分钟。
  - `analysis`：现有流程；B 组用户提示末尾附 `public/ACTIVE_RULES.md`；A 组不附；C 组再附 `C_POLICY.txt`。
- 输出：改后的运行器
- 完成：`RT/test_two_stage_offline.py`（mock 网络与 docker）：不合 schema → 错误 → 合法 → 落盘；`hidden` 不在挂载参数中
- 停止：同 A2

### A8 审计与比对脚本

- 输入：任一 `runs/<run>/draft_*.json` 的 `claims[]`
- 动作：
  - `audit_answers.py --case <case> --run <run>`：抽出 `claims[]` 中含 `quantity` 或数字的主张；对每条，按 `result_id`/`observation_subset`/自然语言中的轨迹 ID，从案例包 `public/` 里的 TSV/JSON 复算（复算规则写在 `cases/<case>/hidden/recompute_rules.py`，每案例一份，冻结）；输出 `source_check.json`：`[{claim_index, claimed_value, recomputed_value, status ∈ {MATCH, MISMATCH, UNVERIFIABLE}, recompute_locator}]`。
  - `compare_to_literature.py --case <case> --run <run>`：把 `claims[]` 与 `hidden/literature_claims.json`（每条：`paper_claim, locator, polarity`）按 `quantity`/关键词对齐，输出 `comparison_table.csv`：`claim_text | paper_claim | locator | relation ∈ {AGREE, DISAGREE, PAPER_SILENT, AGENT_ABSTAIN} | audit_status | rule_ids_cited`。对齐不到的行 `relation=UNALIGNED`，不猜。
- 输出：两个脚本 + `RT/test_audit_offline.py`
- 完成：用 Q05 的历史 `draft_1.json` 与 `q05_development_source_check.json` 做回归：methyl 最大超限复算为 2.75049、C 组主张标 MISMATCH
- 停止：同 A2

### A9 系统级检查与提交

- 动作：
  ```bash
  PYTHONPATH=$RT python3 -m unittest discover -s $RT -p 'test_*.py' -v   # 全部运行器测试，1 次
  cd "$HARNESS-luna" && PYTHONPATH=src python3 -m unittest discover -s tests   # 现有 harness 套件，1 次；不得变红
  ```
  写 `RT/README.md`（组件、命令、边界）。按 `CONTRIBUTING.md` 十节结构开 Draft PR（PM 授权 3）。
- 完成：两套测试全过；PR 打开
- 停止：harness 现有测试变红 → 找出是搬运引入还是既有 → 修一次

**阶段 A 验证预算：** 单测 3 次（A2、A8 后各 1，A9 全量 1）+ harness 套件 1 次；独立审阅 0（Pro 在 §5 审整个系统）；哈希 0。

## 4. 阶段 B：HSP90 四站（Codex，5 天，≤ $0.40）

### B0 前置：MD 方法档（开发 proposal）

- 输入：`WS/autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725/outputs/HSP90_END_TO_END_REPORT.md`（第 19–38 行：Zenodo 6606744、40 条、3352 原子、1021 帧、dt 1000 ps、1.0 μs、力场声明 AMBER99SB vs 目录 `amber14sb_OL15.ff` 矛盾、1021 vs 1001 帧矛盾）；`archive_inventory.json`
- 动作：写 `TASK1/outputs/md_trajectory_method_profile_proposal_v1.json`，七字段（8/24 计划 §4）：`trajectory_topology_provenance, saved_frame_interval_and_window, equilibration_statement, independent_repeats, observable_and_representation, condition_construct, requested_claim_and_forbidden_upgrade`，每字段附取值与来源行号；两处矛盾原样写入 `provenance_conflicts[]`。标签 `DEVELOPMENT_PROPOSAL_NOT_HUMAN_REVIEWED`。选择器调用时通过 `--method-scope` 传一个**副本** `protein_dynamics_method_scope_v1.dev_md.json`（原文件 + 该 proposal），原文件不改。
- 输出：proposal + method scope 副本
- 完成：副本合 method scope 自身 schema；`MD_TRAJECTORY` 在副本中状态为 `DEVELOPMENT_PROPOSAL`
- 停止：无

### B1（S1）数据盘点 → 一页 landscape + A1 元数据卡

- 输入：14 个 hsp90 任务的 `outputs/`；具体取：

  | 文件 | 内容 | 用途 |
  |---|---|---|
  | `dynamics_atlas_hsp90_acquisition_20260725/outputs/archive_inventory.json`、`HSP90_END_TO_END_REPORT.md` | Zenodo 归档、40 条轨迹元数据、provenance 矛盾 | 元数据卡 |
  | `dynamics_atlas_hsp90_time_anatomy_v0_20260730/outputs/trajectory_time_anatomy.tsv`（121 行：`trajectory, seed_lineage, persistence_saved_frames, persistence_ns, first_persistent_direction, first_persistent_start_ns, opposite_direction_departure_candidate, opposite_departure_start_ns, return_candidate, return_start_ns, strict_core_frames`） | 每条轨迹的停留/转向/回返 | A3 |
  | 同任务 `trajectory_time_bins_50ns.tsv`（841 行，50 ns 分箱路线）、`directional_runs.tsv`（1176 行，方向段） | 时间进程 | A3、A4 |
  | `dynamics_atlas_hsp90_coverage_stability_v0_20260730/outputs/trajectory_anchor_proximity.tsv`（81 行：到 NMR anchor 的最小/中位距离）、`prefix_horizon_routes.tsv`（201 行：逐步延长前缀窗口的路线） | 覆盖与收敛 | A4、A5 |
  | 两任务的 `results_summary.json`（含 `statistical_unit, allowed_wording, forbidden_wording`） | 允许/禁止措辞 | rubric |
  | `dynamics_atlas_hsp90_multimodal_reconstruction_v1_20260729/outputs/multimodal_evidence_bundle.json`、`reveal_comparison.tsv` | 已做过的论文比对 | S4 对照 |
  | `dynamics_atlas_hsp90_projection_core_clarity_v0_20260801/outputs/figure_manifest.json` | 图清单 | 报告引用 |

- 动作：写 `TASK1/outputs/HSP90_DATA_LANDSCAPE.md`（一页：三套 HSP90 分清——人 HSP90α NTD 40 MD + 2 NMR ensemble + CPMG；酵母 Hsp90 smFRET 另一分支；本计划只用第一套）和 `HSP90_SOURCE_AND_RUN_CARD.json`（Soojung 5.2 五项：帧数、间隔、总时长、溶剂、条件；加力场与帧数矛盾）。`inventory_hsp90.py` 复制上表文件到 `TASK1/cases/HSP90_shared/public/data/`，写 `SOURCE_INVENTORY.json` 的 `provenance[]`（origin_task、origin_path、sha256）。
- 输出：landscape、卡、`HSP90_shared/public/`（预计 < 5 MB）
- 完成：`provenance[]` 每条 sha256 与源文件一致（1 次检查）
- 停止：任一源文件缺失 → 写入 `missing`，不现算

### B2（S2）比较论文与三个问题

- 输入：Henot 2022 本地 PDF `WS/autoresearch/tasks/dynamics_atlas_hsp90_feasibility_20260725/inputs/henot_2022_hsp90_{article,supplement}.pdf`；阅读笔记 `WS/literature/reading_notes/PAPERFORGE_2022_HENOT_HSP90.md`；主张矩阵 `WS/autoresearch/tasks/dynamics_atlas_hsp90_paper_comparison_20260729/outputs/HSP90_PAPER_ATLAS_CLAIM_MATRIX.md`；20 题中 Q01 原文 `WS/autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904/outputs/20个论文结果验证问题.md` 第 51–73 行
- 动作：建三个案例包，共享 `HSP90_shared/public/data/`：

  | 案例 | `QUESTION.txt` | `hidden/literature_claims.json` 来源 | rubric 验收（Soojung 7/28） |
  |---|---|---|---|
  | `HSP90_Q01_transitions` | Q01 原文："在无配体的人 HSP90α NTD 中，从闭合 ATP-lid 起始的轨迹是否比开放起始轨迹更容易离开原有构象，并出现闭合到开放的转变？请利用给定数据实际核对，说明分析、结果及限制。方法由你选择。" | Henot 2022 Fig. 4a–g；Results "The ATP-lid closed state is a metastable excited state"；主张矩阵对应行 | A3：能区分 stay / transition / excursion / unresolved；不得称单向转变为 equilibrated |
  | `HSP90_convergence` | "用逐步延长观察窗口的方法，判断哪些量（每条轨迹的状态归属、到 NMR anchor 的距离、open/closed 比例）在多长窗口内稳定。现有 40 条 1 μs 轨迹是否足以支持 open/closed population ratio？说明依据与限制。" | Henot 2022 Fig. 5b–c 的 CPMG 占比只作对照，不作为答案；`results_summary.json` 的 forbidden_wording | A4：不足时明确阻止 population claim |
  | `HSP90_coverage` | "NMR ensemble 定义的构象空间覆盖了 MD 访问区域的哪部分？MD 是否采到 NMR 没有的区域？PCA basis 由 NMR 定义时，MD 的分布外点会不会被压缩？给出不确定性与方法敏感性。" | 40 轨迹原论文 landscape 图（Zenodo 6606744 关联论文；locator 由 Codex 从 END_TO_END_REPORT 抽出）；`reveal_comparison.tsv` | A5：有 uncertainty 与 method sensitivity |

  `hidden/grading_rubric.md` = A6 的模板 + 上表验收 + `results_summary.json` 的 allowed/forbidden wording。`hidden/reference_values.json` 由 `inventory_hsp90.py` 直接从 TSV 读出（如每条轨迹 `first_persistent_direction`、`persistence_ns`），不做新计算。`hidden/recompute_rules.py` 写明每类数值如何从 TSV 复算。
  Q02（CPMG 交换速率）不做——需要拟合 CPMG 原始数据，属新科学计算。
- 输出：三个案例包
- 完成：`validate_case_package.py` 三包全 0（1 次）
- 停止：无

### B3（S3a）零费用：从已有记录算 V2a 指标

- 输入：harness 分支 worktree `WS/dynamics-atlas-harness-live-agent-common-flows-v1/`：
  - 人冻结参考 `agent_experiments/v1/sealed_references/profiler_reference_v1.json`；输入 `agent_experiments/v1/workspaces/hsp90_profiler/input.json`
  - MiniMax 8/30 proposal `evidence/live_agent_common_flows_v1/development_runs/authorized_planner_from_frozen_hsp90_minimax_repair1_20260830/trial-1/inputs/profile_proposal.json`
  - Luna 8/30 失败调用解析稿 `evidence/live_agent_common_flows_v1/development_runs/authorized_planner_from_frozen_hsp90_luna_20260830/trial-1/failed_live_calls/profiler/parsed_model_proposal.json`
  - 本地 qwen 记录 `agent_experiments/v1/recorded/qwen2_5_1_5b_20260826_*/hsp90_profiler/proposal.json`
- 动作：写 `TASK1/scripts/v2a_metrics_from_recorded.py`：把每份模型 proposal 与人冻结参考各自过 A5 的桥接（同一选择器、同一 dev method scope），按 8/24 计划 §6 八项打表：可解析、对象身份（NMR 与 MD 是不同 SOURCE）、字段准确（method/modality/role/claim level/EDGE endpoints 逐字段对比）、未知处理、**义务一致**（mandatory obligation 集合的 Jaccard 与差集）、**错目标率**（发给错误 SOURCE/EDGE 的 obligation 数）、claim 安全（是否出现 population/kinetics/free energy/mechanism 字样）、人工修正量（本轮记 N/A）。
- 输出：`TASK1/outputs/v2a_metrics_recorded.csv` + `v2a_metrics_recorded.md`
- 完成：每份 proposal 一行，八列有值或 `N/A` 并注明原因
- 停止：选择器对人冻结参考本身报错 → 先修 B0 的 dev method scope，不改参考

### B4（S3b）Agent 起草元数据档

- 输入：三案例包
- 动作：`OPENROUTER_API_KEY` 由 PM 注入当前 shell；对 `HSP90_shared` 跑 `agent_run.py HSP90_Q01_transitions A --stage profile --image sha256:d99fa29f…` 与 `… B --stage profile`（B 组在 profile 阶段与 A 相同，只为观察波动），共 2 次，≤ $0.05。两份写 `metadata_profile_v0_3.A.json`、`.B.json`。取通过 schema 的第一份为 `metadata_profile_v0_3.json`；两份都不过 → 停，写 `profile_rejected.json`，进 §5 结果包报告"Agent 无法产出合法元数据档"（这本身是决定性结果）。
- 输出：元数据档 + 两份对照稿 + 与 B3 人冻结参考的字段差异 `profile_diff_vs_reference.json`
- 完成：`metadata_profile_v0_3.json` 合 schema；A5 桥接对其成功产出 `review_obligations.json`
- 停止：如上

### B5（S3c）生成义务、规则文本、公开事实、rubric；冻结

- 动作：对三案例各跑 A5、A6。写 `freeze_hsp90.py`：三案例包 `public/` + `hidden/` + `RT/` + 三份 `review_obligations.json` 的 SHA-256 → `TASK1/outputs/frozen_hsp90_v1.json`，含 `model: openai/gpt-5.6-luna, reasoning: medium, image: sha256:d99fa29f…, run_order（随机化）, budget_usd: 0.35`。本阶段唯一一次哈希。
- 完成：`PUBLIC_FACTS.json` 三份存在（可为空并带 `NO_MATCHABLE_RELATION`）；冻结文件写出
- 停止：无

### B6（S3d）运行

- 组别：A（无规则文本）、B（附 `ACTIVE_RULES.md`）；C 仅当某案例 `PUBLIC_FACTS.json` 非空时启用（= B + `finite_checks`）。
- 规模：3 案例 × {A,B} × 2 次 = 12 次（C 启用则 +2/案例）。
- 动作：
  ```bash
  python3 $RT/run_batch.py --freeze "$TASK1/outputs/frozen_hsp90_v1.json" --budget-usd 0.35 --runs-dir "$TASK1/runs"
  ```
  `run_batch.py` = 现 `run_development_batch.py` 加 `--freeze/--budget-usd/--runs-dir` 参数；每次前检查 `UNKNOWN_CHARGE.json`；每次后写 `results.json` 一行。
- 输出：每次 `answer.md, draft_*.json, receipt.json, events.jsonl`；`TASK1/outputs/hsp90_results.json`
- 完成：12 次 receipt 齐；`results.json` 与 receipt 交叉一致（1 次检查）
- 停止：`UNKNOWN_CHARGE.json` 出现 → 停不重试；累计 > $0.35 → 停；运行器 bug 导致 `EXECUTION_ERROR` → 修一次只补跑该次，已跑的不删

### B7（S4）审计与比对

- 动作：对 12 次每次跑 `audit_answers.py` 与 `compare_to_literature.py`。汇总 `TASK1/outputs/hsp90_comparison_all.csv`（12 × 主张行）和 `hsp90_arm_diff.md`：逐案例列 B 相对 A **多说的主张 / 少说的主张 / 说错的主张（audit MISMATCH）/ 引用的 rule_id**。不计数、不设阈值。
- 输出：两个汇总文件；`HSP90_V1_SCIENTIFIC_CHARACTERIZATION_ZH.md` + HTML（八节：元数据五项；A3 状态时间线；A4 收敛与 population 是否允许；A5 覆盖与敏感性；可信/不可信；Agent 贡献与错误；B−A 差异；未解决与下一步）；`REPLAY.md`（命令、哈希、提示原文、确定性/LLM 边界、换 packet 要改哪些文件）
- 完成：报告中每个数字在 `source_check.json` 里 `MATCH`；`MISMATCH`/`UNVERIFIABLE` 的数字不出现在正文，只出现在"Agent 错误"节
- 停止：无

**阶段 B 验证预算：** 检查 4 次（B1 哈希一致、B2 案例包、B6 交叉核对、B7 审计脚本）；哈希 1 次（B5）；独立审阅 0——Pro 在 §5 审。

## 5. 阶段 C：Pro 审查包 #1（HSP90 + 系统）

- 内容目录 `TASK1/outputs/pro_review_1/`：
  1. `00_README.md`：包内容、如何读、边界声明（开发暴露、未领域确认）
  2. `01_SYSTEM.md`：§2 架构图 + 组件表 + 测试结果（A9 输出）+ `REPLAY.md`
  3. `02_V2A_METRICS.md`：B3 八项表 + B4 的 Agent 元数据档与人冻结参考的字段差异
  4. `03_HSP90_REPORT.md`：B7 报告
  5. `04_COMPARISON.csv`、`05_ARM_DIFF.md`、`06_SOURCE_CHECK.json`
  6. `07_RAW/`：12 份 `answer.md` + `receipt.json`（不含 events，太大；按需提供）
  7. `08_PROMPT_FOR_PRO.md`（下）
- `08_PROMPT_FOR_PRO.md` 要 Pro 回答（每条要求给出可执行判断）：
  1. 系统：Rules 选择器是否真的在回路里？元数据档 → 义务 → 规则文本/检查/评分 的链条哪一环可以被绕过？
  2. V2A 指标：模型元数据档与人冻结档的义务一致性如何解读？哪类字段错误最致命？
  3. HSP90 三题：哪些主张与 Henot 2022 一致、哪些不一致、哪些过强？报告正文有没有 audit 没过的数字混进来？
  4. B−A 差异：逐条看，B 多说/少说/说错的东西里，哪些能归因到具名 `rule_id`，哪些不能？
  5. 下一体系：按 §6 决定规则选 ADK 还是 DHFR？规则本身是否合理？
  6. 一句话：这个系统现在值得继续建，还是应该停在 HSP90？
- 处置：Pro 回复存 `pro_review_1/reply.md`；Codex 写 `disposition.json`：每条意见 `{finding, action ∈ {FIX, RECORD, REJECT}, reason, changed_files}`。`FIX` 类只修一次，重跑受影响的审计/比对，不重跑模型。Pro 意见不改变任何结论的 claim ceiling。
- 完成：`disposition.json` 覆盖 Pro 每条意见

## 6. 阶段 D：第二体系只读盘点（Codex，2 天，0 模型费用）

对 ADK 与 DHFR **各**产出 `TASK1/outputs/<SYS>_DATA_LANDSCAPE.md`，字段固定：

| 节 | 具体查什么 | 记录字段 |
|---|---|---|
| D1 结构 | RCSB 检索：ADK 用 `adenylate kinase Escherichia coli`（已知 1AKE 闭、4AKE 开、1E4V G10V 本地已有 Cα）；DHFR 用 `dihydrofolate reductase Escherichia coli`（候选：1RX2、1RA9、5DFR 等，需核实） | `pdb_id, ligand, resolution, conformational_state_label(paper), download_ok` |
| D2 MD 数据集 | ATLAS（`https://www.dsimb.inserm.fr/ATLAS/`）按 PDB ID 查；mdCATH 按 CATH domain ID 查；MegaSim；Zenodo 关键词 `adenylate kinase molecular dynamics` / `DHFR molecular dynamics trajectory` | `dataset, id, n_traj, length, interval, solvent, download_size, license` |
| D3 NMR | BMRB 检索；文献候选（需核实）：ADK — Henzler-Wildman 2007 Nature（松弛/MD）、Wolf-Watz 2004 NSMB；DHFR — Boehr 2006 Science（CPMG）、Bhabha 2011 | `bmrb_id_or_paper, observable(CPMG/relaxation/NOE/RDC), condition, raw_data_available` |
| D4 HDX-MS / 稳定性 | 文献候选：DHFR HDX-MS 局部暴露、ΔG_open（Soojung 点名）；ADK HDX-MS | `paper, observable, per-residue_data_available, condition` |
| D5 模态比较论文 | 每体系 1–3 篇，含明确可比对结论 | `paper, doi, compared_modalities, conclusion_one_sentence, locator(fig/section)` |
| D6 方法范围缺口 | 对照 `protein_dynamics_method_scope_v1.json` 13 个 method_id：静态端点结构最接近 `CANDIDATE_ENSEMBLE`（需确认）；HDX 无对应；NMR_* 已注册 | `needed_method_id, status ∈ {REGISTERED, NEEDS_DEFINITION}` |

盘点只记录，不下载大文件、不分析、不写元数据档。Agent 可用于起草清单（≤ $0.05），每条由 Codex 用 URL 可达性核实。

**决定规则（现在写死）：** 选同时满足 (a) 至少一个可直接下载、无需新模拟的数据集，覆盖 ≥ 2 种模态；(b) ≥ 1 篇比较论文有可比对结论；(c) 所需 method_id 已注册或最多需 1 个新定义 的体系。两者都满足 → ADK（部分资产已在本地：`HARNESS-openrouter/evidence/paper_blind_exposed_v1/frozen_inputs/adk/{1AKE,4AKE}_chain_A_ca.npy`，1E4V）。都不满足 → 写 `second_system_decision.json` 状态 `NEITHER_QUALIFIES`，进 Pro 审查包 #2 作为结果，不硬选。
输出 `TASK1/outputs/second_system_decision.json`：`{chosen, rule_a, rule_b, rule_c, evidence_paths}`。

## 7. 阶段 E：第二体系四站（Codex，5 天，≤ $0.40）

与阶段 B 同构，参数化：

| 步 | 与 HSP90 的差异 |
|---|---|
| E0 方法档 | ADK 若用静态端点 + NMR：确认 `CANDIDATE_ENSEMBLE` 是否适用，否则起草 `STATIC_ENDPOINT_STRUCTURES` 开发 proposal；DHFR 若用 HDX-MS：起草 `HDX_MS` 开发 proposal。同 B0 方式走副本 |
| E1 盘点 | 用 D 阶段结果；下载 D 中标记 `download_ok` 的数据（授权 4）；`SOURCE_INVENTORY.provenance[]` 记 URL + sha256 |
| E2 问题 | 从 D5 比较论文的结论反写 1–3 个问题；`literature_claims.json` 直接来自 D5 locator。问题形态固定为："同一体系的两类观测是否支持同一种结构解释；资料能排除哪些其他解释" |
| E3 记录指标 | 若有 8/30 ADK proposal（`evidence/paper_blind_exposed_v1/agent_runs/profiler/adk_proposal.json`，当时 core FAIL），同样过 B3 脚本 |
| E4–E7 | 同 B4–B7；预算 $0.35 |

进入前置条件：Pro 审查包 #1 的 `disposition.json` 完成；`second_system_decision.json` 非 `NEITHER_QUALIFIES`。

## 8. 阶段 F–G：Pro 审查包 #2、第三体系、汇总

- F：同 §5 结构，多一节 `09_REPLAY_CHECK.md`：换 packet 改了哪些文件（预期只有 `cases/<sys>/`），代码是否改动（预期无；有则列出并说明）。
- G：第三体系 = D 阶段剩下的那个；若其 D 阶段结论是不满足决定规则，则 G 阶段只做 E0–E1（补数据与方法档）并把"为何不能进四站"写成结果；不硬跑。
- 汇总 `THREE_SYSTEMS_SUMMARY_ZH.md`：三体系 × {问题数、运行数、audit MATCH 率、与文献 AGREE/DISAGREE/SILENT 计数、B−A 具名差异条数、费用}；Rules 系统在三个回路里的行为记录；Pro 三轮意见的处置汇总。交 Pro 审查包 #3。

## 9. 跑偏检测器与禁止清单

**每周一次 `python3 TASK1/scripts/drift_check.py`**：读本周修改过的 `autoresearch/tasks/*/state/task_spec.md`，要求首行 `anchor: system=<HSP90|ADK|DHFR|ALL> station=<BUILD|S1|S2|S3|S4|PRO_REVIEW>`；缺失或值域外的任务列出。同时打印本周：新建案例包数、新建题目数、注册表 diff 行数、向 Pro 发送次数与对应新 artifact 路径。任一异常 → 停，报 PM。

**禁止：** 新题库（Q03–Q20 不动）；改 33 条注册表；A/B/C 作主线（B−A 差异只作副产物逐条记录）；无新 artifact 的 Pro 请求；并行两个体系；称公开数据 held-out；Agent 现场 pipeline 直接当最终分析（每个数字必须 `recompute_rules.py` 复算 MATCH）；新 MD、装依赖、充值、换模型。

## 10. 预算与时间

| 阶段 | 天 | 模型费用 | 检查命令 | 哈希 | Pro 审查 |
|---|---|---|---|---|---|
| A 建系统 | 3 | 0 | 4 | 0 | 0 |
| B HSP90 | 5 | ≤ $0.40 | 4 | 1 | 0 |
| C 审查包 #1 | 1 | 0 | 0 | 0 | 1 |
| D 盘点 | 2 | ≤ $0.05 | 2（URL 可达性 ×2 体系） | 0 | 0 |
| E 第二体系 | 5 | ≤ $0.40 | 4 | 1 | 0 |
| F 审查包 #2 | 1 | 0 | 0 | 0 | 1 |
| G 第三体系 + 汇总 | 6 | ≤ $0.40 | 4 | 1 | 1 |
| **合计** | **23 工作日** | **≤ $1.25**（上限 $1.50） | **18** | **3** | **3** |

每阶段结束写 `TASK1/state/validation_ledger.jsonl` 一条：计划的检查、实际跑的、跳过的及理由。

## 11. 治理（Codex 起草，PM 随授权清单一次确认）

- `DYNAMICS_ATLAS_STATUS.md` 新快照：下一阶段 = 本计划；四来源 24 份比较停放；`NEXT_SCIENTIFIC_STEP_ZH.md` 标 superseded。
- Decision Log 一条：PM 授权 §1 五项；采纳本计划；Pro 审查替代领域审查的边界声明。
- PR #26 加评论指向本文；不合并。

## 12. 失败账本

任一步两次修补仍失败：停止编辑，写 `TASK1/outputs/failure_ledger_<step>.md`（尝试的修法、预期机制、实际结果、假设为何变弱、重复了什么假设、下一个替代假设），进最近一次 Pro 审查包。
