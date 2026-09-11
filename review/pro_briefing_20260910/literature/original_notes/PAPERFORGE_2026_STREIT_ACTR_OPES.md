---
title: "PaperForge — Streit et al. 2026 ACTR / OPES multiT"
paper_title: "Transient tertiary structure in intrinsically disordered proteins revealed by multithermal enhanced sampling"
authors: "Julian O. Streit; Michele Invernizzi; Sandro Bottaro; Kamil Tamiola; Kresten Lindorff-Larsen"
year: 2026
journal: "Nature Communications"
volume: 17
article_number: 5558
doi: "10.1038/s41467-026-73067-3"
paper_role: "ACTR multimodal conclusion-blinded workflow test and enhanced-sampling primary source"
priority: "P0"
full_text_status: "primary HTML and official Supplementary Information checked"
local_primary_article: "autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/reveal/nature_article.html"
local_supplement: "autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/reveal/41467_2026_73067_MOESM1_ESM.pdf"
article_sha256: "2cd21cb46d62f451d32adaf8263516f0f9c643c9a59021f171b757abc25ec698"
supplement_sha256: "bda03c53d7ee3a61744b1a55a6c4195408672b97fbba080c96e30a0496733974"
atlas_task: "autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729"
atlas_evidence_bundle: "autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/score/evidence_bundle.json"
atlas_score: "4 CLAIM_LEVEL_MATCH; 2 NOT_COMPARABLE; 0 unsafe upgrades"
blinding_status: "CONCLUSION_BLINDED_DATA_EXPOSED; claims compared only after pre-reveal seal"
post_reveal_evidence_role_reviewed_at: "2026-07-29T19:10:29Z"
zotero_status: "pending_unverified_no_callable_zotero_write_used"
zotero_note_key: null
zotero_note_scope: null
child_note_status: "not_attempted_tooling_not_callable_in_this_task"
tags:
  - project-protein-dynamics
  - priority-p0
  - paper-role-multimodal-conclusion-blinded-packet
  - claim-extracted
---

# Streit et al. 2026：ACTR 多模态重加权论文，以及 Atlas 在揭盲前真正恢复了什么

> **阅读定位。** 这篇论文首先是一篇 enhanced sampling 方法与 IDP 生物物理研究，不是一篇通用 heterogeneous-data workflow 论文。它用 OPES multiT、REST2、unbiased MD、NMR chemical shifts（CS）、paramagnetic relaxation enhancement（PRE）、residual dipolar couplings（RDC）和 SAXS 共同研究 ACTR。对 Dynamics Atlas 的价值有两层：第一，它提供了一个真实的多模态 packet，可以检验我们的 workflow 能否在不看作者结论的情况下恢复同方向、同强度层级的判断；第二，它暴露出仅有“数据类型适配器”仍然不够——系统还必须正确识别作者真正要估计的 scientific estimand。

> **来源纪律。** 下文使用四种标签：`[论文明确陈述]`、`[本项目直接观察]`、`[合理推断]`、`[前瞻建议]`。论文定位以 primary article 的 section/Figure 和 Supplementary Information 的 printed page/Figure 为准；Atlas 数值定位到六个 sealed modality-result JSON。揭盲比较见 `score/evidence_bundle.json`。

> **一句话总判断。** `[本项目直接观察]` Atlas 在六个冻结 claim units 中恢复了四个与 curator-frozen paper claims 相同的 route：权重只能支持 weighted conformer expectation 而不能支持 kinetics、CS/PRE 是 calibration、RDC 与 SAXS 的 post-fit profile consistency 均改善。这里必须做一个揭盲后的 P1 证据角色修正：RDC/SAXS 没有进入 BME weight objective，但作者用二者之间的折中选择 PRE correlation time \(\tau_c\)（OPES 5 ns、REST2 4 ns），所以它们不是严格 untouched held-out evidence。其余两个 route 不是简单“预测错误”：Rg 的 OPES 数值实际精确重现论文，但 Atlas 额外升级为“两类来源均扩展”；contact 则换了 estimand，从论文的 state-conditioned/native-contact analysis 变成 aggregate nonlocal-contact burden，因此不可直接比较。

## § 1 — 研究问题与重要性

### 论文要解决的具体失败

`[论文明确陈述]` IDP 不由单一三级结构描述，而是占据宽广、异质的构象集合。显式溶剂全原子 MD 能给出原子级构象，但普通 MD 很难充分跨越 IDP 的自由能景观；REST2 虽可增强采样，却需要多 replicas，并可能在高 effective temperature 出现 artificial compaction 和 poor mixing。论文因此提出两个相连但必须分开的研究问题：

1. **方法问题：** 单 replica 的 OPES multithermal sampling 能否比 REST2/unbiased MD 更快、更广地探索 IDP 构象空间，同时在常见 ensemble averages 上保持相容？
2. **ACTR 生物学问题：** apo ACTR 是否会短暂采样多条 binding helices 协同折叠并形成 tertiary contacts 的低占比状态？这些状态是否与已有 NMR/SAXS 数据一致？

