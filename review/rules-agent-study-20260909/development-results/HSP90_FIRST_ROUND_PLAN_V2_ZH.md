# HSP90 首轮：一个科学问题、四份答复、有界交付

> **SUPERSEDED BY v3（2026-09-09 深夜）。** Pro 对本版的审查见 `PRO_REVIEW_OF_PLAN_V2_ZH.md`；交付版见 `HSP90_FIRST_ROUND_PLAN_V3_ZH.md`。本文件保留为记录，不再执行。


Dynamics Atlas · 2026-09-09 · v2 · **供 Codex 逐步执行** · 审阅者见文末 `REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md`

> v2 替代 `THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md`（v1）。v1 的三体系六周承诺、通用评分生成、通用文献比对、V2a 旧记录汇总、`drift_check.py` 全部停放。修改依据是 `PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md`，逐条处置见 §11。
> 路径约定：`WS` = 本地工作区根目录（本仓库上级目录，不在 git 内）；`HARNESS` = `WS/dynamics-atlas-harness`；`TASK0` = `WS/autoresearch/tasks/dynamics_atlas_rules_incremental_value_protocol_20260909`；`TASK2` = 本轮新任务目录（A1 建）。

## 0. 本阶段做什么

**本阶段先利用现有 Agent 和已保存的 HSP90 资料，完成一项有明确方法与来源的科学分析，并观察加入现有规则提示后，答案是否得到实质改善。科学评价独立于规则选择结果。完成后由负责人根据科学结果、人工介入和复用成本决定是否进入第二体系；第三体系不作承诺。Pro 提供咨询审阅，不替代领域结论或负责人的投入决定。**

一句话交付物：**一份 HSP90 ATP-lid 有限时间构象变化的科学答复**（Q01），来自同一个已有 Agent 在同一份资料上的四次运行（A 组无规则提示 ×2，B 组附注册表选出的规则提示 ×2），附原始交付、核对记录、与 Henot 2022 的逐主张关系表，以及"规则提示改变了什么"的逐条记录。

**明确不做：** C 组；第二、第三体系；PCA 覆盖题（除非 B1 确认坐标与变换已在本机）；通用评分/比对脚本；从模型元数据推公开事实；V2a 旧记录汇总；换模型、充值、新 MD、改 33 条注册表、新题库。

**到期规则：** Codex 开工后 **7 个工作日**内必须交出 §8 的报告，或交出失败原因；框架未完善不是续期理由。

## 1. PM 一次性授权 **[开工前一次签]**

| 项 | 内容 |
|---|---|
| 1 | 模型费用上限 **$0.20**（四次分析 + 可选一次元数据起草）；`UNKNOWN_CHARGE.json` 出现即停 |
| 2 | 在运行 shell 提供 `OPENROUTER_API_KEY`；Codex 不从任何文件读 key |
| 3 | 允许 `feature/luna-runtime-v1` 分支 commit / push / Draft PR；`runs/`、案例数据、凭证不入库 |
| 4 | 允许把 `MD_TRAJECTORY` 最小方法档作为开发 proposal 经**副本** method scope 送入选择器；原文件不改；标签 `DEVELOPMENT_PROPOSAL_NOT_HUMAN_REVIEWED` |

PM 回复"授权 1–4"后，Codex 写 Decision Log 一条并开工。本轮不需要下载任何外部数据。

## 2. 系统：只补首轮必需的四件事

```text
cases/HSP90_Q01/
  common/        → 挂载为 /source（A、B 都可读）：问题、数据、元数据卡、论文 MD、来源清单
  arm_B/         → 不挂载；ACTIVE_RULES.md 只以文本附进 B 组用户提示
  hidden/        → 不挂载；科学评分依据、参考值、复算规则、规则覆盖记录
```

