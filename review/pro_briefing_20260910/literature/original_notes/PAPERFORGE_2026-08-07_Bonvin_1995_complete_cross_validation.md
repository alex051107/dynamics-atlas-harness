---
title: "Conformational Variability of Solution Nuclear Magnetic Resonance Structures"
authors: ["Alexandre M. J. J. Bonvin", "Axel T. Brunger"]
year: 1995
journal: "Journal of Molecular Biology"
volume_pages: "250(1), 80–93"
doi: "10.1006/jmbi.1995.0360"
pmid: "7602599"
paper_id: C013
challenge_case_id: V003
priority: P0
paper_role: "scientific challenge for overfitting control and claim-specific cross-validation"
full_text_status: "verified local public PDF and extracted text"
pdf_sha256: "f1e3cd0e20d9610c7c59fdaca6efbaaaabac4a9456fea0a88cd858bed862484e"
analysis_date: 2026-08-07
rule_relevance: "C003-RULE-003; C006-RULE-002; C006-RULE-003; C012-RULE-003"
gate_relevance: "G1 native observable and estimand; G2 uncertainty and restraint semantics; G4 validation role; G5 bounded claim"
claim_status: "source-grounded analysis; draft challenge case; not a frozen rule"
zotero_status: "not attempted: no Zotero tool available in current session"
tags: ["NMR", "NOE", "complete-cross-validation", "ensemble-refinement", "overfitting", "Rule-Layer", "V003"]
---

# Bonvin and Brünger 1995 PaperForge deep read

## 先说结论

这篇论文不是在说“conformer 越多越好”，也不是在给所有 heterogeneous data 提供一个统一指标。它回答的是一个更窄、但对我们很关键的问题。

当模型增加自由度后，拟合误差下降到底代表数据真的支持了更复杂的结构，还是只代表模型更容易把已见数据拟合好。

作者的处理很清楚。先用 fitted NOE restraints 看模型是否能解释数据，再把 NOE 数据分成十份，轮流留出一份做 complete cross-validation。最后用 synthetic reference、IL-4 和 IL-8 三种情形检查模型复杂度是否能被区分。结果不是一个统一答案。Protein G、Amb t V 和 IL-8 支持 twin-conformer 的 bounded conclusion，而 IL-4 的 cross-validation 反而支持 single-conformer。

对我们的验证设计来说，最有价值的不是 twin 这个具体答案，而是它把“fit 变好”和“模型被外部约束支持”拆开了。

## Source Record

