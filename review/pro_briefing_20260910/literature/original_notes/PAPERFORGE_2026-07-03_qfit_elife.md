# PaperForge Analysis - qFit eLife PDF

Paper: Stephanie A. Wankowicz et al., "Automated multiconformer model building for X-ray crystallography and cryo-EM", eLife, 2024. DOI: `10.7554/eLife.90606.3`.

Local PDF: `autoresearch/tasks/nature_skills_proposal_litreview/outputs/literature_collection_curated_2026-07-03/PDFs/qfit_elife_Automated_multiconformer_model_building_for_X_ray_crystallography_and_cryo_EM_10_7554_eLife_90606_3.pdf`

Full-text extraction: `autoresearch/tasks/nature_skills_proposal_litreview/outputs/paper_analysis_2026-07-03/fulltext/qfit_elife.txt`

Evidence anchors: `QFIT-S001` to `QFIT-S008` in `source_maps/downloaded_pdf_source_map.json`.

Zotero parent candidates found: `IUQ7C2JW`, `HN6WKHVK`. Prefer `IUQ7C2JW` unless the user later consolidates duplicates.

## Terminology Ledger

| Canonical term | First-use definition | Variants seen | Decision |
|---|---|---|---|
| qFit | Automated multiconformer model-building tool | qFit protein, qFit model | Use `qFit`. |
| multiconformer model | A single structural model using altlocs to encode alternative conformations | multiconformers, alternative conformations | Use `multiconformer model`. |
| altloc | Alternative location indicator in PDB/mmCIF-style structures | alternative location indicator | Define once, then use `altloc`. |
| density map | X-ray electron-density or cryo-EM map | map, density | Use `density map`. |
| MIQP | Mixed-integer quadratic programming | mixed-integer quadratic programming | Define once, then use `MIQP`. |
| BIC | Bayesian information criterion | Bayesian information criteria | Use `BIC`. |
| Rfree | Cross-validation crystallographic R-factor | R-free | Use `Rfree`. |
| Q-score | Map-profile agreement metric for cryo-EM/model fit | Q-score | Use `Q-score`. |

## § 1 - 研究问题与重要性

qFit 解决的是结构生物学中的一个常见信息损失问题：X-ray crystallography 和 cryo-EM 的 density maps 是大量分子构象的 ensemble average，但 deposited model 通常只给出 single-conformer coordinates。这样会把实验数据中存在的 local heterogeneity 压缩成一个平均结构，尤其容易丢掉 side-chain rotamer、local backbone shift、partial occupancy 和 coupled local motions（`QFIT-S002`）。

这篇论文的重要性对我们的项目非常直接。Wankowicz/Fraser 方向代表的是 "experimental-density-grounded multiconformer dynamics"。它不是 MD trajectory，也不提供时间顺序；但它把实验 density 中的局部构象异质性转成 PDB-compatible multiconformer models。对于 Dynamics Atlas，这是一类独立 evidence type：experimental ensemble signal at local scale。

作者提出和验证的核心 claim 是：新版 qFit 通过 BIC、B-factor sampling、updated cryo-EM scoring、open-source optimization 等改进，可以从高分辨率 X-ray 和 cryo-EM density maps 中自动构建更好的 multiconformer models，并在多数高质量 X-ray test structures 上改善 Rfree 和部分几何指标（`QFIT-S003`, `QFIT-S004`, `QFIT-S008`）。

## § 2 - 前人工作与不足

论文中的 prior gap 有三层。

第一，传统 PDB deposition 多数是 single-conformer model，忽略 density 中的 weak but biologically meaningful alternative conformations。手工建模 multiconformers 很慢、主观、容易 burnout，也容易只在研究者注意到的局部区域建 alternate conformers（`QFIT-S002`）。

第二，已有 ensemble refinement 或 multicopy ensemble methods 可以表达更复杂的 ensemble，但输出往往不如 altloc-based multiconformer models 容易被 Coot、Phenix、Refmac、Buster 和 PDB deposition workflow 处理。qFit 选择与标准 altloc 兼容，是一种实用路线（`QFIT-S002`, `QFIT-S007`）。

