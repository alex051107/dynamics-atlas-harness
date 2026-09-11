# Dynamics Atlas × Soojung 会议纪要与行动解析

> 版本：2026-07-28  
> 状态：基于两段自动转写的第一版完整纪要  
> 用途：把会议内容转成可执行任务；不是实验结果，也不是 Soojung 已批准的正式 proposal  

## 先读这一页：会议到底改变了什么

这次会议没有否定 Dynamics Atlas，也没有要求我们立刻搭一个完全自治的 Agent。
Soojung 对“不同 representation 使用不同分析、把流程做成可复用 workflow、允许以后
由社区贡献分析 harness”的方向是认可的。但她也很明确：**现有 HSP90 smoke test
只做到了一个合理的起点，还没有把这批数据能够提供的科学信息真正展示出来。**

因此，下一轮工作的正确顺序不是继续扩写抽象 schema，也不是先做通用 Agent：

```text
先查清楚已有文献怎样做
→ 冻结一套有依据的 HSP90 v1 分析协议
→ 补出可视化、状态转变、excursion、平衡/收敛分析
→ 把这次真实执行固化成可复跑 harness
→ 再拿第二个相似 packet 检查能否复用
```

这里的三个工作方向——完善实验、搜索已有方法、准备 Agent harness——不是三个彼此
独立的项目。它们的因果关系是：

> **已有方法约束实验怎么做；真实实验产生可验证的执行路径；执行路径再被固化成
> harness。**

如果先造一个通用 Agent，再寻找科学方法和实验对象，顺序又会倒过来。

---

## 1. 来源、顺序和纪要规则

### 1.1 原始文件

| 编号 | 文件 | SHA-256 | 在会议中的顺序 |
|---|---|---|---|
| P2 | `audio1173668587-文稿-转写结果.docx` | `4dd467d0...e4f4c6c3` | 第一段 |
| P1 | `1785191764670-文稿-转写结果.docx` | `7339ec83...dd70ead` | Zoom 中断后的第二段 |

完整哈希保存在 `outputs/claim_source_map.jsonl`。P2 的最后一句在讨论 harness 时中断，
P1 开头明确提到 Zoom time limit，并继续同一问题，因此顺序不是按文件名判断，而是由
对话连续性确认。

### 1.2 说话人

- P2：说话人 1 = Soojung；说话人 2 = Alex/Zhenpeng。
- P1：重连后编号反转；说话人 2 = Soojung；说话人 1 = Alex/Zhenpeng。

### 1.3 本纪要的五种标签

- **[会议事实]**：转写里直接说过，并带 `P2:Lx-y` 或 `P1:Lx-y`。
- **[项目事实]**：由本地 proposal、代码、输入或结果文件直接支持。
- **[意图解析]**：对一句话在项目中的含义所作的解释。
- **[建议]**：下一步可执行方案，尚未被 Soojung 批准。
- **[待确认]**：录音含糊、科学定义未冻结，或需要 Soojung/原始来源确认。

---

## 2. 会议目的和合作背景

### 2.1 这次会谈的直接目的

Alex 希望在 proposal 写成后，用一个很小的 HSP90 test 把 Atlas 的想法变得具体：
说明新数据怎样进入系统、怎样形成 structured contract、怎样按 representation
选择分析、怎样形成 profile 和跨资源比较结果，并展示一个 NMR ensemble + MD
trajectory 的 proof of flow。[会议事实：P2:L24-30；P2:L80-105]

### 2.2 Stephanie 与合作背景

Soojung 说明，与 Stephanie 所在团队的正式合作尚未完全建立。Soojung 已经在另一个
DARPA 相关项目中与 Stephanie 合作，主题涉及 protein dynamics representation
learning；她向对方提出了分析并建立更好 dynamics benchmark 的想法，对方认可其
必要性并愿意继续讨论。[会议事实：P2:L46-70]

Stephanie 的价值主要在实验侧：她熟悉从 X-ray crystallography、NMR 等实验数据中
能够提取什么 dynamics，以及这些实验数据能否用于机器学习训练。转写中实验名被识别
为 `cupid`，目前无法可靠恢复专名，所以不能擅自改写成 qFit 或其他方法。
[会议事实：P2:L61-78；待确认：实验专名]

