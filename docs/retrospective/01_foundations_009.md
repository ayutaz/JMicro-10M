# 基盤・Tokenizer・保存再開 — 9/11

[分野一覧へ](01_foundations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/base-preference-comparison-20261006/probe/common-resume/latest.json — None</summary>

[原記録](../../reports/phase6/base-preference-comparison-20261006/probe/common-resume/latest.json) ／ SHA256: `98ea2087721d77d24ce3d6a111f090598b357941cae39f45300f5338e83e31c2` ／ 273 bytes

| 原キー | 保存値 |
|---|---|
| update | 320439 |
| tokens_seen | 10500145152 |

</details>

<details>
<summary>reports/phase6/base-preference-comparison-20261006/probe/common-resume/result.json — None</summary>

[原記録](../../reports/phase6/base-preference-comparison-20261006/probe/common-resume/result.json) ／ SHA256: `96702f1aaf48a5e50a3f2d42e2b6a56b599375bc02836e582306b959bf6b3447` ／ 10,454 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_update | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_tokens_seen | true |
| checks.history_supervised_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_token_digest | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_valid_input_tokens | true |
| checks.history_physical_input_tokens | true |
| checks.history_additional_teacher_tokens | true |
| checks.finite | true |
| checks.fixed_inherited_LR | true |
| verification_teacher_tokens | 261602 |
| GPU_optimizer_updates | 8 |

</details>

<details>
<summary>reports/phase6/base-residual-capacity-control-first-gate-failure-20261008/resume-gate.json — None</summary>

[原記録](../../reports/phase6/base-residual-capacity-control-first-gate-failure-20261008/resume-gate.json) ／ SHA256: `f342bf6ca7274320fb627de349e07fe5fcb8efc082855a64ded1ecb76e2f09e6` ／ 44,974 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.model_config | true |
| checks.spec | true |
| checks.binding | true |
| checks.model | false |
| checks.optimizer | false |
| checks.scheduler | true |
| checks.RNG | true |
| checks.cursor | true |
| checks.counters | true |
| checks.history | false |
| checks.finite | true |
| passed | false |
| verification_updates | 8 |
| verification_teacher_tokens | 80992 |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/resume-gate.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/resume-gate.json) ／ SHA256: `45ba4e77ae8128444c6110136a8e900811325a88c04754a9477187e4793ca8c6` ／ 2,127 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.decay | true |
| checks.same_learned_parent_before_first_update | true |
| checks.full_committed_history | true |
| checks.resident_peak_under90percent | true |
| actual_CUDA_or_CPU_updates | 8 |
| verification_microbatches | 8 |
| initial_counters.update | 10000 |
| initial_counters.supervised_tokens | 94160195 |
| initial_counters.CE_input_tokens | 96655164 |
| initial_counters.auxiliary_input_tokens | 0 |
| initial_counters.auxiliary_pairs | 0 |
| initial_counters.physical_input_tokens | 404673920 |
| initial_counters.original_body_bytes | 382169159 |
| initial_counters.token_digest | "26b260437b751cb63b2e2922659bbac6b6e90adc983cd578626cdb0baf9a3dc4" |
| initial_counters.source_teachers.web | 70620030 |
| initial_counters.source_teachers.textbook | 18832118 |
| initial_counters.source_teachers.story | 4708047 |
| initial_counters.source_EOS.web | 619232 |
| initial_counters.source_EOS.textbook | 139904 |
| initial_counters.source_EOS.story | 35998 |
| final_verification_counters.update | 10004 |
| final_verification_counters.supervised_tokens | 94195927 |
| final_verification_counters.CE_input_tokens | 96691408 |
| final_verification_counters.auxiliary_input_tokens | 0 |
| final_verification_counters.auxiliary_pairs | 0 |
| final_verification_counters.physical_input_tokens | 404826320 |
| final_verification_counters.original_body_bytes | 382314679 |
| final_verification_counters.token_digest | "ef3c1320b1715fd58ecb0e98d4f42a17a9a5c1659683ffc42732ece126eda415" |
| final_verification_counters.source_teachers.web | 70646944 |
| final_verification_counters.source_teachers.textbook | 18839198 |
| final_verification_counters.source_teachers.story | 4709785 |
| final_verification_counters.source_EOS.web | 619477 |
| final_verification_counters.source_EOS.textbook | 139960 |
| final_verification_counters.source_EOS.story | 36016 |
| verification_teacher_tokens | 71464 |
| verification_weights_used_for_science | false |
| parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| peak_VRAM_bytes | 12443788800 |
| scope | "8 additional verification updates from exact learned parent; weights discarded" |

</details>

<details>
<summary>reports/phase6/base_5b_cuda_resume_gate.json — None</summary>

[原記録](../../reports/phase6/base_5b_cuda_resume_gate.json) ／ SHA256: `ed03f9470e5959054f6d6407acd4da66ccb0694096f4676c49fb2375fee5bd69` ／ 13,517 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.stable-extension:version | true |
| checks.stable-extension:spec | true |
| checks.stable-extension:model_config | true |
| checks.stable-extension:model | true |
| checks.stable-extension:optimizer | true |
| checks.stable-extension:scheduler | true |
| checks.stable-extension:rng | true |
| checks.stable-extension:sampler | true |
| checks.stable-extension:update | true |
| checks.stable-extension:tokens | true |
| checks.stable-extension:supervised_tokens | true |
| checks.stable-extension:body_bytes | true |
| checks.stable-extension:token_digest | true |
| checks.stable-extension:shard_manifest_sha256 | true |
| checks.stable-extension:implementation_sha256 | true |
| checks.stable-extension:lineage | true |
| checks.stable-extension:branch_updates | true |
| checks.stable-extension:branch_tokens | true |
| checks.stable-extension:finite | true |
| checks.stable-extension:history:loss | true |
| checks.stable-extension:history:lr | true |
| checks.stable-extension:history:token_digest | true |
| checks.stable-extension:history:tokens_seen | true |
| checks.stable:first_LR_no_jump | true |
| checks.stable:parent_cursor_advances_exactly64_blocks | true |
| checks.decay:version | true |
| checks.decay:spec | true |
| checks.decay:model_config | true |
| checks.decay:model | true |
| checks.decay:optimizer | true |
| checks.decay:scheduler | true |
| checks.decay:rng | true |
| checks.decay:sampler | true |
| checks.decay:update | true |
| checks.decay:tokens | true |
| checks.decay:supervised_tokens | true |
| checks.decay:body_bytes | true |
| checks.decay:token_digest | true |
| checks.decay:shard_manifest_sha256 | true |
| checks.decay:implementation_sha256 | true |
| checks.decay:lineage | true |
| checks.decay:branch_updates | true |
| checks.decay:branch_tokens | true |
| checks.decay:finite | true |
| checks.decay:history:loss | true |
| checks.decay:history:lr | true |
| checks.decay:history:token_digest | true |
| checks.decay:history:tokens_seen | true |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.parent.update | 57984 |
| binding.parent.tokens | 1900019712 |
| binding.parent.spec.seed | 42 |
| binding.parent.spec.schedule_updates | 61036 |
| binding.parent.token_digest | "af54d201d315cccbce31550c9da187ca758d98e798787360bbd7de5fdf968335" |
| optimizer_updates | 16 |
| input_tokens | 524288 |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/stable-extension/continuous/checkpoint.pt | "b037d06263297da4174a0a7eee6629cacf32dbcfe5f23f47fd1ac59dab723889" |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/stable-extension/paused/checkpoint.pt | "9941bfede68bc2fbf06fc8ef002f60a04bff596cf72ae74ec8f122f75a76e265" |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/stable-extension/resumed/checkpoint.pt | "b037d06263297da4174a0a7eee6629cacf32dbcfe5f23f47fd1ac59dab723889" |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/decay/continuous/checkpoint.pt | "73f8923b1619e409fd4df136c3e4da149e219ff3bc5569ddb18dbbb4ca9ff51a" |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/decay/paused/checkpoint.pt | "979c0c73e2da87e0c2e1f27a107cd3c58743ad8cc8cd6bf630abb30bdbcf3632" |
| checkpoint_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-5b-20261004/verification/decay/resumed/checkpoint.pt | "1445e02d5b6bf28a1eeea2831e4813c8dac2e6aebabe0e8925ad2efb187f057d" |

</details>

<details>
<summary>reports/phase6/base_gradient_accumulation_resume_gate.json — None</summary>

[原記録](../../reports/phase6/base_gradient_accumulation_resume_gate.json) ／ SHA256: `4f3c75fbc877165c93052026f726b95e3854ed1dd9f8d379e38e7b1862ad76ec` ／ 618 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.grouping | true |
| checks.full_committed_history | true |
| checks.resident_peak_under90percent | true |
| actual_CUDA_updates | 8 |
| verification_microbatches | 32 |
| verification_teacher_tokens | 312468 |
| peak_VRAM_bytes | 12839938048 |

</details>

<details>
<summary>reports/phase6/base_residual_initialization_resume_gate.json — None</summary>

[原記録](../../reports/phase6/base_residual_initialization_resume_gate.json) ／ SHA256: `c4aae3d099ce1f4c12ec953c9752e6f0603fb870b1f7b5e570a3ad8b77747cab` ／ 622 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.initialization | true |
| checks.full_committed_history | true |
| checks.resident_peak_under90percent | true |
| actual_CUDA_updates | 8 |
| verification_microbatches | 8 |
| verification_teacher_tokens | 75076 |
| peak_VRAM_bytes | 10634586624 |

</details>

<details>
<summary>reports/phase6/base_teacher_decay_2b_resume_gate.json — None</summary>

