# HSP90 首轮：一个科学问题、四份答复、有界交付（v3）

Dynamics Atlas · 2026-09-09 · v3 · **供 Codex 逐步执行** · 本版是交付版，开工不再等下一轮 Pro 批准

> v3 替代 v2（`HSP90_FIRST_ROUND_PLAN_V2_ZH.md`）。范围、规模、四结果表不变。改动来自两处：Pro 对 v2 的审查（`PRO_REVIEW_OF_PLAN_V2_ZH.md`，结论 CHANGES_REQUESTED_BOUNDED，"改几处后执行"）和 2026-09-09 深夜对 v2 引用的每个路径、脚本参数、字段名的本机核实。逐条处置见 §11。v1 意见的处置沿用 v2 §11，不再重复。
>
> 路径约定：`WS` = 本地工作区根目录（不在 git 内）；`HARNESS` = `WS/dynamics-atlas-harness`；`HARNESS_LUNA` = `WS/dynamics-atlas-harness-luna-runtime-v1`（A2 建）；`RT` = `HARNESS_LUNA/agent_experiments/luna_runtime_v1`（代码，入库）；`TASK0` = `WS/autoresearch/tasks/dynamics_atlas_rules_incremental_value_protocol_20260909`；`TASK2` = `WS/autoresearch/tasks/dynamics_atlas_hsp90_first_round_v3_20260910`（案例、运行、账本，不入库，A1 建）。**代码目录和任务目录分开，运行器不再从代码位置推断任务根目录。**

## 0. 本阶段做什么，测到的是什么

本阶段先利用现有 Agent 和已保存的 HSP90 资料，完成一项有明确方法与来源的科学分析，并观察加入现有规则提示后，答案是否得到实质改善。科学评价独立于规则选择结果。完成后由负责人根据科学结果、人工介入和复用成本决定是否进入第二体系；第三体系不作承诺。Pro 提供咨询审阅，不替代领域结论或负责人的投入决定。

**本轮测到的是：** 在一份人工预整理、已经暴露过的 HSP90 派生资料上，同一个 Agent 得到额外的、按当前资料选出的规则提示后，答复发生了什么变化。它不验证原始轨迹处理、自动元数据提取、规则引擎强制执行或跨来源泛化。共同题面已经提醒两组不要把字段名当物理转换，所以 A 不是"毫无科学指导"的裸模型；B−A 测的是这份共同指导之上的额外提示效果。

**一句话交付物：** 一份 HSP90 ATP-lid 有限时间构象变化的科学答复（Q01），来自同一个已有 Agent 在同一份资料上的四次运行（A 组无规则提示 ×2，B 组附注册表选出的规则提示 ×2），附原始交付、核对记录、与 Henot 2022 的逐主张关系表，以及"规则提示改变了什么"的逐条记录。

**明确不做：** C 组；B4 元数据起草（v2 的可选项，本版跳过）；第二、第三体系；PCA 覆盖题；通用评分/比对脚本；从模型元数据推公开事实；V2a 旧记录汇总；换模型、充值、新 MD、改 33 条注册表、新题库；修改历史结果文件。

**到期规则：** Codex 开工后 **7 个工作日**内交出 §7 的报告，或交出失败原因。框架未完善不是续期理由。首轮必须能交出的是：一份 HSP90 有限时间行为的科学回答、四份原始答复或未完成记录、以及额外规则提示帮助、损害或没有明显作用的具体证据；不是一套标记齐全的目录。

## 1. PM 一次性授权 **[开工前一次签]**

| 项 | 内容 |
|---|---|
| 1 | 模型费用上限 **$0.20**（四次分析 ≤ $0.15，余量给失败重试与 A0 的一次接口探测）；这是停止线，不是四份必成的成本预测；`TASK2/outputs/UNKNOWN_CHARGE.json` 出现即停 |
| 2 | 在运行 shell 提供 `OPENROUTER_API_KEY`；Codex 不从任何文件读 key |
| 3 | 允许 `feature/luna-runtime-v1` 分支 commit / push / Draft PR；`runs/`、案例数据、账本、凭证不入库 |
| 4 | 允许把 `MD_TRAJECTORY` 方法档作为开发 proposal 经**副本** method scope 送入选择器；原文件不改；标签 `DEVELOPMENT_PROPOSAL_NOT_HUMAN_REVIEWED` |
| 5 | 允许为本轮写一份新的 `TASK2/runtime/readiness.json`（`approved_for_development: true`，注明本轮授权日期与费用上限）。旧 `TASK0/runtime/readiness.json` 保持 `false`，不改 |

PM 回复"授权 1–5"后，Codex 在 `WS/autoresearch/DYNAMICS_ATLAS_DECISION_LOG.jsonl` 追加一条并开工。本轮不下载任何外部数据。

## 2. 系统：只补首轮必需的四件事

```text
TASK2/cases/HSP90_Q01/
  common/        → 挂载为 /source（A、B 都可读）：问题、数据、元数据卡、字段定义、论文文本、来源清单
  arm_B/         → 不挂载；ACTIVE_RULES.md 只以文本附进 B 组用户提示
  hidden/        → 不挂载；元数据档、评分依据、参考值、文献主张、规则覆盖记录、历史结论文件
TASK2/runs/      → 每次运行一个目录
TASK2/outputs/   → 账本、冻结文件、核对表、报告
TASK2/runtime/   → readiness.json、batch.lock（本轮状态，不是代码）
```

现状（本机核实，`TASK0/runtime/agent_run.py` 维护版）与改动：