具体失败模式是：若只看 \(R_g\) 均值或 per-residue helicity，OPES 与 REST2 可能看起来相似，但 REST2 可能没有访问低占比、较高 helicity 的区域；反过来，仅仅“采样到”一个漂亮结构，也不能说明它属于可信 ensemble，更不能说明其 population、pathway 或 functional mechanism 已被识别。

### 为什么对 Dynamics Atlas 重要

`[本项目直接观察]` ACTR packet 同时包含两类 simulation source families（OPES、REST2）和至少四类实验观测（CS、PRE、RDC、SAXS），且各观测承担不同证据角色：

| 数据 | 原生信息 | 在论文中的角色 | 主要 claim ceiling |
|---|---|---|---|
| OPES/REST2 conformers + weights | weighted conformer expectations | prior ensemble 与重加权承载体 | 不能自动给 physical kinetics 或唯一 population |
| CS | local secondary-structure-sensitive profile | active fitting/calibration | fitted agreement，不是 held-out validation |
| PRE | long-range distance-sensitive average | active fitting/calibration；另有 residue-wise consistency | 受 spin-label/forward-model nuisance parameters 影响 |
| RDC | orientational profile | 未进 weight objective；参与 \(\tau_c\) 选择的 post-fit check | conditional on operator 与 global scale |
| SAXS | global size/shape profile | 未进 weight objective；参与 \(\tau_c\) 选择的 post-fit check | 与 NMR 条件不同，且拟合 scale+offset |
| \(R_g\) | global compaction | reweighting 后的 derived consequence | 不是独立实验验证 |
| native-contact \(Q\)、helicity、cluster | reference-relative/state-resolved structure | rare-state discovery | 依赖 state/reference definition，不能由总体 contact 数替代 |

这正适合检验 Atlas 的核心主张：**标准化 scientific contract，而不是把所有数据压成同一 feature matrix。**

## § 2 — 前人工作与不足

`[论文明确陈述]` 论文建立在几组成熟组件上，而不是从零发明完整体系：

1. **REST2 / replica exchange。** Wang、Friesner 与 Berne 提出 REST2；后续 GROMACS/PLUMED 实现使其成为 IDP enhanced sampling 的常见基线（paper refs. 37–40）。它解决“如何扩大采样”，但仍受 replica mixing、计算成本和高温 compaction 影响。
2. **OPES。** Invernizzi 与 Parrinello 将 enhanced sampling 表述为目标概率分布问题；OPES expanded-ensemble/multiT 用 potential energy 建立 bias，在一个 replica 内覆盖温度范围（paper refs. 47–48）。现有方法提供算法，但尚需在不同大小 IDP 上验证收敛、覆盖与可操作性。
3. **BME ensemble reweighting。** Bottaro、Bengtsen 与 Lindorff-Larsen 的 Bayesian/maximum-entropy 方法将模拟 prior 与实验约束结合（paper ref. 64）。它能寻找与实验更一致且不过度偏离 prior 的权重，但不能保证唯一真实 ensemble。
4. **ACTR experimental knowledge。** Kjaergaard et al. 与 Iešmantavičius et al. 已经建立 ACTR 的温度依赖结构、残余 helix 和 long-range helix–helix interaction 证据（paper refs. 57–58）。这些实验约束 ensemble averages，却不能单独给出每个原子级 rare conformer。
5. **SAXS forward modelling。** Pepsi-SAXS、BIFT error rescaling 和既有 SAXS-refinement workflow 提供全局尺寸/形状对照（paper refs. 103–106），但 SAXS 对多个不同 ensemble 可能不具唯一辨识力。

`[合理推断]` 现有组件的共同缺口不是缺少某个公式，而是缺少一个明确的 evidence control logic：哪些数据参与 fitting，哪些保留为 validation，哪些 nuisance parameters 被重新拟合，哪些条件不一致，以及最终可以把结论升级到哪一层。论文在 ACTR 实例中实际执行了这条逻辑，但没有把它抽象为跨资源 control plane。

## § 3 — 重建作者的思考路径

### 第一步：先证明 OPES 不是只会产生“更多不同结构”

作者从短 helical peptide `(AAQAA)3` 开始，用 unbiased MD 与 REST2 作为可比较基线，检查 \(R_g\)、helicity、ACF、blocking errors 与 cumulative stabilisation。之后逐步扩展到 HTTex1 16Q、ACTR20–60 和 full-length ACTR。这个顺序的逻辑是：先在容易采样、可交叉对照的系统上确认 ensemble averages，再在更困难的系统上讨论低占比空间覆盖。

### 第二步：用多个 convergence/exploration readouts，而不是一个有利指标

`[论文明确陈述]` ACF 测 decorrelation，blocking/error 与 cumulative average 测 ensemble-average stabilisation，\(R_g\)-helicity 和 ELViM 投影测 finite-sampling coverage。论文明确承认这些指标不应产生相同 acceleration factor（Discussion, paragraph beginning “We quantified convergence…”）。这避免把某个单一加速数字当作整个方法的充分证明。

