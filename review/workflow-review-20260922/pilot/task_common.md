# Task: write a Dynamics Atlas entry for one paper

Dynamics Atlas is a database of **alternative apo states**. An alternative apo state is a functionally relevant conformation that a protein samples when the ligand of interest is not bound. Evidence usually comes from NMR: slow exchange that shows two separate peaks, or minor ("excited", "invisible") states detected by exchange experiments such as CPMG relaxation dispersion, CEST, R1ρ or ZZ-exchange. Structures, mutants, binding data and simulations can support the claim. Always record relative to which ligand the protein counts as apo.

## Evidence tiers

- **Strong.** The paper reports the alternative state, there are exchange data and at least one independent line of support (mutant, ligand, second method or structure), and the numbers are traceable to the paper.
- **Weak.** Exchange evidence exists, but the identity, the origin or the functional link is missing one piece; say which.
- **Candidate.** Only a lead, such as peak doubling alone or an author's suggestion; say what should be measured next.
- **Not included.** The state pair is not an apo state under this definition (for example, it was only measured with substrate bound); give the reason.

## Rules

- Read only the paper named in your instructions and its supplementary material, plus BMRB or PDB entries that the paper itself cites (https://api.bmrb.io and https://data.rcsb.org). No general web search, and no other papers.
- For every field give the value, then the source type in brackets — [paper], [our reading of the paper's data] or [inference] — and a locator (section, figure, table, page).
- If the paper does not say something, write "not stated". Do not fill gaps from general knowledge.
- Output only the entry. Do not describe how you worked or what guidance you followed.
- At most 900 words.

## Entry format

Use exactly these headings, in this order.

1. **Protein** — name, species, UniProt if the paper gives it.
2. **Construct and conditions** — construct, mutations, bound nucleotide or cofactor, temperature, pH, field.
3. **Apo relative to** — the ligand whose absence defines "apo" here.
4. **Verdict** — strong, weak, candidate or not included, with a one-line reason.
5. **Major state** — description, population, matching structure.
6. **Alternative state(s)** — description, population, matching structure or "unmapped".
7. **Evidence type** — the experiments that detect the alternative state.
8. **Exchange parameters** — exchange rate, minor-state population, range of chemical-shift differences.
9. **Residues or regions** — where the difference is.
10. **Identity basis** — why the minor state is thought to resemble a known state.
11. **Structural mapping and simulations** — structures used, whether simulations sampled the state, or that none exist.
12. **Functional relevance** — which ligand or partner binds which state; effects on activity.
13. **Competing explanations addressed** — what alternatives the paper ruled out, and how.
14. **What this evidence cannot support** — claims a reader might make that the evidence does not justify.
15. **Provenance** — DOI, figure and table locators, BMRB and PDB IDs.
