---
title: DynaMune 怎样用 ENM 和 NMA 比较两套蛋白系统
paper_title: "DynaMune: An Integrated Ensemble-Based Framework for Comparative Protein Dynamics Using Elastic Network Models"
author: Amirtesh Raghuram
source_status: Research Square method preprint, not peer reviewed in the supplied source
doi: 10.21203/rs.3.rs-8999467/v1
analysis_date: 2026-08-23
priority: P2-development-stress-test
paper_role: frozen-table-derivation-unseen-current-selector-repair-unseen-but-project-policy-exposed-method-paper
source_pdf: Dynamics_Atlas_System_Audit_20260710_115646_CST/sources/DynaMune_rs-8999467_v1.pdf
markdown_derivative: autoresearch/tasks/dynamics_atlas_dynamune_multi_system_selectivity_20260823/outputs/sources/DynaMune_rs-8999467_v1.md
converter: pdftotext -layout fallback after the pdf-to-markdown native dependency was unavailable
conversion_limit: equations, figures, tables and multi-column order checked against the PDF where material
zotero_status: parent_item_not_found_by_title_and_doi_search; child_note_not_created
exposure_status: preprint and AdK case analyzed locally in July 2026 and used in earlier policy, schema and development-harness work; not a source of the frozen 33-row registry and not used in the August selector repairs
claim_ceiling: paper analysis and previously exposed local development reference only; no genuinely-new-paper, blind, held-out or transfer claim
---

# DynaMune 怎样用 ENM 和 NMA 比较两套蛋白系统

## §0 先用一页讲清这篇论文

### 这篇论文在问什么

这篇预印本想解决一个很实际的问题。Normal mode analysis（NMA）和 elastic network model（ENM）计算便宜，也能描述蛋白的大尺度协同运动，但常见工具把 mode calculation、PCA、PRS、domain／hinge analysis、pocket analysis 和 interface contacts 分散在不同程序里。作者问的是，能不能把这些步骤放进同一套参数化 workflow，并用两种机制完全不同的系统说明它既能分析蛋白内部的构象转换，也能分析蛋白复合物界面的重排。

论文选了两个案例。Adenylate kinase（AdK）代表 open／closed domain transition；ACE2–Spike 代表 ligand binding 后的 mode redistribution 与 interface persistence。

### 作者怎么做

1. 用 ProDy 计算 ANM、GNM、PRS、PCA、domain／hinge、pocket 和 deformation metrics。
2. 从 PDB 结构出发，沿低频 mode 生成少量 conformers，再把这些 conformers 当成结构集合分析。
3. 对 AdK 的 1AKE closed state 和 4AKE open state分别计算，并与 B-factor、既有 hinge／cracking 文献和已知 domain motion 对照。
4. 对 apo ACE2（1R42）和 ACE2–Spike complex（6M0J）比较 mode overlap、ΔRMSF、deformation projection、contact map、SASA 与 contact persistence。
5. 把结果与 PDBsum、晶体结构、cryo-EM、MD 和已有 NMA 文献进行 source-reported comparison。

### 论文自己的答案是什么

`Paper states`：DynaMune 在 AdK 上恢复了 CORE–LID–NMP transition、hinge／cracking pattern 和 open／closed flexibility difference；在 ACE2–Spike 上恢复了 Lys353-centered hotspot、multi-mode deformation 和 persistent contact network。作者据此认为，统一的 ENM/NMA workflow 可以用很低的计算成本支持机制解释。

这个结论来自论文自己的分析和与既有文献的一致性，不是 independent held-out validation。论文没有报告 blind test、cross-validation、parameter sensitivity envelope 或外部 benchmark set。

### 最脆弱的假设或适用边界

最脆弱的假设是，把“从输入结构和同一模型生成的结果与已有结构描述一致”当成“mechanism 被验证”。AdK 的 PCA 来自 ANM 生成的 conformers；ACE2 interface 又用同一个 6M0J 结构生成 contacts，再与该结构的 PDBsum map 对照。这些检查能发现实现错误，却不能独立证明动力学机制。

论文还存在三个直接影响解释的内部不一致。

