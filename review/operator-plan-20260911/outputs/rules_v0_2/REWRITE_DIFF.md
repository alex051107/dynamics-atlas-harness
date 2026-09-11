# Rules v0.2 rewrite diff

This file compares the unchanged registry wording with the executable four-field copy. The source registry remains at `dynamics-atlas-harness-showcase/data/rules/rule_registry_v0.1.csv`. The new fields define execution context and claim limits; they do not add paper findings.

## Row-level changes

### C001-RULE-001 | Layer B | hellenkamp_2018_smfret_benchmark

- Original proposed rule: 在 G0>G1>G2 的重点检查中要求 raw/apparent/corrected E, R_<E>, R_MP and averaging law；若无法验证则走 ESTIMAND_UNSPECIFIED。
- Applies when: 当研究使用 measurement_semantics，且本规则所列字段（raw/apparent/corrected E, R_<E>, R_MP and averaging law）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：A smFRET comparison unit must distinguish raw/apparent and corrected FRET efficiency, FRET-averaged distance, and accessible-volume mean-position distance; these are different estimands. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 source_native_measurement 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 ESTIMAND_UNSPECIFIED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C001-RULE-002 | Layer B | hellenkamp_2018_smfret_benchmark

- Original proposed rule: 在 G1>G2>G3 的重点检查中要求 correction, R0, dye/AV and propagated measurement/model uncertainty；若无法验证则走 UNCERTAINTY_UNRESOLVED。
- Applies when: 当研究使用 uncertainty_provenance，且本规则所列字段（correction, R0, dye/AV and propagated measurement/model uncertainty）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：FRET distance uncertainty must include measurement correction, R0, dye-motion/AV and model assumptions rather than only histogram spread. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 uncertainty_aware_comparison 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 UNCERTAINTY_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C001-RULE-003 | Layer B | hellenkamp_2018_smfret_benchmark

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 inter-lab variation, precision versus biological accuracy and calibration status；若无法验证则走 CALIBRATION_STATUS_UNKNOWN。
- Applies when: 当研究使用 measurement_quality，且本规则所列字段（inter-lab variation, precision versus biological accuracy and calibration status）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：A standardized DNA benchmark establishes measurement reproducibility under its stated setup, not universal protein-distance accuracy or biological dynamics validity. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 calibrated_source_comparison 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 CALIBRATION_STATUS_UNKNOWN，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C002-RULE-001 | Layer B | agam_2023_smfret_reliability

- Original proposed rule: 在 G0>G1>G2 的重点检查中要求 source-native observable and corrected/raw status；若无法验证则走 OBSERVABLE_UNSPECIFIED。
- Applies when: 当研究使用 measurement_semantics，且本规则所列字段（source-native observable and corrected/raw status）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：A protein smFRET comparison unit must retain the corrected FRET observable, condition, label/probe context, and calibration semantics; a bare structural distance is not an equivalent substitute. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 source_native_measurement 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 OBSERVABLE_UNSPECIFIED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C002-RULE-002 | Layer C | agam_2023_smfret_reliability

- Original proposed rule: 在 G1>G2>G3>G5 的重点检查中要求 dye/linker behaviour, AV/ACV, averaging law, probe artifact checks and model uncertainty；若无法验证则走 FORWARD_MODEL_OR_PROBE_UNVERIFIED。
- Applies when: 当研究使用 forward_bridge，且本规则所列字段（dye/linker behaviour, AV/ACV, averaging law, probe artifact checks and model uncertainty）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：A structure/ensemble-to-smFRET comparison requires an explicit dye/linker forward model; dye–protein interaction checks may alter the model choice and accuracy. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 probe_aware_forward_model 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 FORWARD_MODEL_OR_PROBE_UNVERIFIED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C002-RULE-003 | Layer C | agam_2023_smfret_reliability

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 BVA/E-tau dynamic shift, photophysical alternatives, probe artifacts and timescale；若无法验证则走 PROBE_ARTIFACT_OR_PHOTOPHYSICS_UNRESOLVED。
- Applies when: 当研究使用 artifact_exclusion，且本规则所列字段（BVA/E-tau dynamic shift, photophysical alternatives, probe artifacts and timescale）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：A BVA or E–τ dynamic shift is a measurement-level deviation that needs photophysical and probe-artifact alternatives to be considered before it supports a conformational-dynamics claim. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 qualitative_diagnostic_matrix 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 PROBE_ARTIFACT_OR_PHOTOPHYSICS_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C003-RULE-001 | Layer B | dimura_2020_fret_assisted_modeling

