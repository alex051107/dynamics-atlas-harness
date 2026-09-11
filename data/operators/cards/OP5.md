# OP5 `excursion_detection`

## Purpose

Detect descriptive stretches outside both NMR reference radii and censor stretches that reach the right tail.

## Input and parameters

- Reference radii are the 95th percentile of member-to-coordinate-median lid RMSD for the aligned open and closed NMR ensembles.
- Frame inputs provide `nearest_open_A` and `nearest_closed_A`; outside means both exceed their respective radii.
- `k` is the minimum contiguous frame count and accepts 5 through 50; F uses 5. An accepted event must touch an adjacent explicit OPEN/CLOSED cluster. A tail event is right-censored.

## Output

The result includes reference member RMSDs, radii, candidate/accepted events, censoring flags, and per-trajectory outside fractions.

## Claim boundary

Excursions are descriptive geometry relative to a fixed reference. They do not define a new state, establish a transition mechanism or rate, or count as independent validation.