**意图解析：** 周五与合作方的交流，不只是展示软件。真正需要建立的是：

1. 我们对每类数据“能看到什么、看不到什么”的理解；
2. 一个真实数据例子；
3. 专家能够指出 state definition、实验信息和比较逻辑哪里不对。

---

## 3. Alex 在会上提出的 Atlas 设计

Alex 介绍的核心思想是：不把 trajectory、unordered ensemble 和 endpoint structures
强行塞进同一个 feature matrix，而是保留各自的 representation 和 source-native
measurement；把系统身份、condition、time semantics、scientific question、
analysis choice、provenance 和 supported statement 固化成 structured contract。
[会议事实：P2:L105-170]

他描述的新数据路径是：

```text
paper / README / metadata / raw dataset
→ identify molecule and condition
→ record representation and time semantics
→ identity/schema check
→ select representation-appropriate adapter
→ source-appropriate analysis
→ Dynamics Profile
→ compare profiles that address a common question
→ evidence file + unresolved issues + recommended next action
```

[会议事实：P2:L130-151]

JSON 被提出作为保存 contract、analysis、profile 和 evidence 的一种机器可读形式。其
目的不是把大型轨迹复制成一种通用格式，而是让假设、输入、方法和结论可检查。
[会议事实：P2:L144-156]

### 3.1 Soojung 对设计的态度

Soojung 认可：

- workflow 的整体方向；
- 让人们公开贡献或审查 harness，使 Atlas 逐步演化；
- 大规模数据分析确实需要可复用 workflow，即使专家知道方法，也仍需反复搭建流程。

[会议事实：P2:L207-227；P2:L516-538]

但这不是对现有 Atlas 实现的最终验收。她紧接着指出：当前 HSP90 state dominance
分析合理但偏基础，周五需要展示“这批数据究竟还能做什么”。
[会议事实：P2:L364-380；P2:L471-480]

---

## 4. HSP90 smoke test：会上理解到的输入、做法和问题

### 4.1 会上展示的输入

- 两个 deposited NMR structural ensembles；
- 四条 MD trajectories；
- open / closed / ambiguous 作为希望恢复的 state interpretation；
- MD 不是 Alex 自己运行，而是来自论文关联数据。

[会议事实：P2:L229-248]

Alex 在现场对 trajectory 长度、抽帧间隔和 frame 数没有把握。这一点本身成为
Soojung 后续强调最低元数据的原因之一。[会议事实：P2:L250-259]

### 4.2 会上解释的初始分析

Soojung 对当前做法的理解是：

1. 用 NMR models 构造 PCA/conformational space；
2. 把 MD trajectory 投影到这个空间；
3. 聚类或利用 NMR state definition 判断 open、closed 或 ambiguous。

Alex 确认她的理解正确。[会议事实：P2:L337-362]

### 4.3 Soojung 的评价

这套做法是 reasonable and useful：

- 它有真实文献数据；
- 有原论文的分析可以作为 reconstruction 对照；
- 以 NMR ensemble 定义候选 state，再看 MD 落在哪里，是当前条件下可接受的起点。

但它只回答了部分问题，尤其只报告“哪个 state 占优”远远不够。
[会议事实：P2:L364-386；P2:L471-480]

---

## 5. Soojung 要求补齐的科学分析

## 5.1 构象空间的可视化

需要在可视化中同时看到：

- NMR-defined state clusters；
- 每条 MD trajectory 从哪里开始；
- 随时间向哪里移动；
- 是否始终停在一个 basin；
- 是否进入另一个 state；
- 是否出现两个稳定态之间的中间帧。

建议形式是把 trajectory 点按时间连接，或采用能够等价表达 time progression 的图。
[会议事实：P2:L379-392；P1:L189-214]

**不是只画一张散点图。** 图必须保留时间方向，否则 trajectory 与 unordered
ensemble 的语义再次被混淆。

## 5.2 最低限度的数据与模拟信息

每次展示 MD 结果，至少需要说明：

