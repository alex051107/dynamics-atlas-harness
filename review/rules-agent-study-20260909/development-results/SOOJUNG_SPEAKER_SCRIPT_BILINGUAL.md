# 讲稿（中英对照）：和 Soojung 讨论整套系统怎么搭

2026-09-10 · 对应 `SOOJUNG_DISCUSSION_20260910_EN.pptx` · 每页三块：**念的英文**、**中文对照**、**扫盲与技术要点**（给自己看，不念）。末尾有追问预案。

念的时候只看英文块。技术要点块是每一步背后的思想和逻辑顺序，被追问时用。

---

## 1 · 标题页

**EN**
Last time you knew I was building a Rules Table prototype. Today I want to discuss how the whole system should be built. I'll show the original idea, the workflow a new system actually goes through, what happened when three real systems went through it, what each layer of the table measured, and then three design options for the table itself. One headline first: putting rules into the prompt did not help. The errors we made were at data entry and at the numbers going out. The only layer that met its criterion was framing the question explicitly.

**中文**
上次你知道的是我在做一个 rules table 的原型。今天我想讨论的是整套系统应该怎么搭。我会讲原始设想、一个新体系实际走过的流程、三个真实体系走完以后发生了什么、表的每一层各测到了什么，最后是表本身的三种设计方案。先说结论：把规则贴进提示没有帮助。我们犯的错在数据进来和数字出去两头。唯一达到预设标准的层是把问题明确拆开。

**要点**
- 会议目标三件事：workflow 合不合理、三个体系对不对、表做成什么形式。
- 不要把"负结果"说成失败。它是把投入从提示文字转到代码和框题的依据。

---

## 2 · 原始设想与表是什么

**EN**
This was the idea from July. A question and a data package come in. The Agent consults a table of rules distilled from methods papers. The rules tell it which operations to run, which extra analyses to add, and where it must abstain. The table has 33 rules from 11 papers, three per paper. Each rule stores what the paper actually showed, what our project must check before using that kind of data, the items the check needs, and where to stop if the check cannot be done. Bottom right is one rule verbatim, from Shevchuk's Bayesian SAXS paper: if the candidate support omits a state, refinement can express uncertainty within the wrong support but cannot create the missing state.

**中文**
这是七月的想法。一道题和一个数据包进来，Agent 查一张从方法论文里提炼出来的规则表。规则告诉它该跑哪些操作、该补哪些分析、什么时候必须弃权。表里 33 条规则，来自 11 篇论文，每篇三条。每条规则存四样东西：论文实际证明了什么、我们用这类数据前必须查什么、这项检查需要哪些条目、查不了时在哪里停。右下角是一条规则原文，来自 Shevchuk 的贝叶斯 SAXS 论文：候选集合缺了某个状态，精修只能在错误的集合内表达不确定性，造不出缺失的状态。

**要点**
- 扫盲：SAXS 是小角 X 射线散射，给的是整体形状的平均信号。"候选集合"指拿去拟合的一组构象；贝叶斯精修只调这些构象的权重。
- 11 篇论文大多是 smFRET、SAXS、cryo-EM、DEER 的方法学论文，加两篇讲多源整合和系综预测。这个覆盖范围后面会成为问题（第 13 页：纯 MD 题取到零张卡）。
- 8 月 17 日外部审查的意见：拆成 papers / rules / index 三张表，当可审阅的账本，不当引擎。

---

## 3 · 新体系进来后的 workflow

**EN**
This is the workflow as it exists now, left to right. Intake: download the authors' deposited data and write a source card. Package: derived tables, field definitions, physical checks, then freeze with hashes. Frame: a person decides which difference the question must distinguish and writes the rubric. Run: the Agent analyses in a sealed container. Check: automatic checks on the submission. Report: every number linked to source, claim ceiling in words. The row underneath shows where the table acts: admission rules at step 2, framing rules at step 3, method cards at step 4, conclusion rules at step 5. Version one used the table only at step 4, as text pasted into the prompt. The three systems on the next slides went through that version.

