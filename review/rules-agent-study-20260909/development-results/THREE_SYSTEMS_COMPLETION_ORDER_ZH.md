# 三体系收官令：把 ADK 做完，交一份三体系总记录，并留下能被检验的工作证据

Dynamics Atlas · 2026-09-10 · **供 Codex 无人值守执行** · 接在 v4 之后（HSP90 两轮已完成，DHFR 一轮已完成但未入库，ADK 只有盘点）· PM 回复"授权 8–10，按收官令执行"即开工

## 0. 现在到哪了（PM 读这一段就够）

| 体系 | 状态 | 科学结果 | Agent 表现 | 证据在哪 |
|---|---|---|---|---|
| HSP90 | **完成两轮** | 闭合起始 20 条中 10 条出现持续开放方向（5 首开 + 5 先闭后开），开放起始 0 反向；原生 NOE 对照：1 Å 容差下 10 条里 9 条仍同时偏离两套参照，只有 ES04、ES15 进入开放参照带；对应论文"almost compatible"，不是到达开态 | A/B 各两次：A1、B1、B2 主计数对，A2 混阈值；规则把 FRET 专用条件带进答复 → 暂停自动扩展 | PR #27 `9b91c04`，`review/hsp90_q01-round-20260910/` |
| DHFR | **完成一轮，本地未入库** | 4′-DTMP 比 TMP 更靠近 M20 环与 R28（O4P/O5P），WT 与 L28R 都成立；每条件一条轨迹 990 帧，是开发者修正周期性包装后的计算 | 两次普通 Agent 都算了，但输入是冻结前未做周期性检查的距离表，两份都没识别假大距离；A1 另有比例转述错误 | 本机 `autoresearch/tasks/dynamics_atlas_adk_plain_agent_v1_20260910/`（目录名写的是 adk，内容是 DHFR），**未提交、未推送** |
| ADK | **只有盘点** | 无 | 无 | 同上目录 `outputs/ADK_DATA_LANDSCAPE.md`；Zenodo 5583119 在 Codex 沙箱超时，本机从外部核过：4 个文件 1.37 GB，CC-BY-4.0（开/闭两条轨迹各一 xtc + gro） |
| Rules | 暂停扩展 | 渲染层修好了"原条款 vs 本题检查"的区分，没有再测 Agent 行为 | — | PR #27 `agent_experiments/luna_runtime_v1/` |

费用：HSP90 $0.076 + DHFR $0.032 = $0.108（v4 上限 $0.30）。下载：DHFR 1.02 GB（v4 上限 2 GB）。凭证：已从旧记录取回一次并存进钥匙串（`openrouter` 与 `codex.openrouter.OPENROUTER_API_KEY` 两个别名），以后从钥匙串读。

## 1. 有没有偏离最初目标（审查结论）

最初目标：从异质蛋白资料得到有用、可复核、不过度的科学回答；Rules 是待检验的方法。

- **HSP90 没有偏。** 两轮都在做"派生判据 vs 原生观测"这类跨来源的可靠性问题，结论带 n、窗口、统计单位和上限。
- **DHFR 偏了一点，可以接受但要说清楚。** 题目是"MD 逐帧距离能否支持作者图 4 的局部接触描述"，这是单一来源（MD）内部的比较，论文的 Ki 和抑制实验只作定性背景；每个条件只有一条轨迹，统计单位 n = 1。它检验的是"换一套数据，同一流程能不能复用"（G3），不是异质资料可比性（G1/G2）的结果。报告里应把这句话写在第一段。
- **DHFR 暴露的真问题是建包流程：** 在冻结前没做坐标物理语义检查（周期性包装），Agent 拿到的是带假大距离的表，所以这轮报告的科学数字是 Codex 事后修正后自己算的，Agent 评价对这轮无效。Codex 如实记录了，没有重跑去掩盖，这是对的；但 ADK 不能再犯：**冻结前物理检查是硬门**（§3 第 2 步）。
- **Rules 没有被偷偷复活，也没有被丢掉。** 状态是"暂停扩展、修了渲染、待重测"，符合 Pro 与 PM 的决定。
- **交付纪律：** v4 之后每轮都有简报、读本、deck；但 DHFR 这轮没有入库推送，PR 上看不到。