第三，cryo-EM 正在进入高分辨率区域，但 map handling、masking、local resolution、bulk-solvent/background treatment 和 validation metrics 仍不如 X-ray 标准化。作者明确说 qFit 在 cryo-EM 上更 exploratory，且受 map consistency 和 resolution validation 限制（`QFIT-S003`, `QFIT-S006`）。

## § 3 - 重建作者的思考路径

作者的思考路径可以重建为：

1. Density maps contain ensemble information, but most final structural models are single conformers.
2. Manual multiconformer modeling is valuable but slow, subjective, and difficult to apply at scale.
3. Altloc-based multiconformer models are a practical compromise: less expressive than nested ensemble representations, but compatible with common model-building/refinement software and PDB deposition.
4. qFit can search local conformational possibilities and select parsimonious sets that explain density.
5. However, earlier qFit versions needed better model-complexity control, B-factor handling, cryo-EM support, and open-source optimization.
6. The updated qFit should therefore combine sampling, QP/MIQP scoring, BIC model selection, B-factor sampling, segment relabeling, and refinement to produce models that fit density better without obvious overfitting.

This reasoning also explains why qFit is a good collaboration target for Dynamics Atlas: it turns "experimental multiconformation" into a computable object, but it demands careful evidence labeling because density-derived heterogeneity is not time-resolved dynamics.

## § 4 - 核心 Intuition

The core intuition is: many proteins in high-resolution density maps are not well represented by one coordinate set per residue; a small number of local alternative conformers can explain the density better than a strained average model.

qFit operationalizes this by sampling plausible backbone/side-chain/B-factor alternatives, scoring density fit, penalizing unnecessary complexity with BIC, enforcing occupancy/altloc consistency, and outputting a parsimonious multiconformer model compatible with ordinary structural biology tools.

## § 5 - 具体方法与完整 Pipeline

qFit 的 pipeline 可分为 residue-level search、segment-level consistency、relabeling、refinement 和 benchmarking。

Input requirement: qFit generally expects a high-resolution density map, around better than 2 Å, and a well-refined single-conformer input model, generally Rfree below 20% for X-ray. For X-ray, authors recommend composite omit maps to reduce model bias. For cryo-EM, they explicitly state model/map quality metrics are still developing and use is more exploratory (`QFIT-S003`).

Residue-level sampling:

1. Strip hydrogens.
2. Sample backbone translations for each residue, guided by anisotropic B-factors when available.
3. For aromatic residues, sample the C-alpha-C-beta-C-gamma aromatic angle.
4. Enumerate chi dihedral conformations around rotameric angles.
5. Remove clashes and redundant conformations.
6. Use QP to identify density-fitting conformations.
7. Sample B-factors by multiplying input B-factors by factors from 0.5 to 1.5.
8. Use MIQP with occupancy/cardinality constraints.
9. Use BIC across cardinality 1-5 to pick the best parsimonious conformer set (`QFIT-S003`, `QFIT-S008`).

Segment and labeling:

1. After residue-level conformers are chosen, qFit reconnects neighboring residues with multiple backbone conformations.
2. Segment-level MIQP/BIC chooses compatible combinations.
3. Monte Carlo relabeling assigns altloc labels to reduce steric clashes among spatially coupled conformers (`QFIT-S003`).

Refinement:

1. The raw qFit multiconformer model is iteratively refined with Phenix.
2. Conformers with occupancy below 10% are removed.
3. Occupancies, coordinates, B-factors, and waters are refined.
4. Final qFit models can be inspected/edited in Coot and further refined in standard pipelines (`QFIT-S003`, `QFIT-S008`).

Benchmarking:

- X-ray benchmark used 144 single-chain, unliganded, high-resolution structures from the PDB, clustered at 30% sequence identity and representing 72 CATH folds.
- qFit improved Rfree in most structures; the text reports 76% (109/144) in the results paragraph, while the figure caption reports 73%, so any use should cite this cautiously as "roughly three quarters" unless version/figure discrepancy is resolved (`QFIT-S004`).
- Deposited models had multiconformers in 2.9% of residues, while qFit models had multiconformers in 40.7% of residues in the analyzed dataset (`QFIT-S004`).
- Synthetic resolution-dependence tests show qFit best detects alternative conformations with high-resolution data around 1.8-2.0 Å or better (`QFIT-S005`).
- Cryo-EM benchmark was much smaller: eight structures after filtering for EMDB-calculated resolution better than 2 Å; qFit increased modeled alternative conformers and recapitulated/identified examples, but map handling and validation inconsistency remain major limitations (`QFIT-S006`).