| 改动 | 现状 | 做什么 | 不做什么 |
|---|---|---|---|
| 凭证 | `TASK0/runtime/agent_run.py` 的 `credential()` 从 `~/.codex/sessions/…/rollout-*.jsonl` 正则抠 key | 只读 `os.environ["OPENROUTER_API_KEY"]`，缺失抛错；保留余额预检 | 不写任何回退 |
| 挂载分离 | `/source` = 整个案例目录 | `/source` 只挂 `common/`；`docker run` 前断言 `common/` 下无 `hidden`、无 `ACTIVE_RULES*`；B 组规则文本从 `arm_B/ACTIVE_RULES.md` 读入并附到用户提示末尾 | 不新建隔离框架 |
| 窄规则桥接 | 无 | `rules_bridge.py`：读 Codex 手写的 `metadata_profile_v0_3.json` → 调上游选择器（只读）→ `review_obligations.json` → `render_active_rules.py` 查 `rule_registry.tsv` 渲染 `arm_B/ACTIVE_RULES.md`（每条带 `rule_id`）；文首加一句"以下为分析提醒，可质疑；与资料冲突时以资料为准并说明" | 不从元数据推公开事实；不生成评分模板 |
| 预算参数化 | `agent_run.py` 每次请求前已做 `spent + reserve > 3` 预留检查 | 把 3 改为 `--budget-usd`；`run_batch.py` 加 `--freeze/--budget-usd/--runs-dir` | 不改预算逻辑 |

`finite_checks.py`、`C_POLICY.txt` 原样搬运但本轮不调用。

## 3. 阶段 A：系统修正（Codex，2 天）

格式：**输入 → 动作 → 输出 → 完成标准 → 停止条件**。

### A1 建任务
- 动作：
  ```bash
  cd "$WS"
  python3 autoresearch/scripts/init_task.py --task-id dynamics_atlas_hsp90_first_round_v2_20260910 --goal "HSP90 Q01 有界首轮：同一 Agent、A/B 各两次、独立科学评价、两层报告"
  # 填 state/context_receipt.md；task_spec.md 首行：anchor: system=HSP90 question=Q01 round=1
  python3 autoresearch/scripts/validate_dynamics_atlas_context_receipt.py --task-id dynamics_atlas_hsp90_first_round_v2_20260910
  ```
- 输出：`TASK2`
- 完成：验证器 PASS。停止：不 PASS 不进 A2。

### A2 分支与搬运
- 动作：
  ```bash
  cd "$HARNESS" && git fetch origin && git worktree add ../dynamics-atlas-harness-luna-runtime-v1 -b feature/luna-runtime-v1 origin/main
  RT=../dynamics-atlas-harness-luna-runtime-v1/agent_experiments/luna_runtime_v1; mkdir -p $RT
  cp "$TASK0"/runtime/{agent_run.py,container_tools.py,finite_checks.py,common_prompt.txt,C_POLICY.txt,check_model.py,preflight.py,run_development_batch.py,test_runner_offline.py,test_submission_maintenance_offline.py} $RT/
  printf 'Frozen 2026-09-09 development copy. Live code: dynamics-atlas-harness/agent_experiments/luna_runtime_v1/\n' > "$TASK0/runtime/FROZEN_SEE_HARNESS.md"
  ```
- 完成：`PYTHONPATH=$RT python3 -m unittest discover -s $RT -p 'test_*.py'` 通过；`python3 $RT/finite_checks.py` 打印 PASS。
- 停止：失败修一次；再失败写失败账本（§12）。

### A3 凭证
- 动作：改 `credential()`；写 `test_credential_env_only.py`（未设变量必抛 `RuntimeError`；设假值时 `pathlib.Path.read_text` 未被调用）。
- 完成：新测试过；`grep -rn "codex/sessions" $RT` 为空。

### A4 挂载分离
- 动作：`agent_run.py` 的 `source=(ROOT/'cases'/case/'common')`；启动前 `assert not (source/'hidden').exists() and not list(source.glob('ACTIVE_RULES*'))`；B 组：`user += '\n\n' + (ROOT/'cases'/case/'arm_B'/'ACTIVE_RULES.md').read_text()`。写 `test_mount_isolation_offline.py`：mock docker，断言 `-v` 参数只含 `common/`；A 组消息里不含 `rule_id` 字样，B 组含。
- 完成：测试过。