[原記録](../../reports/phase6/base_teacher_decay_2b_resume_gate.json) ／ SHA256: `45ba4e77ae8128444c6110136a8e900811325a88c04754a9477187e4793ca8c6` ／ 2,127 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.decay | true |
| checks.same_learned_parent_before_first_update | true |
| checks.full_committed_history | true |
| checks.resident_peak_under90percent | true |
| actual_CUDA_or_CPU_updates | 8 |
| verification_microbatches | 8 |
| initial_counters.update | 10000 |
| initial_counters.supervised_tokens | 94160195 |
| initial_counters.CE_input_tokens | 96655164 |
| initial_counters.auxiliary_input_tokens | 0 |
| initial_counters.auxiliary_pairs | 0 |
| initial_counters.physical_input_tokens | 404673920 |
| initial_counters.original_body_bytes | 382169159 |
| initial_counters.token_digest | "26b260437b751cb63b2e2922659bbac6b6e90adc983cd578626cdb0baf9a3dc4" |
| initial_counters.source_teachers.web | 70620030 |
| initial_counters.source_teachers.textbook | 18832118 |
| initial_counters.source_teachers.story | 4708047 |
| initial_counters.source_EOS.web | 619232 |
| initial_counters.source_EOS.textbook | 139904 |
| initial_counters.source_EOS.story | 35998 |
| final_verification_counters.update | 10004 |
| final_verification_counters.supervised_tokens | 94195927 |
| final_verification_counters.CE_input_tokens | 96691408 |
| final_verification_counters.auxiliary_input_tokens | 0 |
| final_verification_counters.auxiliary_pairs | 0 |
| final_verification_counters.physical_input_tokens | 404826320 |
| final_verification_counters.original_body_bytes | 382314679 |
| final_verification_counters.token_digest | "ef3c1320b1715fd58ecb0e98d4f42a17a9a5c1659683ffc42732ece126eda415" |
| final_verification_counters.source_teachers.web | 70646944 |
| final_verification_counters.source_teachers.textbook | 18839198 |
| final_verification_counters.source_teachers.story | 4709785 |
| final_verification_counters.source_EOS.web | 619477 |
| final_verification_counters.source_EOS.textbook | 139960 |
| final_verification_counters.source_EOS.story | 36016 |
| verification_teacher_tokens | 71464 |
| verification_weights_used_for_science | false |
| parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| peak_VRAM_bytes | 12443788800 |
| scope | "8 additional verification updates from exact learned parent; weights discarded" |

</details>

<details>
<summary>reports/phase6/base_teacher_decay_resume_gate.json — None</summary>

[原記録](../../reports/phase6/base_teacher_decay_resume_gate.json) ／ SHA256: `179b46d565bc6d6b64ef092312d1830391e5f5b45bed9f1b7aff195724683125` ／ 613 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.decay | true |
| checks.full_committed_history | true |
| checks.resident_peak_under90percent | true |
| actual_CUDA_updates | 8 |
| verification_microbatches | 8 |
| verification_teacher_tokens | 75076 |
| peak_VRAM_bytes | 10634586624 |

</details>

<details>
<summary>reports/phase6/batch_performance_report.json — passed</summary>

