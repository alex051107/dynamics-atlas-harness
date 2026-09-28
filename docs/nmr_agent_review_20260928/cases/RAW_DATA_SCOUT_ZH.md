# NMR 弛豫色散原始数据蛋白候选清单

调研时间：2026-09-26。方法：只读浏览存档页面本身（Zenodo API 元数据、Zenodo/bioRxiv/PMC 页面文本），未下载任何数据文件、未登录、未接受除必要 cookie 外的条款。已排除已知的 K-Ras 2023（Zenodo 10.5281/zenodo.8187159）与 RfaH 2025（Figshare）。

## 总表

| # | 蛋白 | 数据类型 | 是否含作者拟合结果/参数文件 | 需要的工具扩展 | 存档链接 |
|---|------|---------|-------------------------|---------------|---------|
| 1 | Im7（野生型，折叠系综） | 15N CEST（600/800/1200 MHz，10/15/20°C）+ 15N TROSY-CPMG | **是**——压缩包内含 ChemEx 实验/方法/参数文件及"提取拟合参数"脚本，需要先剥离 | 多温度、多场强联合拟合；折叠中间体（非简单两态） | [Zenodo 22794667](https://zenodo.org/records/22794667) |
| 2 | SHP2 N-SH2 结构域（结合 Gab1 磷酸肽） | 1H-15N CPMG，16 张 .ucsf 原始谱图（νCPMG 0–1000 Hz），未转换为 R2,eff | 页面描述未提及拟合参数文件（很可能只有原始谱图） | 需要从谱图峰强度自行计算 R2,eff 的前置流程（比常见的"R2,eff 表格"更底层一步）；配体结合体系 | [Zenodo 20732240](https://zenodo.org/records/20732240) |
| 3 | pro-IL-18（WT / Q54V / Q54I） | 15N/13C/1H CPMG + CEST，逐探针 ChemEx 输入格式 | 不确定——ChemEx 输入格式通常含实验/方法文件，是否含最终拟合值未在页面明确说明，需实际解压确认 | 两个激发态（ES1、ES2）+突变体间比较；同一存档还捆绑了 AlphaFlow 结构系综和甲基 NOESY，体量很大，需要精确取用 CPMG.zip / CEST.zip 两个小文件 | [Zenodo 19186893](https://zenodo.org/records/19186893) |
| 4 | 腺苷酸激酶 AQADK | 15N CPMG，raw R2,eff | 未明确提及 | 标准两态（open/closed lid 结构域运动），可作为"简单两态"基准 | [Zenodo 20834076](https://zenodo.org/records/20834076)（Fig5_archive.zip，与 #5–8 打包在同一压缩包） |
| 5 | β-内酰胺酶 TEM-1（BLAC） | 15N CPMG，raw R2,eff | 未明确提及 | 标准两态，催化机制相关 | 同上（Fig5_archive.zip） |
| 6 | 胆绿素还原酶 B（BLVRB） | 15N CPMG，raw R2,eff | 未明确提及 | 需要区分 apo/辅酶结合两种状态的比较模型 | 同上（Fig5_archive.zip） |
| 7 | 亲环素 A（CypA） | 15N CPMG，raw R2,eff | 未明确提及 | 标准两态；**但该蛋白 CPMG 数据在文献中极为经典（Eisenmesser 2002/2005 Nature 系列），新颖性存疑，可能已被同类 AI 工具的训练/示例语料吸收** | 同上（Fig5_archive.zip） |
| 8 | VH1 相关磷酸酶（VHR） | 15N CPMG，raw R2,eff，多场强 | 未明确提及 | 标准两态，别构环（variable insert loop）相关 | 同上（Fig5_archive.zip） |
| 9 | 几丁质酶 19A（Chi19，*Streptomyces coelicolor*，205 残基） | 15N CPMG，raw R2,eff | 含配套"分析脚本"，是否含最终拟合参数未明确 | 全新数据（无历史发表论文可比对结论），标准两态，适合测试模型对未见蛋白的泛化 | [Zenodo 20834076](https://zenodo.org/records/20834076)（Fig6_archive.zip，与 #10 同一压缩包） |
| 10 | 假想蛋白 Hypo（YjbJ/UPF0234，PDB 1RYK，70 残基） | 15N CPMG，raw R2,eff | 同上 | 全新数据，小蛋白，标准两态 | 同上（Fig6_archive.zip） |

**关于 #4–10 的重要说明**：这 7 个蛋白的原始数据全部打包在同一篇 2026 年 *Nature*（Wayment-Steele 等，"Learning millisecond protein dynamics from what is missing in NMR spectra"，即 Dyna-1 模型论文）的 Zenodo 存档 [10.5281/zenodo.20834076](https://zenodo.org/records/20834076) 里，分两个压缩包：`Fig5_archive.zip`（AQADK、BLAC、BLVRB、CypA、KRAS、VHR 六个蛋白共 31.5 MB）与 `Fig6_archive.zip`（Chi19、Hypo 两个蛋白共 15.7 MB）。这些数据本身多是各实验室早年测得、经 Wayment-Steele 团队征集汇总用于测试其机器学习模型，而非全新采集——引用来源分别是 Henzler-Wildman et al. 2007（AQADK）、Elings et al. 2019（BLAC）、Eisenmesser 实验室内部档案（BLVRB）、Kern 实验室内部档案（CypA）、Dryad 10.5061/dryad.j6q573nm0（KRAS，与已排除的 2023 Hansen K-Ras 数据集是不同的存档，但涉及同一蛋白，建议跳过以免与已有 K-Ras 案例混淆）、V. Beaumont 2019 博士论文（VHR）。Chi19 与 Hypo 是该论文首次为"前瞻性测试"专门整理的数据，来源较新。许可证均为 CC-BY-4.0。

## 逐项细节

### 1. Im7（野生型）——折叠自由能景观重建
- **论文**：《Multi-Field CEST NMR Reconstructs a Protein Folding Landscape》，作者 Tiwari, Rozic, Hiller（巴塞尔大学），2026 年存档。
- **存档**：[Zenodo 10.5281/zenodo.22794667](https://zenodo.org/records/22794667)，CC-BY-4.0，单文件 `SI_chemex_scripts_and_data.zip`（3.7 MB）。
- **实验**：15N CEST 与 15N TROSY-CPMG，场强 600/800/1200 MHz，温度 10/15/20°C（多温度、多场强联合数据集）。
- **含拟合结果**：是。压缩包描述明确包含"ChemEx 实验、方法和参数文件"以及"提取拟合参数、绘制图表的脚本"——若要用作 AI 工具的盲测输入，需要先把这些拟合/参数文件从原始 profile 数据中分离出来。
- **核心结论**：通过多场强、多温度 CEST 数据重建 Im7 的折叠自由能景观，观察到稀有中间体的化学位移特征（论文标题即点明"重建折叠景观"，隐含不止两个宏观态）。
- **特殊处理**：需要联合拟合多温度/多场强数据，且要处理折叠中间体而非单一两态交换。

### 2. SHP2 N-SH2 结构域（结合 Gab1 磷酸肽）
- **论文**：Glaser, Pádua, Ojoawo, Sullivan, Kern，《Phosphatase SHP2 pathogenic mutations enhance activity by altering conformational sampling》，*PNAS* 123(3) e2513851123，2026 年 1 月。
- **存档**：[Zenodo 10.5281/zenodo.20732240](https://zenodo.org/records/20732240)，CC-BY-4.0，单文件 `SHP2_NSH2_CPMG.zip`（31.2 MB），数据来自 NMRFAM（威斯康星大学麦迪逊分校）数据仓库，经作者许可转存。
- **实验**：1H-15N CPMG，16 张 .ucsf 格式原始谱图，νCPMG 0–1000 Hz——这是比"逐残基 R2,eff 表格"更早一步的原始形式（谱图本身），场强/温度页面未注明。
- **含拟合结果**：页面描述未提及拟合参数文件，大概率是纯原始谱图。
- **核心结论**：SHP2 致病突变（E139D、T42A 等位于调控 SH2 结构域内）通过改变构象采样而非直接催化位点突变来增强磷酸酶活性；论文同时含 X 射线（PDB 9EH9 等 8 个结构）与 NMR/BMRB（52757–52760）数据。
- **特殊处理**：需要从原始谱图做峰强度提取→R2,eff 计算的完整流程，比常见的"直接读 R2,eff 表"更接近真实实验流程；该体系是配体（Gab1 肽）结合状态，属于配体结合模型而非纯内源交换。

### 3. pro-IL-18（WT / Q54V / Q54I）
- **论文**：Bonin, Lee, Liu, Kim, Kay，《Making invisible excited state protein structures visible by combining NMR and machine learning》，bioRxiv 10.1101/2025.11.27.690854（2025）。
- **存档**：[Zenodo 10.5281/zenodo.19186893](https://zenodo.org/records/19186893)，CC-BY-4.0，总计 43.6 GB，但目标文件很小：`CPMG.zip`（34.4 kB）与 `CEST.zip`（51.3 kB），其余是 AlphaFlow 结构系综（约 2.5 GB×3）和甲基 NOESY 谱图（494 MB），与 NMR 弛豫色散无关，取用时需精确定位到这两个小文件。
- **实验**：15N 骨架、13Cα/Cβ/CO、1H（酰胺/α）、13C 甲基（ILV 标记样品用于 NOESY），CPMG 和 CEST 均为逐探针 ChemEx 输入格式；主场 1 GHz（23.4 T）与 800 MHz，25°C。
- **含拟合结果**：不确定，需要实际解压 CPMG.zip / CEST.zip 查看是否含最终 kex/pop/dw 数值（ChemEx 输入格式本身通常含实验描述文件，但不必然含拟合输出）。
- **核心结论**：WT pro-IL-18 存在两个稀有激发态 ES1、ES2（各 <0.5% 布居）；Q54V 突变使布居分别提升至 6.4% 和 7.6%，寿命 8 ms/16 ms；结构解释为 β-链翻转形成两个可选折叠态（Alt1、Alt2），经甲基-甲基 NOE 验证。WT 化学位移另存于 BMRB 31122。
- **特殊处理**：三态（基态+ES1+ES2）而非两态；需要跨突变体（WT/Q54V/Q54I）联合比较模型。

### 4–8. Fig5_archive.zip 内的五个蛋白（AQADK、BLAC、BLVRB、CypA、VHR）
- **来源论文**：Wayment-Steele, El Nesr 等，《Learning millisecond protein dynamics from what is missing in NMR spectra》，*Nature*（2026）——即 Dyna-1 模型论文。
- **存档**：[Zenodo 10.5281/zenodo.20834076](https://zenodo.org/records/20834076)，CC-BY-4.0，`Fig5_archive.zip`（31.5 MB）。
- **实验**：均为 15N CPMG，raw R2,eff 值（逐残基）。
- **各蛋白背景**（原始数据提供方）：
  - **AQADK**（腺苷酸激酶）：K. Henzler-Wildman 提供，对应 Henzler-Wildman et al. 2007 *Nature* 经典的 lid/NMP 结构域开合两态交换研究。
  - **BLAC**（β-内酰胺酶 TEM-1）：M. Ubbink 提供，对应 Elings et al. 2019 关于 TEM-1 催化机制分步构象动力学的研究。
  - **BLVRB**（胆绿素还原酶 B）：E. Eisenmesser 提供，对应其实验室关于辅酶结合耦合 μs-ms 动力学的系列工作（活性位点 apo 态存在快时标交换，辅酶结合后被抑制）。
  - **CypA**（亲环素 A）：Kern 实验室内部档案，对应经典的酶催化偶联构象交换体系。
  - **VHR**（VH1 相关磷酸酶）：取自 V. Beaumont 2019 年耶鲁大学博士论文，涉及别构环（variable insert loop）对活性的影响。
- **含拟合结果**：页面描述只提到"raw R2,eff 值"，未明确是否含各蛋白原作者的最终拟合参数；需要解压确认。
- **特殊处理**：BLVRB 需要区分 apo/辅酶结合两种状态；CypA 数据新颖性存疑（该体系 CPMG 数据是本领域最著名的教学案例之一，可能已被类似 AI 工具的训练或示例数据吸收，用作"盲测"候选时应谨慎）；AQADK、BLAC、VHR 相对是标准两态体系。

### 9–10. Fig6_archive.zip：Chi19 与 Hypo（前瞻性测试蛋白）
- **来源论文**：同上（Dyna-1 论文）。
- **存档**：同一 Zenodo 记录 10.5281/zenodo.20834076，`Fig6_archive.zip`（15.7 MB）。
- **蛋白**：Chi19（*Streptomyces coelicolor* 几丁质酶 19A，205 残基）、Hypo（假想蛋白 YjbJ/UPF0234，对应 PDB 1RYK，70 残基）。
- **实验**：15N CPMG，raw R2,eff 值，附带"用于对 Dyna-1 模型做前瞻性测试的分析脚本"。
- **含拟合结果**：页面提到含分析脚本，但未明确说明是否含各蛋白的最终交换参数（kex/pop/dw），需要解压确认。
- **核心结论**：这两个蛋白是作者专门为"事先未见过"的前瞻性盲测收集的数据，本身没有独立发表的历史构象交换论文可比对——这正是测试 AI 工具真实泛化能力（而非记忆已发表结论）的理想对象。
- **特殊处理**：标准两态假设，但因缺乏独立发表的"标准答案"论文，评估时需要依赖存档内作者自己的拟合结果作为参照（也意味着这部分参照数据将来需要被封存，不能提前给 AI 看）。

## 有前景但未确认原始数据公开存放位置

- **T4 溶菌酶 L99A（CEST 三态研究）**：Tiwari, Khandave, Hansen, Bouvignies, Kay, Vallurupalli，《Using CEST NMR to discover previously unobserved states on the free energy surface of proteins: Application to the L99A cavity mutant of T4 lysozyme》，*J Biol Chem*，2025，DOI 10.1016/j.jbc.2025.110989（PMC12805379）。15N 骨架 + 13C 甲基（Ile δ1/Leu/Val）CEST，16.4 T 为主，11.5°C；发现 E↔B↔I 三态交换（kex,EB=297±6 s⁻¹，kex,BI=1667±44 s⁻¹，I 态布居约 0.2%）。论文正文明确写"CEST datasets analyzed during the current study are available from the corresponding authors upon reasonable request"，未见 Zenodo/Figshare/Dryad/GitHub 或 SI 原始数据表链接，故未列入正表。
- **FF domain 三态 CEST 研究**：Tiwari, De, Kay, Vallurupalli，《Beyond slow two-state protein conformational exchange using CEST: applications to three-state protein interconversion on the millisecond timescale》，*J Biomol NMR*，2024（PMID 38169015）。研究 HYPA/FBP11 的 FF domain 在 F/I1/I2 三态间的毫秒交换。因 PubMed 页面被验证码拦截、且检索到的同课题组后续 bioRxiv 论文（2024.04.02.587659，高 B1 场 CEST 方法学）明确说该三态论文是独立发表、未被后者收录数据，本次调研未能定位到公开的原始数据存档链接，暂列入待确认。
- **ChemEx GitHub 仓库（examples 目录）**：目录下 `Experiments/` 含 44 个按实验类型分类的子目录（CEST_15N、CPMG_CH3_MQ 等），但这些是程序自带的教学/合成示例配置，不是与具体新蛋白绑定的真实实验原始数据集，未在其中找到额外可用的新蛋白线索。

## 三句话摘要

本次核实到 3 个独立的、明确含逐残基原始弛豫色散数据的存档（Im7、SHP2 N-SH2、pro-IL-18），另外 2026 年 Dyna-1 论文的 Zenodo 存档一次性打包了 7 个蛋白（AQADK、BLAC、BLVRB、CypA、VHR、Chi19、Hypo）的原始 R2,eff 数据，合计确认了 10 个新候选蛋白（另有 1 个 KRAS 因与已排除案例同蛋白而跳过）。最容易直接用现有 15N CPMG/CEST 两态工具跑通的是 AQADK（腺苷酸激酶，经典开合两态）、BLAC（β-内酰胺酶 TEM-1）、VHR（磷酸酶）以及 Chi19/Hypo 这两个全新前瞻测试蛋白——它们都是单一 15N 通道、标准两态交换，不涉及多态、配体结合或大蛋白甲基信号等复杂情形。T4 溶菌酶 L99A 三态研究和 FF domain 三态研究因未找到公开原始数据存放位置，仅列入待确认清单。