### A5 窄规则桥接
- 输入：上游样例 `WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/outputs/case_inputs/selector_repair/lincoff_2020_xeisd_metadata_v0_3.json`；注册表 `WS/autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/ruleset/v0_1/rule_registry.tsv`
- 动作：`rules_bridge.py`：
  ```bash
  python3 "$WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/scripts/select_review_obligations.py" \
    --input cases/<case>/hidden/metadata_profile_v0_3.json --output cases/<case>/hidden/review_obligations.json \
    --receipt cases/<case>/hidden/review_obligations_receipt.json --run-id <case>_<utc> \
    --method-scope cases/<case>/hidden/method_scope_dev_copy.json
  ```
  `render_active_rules.py`：每条 obligation 查 `rule_id` → `**[<rule_id>]** <proposed_project_rule>　必填：<required_fields>　弃权路线：<abstain_route>`；查不到的写 `hidden/unmapped_obligations.json`，不渲染。
- 输出：`arm_B/ACTIVE_RULES.md`
- 完成：`test_rules_bridge_offline.py` 对 lincoff 样例：obligations 非空，渲染每条含 `rule_id`。
- 说明：本轮 B 组规则来自旧注册表 + 旧选择器，是**复用选择**，不是它比 9 月 9 日的七条指导更科学的证明。七条与注册表的对照表 `TASK2/outputs/seven_rules_registry_mapping.tsv` 只作记录。

### A6 预算参数化与批处理
- 动作：`--budget-usd`；`run_batch.py --freeze <json> --budget-usd <x> --runs-dir <dir>`，每次前检查 `UNKNOWN_CHARGE.json`，每次后追加 `results.json`。
- 完成：`test_runner_offline.py` 增加一个预算超限即 `COST_LIMIT` 的用例，过。

### A7 收口
- 动作：全部运行器测试 1 次；`cd $HARNESS-luna && PYTHONPATH=src python3 -m unittest discover -s tests` 1 次（不得变红）；写 `RT/README.md`；开 Draft PR（授权 3）。
- 阶段 A 验证预算：单测 2 次 + harness 套件 1 次；审阅 0；哈希 0。

## 4. 阶段 B：HSP90 Q01 案例（Codex，2 天）

### B0 原文对齐：修正旧报告，不再沿用假矛盾
- 输入：Henot 2022 原文 `WS/autoresearch/tasks/dynamics_atlas_hsp90_feasibility_20260725/inputs/henot_2022_hsp90_article.pdf`（方法节第 560、584–587、603 行附近：**ff14SB**；**1020 ns，前 20 ns 平衡，分析后 1000 ns，每 1 ns 存**；"20 020 snapshots"= 20 × 1001）；旧报告 `WS/autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725/outputs/HSP90_END_TO_END_REPORT.md` 第 19–38 行（写"AMBER99SB vs `amber14sb_OL15.ff` 矛盾"、"1021 vs 1001 帧矛盾"）
- 动作：写 `TASK2/outputs/HSP90_SOURCE_AND_RUN_CARD.json`：
  - `force_field`: `ff14SB`（原文）；目录 `amber14sb_OL15.ff` 与之一致；`note`: 旧报告的 AMBER99SB 为报告错误，出处待查（Zenodo 描述或误抄），**不再称为矛盾**。
  - `frames`: 本地 XTC 1021 帧 = 0–1020 ns 全程；作者 `.dat` 1001 行 = 后 1000 ns。**验证**：用现有 `archive_inventory.json` 或 MDAnalysis 只读一条轨迹的时间数组（首帧、末帧、步长；不做任何分析），写入 `time_axis_check`。无法读取则记 `UNRESOLVED`，仍不称矛盾。
  - Soojung 5.2 五项：帧数、间隔（1 ns）、总时长（1.02 μs，分析窗口 1.0 μs）、显式水、170 mM NaCl（来自旧报告，标来源）。
  - `analysis_window_note`: Agent 若用全部 1021 帧，需自行说明是否剔除前 20 ns。
- 同时写 `hidden/md_trajectory_method_profile_proposal_v1.json`（8/24 计划 §4 七字段，取值引用本卡）与 `hidden/method_scope_dev_copy.json`（原 method scope + 该 proposal，`MD_TRAJECTORY` 标 `DEVELOPMENT_PROPOSAL`）。
- 完成：卡内每个字段有 `source`（原文行号 / 文件路径）；副本合 method scope schema。