[原記録](../../reports/phase6/batch_performance_report.json) ／ SHA256: `96c23f43eaa0f93dd59a28f885263f99d9a3725728f3b628b25a6366e024ff74` ／ 785,914 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| scope | "Phase6 step3 resource and performance verification only; no long Base training" |
| selected.exact.status | "passed_exact" |
| selected.exact.checks.stable_model_exact | true |
| selected.exact.checks.stable_optimizer_exact | true |
| selected.exact.checks.stable_scheduler_exact | true |
| selected.exact.checks.stable_rng_exact | true |
| selected.exact.checks.stable_sampler_exact | true |
| selected.exact.checks.stable_tokens_exact | true |
| selected.exact.checks.stable_supervised_tokens_exact | true |
| selected.exact.checks.stable_body_bytes_exact | true |
| selected.exact.checks.stable_token_digest_exact | true |
| selected.exact.checks.stable_spec_exact | true |
| selected.exact.checks.stable_model_config_exact | true |
| selected.exact.checks.stable_implementation_sha256_exact | true |
| selected.exact.checks.stable_update_exact | true |
| selected.exact.checks.stable_metrics_complete | true |
| selected.exact.checks.stable_update_history_exact | true |
| selected.exact.checks.stable_loss_history_exact | true |
| selected.exact.checks.stable_lr_history_exact | true |
| selected.exact.checks.stable_gradient_norm_history_exact | true |
| selected.exact.checks.stable_tokens_seen_history_exact | true |
| selected.exact.checks.stable_supervised_tokens_history_exact | true |
| selected.exact.checks.stable_body_bytes_seen_history_exact | true |
| selected.exact.checks.stable_token_digest_history_exact | true |
| selected.exact.checks.stable_budget | true |
| selected.exact.checks.stable_finite | true |
| selected.exact.checks.decay_model_exact | true |
| selected.exact.checks.decay_optimizer_exact | true |
| selected.exact.checks.decay_scheduler_exact | true |
| selected.exact.checks.decay_rng_exact | true |
| selected.exact.checks.decay_sampler_exact | true |
| selected.exact.checks.decay_tokens_exact | true |
| selected.exact.checks.decay_supervised_tokens_exact | true |
| selected.exact.checks.decay_body_bytes_exact | true |
| selected.exact.checks.decay_token_digest_exact | true |
| selected.exact.checks.decay_spec_exact | true |
| selected.exact.checks.decay_model_config_exact | true |
| selected.exact.checks.decay_implementation_sha256_exact | true |
| selected.exact.checks.decay_update_exact | true |
| selected.exact.checks.decay_lineage_exact | true |
| selected.exact.checks.decay_branch_updates_exact | true |
| selected.exact.checks.decay_branch_tokens_exact | true |
| selected.exact.checks.decay_metrics_complete | true |
| selected.exact.checks.decay_update_history_exact | true |
| selected.exact.checks.decay_loss_history_exact | true |
| selected.exact.checks.decay_lr_history_exact | true |
| selected.exact.checks.decay_gradient_norm_history_exact | true |
| selected.exact.checks.decay_tokens_seen_history_exact | true |
| selected.exact.checks.decay_supervised_tokens_history_exact | true |
| selected.exact.checks.decay_body_bytes_seen_history_exact | true |
| selected.exact.checks.decay_token_digest_history_exact | true |
| selected.exact.checks.decay_budget | true |
| selected.exact.checks.decay_finite | true |
| selected.exact.checks.parent_checkpoint_and_run_immutable | true |
| selected.exact.checks.branch_budget | true |
| selected.median_tokens_per_second | 694521.4348618583 |
| selected.peak_vram_bytes | 6149073408 |
| capacity.reference-math.status | "verified" |
| capacity.reference-math.maximum_stable_batch | 45 |
| capacity.reference-math.first_oom_batch | 46 |
| capacity.reference-math.bounded_range | 256 |
| capacity.reference-math.boundary_exact | true |
| capacity.reference-math.fastest_short_probe_batch | 16 |
| capacity.reference-math.confirmed.16.variant.name | "reference-math" |
| capacity.reference-math.confirmed.16.variant.backend | "math" |
| capacity.reference-math.confirmed.16.variant.compile | false |
| capacity.reference-math.confirmed.16.variant.training_fast_path | false |
| capacity.reference-math.confirmed.16.variant.deterministic | false |
| capacity.reference-math.confirmed.16.batch | 16 |
| capacity.reference-math.confirmed.16.exact.status | "passed_exact" |
| capacity.reference-math.confirmed.16.exact.checks.stable_model_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_optimizer_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_scheduler_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_rng_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_sampler_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_tokens_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_supervised_tokens_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_body_bytes_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_token_digest_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_spec_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_model_config_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_implementation_sha256_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_update_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_metrics_complete | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_update_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_loss_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_lr_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_token_digest_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_budget | true |
| capacity.reference-math.confirmed.16.exact.checks.stable_finite | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_model_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_optimizer_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_scheduler_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_rng_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_sampler_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_tokens_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_supervised_tokens_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_body_bytes_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_token_digest_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_spec_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_model_config_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_implementation_sha256_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_update_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_lineage_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_branch_updates_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_branch_tokens_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_metrics_complete | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_update_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_loss_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_lr_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_token_digest_history_exact | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_budget | true |
| capacity.reference-math.confirmed.16.exact.checks.decay_finite | true |
| capacity.reference-math.confirmed.16.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.reference-math.confirmed.16.exact.checks.branch_budget | true |
| capacity.reference-math.confirmed.16.exact.batch | 16 |
| capacity.reference-math.confirmed.16.exact.completed_at | "2026-10-03T06:40:12.301764Z" |
| capacity.reference-math.confirmed.16.median_tokens_per_second | 127772.20362495357 |
| capacity.reference-math.confirmed.16.peak_vram_bytes | 8195175936 |
| capacity.reference-math.confirmed.45.variant.name | "reference-math" |
| capacity.reference-math.confirmed.45.variant.backend | "math" |
| capacity.reference-math.confirmed.45.variant.compile | false |
| capacity.reference-math.confirmed.45.variant.training_fast_path | false |
| capacity.reference-math.confirmed.45.variant.deterministic | false |
| capacity.reference-math.confirmed.45.batch | 45 |
| capacity.reference-math.confirmed.45.exact.status | "passed_exact" |
| capacity.reference-math.confirmed.45.exact.checks.stable_model_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_optimizer_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_scheduler_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_rng_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_sampler_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_tokens_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_supervised_tokens_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_body_bytes_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_token_digest_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_spec_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_model_config_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_implementation_sha256_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_update_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_metrics_complete | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_update_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_loss_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_lr_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_token_digest_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_budget | true |
| capacity.reference-math.confirmed.45.exact.checks.stable_finite | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_model_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_optimizer_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_scheduler_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_rng_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_sampler_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_tokens_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_supervised_tokens_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_body_bytes_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_token_digest_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_spec_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_model_config_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_implementation_sha256_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_update_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_lineage_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_branch_updates_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_branch_tokens_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_metrics_complete | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_update_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_loss_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_lr_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_token_digest_history_exact | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_budget | true |
| capacity.reference-math.confirmed.45.exact.checks.decay_finite | true |
| capacity.reference-math.confirmed.45.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.reference-math.confirmed.45.exact.checks.branch_budget | true |
| capacity.reference-math.confirmed.45.exact.batch | 45 |
| capacity.reference-math.confirmed.45.exact.completed_at | "2026-10-03T06:46:31.773813Z" |
| capacity.reference-math.confirmed.45.median_tokens_per_second | 120956.2794625851 |
| capacity.reference-math.confirmed.45.peak_vram_bytes | 22682606080 |
| capacity.compile-reduce-math.status | "verified" |
| capacity.compile-reduce-math.maximum_stable_batch | 53 |
| capacity.compile-reduce-math.first_oom_batch | 54 |
| capacity.compile-reduce-math.bounded_range | 256 |
| capacity.compile-reduce-math.boundary_exact | true |
| capacity.compile-reduce-math.fastest_short_probe_batch | 32 |
| capacity.compile-reduce-math.confirmed.32.variant.name | "compile-reduce-math" |
| capacity.compile-reduce-math.confirmed.32.variant.backend | "math" |
| capacity.compile-reduce-math.confirmed.32.variant.compile | true |
| capacity.compile-reduce-math.confirmed.32.variant.compile_mode | "reduce-overhead" |
| capacity.compile-reduce-math.confirmed.32.variant.training_fast_path | true |
| capacity.compile-reduce-math.confirmed.32.variant.deterministic | true |
| capacity.compile-reduce-math.confirmed.32.batch | 32 |
| capacity.compile-reduce-math.confirmed.32.exact.status | "passed_exact" |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_model_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_optimizer_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_scheduler_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_rng_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_sampler_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_supervised_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_body_bytes_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_token_digest_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_spec_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_model_config_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_implementation_sha256_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_update_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_metrics_complete | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_update_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_loss_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_lr_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_token_digest_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_budget | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.stable_finite | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_model_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_optimizer_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_scheduler_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_rng_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_sampler_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_supervised_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_body_bytes_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_token_digest_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_spec_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_model_config_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_implementation_sha256_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_update_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_lineage_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_branch_updates_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_branch_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_metrics_complete | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_update_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_loss_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_lr_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_token_digest_history_exact | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_budget | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.decay_finite | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.compile-reduce-math.confirmed.32.exact.checks.branch_budget | true |
| capacity.compile-reduce-math.confirmed.32.exact.batch | 32 |
| capacity.compile-reduce-math.confirmed.32.exact.completed_at | "2026-10-03T06:58:19.059499Z" |
| capacity.compile-reduce-math.confirmed.32.median_tokens_per_second | 292078.9772667684 |
| capacity.compile-reduce-math.confirmed.32.peak_vram_bytes | 13123794432 |
| capacity.compile-reduce-math.confirmed.53.variant.name | "compile-reduce-math" |
| capacity.compile-reduce-math.confirmed.53.variant.backend | "math" |
| capacity.compile-reduce-math.confirmed.53.variant.compile | true |
| capacity.compile-reduce-math.confirmed.53.variant.compile_mode | "reduce-overhead" |
| capacity.compile-reduce-math.confirmed.53.variant.training_fast_path | true |
| capacity.compile-reduce-math.confirmed.53.variant.deterministic | true |
| capacity.compile-reduce-math.confirmed.53.batch | 53 |
| capacity.compile-reduce-math.confirmed.53.exact.status | "passed_exact" |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_model_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_optimizer_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_scheduler_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_rng_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_sampler_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_supervised_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_body_bytes_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_token_digest_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_spec_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_model_config_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_implementation_sha256_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_update_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_metrics_complete | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_update_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_loss_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_lr_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_token_digest_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_budget | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.stable_finite | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_model_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_optimizer_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_scheduler_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_rng_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_sampler_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_supervised_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_body_bytes_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_token_digest_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_spec_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_model_config_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_implementation_sha256_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_update_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_lineage_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_branch_updates_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_branch_tokens_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_metrics_complete | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_update_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_loss_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_lr_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_token_digest_history_exact | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_budget | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.decay_finite | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.compile-reduce-math.confirmed.53.exact.checks.branch_budget | true |
| capacity.compile-reduce-math.confirmed.53.exact.batch | 53 |
| capacity.compile-reduce-math.confirmed.53.exact.completed_at | "2026-10-03T07:03:04.127394Z" |
| capacity.compile-reduce-math.confirmed.53.median_tokens_per_second | 286867.43680692214 |
| capacity.compile-reduce-math.confirmed.53.peak_vram_bytes | 21670942208 |
| capacity.compile-reduce-flash.status | "verified" |
| capacity.compile-reduce-flash.maximum_stable_batch | 111 |
| capacity.compile-reduce-flash.first_oom_batch | 112 |
| capacity.compile-reduce-flash.bounded_range | 256 |
| capacity.compile-reduce-flash.boundary_exact | true |
| capacity.compile-reduce-flash.fastest_short_probe_batch | 32 |
| capacity.compile-reduce-flash.confirmed.32.variant.name | "compile-reduce-flash" |
| capacity.compile-reduce-flash.confirmed.32.variant.backend | "flash" |
| capacity.compile-reduce-flash.confirmed.32.variant.compile | true |
| capacity.compile-reduce-flash.confirmed.32.variant.compile_mode | "reduce-overhead" |
| capacity.compile-reduce-flash.confirmed.32.variant.training_fast_path | true |
| capacity.compile-reduce-flash.confirmed.32.variant.deterministic | true |
| capacity.compile-reduce-flash.confirmed.32.batch | 32 |
| capacity.compile-reduce-flash.confirmed.32.exact.status | "passed_exact" |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_model_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_optimizer_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_scheduler_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_rng_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_sampler_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_supervised_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_body_bytes_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_token_digest_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_spec_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_model_config_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_implementation_sha256_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_update_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_metrics_complete | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_update_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_loss_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_lr_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_token_digest_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_budget | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.stable_finite | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_model_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_optimizer_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_scheduler_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_rng_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_sampler_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_supervised_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_body_bytes_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_token_digest_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_spec_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_model_config_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_implementation_sha256_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_update_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_lineage_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_branch_updates_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_branch_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_metrics_complete | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_update_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_loss_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_lr_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_token_digest_history_exact | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_budget | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.decay_finite | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.compile-reduce-flash.confirmed.32.exact.checks.branch_budget | true |
| capacity.compile-reduce-flash.confirmed.32.exact.batch | 32 |
| capacity.compile-reduce-flash.confirmed.32.exact.completed_at | "2026-10-03T07:12:37.013483Z" |
| capacity.compile-reduce-flash.confirmed.32.median_tokens_per_second | 694521.4348618583 |
| capacity.compile-reduce-flash.confirmed.32.peak_vram_bytes | 6149073408 |
| capacity.compile-reduce-flash.confirmed.111.variant.name | "compile-reduce-flash" |
| capacity.compile-reduce-flash.confirmed.111.variant.backend | "flash" |
| capacity.compile-reduce-flash.confirmed.111.variant.compile | true |
| capacity.compile-reduce-flash.confirmed.111.variant.compile_mode | "reduce-overhead" |
| capacity.compile-reduce-flash.confirmed.111.variant.training_fast_path | true |
| capacity.compile-reduce-flash.confirmed.111.variant.deterministic | true |
| capacity.compile-reduce-flash.confirmed.111.batch | 111 |
| capacity.compile-reduce-flash.confirmed.111.exact.status | "passed_exact" |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_model_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_optimizer_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_scheduler_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_rng_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_sampler_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_supervised_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_body_bytes_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_token_digest_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_spec_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_model_config_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_implementation_sha256_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_update_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_metrics_complete | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_update_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_loss_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_lr_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_gradient_norm_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_tokens_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_supervised_tokens_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_token_digest_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_budget | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.stable_finite | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_model_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_optimizer_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_scheduler_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_rng_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_sampler_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_supervised_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_body_bytes_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_token_digest_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_spec_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_model_config_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_implementation_sha256_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_update_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_lineage_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_branch_updates_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_branch_tokens_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_metrics_complete | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_update_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_loss_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_lr_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_gradient_norm_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_tokens_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_supervised_tokens_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_body_bytes_seen_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_token_digest_history_exact | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_budget | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.decay_finite | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.parent_checkpoint_and_run_immutable | true |
| capacity.compile-reduce-flash.confirmed.111.exact.checks.branch_budget | true |
| capacity.compile-reduce-flash.confirmed.111.exact.batch | 111 |
| capacity.compile-reduce-flash.confirmed.111.exact.completed_at | "2026-10-03T07:16:31.720182Z" |
| capacity.compile-reduce-flash.confirmed.111.median_tokens_per_second | 649563.0939632591 |
| capacity.compile-reduce-flash.confirmed.111.peak_vram_bytes | 21053954560 |
| limits | "Bounded CUDA study, 94% allocator cap, exact same-runtime resume and branch, 3x200 completed updates, dev sample only; capacity and fastest speed are separate" |
| completion_evidence.independent_checks | 1286 |
| completion_evidence.audit_sha256 | "998d5ea440fc1fede0d393171fea91f1c08328521ab28d01622fa961b0f01969" |
| completion_evidence.cold_resume_checks | 26 |
| completion_evidence.cold_resume_report | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/performance-cold-resume-20261003/cold_resume_report.json" |
| completion_evidence.cold_resume_sha256 | "3f87d70d0cb0d988ba110a43902d864bf2780bd82b233f781d5ca655e740edb4" |
| completion_evidence.original_study_report_sha256 | "46bfca8e16d0cd8dc4f7d9ade3b3cec0a78134eea906e7198cf3a2dbe45b903a" |

</details>

<details>
<summary>reports/phase6/complete_text_10b_resume_gate.json — None</summary>

