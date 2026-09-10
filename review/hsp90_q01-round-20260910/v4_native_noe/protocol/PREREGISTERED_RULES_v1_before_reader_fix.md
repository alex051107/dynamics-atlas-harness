# Absolute NOE crosswalk preregistration v1
Source: v4 B1 adopted before this analysis.
40 trajectories, 1001 rows each; native index1..1001 maps to time20..1020ns.
V_open and V_closed are mean positive upper-bound violation in Angstrom, second column; no pseudodistance.
Tau={0.5,1.0,2.0}A; primary1.0. O iff Vo<=tau<Vc; C iff Vc<=tau<Vo; FAR both>tau; NEAR both<=tau. Zero is author's exact criterion; tau is project tolerance.
Reference p95 from all20020 open-start Vo points (numpy linear quantile). Entry = first50 consecutive points<=p95; later exit first50 above. Reference is same-data control, not independent calibration.
Direction = positive geometry_delta_A and contact_margin_A; opposite bothnegative; zero/conflict notO. Compare contact_margin_A to Vc-Vo with absolute tolerance1e-8.
Each trajectory: total category fractions; fractions conditional on O direction; noO => NOT_APPLICABLE. Agreement if O_NOE conditional fraction>=.8; relative-only if FAR>=.5; else partial. Open-start >=18/20 agreement at primarytau mandatory; otherwise STOP interpretation, no tuning.
Partitions use frozen anatomy at5/50. Endpoint means use first100 saved points [20,120)ns and last100 (920,1020]ns. No inclusive101-point means.
Preserve first-round part definitions. Output40040 frame rows and40 trajectory rows, alltau sensitivity in summary. Optional panel mapping only from visible SI labels; otherwise NOT_AVAILABLE.
Claim ceiling: decomposition of existing source readouts, no new experiment, no equilibrium population/rates, no verdict author classes wrong. No paid agent needed.
Validation: input identity once; alignment/shape/control in same computation once; report structure once. Output hashes once after generation.
