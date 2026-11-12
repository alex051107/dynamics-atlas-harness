# Judge: compare a table to the paper and to an independent reading

For each paper `Pxx` you are given in `judge/<Pxx>/`: `paper.txt` (the paper), `rows.json` (rows a model filled from this paper), and `items.json` (an independent reader's list of what the paper reports; copied from `reader/<Pxx>/items.json` when it is ready).
You are checking faithfulness, not whether the science is true. Be strict about binding a value to the right sample, residues, temperature and construct. Do not open any other folder or anything under `~/dynamics_atlas_eval/`.

Part 1, per row, per non-empty field among: method_class, temperature, ph, buffer, ligand_or_partner, construct_or_mutation, residues_author, timescale, population, alt_state_structure, stance, species_relation, anchor.
Decide "supported" (the paper states it for that sample), "contradicted" (the paper says something different: a number from another residue, construct, ligand state or temperature; stance overstating the evidence; wrong species relation; residue list from another process), or "not_in_paper" (cannot find it in paper.txt).
For every "contradicted" give a verbatim quote from paper.txt that shows it, and a note of at most 25 words.
Part 2, per item in items.json that has kind rate, population or state_pdb and target "target" or "other_construct": is it covered by some row of rows.json (same value, same sample)? Answer "covered" or "missing". For each "missing", say whether the paper really reports it for this protein ("real") or the reader misread ("reader_error"), with a short reason.
Output `judge/<Pxx>/verdict.json`: {"rows": [{"row_id", "fields": {field: verdict}, "contradictions": [{"field","quote","note"}]}], "items": [{"index", "kind", "covered", "missing_is": "real"|"reader_error"|null, "reason"}]}.
Run `python3 check_verdict.py judge/<Pxx>/verdict.json` until it prints 0 errors. Reply with one line per paper: rows judged, contradicted fields, missing real items.