| 改动 | 现状 | 做什么 | 不做什么 |
|---|---|---|---|
| 任务根目录 | `ROOT=Path(__file__).resolve().parents[1]`；案例 `ROOT/cases`、运行 `ROOT/runs`、账本 `ROOT/outputs/paid_usage.jsonl`、锁 `ROOT/runtime/batch.lock`、`ROOT/runtime/readiness.json`、`ROOT/outputs/UNKNOWN_CHARGE.json` 全部由代码位置推断 | `agent_run.py` 与 `run_batch.py` 显式接收 `--task-root`；上述六项全部改为从 `task_root` 读；提示文件（`common_prompt.txt`）、`container_tools.py` 仍从 `RT` 读 | 不改容器参数、工具协议、提交协议 |
| 凭证 | `credential()` 从 `~/.codex/sessions/…/rollout-*.jsonl` 正则抠 key（`agent_run.py` 第 12–20 行；`check_model.py` 第 4–5 行同样） | 只读 `os.environ["OPENROUTER_API_KEY"]`，缺失抛 `RuntimeError`；保留余额预检；`check_model.py` 同改 | 不写任何回退 |
| 公开事实依赖 | `facts=json.loads((source/'PUBLIC_FACTS.json').read_text())` 无条件执行（第 60 行）；C 组才用 | A/B 不读该文件、不加载 `finite_checks` 与 `C_POLICY.txt`；`arm` 选项保留 `C` 但本轮 `run_batch.py` 拒绝 `C` | 不删 `finite_checks.py`（原样搬运，不调用） |
| 挂载与消息 | `/source` = 整个案例目录；B/C 读 `RT/ACTIVE_RULES_ZH.md`（第 58 行） | `/source` 只挂 `common/`；B 组规则文本从 `TASK2/cases/<case>/arm_B/ACTIVE_RULES.md` 读入并附到用户提示末尾 | 不新建隔离框架 |
| 共同提示 | 第三段写"公开事实索引"和 `method_sources/SOURCE_MAP.txt`（本轮都不存在） | 改为："公开来源目录 /source 含 `SOURCE_INVENTORY.json`（文件清单与来源）和 `FIELD_DEFINITIONS.md`（字段判据），均可自行读取。新计算使用自己的 ID，不冒充已发表结果。"其余段落不动 | 不改交付协议段 |
| 预算 | 每次请求前 `spent+reserve>3` 预留检查（第 92–93 行）；`spent` 从账本累计 | 3 改为 `--budget-usd`；本轮账本 `TASK2/outputs/paid_usage.jsonl` 从零起；`TASK0` 旧账本不动、不混入 | 不改预留公式 |
| 窄规则桥接 | 无 | `rules_bridge.py` + `render_active_rules.py`，见 A5 | 不生成评分模板；不推公开事实 |

维护版本说明：`TASK0/runtime/agent_run.py` 是已应用 `TASK0/outputs/post_development_review/submission_maintenance.patch` 的维护候选（普通确认文字不再覆盖已提交答案）；已执行的旧版在 `post_development_review/before/`。搬运的是维护版，不是 `before/`。

## 3. 阶段 A：环境与系统修正（Codex，2 天）

格式：输入 → 动作 → 输出 → 完成标准 → 停止条件。

### A0 环境预检（半小时，不花钱除非注明）
- 动作：
  1. `docker info` 成功（2026-09-09 深夜本机 Docker 守护进程未运行，需先启动 Docker Desktop）。
  2. `docker image inspect atlas-luna-development:20260909 --format '{{.Id}}'` 输出等于 `TASK0/runtime/frozen_development.json` 的 `image`（`sha256:d99fa29fcffbf7de8dce05abf1c71a7002c39acf8e19276328582a5556c84e29`）。镜像不存在 → 停：本机没有 Dockerfile 或构建记录，重建不在本轮范围，写失败账本交 PM。
  3. 容器内导入检查（改自 `TASK0/runtime/preflight.py` 第 9–27 行，只保留 `import numpy,scipy,matplotlib,PIL,fitz,pandas,sklearn` 和只读/无网断言；**去掉**它后半段的模型图像调用）。注意容器内没有 MDAnalysis，宿主机也没有。
  4. 选择器探测（零费用）：对 `WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/outputs/case_inputs/selector_repair/lincoff_2020_xeisd_metadata_v0_3.json` 运行 `select_review_obligations.py`，输出应含 `obligations`（本机探测：51 条，`unresolved_inputs` 17）。
  5. `python3 -c "import jsonschema"` 成功（选择器测试依赖）。
- 输出：`TASK2/outputs/preflight_env.json`
- 停止：1–3 任一失败即停，写失败账本。

### A1 建任务
- 动作：
  ```bash
  cd "$WS"
  python3 autoresearch/scripts/init_task.py --task-id dynamics_atlas_hsp90_first_round_v3_20260910 --goal "HSP90 Q01 有界首轮：同一 Agent、A/B 各两次、独立科学评价、两层报告"
  # 按 autoresearch/templates/DYNAMICS_ATLAS_TASK_CONTEXT_RECEIPT_TEMPLATE.md 填 state/context_receipt.md
  python3 autoresearch/scripts/validate_dynamics_atlas_context_receipt.py --task-id dynamics_atlas_hsp90_first_round_v3_20260910
  mkdir -p "$TASK2"/{cases/HSP90_Q01/{common,arm_B,hidden},runs,outputs,runtime,inputs}
  ```
- 完成：验证器 PASS。停止：不 PASS 不进 A2。

### A2 分支与搬运
- 动作：
  ```bash
  cd "$HARNESS" && git fetch origin
  git worktree add "$HARNESS_LUNA" -b feature/luna-runtime-v1 origin/main   # origin/main 现为 914bc00
  mkdir -p "$RT"
  cp "$TASK0"/runtime/{agent_run.py,container_tools.py,finite_checks.py,common_prompt.txt,C_POLICY.txt,check_model.py,preflight.py,run_development_batch.py,test_runner_offline.py,test_submission_maintenance_offline.py} "$RT"/
  printf 'Frozen 2026-09-09 development copy (maintenance candidate). Live code: dynamics-atlas-harness/agent_experiments/luna_runtime_v1/\n' > "$TASK0/runtime/FROZEN_SEE_HARNESS.md"
  ```
  `git fetch` 在沙箱 shell 里可能因 keychain 不可用失败；在用户的交互 shell 里执行。
- 完成：`cd "$RT" && python3 test_runner_offline.py && python3 test_submission_maintenance_offline.py` 都不报错（两个文件是带断言的脚本，不是 unittest 用例，`unittest discover` 找不到它们）；`python3 finite_checks.py` 打印 PASS。
- 停止：失败修一次；再失败写失败账本（§12）。

### A3 凭证
- 动作：改 `credential()` 与 `check_model.py`；写 `test_credential_env_only.py`（未设变量必抛 `RuntimeError`；设假值时 `pathlib.Path.read_text` 未被调用）。
- 完成：新测试过；`grep -rn "codex/sessions" "$RT"` 为空。

