# RfaH 2012 与 2025：作者从数据到结论的决策片段

格式同 `KRAS_DECISION_FRAGMENTS_ZH.md`。"明确"= 论文写出的步骤；"重建"= 按证据依赖推出、论文没写先后的步骤。两篇均为 PMC 网页全文（本地 HTML 去标签后阅读），没有期刊页码，定位用小节标题与图表号；SI 未在本地，凡依赖 SI 内容的地方只引用正文对 SI 的描述。阶段名采用六段：frame、inventory、baseline、discriminate、interpret、synthesize。"合同效果"一行说明片段对 Codex 流程提示（`<codex-worktree>/docs/science_workflow/SYSTEM_PROMPT.md`）的作用：加强、细化或抵触，并引用受影响的英文原句；14 个片段中没有出现抵触。

二手参考 `paper_trace_RFAH_2012_2025.md` 与全文核对后沿用其大部分定位；与全文不符或全文没有的内容未采用。

---

## 一、Burmann et al. 2012（Cell）

- 论文：Burmann et al., "An α-helix to β-barrel domain switch transforms the transcription factor RfaH into a translation factor", Cell 150:291–303 (2012)，PMC3430373 作者稿。
- 问题：RfaH 的 C 端结构域（CTD）在全长蛋白里是贴在 N 端结构域上的 α 发夹；它脱离 N 端后会不会变成 NusG-CTD 那样的 β 桶，这个变化有没有功能。
- 作者主要结论：脱离后的 CTD 从全 α 完全重折叠为与 NusG-CTD 相同的全 β 构象，由此能结合核糖体蛋白 S10，并强烈增强 RfaH 调控操纵子的翻译（Summary；Discussion 首段）。
- 数据可得性：新结构 PDB 2LCL（孤立 CTD，NMR）公开；参照结构 2OUG（全长 α 态）、2JVV（NusG-CTD）、3D3B（NusB:S10）公开。正文未给 BMRB 号；BMRB 17615 按标题匹配为 CTD 结构条目，但论文未引用，归属关系未确认。HSQC 谱、弛豫、报告基因、qRT-PCR、ChIP-chip、交联质谱只在图中，无存档（`DATA_AVAILABILITY_PROBE.md` RfaH 行）。

## 片段 1：晶体里的 α 发夹在溶液里是否也成立（明确，Results "Full-length RfaH maintains a closed state in solution"，Fig. 2）
- 观察：全长 RfaH 的晶体结构（2OUG）中 CTD 是 α 发夹、紧贴 N 端结构域；这可能是晶体堆积造成的。
- 问题：溶液中的全长 RfaH 是否也保持这个闭合、全 α 的状态，还是 CTD 在 α 与 β 之间平衡？
- 竞争解释：(a) 溶液中与晶体一致；(b) 溶液中 CTD 存在两种构象的平衡；(c) 两个结构域在溶液中分开。
- 作者的检查：做全长蛋白骨架归属，用 ¹H/¹³C 二级位移（CSI）对照晶体二级结构（Fig. 2B）；测 ¹⁵N R1、R2（18.8 T，288 K），得 R1 = 0.68±0.12 s⁻¹、R2 = 31.8±5.2 s⁻¹、各向同性模型 τc = 13.4 ns，并比较两个结构域的 R1/R2 分布（Fig. 2C–E）。
- 结果与含义：CSI 与晶体二级结构一致，α4 比晶体短约一圈；两个结构域的 R1/R2 分布为单峰、翻转相关时间相同 → 结构域在溶液中紧密结合。作者据此写"排除"了溶液中 CTD 构象平衡。
- 影响：全长蛋白里看不到 β 态，要证明 β 态就必须换系统（片段 2–4）。"排除平衡"只对可观测布居成立：CSI 只报告主态，低布居的次要态看不到（推断）；2025 年论文引言就提到全长 RfaH 存在一个毫秒交换的低布居激发态（2025 Introduction，引文 12）。
- 所属阶段：frame（主）、baseline
- 合同效果：细化——提示只禁止从"数据缺失、工具出错、预算用尽"推出否定结论；本片段说明"低于检测限而未观测到"同样不能写成不存在，应把这一情形加入该句。原文（SYSTEM_PROMPT.md 第 37 行）："Do not infer a scientific negative from unavailable data, tool errors, or an execution budget limit."
- Agent 对应：可执行动作——用 BMRB 52348（全长 RfaH 骨架位移，Cai 2024，公开）算二级位移或 TALOS 类二级结构指数，与 2OUG 的 DSSP 二级结构逐段比对；条目中注明 52348 与 2012 年的温度、缓冲条件不同。2012 年的弛豫数据未存档，τc 判断只能引用论文数值。
- 可迁移的通用教训：晶体结构当作溶液主态之前，先用溶液位移核对二级结构、用弛豫核对结构域是否一起翻转；"没有看到第二个构象"只说明它低于检测限。