**中文**
这是现在的流程，从左到右。接入：下载作者沉积的数据，写来源卡。建包：派生表、字段定义、物理检查，然后带哈希冻结。框题：由人决定这道题要区分哪种差异，写评分依据。运行：Agent 在密封容器里分析。检查：对提交结果做自动检查。报告：每个数字链接到来源，结论上限用文字写明。下面那行标的是表在哪一步起作用：准入规则在第 2 步，框题规则在第 3 步，方法卡在第 4 步，结论规则在第 5 步。第一版只在第 4 步用表，把规则当文字贴进提示。接下来三个体系走的就是那一版。

**要点**
- 扫盲："冻结"是在第一次调用模型前把题目、评分依据、代码、运行顺序记哈希，之后不许改；改了就作废。目的是防止事后调参数让结果好看。
- 人在第 1、3、6 步。第 3 步是唯一不能委托的：竞争解释由人定。
- 这一页是她判断 workflow 合不合理的依据，讲完可以停一下问她"到这里有没有问题"。

---

## 4 · Agent 一次运行做什么

**EN**
One run is one fresh container. No network, data read-only, five tools, and a hard submit call: ordinary text after submission never overwrites the answer. The model is gpt-5.6-luna through OpenRouter at medium reasoning. A typical run is twelve to twenty tool calls, about a minute, under two cents. It genuinely computes: it matched all ninety SAXS points in the nanodisc case and reproduced the four ADK endpoint changes to four decimals. So the cost of an experiment is scoring time, not money. Why the Agent stays in the design: goal four asks whether an agent can lower curation cost without adding unsafe claims. It is the last of four goals and allowed to fail on its own. The question is not "can it analyse", it can. The question is what information given to it produces a measurable gain.

**中文**
一次运行是一个新容器。没有网络，数据只读，五个工具，加一个硬性的提交调用：提交之后的普通文字不会覆盖答案。模型是 OpenRouter 上的 gpt-5.6-luna，中等推理强度。典型一次运行十二到二十次工具调用，一分钟左右，不到两美分。它是真的在算：纳米盘案例里它匹配了全部九十个 SAXS 数据点，ADK 的四个首末变化算到小数点后四位。所以实验的成本是评分的人工时间，不是钱。为什么 Agent 线保留：第四个目标问的是 Agent 能不能在不增加不安全结论的前提下降低整理成本。它排最后，允许单独失败。问题不是"它能不能分析"，它能。问题是给它什么信息能产生可测量的增益。

**要点**
- 扫盲：容器就是一个隔离的运行环境，模型只能看到我们挂进去的目录。三个目录分开挂：公开数据、隐藏评分依据、规则文件；对照组的目录里没有规则文件，有测试断言。
- 9 月 9 日开发运行暴露过一个交付问题：运行器把模型的确认文字当成答案覆盖了初稿。硬性提交调用就是那次的修正。

---

## 5 · HSP90：论文、我们、差距、首轮

**EN**
Left column is the paper. Henot and colleagues combine NMR with forty one-microsecond MD trajectories, twenty from the open crystal structure and twenty from a closed model, to argue that the closed state of the HSP90 N-terminal domain is transiently populated. They classify the twenty closed-start runs as seven near-closed, about nine toward open, four neither, using native NOE violations and clustering. They report millisecond exchange from CPMG and do not claim populations from MD. Middle column is what we computed on the same forty trajectories: one property, whether a trajectory shows a sustained open direction and whether it ever reverses. Ten of twenty, decomposed as five from the start plus five later; reversal candidates five, four, one at three run lengths; zero reversals for open-start. Right column: same data, different question, so our ten need not match their nine. Bottom: this is where the table acted in version one, as prompt text. Three of four answers got the counts right. The two rule answers also imported conditions that belong to single-molecule FRET: RMP restraints, prior ensemble, fit objective. Those came from two smFRET rules that the selector matched by method family.

