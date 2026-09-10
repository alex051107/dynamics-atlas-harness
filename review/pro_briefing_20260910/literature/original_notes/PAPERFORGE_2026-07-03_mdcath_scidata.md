# PaperForge Analysis - mdCATH Scientific Data PDF

Paper: Antonio Mirarchi, Toni Giorgino, Gianni De Fabritiis, "mdCATH: A Large-Scale MD Dataset for Data-Driven Computational Biophysics", Scientific Data, 2024. DOI: `10.1038/s41597-024-04140-z`.

Local PDF: `autoresearch/tasks/nature_skills_proposal_litreview/outputs/literature_collection_curated_2026-07-03/PDFs/mdcath_scidata_mdCATH_A_Large_Scale_MD_Dataset_for_Data_Driven_Computational_Biophysics_10_1038_s41597_024_04140_z.pdf`

Full-text extraction: `autoresearch/tasks/nature_skills_proposal_litreview/outputs/paper_analysis_2026-07-03/fulltext/mdcath_scidata.txt`

Evidence anchors: `MDCATH-S001` to `MDCATH-S006` in `source_maps/downloaded_pdf_source_map.json`.

Zotero parent candidate: `JZ2FHS3P` is the existing project-tagged mdCATH item. Existing PaperForge notes were already found in Zotero, so this file should be treated as the refreshed analysis tied to the newly downloaded PDF.

## Terminology Ledger

| Canonical term | First-use definition | Variants seen | Decision |
|---|---|---|---|
| mdCATH | Molecular-dynamics dataset built from CATH domains | mdCATH dataset | Use `mdCATH`. |
| CATH | Class, Architecture, Topology, Homologous superfamily domain classification | CATH classification system | Spell out contextually, then use `CATH`. |
| MD | Molecular dynamics | molecular dynamics, simulations | Use `MD` after first definition. |
| HDF5 | Hierarchical Data Format version 5 | HDF5 files | Use `HDF5`. |
| RMSD | Root-mean-square deviation | rmsd | Use `RMSD`. |
| RMSF | Root-mean-square fluctuation | fluctuations, rmsf | Use `RMSF`. |
| DSSP | Secondary-structure assignment algorithm | DSSP codes | Use `DSSP`. |
| NNP | Neural network potential | neural network-based potentials | Use `NNP` only where model-training context is explicit. |

## § 1 - 研究问题与重要性

mdCATH 解决的是一个基础设施问题：静态蛋白结构越来越多，结构预测也越来越强，但面向蛋白动力学的、可比较、可训练的大规模 all-atom MD 数据仍然不足。论文在开头明确把 gap 定位为 "datasets that focus on the dynamics of proteins" 的缺乏，并把这个 gap 连接到 function、folding、interactions 和 data-driven modeling（`MDCATH-S001`）。

mdCATH 的答案不是提出新的 trajectory-analysis algorithm，而是构建一个统一 protocol 生成的大规模 domain-level MD dataset。论文报告的数据规模是 5,398 个 domains、134,950 条 trajectories、超过 62 ms accumulated simulation time、每 1 ns 记录 coordinates 和 forces，并提供 RMSD、RMSF、gyration radius、DSSP 等 derived metadata（`MDCATH-S001`, `MDCATH-S004`）。

对我们的 Dynamics Atlas 项目来说，mdCATH 是 MD-based dynamics dataset 的核心 anchor。它能回答的问题包括：在统一 simulation protocol 下，不同 CATH domain class 的 secondary-structure loss、compactness、RMSF、temperature response 如何分布；以及一个 future agent 能否读取 HDF5 schema 后做 subset-gated descriptor analysis。它不能直接回答的问题包括：常温功能态切换、真实生物时间尺度的 ligand/allosteric kinetics、或某个蛋白具体机制，除非后续有专门 subset 分析和外部实验/结构证据。

## § 2 - 前人工作与不足

论文把 mdCATH 放在已有 MD database 的覆盖不足中。GPCRmd、SCoV2-MD、BioExcel-CV19 这类资源对特定系统或特定事件有高价值，但 coverage 偏向目标家族或疫情相关蛋白。MoDEL、Dynameomics、ATLAS、MDDB、MDRepo 等更接近 general MD-database 方向，但论文指出 broader databases 往往受计算成本限制，在 coverage breadth、timescale、replica 和温度条件之间做取舍（`MDCATH-S001`）。

