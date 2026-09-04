# 用论文数据检验 Rules Table 的二十个科学问题

本轮筛出 20 个有具体数据和计算目标的候选，来自 10 篇原始研究。它们检验构象变化、独立观测预测、模型判别和证据支持，替换旧覆盖检查里的字段声明问题。本文给出选题理由与拟议计算路线；20 题尚未执行。

其中 17 题研究蛋白或蛋白脂质体系，2 题用 DNA FRET 标准体系检查定量测量方法，1 题用论文的 YaaA 模拟数据作错误折叠负对照。T4 溶菌酶的两篇论文共享部分原始实验数据，Q09、Q10、Q11 不视为独立实验。全部来自已暴露的开发文献，不能作为盲测集。

当前唯一可路由的科学计算 Operator 绑定原有 HSP90 数据包。本轮 20 题中，已有精确 Operator 完整覆盖的题目为 0；Q01 有相关既有分析组件，其余问题缺少完整的注册计算路线。这是接入范围的发现，不能计成 20 题科学失败。各题的数据网址也只表示已定位的入口；本轮没有完整下载或解析任何新题的数值输入。

每张题目卡的论文目标是待对照的作者结论。计算方法、补充检查和比较量是本轮设计，不能读成已经复现的结果。原始数据、作者处理后数据、作者最终结果和模拟数据分别记账。只重新画作者结果表，不算从数据复算。

## 建议先做的数据验收

| 顺序 | 问题 | 为什么先看 | 取得数据后的第一个计算目标 |
|---|---|---|---|
| 1 | Q09，T4 溶菌酶第三态 | Zenodo 已列出 2.9 MB 原始衰减小包，科学目标明确 | 核准 IRF、DA/DOnly 与变体映射后，对同一衰减比较两态和三态拟合 |
| 2 | Q01，HSP90 初态与转变 | 本地已有同论文分析，可先核对数据同源性 | 检查逐轨迹状态指标与初态分组，区分可复用诊断和本题尚缺的计算 |
| 3 | Q05，nanodisc 多技术整合 | 作者仓库列出散射、BME与MD目录 | 取得数值观测和逐构象输入后，从统一权重基线重算拟合及重加权效果 |
| 下一顺位 | Q15，HiSiaP 闭合与染料冲突 | 同一体系有冲突测量和换染料对照，最能检验补充计算是否有科学作用 | 优先验收 Source Data 数值表，再决定是否获取 GB 级原始档案 |

这些是获取和核对输入的顺序，尚不是可立即执行的三条注册路线。先检查输入和方法，再将缺少的具体能力交给后续最小接入工作；不能用无关的 HSP90 Operator 代跑 FRET 或 SAXS。

## 二十题总览

| 编号 | 要检验的结果 | 需要的实际计算 | 类型 |
|---|---|---|---|
| Q01 | HSP90 开闭初态与亚稳性 | 轨迹对齐、RMSD、NOE超限、按轨迹统计 | 体系问题 |
| Q02 | HSP90 交换态占比与速率 | CPMG 强度预处理与全局交换模型拟合 | 体系问题 |
| Q03 | Sic1 集合对独立 FRET 的预测 | SAXS/PRE集合处理与FRET前向预测 | 体系问题 |
| Q04 | Sic1 突变与磷酸化引起的伸展 | FRET分布拟合与干预效应误差传播 | 体系问题 |
| Q05 | nanodisc 椭圆集合解释多技术观测 | BME重加权、SAXS/NOE前向计算与形状统计 | 体系问题 |
| Q06 | nanodisc 边缘与中心的膜性质 | 膜区域映射、厚度及脂质序参量 | 体系问题 |
| Q07 | NUS 两条件下尺寸变化解耦 | SAXS/FRET重拟合与聚合物模型比较 | 体系问题 |
| Q08 | NUS 集合形状与内部距离变化 | 加权回转张量及内部距离标度 | 体系问题 |
| Q09 | T4 溶菌酶是否需要第三构象态 | IRF卷积TCSPC全局拟合与模型比较 | 体系问题 |
| Q10 | T4 溶菌酶功能突变的状态富集 | FRET/FCS/HPLC多技术条件效应分析 | 体系问题 |
| Q11 | T4 溶菌酶两种短寿命结构判别 | 可及体积FRET预测与结构模型评分 | 体系问题 |
| Q12 | YaaA 错误折叠的模拟负对照 | 模拟FRET留出评分与结构RMSD | 模拟负对照 |
| Q13 | DNA 原始光子到校正距离 | 光子burst处理、FRET校正与距离转换 | DNA测量对照 |
| Q14 | DNA 跨染料距离比的自洽性 | 相关误差传播与跨染料几何检验 | DNA测量对照 |
| Q15 | HiSiaP 底物闭合与染料冲突 | FRET/DEER结构前向预测及染料诊断 | 体系问题 |
| Q16 | MalE 保护剂与开闭态分布 | DEER混合分布与共同时间窗敏感性 | 体系问题 |
| Q17 | ChRmine 噪声权重与局部结构质量 | 局部map噪声、CC与结构几何比较 | 体系问题 |
| Q18 | SPP1 单结构与集合的密度解释 | 集合预测密度平均与单结构基线比较 | 体系问题 |
| Q19 | Fibrillarin 局部多构象的衍射支持 | 衍射密度重算及单/多构象局部检验 | 体系问题 |
| Q20 | Apoferritin 局部多构象的密度支持 | cryoEM局部候选密度与几何检验 | 体系问题 |

## 逐题选择理由与计算路线

所有问题的允许数值差异都需要在数据验收后、运行前依据论文误差和方法精度登记。本轮没有设置统一通过阈值。尚未取得的数据继续标为缺口，不自动替换成截图或无关公开样本。

