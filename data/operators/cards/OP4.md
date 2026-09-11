# OP4 `transition_count`

## Purpose

Count persistent C→O and O→C events, first arrival, returns, and endpoint state under a hysteresis-style persistence threshold.

## Input and parameters

- Input rows use the same signed direction rule as OP1.
- `hysteresis_k` is an integer from 5 through 50; F uses 5.
- Conflict/unknown labels break persistent segments. A return is a seeded-state persistent segment after an opposite-state segment.

## Output

The operator returns per-trajectory persistent sequences, transition counts, first arrival, return count, endpoint state, group summaries, and a global return fraction.

## Claim boundary

Persistent event existence is reportable when observed. A return-free set does not support a transition rate, equilibrium exchange, or mechanism claim.