- frame/time-step 数；
- 相邻保存帧的时间间隔；
- 完整时间范围或总模拟时间；
- 模拟是在 solvent 还是 vacuum；
- 使用什么 solvent/solution condition。

[会议事实：P2:L394-400]

**项目现状：** 当前本地审计已经确认官方 Zenodo 声明为 40 条、每条约 1 μs、
1 ns 保存间隔、显式水、170 mM NaCl；但还存在 force field、1021/1001 frame、
MDP/论文参数不一致等 provenance 问题。因此正式展示必须引用审计结果，不能继续使用
现场口头估计。[项目事实：
`autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725/outputs/HSP90_END_TO_END_REPORT.md`]

## 5.3 state transition 与 state persistence

每条 trajectory 都要回答：

```text
一直待在初始 state？
→ 有离开 basin 的 excursion，但没有完成转换？
→ 完成一次单向 transition 后停住？
→ 多次 open ↔ closed 往返？
```

一次 closed→open 后一直停在 open，不能称为 equilibrated。只有多次往返，才有资格
进一步问 open/closed population ratio 是否可信。[会议事实：P2:L401-418]

## 5.4 equilibration 与 convergence

需要从两个层次检查：

1. **within-trajectory**：同一条 trajectory 内是否有重复转换，某个量是否随观察
   长度增加趋于稳定；
2. **between-trajectories**：不同 trajectories 是否给出相近的 state occupancy 或
   其他 declared quantity。

Soojung 建议使用逐步增加观察窗口的方式，例如先取前几百 ns，再延长，查看某个量
何时稳定；她称之为 bootstrapping/truncation 式分析。[会议事实：P2:L420-434]

重要的是，**equilibration 不是整个 trajectory 的单一标签**。同一条轨迹可能已经
足够支持 residue RMSF，却不足以支持 open/closed population ratio。能信任什么取决
于 motion scale 和 estimand。[会议事实：P1:L69-103]

## 5.5 excursion、transition-like frame 和 MD-only state

即使没有完整 state transition，也可能存在有价值的 excursion：轨迹从稳定 basin
向能垒方向爬升，但没有完成跨越。这些结构未必出现在 NMR ensemble 中。
[会议事实：P1:L197-214]

需要进一步问：

- NMR 是否覆盖了 MD 访问的全部构象空间？
- MD 是否采到了 NMR 中没有的结构？
- NMR structures 可能主要表示稳定态，是否遗漏 transition frames？
- 如果 PCA basis 完全由 NMR 定义，MD 的 out-of-distribution 点是否会被错误压缩？

[会议事实：P2:L448-465]

## 5.6 raw NMR observables：明确放在后续

Soojung 提醒，deposited NMR models 不是 raw NMR data，也不是绝对 ground truth。
若能取得 chemical shifts、NOE、secondary-structure propensity、backbone torsion
等原始或更接近实验的 observable，未来可以通过相应 forward model 与 MD 比较。
但她明确说这不要求周五前完成。[会议事实：P1:L215-229]

---

## 6. 更大的科学问题：如何建立跨数据源 conformational landscape

Soojung 提出 Atlas 的第一个通用输出可以是 conformational landscape：

- 各数据源表示哪些 conformers；
- union 是什么；
- intersection/overlap 是什么；
- 每个来源独有的部分是什么。

[会议事实：P1:L7-23]

但简单拼接所有结构再做 PCA 有明显错误：MD trajectory 可能有成千上万 frames，
而 NMR 只有几十个 models。未经控制的 joint PCA 会主要学习 MD 的 frame density，
NMR 信号可能被忽略。[会议事实：P1:L14-34]

这不是一个已经解决的实现细节，而是可以单独形成研究问题：

> 如何在保留 representation 和 sampling semantics 的前提下，定义跨来源共享的
> state/landscape，并公平识别 shared、source-specific 和 unresolved regions？

Soojung 的判断是，各个 modality 内应该已经有成熟方法；我们需要先查文献，再研究
不同 modality 的 state definition 如何协调。系统性的跨模态 reconciliation 才可能
成为项目贡献。[会议事实：P1:L45-55]

---