### 第三步：把 ACTR 的“更广采样”转成可以被实验约束的 ensemble

OPES 找到 REST2/unbiased MD 未覆盖的高-helicity、compact states，但作者没有直接把它们称为真实。作者对 OPES 与 REST2 两类 prior ensembles 分别做 BME reweighting，并设计两套 active/passive splits：

- CS+SAXS active；RDC+PRE 被作者标为 passive；
- CS+PRE active；RDC+SAXS 被作者标为 passive。

第二套在各观测之间给出较均衡的 agreement，因此后续聚焦 OPES + CS/PRE reweighted ensemble（Results, “An integrative structural ensemble of ACTR”, Fig. 5b–c；Supplementary Fig. 15a–d, printed pp. 24–25）。但 Supplementary Fig. 15b caption 同时说明，作者根据 RDC 与 SAXS 的折中选择 PRE \(\tau_c\)：REST2 4 ns、OPES 5 ns。也就是说，RDC/SAXS 虽未进入 BME 权重目标，却进入了 nuisance-model selection；更准确的证据角色是 **partially reused post-fit consistency**，而不是严格 untouched holdout。

### 第四步：从 ensemble average 转向显式 state definition

作者没有用“全部 nonlocal contacts 的平均数”定义 rare state。其实际路径是：

1. 以 bound structure 1KBH 定义 backbone native contacts；
2. 用 backbone \(Q\) 与 \(R_g\) 构建 free-energy landscape；
3. 沿 \(Q\) 识别 states 1–3；
4. 分状态比较 helical propensity 与 contact maps；
5. 从 bound state 去掉 CBP，做 10 条 5 μs unbiased MD；
6. 对这些轨迹聚类并取得 C1–C6 reference centroids；
7. 检查 OPES 是否多次、可逆地访问 C2/C4/bound-like high-Q basins；
8. 检查 helix co-folding 是否高于独立事件的乘积期望。

这条 state-definition chain 才把“更广采样”推进到“transient helix-bundle-like state”。

### 第五步：保留 identifiability 限制

`[论文明确陈述]` 作者指出，实验数据不能 unequivocally distinguish reweighted OPES 与 REST2 ensembles；多个 ensembles 可以解释 SAXS，而 PRE 约束更强（Results, Fig. 5 context）。因此论文最强的安全表述是：OPES 额外采样的 highly helical states **consistent with** 所考虑实验，并可能属于 apo ensemble，而不是“实验唯一证明了这一组 weights/structures”。

## § 4 — 核心 Intuition

OPES 的核心 intuition 是把“跨越慢自由能障碍”改写为“让单个 simulation 在一组温度分布间扩展采样”，再用严格的 frame weights 回到目标温度求 ensemble expectation。ACTR 部分的核心 intuition 则是：先让 simulation 提供足够宽的候选构象支持，再用局部与全局实验约束 weights，并用未参与拟合的数据检查预测一致性。真正可迁移到 Atlas 的关键不是某一种 reweighting 算法，而是 **candidate support → active calibration → passive validation → state-specific interpretation → claim ceiling** 的顺序。

## § 5 — 具体方法与完整 Pipeline

### 5.1 论文的完整 pipeline

```text
sequence + force field + solvent/condition
→ 10 short OPES bias-convergence trials
→ choose a converged quasi-static bias
→ 5 independent ACTR production replicas
→ temperature reweighting to target T
→ compare native ensemble summaries against REST2/unbiased MD
→ BME reweighting with CS+SAXS or CS+PRE
→ evaluate objective-left-out profiles and use RDC/SAXS compromise to select PRE tau_c
→ choose the balanced OPES CS+PRE ensemble
→ define native-Q / cluster-reference states
→ inspect state-conditioned helicity, contacts, recurrence and cooperativity
→ bounded interpretation of transient tertiary structure
```

关键实现：

- GROMACS 2023.4 + PLUMED 2.10；2 fs timestep；production data every 10 ps（Methods, “Molecular dynamics simulations” and “OPES multithermal simulations”）。
- ACTR full length：5 OPES production replicas × 5 μs；温度区间约 290–450 K（Results, “OPES enables improved…”；Supplementary Table 2）。
- OPES target-temperature weight见 Methods Eq. 3；weighted expectation 见紧随 Eq. 3 的定义；Kish \(N_{\mathrm{eff}}\) 见 Eq. 4。
- CS：SPARTA+ + POTENCI；RDC：PALES local alignment window 15；PRE：DEER-PREdict；SAXS：Pepsi-SAXS（Methods, “Bayesian/maximum entropy reweighting”）。
- BME 以 uniform prior weights 初始化。论文特别说明 OPES-derived weights 与 uniform-averaged OPES observables 很相似，但若将非均匀 OPES weights 作为 BME baseline，会使后续 \(N_{\mathrm{eff}}\) 变化难与 REST2 直接比较。
- CS/PRE fitting 时约束 effective fraction \(\phi=\exp(S_\mathrm{rel})>0.2\)。RDC 和 SAXS 不进入 weight objective，但参与 \(\tau_c\) compromise selection，因此只能提供 partially reused post-fit consistency，不能称为严格独立 held-out validation（Methods Eq. 16 前后；Supplementary Fig. 15b–c caption, printed pp. 24–25）。

