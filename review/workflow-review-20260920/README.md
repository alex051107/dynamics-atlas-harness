# Workflow reproduction — ChatGPT Pro review packet

This packet supports independent review of a proposed scientist-workflow reconstruction and analysis study. It is not a completed reproduction study or an implemented new harness.

用户目标：从科学家的实际分析流程和判断出发，尝试用现有数据支持与论文相近复杂度的结论，并在 2026-09-24 的会议中讨论流程与判断逻辑。固定工作流、记忆和控制程序是否有额外价值仍是待检验问题。

## Materials

| Material | Contents and status |
|---|---|
| [Pro prompt](PROMPT_ZH.md) | 可直接复制的独立审查请求 |
| [Current plan](documents/PLAN_ZH.md) | v1.0 stable execution baseline after self-review and three automated reviewers; scientific execution still pending |
| [Case execution cards](documents/CASE_CARDS_ZH.md) | Concrete K-Ras input-check target, MD-case entry conditions, completion and stopping definitions |
| [Review resolution](documents/REVIEW_RESOLUTION_ZH.md) | One cross-discussion round; retained design, minimal clarifications and unresolved scientific inputs |
| [Earlier architecture](documents/ARCHITECTURE_EARLIER_DRAFT_ZH.md) | Earlier, more database-oriented engineering draft; optional background, superseded in priority by the current plan |
| [Meeting transcript](meeting/TRANSCRIPT_RAW.txt) | Complete existing timestamped machine transcript, 452 segments; not manually verified word for word |
| [Meeting notes](meeting/MEETING_NOTES_ZH.md) | Chinese summary; distinguishes meeting discussion from later user steering |
| [Source status](SOURCE_STATUS.md) | All five starting-paper links, additional candidates, acquisition and analysis status |
| [K-Ras PDF](papers/pdf/KRAS2023.pdf) · [searchable text](papers/text/KRAS2023.md) | Original article PDF, 15 pages; extracted text is a reading aid |
| [Sampling-quality PDF](papers/pdf/Uncertainty2019.pdf) · [searchable text](papers/text/Uncertainty2019.md) | Original guide PDF, 24 pages; a methods/quality reference rather than a reproduction case |
| [Historical operator report](history/OPERATOR_REPORT_ZH.md) | Fixed-input operator and F/D/O development results, with limitations |
| [Historical four-layer report](history/FOUR_LAYER_REPORT_ZH.md) | Earlier decomposition/admission/method/feedback experiments, not evidence for the proposed new harness |
| [Rights and transformations](RIGHTS_AND_PROVENANCE.md) | Attribution, licenses, derivative limitations and meeting-source treatment |
| [Publication scope](PUBLICATION_SCOPE.md) | User authorization and exact review-only boundary |
| [File manifest](MANIFEST.json) | Transfer-identity hashes for packet files; excludes itself |

Choose the reading order according to the question being reviewed. The plan is a proposal to challenge, not a prescribed answer. The two PDFs have not been deeply analyzed in this task, and none of the newly proposed reproduction/model-comparison runs has been executed.

## Wider historical context

The prior review capsule is available at [operator-plan review material](https://github.com/alex051107/dynamics-atlas-harness/tree/df1d4a8/review/operator-plan-20260911). The [September 10 briefing](https://github.com/alex051107/dynamics-atlas-harness/blob/35940d37da4320d2f85d8f4c742a4589c9e47247/review/pro_briefing_20260910/INDEX_ZH.md) provides additional context. Referenced workspace paths in the verbatim historical reports are historical locators; not every artifact was copied into this packet.

The 2026-09-22 revision retains the two-case route and later A/B/C comparison; source data, scientific parameters and runtime budgets remain to be established. The review consensus is not domain-science approval.

The new packet is confined to review/workflow-review-20260920. No production/scientific code, frozen rule table or old experiment result is changed. It does not release scientific execution gates or authorize merging the review branch.

## Transcript and access limitations

The recording itself is not included. The transcript has no reliable diarization; speaker attribution in the summary is interpretive. Its opening silence includes a known ASR hallucination. An existing header lists possible terminology corrections; these suggestions are not independently verified quotations. Scientific and organizational statements in the transcript remain meeting statements.

GitHub can expose PDF files without making their contents readily available to an AI browsing tool. The page-marked text derivatives are therefore included. Equations, figures, tables and column order must be verified in the PDFs when material to a judgment. A local ZIP copy is also supplied to the user for direct attachment if browsing fails.