## § 6 - 核心数学推导

The key formal object is BIC-style model selection over conformer cardinality.

At a high level, qFit balances two terms:

- density residual: how well calculated density from candidate conformers matches experimental density;
- complexity penalty: how many parameters are introduced by adding conformers, coordinates, and B-factors.

In qFit residue, the paper defines the number of parameters as proportional to `number of conformers * number of atoms * 4`, representing x/y/z coordinates plus B-factor. A heuristic scaling factor is used because coordinate parameters are not independent under chemical constraints (`QFIT-S003`, `QFIT-S008`).

The important intuition is not the exact formula alone; it is that qFit does not simply add conformers whenever density can be fit better. It penalizes complexity so the output remains parsimonious. This matters for our project because qFit-derived "dynamics" are discrete local conformers inferred from density, not arbitrary ensembles.

## § 7 - 实验设计与结论

Experiment 1: Does qFit improve X-ray model/data agreement without obvious overfitting?

Design: collect 144 high-resolution PDB structures, re-refine deposited models to normalize refinement protocol, run qFit, compare Rfree and R-gap. Result: qFit improves Rfree for roughly three quarters of structures and maintains similar R-gap, suggesting improved fit without gross overfitting (`QFIT-S004`).

Experiment 2: Does qFit recover and add alternative conformations?

Design: compare deposited and qFit models by residue-level alternative conformer count and rotamer assignment. Result: qFit greatly increases multiconformer residues; most residues are consistent with deposited models, while qFit adds additional rotamers in a minority of residues and highlights weak-density terminal chi-angle ambiguity (`QFIT-S004`).

Experiment 3: How resolution-dependent is qFit?

Design: generate synthetic data across 1.0-3.0 Å, use qFit to recover known or qFit-derived "ground truth" multiconformers. Result: multiconformer recovery falls off around 1.8-2.0 Å; single-conformer modeling remains more robust at lower resolution (`QFIT-S005`).

Experiment 4: Can qFit work on high-resolution cryo-EM maps?

Design: filter cryo-EM structures to those with EMDB-calculated resolution better than 2 Å, sharpen/re-refine maps, run qFit in EM mode, inspect examples. Result: qFit detects and recapitulates local alternative conformers in selected high-resolution cryo-EM cases, but inconsistent map processing and validation limit generality (`QFIT-S006`).

## § 8 - Take-aways

For Dynamics Atlas, qFit should be assigned to:

- source type: experimental density + computational model building;
- dynamics scale: mostly side-chain and local backbone alternative conformations;
- temporal meaning: no time order, no kinetics, no Boltzmann population unless additional assumptions/evidence exist;
- evidence strength: strong for density-supported local heterogeneity in high-resolution structures;
- failure mode: overinterpreting altloc occupancy as dynamic rate or equilibrium thermodynamics.

This paper is especially useful for the proposed toolkit because it provides an algorithmic way to locate an experimental ensemble dataset in "dynamics space": local/discrete/density-grounded/multiconformer, with resolution and input-model-quality gates.

## § 9 - 最脆弱的假设

The fragile assumption is that density-supported alternative conformers are a valid proxy for biologically meaningful conformational dynamics.

This is often useful but not automatically true. A qFit altloc can reflect real conformational heterogeneity, but it may also be affected by map quality, model bias, local resolution, crystal disorder, partial occupancy, solvent/background treatment, or refinement artifacts. The paper actively addresses some risks through Rfree/R-gap, synthetic tests, and cryo-EM caveats, but it does not turn local conformers into time-resolved dynamics.

For our project, the rule should be: qFit supports "local conformational heterogeneity" and hypothesis generation; it does not, by itself, support "slowest mode", "transition pathway", "rate", or "equilibrated dynamics".

## § 10 - 最小复现实验

One-week minimal experiment for the toolkit:

Data: choose 3-5 high-resolution PDB entries with deposited qFit outputs from the Zenodo/code availability record, ideally including one qFit paper example and one project-relevant enzyme/ligand structure.

Implementation:

1. Parse deposited single-conformer and qFit multiconformer PDB/mmCIF.
2. Count residues with altlocs.
3. Classify altlocs by side-chain-only, backbone-involved, local segment, ligand/water-adjacent.
4. Map residues to functional annotations if available.
5. Output a local-heterogeneity card per structure.

Measurement:

- number and fraction of multiconformer residues;
- altloc occupancy distribution;
- side-chain vs backbone involvement;
- residues near ligand/interface/catalytic site;
- whether structure resolution and Rfree pass qFit applicability gates.

Success criterion: the agent labels qFit evidence as "density-grounded local ensemble" and does not infer kinetics.

## § 11 - 最强反例设计

Counterexample 1: low-resolution or poorly modeled input. The paper already shows qFit depends on high-resolution data and good input models. A dataset with >2.5 Å resolution or high Rfree could produce misleading conformers.

Counterexample 2: local density ambiguity. Terminal side-chain chi angles in weak density can lead to rotamer disagreements; a qFit conformer may fit density but remain biologically uninterpretable.

Counterexample 3: global/domain motion. qFit's standard altloc representation is good for local heterogeneity but insufficient for nested ensembles, large domain rearrangements, or time-ordered transitions. A DynDom-style hinge/twist motion or TICA slow mode is a different evidence class.

Counterexample 4: occupancy-as-thermodynamics misuse. Altloc occupancy is a refined model parameter constrained by crystallographic/cryo-EM data and refinement choices; treating it as a direct equilibrium population or rate would overclaim.

## § 12 - Follow-up Research Idea

Non-incremental idea: build a `Density-to-Dynamics Classifier` inside the Dynamics Atlas toolkit.

Motivating limitation: qFit, ensemble refinement, multi-temperature crystallography, cryoDRGN-like cryo-EM heterogeneity models, and MD trajectories all encode ensembles differently.

Borrowed method: combine structural parsing, altloc topology, resolution/Rfree gates, and local functional annotation.

First experiment: For each experimental structure/model, classify evidence into:

- `local side-chain heterogeneity`;
- `local backbone heterogeneity`;
- `loop/segment heterogeneity`;
- `domain-level model ensemble`;
- `trajectory/time-resolved dynamics unavailable`.

Then compare this classification with MD-derived RMSF/TICA descriptors for overlapping proteins. Agreement would suggest cross-dataset concordance; disagreement would reveal where experimental density and simulation sample different parts of dynamics space.

## Nature-Reviewer-Style Critique

Reviewer 1 emphasis - technical soundness: The paper is technically persuasive for high-resolution X-ray cases because it normalizes refinement, uses Rfree/R-gap, tests resolution dependence, and explains input-quality requirements. The main weakness is boundary: selected cryo-EM examples are promising but constrained by inconsistent map processing and small benchmark size.

Reviewer 2 emphasis - originality and significance: The work is significant because it lowers the barrier to routine multiconformer modeling and makes hidden experimental heterogeneity computationally accessible. Its originality lies less in the concept that proteins have alternative conformers and more in the practical automation and updated model-selection/refinement pipeline.

Reviewer 3 emphasis - interdisciplinary readability: The paper is readable for structural biologists and understandable for computational biophysics users, but nonspecialists may overinterpret "ensemble" as time-resolved dynamics. Any atlas entry must explicitly state that qFit outputs are density-grounded structural alternatives, not trajectories.

Consensus: qFit is a central experimental/computational bridge for Dynamics Atlas, especially for side-chain and local backbone heterogeneity. It must be placed separately from MD trajectories, MSM/TICA, and domain-motion databases.

## Source Discipline

- Paper states: qFit input requirements, residue/segment algorithm, BIC and B-factor sampling, benchmark structure counts, Rfree/R-gap results, resolution dependence, cryo-EM caveats, data/code availability.
- Reasonable inference: Dynamics Atlas taxonomy placement and claim ceiling.
- Speculation: Density-to-Dynamics Classifier and cross-dataset comparison proposal.

