# 学習目的・最適化・正則化 — 13/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/natural_context_contrast_paired_semantic_clusters.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_paired_semantic_clusters.json) ／ SHA256: `a99480a471ffb781bafd2242ec3c06871abc37669ee28e8142c5d392dfbb4f2a` ／ 10,305 bytes

| 原キー | 保存値 |
|---|---|
| references.CE.checkpoint_sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| references.CE.DEV_selection.dev_bytes_sha256 | "bc676ad2b955a238b60cc3a2cfccbe4b5e7b793640212980f72716ed3a6a14a2" |
| references.contrast.checkpoint_sha256 | "b3c88153624b9d9c1e9114314c7c19f7feeaf5e4c51650b3e78f0dd40c407707" |
| references.contrast.DEV_selection.dev_bytes_sha256 | "bc676ad2b955a238b60cc3a2cfccbe4b5e7b793640212980f72716ed3a6a14a2" |
| summaries.CE.exact_content_pair_clusters | 96 |
| summaries.CE.original_nominal_accuracy.point | 0.625 |
| summaries.CE.original_nominal_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| summaries.CE.original_nominal_accuracy.units | 96 |
| summaries.CE.original_nominal_accuracy.examples | 192 |
| summaries.CE.original_nominal_accuracy.unit | "family/prompt" |
| summaries.CE.original_nominal_accuracy.seed | 42 |
| summaries.CE.original_nominal_accuracy.repetitions | 2000 |
| summaries.CE.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.content_cluster_accuracy.point | 0.625 |
| summaries.CE.content_cluster_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| summaries.CE.content_cluster_accuracy.units | 96 |
| summaries.CE.content_cluster_accuracy.examples | 192 |
| summaries.CE.content_cluster_accuracy.unit | "family/prompt" |
| summaries.CE.content_cluster_accuracy.seed | 42 |
| summaries.CE.content_cluster_accuracy.repetitions | 2000 |
| summaries.CE.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.both_contexts_hard_correct.point | 0.2708333333333333 |
| summaries.CE.both_contexts_hard_correct.ci95 | [0.1875, 0.3645833333333333] |
| summaries.CE.both_contexts_hard_correct.units | 96 |
| summaries.CE.both_contexts_hard_correct.examples | 96 |
| summaries.CE.both_contexts_hard_correct.unit | "family/prompt" |
| summaries.CE.both_contexts_hard_correct.seed | 42 |
| summaries.CE.both_contexts_hard_correct.repetitions | 2000 |
| summaries.CE.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.causality.seed | 42 |
| summaries.CE.categories.causality.repetitions | 2000 |
| summaries.CE.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.comparison.seed | 42 |
| summaries.CE.categories.comparison.repetitions | 2000 |
| summaries.CE.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.coreference.seed | 42 |
| summaries.CE.categories.coreference.repetitions | 2000 |
| summaries.CE.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.negation.seed | 42 |
| summaries.CE.categories.negation.repetitions | 2000 |
| summaries.CE.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.quantity.seed | 42 |
| summaries.CE.categories.quantity.repetitions | 2000 |
| summaries.CE.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.CE.categories.time.seed | 42 |
| summaries.CE.categories.time.repetitions | 2000 |
| summaries.CE.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.exact_content_pair_clusters | 96 |
| summaries.contrast.original_nominal_accuracy.point | 0.6354166666666666 |
| summaries.contrast.original_nominal_accuracy.ci95 | [0.5833333333333334, 0.6875] |
| summaries.contrast.original_nominal_accuracy.units | 96 |
| summaries.contrast.original_nominal_accuracy.examples | 192 |
| summaries.contrast.original_nominal_accuracy.unit | "family/prompt" |
| summaries.contrast.original_nominal_accuracy.seed | 42 |
| summaries.contrast.original_nominal_accuracy.repetitions | 2000 |
| summaries.contrast.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.content_cluster_accuracy.point | 0.6354166666666666 |
| summaries.contrast.content_cluster_accuracy.ci95 | [0.5833333333333334, 0.6875] |
| summaries.contrast.content_cluster_accuracy.units | 96 |
| summaries.contrast.content_cluster_accuracy.examples | 192 |
| summaries.contrast.content_cluster_accuracy.unit | "family/prompt" |
| summaries.contrast.content_cluster_accuracy.seed | 42 |
| summaries.contrast.content_cluster_accuracy.repetitions | 2000 |
| summaries.contrast.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.both_contexts_hard_correct.point | 0.3125 |
| summaries.contrast.both_contexts_hard_correct.ci95 | [0.21875, 0.40625] |
| summaries.contrast.both_contexts_hard_correct.units | 96 |
| summaries.contrast.both_contexts_hard_correct.examples | 96 |
| summaries.contrast.both_contexts_hard_correct.unit | "family/prompt" |
| summaries.contrast.both_contexts_hard_correct.seed | 42 |
| summaries.contrast.both_contexts_hard_correct.repetitions | 2000 |
| summaries.contrast.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.causality.seed | 42 |
| summaries.contrast.categories.causality.repetitions | 2000 |
| summaries.contrast.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.comparison.seed | 42 |
| summaries.contrast.categories.comparison.repetitions | 2000 |
| summaries.contrast.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.coreference.seed | 42 |
| summaries.contrast.categories.coreference.repetitions | 2000 |
| summaries.contrast.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.negation.seed | 42 |
| summaries.contrast.categories.negation.repetitions | 2000 |
| summaries.contrast.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.quantity.seed | 42 |
| summaries.contrast.categories.quantity.repetitions | 2000 |
| summaries.contrast.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.contrast.categories.time.seed | 42 |
| summaries.contrast.categories.time.repetitions | 2000 |
| summaries.contrast.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired.candidate_minus_control.point | 0.010416666666666666 |
| paired.candidate_minus_control.ci95 | [-0.020833333333333332, 0.041666666666666664] |
| paired.candidate_minus_control.units | 96 |
| paired.candidate_minus_control.examples | 192 |
| paired.candidate_minus_control.unit | "family/prompt" |
| paired.candidate_minus_control.seed | 42 |
| paired.candidate_minus_control.repetitions | 2000 |
| paired.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired.exact_content_pair_clusters | 96 |
| paired.cases | 192 |
| paired.new_acceptance_gate | false |
| scientific_config_sha256 | "70b87bf762f3225fd83f40d3bde301c13e5a4b4243372e541af1a1e38e88bc29" |
| new_GPU_seconds | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| limitations | "All original case weights retained; exact aliases are clustered, not counted as independent cases. Other template correlations remain. CIs describe this constructed DEV packet, not natural Japanese population accuracy. No protected TEST source file is opened by this supplement." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_probe_completion.json — complete_fixed64_native_CUDA_probe_science_not_started</summary>

[原記録](../../reports/phase6/natural_context_contrast_probe_completion.json) ／ SHA256: `f799a6b6d5dd660abf88aff319a0dcd242f0ac484e08177a6009d90e4cbe82c0` ／ 3,793 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_fixed64_native_CUDA_probe_science_not_started" |
| GPU_occupancy_seconds | 12.507994213985512 |
| CPU_tests.seconds | 1.9 |
| CPU_tests.passed | 5 |
| CPU_tests.initial_fixture_failure | "Small fixture head_dim8 retained rotary_dim64; fixed rotary_dim and matching attention scale before freezing. Native model implementation/acceptance criteria unchanged." |
| actual_CUDA_full_state_checks | 26 |
| verification_optimizer_updates | 64 |
| verification_CE_teacher_tokens | 367840 |
| verification_auxiliary_input_tokens | 185328 |
| verification_physical_inputs | 1850816 |
| GPU_maximum_capacity_claimed | false |
| fixed_probe_pair_limit | 64 |
| original_UI.training_tokens | 10000007168 |
| original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| scientific_teacher_tokens | 0 |
| protected_dev_test_used | false |
| Base_complete | false |
| limitations | "Finite gradients, stable fixed64 batches and exact resume do not prove generative quality or whole-corpus throughput. Probe units are old accepted TRAIN, not new supply; auxiliary distractors are not logically false labels. Full Base gates unchanged." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_probe_index.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_probe_index.json) ／ SHA256: `e77c0ae2c6fe91d352461c90de8b4044f8f4645695dedb22e44f2393287d7d66` ／ 36,192 bytes

| 原キー | 保存値 |
|---|---|
| sample_sha256 | "c83d521a979fb5970649bf3249113637dcbfac5b10850ca0b3a7f407af825c35" |
| seed | 2026100743 |
| limitations | "Hash/offset/length index only; full original texts and token IDs retained on native TRAIN disk. Not new corpus supply or content acceptance." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_probe_job.json — complete</summary>

[原記録](../../reports/phase6/natural_context_contrast_probe_job.json) ／ SHA256: `7a12a9866f221cec8f70525f491b4852e3fdfed5b5eaeb5e8546f74ab84d939e` ／ 786 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| GPU_occupancy_seconds | 12.507994213985512 |
| completed_updates | 8 |
| verification_optimizer_updates | 64 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_probe_result.json — complete</summary>