## 片段 2：孤立 CTD 是不是 β 桶（明确，Results "RfaH-CTD refolds into a β-barrel upon release from RfaH-NTD"，Fig. 3，Table S1，Fig. S1）
- 观察：孤立表达的 CTD 的 HSQC 与全长蛋白中 CTD 的信号差别很大（Fig. S1）。
- 问题：孤立 CTD 采取什么折叠？是部分解折叠，还是另一种确定的折叠？
- 竞争解释：(a) 孤立后部分或完全无序；(b) 保留 α 发夹但位移因失去界面而改变；(c) 形成确定的 β 折叠。
- 作者的检查：从头解孤立 CTD 的 NMR 结构（20 个最低能量结构，Fig. 3B；统计见 Table S1）；与同家族已知的 NusG-CTD（2JVV）做骨架叠合；再把 NusG-CTD 疏水核心对应的残基分别标在 α 态（2OUG）与 β 态上（Fig. 3C、3D）。
- 结果与含义：五条 β 链 K115–I118、Q127–F130、R138–N144、E149–K155、F158–K160，链序 β5-β1-β2-β3-β4，无螺旋；与 NusG-CTD 在 P112–L162 上的骨架 RMSD 0.65 Å；最大局部差异在 E132–R138。NusG-CTD 核心对应残基在 α 态中散布在螺旋上，在 β 态中组成疏水核心 → 孤立 CTD 是与 NusG-CTD 同型的 β 桶，(a)(b) 被排除。
- 影响：β 态结构成为此后所有工作的参照（2025 年的 A 态直接用 2LCL）。仍未回答"截短构建体是否人为造成 β 态"，见片段 3、4。
- 所属阶段：interpret（主）、baseline
- 合同效果：加强——作者用自身结构、同源折叠叠合和核心残基对照三种参照判定折叠，正是该句要求的多参照比较。原文（SYSTEM_PROMPT.md 第 13–15 行）："interpret: build claims at the appropriate local or global scope; compare plausible references on comparable data; explain discrepancies without treating resemblance as a unique mechanism or a solved structure."
- Agent 对应：可执行动作——下载 2LCL 与 2JVV，按序列比对建立残基对应，在 P112–L162 上算骨架 RMSD；对 2LCL 跑 DSSP 核对五条链的边界；比较核心残基在 2LCL 与 2OUG 中的溶剂可及面积；另用 BMRB 52718（2025 年孤立 CTD 主态位移，公开）算二级结构指数，作为独立于 NOE 结构的位移证据。所需数据全部公开。RMSD 数值依赖所选模型与比对方式，复算时报告所用模型和残基集。
- 可迁移的通用教训：判断一个新构象是什么折叠，最强的做法是同时拿出自身结构、与已知同源折叠的定量叠合、以及核心残基在两种构象中的角色对照。

## 片段 3：加热和 TFE 让蛋白沉淀，改用削弱界面的点突变（明确，同上小节 Fig. 4A、4B 前两段）
- 观察：孤立 CTD 是 β 桶，但全长蛋白里看不到 β 态。
- 问题：β 态是不是截短构建体的产物？开关能否在全长蛋白里发生？
- 竞争解释：(a) β 态只在截短后出现；(b) 全长蛋白中只要界面被削弱，CTD 就会转为 β 态。
- 作者的检查：先用升温和三氟乙醇削弱结构域界面，两者都立即导致蛋白完全沉淀（推测是暴露了大片非极性界面）。转而做 E48S 单点突变，破坏连接两个结构域的 E48:R138 盐桥，保持可溶；把 E48S 的 HSQC 与野生型全长（α 态参照）和孤立 CTD（β 态参照）叠加（Fig. 4A、4B）。
- 结果与含义：E48S 谱中同时出现 N 端结构域信号、α 态 CTD 信号与 β 桶 CTD 信号，两者峰强相近，约 1:1 共存 → 开关可以在全长蛋白中发生。
- 影响：否定了 (a) 的最强形式，但突变本身可能改变 CTD 的折叠倾向，作者因此追加片段 4。
- 所属阶段：discriminate（主）、interpret
- 合同效果：加强——加热与 TFE 导致沉淀后作者换成界面点突变，是该句"change method"处置的实例。原文（SYSTEM_PROMPT.md 第 34–35 行）："The disposition may be to revisit, change method, limit a claim, or retain it with a concrete reason."
- Agent 对应：仅为建议实验——对"替代折叠只在孤立结构域中出现"的系统，建议在全长蛋白中做一个只削弱结构域界面、不改动该结构域本身序列的点突变，采集 HSQC 并与两种参照谱叠加，以峰体积估两态比例。该论文的谱图未存档，Agent 无法重做。
- 可迁移的通用教训：全局变性手段失败时，改用只针对界面的最小扰动，并用两种已知状态的参照谱做指纹比对来识别新出现的信号。

## 片段 4：用 TEV 切断连接区，排除突变的影响（明确，同上小节 Fig. 4C、4D 及后两段）
- 观察：E48S 显示两态共存，但突变位于 N 端结构域，仍可能间接影响结果。
- 问题：不改动任何结构域序列时，CTD 脱离后是否自发变成 β 桶？
- 竞争解释：(a) E48S 特有效应；(b) 结构域分离本身足以驱动重折叠。
- 作者的检查：在柔性、不保守的连接区插入 TEV 切割位点，先确认该构建体功能与野生型相同（Fig. 4C 及引文）；加 1.75 μM TEV 蛋白酶，孵育 42 h 前后采集 HSQC，并与孤立 CTD 谱叠加（Fig. 4C、4D）。
- 结果与含义：初始谱与全长蛋白一致（另有 TEV 位点 7 个残基的信号）；42 h 后出现 β 桶 CTD 信号，α 态 CTD 信号消失，N 端结构域信号因沉淀丢失 → 结构域断开后 CTD 自发重折叠，支持 (b)。作者说明观察到的速率受 TEV 切割速度限制。
- 影响：结论"CTD 脱离即重折叠"由此成立；"转录中真实发生"是推断（原文用 strongly suggest）。实验只给出终态，没有速率、可逆性和中间态——这正是 2025 年论文要回答的问题。
- 所属阶段：discriminate（主）、synthesize
- 合同效果：细化——该句只要求"一个能区分的检查"；本片段表明扰动本身可能制造结果，需要再用一个不改动相关结构域的正交扰动重复。原文（SYSTEM_PROMPT.md 第 11–12 行）："discriminate: name plausible competing explanations; choose a check that can distinguish them; state what different outcomes would imply; perform the check and update the plan."
- Agent 对应：仅为建议实验——建议对同类系统做"可切割连接区"构建体：先用功能实验确认插入位点不影响活性，再在切割前后用 HSQC 追踪信号出现与消失；若需要速率，改用能快速、同步触发分离的方法，因为切割本身会成为限速步骤。
- 可迁移的通用教训：用突变证明一个现象后，再找一个不改动相关结构域序列的扰动重复一次，排除突变自身造成的结果。