## 7. Atlas 最终应输出什么

会议形成了两类输出，而不是单一分类标签。

### 输出 A：科学分析结果

对单个 system：

- conformational states / landscape；
- NMR–MD overlap 与 unique regions；
- state persistence、transition 或 excursion；
- 对声明估计量的 equilibration/convergence 证据；
- 哪些 ensemble quantities 可以信任；
- 哪些不能信任。

对大规模资源：

- 系统性地标注每个 system/trajectory 在什么 motion scale 上充分采样；
- 为模型训练或 benchmark 使用者提供可直接查询的分析结果；
- 发现不同 simulation protocol 对可信 quantities 的影响。

[会议事实：P1:L61-108]

### 输出 B：可复用分析 workflow / harness

- 这次分析如何完成；
- 用了哪些已建立的方法；
- 输入、参数和输出；
- 如果使用 LLM/Agent，实际 prompt 是什么；
- 能否把相同流程快速应用到另一个相似 dataset；
- 长期是否能让社区贡献新的 analysis harness 并经过评审。

[会议事实：P1:L230-237；P2:L207-227]

---

## 8. 人、确定性工具和 Agent 的边界

### 8.1 会议明确的初始原则

Soojung 的初始立场是：

- 只使用可靠文献中的 established methods；
- 由工具执行 PCA、clustering、equilibrium/convergence 等明确分析；
- 初期最终科学判断仍由人完成；
- 更复杂、全新的分析可咨询 reasoning model；
- 长期目标可以是减少人工决策，而不是第一版就取消人。

[会议事实：P1:L117-146；P1:L170-182]

### 8.2 本项目中 “Agent harness” 最稳妥的含义

**意图解析：** harness 不是一个会聊天的模型。它是包住模型与科学工具的执行环境，
至少管理：

```text
task packet
methods/tools
state
constraints and permissions
execution trace
failure recovery
human review
scoring/replay
```

本项目第一版可以完全由 deterministic runner 执行。LLM 的最早合理位置是：

- 从 paper/README 提取候选 SourceContract；
- 为已批准的 method recipe 填配置；
- 解释失败并准备 review packet；
- 在 policy 允许范围内提出下一工具调用。

LLM 不应自行发明 state definition、把单次 transition 解释为 equilibrium、或在
缺少原始 observable 时升级结论。

---

## 9. 明确的会议决定、建议与开放问题

### 9.1 已明确

| 项目 | 结论 | 来源 |
|---|---|---|
| 当前 HSP90 | 合理且有价值的起点，但分析不够完整 | P2:L364-380；P2:L471-480 |
| 周五科学结果 | 增加构象空间、时间进程、transition/excursion、equilibration/convergence | P2:L379-465；P1:L189-214 |
| MD metadata | 必须给 frame、间隔、总时长、solvent/condition | P2:L394-400 |
| 方法权威 | 初期使用可信已有文献方法 | P1:L117-123 |
| 初期判断 | human final decision | P1:L129-146 |
| raw NMR | future to-do，不要求周五 | P1:L215-229 |
| workflow 输出 | 要显示真实 prompt/harness 和可重跑性 | P1:L230-237 |
| 长期方向 | 大规模资源预分析 + 可复用/可贡献 harness | P2:L207-227；P2:L517-535 |

### 9.2 仍开放

1. 如何公平地联合 frame 数严重不平衡的数据源？
2. NMR ensemble 是 state anchor，还是覆盖完整构象空间的 ground truth？
3. 哪种方法最适合检测 MD-only / OOD / intermediate states？
4. 对每个 motion scale，什么标准才允许谈 equilibration？
5. 多个 modality 的 state definitions 如何 reconcile？
6. 初期到底自动化哪些决定，哪些必须 human review？
7. 第二个用于证明 harness 可复用的 dataset 是什么？

---

## 10. 会议行动清单

这里分成“会议直接要求”和“为了交付而必须补的实现动作”。优先级不是按代码难度，
而是按对周五科学故事的重要性。