[原記録](../../reports/phase6/complete_text_10b_resume_gate.json) ／ SHA256: `67fe94d23b573d350b385e8de15ea2ce08fc9af49aedd6b416bbc3a94fb09642` ／ 7,819 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.spec | true |
| checks.model_config | true |
| checks.implementation_sha256 | true |
| checks.pilot_implementation_sha256 | true |
| checks.pilot_binding | true |
| checks.update | true |
| checks.lineage | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_tokens_seen | true |
| checks.history_supervised_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_token_digest | true |
| checks.finite_losses_gradients | true |
| checks.two_short_two_web_updates | true |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| seconds | 10.23135794099926 |
| GPU_optimizer_updates | 8 |
| input_tokens | 262144 |
| schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-text-10b-100m-20261004/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-text-10b-100m-20261004/resume-gate/resumed.pt"] |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `bf4fc2a8e4779a05f094509823f267df06562f29303af1fcc2ca028a6152ce56` ／ 273 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `b31040c3e9f35d354fb3d531531f7cbbfcd5a0dd3c7771ace271a940cef1bb58` ／ 14,263 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259984 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/control/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/control/resume-gate/latest.json) ／ SHA256: `a7618b29bc2ca3f3f10b6bf732a78091bdeedbb489184ab594c193db52438043` ／ 280 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/control/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/control/resume-gate/result.json) ／ SHA256: `93b81d8d19832b0b96909a2eaefaa0d1efc620a6d67216237dcc1cd6e30a210e` ／ 14,256 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259984 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/positive4/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/positive4/resume-gate/latest.json) ／ SHA256: `e4c849133458591be0b7387d662716b55cf6815750c409db9f60544a9bdb8d8b` ／ 282 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/positive4/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/positive4/resume-gate/result.json) ／ SHA256: `04c5d39a7a51e34ad6289a44123c75b7bb784dcab095630a26cafec802958a4f` ／ 14,268 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259984 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `f7dc959a145febb35c39ebbee65ef062dc8cd4ef55104ef37165f3ab346ca90b` ／ 272 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `12e76a52e4e8db4cc7cd39788a92e7a14cf353b2e22841bb2be0003a2dca2842` ／ 14,249 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259566 |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/probe/large2048/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/probe/large2048/resume-gate/latest.json) ／ SHA256: `2afcbead716109754fe3357c2221412ee5aea76239bfb99c2a9b7612f96c7339` ／ 283 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/probe/large2048/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/probe/large2048/resume-gate/result.json) ／ SHA256: `c158ea9cb5a1b6f3e705d7c1eeec1eeae9a31bda4e44ae32148e39729672d7e2` ／ 14,264 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259984 |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/probe/small512/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/probe/small512/resume-gate/latest.json) ／ SHA256: `b0df081cc7726a29032a490cb0491bdbabba6847dc76f853d4c55b56191f6581` ／ 282 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/probe/small512/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/probe/small512/resume-gate/result.json) ／ SHA256: `d3f547fdc9c26c92c5e145fe955e3f40266f70060efcbbb864e64e94b9654a86` ／ 14,263 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259984 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `710e6112a220b50712fd5bca86025eb8b5606ed65a545609ad4283b31c8c97fb` ／ 272 bytes

| 原キー | 保存値 |
|---|---|
| update | 62170 |
| tokens_seen | 2037186560 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `52d0a6089fd9c9bfb2d40df37c8f3f2a51f7072885c2d356399db30d8951dd04` ／ 14,255 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 259544 |

</details>

<details>
<summary>reports/phase6/condition_learning_resume_gate.json — None</summary>

[原記録](../../reports/phase6/condition_learning_resume_gate.json) ／ SHA256: `39f7bc775e2e72d831a79feacf3192085597ed7c01180b3db3a7fa19f9240cb7` ／ 6,028 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.spec | true |
| checks.model_config | true |
| checks.implementation_sha256 | true |
| checks.pilot_implementation_sha256 | true |
| checks.pilot_binding | true |
| checks.update | true |
| checks.lineage | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_tokens_seen | true |
| checks.history_supervised_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_token_digest | true |
| checks.finite_losses_gradients | true |
| checks.two_short_two_web_updates | true |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| seconds | 10.441188078999403 |
| GPU_optimizer_updates | 8 |
| input_tokens | 262144 |
| schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-learning-20261005/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-learning-20261005/resume-gate/resumed.pt"] |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json) ／ SHA256: `f59cf223dad31bd609b3fa583bccad26df932c065c769fd1776ce58d1398dba6` ／ 268 bytes

| 原キー | 保存値 |
|---|---|
| update | 323193 |
| tokens_seen | 10590388224 |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/result.json) ／ SHA256: `49b697d4d0aaecd2f750bbe2fb1d415757017607d12d653559b4959ebb52ec39` ／ 58,834 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.version | true |
| checks.spec | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.update | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.shard_manifest_sha256 | true |
| checks.implementation_sha256 | true |
| checks.study_implementation_sha256 | true |
| checks.loss_implementation_sha256 | true |
| checks.study_binding | true |
| checks.pilot_binding | true |
| checks.lineage | true |
| checks.branch_updates | true |
| checks.branch_tokens | true |
| checks.history_lr | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_focus_token_digest | true |
| checks.history_actual_source_routes | true |
| checks.history_physical_input_tokens | true |
| checks.history_removed_prefix_targets | true |
| checks.history_source_focus_teachers | true |
| checks.history_source_input_tokens | true |
| checks.history_loss | true |
| checks.history_valid_input_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_source_eos | true |
| checks.history_source_teachers | true |
| checks.history_additional_teacher_tokens | true |
| checks.history_reference_token_digest | true |
| checks.history_actual_source_body_bytes | true |
| checks.history_actual_source_teachers | true |
| checks.history_gradient_norm | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_actual_source_eos | true |
| checks.history_supervised_tokens | true |
| checks.history_tokens_seen | true |
| checks.history_reference_suffix_teacher_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_update | true |
| checks.history_token_digest | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.transition_included | true |
| checks.actual_conditional_mask_active | true |
| GPU_optimizer_updates | 16 |
| verification_teacher_tokens | 351618 |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `481775c9a8d7a13d872c131e49cf25e7891e085820f37057a82320e201d552fd` ／ 279 bytes

| 原キー | 保存値 |
|---|---|
| update | 320439 |
| tokens_seen | 10500145152 |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `5e48f744520fe653f070902226e49775d082157ba37deacca661996981346125` ／ 24,462 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.KL_state | true |
| checks.ranking_state | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_ordinary_CE_loss | true |
| checks.history_reference_KL_loss | true |
| checks.history_reference_non_EOS_teacher_probability_mass | true |
| checks.history_reference_input_tokens | true |
| checks.history_reference_soft_target_body_positions | true |
| checks.history_reference_ignored_positions | true |
| checks.history_reference_digest | true |
| checks.history_combined_student_physical_input_tokens | true |
| checks.history_ranking_loss | true |
| checks.history_ranking_family_indices | true |
| checks.history_ranking_digest | true |
| checks.history_ranking_relational_choice_labels | true |
| checks.history_ranking_valid_input_tokens | true |
| checks.history_ranking_physical_input_positions | true |
| checks.history_ranking_gold_body_scored_positions | true |
| checks.history_ranking_foil_body_scored_positions | true |
| checks.history_ranking_gold_body_scored_bytes | true |
| checks.history_ranking_foil_body_scored_bytes | true |
| checks.history_combined_student_valid_input_tokens | true |
| checks.finite | true |
| checks.no_reheat | true |
| verification_reference_non_EOS_teacher_probability_mass | 65163.615234375 |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261602 |
| verification_reference_input_tokens | 65536 |
| verification_reference_soft_positions | 65276 |
| verification_ranking.updates | 8 |
| verification_ranking.families_seen | 16 |
| verification_ranking.relational_choice_labels | 32 |
| verification_ranking.valid_input_tokens | 2768 |
| verification_ranking.physical_input_positions | 16384 |
| verification_ranking.gold_body_scored_positions | 186 |
| verification_ranking.foil_body_scored_positions | 186 |
| verification_ranking.gold_body_scored_bytes | 834 |
| verification_ranking.foil_body_scored_bytes | 834 |

</details>

<details>
<summary>reports/phase6/corpus_10b_export_complete.json — export_complete_pending_full_independent_audit</summary>

[原記録](../../reports/phase6/corpus_10b_export_complete.json) ／ SHA256: `1de316a2063d83a522b6ee8cec10a93721292aa86f15a2505bd83a83039f3a4e` ／ 2,044 bytes

| 原キー | 保存値 |
|---|---|
| status | "export_complete_pending_full_independent_audit" |
| manifest.status | "built_not_audited" |
| manifest.splits.train.tokens | 12225819077 |
| manifest.splits.train.documents | 25879667 |
| manifest.splits.train.body_bytes | 47525339486 |
| manifest.splits.dev.tokens | 678132065 |
| manifest.splits.dev.documents | 1435451 |
| manifest.splits.dev.body_bytes | 2635935411 |
| manifest.splits.test.tokens | 679399996 |
| manifest.splits.test.documents | 1438276 |
| manifest.splits.test.body_bytes | 2641106123 |
| manifest.splits.test.stream_sha256 | "8f77e0761dea7898829440c6c810c1c825484a1629cde9d521ae232fd44d546b" |
| manifest.splits.test.index_sha256 | "bf1577b1885eeff66eb0a3d96c4cc9b2db66ce9f036d5c67768eef8135bab865" |
| manifest.near_scope | "128 permutations/32x4 equal bands; true character5gram Jaccard&gt;=0.85; probabilistic recall" |
| full_independent_audit_passed | false |
| actual_training_loader_checked | false |
| training_started | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_export_speed_probe.json — passed_all_real_sample_export_bytes</summary>

[原記録](../../reports/phase6/corpus_10b_export_speed_probe.json) ／ SHA256: `cba9b38ce1fc0231400d11ab3554eb62e3fd45b9aad4f74a956d7daa96b0427c` ／ 3,139 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_all_real_sample_export_bytes" |
| measured_gate_passed | true |
| elapsed_seconds | 42.136135644001115 |
| runtime_budget_seconds | 180 |
| scope | "Train-only fixed sample; same Tokenizer and all corpus/token/index bytes; ABBA ordering; no global cache flush" |

</details>

<details>
<summary>reports/phase6/corpus_10b_handoff_resume.json — resumed_exit_observation_live</summary>

[原記録](../../reports/phase6/corpus_10b_handoff_resume.json) ／ SHA256: `d0c05035a52e45bd958477604522d94269b33b39e71c8de3cdb0c48c9733f722` ／ 1,574 bytes

| 原キー | 保存値 |
|---|---|
| status | "resumed_exit_observation_live" |
| watcher.status | "waiting_for_prior_exit" |
| watcher.prior_identity.status | "running" |
| watcher.prior_identity.prior_cumulative_seconds | 680.553657957 |
| tests_passed | 5 |

</details>

<details>
<summary>reports/phase6/corpus_10b_handoff_timeout.json — failed</summary>

