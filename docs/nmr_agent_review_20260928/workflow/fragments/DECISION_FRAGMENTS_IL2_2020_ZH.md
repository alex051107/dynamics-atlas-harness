# IL-2 2020：作者从数据到结论的决策片段

论文：De Paula VS et al., "Interleukin-2 druggability is modulated by global conformational transitions controlled by a helical capping switch", PNAS 117(13):7183–7192 (2020), DOI 10.1073/pnas.2000419117。全文为本地 PMC HTML（`literature/workflow_papers_20260920/metadata/IL2_2020.html`，无页码，定位写"小节标题 + 图号"）；SI PDF 未读，SI 内容只按正文引用描述。"明确"= 论文写出的步骤；"重建"= 我根据证据依赖推出、论文没写先后的步骤。
问题：游离小鼠 IL-2（mIL-2）是否自发采样一个稀有构象；这个构象由什么结构特征控制；能否用突变或小分子改变它，从而改变抗体结合。
作者主要结论：游离 mIL-2 在 μs–ms 尺度上以一次全局协同转变在 92% "closed/uncapped" 与约 8% "open/capped" 之间交换（kex = 1,000 ± 72 s⁻¹，pE = 8.0 ± 0.4%，Results「Free mIL-2 Samples a Global Transition…」，Fig. 2E），开关是 AB loop 上 R52 的 C-capping 氢键网络；R52A 淬灭交换并使 JES6-1 亲和力下降约三个数量级，Ro 26-4550 结合也压低交换（Fig. 3、Fig. 5、Discussion 与 Fig. 6）。
数据可得性：BMRB 27969（游离 WT，骨架酰胺 + MILV 甲基）、27970（+JES6-1，仅 ILV proS 甲基）、27971（+IL-2Rα，仅 ILV proS 甲基）、27974（R52A，MILV 甲基）只有化学位移；CPMG/CEST 曲线、逐残基 kex/pE/|Δω|（SI Table S1）、NOE 距离（Table S2）、ITC 表（Table S3）只在 SI PDF；PDB 1M47、1M48、2B5I（均为人 IL-2）和 4YQX（鼠 IL-2 + JES6-1）公开；没有 MD 或原始弛豫数据存档（`DATA_AVAILABILITY_PROBE.md` IL-2 行）。

每个片段按这个顺序写：观察 → 问题 → 竞争解释 → 作者的检查 → 结果与含义 → 影响。"合同效果"引用的是 Codex 系统提示（`docs/science_workflow/SYSTEM_PROMPT.md`）原句。

## 片段 1：酰胺谱大面积消失，换成甲基读数（明确，Results「Long-Range Effects…」与「Free mIL-2 Samples a Global Transition…」；SI Fig. S1、Fig. S6A）
- 观察：游离 mIL-2 的 ¹H-¹⁵N TROSY 谱质量很差，33% 的酰胺峰完全展宽消失，AB loop 的酰胺信号缺失。
- 问题：主读数缺了三分之一，无法按常规骨架探针研究动力学；先要知道信号为什么消失。
- 竞争解释：μs–ms 构象交换导致的展宽；聚集或寡聚使整体弛豫变快；样品或谱图质量问题。
- 作者的检查：用 SEC-MALS 确认样品在 NMR 条件下严格单体（SI Fig. S1）；把展宽解释为 AB loop 在多个骨架构象间中间时标交换；改用 MILV 甲基（全氘、立体专一 proS 标记，60 个甲基归属）做 CPMG 和 CEST。
- 结果与含义：单体结果排除了聚集这一解释，展宽被当作交换的线索而不是数据损失。之后 R52A 突变体的 TROSY 谱显著改善（SI Fig. S6A），回头支持"展宽来自交换"。
- 影响：全文的动力学证据都来自甲基；骨架层面的交换没有被定量。
- 所属阶段：inventory, frame
- 合同效果：细化 —— 系统提示把缺失当作覆盖率记录，本片段补充：排除样品原因后，成片、成区的信号缺失本身是交换的正向线索，应记为观察而非仅记为覆盖损失；受影响原句 "Track coverage from the available input, including exclusions."
- Agent 对应：可执行动作 —— 从 BMRB 27969（公开）读出骨架酰胺归属，按序列列出未归属位置，检查是否集中在 AB loop；27974 只有甲基，无法从数据库复核 R52A 的酰胺改善。未归属只能算"交换展宽候选区"，脯氨酸、重叠或归属策略也会造成缺失；条目内容本次未联网核验。
- 可迁移的通用教训：主读数大面积缺失时，先排除聚集等样品原因，再把缺失的分布当作交换线索，并换一种受交换影响小的探针继续测。

