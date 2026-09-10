# What the current data support

Dynamics Atlas aims to make differences between protein-dynamics evidence interpretable and reproducible. Its scientific results concern specific observables under specified conditions. A structural change, a state population and a transition rate are different quantities and require different evidence.

## HSP90: direction and reference agreement answer different questions

The analysis covered 40 trajectories: 20 from closed-start structures and 20 from open-start structures. Each contributed 1001 saved points from 20 to 1020 ns. Under the five-point persistence definition, the closed-start set split into five initially open-direction trajectories, five that later entered an open direction and ten that never did. Thus, 10/20 does not mean ten newly observed opening events.

The native NOE series measures positive violations of experimental upper-distance bounds. At a 1 Å project tolerance, among the ten closed-start trajectories with open-direction frames, nine met the relative-direction-only criterion, one was partially consistent, and none met the open-reference agreement criterion. Among the 20 open-start controls, 18 were consistent, one partial and one relative-only.

This is a comparison with the deposited reference analysis, not an independent experimental replication. The tolerance changes the classifications, so the replay also reports 0.5 and 2 Å results. Movement away from a closed reference does not by itself establish an equilibrium population or transition rate. [Henot et al., 2022](https://doi.org/10.1038/s41467-022-35399-8).

## DHFR: a local proximity difference after correcting periodic coordinates

Four trajectories compared wild type (WT) and L28R with trimethoprim (TMP) and 4′-DTMP. The report used 990 frames per trajectory, corresponding to frames 11–1000, not all 1001 saved frames.

| Variant | TMP: mean M20–O3P / Å | 4′-DTMP: mean M20–O3P / Å |
|---|---:|---:|
| WT | 8.687677 | 4.622056 |
| L28R | 10.435783 | 4.808910 |

The corrected local distance is smaller with 4′-DTMP in both variants. Initial coordinate handling had produced apparent distances of roughly 60–90 Å from an inappropriate periodic representation. After correction, VMD reproduced the selected distances to approximately 0.00001 Å.

Each condition has one trajectory. These means describe local proximity, not independent replicate variability. A distance alone does not establish a hydrogen bond, which also depends on geometry, or a unique inhibition mechanism. O3P is the historical atom label, not a statement that TMP contains phosphate. [Cetin et al., 2023](https://doi.org/10.1021/acs.jcim.3c00818).

## ADK: neither endpoint comparison shows joint domain closure

The open-start trajectory contained 2253 frames over 0–450.4 ns; the closed-start trajectory contained 1678 frames over 0–335.4 ns. Domain separation was calculated as the average Cα-pair distance between project-defined regions. The first and last 10% of frames were compared.

| Starting structure | NMP–CORE change / Å | LID–CORE change / Å |
|---|---:|---:|
| Open | +0.070721 | +2.290411 |
| Closed | +1.090895 | +1.176421 |

Positive changes indicate greater separation for these descriptors. Neither comparison therefore shows both regions closing together. Distance distributions still overlap; endpoint-window changes do not describe every event in the trajectories.

The original physical checks reconstructed a complete molecule and compared selected atom-pair distances with GROMACS over all frames, with differences around 0.005 Å. An independent numerical implementation also checked the domain averages. The small replay package starts after this coordinate-preparation stage.

These deposited simulations are apo, with no ATP or AMP in the deposited structures. The source experiment examined ATP photorelease in the presence of AMP using time-resolved X-ray scattering. Different conditions and timescales prevent treating these descriptors as a reproduction or refutation of the paper's experimental intermediate. [Orädd et al., 2021](https://doi.org/10.1126/sciadv.abi5514).

## What comes next scientifically

The next useful comparison should specify the molecular distinction of interest, establish whether the inputs describe compatible objects and conditions, and select a mature forward model when comparing structures with experimental observables. A forward model predicts an observable from a structural model. A better fit to one observable need not identify a unique ensemble.

The current work supports a reproducible analysis workflow and a source-linked account of its assumptions. Broader biological generalization and independent domain review remain open.
