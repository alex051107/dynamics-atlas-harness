# OP6 `coverage_vs_reference`

## Purpose

Classify each frame by overlap with the open and closed reference radii.

## Input and parameters

- `ONLY_OPEN`: within open radius and outside closed radius.
- `ONLY_CLOSED`: within closed radius and outside open radius.
- `BOTH`: within both radii.
- `NONE`: outside both radii.
- Trajectory bootstrap uses 1000 resamples with replacement; frames remain correlated within each trajectory.

## Output

The operator returns per-trajectory class counts/fractions, lineage-level descriptive means, bootstrap intervals, and the radius calculation.

## Claim boundary

Coverage is a four-class descriptive comparison to the selected NMR reference. MD-only coverage is not evidence for a new state or independent validation.

