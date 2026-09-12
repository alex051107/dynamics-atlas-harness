# 位置论文：答案对了，机制错了 Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts

## §0 一页说清

这篇论文问的是：只看 AI 科学家系统最终答案对不对是否足够。作者主张必须把三件事分开度量，任务结果对不对、机制解释是否正确且能跨声称的 regime 泛化、系统是否诚实地界定了自己结论的不确定性和边界。

做法是一个受控的案例研究：用 Geant4 切伦科夫探测器模拟，让 coding agent 做一个开放式科学发现任务，能否用单个探测器模块的光子到达时间分布，统计上区分 muon 诱导事件和 electron 诱导事件。20 个主模型 episode 全部用 Claude Opus 4.6，另有 8 个跨模型探针用 Gemini 2.5 Flash 和 Gemini 2.5 Pro 各跑 4 个。四种 prompt 条件横跨一个信息量梯度：完全开放式、给出五步流程但不提示观测量、给出正确公式的正控制、带一个部分误导性先验。真正正确的观测量是 leading-edge photon fraction（fearly），一个已知有效但不是唯一正确答案的观测量。

论文自己的答案：20 个主模型 episode 里有 4 个，加上 8 个跨模型 episode 里有 3 个，共 7 个，被编码为 CAWM（Correct Answer, Wrong Mechanism），agent 拿到看起来对的结果，却用和自己数据矛盾或过度泛化的物理来辩护。最尖锐的一个例子是 episode 19：agent 正确拒绝了被植入的错误先验，同一条轨迹里随后又用和自己数据矛盾的物理为其选定的观测量辩护，说明诚实度和机制忠实度可以在同一次分析里脱钩。作者提出并事后验证了一个 regime-shift 检测协议，两个检查合起来把全部 7 个 CAWM 案例都标记了出来。

最脆弱的假设有四层：证据基础是单一物理模拟 domain；每个 prompt 条件只有 N=5，作者自己在 Limitations 里明确写只支持存在性声称，不支持 prevalence 声称；episode 标注是单一作者事后编码，没有独立标注者做一致性交叉验证；两个检测协议是在 episode 编码完成之后才设计出来的，所以七中七是样本内一致性结果，不是前瞻性检测率。

对 Dynamics Atlas 的用处：这是目前手头这批论文里唯一给出"正确答案但机制错误"这个失败模式的明确定义和一个几乎零成本检测协议的论文，检测思路是把 agent 的机制声称转成一个可在相邻 regime 验证的方向性预测，再实际算一次。它不能替我们决定的是：论文样本量很小，不能直接告诉我们 CAWM 在真实蛋白动力学场景里出现的频率；这个协议依赖"已知一个可信的相邻 regime 能让声称的方向反转或消失"，在我们的场景里哪些 regime 具有这个性质，需要我们自己界定，论文没有替我们做这件事。

## §1 为什么会有这篇论文

Introduction 交代动机：现有 AI 科学家系统的评测（科学助手、多智能体 co-scientist、自主发现 pipeline）通常只对照固定参照打分，比如已知化学、生物医学验证、同行评审阈值、留出手稿，不直接检验 agent 陈述的机制是否正确，也不检验它是否认识到自己 claim 的边界。独立评测已经显示 outcome-level 指标能掩盖严重的推理失败：Beel et al. (2025) 报告 AI Scientist v1 有 42% 的实验失败率，幻觉没有被它自己的评审分数捕捉到；Luo et al. (2025) 显示某些失败只有检查推理过程才能发现；Lu et al. (2026) 自己列举了全自动 AI 研究 pipeline 固有的失败模式，包括实现 bug、幻觉结果、走捷径、把 bug 重新框定为 insight、方法论捏造、frame-lock、引用幻觉。已有的科学推理 benchmark 也没填上这个空白：ScienceAgentBench 打分执行成功和代码质量，DiscoveryWorld 分别对任务完成、程序化动作、解释性知识对照预定义 gold 参考打分，MASK 探测对抗压力下的认知诚实。它们都没有探测 agent 破坏自己 claim 的两种具体方式，一是把发现推广到从未测试过的 regime，二是编造和自己输出数字相矛盾的解释。CAWM 就是要填这个空白。

