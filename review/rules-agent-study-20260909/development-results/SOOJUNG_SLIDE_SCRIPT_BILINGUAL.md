# 逐页讲稿（中英对照）：对着 slides 念

2026-09-10 · 对应 `SOOJUNG_DISCUSSION_20260910_EN.pptx` v3（18 页正文，按 Pro 审查修订）· 每页两块：**念的英文**、**中文对照**。每页末尾一行"她若追问"。技术细节和扫盲在 `SOOJUNG_FULL_EXPLANATION_ZH.md`。

念的时候只看英文块，每页 60 到 100 秒。

---

## 1 · 标题

**EN**
Last time you knew I was building a Rules Table prototype. Today I want to discuss how the whole system should be built. I'll show the original idea, the workflow a new system goes through, what happened when three real systems went through it, what each use of the table measured, and three design options for the table itself. One headline first: putting rules into the AI's prompt did not help on the two questions where we tried it. Most of the errors we could locate sat at data entry or in the reported numbers; that audit is retrospective, not a controlled test. The one use that met its pre-set criterion was framing the question explicitly, and that part is done by a person.

**中文**
上次你知道的是我在做一个 rules table 的原型。今天我想讨论整套系统该怎么搭。我会讲原始设想、一个新体系走过的流程、三个真实体系走完后发生了什么、表的每一种用途各测到了什么，最后是表本身的三种设计方案。先说结论：在试过的两道题上，把规则贴进 AI 的提示没有帮助。能定位到的错误多数出在数据进来和数字出去两头，这是回头审计，不是对照实验。唯一达到预设标准的用途是把问题明确拆开，而那一步是人做的。

---

## 2 · 原始设想与表是什么

**EN**
This was the idea from July. A question and a data package come in. The AI analyst, I'll call it the Agent, consults a table of rules distilled from methods papers. The rules tell it which operations to run, which extra analyses to add, and where it must stop. The table has 33 rules from 11 papers, three per paper. Each rule stores what the paper showed, what we must check before using that kind of data, what the check needs, and where to stop if the check cannot be done. Bottom right is one rule verbatim, from Shevchuk's Bayesian SAXS paper: if the candidate structures omit a state, refinement can express uncertainty within the wrong set but cannot create the missing state.

**中文**
这是七月的想法。一道题和一个数据包进来。AI 分析助手，下面叫 Agent，查一张从方法论文里提炼的规则表。规则告诉它该跑哪些操作、补哪些分析、什么时候必须停。表里 33 条规则，来自 11 篇论文，每篇三条。每条存四样东西：论文证明了什么、我们用这类数据前必须查什么、检查需要哪些条目、查不了时在哪里停。右下角是一条规则原文，来自 Shevchuk 的贝叶斯 SAXS 论文：候选结构缺了某个状态，精修只能在错误的集合内表达不确定性，造不出缺失的状态。

她若追问"规则谁写的"：我八月从深读里提的；8 月 17 日外部审查要求把表当可审阅的账本，不当引擎。

---

## 3 · 新体系走过的六步

**EN**
Left to right. Intake: download the authors' deposited data and write a source card, a one-page record of paper, SI, README, frame counts and units. Package: derived tables such as per-frame distances, field definitions, physical checks, then freeze. Freezing means hashing the question, the grading key and the code before the first model call, so nothing is tuned afterwards. Frame: a person decides which difference the question must distinguish and writes the grading key, the list of what a correct answer must contain. Run: the Agent works in a sealed container. Check: automatic checks on what it submitted. Report: every number linked to its source, and the limit of the claim in words. The bottom row shows where the table can act: data checks at step 2, question framing at step 3, method guidance at step 4, conclusion checks at step 5. Before September we tested whether the selector picked the right checks: 41 of 41 pre-registered checks, among 146 generated. That is selection coverage, not scientific help. When the three systems ran, the table reached the Agent only at step 4, as selected rules pasted into the prompt.