mdCATH 的改进点是三层结构化：第一，用 CATH S20 non-homologous domains 作为覆盖骨架；第二，每个 domain 做 5 个 temperatures 和 5 个 replicas；第三，把 coordinates、forces 和 precomputed descriptors 放进统一 HDF5 结构（`MDCATH-S002`, `MDCATH-S003`, `MDCATH-S004`）。

在 Dynamics Atlas 里，这意味着 mdCATH 和 ATLAS 的角色不同。ATLAS 更像轻量、可浏览、descriptor-oriented 的 MD database；mdCATH 更像高规模、可训练、可 subset 下载的 trajectory/force/descriptors substrate。我们不能把两者合并成同一种证据，而应该在 atlas 中分开标注：coverage breadth、access cost、raw trajectory availability、temperature design、replicate design、force availability、claim ceiling。

## § 3 - 重建作者的思考路径

作者的逻辑可以重建为：

1. Protein function is dynamic，但可用结构资源大多以静态结构或少量 trajectory 为中心。
2. Machine learning potential 和 data-driven biophysics 需要的不只是结构坐标，还需要 forces、consistent simulation settings、diverse conformational states 和 metadata。
3. CATH 已经提供 domain-level taxonomy，适合作为 proteome-wide sampling frame。
4. 如果从 CATH S20 non-homologous set 出发，做严格过滤、统一 system preparation、统一 simulation protocol，再用 HDF5 打包，就能得到一个既广又同质的数据集。
5. 为了让数据不仅是文件集合，作者用 temperature denaturation、RMSF/secondary-structure relationship、CATH-class thermodynamics 和 secondary-structure loss kinetics 证明数据中有物理合理信号（`MDCATH-S005`）。

这个思路对我们很重要：mdCATH 是一个 dataset-construction paper，而不是 one-paper mechanistic discovery。读它时应关注 schema、field semantics、sampling design、validation logic，而不是期待它给出某个通用 "slowest mode" 的最终答案。

## § 4 - 核心 Intuition

mdCATH 的核心 intuition 是：如果要让机器学习或统计分析理解 protein dynamics，必须有覆盖广、协议一致、带 forces 和 descriptors 的 all-atom trajectory substrate。CATH 提供结构分类空间，temperature ladder 提供扩展 sampling，replicates 提供统计重复，HDF5 schema 提供可程序化访问。

换句话说，mdCATH 不是在证明 "高温 MD 就是生物功能动力学"；它是在构建一个可以系统比较 domain dynamics、stability response 和 simulated unfolding behavior 的标准化数据底座。

## § 5 - 具体方法与完整 Pipeline

论文 pipeline 可以拆成九步。

1. 从 CATH release 4.2.0 的 S20 non-homologous domains 出发，初始集合是 14,433 个 domains。
2. 过滤到 50-500 amino acids 的 domain 范围，排除 backbone non-contiguous、non-standard amino acids、过大 solvation box 等不适合统一 simulation 的系统。
3. 对结构做 pH 7 protonation、charge-state assignment、proton placement 和 H-bond network optimization。
4. 使用 capped termini、TIP3P water、0.150 M NaCl、CHARMM22* force field、HTMD building workflow 和 ACEMD simulation engine。
5. 每个系统先做 20 ns NPT pre-equilibration，前 10 ns 对 C-alpha 和 heavy atoms 加 restraints，后 10 ns 去掉 restraints。
6. 从 equilibration 后的 final configuration 出发，对每个 domain 启动 25 条 production simulations：5 temperatures x 5 replicas。温度为 320 K、348 K、379 K、413 K、450 K。
7. Production 使用 NVT ensemble 和 Langevin thermostat；atom positions 和 forces 每 1 ns 记录一次。论文明确指出 1 ns sampling rate 能解析相对较慢的 conformational changes，但不适合 faster motions，例如 solvent-exposed side-chain rotations（`MDCATH-S003`）。
8. 每个 domain 一个 HDF5 file，字段包括 chain、element、residue ID、PDB/PSF string、coords、forces、simulation box、DSSP、gyrationRadius、RMSD、RMSF 等（`MDCATH-S004`）。
9. 使用 technical validation 分析展示 dataset 的物理合理性，包括 temperature denaturation、fluctuation-unfolding cooperativity、CATH class-wise denaturation thermodynamics 和 secondary-structure loss kinetics（`MDCATH-S005`）。