[原記録](../../reports/phase6/corpus_10b_handoff_timeout.json) ／ SHA256: `58109ce5898cbe054f53663745b90939942f56829da18a8d6fce5d7ec5545275` ／ 1,165 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| prior_identity.status | "running" |
| prior_identity.prior_cumulative_seconds | 680.553657957 |
| failure | "TimeoutError: Prior process did not exit after SIGINT; no replacement launched" |

</details>

<details>
<summary>reports/phase6/corpus_10b_handoff_watch.json — handoff_watcher_live</summary>

[原記録](../../reports/phase6/corpus_10b_handoff_watch.json) ／ SHA256: `43495fe3873734e3d60b0c8526e13b81229457e75c1e61167f09dca6f5a4c160` ／ 1,858 bytes

| 原キー | 保存値 |
|---|---|
| status | "handoff_watcher_live" |
| watcher.status | "waiting_for_completed_export" |
| watcher.prior_identity.status | "running" |
| watcher.prior_identity.prior_cumulative_seconds | 680.553657957 |
| guard_tests_passed | 3 |
| export_progress.splits.train.tokens | 5845385887 |
| export_progress.splits.train.documents | 12402433 |
| export_progress.splits.train.body_bytes | 22777003145 |
| export_progress.splits.dev.tokens | 324139354 |
| export_progress.splits.dev.documents | 688024 |
| export_progress.splits.dev.body_bytes | 1263021296 |
| export_progress.splits.test.tokens | 324817263 |
| export_progress.splits.test.documents | 689639 |
| export_progress.splits.test.body_bytes | 1265752785 |
| export_progress.seconds | 574.9703108080002 |
| audit_passed | false |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `779b27c735b76461cab2863d5871a04dc1b1835eff6465403fe589a4dfbc8257` ／ 276 bytes

| 原キー | 保存値 |
|---|---|
| update | 320439 |
| tokens_seen | 10500145152 |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `0057199d027deec9f4afa129e2cb9f44b59df82d19bb77770e6a628548ca867a` ／ 18,263 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.KL_state | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_ordinary_CE_loss | true |
| checks.history_reference_KL_loss | true |
| checks.history_reference_non_EOS_teacher_probability_mass | true |
| checks.history_reference_input_tokens | true |
| checks.history_reference_soft_target_body_positions | true |
| checks.history_reference_ignored_positions | true |
| checks.history_reference_digest | true |
| checks.history_combined_student_physical_input_tokens | true |
| checks.finite | true |
| checks.no_reheat | true |
| verification_reference_non_EOS_teacher_probability_mass | 65163.615234375 |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261602 |
| verification_reference_input_tokens | 65536 |
| verification_reference_soft_positions | 65276 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/latest.json) ／ SHA256: `d365dafb0a2bac30f107b2febd0bbfa61322f8c7bf4be5053116a54c3d74e8f4` ／ 282 bytes

| 原キー | 保存値 |
|---|---|
| update | 323507 |
| tokens_seen | 10600677376 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/result.json) ／ SHA256: `d6cadbfcbf727d8e01a970732e76f0295ede1a2facdb37b484d1635fce4133f7` ／ 15,618 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.history_CE_loss | true |
| checks.history_parameter_penalty | true |
| checks.history_parameter_coefficient | true |
| checks.history_parameter_penalty_teacher_tokens | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261616 |

</details>

<details>
<summary>reports/phase6/gated-shared-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/gated-shared-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `b75792817056d7bfcced4418d53a909fce41c12d6deece27b522ac44f154a1df` ／ 268 bytes

| 原キー | 保存値 |
|---|---|
| update | 323507 |
| tokens_seen | 10600677376 |

</details>

<details>
<summary>reports/phase6/gated-shared-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/gated-shared-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `c82bfffc5e0f757ac10393ea1b977507f63c390ee6b0cfd956b90b16e6359509` ／ 15,525 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.history_CE_loss | true |
| checks.history_new_gate_LR | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261616 |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/latest.json) ／ SHA256: `bd797c551259384abf4bed565052b954d4fbb83aed7c95d89732bd8d74237905` ／ 276 bytes

| 原キー | 保存値 |
|---|---|
| update | 320439 |
| tokens_seen | 10500145152 |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/result.json) ／ SHA256: `27dfba69498434dea566b4ff1fa6d4d7056e67f8d80d1326cc0fa783367e4c22` ／ 18,738 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.hard_replay_state | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_ordinary_CE_loss | true |
| checks.history_reference_body_CE_loss | true |
| checks.history_combined_hard_teacher_positions | true |
| checks.history_reference_non_EOS_teacher_probability_mass | true |
| checks.history_reference_input_tokens | true |
| checks.history_reference_hard_body_target_positions | true |
| checks.history_reference_ignored_positions | true |
| checks.history_reference_digest | true |
| checks.history_combined_student_physical_input_tokens | true |
| checks.finite | true |
| checks.no_reheat | true |
| verification_reference_non_EOS_teacher_probability_mass | 65163.615234375 |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261602 |
| verification_reference_input_tokens | 65536 |
| verification_reference_hard_positions | 65276 |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json) ／ SHA256: `01f95c57c65be222970611a5d04b67d781eaa85bae9e4f5e227dca29833db1f0` ／ 270 bytes

| 原キー | 保存値 |
|---|---|
| update | 320443 |
| tokens_seen | 10500276224 |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/result.json) ／ SHA256: `a9a80450ec5543093c3dfcea8ac63e2c73c19219430555a7d35c30684fee6921` ／ 79,841 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.version | true |
| checks.spec | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.update | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.shard_manifest_sha256 | true |
| checks.implementation_sha256 | true |
| checks.study_implementation_sha256 | true |
| checks.loss_implementation_sha256 | true |
| checks.study_binding | true |
| checks.pilot_binding | true |
| checks.lineage | true |
| checks.branch_updates | true |
| checks.branch_tokens | true |
| checks.history_loss | true |
| checks.history_source_eos | true |
| checks.history_body_bytes_seen | true |
| checks.history_reference_suffix_teacher_tokens | true |
| checks.history_gradient_norm | true |
| checks.history_source_input_tokens | true |
| checks.history_token_digest | true |
| checks.history_reference_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_additional_teacher_tokens | true |
| checks.history_actual_source_eos | true |
| checks.history_supervised_tokens | true |
| checks.history_tokens_seen | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_source_focus_teachers | true |
| checks.history_actual_source_teachers | true |
| checks.history_actual_source_body_bytes | true |
| checks.history_actual_source_routes | true |
| checks.history_valid_input_tokens | true |
| checks.history_update | true |
| checks.history_source_digests | true |
| checks.history_physical_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_focus_token_digest | true |
| checks.history_removed_prefix_targets | true |
| checks.history_lr | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.mixed_sources_present | true |
| checks.actual_conditional_mask_active | true |
| GPU_optimizer_updates | 16 |
| verification_teacher_tokens | 478390 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/resume-gate/latest.json) ／ SHA256: `96aee86f8ab78a889474667c7645ac472ae3ee66e929afd6f310100456b65a12` ／ 293 bytes

| 原キー | 保存値 |
|---|---|
| update | 322689 |
| tokens_seen | 10573873152 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/resume-gate/result.json) ／ SHA256: `ea90f3dcf1c1ffcf87ea8a8d9ea53c1400053d88867434ee9cef02cd24dc633b` ／ 11,687 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_update | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_tokens_seen | true |
| checks.history_supervised_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_token_digest | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_valid_input_tokens | true |
| checks.history_physical_input_tokens | true |
| checks.history_additional_teacher_tokens | true |
| checks.finite | true |
| checks.fixed_inherited_LR | true |
| verification_teacher_tokens | 257698 |
| GPU_optimizer_updates | 8 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/resume-gate/latest.json) ／ SHA256: `1a14a3ab714e1aaffb422659d9812c2bf3b704f3b0fb7012dbb26d2958e8c92e` ／ 285 bytes

| 原キー | 保存値 |
|---|---|
| update | 322689 |
| tokens_seen | 10573873152 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/resume-gate/result.json) ／ SHA256: `f9540fadf122adb83ebe6749e1ddc4b1d129110d0cd2372fef1c5d06ed5d90b7` ／ 11,661 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_update | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_tokens_seen | true |
| checks.history_supervised_tokens | true |
| checks.history_body_bytes_seen | true |
| checks.history_token_digest | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_valid_input_tokens | true |
| checks.history_physical_input_tokens | true |
| checks.history_additional_teacher_tokens | true |
| checks.finite | true |
| checks.fixed_inherited_LR | true |
| verification_teacher_tokens | 261592 |
| GPU_optimizer_updates | 8 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json) ／ SHA256: `8a7a5fa8afab1cc49670dd01e1663b346a7789364ed554469394dd8402a72ad9` ／ 288 bytes

| 原キー | 保存値 |
|---|---|
| update | 320443 |
| tokens_seen | 10500276224 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/result.json) ／ SHA256: `167092fbd2ed206172a9f351aa5f9e96a84cccaa513814fb579695127599f6d9` ／ 81,889 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.version | true |
| checks.spec | true |
| checks.model_config | true |
| checks.model | true |
| checks.unmerged_training_model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.update | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.shard_manifest_sha256 | true |
| checks.implementation_sha256 | true |
| checks.study_implementation_sha256 | true |
| checks.study_binding | true |
| checks.pilot_binding | true |
| checks.lineage | true |
| checks.branch_updates | true |
| checks.branch_tokens | true |
| checks.merged_for_native_evaluation | true |
| checks.native_parameters | true |
| checks.trainable_parameters | true |
| checks.history_supervised_tokens | true |
| checks.history_actual_source_eos | true |
| checks.history_tokens_seen | true |
| checks.history_source_input_tokens | true |
| checks.history_gradient_norm | true |
| checks.history_additional_teacher_tokens | true |
| checks.history_loss | true |
| checks.history_actual_source_body_bytes | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_source_body_bytes | true |
| checks.history_token_digest | true |
| checks.history_removed_prefix_targets | true |
| checks.history_body_bytes_seen | true |
| checks.history_reference_suffix_teacher_tokens | true |
| checks.history_trainable_parameters | true |
| checks.history_valid_input_tokens | true |
| checks.history_reference_token_digest | true |
| checks.history_actual_source_teachers | true |
| checks.history_source_teachers | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_source_eos | true |
| checks.history_focus_token_digest | true |
| checks.history_physical_input_tokens | true |
| checks.history_native_parameters | true |
| checks.history_source_digests | true |
| checks.history_update | true |
| checks.history_actual_source_routes | true |
| checks.history_arm | true |
| checks.history_lr | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.mixed_sources_present | true |
| checks.actual_conditional_mask_active | true |
| GPU_optimizer_updates | 16 |
| verification_teacher_tokens | 478390 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json) ／ SHA256: `d9a94f389888c22dec301452605e4cd993c37a28703aed29bd59fd4902c2da28` ／ 294 bytes