**中文**
左列是论文。Henot 等人把核磁和四十条一微秒的 MD 轨迹结合起来，二十条从开态晶体结构出发，二十条从闭态模型出发，论证 HSP90 N 端结构域的闭态是瞬时占据的。他们用原生 NOE 违例和聚类把二十条闭合起始的轨迹分成近闭 7 条、趋开约 9 条、皆非 4 条。他们用 CPMG 报告毫秒级交换，不从 MD 里估占比。中列是我们在同一批四十条轨迹上算的：只挑一个性质，一条轨迹是否出现持续的开放方向，之后有没有反向。二十条里十条，拆成一开始就是的 5 条加后来才是的 5 条；反向候选在三种片段长度下是 5、4、1；开放起始零反向。右列：同一数据，不同问题，所以我们的 10 不必等于他们的 9。下面：这是第一版里表起作用的地方，作为提示文字。四份答复三份计数正确。两份规则组答复还带进了属于单分子 FRET 的条件：RMP 约束、先验系综、拟合目标。它们来自选择器按方法族匹配到的两条 smFRET 规则。

**要点**
- 扫盲：NOE 是核磁里一种观测，限制特定原子对的接近程度；"违例"是模拟里超出 NOE 上限的量，越接近零越符合那个状态的参照。CPMG 是核磁弛豫实验，测毫秒级的交换。
- "开放方向"的定义：两个差值读数的符号在连续 5 个点上保持开放方向。它丢掉了绝对吻合度，所以只能说方向，不能说到达。这是第 6 页的铺垫。
- 5/4/1 随阈值下降的原因：阈值同时改变哪些片段够长和拿哪一段当参照。ES15 从 115 ns 起连续 906 个点开放，在 50 点阈值下第一个合格段就是开放，就不再算"离开"。
- 规则泄漏的来源：C001-RULE-003（Hellenkamp smFRET 校准：inter-lab variation、R0）和 C003-RULE-002（Dimura FRET 辅助建模：RMP restraint、prior ensemble）。选择器把一条通用的"MD 不确定性"检查映射到了它们。

---

## 6 · HSP90：真正的科学结果

**EN**
The first round's "open direction" is the sign of a difference and says nothing about reaching the open state. So we compared every trajectory with the authors' deposited NOE violation series for both references. At one ångström tolerance, nine of the ten are still far from both references, one is partial, none is consistent with the open reference. The open-start controls are eighteen of twenty consistent, which is what validates the tolerance. This matches the paper's own phrase that the trajectories almost satisfy the open NOEs. Leaving the closed state and arriving at the open state are two different questions. What the system-level matching shows: the Agent reproduced the direction counts, but nothing in the rules made it ask the arrival question. That question was added by a person going back to the authors' raw observable. This is what the framing layer is for.

**中文**
首轮说的"开放方向"是差值的符号，说明不了有没有到达开态。所以我们把每条轨迹和作者沉积的两套 NOE 违例序列逐条对照。在 1 Å 容差下，十条里九条仍然同时远离两套参照，一条部分一致，没有一条与开态参照一致。开放起始的对照组二十条里十八条一致，这是容差成立的依据。这和论文自己的措辞一致，他们说这些轨迹"几乎满足"开态 NOE。离开闭态和到达开态是两个问题。系统层面的匹配说明了什么：Agent 复现了方向计数，但规则里没有任何东西让它去问到达的问题。那个问题是人回到作者的原始观测量之后加上的。这就是框题层的作用。

**要点**
- 容差预注册了 0.5、1、2 Å。0.5 Å 下对照只有 7/20 符合，太严；2 Å 下闭合组有 3 条变成一致。三档都报。
- 数据列的核对：作者沉积文件第 2 列是原生违例，第 3 列是伪距离；旧方向读数用的是第 3 列，Codex 分类前核出来的。这是"核对列含义比加一条提醒更直接改变分析"的例子。
- 为什么不能说占比或速率：40 条各 1 µs，论文自己说不具遍历性；开放起始的没回来过，闭合起始的离开后也没回来；CPMG 的交换在毫秒量级。

---

## 7 · DHFR