- AdK closed state 用 20 Å ANM cutoff，open state 用 15 Å，因此 state difference 与 parameter difference 混在一起。
- Interface contact cutoff 在 Methods 写 4.5 Å、Table 1 和 Results 写 5.0 Å。
- Stable contact 在 Table 1 定义为至少 75%，Figure 17 caption 又写至少 50%；正文说 20 conformers，默认和 AdK case 又写 10 conformers。

### 对当前项目有什么用

这篇论文适合做 Rules Table 的压力测试，不适合做规则来源。它同时带来 PDB coordinates、ANM/GNM modes、model-generated conformers、B-factors、mode overlaps、contact maps 和 literature comparison，能检验当前 selector 是否会主动询问 source identity、parameter comparability、validation independence、forward model 与 claim ceiling。

### 它不能替我们决定什么

这篇预印本不能替项目决定 ENM conformers 是否代表 thermodynamic populations、transition rates 或真实 pathways。它也不能证明 Rules Table 已经覆盖 NMA/ENM，不能作为 Agent effectiveness、production readiness 或 cross-system generalization 的证据。

### 深读、来源与相关决定

- 本地 PDF（该链接目标未纳入本包）
- Markdown derivative（该链接目标未纳入本包）
- 任务 Context Receipt（该链接目标未纳入本包）
- 当前授权边界见 `DA-20260820-015`。本次只测试 Stage-1 review-obligation selection。

## §1 研究问题与重要性

论文面对的具体失败不是“没有 NMA”，而是分析路径碎片化。研究者可以用 ProDy、iMODS、WEBnm@ 或 Bio3D 计算某一类 mode 或 fluctuation，但要把 apo／complex comparison、ensemble generation、interface persistence、hinge segmentation 和统一输出连起来，仍需要自己写脚本、选参数并解释不同模块的关系。

作者认为，这种碎片化会带来两类问题。

- 同一分析在不同人手里使用不同 cutoff、mode count 和 ensemble size，结果难以复现。
- 单一 module 的输出容易被直接解释成 mechanism，缺少跨 module 的相互约束。

如果统一 workflow 真能稳定工作，它的价值不是替代 MD，而是把 ENM/NMA 变成一种快速的 hypothesis-generation 与 comparative screening 工具。对当前项目而言，真正重要的问题是它能否保留参数、source、comparability 和 claim ceiling，而不是能生成多少张图。

## §2 前人工作与不足

`Paper states`：ProDy 提供 ANM、GNM、PRS 和 ensemble analysis 的计算核心；iMODS、WEBnm@ 与 Bio3D 提供不同程度的 NMA 功能。DynaMune 的主要贡献是把这些分析组织成 CLI／web workflow，并增加自动 apo–complex comparison、contact persistence、domain／hinge 和 pocket outputs。

论文没有提出新的 ENM physical model，也没有提出新的 statistical estimator。它的创新主要是 integration、parameter packaging 和 report standardization。Table 2 的 feature comparison 全由论文作者整理，缺少运行级 benchmark、版本锁定和失败案例，因此只能支持“作者设计了更完整的 feature surface”，不能单独支持“比现有工具更可靠”。

最接近的科学基础包括 Tirion-style elastic network、ANM/GNM、PRS、mode-overlap deformation analysis 和 ProDy。论文把这些 established components 组合起来，但没有独立证明组合后的解释一定比单独模块更准确。

## §3 重建作者的思考路径

可以把作者的推理还原成五步。

1. Static structures 很多，full MD 太贵，ENM/NMA 适合快速筛查。
2. 现有工具能做局部计算，却没有统一的 cross-state workflow。
3. 如果把 established modules 放在相同输入和报告框架里，就能降低人工脚本与参数漂移。
4. 选择一个 domain transition system 和一个 protein–protein interface system，检查同一 workflow 能否恢复两种已知机制。
5. 如果输出与既有结构和动力学文献一致，就把 workflow 定位为 scalable mechanistic interpretation platform。

前四步合理。第五步跨得太远，因为“与已知描述一致”同时包含 implementation sanity check、same-structure reconstruction、literature concordance 和真正的 independent validation。论文没有把这四种证据拆开。