## 片段 2：一个全局过程，还是几个过程（明确，Results「Free mIL-2 Samples a Global Transition…」；Fig. 2A–C；SI Fig. S3A、S4、S5，Table S1）
- 观察：B、C、D 螺旋上多个甲基有 CPMG 弥散，CEST 在相同残基上出现第二个凹陷。60 个甲基中只有 20 个弥散曲线足够好，其余因信噪比低或重叠被排除。
- 问题：这些分布在全蛋白的交换是一个协同过程，还是几个独立的局部过程；CPMG 与 CEST 看到的是不是同一个过程。
- 竞争解释：单一全局两态交换；速率相近的多个局部过程；两种方法各自看到不同过程；温度不同导致位移不同而非过程不同。
- 作者的检查：20 个甲基的 CPMG 做全局两态拟合（kex = 1,000 ± 72 s⁻¹，pE = 8.0 ± 0.4%）；CPMG（25 °C）和 CEST（10 °C，B1 = 16.2 Hz）各自独立拟合出 |Δω|，再做线性相关（Fig. 2C）。
- 结果与含义：多数甲基的 |Δω| 相关良好，作者据此认为两种方法报告相似的交换过程；两个离群点（L133δ1、L80δ2）被解释为主、次态位移的温度依赖，这一解释没有被实验检验。正文未报告逐残基拟合与全局拟合的比较，也没有比较多过程模型；两态拓扑是拟合假设，不是被选出来的模型。
- 影响："全局协同"在这一步只得到相关性层面的支持，真正的区分证据在片段 5（R52A 同时淬灭所有位点）。
- 所属阶段：baseline, discriminate
- 合同效果：加强 —— 作者直接用全局两态模型，状态数和"单一过程"没有被当作待比较的选择，正对应提示中禁止预设的内容；受影响原句 "Do not presume a number of conformational states, topology, reference structure, or expected paper conclusion."
- Agent 对应：结论边界 —— 逐残基 kex/pE/|Δω| 只在 SI PDF（未结构化），数据库环境无法重拟合。Agent 报告时应写明：20/60 是按数据质量事后筛选的覆盖；两态是模型条件下的参数；两个离群点的温度解释未检验，列为未解决分歧。若人工从 SI Table S1 提取数值，才可复算相关性和离群点。
- 可迁移的通用教训：不同条件下两种方法给出的参数只能在相关性层面合并，离群点的"条件差异"解释没有被检验时，应作为未解决分歧保留。