**EN**
The paper: trimethoprim loses potency against the L28R mutant of DHFR, and the analog 4′-DTMP recovers it. Their Table 1 inhibition constants: wild type 4.2 versus 5.1 nanomolar, L28R 65 versus 34. Their MD explanation is that 4′-DTMP sits closer to atoms of the M20 loop and arginine 28. We chose one property we could compute from the deposited trajectories: the specified protein-ligand atom distances, one trajectory per condition, 990 frames. The first result was wrong. The frozen table used wrapped coordinates, ligand copies in neighbouring periodic images gave distances of sixty to ninety ångström, and both Agent answers used them; one called the tail conformational switching. After correcting with the nearest ligand image and cross-checking with VMD to ten to the minus five ångström, the M20 nitrogen to ligand O3P distance goes from 8.7 to 4.6 in wild type and 10.4 to 4.8 in L28R when TMP is replaced by 4′-DTMP. Direction matches the paper's Figure 4 for all six specified pairs. The gap: the paper frames hydrogen bonds; we have mean distances, one trajectory each, no angles. What the matching shows: no rule text could have caught the input. The check has to sit at step 2, in code, before freezing. This was a curator-side defect, and it is the strongest argument in the deck for the admission layer.

**中文**
论文：甲氧苄啶对 DHFR 的 L28R 突变体失去效力，类似物 4′-DTMP 恢复了效力。他们表 1 的抑制常数：野生型 4.2 对 5.1 纳摩尔，L28R 是 65 对 34。他们用 MD 的解释是 4′-DTMP 更靠近 M20 环和精氨酸 28 的原子。我们挑了一个能从沉积轨迹算出来的性质：指定的蛋白配体原子距离，每个条件一条轨迹，990 帧。第一次结果是错的。冻结的表用了包装坐标，相邻周期镜像里的配体副本给出 60 到 90 Å 的距离，两份 Agent 答复都用了这些数，一份还把长尾叫构象切换。用最近的配体镜像修正、并用 VMD 交叉核对到十的负五次方 Å 之后，M20 的氮到配体 O3P 的距离在野生型从 8.7 缩到 4.6，L28R 从 10.4 缩到 4.8，都是 TMP 换成 4′-DTMP。六对指定原子的方向都和论文图 4 一致。差距：论文讲的是氢键，我们只有平均距离，每个条件一条轨迹，没有角度。匹配说明了什么：任何规则文字都抓不住这个输入。检查必须放在第 2 步、用代码、在冻结之前。这是整理者一侧的缺陷，也是整份 deck 里支持准入层的最强论据。

**要点**
- 扫盲：模拟盒子在空间里无限重复（周期性边界）。量蛋白和配体的距离时，如果配体被"包装"到盒子另一侧，直接量会得到假的大距离；正确做法是取最近的那个副本（最小映像）。这里只对跨分子的蛋白配体距离这样做。
- O3P 是原子名，不代表 TMP 含磷酸基团。
- 论文的 Ki 来自参考文献 25，不是本文测的。L28R 中 4′-DTMP 的 Ki 约是 TMP 的一半（65/34.3 = 1.9 倍）。
- 距离变短不等于氢键（还要角度），也不等于抑制机制；一条轨迹估不出轨迹间波动。
- 原两份答复保留不改、不算科学成绩；修正后的数字是开发者计算。

---

## 8 · ADK

**EN**
The paper: photorelease of ATP, time-resolved X-ray solution scattering, a transient of about 4.3 milliseconds, interpreted with MD-derived candidate structures. The deposited MD: two trajectories, open-start 450 nanoseconds and closed-start 335, and no ATP or AMP in the coordinates. We chose the one property we could actually compute: mean C-alpha distances between LID or NMP and CORE, first versus last ten percent of frames. All four changes are positive and the distributions overlap. The gap: no ligand, no scattering recomputation, no millisecond process, so this does not test the paper's mechanism. The system-level lesson is about my own rule. After DHFR I wrote an admission rule: any distance above half the box length fails. Open ADK spans 56 ångström along one axis in a 98 to 100 ångström box, so C-alpha distances of 62 and 70 ångström are real and GROMACS reproduces them. The rule was replaced by a physical criterion: whole reconstructed molecule, adjacent C-alpha within 4.5, GROMACS agreement within 0.01. Framing also helped here: the split version of the ADK question scored five of five.