### A4 挂载与消息隔离
- 动作：`source = task_root/'cases'/case/'common'`。启动前断言（递归遍历 `common/` 全部后代，`Path.resolve()` 后再查）：不存在名为 `hidden`、`arm_B` 的目录或链接；不存在 `ACTIVE_RULES*`、`grading_rubric*`、`reference_values*`、`literature_claims*`、`rule_coverage*`、`metadata_profile*`；没有任何符号链接指向 `common/` 之外。B 组：`user += '\n\n' + (task_root/'cases'/case/'arm_B'/'ACTIVE_RULES.md').read_text()`。
- 测试 `test_mount_isolation_offline.py`（mock docker）：
  - 案例资料只挂载 `common/`：`-v` 参数里以 `:/source:ro` 结尾的恰好一条，且其宿主路径以 `/common` 结尾；允许现有的 `/work:rw` 和 `/tool.py:ro` 两条；不出现案例父目录、整个仓库、`arm_B/`、`hidden/`。
  - 消息：A、B 的 system 消息相同；A 的 user 消息 = `QUESTION.txt` 原文；B 的 user 消息 = 同一原文 + 冻结的 `ACTIVE_RULES.md` 全文；测试比较实际消息内容，不用"A 中没有 `rule_id` 字样"代替。
  - 在一个不含 `PUBLIC_FACTS.json` 的临时任务目录里启动 A 和 B（沿用 `test_runner_offline.py` 的 mock 方式），确认读到正确案例、写到 `task_root/runs/`、账本写到 `task_root/outputs/paid_usage.jsonl`，最后一次有效提交被保留。这一项证明路径接通，不只是能 import。
- 完成：测试过。

### A5 窄规则桥接
- 输入：
  - 选择器：`WS/autoresearch/tasks/dynamics_atlas_metadata_selector_validation_20260813/scripts/select_review_obligations.py`（参数 `--input --output --receipt --run-id [--index] [--method-scope]`；`--index` 默认 `outputs/selector_sidecar/rule_selector_index_v0_1.json`，存在）
  - 注册表：`WS/autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/ruleset/v0_1/rule_registry.tsv`。**扩展名是 .tsv，内容是逗号分隔（0 个制表符，814 个逗号）**，用 `csv.DictReader` 默认分隔符读；33 条，`rule_id` 从 `C001-RULE-001` 到 `C012-RULE-003`，列含 `rule_id, proposed_project_rule, required_fields, abstain_route, project_status`。
  - method scope：`…/outputs/contracts/protein_dynamics_method_scope_v1.json`。`MD_TRAJECTORY` 现状 `status: NEEDS_METHOD_DEFINITION`；选择器只对 `status == "REGISTERED_FOR_METADATA_REVIEW"` 的方法做方法特定选择（`select_review_obligations.py` 第 275 行），否则记 `gap_class: UNREGISTERED`。方法定义七字段来自同文件 `required_definition_fields`：`native_observable, estimand, time_semantics, spatial_support, unit_or_aggregation, uncertainty_status, evidence_role`。
- 动作：
  - `rules_bridge.py`：
    ```bash
    python3 "$SELECTOR" --input "$CASE/hidden/metadata_profile_v0_3.json" --output "$CASE/hidden/review_obligations.json" \
      --receipt "$CASE/hidden/review_obligations_receipt.json" --run-id HSP90_Q01_$(date -u +%Y%m%dT%H%M%SZ) \
      --method-scope "$CASE/hidden/method_scope_dev_copy.json"
    ```
    `method_scope_dev_copy.json` = 原 method scope 的副本，`MD_TRAJECTORY` 的 `status` 改为 `REGISTERED_FOR_METADATA_REVIEW`，七字段取值引用 B0 卡，加 `"development_proposal": "DEVELOPMENT_PROPOSAL_NOT_HUMAN_REVIEWED"`。
  - `render_active_rules.py`：读 `review_obligations.json` 的 `obligations[]`（每条含 `obligation_id, rule_id, target, required_check, claim_scope, reason_from_input`）。**按 `rule_id` 分组**，每个不同的 `rule_id` 渲染一块：`**[<rule_id>]** <proposed_project_rule>　必填：<required_fields>　弃权路线：<abstain_route>　本案触发对象：<target.source_ids 或 comparison_ids 去重>　检查：<required_check 去重>`。查不到 `rule_id` 的写 `hidden/unmapped_obligations.json`，不渲染。文首固定一句："以下为分析提醒，可质疑；与资料冲突时以资料为准并说明。"
  - 七条指导与注册表对照表 `TASK2/outputs/seven_rules_registry_mapping.tsv`（七条来自 `TASK0/runtime/ACTIVE_RULES_ZH.md`）只作记录。
- 输出：`arm_B/ACTIVE_RULES.md`
- **分支（冻结前写清，不临时补救）：** 选择器抛错 / `obligations` 为空 / 渲染后为空 → 记录属于技术失败、没有适用规则、还是映射未覆盖；仍完成 A 组两次科学回答；**不手挑规则补出 B**，不把相同输入的两组称为有处理差异的 A/B 比较。
- 完成：`test_rules_bridge_offline.py` 对 lincoff 样例：obligations 非空，渲染每块含 `rule_id`，块数 = 不同 `rule_id` 数。
- 说明：B 组规则来自旧注册表 + 旧选择器，是复用选择，不是它比 9 月 9 日的七条指导更科学的证明。

### A6 任务根目录、预算参数化、批处理
- 动作：`--task-root`、`--budget-usd`；`run_batch.py --freeze <json> --task-root <dir> --budget-usd <x>`：读冻结文件的 `run_order`，每次前检查 `task_root/outputs/UNKNOWN_CHARGE.json`，每次后追加 `task_root/outputs/results.json`；`arm == 'C'` 直接拒绝。`readiness.json` 从 `task_root/runtime/` 读（授权 5）。
- 完成：`test_runner_offline.py` 增加预算超限即 `COST_LIMIT` 的用例；A4 的路径接通用例通过。

### A7 收口
- 动作：`cd "$RT"` 跑本目录全部测试 1 次；`cd "$HARNESS_LUNA" && PYTHONPATH=src python3 -m unittest discover -s tests` 1 次（不得变红）；写 `RT/README.md`（说明维护版来源、`--task-root` 约定、本轮不入库的目录）；开 Draft PR（授权 3）。
- 阶段 A 验证记录：单测 2 次 + harness 套件 1 次；审阅 0；哈希 0。