## 片段 3：主态是哪种 AB loop 构象（明确，Results「Free mIL-2 Samples a Global Transition…」末段；Fig. 2F–G；SI Table S2）
- 观察：已有晶体结构给出两种 AB loop 构象：JES6-1 结合态里 AB loop 刚性旋转约 38°（Y45–T55）；人 IL-2 游离态和受体结合态里 AB loop 贴着疏水核。
- 问题：溶液中 92% 的主态更像哪一种；不确定主态，就无法说次态"是什么"。
- 竞争解释：主态为 "closed"（像游离人 IL-2 / IL-2Rα 结合态）；主态为 "open"（像 JES6-1 结合态）。
- 作者的检查：3D CM-CMHM SOFAST NOESY 测甲基 NOE，与三个参照比较：以人 IL-2 游离结构 1M47 为模板的 Rosetta 同源模型、鼠 IL-2/JES6-1 共晶 4YQX、以人 IL-2/IL-2Rα 复合物 2B5I 为模板的模型。
- 结果与含义：M42、M53、L54、L80、V83、V129 之间出现多条短程 NOE（5 Å 上限），符合 closed；在 4YQX 中 M53、L54 的甲基离核心甲基约 13 Å，超过 10 Å 的 NOE 检测极限（SI Table S2）。主态被定为 closed。
- 影响：NOE 由 92% 的主态主导，只能确定主态，对 8% 次态的构象没有直接约束；次态的身份只能靠后续推断（片段 4、5）。
- 所属阶段：interpret, discriminate
- 合同效果：细化 —— 作者确实比较了多个参照，但其中两个是以人 IL-2 为模板的未公开同源模型；"可比数据"需要跨物种编号映射，并注明参照是模型而非实测结构；受影响原句 "compare plausible references on comparable data"（interpret 条目中的分句）。
- Agent 对应：可执行动作 —— 从 PDB 1M47、2B5I、4YQX（公开）计算上述六个残基甲基碳之间的距离，判断每个参照是否满足 5 Å / 10 Å 阈值。人/鼠编号正文只给了三个对应（hIL-2 M39、V69、L72 = mIL-2 M53、V83、L86，Results「Skewing the Dynamic Landscape…」），其余要先做序列比对。实测 NOE 只在 SI Table S2，未结构化公开；作者的鼠 IL-2 同源模型未存档。
- 可迁移的通用教训：用实测短程距离约束在多个候选参照结构中选出主态，这一步只定主态，不能顺带确定次态。

## 片段 4：次态无法从位移直接建结构，借已知结合态提出假设（明确；排除顺序为重建。Results「A Conserved Hydrogen Bond Network…」；Fig. 1D–E、2D、3A–D；Discussion 第二段）
- 观察：发生交换的甲基（Fig. 2D）与 JES6-1、IL-2Rα 结合时化学位移扰动大的甲基（Fig. 1D–E，CSP > 0.05 ppm）有明显重叠，包括 AB loop、L80δ2、L86δ2 以及核心的 L133δ2、I137δ1。
- 问题：8% 的次态长什么样。作者明确说甲基位移解释存在歧义，无法据此从头建模次态结构。
- 竞争解释：次态像 JES6-1 结合态（open/capped）；次态像 IL-2Rα 结合态；次态是两者之外的构象；重叠只说明结合与交换都经过同一条 AB loop—核心网络，不说明次态像哪个结合态。
- 作者的检查：定性比较残基重叠；在 4YQX 中寻找游离结构没有的特征，发现 R52 胍基与 M42、Y45、R46、L48 的骨架羰基形成 C-capping 氢键，而游离人 IL-2（1M47）中 R52 朝向溶剂；比较直系同源物中该序列基序的保守性（Fig. 3D）。据此提出假设：次态具有 JES6-1 结合态的 C-capping 特征。
- 结果与含义：重叠同时出现在两个结合态上，本身不能在 JES6-1 样与 IL-2Rα 样之间做选择。选择 JES6-1 样依赖两个前提（重建）：主态已被 NOE 定为 closed，且 closed 与 IL-2Rα 结合态相似，所以次态应是另一种；C-capping 是 4YQX 独有、可被单点突变破坏的特征。这一步产出的是可检验假设，不是次态结构。
- 影响：为片段 5 的 R52A 扰动提供了目标；整篇的次态"结构"始终是类比加扰动推断，没有坐标。
- 所属阶段：interpret, discriminate
- 合同效果：细化 —— 提示要求不预设参照结构；作者的做法说明参照结构可以被选定，但必须写成带名字的假设并配一个能推翻它的扰动检验；受影响原句 "Do not presume a number of conformational states, topology, reference structure, or expected paper conclusion."
- Agent 对应：可执行动作 —— (a) 用 BMRB 27969 对 27970、27971（公开，复合物只有 ILV proS 甲基）逐甲基计算 CSP，自行声明加权方式（正文未给公式），先核对三个条目的温度和缓冲条件；(b) 分别列出 JES6-1 特有、IL-2Rα 特有和共有的扰动位点，与正文点名的大 |Δω| 甲基（L48δ1、L54δ1、L80δ2、V83γ1、L84δ1、I101δ1、V130γ2、L133δ1、I137δ1）对照，检查重叠能否区分两种结合态；(c) 在 4YQX（公开）中计算 R52 侧链与上述骨架羰基的氢键距离。定量的 |Δω| 对 CSP 比较需要 SI Table S1，未结构化公开；CPMG |Δω| 无符号，结合态 CSP 还混有直接接触效应。
- 可迁移的通用教训：次态无法直接建结构时，从已知结构中找一个独有且可被扰动破坏的特征写成假设，不要把残基重叠当作身份鉴定。

