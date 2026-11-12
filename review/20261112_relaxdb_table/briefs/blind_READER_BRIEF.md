# Blind reader: list what a paper reports about the dynamics of its protein

You read scientific papers on protein dynamics. For each paper folder you are given, `reader/<Pxx>/paper.txt` is the paper text (main text, extracted from a PDF or XML; tables may be garbled).
You have NOT seen any table built from this paper and must not look for one. Do not open any folder other than your own paper folders: not `../judge`, not any `cases/` folder, not anything under `~/dynamics_atlas_eval/`.

Write `reader/<Pxx>/items.json`: a JSON list. One item for each of the following that the paper reports for its protein (including other constructs of it; mark homologs separately):
- kind "rate": every exchange or kinetic rate or lifetime (kex, kAB, kBA, kopen, kclose, tau_ex, Rex values, flip rates, interconversion rates). One item per distinct value and sample.
- kind "population": every population or fraction of a state (major/minor %, pB, occupancy).
- kind "state_pdb": every PDB id the authors tie to a distinct conformational state of the protein (not merely a comparison structure).
- kind "condition": for each NMR or other dynamics sample: temperature, pH, buffer, field strength(s).
- kind "residues": every explicit list of residues the authors say show exchange or other slow dynamics.
- kind "order": order parameters or fast-motion results for named residues or regions (summarize one item per named region or table).
Each item: {"kind", "value" (as printed), "sample" (construct, ligand state, mutant, temperature if stated), "quote" (verbatim from paper.txt, 8 to 40 words, containing the value), "where" (section, figure or table), "target": "target" | "other_construct" | "homolog"}.
Quotes must be copied character for character from paper.txt. Do not compute values. Do not skip values that appear only in a table; read table text carefully, and say "garbled" in `where` when a table is too garbled to read.
Then run `python3 check_items.py reader/<Pxx>/items.json` until it prints 0 errors.
Reply with one line per paper: items per kind, and anything unreadable.
