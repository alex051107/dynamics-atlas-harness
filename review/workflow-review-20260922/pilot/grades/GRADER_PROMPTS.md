# Grader prompts as sent (Opus, one call per paper)

Filled from the template in RUN_PROMPTS.md. The clarifications paragraph is the format and scope addition logged in PREREGISTRATION.md.

## XIE20

```text
You are grading four database entries written about the same paper, against a reference answer. You do not know how the entries were produced; do not guess. Grade each entry on its content only.

Reference answer (reference entry, must-get-right facts, over-claim list):
<pilot>/_sealed_reference/REF_XIE20.md
Task definition the entries were written to:
<pilot>/task_common.md
Entries, labeled E1 to E4:
<pilot>/grades/_blind/XIE20/E1.md
<pilot>/grades/_blind/XIE20/E2.md
<pilot>/grades/_blind/XIE20/E3.md
<pilot>/grades/_blind/XIE20/E4.md
Open only these files. You may open the paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC7920495/ ; Europe PMC full text https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7920495/fullTextXML) to settle a disagreement between an entry and the reference; say when you do.

For each entry, score items 1–9 as 0 (wrong or missing), 1 (partly right), 2 (right), or NA (the paper has no such information):
1 apo verdict and the ligand it is relative to; 2 major and alternative states; 3 exchange parameters with sources; 4 residues or regions; 5 identity basis; 6 structural mapping and simulations; 7 functional relevance, with wording matched to the evidence; 8 evidence type and provenance; 9 tier.
Then count: over-claims (statements the paper does not support, including those on the reference's over-claim list) and factual errors (wrong numbers, IDs, conditions). Give one line of justification per nonzero deduction.
Output a table (entry × items, over-claims, factual errors, total of scored items, number of scored items) and short notes. Write to <pilot>/grades/GRADE_XIE20.md and return the same content.

Clarifications. If the reference ends with an errata section, the errata override the text above them. A fact that appears only in the supplementary material and is missing from an entry counts as missing, not as a factual error. Use NA for an item only when the paper itself lacks that information, and then use it for all four entries. After the table, repeat the numbers in one fenced json block of this form, with null for NA: {"E1": {"items": [i1, i2, i3, i4, i5, i6, i7, i8, i9], "over_claims": n, "factual_errors": n}, "E2": {...}, "E3": {...}, "E4": {...}}.
If you need a web browser, open your own new tab and use only that tab; do not read or navigate any other tab. Do not open any other file on this computer.
```

## STILLER22

```text
You are grading four database entries written about the same paper, against a reference answer. You do not know how the entries were produced; do not guess. Grade each entry on its content only.

Reference answer (reference entry, must-get-right facts, over-claim list):
<pilot>/_sealed_reference/REF_STILLER22.md
Task definition the entries were written to:
<pilot>/task_common.md
Entries, labeled E1 to E4:
<pilot>/grades/_blind/STILLER22/E1.md
<pilot>/grades/_blind/STILLER22/E2.md
<pilot>/grades/_blind/STILLER22/E3.md
<pilot>/grades/_blind/STILLER22/E4.md
Open only these files. You may open the paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC9126080/ ; Europe PMC full text https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9126080/fullTextXML) to settle a disagreement between an entry and the reference; say when you do.

For each entry, score items 1–9 as 0 (wrong or missing), 1 (partly right), 2 (right), or NA (the paper has no such information):
1 apo verdict and the ligand it is relative to; 2 major and alternative states; 3 exchange parameters with sources; 4 residues or regions; 5 identity basis; 6 structural mapping and simulations; 7 functional relevance, with wording matched to the evidence; 8 evidence type and provenance; 9 tier.
Then count: over-claims (statements the paper does not support, including those on the reference's over-claim list) and factual errors (wrong numbers, IDs, conditions). Give one line of justification per nonzero deduction.
Output a table (entry × items, over-claims, factual errors, total of scored items, number of scored items) and short notes. Write to <pilot>/grades/GRADE_STILLER22.md and return the same content.

Clarifications. If the reference ends with an errata section, the errata override the text above them. A fact that appears only in the supplementary material and is missing from an entry counts as missing, not as a factual error. Use NA for an item only when the paper itself lacks that information, and then use it for all four entries. After the table, repeat the numbers in one fenced json block of this form, with null for NA: {"E1": {"items": [i1, i2, i3, i4, i5, i6, i7, i8, i9], "over_claims": n, "factual_errors": n}, "E2": {...}, "E3": {...}, "E4": {...}}.
If you need a web browser, open your own new tab and use only that tab; do not read or navigate any other tab. Do not open any other file on this computer.
```