## 2. PM 一次性授权（新增三项，其余沿用 v4 授权 1–7）

| 项 | 内容 |
|---|---|
| 8 | ADK 下载：Zenodo 5583119 全部 4 个文件 ≈ 1.37 GB（CC-BY-4.0），本轮下载上限在 v4 基础上追加 1.5 GB；仍只允许 PDB / BMRB / Zenodo / 论文 SI 来源，记 sha256 与许可证 |
| 9 | ADK 两次普通 Agent（A-only）≤ $0.15；不跑 B 组，不跑新 MD，不做前向散射计算以外的新方法（前向计算只允许用论文自己给出的已发表方法与参数，且限一种） |
| 10 | 把 DHFR 一轮与 ADK 一轮的报告目录提交到 `feature/luna-runtime-v1`（PR #27），PM 负责 push；`runs/`、数据文件、账本、凭证不入库 |

## 3. 执行顺序（Codex 不问人，5 个工作日内全部交付）

### 第 1 步：先把 DHFR 入库（半天）
- 把 `dynamics_atlas_adk_plain_agent_v1_20260910/outputs/{report/,AGENT_AUDIT_ZH.md,check/,PBC_VALIDATION.json,POST_FREEZE_ISSUE.md,REPLAY.md,DOWNLOAD_MANIFEST.json,FREEZE.json}` 复制到 `HARNESS_LUNA/review/dhfr_q01-round-20260910/`，提交。目录名的 `adk` 误导，在 `REPORT_INDEX.md` 首行写明"本目录是 DHFR 轮次"。
- DHFR 报告第一段补三句：单一来源 MD 内部比较；每条件一条轨迹；本轮科学数字是开发者修正后的计算，Agent 在缺陷输入上的答复不作为分析能力证据。
- 更新 `DYNAMICS_ATLAS_STATUS.md`（v0.256）与决策日志一条。

### 第 2 步：ADK 建包，冻结前过"物理语义硬门"（1.5 天）
- 任务：`dynamics_atlas_adk_plain_agent_v2_<date>`（新目录，不复用写着 DHFR 内容的旧目录），回执 PASS。
- 下载 4 个文件，记清单；沙箱内 Zenodo API 超时就用文件直链加 `--max-time 600` 分段重试，三次仍失败 → 停，交阻塞报告，不猜。
- 论文：Orädd 等 2021《Tracking the ATP-binding response in adenylate kinase in real time》（PMC8597995）。题面必须是论文自己陈述的一个可比较性质，例如"ATP 结合后 LID/NMP 结构域闭合的时间顺序或幅度，MD 构象与时间分辨 X 射线溶液散射差谱的对应"。若 SI 或数据库里拿不到数值散射差谱，题目**降级**为 MD 内部的开/闭两条轨迹结构域距离比较，并在题面和报告第一段明确"单一来源"。
- **冻结前物理语义检查（硬门，全部 PASS 才能冻结）：** 帧数与时间轴（首帧、末帧、步长）；盒子与周期性（用最小映像或 `gmx trjconv -pbc mol` 处理后再量距离，任一残基对距离 > 盒长一半即 FAIL）；单位（nm/Å）；原子映射（gro 中的残基编号与论文编号对照表）；两条轨迹的构建体、配体、离子条件是否与论文一致；每项写进 `PREFREEZE_PHYSICAL_CHECK.json`。这一步就是 DHFR 那轮缺的。
- `common/` 只放派生量表、字段定义、论文文本、来源卡；坐标不进 `common/`（容器里没有 MDAnalysis）。rubric 与 `literature_claims.json` 在运行前冻结，哈希进 `FREEZE.json`。

