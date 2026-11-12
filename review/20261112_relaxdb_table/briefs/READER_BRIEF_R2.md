# Round 2 delta to READER_BRIEF.md

Read `READER_BRIEF.md` first and follow it, with these changes for round 2:

- Your manifest is `source_read/manifest_round2.json` (not manifest.json). Your papers are the entries whose `batch` equals your batch number.
- `main_text` is already a text file for the paper (converted from the PDF; layout may be rough, tables may be garbled). Copy it to `paper.txt`.
  If a table you need is garbled in the text, find the original PDF: it is the file with the same stem and extension .pdf in the same folder as
  `main_text`; run `pdftotext -layout` on it and read the table from that. Quotes (anchors) must still appear in `paper.txt`, so append the better table text to paper.txt under `=== TABLE TEXT RERUN ===`.
- Supplements: `local_supplements` lists files already downloaded for this paper. Convert each PDF with `pdftotext -layout` and append it to paper.txt after a line `=== SUPPLEMENT: <file name> ===`. Do not curl anything when `local_supplements` is non-empty.
  When it is empty and `pmcid` is set, make the one Europe PMC supplementary-files request from the original brief. Otherwise write "no supplement available" in notes.txt.
- Folder name: `source_read/<first entry>__<doi with / replaced by _>/` as before. Papers already in `source_read/` from round 1 are not in your manifest.
- Many of these are 1990s papers. Old papers often print conditions in the Methods or a table footnote; search for them before you write an empty-reason.
- Some papers are short assignment notes with no dynamics data. For those, write the rows the paper supports (for example amide protection or missing peaks) or an empty rows.jsonl with the reason in notes.txt. An empty file is a correct answer when the paper has no dynamics evidence.
- Everything else (sealed list, no other agents' folders, check_rows.py until 0 errors, final reply format) is unchanged.