## 片段 5：β 态 CTD 能与谁结合，结合是否依赖折叠（明确，Results "Functional role for RfaH-CTD refolding" 第 3 段，"RfaH:CTD forms a complex with S10 in vitro"，Fig. 6，Fig. S4，Fig. S6）
- 观察：NusG-CTD 的 β 桶能结合 Rho 和 S10；RfaH-CTD 采取同样折叠。
- 问题：相同折叠是否意味着相同的结合伙伴？结合是否只对 β 态成立？
- 竞争解释：(a) 同折叠同伙伴；(b) 只结合其中一部分；(c) 伙伴本身能诱导全长 RfaH 打开。
- 作者的检查：用 ¹⁵N-CTD 的 HSQC 滴定 Rho（Fig. S4）；用 NMR 与凝胶过滤检测 CTD 与 S10 的结合（Fig. S6D–F），在 S10 与 CTD 两侧做化学位移扰动映射并与 NusG-CTD:S10 界面对照（Fig. 6）；再把未标记的全长 RfaH 滴入 ¹⁵N-S10（Fig. S6G）。
- 结果与含义：Rho 滴定无显著变化 → 不结合；S10 直接结合，界面与 NusG-CTD 相似；Kd 无法由 NMR 数据确定，只在高浓度下观察到结合。全长 RfaH 与 S10 无相互作用 → S10 只识别 β 态，且不能单独诱导打开，排除 (c)。
- 影响：把"折叠变化"与"新伙伴"对应起来；亲和力缺失，功能证据要靠片段 6 的体内实验补足。
- 所属阶段：discriminate（主）、interpret
- 合同效果：加强——"原构象对同一伙伴是否结合"是必须盘点的对照，缺少时应记为 missing control。原文（SYSTEM_PROMPT.md 第 7–8 行）："inventory: distinguish measured inputs, derived quantities, references, and missing controls."
- Agent 对应：仅为建议实验——建议对每个候选伙伴分别用两种构象的样品做 HSQC 滴定（替代构象的孤立结构域与天然全长蛋白各一次），把"不结合"的对照和"结合"同等报告；需要亲和力时改用 ITC 或 BLI。滴定谱未存档。
- 可迁移的通用教训：声称"新构象带来新伙伴"时，要同时测原构象对同一伙伴的结合，并检验伙伴本身能否诱导构象变化。

## 片段 6：开关在体内是否承担功能（明确，Results "Functional role for RfaH-CTD refolding"、"RfaH interacts with S10 in vivo"，Fig. 5，Fig. S5，Fig. S7）
- 观察：RfaH 在体外对转录的影响只有 3–4 倍，在体内却很大（Discussion "RfaH as a transcription antiterminator"）。
- 问题：差额是否来自 β 态 CTD 对翻译的作用？
- 竞争解释：(a) 修饰转录延伸复合物；(b) 排除 NusG；(c) 与 Rho 非生产性结合；(d) 增强翻译（作者列出的四种机制）。(c) 已由片段 5 排除。
- 作者的检查：用有/无核糖体结合位点（RBS）的 ops-lux 报告基因制造"翻译受损"的敏感背景，比较野生型、CTD 缺失、界面削弱突变 E48A、S10 界面突变 I146D（Fig. 5A、5B）；在天然 rfb 操纵子上用 qRT-PCR 测 wbbI（Fig. 5C，另加 L145D）；ChIP-chip 比较 rfb 与对照操纵子上 S10、NusG、NusB 信号（Fig. 5D–G）；甲醛交联质谱找 CTD 结合蛋白（Fig. S7）。
- 结果与含义：无 RBS 时野生型 RfaH 使荧光提高 1,000 倍，恢复到有 RBS 时的 18%；CTD 缺失使其降低 6 倍以上；E48A 比野生型高约 4 倍；I146D 只在无 RBS 时显著降低。wbbI：E48A 升高 1.6 倍，CTD 缺失、I146D、L145D 分别降低约 11、7、4 倍。rfb 上有 S10 信号而无 NusG、NusB；交联质谱中 S10 优先结合 CTD → 支持 (d)。
- 影响：功能论证链是"结构（片段 2）+ 体外结合（片段 5）+ 突变表型（本片段）"。转录中 CTD 的折叠从未被直接观测，结构与功能的连接依赖突变和同源类比。
- 所属阶段：synthesize（主）、interpret
- 合同效果：加强——功能相关性由突变表型推断，条目必须写明范围与认识状态（hypothesis），符合该句要求。原文（SYSTEM_PROMPT.md 第 40 行）："Each candidate claim states its scope, epistemic status, evidence references and limits."
- Agent 对应：结论边界——Atlas 条目的"功能相关性"字段要写成"由突变表型与同源界面推断（文献），未直接观测转录复合物中的 CTD 构象"；这些功能数据不在任何公开数据库中，Agent 只能引用论文数值。
- 可迁移的通用教训：把构象状态与功能挂钩时，要先制造一个功能对该状态敏感的背景，再用只改变该状态或其界面的突变测试，并在报告中区分"观测到的构象"与"由表型推断的构象"。

