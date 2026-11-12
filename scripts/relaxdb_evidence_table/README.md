# RelaxDB evidence table: scripts

These scripts build and check the RelaxDB evidence workbook (see `review/20261112_relaxdb_table/REPORT.html`).
They expect the layout used when they were written: a work folder `~/dynamics_atlas_work/` (cached sources, ledgers, spine tables), an eval folder `~/dynamics_atlas_eval/` (the split file with the sealed list), and `ATLAS_WORKSPACE` pointing at the project workspace for the two scripts that read earlier workbooks.
Paper texts, PDFs and supplements are not in this repository (copyright). To rerun the checks you need your own copies of the papers.

| Script | What it does |
|---|---|
| `source_fulltext.py`, `access_fulltext.py`, `fulltext_check.py` | free legal full-text recovery and the identity check of dropped PDFs |
| `build_manifest.py` | lists papers with a checked full text and no reader folder yet |
| `check_rows.py` | checks evidence rows against the paper text (quotes, numbers, reasons, sealed entries) |
| `cond_fill/check_conditions.py`, `cond_fill/tripwire.py`, `cond_fill/find_text.py` | condition cells: snippet check, the not-reported tripwire, text lookup |
| `blind/check_items.py`, `blind/check_verdict.py`, `blind/score_blind.py` | blind review: checks and scoring |
| `build_all.py` | merges all rows into the workbook and runs its self-checks |
| `coverage.py` | per-protein coverage of the items |
| `verify_all.py` | reruns every check and the planted-defect canaries |
| `make_report.py` | builds the HTML report from the result files |