**中文**
从左到右。接入：下载作者沉积的数据，写来源卡，一页纸记录论文、SI、README、帧数、单位。建包：派生表比如逐帧距离、字段定义、物理检查，然后冻结。冻结指在第一次调用模型前把题目、评分依据和代码记哈希，之后不能再调。框题：由人决定这道题要区分哪种差异，写评分依据，也就是正确答案必须包含什么的清单。运行：Agent 在密封容器里工作。检查：对它提交的内容做自动检查。报告：每个数字链接到来源，结论的边界用文字写明。下面那行是表能起作用的位置：数据检查在第 2 步，框题在第 3 步，方法指导在第 4 步，结论检查在第 5 步。九月之前测的是选择器有没有选中该选的检查：生成的 146 项里包含全部 41 项预登记检查。那是选中率，不是科学上的帮助。三个体系运行时，表只在第 4 步以选中规则贴进提示的形式到达 Agent。

她若追问"人在哪"：第 1、3、6 步。第 3 步不能委托，竞争解释由人定。这页讲完停一下，问她流程到这里有没有问题。

---

## 4 · 四个案例与比较设计

**EN**
Before the systems, the vocabulary. Four cases appear today. HSP90, DHFR and ADK are the systems you named. The nanodisc is a development case from Bengtsen's paper; we used it in September to check that the Agent can compute at all, and it reappears in one later test. The criterion I propose for choosing a system: it needs MD plus an experiment that constrains the very difference the question is about. Among the three systems you named, only HSP90 fully qualifies; the nanodisc qualifies too, but it is a development case, and its cross-observable result is in the appendix. I'll come back to this at the end. The comparison design is always the same. Same question, two or three conditions, four fresh runs each. A condition, or arm, differs in exactly one thing, for example rules in the prompt or not. Answers are scored against a grading key written from the public question, the data and the paper, frozen before the first run, never from the rules. Each question has five core units, the pieces a correct answer must contain, and we count units correct, errors, overclaims and omissions, then compare medians of four.

**中文**
讲体系之前先定词汇。今天出现四个案例。HSP90、DHFR、ADK 是你点名的体系。纳米盘是 Bengtsen 论文的开发案例，九月用它检查 Agent 到底能不能算，后面一个测试里还会出现。我提的选体系标准：要同时有 MD 和一份能约束"题目要区分的那个差异"的实验。按这个标准，你点名的三个体系里只有 HSP90 完全符合；纳米盘也符合，但它是开发案例，它的跨观测结果放在附录。最后再回到这点。比较设计始终一样：同一道题，两到三个条件，每个条件四次新运行。一个条件，或者叫一个组，只有一件事不同，比如提示里有没有规则。答复按评分依据打分，评分依据从公开题面、数据和论文写，第一次运行前冻结，从不从规则写。每道题有五个核心单元，就是正确答案必须包含的内容，数正确单元、错误、过强结论和遗漏，然后比四次的中位数。

她若追问"为什么四次"：够做投入决定，不够算正确率。

---

## 5 · HSP90：论文与我们的问题

**EN**
What the paper is. Henot and colleagues combine NMR with forty one-microsecond MD trajectories, twenty from the open crystal structure and twenty from a closed model, to argue that the closed state of the N-terminal domain is transiently populated. They classify the twenty closed-start runs as seven near-closed, about nine toward open, four neither, using NOE violations and clustering. They report millisecond exchange from CPMG and do not claim populations from MD. What we asked on the same forty trajectories: does a run show a sustained open direction, meaning the sign of two difference readouts stays open for five consecutive saved points, and does it ever reverse. The figure: of twenty closed-start runs, ten show a sustained open direction. For five, the first qualifying segment is already open-direction, which does not mean they were open at time zero. The other five first held a closed direction and turned open later; those are the same five counted as departures from the first sustained direction. Ten never show it. Open-start runs: none depart. Same data, different question, so our ten need not match their nine. The next slide connects the two.

**中文**
论文是什么。Henot 等人把核磁和四十条一微秒 MD 轨迹结合起来，二十条从开态晶体结构出发，二十条从闭态模型出发，论证 N 端结构域的闭态是瞬时占据的。他们用 NOE 违例和聚类把二十条闭合起始分成近闭 7、趋开约 9、皆非 4。他们用 CPMG 报告毫秒交换，不从 MD 估占比。我们在同一批四十条上问的是：一条轨迹是否出现持续的开放方向，定义是两个差值读数的符号在连续五个保存点上保持开放，以及之后有没有反向。图里：二十条闭合起始里十条有持续开放方向。其中五条的第一个合格片段就是开放方向，这不等于它们在零时刻就是开的。另外五条先保持闭合方向、后来转成开放，它们就是计作离开第一个持续方向的那五条。十条从没有。开放起始零离开。同一数据，不同问题，所以我们的 10 不必等于他们的 9。下一页把两者接起来。

