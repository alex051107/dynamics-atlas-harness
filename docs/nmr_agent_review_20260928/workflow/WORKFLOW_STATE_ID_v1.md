# 识别替代构象状态的工作流 v1（源文件）

版本 v1，2026-09-28，草案，待用户与 Gina 审定后冻结。本文件是工作流的唯一源文件；第 5 节是给人的一页清单，第 6 节是给 Agent 的提示，两者由本文件第 2–4 节导出，改一处两边同改。修改规则见第 7 节。

出处写法："论文-片段号"，对应 `workflow/fragments/` 各文件的"片段 N"。例：K-Ras-2 = `DECISION_FRAGMENTS_KRAS2023_ZH.md` 片段 2；RfaH2025-3 = `DECISION_FRAGMENTS_RFAH_2012_2025_ZH.md` 第二部分片段 3。

## 1 这份工作流解决什么问题

给一个样品的沉积证据，判断这个蛋白在这个样品、这个条件下，是否存在一个与主态共存的替代构象状态；存在的话，是哪些残基、什么时标、像什么结构、有没有功能证据；证据不够时，说清楚缺什么。

首批入库的操作定义（待 Gina 确认）：蛋白不结合配体（APO），同一样品、同一条件下，同一残基出现两套可指认的信号（慢交换）。只能靠 CEST 或弛豫色散看到的低布居态，首批是否纳入由 Gina 决定；工作流照样处理它们，只在第 J8 步标注是否属于首批。

## 2 输入与输出

**输入：一个证据包。** 构建体与序列；配体、辅因子、核苷酸状态；样品条件（温度、pH、缓冲液、浓度、寡聚态）；指认化学位移表，可能不止一张，同一残基可能有多个值，每张表带它对应的样品与条件；常规弛豫（R1、R2、NOE），若有；弛豫色散或 CEST 曲线，若有；关联的 PDB 条目。每条记录有编号，结论必须引用编号。人走完整资料时另外看论文正文和补充材料；Agent 评测时不给。

**输出：一条状态条目。** 五层断言分开写，每层可以单独弃权：

1. **观察**：在哪个构建体、什么条件下，看到了什么信号特征（引用记录编号）。
2. **归属**：这些特征是同一样品的两个态，还是来自不同条件、不同链、不同样品或样品问题。
3. **状态**：涉及哪些残基；时标类别（慢，两套峰 / 中间，展宽 / 快，单峰平均）；布居与速率，仅在数据能定时给出。
4. **结构对应**：与哪个 PDB 条目或参照相符，逐区给出；或无对应。
5. **功能相关**：有无同条件下的独立证据；没有就标为假设或弃权。

最后给总判定：**有 / 无（限所测条件）/ 弃权**。附：未排除的竞争解释；最能消除歧义的下一项测量；是否属于首批入库定义。程序中断、工具出错与"证据不足"分开报告。

## 3 八个判断点

按顺序走，可以回头。每个判断点写下"看到了什么、判了什么、依据哪条记录"。

### J1 对象是否成立

**看什么**：构建体（全长还是结构域、有无标签）、序列、配体状态、寡聚态、物种。
**怎么判**：确认这是一个明确的对象。结论只适用于这个构建体：孤立结构域的结论不写成全长蛋白的结论（RfaH2025-1），结构来自一个物种、动力学来自另一个物种时要注明（AdK-3）。配体结合的样品不属于首批定义，照常分析，在 J8 标"不属于首批"。
**何时弃权**：配体状态或构建体无法确定。

### J2 证据有哪几类

**看什么**：有几张位移表，各对应什么样品和条件；指认覆盖多少残基，连续缺失的区段在哪；有没有常规弛豫、色散、CEST；关联几个 PDB 条目，是否多构象。
**怎么判**：列一张证据清单，写明每类证据能回答后面哪个判断点。缺指认只记为候选线索，不等于交换展宽：信号可能因重叠、灵敏度、寡聚或交换展宽消失（IL-2-1：酰胺谱大面积消失，作者改用甲基读数）。该出现的第二套峰没出现，要问是没有运动还是超出了方法窗口（AdK-1、AdK-2）。
**何时弃权**：不弃权，这一步只限制后面能回答什么。