## 4. 阶段 B：HSP90 Q01 案例（Codex，2 天）

### B0 原文对齐：分开记"论文声明"和"本轮输入已核对内容"
- 输入（全部本机存在）：
  - 原文 PDF `WS/autoresearch/tasks/dynamics_atlas_hsp90_feasibility_20260725/inputs/henot_2022_hsp90_article.pdf`（记录源）；文本抽取 `WS/tmp/pdfs/henot_2022_article.txt`（823 行；复制到 `TASK2/inputs/` 并记 sha256 后用其行号作 locator）：第 560 行 ff14SB；第 570 行 170 mM；第 584–587 行 "1020 ns … first 20 ns … initial equilibration … last 1000 ns"；第 301、603 行 "20 020 snapshots … every 1 ns"。Markdown 衍生件 `WS/autoresearch/tasks/dynamics_atlas_pdf_markdown_derivatives_v1_20260901/outputs/markdown_library/derivatives/01-henot-2022-hsp90-article--2a37d00b43c1.md` 单词粘连，只作备份。
  - 作者 README `WS/autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725/data/contract/MD/README`：`md_0-10_evert1ns_fitBB_protonly.xtc 1020ns (1020 frames)`、`md_1-10_… 1000ns (1000 frames)`。
  - Zenodo 记录 `…/dynamics_atlas_hsp90_feasibility_20260725/inputs/zenodo_6606744_record.json`：描述写 "AMBER99SB force field"。**旧报告的 AMBER99SB 抄自这里，不是误抄。**
  - 旧报告 `…/dynamics_atlas_hsp90_acquisition_20260725/outputs/HSP90_END_TO_END_REPORT.md` 第 19–38 行。
  - 提取清单 `…/dynamics_atlas_hsp90_acquisition_20260725/data/trajectories/extraction_manifest.json`、`extraction_manifest_r60a.json`：R46A 取 `md_0-10_evert1ns_fitBB_protonly.xtc`；R60A 同名文件是作者符号链接，实际提取 `md_all_prot_fit.xtc`，逐文件 sha256 与大小已记录。
  - 7/28 会议纪要 `WS/会议纪要/28号会议纪要/01_GOAL_AND_TASK_BREAKDOWN.md` 第 44–46 行（元数据字段与"力场存疑"）。
- 动作：写 `TASK2/outputs/HSP90_SOURCE_AND_RUN_CARD.json`，两层：
  - `paper_statement`：ff14SB、显式水、~170 mM NaCl、1020 ns、前 20 ns 平衡、后 1000 ns 分析、每 1 ns 快照；每项带 locator。
  - `local_inputs_checked`：
    - `force_field`：目录 `amber14sb_OL15.ff` 与原文一致；Zenodo 描述写 AMBER99SB，记为资源描述与论文不一致，**不再称为分析阻碍**；7/28 的"力场存疑"据此更新。
    - `frames`：README 名义 1020 帧；旧报告实测 1021 帧（含 t=0）；派生表 1001 点。三者对应全程含零帧 / 全程名义 / 后 1000 ns 含端点，**不是冲突**。
    - `time_axis_of_round_inputs`（本轮真正交给 Agent 的表）：读 `frame_state_assignments.tsv`（B1）的 `time_ns` 列。本机核实：40 条轨迹、每条 1001 行、20.0–1020.0 ns、步长 1.0 ns。写明"派生表时间零点沿用原轨迹，窗口 20–1020 ns"。
    - `xtc_spot_check`：可选，一条 R46A、一条 R60A。宿主机与容器都没有 MDAnalysis，本轮**不为此安装依赖**；若 `gmx check` 可用就记首末帧与帧数，否则记 `NOT_ATTEMPTED`。标为抽查，不用于声称 40 条都已核对。
    - `lineage`：R46A/R60A 文件来源（上面提取清单）；seed lineage 与目录名的对应。
    - 溶剂、离子、温度取旧报告与 7/28 纪要（标来源）；`analysis_window_note`：Agent 拿到的表已从 20 ns 起，若引用全程 1021 帧须自行说明。
  - `hidden/md_trajectory_method_profile_proposal_v1.json`：七字段（A5 所列）取值引用本卡；`hidden/method_scope_dev_copy.json` 按 A5。
- 完成：卡内每个字段有 `source`；副本能被选择器读取（A0 第 4 项同样方式探测一次）。

### B1 数据盘点与 `common/`
- 优先核对具名文件，不泛搜。以下文件全部本机核实存在：

  | 文件 | 内容 | 放入 |
  |---|---|---|
  | `WS/autoresearch/tasks/dynamics_atlas_hsp90_v1_science_20260728/results/round2/frame_state_assignments.tsv`（5.9 MB，40 040 行；列 `trajectory, time_ns, state_core, d_open_medoid_A, d_closed_medoid_A, geometry_delta_A, nearest_open_A, nearest_closed_A, contact_margin_A`；仓库冻结副本登记在 `HARNESS/evidence/real_case_vertical_slice_v1/hsp90_operator_input_manifest_v1.json`） | 逐帧派生量，分类之前的量 | `common/` |
  | 同目录 `state_core_definition.json`（`assignment` 规则与 `theta_open/theta_closed/radius_open_A/radius_closed_A` 数值） | `state_core` 的判据 | `common/` |
  | `WS/autoresearch/tasks/dynamics_atlas_hsp90_time_anatomy_v0_20260730/outputs/trajectory_time_anatomy.tsv`（120 数据行 + 表头） | 逐轨迹分类 | `common/` |
  | 同目录 `trajectory_time_bins_50ns.tsv`（840 + 表头）、`directional_runs.tsv`（1175 + 表头） | 50 ns 分箱、方向段 | `common/` |
  | 同目录 `scripts/run_time_anatomy_v0.py`（字段的实际定义；仓库冻结副本 `HARNESS/evidence/real_case_vertical_slice_v1/frozen_inputs/hsp90/run_time_anatomy_v0_frozen.py`，Codex 先 `diff` 两者） | 写 `FIELD_DEFINITIONS.md` 的依据 | 脚本本身进 `hidden/`；定义写进 `common/FIELD_DEFINITIONS.md` |
  | `HSP90_SOURCE_AND_RUN_CARD.json`（B0） | 元数据 | `common/` |
  | Henot 原文 PDF + SI PDF（`…feasibility_20260725/inputs/henot_2022_hsp90_supplement.pdf`）+ 文本抽取 `henot_2022_article.txt` | 论文 | `common/` |
  | 同目录 `route_predictions.tsv`（含 `atlas_route`、`claim` 列的历史结论文字）、`event_and_window_stability.tsv`（含 `claim_boundary` 列）、`results_summary.json`、`figure_captions_and_claim_boundaries.md` | 历史答复与措辞 | `hidden/`（仅供评分与核对用） |
  | `WS/autoresearch/tasks/dynamics_atlas_hsp90_paper_comparison_20260729/outputs/HSP90_PAPER_ATLAS_CLAIM_COMPARISON.md`（224 行，HPA-01…14；v2 写的 `…CLAIM_MATRIX.md` 只是 302 字节的指针文件） | 项目结论 | `hidden/` |

  seed lineage 从 `trajectory_time_anatomy.tsv` 的 `seed_lineage` 列取，不需要 `route_predictions.tsv` 进 `common/`。