她若追问"为什么 5 个点"：预注册 5、20、50；反向计数 5/4/1 随阈值下降，因为阈值同时改变拿哪一段当参照。

---

## 6 · HSP90：真正的科学结果

**EN**
"Open direction" is the sign of a difference and says nothing about reaching the open state. So we read the authors' deposited NOE violation series for both references, point by point. For each trajectory we asked what share of its open-direction points lies within 1 Å of the open references. If at least half are far from both references, the run is called relative only. Nine of the ten are relative only, ES04 is partial, and none reaches agreement. The open-start controls, the squares, agree in eighteen of twenty, which is what validates the tolerance. The scatter is for orientation; each point is the mean of the last hundred points. The runs have clearly left the closed side, and several end near the open line. ES15 drops from 9.1 to 1.1 ångström between its first and last hundred points, and ES04 and ES15 enter the band where the controls sit, below 1.32 ångström for fifty points, at 188 and 690 nanoseconds. So there is real structural change; moving closer is not the same as meeting the open tolerance most of the time. This agrees with the paper's own phrase that these runs almost satisfy the open NOEs. The system-level point: the Agent reproduced direction counts; nothing in the rules made it ask "did it arrive". A person added that question. That is what the framing use of the table is for. A question for you: is a 1 ångström tolerance on mean NOE violation a sensible test for being at the open state, and what would you use?

**中文**
"开放方向"只是差值的符号，说明不了有没有到达开态。所以我们逐点读取作者沉积的两套 NOE 违例序列。对每条轨迹，问它的开放方向点里有多大比例落在开态参照 1 Å 以内；如果至少一半同时远离两套参照，就记为只有相对方向。十条里九条是只有相对方向，ES04 部分一致，没有一条完全一致。开放起始对照组是方块，二十条里十八条一致，这是容差成立的依据。散点图只作定位，每个点是最后一百个点的均值。这些轨迹明显离开了闭态一侧，有几条末端靠近开态那条线。ES15 的开态违例从前一百点的 9.1 Å 降到后一百点的 1.1 Å；ES04 和 ES15 分别在 188 和 690 纳秒进入对照组所在的带（开放组 95 百分位 1.32 Å，连续 50 点）。所以结构变化是真的，但变近和多数时间满足开态容差是两回事。这和论文自己的说法一致，他们说这些轨迹"几乎满足"开态 NOE。系统层面的要点：Agent 复现了方向计数，规则里没有任何东西让它问"到了没有"。这个问题是人加的，这就是表的框题用途要做的事。想请你判断：用平均 NOE 违例 1 Å 的容差判断到达开态，合不合适，你会用什么？

她若追问"为什么 1 Å"：预注册 0.5、1、2；0.5 时对照只有 7/20；2 Å 时 3 条候选变一致；三档都报。
她若追问"到底开没开"：部分轨迹出现开放方向，并在局部接近开态参照，不能统一算成完整的物理转换。对照带是同源的经验比较，不是独立的状态校准。

---

## 7 · HSP90：第一次对照

**EN**
This was the first real use of the table, in the form the three systems ran under. Same question, four answers: two with only the data, two with the selected rules rendered into the prompt, seven rules, eight obligations, about 7,600 characters. Three of four got the main counts right; one mixed the five-point and fifty-point thresholds and did no calculation. The two rule answers were not more accurate. One of them, B2, added a useful 10 of 20 count. Both carried RMP-restraint conditions that belong to FRET-assisted modeling. That text reached the prompt because an NMR reference-source check was mapped onto Dimura's FRET-assisted modeling rule, and an MD-uncertainty check onto a smFRET uncertainty-provenance rule with R0 and dye volume. The paper supports those conditions for its own method; making them required fields for any NMR or MD analysis was our addition. A rule can be retrieved correctly and still be wrong for the task. Two runs per arm, and both arms shared the hand-written question, tables and field notes, so this cannot separate the selector from the protocol, the curation or the text length. It was enough to stop expanding this form and ask where the errors actually live.