---

## 二、Cai et al. 2025（PNAS）

- 论文：Cai et al., "Unraveling structural transitions and kinetics along the fold-switching pathway of the RfaH C-terminal domain using exchange-based NMR", PNAS 122:e2506441122 (2025)，PMC12107155，CC BY-NC-ND。
- 问题：孤立 RfaH-CTD 在 β 卷主态之外还访问哪些状态，它们各自像什么、以什么速率互相转换，其中哪些位于折叠转换路径上。
- 作者主要结论：除主态 A（β 卷，约 76–77%）外还有四个状态：B（约 23%，τex 约 300 ms，大部分无序但含瞬时 α5* 螺旋与 β1*/β2* 发夹）、A′（约 0.35%，路径外，局部环区变化）、B′（约 0.3%，比 B 更无序）、B″（约 0.05%，螺旋性增加的中间态）；线性与分支两种五态模型在拟合上无法区分（Abstract；Concluding Remarks；Fig. 6）。
- 数据可得性：原始 ¹⁵N-CEST 与 CPMG 数据及 MATLAB 拟合程序在 Figshare 10.6084/m9.figshare.28629485.v1；A、B 两态骨架位移 BMRB 52718、52719（探针记录两条目含位移及 NOE、T1、T1ρ、RDC）；参照用全长 CTD 位移 BMRB 52348（Cai 2024）、PDB 2LCL、2OUG。正文打印的 "6C6C" 可能是笔误（Data Availability 段；`DATA_AVAILABILITY_PROBE.md` RfaH 行）。

## 片段 1：全长蛋白里看不到 α↔β 互变，只能研究孤立 CTD（明确，Introduction 第 1 段，Fig. 1，Concluding Remarks 首段与末句）
- 观察：游离全长 RfaH 中未观测到 CTD 在 α 发夹与 β 卷之间互变；全长蛋白只有一个低布居的毫秒激发态，涉及 N 端 β3/β4 发夹（Introduction，引文 4、10、12）。
- 问题：研究折叠转换路径时，用什么体系能看到转换中的状态？
- 竞争解释：(a) 在全长蛋白中寻找更低布居的 β 态；(b) 用孤立 CTD 作为替代体系，研究从 β 态出发的结构变化；前人 CEST 已在孤立 CTD 中看到慢交换到主要无序的次要态（引文 13）。
- 作者的检查：选择 (b)，并在结尾写明下一步要构建能与孤立 CTD 直接相互作用的可溶 N 端结构域，才能观察完整路径。
- 结果与含义：所有结论都限定在孤立 CTD；"位于折叠转换路径上"是由结构特征推断（B 同时含两端结构的元素），不是在全长蛋白中观测到的。
- 影响：定义了整篇论文的结论上限。
- 所属阶段：frame（主）、synthesize
- 合同效果：加强——样品是孤立 CTD 而非全长蛋白，这一 frame 决定了全文结论的上限。原文（SYSTEM_PROMPT.md 第 6 行）："frame: identify the sample, conditions, observables, inferential target and question."
- Agent 对应：结论边界——条目的构建体字段写"孤立 CTD"，不得写成全长 RfaH 的无配体状态；"路径中间态"标为作者推断。
- 可迁移的通用教训：在替代体系（截短、突变、孤立结构域）中看到的状态，只能在该体系的范围内报告，外推到天然体系必须单独取证。

## 片段 2：次要态峰弱且重叠，常规方法难以归属（明确，Results "Complete Backbone Chemical Shift Assignments of the Observable Minor State"，"Slow Conformational Exchange … by 15N-CEST" 末句；Experimental Procedures "Quantitative Kinetic Analysis" 第 2 段；SI Fig. S2–S5、S10）
- 观察：谱中有两组峰，主态 A 约 75%、次要态 B 约 25%；B 近似无规卷曲，位移分散小、峰弱、重叠。
- 问题：如何可靠地知道 B 的每个峰对应哪个残基？归属错误会传递到之后所有的 Δω 与结构解读。
- 竞争解释：(a) 直接用常规三维贯键实验归属 B；(b) 借助 A 与 B 之间的慢交换，把 A 的已知归属转移给 B。
- 作者的检查：用非均匀采样的三维 zz-exchange HNH 与 NNH 实验，通过 A-B 交换交叉峰归属 B 的酰胺 ¹H/¹⁵N；再用常规三维实验补齐 ¹³C 与 ¹H 骨架位移。之后做两条独立路径的核对：CEST 拟合得到的 ¹⁵N Δω(B−A) 与 zz-exchange 直接测得的 Δδ(B−A) 完全一致；CEST 拟合的布居与二维 HSQC 峰积分一致（SI Fig. S10）。
- 结果与含义：B 态归属与两态动力学参数相互印证，后续结构解读有可靠起点。
- 影响：之后的 B 态结构推断（片段 6、7）和暗态 Δω 符号确定（片段 8）都以此为基础。
- 所属阶段：inventory（主）、baseline
- 合同效果：细化——该句区分输入与派生量；本片段补充：同一参数既能直接测得又能拟合得到时，两者都登记并做一致性核对。原文（SYSTEM_PROMPT.md 第 7–8 行）："inventory: distinguish measured inputs, derived quantities, references, and missing controls."
- Agent 对应：可执行动作——由 BMRB 52718、52719 计算每个残基的 ¹⁵N Δδ(B−A)，与 Agent 自己从 Figshare 原始 CEST 拟合出的 Δω(B−A) 做逐残基相关；若 Figshare 文件保留未归一化的参比强度，再用 A、B 峰强比核对拟合布居（文件内容未核实）。所需数据公开。
- 可迁移的通用教训：一个参数能由两条独立测量路径得到时，先做一致性核对，再把它作为后续推断的输入。