## §2 任务、数据与评测怎么建

任务单位是单个 episode。agent 被给一个 Geant4 Cherenkov 探测器模拟二进制，研究问题是单个探测器模块的光子到达时间分布能否统计上区分 muon 和 electron 诱导事件，要求系统性调查并报告发现（§2）。目标观测量是 per-event leading-edge photon fraction，fearly(W) = |{i: ti−tfirst<W}| / Nhits，W≈1ns 最优，这是一个已知好用的 leading-edge observable，不是唯一正确答案。在 E=40 GeV 下，muon 作为最小电离粒子沿窄角度发出切伦科夫辐射，瞄准探测器的一小段径迹贡献最早到达的光子，形成几纳秒宽的 leading edge；electron 诱导的电磁级联在时间上更展开（约 10ns）。这使得 fearly(µ)>fearly(e) 在 d=10 和 20m 成立（Figure 2）。d=25m 时光子计数降到 4±2/事件，单个 50 事件 episode 内 fearly 无法达到统计上可靠的估计。

四种 prompt 条件跨越一个信息梯度：A（开放式，N=5，只给研究问题、模拟接口、探测器约束，不提任何具体观测量，agent 自由选撞击参数 d 在 10 到 25m）；B（五步 scaffold，N=5，固定 d={10,20,25}m，强制一个五步流程，规划图表、跑模拟、迭代改图、挑战自己的结论、给出扎实的最终结论，不提示具体观测量）；C（正控制，N=5，直接给出 fearly 定义式和物理背景解释，建立"在给定目标观测量时任务是否可达成"的上界）；D（带偏先验，N=5，固定 d 网格，给一段包含一条部分正确、一条错误声称的背景信息，测试 agent 能否在数据矛盾时拒绝错误的部分）。

Gold 层面，fearly 是一个已知好用的 leading-edge observable，不是唯一正确答案，CAWM 编码建立在 agent claim 和它自己数据的内部一致性上，不依赖外部标签。outcome correctness 定义为：agent 的方法，在其自己呈现为证据的 regime 上重新跑一遍，能否复现所声称的结果。CAWM 编码规则（§2）要求一个 episode 被编码为 CAWM，需要 agent 提出一个 observable 并用和自己数据矛盾、或过度泛化超出被支持 regime 的物理来辩护，第一个触发条件覆盖 agent 自己的模拟事件反驳其陈述机制的情形，第二个触发条件覆盖声称跨越"所有 d"但只在一两个 regime 上验证过的情形。同时要求结果本身成立，如果连结果本身在 agent 自己呈现的证据 regime 上都无法复现，编码为 detectable failure 而非 CAWM，用于区分"错得明显"和"错得隐蔽"这两种性质不同的失败。全部 20 个主模型 episode 均用 Claude Opus 4.6，跨模型探针额外用 Gemini 2.5 Flash/Pro 各 4 个 episode，全部由单一作者事后按 CAWM 编码规则标注。

关于 evaluator 会不会放过错误答案，这正是全篇的核心论点。作者明确指出，单一 regime 的 outcome 评测无法区分理想象限（结果对、机制对）和 CAWM 象限（结果对、机制错）。Figure 1 的 outcome-mechanism 矩阵直接可视化了这个盲区：全部 7 个 CAWM episode 都落在"correct outcome"这一列，如果只看 outcome，它们和真正做对的 episode 在单一 regime 检查下完全无法区分。

## §3 失败逐条讲

