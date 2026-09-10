---
title: "PaperForge — Henot et al. 2022 HSP90 ATP-lid"
paper_title: "Visualizing the transiently populated closed-state of human HSP90 ATP binding domain"
authors: "Henot et al."
year: 2022
journal: "Nature Communications"
doi: "10.1038/s41467-022-35399-8"
paper_role: "HSP90 development proof-of-concept primary source"
priority: "P0"
full_text_status: "article and supplement checked"
local_article_pdf: "autoresearch/tasks/dynamics_atlas_hsp90_feasibility_20260725/inputs/henot_2022_hsp90_article.pdf"
local_supplement_pdf: "autoresearch/tasks/dynamics_atlas_hsp90_feasibility_20260725/inputs/henot_2022_hsp90_supplement.pdf"
claim_matrix: "autoresearch/tasks/dynamics_atlas_hsp90_paper_comparison_20260729/outputs/HSP90_PAPER_ATLAS_CLAIM_MATRIX.md"
zotero_status: "parent_item_not_found_local_markdown_is_auditable_fallback"
zotero_searches: "exact title; DOI; Henot HSP90; HSP90 ATP-lid — no item found on 2026-07-29"
zotero_note_key: null
zotero_note_scope: null
child_note_status: "not_created_parent_item_missing"
tags:
  - project-protein-dynamics
  - priority-p0
  - paper-role-development-packet
  - claim-extracted
---

# Henot et al. 2022：这篇 HSP90 论文真正建立了什么，以及 Atlas 应该怎样借用

> **阅读定位。** 这篇论文不是一个“heterogeneous dynamics workflow”方法论文。它是一项多模态结构生物学研究：作者让 NOESY、突变、CPMG、NMR structure refinement 和 seeded MD 分别回答不同层级的问题，再用一个受限的联合模型把证据连起来。对 Dynamics Atlas 最重要的不是复制它的全部生物学结论，而是学习它怎样区分 structural support、dynamic exchange、thermodynamic population 和 mechanistic plausibility。

> **来源纪律。** 下文用四种标签区分陈述强度：`[论文明确陈述]`、`[本项目直接观察]`、`[合理推断]`、`[前瞻建议]`。逐项 paper-versus-Atlas locator、allowed wording 和 forbidden wording 见配套 claim matrix（该链接目标未纳入本包）。

## § 1 — 研究问题与重要性

### 论文要解决的具体失败

`[论文明确陈述]` 人 HSP90α N-terminal domain 的 ATP-lid 在晶体结构中主要呈 open conformation，但溶液 NMR 出现了无法由一个 open structure 同时解释的 NOE 与 line broadening。真正的问题不是“结构会不会动”——这件事并不新——而是：

1. 溶液中是否存在一个此前未直接观察到的 closed ATP-lid conformation；
2. open 与 closed 是否真的发生交换；
3. minor state 的 population 和 exchange rate 是什么；
4. seeded MD 是否支持 closed structure 在微秒窗口内至少具有 metastable plausibility，并给出可能的 opening path。

这个问题重要，是因为 HSP90 的 ATP-lid 覆盖 nucleotide/drug-binding site。若溶液中存在低占比 closed state，它会改变我们理解 ligand recognition、drug design 和 HSP90 conformational cycle 的方式。

### 为什么 Atlas 选择它

`[本项目直接观察]` 这个 packet 同时具有：

- unordered NMR structural ensembles：8B7I（R60A-informed open）与 8B7J（R46A-informed closed），各 20 models；
- time-ordered seeded MD：20 open-start + 20 closed-start trajectories，每条 1.02 μs；
- source-provided contact-violation time series；
- WT CPMG-derived population/rate context；
- 原论文明确承认 non-ergodicity 和结构身份的不确定性。

这使它成为 representation-aware workflow 的好开发样例：同一篇论文里的不同对象已经不能被当作同一种 ensemble，更不用说跨数据库时。

## § 2 — 前人工作与不足

`[论文明确陈述]` 在本文之前，HSP90 ATP-lid 的构象变化主要由 X-ray、full-length HSP90 structures、fluorescence/PET 和早期 simulation 描述。它们已经表明 ATP-lid 可以发生大尺度 rearrangement，但仍留下三类缺口：