### B1 数据盘点与 `common/`
- 输入候选（Codex 逐一确认存在并记录；找不到就记 `missing`，**不现算**）：

  | 文件 | 内容 | 放入 common/ |
  |---|---|---|
  | `WS/autoresearch/tasks/dynamics_atlas_hsp90_time_anatomy_v0_20260730/outputs/trajectory_time_anatomy.tsv`（121 行；列 `trajectory, seed_lineage, persistence_saved_frames, persistence_ns, first_persistent_direction, first_persistent_start_ns, opposite_direction_departure_candidate, opposite_departure_start_ns, return_candidate, return_start_ns, strict_core_frames`） | 旧流程的逐轨迹分类 | 是，**并附字段定义文件** `FIELD_DEFINITIONS.md`（从该任务 `results_summary.json` 与 `figure_captions_and_claim_boundaries.md` 抽出每列的判据与阈值） |
  | 同任务 `trajectory_time_bins_50ns.tsv`（841 行）、`directional_runs.tsv`（1176 行） | 50 ns 分箱路线、方向段 | 是 |
  | **逐帧序列**（每条轨迹每帧到开/闭参照的距离或 state-margin）：在 `dynamics_atlas_hsp90_v1_science_20260728`、`dynamics_atlas_hsp90_multimodal_reconstruction_v1_20260729`、`dynamics_atlas_hsp90_time_anatomy_v0_20260730` 三个任务的 `outputs/` 与 `inputs/` 下按 `*margin*`、`*rmsd*`、`*per_frame*`、`*series*` 查 | 让 Agent 能回到分类之前的量 | 找到则放入（< 50 MB）；找不到写 `missing` 并在题面说明"只有分箱与分类结果" |
  | `HSP90_SOURCE_AND_RUN_CARD.json`（B0） | 元数据 | 是 |
  | Henot 2022 论文 Markdown 衍生件（若 `WS/literature/` 或任务目录已有；否则从 PDF 生成，PDF 为记录源） + SI PDF | 论文原文 | 是 |
  | `WS/autoresearch/tasks/dynamics_atlas_hsp90_paper_comparison_20260729/outputs/HSP90_PAPER_ATLAS_CLAIM_MATRIX.md` | 已有主张矩阵 | **否**（含项目结论，进 `hidden/`） |

- 输出：`common/`、`common/SOURCE_INVENTORY.json`（`files[]`, `provenance[]{origin_task, origin_path, sha256}`, `missing[]`）、`common/SOURCE_MAP.txt`
- 完成：`provenance[]` 每条 sha256 与源一致（1 次检查）；`common/` 无 `hidden`、无 `ACTIVE_RULES*`。
- **覆盖题准入检查**（只查不做）：在上述三任务里找共同坐标/特征矩阵、原子对应、PCA 变换。找到 → 记 `coverage_inputs: PRESENT`，作为 §9 后续候选；找不到 → `ABSENT`，覆盖题不进本轮。

### B2 问题、元数据档、规则文本、评分依据
- `common/QUESTION.txt`（Q01，按 Pro 意见改写能力描述）：

  > 在无配体的人 HSP90α NTD 中，从闭合 ATP-lid 起始的轨迹是否比开放起始轨迹更容易离开原有构象，并出现闭合到开放的转变？
  > 资料包含 40 条 1 μs 轨迹的既有逐轨迹分析结果（`trajectory_time_anatomy.tsv` 等，字段判据见 `FIELD_DEFINITIONS.md`）、50 ns 分箱路线、方向段、元数据卡和原论文。请检查这些字段的判据与原论文对"open/closed/transition"的定义之间的关系，说明哪种可复核的观测变化发生了、依据何种判据、仍与哪些解释相容；不要仅因字段名含 departure/return 就接受其科学含义。需要计算时实际执行；方法由你选择。交付：结论及条件、证据位置、实际分析、未解决部分、有信息价值的下一步。