[原記録](../../reports/phase6/natural_context_contrast_probe_result.json) ／ SHA256: `ee11994007587473c09c0a66dd42e202e6c7b490c9b91310d20ee4e748bbd906` ／ 114,711 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| passed | true |
| fixed_sample_capacity_limit | 64 |
| actual_GPU_maximum_claimed | false |
| timings.full_CE-batch16.median_CE_targets_per_second | 39235.25063476498 |
| timings.full_CE-batch16.median_physical_inputs_per_second | 101860.40864032219 |
| timings.full_CE-batch16.peak_VRAM_bytes | 2068601344 |
| timings.CE_plus_native_contrast-batch16.median_CE_targets_per_second | 27767.73325666305 |
| timings.CE_plus_native_contrast-batch16.median_physical_inputs_per_second | 131896.257671024 |
| timings.CE_plus_native_contrast-batch16.peak_VRAM_bytes | 2110217216 |
| timings.full_CE-batch32.median_CE_targets_per_second | 91007.88148784773 |
| timings.full_CE-batch32.median_physical_inputs_per_second | 225848.13038616904 |
| timings.full_CE-batch32.peak_VRAM_bytes | 3926143488 |
| timings.CE_plus_native_contrast-batch32.median_CE_targets_per_second | 46455.3899153097 |
| timings.CE_plus_native_contrast-batch32.median_physical_inputs_per_second | 249771.23775497105 |
| timings.CE_plus_native_contrast-batch32.peak_VRAM_bytes | 3956429824 |
| timings.full_CE-batch64.median_CE_targets_per_second | 98844.61291217098 |
| timings.full_CE-batch64.median_physical_inputs_per_second | 343544.1474612488 |
| timings.full_CE-batch64.peak_VRAM_bytes | 7639445504 |
| timings.CE_plus_native_contrast-batch64.median_CE_targets_per_second | 52853.89004621561 |
| timings.CE_plus_native_contrast-batch64.median_physical_inputs_per_second | 377108.71213835746 |
| timings.CE_plus_native_contrast-batch64.peak_VRAM_bytes | 7651578880 |
| gates.full_CE.passed | true |
| gates.full_CE.checks.kind | true |
| gates.full_CE.checks.spec | true |
| gates.full_CE.checks.binding | true |
| gates.full_CE.checks.lineage | true |
| gates.full_CE.checks.model_config | true |
| gates.full_CE.checks.model | true |
| gates.full_CE.checks.optimizer | true |
| gates.full_CE.checks.scheduler | true |
| gates.full_CE.checks.RNG | true |
| gates.full_CE.checks.sampler | true |
| gates.full_CE.checks.counters | true |
| gates.full_CE.checks.finite | true |
| gates.full_CE.checks.all_history_except_timing | true |
| gates.full_CE.checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/full_CE/resume-gate/continuous.pt" |
| gates.full_CE.checkpoints.continuous.sha256 | "edd893db6360a498f77a66685a64d23474a5c100cfc80624bd09661a8f5b3662" |
| gates.full_CE.checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/full_CE/resume-gate/resumed.pt" |
| gates.full_CE.checkpoints.resumed.sha256 | "cf89ba454c77be60e06baf0b1913d53be5259bb2265cd9eb2f108d724d4d7d95" |
| gates.CE_plus_native_contrast.passed | true |
| gates.CE_plus_native_contrast.checks.kind | true |
| gates.CE_plus_native_contrast.checks.spec | true |
| gates.CE_plus_native_contrast.checks.binding | true |
| gates.CE_plus_native_contrast.checks.lineage | true |
| gates.CE_plus_native_contrast.checks.model_config | true |
| gates.CE_plus_native_contrast.checks.model | true |
| gates.CE_plus_native_contrast.checks.optimizer | true |
| gates.CE_plus_native_contrast.checks.scheduler | true |
| gates.CE_plus_native_contrast.checks.RNG | true |
| gates.CE_plus_native_contrast.checks.sampler | true |
| gates.CE_plus_native_contrast.checks.counters | true |
| gates.CE_plus_native_contrast.checks.finite | true |
| gates.CE_plus_native_contrast.checks.all_history_except_timing | true |
| gates.CE_plus_native_contrast.checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/CE_plus_native_contrast/resume-gate/continuous.pt" |
| gates.CE_plus_native_contrast.checkpoints.continuous.sha256 | "80f7306d1ab81194e2d1a3e311e56e1a847fd3e167b55c0837fb65e34d0f356c" |
| gates.CE_plus_native_contrast.checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/CE_plus_native_contrast/resume-gate/resumed.pt" |
| gates.CE_plus_native_contrast.checkpoints.resumed.sha256 | "239637a824be486af29a5fd5dcddaf16e1771b6febc2ab6b7c8bb27a804a8000" |
| verification_optimizer_updates | 64 |
| verification_CE_teacher_tokens | 367840 |
| verification_auxiliary_input_tokens | 185328 |
| verification_physical_inputs | 1850816 |
| GPU_occupancy_seconds | 12.507994213985512 |
| GPU_limit_seconds | 180 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| limitations | "Finite gradients, stable fixed64 batches and exact resume do not prove generative quality or whole-corpus throughput. Probe units are old accepted TRAIN, not new supply; auxiliary distractors are not logically false labels. Full Base gates unchanged." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_comparison_completion.json — fixed_projection100M_complete_rejected_Base_incomplete</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_comparison_completion.json) ／ SHA256: `3166f10c64ef3d2851ed634861c519fb09e319a8855881a60cad6f7aa4090985` ／ 15,720 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_projection100M_complete_rejected_Base_incomplete" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-projection-comparison-20261007/projection/checkpoint-00017698.pt" |
| checkpoint.sha256 | "cf20fbbc809ec6b63a2223879ebccfa7e6693714f4114bb5cdddddd545e04476" |
| GPU_occupancy_seconds | 2382.8204671700078 |
| GPU_budget_seconds | 5009 |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teacher_tokens | 200000000 |
| reused_control_GPU_seconds | 0 |
| accounting.completed_updates | 17698 |
| accounting.head_optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 86885793 |
| accounting.auxiliary_pairs | 676384 |
| accounting.physical_input_tokens | 683893095 |
| accounting.original_body_bytes | 405882136 |
| history.committed_updates | 17698 |
| history.head_updates | 17698 |
| history.observed_completed_attempt_updates | 17698 |
| summaries.projection.BPB | 1.0007222231116217 |
| summaries.projection.rates.eos | 21 |
| summaries.projection.rates.repetition | 47 |
| summaries.projection.rates.unicode_failure | 0 |
| summaries.projection.rates.role_leak | 0 |
| summaries.projection.rates.empty | 0 |
| summaries.projection.grammar2 | 57 |
| summaries.projection.relevance2 | 25 |
| summaries.projection.coherent | 4 |
| summaries.projection.appropriate | 3 |
| summaries.projection.notes_sha256 | "f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1" |
| summaries.CE.BPB | 0.998487162513845 |
| summaries.CE.rates.eos | 19 |
| summaries.CE.rates.repetition | 45 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 44 |
| summaries.CE.relevance2 | 25 |
| summaries.CE.coherent | 2 |
| summaries.CE.appropriate | 2 |
| summaries.CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| summaries.strong_staged.BPB | 1.1336128657420816 |
| summaries.strong_staged.rates.eos | 76 |
| summaries.strong_staged.rates.repetition | 2 |
| summaries.strong_staged.rates.unicode_failure | 0 |
| summaries.strong_staged.rates.role_leak | 0 |
| summaries.strong_staged.rates.empty | 0 |
| summaries.strong_staged.grammar2 | 65 |
| summaries.strong_staged.relevance2 | 39 |
| summaries.strong_staged.coherent | 23 |
| summaries.strong_staged.appropriate | 26 |
| summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| strong_and_matched_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.CE.checks.EOS_nonworsening | true |
| strong_and_matched_quality.CE.checks.repetition_nonworsening | false |
| strong_and_matched_quality.CE.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.CE.checks.BPB_gate | true |
| strong_and_matched_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.CE.passed | false |
| strong_and_matched_quality.contrast.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.contrast.checks.paired_CI_lower_above0 | true |
| strong_and_matched_quality.contrast.checks.EOS_nonworsening | true |
| strong_and_matched_quality.contrast.checks.repetition_nonworsening | true |
| strong_and_matched_quality.contrast.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.contrast.checks.BPB_gate | true |
| strong_and_matched_quality.contrast.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.contrast.passed | false |
| strong_and_matched_quality.strong_staged.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.strong_staged.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.strong_staged.checks.EOS_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.repetition_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.strong_staged.checks.BPB_gate | true |
| strong_and_matched_quality.strong_staged.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.0022350605977766573 |
| paired_common_byte_BPB.CE.ci95 | [0.0019195271648210727, 0.002551265532697412] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0022384470043157 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "projection minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| paired_common_byte_BPB.contrast.point | -0.002167795177503928 |
| paired_common_byte_BPB.contrast.ci95 | [-0.002634424532899614, -0.0017505857420847695] |
| paired_common_byte_BPB.contrast.documents | 256 |
| paired_common_byte_BPB.contrast.common_bytes | 472055 |
| paired_common_byte_BPB.contrast.control_BPB | 1.0028900182891256 |
| paired_common_byte_BPB.contrast.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.contrast.relative_ratio | 0.9978384517365104 |
| paired_common_byte_BPB.contrast.degradation_ci_lower_above0 | false |
| paired_common_byte_BPB.contrast.seed | 42 |
| paired_common_byte_BPB.contrast.repetitions | 2000 |
| paired_common_byte_BPB.contrast.direction | "projection minus completed contrast; positive means worse" |
| paired_common_byte_BPB.contrast.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.projection.exact_content_pair_clusters | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.point | 0.625 |
| exact_content_semantics.projection.original_nominal_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.original_nominal_accuracy.units | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.projection.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.projection.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.content_cluster_accuracy.point | 0.625 |
| exact_content_semantics.projection.content_cluster_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.content_cluster_accuracy.units | 96 |
| exact_content_semantics.projection.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.projection.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.projection.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.both_contexts_hard_correct.point | 0.2916666666666667 |
| exact_content_semantics.projection.both_contexts_hard_correct.ci95 | [0.20833333333333334, 0.3854166666666667] |
| exact_content_semantics.projection.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.projection.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.projection.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.projection.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.causality.seed | 42 |
| exact_content_semantics.projection.categories.causality.repetitions | 2000 |
| exact_content_semantics.projection.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.comparison.seed | 42 |
| exact_content_semantics.projection.categories.comparison.repetitions | 2000 |
| exact_content_semantics.projection.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.coreference.seed | 42 |
| exact_content_semantics.projection.categories.coreference.repetitions | 2000 |
| exact_content_semantics.projection.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.negation.seed | 42 |
| exact_content_semantics.projection.categories.negation.repetitions | 2000 |
| exact_content_semantics.projection.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.quantity.seed | 42 |
| exact_content_semantics.projection.categories.quantity.repetitions | 2000 |
| exact_content_semantics.projection.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.time.seed | 42 |
| exact_content_semantics.projection.categories.time.repetitions | 2000 |
| exact_content_semantics.projection.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | 0.0 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.020833333333333332, 0.020833333333333332] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
| exact_content_semantics.paired.contrast.candidate_minus_control.point | -0.010416666666666666 |
| exact_content_semantics.paired.contrast.candidate_minus_control.ci95 | [-0.041666666666666664, 0.026041666666666668] |
| exact_content_semantics.paired.contrast.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.contrast.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.contrast.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.contrast.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.contrast.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.contrast.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.contrast.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.contrast.cases | 192 |
| exact_content_semantics.paired.contrast.new_acceptance_gate | false |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.full_sampler | true |
| common_CE_checks.contrast.update | true |
| common_CE_checks.contrast.token_digest | true |
| common_CE_checks.contrast.supervised_tokens | true |
| common_CE_checks.contrast.source_teachers | true |
| common_CE_checks.contrast.source_EOS | true |
| common_CE_checks.contrast.CE_input_tokens | true |
| common_CE_checks.contrast.original_body_bytes | true |
| common_CE_checks.contrast.full_sampler | true |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| fixed_recipe_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 106225836 |
| archive.compressed_bundle.bytes | 52105787 |
| archive.compressed_bundle.lossless | true |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_comparison_review.json — new80_and_reused160_projection_comparison_reviewed</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_comparison_review.json) ／ SHA256: `19f42a3fb9f678740f02f9c713d5487196ba949c21abaea96e25e668743172e0` ／ 14,055 bytes

