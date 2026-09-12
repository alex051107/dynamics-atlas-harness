# 单分子FRET怎么被过度解读 FRET-based dynamic structural biology: challenges, perspectives and an appeal for open-science practices

来源，Lerner, Barth, Hendrix等40余位作者，eLife 2021;10:e60416，DOI 10.7554/eLife.60416。全文已读，locator对应正文小节标题、Figure/Table编号，页码按eLife PDF页脚（共69页）标注。

## §0 一页讲清这篇论文

这是一篇由smFRET领域主要实验室联署的立场论文（position paper），不是原创研究（Abstract, p.2）。论文问的问题是，smFRET要成为可靠的定量结构生物学工具，从样品制备到结构建模的整条流程里哪些步骤缺乏共识、容易出错，社区该如何统一操作和报告。作者的做法是沿着smFRET实验的标准工作流逐段总结现状、列出陷阱、给出"软性建议"（soft recommendations），并引用已完成和进行中的多实验室盲测作为证据（Introduction节, p.4-6）。

论文自己的答案是，smFRET原理可靠，但实验室之间在γ校正因子的确定方式、动态子群与静态子群的区分标准、染料光谱性质的报告习惯上差异很大，是当前重现性不足的主要来源（Epilogue节, p.40）。最脆弱的假设有两处。一是κ2=2/3各向同性平均近似，蒙特卡洛模拟显示这一简化会带来RDA误差，但论文也说目前没有实验数据明显与该模型不符（Dye models节, p.24）。二是态内动力学与态间跃迁的区分标准，论文直接写"这一区分仍在争议中，高度依赖能垒的定义和所用的实验模态"（Detection and characterization of intra-state dynamics节, p.19）。

对Dynamics Atlas的用处是，这篇文章按工作流节点提供了一份系统的smFRET失败模式清单和报告项清单，可以直接映射为规则表的准入和伪影检查项，并且明确区分了"社区已有共识、可写成硬性判据"和"仍在讨论、只能当建议"两类条目（Epilogue节, p.40）。它不能替本项目决定的是，具体某个已发表的smFRET子群该判定为一个态还是毫秒尺度互换的平均，因为论文自己承认这个区分没有统一判据，需要该数据集自己的对照实验支持，不能靠本文的通用标准代劳。

需要注意的适用范围是，这篇论文正文讨论的是有机染料标记的溶液或表面固定化smFRET，细胞内smFRET和荧光蛋白标记体系的特殊伪影只在Future of smFRET节（p.36，细胞内部分见p.38）作为尚未成熟的展望方向提及，不是本文正文陷阱清单覆盖的现有共识部分。项目在套用本文判据前，需要先确认待判断的数据集是否落在论文讨论的适用范围之内。

## §1 为什么会有这篇论文

论文引用的直接证据是Hellenkamp等2018年组织的20实验室盲测，用同一批dsDNA标准品测smFRET效率，各实验室报告的平均效率之间的差异ΔE在0.02到0.05之间，具体数值取决于样品（Introduction节, p.6，引Hellenkamp et al. 2018a）。论文称这个结果"令人惊讶地高度一致"，但随即指出一致性"还可以进一步提高"，因为不同实验室采用的数据校正方法不完全相同（Introduction节, p.6）。更尖锐的证据来自尚未发表、由Cordes牵头的蛋白质FRET挑战（Gebhardt et al., in preparation），论文明确写道，γ因子确定的不确定性"是目前不同实验室之间smFRET直方图差异的最大来源之一"（Determining the g factor in confocal mode节, p.20）。这篇论文诞生于一个已经被盲测量化过的、实验室间不一致的具体失败场景。

## §2 论文的组织方式