1. **isolated human HSP90α-NTD 的 closed solution structure 缺失。** 晶体结构并不能充分代表溶液中的 minor conformer。
2. **结构与 kinetics 没有被同一研究体系连接。** 看见两个 endpoint 不等于知道它们是否在溶液中交换，也不等于知道 population/rate。
3. **MD 的角色容易被过度解释。** seeded trajectories 可以检查局部稳定性和可能的 path，但若没有 bidirectional sampling 和 equilibrium initialization，就不能把 frame counts 当作 Boltzmann populations。

`[合理推断]` 论文的贡献不是发明一种新的通用 ensemble inference 算法，而是把几种成熟方法按证据职责组合起来：

| 方法 | 论文中承担的职责 | 不能单独承担的职责 |
|---|---|---|
| NOESY + structure refinement | 提供 open/closed structural hypotheses | population、rate |
| Mutagenesis | 检查结构假设能否解释谱图变化 | 证明 WT 中同一 state 的 population |
| CPMG | 在 two-state fit 下估计 exchange/population | 直接给 minor state 原子结构 |
| Seeded MD | 检查结构稳定性、方向和候选 path | equilibrium population、唯一 mechanism |
| RMSD/clustering/contact violations | 描述 trajectory behavior | 自动成为 slow kinetics/free energy |

## § 3 — 重建作者的思考路径

下面是根据论文证据重建的逻辑链，不把论文结论预先当作前提。

### 第一步：单一 open structure 解释不了全部 NMR 信号

`[论文明确陈述]` 作者发现部分 long-range NOEs 与已知 open structures 不兼容，ATP-lid 区域还存在显著 line broadening。一个自然解释是：数据不是来自一个静态 structure。

### 第二步：用有偏好的 mutants 增强不同 structural hypotheses

作者没有直接从混合信号中估计任意多状态 ensemble，而是利用 R60A 与 R46A backgrounds 分别稳定/富集 open-like 与 closed-like structural evidence，再计算两套 NMR ensembles。这个策略降低了“从平均信号直接反演多个状态”的欠定性。

### 第三步：检查两个结构是否只是 refinement artifact

结构若只在 restraint refinement 中存在，却在无 restraint MD 中立即坍塌，就很难被称为物理上 plausible。于是作者从 20 个 open conformers 和 20 个 closed conformers 分别启动 40 条 unrestrained MD。

### 第四步：把 MD 结果限制在 trajectory behavior

`[论文明确陈述]` open-start simulations 保持 open-like；closed-start simulations 分成三类：7 条在 closed 附近、约 9 条朝 almost open-compatible 区域移动、4 条既不像 open 也不像 closed。作者明确说这些 simulations are not ergodic（article p. 6）。

这一句非常重要：如果 non-ergodic，7/9/4 就不能作为 equilibrium population。

### 第五步：另用 CPMG 回答 MD 无资格回答的 population/rate

`[论文明确陈述]` WT methyl CPMG two-state global fit 在 293 K 给出：

- \(k_{\mathrm{ex}} = 2490 \pm 61\ \mathrm{s}^{-1}\)；
- major/minor populations \(96.8 \pm 0.1\%\) 与 \(3.2 \pm 0.1\%\)；
- \(\Delta G = 8.3 \pm 0.2\ \mathrm{kJ\,mol}^{-1}\)。

这一步没有用 MD frame fraction 替代实验 population。

### 第六步：承认结构身份仍是推断

`[论文明确陈述]` 作者写明，没有 direct experimental evidence 证明 CPMG minor state 就是 NOESY/mutagenesis 推出的 closed structure；他们称其为能解释全部数据的 simplest model（article p. 6）。

因此，论文的最终模型是多证据支持的合理联合解释，而不是直接观测到的唯一 latent truth。

## § 4 — 核心 Intuition

一个 heterogeneous evidence problem 不应先问“怎样把所有数据压成一个 feature matrix”，而应先问“每种数据能够约束哪一类 latent quantity”。这篇论文用 structural restraints 建立候选结构、用 seeded MD 检查局部可行性和路径、用 CPMG 估计交换与 population，再明确保留 state identity 的不确定性。它真正值得 Atlas 借用的是这种 **claim-specific division of labor**，而不是把所有来源解释成同一个 ensemble sample。

## § 5 — 具体方法与完整 Pipeline

### 5.1 输入对象