**中文**
论文：光释放 ATP，时间分辨 X 射线溶液散射，一个约 4.3 毫秒的瞬态，用 MD 产生的候选结构来解释。沉积的 MD：两条轨迹，开态起始 450 纳秒，闭态起始 335 纳秒，坐标里没有 ATP 和 AMP。我们挑了唯一能算的性质：LID 或 NMP 到 CORE 的平均 Cα 距离，首末各 10% 的帧。四个变化都是正的，分布重叠。差距：没有配体，没有重算散射，没有毫秒过程，所以它检验不了论文的机制。系统层面的教训是关于我自己的规则。DHFR 之后我写了一条准入规则：任何距离超过半盒长就判失败。开态 ADK 沿一个轴延展 56 Å，盒子 98 到 100 Å，所以 62 和 70 Å 的 Cα 距离是真的，GROMACS 也复现了。这条规则换成了物理判据：补整后的完整分子、相邻 Cα 不超过 4.5 Å、GROMACS 核对差不超过 0.01 Å。框题在这里也有帮助：拆题版的 ADK 问题得了五分之五。

**要点**
- 扫盲：ADK 是腺苷酸激酶，LID 和 NMP 两个结构域相对 CORE 开合。时间分辨散射是用一束 X 射线在毫秒尺度上看整体形状的变化。
- 为什么半盒长规则错：最小映像距离的上限是 √3/2 倍盒长，分子内距离在补整的完整分子上量，不能逐对折回。分子延展超过半盒长时逐对折回会把真距离折短。
- 结构域定义是项目自定义（CORE 1–29/68–115/168–214，NMP 30–67，LID 118–160），和作者正文与 SI 的边界有差别，所以不声称复现作者的结构域 RMSD。
- ADK 的独特价值：它是规则表 11 篇来源和选择器都没见过的体系，是唯一的泛化信号来源，也是 Soojung 8/24 点名的。

---

## 9 · 回溯审计

**EN**
Before testing the four layers we audited every historical answer: thirteen observations in eight answers, seven same-cause groups, correlated rather than thirteen independent cases. Grouped by where each lives: input representation, numbers read from the wrong column or threshold, the sign of a difference read as arrival, and imported conditions. Reminder text prevents none of them. Code before freezing or after submission could plausibly prevent most; two need the question asked better. That was a candidate attribution. The next slides test it rather than trust it.

**中文**
测四层之前，我们审计了每一份历史答复：8 份答复里 13 处观察，7 个同因组，是相关的观察，不是 13 个独立案例。按错误住在哪一步分组：输入表示、从错误的列或阈值读数、差值符号被读成到达、带入的不适用条件。提醒文字一处都防不住。冻结前或提交后的代码看起来能防大多数；两处需要把问题问得更好。这只是候选归因。接下来几页是去测它，不是信它。

**要点**
- 3 处在重放中被代码实际检出，都属于 DHFR 的输入检查和答案保存机制；提交后的数字检查一处没检出。
- 不要把 13 说成 13 个错误。

---

## 10 · 四层

**EN**
This is the current design, and it is a direct answer to the original question of how the Agent should use the table. Framing: six rules become sub-questions and the rubric, never shown to the Agent. Admission: ten rules become code before freezing, reaching the Agent only as a card of results. Method cards: eleven rules become short cards retrieved by method family, the only rule text the Agent reads. Conclusion: six rules become an automatic check after submission with one feedback message. Each layer changes exactly one thing about what the Agent receives, so each can be tested on its own.

**中文**
这是现在的设计，也是对"Agent 应该怎么用这张表"这个原始问题的直接回答。框题：6 条规则变成子问题和评分依据，不给 Agent 看。准入：10 条变成冻结前的代码，Agent 只收到一张结果卡。方法卡：11 条变成按方法族检索的短卡，是 Agent 唯一读到的规则文字。结论：6 条变成提交后的自动检查，加一次反馈。每一层只改变 Agent 收到的一样东西，所以每层可以单独测。