- `common/FIELD_DEFINITIONS.md` 必须写清（从脚本抽出，**不复制历史文件里的"建议怎样回答"和允许/禁止措辞**）：
  1. 统计单位是轨迹（n = 40：`closed_seeded` 20、`open_seeded` 20）；帧是轨迹内的描述对象。
  2. 逐帧标签规则：`geometry_delta_A > 0 且 contact_margin_A > 0` → `OPEN_CONSENSUS`；两者 `< 0` → `CLOSED_CONSENSUS`；否则 `READOUT_CONFLICT`（零符号规则，未优化）。`state_core` 另按 `state_core_definition.json` 的 `assignment` 判 `C/O/U`（本机核实：40 037 帧 U、2 帧 O、1 帧 C）。
  3. `trajectory_time_anatomy.tsv` **每条轨迹三行**，对应持续性阈值 5、20、50 个保存帧（`persistence_saved_frames`）；120 行是 40 × 3，不是 120 条轨迹。按阈值分别统计再比较敏感性，不合并。
  4. `first_persistent_direction` = 第一个长度 ≥ 阈值且不是 `READOUT_CONFLICT` 的连续段的标签；`opposite_direction_departure_candidate` = 其后出现的与它**相反**的持续段；`return_candidate` = departure 之后再出现与第一个持续方向相同的持续段。**departure 相对于第一个持续方向，不相对于起始结构标签**：若某条轨迹的第一个持续方向已不同于 seed lineage，直接累计 departure 会答错 Q01。
  5. 时间量约定：`length_ns`、`persistence_ns` 等于保存帧数（帧数式约定）；连续 5 个间隔 1 ns 的点首末相差 4 ns。区分保存帧数、采样窗口约定和首末时间差；不把帧数式长度称为精确驻留时间。
  6. 50 ns 分箱用箱内中位数判方向，是显示用的另一时间分辨率汇总，不能恢复逐帧连续段。
  7. 时间窗口 20–1020 ns，每条 1001 点（引 B0 卡）。
- 输出：`common/`、`common/SOURCE_INVENTORY.json`（`files[]`, `provenance[]{origin_task, origin_path, sha256}`, `missing[]`）。
- 完成：`provenance[]` 每条 sha256 与源一致（1 次检查）；A4 的断言对 `common/` 通过；`diff` 冻结脚本与本机脚本的结果写入 `SOURCE_INVENTORY.json`。
- **覆盖题准入检查**（只查不做）：同目录 `landscape_projection.tsv`（80 160 行，`NMR_ANCHOR`/`SOURCE_BALANCED` 两视图的 PC1/PC2 投影）、`nmr_anchor_pca.json`、`source_balanced_pca.json`（`weights`、`k90`，无原子坐标矩阵）。记 `coverage_inputs: PROJECTION_ONLY`；覆盖题不进本轮，§9 记条件。
- 本轮不修历史结果文件；发现旧字段含义易误导，保留原文件，在 `FIELD_DEFINITIONS.md` 和报告里解释。

### B2 问题、元数据档、规则文本、评分依据
- `common/QUESTION.txt`（Q01）：

  > 在无配体的人 HSP90α NTD 中，从闭合 ATP-lid 起始的轨迹是否比开放起始轨迹更容易离开原有构象，并出现闭合到开放的转变？
  > 资料包含 40 条轨迹（20 条闭合起始、20 条开放起始，各 1 μs）的逐帧派生量（`frame_state_assignments.tsv`）、既有逐轨迹分析结果（`trajectory_time_anatomy.tsv` 等）、50 ns 分箱路线、方向段、元数据卡、字段判据（`FIELD_DEFINITIONS.md`）和原论文。请检查这些字段的判据与原论文对 open / closed / transition 的定义之间的关系，说明哪种可复核的观测变化发生了、依据何种判据、仍与哪些解释相容；不要仅因字段名含 departure / return 就接受其科学含义。需要计算时实际执行；方法由你选择。
  > 答复中请写明你所依据的比较条件、时间窗口和统计单位。交付：结论及条件、证据位置、实际分析、未解决部分、有信息价值的下一步。