1. WT 与 mutant NMR spectra/NOEs；
2. R60A-informed open structural ensemble（8B7I）；
3. R46A-informed closed structural ensemble（8B7J）；
4. 40 条 seeded MD trajectories；
5. WT 与 mutant CPMG relaxation-dispersion data；
6. clustering、RMSD、NOE-distance violation 和 DSSP analyses。

### 5.2 结构分支

`[论文明确陈述]` 作者用 NOE-derived distance restraints 和 mutant evidence refined 两套 solution structures。20 models 表示满足 restraint/structure-calculation protocol 的 structural bundle，不是 20 个独立 population samples。

### 5.3 MD 分支

`[论文明确陈述]` 40 条 trajectories：

- 20 open-start；
- 20 closed-start；
- production 1,020 ns；
- first 20 ns treated as equilibration；
- last 1,000 ns analyzed；
- snapshots every 1 ns for clustering，every 10 ns for Figure 4a RMSD；
- temperature 300 K；
- article Methods 的 main alignment：residues 40–97 与 137–220；
- lid RMSD region：98–136。

需要保留三处 source discrepancy：

1. article 写 integration step 2 ps，而 deposited MDP 是 0.002 ps（2 fs）；
2. article thermostat coupling constant 2 ps，而 deposited MDP 记录 0.1 ps；
3. Supplementary Table 4 的 centroid/X-ray comparison 写 alignment 11–97 与 137–220，而 article trajectory Methods 写 40–97 与 137–220。

这些差异说明“paper method”与“executed archive contract”必须分开记录。

### 5.4 Contact-violation 分支

论文公式为：

\[
v_{ij}(t)=\max\left(0,d_{ij}(t)-d^{\mathrm{viol}}_{ij}\right),
\qquad
V(t)=\frac{1}{N}\sum_{\{ij\}} v_{ij}(t)
\]

并声明：

\[
d^{\mathrm{viol}}_{ij}
=
\langle d_{ij}\rangle_{\mathrm{NMR}}
+2\sigma(d_{ij})_{\mathrm{NMR}}.
\]

但是，`[本项目直接观察]` deposited `Violation.zsh` 调用 `trj_violations.py` 时没有 reference trajectory/file，实际走 ITP `up1` branch：open/GS contacts 使用统一 10.0 Å，closed/ES contacts 使用统一 8.5 Å。

所以 Atlas 可以将 deposited score 当作 source-native readout，但不能称其为论文公式的精确数值重现。

### 5.5 CPMG 分支

作者对 21 个 methyl probes 做 two-site global fit，以 grid search 给 global parameters 初值，用 jackknife 检查 residues 是否共享 exchange process，再用 40 Monte Carlo repeats 估计 precision（article p. 10）。

### 5.6 原论文的输出

- two structural anchor ensembles；
- open-start/closed-start seeded-MD behavior；
- 7/9/4 closed-start classification；
- WT two-state-fit population、rate 和 free-energy difference；
- helix-5 rearrangement作为 candidate rate-limiting step；
- 一个明确承认 intermediate/identity ambiguity 的联合解释。

## § 6 — 核心数学推导

这篇论文没有提出新的通用数学框架，但有三个需要区分的量。

### 6.1 Contact violation 不是 likelihood

\(V(t)\) 是超过 upper bound 的平均距离 excess。它可以描述“当前 frame 更违反哪一组 state-specific contacts”，但它不是：

- normalized probability；
- NMR ensemble likelihood；
- posterior state probability；
- free energy。

### 6.2 CPMG two-state quantities

在 two-state exchange model 下：

\[
k_{\mathrm{ex}}=k_1+k_{-1}.
\]

若 minor-state fraction 为 \(p_B\)，则：

\[
p_A=1-p_B,\qquad
\frac{p_B}{p_A}=\exp\left(-\frac{\Delta G}{RT}\right),
\]

因此：

\[
\Delta G=-RT\ln\frac{p_B}{p_A}.
\]

这些 quantity 的 authority 来自 matched CPMG forward model 与 global fit，不来自 MD event count。

### 6.3 Seeded-MD count 为什么不是 population

40 条 runs 被人为分成 20 open-start 与 20 closed-start。初始权重由 experimental design 决定，不由 equilibrium measure 决定。若 trajectories 在观察窗口内没有充分 bidirectional mixing，则：

\[
\frac{\text{frames in state B}}{\text{all frames}}
\neq p_B^{\mathrm{eq}}.
\]