**要点**
- 分层依据是表里的 rule_class 字段，6/10/11/6 的分配在附录 A2，可以逐条争论。
- 顺序来自那篇 ensemble 博文：先确定要区分哪种差异，再确认它在测量和处理后还留在数据里，然后才选方法。T4L 论文补了一句：采样进入某个区域不等于那是实验确认的状态。

---

## 11 · 每层测了什么、为什么

**EN**
Here is the reasoning behind the three questions we measured, with the criterion written before running. Framing: from HSP90 we knew the Agent answered the direction question but never the arrival question; if the layer helps, splitting the question raises supported coverage without adding overclaims. Admission: from DHFR we knew a bad table passed; the checker was tested on six planted defects and three clean packages, and the Agent was given or not given the card on the defective table; if the layer helps, it downgrades its conclusions when it has the card. Method cards: from HSP90 we knew full rules imported conditions; if the layer helps, scoped cards keep accuracy and stop the imports, judged against a seven-line protocol and the full rules. Conclusion: from the threshold mix-up and the nanodisc bound array we knew numbers went out wrong; if the layer helps, one automated pass reduces core errors without more omissions. Same model, four runs per condition, frozen, de-labelled scoring, medians of four.

**中文**
这是我们测的三个问题背后的推理，标准都在运行前写好。框题：从 HSP90 我们知道 Agent 答了方向问题但从没问到达问题；如果这层有用，拆题后有支持的覆盖会上升、过强结论不增加。准入：从 DHFR 我们知道坏表通过了；检查器在六种植入缺陷和三个干净包上测，Agent 在坏表上分别拿到和拿不到卡；如果这层有用，拿到卡时它会降级结论。方法卡：从 HSP90 我们知道完整规则带入了不适用条件；如果这层有用，按族检索的短卡保住准确率、停止带入，对照的是七行协议和完整规则。结论：从阈值混用和纳米盘的上限数组我们知道数字出去时是错的；如果这层有用，一次自动检查会减少核心错误、不增加遗漏。同一模型，每组四次，冻结，去标签评分，四次的中位数。

**要点**
- 评分：五个冻结的核心单元，各记对、错、缺；另记核心错误数、过强结论数、遗漏数、缺陷识别、下一步价值、成本。
- 评分人是建包的同一个代理，标签遮住，只有一位评分者。这是本轮最大的方法限制，主动说。
- 每组四次是为投入决定，不是为统计显著性。

---

## 12 · 结果

**EN**
Four rows. Framing: coverage went from 2 to 2.5 of 3 on HSP90 and 2 to 3 of 3 on ADK, no new overclaims; keep. One caveat: HSP90's total errors across four runs went from 1 to 2, so the gain is completeness, not uniformly accuracy. Admission: the checker caught all six planted defects, but the Agent detected the DHFR defect zero of four times with the card and zero of four without. Method cards: on HSP90 the plain protocol scored 4.5 of 5, full rules 2, cards 2.5; on the nanodisc question 4.5, 5, 4.5. Cards failed non-inferiority. The exception I want on record: full rules were best on the nanodisc question, all four answers covered all five units. Feedback: only ADK improved, and that difference already existed in the initial drafts; no revision reduced its own error count; three lost content.

**中文**
四行。框题：覆盖在 HSP90 从 3 分之 2 到 2.5，ADK 从 2 到 3，没有新增过强结论；保留。一个但书：HSP90 四次运行的错误总数从 1 到 2，所以收益是完整性，不是一律更准。准入：检查器抓到全部六种植入缺陷，但 Agent 拿卡时发现 DHFR 缺陷的次数是 0/4，不拿也是 0/4。方法卡：HSP90 上七行协议 5 分之 4.5，完整规则 2，卡 2.5；纳米盘题上 4.5、5、4.5。卡没有达到非劣标准。我想记在案的例外：纳米盘题上完整规则最好，四份答复全部覆盖五个单元。反馈：只有 ADK 改善，而且那个差异在初稿里就有；没有一次修订减少了自己的错误数；三份丢了内容。

