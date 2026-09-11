# Definitions behind the HSP90 trust judgments

Updated 11 September 2026

Every trust judgment for HSP90 in [RESULTS.md](RESULTS.md) rests on the definitions below. We chose them. None has been reviewed by a domain expert, and two failed a basic control on 11 September. For each definition we give what it is, where it came from, the control, how it compares with the paper, and the question we would like answered. The rules behind them are in [Rules Table version 2](data/rules/RULES_TABLE_V2.md); the numbers are in [data/operators/](data/operators/).

## Common setup

- 40 trajectories deposited by Henot et al. (2022). 20 start from representative open-state conformers and 20 from closed-state conformers of the authors' structural ensembles. The window is 20–1020 ns, with 1001 saved points per run, 1 ns apart. The run, not the frame, is the statistical unit.
- The ATP-lid is residues 98–136, as in the paper. Before lid RMSD is computed, each frame is aligned on residues 40–97 and 137–220. The paper superposes structures on residues 11–97 and 137–223; we have not found the reason for our narrower core in our records.
- The NMR references are the authors' open-state and closed-state structural ensembles.

## 1. Direction of change (OP1): usable

| | |
|---|---|
| Definition | A saved point points toward open when (a) lid RMSD to the closed-state medoid minus lid RMSD to the open-state medoid is positive, and (b) the closed-state contact-violation readout minus the open-state readout is positive. It points toward closed when both are negative, and is a conflict otherwise. A direction is sustained when it holds for 5, 20 or 50 consecutive points. |
| Origin | Our analysis of July 2026. |
| Control | All 20 open-start runs point toward open from the start of the window. Passed. |
| Paper | Uses pairwise lid RMSD, clustering and NOE violations; it has no direction readout. |
| Result | 10 of 20 closed-start runs show a sustained open direction. After their first sustained direction, 5, 4 and 1 reverse at 5, 20 and 50 points. |
| Open question | None pressing. This is a relative readout, so it cannot show that a state is reached (see 2). |

## 2. Agreement with the open-state NOE references (OP2): usable, in tension with the paper

| | |
|---|---|
| Definition | At each point, a run is near the open state when the mean violation of the open-state NOE contacts (authors' files, second data column) is at most τ and the closed-state violation exceeds τ. A run agrees with the open state when at least 80 % of its open-direction points are near open, and is relative only when at least half of them are far from both references. τ = 0.5, 1 and 2 Å, fixed before the analysis; 1 Å is the primary value. |
| Origin | Our preregistration of 10 September 2026. |
| Control | Open-start runs agree in 7, 18 and 19 of 20 cases at 0.5, 1 and 2 Å. At 1 Å the control passes. |
| Paper | About 9 of the 20 closed-start runs move toward "conformations almost compatible with the NOE restraints characteristic of the ATP-lid open state", with lid RMSD to open-start conformations as low as 1.5 Å. |
| Result | Of the 10 closed-start runs with a sustained open direction: at 1 Å, 0 agree, 1 partly and 9 relative only; at 2 Å, 3 agree, 2 partly and 5 relative only. |
| Note | Our check of the authors' deposited analysis script (5 September) found 19 open-state and 5 closed-state contacts, with one distance threshold per state. The paper reports 22 open-state and 5 closed-state characteristic NOEs. We do not know the reason for the difference. |
| Open question | What should "near the open state" mean here? A tolerance on the mean violation (and which value matches what the authors call almost compatible), a lid-RMSD neighbourhood (see 3), or the authors' clustering? |

## 3. Reference neighbourhoods (OP5, OP6): withdrawn

| | |
|---|---|
| Definition used | Radius = 95th percentile of each NMR ensemble's lid RMSD to its median structure (open 1.35 Å, closed 2.62 Å). A frame is near a reference when its lid RMSD to the nearest model of that ensemble is below the radius. |
| Control | Failed. 99.99 % of open-start frames fall outside both neighbourhoods, although 18 of 20 open-start runs agree with the open NOEs. |
| Why it fails | The radius measures how far the NMR models sit from each other. The frame distance also includes thermal motion over 1 μs. The two are different quantities, the kind of mismatch rule C005-RULE-001 describes. |
| Paper | Open-start conformations have an average pairwise lid RMSD of 4.0 Å; closed-start conformations, 9.3 Å. |
| Options | (a) A radius taken from the open-start runs themselves. It passes the positive control by construction, so it needs a negative control, such as the first 20 points of every closed-start run falling outside. (b) The paper's own measure: lid RMSD of each closed-start frame to open-start conformations sampled every 10 ns, with the authors' 1.5 Å as a reference point. (c) The authors' clusters, if their MD clustering can be reproduced from the paper. |
| Open question | Which definition would you accept, and which negative control should it pass? |

## 4. Whether state fractions have settled (OP3): not usable as run

| | |
|---|---|
| Definition used | Each point is labelled open, closed or neither from definition 2 at 1 Å. Fractions in the first 100, 250, 500 and 1000 ns are compared with the full run, and they count as settled if every difference is below 0.05. |
| Problems | The 0.05 threshold is ours and uncalibrated. The 1000 ns window is the full run, so that comparison is zero by construction. About half of all points (51 %) are labelled neither. |
| Established approach | Estimate the uncertainty of the observable from block averages and from the spread between independent runs (Grossfield et al. 2019). |
| Separate gate | A population needs crossings in both directions. No run returns (0 of 40), so no population can be stated whatever the window test says. |
| Paper | Does not estimate populations from MD. NMR relaxation dispersion gives 96.8 % and 3.2 % for the two states, with an exchange rate of 2490 s⁻¹. |
| Open question | Is "no population from these runs" the right entry, or should fractions also be reported with block-averaged uncertainty as descriptive numbers? |

## 5. Persistent changes (OP4): duplicate of 1

| | |
|---|---|
| Definition used | A change is counted when a run holds the opposite direction label from definition 1 for 5 consecutive points. |
| Result | 5 closed-to-open events in 5 runs, no returns. These are the same five events as in definition 1. |
| Open question | What should count as a completed transition? For example, reaching the open neighbourhood of definition 3 and staying there for a set time. |

## 6. ADK domains

| | |
|---|---|
| Definition | CORE residues 1–29, 68–115 and 168–214; NMP 30–67; LID 118–160. Our choice, not the authors'. Distances are measured inside the whole molecule. |
| Control | GROMACS reproduces the distances within 0.005 Å. This checks the arithmetic, not the choice of boundaries. |
| Open question | Should the authors' domain boundaries be used instead? |