这是综述加倡议的混合体（Abstract称"position paper", p.2）。组织线索是smFRET实验的标准工作流顺序，仪器选择、样品制备（染料、偶联、固定化、光谱表征）、分子鉴定与验证、构象动力学检测（慢动力学、快动力学、态内动力学）、FRET效率的定义与绝对值确定、染料到距离的转换（R0、染料模型）、结构建模、用模拟做流程验证，最后单列"开放科学"一节讲文件格式、软件、数据仓库和社区行动（State of the art of single-molecule FRET experiments节起, p.6）。每个工作流节点固定按"现状综述、常见问题、推荐做法、待解决的科学问题"四项展开（p.6）。陷阱分散在各工作流小节里，没有单独的总表。

## §3 陷阱逐条讲

| 陷阱 | 定义/机制 | 论文例子或数字 | 为什么容易犯 | 推荐检查 |
|---|---|---|---|---|
| 静态与动态子群不可靠区分 | 态内动力学（single energy minimum内的快速涨落）和态间跃迁（跨越大于kBT能垒的转变）在一维FRET直方图上都表现为分布展宽，区分依赖能垒定义和所用模态 | 论文直接写这一区分"仍在争议中"（Detection and characterization of intra-state dynamics节, p.19） | 一维FRET直方图无法单独区分两种机制，看峰宽窄容易把互换的平均误读成单一构象 | 用FRET效率-寿命二维图（Figure 4A-B, p.17）辅助判断，作者建议建立多算法交叉验证工作流而不是只信一种方法（Faster dynamics节, p.18） |
| 时间平均（dynamic averaging）机制 | 若构象互换速率快于采样时间（confocal小于约0.1 ms，TIRF小于约10 ms），观测到的时间序列或直方图只是按各态占比加权的平均FRET值 | Detecting dynamics节明确给出两个模态的时间阈值（p.16） | 单看一次直方图的位置和宽度，容易把两态快速互换的平均误读成单一居间构象 | 用burst variance analysis（BVA）、2CDE、FRET分布宽度与shot noise极限比较、时间窗分析确认动力学是否存在（Detecting dynamics节, p.16列出五类方法） |
| 校正因子与R0系统误差 | 绝对E需要α（供体串扰）、δ（受体直接激发）、γ（探测效率与量子产率失配）三个校正因子，R0依赖φF、光谱重叠积分、κ2、折射率四项，且对光谱位移呈λ⁴依赖 | γ因子被明确列为"smFRET实验不确定性的最大来源"（Determining absolute FRET efficiencies from fluorescence intensities节, p.20）；折射率取1.4时最大R0误差约4%（Refractive index节, p.22，引Clegg 1992） | γ在动态平均的样品里更难确定，"需要做不同假设"；折射率长期被忽视（p.20，p.22） | 用两个以上E不同但γ相同的物种做ALEX/PIE联合标定；报告γ的确定方法和折射率取值（Determining the g factor in confocal mode节, p.20） |
| 染料与连接臂 | 染料经10-15个原子的柔性连接臂偶联，量子产率φF随标记位点和构象变化，R0本身不是常数 | Cy3B量子产率在dsDNA不同标记位点从0.19变到0.97，同一染料对Cy3B-ATTO647N的R0因此在54.8至65.9 Å之间波动（Fluorescence quantum yield节, p.22） | 常把R0当作查表得到的固定常数用，忽略标记位点依赖性 | 对每个标记位点独立测φF；用nsALEX/PIE或MFD直接探测φF变化（p.22） |
| 光物理伪影 | 光闪烁、光漂白、各向异性变化、PIFE、光饱和、染料间相互作用、染料与生物分子表面堆叠或光诱导电子转移都能产生假FRET子群 | Cy3碱基堆叠到DNA末端导致κ2偏离2/3的例子（Dye transition dipole orientation factor节, p.23，引Ranjit 2009; Wranne 2017; Iqbal 2008） | 这些伪影在FRET直方图上和真实构象子群表现相似，简单阈值无法区分 | 单标记对照测寿命和各向异性；用ALEX/PIE、MFD或E分布宽度识别染料伪影；换用另一对染料或调换标记位点做交叉验证（Spectroscopic characterization节, p.13） |
| 跨实验室一致性 | 同一样品在不同实验室、不同校正流程下得到的平均E存在系统性差异 | 20实验室dsDNA盲测ΔE为0.02-0.05（Introduction节, p.6）；蛋白质FRET挑战把γ因子列为差异主因（p.20） | 各实验室γ和折射率取值传统不同，此前没有统一报告规范 | 用统一dsDNA标准品做日常标定；报告完整校正参数供他人复算（p.6，p.20） |
| 报告与开放数据要求 | 原始光子数据、校正参数、分析代码、结构模型的不确定性缺乏统一报告规范 | Figure 8（p.32）给出A-E五类必报字段；Table 1（p.28-30）列出约20款开源分析软件；Table 2（p.33）列出6个可引用数据仓库及容量费用 | 论文指出目前没有标准文件格式，导致实验室内部长期数据都难以复用（Standard file format节, p.28） | 用Photon-HDF5等格式存原始数据；按Figure 8五类信息报告，实验者信息、样品与FRET细节、仪器与采集参数、分析协议与拟合质量、最终模型与不确定性（p.32） |