### 5.2 Atlas 揭盲前执行的 pipeline

```text
official Zenodo files
→ exact-file source manifest + hashes
→ frozen scientific contract
→ common-support mapping
→ define p and standalone q without assuming posterior identity
→ modality-native calculations
→ frozen effect/sensitivity gates
→ six sealed claim routes
→ reveal attested curator-frozen paper claim file
→ claim-level direction/strength comparison
```

`[本项目直接观察]` packet 内实际处理：

- OPES：61,008 frames；其中 60,034 映射到共同支持；
- REST2：37,911 frames；其中 37,342 映射到共同支持；
- CS：C/CA/CB/H/N 五类 nuclei；
- RDC：57 个 mapped residues；
- SAXS：1,832 个 q points；
- \(R_g\)：OPES 五个 source lineages 与 REST2 sensitivity；
- residue-distance arrays：71 residues，\(|i-j|\ge10\) 的 1,891 对候选 residue pairs。

权重语义被刻意拆开：

\[
p=\operatorname{normalize}(\text{source prior on common support}),
\]

\[
q=\operatorname{normalize}(\text{author-supplied standalone measure}),
\]

\[
q_{\mathrm{comp}}=\operatorname{normalize}(p\cdot q),
\]

其中 \(q_{\mathrm{comp}}\) 只用于 sensitivity，不被称为重新拟合的 posterior。实现定位：

- weight mapping 与三种 measures：`scripts/run_actr_pre_reveal_v1_1.py`, lines 385–443；
- Kish ESS / entropy-perplexity gates：lines 446–531；
- RDC profile、global-scale 和 leave-one-lineage-out：lines 817–923；
- SAXS affine scale+offset、scale-only sensitivity：lines 1034–1218；
- \(R_g\) route：lines 1234–1339；
- aggregate nonlocal-contact burden：lines 1342–1519；
- exact source verification 与 claim execution：lines 1664 onward。

### 5.3 六个 claim units 的揭盲后对照

| Claim unit | Atlas 揭盲前判断 | 论文/attested curator-frozen claim | 比较结论 |
|---|---|---|---|
| Weight/time | admissible weighted measures；no kinetics | 同 | `CLAIM_LEVEL_MATCH` |
| CS/PRE | OPES 与 REST2 的 CS calibration 均改善；PRE 仅保留 source fitting lineage | 同 | `CLAIM_LEVEL_MATCH` |
| objective-left-out RDC | 两 source families 均改善；Atlas 使用无约束 all-residue scale | 同方向；但参与 \(\tau_c\) 选择，且 paper operator 不同 | `CLAIM_LEVEL_MATCH` |
| cross-condition SAXS | 两 source families 均改善；affine fit；不是 same-condition validation | 同方向；但参与 \(\tau_c\) 选择 | `CLAIM_LEVEL_MATCH` |
| \(R_g\) shift | OPES 与 REST2 都扩展 | curator file 只允许 partial；论文明确报告 OPES | `NOT_COMPARABLE` |
| nonlocal contact | aggregate burden 减少 | 论文没有这个 aggregate prior-vs-reweighted estimand | `NOT_COMPARABLE` |

**不能把 4/6 称为 67% scientific accuracy。** 六个 units 不是等权、独立的 biological endpoints；比较只说明四条冻结 routes 在方向与证据等级上与论文一致，另两条 estimand/coverage 不同。

## § 6 — 核心数学推导

### 6.1 从 multithermal sampling 回到目标温度

论文将目标分布写为多个 inverse temperatures 的 canonical mixture（Methods Eq. 1）。OPES 在参考 \(\beta_0\) 下建立 bias \(V(x)\)，收敛后，对 frame \(i\) 在目标温度 \(\beta^*\) 的非归一化权重为：

\[
w_i(\beta^*)=
\exp\left[-(\beta^*-\beta_0)U_i+\beta_0V(x_i)\right].
\]

归一化后，

\[
\langle A\rangle_{\beta^*}
=\sum_i \widetilde w_i(\beta^*)A(x_i).
\]

这里得到的是目标温度下、给定 simulation/bias/force-field 的 weighted conformer expectation。因为轨迹经过 temperature acceleration 和 bias，保存顺序不能直接拿来估 physical transition rate。Atlas 因此正确路由为 `WEIGHT_MEASURES_ADMISSIBLE_NO_KINETICS`。

### 6.2 Kish ESS 不是独立生物学样本数

\[
N_{\mathrm{eff}}=
\frac{(\sum_i w_i)^2}{\sum_i w_i^2}.
\]

它衡量权重集中程度：若一个 frame 独占大权重，ESS 低；若权重均匀，ESS 高。Atlas 的 OPES `q` Kish ESS 为 4,967，REST2 `q` 为 3,094，说明 supplied measures 没有退化为极少数 frames，但这些数字不是“4,967 个独立 trajectories”，也不证明 biological population identifiable。

