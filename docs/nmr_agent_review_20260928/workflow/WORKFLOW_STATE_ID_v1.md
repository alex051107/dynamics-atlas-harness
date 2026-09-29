# 识别替代构象状态的工作流 v1（源文件，第 2 稿）

2026-09-28。草案，未冻结。第 2 稿按第二轮外部审查修订了 J1、J3–J8、输入定义、人用清单、Agent 提示与修改规则（见第 7 节）。本文件是唯一源文件；第 5 节人用清单和第 6 节 Agent 提示由第 2–4 节导出，改一处两边同改。

出处写法："论文-片段号"，对应 `workflow/fragments/` 各文件的"片段 N"。例：K-Ras-2 = `DECISION_FRAGMENTS_KRAS2023_ZH.md` 片段 2；RfaH2025-3 = `DECISION_FRAGMENTS_RFAH_2012_2025_ZH.md` 第二部分片段 3。

## 1 这份工作流解决什么问题

给一个病例的沉积证据，判断这个构建体在所测样品和条件下，是否有证据支持一个与主态共存的替代构象状态；有的话，证据支持到哪一层（观察、归属、状态、结构、功能）；不够时，缺什么、下一步查什么。

**病例**是一个待判断的样品或构建体问题，不等于一个 BMRB 条目。一个病例的证据包可以包含多个相关条目。例：RfaH 2025 的主态与次态分别沉积为 BMRB 52718 与 52719，两个条目各有一套指认；按单个条目打包，Agent 只会拿到一半。条目之间的来源关系必须保留，不能凭蛋白名、条件相近或编号相同自动合并。

**首批入库的操作定义**待 Gina 确认：候选是 APO 蛋白、同一样品中可直接看到并指认的两套信号；只能由 CEST 或弛豫色散看到的低布居隐态是否纳入首批，由她决定。工作流对两类都照常处理，只在 J8 标注是否属于首批。

## 2 输入与输出

**输入：一个证据包。** 每项有编号，并标明性质：实测记录、作者解释、计算生成物。例：BMRB 条目页上的部分 HSQC 下载是由位移模拟的峰，属于计算生成物，不能当作采谱证明；"主态／次态"这类名称是作者解释。

包含的类别（有则读取，不要求全部有）：
- 构建体与序列；配体、辅因子、核苷酸状态；样品条件（温度、pH、缓冲液、浓度、寡聚态）。
- 指认化学位移表，可能多张，可能来自多个条目；每张带条目号、列表号、分子实体、样品与条件。
- 实测谱图或峰表、峰强度或体积及误差。
- 把两套信号联系起来的交换实验资料（如 zz-exchange、CEST），及其来源。
- 常规弛豫（R1、R2、NOE）；弛豫色散或 CEST 曲线。
- 关联的 PDB 条目。

人走完整资料时另外看论文正文和补充材料；Agent 盲化评测时只给证据包。

**输出：一条状态条目。** 五层断言分开写，每层可以单独弃权，每条引用记录编号：

1. **观察**：在哪个构建体、什么条件下，看到了什么。
2. **归属**：两套信号或交换信号属于同一构建体的两个构象，还是来自不同条件、链、样品或样品问题；未决时写"共存／归属未决"。
3. **状态**：涉及哪些残基；时标类别；强度比或布居、速率，仅在数据能定时给出。
4. **结构对应**：与哪个结构或参照相似、在哪些区域、到什么程度；或无对应。
5. **功能相关**：有无与该状态有明确联系的功能证据；没有就标假设或弃权。

总判定：**有 / 无（限所测条件与方法窗口）/ 未决**。每个未决判断附第 J8 步的四个回答。程序中断、工具出错、原始记录未取得，与"证据不足"分开报告，都不计为科学结论。

## 3 八个判断点

按顺序走，可以回头。每个判断点写下看到了什么、判了什么、依据哪条记录。遇到未决，立刻按 J8 的四个问题决定下一步动作，不必等到最后。

### J1 对象是否成立