| 原キー | 保存値 |
|---|---|
| status | "new80_and_reused160_projection_comparison_reviewed" |
| summaries.projection.BPB | 1.0007222231116217 |
| summaries.projection.rates.eos | 21 |
| summaries.projection.rates.repetition | 47 |
| summaries.projection.rates.unicode_failure | 0 |
| summaries.projection.rates.role_leak | 0 |
| summaries.projection.rates.empty | 0 |
| summaries.projection.grammar2 | 57 |
| summaries.projection.relevance2 | 25 |
| summaries.projection.coherent | 4 |
| summaries.projection.appropriate | 3 |
| summaries.projection.notes_sha256 | "f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1" |
| summaries.CE.BPB | 0.998487162513845 |
| summaries.CE.rates.eos | 19 |
| summaries.CE.rates.repetition | 45 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 44 |
| summaries.CE.relevance2 | 25 |
| summaries.CE.coherent | 2 |
| summaries.CE.appropriate | 2 |
| summaries.CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| summaries.strong_staged.BPB | 1.1336128657420816 |
| summaries.strong_staged.rates.eos | 76 |
| summaries.strong_staged.rates.repetition | 2 |
| summaries.strong_staged.rates.unicode_failure | 0 |
| summaries.strong_staged.rates.role_leak | 0 |
| summaries.strong_staged.rates.empty | 0 |
| summaries.strong_staged.grammar2 | 65 |
| summaries.strong_staged.relevance2 | 39 |
| summaries.strong_staged.coherent | 23 |
| summaries.strong_staged.appropriate | 26 |
| summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| strong_and_matched_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.CE.checks.EOS_nonworsening | true |
| strong_and_matched_quality.CE.checks.repetition_nonworsening | false |
| strong_and_matched_quality.CE.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.CE.checks.BPB_gate | true |
| strong_and_matched_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.CE.passed | false |
| strong_and_matched_quality.contrast.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.contrast.checks.paired_CI_lower_above0 | true |
| strong_and_matched_quality.contrast.checks.EOS_nonworsening | true |
| strong_and_matched_quality.contrast.checks.repetition_nonworsening | true |
| strong_and_matched_quality.contrast.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.contrast.checks.BPB_gate | true |
| strong_and_matched_quality.contrast.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.contrast.passed | false |
| strong_and_matched_quality.strong_staged.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.strong_staged.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.strong_staged.checks.EOS_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.repetition_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.strong_staged.checks.BPB_gate | true |
| strong_and_matched_quality.strong_staged.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.0022350605977766573 |
| paired_common_byte_BPB.CE.ci95 | [0.0019195271648210727, 0.002551265532697412] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0022384470043157 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "projection minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| paired_common_byte_BPB.contrast.point | -0.002167795177503928 |
| paired_common_byte_BPB.contrast.ci95 | [-0.002634424532899614, -0.0017505857420847695] |
| paired_common_byte_BPB.contrast.documents | 256 |
| paired_common_byte_BPB.contrast.common_bytes | 472055 |
| paired_common_byte_BPB.contrast.control_BPB | 1.0028900182891256 |
| paired_common_byte_BPB.contrast.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.contrast.relative_ratio | 0.9978384517365104 |
| paired_common_byte_BPB.contrast.degradation_ci_lower_above0 | false |
| paired_common_byte_BPB.contrast.seed | 42 |
| paired_common_byte_BPB.contrast.repetitions | 2000 |
| paired_common_byte_BPB.contrast.direction | "projection minus completed contrast; positive means worse" |
| paired_common_byte_BPB.contrast.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.projection.exact_content_pair_clusters | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.point | 0.625 |
| exact_content_semantics.projection.original_nominal_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.original_nominal_accuracy.units | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.projection.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.projection.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.content_cluster_accuracy.point | 0.625 |
| exact_content_semantics.projection.content_cluster_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.content_cluster_accuracy.units | 96 |
| exact_content_semantics.projection.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.projection.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.projection.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.both_contexts_hard_correct.point | 0.2916666666666667 |
| exact_content_semantics.projection.both_contexts_hard_correct.ci95 | [0.20833333333333334, 0.3854166666666667] |
| exact_content_semantics.projection.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.projection.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.projection.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.projection.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.causality.seed | 42 |
| exact_content_semantics.projection.categories.causality.repetitions | 2000 |
| exact_content_semantics.projection.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.comparison.seed | 42 |
| exact_content_semantics.projection.categories.comparison.repetitions | 2000 |
| exact_content_semantics.projection.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.coreference.seed | 42 |
| exact_content_semantics.projection.categories.coreference.repetitions | 2000 |
| exact_content_semantics.projection.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.negation.seed | 42 |
| exact_content_semantics.projection.categories.negation.repetitions | 2000 |
| exact_content_semantics.projection.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.quantity.seed | 42 |
| exact_content_semantics.projection.categories.quantity.repetitions | 2000 |
| exact_content_semantics.projection.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.time.seed | 42 |
| exact_content_semantics.projection.categories.time.repetitions | 2000 |
| exact_content_semantics.projection.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | 0.0 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.020833333333333332, 0.020833333333333332] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
| exact_content_semantics.paired.contrast.candidate_minus_control.point | -0.010416666666666666 |
| exact_content_semantics.paired.contrast.candidate_minus_control.ci95 | [-0.041666666666666664, 0.026041666666666668] |
| exact_content_semantics.paired.contrast.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.contrast.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.contrast.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.contrast.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.contrast.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.contrast.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.contrast.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.contrast.cases | 192 |
| exact_content_semantics.paired.contrast.new_acceptance_gate | false |
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 17698 |
| accounting.head_optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 86885793 |
| accounting.auxiliary_pairs | 676384 |
| accounting.physical_input_tokens | 683893095 |
| accounting.original_body_bytes | 405882136 |
| history.committed_updates | 17698 |
| history.head_updates | 17698 |
| history.observed_completed_attempt_updates | 17698 |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.full_sampler | true |
| common_CE_checks.contrast.update | true |
| common_CE_checks.contrast.token_digest | true |
| common_CE_checks.contrast.supervised_tokens | true |
| common_CE_checks.contrast.source_teachers | true |
| common_CE_checks.contrast.source_EOS | true |
| common_CE_checks.contrast.CE_input_tokens | true |
| common_CE_checks.contrast.original_body_bytes | true |
| common_CE_checks.contrast.full_sampler | true |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 200000000 |
| reused_control_GPU_seconds | 0 |
| probe_verification_updates | 33 |
| probe_verification_CE_teachers | 145531 |
| GPU_occupancy_seconds | 2382.8204671700078 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "Single learned seed, repeated nonblind DEV, head parameters/auxiliary compute differ. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_comparison_start.json — actual_durable_projection_science_started</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_comparison_start.json) ／ SHA256: `927658bc49a6ae1151ac34718f928ed62a4964437cb5a84dad42c0e16cbec830` ／ 2,511 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_durable_projection_science_started" |
| job.status | "running" |
| job.GPU_occupancy_seconds | 25.334230191016104 |
| job.Base_complete | false |
| job.resident_memory_policy.visible_device_bytes | 25756696576 |
| job.resident_memory_policy.allocator_allowance_bytes | 23181026918 |
| job.resident_memory_policy.expected_worst_peak_bytes | 19265087488 |
| job.scientific_CE_teacher_tokens | 906290 |
| job.local_update | 160 |
| job.loss | 2.8322615146636965 |
| last_completed_update.update | 169 |
| last_completed_update.supervised_tokens | 956300 |
| last_completed_update.CE_loss | 2.6594126224517822 |
| last_completed_update.contrast_loss | 0.9407499432563782 |
| last_completed_update.combined_loss | 2.75348761677742 |
| last_completed_update.auxiliary_gradient_norm | 0.6211603283882141 |
| last_completed_update.train_only_head_gradient_norm | 0.4301033616065979 |
| last_completed_update.source_teachers.web | 717105 |
| last_completed_update.source_teachers.textbook | 191385 |
| last_completed_update.source_teachers.story | 47810 |
| checkpoint_paths | [] |
| scientific_token_goal | 100000000 |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_content_review.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_content_review.json) ／ SHA256: `143bdf03f069da57a64fc4039339327d364e7512bbed50394701a9f343ef9cf3` ／ 721 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.0007222231116217 |
| rates.eos | 21 |
| rates.repetition | 47 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 57 |
| relevance2 | 25 |
| coherent | 4 |
| appropriate | 3 |
| notes_sha256 | "f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1" |
| scope | "new80_content_only_final_comparison_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_notes.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_notes.json) ／ SHA256: `f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1` ／ 22,266 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_probe_completion.json — actual_projection_probe_passed_scientific_command_ready</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_probe_completion.json) ／ SHA256: `2f6b2effd6a05538686ccf7cc06ac58a601057148e42d8f4b633bb8d39bed950` ／ 4,402 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_projection_probe_passed_scientific_command_ready" |
| CPU_protocol_tests | 7 |
| CPU_run_tests | 2 |
| CPU_protocol_seconds | 4.12 |
| CPU_run_seconds | 0.79 |
| GPU_seconds | 11.138348664011573 |
| GPU_limit_seconds | 180 |
| initial_checks.native_weights | true |
| initial_checks.original_parent_weights | true |
| initial_checks.native_RNG | true |
| initial_checks.native_parameters | true |
| initial_checks.head_parameters | true |
| initial_checks.native_tied | true |
| initial_checks.separate_head_state | true |
| initial_checks.native_logits | true |
| resume_checks.kind | true |
| resume_checks.spec | true |
| resume_checks.binding | true |
| resume_checks.lineage | true |
| resume_checks.model_config | true |
| resume_checks.model | true |
| resume_checks.optimizer | true |
| resume_checks.scheduler | true |
| resume_checks.RNG | true |
| resume_checks.sampler | true |
| resume_checks.counters | true |
| resume_checks.projector | true |
| resume_checks.finite | true |
| resume_checks.all_history_except_timing | true |
| verification_updates | 33 |
| verification_CE_teacher_tokens | 145531 |
| fixed_TRAIN64_auxiliary_backward_optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| fastest_measured_batch | 48 |
| maximum_context_peak_bytes | 19265087488 |
| allocator_policy.visible_device_bytes | 25756696576 |
| allocator_policy.allocator_allowance_bytes | 23181026918 |
| allocator_policy.expected_worst_peak_bytes | 0 |
| archive.bytes | 1069184 |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| preflight_repairs | "Initial CPU assertions incorrectly referenced the embedding parent and required auxiliary gradients on pair-ineligible windows; corrected fixtures, original labels unchanged. Before GPU, isolated head seeding to CPU default_generator so CUDA RNG is preserved; native initial public path uses math attention for its explicit mask, training uses flash causal. Both superseded preparation configurations/source and the original fixture failure are retained. Actual CUDA probe ran once." |
| scientific_configuration.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/natural_context_contrast_projection_comparison.json" |
| scientific_configuration.sha256 | "ff61ab14485ef239dc5c59b2ef2750dd2ce0e74f80c753c3cd33034e6283d1db" |
| scientific_configuration.forecast_seconds | 2939.264688013192 |
| scientific_configuration.GPU_limit_seconds | 5009 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Short source timing is a forecast, not measured whole100M duration. Allocator resident guard does not prove maximum utilization. Initialization/finite/resume evidence is not generation quality. No additional unique data or scientific teachers were created by the probe." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_projection_proposal.json — training_only_projection_mechanism_proposed_not_implemented</summary>