| ID | 类型 | 动作 | 直接产物 | 验收标准 | 时间层级 | 来源 |
|---|---|---|---|---|---|---|
| A1 | 会议要求 | 核实 HSP90 全部 MD metadata | `HSP90_SOURCE_AND_RUN_CARD.json/md` | frame、interval、time range、solvent、salt、force field authority 与冲突均显式 | P0 | P2:L394-400 |
| A2 | 会议要求 | 构建 NMR state space 并显示 MD time progression | 2D landscape + 每条轨迹时间路径图 | NMR 与 MD 有不同符号；时间方向可见；不把 models 当时间 | P0 | P2:L379-392 |
| A3 | 会议要求 | 对每条 trajectory 做 state-vs-time 分类 | state timeline/table | 能区分 stay、transition、excursion、unresolved | P0 | P2:L401-418 |
| A4 | 会议要求 | 做 truncation / across-run convergence | convergence curves + negative result if not converged | 不足时明确阻止 population claim | P0 | P2:L420-434 |
| A5 | 会议要求 | 检测 NMR overlap、MD-only 和 OOD 区域 | coverage/novelty report | 不仅报告同一 lid；有 uncertainty 和 method sensitivity | P0 | P2:L448-465 |
| A6 | 会议要求 | 整理实际 workflow、prompt、harness | replay README + command + config | 相似 packet 可按明确步骤复跑；无 LLM 时明确写 deterministic | P0 | P1:L230-237 |
| A7 | 会议要求 | 补发/更新结果表 | meeting-ready table | 所有数字可追溯到结果文件 | P0 | P2:L282-287；P1:L246-248 |
| M1 | 科学前置 | 检索 joint landscape/state comparison 方法 | method evidence matrix | 每个选择有 primary source、assumption 和 failure mode | P0 | P1:L45-55；P1:L117-123 |
| M2 | 科学前置 | 冻结 HSP90 v1 estimands 与 decision rules | protocol JSON/MD | 先于新结果；阈值、state definition、统计单位明确 | P0 | 意图解析 |
| M3 | 科学前置 | 搜索 raw NMR↔MD forward-model 方法 | future method map | 明确只列 future，不挤占 P0 | P1 | P1:L215-229 |
| H1 | 复用前置 | 把 SystemPacket 补成可验证 schema | schema + example | 缺字段/错误类型 fail closed | P1 | 意图解析 |
| H2 | 复用前置 | 建立 method recipe/tool registry | recipe cards | 每个 recipe 声明 representation、input、output、citation、forbidden use | P1 | P1:L117-123 |
| H3 | 复用前置 | 固化 run trace 与 provenance | run bundle | input hash、code version、parameters、outputs、failures 可重放 | P1 | P1:L230-237 |
| H4 | 复用前置 | 准备 human-review packet | review template | 自动化不能决定时，明确呈现证据与待选项 | P1 | P1:L129-146 |
| H5 | 验证复用 | 选第二个相似 packet 做 replay | replay comparison report | 不手改核心分析逻辑；只换 packet/config | P1 | P1:L230-237 |
| F1 | 长期研究 | 研究公平的跨模态 landscape | methods study / benchmark | 显式解决 sample-size、weight、OOD 与 representation 差异 | P2 | P1:L7-36 |
| F2 | 长期研究 | raw NMR observable 与 MD forward prediction | separate pilot | 使用原始观测及误差，不以 PDB models 代替 | P2 | P1:L215-229 |
| F3 | 长期扩展 | 扩展 ATLAS/mdCATH 等大规模资源 | batch Atlas release | 统计单位、失败率与可信 quantity 可查询 | P2 | P1:L80-108 |
| F4 | 长期 Agent | 评估低人工 onboarding/analysis | held-out benchmark | 相对 deterministic baseline 提效且不降低 provenance/safety | P2 | P1:L150-182 |

---

## 11. 当前工作相对会议要求的真实状态

会议转写描述的是当时的四条 trajectory smoke test。共享 workspace 在会后已经存在两层
更完整的实现，因此不能把“会上没讲”误写成“现在完全没做”。

### 已经有