**看什么**：构建体（全长还是结构域、有无标签）、序列、配体状态、寡聚态、物种。
**怎么判**：确认对象，结论只适用于这个构建体：孤立结构域的结论不写成全长蛋白的（RfaH2025-1）；结构与动力学来自不同物种时注明（AdK-3）。配体结合的样品照常分析，在 J8 标"不属于首批"。
**何时弃权**：构建体无法确定时，后面的归属受限。配体状态不明时，首批资格标"待定"，不弃权整个病例，已观察到的信号照常记录。

### J2 证据有哪几类

**看什么**：第 2 节列的每一类，有没有、来自哪个条目、是实测还是解释还是计算。
**怎么判**：列一张证据清单，写明每类能支撑后面哪个判断点。缺指认只记为候选线索：信号可能因重叠、灵敏度、寡聚或交换展宽消失（IL-2-1：酰胺谱大面积消失，作者改用甲基读数）。该出现的第二套峰没出现，要问是没有运动还是超出了方法窗口（AdK-1、AdK-2）。
**何时弃权**：不弃权，只限制后面能回答什么。

### J3 有没有支持额外状态或交换过程的候选证据

**看什么**：同一分子实体、对应残基、同一原子的两套观测值（可能分处两个条目）；交换敏感数据（CEST 次级凹陷、色散）；间接线索（连续缺指认、R2 偏高、展宽）。作者给的"第二态／次态"标签用来定位，是待核验的作者归属，不能算作本次独立识别的结果。
**怎么判**：分三条去向。

| 当前证据 | 可以写什么 | 下一步 |
|---|---|---|
| 可核对的两套对应观测 | 两套信号候选 | J4 核查共存与归属 |
| CEST、色散等交换敏感数据 | 交换过程或隐态候选 | J4 核对对象，再到 J5 做模型检查 |
| 缺指认、R2 异常等间接线索 | 候选线索，不足以确认状态 | 查证据包内有无补充证据；没有则限定结论 |

次要态峰弱且重叠时，归属本身需要证据（RfaH2025-2）。单一 CEST 次级凹陷支持一个次要态，不支持更多（K-Ras-2）。
**何时弃权**：只有间接线索且包内无补充证据。

### J4 两套信号能否归为同一构建体的两个构象

**看什么**：两套记录各自的条目、列表、实体、原子、残基对应；样品与条件；把它们联系起来的交换实验；样品状态（纯度、降解、配体水解、存放时间）。
**怎么判**：先确认两套信号属于可联合解释的样品观测，并核对实体、原子和残基对应。样品与条件一致只建立比较资格。是否支持同一构建体的替代构象，要结合交换联系（如 RfaH 作者用 zz-exchange 把次态峰与主态峰连起来）、跨残基的一致性、样品伪影检查一起判断：K-Ras 的作者检查了次要态会不会是 GTP 水解产物或 GDP 污染（K-Ras-5）；RfaH 的作者用点突变和酶切排除人为因素（RfaH2012-3、RfaH2012-4）。不同温度、pH、配体、突变或构建体的两张表是不同对象，拆开分别走 J1。同编号的两条链先区分对称二聚体与两个态。不要求每个病例做同一种交换实验，由证据组合决定能支持到哪一层。
**何时弃权**：证据不足时写"两套信号共存／归属未决"，不升级为两个构象态。

### J5 时标与布居

**看什么**：两套信号的强度或体积；色散、CEST 曲线。
**怎么判**：
- 只有位移表时不给速率。
- 交换归属成立后，两套可见信号对相应核与条件指向慢交换。只有一套可见信号不证明快交换，低布居的慢交换态可能看不见。
- 强度或体积先报比值；只有在响应可比、或展宽等差异已处理时，才换算成布居。
- 有原始曲线时：交换证据尚未建立，先检查无交换或平坦响应是否足以解释数据；已有交换证据，从最简单的适用交换模型开始。加状态之前，先查归属、误差、实验模型和优化收敛是否造成残差；只在排除这些后仍有未解释信号时才加，并写明何时停止（RfaH2025-4）。用一类数据拟出的参数预测另一类数据，预测失败先回查上述环节，排除后再判断是否缺少过程；联合重拟合不算预测（RfaH2025-3）。拟合优度相近的拓扑并列报告（K-Ras-2）。
**何时弃权**：不收敛或不可辨的参数单独弃权。

### J6 结构对应