[原記録](../../reports/phase6/natural_context_contrast_projection_proposal.json) ／ SHA256: `8568100442361fcf10999d47c426a99106c5f7e0d2a6d5dd2516696dd095db24` ／ 4,847 bytes

| 原キー | 保存値 |
|---|---|
| new_GPU_seconds | 0 |
| head.head_seed | 2026100751 |
| prototype.GPU_seconds_limit | 180 |
| prototype.CPU_seconds_limit | 30 |
| new_teacher_tokens | 0 |
| status | "training_only_projection_mechanism_proposed_not_implemented" |
| unchanged_failed_branches | "Preserve both closed100M recipes and all nine likelihood views. Do not retune raw InfoNCE, start8K tokenizer retraining, or automatically launch a larger/untied native model. Earlier8K100M common-byte BPB and generation failures remain negative local evidence, not a global impossibility proof." |
| Base_adopted | false |
| Base_complete | false |
| adoption | "Same strong/matched/absolute/historical Web gates and all80 raw-bound content. A projected candidate must qualify against CE, previous direct-feature contrast, and original full Base criteria; retrieval/retention alone does not qualify. Independent learned seed/full DEV/protected final TEST/adoption remain required. If failed, close this fixed mechanism; no head-width/activation/seed/LR/coefficient/source/epoch rescue." |
| protected_test_used | false |
| measured_reason | "DEV64 native embedding retrieval7.813 to18.750 percent but same matched suffix BPB0.995055 to1.000546, paired difference0.005491/CI[0.003823,0.007581]. Context-benefit change0.000606/CI[-0.000569,0.001761]. These paired same-CE results suggest representation discrimination and autoregressive accuracy differ; they do not prove causally that direct feature constraints alone caused the failed natural generation." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_proposal.json — new_mechanism_proposed_probe_inputs_prepared_objective_not_yet_implemented</summary>

[原記録](../../reports/phase6/natural_context_contrast_proposal.json) ／ SHA256: `6066431729db9b1a96cfd0556b1c16a026c258bc0db6220d33d0a46c18541422` ／ 5,454 bytes