### 6.3 BME 的约束—偏离折中

论文用 relative entropy 控制新权重对 prior 的偏离：

\[
S_\mathrm{rel}=-\sum_i w_i\ln\frac{w_i}{w_i^0},
\qquad
\phi=\exp(S_\mathrm{rel}),
\]

并要求 \(\phi>0.2\)。直觉是：实验拟合不能靠把全部概率压到极少数构象上实现。但 \(\phi\) 只能限制权重退化，不会把欠定反问题变成唯一解。

### 6.4 RDC 与 SAXS 的 nuisance parameters

RDC 用 Q-factor：

\[
Q=
\frac{\mathrm{rms}(RDC_{\exp}-\langle RDC_{\mathrm{calc}}\rangle)}
{\mathrm{rms}(RDC_{\exp})},
\]

但 ensemble-averaged predicted RDC magnitude 先用一个 global scale 优化。这里还有一个 operator mismatch：

- Atlas frozen runner 在所有 mapped residues 上直接拟合一个无约束 scale，因此在未先反转 \({}^{15}N\) convention 时得到负 scale；
- paper-style operator 先做 \({}^{15}N\) sign inversion，只保留 predicted/experimental sign-matching residues，并约束 scale 非负。

使用 paper-style operator 的 post-reveal check 仍得到 OPES Q-factor \(0.66135\rightarrow0.45063\)，与 frozen Atlas 的 \(0.65748\rightarrow0.45057\) 保持同方向和相近量级。这支持 direction robustness，但两套 operator 不能称为数值同构。冻结文件 `ACTR_CLM_03_HELDOUT_RDC.json` 保留 legacy 名称以维护 seal/hash；正文中的科学角色已修正为 `OBJECTIVE_LEFT_OUT_BUT_TAU_C_REUSED_PROFILE_CONSISTENCY_CONDITIONAL_OPERATOR_AND_SCALE`。

SAXS 使用：

\[
\chi^2_{\mathrm{red}}
=\frac1N\sum_i
\frac{[I_i^\exp-(\alpha\langle I_i^\mathrm{gen}\rangle+\beta)]^2}
{\sigma_i^2}.
\]

\(\alpha\) 是 scale，\(\beta\) 是 constant background。Atlas 复现 affine fit，并把 scale-only fit 保留为 descriptive sensitivity；因此不能称 parameter-free SAXS prediction。SAXS 也参与 \(\tau_c\) compromise selection，所以冻结文件 `ACTR_CLM_04_CROSS_CONDITION_SAXS.json` 的内容仍可审计，但其 validation role 必须解释为 cross-condition, partially reused post-fit consistency。

## § 7 — 实验设计与结论

### 问题 1：OPES 能否更快探索，同时保持常见 ensemble properties 相容？

**实验：** 从 `(AAQAA)3` 到 HTTex1、ACTR20–60、full ACTR，比较 OPES、REST2，部分系统再比较 unbiased MD；使用 ACF、blocking errors、cumulative stabilisation、\(R_g\)、helicity、ELViM 与 2D coverage。

**答案：** `[论文明确陈述]` OPES 在多数 readouts 上更快，并访问更多低占比 high-helicity/compact regions；但 acceleration factor 随指标变化，且 full ACTR 的 ensemble averages 与 REST2 仍大体相容（Figs. 2–4；Discussion）。

### 问题 2：重加权后是否只是更好地拟合 active data？

**实验：** 两套作者标记的 active/passive split；重点是 CS+PRE active，RDC+SAXS 名义上 passive，但二者随后参与 \(\tau_c\) compromise selection。

**论文答案：** CS/PRE fit 改善，未进入 weight objective 的 RDC/SAXS profiles 也改善。OPES reweighted ensemble 的 RDC Q-factor 约 0.45，REST2 约 0.55；SAXS reduced \(\chi^2\) 分别约 1.40 和 1.19（Fig. 5c；Supplementary Fig. 15c）。但这两项被用来选择 PRE \(\tau_c\)，所以它们不是 strictly untouched held-out tests。

**Atlas 揭盲前答案：**

- OPES RDC Q：0.6575 → 0.4506（31.5% reduction）；
- REST2 RDC Q：0.7086 → 0.5505（22.3% reduction）；
- OPES SAXS affine \(\chi^2\)：3.1404 → 1.4016（55.4% reduction）；
- REST2 SAXS affine \(\chi^2\)：1.9472 → 1.1942（38.7% reduction）。

RDC 的 frozen Atlas operator 与 paper operator 不同；paper-style OPES recheck 为 0.66135 → 0.45063，说明改善方向不是由这个 operator 差异制造，但 frozen pre-reveal 数字不能冒充 paper-exact reconstruction。

这些数值分别定位于：

- `pre_reveal/modality_results/ACTR_CLM_03_HELDOUT_RDC.json`
- `pre_reveal/modality_results/ACTR_CLM_04_CROSS_CONDITION_SAXS.json`

`[本项目直接观察]` 五个 OPES lineages 的 leave-one-file-out 方向均稳定；但这五个 lineages 是 sensitivity units，不是五个独立 biological replicates。

