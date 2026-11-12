# Brief: one workbook for all open RelaxDB proteins, in the format already built for Gina

Goal: Gina reviews literature evidence of protein dynamics per RelaxDB protein. A workbook in her agreed format
exists for 10 proteins. Evidence rows for about 120 more proteins exist in other shapes and were never exported.
Write `build_all.py` (in `~/dynamics_atlas_work/outputs/gina_table_20261112/`) that builds
`out/RelaxDB_evidence_all_DRAFT.xlsx`, and run it. Use `~/.venvs/taskfactory/bin/python` (it has openpyxl). Install nothing.

## Format to copy
`$ATLAS_WORKSPACE/autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs/gina_cpmg10_v03/out/RelaxDB_CPMG10_evidence_v0.3.2_draft.xlsx`
and its `../package/column_dictionary.csv`. The Evidence sheet's columns and their order are the contract. Add two
columns at the end: "Filled by" and "Checks passed".

## Inputs (read `coverage.py` in the same folder first: it already loads all of them)
1. The 10 CPMG proteins: copy Evidence rows from the v0.3.2 workbook unchanged. Filled by = "11-01 workbook v0.3.2".
2. `.../outputs/delivery_table_v02/out/Dynamics_Atlas_RelaxDB_v0.2_draft.xlsx`, sheet Evidence: the other entries of the 11-01 table. Map by column name.
3. `~/dynamics_atlas_work/ledger/run133_state.json` -> `cases/<fill.case>/rows.jsonl`: 78 entries, Sonnet rows.
4. Race entries listed in coverage.py: newest `cases/B1_r6_<entry>_*/rows.jsonl`.
5. `source_read/*/rows.jsonl` if any exist when you run (new source-paper reads; they may appear later, so the script must pick them up on rerun). Filled by = "11-12 source-paper read with supplement".
6. `~/dynamics_atlas_work/outputs/spine_20261112/spine.csv`: one row per protein with the deposited conditions.

Mapping for JSON rows (inputs 3 to 5): evidence_id = "<entry>-<row_id>" (prefix "S-" for input 5); Residues / region = residues_author;
Alternate-state structure = alt_state_structure; Related structures = related_structures, or the "related structures: ..." part of other_conditions;
Experiment = experiment; Timescale, Population as is; Exchange regime = the "regime (authors): ..." part of other_conditions;
Dynamics observed = dynamics_type; Authors' conclusion = author_claim; Experiment and conditions = other_conditions;
Temperature (K) = temperature as printed (do not convert); pH; Buffer; Ligand = ligand_or_partner; Phosphate = "yes" if buffer mentions phosphate, "" otherwise;
Construct = construct_or_mutation; Same sample as RelaxDB entry? = same_sample_as_deposit if present else "not assessed";
Organism / construct vs entry = species_relation; Caveats = caveat_note plus artefact_note; Paper = title; Year; DOI link = https://doi.org/<doi>;
Open full text = https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/ when source_file is PMC<digits>.txt, else "";
Quote = anchor; Location in paper = locator; Passage link = (Open full text or DOI link) + "#:~:text=" + URL-encoded first 8 words of the anchor;
What we read = "full_text" or "abstract_only" from access; Review priority = "A - please check" when review_priority is true.
A cell with an empty_reasons entry shows "[empty: <reason>]". Columns with no source stay empty.

## Sheets
- Proteins: one row per open protein from spine.csv (entry, set, name, UniProt, length, deposited temperature / field / pH / sample
  components with the origin of each value: BMRB or Gina's sheet; a sheet temperature of exactly 298.5 K with no BMRB value is shown as
  "298.5 (possible placeholder)"), then counts: evidence rows, full-text rows, papers, and for residues / alt-state PDB / timescale /
  population the number of full-text non-homolog rows that carry a value; and "Filled by".
- Evidence: all rows, v0.3.2 column order.
- Papers: one row per DOI: title, year, DOI link, open full text, entries, row count, what we read.
- Structures: one row per (entry, PDB id) parsed from Alternate-state structure, with the state text and row id.
- Gaps: one row per protein and item (residues, alt-state PDB, timescale, population, temperature, pH, buffer) that has no
  full-text value, with the most specific cause the data shows: "no full text read (n papers abstract only)",
  "read in full, not found", "not filled yet", "calls failed".
- README: what each sheet is, the row counts per input, and this sentence: "Draft. Rows from 11-11 have not had a blind accuracy check."

## Hard rules
- The 12 sealed entries (`~/dynamics_atlas_eval/gold/splits.json`, key `sealed`) must not appear in any sheet. Read only that
  key; open nothing else under `~/dynamics_atlas_eval/`.
- No local file paths, case folder names or model session ids in any cell.
- Do not change, move or delete any input. Write only inside `~/dynamics_atlas_work/outputs/gina_table_20261112/`.
- The script must be rerunnable and give the same workbook from the same inputs.

## Self-check the script must print (and you must report)
Rows per input read and rows written (they must match, list any dropped row with the reason); proteins in Proteins (expect 131);
sealed ids found (expect 0); cells containing "/Users/" or "B1_r6_" (expect 0); evidence_id duplicates (expect 0).

Final reply: the printed self-check, the path of the workbook, and anything you could not map.