### 第 3 步：两次普通 Agent + 核对 + 报告（2 天）
- `run_order = [A, A]`，≤ $0.15；分支同 v4 §5。
- 核对：三列 + 全文主张 + 逐句真实引文的论文关系表（`check_relation_tables.py` 必须过）；每个报告数字由 Codex 用独立脚本再算一遍（`independent_recompute.json`，与 Agent 数值逐项对照）。
- 汇报包：简报、读本、9–12 页 deck、`REPORT_INDEX.md`、`review_report.md`，`report_bundle_check.py` 过；入库到 `review/adk_q01-round-<date>/`。

### 第 4 步：三体系总记录 + 工作证据表（1 天）
- `review/THREE_SYSTEMS_RECORD_ZH.md/.html` + 10 页 deck：每个体系一节，固定字段：问题 · 数据与统计单位 · 冻结时间 · 得到了什么（带 n、单位、窗口）· 证明了什么 / 没证明什么 · Agent 表现（逐份）· 人工介入 · 费用与时间 · 证据路径。最后一节写"三个体系合起来能说什么、不能说什么"，不写"Engine 有效/无效"。
- **工作证据表 `WORK_EVIDENCE_LEDGER.json`（PM 用来检验 Codex 有没有好好干）**，每体系一行，每项给可点开的路径或哈希：

  | 检查项 | 通过标准 | 证据 |
  |---|---|---|
  | 题目与评分在运行前冻结 | `FREEZE.json` 时间早于第一份 receipt；rubric 哈希在冻结文件里 | 路径 + 两个时间戳 |
  | 输入在冻结前做过物理检查 | `PREFREEZE_PHYSICAL_CHECK.json` 全 PASS（DHFR 一轮如实记 FAIL_AFTER_FREEZE） | 路径 |
  | Agent 原答未改 | `AGENT_RAW/` 文件哈希 = receipt 记录的哈希 | 哈希对 |
  | 每个报告数字有独立复算 | `independent_recompute.json` 逐项一致；PM 一条命令能重跑 | 命令 + 输出路径 |
  | 论文关系表是真引文 | `check_relation_tables.py` PASS；无占位句、无跨文件相同 | 校验输出 |
  | 上限句在报告里 | 单一来源 / n / 窗口 / 不是平衡占比 / 开发者核对非独立评审 | 行号 |
  | 汇报包完整 | `report_bundle_check.py` PASS | 输出 |
  | 已入库推送 | PR #27 上能点开 | commit 哈希 |
  | 账本对得上 | 账本合计 = 报告费用 | 两个数 |
  | 偏离自述 | 本轮所有偏离计划的地方一条不漏（DHFR 的周期性检查、凭证取回等） | `DEVIATIONS.md` |

- **红旗清单（PM 看到任何一条就该追问）：** 报告里的数字在产物里找不到；关系表有占位句或多份相同；rubric 在运行后被改过；为了好看重跑同题；简报没有边界句；`runs/` 里的 events.jsonl 比答复短得离谱；费用与账本对不上；有下载没有清单。

## 4. 停止线
- 5 个工作日；ADK ≤ $0.15；下载 ≤ 1.5 GB 追加；任一 `UNKNOWN_CHARGE.json` 全停；物理硬门 FAIL 两次修补未解 → 停，交阻塞报告；需交互登录或额外授权 → 停。停下来也要交第 4 步的总记录（把 ADK 记为未完成及原因）。

## 5. 给 Codex 的一句话
先把 DHFR 入库并补上单一来源与 n=1 的边界句；再做 ADK：下载 Zenodo 5583119，冻结前过物理语义硬门，两次普通 Agent，独立复算，汇报包入库；最后交三体系总记录和工作证据表，偏离一条不漏。不跑 B 组，不跑新 MD，不为好看重跑。授权 8–10 到位即开工，5 个工作日到线即停。
