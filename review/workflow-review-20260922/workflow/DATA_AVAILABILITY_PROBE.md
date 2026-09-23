# Public data availability for the four development systems

Probe date 2026-09-22. Read-only API and page checks by four assistant sub-agents; nothing was downloaded. IDs below were seen in API responses or the papers' own text. Items marked *uncertain* were not fully verified.

## Summary

| System | Paper full text | BMRB shifts | Exchange data (CPMG/CEST) | PDB | Author deposits | Public MD |
|---|---|---|---|---|---|---|
| AdK (Kerns 2015) | Yes, PMC4318763 (open, NIH manuscript) | 19089–19093, shifts only (E. coli AdK + ADP; 19089 has 4 temperatures) | Not deposited; SI only | 4JL5, 4JLD, 4JLB, 4JL8, 4JL6, 4JLA, 4JKY, 3SR0, 4JLO, 4JLP, 4CF7 (all Aquifex, all ligand-bound); 2RGX apo Aquifex used as MR model | None; 3 SI files | MDAnalysisData "AdK equilibrium": apo AdK, 1.004 µs, 4,187 frames, CHARMM27 (source PDB not stated on page); Figshare DIMS/FRODA closed→open ensembles (*uncertain*, snippet only). Not in ATLAS (6 codes checked) |
| IL-2 (De Paula 2020) | Yes, PMC7132253, CC BY-NC-ND | 27969 (free WT), 27970 (+JES6-1), 27971 (+IL-2Rα), 27974 (R52A); mouse; shifts only | Not deposited; SI PDF only (pnas.2000419117.sapp.pdf, 3,438,595 bytes) | 1M47 (apo human), 1M48 (+Ro 26-4550), 2B5I (receptor complex), 4YQX (mouse + JES6-1) | None | None found (ATLAS, mdCATH checked). Lead: Woodward et al. 2025 JMB (PMC12077578) ran NMR + MD on human IL-2 variants; deposit status unknown |
| K-Ras (Hansen 2023) | Yes, PMC10584678, CC BY 4.0; SI = 2 PDF + 4 XLSX (Source Data) | 52021 (WT·GTP), 52023 (G12D·GTP), 52024 (G12C·GTP); pH 7.0; 283 K (WT, G12D) and 288 K (G12C); shifts only | Dryad 10.5061/dryad.j6q573nm0, CC0: README.md 1,267 B; NASR.zip 28,118 B; RelaxationDispersion.zip 1,090,383 B (ChemEx input text files). Mirror: Zenodo 10.5281/zenodo.8187159 | 5VQ2 (WT·GTP, real GTP), 4OBE, 6MBU (WT·GDP), 4EPR (G12D·GDP), 6ASE (A59G·GDP), 6ASA (D33E·GDP); no GppNHp, no G12C structure | Dryad as above | None found (ATLAS confirmed absent; DESRES has no K-Ras download) |
| RfaH (Burmann 2012; Cai 2025) | 2012: PMC3430373 author manuscript, not OA-licensed but readable; 2025: PMC12107155, CC BY-NC-ND | 52718 (CTD state A), 52719 (CTD state B, "minor state"), both with shifts + NOE, T1, T1ρ, RDC; 17615 (CTD structure, matched by title, not cited in the 2012 paper); related 52348, 52444 (full length, Cai 2024 Biochemistry; 52444 includes 2,468 atm high pressure) | Not in BMRB. Cai 2025: Figshare 10.6084/m9.figshare.28629485.v1 (raw CEST/CPMG + MATLAB fitting scripts) | 2LCL (CTD β-barrel, NMR, from 2012), 2OUG (full length α, X-ray); Cai 2025 prints "6C6C", which resolves to an unrelated structure; likely meant 6C6S or 6C6T (RNAP–RfaH cryo-EM) | 2025 Figshare as above; 2012 none | Third-party only: Zenodo 12594323 (AWSEM structure-based model, fold-switching trajectories), Zenodo 8061752 (MELD × MD free energies) |

## Details cited elsewhere in the plan

- **BMRB 19089 citation is stale.** Its entry record (`https://api.bmrb.io/v2/entry/19089?format=json`) lists the citation as "Catalytic Strategies used by Kinases in Phosphoryl-Transfer Reactions", status "in preparation", journal PNAS. The link to Kerns 2015 (NSMB) rests on the paper's own accession statement ("BMRB: 19089, 19090, 19091, 19092, and 19093") and matching authors. Entry 19090's related-entries label reads "EADK_CPMG_CaADP (25C)", yet its only data type is assigned chemical shifts.
- **IL-2 BMRB entry titles** (from the BMRB instant search): 27969 "Backbone amide and MILV methyl chemical shift assignments of mouse Interleukin-2"; 27970 "ILV(proS) methyl assignment of mIL-2 in complex with JES6-1 scFV antibody"; 27971 "ILV(proS) methyl assignment of mIL-2 in complex with IL-2Ra (CD25) receptor"; 27974 "MILV methyl chemical shift assignments of the R52A mutant of mouse Interleukin-2". So the two complexes carry ILV proS methyls only.
- **K-Ras Dryad usage note** (dataset metadata, files not opened): "All relaxation dispersion data are provided as text files that can be used by the ChemEx software. A table of relaxation rates and S² values is provided for NASR results."

## What this means for the plan

1. **No exchange data in BMRB for any of the four systems.** BMRB holds chemical-shift assignments (plus standard T1/T2/NOE/RDC for RfaH 2025). Newer papers put exchange data in general repositories (Dryad, Figshare); older ones leave it in the SI.
2. **K-Ras is the best recomputation target.** Source Data XLSX supports a Table 2 recomputation with pandas; the Dryad files would allow a full ChemEx refit, which needs installing ChemEx.
3. **IL-2 supports a partner-perturbation check from BMRB alone** (27969 against 27970 and 27971). The exchange fit itself needs the SI PDF.
4. **RfaH 2025 is the most complete deposit** (raw data plus fitting code) and has a separate BMRB entry for the minor state. The 2012 structural result (0.65 Å against NusG-CTD) is recomputable from PDB.
5. **AdK is the only system with a public apo trajectory**, but the 2015 paper studies the substrate-bound enzyme, so an MD check would test apo AdK claims from other papers.
6. **Condition mismatches are real stuck points:** K-Ras BMRB assignments (283/288 K) versus exchange experiments (298 K); AdK crystal structures (Aquifex) versus NMR and kinetics (E. coli).
7. **Tooling notes:** the PMC OA web service (oa.fcgi) now returns 404; use Europe PMC REST (`/<PMCID>/supplementaryFiles`, `/fullTextXML`). PMC and publisher pages show CAPTCHA or Cloudflare challenges to scripts; do not bypass them. BMRB JSON (`api.bmrb.io/v2/entry/<ID>?format=json`) works without pynmrstar.

## API calls that worked

```text
https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=<DOI>&format=json
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<DOI>&format=json&resultType=core
https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML
https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/supplementaryFiles
https://api.bmrb.io/v2/instant?term=<protein name>
https://api.bmrb.io/v2/entry/<BMRB ID>?format=json
https://data.rcsb.org/rest/v1/core/entry/<PDB ID>
https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.j6q573nm0
https://datadryad.org/api/v2/versions/246187/files
https://zenodo.org/api/records/<record id>
```