## 片段 5：用 R52A 突变区分"单一协同过程"与"局部运动"（明确，Results「A Conserved Hydrogen Bond Network…」；Fig. 3E–F；SI Fig. S3B、S5、S6）
- 观察：假设已经提出（片段 4），但全局拟合本身不能证明交换是一个协同过程。
- 问题：破坏 C-capping 后，交换会不会在所有位点同时消失。
- 竞争解释：R52A 去掉次态，所有位点一起淬灭（单一协同过程）；只淬灭 AB loop 附近，远端不变（多个局部过程）；R52A 改变了基态折叠，使 |Δω| 变小或速率移出检测窗口，而非去掉次态。
- 作者的检查：作者事先写明预测：若交换是协同过程，破坏 open 态的突变应以一致方式改变交换参数。在相同条件下重测 R52A 的 CPMG 和 CEST。
- 结果与含义：WT 中所有有交换的甲基在 R52A 中弥散都被压低；全局拟合的 χ² 面没有明确极小，kex 和布居无法估计；CEST 第二凹陷在 I101δ1 勉强可见，在 L70δ2、I143δ1、L133δ1、L133δ2 消失，作者据此认为次态布居低于检测限。远端与近端同时淬灭，是反对"多个局部过程"的主要证据。定性淬灭本身不能区分"布居下降"、"速率移出窗口"和"|Δω| 变小"三种情况，作者选择了第一种。
- 影响："R52A 使次态布居低于检测限"只能作定性表述，没有 R52A 的布居数值。
- 所属阶段：discriminate, interpret
- 合同效果：细化 —— 拟合失败（χ² 无极小）在这里不是工具故障，而是扰动成功的表现；提示要求检查未确认的优化，本片段补充：应把"无法拟合"与"曲线变平、凹陷消失"一起解读，并把结论降为定性；受影响原句 "When a tool fails, optimization is unconfirmed, coverage changes, or results conflict, inspect the affected evidence and review the discrepancy."
- Agent 对应：可执行动作 —— 弥散和 CEST 实验无法重做；Agent 可用 BMRB 27974 对 27969（均公开，均含 MILV 甲基）逐甲基算 R52A−WT 位移差，检查大差异是否局限在 AB loop 附近（折叠保持）还是遍布全蛋白（基态改变），以此评估第三种竞争解释。正文未报告这一比较。
- 可迁移的通用教训：用一个只破坏候选次态特征的扰动检验"单一协同过程"时，要同时确认扰动没有改变基态折叠，并且定性淬灭不能换算成定量布居。