这正是 Atlas 拒绝用 7/29/4 检验 3.2% 的数学原因。

## § 7 — 实验设计与结论

### Q1：是否存在两个可解释 NMR evidence 的结构？

**实验：** mutant-assisted NOE analysis 与两套 structure refinement。  
**回答：** `[论文明确陈述]` 得到 open 与 closed solution ensembles，并通过 restraint satisfaction、mutagenesis 和其他结构比较支持其合理性。

### Q2：open/closed refined structures 在无 restraint MD 中是否具有局部物理可行性？

**实验：** 从 40 个 NMR models 各启动一条 1.02 μs MD。  
**回答：** open-start 20 条稳定；closed-start 出现 7/约9/4 三类行为。closed state 在部分 runs 中可保持数百纳秒到 1 μs，但 packet non-ergodic。

### Q3：是否存在 millisecond exchange，population/rate 是多少？

**实验：** WT methyl/backbone CPMG，two-state global fit。  
**回答：** WT minor population 约 3.2%，\(k_{\mathrm{ex}}\) 约 2.49 kHz；但 minor state structural identity 仍是联合推断。

### Q4：MD 是否证明完整 mechanism？

**实验：** selected transition-like trajectories 的 geometry、NOE violations 与 helix propensity。  
**回答：** `[论文明确陈述]` 作者提出 helix-5 folding/unfolding 可能是 rate-limiting rearrangement，同时承认 path 比 two-state model 更复杂、可能包含 intermediates（article p. 7）。

`[合理推断]` 这属于 mechanism proposal，而非由 unbiased transition-path ensemble 或 kinetic model 定量验证的机制。

## § 8 — Take-aways

### 对 Dynamics Atlas 最重要的六点

1. **先审论文再运行。** 否则会把作者已有的 7/9/4 当成新发现。
2. **保留 representation 和 statistical unit。** NMR model、MD frame、trajectory 和 CPMG curve 不是同一种 sample。
3. **方向、到达、交换和 population 是四种 claim。** “toward open”不等于“entered the open NMR core”。
4. **paper text 与 deposited execution 必须分别审计。** Contact upper-bound branch 已经给出真实反例。
5. **不能用一个漂亮 readout 支撑 combined conclusion。** Geometry/contact 可以支持 structural direction；CPMG 才对 population/rate 有 authority。
6. **abstention 是科学输出。** 对 CPMG-versus-seeded-MD numerical comparison 的拒绝不是分析失败。

### Atlas v1 与论文的精确关系

`[本项目直接观察]` Atlas 在 same packet 上给出：

- 7 closed-directed；
- 29 open-directed；
- 4 geometry/contact conflicts；
- 0 completed conservative NMR-core passages；
- 45 observed-window-stable、43 drift、192 not-estimable trajectory–observable diagnostics；
- numerical CPMG comparison abstention。

其中 7/29/4 与论文 aggregate direction grouping 一致；0 strict-core passages 不与论文冲突，因为论文写的是 “toward” 和 “almost compatible”，不是“进入保守 NMR core”。

## § 9 — 最脆弱的假设

最脆弱的假设是：

> CPMG two-state fit 中的 low-populated excited state，与 NOESY/mutagenesis/structure-refinement 得到的 closed ATP-lid structure 是同一个物理状态。

为什么它脆弱：

1. CPMG 给出 exchange-sensitive observables，不直接给原子结构；
2. mutant-enriched structural anchors 与 WT CPMG 的 construct/condition 不完全相同；
3. 作者自己承认没有 direct experimental evidence 证明 state identity；
4. MD 中出现 neither-open-nor-closed trajectories，提示 intermediate/heterogeneous paths；
5. two-state fit 可以是有效的 phenomenological model，却不保证 microscopic path 只有两个结构盆地。

这不推翻论文，但限定了结论措辞：closed-state identity 是最简 joint explanation，而不是直接观测到的唯一映射。

## § 10 — 最小复现实验

### 一周内可以完成的 bounded reproduction

**数据：**

- 8B7I 与 8B7J 结构 bundles；
- deposited 40-trajectory coordinate packet；
- deposited violation time series；
- article、supplement、source-data workbook 和 analysis scripts。

**预先冻结：**