**要点**
- 被问"规则没用？"的答法：提示形式没有得到支持；库仍是检查和卡的原料；Q05 是完整文本帮了忙的一个案例；不能说的是稳定增量。

---

## 13 · 为什么失败

**EN**
Three mechanisms, and each points at a specific repair. The card was available but never opened: all four card runs listed the file, none read it. A file is not a channel. Retrieval by method family gave HSP90 one card, a BME reweighting card, for a task that compares deposited violations and fits nothing; family membership is not operation applicability; and DHFR and ADK retrieved zero cards, because the eleven papers do not cover pure-MD questions. The conclusion checker asks whether a number appears in the tool output; in the nanodisc case the wrong bound array was written to the log first, so the wrong 4.35 ångström passed; on eight historical answers it caught zero of seven known errors and raised one false alarm on the exponent of inverse ångström.

**中文**
三个机制，各指向一个具体修法。卡在那里但从没被打开：四次卡组运行都列出了文件名，没有一次读内容。文件不是通道。按方法族检索给 HSP90 取到一张卡，是 BME 重加权卡，而这道题只比较沉积的违例、不拟合任何权重；同属一个方法族不等于操作适用；DHFR 和 ADK 取到零张，因为那 11 篇论文不覆盖纯 MD 的题。结论检查器问的是数字有没有出现在工具输出里；纳米盘案例里错误的上限数组先写进了日志，所以错的 4.35 Å 通过了；在 8 份历史答复上它 7 个已知错误一个没抓到，还在 Å⁻¹ 的指数上报了一次误报。

**要点**
- 扫盲：BME 是最大熵重加权，通过调已有构象的权重让预测更符合实验，同时限制偏离先验。读现成的 NOE 违例不产生这种义务。
- 被问"换更强的模型？"：最严重的错误在模型看不到的输入里，数字错误要按原始量重算才能判；都是流程问题。

---

## 14 · 表怎么搭：三种形式

**EN**
Back to the original idea: an Agent that enters the table and follows rules to choose operations and extra analyses. Three forms of that. Form one: keep the four layers and repair each with the mechanism from the previous slide, then retest on new questions. It assumes the failures were implementation, not concept. Form two: the rules serve the people who write the protocol and the rubric; the Agent gets a seven-line protocol only. This is what the current evidence directly supports, since the protocol arm was never worse, but it gives up the original idea. Form three: each rule becomes the configuration of a deterministic operator, an admission check, a computation, a claim-ceiling test; the Agent proposes which operator to call, code executes it and bounds the claim, and the Agent never reads rule text. This is closest to the original idea and closest to what DHFR and ADK taught, but none of it has been tested. My lean is to build toward three and keep two as the baseline that every version has to beat on new questions. Your call.

**中文**
回到原始设想：一个进入表、按规则选操作和补分析的 Agent。它有三种形式。形式一：保留四层，用上一页的机制逐层修，然后在新题上重测。它假设失败在实现，不在概念。形式二：规则服务写协议和评分依据的人，Agent 只拿七行协议。这是现有证据直接支持的，协议组从没更差，但它放弃了原始设想。形式三：每条规则变成一个确定性算子的配置，准入检查、计算、结论上限测试；Agent 提议调哪个算子，代码执行并限定结论，Agent 不读规则文字。这最接近原始设想，也最接近 DHFR 和 ADK 教的东西，但一点都没测过。我倾向朝三建，把二当作每个版本在新题上都必须击败的基线。你定。

**要点**
- 形式三对应 SYSTEM.md 里的分工：Agent 提议，确定性系统拥有验证、路由、数值、上限，人拥有竞争解释。
- 形式二的证据：HSP90 协议 4.5/5，Q05 4.5/5。
- 形式三"没测过"要说清楚，不要让她以为已经在做。

---

## 15 · 三个体系对不对