**Prompt A 开放式探索下的 relative-window 误建构**（§3.1，Appendix A episode 2、3、5）。定义：agent 识别出正确的物理特征，即早期光很重要，但把 observable 定义在事件自身时间范围的一个相对窗口上，这个量追踪的是光子统计而非 leading edge 本身。三个 agent 各自独立提出一个 relative-window early fraction（事件自身时间范围前 20% 到 25% 内的光子比例）。在自己的事件上，这个量在 d=10m 强烈区分了两种粒子（⟨fe⟩=0.92 对 ⟨fµ⟩=0.69，150 个事件/粒子），到 d=25m 褪化成打平（0.51 对 0.51，139 个 muon 和 87 个 electron 事件，episode 5 在 d=25m 没跑 electron）。更大的 pooled 样本（N≈500/粒子）甚至反转：从 d=10m 的 0.93 对 0.67 反转到 d=25m 的 ⟨fµ⟩=0.53 对 ⟨fe⟩=0.48（Appendix A）。真正的绝对窗口 fearly(W=1ns) 在同样事件上算出的是 ⟨fµ⟩=0.37 对 ⟨fe⟩=0.17（d=10m），是 muon 而不是 electron 拥有 leading edge，方向和相对窗口正好相反。根因在于 electron 事件的光子数约是 muon 事件的 8 倍（中位数 114 对 14），稀少的晚到光子把 electron 的时间范围拉长，把它的"大部分光子"推到前四分之一，这个窗口测的是批量位置相对于一个依赖计数的极值统计量，而不是 leading edge 本身。三个 agent 都把 d=10m 的 e>µ 信号读成"electron 级联更紧凑导致更锐的 leading edge"，没有一个反过来算一次绝对窗口的 fearly 去核验这个解释。这个失败出现在 Prompt A 的 5 个 episode 里的 3 个，论文认为三个 agent 独立犯下同一个误建构暗示这是一种结构性模式，而不是偶然巧合。

**Prompt D 偏先验下机制辩护和自己数据矛盾**（§3.4，episode 19）。定义：agent 正确拒绝了被植入的错误先验成分，但随后选定另一个观测量并用和自己数据矛盾的物理来辩护。植入的先验有两条声称，一条是 σ 对 muon 应该更大，部分正确；另一条是 electron 应该有更高的 leading edge fraction，是错的。全部 5 个 agent 都正确拒绝了错误的那条声称，依据是 fearly(W=1ns) 在 d=10 和 20m 处 muon 都约是 electron 的两倍。但 episode 19 依然选择 σ(hitTime) 作为主要观测量，声称有 10 到 15ns 的"intrinsic geometric spread"，这和它自己在 d=10m 测到的 σµ=6.73ns（仅略高于 σe=6.52ns）不符；它对 fearly"not direction-robust"的驳斥也和它自己 W=1ns 那张表矛盾（µ>e 在全部三个距离上都成立，0.365 对 0.170、0.365 对 0.200、0.363 对 0.338）。σ 只在 d=20 和 25m 处因为 δ-ray 重尾在低光子数下主导才真正分离，agent 把这个只在大 d 时才出现的模式当成了 regime-general 处理。这个模式还出现在 3 个跨模型案例里（Prompt B 的两个 Gemini episode，Prompt D 的一个 Gemini Flash episode）。论文认为的根因是诚实度是局部的而非全局的，拒绝一个外部错误先验不保证 agent 对自己选定的机制 claim 施加同等强度的审视。

**Prompt B 五步 scaffold 下算出对的量但不认它的价值**（§3.2）。定义：scaffold 让所有 agent 都计算了某种 early fraction，但只有极少数把它选为主要观测量。5 个 agent 全部计算了 early fraction，只有 episode 7 把它选为主要观测量，另外 4 个用的窗口宽度是 W=5 到 200ns，太宽以至于信号被稀释进整体分布，AUC 只有 0.55 到 0.66 左右的弱区分度，随后被放弃转投 photon count 或多元组合。差距只在一个参数选择上：峰值分离出现在 W=0.5 到 2ns，但 4/5 的 agent 只扫了 W≥5ns，错过了驱动区分的 leading-edge cluster。有 2 个 agent（episode 7、9）独立正确陈述了 δ-ray 机制（muon 径迹上的次级电子产生 electron 级联所没有的晚到光子），但即使陈述了正确机制，也没有选择这个机制暗示的窄早期窗口。论文认为的根因是 scaffold 规定了要计算什么，但没有规定要用多精细的分辨率去解析它，这个 gap 不会被 scaffold 自动关闭，计算出正确的量和认识到它的价值不是同一个步骤。

