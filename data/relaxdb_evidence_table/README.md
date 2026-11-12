# RelaxDB evidence table (draft, 12 November 2026)

Literature evidence of protein dynamics for the open RelaxDB proteins, in the column format built for the 10-protein CPMG workbook.
**Draft.** Rows have had an automatic check against the paper text. A sample of 15 papers had a blind review. A scientist has not reviewed the new rows.

| File | What it is |
|---|---|
| `RelaxDB_evidence_all_DRAFT.xlsx` | the workbook: Proteins, Evidence, Papers, Structures, Gaps, README |
| `coverage.csv` | per protein: which items have a value from a full-text row |
| `spine.csv`, `source_papers.csv`, `source_text_status.csv` | the 133-protein skeleton (deposited conditions, source papers) and the full-text status of each source paper. The 12 held-out entries are removed |
| `source_rows/<entry>__<doi>/rows.jsonl` | evidence rows read from each source paper (with `notes.txt`) |
| `cond_fill_out/*.jsonl` | sample conditions added to the 11-01 rows, each with its supporting snippet |
| `blind_review/` | the sample, the independent readings, the judges' verdicts and `summary.json` |

Not included: paper texts, PDFs and supplements.