| 字段 | 记录 |
| --- | --- |
| Canonical record | DOI 10.1006/jmbi.1995.0360，PMID 7602599 |
| 论文入口 | [PubMed record](https://pubmed.ncbi.nlm.nih.gov/7602599/) |
| 本地 PDF | `workspace-source/autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/literature/fulltext/PDFs/Bonvin_1995_JMB_Conformational_variability_complete_cross_validation.pdf` |
| 抽取文本 | `workspace-source/autoresearch/tasks/dynamics_atlas_literature_card_male_pilot_20260805/outputs/literature/fulltext/extracted_text/Bonvin_1995_JMB_Conformational_variability_complete_cross_validation.txt` |
| PDF 核验 | 14 pages by `pdfinfo`; 2,239,136 bytes; SHA-256 `f1e3cd0e20d9610c7c59fdaca6efbaaaabac4a9456fea0a88cd858bed862484e` |
| Text 核验 | 781 lines; 8,823 words; SHA-256 `c1f9fb7601e2faac00843f7e060a949a48bdfb4104380ec139046b220773e02a` |
| Access note | A publicly accessible PDF copy was used for local reading. Access was not treated as a separate reuse-license confirmation. |
| Exposure | Paper conclusion was visible before this case was selected. This is a retrospective exposed challenge, not project-level held-out evidence. |

## §1 研究问题与重要性

### 论文在问什么

NMR 的 NOE restraints 是时间平均或 ensemble average。用一个结构去解释具有真实 conformational variability 的体系，可能会把多个构象强行压成一个平均结构。反过来，如果直接增加 conformer 数量，参数会明显增多，也可能发生 overfitting。作者要判断的是，complete cross-validation 能不能帮助选择一个足够解释数据、又不过度增加自由度的 ensemble model。[BON-S01; BON-S02]

### 这个问题为什么重要

如果没有外部约束，任何增加模型自由度的做法都可能看起来更好。对我们来说，这对应一个更一般的规则。

> 一个 source-native fit 的改善，只能说明该 source 在当前模型下变得更容易解释，不能单独说明模型复杂度、状态数或结构 variability 得到了独立支持。

这条规则后来可以迁移到 FRET、SAXS、EM 或 dynamics observable，但迁移的是验证逻辑，不是 NOE 的数值阈值。

## §2 前人工作与不足

作者指出，X-ray 与 solution NMR 本身都测到时间或 ensemble average。传统单结构 refinement 能给出一个方便的结构，却不一定表达 solution 中的 variability。多构象 refinement 提供了表达 variability 的方式，但自由参数随 conformer 数量增长，拟合下降可能只是参数数量增加的结果。[BON-S02]

论文的补足点不是另造一个“复杂度分数”，而是引入 test subset。每次 refinement 只用一部分 NOE，随后检查没有参与 refinement 的那部分是否仍然被解释。这个思路后来成为本文最适合进入 Rule Layer 的部分。[BON-S02; BON-S10]

## §3 作者的思考路径

1. 先承认 native observable 是 ensemble-averaged NOE distance，而不是普通的单结构几何距离。
2. 构造已知 reference ensemble 的 synthetic test case，检查 cross-validation 是否能找回参考 variability。
3. 改变 conformer 数量，比较 fitted-data RMSD 与 omitted-data RMSD、violations 的变化。
4. 改变 error-bound 条件，测试规则是否依赖 restraint semantics。
5. 将同一流程放到 IL-4 和 IL-8，观察 cross-validation 是否能给出不同的 model-complexity decision。
6. 对 IL-8 进一步检查 MD stability、15N relaxation exchange broadening 和 X-ray packing，避免把一个 NMR 模型选择直接升级成 population 或 mechanism。[BON-S04; BON-S05; BON-S06]

这条链路值得保留，因为每一步都对应一个可审查的 evidence role。拟合是 fit evidence，省略 subset 是 validation evidence，synthetic reference 是 recovery evidence，orthogonal measurements 是解释或边界证据。

## §4 核心 intuition

最重要的一句话是，模型对已见数据的解释力和模型对未参与拟合的数据的预测力不是一回事。

Protein G 的 fitted RMSD 随 conformer 数量增加而下降，但 cross-validated RMSD 和 violations 在超过两个 conformer 后变差。Twin-conformer 同时更接近 reference variability。Amb t V 也出现 single 到 twin 的明显改善，而继续增加 conformer 没有显著收益。[BON-S03; BON-S04]

IL-4 更能说明为什么规则不能写成“复杂模型优先”。其 fitted RMSD 从 single 到 twin 下降，但 cross-validated RMSD 和 violations 随 conformer 增加而升高。作者还发现 twin model 的 effective B-factor 明显过高，因此选择 single-conformer。[BON-S05]

IL-8 则是相反的 bounded case。Cross-validation 在 twin-conformer 处有 minimum，loop 16–22 出现两种构象。作者同时指出，X-ray 中看不到 alternate conformation 不能排除 solution 中存在它，因为 crystal packing 可能压住该区域；15N exchange broadening 和两次 100 ps unrestrained MD stability 提供了额外支持，但不提供 population 或 kinetics。[BON-S06]

## §5 方法与完整 pipeline

### Synthetic Protein G

- 56-residue IgG-binding domain。
- 30 ps vacuum MD at 300 K，取最后 20 ps 生成 80 个结构。
- 生成 854 个 (r^{-6})-averaged NOE distances，并设置 error bounds。
- 比较 single 到 multiple conformer ensembles。
- 用十个 omitted subsets 做 complete cross-validation。[BON-S03; BON-S08]

### Synthetic Amb t V

- 40-residue ragweed allergen，loop 被构造成两个 reference conformations。
- 生成 1031 个 (r^{-6})-averaged NOE distances。
- 比较 1–6 个 conformers，并使用 0%、10%、20%、25% error-bound 或 qualitative ranges。
- 结果显示，error bounds 改变会改变最优 conformer 数量，直接比较不同 error-bound 的 cross-validated 数值并不成立。[BON-S04; BON-S08]

### Experimental IL-4 与 IL-8

- IL-4 使用 1ITL 起始结构、qualitative NOE ranges、hydrogen-bond 和 torsion restraints，并与两个 X-ray structures 的 B-factors 比较。
- IL-8 使用 1IL8 起始结构、qualitative NOE ranges、hydrogen-bond 和 torsion restraints，并与 3IL8、15N relaxation、MD stability 和 receptor-binding context 交叉检查。
- Cross-validation 只应用于 NOE data。Hydrogen-bond 与 dihedral restraints 没有做 cross-validation。[BON-S05; BON-S06; BON-S10]

### Probability-map refinement

作者用 probability map 让 multi-conformer ensemble 变成更物理一致的结构表达。它改善的是 ensemble 的表示方式，不是一个新的 independent validation source。[BON-S07; BON-S11]

## §6 核心数学、observable 与 estimand

### Native observable

NOE restraint 使用 ensemble-averaged distance

\[
r_{ens}=\langle r^{-6}\rangle^{-1/6}.
\]

因此这里的 observable 不是“结构里两原子的直线距离”，而是由 NOE averaging law 决定的 effective distance。若把它改成普通 geometric distance，规则就已经换了对象。[BON-S08]

### Validation quantities

作者主要监测两个 test-set quantities。

1. Omitted NOE distance RMSD。
2. Omitted NOE restraints 中超过 0.2 Å 的 violations 数量。

NOE distances 分成十个 subsets，每一份轮流省略；每个 model complexity 运行十次 refinement，再平均 omitted-set quantities。[BON-S10]

### 本项目的 draft estimand

在论文的 NMR ensemble-refinement 条件、给定 (r^{-6}) forward semantics 和给定 error-bound condition 下，某个 conformer count 对 omitted NOE data 的平均预测误差与 violation burden。

这个 estimand 不能升级成真实 state population、transition rate、free-energy landscape 或普适结构准确度。

### 一个必须保留的边界

作者明确说，不同 error bounds 的 cross-validated quantities 不能直接比较，因为 error bounds 同时改变了 working set 和 test set。即使 0% bounds 的平均结构更接近 reference，它的 cross-validated RMSD 和 violation 也可能更高。[BON-S04]

这正是我们要放进 Card 的字段。`error_model` 不是附注，而是 comparison eligibility 的一部分。

## §7 实验设计与论文结果

| 情形 | Fitted-data 结果 | Cross-validation 结果 | 论文的 bounded interpretation |
| --- | --- | --- | --- |
| Protein G | conformer 越多，fit 越好 | twin 改善，超过 twin 后变差 | twin 更接近 reference variability |
| Amb t V | single 到 twin 改善 | twin 有显著改善，继续增加无显著收益 | twin 足以表达两个 loop conformations |
| IL-4 | single 到 twin 的 fitted RMSD 改善 | conformer 增加后 RMSD 与 violations 变差 | single 更可信，twin 过拟合 |
| IL-8 | fitted curve 较平，twin 只有浅 minimum | twin 的 cross-validated measures minimum | twin loop representation 得到多条证据支持 |

IL-8 的多条证据包括 loop 16–22 的 twin structure、两个 100 ps unrestrained MD 中没有 transition、His18 的 exchange broadening、较高 order parameter，以及 crystal packing 对 alternate state 的遮挡解释。[BON-S06]

需要特别注意，MD stability 在这里不是 held-out validation，也没有测 population。它只支持“两个构象可能是相对稳定的 distinct minima”这一层解释。[BON-S06]

## §8 创新点、价值与遇到的问题

### 创新点

1. 把 complete cross-validation 引入 ensemble-averaged NOE refinement，用 omitted data 约束 model complexity。
2. 用 synthetic reference、正向结果和反向结果一起测试规则，而不是只展示一个成功案例。
3. 明确展示同一逻辑可以给出 single、twin 或 abstain-like bounded decision，避免把方法写成固定答案。
4. 将 probability-map refinement 与 cross-validation 分开。前者改善结构表示，后者判断模型是否过拟合。

### 对 Dynamic Data 的价值

这篇论文给我们的不是 NOE 阈值，而是一条可以迁移的审查顺序。

`native observable → forward/averaging semantics → fitted evidence → omitted or orthogonal evidence → complexity decision → claim ceiling`

它直接支持四条 draft rules。

- `C003-RULE-003` 不能把 fitted-data improvement 当成 cross-validation。
- `C006-RULE-002` 复杂度增加必须面对 prior、test-set 或另一个明确的 external constraint。
- `C006-RULE-003` 不同案例可以得到不同 bounded model decision。
- `C012-RULE-003` paper-internal cross-validation 不能升级成 project-level generalization。

### 论文自身的问题

- Synthetic reference 来自短时间、特定 force field 和特定 restraints 的 MD，不是独立实验真值。
- 不同 error bounds 之间不能直接比较，说明 cross-validation 数值依赖 data semantics。
- IL-4 的 X-ray B-factors 受 crystal packing 影响，不能被当成简单 gold standard。
- IL-8 的 100 ps MD 没有 transition，只能支持短时间稳定性，不能测慢 kinetics。
- 15N exchange broadening、X-ray packing 与 receptor-binding context 都是支持性证据，不能独立证明 population。
- Cross-validation 只覆盖 NOE，hydrogen-bond 和 dihedral restraints 的贡献没有同等 held-out 检查。
- 这是一个 NMR-specific case。把它直接推广到 SAXS、FRET 或 EM，需要重新定义 observable、forward model 和 uncertainty。

## §9 最脆弱的假设与 failure modes

| 假设 | 失效后会发生什么 | Rule Layer 应如何处理 |
| --- | --- | --- |
| Omitted NOE subset 代表相同 data-generating semantics | test-set 不能代表目标 claim | `ABSTAIN`，保留 source-specific limitation |
| (r^{-6}) averaging model 合适 | geometric distance 与 NOE observable 被混用 | `NOT_COMPARABLE` |
| error bounds 已正确表达 uncertainty | model ranking 可能只是 bounds effect | `ABSTAIN` 或只做 side-by-side |
| synthetic reference 足够接近 target variability | recovery result 被误当成 independent truth | 只能算 within-study recovery |
| orthogonal evidence 真正独立 | 多个来源共享同一偏差 | 降低 claim ceiling，要求 next measurement |
| X-ray 与 solution condition 可比 | crystal packing 造成假冲突 | `CONDITION_MISMATCH` |

## §10 最小验证实验

本轮不复刻 X-PLOR，也不生成新的 NMR ensemble。最小验证是 Rule Layer 的 evidence-routing replay。

### 输入

- 论文的 native observable、error-bound 条件、conformer count、working/test role。
- Protein G、Amb t V、IL-4、IL-8 的 fitted 与 cross-validated result summary。
- 论文对 MD、B-factors、exchange broadening 和 crystal packing 的边界说明。

### 预期输出

- 对 IL-4，不能因为 fitted RMSD 改善就输出 twin pass。
- 对 Protein G、Amb t V 和 IL-8，可以输出 bounded twin-support route，但要保留 paper-specific conditions。
- 对不同 error-bound datasets，禁止把 cross-validated numeric rank 直接横向比较。
- 对 population、kinetics、mechanism 或 project generalization，输出 `ABSTAIN`。

### 验收标准

1. 先经过 G0 到 G5 的完整路由。
2. `fit improvement` 与 `held-out support` 必须出现在不同字段。
3. 所有四个 challenged rule 都有 source locator 和 case assertion。
4. 任何 forbidden upgrade 都会使 case fail，而不是被文字弱化。
5. 由于 paper conclusion 已暴露，本轮结果只能叫 retrospective development replay。

## §11 最强反例设计

最危险的错误是做出一张只有 `fitted RMSD` 的表，然后得出“conformer 越多越合理”。

反例输入可以保持论文中的 IL-4 fitted-data curve，却删除 omitted-set RMSD、violation count、error-bound condition 和 B-factor boundary。一个只看拟合的系统会把 IL-4 错判为 twin 或更复杂 model。正确的 Rule Layer 必须在 G2 或 G4 阻止该结论，并指出缺少 test-set support。

第二个反例是把 IL-8 的 twin structure、MD no-transition 和 His18 exchange broadening 合并成“已经测得两个 state 的 population 和 kinetics”。这会测试 G5 claim ceiling。正确结果应该保留结构 variability 的 bounded claim，并对 population 与 kinetics `ABSTAIN`。

## §12 Evidence Comparability Card 草案

| Card 字段 | V003 的填写 | 不能写成 |
| --- | --- | --- |
| Scientific claim | model complexity must be supported by omitted NOE fit, not fitted fit alone | more conformers are generally better |
| Native observable | ensemble-averaged NOE distance using (r^{-6}) law | generic atom-pair distance |
| Statistical unit | ten omitted NOE subsets per refinement condition | one paper-level score |
| Error model | declared NOE error bounds or qualitative ranges | common cross-modal sigma |
| Validation role | within-paper complete cross-validation | project-level held-out validation |
| Positive support | Protein G, Amb t V, IL-8 bounded twin decisions | universal twin rule |
| Negative support | IL-4 fitted improvement without cross-validated support | failed experiment |
| Claim ceiling | paper-specific model-selection evidence | population, kinetics, mechanism or generalization |
| Abstention route | missing held-out role, changed error semantics, or unsupported upgrade | force a numeric rank |

这张 Card 不是第二套规则。它是 Rule Registry 的 reader-facing review view，并且必须能回到本地 PaperForge note、全文行号和 Case Packet。

## §13 Source Record 与 Rule extraction

### 证据矩阵

| Evidence item | Paper source | Evidence role | Strength for V003 |
| --- | --- | --- | --- |
| in-sample RMSD | BON-S03, BON-S04, BON-S05, BON-S06 | fit input/result | 必要但不能独立选复杂度 |
| omitted-set RMSD and violations | BON-S10 plus figure descriptions | within-study cross-validation | 主要 model-selection evidence |
| synthetic reference recovery | BON-S03, BON-S04 | recovery control | 支持方法在自洽 synthetic case 中可判定 |
| IL-4 versus IL-8 contrast | BON-S05, BON-S06 | negative and positive paper cases | 防止把规则写成固定答案 |
| error-bound caveat | BON-S04 | uncertainty and comparability boundary | 直接阻止跨 bounds 数值合并 |
| MD stability | BON-S06 | orthogonal supporting context | 只支持 stability，不支持 kinetics |
| 15N exchange broadening | BON-S06 | orthogonal supporting context | 支持 multiple species hypothesis，不给 population |
| X-ray packing | BON-S06 | condition/confounder explanation | 阻止把 crystal absence 当作 solution absence |

### Draft claim seal

> 在 Bonvin 与 Brünger 1995 的 NMR ensemble-refinement 条件下，模型复杂度的接受必须依赖 omitted NOE cross-validation；fitted-data improvement 不能单独支持增加 conformer 数量。

允许的解释是 paper-specific model-selection evidence。禁止把它升级为真实 population、kinetics、mechanism、所有蛋白通用规律或项目层面的 held-out performance。

## §14 Follow-up research idea

下一步应当不是马上把 Bonvin 的 0.2 Å 或十份 subset 复制成所有 modality 的固定阈值，而是把验证结构抽象成四个可替换字段。

1. source-native observable。
2. source-specific forward or averaging model。
3. omitted, orthogonal 或 independent validation role。
4. claim-specific acceptance relation 与 abstention route。

然后再用一个跨 modality 的 conflict case 检查这四个字段能否处理“不同 sources 都有数据，但它们不是同一个 observable”的情况。若没有明确 bridge，输出 `NOT_COMPARABLE`，而不是把多个 residual 平均成 universal score。

## Source-discipline summary

- `Paper states`：BON-S01 至 BON-S11 所标出的论文事实、方法、结果和限制。
- `Reasonable inference`：把 fitted versus omitted 的验证逻辑转化为 V003 Rule Layer challenge，并把 Card 字段写成 source-native 结构。
- `Design proposal`：R4 draft Case Packet、R5 coverage audit 和后续 R6 human freeze 前的 acceptance relation。它们还不是论文结论，也不是已执行的 scientific validation。
