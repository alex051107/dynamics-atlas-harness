---
title: "Cross-validation of distance measurements in proteins by PELDOR/DEER and single-molecule FRET"
authors: ["Martin F. Peter", "Christian Gebhardt", "et al."]
year: 2022
journal: "Nature Communications"
doi: "10.1038/s41467-022-31945-6"
paper_id: C009
priority: P0
paper_role: "direct cross-method validation and probe-condition confounding"
full_text_status: "verified local publisher PDF and extracted text"
analysis_date: 2026-08-06
zotero_status: "not attempted: no Zotero tool available in current session"
tags: ["PELDOR", "DEER", "smFRET", "MalE", "cross-validation", "probe-artifact"]
---

# Peter et al. 2022 PaperForge deep read

## § 1 — 研究问题与重要性

本文直接比较 PELDOR/DEER 与 smFRET 是否在同一蛋白、同一 labeling sites、apo/holo conditions 下给出一致的 inter-probe distance 和 conformational-change trend。作者使用三个 substrate-binding proteins（包括 MalE）和 YopO，目标是识别一致性、差异来源和两种方法的互补价值，而非推出一个 universal conversion。[PET-S01]

## § 2 — 前人工作与不足

两种方法都能探测 nm-scale distance 和 conformational change，但 sample state、label chemistry、linker length、averaging 和 time window 不同。过去很少在多个 identical labeling sites 上做大规模 cross-validation，因此 disagreement 往往无法定位到 probe、condition 或 biology。[PET-S01; PET-S02]

## § 3 — 作者的思考路径

先用 crystal structures/accessible-volume simulations 预测两个 probe types 的 distance，再在相同 double variants、apo/holo ligand conditions 下测 DEER 和 smFRET。若出现 mismatch，进一步改变 cryoprotectant、FRET dye pair、做 anisotropy/lifetime/BVA，检查 label–protein interaction 和 fast dynamics，而不是直接选择一个方法为真。[PET-S02; PET-S03]

## § 4 — 核心 intuition

“same nominal distance”不等于 same observable。DEER 主要给 frozen-solution interspin distance distribution，smFRET 给 liquid-solution FRET efficiency/averaged distance；不同 labels 和 conditions 会改变 measured distribution。一个好的 cross-validation 应比较 trend、probe-aware forward prediction 和 error margins，并保存 disagreement 的 cause hypothesis。

## § 5 — 具体方法与完整 pipeline

1. 选择 HiSiaP、MalE、SBD2、YopO 的 double-cysteine variants；为每个 variant 记录 residue pair、ligand condition 和 probe type。
2. 用 mtsslWizard/FPS 等 probe models 预测 inter-probe distances。
3. DEER 在通常 50 K/frozen solution 条件下取得 distance distributions；smFRET 在 liquid solution 下取得 mean FRET efficiencies/distances。
4. 对 MalE 使用 87/127、36/352、29/352、134/186，其中后者是 same-domain no-change control expectation。
5. 对异常 variants 复测不同 dyes、无/有 cryoprotectant，并用 anisotropy、lifetime、BVA 判断 mobility/dynamics。
6. 只对 monomodal datasets 做 quantitative error comparison，同时保留 multimodal/dynamic datasets 的 qualitative analysis。[PET-S03; PET-S04]

## § 6 — 核心数学与 estimand

DEER 的 signal 由 dipolar coupling \(\sim r^{-3}\) 产生，反演为 interspin distance distribution；smFRET 的 efficiency 受 \(r^{-6}\) dependence 和 \(R_0\) 影响，常转换为 FRET-averaged distance。作者报告的 typical prediction tolerances 约为 DEER ±3.5 Å、smFRET ±5 Å，但这些是 probe/model/condition-specific error margins，不是跨来源统一 sigma。[PET-S05]

## § 7 — 实验设计与结论

大多数 datasets 两种方法对 ligand-induced trend 和 structure-based predictions 有总体一致性。MalE 中两种方法都能看到 substrate-induced closure，但 cryoprotectant 会影响 DEER state distribution；某些 HiSiaP smFRET anomalies 由 Alexa dyes 的 surface interaction 解释，换成 TMR/Cy5 后一致性改善。YopO apo 的 broader/multimodal behavior 还显示单一 FRET distance 会隐藏 conformational dynamics。[PET-S03; PET-S04]

定量上，选出的 15 个 monomodal datasets 两方法结果大致相差约 5 Å，整体 spread 约 ±10 Å；这只能说明该实验设计下的 practical agreement，不能证明同一结构 estimand。

## § 8 — Take-aways

1. `Paper states`: probe interaction、cryoprotectant 和 linker length 可以制造 source discrepancy。
2. `Paper states`: BVA/anisotropy/lifetime 是解释 smFRET mismatch 的必要 diagnostic，不能只看 mean FRET。
3. `Paper states`: MalE 是一个具体 cross-validation case，不是 universal benchmark。
4. `Reasonable inference`: Card 要记录 probe chemistry、sample physical state、averaging/selection、monomodal vs multimodal 和 negative control。
5. `Forbidden upgrade`: 两种方法“总体一致”不等于 all proteins、all distances 或 kinetics/populations 一致。

## § 9 — 最脆弱的假设

crystal structures 作为 state references、probe model 的准确性、frozen vs liquid condition 的可比性、labeling 不扰动 protein、BVA 对 sub-500 µs transitions 的盲区，以及 multimodal distance 的 reduction 都是潜在弱点。没有这些 metadata，数值差异不能被解释为 method error 或 biology。

## § 10 — 最小复现实验

只做 source audit：从 paper 的 MalE variants 建一个四行 comparison matrix，分别填 residue pair、expected direction、DEER condition、smFRET condition、probe model 和 negative-control status。检查同一套字段能否表达“trend agreement + absolute mismatch + probe-condition cause”，不执行新实验。

## § 11 — 最强反例设计

选一个 label-protein interaction 强的 pair，使 smFRET mean distance 偏移而 DEER 正常；再选一个 cryoprotectant-dependent DEER mixture，使两种方法对 population 不同。若 pipeline 只计算 absolute distance MAE，就会把两个不同 failure mode 混为一个分数。

## § 12 — Follow-up research idea

把 Peter 的 cross-validation 作为 later V0 exposed MalE calibration 的 guardrail：先验证 Card 能保留 `same system / different probe / different physical state / different averaging law / negative control / abstention`，再决定是否允许任何 structure-level comparison。MalE 仍不能作为 blind/held-out generalization evidence。

## Source-discipline summary

- Paper states: [PET-S01] abstract/introduction; [PET-S02] method comparison; [PET-S03] HiSiaP/MalE/SBD2 results; [PET-S04] YopO and probe-artifact analysis; [PET-S05] quantitative error and discussion.
- Reasonable inference: MalE Card fields and later exposed-calibration guardrail.
- Speculation: V0 replay implementation.