**看什么**：关联的 PDB 条目；其他已沉积状态的位移；序列预测的随机卷曲位移。
**怎么判**：参照要覆盖当前真正需要区分的解释。有多个合理的竞争参照时逐一比较，在共有残基上逐区看相关性和绝对差（K-Ras-3）。只有一个合适参照时，可以报告有范围的相似性，但不能据此确认唯一的状态身份。偏离参照的残基先查局部化学环境再解释为构象差异（K-Ras-4）。把次要态对应到文献中的已知状态，要有数据层面的核对，并标明用了外部知识（K-Ras-7）。主态的结构证据不能未经合理联系直接转移到次要态。没有结构对应，不撤销已经成立的信号或状态证据。
**何时弃权**：共有残基太少，或没有合适参照。

### J7 功能相关

**看什么**：结合、活性、突变或扰动实验、配体效应。
**怎么判**：功能证据必须与目标构建体和状态有明确联系，并写明有意改变的变量及其余条件的可比性。扰动改变状态布居、同时改变功能，可以支持关联（AdK-5、IL-2-5、IL-2-7）；更强的因果断言还要处理扰动对功能的其他影响。把交换对应到某个功能步骤要有时标匹配（AdK-4）。时标不匹配的模拟不能支持相应的动力学时标或速率断言（AdK-7），它是否支持结构相容性另作判断。作者只写 "may" 的，条目也只写假设（K-Ras-8）。
**何时弃权**：默认弃权。

### J8 写条目，并为每个未决判断选下一步动作

**怎么判**：按第 2 节五层分开写。阴性写"在所测条件和方法窗口内未检出"，不写"单一构象"。功能开关在体内是否成立，没有体内证据就不写（RfaH2012-6）。标明是否属于首批定义。

每个未决判断回答四个问题：
1. 当前哪两个解释没有分开？
2. 已有资料里下一步能查什么或算什么（取得另一个关联条目、读补充峰表、核对样品关系、用已有曲线检验另一解释）？
3. 得到哪种结果会改变判断？
4. 没有可执行动作时，保留什么结论并停止？

## 4 常见错误（每条来自真实案例或审查）

- 把缺指认直接当交换展宽。
- 把样品条件字段一致当作两态成立的证据。
- 把作者的"次态"标签当成自己的识别结果。
- 把两个条件下的两张表当成同一样品的两个态。
- 只拿到一个条目，就判断一个两态病例。
- 从"有两套信号"直接写"功能相关的替代态"。
- 只有位移表却给出速率或布居；把强度比直接当布居。
- 预测失败就加隐态。
- 用一个参照相似就断定次要态的结构身份。
- 把工具出错、原始记录未取得或预算用尽写成"没有替代态"。

## 5 人用清单（一页）

走读前写明：病例号、证据包版本、走读人、是否熟悉该论文（熟悉病例的走读是开发走读，不是不知道答案的参照）。

| 判断点 | 看到了什么（记录编号、性质） | 判定 | 未决时：下一步动作 |
|---|---|---|---|
| J1 对象 | | 首批资格：是 / 否 / 待定 | |
| J2 证据清单 | | | |
| J3 候选证据 | 两套观测： 交换数据： 间接线索： | 两套信号候选 / 交换候选 / 线索 / 无 | |
| J4 归属 | 连接证据： 伪影检查： | 两个构象 / 共存归属未决 / 拆成 N 个对象 | |
| J5 时标与布居 | | 时标： 强度比或布居： | |
| J6 结构对应 | 参照： | | |
| J7 功能 | | | |
| J8 总判定 | 有 / 无（限条件） / 未决 | 首批：是 / 否 / 待定 | |
| 清单之外实际用到的判断 | | | |

最后一行给工作流修订用：写下清单没写、但你实际用了的知识或判断。

## 6 Agent 提示