## §4 核心 Intuition

蛋白的低频 collective modes 往往与大尺度功能运动方向相近。把多个 ENM/NMA-derived views 放在同一 source、参数与坐标框架里，可以快速发现 domain coupling、hinge、interface hotspot 和可能的 deformation direction。

这个 intuition 适合提出“哪里值得进一步测量或模拟”，不适合直接给出 population、kinetics、free energy 或 causal mechanism。论文在 Limitations 中承认 ENM conformers 不是 thermodynamically sampled states，也不能描述 solvent、side-chain rearrangement、anharmonic motion 或 time-dependent kinetics（PDF p.21，§4.5）。

## §5 具体方法与完整 Pipeline

### 输入与预处理

- 输入是 experimentally determined 或 predicted PDB coordinates。
- AdK 使用 closed 1AKE 和 open 4AKE；ACE2 使用 apo 1R42 与 bound 6M0J。
- 论文称结构在 PyMOL 中人工清理，去掉 solvent 与 heteroatoms；没有给出处理脚本或 coordinate receipt。

### ENM/NMA 与 ensemble generation

- ANM 用 residue-distance network 建 Hessian，计算前 20 个 non-zero modes。
- 默认 ANM cutoff 为 15 Å，GNM 为 10 Å，默认生成 10 conformers，sampling RMSD 约 0.8–1.5 Å。
- AdK closed case 改用 20 Å ANM cutoff，open case 保持 15 Å。这个 change 没有 sensitivity analysis。
- PCA 在 ANM-generated ensemble 上计算，因此 ANM–PCA agreement 不是独立 validation。

### 比较与解释模块

- GNM 给 fluctuation magnitude 与 theoretical B-factor，不提供 direction。
- PRS 用 inverse Hessian 分析 residue perturbation effectiveness／sensitivity。
- Domain／hinge 通过 motion-correlation clustering 与 fluctuation minima 定位。
- Pocket module比较 RMSF、shape variance、volume fluctuation 与 accessibility。
- Apo／complex module 比较 eigenvectors 与 ΔRMSF。
- Deformation mapping 把两个结构的坐标差投影到 apo ANM modes。
- Contact module计算 geometric contacts、SASA、hydrophobicity 与 conformer-level persistence。

### 输出

Workflow 输出 CSV、PNG、JSON summary、PyMOL scripts 和 PDB conformers。论文声称可用 CLI 和 Flask web interface，但 supplied PDF 没有给出 code repository、release tag、test data 或 exact command，所以“open source”和“可复现”在本地来源中无法核实。

## §6 核心数学推导

论文是 algorithmic／empirical method paper，没有给出完整数学推导。下面三个量是理解结果所需的标准解释，不是论文新提出的公式。

### Mode 与 conformer

ANM 把选定 cutoff 内的 residue pairs 视作 harmonic network。对 Hessian 做 eigen-decomposition 后，低 eigenvalue 对应低频 collective modes。沿 mode 生成 conformer 可以概念化为

`x_k = x_0 + Σ_i a_{ki} v_i`

其中 `v_i` 是 mode vector，`a_{ki}` 是人为设定的 displacement amplitude。因为 `a_{ki}` 不是由 equilibrium sampling 得到，conformer frequency 不能解释成 population，conformer index 也不是 time。

### Deformation overlap

结构差向量 `d` 与 mode `v_i` 的 squared overlap 通常写成

`O_i = (d · v_i)^2 / (||d||^2 ||v_i||^2)`

它回答“这个 mode 与已知结构差方向有多像”，不回答该 transition 会不会发生、发生多快或自由能多高。ACE2 case 的最大 individual overlap 约 0.13，只能支持 deformation distributed across several modes，不能单独证明 allostery-driven pathway。

### Contact persistence

某 residue pair 的 persistence 可以写成

`p_ij = N_contact(i,j) / N_conformers`

这个值受 contact cutoff、conformer generation amplitude、ensemble size 和输入 geometry 共同决定。没有 sensitivity analysis 时，75% 或 50% 的类别边界只是 paper-specific reporting threshold，不能冻结成 universal rule。

## §7 实验设计与结论

### AdK 的 open/closed 对照究竟测到了什么