**中文**
这是表的第一次真实使用，也是三个体系运行时的形式。同一道题四份答复：两份只有数据，两份把选中的规则渲染进提示，7 条规则、8 项义务、约 7,600 字符。三份主计数正确；一份把 5 点和 50 点阈值混在一起，而且没做计算。两份规则组答复没有更准，其中 B2 多给了一个有用的 10/20 计数。两份都带入了属于 FRET 辅助建模的 RMP 约束条件。这段文字进提示，是因为一条 NMR 参考来源检查被映射到 Dimura 的 FRET 辅助建模规则，一条 MD 不确定性检查被映射到带 R0 和染料体积的 smFRET 不确定性来源规则（C001-RULE-002）。论文支持这些条件用于它自己的方法；把它们变成任何 NMR 或 MD 分析的必填项，是我们加的。规则可以被正确检索到，同时不适用于这道题。每组两次，而且两组共用人写的题面、表格和字段说明，所以分不开选择器、协议、整理和文本长度各自的作用。但这足够让我们停止扩展这种形式，去问错误到底在哪。

---

## 8 · DHFR

**EN**
What the paper is. Trimethoprim loses potency against the L28R mutant of DHFR; the analog 4′-DTMP recovers it. Their Table 1 inhibition constants: wild type 4.2 versus 5.1 nanomolar, L28R 65 versus 34. Their MD explanation: 4′-DTMP sits closer to atoms of the M20 loop and arginine 28. What we asked: the specified protein–ligand atom distances, one trajectory per condition, 990 frames. The figure: on the left, the frozen table built from stored coordinates. A whole cluster of frames sits between 46 and 94 ångström. That is not a conformation; the ligand copy in a neighbouring periodic image was measured. Both Agent answers used these numbers; one called the tail conformational switching. On the right, the corrected table using the nearest periodic ligand image, cross-checked with VMD to ten to the minus five. M20 nitrogen to ligand O3P goes from 8.7 to 4.6 in wild type and 10.4 to 4.8 in L28R when TMP becomes 4′-DTMP; all six specified pairs move the same way as the paper's Figure 4. The gap: the paper frames hydrogen bonds; we have mean distances, no angles, one run each. The lesson: no rule text catches an input artifact. The check must sit at step 2, in code, before freezing. This was a preparation defect on my side.

**中文**
论文是什么。甲氧苄啶对 DHFR 的 L28R 突变体失效，类似物 4′-DTMP 恢复了效力。表 1 的抑制常数：野生型 4.2 对 5.1 纳摩尔，L28R 65 对 34。他们的 MD 解释：4′-DTMP 更靠近 M20 环和精氨酸 28 的原子。我们问的是：指定的蛋白配体原子距离，每个条件一条轨迹，990 帧。图：左边是用存储坐标建的冻结表。一大簇帧落在 46 到 94 Å。那不是构象，量到的是相邻周期镜像里的配体副本。两份 Agent 答复都用了这些数，一份把长尾叫构象切换。右边是用最近周期配体镜像修正后的表，用 VMD 交叉核对到十的负五次方。M20 的氮到配体 O3P 在野生型从 8.7 缩到 4.6，L28R 从 10.4 缩到 4.8，都是 TMP 换成 4′-DTMP；六对指定原子的方向都和论文图 4 一致。差距：论文讲氢键，我们只有平均距离，没有角度，每个条件一条轨迹。教训：任何规则文字都抓不住输入伪影。检查必须放在第 2 步、用代码、冻结之前。这是我这边的准备缺陷。

她若追问"一条轨迹能说什么"：指定原子对的距离差别和方向；说不了机制和氢键，估不出波动。

---

## 9 · ADK

