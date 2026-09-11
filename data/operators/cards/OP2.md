# OP2 `noe_reference_crosswalk`

## Purpose

Crosswalk the native NOE violation column against open and closed reference conditions at preregistered `tau` values.

## Input and parameters

- The native violation is the second numeric data column. The third pseudo-distance column is retained only as a diagnostic in the input record.
- Per-frame classes are `OPEN_NOE` (`Vo <= tau < Vc`), `CLOSED_NOE` (`Vc <= tau < Vo`), `BOTH_FAR` (both above `tau`), and `BOTH_NEAR` (both at or below `tau`).
- Default `tau` values are 0.5, 1.0, and 2.0 Å, with 1.0 Å primary. Agreement requires conditional `OPEN_NOE >= 0.8` among OPEN-direction frames. Relative-only requires `BOTH_FAR >= 0.5` when agreement is absent.

## Output

The operator returns one record per trajectory and tau, group judgment counts, frame class counts, and the open-start positive control at primary tau.

## Claim boundary

This is a same-source decomposition and threshold-sensitivity analysis. It is not independent experimental validation and does not produce kinetic claims.