## 片段 3：两态 CEST 模型能拟合 CEST，却预测不了 CPMG（明确，Results "Slow Conformational Exchange … by 15N-CEST" 与 "Fast Conformational Exchange Processes … 15N-CPMG" 前三段；SI Fig. S11–S14、S16）
- 观察：两态 Bloch–McConnell 模型全局拟合 CEST（饱和 600 ms，10、15、25 Hz）得到 τex 约 300 ms、kAB 约 0.8 s⁻¹、kBA 约 2.4 s⁻¹、pA 约 75%、pB 约 25%。
- 问题：两态模型是否足以描述全部交换？
- 竞争解释：(a) 只有 A↔B 一个过程；(b) A、B 各自还参与更快的交换。
- 作者的检查：两个独立迹象。其一，比较 R1ρ（2 kHz 自旋锁）与 CEST 拟合所得 ¹⁵N R2，后者在 A、B 两态的特定区段显著偏高，提示存在中间交换区的更快过程（SI Fig. S11）。其二，用 CEST 得到的速率与 Δω 直接模拟两态 CPMG 曲线（600、900 MHz），与实测对比。
- 结果与含义：模拟与多数实测 CPMG 不符，归一化 χ² 在 A 峰上为 22.6、在 B 峰上为 51.7 → A、B 各自还有更快的交换过程，(a) 被否定。约 300 ms 的交换在 17–1000 Hz 的 CPMG 窗口内几乎不产生弥散，因此 CPMG 弥散必然来自别的过程（推断）。
- 影响：打开了寻找隐藏态的问题（片段 4）。A↔B 很慢，于是可以把 A 峰和 B 峰的快过程分开建模。
- 所属阶段：baseline（主）、discriminate
- 合同效果：加强——CEST 模型预测 CPMG 失败正是"results conflict"，作者的处置是检查并修改模型。原文（SYSTEM_PROMPT.md 第 33–34 行）："When a tool fails, optimization is unconfirmed, coverage changes, or results conflict, inspect the affected evidence and review the discrepancy."
- Agent 对应：可执行动作——用 Figshare 原始 CEST 数据独立拟合两态模型，再用所得参数前向模拟 CPMG，计算每组峰的归一化 χ² 与逐残基残差；另比较 BMRB 52718/52719 中的 T1ρ 与 CEST 拟合 R2。需要多态 Bloch–McConnell 前向模拟工具；数据公开。
- 可迁移的通用教训：用一种实验拟合出的模型，要拿去预测另一种覆盖不同时间尺度的实验；预测失败说明模型缺少过程，而不是需要放宽误差。

## 片段 4：逐个加隐藏态，何时停止（明确，Results "Fast Conformational Exchange Processes …" 第 4–6 段；Experimental Procedures "Quantitative Kinetic Analysis"；Fig. 5B，Fig. 6；SI Fig. S14–S18）
- 观察：两态模型不够；A 峰与 B 峰都有 CPMG 弥散。
- 问题：要加几个隐藏态、接在哪里？什么时候停？
- 竞争解释：A 侧候选三态拓扑 A′↔A↔B、A↔I↔B、A↔B↔B′；B 侧先试 A↔B↔B′，不够再扩展为线性 A↔B↔B′↔B″ 或分支 A↔B、B↔B′、B↔B″。
- 作者的检查：利用 A↔B 慢交换，先分治：A 峰 CPMG + 全部 CEST 一起拟合，B 峰 CPMG + 全部 CEST 一起拟合；两侧分别从最简单模型起逐个加态，比较归一化 χ² 并看 CPMG 残差是否有系统偏差；最后把两侧合成五态模型，对全部数据全局拟合。速率为全局参数，Δω 与本征弛豫为逐残基参数，CEST 与 CPMG 权重为 1.0 与 0.5。
- 结果与含义：A 侧 A′↔A↔B 使 χ²(all) = 1.02、χ²(CPMG) = 1.00、χ²(CEST) = 1.03；A↔I↔B 与 A↔B↔B′ 的 χ²(CPMG) 为 2.9 与 14.8，有明显系统偏差。B 侧 A↔B↔B′ 的 χ²(all) = 1.24、χ²(CPMG) = 2.1，残差有系统偏差；加入 B″ 后 χ²(CPMG) 约 1.4、χ²(all) 约 1.1，系统偏差消失。五态全局拟合 χ²(all) = 0.98。停止规则是"能定量解释数据的最简单模型"：归一化 χ² 接近 1 且残差无系统偏差。
- 影响：状态数由这一过程确定。停止判据依赖误差估计与权重：CPMG 误差只由一个 νCPMG 点（500 Hz）的重复测得（Experimental Procedures "15N CPMG Relaxation Dispersion Measurements"），归一化 χ² 的绝对值随之变化。正文没有报告 F 检验、AIC 等信息准则（SI 未读，不能确认）。
- 所属阶段：discriminate（主）、baseline
- 合同效果：细化——提示只禁止预设状态数与拓扑，没有给出如何加态、何时停止；本片段提供"分治、逐个加态、比较所有接法、χ²≈1 且残差无系统偏差即停"的具体规则。原文（SYSTEM_PROMPT.md 第 2–3 行）："Do not presume a number of conformational states, topology, reference structure, or expected paper conclusion."
- Agent 对应：可执行动作——在 Figshare 原始数据上按"分治 → 逐个加态 → 全局合并"重做：每一步列出全部候选拓扑，报告各自的归一化 χ²、逐残基残差图和参数数目，再加信息准则或交叉验证作为作者之外的第二停止判据；对误差估计做敏感性检验（例如把误差放大或缩小一倍，看停止点是否改变）。需要能定义任意拓扑的 n 态 Bloch–McConnell 拟合器；数据公开。
- 可迁移的通用教训：加隐藏态要逐个加、每一步同时比较所有接法，停止判据要写明（拟合优度接近 1 且残差无系统偏差），并检查判据对误差估计的敏感性。