- 原始 Zenodo archive 和 40 条 trajectory 的 inventory；
- NMR/MD identity、residue mapping、time audit；
- representation-specific runner；
- 4 条 Mini-Atlas trajectory 的 RMSD-to-state、Rg、RMSF、autocorrelation、tICA；
- 40 条轨迹的 state-margin 分析、state-switch count 与相关时间摘要；
- provenance 矛盾和 forbidden claims；
- `SystemPacket → analyses → Atlas locations → ComparisonRecord → EvidenceBundle`。

### 仍未闭环

- presentation-ready joint landscape；
- 清楚的 per-trajectory time path；
- excursion 与 transition event 的正式定义和可视化；
- 观察窗口随长度增长的 convergence curve；
- MD-only/OOD state detection 的方法比较；
- solvent/condition 在 Mini-Atlas packet 中的结构化字段；
- 每项方法的 primary-literature justification；
- 证明可复用的第二 packet replay；
- 实际 LLM/Agent benchmark。

因此最准确的状态是：

```text
HSP90 raw-data ingestion: substantially complete
deterministic source-native analysis: partially complete
meeting-requested scientific visualization and convergence story: incomplete
reusable deterministic harness skeleton: exists
second-packet replay: not demonstrated
Agent incremental value: not tested
```

---

## 12. 对原 proposal 的影响

原 proposal 的主线仍然成立：把 heterogeneous conformational resources 组织成
source-traceable evidence framework，并区分 observation、population、kinetics、
mechanism 和 function。

会议把它变得更具体：

1. Atlas 不能只输出 claim boundary，还要输出实际 scientific characterization；
2. “common evidence space” 不能靠简单拼接结构实现；
3. state、transition、equilibration 都必须是 estimand- 和 scale-specific；
4. 每个 modality 先复用 established methods；
5. harness 的第一贡献是可复跑、可审查，不是 LLM 自治；
6. Agent 应建立在真实方法 recipe 和运行记录上，而不是替代它们。

这不是换题，而是把 proposal 从“证据治理框架”推进为：

> **能够产生科学分析结果、解释其可信范围，并将其过程复用到下一批数据的 Atlas
> workflow。**

---

## 13. 下一次需要向 Soojung 确认的高层问题

这些问题故意保持宏观，不陷入某个阈值或函数的工程细节。

1. **第一版的成功标准是什么？**  
   是 HSP90 上把 state/transition/convergence 讲清楚，还是必须再加一个独立
   protein system 才算完成第一阶段？

2. **NMR 在这个示例中的角色是什么？**  
   我们应把它称为 experimental state anchor，还是希望进一步取得 raw observables，
   使其成为可检验的实验约束？

3. **Atlas 的第一类统一输出是什么？**  
   更重视 shared conformational landscape，还是“每个 dataset 哪些 quantities
   已收敛、可以信任”的 reliability profile？

4. **周五合作讨论最需要得到什么反馈？**  
   是实验 modality 的 state definition、一个更好的 benchmark system，还是他们愿意
   提供的 raw data/ground truth？

5. **Agent/harness 第一阶段应证明什么价值？**  
   是换 dataset 后少写代码、少人工整理 metadata，还是自动提出并执行下一项分析？

---

## 14. 转写校正表

| 自动转写 | 本纪要采用 | 置信度 |
|---|---|---:|
| `mnr` / `animal` / `an mr` | NMR | 高 |
| `t car` / `teacup` / `take a` | tICA | 高 |
| `msn` | MSM | 高 |
| `jason` | JSON | 高 |
| `guitar` | GitHub | 高 |
| `outlaws` / `empty card` | ATLAS / mdCATH | 中高 |
| `tradition` | transition | 高 |
| `exclusion` | excursion | 高 |
| `baltimore equilibrium ensemble` | Boltzmann/equilibrium ensemble | 中 |
| `cupid` | 未确定的 X-ray dynamics/entropy 方法或实验名 | 低，保留待确认 |

---

## 15. 一句话行动结论

> 下一轮不应先扩建一个通用 Agent。应先用文献冻结 HSP90 v1 的状态空间、转变与收敛
> 分析，把科学结果补完整，再把这一条真实执行路径封装为可复跑、可审查、以后可由
> Agent 配置和扩展的 harness。