### 问题 3：重加权如何改变 global compaction？

**论文答案：** OPES \(R_g\) 从 \(1.90\pm0.04\) nm 增至 CS+SAXS 的 \(2.19\pm0.06\) nm 和 CS+PRE 的 \(2.16\pm0.05\) nm（Results, paragraph beginning “Consistent with this interpretation…”；Supplementary Fig. 15f, printed p. 24）。

**Atlas 揭盲前答案：** OPES \(p\) mean 1.8983 nm，\(q\) mean 2.1599 nm，\(\Delta=+0.2616\) nm，实际精确重现了论文 CS+PRE 方向与均值。Atlas 同时计算 REST2 2.0544 → 2.3433 nm，并据此给出“两 source families expanded”。

**为什么最后是 `NOT_COMPARABLE`：** attested curator-frozen claim file 只把论文明确报告的 OPES Rg consequence 编为 `RG_SHIFT_PARTIAL`；论文没有用相同显式 claim 报告 REST2 的 prior-to-CS/PRE \(R_g\) shift。Atlas 的数值没有错，但 route 扩大了 source-family coverage，导致 claim granularity 不一致。该 curator file 有时间戳与 hash attestation，但没有证据证明 curator 在组织层面独立，因此不能把它描述为组织独立的 gold standard。

### 问题 4：是否恢复了论文的 transient tertiary structure 结论？

**论文实验：** bound-reference backbone/all-atom \(Q\)、\(R_g\) landscape、state 1–3、state-conditioned contact maps、bound-start unbiased MD、C1–C6 cluster references、OPES time-series recurrence 和 helix cooperativity（Fig. 5e–i；Supplementary Figs. 15e,g、16–18）。

**Atlas 当前实验：** 计算所有 \(|i-j|\ge10\) residue pairs 在 0.75/0.80/0.85 nm cutoffs 下的 aggregate expected contact burden。0.80 nm 时从 110.21 降至 74.49 contacts/frame，relative change −32.4%，五个 leave-one-lineage-out 和两组 cutoff sensitivity 同号。

**结论：** `NOT_COMPARABLE`。论文 Supplementary Fig. 15g 使用 0.6 nm heavy-atom cutoff，比较的是 reweighted ensemble 内 state 1–3 的 contact-probability maps；论文没有报告“prior vs reweighted 的全局 nonlocal-contact burden”。总体 contacts 减少与某个稀有、state-conditioned basin 内特定 tertiary contacts 增强完全可以同时成立。

揭盲后的 explanatory diagnosis 使用作者提供的 `state3_frames.ndx` 和 native-Q arrays 对这一点做了定量核查：

1. 作者 state3 文件采用 **1-based source-frame indices**；分析先显式转换为 **0-based array indices**；
2. state3 含 2,871 frames；
3. state3 mass 分别为 source-native \(p=4.871\%\)、common-support \(p=4.952\%\)、supplied \(q=2.612\%\)；
4. 在 supplied \(q\) 下，state3 的 mean backbone-Q 为 0.830，而 complement 为 0.293；
5. 同时，whole-ensemble aggregate contact burden 在 0.8 nm 下仍从 110.21 降到 74.49 contacts/frame，即 −32.4%。

所以“总体非特异 contacts 减少”与“保留一个低权重占比、但 bound-reference Q 较高的作者定义 state”确实可以共存。结果位于 `outputs/post_reveal_state_definition_diagnosis.json`。这一步在揭盲后使用作者 state labels，因此其角色严格是 `POST_REVEAL_EXPLANATORY_NOT_INDEPENDENT_VALIDATION`：它解释 estimand mismatch，不是 Atlas 独立发现 state3，也不识别 biological population。

### 揭盲总体结论

`[本项目直接观察]`

- 4 `CLAIM_LEVEL_MATCH`
- 2 `NOT_COMPARABLE`
- 0 unsafe upgrades
- 0 wrong-direction claims
- 0 false abstentions

这个结果支持 **workflow 能在一个真实多模态 packet 中恢复多项 bounded evidence judgments**。它不支持 independent biological truth、cross-system generalization、Agent incremental value，也不支持“系统已经自动重建论文中心发现”。

## § 8 — Take-aways

1. **论文比较的正确单位是 claim，不是段落或 figure。** Atlas 无需复制论文叙述，只需在结论揭盲前冻结输入、estimand、route 和 claim ceiling，再比较方向与证据等级。
2. **objective inclusion 与 validation independence 必须分开记录。** CS/PRE 进入 weight objective；RDC/SAXS 没进入 objective，但参与 \(\tau_c\) 选择，因此只能算 partially reused post-fit consistency。
3. **nuisance parameter 与 operator 必须进入 claim 文本。** RDC 依赖 sign convention、residue selection 与 global scale；SAXS 依赖 affine scale+offset，而且 SAXS 条件与 NMR 不同。
4. **权重不是自动的 population/kinetics。** 本 packet 只允许 weighted conformer expectations。
5. **全局 readout 不能替代 state-specific estimand。** 这是 contact claim 失败的根因，也是下一版 workflow 最重要的修改。
6. **“不 comparable”是有信息的结果。** Rg 暴露 claim granularity mismatch；contact 暴露 estimand mismatch。它们比事后硬凑一致更能验证 workflow 的科学纪律。
7. **Agent 的合理角色在上游。** Agent 可以从 paper/README/source files 提议 `SourceContract`、active/passive roles、condition differences 和 candidate state definitions；deterministic code 与 human reviewer 决定计算、gate 和 claim upgrade。