- `hidden/metadata_profile_v0_3.json`：由负责实验准备的 Codex 根据公共材料整理（不是本轮被测 Agent 临时生成，也不是人类领域专家确认），标签 `DEVELOPER_PREPARED_TRACEABLE_NOT_DOMAIN_CONFIRMED`。格式参照 lincoff 样例（`contract_version: protein-dynamics-metadata/v0.3-development`，顶层 `case, evidence_items, comparisons`）。**按实际方法和用途记录证据对象，不预设两个 SOURCE 一条 EDGE**：MD 轨迹派生量是本题实际使用的来源；NMR 结构参照（8B7I/8B7J 的 medoid 与阈值来自 `state_core_definition.json`）按其在判据中的角色记；CPMG 只是作者背景，不进入数值比较，不记为本题证据对象。决定规则选择的来源事实必须能在 `common/` 的公开资料中找到；不得把评分结论或预期答案写成元数据事实。
- `arm_B/ACTIVE_RULES.md`：A5 产出。
- `hidden/rule_coverage_record.md`：选择器选出的 `rule_id` 与义务；三列留空供事后填：相关 / 遗漏了什么 / 无用工作。**不参与评分。**
- `hidden/grading_rubric.md`（科学评价依据，A/B 同一份，独立于选择器）：
  1. 公开问题与数据能回答什么：按阈值分别统计的持续方向、离开/回返候选、按 seed lineage 的计数、对阈值的敏感性；不能回答什么：平衡占比、速率、机制。**当前数据不能推出的占比/速率**与**论文报告的占比/速率可作为作者报告引用**是两个范围，不用一句"不能回答占比"盖过。
  2. Henot 2022 的定义与结论及 locator（Fig. 4a–g；"closed state is a metastable excited state"；20 条 closed-start 的三类行为；HPA-02/03/05/10/11 的论文侧陈述）。
  3. Soojung 7/28 要求（`WS/会议纪要/28号会议纪要/02_MASTER_GOAL_AND_TASK_TREE_ZH.md` 第 41、165、271–275、684 行；`01_GOAL_AND_TASK_BREAKDOWN.md` 第 44–46 行）：区分"持续停留 / 完成转变 / 短暂偏离 / 无法判定"这四种科学区别——评价是否作出了区别，**不要求沿用 stay/transition/excursion/unresolved 这几个内部英文标签**；单向转变后停住不得称 equilibrated；元数据只处罚**会改变结论含义的关键遗漏**（比如没说时间窗口、没说统计单位），不因缺少固定五项中的某一项判不合格。
  4. "合理的替代分析"（如在另一时间分辨率下用 50 ns 分箱做辅助分析，注明它不等价于逐帧复算）与"过强结论清单"（全部轨迹已收敛、占比、速率、唯一机制、把 departure 计数直接当转变）。
- `hidden/reference_values.json`：直接从 TSV 读出（每条轨迹三个阈值下的 `first_persistent_direction`、`persistence_ns`、`opposite_direction_departure_candidate`、`return_candidate`；按 `seed_lineage × 阈值` 的计数。本机核实 `results_summary.json`：阈值 5/20/50 的 departure 候选数 5/4/1，全部在 `closed_seeded`；return 候选 0），不做新计算。
- `hidden/literature_claims.json`：从 `HSP90_PAPER_ATLAS_CLAIM_COMPARISON.md` 的 HPA-02、03、04、05、08、10、11、14 各取论文侧陈述（`paper_claim, locator, polarity, object, condition`），6–10 条。
- 完成：`validate_case_package.py`（三目录存在、`common/` 无禁项、元数据档能被选择器读取）返回 0（1 次）。

### B3 冻结
- `freeze_hsp90_q01.py`：`common/`、`arm_B/`、`hidden/`、`RT/` 的 SHA-256 → `TASK2/outputs/frozen_hsp90_q01_v3.json`，含 `model: openai/gpt-5.6-luna, reasoning: medium, image: sha256:d99fa29f…, run_order: 随机化的 [A,A,B,B], budget_usd: 0.15, system_prompt_sha256, arm_B_rules_sha256, selector_branch: OK | EMPTY | FAILED`。唯一一次哈希。
- 冻结前把 A5 的分支结果写进冻结文件；`selector_branch != OK` 时 `run_order` 只含 A×2，报告按"无处理差异"写。

### B4 元数据起草：本轮跳过
- v2 的可选项需要新加 `--stage profile`（现有 `agent_run.py` 没有）、准备 schema、字段对照，且不影响本轮下游。跳过，记 `SKIPPED_BY_PLAN_V3`。自动元数据提取的价值另行判断。

## 5. 阶段 C：运行（Codex，半天，≤ $0.15）
```bash
export OPENROUTER_API_KEY=…        # PM 注入当前 shell
python3 "$RT/run_batch.py" --freeze "$TASK2/outputs/frozen_hsp90_q01_v3.json" --task-root "$TASK2" --budget-usd 0.15
```
- 4 次：A×2、B×2，顺序按冻结文件。
- 输出：每次 `answer.md, draft_*.json, receipt.json, events.jsonl`；`TASK2/outputs/results.json`
- 完成：4 份 receipt 齐；`results.json` 与 receipt 交叉一致（1 次检查）
- 停止：`UNKNOWN_CHARGE.json` → 停不重试；累计 > $0.15 → 停；模型算错/弃权/预算截停 → **保存为结果，不补跑**。
- **运行器 bug 分支：** 修一次。若修复只影响失败的那一次，只补跑该次；若修复会改变其他已完成运行的行为（提示、挂载、提交协议），保留原结果，写明受影响范围，预算内不能得到同版本的完整对照就交付不完整比较，不强行补齐。已跑不删。

## 6. 阶段 D：核对（Codex，1 天）：三件事分开记，看全文

先按同一份 `grading_rubric.md` 完成四份答复的科学判断，再看规则覆盖和组间差异。

**主张范围：** `answer.md` 全文里的重要主张（含没有数字的过强结论，例如"所有轨迹已收敛"）都进核对表，并核对与 `claims[]` 是否一致；正文有、数组没有的主张照样记。

`TASK2/outputs/check/<run>_claims_check.csv`：

| 列 | 取值 | 回答什么 |
|---|---|---|
| `provenance` | `FROM_CITED_FILE` / `FROM_AGENT_COMPUTATION` / `AUTHOR_REPORT` / `NOT_LOCATED` | 数字来自哪里；`AUTHOR_REPORT` 允许并需 locator |
| `reproducible` | `YES`（用 `events.jsonl` 中 Agent 自己的 python 代码 + `common/` 重跑得同值）/ `NO` / `NOT_ATTEMPTED` | 计算是否可复现；只支持"该计算可复现" |
| `input_checked` | `YES` / `NO` | 影响核心答案的分组、计数、单位，Codex 直接对照 `common/` 中的记录再核一次 |
| `method_note` | 自由文本，标 `DEVELOPER_JUDGMENT` | 方法是否适用于对象与问题；争议项不强行二元裁决 |
| `status` | `VERIFIED` / `MISMATCH` / `NOT_INDEPENDENTLY_VERIFIED` | 核对器不支持 ≠ 错误 |

文献关系表 `TASK2/outputs/check/<run>_literature_relation.csv`：Codex 手工对齐 `hidden/literature_claims.json`，每行 `agent_claim | paper_claim | locator | relation ∈ {AGREE, DISAGREE, PAPER_SILENT, AGENT_ABSTAIN, UNDETERMINED} | note`。`DISAGREE` 是与作者结论的关系，不是错误判定。

