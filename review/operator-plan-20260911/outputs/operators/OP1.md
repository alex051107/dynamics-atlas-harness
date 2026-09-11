# OP1 `direction_runs`

## Purpose

Count persistent OPEN/CLOSED directional runs in the fixed HSP90 20–1020 ns window and record the first opposite-direction candidate and any return candidate.

## Input and parameters

- Input rows contain `trajectory`, `time_ns`, `geometry_delta_A`, and `contact_margin_A`.
- OPEN requires both signed fields to be positive. CLOSED requires both to be negative. Any other row is `CONFLICT` and breaks a run.
- `persistence_ns` accepts integer values from 5 through 50. The F run uses 5, 20, and 50 ns separately.

## Output

`trajectory_records` reports the first persistent direction, first opposite run, return candidate, run sequence, and counts. `group_summary` aggregates by the fixed R46A_ES closed-seeded and R60A_GS open-seeded lineages.

## Claim boundary

The operator supports persistent directional events in the observed window. It does not establish equilibrium populations, exchange rates, mechanisms, or a new physical state.