- Original proposed rule: 在 G1>G3>G4 的重点检查中要求 candidate support, informative pair selection and complexity-aware fit definition；若无法验证则走 CANDIDATE_SUPPORT_UNVERIFIED。
- Applies when: 当研究使用 candidate_design，且本规则所列字段（candidate support, informative pair selection and complexity-aware fit definition）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：FRET-guided structure modeling requires an explicit candidate ensemble, probe-aware forward model, informative-pair design and independent validation pairs. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 candidate_support_and_pair_selection 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 CANDIDATE_SUPPORT_UNVERIFIED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C003-RULE-002 | Layer C | dimura_2020_fret_assisted_modeling

- Original proposed rule: 在 G1>G3>G4 的重点检查中要求 RMP restraint, prior ensemble, fit objective and model uncertainty；若无法验证则走 PRIOR_OR_MODEL_UNRESOLVED。
- Applies when: 当研究使用 reweighting，且本规则所列字段（RMP restraint, prior ensemble, fit objective and model uncertainty）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：A high-quality FRET fit cannot repair a missing fold or state from the initial candidate support; failure should route to prior/support revision. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 forward_model_reweighting 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 PRIOR_OR_MODEL_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C003-RULE-003 | Layer B | dimura_2020_fret_assisted_modeling

- Original proposed rule: 在 G3>G4>G5 的重点检查中要求 training/guiding versus held-out pairs and complexity penalty；若无法验证则走 NO_HELDOUT_SUPPORT。
- Applies when: 当研究使用 held_out_validation，且本规则所列字段（training/guiding versus held-out pairs and complexity penalty）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：Model uncertainty, reference-structure accuracy and agreement with FRET are separate quantities and must be reported separately. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 held_out_cross_validation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 NO_HELDOUT_SUPPORT，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C005-RULE-001 | Layer A | fuertes_2017_saxs_smfret_non_equivalence

- Original proposed rule: 在 G0>G1>G2 的重点检查中要求 observable, spatial support, time averaging and inverse-model semantics；若无法验证则走 ESTIMAND_OR_SUPPORT_MISMATCH。
- Applies when: 当研究使用 estimand_non_equivalence，且本规则所列字段（observable, spatial support, time averaging and inverse-model semantics）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：A SAXS-derived global radius of gyration and a terminal smFRET-derived dye distance are distinct observables with different spatial support, averaging and inverse-model assumptions; matching system and condition alone does not make them one direct numeric comparison. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 qualitative_difference_preservation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 ESTIMAND_OR_SUPPORT_MISMATCH，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C005-RULE-002 | Layer D | fuertes_2017_saxs_smfret_non_equivalence

- Original proposed rule: 在 G1>G3>G4>G5 的重点检查中要求 source-native observables plus an explicit joint-ensemble or qualitative relation；若无法验证则走 BRIDGE_UNAVAILABLE。
- Applies when: 当研究使用 complementary_evidence，且本规则所列字段（source-native observables plus an explicit joint-ensemble or qualitative relation）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：A reproducible SAXS–smFRET discrepancy can be scientifically informative and may require a joint latent-ensemble analysis rather than error averaging or selection of one preferred modality. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 qualitative_triangulation_or_joint_ensemble 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 BRIDGE_UNAVAILABLE，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C005-RULE-003 | Layer C | fuertes_2017_saxs_smfret_non_equivalence

- Original proposed rule: 在 G1>G3>G4 的重点检查中要求 distance-distribution assumption and model-check result；若无法验证则走 INVERSE_MODEL_UNSUPPORTED。
- Applies when: 当研究使用 inverse_model，且本规则所列字段（distance-distribution assumption and model-check result）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：Generic polymer distributions used to invert mean FRET values require system- and condition-specific scrutiny; non-uniform heteropolymer expansion can decouple terminal and global dimensions. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 distribution_forward_or_inverse_model 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 INVERSE_MODEL_UNSUPPORTED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C006-RULE-001 | Layer C | shevchuk_2017_bayesian_saxs_refinement