**EN**
What the paper is. Photorelease of ATP, time-resolved X-ray solution scattering, a transient of about 4.3 milliseconds, interpreted with MD-derived candidate structures. The deposited MD: two trajectories, open-start 450 nanoseconds and closed-start 335, and no ATP or AMP in the coordinates. What we asked, the one thing computable: mean C-alpha distances between the LID or NMP domain and the CORE, comparing the first and last ten percent of frames, the shaded windows. All four changes are positive and the distributions overlap, so there is no net joint closure between the endpoint windows; this does not exclude closure episodes inside the runs. The gap: no ligand, no scattering recomputed, nanoseconds against milliseconds; this does not test the paper's mechanism. The system lesson is about my own rule. After DHFR I wrote a data check: any distance above half the box length fails. Open ADK spans 56 ångström along one axis in a 98 to 100 ångström box, so C-alpha distances of 62 and 70 ångström are real, and GROMACS reproduces them. The rule was replaced by a physical criterion. DHFR asked a protein–ligand contact, so the nearest ligand image is right there; ADK asks a distance inside one protein, so the molecule must stay whole. The check has to follow the observable. Framing also helped here: the split version of the ADK question scored five of five.

**中文**
论文是什么。光释放 ATP，时间分辨 X 射线溶液散射，约 4.3 毫秒的瞬态，用 MD 产生的候选结构解释。沉积的 MD：两条轨迹，开态起始 450 纳秒，闭态起始 335 纳秒，坐标里没有 ATP 和 AMP。我们问的是唯一能算的：LID 或 NMP 到 CORE 的平均 Cα 距离，比较首末各 10% 的帧，就是阴影窗口。四个变化都是正的，分布重叠，所以首末窗口之间没有净的共同闭合；这不排除轨迹中间出现过闭合片段。差距：没有配体，没有重算散射，纳秒对毫秒；它检验不了论文的机制。系统教训是关于我自己的规则。DHFR 之后我写了一条数据检查：任何距离超过半盒长就判失败。开态 ADK 沿一个轴延展 56 Å，盒子 98 到 100 Å，所以 62 和 70 Å 的 Cα 距离是真的，GROMACS 也复现了。这条规则换成了物理判据。DHFR 问的是蛋白配体接触，取最近的配体镜像是对的；ADK 问的是同一个蛋白内部的距离，分子必须保持完整。检查要跟着观测量走。框题在这里也有帮助：拆题版的 ADK 问题得了五分之五。

她若追问"为什么留 ADK"：规则和选择器唯一没见过的体系；也是你点名的。

---

## 10 · 回看错误

**EN**
Before testing the four uses we audited every answer we had: eight answers, thirteen observations, seven underlying causes, so correlated observations rather than thirteen independent cases. Grouped by the workflow step where each lives: input representation, numbers read from the wrong column or threshold, the sign of a difference read as arrival, imported conditions. Reminder text had no obvious hook in any of them; that is a judgement, not a test. Code before freezing or after submission could plausibly prevent most; two need the question asked better. That was a candidate attribution from a non-random set of answers; the next slides test it. One detail for later: three of the thirteen were caught when we replayed the DHFR input checks; the conclusion checker on slide 15 caught zero of the seven numeric ones. Different subsets, both true.

**中文**
测四种用途之前，我们审计了手上全部答复：8 份答复，13 处观察，7 个根本原因，所以是相关的观察，不是 13 个独立案例。按错误住在哪一步分组：输入表示、从错的列或阈值读数、差值符号被读成到达、带入的条件。提醒文字在这些错误上都找不到明显的着力点，这是判断，不是实验。冻结前或提交后的代码看起来能防大多数；两处需要把问题问得更好。这是从非随机样本得出的候选归因，接下来几页去测它。一个细节留到后面：13 处里有 3 处在重放 DHFR 输入检查时被抓到；第 15 页的结论检查器在 7 处数值错误上一处没抓到。两个不同的子集，都成立。

---

## 11 · Agent 一次运行

**EN**
Before the tests, what one run is. A fresh container: no network, data read-only, five tools, and a submit call that ends the answer; ordinary text afterwards never overwrites it. The model is gpt-5.6-luna at medium reasoning. A typical run is twelve to twenty tool calls, about a minute, under two cents. It genuinely computes: it matched all ninety SAXS points in the nanodisc case and reproduced the four ADK window changes to four decimals. So the cost of an experiment is scoring time, not money. Why the Agent stays: goal four asks whether an agent can lower curation cost without adding unsafe claims; it is the last goal and allowed to fail on its own. The open question is not "can it analyse". It is what information given to it produces a measurable gain.