## §4 论文提出的判据和报告清单

可以直接进规则表的判据，有明确阈值或明确机制。第一，时间平均阈值，confocal模态互换快于约0.1 ms、TIRF模态快于约10 ms时，观测值是占比加权平均而非单态（Detecting dynamics节, p.16）。第二，静态假设适用区间，E小于0.8且染料不与蛋白表面相互作用时，染料动力学导致的距离偏差通常可忽略（Dye models节, p.24）。第三，折射率取值与误差，nim取1.4时最大R0误差约4%（Refractive index节, p.22）。第四，不同染料模型对同一E给出的RDA分布偏差约5%（Dye models节, p.24）。第五，γ因子确定的前提条件，ALEX/PIE方法要求样品至少含两个E不同但γ相同的物种，否则该方法本身失效（Determining the g factor in confocal mode节, p.20）。

只是建议，没有量化阈值，不宜直接写成硬性规则。论文多处用"we recommend"要求报告burst搜索参数、标记效率、光稳定剂种类（p.14、p.20-21、p.28-29），这些是报告完整性要求，不是可判定对错的准入条件。论文建议交叉验证不同标记对或调换标记位点防止假阳性（p.13-14），缺乏统一的通过/不通过标准。开放科学、文件格式、数据仓库选择（Open science节, p.27）是社区治理倡议，Epilogue明确说这些建议应被当作建设性意见而非规程（p.40）。

## §5 证据支撑到哪里、没覆盖什么

论文的实证支撑主要来自两项多实验室研究，已发表的Hellenkamp等2018 dsDNA 20实验室盲测（Observed，有具体ΔE数值，p.6）和尚未发表的Cordes牵头蛋白质FRET挑战（Observed但未经同行评议，只引用其in preparation阶段结论，p.6、p.20）。除此之外，κ2各向同性平均、时间平均、染料模型选择的5%偏差这类机制性论述，来自作者们各自实验室此前的方法学论文，属于领域共识水平的Inference，不是本文的新证据。

论文自己承认的最脆弱假设有两处。一是κ2=2/3动态旋转-静态平移近似，蒙特卡洛模拟显示这一简化可能导致RDA误差，但论文也说目前没有主要实验数据与该模型明显不符（Dye models节, p.24-25），也就是该假设未被证伪但也未经充分测试覆盖所有体系。二是态内动力学与态间跃迁的区分标准，论文明确称其仍在争议中（p.19），没有给出任何可操作的判定阈值。

论文没有覆盖的部分包括NMR、cryoEM等其他技术的伪影分析，只在Introduction中作为背景简单提及（p.3），以及跨技术比较（如smFRET距离与MD模拟距离）的具体统计检验方法，论文只给出概念性框架，即类比X射线晶体学Rfree的χ²ᵣ质量估计（Structural modeling节, p.26-27），未给出跨resource比较的操作细则。