对我们自己的 agent toolkit 来说，合理 implementation 应该是：先读取 manifest/schema；再选小 subset；再读取 existing fields；最后生成 descriptor report。不能直接下载全库，也不能把 full dataset existence 当作已经完成 dynamics analysis。

## § 6 - 核心数学推导

这篇文章没有提出新的数学推导。它的 "math" 主要是 descriptor 定义和统计聚合。

RMSD 描述 trajectory frame 相对起始结构或参考结构的整体偏移；RMSF 描述每个 residue 的 fluctuation；radius of gyration 描述 compactness；DSSP secondary-structure occupancy 描述 alpha/beta/coil 的时间比例。作者把这些 descriptors 按 temperature、CATH class、time 和 residue position 聚合，用来验证 simulated unfolding 和 local fluctuation 的合理关系。

本项目必须注意：这些 descriptors 可以定位在 Dynamics Atlas 的 "computed trajectory descriptors" 区域，但只有在我们实际读取 HDF5 或运行分析后，才能成为本项目自己的结果。当前文件只记录论文中的 dataset design 和作者验证。

## § 7 - 实验设计与结论

作者的 validation 不是为了证明某个模型准确率，而是证明 dataset 有物理信号、结构合理、可被下游使用。

第一个验证问题：temperature ladder 是否诱导合理 denaturation behavior。作者比较 secondary-structure fraction 和 radius of gyration。低温下多个 domains 大多围绕均值波动；在示例 subtilisin inhibitor-like domain 中，413 K 开始 destabilization，450 K 出现 secondary structure drop 和 radius of gyration increase（`MDCATH-S005`）。

第二个验证问题：local structural stability 与 residue fluctuation 是否一致。作者比较 residue-level alpha/beta occupancy 和 RMSF，发现 high-temperature 下 secondary-structure participation 更连续，并与 RMSF 大致反相关（`MDCATH-S005`）。

第三个验证问题：CATH class 是否能解释 denaturation pattern。作者用 ternary plots 按 CATH class 和 temperature 展示 helical、strand、coil/turn content 的分布，观察到高温下 helical/strand 向 coil/turn shift，strand content 更抗 thermal denaturation（`MDCATH-S005`）。

第四个验证问题：能否做 class-conditioned kinetics-style summary。作者按 class 聚合 secondary-structure conservation over time，显示不同 domain classes 有不同 cooperativity regimes（`MDCATH-S005`）。

这些结果支持 mdCATH 作为 stability/unfolding/flexibility descriptor substrate。但它们不支持把所有 high-temperature conformations 解读为 physiological functional modes。

## § 8 - Take-aways

mdCATH 应该在 Dynamics Atlas 里被标成 `MD-derived large-scale dataset`，证据等级高，但 access cost 和 claim ceiling 也高。

它支持：

- dataset-level coverage and schema analysis;
- domain-class-conditioned stability/flexibility descriptors;
- temperature-response and unfolding taxonomy;
- future ML potential / data-driven biophysics framing;
- future subset-gated trajectory tooling.

它不直接支持：

- 一步得到每个 protein 的 biological slowest mode;
- 常温 ligand/allostery mechanism;
- kinetics/free-energy conclusions from our project;
- side-chain fast-rotamer dynamics below 1 ns sampling resolution;
- any claim requiring actual HDF5 parsing before we run it.

## § 9 - 最脆弱的假设

最脆弱的假设是：high-temperature MD response 能作为 broadly useful protein dynamics proxy。这个假设有条件成立，但不能无条件外推。

320-450 K 的 temperature ladder 有利于扩大 conformational sampling、诱导 unfolding/stability differences，并让 ML 模型看到更宽的 conformational space。可是功能动力学通常发生在生理温度、特定 ligand/protein context、特定 timescale 和特定 environment 中。一个 domain 在 450 K 的 secondary-structure loss，可能说明热稳定性，也可能只是高温 denaturation，不一定说明常温功能构象切换。

因此在 proposal/literature review 中，mdCATH 应作为 "large-scale simulated dynamics and stability dataset"，而不是直接作为 "experimental functional dynamics map"。

## § 10 - 最小复现实验

一周内最小实验应避免全库下载。

目标：验证 future toolkit 能否安全读取 mdCATH subset 并生成 source-grounded descriptor card。