论文用 1AKE 表示 closed state，用 4AKE 表示 open state。两份结构都先在 PyMOL 中去掉 solvent 和 heteroatoms。closed state 的 ANM cutoff 是 20 Å，open state 是 15 Å；两边都计算 20 个 non-zero modes，并各生成 10 个 conformers（Methods §3.1.1–3.1.3，PDF pp.10–11；Markdown lines 398–425）。

`Paper states`：closed state 的 fluctuation 更小、conformer cluster 更窄，open state 的 substrate-access region 更灵活；ANM 与 PCA 的前三个分量接近完全对齐，theoretical B-factor correlation 从 closed 的 0.28 升到 open 的 0.78。作者据此写成 state-dependent transition mechanics。

这组对照没有把 state effect 和 parameter effect 分开。20 Å 与 15 Å 会建立不同的 elastic network，PCA 又是在 ANM-generated conformers 上计算。现有结果支持 workflow 能从两个 endpoint 生成内部一致、与既有描述相符的图和指标；它没有独立识别 pathway、kinetic stabilization 或 allosteric mechanism。项目在 2026-07-10 的旧 AdK audit 已经量化过这一混杂，不能把本轮重新包装成首次发现。

### ACE2–Spike 的 multi-mode deformation

论文比较 apo ACE2 1R42 chain A 与 bound complex 6M0J 中的 ACE2，并称两边使用相同的 ensemble generation 和 normal-mode parameters（Methods §3.2.1，PDF p.15；Markdown lines 562–570）。apo/complex mode matrix 的 mean diagonal overlap 是 0.015，mean best-match overlap 是 0.316。把 endpoint deformation 投影到 apo modes 后，mode 6 与 mode 20 的 squared overlap 分别约为 0.13 和 0.10，其余选中 modes 单个约为 0.02–0.03（Results §3.2.2–3.2.3，PDF pp.15–16；Markdown lines 571–623；Figure 13–14，PDF pp.37–38）。

`Paper states`：没有一个 mode 主导 1R42 到 6M0J 的结构差，作者把结果解释为 Spike binding 后的 mode redistribution 和 multi-mode deformation。

`Reasonable inference`：这些数值说明，给定 endpoint difference 与这套 ANM 表示，结构差不能由某一个 apo mode 解释。它们不提供 molecular time order，也没有把 bound structure、crystal context、alignment choice 与真正的 binding-induced ensemble change 分开。`allostery-driven engagement` 和 `transition-ready architecture` 超出了这组 overlap 本身能证明的范围。

### ACE2–Spike 的 contact persistence

contact module 从 6M0J 几何与 ANM-generated conformers 计算 interface contacts，再与同一 6M0J 的 PDBsum interaction map 比较。论文报告 8 对 inter-chain contacts，其中 6 对在 20 个 conformers 中超过 75%，Lys353–Asn501 与 Lys353–Tyr505 为 100%（Results §3.2.4–3.2.5，PDF pp.16–17；Markdown lines 625–695；Figure 17，PDF p.40）。

`Paper states`：这些 contact pairs 恢复了 Lys353-centered hotspot 和 crystallography/cryo-EM 文献中的 central triad。

这里的 validation 主要检查实现与几何一致性。PDBsum 和 DynaMune 都从 6M0J 出发；ANM conformers 也由该结构生成。它们不是独立数据。配置记录还互相冲突：Methods 写 4.5 Å contact cutoff，Table 1 与 Results 写 5.0 Å；Table 1 把 stable 定义为至少 75%，Figure 17 caption 写至少 50%；默认和 AdK 使用 10 个 conformers，ACE2 contact timeline 使用 20 个。没有 exact run receipt 时，contact persistence 的类别无法被独立重现。

## §8 Take-aways