## 片段 6：亲和力下降三个数量级，能不能全归因于构象平衡（明确，Results「A Conserved Hydrogen Bond Network…」ITC 与 STAT5 两段；Fig. 3A、3G–H；SI Table S3）
- 观察：WT 以 2 nM 结合 JES6-1，结合主要由熵驱动（293 K 下 ΔH = +12.7 kcal·mol⁻¹，−TΔS = −24.3 kcal·mol⁻¹）；R52A 亲和力低约三个数量级，原因是结合熵更不利。
- 问题：亲和力损失来自"open 态更难形成"，还是 R52 本身就是抗体界面上的接触残基。
- 竞争解释：构象平衡移向 closed，需要付出额外的构象自由能；R52 与 JES6-1 的 E60 在 4YQX 中形成盐桥，突变直接丢失界面相互作用。
- 作者的检查：没有设计能拆开两者的实验；正文明确写 1,000 倍下降反映两部分的合并效应。细胞实验中，JES6-1 使 WT 的 STAT5 信号降低约 5 倍，而 R52A 的 EC50 与是否加 JES6-1 无关；R52A 经 IL-2Rα 的信号与 WT 相近（Fig. 3H 图注）。
- 结果与含义：功能与 ITC 一致，但动力学对亲和力的贡献份额无法从本文数据分出。另有措辞问题：ITC 段落说 closed 态"competent for binding"，而 Fig. 6 和 Discussion 把 JES6-1 的高亲和结合归给 open 态；按全文模型应以 Fig. 6 为准，但抽取论断时要标出这处不一致。
- 影响：可以说"R52A 使 JES6-1 亲和力下降约三个数量级，并伴随交换淬灭"，不能说"交换淬灭导致了三个数量级的下降"。人 IL-2 的相关性由序列与结构保守性论证，本文未测。
- 所属阶段：interpret, synthesize
- 合同效果：加强 —— 该论断必须写明范围（合并效应）、认识状态和限制，否则会被读成动力学单独解释亲和力；受影响原句 "Each candidate claim states its scope, epistemic status, evidence references and limits."
- Agent 对应：结论边界 —— ITC 数值表只在 SI Table S3；Agent 可以从 4YQX（公开）确认 R52 位于抗体界面，作为"不能单独归因"的依据，但不能重新分配两部分的贡献。报告中把亲和力变化标为"突变的合并效应"，并标出原文 closed/open 措辞不一致。
- 可迁移的通用教训：扰动位点同时位于结合界面时，亲和力变化不能单独归因于构象平衡的移动。

## 片段 7：用化学上无关的小分子复现同一效应（明确，Results「Skewing the Dynamic Landscape of mIL-2 by Ligand Binding」；Fig. 5A–D；SI Fig. S7）
- 观察：R52A 的结论只来自一个突变，突变特有的副作用无法排除。
- 问题：另一种不改序列的扰动，若同样偏向 closed，会不会同样压低全局交换。
- 竞争解释：Ro 26-4550 偏好 closed 态，使平衡移动、全局交换下降；只在结合口袋附近产生局部效应；这个人 IL-2 抑制剂与鼠 IL-2 结合太弱，看不到效应。
- 作者的检查：作者写明假设：优先结合 closed 构象的小分子应产生与 R52A 类似的效应。HMQC 滴定（1:4 摩尔比，快交换）；V129γ2、L133δ2 线形分析（TITAN）得 Kd = 39.4 ± 5.5 µM；在"饱和结合"、相同蛋白浓度下重测 CPMG（600 MHz，25 °C）。
- 结果与含义：最大 CSP 在 AB loop 附近（L48δ1、L54δ1、L60δ1），但延伸到距 1M48 中抑制剂位点 12 Å 以外的核心甲基；CPMG 弥散在全蛋白被明显压低，与 R52A 方向一致。仍有残余交换，作者解释为结合态下 open 态仍可被采样。残余交换也可能来自未完全饱和，这一点取决于实际蛋白与配体浓度，正文未给出。
- 影响：两种化学上无关的扰动给出同向结果，加强"单一可调平衡"的解释。Discussion 与 Fig. 6 把"亲和力下降三个数量级"写成突变或小分子都会导致，但本文只对 R52A 测了 JES6-1 亲和力，小分子对抗体结合的影响未测。
- 所属阶段：discriminate, interpret
- 合同效果：细化 —— "饱和结合"是解释残余信号前必须核实的假设；提示要求在解释数字前检查假设，本片段补充：扰动实验要先算清占有率，再解释残余效应；受影响原句 "Check units, missingness, uncertainty, optimization and assumptions before interpreting its numbers."
- Agent 对应：可执行动作 —— (a) 用 Kd = 39.4 µM 和 SI 中给出的 CPMG 样品蛋白、配体浓度，按单位点结合二次方程计算结合分数，判断残余交换能否由游离蛋白解释；浓度只在 SI PDF，未结构化公开。(b) 在 PDB 1M48（公开）中计算抑制剂到各甲基残基的距离，复核">12 Å"，编号映射同片段 3。(c) 在报告中把"小分子降低抗体亲和力"标为未测。
- 可迁移的通用教训：用化学上无关的第二种扰动复现同一效应时，先算清结合占有率再解释残余信号，并且只把实际测过的读数推广到第二种扰动。