## 片段 5：线性与分支拓扑能否区分（明确，Results "Fast Conformational Exchange Processes …" 末段，Fig. 6 图注；"15N Backbone Chemical Shift Characterization of the Excited B′ and B″ States" 末段；SI Fig. S18–S20）
- 观察：五态线性模型与分支模型给出几乎相同的拟合：χ²(all) 均为 0.98，χ²(CPMG) 为 1.02 与 1.03，χ²(CEST) 为 0.95 与 0.96（分支/线性）。
- 问题：B″ 是经 B′ 到达，还是直接与 B 交换？
- 竞争解释：(a) 线性 A↔B↔B′↔B″；(b) 分支 B↔B′、B↔B″。
- 作者的检查：直接写明"拟合无法区分"；检查拓扑选择是否影响结构推断——两模型的 Δω(B′−B) 与 |Δω(B″−B)| 在误差内一致（SI Fig. S19），B↔B′ 寿命在两模型中均约 1.2–1.3 ms。然后用结构推断做倾向性判断：B′ 比 B 更无序、B″ 更有螺旋，若这些推断正确，分支模型"更可能"，B′ 为路径外状态。
- 结果与含义：拓扑在数据上未定；拓扑无关的量（Δω、布居）可以使用；分支模型的偏好是有条件的结构论证，不是拟合结果。
- 影响：路径图（Fig. 6）同时给出两种拓扑；"B′ 路径外、B″ 路径上"依赖片段 8 的结构推断。
- 所属阶段：discriminate（主）、interpret
- 合同效果：加强——线性与分支拓扑拟合不可分，应作为 unresolved alternatives 并列提交，而不是强行选一个。原文（SYSTEM_PROMPT.md 第 16–17 行）："synthesize: provide evidence-linked answers, limitations, unresolved alternatives and specific follow-up measurements; submit a candidate for human scientific review."
- Agent 对应：结论边界——Agent 在拟合无法区分两种拓扑时，必须并列报告两者，只把在两种拓扑下都稳定的量写进条目，拓扑偏好标为"基于结构推断的条件性判断"。执行部分并入片段 4 的拟合。
- 可迁移的通用教训：拟合优度相同的模型不能靠拟合选出；先找出不依赖模型选择的量，再单独标注任何基于外部论证的偏好。

## 片段 6：B 态像什么——三个参照与分区比较（明确，Results "Transient Secondary Structure within the Observable Minor B State" 与 "Backbone Amide RDCs and 15N-Relaxation Data"，Fig. 2、Fig. 3，SI Fig. S6、S7，Table S1）
- 观察：B 态位移分散小，整体像无规卷曲。
- 问题：B 是简单的解折叠态，还是含有两端构象（β 卷与全长中的 α 发夹）元素的中间态？
- 竞争解释：(a) 纯无规卷曲；(b) 局部保留 β 卷（A 态）元素；(c) 局部出现全长 α 态的螺旋；(b)(c) 可以同时成立。
- 作者的检查：三类参照——A 态（2LCL，BMRB 52718）、全长 RfaH 中的 CTD（2OUG，BMRB 52348）、由序列算得的无规卷曲位移（引文 25 的算法）。先看 ¹³Cα、¹³C′ 二级位移和 TALOS-N 二级结构指数（Fig. 2A、Fig. 3）。再做相关：¹⁵N Δδ(A−B) 分别对 Δδ(A−无规卷曲) 与 Δδ(A−全长) 回归，整体与分区（α5*、β1*/β2* 发夹、其余）各算一次（Fig. 2B）。最后用非位移的独立观测：B 态 RDC 与 ¹⁵N 弛豫（SI Fig. S7，Table S1）。
- 结果与含义：整体上 B 更接近无规卷曲（R = 0.98 对 0.88）。分区后结论反转：α5* 区对全长参照 Q = 0.27、对无规卷曲 Q = 0.45，β1*/β2* 发夹区对全长 Q = 0.98、对无规卷曲 Q = 0.24 → α5* 区像全长 α 态，发夹区接近无规卷曲。TALOS-N 给出 β1*（115–120）、β2*（127–132）、α5*（136–145），指数相对 A 态 β1、β2 降约 20% 与 80%，α5* 比全长 α5 晚一个残基开始、短约六个残基。B 态 RDC 约为 A 态的五分之一；R2 为 4.5±1.2 对 7.6±0.8 s⁻¹，NOE 为 0.32±0.16 对 0.70±0.06；扩展 model-free 给出 α5* 的 S²slow 约 0.7、其余约 0.45。占有率估计：α5* 可达约 40%，β1*/β2* 约 10–20%。作者写明 TALOS 指数是概率，不能直接当作占有率。
- 影响：B 被解释为"两端结构元素都部分出现的无序集合"，这是"B 可能位于路径上"的主要证据。
- 所属阶段：interpret（主）、discriminate
- 合同效果：细化——该句允许"局部或全局"之一；本片段表明整体与分区结论会反转，两种尺度都要算，且至少比较两类参照。原文（SYSTEM_PROMPT.md 第 13–15 行）："interpret: build claims at the appropriate local or global scope; compare plausible references on comparable data; explain discrepancies without treating resemblance as a unique mechanism or a solved structure."
- Agent 对应：可执行动作——用 BMRB 52718、52719、52348 与序列无规卷曲预测（POTENCI 或同类算法）复算二级位移，整体与分区各做一次相关，报告 R 和 Q；用 52719 中的 RDC、T1、NOE 做独立佐证。所需数据全部公开；52348 为不同构建体与条件，比较时注明。分区边界本身来自 TALOS 结果，复算时先由位移定区段，再做分区比较，避免用答案定分区（见文末封存提示）。
- 可迁移的通用教训：给无序或部分有序状态定性时至少比较两类参照，整体与分区各算一次；整体相关会掩盖局部结构，局部结论要用非位移观测（RDC、弛豫）佐证。