## § 9 — 最脆弱的假设

**最脆弱假设：多个 ensemble-averaged observables 的一致性足以支持稀有 helix-bundle-like subensemble 的结构身份。**

为什么脆弱：

1. inverse problem 欠定；论文自己指出不同 reweighted OPES/REST2 ensembles 不能被实验 unequivocally distinguished；
2. SAXS 对 global size/shape 敏感但结构辨识度低，且这里是 318 K、pH 7.4、0.2 M，与 NMR/BME 的 310 K、pH 6.5、0.033 M 不同；
3. CS 主要报告局部结构，RDC 需 global scaling，PRE 依赖 spin-label/rotamer 与 correlation-time nuisance assumptions；
4. state 3 的约 2.6% population 来自 reweighted simulation state definition，不是实验直接读数；
5. bound-reference \(Q\)、cluster cutoff 与 reference centroids 共同决定“像哪个 state”。

论文提供的缓解证据包括：两类 simulation priors、多种 active/passive splits、bound-start unbiased MD、多个独立 OPES replicas 中的重复访问、温度敏感性与 helix cooperativity。但这些仍支持“plausible and experimentally consistent rare state”，不支持“unique true ensemble”。

## § 10 — 最小复现实验

### 一周内可执行的最小版本

**目标：** 不复现所有 OPES simulation，只用 official released ACTR archive 检验“CS+PRE supplied measure 是否同时改善 objective-left-out but \(\tau_c\)-reused RDC、跨条件 SAXS，并恢复论文报告的 OPES \(R_g\) shift”；随后增加一个最小 state-specific \(Q\) test。

**输入：**

1. Zenodo record 18249727 的 ACTR OPES/REST2 per-frame forward products、weights、frame mapping；
2. CS/PRE supplied reweighting measures；
3. RDC 和 SAXS experimental profiles；
4. OPES coordinates 或已提供的 reference-contact products；
5. bound structure PDB 1KBH。

**实施：**

```text
verify file hash and exact support
→ define p and standalone q
→ reproduce CS calibration direction
→ fit one RDC global scale and score Q
→ fit SAXS scale+offset and score chi-square
→ reproduce OPES weighted Rg
→ define backbone-Q from 1KBH exactly as paper Eq. 8
→ estimate q-weighted high-Q basin mass
→ repeat leave-one-OPES-lineage-out
```

**支持条件：**

- CS calibration 与 partially reused post-fit RDC/SAXS 同方向改善；
- OPES \(R_g\) 约从 1.90 到 2.16 nm；
- frozen bound-backbone-Q state definition 下出现论文同方向的 low-population high-Q basin；
- leave-one-lineage-out 不改变方向。

**反驳/降级条件：**

- post-fit improvement 依赖单个 lineage、\(\tau_c\) selection 或 nuisance fit；
- high-Q basin 对 contact definition/reference/cutoff 极度敏感；
- q 权重把 ESS 压到不足以支持该 state；
- alternative weights 在同等 RDC/SAXS fit 下给出完全不同 high-Q mass。

当前 Atlas 已完成前五步与相应 sensitivity，但尚未执行严格 paper-matched native-Q/state test；因此中心 biological claim 的最小复现仍未闭环。

## § 11 — 最强反例设计

### Counterfactual ensemble equivalence test