### J3 有没有第二套信号

**看什么**：直接特征：同一残基在同一样品下有两个指认值；标明为第二态或次要态的位移表；CEST 曲线上的次级凹陷；色散曲线上的弥散。间接特征：连续缺指认、R2 偏高、谱线展宽。
**怎么判**：至少有一类直接特征，才记为"有候选"。只有间接特征时记为"线索"，写明它的竞争解释（重叠、寡聚、各向异性运动、样品问题），不升级。次要态峰弱且重叠时，归属本身就是一个需要证据的判断（RfaH2025-2）。单一的 CEST 次级凹陷支持一个次要态，不支持更多（K-Ras-2）。
**何时弃权**：只有间接特征。

### J4 是不是同一样品的两个态

**看什么**：两套信号各自对应的样品、条件、链、构建体；样品状态（纯度、降解、配体水解、存放时间）。
**怎么判**：两套记录来自同一样品、同一条件，且残基对应关系一致，才归为同一样品的两个态。不同温度、pH、配体、突变或构建体的两张表，是两个对象，不是两个态，拆开分别走 J1。同编号的两条链要区分是对称二聚体还是两个态。要排除样品本身造成的第二套信号：K-Ras 的作者专门检查了次要态会不会是 GTP 水解产物或 GDP 污染（K-Ras-5）；RfaH 的作者用点突变和酶切排除了人为因素（RfaH2012-3、RfaH2012-4）。
**何时弃权**：条件字段缺失、无法核对两套记录是否来自同一样品。容差（温度、pH 差多少以内算同一条件）待 Gina 确定。

### J5 时标与布居

**看什么**：两套峰是否都可见；峰强度；有无色散或 CEST 曲线。
**怎么判**：两套峰都可见即慢交换，布居可由峰强度粗估并注明误差来源。只有位移表时不给速率。有原始曲线时走拟合分支：先拟两态；只有出现两态解释不了的信号才加状态，并写明何时停止（RfaH2025-4）；用一类数据拟出的参数去预测另一类数据，预测失败说明模型不完整，联合重拟合不算预测（RfaH2025-3）；拟合优度相近的拓扑并列报告，不选一个（K-Ras-2）。
**何时弃权**：只有位移表时对速率弃权；拟合不收敛或参数不可辨时对相应参数弃权。

### J6 结构对应

**看什么**：关联的 PDB 条目；其他已沉积状态的位移；序列预测的随机卷曲位移。
**怎么判**：在两套信号共有的残基上逐区比较，至少用两类参照，同时看相关性和绝对差（K-Ras-3）。偏离参照的残基先查局部化学环境（如靠近配体）再解释为构象差异（K-Ras-4）。与某参照相似只说明相似，不等于同一个状态；把次要态对应到文献中的已知状态要有数据层面的核对，且标明这一步用了外部知识（K-Ras-7）。主态的结构证据不能直接用来约束次要态。
**何时弃权**：只有一类参照，或共有残基太少。

### J7 功能相关

**看什么**：同条件下的独立证据：结合、活性、突变或扰动实验、配体效应。
**怎么判**：有独立证据把状态与功能连起来才写。用选择性扰动（突变、离子、小分子）改变布居并观察功能变化，是最直接的证据（AdK-5、IL-2-5、IL-2-7）。把交换对应到某个功能步骤要有时标匹配（AdK-4）；时标不匹配的模拟不能作为证据（AdK-7）。作者本人只写 "may" 的，条目也只能写假设（K-Ras-8）。
**何时弃权**：默认弃权。

### J8 写条目

**怎么判**：按第 2 节五层分开写，每层引用记录编号。阴性结论写明条件范围："在所测条件和方法窗口内未检出"，不写"单一构象"。列出未排除的竞争解释和下一项测量。标明是否属于首批入库定义。功能开关在体内是否成立这类问题，没有体内证据就不写（RfaH2012-6）。