| 原キー | 保存値 |
|---|---|
| status | "new_mechanism_proposed_probe_inputs_prepared_objective_not_yet_implemented" |
| scope | "Native 10M Base only; notify and stop at evidence-qualified Base; no Chat/SFT/quantization" |
| parent_checkpoint | "reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| accepted_TRAIN_pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| fixed_probe_sample_sha256 | "c83d521a979fb5970649bf3249113637dcbfac5b10850ca0b3a7f407af825c35" |
| fixed_probe_pairs | 64 |
| objective.loss_coefficient | 0.1 |
| objective.total_loss | "full_unit_CE + 0.1 * symmetric_InfoNCE" |
| objective.negative_interpretation | "Other in-batch suffixes are corpus-retrieval distractors, not certified false factual outcomes. Duplicate families/bodies within a contrast batch must be excluded." |
| bounded_next_probe.GPU_seconds_maximum | 180 |
| conditional_scientific_comparison.status | "not_frozen_not_started" |
| conditional_scientific_comparison.proposed_arms | ["matched full-unit CE", "same CE plus native context/suffix InfoNCE"] |
| conditional_scientific_comparison.proposed_CE_target_tokens_per_arm | 100000000 |
| conditional_scientific_comparison.must_freeze_before_launch | "Actual record windowing/sampler/source eligibility and common byte exposures, measured batch/optimizer/LR/scheduler/seed, all CE and extra auxiliary exposures, save/resume evidence, finite GPU budget derived from probe, and fixed evaluation/completion conditions. No scientific job until this exists." |
| conditional_scientific_comparison.accounting | "Same CE target is not equal total compute: report auxiliary forward tokens, pair count, valid/physical inputs, optimizer updates and GPU seconds separately; preserve original source identity and accepted mixture." |
| conditional_scientific_comparison.acceptance | "All existing relative/absolute/Base EOS/repetition/Unicode/role/historical Web BPB criteria remain unchanged. Full80 raw content and fixed Japanese DEV comparisons; independent learning seed/full DEV/protected final TEST/adoption still required before Base completion." |
| conditional_scientific_comparison.on_failure | "Close this fixed mechanism comparison without source/temperature/coefficient/LR/checkpoint/epoch rescue or automatic training extension." |
| limitations | "Contrastive context representation papers motivate an experiment; they do not prove Japanese native10M generative improvement. Probe64 is reused accepted TRAIN, not fresh supply or 64 newly reviewed content samples. This is not teacher transfer, corpus semantic labeling, logically false negative verification or Base adoption." |
| new_scientific_training_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_training_endpoints.json — bounded_saved_training_metrics_described</summary>

[原記録](../../reports/phase6/natural_context_contrast_training_endpoints.json) ／ SHA256: `cac12570258d602e784a8e6c78031ac0750560d2a1c73e1774658dbfe15798a5` ／ 23,938 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_saved_training_metrics_described" |
| source_bytes | 101227090 |
| bounded_bytes_read | 524288 |
| means.initial20.CE_loss | 2.742115008831024 |
| means.initial20.contrast_loss | 1.6210994184017182 |
| means.initial20.combined_loss | 2.904224950671196 |
| means.initial20.eligible_pairs_this_update | 37.5 |
| means.initial20.auxiliary_pairs_this_update | 37.5 |
| means.initial20.original_windows_this_update | 48 |
| means.terminal20_excluding_last.CE_loss | 2.5798150420188906 |
| means.terminal20_excluding_last.contrast_loss | 0.3759314835071564 |
| means.terminal20_excluding_last.combined_loss | 2.617408190369606 |
| means.terminal20_excluding_last.eligible_pairs_this_update | 37.75 |
| means.terminal20_excluding_last.auxiliary_pairs_this_update | 37.75 |
| means.terminal20_excluding_last.original_windows_this_update | 48 |
| interpretation | "Different sampled TRAIN batches and changing pair counts: descriptive endpoints, not same-input validation or proof of generalization. Nonzero representation variance is not proof that all features avoid collapse. Do not infer semantic correctness from document retrieval discrimination." |
| new_GPU_seconds | 0 |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| CPU_seconds | 0.004026818991405889 |

</details>

<details>
<summary>reports/phase6/nonorm_cache_precision_trace.json — diagnosis_complete</summary>

[原記録](../../reports/phase6/nonorm_cache_precision_trace.json) ／ SHA256: `ea45329eb65e41f351a51d7145ad7e751f3c1c6d56a7df2303bcfd436a9651dd` ／ 46,205 bytes

| 原キー | 保存値 |
|---|---|
| status | "diagnosis_complete" |
| checkpoint_binding.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt" |
| checkpoint_binding.checkpoint_sha256 | "e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07" |
| checkpoint_binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checkpoint_binding.implementation.src/jmicro/model.py | "2861baaf1860174fc8f7ae5da23386ae39146b8a907077bce4958a4b6b315b3a" |
| checkpoint_binding.implementation.src/jmicro/shards.py | "9544c5a0c385f817f93510eaae6375e8c044286822fd86e333d2f07123b63e4c" |
| checkpoint_binding.implementation.src/jmicro/training.py | "d898b9ba7d15d7e24c497c5981f3fc090894833d08f202d44ef881d0bb6f5086" |
| checkpoint_binding.implementation.uv.lock | "29821397f48485dfa3317319da5248cb260c3963b6db4aad18276ed3ab9ce298" |
| checkpoint_binding.verifier_sha256 | "0dc999752f1aaa1f5df9940c7b339481d68ba676adb807957ed1b89d6eb91aa2" |
| checkpoint_binding.protocol_sha256 | "49e0273d4ae315288c9969a11493bf52d9ba8aa21d51f7ac1c35757f5b3b4ec9" |
| checkpoint_binding.runtime_receipt_sha256 | "903d14b081e753519fae3b084029499c59cb8c76f741d73e9414814ed9dd16d7" |
| scope | "One fixed FP32 CPU full1024 versus cache511+1+512, all module outputs; no environment sweep or training" |

</details>

<details>
<summary>reports/phase6/nonorm_cpu_precision_report.json — complete</summary>

[原記録](../../reports/phase6/nonorm_cpu_precision_report.json) ／ SHA256: `82de4a292d79ccd874ef391ce0cce0630f1118db8c258007a33d7df5e2cbc06a` ／ 73,659 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.completion | "Evaluate all 8 fixed CPU configurations using all 12 original comparisons and both actual stop fixtures; no tolerance/input/model changes, no follow-up sweep" |

</details>

<details>
<summary>reports/phase6/nonorm_precision_repair_report.json — passed_real_cpu_inference_profile</summary>