- `hidden/metadata_profile_v0_3.json`：**Codex 手写**（不由模型起草），来源为原文 + 元数据卡；过 v0.3 schema；两个 SOURCE（MD 轨迹、NMR 结构/CPMG 作为论文报告的对照来源）、一条 EDGE。标签 `DEVELOPER_WRITTEN_DEVELOPMENT_EXPOSED`。
- `arm_B/ACTIVE_RULES.md`：A5 桥接产出。
- `hidden/rule_coverage_record.md`：选择器选出了哪些 `rule_id`、对应什么义务；留三列空白供事后填：`相关 / 遗漏了什么 / 无用工作`。**它不参与评分。**
- `hidden/grading_rubric.md`（**科学评价依据，A/B 同一份，独立于选择器**），从三处写：
  1. 公开问题与数据能回答什么：逐轨迹的持续方向、离开/回返候选、按 seed_lineage 分组的计数；不能回答什么：平衡占比、速率、机制。
  2. Henot 2022 的定义与结论（Fig. 4a–g；"closed state is a metastable excited state"；20 条 closed-start 的三类行为）及其 locator。
  3. Soojung 7/28 验收：区分 stay / transition / excursion / unresolved；单向转变后停住不得称 equilibrated；MD 元数据五项必须出现。
  另列"合理的替代分析"（如用 50 ns 分箱重算方向持续性）与"过强结论清单"。
- `hidden/reference_values.json`：直接从 TSV 读出（每条轨迹 `first_persistent_direction`、`persistence_ns`、`return_candidate`；按 `seed_lineage` 的计数），不做新计算。
- `hidden/literature_claims.json`：从原文与主张矩阵手工抽 6–10 条可比对主张，每条 `paper_claim, locator, polarity, object, condition`。
- 完成：`validate_case_package.py`（A 阶段随手写的最小校验：三目录存在、`common/` 无禁项、schema 合法）返回 0（1 次）。

### B3 冻结
- `freeze_hsp90_q01.py`：`common/`、`arm_B/`、`hidden/`、`RT/` 的 SHA-256 → `TASK2/outputs/frozen_hsp90_q01_v2.json`，含 `model: openai/gpt-5.6-luna, reasoning: medium, image: sha256:d99fa29f…, run_order: 随机化的 [A,A,B,B], budget_usd: 0.15`。唯一一次哈希。

### B4 可选：元数据起草能力（≤ $0.03，不影响下游）
- 动作：`agent_run.py HSP90_Q01 A --stage profile` 一次（新加的 stage 只做 schema 校验与落盘 `TASK2/outputs/agent_profile_draft.json`，**不送入选择器、不生成任何下游文件**）。
- 输出：与 Codex 手写档的字段差异 `profile_diff.json`（对象身份、method/modality/role、EDGE 端点、unknown 处理）。
- 说明：这是 8/24 V2a 的一次单点观察，同一公开输入、同一目标；不汇总旧记录。

## 5. 阶段 C：运行（Codex，半天，≤ $0.15）
```bash
export OPENROUTER_API_KEY=…        # PM 注入当前 shell
python3 $RT/run_batch.py --freeze "$TASK2/outputs/frozen_hsp90_q01_v2.json" --budget-usd 0.15 --runs-dir "$TASK2/runs"
```
- 4 次：A×2、B×2，顺序按冻结文件。
- 输出：每次 `answer.md, draft_*.json, receipt.json, events.jsonl`；`TASK2/outputs/results.json`
- 完成：4 份 receipt 齐；`results.json` 与 receipt 交叉一致（1 次检查）
- 停止：`UNKNOWN_CHARGE.json` → 停不重试；累计 > $0.15 → 停；运行器 bug → 修一次只补跑该次，已跑不删；模型算错/弃权/预算截停 → **保存为结果，不补跑**。

## 6. 阶段 D：核对（Codex，1 天）——三件事分开记

对每份答复的 `claims[]` 中每条带数值或具名对象的主张，写 `TASK2/outputs/check/<run>_claims_check.csv`：

| 列 | 取值 | 回答什么 |
|---|---|---|
| `provenance` | `FROM_CITED_FILE` / `FROM_AGENT_COMPUTATION` / `AUTHOR_REPORT` / `NOT_LOCATED` | 数字来自哪里；`AUTHOR_REPORT` 允许并需 locator |
| `reproducible` | `YES`（用 `events.jsonl` 中 Agent 自己的 python 代码 + `common/` 重跑得同值）/ `NO` / `NOT_ATTEMPTED`（非本次计算） | 计算是否可复现 |
| `method_note` | 自由文本，Codex 写；标 `DEVELOPER_JUDGMENT` | 方法是否适用于对象与问题（不自动判定） |
| `status` | `VERIFIED` / `MISMATCH` / `NOT_INDEPENDENTLY_VERIFIED` | 核对器不支持 ≠ 错误 |