| 原キー | 保存値 |
|---|---|
| update | 320443 |
| tokens_seen | 10500276224 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/result.json) ／ SHA256: `3da04e4448427ba0b3059ca904e7989565e87096a42f9e3ce6e394b6deb9373f` ／ 81,981 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.version | true |
| checks.spec | true |
| checks.model_config | true |
| checks.model | true |
| checks.unmerged_training_model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.update | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.shard_manifest_sha256 | true |
| checks.implementation_sha256 | true |
| checks.study_implementation_sha256 | true |
| checks.study_binding | true |
| checks.pilot_binding | true |
| checks.lineage | true |
| checks.branch_updates | true |
| checks.branch_tokens | true |
| checks.merged_for_native_evaluation | true |
| checks.native_parameters | true |
| checks.trainable_parameters | true |
| checks.history_supervised_tokens | true |
| checks.history_actual_source_eos | true |
| checks.history_tokens_seen | true |
| checks.history_source_input_tokens | true |
| checks.history_gradient_norm | true |
| checks.history_additional_teacher_tokens | true |
| checks.history_loss | true |
| checks.history_actual_source_body_bytes | true |
| checks.history_weighted_teacher_mass | true |
| checks.history_outcome_weight | true |
| checks.history_source_body_bytes | true |
| checks.history_token_digest | true |
| checks.history_removed_prefix_targets | true |
| checks.history_body_bytes_seen | true |
| checks.history_reference_suffix_teacher_tokens | true |
| checks.history_trainable_parameters | true |
| checks.history_valid_input_tokens | true |
| checks.history_reference_token_digest | true |
| checks.history_actual_source_teachers | true |
| checks.history_source_teachers | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_source_eos | true |
| checks.history_focus_token_digest | true |
| checks.history_physical_input_tokens | true |
| checks.history_native_parameters | true |
| checks.history_source_digests | true |
| checks.history_update | true |
| checks.history_actual_source_routes | true |
| checks.history_arm | true |
| checks.history_lr | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.mixed_sources_present | true |
| checks.actual_conditional_mask_active | true |
| GPU_optimizer_updates | 16 |
| verification_teacher_tokens | 478390 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-corpus-evidence-20261007/CE-resume-result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-corpus-evidence-20261007/CE-resume-result.json) ／ SHA256: `553bee1669f8e32e40c2ff45431f70451ca114009a5d5c9dece2f414955b6b82` ／ 79,860 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.finite | true |
| checks.all_history_except_timing | true |
| checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-corpus-probe-20261007/CE/resume-gate/continuous.pt" |
| checkpoints.continuous.sha256 | "9f824b591b1ef25282b7cf7761e3aaf2fb6e1907635762897eead2af9e1c58de" |
| checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-corpus-probe-20261007/CE/resume-gate/resumed.pt" |
| checkpoints.resumed.sha256 | "3858d583950786b70c1ea0269b9a1ee3ccf7ffb9160d85f9efe6e55996ebb740" |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-corpus-evidence-20261007/contrast-resume-result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-corpus-evidence-20261007/contrast-resume-result.json) ／ SHA256: `af9f163a0eb4884245c3fa4e4cde77c428781b66a3df82c2f46ccbb8f23a0fdc` ／ 80,577 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.finite | true |
| checks.all_history_except_timing | true |
| checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-corpus-probe-20261007/contrast/resume-gate/continuous.pt" |
| checkpoints.continuous.sha256 | "f44cead2885cddafd8fff5dafca53c7a13628d9c81dec00b3d6d5bb7305a1496" |
| checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-corpus-probe-20261007/contrast/resume-gate/resumed.pt" |
| checkpoints.resumed.sha256 | "f78fe006db52e88e8e84248ec4b8c3cd2d946ee3b8d732b335355bf8527dbcb7" |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-probe-evidence-20261007/CE_plus_native_contrast-resume-result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-probe-evidence-20261007/CE_plus_native_contrast-resume-result.json) ／ SHA256: `175e5da139153aae8aa883ced7898a6a31f719f7109fe29a3a8c4ce39cc7bf1a` ／ 15,703 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.finite | true |
| checks.all_history_except_timing | true |
| checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/CE_plus_native_contrast/resume-gate/continuous.pt" |
| checkpoints.continuous.sha256 | "80f7306d1ab81194e2d1a3e311e56e1a847fd3e167b55c0837fb65e34d0f356c" |
| checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/CE_plus_native_contrast/resume-gate/resumed.pt" |
| checkpoints.resumed.sha256 | "239637a824be486af29a5fd5dcddaf16e1771b6febc2ab6b7c8bb27a804a8000" |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-probe-evidence-20261007/full_CE-resume-result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-probe-evidence-20261007/full_CE-resume-result.json) ／ SHA256: `be5067525f12b0ae24dabfbe4d77ce68c4a7706eeb0f67792c5603c201efa847` ／ 14,992 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.sampler | true |
| checks.counters | true |
| checks.finite | true |
| checks.all_history_except_timing | true |
| checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/full_CE/resume-gate/continuous.pt" |
| checkpoints.continuous.sha256 | "edd893db6360a498f77a66685a64d23474a5c100cfc80624bd09661a8f5b3662" |
| checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-probe-20261007/full_CE/resume-gate/resumed.pt" |
| checkpoints.resumed.sha256 | "cf89ba454c77be60e06baf0b1913d53be5259bb2265cd9eb2f108d724d4d7d95" |

</details>

<details>
<summary>reports/phase6/natural_learning_resume_gate.json — None</summary>

[原記録](../../reports/phase6/natural_learning_resume_gate.json) ／ SHA256: `7283e21c7ec3e3e1286a0c2f01a2799b4c2231524b6f4df82b1c591cae9c93b9` ／ 17,465 bytes

| 原キー | 保存値 |
|---|---|
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.tests/test_natural_learning.py | "cf1b52952aa6d036c741a80d511d6651b6b5cf425ae88324cdcc4c349883f8d2" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| passed | true |
| arms.inherit.checks.model | true |
| arms.inherit.checks.optimizer | true |
| arms.inherit.checks.scheduler | true |
| arms.inherit.checks.rng | true |
| arms.inherit.checks.sampler | true |
| arms.inherit.checks.tokens | true |
| arms.inherit.checks.supervised_tokens | true |
| arms.inherit.checks.body_bytes | true |
| arms.inherit.checks.token_digest | true |
| arms.inherit.checks.spec | true |
| arms.inherit.checks.model_config | true |
| arms.inherit.checks.pilot_binding | true |
| arms.inherit.checks.lineage | true |
| arms.inherit.checks.update | true |
| arms.inherit.checks.history_loss | true |
| arms.inherit.checks.history_gradient_norm | true |
| arms.inherit.checks.history_lr | true |
| arms.inherit.checks.history_source_teachers | true |
| arms.inherit.passed | true |
| arms.fresh.checks.model | true |
| arms.fresh.checks.optimizer | true |
| arms.fresh.checks.scheduler | true |
| arms.fresh.checks.rng | true |
| arms.fresh.checks.sampler | true |
| arms.fresh.checks.tokens | true |
| arms.fresh.checks.supervised_tokens | true |
| arms.fresh.checks.body_bytes | true |
| arms.fresh.checks.token_digest | true |
| arms.fresh.checks.spec | true |
| arms.fresh.checks.model_config | true |
| arms.fresh.checks.pilot_binding | true |
| arms.fresh.checks.lineage | true |
| arms.fresh.checks.update | true |
| arms.fresh.checks.history_loss | true |
| arms.fresh.checks.history_gradient_norm | true |
| arms.fresh.checks.history_lr | true |
| arms.fresh.checks.history_source_teachers | true |
| arms.fresh.passed | true |
| verification_teacher_tokens | 215168 |
| optimizer_updates | 16 |

</details>

<details>
<summary>reports/phase6/nonorm_export_initial_failure.json — failed</summary>

[原記録](../../reports/phase6/nonorm_export_initial_failure.json) ／ SHA256: `be603e1cdb1783fb198685f84142765bee3d44773b57b11c3f175255b8cc1285` ／ 3,908 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| binding.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt" |
| binding.checkpoint_sha256 | "e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| runtime.completion_binary_sha256 | "b0d29bb342c6e17635ffef4dea4d935a834f9ca898f3c999c182556acd0bfd6b" |
| runtime.note | "Archive checkout; embedded git build version can inherit parent repo and is not revision evidence" |
| scope | "Learned NoNorm export/cache/controller integrity; not Base quality or quantized quality" |
| failure | "Native learned short GGUF FP32 logits exceeded frozen tolerance; full 1024 diagnostic also fails. See original stderr and probe_nonorm_precision.py output." |

</details>

<details>
<summary>reports/phase6/nonorm_export_parity_report.json — passed</summary>

