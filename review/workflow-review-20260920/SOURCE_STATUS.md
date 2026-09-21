# Source acquisition and review status

Status at packet preparation, 2026-09-20. Acquisition, text extraction, scientific reading, reanalysis and validation are separate states.

## Five user-supplied papers

| ID | Source | Available in this packet | Remaining limitations |
|---|---|---|---|
| ADK2015 | Kerns et al., The energy landscape of adenylate kinase during catalysis. [DOI 10.1038/nsmb.2941](https://www.nature.com/articles/nsmb.2941) | Source link | Valid main/SI PDF not acquired for this packet; no completed deep read or reanalysis |
| IL2_2020 | De Paula et al., Interleukin-2 druggability is modulated by global conformational transitions controlled by a helical capping switch. [DOI 10.1073/pnas.2000419117](https://www.pnas.org/doi/10.1073/pnas.2000419117) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7132253/) | Source links | Main/SI PDF requests returned non-PDF responses. Locally captured HTML is not treated as a completed reading derivative and is not republished here |
| KRAS2023 | Hansen et al., Excited-state observation of active K-Ras reveals differential structural dynamics of wild-type versus oncogenic G12D and G12C mutants. [DOI 10.1038/s41594-023-01070-z](https://www.nature.com/articles/s41594-023-01070-z) | [Original PDF](papers/pdf/KRAS2023.pdf), [page-marked text](papers/text/KRAS2023.md) | SI/source-data package not included; no completed deep read, workflow reconstruction or reanalysis |
| RFAH2012 | Burmann et al., An α-helix to β-barrel domain switch transforms the transcription factor RfaH into a translation factor. [PMID 22817892](https://pubmed.ncbi.nlm.nih.gov/22817892/) · [DOI 10.1016/j.cell.2012.05.042](https://doi.org/10.1016/j.cell.2012.05.042) | Source links | Main/SI PDF requests returned non-PDF responses; no completed deep read or reanalysis |
| RFAH2025 | Cai et al., Unraveling structural transitions and kinetics along the fold-switching pathway of the RfaH C-terminal domain using exchange-based NMR. [DOI 10.1073/pnas.2506441122](https://www.pnas.org/doi/10.1073/pnas.2506441122) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12107155/) | Source links | Main/SI PDF requests returned non-PDF responses; no completed deep read or reanalysis |

The initial references were forwarded by the user from Soojung. They are development sources already exposed to the planning assistant, not held-out evaluation material.

## Additional sources and engineering references

- Grossfield et al. (2019), Best Practices for Quantification of Uncertainty and Sampling Quality in Molecular Simulations, article v1.0. [DOI](https://doi.org/10.33011/livecoms.1.1.5067), [publisher PDF](https://livecomsjournal.org/index.php/livecoms/article/download/v1i1e5067/913/2595), [packet PDF](papers/pdf/Uncertainty2019.pdf), [text](papers/text/Uncertainty2019.md). Acquired and converted only; used as a candidate quality reference.
- Chodera (2016), A Simple Method for Automated Equilibration Detection in Molecular Simulations. [DOI](https://doi.org/10.1021/acs.jctc.5b00784). Screening candidate; not acquired or deeply read for this packet.
- Zimmerman and Bowman (2015), FAST Conformational Searches by Balancing Exploration/Exploitation Trade-Offs. [DOI](https://doi.org/10.1021/acs.jctc.5b00737). Screening candidate for iterative sampling decisions; not a selected, data-ready reproduction case.
- [FutureHouse](https://github.com/Future-House), especially [LDP](https://github.com/Future-House/ldp) and [Aviary](https://github.com/Future-House/aviary), were examined for architectural ideas, not validated as a complete fit for this task.
- Design references include [effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), and [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence). These inform proposals; they do not establish effectiveness in this scientific setting.

## Meeting and historical evidence

The existing transcript was reused after decoded-audio identity verification. Two key portions were retranscribed with the same ASR model; this is not independent human validation. The 452 segments span approximately 64 minutes, and there is no reliable speaker separation.

The historical operator report documents a smaller-model development experiment with unequal operator access between groups and an absent second scorer. The four-layer report documents previous prompt/component comparisons. Their measured outcomes belong to their own protocols; neither establishes incremental value for the proposed high-reasoning workflow system.

## What is not present

No raw audio, raw NMR/MD data, newly generated scientific analysis, completed expert workflow report, new autonomous model run or formal scientific approval is included. Missing articles are represented by source links rather than fabricated PDFs or partial text presented as full papers.