**中文**
测试之前，先说一次运行是什么。一个新容器：没有网络，数据只读，五个工具，一个结束答案的提交调用；之后的普通文字不会覆盖。模型是中等推理强度的 gpt-5.6-luna。典型一次运行十二到二十次工具调用，一分钟左右，不到两美分。它是真的在算：纳米盘案例里匹配了全部九十个 SAXS 点，ADK 的四个窗口变化算到小数点后四位。所以实验的成本是评分时间，不是钱。为什么 Agent 保留：第四个目标问的是 Agent 能不能在不增加不安全结论的前提下降低整理成本；它排最后，允许单独失败。悬而未决的不是"它能不能分析"，是给它什么信息能产生可测量的增益。

---

## 12 · 四种用途

**EN**
This is the current design, and a direct answer to the original question of how the Agent should use the table. Framing: six rules become sub-questions and the grading key, never shown to the Agent. Data checks: ten rules become code before freezing, reaching the Agent only as a card of results. Method cards: eleven rules become short cards retrieved by method family, the only rule text the Agent reads. Conclusion checks: six rules become an automatic check after submission with one feedback message. Each use changes exactly one thing about what the Agent receives, so each can be tested on its own. The ensemble blog by Li, Thomasen and Cossio motivates the order: decide which difference to distinguish, confirm it survives measurement and processing, then choose the method. The four-way split is our own design hypothesis, not a conclusion of the blog, and the uses overlap: whether a method applies matters in preparation, computation and interpretation alike.

**中文**
这是现在的设计，也是对"Agent 该怎么用这张表"这个原始问题的直接回答。框题：6 条规则变成子问题和评分依据，不给 Agent 看。数据检查：10 条变成冻结前的代码，Agent 只收到一张结果卡。方法卡：11 条变成按方法族检索的短卡，是 Agent 唯一读到的规则文字。结论检查：6 条变成提交后的自动检查加一次反馈。每种用途只改变 Agent 收到的一样东西，所以每种可以单独测。Li、Thomasen、Cossio 的 ensemble 博文给了顺序的理由：先定要区分哪种差异，再确认它经过测量和处理后还在，然后才选方法。拆成四种用途是我们自己的设计假设，不是博文的结论；几种用途也有重叠，方法适不适用在准备、计算、解释三个阶段都要问。

她若追问"分层是不是随意的"：按表里的 rule_class 字段分，附录 A2 可逐条争论。

---

## 13 · 每种用途测了什么

**EN**
The reasoning behind the three questions we measured. Framing: from HSP90 we knew the Agent answered the direction question but never the arrival question; if framing helps, splitting the question raises supported coverage without adding overclaims. Data checks: from DHFR we knew a bad table passed; the checker was tried on six planted defects and three clean packages, and the Agent was given or not given the card on the defective table; if the card helps, it downgrades its conclusions. Method cards: from HSP90 we knew full rules imported conditions; if cards help, they keep accuracy and stop the imports, judged against a seven-line protocol and the full rules. Conclusion checks: from the threshold mix-up and the nanodisc bound array we knew numbers went out wrong; if the check helps, one automated pass reduces core errors without more omissions. Same model, four runs per condition, frozen, de-labelled scoring, medians of four.

**中文**
我们测的三个问题背后的推理。框题：从 HSP90 知道 Agent 答了方向没答到达；如果框题有用，拆题后有支持的覆盖上升、过强结论不增加。数据检查：从 DHFR 知道坏表通过了；检查器在六种植入缺陷和三个干净包上试，Agent 在坏表上分别拿到和拿不到卡；如果卡有用，它会降级结论。方法卡：从 HSP90 知道完整规则带入了条件；如果卡有用，它保住准确率、停止带入，对照七行协议和完整规则来判。结论检查：从阈值混用和纳米盘的上限数组知道数字出去时是错的；如果检查有用，一次自动检查减少核心错误、不增加遗漏。同一模型，每个条件四次，冻结，去标签评分，四次中位数。

她若追问"谁评的分"：建包的同一个代理，标签遮住，单评分人；这是最大限制，报告里写明。

---

## 14 · 结果