[原記録](../../reports/phase6/nonorm_export_parity_report.json) ／ SHA256: `6c224bda2b9a47b05e1516d8a1cebda529c9786e60425a8a948fb02882b7286a` ／ 44,562 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| binding.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt" |
| binding.checkpoint_sha256 | "e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.cpu_threads | 2 |
| binding.cpu_environment.MKL_CBWR | null |
| binding.cpu_environment.MKL_DYNAMIC | null |
| binding.cpu_environment.OMP_DYNAMIC | null |
| runtime.shared_library_sha256.build/bin/libggml-cpu.so | "881bb2294ad09447a1579691386309757b54bdead98e023f8c819d8cabcd5bff" |
| runtime.shared_library_sha256.build/bin/libllama-completion-impl.so | "5b257acb567e61ce8bc29a38e2793508a6f9757b260c15d314b48f5f39e5723f" |
| runtime.completion_binary_sha256 | "f6cd0818100f510c9cf0509c9ac22d8c50fb22ede3b4ad8ca43ea92a93d044f4" |
| runtime.note | "Archive checkout; embedded git build version can inherit parent repo and is not revision evidence" |
| checks.hf_llama_architecture_without_qknorm | true |
| checks.hf_tied_embedding | true |
| checks.learned_parameter_count | true |
| checks.precision_profile_keeps_all_weights_exact | true |
| checks.profile_is_real_artifact_inference | true |
| checks.native_eos_and_eot_eog_metadata | true |
| checks.all_short_and_1024_logits_cache_comparisons | true |
| checks.tied_embedding_exported_once | true |
| checks.golden_external_codec_roundtrips | true |
| checks.three_backend_greedy_ids_exact | true |
| checks.actual_argmax_stop_3_all_backends | true |
| checks.actual_argmax_stop_7_all_backends | true |
| checks.original_checkpoint_unchanged | true |
| comparisons.short_hf_full.passed | true |
| comparisons.short_torch_cache.passed | true |
| comparisons.short_hf_cache.passed | true |
| comparisons.short_gguf_prefill.passed | true |
| comparisons.short_gguf_cache.passed | true |
| comparisons.short_gguf_cache_vs_prefill.passed | true |
| comparisons.context1024_hf_full.passed | true |
| comparisons.context1024_torch_cache.passed | true |
| comparisons.context1024_hf_cache.passed | true |
| comparisons.context1024_gguf_prefill.passed | true |
| comparisons.context1024_gguf_cache.passed | true |
| comparisons.context1024_gguf_cache_vs_prefill.passed | true |
| scope | "Learned NoNorm export/cache/controller integrity; not Base quality or quantized quality" |
| float_gguf.file_bytes | 40097216 |
| weight_mapping.model.embed_tokens.weight | "token_embd.weight" |
| ordinary_generation.torch.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.torch.stop_reason | "max_new_tokens" |
| ordinary_generation.hf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.hf.stop_reason | "max_new_tokens" |
| ordinary_generation.gguf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.gguf.stop_reason | "max_new_tokens" |
| model_driven_stop_fixtures.3.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.gguf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.gguf.stop_reason | "stop_id" |

</details>

<details>
<summary>reports/phase6/nonorm_export_precision_failure.json — failed</summary>

[原記録](../../reports/phase6/nonorm_export_precision_failure.json) ／ SHA256: `b68adf56bca00157c934edf02ef629fa09984dc9c9db0bf03a4a109e666f9471` ／ 45,490 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| binding.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt" |
| binding.checkpoint_sha256 | "e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| runtime.completion_binary_sha256 | "cb38cc3fe04e5e26c86ad93ccd7e4f6278db810cebed1728c849bfc41ffec08f" |
| runtime.note | "Archive checkout; embedded git build version can inherit parent repo and is not revision evidence" |
| checks.hf_llama_architecture_without_qknorm | true |
| checks.hf_tied_embedding | true |
| checks.learned_parameter_count | true |
| checks.native_eos_and_eot_eog_metadata | true |
| checks.all_short_and_1024_logits_cache_comparisons | false |
| checks.tied_embedding_exported_once | true |
| checks.golden_external_codec_roundtrips | true |
| checks.three_backend_greedy_ids_exact | true |
| checks.actual_argmax_stop_3_all_backends | true |
| checks.actual_argmax_stop_7_all_backends | true |
| checks.original_checkpoint_unchanged | true |
| comparisons.short_hf_full.passed | true |
| comparisons.short_torch_cache.passed | true |
| comparisons.short_hf_cache.passed | true |
| comparisons.short_gguf_prefill.passed | false |
| comparisons.short_gguf_prefill.failure | "Tensor-likes are not close!\n\nMismatched elements: 4 / 126976 (0.0%)\nGreatest absolute difference: 1.2922915630042553e-05 at index (0, 21, 3905) (up to 1e-05 allowed)\nGreatest relative difference: 0.014835619367659092 at index (0, 21, 3905) (up to 0.0001 allowed)" |
| comparisons.short_gguf_cache.passed | false |
| comparisons.short_gguf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 2 / 126976 (0.0%)\nGreatest absolute difference: 1.1768192052841187e-05 at index (0, 21, 567) (up to 1e-05 allowed)\nGreatest relative difference: 0.01339865941554308 at index (0, 21, 3905) (up to 0.0001 allowed)" |
| comparisons.short_gguf_cache_vs_prefill.passed | true |
| comparisons.context1024_hf_full.passed | false |
| comparisons.context1024_hf_full.failure | "Tensor-likes are not close!\n\nMismatched elements: 1272 / 4194304 (0.0%)\nGreatest absolute difference: 3.9439648389816284e-05 at index (0, 12, 3338) (up to 1e-05 allowed)\nGreatest relative difference: 2.5112497806549072 at index (0, 51, 1096) (up to 0.0001 allowed)" |
| comparisons.context1024_torch_cache.passed | false |
| comparisons.context1024_torch_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 927 / 4194304 (0.0%)\nGreatest absolute difference: 3.789365291595459e-05 at index (0, 157, 3332) (up to 1e-05 allowed)\nGreatest relative difference: 0.6807678937911987 at index (0, 370, 130) (up to 0.0001 allowed)" |
| comparisons.context1024_hf_cache.passed | false |
| comparisons.context1024_hf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 565 / 4194304 (0.0%)\nGreatest absolute difference: 3.997981548309326e-05 at index (0, 88, 3836) (up to 1e-05 allowed)\nGreatest relative difference: 0.8939228057861328 at index (0, 445, 3203) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_prefill.passed | false |
| comparisons.context1024_gguf_prefill.failure | "Tensor-likes are not close!\n\nMismatched elements: 1286 / 4194304 (0.0%)\nGreatest absolute difference: 3.254786133766174e-05 at index (0, 50, 3247) (up to 1e-05 allowed)\nGreatest relative difference: 0.29708197712898254 at index (0, 216, 3426) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_cache.passed | false |
| comparisons.context1024_gguf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 1225 / 4194304 (0.0%)\nGreatest absolute difference: 3.254786133766174e-05 at index (0, 50, 3247) (up to 1e-05 allowed)\nGreatest relative difference: 0.29708197712898254 at index (0, 216, 3426) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_cache_vs_prefill.passed | true |
| scope | "Learned NoNorm export/cache/controller integrity; not Base quality or quantized quality" |
| float_gguf.file_bytes | 40097152 |
| weight_mapping.model.embed_tokens.weight | "token_embd.weight" |
| ordinary_generation.torch.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.torch.stop_reason | "max_new_tokens" |
| ordinary_generation.hf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.hf.stop_reason | "max_new_tokens" |
| ordinary_generation.gguf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.gguf.stop_reason | "max_new_tokens" |
| model_driven_stop_fixtures.3.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.gguf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.gguf.stop_reason | "stop_id" |
| failure | "AssertionError: {'hf_llama_architecture_without_qknorm': True, 'hf_tied_embedding': True, 'learned_parameter_count': True, 'native_eos_and_eot_eog_metadata': True, 'all_short_and_1024_logits_cache_comparisons': False, 'tied_embedding_exported_once': True, 'golden_external_codec_roundtrips': True, 'three_backend_greedy_ids_exact': True, 'actual_argmax_stop_3_all_backends': True, 'actual_argmax_stop_7_all_backends': True, 'original_checkpoint_unchanged': True}" |

</details>

<details>
<summary>reports/phase6/nonorm_export_stock_fp32_failure.json — failed</summary>