## §6 映射到Dynamics Atlas

以下每条标注论文事实、分析推断或项目提议。

1. 拆题与准入，判断一个smFRET子群是一个态还是毫秒尺度互换的平均，落在Dynamics Atlas的UNORDERED_ENSEMBLE还是ORDERED_TRAJECTORY分支准入点上（论文事实，时间阈值confocal小于0.1ms、TIRF小于10ms，p.16）。态内态间区分本身仍有争议是论文自己的陈述（p.19），项目在此处只能设"存在争议，需人工复核"的软规则，不能设硬判据（项目提议）。
2. 选定义与伪影，V1规则表中raw/apparent/corrected efficiency三级区分、R0与染料和accessible volume校正、burst-variance analysis检测动力学这几条FRET规则，与本文Determining absolute FRET efficiencies、Inter-dye distances、Detecting dynamics三节内容一致（论文事实，p.19-24），可视为已获文献支持。
3. 采样与处理，本文关于burst search参数、用户偏倚、TIRF固定化伪影的检查（Molecule identification and validation节, p.14-15）对应Dynamics Atlas的采样代表性判断点，V1规则表目前未见对应条目（分析推断，是V1没有覆盖的部分）。
4. 跨来源比较，本文强调smFRET距离是FRET-averaged apparent distance，不等于两个染料质心间的真实距离（Inter-dye distances节, Equation 5, p.21），这是判断FRET距离与MD模拟距离是否为同一量的核心机制依据，直接支持V1里dye linker和accessible volume校正的规则（论文事实）。本文没有专门讨论smFRET距离和NMR平均距离是否可比，这部分需要项目自行补充（项目提议）。
5. 结论措辞，本文对κ2和态区分两处不确定性的坦率承认（p.19、p.24-25）支持claim ceiling设计中必须允许ABSTAIN的原则，与项目文档已有的claim discipline一致（论文事实）。
6. V1曾把FRET规则误用于NMR问题这一教训，本文没有涉及NMR方法学细节，说明问题出在V1规则表适用范围（scope）标注缺失，把FRET专属的γ、R0、accessible volume规则套到NMR数据上，不是本文内容有误（项目提议）。

## §7 可以直接进规则表的候选

1. 触发条件，smFRET子群报告为单一构象态但未给出BVA、2CDE或E-寿命二维图等动力学检测结果。防止把时间平均的多态混合误判为单一静态构象。来源，Detecting dynamics节, p.16。
2. 触发条件，报告了绝对FRET效率或距离但未说明γ因子确定方法（confocal的ALEX/PIE双物种法或TIRF的光漂白法）。防止把未经γ校正或校正方式不明的E当作可比的绝对值使用。来源，Determining the g factor in confocal/TIRF mode节, p.20，阈值为ALEX/PIE方法要求至少两个不同E但相同γ的物种。
3. 触发条件，R0取自单一文献查表值，未标注具体标记位点。防止忽略φF的位点依赖性导致R0系统性偏差，Cy3B案例R0波动54.8-65.9 Å。来源，Fluorescence quantum yield节, p.22。
4. 触发条件，距离解释基于E大于0.8区间的数据但未做染料模型敏感性分析。防止染料自身动力学偏差被计入结构距离。来源，Dye models节, p.24，阈值E小于0.8时偏差通常可忽略，不同染料模型间RDA偏差约5%。
5. 触发条件，报告了稀有构象子群但未说明筛选百分比和阳性判据。防止把选择算法或光物理伪影产生的稀有事件误判为生物学稀有态。来源，User bias节, p.15。
6. 触发条件，跨实验室或跨论文比较smFRET效率时未核实是否使用同一dsDNA标准品或等效日常校准。防止把实验室间系统偏差（历史观测值ΔE 0.02-0.05）误读为真实生物学差异。来源，Introduction节, p.6，引Hellenkamp et al. 2018a。
