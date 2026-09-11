# OP3 `state_population_convergence`

## Purpose

Compare trajectory-level state fractions in windows beginning at 20 ns with the full 20–1020 ns window.

## Input and parameters

- `state_definition` is `state_core` or `noe_tau1`. The latter requires each row to carry `noe_state_tau1` or `noe_class`.
- Window lengths are integer nanoseconds in [100, 1000]; the F run uses 100, 250, 500, and 1000 ns.
- Bootstrap resamples trajectories with replacement 1000 times. The convergence rule is an absolute window-minus-full difference below 0.05 for every state.

## Output

Each window reports trajectory-mean fractions, full-window fractions, differences, convergence, and a trajectory bootstrap interval. Population credibility also requires OP4 returns in at least 50% of tracks.

## Claim boundary

Fractions are descriptive for the fixed trajectories. A single-direction/no-return result blocks an equilibrium-population claim even when a window is numerically close to the full window.