## 片段 7：CS-ROSETTA 模型的地位（明确，Results "CS-ROSETTA Modeling of the Minor B State"，Fig. 3B 图注，Fig. 4，Abstract）
- 观察：B 态有两个瞬时元素（α5* 与 β1*/β2* 发夹）。
- 问题：两个元素是否彼此接触、形成半紧凑结构？
- 竞争解释：(a) 两元素相互堆积；(b) 两元素各自独立、取向随机。
- 作者的检查：用 B 态全套骨架位移做 CS-ROSETTA，生成 10,000 个结构，取能量最低的 10 个，分别以 α5* 和发夹叠合（Fig. 4）。
- 结果与含义：α5* 在 10 个结构中全部保留；发夹在全部结构中形成，但整个 β 片层不总保留；发夹相对 α5* 的取向变化大，10 个中有 8 个落在约 50°–70° 的锥形范围内。作者在摘要中用"suggest … may interact"，图 3B 的单个结构注明"仅作示意"。
- 影响：(a) 以假设形式进入结论，没有距离类实验证据（如 NOE、PRE）支持。CS-ROSETTA 输出单一折叠结构，而输入位移是一个集合的布居平均值（α5* 约 40%、发夹约 10–20%），模型对应的是一个两元素同时完整形成的假想构象（推断，论文未讨论这一点）。
- 所属阶段：interpret（主）、synthesize
- 合同效果：加强——CS-ROSETTA 模型只是与位移相容的假设，不能当作"a solved structure"。原文（SYSTEM_PROMPT.md 第 13–15 行）："interpret: build claims at the appropriate local or global scope; compare plausible references on comparable data; explain discrepancies without treating resemblance as a unique mechanism or a solved structure."
- Agent 对应：结论边界——若工具可用，Agent 可以用 BMRB 52719 的位移跑 CS-ROSETTA 或同类位移驱动建模，但输出只能标为"与位移相容的假设结构"，不得作为状态结构进入条目，也不得据此给出三级接触结论；需要接触证据时，建议 PRE 或 NOE 实验。
- 可迁移的通用教训：由布居平均位移生成的结构模型只是假设；对部分有序的集合，模型中的元素完整度与相对取向都不是测量值。

## 片段 8：暗态 A′、B′、B″ 只有 ¹⁵N Δω，怎样推断结构（明确，Results "15N Backbone Chemical Shift Characterization of the Excited A′ State"、"… B′ and B″ States"，Fig. 7、Fig. 8；Experimental Procedures "Quantitative Kinetic Analysis" 末两段；SI Fig. S19–S22，Table S7）
- 观察：三个暗态布居都低于 1%，没有直接可见的峰；每个暗态只有逐残基 ¹⁵N Δω。
- 问题：只凭 ¹⁵N Δω 能说出暗态的什么结构特征？B″ 布居约 0.05%，数值可信吗？
- 竞争解释：A′ 是 β 卷的局部变化还是整体解折叠；B′ 更有序还是更无序；B″ 是向 α 态靠近还是别的构象；B″ 的 |Δω| 是否只是拟合初值造成的。
- 作者的检查：Δω 符号：A-B 的符号由 CEST 与归属确定，再用不同状态作参照（ω = 0）同时拟合重复数据，约束 Δω 闭合，从而确定其他暗态的符号；B″ 的符号因布居太小无法确定。B″ 稳健性：以 Δω(B″−B) 初值 0、+5、−5 ppm 各拟合一次（线性与分支均做，SI Fig. S21、S22，Table S7）。结构解读：A′ 看 Δω 大小和在 2LCL 上的位置；B′ 看 α5* 区 Δω 的符号（¹⁵N 向低场移动表示螺旋减少）；B″ 看 |Δω| 最大的区段与全长 α 态螺旋区的对应。
- 结果与含义：A′ 的 Δω 普遍不超过约 1 ppm，较大值集中在 β1/β2 环与 β4 → β 卷保留，局部环区变化。B′ 相对 B 的 Δω 除两个残基外都小于 1.0 ppm、无超过 2 ppm 者，α5* 区为正值 → 比 B 更接近无规卷曲。B″ 的 |Δω| 在三种初值下稳定；最大值在 134–150、其次在 115–121 → 作者推断 α5* 延长、β1* 区转为全长 α4 的 N 端螺旋。B″ 的"螺旋增加"只有无符号的 ¹⁵N 大小支持，作者没有把 |Δω| 与全长参照做定量比较。
- 影响：A′ 被定为路径外；B′、B″ 的结构推断又反过来支撑片段 5 中分支模型的偏好。B″ 的结构身份是全文证据最弱的一环。
- 所属阶段：interpret（主）、discriminate
- 合同效果：加强——B″ 的初值扫描是优化检查，Δω 符号无法确定属于 missingness，二者都应在解读数值前完成。原文（SYSTEM_PROMPT.md 第 9–10 行）："Check units, missingness, uncertainty, optimization and assumptions before interpreting its numbers."
- Agent 对应：可执行动作（重建，作者未做）——把拟合所得 |Δω(B″−B)| 与 |δ全长 − δB|（BMRB 52348 对 52719）以及 |δ无规卷曲 − δB| 逐残基相关，把 B′ 的带符号 Δω 与 δ无规卷曲 − δB 相关，报告 R 与 Q；对 B″ 另做初值扫描和误差重抽样，报告 |Δω| 的置信区间。所需数据公开（Figshare 原始数据经 Agent 自己拟合，BMRB 52348、52719，序列无规卷曲预测）。
- 可迁移的通用教训：只有单核、无符号 Δω 的低布居状态，结构解读要与参照态做定量比较并报告稳健性；定性的区段对应只能写成假设。