- DynaMune 的长处是把 established ENM/NMA modules 放进同一个执行面。论文展示了 module coverage，没有给出足以验证可靠性的 frozen run artifact。
- ENM-generated conformers 是 model outputs。它们没有 Boltzmann weights、physical time 或 transition rates。
- 同一输入结构衍生出的 PCA、contact map 和 PDBsum comparison 可以做 implementation sanity check。它们不能同时充当 independent validation。
- 参数属于 claim 的一部分。AdK 的 20 Å/15 Å cutoff 和 ACE2 contact 阈值冲突都足以改变解释。
- 当前深读不能叫新论文 blind test。DynaMune 和 AdK 已在 7 月被本地分析，并影响过早期 policy/schema/harness；它只没有进入冻结的 33-row registry，也没有参加 8 月 selector repair。

## §9 最脆弱的假设

论文最脆弱的假设，是把 construction-linked agreement 当成 mechanism validation。

AdK 的 PCA 使用 ANM-generated ensemble；ACE2 的 contact comparison 从 6M0J 生成 contacts，再拿同一结构的 PDBsum map 作参照；mode deformation 又以 1R42/6M0J endpoint difference 为目标。这样的 agreement 会在实现正确时自然出现。它能排查 pipeline 有没有明显跑偏，却无法回答这套表示是否恢复了 independent ensemble、physical pathway 或 binding causality。

一旦这个假设不成立，论文仍然可以保留为 integrated analysis workflow。需要降级的是 `validated mechanistic interpretation`，不是所有软件输出。

## §10 最小复现实验

一周内最有信息量的复现，是拆开 AdK state 与 ANM cutoff。

1. 使用同一批 1AKE 与 4AKE coordinates，保留 AP5-bound history 和 coordinate revision。
2. 对两份结构都运行 15 Å 与 20 Å 两档 cutoff，固定 gamma、20 modes、conformer count、displacement amplitude、alignment 和随机种子。
3. 记录 network edge count、前 k 个 modes 的 subspace overlap、RMSF、B-factor correlation、hinge/domain assignment 与 endpoint-deformation overlap。
4. 用 2×2 design 分开 structure main effect、cutoff main effect 与 interaction；把 1AKE/4AKE endpoint 只作为几何参照，不当作 held-out validation。

若 open/closed 的方向与主要结论在两个 cutoff 下稳定，而且 cutoff-only difference 明显小于 state difference，可以支持参数稳健的 endpoint/mode agreement。若结论随 cutoff 翻转或同一结构的 cutoff effect 与 state effect 同量级，论文当前的 state-dependent mechanism 解释就不成立。两种结果都不产生 kinetics、population 或 free-energy 结论。

## §11 最强反例设计

最强反例是一组 parameter-only pseudo-transition。固定 1AKE coordinates，只把 ANM cutoff 从 15 Å 改到 20 Å；再固定 4AKE 做同样处理。如果这种参数变化能复制论文归因于 open/closed state 的 mode overlap、domain count、PRS propagation 或 fluctuation shift，state-based mechanism 就不是这些输出的唯一解释。

ACE2 contact claim 还有一个更便宜的负控。保持 6M0J 不变，只改变 contact cutoff、conformer count 和 persistence threshold。如果 Lys353 hotspot 始终保留，只说明 starting geometry 很强；如果 stable/intermediate 分类大幅变化，就说明 persistence label 依赖 paper-specific configuration。两种情况都不能把 contact persistence 当成独立动力学验证。

## §12 Follow-up Research Idea

`Design proposal`：把低成本 dynamics workflow 改造成 intervention-aware evidence graph，而不是继续增加分析模块。

每个输出同时记录 source structure、condition history、parameter vector、construction lineage、comparison target 与 validation independence。系统自动生成最小 counterfactual lattice，例如固定结构改 cutoff、固定 cutoff 换结构、固定 contact geometry 改 aggregation threshold。只有在这些 intervention 下保持稳定的结论，才进入更高的 claim level。

第一项实验直接复用 AdK 与 ACE2。AdK 检验 structure×cutoff，ACE2 检验 input geometry×contact cutoff×persistence threshold。结果不是再给 DynaMune 加一张图，而是回答每个 mechanistic sentence 究竟由 structure、parameter、derived representation 还是 independent evidence 支撑。

## Gate-aware rule extraction

以下条目是 source-linked rule candidates，不是冻结 protocol。

### 参数与 state 必须解耦