**EN**
The criterion I propose: a system needs MD plus an experimental observable that constrains the difference the question is about. HSP90 has two NOE references and CPMG; it fully qualifies, and it is the one system that gave a real cross-source result. DHFR has kinetics only, no structural observable; it tested the workflow, not the science, and it earned its keep by exposing the missing admission check. ADK has time-resolved scattering, but the deposited MD is apo and hundreds of nanoseconds against a millisecond process; it broke my admission rule, framing helped on it, and it is the only system the rules had never seen. The question for you: is this the right criterion, and is there a fourth system with MD plus NMR, SAXS or single-molecule FRET data that constrains populations, ideally from the group's own work?

**中文**
我提的标准：一个体系要同时有 MD 和一份能约束"题目要区分的差异"的实验观测。HSP90 有两套 NOE 参照和 CPMG，完全符合，也是唯一给出真正跨来源结果的体系。DHFR 只有动力学数据，没有结构观测；它测的是流程不是科学，它的价值是暴露了缺失的准入检查。ADK 有时间分辨散射，但沉积的 MD 是空载、几百纳秒对毫秒过程；它打破了我的准入规则，框题在它上面有效，它也是规则表唯一没见过的体系。问你的是：这个标准对不对，有没有第四个体系同时有 MD 和能约束占比的核磁、SAXS 或单分子 FRET 数据，最好是组里自己的工作？

**要点**
- DHFR 该不该丢：作为科学体系可以，作为流程回归测试值得留。
- 第四个体系的要求写清楚，让她的回答直接决定下一轮。

---

## 16 · 结论与三个问题

**EN**
Three sentences. The three systems produced bounded, checkable results; HSP90 is the strongest and is a real cross-source comparison. The table as prompt text did not earn its place; its content is still the raw material for executable checks and operation-indexed guidance, and framing the question explicitly is the one layer that measurably helped. The next build should put physical admission inside data preparation, make rules executable where they can be, and be tested against the seven-line protocol on new questions with independent scoring. Three decisions from you: is the workflow on slide 3 reasonable; which form of the table should we build toward; are these the right three systems, and is there a fourth.

**中文**
三句话。三个体系产出了有边界、可核查的结果；HSP90 最强，是真正的跨来源比较。表作为提示文字没有挣到位置；它的内容仍是可执行检查和按操作索引的指导的原料，把问题明确拆开是唯一可测量地有帮助的层。下一次构建应该把物理准入放进数据准备，把能做成可执行的规则做成可执行，并在新题上、用独立评分对照七行协议来测。请你定三件事：第 3 页的流程合不合理；表朝哪种形式建；这三个体系对不对，有没有第四个。

**要点**
- 这页留在屏幕上讨论。
- 不要再回到细节；她问什么翻附录。

---

## 追问预案

| 她可能问 | 答 |
|---|---|
| 10/20 和论文的 9 条一致吗 | 不同分类标准，问的不是同一件事；NOE 对照里 9/10 仍偏离两套参照，和论文"几乎满足开态 NOE"相容 |
| 为什么 1 Å | 预注册三档；0.5 Å 对照只有 7/20，太严；1 Å 对照 18/20；2 Å 下 3 条变一致；三档都报 |
| DHFR 一条轨迹能说什么 | 指定原子对的距离差别和方向；说不了机制和氢键，估不出波动 |
| ADK 为什么留 | 唯一没被规则和选择器见过的体系；Soojung 点名；准入规则的反例 |
| 规则没用了？ | 提示形式没得到支持；库是检查和卡的原料；Q05 上完整规则最好；不能说稳定增量 |
| 谁评的分 | 建包的同一个代理，标签遮住，单评分人；独立专家评分未做 |
| n=4 太少 | 是；四次中位数，标准预设，只做投入决定，不做正确率 |
| 换更强模型 | 最严重错误在输入，模型看不到；数字错误要重算；先管流程再比模型 |
| 形式三做过吗 | 没有，一行代码都没有；只有 DHFR/ADK 的物理检查是它的雏形 |
| 我要做什么 | 判 workflow；选形式；定每题竞争解释；给第四个体系 |