## 4 常见错误（每条来自一个真实案例）

- 把缺指认直接当交换展宽。
- 把两个条件下的两张表当成同一样品的两个态。
- 从"有两套峰"直接写"功能相关的替代态"。
- 只有位移表却给出速率或布居。
- 用一个参照相似就断定次要态的结构身份。
- 把工具出错或预算用尽写成"没有替代态"。

## 5 人用清单（一页）

| 判断点 | 看到了什么（记录编号） | 判定 | 弃权？原因 |
|---|---|---|---|
| J1 对象 | | | |
| J2 证据清单 | | | |
| J3 第二套信号 | 直接特征： 间接特征： | 有候选 / 线索 / 无 | |
| J4 同一样品？ | | 同一样品两态 / 拆成 N 个对象 | |
| J5 时标与布居 | | 慢 / 中 / 快；布居： | |
| J6 结构对应 | 参照 1： 参照 2： | | |
| J7 功能 | | | |
| J8 总判定 | 有 / 无（限条件） / 弃权 | 首批：是 / 否 | |
| 竞争解释与下一项测量 | | | |
| 卡在哪里（给工作流修订用） | | | |

## 6 Agent 提示

```
You identify alternative conformational states of a protein from deposited NMR evidence.

You receive one evidence package: construct and sequence, ligand state, sample conditions,
one or more assigned chemical-shift lists (each linked to a sample and condition),
relaxation data and dispersion/CEST profiles if present, and linked PDB entries.
Every record has an ID. Every statement you make must cite record IDs.

Work through eight judgment points in order; you may go back.
J1 Object: construct, ligand state, oligomer, species. Claims apply to this construct only.
   Ligand-bound samples are analysed but marked "outside first slice". Abstain if ligand
   state or construct cannot be determined.
J2 Evidence inventory: list what evidence exists and which later judgments it can support.
   Missing assignments are a lead, not proof of exchange broadening.
J3 Second signal set: direct features are two assigned values for the same residue in the
   same sample, a list marked as a second or minor state, CEST minor dips, or dispersion.
   Missing assignments, high R2 or broadening are indirect and never sufficient alone.
J4 Same sample? Two signal sets count as two states only if they come from the same sample
   and condition. Different temperature, pH, ligand, mutant or construct means separate
   objects. Check chains and sample problems (degradation, hydrolysis, contamination).
   Abstain if condition links are missing.
J5 Timescale and population: two visible peak sets mean slow exchange. With shift lists only,
   give no rates. With dispersion/CEST profiles, fit two states first, add states only for
   unexplained signal, test a fit by predicting a different data type, report tied
   topologies together.
J6 Structure: compare on the shared residue set, region by region, with at least two kinds
   of reference; similarity is not identity; the major state does not constrain the minor.
J7 Function: only with independent same-condition evidence; otherwise mark as hypothesis.
J8 Entry: write five separate layers (observation, attribution, state, structure, function),
   an overall verdict (yes / no within tested conditions / abstain), unresolved alternatives,
   the single most useful next measurement, and whether the case meets the first-slice
   definition (APO, same sample and condition, two assignable signal sets).

If you recognise the protein or remember a publication, do not use that memory as evidence.
Any external knowledge you use must be labelled as such. A tool error or running out of
budget is reported as such, never as "no alternative state".
```

## 7 修改规则

v1 在用户与 Gina 审定后冻结。之后只有被某个病例暴露的问题才能修改，每次修改在下表加一行：病例号、卡在哪个判断点、原文、新文、为什么这样改能让该病例通过而不伤其他已走病例。"读起来更合理"或"为了对上某篇论文的结论"不是修改理由。人用清单和 Agent 提示同时改。

| 版本 | 日期 | 病例 | 判断点 | 原文 | 新文 | 理由 |
|---|---|---|---|---|---|---|
| v1 | 2026-09-28 | — | — | — | — | 初稿，由五篇论文 37 条片段与 K-Ras 案例整理 |