- Original proposed rule: 在 G1>G2>G3>G4 的重点检查中要求 SAXS likelihood, physical prior, nuisance error and state-weight parameterization；若无法验证则走 POSTERIOR_AMBIGUITY。
- Applies when: 当研究使用 forward_bridge，且本规则所列字段（SAXS likelihood, physical prior, nuisance error and state-weight parameterization）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：SAXS ensemble refinement needs an explicit intensity forward model, physical prior, nuisance/systematic-error model and posterior uncertainty because the curve is low-information. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 Bayesian_forward_model 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 POSTERIOR_AMBIGUITY，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C006-RULE-002 | Layer C | shevchuk_2017_bayesian_saxs_refinement

- Original proposed rule: 在 G2>G3>G4 的重点检查中要求 posterior, prior sensitivity, nuisance error and entropy/regularization choice；若无法验证则走 PRIOR_DOMINANCE_OR_MISSING_STATE。
- Applies when: 当研究使用 uncertainty_integration，且本规则所列字段（posterior, prior sensitivity, nuisance error and entropy/regularization choice）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：Posterior weight-boundary behavior can test whether a small-state representation is plausible, but the inferred structural weights remain condition- and prior-dependent. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 Bayesian_or_MaxEnt_reweighting 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 PRIOR_DOMINANCE_OR_MISSING_STATE，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C006-RULE-003 | Layer D | shevchuk_2017_bayesian_saxs_refinement

- Original proposed rule: 在 G1>G3>G4>G5 的重点检查中要求 candidate-support coverage, state-number adequacy and missing-state audit；若无法验证则走 MISSING_STATE_SUPPORT。
- Applies when: 当研究使用 claim_ceiling，且本规则所列字段（candidate-support coverage, state-number adequacy and missing-state audit）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：If candidate support omits a state, Bayesian SAXS refinement can express uncertainty within the wrong support but cannot create the missing state. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 bounded_hypothesis_set 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 MISSING_STATE_SUPPORT，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C007-RULE-001 | Layer B | bengtsen_2020_multimodal_nanodisc

- Original proposed rule: 在 G0>G1>G3 的重点检查中要求 per-source observable, spatial/contrast support, averaging law and condition；若无法验证则走 SOURCE_SEMANTICS_MERGED。
- Applies when: 当研究使用 multi_source_semantics，且本规则所列字段（per-source observable, spatial/contrast support, averaging law and condition）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：NMR/NOE, SAXS/SANS and MD in the nanodisc study constrain different spatial scales and observables; their values should not be merged into one common numeric metric. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 source_specific_likelihoods 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 SOURCE_SEMANTICS_MERGED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C007-RULE-002 | Layer C | bengtsen_2020_multimodal_nanodisc

- Original proposed rule: 在 G1>G3>G4 的重点检查中要求 BME/MaxEnt operator, MD prior, perturbation/entropy and source weights；若无法验证则走 INTEGRATION_OPERATOR_UNVERIFIED。
- Applies when: 当研究使用 integration_operator，且本规则所列字段（BME/MaxEnt operator, MD prior, perturbation/entropy and source weights）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：BME/maximum-entropy reweighting combines source-specific likelihoods while limiting perturbation from an MD prior; it is not a state-discovery or kinetics estimator by itself. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 shared_weights_source_specific_forward_models 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 INTEGRATION_OPERATOR_UNVERIFIED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C007-RULE-003 | Layer D | bengtsen_2020_multimodal_nanodisc

- Original proposed rule: 在 G2>G3>G4>G5 的重点检查中要求 source independence, condition match, forward calculations, shared-error audit；若无法验证则走 SHARED_ERROR_OR_CONDITION_MISMATCH。
- Applies when: 当研究使用 integration_validation，且本规则所列字段（source independence, condition match, forward calculations, shared-error audit）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：Combined data are informative only when source independence, condition matching, forward calculations and held-out validation are explicit; shared errors can make a joint fit overconfident. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 joint_likelihood_with_heldout_validation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 SHARED_ERROR_OR_CONDITION_MISMATCH，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C008-RULE-001 | Layer B | hoff_2024_emmivox_cryoem

