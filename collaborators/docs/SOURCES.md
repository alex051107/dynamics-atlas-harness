# Primary sources and data provenance

| System | Primary paper | Data and use in this package |
|---|---|---|
| HSP90 | [Henot et al. (2022), Visualizing the transiently populated closed-state of human HSP90 ATP binding domain](https://doi.org/10.1038/s41467-022-35399-8) | Native NOE violation series and previously derived trajectory descriptors; source data availability is identified in the paper |
| DHFR | [Cetin et al. (2023), Kinetic Barrier to Enzyme Inhibition Is Manipulated by Dynamical Local Interactions in E. coli DHFR](https://doi.org/10.1021/acs.jcim.3c00818) | [Zenodo 7966540](https://zenodo.org/records/7966540); selected corrected local distances, not raw trajectories |
| ADK | [Orädd et al. (2021), Tracking the ATP-binding response in adenylate kinase in real time](https://doi.org/10.1126/sciadv.abi5514) | [Zenodo 5583119](https://zenodo.org/records/5583119); project-defined domain-distance tables |
| Nanodisc | [Bengtsen et al. (2020), Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with molecular dynamics simulations](https://doi.org/10.7554/eLife.56518) | Prior development case for observable-specific fitting and validation; not rerun in this package |

Two recent conceptual sources sharpened the distinction between structural coverage and measurement-supported distributions: [Are We Capturing the Ensemble?](https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html), by Li, Thomasen and Cossio (2026), and [Bhakat's T4 lysozyme study](https://doi.org/10.1021/acs.jcim.6c02044). Their role is to organize questions about what a measurement can distinguish, not to supply extra mandatory checks for every analysis.

## Exact numerical input lineage

`data/MANIFEST.json` records each included file, its original archive member, selected columns, row count, transformation and checksum. The source archive belongs to the frozen E2 evidence package at commit `1beb385d59fd2a4ae46bf654ac4b38d71468cc8d` of `alex051107/dynamics-atlas-harness`.

The portable files project only the columns required for these demonstrations. Numerical values are preserved; delimiters and field labels are normalized where documented. HSP90 author workstation paths in comment headers are not included. The notebook-style scientific acceptance checks retain the original analysis windows and tolerances.

This package is a research analysis derivative, not a relicense of source data. Cite the original papers and observe the deposit terms when acquiring or redistributing their full data.
