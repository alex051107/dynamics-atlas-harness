# HSP90 D1 operator table

| metric | quantity | trust | evidence/result | allowed wording | forbidden wording |
|---|---|---|---|---|---|
| D1-01-direction-runs | persistent directional runs and opposite-direction candidates | credible_limited_window | `OP1_direction_runs__p7286bda5__i60bac79f; OP1_direction_runs__pcc97f5f0__i60bac79f; OP1_direction_runs__p8705a961__i60bac79f` | report direction and limited-window reverse candidates | equilibrium, exchange rate, mechanism |
| D1-02-noe-reference-arrival | open-direction/native-NOE agreement and tau sensitivity | credible_but_tolerance_sensitive | `OP2_noe_reference_crosswalk__p61ec8ada__i60bac79f` | same-source agreement decomposition and threshold sensitivity | independent experimental validation or kinetic arrival |
| D1-03-population-convergence | trajectory-level state fractions in 100/250/500/1000 ns windows | not_credible_as_population | `OP3_state_population_convergence__p73102ba2__if92cde8b; OP3_state_population_convergence__pcd0b3328__i60bac79f` | descriptive window comparison; no-return gate remains open | equilibrium population or thermodynamic weight |
| D1-04-transition-count | persistent C-to-O/O-to-C event and return counts | event_existence_only | `OP4_transition_count__p1faa5dbf__i60bac79f` | observed persistent event existence | rate when returns are zero |
| D1-05-excursions | outside-both-reference-radius contiguous stretches | descriptive_only | `OP5_excursion_detection__p637f0522__i60bac79f` | descriptive excursions with censoring | new state, mechanism, independent validation |
| D1-06-coverage | ONLY_OPEN/ONLY_CLOSED/BOTH/NONE frame coverage | descriptive_only | `OP6_coverage_vs_reference__p891435f0__i60bac79f` | four-class coverage relative to selected NMR reference | MD-only new state or independent validation |

Independent recompute: `PASS`, max absolute difference `0`.

Claim ceiling: same-source HSP90 analysis in the observed 20–1020 ns window; no equilibrium, rate, mechanism, new-state, or independent-validation upgrade.