1. identity/construct/lineage；
2. author residue numbering；
3. article Methods alignment 40–97 ∪ 137–220；
4. lid region 98–136；
5. 20–1020 ns window；
6. geometry 与 contact readouts 分开；
7. terminal-window rule、sensitivity windows 与 forbidden upgrades。

**执行：**

```text
source audit
→ NMR anchor geometry
→ all-trajectory geometry/contact paths
→ final-window two-readout route
→ conservative core/event branch
→ observed-window diagnostics
→ CPMG compatibility gate
→ EvidenceBundle
```

**支持条件：**

- 在不读取 panel-to-trajectory mapping 的情况下先生成 routes；
- reveal 后重建 7/9/4 direction grouping；
- 冲突 trajectories 被 abstain；
- 不能把方向升级成 core arrival/population/rate。

**反驳条件：**

- route 依赖一个任意、未报告的 window/threshold；
- paper/deposition discrepancy 被隐藏；
- system 把 7/9/4 当 equilibrium quantity；
- strict-core failure 被继续调阈值“修好”。

`[本项目直接观察]` 当前 HSP90 v1 已完成这个 same-packet development reproduction；它还不是 held-out generalization。

## § 11 — 最强反例设计

### 反例：所有证据都可以由“多个不同 minor conformations”解释

设想 WT CPMG minor state、R46A-enriched closed NMR structure、部分 closed-start MD basin 和 neither-open-nor-closed MD regions并不是同一个 microscopic state，而是几个在不同 construct/condition 下出现的 states：

- CPMG 仍可能被一个 effective two-state model 拟合；
- mutant spectra 仍会偏移；
- seeded MD 仍会出现 7/9/4；
- selected trajectories 仍会显示 lid swap 与不完整 helix-5 refolding；
- 但“一个 closed state 统一解释全部数据”的 state-identity claim 不成立。

怎样检验：

1. 在 matched WT conditions 下获得更直接的 structural observable；
2. 构建能从 candidate ensembles 预测 CPMG/NOE/FRET/SAXS observables 的 forward models；
3. 做 held-out observable prediction，而不是只做 retrospective fit；
4. 比较 one-closed-state 与 multiple-intermediate models 的 predictive adequacy；
5. 报告 posterior/state-identity uncertainty，而不是只输出一个结构标签。

## § 12 — Follow-up Research Idea

### 从“重现 paper conclusion”升级为“conclusion-hidden claim compiler benchmark”

`[前瞻建议]` 非增量方向不是再给 HSP90 加一个 PCA 或更复杂 classifier，而是建立一个 conclusion-hidden benchmark：

```text
raw paper / supplement / repository / sample payload
→ evidence-locator proposal
→ SourceContract
→ representation-specific deterministic adapters
→ claim-specific compatibility gates
→ scientific execution
→ held-out paper conclusion reveal
→ expert-adjudicated claim comparison
```

第一个实验应包含：

- 一个新的、未用于设计规则的 protein system；
- 至少两个 representation；
- 一项明确可由 deposited data 重建的 bounded conclusion；
- 一项作者讨论但数据不足以独立验证的 higher-level claim；
- 一个故意不兼容的 condition/construct control。

主要终点不是“是否得到与作者相同的一句话”，而是：

1. bounded conclusion retention；
2. unsafe claim-upgrade rate；
3. provenance completeness；
4. expert correction time；
5. deterministic baseline 与 Agent-assisted onboarding 的差异。

这条研究线直接测试 Dynamics Atlas 的核心假设：**能否把论文中隐含的 evidence logic 固化为可复跑、可拒绝、可审查的 workflow，而不把所有 heterogeneous data 假装成同一个 ensemble。**

## 最终项目判断

这篇论文支持 HSP90 作为 development packet，但不支持把当前 Atlas 称为通用系统。当前最稳妥的结论是：

> 在声明的 HSP90 lineage 与 20–1020 ns analysis contract 下，unordered NMR anchors、time-ordered seeded MD、lid geometry 与 deposited contact measurements 支持 paper-consistent directional reconstruction、conflict routing 和 observable-specific uncertainty reporting；它们不支持从该 packet 估计 WT equilibrium population、exchange rate、free energy、完整 pathway 或 mechanism。

下一步必须离开 HSP90 same packet，执行 conclusion-hidden held-out replay。只有这样，才能判断 Atlas 是否学习到了可复用的 scientific control logic，而不只是重新表达了一篇已经知道答案的论文。