## 片段 8：环—核心耦合的传递路径是算出来的假设（明确，Results「Allosteric Communication in mIL-2 through a Remodeling of Side Chain Rotamers」；Fig. 4A–C；SI Fig. S8–S9）
- 观察：结合引起的远端 CSP（片段 4）和全局协同交换（片段 2、5）都说明 AB loop 与疏水核耦合，但 NMR 只给出一个全局 kex，给不出耦合的空间次序。
- 问题：AB loop 的构象变化通过什么结构路径传到核心。
- 竞争解释：沿特定残基的侧链重排逐级传递；整体螺旋"呼吸"式的集体运动，没有特定次序；两个静态骨架上可允许旋转异构体集合的差异，本身并不对应真实的传递。
- 作者的检查：以 closed 与 open 两个固定骨架为输入，用 Rosetta 基于可满足性的方法枚举相容的侧链旋转异构体对；把允许数差 > 3 的埋藏残基（L28、L39、M42、L48、M53、F58、F132、L133、W136、F139）连成一条从 AB loop 经内核到 A、D 螺旋 N 端的路径，并与 CPMG Rex 较大的甲基叠加（Fig. 4C）。
- 结果与含义：作者自己称这条路径为"plausible"和"putative"。它来自两个静态结构的比较，不是动力学模拟，路径上的先后顺序也没有被测量。
- 影响：机理层面的"变构路径"只到假设级别；本文把核心突变作为改造 IL-2 功能的机会提出（Discussion 末段），但没有做。
- 所属阶段：interpret, synthesize
- 合同效果：加强 —— 路径应作为未解决的替代解释与具体的后续测量一起提交，而不是写进结论；受影响原句 "provide evidence-linked answers, limitations, unresolved alternatives and specific follow-up measurements; submit a candidate for human scientific review."
- Agent 对应：仅为建议实验 —— 在 D 螺旋 V129–F139 这段路径上选一个远离 AB loop、旋转异构体集合变化大的埋藏残基做保守突变，另选一个不在路径上的埋藏残基作对照；两者都测甲基 CPMG（看 AB loop 与核心甲基的交换是否改变）和 JES6-1 ITC。路径残基突变应改变 AB loop 的交换和抗体亲和力，对照突变不应改变。作者的鼠 IL-2 同源模型未存档，Agent 也无法在数据库环境中复现枚举。
- 可迁移的通用教训：从两个静态结构的比较中得到的传递路径只是假设，需要用路径上与路径外的成对扰动来检验。

## 汇总

| 片段 | 阶段（主段在前） | Agent 对应类型 | 需要的公开数据是否存在 |
|---|---|---|---|
| 1 酰胺谱消失、换甲基读数 | inventory, frame | 可执行动作 | 是（BMRB 27969 位移表；内容未联网核验） |
| 2 一个全局过程还是几个 | baseline, discriminate | 结论边界 | 否（逐残基参数只在 SI PDF） |
| 3 主态是哪种构象 | interpret, discriminate | 可执行动作 | 部分（PDB 1M47/2B5I/4YQX 是；NOE 只在 SI Table S2；同源模型未存档） |
| 4 次态身份的假设 | interpret, discriminate | 可执行动作 | 部分（BMRB 27969/27970/27971 与 4YQX 是；逐残基 \|Δω\| 只在 SI） |
| 5 R52A 区分协同与局部 | discriminate, interpret | 可执行动作 | 是（BMRB 27974、27969）；弥散与 CEST 曲线否 |
| 6 亲和力下降的归因 | interpret, synthesize | 结论边界 | 部分（4YQX 是；ITC 表只在 SI Table S3） |
| 7 小分子复现效应 | discriminate, interpret | 可执行动作 | 部分（PDB 1M48 是；样品浓度只在 SI） |
| 8 变构传递路径 | interpret, synthesize | 仅为建议实验 | 不适用（需要新湿实验） |
