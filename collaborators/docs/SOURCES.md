# Primary papers and the evidence used in this brief

[Back to the research brief](../README.md) · [Author claims and project results](RESULTS.md)

The links below go to the original publications. Project interpretations and measurements are identified separately in the results page; reading a paper or reproducing selected numbers is not the same as validating its complete conclusion.

## Scientific cases

| Paper | Role in this work | Original paper and data |
|---|---|---|
| Henot et al., 2022. *Visualizing the transiently populated closed-state of human HSP90 ATP binding domain* | Compare finite-time direction labels with deposited native NOE reference violations. The authors' full structural and exchange-state interpretation uses additional evidence. | [Full text](https://www.nature.com/articles/s41467-022-35399-8), especially Fig. 4, Methods and Discussion; data links are in the paper's Data availability section |
| Bengtsen et al., 2020. *Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with molecular dynamics simulations* | Earlier cross-observable development case, and later method-guidance task; these are different project analyses. | [Paper](https://doi.org/10.7554/eLife.56518) · [Open-access full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7426092/) · [Deposited BME inputs and methods](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al/BME_reweight) |
| Cetin et al., 2023. *Kinetic Barrier to Enzyme Inhibition Is Manipulated by Dynamical Local Interactions in E. coli DHFR* | Selected protein–ligand distances after correction of periodic representation; not a reproduction of the full kinetic mechanism. | [Paper](https://doi.org/10.1021/acs.jcim.3c00818) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37491825/) · [Zenodo 7966540](https://zenodo.org/records/7966540) |
| Orädd et al., 2021. *Tracking the ATP-binding response in adenylate kinase in real time* | Context for the distinction between our apo MD descriptors and the authors' ATP-triggered scattering experiment. | [Paper](https://doi.org/10.1126/sciadv.abi5514) · [Zenodo 5583119](https://zenodo.org/records/5583119) |

## The two readings that changed the design question

**Li, Thomasen and Cossio, 31 August 2026 — [Are We Capturing the Ensemble?](https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html).** This is a conceptual blog, not an Agent experiment. The sections “How experiments constrain the source distribution,” “How processing can wash out the source distribution,” and “The question of ensemble resolution” explain why information must be assessed for a particular difference between distributions. Our inference is to ask what the evidence can distinguish before choosing a workflow. The blog does not prescribe a Rules Table or four software layers.

**Bhakat, 2026 — [Benchmarking Generative AI and Physics-Based Molecular Simulation for Sampling Conformational Heterogeneity in T4 Lysozyme](https://doi.org/10.1021/acs.jcim.6c02044).** Read the Supporting Information as well as the main article: Fig. 4 addresses finite production-budget sampling; S1 addresses FRET predictions; S6–S7 report estimated region weights. The useful distinction for this project is between structural-region coverage, estimated weights and experimental prediction. The article is not evidence that our rule selector or Agent is effective.

## Project evidence and reading scope

[Completed-pilot report](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md) · [Individual final scores](../../review/four-layer-20260910/outputs/UNBLINDED_SCORES.csv) · [Evaluation limitations](../../review/four-layer-20260910/outputs/METHODS_AND_LIMITS_ZH.md)

[Source-linked rule archive](../../review/pro_briefing_20260910/rules/rule_registry.tsv) · [What was read, and to what depth](../../review/pro_briefing_20260910/PAPERS_READ_ZH.md)

The rule archive contains candidate project interpretations of source material, not author-written runtime rules. Its states and identifiers do not establish scientific approval. The broad reading index distinguishes a stored file, searchable text, targeted reading and deeper analysis; this brief does not expand those reading claims.

## Numerical reproduction boundary

[The input manifest](../data/MANIFEST.json) identifies the files used by the portable HSP90/DHFR/ADK replay, their original archive members, selected columns, row counts and transformations. The source archive is recorded at commit `1beb385d59fd2a4ae46bf654ac4b38d71468cc8d`. The replay starts from analysed tables, not raw MD coordinates or experimental signals.

[Reproduction instructions](REPRODUCE.md) are optional. Reading the brief requires no Docker installation, API key or code execution. The earlier ZIP and offline page are preserved reproduction snapshots; they are not updated copies of the present decision brief. No new paper PDFs, raw trajectories or third-party data are redistributed by this documentation edit.