[原記録](../../reports/phase6/nonorm_precision_repair_report.json) ／ SHA256: `b95aad196408639d718042be7ec460a36f603889dbb2d716d422cad75567a952` ／ 2,144 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_real_cpu_inference_profile" |
| repair_candidates | 2 |
| first_repair | "independent default RoPE frequencies" |
| second_repair | "FP64 accumulation with FP32 storage/activation/cache/logits; accurate default RoPE trig" |
| short_and_context1024_comparisons_passed | 12 |
| formal_contract_checks_passed | 13 |
| real_CLI_and_weight_audit_checks_passed | 149 |
| evidence./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readiness-20261003/precision-repair-v1/result.json | "73894f1c8c6574869e0829fd1b8ff8180a1a8803cb5fd150e3907eaf9ab00004" |
| evidence./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readiness-20261003/precision-repair-v1-fixed-loader/result.json | "82f8b10e42dc17e8b3ec6403db78b4480e2c03015da9807b7f3fbcebda581bbd" |
| evidence./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readiness-20261003/precision-repair-v1-fixed-loader/trig_rounding.json | "0abbc6f462cb6d62bfd265e7e0632a4e959c0b33087684e1d37fd68e835655d2" |
| evidence./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readiness-20261003/precision-repair-v2/result.json | "3ca54d46771c260f9512a80f524c8fb47be96e7e774d8893ed0a8c0ba6191fa6" |
| retained_stock_failures | ["reports/phase6/nonorm_export_stock_fp32_failure.json", "reports/phase6/nonorm_export_initial_failure.json", "reports/phase6/nonorm_export_precision_failure.json", "reports/phase6/nonorm_cpu_precision_report.json", "reports/phase6/nonorm_cuda_reference_report.json"] |
| precision_profile_scope | "actual CPU inference; stock CPU/CUDA FP32 failure retained; CUDA/BF16 training path unchanged" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v2-20261006/probe/job.json — failed_or_interrupted</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v2-20261006/probe/job.json) ／ SHA256: `5351f82fd97fd249ba110021f72eb67aeca6e0d1f5f92565f7cef5a0491003d9` ／ 674 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed_or_interrupted" |
| GPU_elapsed_seconds | 1.8781388830102514 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v2-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v2-probe-launcher-20261006/launcher.json) ／ SHA256: `998aa694b23d8051d2d4db0719975d12df95cc3502027dedf1e0c7c524c7dfa0` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v2-probe-launcher-20261006/result.json — failed</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v2-probe-launcher-20261006/result.json) ／ SHA256: `3f15aaecf6465ec9880a8e8665451d1adce32acd4e2e2f0c6b47243c46ae1a07` ／ 176 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/compare-result.json — two100M_GPU_complete_pending_all160_content_review</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/compare-result.json) ／ SHA256: `4f71f1842a6cd85b3f34696a8052ee38f9c1aba9c94c5c67580fd85aa46a54d9` ／ 1,257,258 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.matched_staged_CE.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE/training/checkpoint-00326571.pt" |
| checkpoints.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| checkpoints.matched_staged_CE.binding.config_sha256 | "7fb897e9905eceaecc754a4d323f2e8d90c68e47e592872c8f20cf980721e249" |
| checkpoints.matched_staged_CE.binding.arm | "matched_staged_CE" |
| checkpoints.matched_staged_CE.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.matched_staged_CE.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.matched_staged_CE.binding.teacher_goals.web | 75000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.story | 5000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.binding.study_kind | "mixed_fullstate_matched_staged_parameter_displacement_v1" |
| checkpoints.matched_staged_CE.binding.parameter_coefficient | 0.0 |
| checkpoints.matched_staged_CE.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.matched_staged_CE.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.matched_staged_CE.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.matched_staged_CE.binding.optimizer_policy | "inherit" |
| checkpoints.matched_staged_CE.binding.peak_lr | 1e-05 |
| checkpoints.matched_staged_CE.update | 326571 |
| checkpoints.matched_staged_CE.tokens | 10701078528 |
| checkpoints.matched_staged_CE.supervised_tokens | 10677786961 |
| checkpoints.matched_staged_CE.additional_supervised_tokens | 100000000 |
| checkpoints.matched_staged_CE.additional_input_tokens | 100532224 |
| checkpoints.matched_staged_CE.source_teachers.web | 75000000 |
| checkpoints.matched_staged_CE.source_teachers.story | 5000000 |
| checkpoints.matched_staged_CE.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.source_teachers.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.source_eos.web | 159447 |
| checkpoints.matched_staged_CE.source_eos.story | 38240 |
| checkpoints.matched_staged_CE.source_eos.ordinary_textbook | 74183 |
| checkpoints.matched_staged_CE.source_eos.conditional_textbook | 234328 |
| checkpoints.matched_staged_CE.source_input_tokens.web | 75183104 |
| checkpoints.matched_staged_CE.source_input_tokens.story | 5039104 |
| checkpoints.matched_staged_CE.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.matched_staged_CE.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.matched_staged_CE.source_focus_teachers.web | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.story | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.matched_staged_CE.focus_teacher_tokens | 1407427 |
| checkpoints.matched_staged_CE.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.matched_staged_CE.weighted_teacher_mass | 100000000 |
| checkpoints.matched_staged_CE.outcome_weight | 1 |
| checkpoints.matched_staged_CE.training_seconds | 183.06313274789136 |
| checkpoints.matched_staged_CE.completed_at | "2026-10-06T10:16:39.374828Z" |
| checkpoints.matched_staged_CE.parameter_coefficient | 0.0 |
| checkpoints.matched_staged_CE.parameter_penalty_teacher_tokens | 0 |
| checkpoints.matched_staged_CE.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.matched_staged_CE.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.matched_staged_CE.sampler.goals.web | 75000000 |
| checkpoints.matched_staged_CE.sampler.goals.story | 5000000 |
| checkpoints.matched_staged_CE.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.context | 1024 |
| checkpoints.matched_staged_CE.sampler.seed | 42 |
| checkpoints.matched_staged_CE.sampler.position | 3068 |
| checkpoints.matched_staged_CE.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.matched_staged_CE.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.context | 1024 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.matched_staged_CE.sampler.streams.story.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.story.genre | "story" |
| checkpoints.matched_staged_CE.sampler.streams.story.documents | 761448 |
| checkpoints.matched_staged_CE.sampler.streams.story.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.story.document_position | 38243 |
| checkpoints.matched_staged_CE.sampler.streams.story.token_offset | 87 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.matched_staged_CE.sampler.source_teachers.web | 75000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.story | 5000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.source_eos.web | 159447 |
| checkpoints.matched_staged_CE.sampler.source_eos.story | 38240 |
| checkpoints.matched_staged_CE.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.matched_staged_CE.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.matched_staged_CE.sampler.source_tokens.web | 75183104 |
| checkpoints.matched_staged_CE.sampler.source_tokens.story | 5039104 |
| checkpoints.matched_staged_CE.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.matched_staged_CE.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.web | 292167653 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.story | 20452979 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.web | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.story | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.matched_staged_CE.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.matched_staged_CE.source_body_bytes.web | 292167653 |
| checkpoints.matched_staged_CE.source_body_bytes.story | 20452979 |
| checkpoints.matched_staged_CE.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.matched_staged_CE.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.matched_staged_CE.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| checkpoints.parameter_anchor.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor/training/checkpoint-00326571.pt" |
| checkpoints.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| checkpoints.parameter_anchor.binding.config_sha256 | "7fb897e9905eceaecc754a4d323f2e8d90c68e47e592872c8f20cf980721e249" |
| checkpoints.parameter_anchor.binding.arm | "parameter_anchor" |
| checkpoints.parameter_anchor.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.parameter_anchor.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.parameter_anchor.binding.teacher_goals.web | 75000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.story | 5000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.binding.study_kind | "mixed_fullstate_matched_staged_parameter_displacement_v1" |
| checkpoints.parameter_anchor.binding.parameter_coefficient | 0.04161064039180984 |
| checkpoints.parameter_anchor.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.parameter_anchor.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.parameter_anchor.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.parameter_anchor.binding.optimizer_policy | "inherit" |
| checkpoints.parameter_anchor.binding.peak_lr | 1e-05 |
| checkpoints.parameter_anchor.update | 326571 |
| checkpoints.parameter_anchor.tokens | 10701078528 |
| checkpoints.parameter_anchor.supervised_tokens | 10677786961 |
| checkpoints.parameter_anchor.additional_supervised_tokens | 100000000 |
| checkpoints.parameter_anchor.additional_input_tokens | 100532224 |
| checkpoints.parameter_anchor.source_teachers.web | 75000000 |
| checkpoints.parameter_anchor.source_teachers.story | 5000000 |
| checkpoints.parameter_anchor.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.source_teachers.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.source_eos.web | 159447 |
| checkpoints.parameter_anchor.source_eos.story | 38240 |
| checkpoints.parameter_anchor.source_eos.ordinary_textbook | 74183 |
| checkpoints.parameter_anchor.source_eos.conditional_textbook | 234328 |
| checkpoints.parameter_anchor.source_input_tokens.web | 75183104 |
| checkpoints.parameter_anchor.source_input_tokens.story | 5039104 |
| checkpoints.parameter_anchor.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.parameter_anchor.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.parameter_anchor.source_focus_teachers.web | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.story | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.parameter_anchor.focus_teacher_tokens | 1407427 |
| checkpoints.parameter_anchor.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.parameter_anchor.weighted_teacher_mass | 100000000 |
| checkpoints.parameter_anchor.outcome_weight | 1 |
| checkpoints.parameter_anchor.training_seconds | 172.07054460450308 |
| checkpoints.parameter_anchor.completed_at | "2026-10-06T10:20:34.571311Z" |
| checkpoints.parameter_anchor.parameter_coefficient | 0.04161064039180984 |
| checkpoints.parameter_anchor.parameter_penalty_teacher_tokens | 0 |
| checkpoints.parameter_anchor.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.parameter_anchor.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.parameter_anchor.sampler.goals.web | 75000000 |
| checkpoints.parameter_anchor.sampler.goals.story | 5000000 |
| checkpoints.parameter_anchor.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.context | 1024 |
| checkpoints.parameter_anchor.sampler.seed | 42 |
| checkpoints.parameter_anchor.sampler.position | 3068 |
| checkpoints.parameter_anchor.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.parameter_anchor.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.context | 1024 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.parameter_anchor.sampler.streams.story.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.story.genre | "story" |
| checkpoints.parameter_anchor.sampler.streams.story.documents | 761448 |
| checkpoints.parameter_anchor.sampler.streams.story.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.story.document_position | 38243 |
| checkpoints.parameter_anchor.sampler.streams.story.token_offset | 87 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.parameter_anchor.sampler.source_teachers.web | 75000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.story | 5000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.source_eos.web | 159447 |
| checkpoints.parameter_anchor.sampler.source_eos.story | 38240 |
| checkpoints.parameter_anchor.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.parameter_anchor.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.parameter_anchor.sampler.source_tokens.web | 75183104 |
| checkpoints.parameter_anchor.sampler.source_tokens.story | 5039104 |
| checkpoints.parameter_anchor.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.parameter_anchor.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.web | 292167653 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.story | 20452979 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.web | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.story | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.parameter_anchor.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.parameter_anchor.source_body_bytes.web | 292167653 |
| checkpoints.parameter_anchor.source_body_bytes.story | 20452979 |
| checkpoints.parameter_anchor.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.parameter_anchor.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.parameter_anchor.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| evaluations.matched_staged_CE.binding.teacher_goals.web | 75000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.story | 5000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| evaluations.matched_staged_CE.body.documents | 256 |
| evaluations.matched_staged_CE.body.limit_documents | 256 |
| evaluations.matched_staged_CE.body.body_nll | 338873.8658795357 |
| evaluations.matched_staged_CE.body.eos_nll | 526.858716275543 |
| evaluations.matched_staged_CE.body.body_bytes | 472055 |
| evaluations.matched_staged_CE.body.body_tokens | 122343 |
| evaluations.matched_staged_CE.body.bpb | 1.0356667036495277 |
| evaluations.matched_staged_CE.body.seconds | 1.3664823299914133 |
| evaluations.matched_staged_CE.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.matched_staged_CE.generation.max_new_tokens | 64 |
| evaluations.matched_staged_CE.greedy_rates.eos | 69 |
| evaluations.matched_staged_CE.greedy_rates.repetition | 6 |
| evaluations.matched_staged_CE.greedy_rates.unicode_failure | 0 |
| evaluations.matched_staged_CE.greedy_rates.role_leak | 0 |
| evaluations.matched_staged_CE.greedy_rates.empty | 0 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.ci95 | [0.5, 0.5833333333333334] |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4739583333333333, 0.5260416666666666] |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.macro_f1 | 0.49978289188015634 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.point | 0.7613293051359517 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.ci95 | [0.716012084592145, 0.8066465256797583] |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.hard_accuracy | 0.7613293051359517 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.matched_staged_CE.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.ci95 | [0.27164879356568367, 0.3235254691689007] |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2806076854334227 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.25466934763181415, 0.30654602323503116] |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2806076854334227 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2797558541778977 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.mcc | 0.1012522601643278 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.matched_staged_CE.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.semantic_both_contexts.correct | 13 |
| evaluations.matched_staged_CE.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.matched_staged_CE.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.matched_staged_CE.protected_test_used | false |
| evaluations.parameter_anchor.binding.teacher_goals.web | 75000000 |
| evaluations.parameter_anchor.binding.teacher_goals.story | 5000000 |
| evaluations.parameter_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.parameter_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| evaluations.parameter_anchor.body.documents | 256 |
| evaluations.parameter_anchor.body.limit_documents | 256 |
| evaluations.parameter_anchor.body.body_nll | 324149.8256213665 |
| evaluations.parameter_anchor.body.eos_nll | 555.5783282071352 |
| evaluations.parameter_anchor.body.body_bytes | 472055 |
| evaluations.parameter_anchor.body.body_tokens | 122343 |
| evaluations.parameter_anchor.body.bpb | 0.9906670746607233 |
| evaluations.parameter_anchor.body.seconds | 1.286099833989283 |
| evaluations.parameter_anchor.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.parameter_anchor.generation.max_new_tokens | 64 |
| evaluations.parameter_anchor.greedy_rates.eos | 67 |
| evaluations.parameter_anchor.greedy_rates.repetition | 6 |
| evaluations.parameter_anchor.greedy_rates.unicode_failure | 0 |
| evaluations.parameter_anchor.greedy_rates.role_leak | 0 |
| evaluations.parameter_anchor.greedy_rates.empty | 0 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.ci95 | [0.47903645833333336, 0.578125] |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.point | 0.4895833333333333 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.453125, 0.5208333333333334] |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.4895833333333333 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.macro_f1 | 0.4890843923101988 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.mcc | -0.020874143036171647 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.point | 0.7552870090634441 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.ci95 | [0.7098942598187311, 0.8006042296072508] |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.hard_accuracy | 0.7552870090634441 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7764350453172205] |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.parameter_anchor.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.jblimp.raw_pair_accuracy | 0.7643504531722054 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.point | 0.32171581769436997 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.ci95 | [0.2949061662198391, 0.3485254691689008] |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2940125111706881 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.32171581769436997] |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2940125111706881 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29296810549471497 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.mcc | 0.1178563840532624 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.parameter_anchor.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.parameter_anchor.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.parameter_anchor.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.parameter_anchor.protected_test_used | false |
| transfer.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| transfer.matched_staged_CE.checks.weights_unchanged | true |
| transfer.matched_staged_CE.checks.no_gradients | true |
| transfer.matched_staged_CE.checks.eval_mode | true |
| transfer.matched_staged_CE.checks.RNG_restored | true |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.75 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.both_correct | 74 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 49 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 25 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.74609375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 73 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 45 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.75390625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 75 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 43 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 31 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| transfer.matched_staged_CE.optimizer_updates | 0 |
| transfer.matched_staged_CE.scientific_teacher_tokens | 0 |
| transfer.matched_staged_CE.protected_test_used | false |
| transfer.matched_staged_CE.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| transfer.parameter_anchor.checks.weights_unchanged | true |
| transfer.parameter_anchor.checks.no_gradients | true |
| transfer.parameter_anchor.checks.eval_mode | true |
| transfer.parameter_anchor.checks.RNG_restored | true |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7421875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 70 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 47 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 69 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7421875 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 50 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.parameter_anchor.optimizer_updates | 0 |
| transfer.parameter_anchor.scientific_teacher_tokens | 0 |
| transfer.parameter_anchor.protected_test_used | false |
| transfer.parameter_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| retention.matched_staged_CE.checks.weights_unchanged | true |
| retention.matched_staged_CE.checks.no_gradients | true |
| retention.matched_staged_CE.checks.eval_mode | true |
| retention.matched_staged_CE.checks.RNG_restored | true |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.both_correct | 47 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7109375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 66 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 19 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69921875 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.matched_staged_CE.optimizer_updates | 0 |
| retention.matched_staged_CE.scientific_teacher_tokens | 0 |
| retention.matched_staged_CE.protected_test_used | false |
| retention.matched_staged_CE.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| retention.parameter_anchor.checks.weights_unchanged | true |
| retention.parameter_anchor.checks.no_gradients | true |
| retention.parameter_anchor.checks.eval_mode | true |
| retention.parameter_anchor.checks.RNG_restored | true |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 47 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 39 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 56 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 40 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.parameter_anchor.optimizer_updates | 0 |
| retention.parameter_anchor.scientific_teacher_tokens | 0 |
| retention.parameter_anchor.protected_test_used | false |
| retention.parameter_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| scientific_teacher_tokens | 200000000 |
| all_scientific_input_streams_match | true |
| status | "two100M_GPU_complete_pending_all160_content_review" |
| GPU_seconds | 481.3385134199925 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/body.json) ／ SHA256: `3f9b9c5846c3c5841560aad9f7c7542e5693b8fb7ca5b1748769479cc54b9ddb` ／ 67,235 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 338873.8658795357 |
| body.eos_nll | 526.858716275543 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0356667036495277 |
| body.seconds | 1.3664823299914133 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/generation.json) ／ SHA256: `c46048934bbc1b710ba198ec6a7eb868e21c5a9beb7a731601f29414ce8d8cc6` ／ 75,646 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/jblimp.json) ／ SHA256: `48bacf543b0f82ae9b0009759f99912ac5ad0b78692550a4deae910d589ef0de` ／ 338,438 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7613293051359517 |
| summary.primary.accuracy.ci95 | [0.716012084592145, 0.8066465256797583] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7613293051359517 |
| summary.per_token_secondary.accuracy.point | 0.7311178247734139 |
| summary.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| summary.per_token_secondary.macro_f1 | 0.4223385689354276 |
| summary.per_token_secondary.mcc | 0.0 |
| summary.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summary.unigram_control.accuracy.point | 0.40483383685800606 |
| summary.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summary.unigram_control.accuracy.units | 331 |
| summary.unigram_control.accuracy.examples | 331 |
| summary.unigram_control.accuracy.unit | "family/prompt" |
| summary.unigram_control.accuracy.seed | 42 |
| summary.unigram_control.accuracy.repetitions | 2000 |
| summary.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.unigram_control.hard_accuracy | 0.4773413897280967 |
| summary.train_majority_accuracy | null |
| summary.categories.island effects.seed | 42 |
| summary.categories.island effects.repetitions | 2000 |
| summary.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.binding.seed | 42 |
| summary.categories.binding.repetitions | 2000 |
| summary.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.argument structure.seed | 42 |
| summary.categories.argument structure.repetitions | 2000 |
| summary.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.ellipsis.seed | 42 |
| summary.categories.ellipsis.repetitions | 2000 |
| summary.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.verbal agreement.seed | 42 |
| summary.categories.verbal agreement.repetitions | 2000 |
| summary.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.filler-gap.seed | 42 |
| summary.categories.filler-gap.repetitions | 2000 |
| summary.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.morphology.seed | 42 |
| summary.categories.morphology.repetitions | 2000 |
| summary.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.nominal structure.seed | 42 |
| summary.categories.nominal structure.repetitions | 2000 |
| summary.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.quantifiers.seed | 42 |
| summary.categories.quantifiers.repetitions | 2000 |
| summary.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.NPI licensing.seed | 42 |
| summary.categories.NPI licensing.repetitions | 2000 |
| summary.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.control/raising.seed | 42 |
| summary.categories.control/raising.repetitions | 2000 |
| summary.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| control.note | "minimal pair preference; labels are not a classification prior" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/jcqa.json) ／ SHA256: `69355063250afdfe4a021f3b406bee266f3ab1385efb9a6ced82eda8decee718` ／ 1,642,244 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.2975871313672922 |
| summary.primary.accuracy.ci95 | [0.27164879356568367, 0.3235254691689007] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.2975871313672922 |
| summary.per_token_secondary.accuracy.point | 0.2806076854334227 |
| summary.per_token_secondary.accuracy.ci95 | [0.25466934763181415, 0.30654602323503116] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.2806076854334227 |
| summary.per_token_secondary.macro_f1 | 0.2797558541778977 |
| summary.per_token_secondary.mcc | 0.1012522601643278 |
| summary.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summary.unigram_control.accuracy.point | 0.17247542448614836 |
| summary.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summary.unigram_control.accuracy.units | 1119 |
| summary.unigram_control.accuracy.examples | 1119 |
| summary.unigram_control.accuracy.unit | "family/prompt" |
| summary.unigram_control.accuracy.seed | 42 |
| summary.unigram_control.accuracy.repetitions | 2000 |
| summary.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.unigram_control.hard_accuracy | 0.17247542448614836 |
| summary.train_majority_accuracy | 0.21179624664879357 |
| summary.categories.commonsense.seed | 42 |
| summary.categories.commonsense.repetitions | 2000 |
| summary.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/result.json) ／ SHA256: `97756b2d13586595ef0513c7467d79d3c6c557a4083a384a991da79335e394ce` ／ 168,457 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 338873.8658795357 |
| body.eos_nll | 526.858716275543 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0356667036495277 |
| body.seconds | 1.3664823299914133 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 69 |
| greedy_rates.repetition | 6 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5, 0.5833333333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4739583333333333, 0.5260416666666666] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.49978289188015634 |
| diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| diagnostics.semantics.unigram_control.accuracy.units | 96 |
| diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| diagnostics.semantics.train_majority_accuracy | 0.5 |
| diagnostics.semantics.categories.negation.seed | 42 |
| diagnostics.semantics.categories.negation.repetitions | 2000 |
| diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.categories.quantity.seed | 42 |
| diagnostics.semantics.categories.quantity.repetitions | 2000 |
| diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.categories.time.seed | 42 |
| diagnostics.semantics.categories.time.repetitions | 2000 |
| diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.categories.comparison.seed | 42 |
| diagnostics.semantics.categories.comparison.repetitions | 2000 |
| diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.categories.coreference.seed | 42 |
| diagnostics.semantics.categories.coreference.repetitions | 2000 |
| diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.categories.causality.seed | 42 |
| diagnostics.semantics.categories.causality.repetitions | 2000 |
| diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.jblimp.primary.accuracy.point | 0.7613293051359517 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.716012084592145, 0.8066465256797583] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7613293051359517 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| diagnostics.jblimp.train_majority_accuracy | null |
| diagnostics.jblimp.categories.island effects.seed | 42 |
| diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.binding.seed | 42 |
| diagnostics.jblimp.categories.binding.repetitions | 2000 |
| diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.argument structure.seed | 42 |
| diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.ellipsis.seed | 42 |
| diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.filler-gap.seed | 42 |
| diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.morphology.seed | 42 |
| diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.nominal structure.seed | 42 |
| diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.quantifiers.seed | 42 |
| diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.categories.control/raising.seed | 42 |
| diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.27164879356568367, 0.3235254691689007] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2806076854334227 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.25466934763181415, 0.30654602323503116] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2806076854334227 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2797558541778977 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.1012522601643278 |
| diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| diagnostics.jcqa.categories.commonsense.seed | 42 |
| diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.semantic_both_contexts.correct | 13 |
| memory.maximum_observed_allocated_bytes | 315223040 |
| memory.maximum_observed_reserved_bytes | 13325303808 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/matched_staged_CE/evaluation/semantics.json) ／ SHA256: `9c14aedc1172568edd39aeebd8013abb37d13c491ea046ace7cffaab36e1e87c` ／ 203,285 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5416666666666666 |
| summary.primary.accuracy.ci95 | [0.5, 0.5833333333333334] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5416666666666666 |
| summary.per_token_secondary.accuracy.point | 0.5 |
| summary.per_token_secondary.accuracy.ci95 | [0.4739583333333333, 0.5260416666666666] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5 |
| summary.per_token_secondary.macro_f1 | 0.49978289188015634 |
| summary.per_token_secondary.mcc | 0.0 |
| summary.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summary.unigram_control.accuracy.point | 0.5 |
| summary.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summary.unigram_control.accuracy.units | 96 |
| summary.unigram_control.accuracy.examples | 192 |
| summary.unigram_control.accuracy.unit | "family/prompt" |
| summary.unigram_control.accuracy.seed | 42 |
| summary.unigram_control.accuracy.repetitions | 2000 |
| summary.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.unigram_control.hard_accuracy | 0.5 |
| summary.train_majority_accuracy | 0.5 |
| summary.categories.negation.seed | 42 |
| summary.categories.negation.repetitions | 2000 |
| summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.quantity.seed | 42 |
| summary.categories.quantity.repetitions | 2000 |
| summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.time.seed | 42 |
| summary.categories.time.repetitions | 2000 |
| summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.comparison.seed | 42 |
| summary.categories.comparison.repetitions | 2000 |
| summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.coreference.seed | 42 |
| summary.categories.coreference.repetitions | 2000 |
| summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.causality.seed | 42 |
| summary.categories.causality.repetitions | 2000 |
| summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/body.json) ／ SHA256: `6d72fe71630181e1a519faaf1bb040c904e4059ba5b3bfea7b7d0b95b0fdef66` ／ 67,308 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 324149.8256213665 |
| body.eos_nll | 555.5783282071352 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9906670746607233 |
| body.seconds | 1.286099833989283 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/generation.json) ／ SHA256: `dd285bcad06ac9b1498203d461f14599a8c98c45cea67b5666efe3067847ec5f` ／ 80,647 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/jblimp.json) ／ SHA256: `4f6165457514448a124f7c61c5006679f6433225e576dc561bc2f3d0bb71042f` ／ 338,529 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7552870090634441 |
| summary.primary.accuracy.ci95 | [0.7098942598187311, 0.8006042296072508] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7552870090634441 |
| summary.per_token_secondary.accuracy.point | 0.7280966767371602 |
| summary.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7764350453172205] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| summary.per_token_secondary.macro_f1 | 0.42132867132867136 |
| summary.per_token_secondary.mcc | 0.0 |
| summary.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summary.unigram_control.accuracy.point | 0.40483383685800606 |
| summary.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summary.unigram_control.accuracy.units | 331 |
| summary.unigram_control.accuracy.examples | 331 |
| summary.unigram_control.accuracy.unit | "family/prompt" |
| summary.unigram_control.accuracy.seed | 42 |
| summary.unigram_control.accuracy.repetitions | 2000 |
| summary.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.unigram_control.hard_accuracy | 0.4773413897280967 |
| summary.train_majority_accuracy | null |
| summary.categories.island effects.seed | 42 |
| summary.categories.island effects.repetitions | 2000 |
| summary.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.binding.seed | 42 |
| summary.categories.binding.repetitions | 2000 |
| summary.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.argument structure.seed | 42 |
| summary.categories.argument structure.repetitions | 2000 |
| summary.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.ellipsis.seed | 42 |
| summary.categories.ellipsis.repetitions | 2000 |
| summary.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.verbal agreement.seed | 42 |
| summary.categories.verbal agreement.repetitions | 2000 |
| summary.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.filler-gap.seed | 42 |
| summary.categories.filler-gap.repetitions | 2000 |
| summary.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.morphology.seed | 42 |
| summary.categories.morphology.repetitions | 2000 |
| summary.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.nominal structure.seed | 42 |
| summary.categories.nominal structure.repetitions | 2000 |
| summary.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.quantifiers.seed | 42 |
| summary.categories.quantifiers.repetitions | 2000 |
| summary.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.NPI licensing.seed | 42 |
| summary.categories.NPI licensing.repetitions | 2000 |
| summary.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.control/raising.seed | 42 |
| summary.categories.control/raising.repetitions | 2000 |
| summary.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| control.note | "minimal pair preference; labels are not a classification prior" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/jcqa.json) ／ SHA256: `1d6a8101729d460ad80277a8bc1e3ce002b9cdc170707a82637369f2bbb81861` ／ 1,641,200 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.32171581769436997 |
| summary.primary.accuracy.ci95 | [0.2949061662198391, 0.3485254691689008] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.32171581769436997 |
| summary.per_token_secondary.accuracy.point | 0.2940125111706881 |
| summary.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.32171581769436997] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.2940125111706881 |
| summary.per_token_secondary.macro_f1 | 0.29296810549471497 |
| summary.per_token_secondary.mcc | 0.1178563840532624 |
| summary.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summary.unigram_control.accuracy.point | 0.17247542448614836 |
| summary.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summary.unigram_control.accuracy.units | 1119 |
| summary.unigram_control.accuracy.examples | 1119 |
| summary.unigram_control.accuracy.unit | "family/prompt" |
| summary.unigram_control.accuracy.seed | 42 |
| summary.unigram_control.accuracy.repetitions | 2000 |
| summary.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.unigram_control.hard_accuracy | 0.17247542448614836 |
| summary.train_majority_accuracy | 0.21179624664879357 |
| summary.categories.commonsense.seed | 42 |
| summary.categories.commonsense.repetitions | 2000 |
| summary.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |

</details>