**EN**
Four rows. Framing: coverage HSP90 2 to 2.5 of 3, ADK 2 to 3 of 3, no new overclaims; keep. Two caveats: HSP90's total errors across four runs went 1 to 2, so the gain is completeness, not uniformly accuracy; and the sub-questions were written by a person, so this is a gain of the person-plus-Agent workflow, not of the Agent alone. Data checks: the checker caught all six planted defects, but the Agent detected the DHFR defect zero of four times with the card and zero of four without. Method cards: on HSP90 the plain protocol scored 4.5 of 5, full rules 2, cards 2.5; on the nanodisc question 4.5, 5, 4.5. Cards failed. The exception to keep on record: full rules were best on the nanodisc question, all four answers covered all five units. Feedback: only ADK improved, and that difference already existed in the initial drafts; no revision reduced its own error count; three lost content, one of them without receiving any warning.

**中文**
四行。框题：覆盖 HSP90 从 3 分之 2 到 2.5，ADK 从 2 到 3，没有新增过强结论；保留。两个但书：HSP90 四次运行的错误总数从 1 到 2，所以收益是完整性，不是一律更准；子问题是人写的，所以这是人加 Agent 流程的收益，不是 Agent 单独的。数据检查：检查器抓到全部六种植入缺陷，但 Agent 拿卡时发现 DHFR 缺陷 0/4，不拿也 0/4。方法卡：HSP90 上协议 5 分之 4.5，完整规则 2，卡 2.5；纳米盘题 4.5、5、4.5。卡没达标。要记在案的例外：纳米盘题上完整规则最好，四份答复全覆盖五个单元。反馈：只有 ADK 改善，而且差异初稿就有；没有一次修订减少自己的错误；三份丢内容，其中一份根本没收到提示。

她若追问"规则没用了？"：提示形式没得到支持；库仍是检查和卡的原料；纳米盘是完整文本帮了忙的一个案例；不能说的是稳定增量。
她若追问"拆题有效是不是只是提示更详细"：这是当前证据允许的主要解释；额外要求、文本长度和推理能力还没有分开。

---

## 15 · 为什么失败

**EN**
Three mechanisms, each pointing at a specific repair. The card was available but never opened: all four card runs listed the file, none read it. A file is not a channel. Retrieval by method family gave HSP90 one card, a BME reweighting card, for a task that compares deposited violations and fits nothing. BME, Bayesian maximum entropy, adjusts the weights of existing conformations to match experiment; reading deposited NOE violations creates no such obligation. DHFR and ADK retrieved zero cards, because the eleven papers do not cover pure-MD questions. The conclusion checker asks whether a number appears in the tool output; in the nanodisc case the wrong bound array was written to the log first, so the wrong 4.35 ångström passed. On eight historical answers it caught zero of seven known numeric errors and raised one false alarm on the minus one in inverse ångström.

**中文**
三个机制，各指向一个具体修法。卡在那里但从没被打开：四次卡组运行都列出了文件名，没有一次读。文件不是通道。按方法族检索给 HSP90 一张卡，是 BME 重加权卡，而这道题只比较沉积的违例、不拟合任何东西。BME 是贝叶斯最大熵，调已有构象的权重让预测符合实验；读现成的 NOE 违例不产生这种义务。DHFR 和 ADK 取到零张，因为那 11 篇论文不覆盖纯 MD 的题。结论检查器问的是数字有没有出现在工具输出里；纳米盘案例里错误的上限数组先写进了日志，所以错的 4.35 Å 通过了。在 8 份历史答复上它 7 个已知数值错误一个没抓到，还在 Å⁻¹ 的 −1 上误报一次。

她若追问"换更强的模型"：最严重的错误在模型看不到的输入里；数字错误要按原始量重算；都是流程问题。

---

## 16 · 三种形式

**EN**
Back to the original idea: an Agent that enters the table and follows rules to choose operations and extra analyses. Three forms of that. Form one: keep the four uses and repair each with the mechanism from the previous slide, then retest on new questions; it assumes the failures were implementation, not concept. Form two: the rules serve the people who write the protocol and the grading key; the Agent gets a seven-line protocol only. This has the strongest evidence today, the protocol arm was never worse, but it gives up the original idea. Form three: each rule becomes the configuration of a deterministic operator, a data check, a computation, a claim-limit test; the Agent proposes which operator to call, code executes it and bounds the claim, and the Agent never reads rule text. The bridge from evidence to this form is the mechanisms: the checks that actually mattered, in DHFR and ADK, were physical and executable, and the failures were all about text, delivery, applicability, string matching. It is closest to the original idea and to that lesson, but none of it has been built or tested. My lean: build toward three, keep two as the baseline every version must beat on new questions. Your call.