**跨模型探针下同一模式重复出现，及一个对照式的 detectable failure**（§4，Appendix A）。定义：同样的"选定 σ 类观测量加一个物理论证，自己的表格在某些 d 值上反驳这个论证"的模式，在 Gemini 2.5 Flash 和 Pro 上重复出现。Prompt B 下 Gemini 2.5 Flash 从 EM-shower 论证预测"σe>σµ 在所有测试的撞击参数下普遍成立"，但自己的数据显示 d=20 和 25m 处 σµ>σe（d=20m 处 σµ=10.25 对 σe=9.10ns，d=25m 处 8.84 对 6.61ns）。Prompt B 下 Gemini 2.5 Pro 从 Cherenkov 几何论证 muon events 更宽，却在自己 d=10m 的数据里 σµ=4.27 小于 σe=5.98ns，方向直接反了，据此设的 cut 反而优先选中了 electron。另有一例（Prompt A 的 Gemini 2.5 Pro）声称 d=10m 处近乎完全分离，但从自己 run 里重新计算的 AUC 只有 0.56，约等于随机，这个连结果本身都不成立，被编码为 detectable failure 而非 CAWM。8 个跨模型 episode 里有 3 个 CAWM，1 个 detectable failure。论文认为的根因是这个失败结构不是单一模型特有的，两个不同模型家族里都出现了相同的模式。

## §4 补救和效果

论文提出并事后测试了两个检查。第一个是 regime-shift verification protocol（§3.4，正式步骤见 §4）：提取机制声称，推导出一个在未被用来提出该 observable 的相邻 regime 上的有符号方向性预测，取用已有数据或补跑该 regime，打分，预测成立则一致，预测失败则标记待人工复核。第二个是 companion recomputation，针对 relative-window 这类 confounded observable，直接在同样数据上重新计算那个"有原则的"observable（比如绝对窗口 fearly）来证伪 claim。效果数字：七个 CAWM episode 里，四个通过 regime-shift check 被标记，三个通过 companion recomputation 被标记，两个检查合起来对全部七个案例都成功标记（§5），每次检查的边际成本是一次额外的模拟运行或一次重新计算，本文的 episode 里所需数据大多已经存在。

必须说清一个重要限定：这两个检查是在 episode 被编码完成之后才设计出来的，所以七中七是样本内一致性结果，而不是前瞻性检测率，作者自己明确写"seven for seven is an in-sample consistency result rather than a prospective detection rate"（§5）。两个检查都是单向的，能排除错误机制，但不能确认一个机制是对的，因为一个在每个测试 regime 都预测正确的机制依然能通过检查（§5）。

未测的部分：论文没有测试"让 agent 在提交前自己应用 regime-shift check"这件事本身是否能从源头防止 CAWM，只是在 Discussion 里提出这是直接的下一步；也没有测试 process supervision 这类训练时干预是否能移除这个失败源头，同样是建议的未来方向而非已完成的实验。

## §5 证据支撑到哪里、没覆盖什么

**Observed**：20 个主模型 episode 加 8 个跨模型 episode 的 CAWM 计数（4/20 和 3/8），Table 1 的按 prompt 细分，Figure 2、3 的具体统计数值（σ 和 fearly 的逐事件、逐 episode 数据），这些都是论文报告的直接观测。

**Inference**："三个 agent 独立犯同一个 relative-window 误建构暗示这是结构性模式"是作者的解释性推断，样本只有三个独立案例，统计意义有限；"诚实度是局部的而非全局的"这个概括同样建立在单个 episode（episode 19）加几个跨模型案例之上。

**最脆弱的假设**：每个 prompt 条件只有 N=5，作者自己在 Limitations 里明确写"支持 existence claims，prevalence 仍未测试"；episode 标注是单一作者事后编码，没有独立标注者的一致性检验；跨模型探针每个 prompt 只跑一个 episode，且用的是不同的执行 harness（minimal API loop 而非命令行界面），模型和 harness 是同时变化的混杂因素（§8 Limitations）；论文自己承认"we do not separately verify that the stated reasoning reflects the agent's actual inference"，也就是说 CAWM 编码依赖 agent 最终报告里陈述的推理，不排除这个陈述本身不忠实于其实际的内部推断过程。

