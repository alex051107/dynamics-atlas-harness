# Measurements, analysis choices and interpretation limits

## HSP90

An NOE (nuclear Overhauser effect) is distance-sensitive NMR evidence. The supplied native violation series records an average positive violation of an upper bound. It is not a measured coordinate distance. The native second column and the third-column pseudo-distance used by an older directional score are distinct quantities.

The portable table joins native open/closed violation values to previously computed geometry and contact-margin descriptors. An open-direction frame has both a positive geometry difference and a positive contact margin. At tolerance τ, an open-reference-compatible frame has open violation ≤ τ and closed violation > τ. A both-far frame has both violations > τ.

A trajectory with open-direction frames is classified as agreement if at least 80% of those frames are open-reference-compatible; as relative-only if at least 50% are both-far; otherwise as partial. A trajectory without open-direction frames is not applicable to that conditional comparison. The primary tolerance is 1 Å; 0.5 and 2 Å are sensitivity analyses. The five-point direction partition is taken from the frozen anatomy table. These project criteria do not define equilibrium states.

## DHFR

The portable input selects the corrected M20 nitrogen–O3P distance from four frozen tables and retains their original frame indices. TMP is labelled `tmpp` and 4′-DTMP `d4tmpp` in the files. The script excludes frames 0–10 and computes arithmetic means over frames 11–1000, corresponding to the reported 11–1000 ns window.

The earlier correction chose the appropriate nearby periodic ligand representation for a local protein–ligand measurement. The replay uses those corrected values; it does not repeat coordinate unwrapping or choose ligand images again. One saved frame is not an independent experimental replicate.

## ADK

The project regions are CORE residues 1–29, 68–115 and 168–214; NMP 30–67; LID 118–160. These project-defined descriptors are not the paper's full structural inference or a universal domain convention. The mean covers all Cα pairs between the mobile region and CORE.

Intramolecular distances were calculated on a complete protein representation. Shortening a long intramolecular vector by minimum-image wrapping can change the intended quantity. Extension beyond half the box length is therefore not itself a failed physical check.

The portable replay averages the first and last floor(n/10) frames. Open-start windows contain 225 frames and span 0–44.8 and 405.6–450.4 ns. Closed-start windows contain 167 frames and span 0–33.2 and 302.2–335.4 ns. It reports means, changes and full-trajectory medians.

## Reproduction levels

| Level | Included here? | Meaning |
|---|---|---|
| Read the scientific argument | Yes | English results, methods and primary sources |
| Recalculate table-to-report values | Yes, tested | Supplied analysed inputs, deterministic script and fixed container |
| Rebuild analysed tables from raw trajectories | No | Requires original deposits, topology/atom mapping, representation correction and scientific software |
| Repeat model-based Agent experiments | No | Separate experimental environment, provider access and budget |
| Independently validate biology | No | Additional appropriate experimental or expert evidence |

The expected-number comparisons are acceptance checks after recalculation. They do not supply the arithmetic results. Input hashes detect accidental replacement of the supplied table projections; they do not prove scientific validity.