文献关系表 `TASK2/outputs/check/<run>_literature_relation.csv`：Codex **手工**对齐（不做关键词自动对齐），每行 `agent_claim | paper_claim | locator | relation ∈ {AGREE, DISAGREE, PAPER_SILENT, AGENT_ABSTAIN, UNDETERMINED} | note`。`DISAGREE` 是与作者结论的关系，不是错误判定；允许注明"Agent 正确地不同意作者过强表述"。

`hidden/rule_coverage_record.md` 事后填三列：B 组引用的 `rule_id` 哪些对应了实际分析动作、选择器遗漏了什么、哪些义务没带来任何内容。

验证预算：核对脚本运行 1 次（复现列）；其余为人工表格。

## 7. 阶段 E：两层报告（Codex，1 天）

- `TASK2/outputs/AGENT_RAW/`：4 份 `answer.md` + `draft_*.json` + `receipt.json` **原样**，不改一字。
- `TASK2/outputs/HSP90_Q01_VERIFIED_REPORT_ZH.md`（+ HTML）：
  1. 元数据五项（引 B0 卡，含旧报告的两处修正）
  2. 问题与数据能回答的范围
  3. 逐轨迹观测变化：发生了什么、判据、与原文定义的关系、仍相容的解释（引 `status=VERIFIED` 的数字；`NOT_INDEPENDENTLY_VERIFIED` 的数字可引但标注）
  4. 与 Henot 2022 的关系表（§6）
  5. Agent 原始交付的评价：四份各自答对/过强/弃权/未完成，引 `claims_check.csv`
  6. **规则提示改变了什么**：B 相对 A 逐条——多说、少说、说错、引用了哪个 `rule_id`、该规则是否对应实际分析动作；不计数、不设阈值
  7. **人工介入清单**：报告中每一处非 Agent 产出的修正、补充、重述，逐条列出
  8. 未解决与下一步（含覆盖题、收敛题的输入状态）
- `REPLAY.md`：命令、哈希、系统提示与两组用户提示原文、确定性/LLM 边界、换问题要改哪些文件。

## 8. 交付后：由 PM 用四结果表决定，不自动推进

| 首轮结果 | 下一步 |
|---|---|
| A 已给出有用答案，B 没有明确帮助 | 保留普通流程继续科学工作；不为维护 Rules 追加开发 |
| B 帮助发现一个实质遗漏，且未损失可回答内容 | 保留这一具体用途；再到第二体系检查能否复用；不扩大成"Engine 有效" |
| 关键错误来自元数据、输入缺失或工具未返回 | 按实际失败归因；不算成规则效果，也不修到答案必然正确 |
| 必须不断新增题目专用代码或核对器才能交付 | 停止系统扩展；先交付已有科学结果与真实限制 |

Pro 审阅 §7 报告（提示见 `REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md`）；Pro 意见按条记 `disposition.json`（`FIX/RECORD/REJECT` + 理由），**处置完成不构成进入下一阶段的条件**。

## 9. 停放项与后续条件（不在本轮）

- 收敛题：输入已在（`prefix_horizon_routes.tsv`、`trajectory_anchor_proximity.tsv`）；若进入，须允许"某量在前缀窗口内变化小"与"不足以估计平衡比例"两结论并存；CPMG 交换态与 MD 几何类别的对应不自动成立（原文自己保留此限制）。
- 覆盖题：仅当 B1 记 `coverage_inputs: PRESENT`。
- 第二体系（ADK / DHFR）：只在 PM 按 §8 决定后开始；选择时须写明两类资料的构建体与条件、具体可比性质、现有方法能给出哪项有用答案；"方法最多新增一个定义"只是工程成本上限，不是科学判据。第三体系不承诺。
- V2a 旧记录汇总：参考 `hsp90_directional_time_anatomy_development_v1_alpha` 与 MiniMax 提案 `HSP90_NTD_EXPOSED_PAPER_BLIND_V1` 不是同一任务，不汇总；B4 的单点观察替代。
- 从元数据推公开事实、通用评分模板、通用文献比对、`drift_check.py`：不做。

