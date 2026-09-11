# Dynamics Atlas 完整计划表（截至 2026-09-10，汇报用）

一句主线：**我们要从异质蛋白动力学资料得到有用、可复核、不过度的科学回答；Rules Table 是为此提出的一种方法，现在已经在真实数据上试过一轮，科学回答拿到了，方法本身的价值还没证明。** 下面每一行都回到最初的四个目标（G1–G4）上说清楚：做了什么、证据在哪、下一步是什么、谁来定。

## 一、按最初目标看进度

| 目标 | 当初要做什么 | 已完成（证据） | 进行中 / 未完成 | 下一步 | 停止条件 | 谁决定 |
|---|---|---|---|---|---|---|
| **G1 可靠性科学**：说清哪些 ensemble 量可信 | 在明确表示、条件、时间语义、统计单位后回答具体问题 | **HSP90**：闭合起始 20 条中 10 条在 1 μs 内出现持续开放方向（5 条几乎一开始就开、5 条先闭后开），开放起始 0 条反向；原生 NOE 对照：1 Å 容差下这 10 条里 9 条仍同时偏离两套 NOE 参照，只有 ES04、ES15 进入开放参照带（对应论文"almost compatible"，不是到达开态）。证据：PR #27 `review/hsp90_q01-round-20260910/`，`v4_native_noe/` | 原生读数支持"近闭 / 漂离两者皆非 / 趋开"三类描述，比双读出符号规则更接近论文的 7/9/4，尚未按预注册阈值正式做 | 一次预注册的小步骤：三类阈值先定死，做逐轨迹三类表，不为凑 7/9/4 调阈值 | 阈值一旦调整即停并记录 | PM |
| **G2 跨模态 landscape**：公平比较不同来源 | 识别 shared / unique / unresolved 区域 | HSP90 的 MD 派生量与 NMR 结构参照、作者 NOE 违例序列已在同一张逐帧表上对齐（40 条 × 1001 点） | 覆盖题（PCA 投影只有投影没有坐标矩阵）、收敛题停放 | 只在 G1 的三类表做完后再决定是否开覆盖题 | 缺坐标与变换矩阵即不做 | PM |
| **G3 可复用 workflow**：换数据能复跑 | 固化方法、输入、参数、来源、执行与审核 | **DHFR** 一轮证明流程可以换数据复用：下载 1.02 GB 作者沉积轨迹、两次普通 Agent、核对、汇报包；科学结果：4′-DTMP 比 TMP 更靠近 M20 环与 R28（O4P/O5P），WT 与 L28R 都成立，每条件一条轨迹（n=1，MD 单一来源） | DHFR 建包在冻结前漏了坐标周期性检查，Agent 拿到带假大距离的表；成果只在本机，未入库推送。**ADK** 只有盘点，数据 1.37 GB 可下 | 先把 DHFR 入库并补边界句；ADK 按"冻结前物理语义硬门"重做建包，两次普通 Agent，三体系总记录 | 5 个工作日、ADK ≤ $0.15、追加下载 ≤ 1.5 GB；物理硬门两次不过即停 | PM 授权 8–10 |
| **G4 有限 Agent 自动化**：Agent 能否减少整理成本而不增加不安全 claim | 在冻结基线上检验 Agent，Rules 是其中一种约束方法 | 12 次开发运行（9/9）+ HSP90 四次（9/10）+ DHFR 两次：Agent 能自主读表、算数、交答复；HSP90 四份里三份主计数对、一份混阈值；DHFR 两份都没识别输入缺陷。**Rules**：规则提示把 FRET 专用条件带进了答复，选择器把通用检查绑到了带专用条件的原条款上；渲染层已修，未重测 | Rules 增益未建立，也未被否定；自动扩展已按预定规则暂停 | 不重跑同题求胜负；ADK 只跑普通 Agent；Rules 是否重测由三体系结果后 PM 决定 | 任一轮出现为好看重跑、改评分、补造答复即判无效 | PM |
| **治理与交付** | 对外可读、可批评 | 进度报告（10 页 deck）、HSP90 报告（12 页）、NOE 对照（7 页）、DHFR（9 页）、每周五自动一页周报 | 8/25–9/04 两周只有内部产物；DHFR 未推送；无领域专家独立评审 | 每轮结束必须过汇报包检查并推送；每周五一页对外更新 | 没有交付物不出新版计划 | Codex 执行，PM 看 |

## 二、时间线（只留改变判断的节点）

| 日期 | 节点 | 得到了什么 |
|---|---|---|
| 07-25 → 07-30 | HSP90 数据接入、v1 科学分析、时间解剖 | 逐帧派生量、三阈值方向表；两处文档差异（力场、帧数）分别保留 |
| 07-28、08-24 | 与 Soojung 两次会 | 先把已有 HSP90 讲清楚；原型先小后大；HSP90、DHFR、ADK 为候选，不同时做 |
| 08-05 → 08-16 | Rules Table v0.1（12 篇论文 33 条）、选择器、Pro 审查 | 条款可追溯到文献；数量不等于正确率 |
| 08-25 → 09-04 | 原型、PR #1–#24、基准、交接 | 工程证据积累快，对外叙事停滞 |
| 09-09 | 12 次 Luna 开发运行 | Agent 能算；交付会被覆盖；有限检查防不住具体错误 |
| 09-09 → 09-10 | 计划 v1 → v3.4（Pro 三轮） | 缩到一题四答复，评分独立于规则，自动判定与停止线 |
| 09-10 | HSP90 首轮四次运行（45 分钟，$0.076） | 5/5/10 分区；A1 B1 B2 对、A2 错；规则专用条件迁移；暂停扩展 |
| 09-10 | v4：进度报告、首轮收口、NOE 对照、渲染修复 | "出现开放方向 ≠ 接近开态"；两条进入开放参照带 |
| 09-10 | DHFR 一轮（$0.032，1.02 GB） | 4′-DTMP 更近 M20 环；冻结前漏了周期性检查 |
| 下一步 | DHFR 入库 → ADK → 三体系总记录 | 见收官令 |