### Q01　HSP90 开闭初态与亚稳性

**科学问题**　在无配体的人 HSP90α NTD 中，从闭合 ATP-lid 起始的轨迹是否比开放起始轨迹更容易离开原有构象，并出现闭合到开放的转变？

**论文及结果位置**　[Henot et al. 2022, Visualizing the transiently populated closed-state of human HSP90 ATP binding domain](https://www.nature.com/articles/s41467-022-35399-8)。Fig. 4a–g; Results: The ATP-lid closed state is a metastable excited state。

**待对照的论文结论**　开放起始轨迹较稳定；闭合起始组出现持续闭合、转为开放及偏离两态三种行为，支持闭合态为亚稳态。不能用这些非遍历轨迹直接估计平衡占比。

**选择理由**　直接复算同一蛋白两个初始构象的动力学差异，检验系统能否从轨迹和实验距离约束共同形成结构结论。

**输入**　各20条开放/闭合起始、每条1 μs的已发表轨迹、拓扑、初始构象及状态特异 NOE 接触阈值；保留每条独立重复身份。

**主计算与补充计算**　按论文刚性骨架对齐；逐帧计算 lid RMSD、开放和闭合特异 NOE 超限量；依据双指标分类各轨迹，统计首次离开时间、终态比例及按轨迹重采样的不确定性。

**怎样比较结果**　比较两起始组的状态保持与转变方向，并与 Fig. 4 的分组和分布比较；不以总体帧数当重复数，不强行重现平衡速率。

**要检验的规则作用**　能否触发状态定义、对齐区域、重复单位及非平衡采样限制；距离/RMSD计算完成后能否形成有边界的亚稳态判断。

**当前计算接入**　已有同论文HSP90描述性分析组件，但当前精确Operator不负责重建本题全部计算，也不允许据其输出平衡、速率或机制结论。须先核验原始输入、方法和本题输出关系。

**数据与工作量**　论文明确给出轨迹与脚本存放地址；本轮 Zenodo 页面取回失败，未核验文件清单与大小。优先检查本地是否已有对应轨迹。 中高：只分析已发表轨迹，不重跑MD；具体读取量待清单核验。

**数据入口**　[来源 1](https://doi.org/10.5281/zenodo.6606744)；[来源 2](https://www.rcsb.org/structure/8B7I)；[来源 3](https://www.rcsb.org/structure/8B7J)；[来源 4](https://bmrbig.org/released/bmrbig44)。

### Q02　HSP90 交换态占比与速率

**科学问题**　HSP90α NTD 的多磁场 CPMG 数据是否支持共享的低占比交换态，其占比和交换速率能否复现论文的室温结果？

**论文及结果位置**　[Henot et al. 2022, Visualizing the transiently populated closed-state of human HSP90 ATP binding domain](https://www.nature.com/articles/s41467-022-35399-8)。Fig. 5b–c; Methods: Relaxation dispersion data analysis。

**待对照的论文结论**　两态全局拟合得到室温约3–4%的少数态及约2.5 kHz交换速率；将这个交换态认作闭合 lid 是综合结构证据后的解释。

**选择理由**　这是从真实测量曲线推断隐含动力学参数的检验，比检查论文有没有报告速率更贴近 operator 的科学能力。

**输入**　各探针、多磁场、多温度 CPMG 强度/参考强度或 R2eff 曲线、误差、频率、温度与探针注释；拟合配置。

**主计算与补充计算**　由强度计算 R2eff；拟合无交换与两态交换模型，再做跨探针全局拟合、参数轮廓和按探针剔除检查；输出 kex、少数态占比和区间。

**怎样比较结果**　与 Fig. 5 的占比/速率及温度依赖比较；参数相近但模型不可辨识时不给通过。

**要检验的规则作用**　拟合模型、共享参数、噪声下限和可辨识性是否有可执行判据；能否避免把动力学少数态自动等同于结构闭合态。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　BMRbig 页面地址可打开但没有可解析文件清单；须先定位曲线/谱图文件，不能把存库声明当作已取得可拟合数据。 中：已有曲线时适合CPU拟合；仅有谱图则增加预处理。

**数据入口**　[来源 1](https://bmrbig.org/released/bmrbig44)；[来源 2](https://www.nature.com/articles/s41467-022-35399-8)。

### Q03　Sic1 集合对独立 FRET 的预测

**科学问题**　对 Sic1 和磷酸化 pSic1，只用 SAXS 得到的构象集合与加入 PRE 后的集合，哪一种能预测未参与拟合的 smFRET 效率？

**论文及结果位置**　[Gomes et al. 2020, Conformational Ensembles of an Intrinsically Disordered Protein Consistent with NMR, SAXS, and Single-Molecule FRET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9987321/)。Table 1; Results section 2.2; Discussion; Methods 5.4。

**待对照的论文结论**　SAXS+PRE 约束的集合能够同时匹配 smFRET 等验证观测，解释单独 SAXS 与按聚合物假设解释 FRET 时的表观不一致。

**选择理由**　测试跨技术额外计算是否真正改善独立预测；拟合数据和验证数据的区分有明确结果可查。

**输入**　SAXS q/I/σ、PRE约束、两种条件的原始构象池及选择后的集合或权重、染料参数、独立FRET效率/曲线及误差。

**主计算与补充计算**　冻结FRET为验证集；用已有SAXS-only和SAXS+PRE集合进行染料可及体积计算，再按逐构象效率平均预测FRET；比较两类集合预测误差及5个独立集合的变异。若只有起始池则按论文重做选择。

**怎样比较结果**　对两种磷酸化条件报告预测效率与实测效率差及传播误差，检查加入PRE是否使独立FRET预测进入论文误差范围。

**要检验的规则作用**　是否要求观测算子、正确的非线性平均顺序、独立验证以及模型误差；是否把训练拟合改善误当独立证据。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　主文和SI已有；论文指明NMR BMRB号。完整SAXS/FRET数字曲线、构象池与权重下载尚未核实，首轮暂作条件入选。 中：取得已有集合后CPU回算；若必须重新生成并选择集合则提高成本。

**数据入口**　[来源 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9987321/)；[来源 2](https://bmrb.io/data_library/summary/index.php?bmrbId=16657)；[来源 3](https://bmrb.io/data_library/summary/index.php?bmrbId=16659)。

### Q04　Sic1 突变与磷酸化引起的伸展

**科学问题**　Y14A 突变是否使 Sic1 更伸展，且磷酸化后的 Y14A 是否进一步伸展？这些差异在FRET校准误差下是否仍可分辨？

**论文及结果位置**　[Gomes et al. 2020, Conformational Ensembles of an Intrinsically Disordered Protein Consistent with NMR, SAXS, and Single-Molecule FRET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9987321/)。Fig. 5; Results immediately preceding Discussion; SI Table S9。

**待对照的论文结论**　Y14A 及其磷酸化样本的FRET效率向较低值移动，支持端到端距离更伸展，并为Y14长程接触的构象假设提供验证。

**选择理由**　通过突变与磷酸化的四组对比检验构象预测，接近可被实验干预反驳的生物学问题。

**输入**　Sic1/pSic1和两者Y14A的逐burst光子/FRET数据或未拟合数字直方图、样本/日重复、校准参数、磷酸化质谱组成。

**主计算与补充计算**　统一burst过滤和校准后拟合各组FRET效率分布；以独立实验重复为单位计算突变、磷酸化及交互差值，并传播校准误差；检测是否存在亚群或组成变化。

**怎样比较结果**　比较 Fig. 5 的移动方向与 Table S9 的幅度；输出可分辨性及无法排除的磷酸化组成差异。

**要检验的规则作用**　是否区分构象读出、接触机制解释及结合活性；能否在有干预时处理混合磷酸化组成与系统误差。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　原文承认Y14A可能改变磷酸化模式；原始FRET及质谱下载未确认。只能用图像数字化时降为结果重分析，不能记原始数据复现通过。 低中：若有逐burst表或数字直方图；获取未公开原始数据可能阻断。

**数据入口**　[来源 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9987321/)。

### Q05　nanodisc 椭圆集合解释多技术观测

**科学问题**　ΔH5–DMPC nanodisc 能否通过同一构象集合同时解释SAXS和NOE，并由互相转向的椭圆构象解释平均近圆形结构？

**论文及结果位置**　[Bengtsen et al. 2020, Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with molecular dynamics simulations](https://elifesciences.org/articles/56518)。Fig. 3A–D; Results on integration and elliptical fluctuations。

**待对照的论文结论**　SAXS与NOE整合后的异质集合保留椭圆构象，主要椭圆轴方向不同的构象族解释不同技术得到的形状差异。

**选择理由**　一个有明确定量目标的多技术整合问题：同一体系的表观几何矛盾是否由集合平均解释。

**输入**　ΔH5–DMPC轨迹/构象、SAXS曲线及误差、NOE距离上界、逐构象前向计算和BME参数；可选独立PRE/DEER作为验证。

**主计算与补充计算**　从均匀权重基线开始重做BME整合，回算SAXS残差与NOE超限；计算每帧回转张量、acylindricity和主轴角，比较重加权前后分布、簇权重及有效样本量。

**怎样比较结果**　对照 Fig. 3 的散射拟合、形状分布与簇权重方向；若验证PRE/DEER，单列其预先未参与拟合的误差。

**要检验的规则作用**　能否区分平均结构与结构集合，正确处理散射/NOE不同平均方式，以及重加权造成的有效样本缩减。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　作者GitHub顶层已观察到BME_reweight、DEER_and_PRE、SAXS_and_SANS及MD四目录；子目录payload取回失败，下一步仅需定点清单与小文件读取。 中：若已有逐构象前向值可快速CPU重加权；不生成新MD。

**数据入口**　[来源 1](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al)；[来源 2](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al/BME_reweight)。

### Q06　nanodisc 边缘与中心的膜性质

**科学问题**　ΔH5–DMPC nanodisc 的边缘脂质是否比中心更薄、更无序，而中心是否更接近普通DMPC双层？

**论文及结果位置**　[Bengtsen et al. 2020, Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with molecular dynamics simulations](https://elifesciences.org/articles/56518)。Fig. 4A–C; Analyses of the lipid properties in nanodiscs; Methods: Lipid properties。

**待对照的论文结论**　靠近蛋白带的区域较薄且较无序，中心较厚且较有序、更接近平面双层，说明小nanodisc并非均匀的膜环境。

**选择理由**　直接检验一种模型体系能否代表真实膜环境；空间分区和参考体系决定结论，适合暴露通用几何operator的科学限制。

**输入**　完整脂质nanodisc及普通DMPC双层轨迹和拓扑、BME权重、C–H原子对应、膜法向和蛋白带距离。

**主计算与补充计算**　按到蛋白带距离10 Å划分中心/边缘；处理周期边界和膜法向后计算头基间厚度与逐碳SCH；用论文权重汇总并按时间块评估中心—边缘—双层差异。

**怎样比较结果**　与 Fig. 4 的空间分布和链段序参量曲线比较；报告中心/边缘差值及参考双层的差值，不从脂质有序度直接推出膜蛋白活性。

**要检验的规则作用**　能否验证参考体系条件、区域定义、原子映射、时间相关性与重加权；蛋白轨迹适配器是否错误忽略脂质。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　需核实MD目录是否包含完整脂质和参考双层；若只有蛋白坐标则数据不足，不用不相干轨迹替代。 中高：已有轨迹的CPU后处理，读取量待核验。

**数据入口**　[来源 1](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al)；[来源 2](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al/molecular_dynamics_simulations)。

### Q07　NUS 两条件下尺寸变化解耦

**科学问题**　NUS 在原生与变性条件之间的变化中，端到端距离与回转半径的相对变化是否不同，从而否定统一比例缩放的链塌缩解释？

**论文及结果位置**　[Fuertes et al. 2017, Decoupling of size and shape fluctuations in heteropolymeric sequences reconciles discrepancies in SAXS vs. FRET measurements](https://www.pnas.org/doi/full/10.1073/pnas.1704692114)。Fig. 2A–I; Fig. 3A–B。

**待对照的论文结论**　原生条件下端到端距离和整体尺寸可解耦；用固定同聚物比例把FRET距离换为Rg会产生不一致。

**选择理由**　同一有标签体系的两种测量形成可计算的冲突；规则必须判断差异来源并发起合适的模型比较。

**输入**　NUS及其他用于对照的样本在两条件下的SAXS q/I/σ、FRET直方图及校准、标签/未标签配对、若重加权则需原始模拟构象池。

**主计算与补充计算**　重拟合SAXS的Rg与FRET效率；比较固定同聚物缩放模型和异质构象集合回算模型，对两条件计算Rg与Re的相对变化及G比值敏感性；标签对照独立检查。

**怎样比较结果**　首先复现 Fig. 2 的可观测量，再比较 Fig. 3 的两种尺寸变化；Re不是直接观测值，须随模型一并报告。

**要检验的规则作用**　跨技术指标可比性、标签对照、非线性观测算子及模型选择；能否从冲突主动计算而不是仅记录两个数值。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　本地主文已在；原文给出SI表/图位置，本轮未发现可确认的曲线及构象库下载。不得把原文图或表中的最终Rg/Re作为完整原始输入。 中：曲线重拟合低成本，完整重加权依赖未核实构象库。

**数据入口**　[来源 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5547626/)；[来源 2](https://www.pnas.org/doi/full/10.1073/pnas.1704692114)。

### Q08　NUS 集合形状与内部距离变化

**科学问题**　同时匹配FRET与Rg的NUS原生和变性构象集合，能否重现变性后形状更细长以及尺寸与形状变化不成固定关系的结果？

**论文及结果位置**　[Fuertes et al. 2017, Decoupling of size and shape fluctuations in heteropolymeric sequences reconciles discrepancies in SAXS vs. FRET measurements](https://www.pnas.org/doi/full/10.1073/pnas.1704692114)。Fig. 4A–O; Fig. 5A–B (NUS)。

**待对照的论文结论**　同时约束的异质构象集合在变性条件下更伸长；尺寸和形状的联合分布及内部距离标度比单一Rg更能区分条件。

**选择理由**　从构象坐标计算形状和内部距离，验证统一尺寸指标是否遗漏真实条件差异；与Q07的可观测量拟合形成不同失败探针。

**输入**　三个独立模拟的原始与重加权构象/权重、原生及变性条件标签、FRET和Rg约束及误差。

**主计算与补充计算**　逐构象计算回转张量本征值、Rg和asphericity，建立加权二维分布；计算按序列间距分组的内部距离标度，并在每个独立模拟上分别比较条件后汇总。

**怎样比较结果**　对照 Fig. 4 的形状移动方向、内部标度变化与 Fig. 5 的NUS集合；只显示代表结构不能算计算通过。

**要检验的规则作用**　是否具备从ensemble到联合分布的算子及集合权重/重复管理；能否区分构象代表图、统计分布与物理机制。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　原文明确三个独立模拟误差来源；原始模拟池与权重尚未确认公开可下载，当前是高信息量但待数据的候选。 中：若取得坐标，几何计算轻量；不授权为补缺口重新运行论文模拟。

**数据入口**　[来源 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5547626/)；[来源 2](https://www.pnas.org/doi/full/10.1073/pnas.1704692114)。

### Q09　T4 溶菌酶是否需要第三构象态

**科学问题**　T4溶菌酶的33组时间分辨FRET衰减，在全局分析中是否确实需要第三个构象态，而不仅是已知开放/闭合两态？

**论文及结果位置**　[Sanabria et al. 2020, Resolving dynamics and function of transient states in single enzyme molecules](https://www.nature.com/articles/s41467-020-14886-w)。Fig. 4a–c; Fig. 5b–c; Characterization of the third conformer by eTCSPC。

**待对照的论文结论**　三组分全局分析比两组分更一致地解释衰减及结构距离；少数C3态的最优占比约0.21。

**选择理由**　最贴合当前目标的数据到科学结论任务：同一批原始光子衰减需要模型选择、额外结构计算和不确定性判断。

**输入**　eTCSPC全部33变体的DA/DOnly衰减、仪器响应IRF、校准与标记信息；已知开放/闭合结构及染料模型作独立结构一致性检查。

**主计算与补充计算**　进行带IRF卷积的两态/三态全局衰减拟合，共享态占比；比较加权残差、参数轮廓和复杂度；用结构可及体积回算检查C1/C2距离一致性。

**怎样比较结果**　重现模型优劣与C3占比区间；以结构一致性和残差共同判定，不因增加参数后误差变小就通过。

**要检验的规则作用**　是否触发模型可辨识性、仪器响应、跨变体共享参数与正交证据；能否从实际拟合输出推出态数判断。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　Zenodo实际列出eTCSPC_wildtype.zip 2.9 MB与结构筛查25.3 kB，适合优先小包获取；包内格式和现有拟合operator仍需核验。 中：数据小，但全局拟合实现与误差估计有门槛；可先小包确认完整性。

**数据入口**　[来源 1](https://zenodo.org/records/3376527)；[来源 2](https://zenodo.org/records/3376527/files/eTCSPC_wildtype.zip?download=1)；[来源 3](https://zenodo.org/records/3376527/files/FRET_screening_of_PDB_structures.zip?download=1)。

### Q10　T4 溶菌酶功能突变的状态富集

**科学问题**　T4溶菌酶E11A和T26E功能突变体加入肽聚糖后，能否分别复现C2和C3富集，并与底物结合/产物加合物证据对应？

**论文及结果位置**　[Sanabria et al. 2020, Resolving dynamics and function of transient states in single enzyme molecules](https://www.nature.com/articles/s41467-020-14886-w)。Fig. 6c–g; Trapped reaction states of T4L。

**待对照的论文结论**　E11A底物捕获条件下C2增加；T26E产物加合物条件下C3增加，论文据此将C3与产物释放步骤联系。

**选择理由**　包含真正的体系功能问题：把突变和底物干预、构象占比及HPLC/扩散证据连接，避免只做状态分类。

**输入**　wt**、E11A与T26E各自有/无底物的单分子与TCSPC数据、FCS数据、HPLC时间/峰信号和背景；样品与标记条件。

**主计算与补充计算**　统一拟合各条件态占比，计算有/无底物的配对变化；重新拟合FCS扩散时间，并对HPLC进行背景扣除、峰积分及时间变化比较，按样品证据连接构象与功能态。

**怎样比较结果**　对照 Fig. 6e 的C2/C3变化方向及 Fig. 6c/f 的结合/加合物证据；缺少HPLC或对照时只报告构象差异，不能判定产物释放机制已证明。

**要检验的规则作用**　跨实验样品身份、干预对照、不同证据强度以及构象差异到功能机制的推断边界；几何operator是否被误用为活性证据。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　Zenodo实际列出功能变体包4.8 GB；不适合整包快速首跑。优先查档案说明和可选择子文件；HPLC原始轨迹尚未核验。 高：4.8 GB原始包且需多技术预处理；本轮不下载大包。

**数据入口**　[来源 1](https://zenodo.org/records/3376527)；[来源 2](https://zenodo.org/records/3376527/files/Single_molecule_Functional_variants.zip?download=1)；[来源 3](https://www.nature.com/articles/s41467-020-14886-w)。

### Q11　T4 溶菌酶两种短寿命结构判别

**科学问题**　T4 lysozyme 的实验 FRET 约束是否足以从候选结构中分别识别 C1、C2 两种短寿命构象，并重现各自接近参考晶体构象的结构范围？

**论文及结果位置**　[Dimura et al. (2020), Automated and optimally FRET-assisted structural modeling](https://www.nature.com/articles/s41467-020-19023-1)。Results, Benchmarking the methodology; Figure 4; Supplementary Figure 6; Supplementary Table 1; PDBDEV_00000044。

**待对照的论文结论**　论文用实验距离约束解析 C1/C2；两参考构象相差约 4 Å RMSD，FRET 信息能够区分它们。

**选择理由**　直接从实验观测走到构象判别；需要前向预测、误差加权和留出距离检验，不能仅比较两个 PDB 的 RMSD。

**输入**　两状态的 FRET 距离与误差、标记位置/染料参数、候选结构、参考结构；原始荧光衰减用于必要时重估距离。

**主计算与补充计算**　按染料可及体积前向计算候选结构的距离；用误差和有效自由度计算标准化 χ²；把拟合与检验距离分开，分别筛 C1/C2，再计算 Cα RMSD 与结构不确定性。

**怎样比较结果**　比较两态候选排名、留出 χ²、各自相对参考构象的 RMSD 及两态可分性；容差需在数据验收后预先冻结。

**要检验的规则作用**　规则能否把状态人口、染料模型和独立验证连接到结构结论；若只检查距离字段齐全会漏掉状态配对或训练数据重复使用。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　优先级中高；已有小型 FRET screening ZIP 25.3 kB 和 eTCSPC ZIP 2.9 MB；全原始库 16.1 GB 无需先全下。PDB-Dev 本次打开失败；约束/候选结构完整性待验收。轻量再评分中等成本，重新采样高成本。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/records/3376527)；[来源 2](https://pdb-dev.wwpdb.org/entry.html?PDBDEV_00000044)；[来源 3](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-020-19023-1/MediaObjects/41467_2020_19023_MOESM1_ESM.pdf)。

### Q12　YaaA 错误折叠的模拟负对照

**科学问题**　对 YaaA 的不同初始折叠，保留未用于结构优化的 FRET 距离后，能否识别错误折叠仍与数据不符，并重现正确折叠附近候选的优势？

**论文及结果位置**　[Dimura et al. (2020), Automated and optimally FRET-assisted structural modeling](https://www.nature.com/articles/s41467-020-19023-1)。Figure 3a,c; Results, FRET-guided optimization of conformers; Figure 2a,c。

**待对照的论文结论**　不同初始折叠优化后仍有不同的检验 χ² 水平；错误折叠无法靠本轮约束采样修正，增加独立检验距离后质量指标趋于稳定。

**选择理由**　加入明确失败对照，检验系统会否把优化过程完成或训练误差下降误判成正确科学结论。

**输入**　YaaA CASP11 T806 候选及优化后结构、模拟 FRET 距离/误差、优化与检验 pair 划分、5CAJ 参考结构、Figure 3 数值。

**主计算与补充计算**　保持论文距离划分，以既有候选重算前向距离、留出标准化 χ² 和 Cα RMSD；增加检验 pair 数量，比较各初始折叠曲线及排名稳定性。

**怎样比较结果**　检查低 RMSD 候选是否同时有更好留出 χ²；错误折叠是否仍被拒绝；检验曲线是否出现论文报告的稳定趋势。

**要检验的规则作用**　独立证据、初始模型覆盖和失败停止是否可执行；不能把低训练残差当准确度。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中优先级的模拟数据负对照，不计为真实实验体系复现。Source Data 链接已见但 web 读取失败；完整候选结构尚未确认。重评分中成本，重新 NMSim/MD 为高成本，当前不启动。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://www.nature.com/articles/s41467-020-19023-1#Sec19)；[来源 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-020-19023-1/MediaObjects/41467_2020_19023_MOESM4_ESM.xlsx)；[来源 3](https://github.com/Fluorescence-Tools/Olga)。

### Q13　DNA 原始光子到校正距离

**科学问题**　从同一批 confocal 原始光子数据出发，完整校正后能否恢复 DNA 两个标记间距状态，并得到与结构模型一致的距离差？

**论文及结果位置**　[Hellenkamp et al. (2018), Precision and accuracy of single-molecule FRET measurements—a multi-laboratory benchmark study](https://www.nature.com/articles/s41592-018-0085-0)。Figure 2a–d; Figure 4a,c; Methods, intensity corrections and distance conversion。

**待对照的论文结论**　校正改变 FRET 峰的位置，尤其低 FRET 峰；正确距离转换后测得的 DNA 间距与已知结构相容。

**选择理由**　通过原始数据—校正—距离—结构判断的完整小链路检查算子，难度高于识别 FRET 是否模型推导。

**输入**　confocal HDF5/HT3、背景/串色/直接激发/γ/β参数、样本身份、R0 和染料模型、DNA 标记位点与参考几何。

**主计算与补充计算**　选 burst、逐步校正通道计数并拟合 E 分布；使用 R0 与染料可及体积换算距离，传播测量及 R0 不确定性后比较两态间距。

**怎样比较结果**　以校正后峰位、两态间距方向和与结构预测的归一化残差为终点；不以裸 E 峰的差异代替结构距离。

**要检验的规则作用**　是否正确安排校正依赖顺序、区分平均效率对应的表观距离与物理平均位置距离，并传播系统误差。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　可作为计算链首轮候选，CPU 中成本。库中 134.1 MB HDF5 ZIP 命名为 1_lo_1_hi_Mix，而文中 Figure 2 描述 lo/mid；必须先核对文件说明，不能按文件名猜样本身份。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/records/1249497)；[来源 2](https://www.nature.com/articles/s41592-018-0085-0#Sec15)。

### Q14　DNA 跨染料距离比的自洽性

**科学问题**　在传播染料和仪器不确定性后，两种染料对对 DNA 长/短间距比的估计是否一致，并且能够支持同一几何模型？

**论文及结果位置**　[Hellenkamp et al. (2018), Precision and accuracy of single-molecule FRET measurements—a multi-laboratory benchmark study](https://www.nature.com/articles/s41592-018-0085-0)。Results, Distance determination and Self-consistency argument; Figure 4; Methods, self-consistency; Supplementary Tables 2–4 and Notes 3,5。

**待对照的论文结论**　不同染料对所得相对距离可通过自洽检验；距离比较依赖染料运动与可及体积假设。

**选择理由**　真正测试跨测量的定量可比性：共享 R0 的误差可在比值中部分抵消，染料模型偏差却可能保留。

**输入**　各实验室/染料对 lo、mid 的 E 与误差，校正参数、R0、染料运动数据及模型距离；完整跨实验室数值是否可下载待确认。

**主计算与补充计算**　由 E 计算各样品距离及长短比，按共享校准参数做相关误差传播；计算不同染料对之间的差值区间和模型残差；做染料模型敏感性分析。

**怎样比较结果**　比较各染料对距离比与参考几何比的兼容区间，而不是只比较点估计或逐点误差条。

**要检验的规则作用**　规则是否识别共享系统误差、重复单位为实验室而非单个光子，以及不同染料是否能合并。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中优先级；所需表格载荷未核验。Zenodo 只承诺 Figure 2 原始数据，不能当全部实验室数据已公开。拿到数表后低到中成本，必要时先保留为数据受限候选。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://www.nature.com/articles/s41592-018-0085-0)；[来源 2](https://zenodo.org/records/1249497)。

### Q15　HiSiaP 底物闭合与染料冲突

**科学问题**　HiSiaP 结合底物后是否发生结构域闭合；为什么 175/228 位点的一组 FRET 染料给出异常判断，而更换染料后恢复与 DEER 和结构预测一致的结论？

**论文及结果位置**　[Peter et al. (2022), Cross-validation of distance measurements in proteins by PELDOR/DEER and single-molecule FRET](https://www.nature.com/articles/s41467-022-31945-6)。Results, Comparison 1: HiSiaP; Figures 3 and 4c–e; Supplementary Figures 4–6。

**待对照的论文结论**　TMR/Cy5 条件的测量恢复预期闭合；异常荧光结果与染料和蛋白相互作用相联系。

**选择理由**　同一体系有相互矛盾的测量和干预对照，最能揭露机械平均多方法距离的失败。

**输入**　两组染料的 apo/holo smFRET、DEER 时间迹与分布、各向异性/寿命、标记位点和结构 2CEY/3B50。

**主计算与补充计算**　重估各条件距离变化与区间，计算与开/闭结构染料前向预测的残差；关联各向异性和寿命变化，比较换染料前后对闭合假设的支持。

**怎样比较结果**　检查闭合方向是否与两个独立测量链相容，异常是否随染料替换消失；保留非唯一因果解释边界。

**要检验的规则作用**　冲突证据能否触发染料模型适用性检查和额外计算，避免把异常 probe 当成新的蛋白构象。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　高优先级。Figure3.zip 1.5 GB、Figure4.zip 1.7 GB；优先验收出版社数值表再取所需原始片段。计算中成本；当前未下载，表内完整性未知。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/record/6683587)；[来源 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-31945-6/MediaObjects/41467_2022_31945_MOESM4_ESM.xlsx)。

### Q16　MalE 保护剂与开闭态分布

**科学问题**　MalE 加入麦芽糖后，DEER 中残留的开放态是真正的配体未饱和，还是与冷冻保护剂条件有关；去除保护剂后能否复现闭合态占优？

**论文及结果位置**　[Peter et al. (2022), Cross-validation of distance measurements in proteins by PELDOR/DEER and single-molecule FRET](https://www.nature.com/articles/s41467-022-31945-6)。Results, Comparison 2: MalE; Figure 5c; Supplementary Figures 9–10。

**待对照的论文结论**　增加麦芽糖未消除混合态；改变/去除冷冻保护剂后闭合态更明显。

**选择理由**　同一生物问题含配体剂量和环境对照，适合验证规则能否挑出解释冲突所需的额外计算。

**输入**　36/352、29/352 的不同麦芽糖剂量和保护剂下 DEER 时间迹；smFRET 及 134/186 阴性对照；结构 1OMP/1ANF。

**主计算与补充计算**　在共同可解析时间/距离范围内重拟合 DEER 分布，估计开闭混合权重及不确定性；比较剂量改变与保护剂改变的权重效应，并与 smFRET 和阴性对照对照。

**怎样比较结果**　比较同位点的条件效应及方向，不把不同时间迹长度造成的峰分辨率变化当真实人口改变。

**要检验的规则作用**　测量温度、保护剂、SNR 和时间窗能否进入可比性与模型选择，而非只作为存档字段。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　高优先级。Figure5.zip 1.8 GB；出版社表优先，计算中成本。无保护剂时间迹较短，拟合必须做共同窗口敏感性检验。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/record/6683587)；[来源 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-31945-6/MediaObjects/41467_2022_31945_MOESM4_ESM.xlsx)。

### Q17　ChRmine 噪声权重与局部结构质量

**科学问题**　ChRmine 的高噪声密度区，降低数据约束权重后能否得到更合理的局部结构，即使这些区域的 map 拟合变差？

**论文及结果位置**　[Hoff et al. (2024), Accurate model and ensemble refinement using cryo-electron microscopy maps and Bayesian inference](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012180)。Figure 2a–c; Results, Bayesian noise models reduce data overfitting; PDB 7w9w, EMD-32377。

**待对照的论文结论**　噪声较大区域更多依靠物理约束；相较沉积结构，碰撞减少、氢键和盐桥几何改善。

**选择理由**　检验是否会错误地把更高 map correlation 当唯一成功判据；要求对具体通道结构联合评估数据和物理可行性。

**输入**　7w9w 原始与 EMMIVox 精修结构、EMD-32377 map/half-maps、残基邻域定义、原方法噪声和几何评价参数。

**主计算与补充计算**　从 half-map 差异估局部噪声；按相同残基和 mask 重算 local CC、碰撞、氢键/盐桥；比较高低噪声区的配对改善。

**怎样比较结果**　核对局部噪声—拟合变化关系以及几何改善的方向；不以整体 CC 一项替代结构质量结论。

**要检验的规则作用**　规则能否触发局部噪声分层、多指标联合判断，以及接受有依据的局部 fit 下降。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中高优先级；仓库列出 02-7w9w 和验证脚本，具体模型/half-map 载荷未核验。若已有工具只做结构和 map 分析，中成本；不重跑 MD。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://www.plumed-nest.org/eggs/23/041/)；[来源 2](https://github.com/COSBlab/EMMIVox-BENCHMARK)；[来源 3](https://github.com/COSBlab/EMMIVox)。

### Q18　SPP1 单结构与集合的密度解释

**科学问题**　对 SPP1 噬菌体尾管，构象集合是否比单个带 B-factor 的结构更能解释 cryo-EM 密度，而非仅因增加参数得到表面改善？

**论文及结果位置**　[Hoff et al. (2024), Accurate model and ensemble refinement using cryo-electron microscopy maps and Bayesian inference](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012180)。Figure 4a; Results, Ensemble refinement; PDB 6yeg, EMD-10792。

**待对照的论文结论**　论文中 SPP1 的集合 CCmask 从单结构约 0.60 增至约 0.77，是该 benchmark 最大改善。

**选择理由**　直接比较同一体系的单态/多态解释；要求重算前向平均密度、控制 mask，并审查集合复杂度。

**输入**　SPP1 单结构、精修集合及权重、EMD-10792 map/half-maps、同一 forward model 和 mask；集合是否公开需另验。

**主计算与补充计算**　按集合权重平均预测密度，与单结构在同一 mask 下计算 CC；做减小集合规模、保留验证数据和 B-factor 基线的敏感性比较。

**怎样比较结果**　先重现作者同口径 CC 差，再用额外验证判断改善稳定性；额外验证不冒称作者已报告。

**要检验的规则作用**　是否区分更好拟合与已证实异质性；是否要求集合权重、前向平均和复杂度/验证独立性。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中优先级但数据受限。论文 Data availability 明确单结构模型与输入可用，未保证全 ensemble 轨迹。缺集合就记数据缺口，不临时开 MD；重评估中成本，重新生产集合高成本。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://www.plumed-nest.org/eggs/23/041/)；[来源 2](https://github.com/COSBlab/EMMIVox-BENCHMARK)；[来源 3](https://github.com/COSBlab/EMMIVox)。

### Q19　Fibrillarin 局部多构象的衍射支持

**科学问题**　Fibrillarin 的 RNA 结合区域邻近残基是否支持多种局部构象，能否用衍射数据重新支持 Leu58、Phe69、Met175 的替代构象而非仅读取 qFit 输出标签？

**论文及结果位置**　[Wankowicz et al. (2024), Automated multiconformer model building for X-ray crystallography and cryo-EM, Version of Record](https://elifesciences.org/articles/90606)。Figure 2b; Results, qFit improves overall fit to data relative to deposited structures; PDB 1G8A。

**待对照的论文结论**　qFit 在 1G8A 的上述残基识别了原模型没有表达的替代构象；与 RNA 结合功能的联系在论文中仍是待检验假说。

**选择理由**　从真实密度证据判断局部异质性，避免把模型中存在 altloc 直接当成实验支持。

**输入**　1G8A 结构与 structure factors/自由反射集、qFit 模型、构图与精修参数；针对三残基的单/多构象候选。

**主计算与补充计算**　用相同反射集重算电子密度与局部 fit，比较单/多构象的占有率、χ角、差异密度、Rfree 与几何冲突；必要时对三残基做受限模型选择。

**怎样比较结果**　比较被数据支持的替代构象与作者模型的局部 RMSD/rotamer；精修独立验证不变，功能活性不作为本题输出。

**要检验的规则作用**　局部结构异质性是否有观测支持、增加构象是否过拟合，以及结构证据到功能假说之间的结论边界。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中高优先级；Zenodo 直接 open 报错，但 primary search 返回 qfit_test_set_zenodo.zip 17.8 MB 和说明：MTZ/沉积模型从 PDB 获取。载荷未核验；局部分析中成本，Phenix/qFit 依赖待检查，不安装。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/records/10936292)；[来源 2](https://github.com/ExcitedStates/qfit-3.0)；[来源 3](https://www.rcsb.org/structure/1G8A)。

### Q20　Apoferritin 局部多构象的密度支持

**科学问题**　Apoferritin 的 1.22 Å cryo-EM map 能否同时支持 Arg22 的已知两构象，以及 Glu14 在原沉积模型中未表达的额外构象？

**论文及结果位置**　[Wankowicz et al. (2024), Automated multiconformer model building for X-ray crystallography and cryo-EM, Version of Record](https://elifesciences.org/articles/90606)。Figure 5a,b; Results, qFit models alternative conformers in cryo-EM density maps; PDB 7A4M。

**待对照的论文结论**　qFit 在 7A4M 中恢复 Arg22 两构象，并为 Glu14 提出有密度支持的新增构象。

**选择理由**　同一 map 含已知阳性对照与新增候选，适合检查 operator 能否从密度支撑两类结论并排除仅增加模型复杂度。

**输入**　7A4M 结构、对应 EMDB map/half-maps、原/qFit 模型、map sharpening 与坐标/占有率精修参数；EMDB accession 需数据 intake 核实。

**主计算与补充计算**　对 Arg22/Glu14 生成局部单/双构象候选，按统一 map 计算 Q-score/局部残差、占有率与 clash；对 Arg22 比较原两构象 RMSD，并检查 sharpening/half-map 敏感性。

**怎样比较结果**　Arg22 以两构象均被恢复为阳性对照；Glu14 需额外构象确实改善局部密度解释且几何合理。比较容差与作者 RMSD 0.5 Å 分类口径对应。

**要检验的规则作用**　是否要求统一地图处理、局部分辨率和独立 map 验证，是否区分发现新构象与复制已有坐标。

**当前计算接入**　当前注册表没有覆盖本题完整计算的可路由Operator；所列计算为拟接能力，尚未实现或在本题验证。

**数据与工作量**　中高优先级；qFit 档案 17.8 MB 清单可见，map 大小/half-map 可用性尚未核验。局部计算中成本；无必要重建全颗粒图像。 见准备程度说明；只计划重分析，不重新生成大规模模拟或采集数据。

**数据入口**　[来源 1](https://zenodo.org/records/10936292)；[来源 2](https://github.com/ExcitedStates/qfit-3.0)；[来源 3](https://www.rcsb.org/structure/7A4M)。

## 这套题怎样找最大问题

先保持 Rules 和当前 Operator 注册表不变，逐题记录能否取得匹配数据、能否形成计算计划，以及是否有允许的计算入口。没有执行条件的题目归入数据或计算接入缺口。得到实际计算后，再比较规则触发、补充计算、结论和论文参照。

最终按重复的根本原因汇总，分别统计题数与论文/共享数据组数。重点辨别漏掉必要计算、用了错误的适用条件、没有足够的科学判据、执行实现出错，以及数据本身不足。只有实际结果支持后才选一项修订，不根据哪项代码最好改来安排主线。

本轮状态为计划已修订、候选已筛选、数据入口已核查到逐题注明的程度。数据完整性验收、20题运行、论文结果一致性与正式科学审核仍未完成。

复核文件包括 [机器可读题目表](questions_20.json)、[CSV题目表](questions_20.csv) 和 [Operator实际范围](OPERATOR_READINESS.md)。