## 10. 预算

| 阶段 | 工作日 | 模型费用 | 检查命令 | 哈希 | 审阅 |
|---|---|---|---|---|---|
| A 系统修正 | 2 | 0 | 3 | 0 | 0 |
| B 案例 | 2 | ≤ $0.03（B4 可选） | 2 | 1 | 0 |
| C 运行 | 0.5 | ≤ $0.15 | 1 | 0 | 0 |
| D 核对 | 1 | 0 | 1 | 0 | 0 |
| E 报告 | 1 | 0 | 0 | 0 | 1（Pro） |
| **合计** | **6.5（上限 7）** | **≤ $0.18（上限 $0.20）** | **7** | **1** | **1** |

每阶段结束写 `TASK2/state/validation_ledger.jsonl`：计划的检查、实际跑的、跳过的及理由。

## 11. 对 Pro 审查意见（v1）的处置

| Pro 意见 | 处置 | 落在 |
|---|---|---|
| 规则输出不能决定评分范围 | FIX：评分依据独立写；规则覆盖另记，不参与评分；删"rubric 段数 = obligations 数" | §4 B2 |
| 格式合法的元数据不是事实；勿从模型元数据推公开事实 | FIX：元数据档由 Codex 手写；不生成公开事实；C 组停 | §2、§4 B2 |
| MATCH ≠ 科学正确；作者报告可引用；核对器不支持 ≠ 错误 | FIX：三列分开；`AUTHOR_REPORT`；`NOT_INDEPENDENTLY_VERIFIED` | §6 |
| B0 力场与帧数矛盾是旧报告错误 | FIX：已在本地 PDF 核实 ff14SB / 1020 ns / 20 ns / 1001；卡改写，加时间轴检查 | §4 B0 |
| Q01 能力应写成"检查并综合已有分析"；字段名不等于科学含义 | FIX：题面改写；附 `FIELD_DEFINITIONS.md` | §4 B2 |
| 收敛题需分开两种结论；CPMG↔MD 对应不自动成立 | RECORD：本轮不做；条件写入 §9 | §9 |
| 覆盖题缺输入 | FIX：只做准入检查，不进本轮 | §4 B1、§9 |
| B3 对象不一致；关键词判 claim 安全不当 | FIX：B3 停放；B4 单点观察替代；删关键词判定 | §9、§4 B4 |
| A 组可读 `public/ACTIVE_RULES.md` 泄漏 | FIX：`common/ arm_B/ hidden/` 三分；断言 + 测试 | §2、§3 A4 |
| 共享元数据 vs 独立提取要写明 | FIX：本轮共享 Codex 手写档，比较的是给定元数据后的分析增量；Agent 可回到原文指出元数据错误 | §4 B2 题面、§7 第 2 节 |
| 规则应是可质疑的提醒 | FIX：`ACTIVE_RULES.md` 文首声明 | §3 A5 |
| Pro 不是真值和阶段门 | FIX：§8 由 PM 决定；处置完成不构成条件 | §8 |
| 文献比对不能关键词对齐；DISAGREE 可为正确 | FIX：手工对齐；`UNDETERMINED`；注明 | §6 |
| 第二体系标准应围绕科学问题；不预设 ADK/DHFR；第三不自动 | FIX | §9 |
| 人力与通用脚本被低估；请求前预算检查 | FIX：范围缩至一题四份；通用脚本停放；预算参数化（现有请求前预留检查保留） | §0、§2、§10 |
| `drift_check.py` 无效；改用到期交付 | FIX：删；§0 到期规则 | §0 |
| 注册表规则不比七条更科学 | RECORD：§3 A5 声明 | §3 A5 |
| 环境变量凭证应保留 | KEEP | §3 A3 |

## 12. 失败账本
任一步两次修补仍失败：停止编辑，写 `TASK2/outputs/failure_ledger_<step>.md`（尝试的修法、预期机制、实际结果、假设为何变弱、重复了什么假设、下一个替代假设），进 §7 报告的"未解决"节。
