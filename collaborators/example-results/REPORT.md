# Reproduced scientific summaries

**PASS: all three table-to-report comparisons match the published reference values.**

This run recalculates results from the provided analysed tables. It does not regenerate coordinates, perform new MD, or establish independent experimental validation.

## HSP90

At the five-point persistence setting, the 20 closed-start trajectories split into 5 initially open-direction, 5 later open-direction and 10 never open-direction.

| Native NOE tolerance / Å | Start group | Consistent | Partial | Relative only | No open-direction frames |
|---|---|---:|---:|---:|---:|
| 0.5 | closed_seeded | 0 | 0 | 10 | 10 |
| 0.5 | open_seeded | 7 | 8 | 5 | 0 |
| 1.0 | closed_seeded | 0 | 1 | 9 | 10 |
| 1.0 | open_seeded | 18 | 1 | 1 | 0 |
| 2.0 | closed_seeded | 3 | 2 | 5 | 10 |
| 2.0 | open_seeded | 19 | 0 | 1 | 0 |

The classification is conditional on frames with an open direction. Direction alone does not establish absolute reference agreement.

## DHFR

| Condition | Frames | Mean M20–O3P distance / Å |
|---|---:|---:|
| tmpp-wt | 990 | 8.687677 |
| d4tmpp-wt | 990 | 4.622056 |
| tmpp-l28r | 990 | 10.435783 |
| d4tmpp-l28r | 990 | 4.808910 |

Each condition has one trajectory. Local proximity does not by itself establish hydrogen bonding, a unique mechanism or a dissociation rate.

## ADK

| Start | Domain | Frames per window | Last minus first window / Å |
|---|---|---:|---:|
| open | NMP | 225 | 0.070721 |
| open | LID | 225 | 2.290411 |
| closed | NMP | 167 | 1.090895 |
| closed | LID | 167 | 1.176421 |

Positive changes indicate greater separation for the project-defined descriptors. Apo MD does not reproduce the ATP-photorelease experiment.

## Provenance

The input manifest records the exact frozen archive, selected columns and checksums. See docs/METHODS.md and docs/SOURCES.md in the group package.