`hidden/rule_coverage_record.md` 事后填三列：B 组引用的 `rule_id` 哪些对应了实际分析动作、选择器遗漏了什么、哪些义务没带来内容。**规则引用次数不作为得分；出现某条规则引用，不足以证明该规则造成了改进**，只记"与该提醒一致的分析行为"。

验证记录：复现脚本 1 次；其余为人工表格。

## 7. 阶段 E：两层报告（Codex，1 天）

- `TASK2/outputs/AGENT_RAW/`：4 份 `answer.md` + `draft_*.json` + `receipt.json` 原样。
- `TASK2/outputs/HSP90_Q01_VERIFIED_REPORT_ZH.md`（+ HTML）：
  1. 元数据：论文声明 vs 本轮输入已核对（引 B0 卡）
  2. 问题与数据能回答的范围；本轮测到的是什么（§0 第二段原话）
  3. 逐轨迹观测变化：发生了什么、判据、按阈值的敏感性、与原文定义的关系、仍相容的解释（引 `status=VERIFIED` 的数字；`NOT_INDEPENDENTLY_VERIFIED` 可引但标注）
  4. 与 Henot 2022 的关系表（§6）
  5. Agent 原始交付的评价：四份各自答对/过强/弃权/未完成，引 `claims_check.csv`，含全文主张
  6. 规则提示改变了什么：B 相对 A 逐条记：多说、少说、说错、引用了哪个 `rule_id`、是否对应实际分析动作；不计数、不设阈值、不下因果结论
  7. 人工介入清单：报告中每一处非 Agent 产出的修正、补充、重述
  8. 未解决与下一步（覆盖题、收敛题的输入状态；选择器分支或运行器修改分支的影响范围）
- `REPLAY.md`：命令、哈希、系统提示与两组用户提示原文、确定性/LLM 边界、换问题要改哪些文件。

## 8. 交付后：由 PM 用五结果表决定，不自动推进

| 首轮结果 | 下一步 |
|---|---|
| A 已给出有用答案，B 没有明确帮助 | 保留普通流程继续科学工作；不为维护 Rules 追加开发 |
| B 帮助发现一个实质遗漏，且未损失可回答内容 | 保留这一具体用途；再到第二体系检查能否复用；不扩大成"Engine 有效" |
| **混合、负面或不稳定：** B 多答对一项同时引入严重错误、B 漏掉可回答内容、或 B 两次没有一致方向 | 完整报告收益与损失；本轮不支持扩张该规则提示的用途；不为得到明确胜负追加同题运行；PM 决定普通流程、暂停或提新的独立问题 |
| 关键错误来自元数据、输入缺失或工具未返回 | 按实际失败归因；不算成规则效果，也不修到答案必然正确 |
| 必须不断新增题目专用代码或核对器才能交付 | 停止系统扩展；先交付已有科学结果与真实限制 |

Pro 审阅 §7 报告；意见按条记 `disposition.json`（`FIX/RECORD/REJECT` + 理由），处置完成不构成进入下一阶段的条件。

## 9. 停放项与后续条件（不在本轮）

- 收敛题：输入在 `WS/autoresearch/tasks/dynamics_atlas_hsp90_coverage_stability_v0_20260730/outputs/`（`prefix_horizon_routes.tsv`、`trajectory_anchor_proximity.tsv`；v2 写错了任务目录）；若进入，须允许"某量在前缀窗口内变化小"与"不足以估计平衡比例"两结论并存；CPMG 交换态与 MD 几何类别的对应不自动成立。
- 覆盖题：现有 `landscape_projection.tsv` 只有投影，无坐标矩阵与变换（B1 `PROJECTION_ONLY`）；要做需先确认坐标与对齐方式在本机，对已有轨迹做后处理不算新 MD。
- 第二体系（ADK / DHFR）：只在 PM 按 §8 决定后开始（Soojung 8/24："根据反馈决定下一案例是 DHFR 还是 ADK；不同时做两者"，`WS/autoresearch/tasks/dynamics_atlas_soojung_meeting_transcript_prototype_20260824/outputs/03_FIXED_RESEARCH_PLAN_AND_PROTOTYPE_BUILD_ZH.md` 第 124 行）；选择时须写明两类资料的构建体与条件、具体可比性质、现有方法能给出哪项有用答案；"方法最多新增一个定义"只是工程成本上限。第三体系不承诺。
- B4 元数据起草、V2a 旧记录汇总、从元数据推公开事实、通用评分模板、通用文献比对、`drift_check.py`：不做。

## 10. 预算（执行记录，不是硬性科学标准）

| 阶段 | 工作日 | 模型费用 | 检查命令 | 哈希 | 审阅 |
|---|---|---|---|---|---|
| A 环境与系统 | 2 | 0 | 4 | 0 | 0 |
| B 案例 | 2 | 0 | 2 | 1 | 0 |
| C 运行 | 0.5 | ≤ $0.15 | 1 | 0 | 0 |
| D 核对 | 1 | 0 | 1 | 0 | 0 |
| E 报告 | 1 | 0 | 0 | 0 | 1（Pro） |
| **合计** | **6.5（上限 7）** | **≤ $0.15（上限 $0.20）** | **8** | **1** | **1** |

七天内完成必要验证即可。一次确有必要的核对不因"只检查一次"被挡；没有信息增益的检查也不为凑表重复。每阶段结束写 `TASK2/state/validation_ledger.jsonl`：计划的检查、实际跑的、跳过的及理由。

## 11. 对 Pro 审查意见（v2）的处置，以及本机核实新增的修正

### 11.1 Pro 意见