[原記録](../../reports/phase6/nonorm_export_stock_fp32_failure.json) ／ SHA256: `d1ea55e5e3633e2bd15662381008d01e65bc2deff49580b2a7f2a65d3a13b0f1` ／ 45,629 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| binding.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt" |
| binding.checkpoint_sha256 | "e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.cpu_threads | 2 |
| binding.cpu_environment.MKL_CBWR | "AUTO" |
| binding.cpu_environment.MKL_DYNAMIC | "FALSE" |
| binding.cpu_environment.OMP_DYNAMIC | "FALSE" |
| runtime.completion_binary_sha256 | "cb38cc3fe04e5e26c86ad93ccd7e4f6278db810cebed1728c849bfc41ffec08f" |
| runtime.note | "Archive checkout; embedded git build version can inherit parent repo and is not revision evidence" |
| checks.hf_llama_architecture_without_qknorm | true |
| checks.hf_tied_embedding | true |
| checks.learned_parameter_count | true |
| checks.native_eos_and_eot_eog_metadata | true |
| checks.all_short_and_1024_logits_cache_comparisons | false |
| checks.tied_embedding_exported_once | true |
| checks.golden_external_codec_roundtrips | true |
| checks.three_backend_greedy_ids_exact | true |
| checks.actual_argmax_stop_3_all_backends | true |
| checks.actual_argmax_stop_7_all_backends | true |
| checks.original_checkpoint_unchanged | true |
| comparisons.short_hf_full.passed | true |
| comparisons.short_torch_cache.passed | true |
| comparisons.short_hf_cache.passed | true |
| comparisons.short_gguf_prefill.passed | false |
| comparisons.short_gguf_prefill.failure | "Tensor-likes are not close!\n\nMismatched elements: 4 / 126976 (0.0%)\nGreatest absolute difference: 1.2922915630042553e-05 at index (0, 21, 3905) (up to 1e-05 allowed)\nGreatest relative difference: 0.014835619367659092 at index (0, 21, 3905) (up to 0.0001 allowed)" |
| comparisons.short_gguf_cache.passed | false |
| comparisons.short_gguf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 2 / 126976 (0.0%)\nGreatest absolute difference: 1.1768192052841187e-05 at index (0, 21, 567) (up to 1e-05 allowed)\nGreatest relative difference: 0.01339865941554308 at index (0, 21, 3905) (up to 0.0001 allowed)" |
| comparisons.short_gguf_cache_vs_prefill.passed | true |
| comparisons.context1024_hf_full.passed | false |
| comparisons.context1024_hf_full.failure | "Tensor-likes are not close!\n\nMismatched elements: 1272 / 4194304 (0.0%)\nGreatest absolute difference: 3.9439648389816284e-05 at index (0, 12, 3338) (up to 1e-05 allowed)\nGreatest relative difference: 2.5112497806549072 at index (0, 51, 1096) (up to 0.0001 allowed)" |
| comparisons.context1024_torch_cache.passed | false |
| comparisons.context1024_torch_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 927 / 4194304 (0.0%)\nGreatest absolute difference: 3.789365291595459e-05 at index (0, 157, 3332) (up to 1e-05 allowed)\nGreatest relative difference: 0.6807678937911987 at index (0, 370, 130) (up to 0.0001 allowed)" |
| comparisons.context1024_hf_cache.passed | false |
| comparisons.context1024_hf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 565 / 4194304 (0.0%)\nGreatest absolute difference: 3.997981548309326e-05 at index (0, 88, 3836) (up to 1e-05 allowed)\nGreatest relative difference: 0.8939228057861328 at index (0, 445, 3203) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_prefill.passed | false |
| comparisons.context1024_gguf_prefill.failure | "Tensor-likes are not close!\n\nMismatched elements: 1286 / 4194304 (0.0%)\nGreatest absolute difference: 3.254786133766174e-05 at index (0, 50, 3247) (up to 1e-05 allowed)\nGreatest relative difference: 0.29708197712898254 at index (0, 216, 3426) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_cache.passed | false |
| comparisons.context1024_gguf_cache.failure | "Tensor-likes are not close!\n\nMismatched elements: 1225 / 4194304 (0.0%)\nGreatest absolute difference: 3.254786133766174e-05 at index (0, 50, 3247) (up to 1e-05 allowed)\nGreatest relative difference: 0.29708197712898254 at index (0, 216, 3426) (up to 0.0001 allowed)" |
| comparisons.context1024_gguf_cache_vs_prefill.passed | true |
| scope | "Learned NoNorm export/cache/controller integrity; not Base quality or quantized quality" |
| float_gguf.file_bytes | 40097152 |
| weight_mapping.model.embed_tokens.weight | "token_embd.weight" |
| ordinary_generation.torch.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.torch.stop_reason | "max_new_tokens" |
| ordinary_generation.hf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.hf.stop_reason | "max_new_tokens" |
| ordinary_generation.gguf.generated_body_bytes_hex | "e9a088e381a8e381af0ae58685e5aeb9e7b4b9e4bb8b0ae3808ce7" |
| ordinary_generation.gguf.stop_reason | "max_new_tokens" |
| model_driven_stop_fixtures.3.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.3.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.3.results.gguf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.torch.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.torch.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.hf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.hf.stop_reason | "stop_id" |
| model_driven_stop_fixtures.7.results.gguf.generated_body_bytes_hex | "" |
| model_driven_stop_fixtures.7.results.gguf.stop_reason | "stop_id" |
| failure | "AssertionError: {'hf_llama_architecture_without_qknorm': True, 'hf_tied_embedding': True, 'learned_parameter_count': True, 'native_eos_and_eot_eog_metadata': True, 'all_short_and_1024_logits_cache_comparisons': False, 'tied_embedding_exported_once': True, 'golden_external_codec_roundtrips': True, 'three_backend_greedy_ids_exact': True, 'actual_argmax_stop_3_all_backends': True, 'actual_argmax_stop_7_all_backends': True, 'original_checkpoint_unchanged': True}" |

</details>

<details>
<summary>reports/phase6/packing_study_resume_gate.json — None</summary>

[原記録](../../reports/phase6/packing_study_resume_gate.json) ／ SHA256: `a7c3a5de9870deabd96c0cd45415b302304fe8750ca675761aa5b040dc8297b4` ／ 24,317 bytes

| 原キー | 保存値 |
|---|---|
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| passed | true |
| arms.fixed.checks.model | true |
| arms.fixed.checks.optimizer | true |
| arms.fixed.checks.scheduler | true |
| arms.fixed.checks.rng | true |
| arms.fixed.checks.sampler | true |
| arms.fixed.checks.tokens | true |
| arms.fixed.checks.supervised_tokens | true |
| arms.fixed.checks.body_bytes | true |
| arms.fixed.checks.token_digest | true |
| arms.fixed.checks.spec | true |
| arms.fixed.checks.model_config | true |
| arms.fixed.checks.pilot_binding | true |
| arms.fixed.checks.lineage | true |
| arms.fixed.checks.update | true |
| arms.fixed.checks.history_loss | true |
| arms.fixed.checks.history_gradient_norm | true |
| arms.fixed.checks.history_lr | true |
| arms.fixed.checks.history_tokens_seen | true |
| arms.fixed.checks.history_supervised_tokens | true |
| arms.fixed.checks.history_body_bytes_seen | true |
| arms.fixed.checks.history_token_digest | true |
| arms.fixed.checks.history_source_teachers | true |
| arms.fixed.checks.finite_losses_gradients | true |
| arms.fixed.checks.teachers_input_padding_exact | true |
| arms.fixed.peak_allocated_bytes | 6149073408 |
| arms.fixed.passed | true |
| arms.shuffle.checks.model | true |
| arms.shuffle.checks.optimizer | true |
| arms.shuffle.checks.scheduler | true |
| arms.shuffle.checks.rng | true |
| arms.shuffle.checks.sampler | true |
| arms.shuffle.checks.tokens | true |
| arms.shuffle.checks.supervised_tokens | true |
| arms.shuffle.checks.body_bytes | true |
| arms.shuffle.checks.token_digest | true |
| arms.shuffle.checks.spec | true |
| arms.shuffle.checks.model_config | true |
| arms.shuffle.checks.pilot_binding | true |
| arms.shuffle.checks.lineage | true |
| arms.shuffle.checks.update | true |
| arms.shuffle.checks.history_loss | true |
| arms.shuffle.checks.history_gradient_norm | true |
| arms.shuffle.checks.history_lr | true |
| arms.shuffle.checks.history_tokens_seen | true |
| arms.shuffle.checks.history_supervised_tokens | true |
| arms.shuffle.checks.history_body_bytes_seen | true |
| arms.shuffle.checks.history_token_digest | true |
| arms.shuffle.checks.history_source_teachers | true |
| arms.shuffle.checks.finite_losses_gradients | true |
| arms.shuffle.checks.teachers_input_padding_exact | true |
| arms.shuffle.peak_allocated_bytes | 6149073408 |
| arms.shuffle.passed | true |
| arms.isolated.checks.model | true |
| arms.isolated.checks.optimizer | true |
| arms.isolated.checks.scheduler | true |
| arms.isolated.checks.rng | true |
| arms.isolated.checks.sampler | true |
| arms.isolated.checks.tokens | true |
| arms.isolated.checks.supervised_tokens | true |
| arms.isolated.checks.body_bytes | true |
| arms.isolated.checks.token_digest | true |
| arms.isolated.checks.spec | true |
| arms.isolated.checks.model_config | true |
| arms.isolated.checks.pilot_binding | true |
| arms.isolated.checks.lineage | true |
| arms.isolated.checks.update | true |
| arms.isolated.checks.history_loss | true |
| arms.isolated.checks.history_gradient_norm | true |
| arms.isolated.checks.history_lr | true |
| arms.isolated.checks.history_tokens_seen | true |
| arms.isolated.checks.history_supervised_tokens | true |
| arms.isolated.checks.history_body_bytes_seen | true |
| arms.isolated.checks.history_token_digest | true |
| arms.isolated.checks.history_source_teachers | true |
| arms.isolated.checks.finite_losses_gradients | true |
| arms.isolated.checks.teachers_input_padding_exact | true |
| arms.isolated.peak_allocated_bytes | 10076272128 |
| arms.isolated.passed | true |
| verification_teacher_tokens | 625842 |
| GPU_optimizer_updates | 24 |
| seconds | 28.915837920008926 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/resume-gate/latest.json) ／ SHA256: `0174a5c10771c456ab7a7bd76ac5b3ed338adde7aea50ea43a821f5312551ce1` ／ 295 bytes

| 原キー | 保存値 |
|---|---|
| update | 323507 |
| tokens_seen | 10600677376 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/resume-gate/result.json) ／ SHA256: `2a70a54a25d0e85093015275037731e4b06fbe8fa4c23ea80be622822bdd3927` ／ 15,383 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.history_CE_loss | true |
| checks.history_parameter_penalty | true |
| checks.history_parameter_coefficient | true |
| checks.history_parameter_penalty_teacher_tokens | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261616 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/resume-gate/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/resume-gate/latest.json) ／ SHA256: `c7e0d44ff0bdb2be08e8a58e61e3afa7009de2088244f5f76dd687e79f4ed6da` ／ 294 bytes

| 原キー | 保存値 |
|---|---|
| update | 323507 |
| tokens_seen | 10600677376 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/resume-gate/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/resume-gate/result.json) ／ SHA256: `e04e0bd5d2c2779fb6be73d757e4e8a17dacce605ed214b6149e0260747c00e2` ／ 15,627 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.rng | true |
| checks.sampler | true |
| checks.lineage | true |
| checks.tokens | true |
| checks.supervised_tokens | true |
| checks.body_bytes | true |
| checks.token_digest | true |
| checks.focus_token_digest | true |
| checks.focus_teacher_tokens | true |
| checks.weighted_teacher_mass | true |
| checks.update | true |
| checks.spec | true |
| checks.model_config | true |
| checks.pilot_binding | true |
| checks.study_binding | true |
| checks.history_loss | true |
| checks.history_gradient_norm | true |
| checks.history_lr | true |
| checks.history_token_digest | true |
| checks.history_source_teachers | true |
| checks.history_source_eos | true |
| checks.history_source_input_tokens | true |
| checks.history_source_body_bytes | true |
| checks.history_source_focus_teachers | true |
| checks.history_focus_token_digest | true |
| checks.history_focus_teacher_tokens | true |
| checks.history_weighted_teacher_mass | true |
| checks.finite | true |
| checks.no_reheat | true |
| checks.history_CE_loss | true |
| checks.history_parameter_penalty | true |
| checks.history_parameter_coefficient | true |
| checks.history_parameter_penalty_teacher_tokens | true |
| GPU_optimizer_updates | 8 |
| verification_teacher_tokens | 261616 |

</details>