Data：选择 1-3 个小 domain HDF5 files，最好覆盖 320 K 和 450 K，同一 domain 少量 replicas。

Implementation：读取 HDF5 schema，提取 coords、DSSP、gyrationRadius、RMSD、RMSF。只用已有 fields，不重新跑 MD，不做 PyEMMA/TICA，不做 free-energy claim。

Measurements：输出 per-domain table：domain ID、CATH class、temperature、replica、frames、Rg trend、secondary-structure occupancy、RMSF availability、file size、field provenance。

Support result：agent 能保留 unit、temperature、replica 和 field provenance，并正确标注 "paper states" 与 "computed locally" 的区别。

Failure result：agent 混淆 temperatures、units、replicas，或在未分析 raw data 时生成 kinetics/mechanism claims。

## § 11 - 最强反例设计

强反例一：选择一组已知 function-relevant conformational changes 的系统，比较 mdCATH high-temperature descriptors 是否能预测常温 functional state switching。如果 descriptors 主要捕捉 thermal denaturation 而不能捕捉 functional mode，说明 mdCATH 对 Dynamics Atlas 的角色应限制在 stability/flexibility/unfolding evidence，而不是 broad mechanism evidence。

强反例二：选同一 domain family 的外部 MD 或实验 flexibility/stability evidence，与 mdCATH descriptor ranking 比较。如果统一 force-field/protocol 产生的 ranking 与外部证据不稳定，则 mdCATH 更适合 pretraining 和 hypothesis triage，而不适合未经校准的 biological conclusion。

强反例三：对 side-chain/local fast fluctuations 做分析需求。如果 1 ns recording interval 无法解析 fast rotameric side-chain motion，则 mdCATH 对 "side-chain fluctuation" taxonomy 的支持必须限定为 low-frequency/stored-frame descriptors，而不是完整 fast dynamics。

## § 12 - Follow-up Research Idea

非增量方向：构建一个 `Dynamics Dataset Triage Agent`。

Motivating limitation：mdCATH、ATLAS、qFit、NMR ensembles、DynDom、PED、MegaScale/MegaSim 这类资源代表不同 evidence classes。当前最大风险不是不会算，而是把 MD trajectories、experimental ensemble, static alternative conformers, high-temperature unfolding, learned/generated ensembles 和 domain-motion geometry 混成同一种 "dynamics"。

Borrowed idea：data cards / model cards / evidence grading。

First experiment：对每个 dataset 自动生成 claim card：source type、raw data availability、temperature/replica/time resolution、experimental vs computational status、observable dynamics scale、required analysis method、claim ceiling、download/access cost。mdCATH card 会明确：raw MD + forces + descriptors; large-scale; subset-gated; supports stability/unfolding/flexibility; does not by itself establish physiological kinetics.

## Nature-Reviewer-Style Critique

Reviewer 1 emphasis - technical soundness: The dataset construction is strong because it uses uniform setup, broad CATH sampling, explicit HDF5 schema, forces, multiple temperatures, multiple replicas, and validation descriptors. The main technical weakness for our use is not the dataset itself but the interpretation boundary: high-temperature, 1 ns-saved trajectories cannot automatically support fast side-chain dynamics or physiological mechanism claims.

Reviewer 2 emphasis - originality and significance: mdCATH is highly significant as a data resource because it packages broad domain-level all-atom MD with forces and descriptors. Its broader value is strongest for ML potentials, stability/unfolding analysis, and data-driven biophysics. For a Nature-style broad-interest argument, the dataset is enabling infrastructure rather than a single mechanistic discovery.

Reviewer 3 emphasis - interdisciplinary readability: The paper is unusually useful for agent design because the schema, statistics, validation analyses, usage notes, and code availability are explicit. A nonspecialist reader can understand why the dataset exists, but downstream users still need strong guardrails to avoid overinterpreting high-temperature simulations as biology.

Consensus: In the Dynamics Atlas, mdCATH should be a P0/P1 core MD dataset, but all downstream claims must be subset-gated and descriptor-grounded.

## Source Discipline

- Paper states: dataset scale, CATH filtering, 5 temperatures, 5 replicas, 1 ns coordinate/force recording, HDF5 organization, derived descriptors, technical validation themes.
- Reasonable inference: role in Dynamics Atlas, subset-first policy, claim ceiling for high-temperature dynamics.
- Speculation: the proposed Dynamics Dataset Triage Agent and specific future subset experiments.