- Original proposed rule: 在 G0>G1>G2 的重点检查中要求 map/half-map provenance, resolution, voxel correlation and preprocessing；若无法验证则走 MAP_PROVENANCE_OR_NOISE_UNKNOWN。
- Applies when: 当研究使用 source_quality，且本规则所列字段（map/half-map provenance, resolution, voxel correlation and preprocessing）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：cryo-EM voxel evidence requires correlation-aware sampling, half-map/noise provenance and a voxel-to-density forward model before model fit is interpreted. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 correlation_aware_map_evidence 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 MAP_PROVENANCE_OR_NOISE_UNKNOWN，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C008-RULE-002 | Layer C | hoff_2024_emmivox_cryoem

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 map noise, B-factor, alignment/radiation-damage alternatives and heterogeneity；若无法验证则走 NOISE_DYNAMICS_CONFUSION。
- Applies when: 当研究使用 artifact_exclusion，且本规则所列字段（map noise, B-factor, alignment/radiation-damage alternatives and heterogeneity）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：Fuzzy cryo-EM density must be separated into conformational heterogeneity versus experimental noise/B-factor effects using negative controls and local uncertainty diagnostics. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 noise_heterogeneity_separation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 NOISE_DYNAMICS_CONFUSION，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C008-RULE-003 | Layer C | hoff_2024_emmivox_cryoem

- Original proposed rule: 在 G2>G3>G4 的重点检查中要求 density forward model, metainference ensemble and sampling/preprocessing provenance；若无法验证则走 FORWARD_OR_SAMPLING_UNRESOLVED。
- Applies when: 当研究使用 forward_bridge，且本规则所列字段（density forward model, metainference ensemble and sampling/preprocessing provenance）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：A cryo-EM metainference ensemble is map- and prior-consistent under the stated conditions; it may represent local dynamics around a macrostate rather than the full room-temperature landscape. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 ensemble_metainference 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 FORWARD_OR_SAMPLING_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C009-RULE-001 | Layer B | peter_2022_deer_smfret_crossvalidation

- Original proposed rule: 在 G1>G2>G4>G5 的重点检查中要求 same label sites, physical state, probe chemistry, averaging and negative controls；若无法验证则走 CROSS_MODAL_CONDITION_MISMATCH。
- Applies when: 当研究使用 cross_validation，且本规则所列字段（same label sites, physical state, probe chemistry, averaging and negative controls）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：DEER and smFRET inter-probe measurements must retain probe chemistry, physical sample state, averaging law and condition because nominal distance is not the same observable. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 direct_cross_validation_matrix 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 CROSS_MODAL_CONDITION_MISMATCH，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C009-RULE-002 | Layer B | peter_2022_deer_smfret_crossvalidation

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 cryoprotectant, dye swap, anisotropy/lifetime/BVA and condition controls；若无法验证则走 PROBE_OR_CONDITION_CAUSE_UNRESOLVED。
- Applies when: 当研究使用 diagnostic_controls，且本规则所列字段（cryoprotectant, dye swap, anisotropy/lifetime/BVA and condition controls）会影响比较、解释或准入时；当前证据单元归入 Layer B。
- Scientific reason: 来源记录要求处理这一类问题：Probe–protein interactions and cryoprotectants can explain method discrepancies; anisotropy, lifetime, BVA and no-cryoprotectant controls are part of the interpretation evidence. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 qualitative_diagnostic_matrix 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 PROBE_OR_CONDITION_CAUSE_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C009-RULE-003 | Layer A | peter_2022_deer_smfret_crossvalidation

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 DEER frozen distribution versus liquid-phase FRET average and condition；若无法验证则走 ESTIMAND_OR_STATE_MISMATCH。
- Applies when: 当研究使用 estimand_non_equivalence，且本规则所列字段（DEER frozen distribution versus liquid-phase FRET average and condition）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：Overall agreement across the tested datasets supports complementary use of DEER and smFRET under stated protocols, not cross-system generalization or population equivalence. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 conditional_cross_validation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 ESTIMAND_OR_STATE_MISMATCH，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C010-RULE-001 | Layer A | sanabria_2020_transient_states

- Original proposed rule: 在 G1>G4>G5 的重点检查中要求 claim level, pair coverage, time scale, orthogonal evidence and function link；若无法验证则走 CLAIM_LEVEL_UNSUPPORTED。
- Applies when: 当研究使用 claim_ladder，且本规则所列字段（claim level, pair coverage, time scale, orthogonal evidence and function link）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：A transient-state claim is strongest when multiple label pairs, timescales, global models and orthogonal probes jointly support the same latent state. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 claim_conditioned_evidence_ladder 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 CLAIM_LEVEL_UNSUPPORTED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C010-RULE-002 | Layer A | sanabria_2020_transient_states