## PONT15

```text
You are grading four database entries written about the same paper, against a reference answer. You do not know how the entries were produced; do not guess. Grade each entry on its content only.

Reference answer (reference entry, must-get-right facts, over-claim list):
<pilot>/_sealed_reference/REF_PONT15.md
Task definition the entries were written to:
<pilot>/task_common.md
Entries, labeled E1 to E4:
<pilot>/grades/_blind/PONT15/E1.md
<pilot>/grades/_blind/PONT15/E2.md
<pilot>/grades/_blind/PONT15/E3.md
<pilot>/grades/_blind/PONT15/E4.md
Open only these files. You may open the paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC4470301/ ; Europe PMC full text https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4470301/fullTextXML) to settle a disagreement between an entry and the reference; say when you do.

For each entry, score items 1–9 as 0 (wrong or missing), 1 (partly right), 2 (right), or NA (the paper has no such information):
1 apo verdict and the ligand it is relative to; 2 major and alternative states; 3 exchange parameters with sources; 4 residues or regions; 5 identity basis; 6 structural mapping and simulations; 7 functional relevance, with wording matched to the evidence; 8 evidence type and provenance; 9 tier.
Then count: over-claims (statements the paper does not support, including those on the reference's over-claim list) and factual errors (wrong numbers, IDs, conditions). Give one line of justification per nonzero deduction.
Output a table (entry × items, over-claims, factual errors, total of scored items, number of scored items) and short notes. Write to <pilot>/grades/GRADE_PONT15.md and return the same content.

Clarifications. If the reference ends with an errata section, the errata override the text above them. A fact that appears only in the supplementary material and is missing from an entry counts as missing, not as a factual error. Use NA for an item only when the paper itself lacks that information, and then use it for all four entries. After the table, repeat the numbers in one fenced json block of this form, with null for NA: {"E1": {"items": [i1, i2, i3, i4, i5, i6, i7, i8, i9], "over_claims": n, "factual_errors": n}, "E2": {...}, "E3": {...}, "E4": {...}}.
If you need a web browser, open your own new tab and use only that tab; do not read or navigate any other tab. Do not open any other file on this computer.
```

## WHIT13

```text
You are grading four database entries written about the same paper, against a reference answer. You do not know how the entries were produced; do not guess. Grade each entry on its content only.

Reference answer (reference entry, must-get-right facts, over-claim list):
<pilot>/_sealed_reference/REF_WHIT13.md
Task definition the entries were written to:
<pilot>/task_common.md
Entries, labeled E1 to E4:
<pilot>/grades/_blind/WHIT13/E1.md
<pilot>/grades/_blind/WHIT13/E2.md
<pilot>/grades/_blind/WHIT13/E3.md
<pilot>/grades/_blind/WHIT13/E4.md
Open only these files. You may open the paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC4078984/ ; Europe PMC full text https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4078984/fullTextXML) to settle a disagreement between an entry and the reference; say when you do.

For each entry, score items 1–9 as 0 (wrong or missing), 1 (partly right), 2 (right), or NA (the paper has no such information):
1 apo verdict and the ligand it is relative to; 2 major and alternative states; 3 exchange parameters with sources; 4 residues or regions; 5 identity basis; 6 structural mapping and simulations; 7 functional relevance, with wording matched to the evidence; 8 evidence type and provenance; 9 tier.
Then count: over-claims (statements the paper does not support, including those on the reference's over-claim list) and factual errors (wrong numbers, IDs, conditions). Give one line of justification per nonzero deduction.
Output a table (entry × items, over-claims, factual errors, total of scored items, number of scored items) and short notes. Write to <pilot>/grades/GRADE_WHIT13.md and return the same content.

Clarifications. If the reference ends with an errata section, the errata override the text above them. A fact that appears only in the supplementary material and is missing from an entry counts as missing, not as a factual error. Use NA for an item only when the paper itself lacks that information, and then use it for all four entries. After the table, repeat the numbers in one fenced json block of this form, with null for NA: {"E1": {"items": [i1, i2, i3, i4, i5, i6, i7, i8, i9], "over_claims": n, "factual_errors": n}, "E2": {...}, "E3": {...}, "E4": {...}}.
If you need a web browser, open your own new tab and use only that tab; do not read or navigate any other tab. Do not open any other file on this computer.
```