---

## 汇总

| 片段号 | 阶段（主段在前） | Agent 对应类型 | 需要的公开数据是否存在 |
|---|---|---|---|
| 2012-1 全长溶液结构核对 | frame、baseline | 可执行动作 | 部分：BMRB 52348 与 2OUG 公开（条件不同）；2012 弛豫未存档 |
| 2012-2 孤立 CTD 是 β 桶 | interpret、baseline | 可执行动作 | 是：2LCL、2JVV、2OUG、BMRB 52718 |
| 2012-3 E48S 界面突变 | discriminate、interpret | 仅为建议实验 | 否：HSQC 谱未存档 |
| 2012-4 TEV 切割连接区 | discriminate、synthesize | 仅为建议实验 | 否：HSQC 谱未存档 |
| 2012-5 伙伴结合依赖折叠 | discriminate、interpret | 仅为建议实验 | 否：滴定谱未存档 |
| 2012-6 体内功能 | synthesize、interpret | 结论边界 | 否：功能数据只在图中 |
| 2025-1 只能研究孤立 CTD | frame、synthesize | 结论边界 | 不需要 |
| 2025-2 次要态归属与交叉核对 | inventory、baseline | 可执行动作 | 是：BMRB 52718/52719、Figshare CEST；峰强比是否保留未核实 |
| 2025-3 两态预测不了 CPMG | baseline、discriminate | 可执行动作 | 是：Figshare CEST/CPMG；BMRB T1ρ |
| 2025-4 逐个加态与停止 | discriminate、baseline | 可执行动作 | 是：Figshare CEST/CPMG（需 n 态拟合器） |
| 2025-5 线性与分支不可分 | discriminate、interpret | 结论边界 | 不需要（执行并入 2025-4） |
| 2025-6 B 态三参照比较 | interpret、discriminate | 可执行动作 | 是：BMRB 52718/52719/52348、序列 |
| 2025-7 CS-ROSETTA 地位 | interpret、synthesize | 结论边界 | 是：BMRB 52719（建模工具是否可用另计） |
| 2025-8 暗态 ¹⁵N Δω 解读 | interpret、discriminate | 可执行动作 | 是：Figshare、BMRB 52348/52719 |

合计：可执行动作 7（2012 两条、2025 五条），仅为建议实验 3（均为 2012），结论边界 4（2012 一条、2025 三条）。

## 对 RfaH 2025 作为开发案例的提示

应对解题会话封存的量（答案）：
- A↔B 的布居、τex、kAB、kBA：这是 baseline 阶段要由原始 CEST 自己拟合出的第一组数，提前看到就无法检验拟合流程。
- 状态数、各候选拓扑的归一化 χ²、五态结构以及"线性与分支不可分"：这是 discriminate 阶段的核心判断，泄露后"逐个加态"只剩形式。
- 暗态 A′、B′、B″ 的布居、寿命和逐残基 Δω：只能由拟合得到，是拟合正确与否的核对标准。
- B 态的结构解读，包括 α5*、β1*/β2* 的区段边界、占有率估计、R 与 Q 值、TALOS 与 CS-ROSETTA 结果：这是 interpret 阶段的答案；区段边界尤其要封存，否则分区比较会变成用答案定分区。
- Figshare 中的 MATLAB 拟合程序及其模型定义、初值、权重：程序编码了五态拓扑和作者的建模选择，只放行原始数据与实验参数。
- 论文正文、SI，以及 BMRB 条目中指向本文的标题、引文与状态描述字段：这些字段会直接透露状态解读，放行 BMRB 位移时需去掉。
- 正文内部有两处不一致，核对答案时以 Results 为准并注明：A′ 的 τex 在摘要中为约 1 ms、在 Results 中为约 500 µs；pA 在两态 CEST 拟合中约 75%、在五态结果中约 76–77%。

可以放行的先验参照：
- PDB 2LCL（孤立 CTD β 态结构，2012）与 2OUG（全长 α 态，2007）：发表早于本文，是作者动手前已有的两端结构。
- BMRB 52348（全长 RfaH 中 CTD 的位移，Cai 2024）：作者用的外部参照，早于本文发表，不含本文结果。
- 序列与无规卷曲位移预测：只由序列计算，不含任何本文结论。
- BMRB 52718、52719 的位移、RDC 与弛豫数值（去掉标题与引文字段后）：B 态是可直接观测的状态，这些是测量输入，相当于 KRAS 案例中"已归属好的数据"。
- Figshare 原始 CEST/CPMG 数据与采集参数（饱和场强、饱和时间、谱仪频率、νCPMG 列表）和样品条件（25 °C，pH 6.5，约 1.0 mM）：解题所需的测量本身。
- 前人对孤立 CTD 的 CEST 结果（慢交换到主要无序的次要态，2025 引文 13）与全长蛋白激发态结果（引文 12）：作者开题时已知的文献，放行后解题会话与作者站在同一起点。