**中文**
回到原始设想：一个进表、按规则选操作和补分析的 Agent。它有三种形式。形式一：保留四种用途，用上一页的机制逐个修，然后在新题上重测；它假设失败在实现不在概念。形式二：规则服务写协议和评分依据的人；Agent 只拿七行协议。这是今天证据最强的，协议组从没更差，但它放弃了原始设想。形式三：每条规则变成一个确定性算子的配置，一个数据检查、一个计算、一个结论上限测试；Agent 提议调哪个算子，代码执行并限定结论，Agent 从不读规则文字。从证据到这个形式的桥是那些机制：真正起作用的检查，DHFR 和 ADK 的，都是物理的、可执行的；失败的全是关于文字的，投递、适用性、字符串匹配。它最接近原始设想和这个教训，但一点都没建、没测。我的倾向：朝三建，把二当作每个版本在新题上都必须击败的基线。你定。

她若追问"形式三做过吗"：没有，一行代码都没有；DHFR/ADK 的物理检查是它的雏形。

---

## 17 · 三个体系对不对

**EN**
Back to the criterion: MD plus an experiment that constrains the difference the question is about. HSP90 has two NOE references and CPMG; it fully qualifies, and together with the nanodisc development case it is where we have a cross-source result. DHFR has kinetics only; it tested the workflow, not the science, and exposed the missing data check. ADK has time-resolved scattering, but the deposited MD is ligand-free and nanoseconds against milliseconds; it broke my data check, framing helped on it, and it is the only system the rules had never seen. The question for you: is this the right criterion, and is there a fourth system with MD plus NMR, SAXS or single-molecule FRET data that constrains populations, ideally from the group's own work?

**中文**
回到标准：MD 加一份能约束"题目要区分的差异"的实验。HSP90 有两套 NOE 参照和 CPMG，完全符合；它和纳米盘开发案例是我们手上有跨来源结果的地方。DHFR 只有动力学数据；它测的是流程不是科学，暴露了缺失的数据检查。ADK 有时间分辨散射，但沉积的 MD 没有配体、纳秒对毫秒；它打破了我的数据检查，框题在它上面有效，它也是规则唯一没见过的体系。问你的是：这个标准对不对，有没有第四个体系同时有 MD 和能约束占比的核磁、SAXS 或单分子 FRET 数据，最好是组里自己的工作？

她若追问"DHFR 丢掉？"：作为科学体系可以，作为流程回归测试值得留。

---

## 18 · 结论与三个问题

**EN**
Three sentences. The three systems produced bounded, checkable results; HSP90 is the strongest and a real cross-source comparison. The table as prompt text did not earn its place; its content is still the raw material for executable checks and operation-indexed guidance, and framing the question explicitly, by a person, is the one use that measurably helped. The next build should put physical data checks inside preparation, make rules executable where they can be, and be tested against the seven-line protocol on new questions with independent scoring. Three decisions from you: is the workflow on slide 3 reasonable; which form of the table should we build toward; are these the right three systems, and is there a fourth. And one science question: in HSP90, is a 1 ångström tolerance on mean NOE violation the right test for being at the open state?

**中文**
三句话。三个体系产出了有边界、可核查的结果；HSP90 最强，是真正的跨来源比较。表作为提示文字没有挣到位置；它的内容仍是可执行检查和按操作索引的指导的原料，由人把问题明确拆开是唯一可测量地有帮助的用途。下一次构建应该把物理数据检查放进准备阶段，能做成可执行的规则做成可执行，并在新题上用独立评分对照七行协议来测。请你定三件事：第 3 页的流程合不合理；表朝哪种形式建；这三个体系对不对，有没有第四个。还有一个科学问题：HSP90 里，用平均 NOE 违例 1 Å 的容差判断到达开态，合不合适？

这页留在屏幕上讨论。她问什么，翻附录。