构造一组 alternative weights \(q'\)，要求：

1. 与原 \(q\) 具有相近 Kish ESS / relative entropy；
2. CS、PRE calibration 不劣于预设 tolerance；
3. post-fit RDC Q-factor 与 SAXS \(\chi^2\) 保持在原 \(q\) 的 uncertainty/tolerance 内；
4. 但最大化或最小化 bound-backbone-Q high-state mass，或破坏 helix 1–2–3 cooperativity。

伪代码：

```python
for target in ["minimize_high_Q", "maximize_high_Q"]:
    q_prime = optimize_weights(
        constraints=[
            CS_fit <= CS_fit_q + tol_cs,
            PRE_fit <= PRE_fit_q + tol_pre,
            RDC_Q <= RDC_Q_q + tol_rdc,
            SAXS_chi2 <= SAXS_chi2_q + tol_saxs,
            phi >= 0.20,
        ],
        objective=target(high_Q_mass, helix_cooperativity),
    )
    compare(q_prime, q, observables, high_Q_mass, contact_maps)
```

若 \(q'\) 能在所有实验 profile 上几乎等价，却让 rare bundle population 从接近零变到数个百分点，那么实验一致性不能识别该 rare-state population；论文结论应保留为 simulation-supported structural hypothesis。若所有满足约束的 \(q'\) 都保留相似 high-Q mass 与 cooperativity，结构结论会明显增强。

这是比“再算一次相关系数”更强的反例，因为它直接攻击 central claim 的 identifiability，而不是只测试数值复现。

## § 12 — Follow-up Research Idea

### 建立 StateDefinition-aware Atlas，而不是继续增加通用 descriptors

`[前瞻建议]` 当前 Atlas 已能处理 modality-native profiles 与 claim ceilings，但 ACTR contact 失败显示：系统还缺一个显式 `StateDefinition` 层。新方向是把每个 structural claim 编译成：

```text
StateDefinition
  reference object: PDB 1KBH / learned centroid / no reference
  atom selection: backbone / heavy atom / residue centers
  state variable: Q / contact pattern / helicity / cluster label
  threshold or basin rule
  condition and weight semantics
  robustness perturbations
  allowed and forbidden claims
```

第一项实验不是再找一篇相似论文，而是在 ACTR 上并列执行：

1. paper-matched bound-backbone-Q；
2. cluster-centroid C2/C4-Q；
3. reference-free aggregate contact burden；
4. counterfactual ensemble equivalence test。

比较它们分别能恢复论文哪一层结论，以及哪些结果只在某个 state definition 下成立。之后再将同一 `StateDefinition` compiler 应用于 HSP90 的 open/closed lid、AdK domain closure 或另一个 IDP packet。

Agent 可以在此层读取 paper/README 并**提议** reference、residue range、contact definition 与 expected claim；但这些候选必须带 locator，并由 deterministic schema validator 和 human review 冻结后才能执行。这样 Agent 的价值是减少新 packet onboarding 成本，而不是替代 scientific judgment。

---

## 支持与禁止表述

### 当前材料支持

- “在 conclusion-blinded、data-exposed 的 ACTR packet 上，Atlas 对六个预冻结 claim units 中四个恢复了与论文一致的方向与证据等级，另外两个因 claim granularity 或 estimand 不同而不可比较。”
- “CS/PRE supplied reweighting measure 对 active CS calibration 有改善；未进入 weight objective、但参与 \(\tau_c\) 选择的 RDC 与跨条件 SAXS profiles 也呈改善。”
- “OPES \(R_g\) 的 Atlas 结果 1.898 → 2.160 nm 重现论文 CS+PRE 的约 1.90 → 2.16 nm。”
- “当前 aggregate contact-burden result 是新的 Atlas estimand，不是论文 native-Q/state-conditioned contact result。”
- “揭盲后、使用作者 state3 labels 的 diagnosis 显示，2.612% q-mass 的 state3 具有 mean backbone-Q 0.830，而 complement 为 0.293；这解释了总体 contact burden −32.4% 与局部高-Q state 可以共存。”
- “该实验支持 representation-aware、claim-specific workflow 的可行性，但中心 rare-state discovery 尚需 paper-matched StateDefinition test。”

### 当前材料禁止

- “Atlas 已经独立证明 ACTR 存在唯一的 2.6% helix-bundle population。”
- “OPES/reweighted frame order 给出了 physical kinetics、transition rate 或 pathway。”
- “四个 claim matches 等于 67% scientific accuracy。”
- “SAXS 是同条件、parameter-free 的独立验证。”
- “RDC/SAXS 是完全 untouched held-out evidence。”
- “RDC 给出 absolute orientation prediction，且 residues 是独立 biological replicates。”
- “aggregate contacts 减少反驳论文的 tertiary contacts 增强。”
- “Atlas 在揭盲前独立发现了 state3，或 state3 mass 是实验识别的 biological population。”
- “实验已经证明 cross-system generalization 或 Agent incremental value。”
- “多模态 agreement 唯一识别了真实 ensemble。”

## 审计入口

- Primary article：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/reveal/nature_article.html`
- Supplement：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/reveal/41467_2026_73067_MOESM1_ESM.pdf`
- Attested curator-frozen claim file：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/reveal/gold_claims_v1_1.json`
- Pre-reveal six results：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/pre_reveal/modality_results/`
- Claim comparison：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/score/claim_comparison.tsv`
- Evidence bundle：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/score/evidence_bundle.json`
- Post-reveal state diagnosis：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/outputs/post_reveal_state_definition_diagnosis.json`
- Frozen contract：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/protocol/scientific_contract.json`
- Analysis config：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/protocol/actr_analysis_config.json`
- Deterministic runner：`autoresearch/tasks/dynamics_atlas_actr_heldout_v1_20260729/scripts/run_actr_pre_reveal_v1_1.py`

## Zotero 同步状态

本次任务环境没有已调用且可验证的 Zotero 写入工具，因此未创建 Zotero note。状态记录为 `pending_unverified_no_callable_zotero_write_used`；本地 Markdown 是当前可审计正文。后续若启用 Zotero，必须创建/定位 parent item、写入 full 或 compressed 12-section note、搜索验证 note key，并单独核验 child-note attachment，不能仅凭“创建成功”声称已经附着到论文条目。