- **Gate**：G1 claim/semantics；G2 source quality/uncertainty。
- **Locator 与身份**：Methods §3.1.2，PDF p.10，Markdown lines 404–410。`Paper states` 1AKE 使用 20 Å，4AKE 使用 15 Å。参数混杂的后果是 `Reasonable inference`。
- **Required fields**：input structure revision、condition/ligand history、cutoff、gamma、mode count、conformer count、amplitude、seed、alignment、sensitivity grid。
- **Allowed relation**：在共享参数或完整 sensitivity grid 下比较 state effect。
- **Validation route**：structure×parameter factorial replay。
- **Abstention route**：`PARAMETER_CONFOUNDED_STATE_COMPARISON`。
- **Threshold status**：calibration-required；15 Å 或 20 Å 都不能升级为 universal threshold。

### ENM conformers 没有 population 或 time semantics

- **Gate**：G1 claim/semantics；G5 claim ceiling/human review。
- **Locator 与身份**：Limitations §4.5，PDF p.21，Markdown lines 862–873。`Paper states` generated conformers are not thermodynamically sampled states and ENM cannot capture time-dependent kinetics。
- **Required fields**：generator、mode/amplitude、sampling rule、weight semantics、time semantics、allowed claim level。
- **Allowed relation**：model-generated structural variation 或 endpoint-aligned deformation。
- **Validation route**：独立 trajectory/experiment 或明确的 thermodynamic/kinetic model。
- **Abstention route**：population、rate、residence time、pathway 与 free-energy claim 进入 `NOT_COMPARABLE` 或 `HUMAN_REQUIRED`。
- **Threshold status**：not applicable。

### construction-linked comparison 不能冒充 held-out validation

- **Gate**：G4 integration/validation；G5 claim ceiling/human review。
- **Locator 与身份**：Methods §2.2.1 与 Results §3.1.3，PDF pp.5,11，Markdown lines 183–193 与 419–425；Results §3.2.4，PDF p.16，Markdown lines 625–654。ANM→PCA 与 6M0J→PDBsum 的 dependence 是 `Reasonable inference`。
- **Required fields**：construction source IDs、fit target、comparator source IDs、data overlap、parameter-selection exposure、`validation_independence`。
- **Allowed relation**：source-reported implementation consistency。
- **Validation route**：在模型、参数与阈值冻结后使用独立 dataset 或 predeclared perturbation。
- **Abstention route**：共享输入或 outcome-informed comparator 标为 `SOURCE_REPORTED_NON_HELD_OUT`。
- **Threshold status**：not applicable。

### 配置冲突必须 fail closed

- **Gate**：G0 source registration；G2 source quality/uncertainty。
- **Locator 与身份**：Methods §2.2.8、Table 1、Execution Workflow、Results §3.2.4–3.2.5 与 Figure 17，PDF pp.7–8,16–17,40；Markdown lines 243–311,321–325,625–695,1255–1265。冲突值均为 `Paper states`。
- **Required fields**：exact contact cutoff、interaction type、ensemble size、persistence threshold、software version、command/run receipt。
- **Allowed relation**：只解释能绑定到同一 exact configuration 的结果。
- **Validation route**：配置 readback 与 threshold sensitivity。
- **Abstention route**：无法确定实际配置时返回 `CONFIGURATION_IDENTITY_UNRESOLVED`。
- **Threshold status**：paper-specific and internally inconsistent；禁止冻结为 universal percentage rule。

### 删除 ligand 不会改写结构的 condition history

- **Gate**：G0 source registration；G1 claim/semantics。
- **Locator 与身份**：System Preparation §3.1.1，PDF p.10，Markdown lines 398–403；1AKE 的 AP5-bound provenance 来自 PDB/source audit。前者是 `Paper states`，后者是旧本地 source audit。
- **Required fields**：ligand history、heteroatom-removal step、sample condition、structure revision、assembly/chain。
- **Allowed relation**：AP5-stabilized closed endpoint 与 unligated open endpoint 的几何比较。
- **Validation route**：保留 condition mismatch，并另找真正 apo closed source 或 matched perturbation。
- **Abstention route**：禁止把 ligand-stripped coordinates 写成 experimentally apo closed state。
- **Threshold status**：not applicable。