- Original proposed rule: 在 G1>G2>G5 的重点检查中要求 state model, pair coverage, time window and global/shared fractions；若无法验证则走 STATE_MODEL_UNIDENTIFIABLE。
- Applies when: 当研究使用 state_semantics，且本规则所列字段（state model, pair coverage, time window and global/shared fractions）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：Global shared-fraction analysis and explicit linker/orientation uncertainty improve identifiability but remain model- and condition-dependent spectroscopic inference. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 state_model_comparison 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 STATE_MODEL_UNIDENTIFIABLE，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C010-RULE-003 | Layer D | sanabria_2020_transient_states

- Original proposed rule: 在 G4>G5 的重点检查中要求 perturbation, independent function assay, alternative mechanism and mapping uncertainty；若无法验证则走 FUNCTIONAL_LINK_UNSUPPORTED。
- Applies when: 当研究使用 functional_validation，且本规则所列字段（perturbation, independent function assay, alternative mechanism and mapping uncertainty）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：FRET-to-structure screening can validate known-state compatibility and expose an unknown-state residual, but it does not determine the unknown state's coordinates without additional evidence. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 orthogonal_functional_validation 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 FUNCTIONAL_LINK_UNSUPPORTED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C011-RULE-001 | Layer C | steffen_2021_fretraj

- Original proposed rule: 在 G1>G3>G4 的重点检查中要求 ACV, dye/linker, trajectory frames, time cut-off and photon statistics；若无法验证则走 FORWARD_IMPLEMENTATION_INCOMPLETE。
- Applies when: 当研究使用 forward_implementation，且本规则所列字段（ACV, dye/linker, trajectory frames, time cut-off and photon statistics）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：ACV-based trajectory-to-FRET prediction is a probe forward model that must retain dye/linker, trajectory and photon-statistics metadata. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 trajectory_to_measurement_forward_model 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 FORWARD_IMPLEMENTATION_INCOMPLETE，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C011-RULE-002 | Layer C | steffen_2021_fretraj

- Original proposed rule: 在 G1>G2>G3>G5 的重点检查中要求 conformational-sampling component, photon shot-noise model, timescale/window, package/version, input trajectory and implementation receipt；若无法验证则走 NOISE_CONFORMATION_OR_IMPLEMENTATION_UNRESOLVED。
- Applies when: 当研究使用 uncertainty_decomposition，且本规则所列字段（conformational-sampling component, photon shot-noise model, timescale/window, package/version, input trajectory and implementation receipt）会影响比较、解释或准入时；当前证据单元归入 Layer C。
- Scientific reason: 来源记录要求处理这一类问题：Predicted FRET-distribution width combines conformational sampling and shot noise; these components must be separated before inferring protein dynamics. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 noise_and_conformation_decomposition 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 NOISE_CONFORMATION_OR_IMPLEMENTATION_UNRESOLVED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C011-RULE-003 | Layer D | steffen_2021_fretraj

- Original proposed rule: 在 G3>G4>G5 的重点检查中要求 measurement-space residual and alternative explanations for agreement；若无法验证则走 AGREEMENT_OVERINTERPRETED。
- Applies when: 当研究使用 claim_ceiling，且本规则所列字段（measurement-space residual and alternative explanations for agreement）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：A software demonstration on a DNA hairpin establishes a reproducible implementation path, not protein-specific biological accuracy or cross-system generalization. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 measurement_space_consistency 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 AGREEMENT_OVERINTERPRETED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C012-RULE-001 | Layer A | wankowicz_bonomi_2026_ensemble_prediction

- Original proposed rule: 在 G0>G1>G2>G3>G4>G5 的重点检查中要求 condition, claim, modality-specific observable, forward model, uncertainty and intended use；若无法验证则走 BENCHMARK_SCOPE_UNDEFINED。
- Applies when: 当研究使用 benchmark_contract，且本规则所列字段（condition, claim, modality-specific observable, forward model, uncertainty and intended use）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：The basic comparison unit for ensemble work is condition plus claim plus modality-specific observable/forward model/uncertainty, not a universal structural metric. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 claim_conditioned_benchmark 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 BENCHMARK_SCOPE_UNDEFINED，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C012-RULE-002 | Layer A | wankowicz_bonomi_2026_ensemble_prediction