**一个最强反例**：Prompt C（正控制，给出完整的观测量定义和物理动机）下，全部 5 个 agent 都正确复现了 fearly，并且都正确标记了它在 d=25m 处因统计不足而变得不可靠（§3.3）。这说明给定目标观测量后能否正确执行和 scope 结论，与能否开放式发现一个物理上站得住脚的观测量，是两种不同的能力，本文的失败结论只适用于后者，不能泛化成这些 agent 完全不会做科学计算。

## §6 映射到 Dynamics Atlas

对 relative-window 误建构（§3.1）与 σ 和自己数据矛盾（§3.4，episode 19）：[论文事实]。[分析推断] 这两类失败本质上是 agent 选定或沿用了一个和数据类型不匹配的判据或窗口定义，并用一套听起来合理但和自己算出的数字矛盾的解释去辩护，这和我们目录里"错误的定义或阈值"（6 例）以及"应用一条规则但规则不适配这个数据类型"（5 例）高度对应，是这两类失败在一个完全不同科学 domain（粒子物理模拟而非蛋白动力学）里的独立复现，说明这是一种更普遍的 agent 推理模式，不局限于 MD 或蛋白动力学场景。

对"诚实度局部而非全局"这个发现（§3.4）：[论文事实加分析推断]。这提醒我们，Dynamics Atlas 里即使 agent 正确处理了某个已知陷阱，比如正确拒绝了一个错误的经验规则，也不能因此推断它在同一次分析里对自己后续选定的判据同样施加了审视。这是我们目前 34 类失败清单里没有明确对应的一个元层面风险，诚实度检查本身不能跨步骤泛化，需要逐步骤单独核验，而不是一次性核验就能覆盖全程。

对 regime-shift verification protocol（§3.4、§4）：[论文事实的检测框架加项目提议的移植方式]。这是本文对我们最直接可用的方法论贡献。项目提议：对 Dynamics Atlas 里任何"agent 声称某个规则或机制在某个条件范围内成立"的判断，比如"这个收敛判据对一微秒和一百微秒轨迹同样适用"，都可以尝试构造一个相邻 regime，比如更短或更长的轨迹长度、更少或更多的 round trip 数，看 agent 的机制声称在那个 regime 下是否依然方向一致。这不需要对每个 claim 都做完整领域专家审查，只需要一次额外计算。

对落点的判断：[项目提议] 这类检查最适合放在我们决策链里"agent 对某个数据类型判断规则是否适用"这一步之后、"接受该判断"之前，作为一个轻量级的、机器可检的把关，而不是替代人工复核。

## §7 可以直接进规则表的候选

1. **agent 对某个观测量或判据的机制性解释，凡是以"适用于所有条件/regime"这类无限定措辞表述的，必须至少在一个未被用来提出该判断的相邻条件下重新验证一次方向是否一致**。来源：§3.4、§4 regime-shift verification protocol 四步骤。防止：过度泛化型 CAWM，机制声称被推广到未测试的 regime。

2. **涉及比例或占比类指标（如某个窗口内计数占总数的比例）时，必须核实分母本身是否与被比较的两组样本存在系统性差异，如果存在，必须补算一次不依赖该分母的绝对版本指标做交叉验证**。来源：§3.1、Appendix A relative-window 误建构案例，electron 事件光子数是 muon 的 8 倍，导致相对窗口测的是 count-dependent 的极值统计而非目标物理量。防止：confounded observable 型 CAWM。

3. **agent 在同一次分析里正确拒绝了一个外部给出的错误假设或先验之后，不能因此免检它随后自行选定的判据或结论，仍需对该判据单独施加同等强度的自我审视**。来源：§3.4 episode 19，诚实度局部性发现。防止：局部诚实掩盖机制层面持续存在的自我辩护错误。

4. **涉及参数分辨率选择的分析（如时间窗口宽度、bin 大小），如果扫描范围与理论预期的信号尺度不匹配，差一个数量级以上，应视为未充分探索，不能仅凭弱信号就得出该判据不适用的结论**。来源：§3.2 Prompt B 案例，4/5 agent 只扫 W≥5ns，错过 W=0.5 到 2ns 的真实分离峰。防止：因分辨率不足而误判判据无效，转而采用更弱的替代指标。