## 三、今天汇报够不够：够，但要按下面的口径讲

**结论：足够做一次组会进度汇报。** 有两项经过独立复算的 HSP90 科学结果、一项有边界的 DHFR 结果、一个关于 Rules 的具体发现、四份现成 deck。不够的地方要明说，不要藏。

### 15 分钟的页序（全部从现成 deck 抽，不用新做）

| 页 | 来源 deck | 标题 |
|---|---|---|
| 1 | 进度 deck 1 | Dynamics Atlas: a scientific answer comes first |
| 2 | 进度 deck 2 | The goal: connect evidence to a bounded answer |
| 3 | 进度 deck 4 | The path: data → rules → agent answers |
| 4 | HSP90 deck 3 | We ask whether closed-seeded trajectories show opening |
| 5 | 进度 deck 6 | Half show open direction, through two different histories |
| 6 | HSP90 deck 8 | A sustained open segment is not the same as a transition |
| 7 | NOE deck 1 | Open direction does not guarantee near-open NOE agreement |
| 8 | NOE deck 6 | Two closed-start traces enter the open-start reference band |
| 9 | HSP90 deck 9 | Three answers recover the counts; one confuses thresholds |
| 10 | HSP90 deck 10 | Selected rules carried method conditions into the wrong context |
| 11 | DHFR deck 5 | 六项指定环区比较均显示 4′-DTMP 更近（讲明 n=1、MD 单一来源、流程复用测试） |
| 12 | DHFR deck 4 | 存储坐标的大距离主要来自周期性包装（讲成"建包流程的教训"） |
| 13 | 进度 deck 9 | The bottleneck: turn work into usable delivery |
| 14 | 新加一页（用本表第一节） | 按 G1–G4 的下一步与需要决定的事 |

### 可以说的话
- HSP90 闭合起始一半轨迹在 1 μs 内出现持续开放方向读数，开放起始零条反向；这是派生判据下的方向不对称。
- 原生 NOE 对照表明多数"开放方向"片段仍未接近开态定义，只有两条进入开放参照带；与论文"almost compatible"一致。
- Agent 能自主完成真实计算并交付答复；四份里三份主计数正确。
- 规则提示存在具体的方法适用性问题：通用检查被绑到带 FRET 专用条件的条款上。这是本轮对 Rules 最有价值的发现。
- 同一流程换到 DHFR 数据能复跑，得到一个有边界的局部接触结果。

### 不能说的话
- 不说"Rules 有效"或"Rules 无效"；说"增益未建立，问题已定位"。
- 不说"复现了论文的 7/9/4"；说"方向相容，统计对象不同"。
- 不说 DHFR 是跨来源结果；它是 MD 单一来源、每条件一条轨迹的复用测试，且科学数字是开发者修正后算的。
- 不说"已经过独立评审"；目前只有开发者核对与 Pro 的咨询审阅。
- 不说 ADK 已做；只有盘点。

### 汇报前要做的两件小事
1. 把 DHFR 推送到 PR #27（收官令第 1 步），否则链接点不开。
2. 第 14 页用本表第一节做一张"目标 × 下一步 × 谁决定"的表。

## 四、下一步总表（一次授权，Codex 自动推进）

| 顺序 | 做什么 | 天 | 费用 / 下载 | 完成证据 | 停止条件 |
|---|---|---|---|---|---|
| 1 | DHFR 入库、补边界句、更新状态面板 | 0.5 | 0 | PR #27 `review/dhfr_q01-round-20260910/` | — |
| 2 | ADK 建包：下载 Zenodo 5583119（1.37 GB），冻结前物理语义硬门（帧数、盒子与周期性、单位、原子映射、条件对应） | 1.5 | ≤ 1.5 GB | `PREFREEZE_PHYSICAL_CHECK.json` 全 PASS，`FREEZE.json` 早于首份答复 | 硬门两次不过即停 |
| 3 | ADK 两次普通 Agent、核对、独立复算、汇报包、入库 | 2 | ≤ $0.15 | `independent_recompute.json`、`report_bundle_check.py` PASS | `UNKNOWN_CHARGE` 即停 |
| 4 | 三体系总记录 + 工作证据表 + 偏离自述 | 1 | 0 | `THREE_SYSTEMS_RECORD_ZH.html`、`WORK_EVIDENCE_LEDGER.json`、`DEVIATIONS.md` | — |
| 5（之后，PM 定） | HSP90 三类表（预注册）；Rules 修复后的一次重测；是否请领域专家看 | — | — | — | — |

授权句：**"授权 8–10，按 THREE_SYSTEMS_COMPLETION_ORDER_ZH.md 执行。"** 总预算已用 $0.108 / $0.30，下载 1.02 GB / 2 GB（ADK 追加 1.5 GB）。