```
You assess whether deposited NMR evidence supports an alternative conformational state
of a protein construct, and you write a database candidate entry.

A case is one sample/construct question. Its evidence package may contain several
database entries. Every item has an ID and a label: measured, author interpretation, or
computed (e.g. peaks simulated from shifts). Keep entries separate; never merge records
because protein names, conditions or residue numbers match. Cite item IDs for every
statement.

Work through eight judgment points in order; you may go back. Whenever a judgment stays
unresolved, answer the four J8 questions and act on the next available check before
moving on.

J1 Object: construct, ligand state, oligomer, species. Claims apply to this construct only.
   Ligand-bound samples are analysed and marked "outside first slice". If the ligand state
   is unknown, mark first-slice eligibility "pending" and keep recording what is observed.
J2 Evidence inventory: list each evidence class, its source entry and its label, and which
   later judgments it can support. Missing assignments are a lead, not proof of broadening.
J3 Candidate evidence for an extra state or exchange process. Route:
   (a) two observations for the same entity, residue and atom -> two-signal candidate;
   (b) CEST or dispersion data -> exchange or hidden-state candidate;
   (c) missing assignments, high R2, broadening -> lead only.
   An author label such as "minor state" locates data; it is not your finding.
J4 Attribution: first confirm the two signal sets belong to observations that can be
   interpreted together, and check entity, atom and residue correspondence. Matching sample
   conditions only make them comparable. Supporting two conformations of one construct also
   needs linking exchange evidence, consistency across residues, and checks for sample
   artefacts. Different temperature, pH, ligand, mutant or construct means separate objects.
   If support is insufficient, write "two signal sets coexist; attribution unresolved".
J5 Timescale and population: with shift lists only, give no rates. Two visible signal sets
   indicate slow exchange only once the exchange attribution is supported; one visible set
   does not prove fast exchange. Report intensity ratios; convert to populations only when
   responses are comparable. With profiles: if exchange is not yet established, first test
   whether no exchange explains the data; otherwise start from the simplest applicable
   model. Before adding a state or reacting to a failed cross-prediction, check assignment,
   errors, the experiment model and convergence. Report tied topologies together.
J6 Structure: references must cover the explanations you need to separate. Compare competing
   references on the shared residue set, region by region. With one suitable reference you
   may report bounded similarity, never unique identity. Do not transfer major-state
   structural evidence to the minor state without a stated justification. Lack of a
   structural match does not cancel established signal evidence.
J7 Function: only with evidence explicitly linked to this construct and state; state which
   variable was deliberately changed. Co-variation of population and function supports an
   association; causal claims need more. Mismatched-timescale simulations do not support
   timescale or rate claims.
J8 Entry: five separate layers (observation, attribution, state, structure, function), an
   overall verdict (yes / no within tested conditions and method window / unresolved),
   first-slice eligibility, and for every unresolved judgment: which two explanations remain,
   what can be checked or computed next from available material, which outcome would change
   the judgment, and what to keep if nothing can be done.

If you recognise the protein or remember a publication, do not use that memory as evidence;
label any external knowledge. Report tool errors, missing raw records or exhausted budget as
such, never as "no alternative state".
```

## 7 修改规则与修订记录

每批评测期间冻结。可以触发修订的只有三类：具体病例暴露的问题、可复现的反例、有来源的方法错误。修订的目的是纠正错误判断或不当弃权，不是让病例命中论文标签。每次修订记入下表，修订后作为新版本报告；人用清单和 Agent 提示同时改。

| 版本 | 日期 | 触发 | 判断点 | 改了什么 | 理由 |
|---|---|---|---|---|---|
| v1 第 1 稿 | 2026-09-28 | 初稿 | — | — | 由五篇论文 37 条片段与 K-Ras 案例整理 |
| v1 第 2 稿 | 2026-09-28 | 病例：RfaH 2025 主次态分处 BMRB 52718/52719 | 输入定义、J3、J4 | 病例可含多个条目；输入加入实测峰表、连接两套信号的交换实验、证据性质标签；J3 分三条去向，作者标签不算发现；J4 条件一致只建立比较资格 | 按单条目打包只能拿到一半证据；相同条件字段不能建立交换关系 |
| v1 第 2 稿 | 2026-09-28 | 方法错误（外部审查） | J1、J5、J6、J7、J8 | J1 配体不明只把首批资格标待定；J5 先检查无交换解释、一套可见峰不证明快交换、强度比不直接当布居、预测失败先回查；J6 删去"必须两类参照"；J7 允许有明确变量的扰动实验，模拟只限制时标断言；J8 每个未决判断选下一步动作 | 原文会阻断正常分析、提前加隐态，或把一种方法写成普遍门槛 |