| Pro 意见 | 处置 | 落在 |
|---|---|---|
| 运行器 `ROOT` 由代码位置推断，搬到 harness 后找不到 TASK2 | FIX：`--task-root`；六项状态全部从任务目录读 | §2、A6 |
| A/B 无条件读 `PUBLIC_FACTS.json` | FIX：A/B 不读、不加载 C 政策；`run_batch.py` 拒绝 C | §2 |
| 共同提示指向不存在的 `method_sources/SOURCE_MAP.txt` | FIX：提示第三段改指 `SOURCE_INVENTORY.json` 与 `FIELD_DEFINITIONS.md` | §2 |
| `$HARNESS-luna` 不是变量 | FIX：`HARNESS_LUNA` | 路径约定、A2、A7 |
| 用维护版，不恢复覆盖答案缺陷 | FIX：写明搬运的是已打补丁的 `TASK0/runtime/`，`before/` 不搬 | §2 末段 |
| 本轮账本从零起，旧账本不混入 | FIX | §2 预算行 |
| 路径接通要用真实启动验证，不只 import | FIX：A4 第三项集成用例 | A4 |
| A4 "`-v` 只含 common" 会误伤 `/work`、`/tool.py` | FIX：改为"案例资料只挂 `common/`，允许 `/work`、`/tool.py`"；递归检查后代与链接解析 | A4 |
| 不用"A 无 `rule_id` 字样"代替内容隔离 | FIX：比较实际消息 | A4 |
| `FIELD_DEFINITIONS.md` 不复制历史"建议怎样回答"与允许/禁止措辞 | FIX：含结论文字的历史文件进 `hidden/` | B1 |
| A 不是裸模型，B−A 是共同指导之上的额外效果 | RECORD | §0 第二段 |
| B0 分开"论文声明"与"本轮输入已核对"；单条抽查不推广 | FIX：卡片两层；抽查标 spot check；优先核派生表时间列 | B0 |
| B1 搜索模式会漏掉已登记的 `frame_state_assignments.tsv` | FIX：改为优先核对具名文件（已本机核实存在与规模），去掉泛搜 | B1 |
| 一条轨迹三个持续性设置；departure 相对第一个持续方向；帧数式时间约定；分箱不能恢复连续段 | FIX：写进 `FIELD_DEFINITIONS.md` 七条 | B1 |
| 不修历史结果追求一致 | FIX | B1 末 |
| "Codex 手写，不由模型起草"改为准确角色 | FIX：`DEVELOPER_PREPARED_TRACEABLE_NOT_DOMAIN_CONFIRMED` | B2 |
| 不预设两个 SOURCE 一条 EDGE；CPMG 不与结构参照合并 | FIX | B2 |
| 隐藏评分不得增加题面没提的强制交付；不固定四个英文标签；两个"占比/速率"范围分开 | FIX：题面加"写明比较条件、时间窗口、统计单位"；评分只罚改变结论含义的遗漏 | B2 题面、rubric 第 1、3 条 |
| 核对看全文，不只 `claims[]`；先科学判断再看规则；引用次数不是得分；核心计数直接对照输入 | FIX：`input_checked` 列；全文主张进表 | §6 |
| §8 缺"混合/负面/不稳定" | FIX：加一行 | §8 |
| 选择器失败或规则为空的分支 | FIX：冻结前写清，不手挑规则 | A5 分支、B3 |
| 运行器修改后的影响范围 | FIX | §5 分支 |
| 规则引用 ≠ 因果 | FIX | §6、§7 第 6 节 |
| 跳过 B4 | FIX | §0、B4 |
| 检查次数与哈希是记录，不是硬标准 | FIX | §10 |
| 云端暂存区不构成批量提交授权 | RECORD：本文件不涉及 `~/claude-cloud-workspace`；提交前须确认 diff 只含计划文件 | — |

### 11.2 本机核实新增的修正（v2 里 Codex 会卡住的地方）

| 发现 | 修正 |
|---|---|
| `rule_registry.tsv` 是逗号分隔（0 个制表符） | A5 写明用默认分隔符读 |
| 选择器只对 `REGISTERED_FOR_METADATA_REVIEW` 的方法做选择；`MD_TRAJECTORY` 现为 `NEEDS_METHOD_DEFINITION`；七字段来自 `required_definition_fields` | A5 写明副本要改的字段与七字段来源 |
| lincoff 样例选出 51 条义务，很多共享 `rule_id` | 渲染按 `rule_id` 分组，否则 B 组提示过长 |
| `TASK0/runtime/readiness.json` 是 `approved_for_development: false`，运行器启动即断言失败 | 授权第 5 项；本轮 `TASK2/runtime/readiness.json` |
| `test_runner_offline.py`、`test_submission_maintenance_offline.py` 是断言脚本，`unittest discover` 找不到 | A2 完成标准改为直接运行 |
| `agent_run.py` 没有 `--stage`；`--image` 是必填 | B4 跳过；批处理传 `--image` |
| Docker 守护进程当晚未运行；镜像 `atlas-luna-development:20260909` 无 Dockerfile 或构建记录 | A0 预检；镜像缺失即停 |
| 宿主机与容器都没有 MDAnalysis | B0 时间轴改读派生表 `time_ns` 列；XTC 抽查可选 |
| 旧报告的 AMBER99SB 来自 Zenodo 记录描述 | B0 记为资源描述与论文不一致，不是误抄 |
| 作者 README 写 1020 帧，本机实测 1021，派生表 1001 | B0 三者对应关系写明 |
| R60A 的 `md_0-10_…xtc` 是符号链接，实际用 `md_all_prot_fit.xtc` | B0 `lineage` |
| `HSP90_PAPER_ATLAS_CLAIM_MATRIX.md` 只是 302 字节指针 | B1/B2 改用 `…CLAIM_COMPARISON.md` |
| `prefix_horizon_routes.tsv`、`trajectory_anchor_proximity.tsv` 在 `coverage_stability_v0_20260730`，不在 `time_anatomy` | §9 路径改正 |
| `route_predictions.tsv`、`event_and_window_stability.tsv` 含历史结论文字 | 进 `hidden/` |
| 覆盖题输入只有投影 | B1 `PROJECTION_ONLY` |
| `check_model.py` 也从会话记录抠 key | A3 同改 |

## 12. 失败账本
任一步两次修补仍失败：停止编辑，写 `TASK2/outputs/failure_ledger_<step>.md`（尝试的修法、预期机制、实际结果、假设为何变弱、重复了什么假设、下一个替代假设），进 §7 报告的"未解决"节。

## 13. 给 Codex 的一句话

采用 v2 的一题四答复范围，按本版补齐任务路径与旧依赖、数据字段说明、输入隔离、全文核对和混合结果处理；跳过 B4，不扩框架。负责人授权 1–5 落实、A0 预检通过后直接执行；七个工作日内交科学结果或具体失败原因，不追加同题运行来追求通过，也不等待下一轮 Pro 批准。