- Original proposed rule: 在 G1>G2>G3>G4>G5 的重点检查中要求 forward likelihood, posterior hypotheses, shared-error audit, prior sensitivity, missing-state support and next discriminating action；若无法验证则走 NON_IDENTIFIABILITY_OR_MISSING_SUPPORT。
- Applies when: 当研究使用 identifiability，且本规则所列字段（forward likelihood, posterior hypotheses, shared-error audit, prior sensitivity, missing-state support and next discriminating action）会影响比较、解释或准入时；当前证据单元归入 Layer A。
- Scientific reason: 来源记录要求处理这一类问题：Multimodal fit cannot by itself identify a unique ensemble because shared errors, prior dominance, missing states and non-identifiability can remain. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 hypothesis_set_with_discriminating_action 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 NON_IDENTIFIABILITY_OR_MISSING_SUPPORT，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

### C012-RULE-003 | Layer D | wankowicz_bonomi_2026_ensemble_prediction

- Original proposed rule: 在 G0>G1>G4>G5 的重点检查中要求 ground truth, representation, comparison, uncertainty and intended-use status；若无法验证则走 GROUND_TRUTH_OR_VALIDATION_MISSING。
- Applies when: 当研究使用 claim_ceiling，且本规则所列字段（ground truth, representation, comparison, uncertainty and intended-use status）会影响比较、解释或准入时；当前证据单元归入 Layer D。
- Scientific reason: 来源记录要求处理这一类问题：Benchmark outputs should include evidence lineage, allowed/forbidden claims, uncertainty, held-out validation and the next discriminating action rather than only a submitted ensemble. 这些量或条件决定估计对象、误差来源与跨方法可比性。
- Operation: 在计算前保留所需字段并记录来源定位，按 abstain_or_next_action 接入；对阈值、校准、缺失值或模型假设逐项留下可回放记录。
- Claim boundary: 仅可在字段已核对且验证路径可回放时使用项目规则；证据不足时转入 GROUND_TRUTH_OR_VALIDATION_MISSING，不得把该规则升级为更强的因果、机制、平衡、速率或泛化结论。

## Project additions

### P-RULE-001

- Applies when: When an HSP90 NOE result compares native violation with open/closed reference conditions.
- Scientific reason: Signed native violation and the absolute pseudodistance-fit quantity are different observables; using one as the other changes the meaning of agreement.
- Operation: Read native violation from the second data column for the preregistered threshold crosswalk at tau=0.5, 1, and 2 Å; retain the third column only as an explicit diagnostic.
- Claim boundary: Supports same-source reference decomposition and threshold sensitivity only; it is not independent experimental validation and does not support kinetic claims.
- Source: `PREREGISTERED_RULES.md; C009-RULE-001/C009-RULE-002`

### P-RULE-002

- Applies when: When a geometric distance or excursion is calculated from periodic molecular-dynamics coordinates.
- Scientific reason: Minimum-image and whole-molecule distances answer different geometric questions; an unnoticed periodic-boundary shortcut can create a false displacement or transition.
- Operation: Use the production alignment and explicit atom/residue masks, record whether coordinates are already unwrapped/aligned, and reject a shortcut when the selected geometry requires whole-molecule continuity.
- Claim boundary: Supports a defined geometric descriptor and its continuity check; it does not establish a transition mechanism, rate, or new physical state.
- Source: `hsp90_v1_protocol.json; run_hsp90_v1.py lines 1110-1145; ADK FIELD_DEFINITIONS.md`

### P-RULE-003

- Applies when: When a final numerical statement is produced from the current session's operator output.
- Scientific reason: A number without the operator, parameter set, input snapshot, and result identity cannot be replayed or distinguished from an exploratory draft.
- Operation: Require the current operator result_id on every submitted numerical claim; allow exploratory qualitative notes without result_id only when they are labeled exploratory and excluded from final numeric evidence.
- Claim boundary: A bound numerical claim can be traced to this session's result object; binding alone does not prove scientific correctness, independence, or agreement with an external measurement.
- Source: `CODEX_EXECUTION_ORDER_OPERATOR_PLAN_20260911_ZH.md Step 6 and Step 8`

