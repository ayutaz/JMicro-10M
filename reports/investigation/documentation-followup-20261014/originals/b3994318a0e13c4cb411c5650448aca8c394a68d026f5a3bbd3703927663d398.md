# 教材・供給・品質・量 — 1/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/anchored_context_outcome_preparation.json — positive_anchor_CPU_loss_masks_causal_model_full_resume_passed_CUDA_pending</summary>

[原記録](../../reports/phase6/anchored_context_outcome_preparation.json) ／ SHA256: `171149fccc729ce25f6d4d47b0deec29d4a38a8a4c22071dd0cbcb838cc8d825` ／ 2,911 bytes

| 原キー | 保存値 |
|---|---|
| status | "positive_anchor_CPU_loss_masks_causal_model_full_resume_passed_CUDA_pending" |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/anchored_context_outcome_cpu_tests.xml" |
| CPU_tests.sha256 | "149bb8515af537e684f226bf65c4b79124cb862bd6b9ac77b0fd479ab385e27b" |
| CPU_passed_tests | 4 |
| CPU_test_seconds | 1.678 |
| source_sha256.tests/test_anchored_context_outcome.py | "696248ebab43a216c30d952216f545d276e1802fe5555a3965827ffd4954d951" |
| source_sha256.tests/test_anchored_context_outcome_trainer.py | "8cc5d04a0b5308b82503fdd0abc61c4c3fe7acfeaa82205870f1d052ebb6635a" |
| actual_checks | ["Positive correct-row token-weighted loss and identical old ranking term; foil/prefix/pad/directEOS hard gradient excluded.", "Concrete lower-gold-probability/improved-ranking example detected by added anchor.", "Real tiny learned CPU model4vs2+2 matches entire saved state and all nonduration history; all3 samplers, newhard ledger and singleAdamstep preserved; corrupted teacher state rejected.", "Actual JMicro CPU valid logits match padded/standalone rows; future changed tokens cannot alter earlier logits."] |
| new_original_corpus_tokens | 0 |
| GPU_training_seconds | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/aozora_source_pin.json — None</summary>

[原記録](../../reports/phase6/aozora_source_pin.json) ／ SHA256: `d189308fc43c87fdf80e935f5a02b0d26042b4e91aa6d4560a31e24a5541b1a9` ／ 1,000 bytes

| 原キー | 保存値 |
|---|---|
| maximum_raw_bytes | 500000000 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base-headwise-gate-comparison-20261007/review-CPU-state-v3-preparation.json — read_only_CPU_fullstate_audit_repair_verified_not_quality</summary>

[原記録](../../reports/phase6/base-headwise-gate-comparison-20261007/review-CPU-state-v3-preparation.json) ／ SHA256: `1d9b6ef1f0168d9c7bacb2707f18b4e52abcc949c85f3ad0922f6cc2ed3c7991` ／ 2,383 bytes

| 原キー | 保存値 |
|---|---|
| status | "read_only_CPU_fullstate_audit_repair_verified_not_quality" |
| original_CPU_metadata_refusals.static_half | "Gate recipe/arm/parent/source/config differs" |
| original_CPU_metadata_refusals.query_headwise | "Gate recipe/arm/parent/source/config differs" |
| actual_completed_checkpoints.static_half.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-headwise-gate-comparison-20261007/static_half/checkpoint-00017698.pt" |
| actual_completed_checkpoints.static_half.checkpoint_sha256 | "5ae7d58dd8ed529679139a75237a40c3f92fbb6ff37cbb98d33a99e779fac886" |
| actual_completed_checkpoints.static_half.update | 17698 |
| actual_completed_checkpoints.static_half.supervised_tokens | 100000000 |
| actual_completed_checkpoints.static_half.all_actual_committed_state_validated_on_CPU | true |
| actual_completed_checkpoints.query_headwise.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-headwise-gate-comparison-20261007/query_headwise/checkpoint-00017698.pt" |
| actual_completed_checkpoints.query_headwise.checkpoint_sha256 | "c2d8c730632093bbc10ff2adfff2cbe37e3372d3f957110db141bf4ad66c34aa" |
| actual_completed_checkpoints.query_headwise.update | 17698 |
| actual_completed_checkpoints.query_headwise.supervised_tokens | 100000000 |
| actual_completed_checkpoints.query_headwise.all_actual_committed_state_validated_on_CPU | true |
| wrong_scientific_precision_rejected | "Actual scientific CUDA BF16/Flash recipe required" |
| candidate80_read_for_this_repair | 0 |
| new_forward_backward_updates | 0 |
| new_optimizer_updates | 0 |
| GPU_seconds | 0 |
| scientific_source_changed | false |
| scientific_recipe_changed | false |
| Base_complete | false |
| scope | "Read saved actual CUDA states on CPU. Retains strict bf16/flash training recipe and all original fullstate checks; no CPU forward is evidence of CUDA learning." |

</details>

<details>
<summary>reports/phase6/base-headwise-gate-comparison-20261007/review-JSON-spec-v2-preparation.json — reviewer_JSON_metadata_adapter_prepared_not_quality</summary>

[原記録](../../reports/phase6/base-headwise-gate-comparison-20261007/review-JSON-spec-v2-preparation.json) ／ SHA256: `b8faae8ad907a954b70975d93120890a92c159af8b1a68fbcd126a01ce91671a` ／ 1,220 bytes

| 原キー | 保存値 |
|---|---|
| status | "reviewer_JSON_metadata_adapter_prepared_not_quality" |
| scientific_source_changed | false |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-hq-feasibility-20261007/repository.json — None</summary>

[原記録](../../reports/phase6/base-hq-feasibility-20261007/repository.json) ／ SHA256: `cdf9d3207f348a779aaca18032e58e223d9de45903e7898983aa3d7b8381d557` ／ 256,745 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-hq-feasibility-20261007/sample-plan.json — None</summary>

[原記録](../../reports/phase6/base-hq-feasibility-20261007/sample-plan.json) ／ SHA256: `e66295e0829e9b092f7ebb4c888951588e85f3e35c9572796b7af1e93e0af627` ／ 1,172 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100723 |
| expected_compressed_column_bytes | 13381085 |
| wall_limit_seconds | 60 |
| CPU_limit_seconds | 30 |
| remote_byte_limit | 104857600 |
| limitations | "One source file/dump; source inspection, not globally independent or accepted training data. Old-family near duplicates and fixed suite exclusions must be handled before learning." |

</details>

<details>
<summary>reports/phase6/base-source-semantic-judge-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/base-source-semantic-judge-20261007/job.json) ／ SHA256: `7bb069c568da06d05ed08e2b45a3525c851c3eb27e44f8ef374c6dc2ad52028a` ／ 761 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 54.2281782880018 |
| completed_documents | 64 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| classifier_feasibility_passed | false |

</details>

<details>
<summary>reports/phase6/base-source-semantic-judge-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-source-semantic-judge-launcher-20261007/launcher.json) ／ SHA256: `39518bc3ee02dbb415c9ff2c06f0b451de76882df4cfc1169ec4e8a2b6801442` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-source-semantic-judge-launcher-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-source-semantic-judge-launcher-20261007/result.json) ／ SHA256: `53fd7f12219e7b8b4802aeac056d6bf9a9097db28383e6c502a4b5d35d5fba89` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base_10b_preparation_completion_audit.json — completed_step1_preparation_verified</summary>

[原記録](../../reports/phase6/base_10b_preparation_completion_audit.json) ／ SHA256: `f048a4d5467cbc2a2ceb8bfec2b1fdf31b2b1998b35a0ab3fd48c4bfca169bda` ／ 2,972 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_step1_preparation_verified" |
| requested_scope | "Chat step1: configure direct10B execution and verify checkpoint/CUDA save-resume; stop before science training" |
| requirements.direct10B_budget | 10000007168 |
| requirements.planned_scientific_additional_tokens | 5249990656 |
| requirements.actual_scientific_training_tokens | 0 |
| requirements.verification_tokens | 524288 |
| requirements.verification_optimizer_updates | 16 |
| requirements.CPU_tests_passed | 14 |
| requirements.saved_evidence_checks_passed | 26 |
| requirements.default_shell_completed_verification_without_retraining | true |
| job.status | "complete" |
| job.actual_GPU_compute_idle | true |
| job.GPU_seconds | 19.216758719999987 |
| job.preparation_budget_seconds | 600 |
| preserved_historical_checkpoint_sha256.reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt | "1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a" |
| preserved_historical_checkpoint_sha256.reports/phase6/eos-5b-finish-100m-20261004/web/checkpoint-00155640.pt | "c1b83c8e03f653af378797fbfea604ea33aec2134a6fea936ea0bb2157a9e0bb" |
| preserved_historical_checkpoint_sha256.reports/phase6/eos-5b-finish-100m-20261004/short20/checkpoint-00155640.pt | "19a960feb5b809c277cd710f23765e14d27099502153561ba437eee20dd42d54" |
| artifacts_sha256.tests/test_base_10b.py | "2d17c21c3eba5a687e7b721f1bcce2d4efa818a93d4845b69d7b357a52934bc2" |

</details>

<details>
<summary>reports/phase6/base_10b_preparation_launcher.json — None</summary>

[原記録](../../reports/phase6/base_10b_preparation_launcher.json) ／ SHA256: `de4b2a67a4175ea5d0ed9406f30d9650c3dea3892a8d8070570f0c179f878c02` ／ 323 bytes

| 原キー | 保存値 |
|---|---|
| scientific_training_started | false |

</details>

<details>
<summary>reports/phase6/base_10b_preparation_review.json — completed_step1_ready_before_scientific10B</summary>

[原記録](../../reports/phase6/base_10b_preparation_review.json) ／ SHA256: `f90590419743244c46b687373ea93cc89491462a7e0293db84037aff3c46d4d3` ／ 5,453 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_step1_ready_before_scientific10B" |
| checks.actual_verification_process_complete_exited | true |
| checks.science_training_not_started | true |
| checks.frozen_sources_core | true |
| checks.tests_no_failure_error_skip | true |
| checks.train_manifest_tokenizer_unchanged | true |
| checks.go_evidence_bound | true |
| checks.stable_parent_evidence_bound | true |
| checks.real_CUDA16_verification_tokens_separate | true |
| checks.CUDA_budget | true |
| checks.immutable_real_stable4_75B_parent | true |
| checks.no_LR_jump_or_other_setting_change | true |
| checks.model10M_unchanged | true |
| checks.data_cursor_epoch0_can_reach10B | true |
| checks.direct10B_exact_budget | true |
| checks.production_LR_curve_floor | true |
| checks.stable-extension_all_saved_state_exact | true |
| checks.stable-extension_completed_updates_tokens_saved | true |
| checks.stable-extension_Adam_scheduler_RNG_sampler_counters | true |
| checks.stable-extension_finite_forward_backward_and_matching_history | true |
| checks.stable_extension_lineage_from_correct_parent | true |
| checks.decay_all_saved_state_exact | true |
| checks.decay_completed_updates_tokens_saved | true |
| checks.decay_Adam_scheduler_RNG_sampler_counters | true |
| checks.decay_finite_forward_backward_and_matching_history | true |
| checks.verification4_update_decay_is_not_production15259 | true |
| checks.uv_pinned_Python_WSL4090_BF16 | true |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.tests/test_base_10b.py | "2d17c21c3eba5a687e7b721f1bcce2d4efa818a93d4845b69d7b357a52934bc2" |
| binding.source_sha256.tests/test_stable_extension.py | "950f717651267d1c5222f1d62e8c5fba05d6709c808579ed7ebb6d37476fcef3" |
| binding.parent.update | 144959 |
| binding.parent.tokens | 4750016512 |
| binding.parent.spec.seed | 42 |
| binding.parent.spec.schedule_updates | 144959 |
| binding.parent.token_digest | "55aab30d70a67de138e19e57be26549f366a378dc4fc6192ea583129300345c7" |
| parent.update | 144959 |
| parent.tokens | 4750016512 |
| parent.spec.seed | 42 |
| parent.spec.schedule_updates | 144959 |
| parent.token_digest | "55aab30d70a67de138e19e57be26549f366a378dc4fc6192ea583129300345c7" |
| tests.tests | 14 |
| tests.failures | 0 |
| tests.errors | 0 |
| tests.skipped | 0 |
| scientific_training_input_tokens | 0 |
| verification_optimizer_updates | 16 |
| verification_input_tokens | 524288 |
| preparation_gpu_elapsed_seconds | 19.216758719999987 |
| planned_scientific_additional_tokens | 5249990656 |
| planned_total_training_tokens | 10000007168 |

</details>

<details>
<summary>reports/phase6/base_5b_preparation.json — step1_verified_step2_running</summary>

[原記録](../../reports/phase6/base_5b_preparation.json) ／ SHA256: `f24d43704b389fc2c734a2de723dd472390997d0ea668f0d58ee37c8929818b8` ／ 2,940 bytes

| 原キー | 保存値 |
|---|---|
| status | "step1_verified_step2_running" |
| checked_at | "2026-10-04T06:05:17.1712293Z" |
| scope | "Requested steps1,2: stable budget extension and total5B training; evaluation deferred" |
| tests.tests | 6 |
| tests.failures | 0 |
| tests.errors | 0 |
| tests.skipped | 0 |
| tests.report | "reports/phase6/base_5b_tests.xml" |
| CUDA_gate_passed | true |
| CUDA_gate_checks.stable-extension:version | true |
| CUDA_gate_checks.stable-extension:spec | true |
| CUDA_gate_checks.stable-extension:model_config | true |
| CUDA_gate_checks.stable-extension:model | true |
| CUDA_gate_checks.stable-extension:optimizer | true |
| CUDA_gate_checks.stable-extension:scheduler | true |
| CUDA_gate_checks.stable-extension:rng | true |
| CUDA_gate_checks.stable-extension:sampler | true |
| CUDA_gate_checks.stable-extension:update | true |
| CUDA_gate_checks.stable-extension:tokens | true |
| CUDA_gate_checks.stable-extension:supervised_tokens | true |
| CUDA_gate_checks.stable-extension:body_bytes | true |
| CUDA_gate_checks.stable-extension:token_digest | true |
| CUDA_gate_checks.stable-extension:shard_manifest_sha256 | true |
| CUDA_gate_checks.stable-extension:implementation_sha256 | true |
| CUDA_gate_checks.stable-extension:lineage | true |
| CUDA_gate_checks.stable-extension:branch_updates | true |
| CUDA_gate_checks.stable-extension:branch_tokens | true |
| CUDA_gate_checks.stable-extension:finite | true |
| CUDA_gate_checks.stable-extension:history:loss | true |
| CUDA_gate_checks.stable-extension:history:lr | true |
| CUDA_gate_checks.stable-extension:history:token_digest | true |
| CUDA_gate_checks.stable-extension:history:tokens_seen | true |
| CUDA_gate_checks.stable:first_LR_no_jump | true |
| CUDA_gate_checks.stable:parent_cursor_advances_exactly64_blocks | true |
| CUDA_gate_checks.decay:version | true |
| CUDA_gate_checks.decay:spec | true |
| CUDA_gate_checks.decay:model_config | true |
| CUDA_gate_checks.decay:model | true |
| CUDA_gate_checks.decay:optimizer | true |
| CUDA_gate_checks.decay:scheduler | true |
| CUDA_gate_checks.decay:rng | true |
| CUDA_gate_checks.decay:sampler | true |
| CUDA_gate_checks.decay:update | true |
| CUDA_gate_checks.decay:tokens | true |
| CUDA_gate_checks.decay:supervised_tokens | true |
| CUDA_gate_checks.decay:body_bytes | true |
| CUDA_gate_checks.decay:token_digest | true |
| CUDA_gate_checks.decay:shard_manifest_sha256 | true |
| CUDA_gate_checks.decay:implementation_sha256 | true |
| CUDA_gate_checks.decay:lineage | true |
| CUDA_gate_checks.decay:branch_updates | true |
| CUDA_gate_checks.decay:branch_tokens | true |
| CUDA_gate_checks.decay:finite | true |
| CUDA_gate_checks.decay:history:loss | true |
| CUDA_gate_checks.decay:history:lr | true |
| CUDA_gate_checks.decay:history:token_digest | true |
| CUDA_gate_checks.decay:history:tokens_seen | true |
| verification_input_tokens | 524288 |
| scientific_total_tokens_seen | 1938227200 |
| scientific_target_tokens | 5000003584 |
| additional_scientific_budget_tokens | 3099983872 |

</details>

<details>
<summary>reports/phase6/base_ademamix_closeout_preparation.json — closeout_preparation_verified_not_scientific_completion</summary>

[原記録](../../reports/phase6/base_ademamix_closeout_preparation.json) ／ SHA256: `c603c72d50d66b99b6305cb94058c05aac40dc9e9ac9f5c090b6717270bb1000` ／ 5,815 bytes

| 原キー | 保存値 |
|---|---|
| status | "closeout_preparation_verified_not_scientific_completion" |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_context_mixing_runner_preparation_completion.json — CUDA_verified_same_gold100M_science_live</summary>

[原記録](../../reports/phase6/base_context_mixing_runner_preparation_completion.json) ／ SHA256: `97819f90874968c01cd56c3f036a3ce5e4af54e5f09ef120d6351962b3faacfa` ／ 2,464 bytes

| 原キー | 保存値 |
|---|---|
| status | "CUDA_verified_same_gold100M_science_live" |
| actual_CPU_runner_checks | 8 |
| CPU_runner_test_seconds | 2.55 |
| runner_tests_sha256 | "663b2ab6b252a7623de9d96f0db426354729346151b34ce923f360338d5369d2" |
| AST_sources_checked | 9 |
| durable_launchers_parse_checked | 2 |
| snapshot.status | "running" |
| snapshot.GPU_occupancy_seconds | 88.76185025900486 |
| snapshot.Base_complete | false |
| snapshot.memory_policy.visible_device_bytes | 25756696576 |
| snapshot.memory_policy.allocator_allowance_bytes | 23181026918 |
| snapshot.memory_policy.expected_worst_peak_bytes | 11078919680 |
| snapshot.completed_updates | 800 |
| snapshot.original_teachers | 4513754 |
| snapshot.CE_loss | 2.9107372760772705 |
| snapshot.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-context-mixing-comparison-20261007/context_mixing/checkpoint-00000750.pt" |
| live_closeout_guard.completion_archive_manifest_absent | true |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_gradient_accumulation_preparation.json — CPU_grouping_comparison_prepared_frozen_GPU_not_started</summary>

[原記録](../../reports/phase6/base_gradient_accumulation_preparation.json) ／ SHA256: `0350d7b8e2ac47da49336bdea0f5c376c6926351210ce812811b9341ffd67520` ／ 1,214 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_grouping_comparison_prepared_frozen_GPU_not_started" |
| actual_CPU_synthesis_seconds | 0.45036204099596944 |
| actual_GPU_seconds | 0 |
| CPU_tests | 3 |
| CPU_test_seconds | 5.07 |
| CPU_tests_path | "reports/phase6/base_gradient_accumulation_tests.xml" |
| initial_fixture_failure | "Old test fixture10000-teacher quota exhausted before16 grouped microbatches; new independent fixture100000-teacher quota permits required four grouped updates. Production goals and assertions unchanged." |
| PowerShell_syntax_passed | true |
| actual_control_teacher_tokens | 94160195 |
| actual_control_optimizer_updates | 10000 |
| candidate_optimizer_updates | 2500 |
| GPU_cap_seconds | 1992 |
| Base_complete | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_gradient_precision_initial_preparation_failure.json — CPU_preparation_reference_path_failure_before_config_UI_or_GPU</summary>

[原記録](../../reports/phase6/base_gradient_precision_initial_preparation_failure.json) ／ SHA256: `bfe0447faab50648677fabe631e809ced140f66ef012099e2eb1b8b09435ab7c` ／ 1,076 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_preparation_reference_path_failure_before_config_UI_or_GPU" |
| correction | "Bind to the actual native precision contract and validate all references before writing the payload. Reuse the exact same cached24 TRAIN records and same fixed long window; no new random draws or threshold/recipe/budget changes." |
| GPU_seconds | 0 |
| optimizer_updates | 0 |

</details>

<details>
<summary>reports/phase6/base_gradient_precision_initial_preparation_payload.json — None</summary>

[原記録](../../reports/phase6/base_gradient_precision_initial_preparation_payload.json) ／ SHA256: `ad40e86d8c5ec449b29c167d106f65c99e4b368b0d20840e703d55350e9498ec` ／ 103,948 bytes

| 原キー | 保存値 |
|---|---|
| original24_document_payload.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_embedding_gradient_payload.json" |
| original24_document_payload.sha256 | "4b592ba9e5ec64a664b249b07ade7dd4763db1e3e93a14c2a421a4efa2f23671" |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_closeout_preparation.json — paired_closeout_prepared_not_completion</summary>

[原記録](../../reports/phase6/base_headwise_gate_closeout_preparation.json) ／ SHA256: `908abdcb373b539e37b1631858b8b953559371e7341808dee96ccb6968043fc8` ／ 6,377 bytes

| 原キー | 保存値 |
|---|---|
| status | "paired_closeout_prepared_not_completion" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_parent_CPU_preparation_initial_failure.json — CPU_preparation_refused_incorrect_128_position_packet_assumption_before_forward</summary>

[原記録](../../reports/phase6/base_headwise_gate_parent_CPU_preparation_initial_failure.json) ／ SHA256: `2b7e6baf3be3299ea0975ffac9d6e9318105076d426730331f3f3b7641b459f3` ／ 987 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_preparation_refused_incorrect_128_position_packet_assumption_before_forward" |
| repair | "Validate against the original model context limit and retain all 24 original windows without cropping/resampling; CPU30s ceiling remains unchanged. No scientific configuration had been frozen." |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| model_code_changed_for_this_repair | false |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_preparation_v2.json — matched_headwise_gate_model_trainer_typed_evaluator_CPU_verified_GPU_unstarted</summary>

[原記録](../../reports/phase6/base_headwise_gate_preparation_v2.json) ／ SHA256: `29744d73eba32555a85ecfe468a31433eb4654d95a038d17bd7b07062dd20461` ／ 6,919 bytes

| 原キー | 保存値 |
|---|---|
| status | "matched_headwise_gate_model_trainer_typed_evaluator_CPU_verified_GPU_unstarted" |
| current_CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_CPU_tests_v2.xml" |
| current_CPU_tests.sha256 | "d3d733e852387cb2749e159cec8a9ab2b25085d8bf52c5572483630c8e9dfafd" |
| CPU_tests | 33 |
| model_checks | 16 |
| trainer_and_evaluation_checks | 17 |
| initial_failures.model_fixture.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_model_tests_initial.xml" |
| initial_failures.model_fixture.sha256 | "f056fc3b4d7714840e16bc29d3ddf16d860b3f256a7280fa4b228be2071dfd11" |
| initial_failures.trainer_static_validation.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_trainer_tests_initial_failure.xml" |
| initial_failures.trainer_static_validation.sha256 | "d1e6895d563506ce542b488d1282171f6179905230874db8b25d0ba6645bea2a" |
| initial_failures.preparation_input_assumption.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_parent_CPU_preparation_initial_failure.json" |
| initial_failures.preparation_input_assumption.sha256 | "2b7e6baf3be3299ea0975ffac9d6e9318105076d426730331f3f3b7641b459f3" |
| repair | "Static gate checkpoint validation incorrectly matched SwiGLU MLP gate_proj as well as the added attention gate. Restrict the predicate to .self_attn.gate_proj.weight. Keep static gates zero; add a successful static model/Adam roundtrip and both-arm full trainer resume checks. Model forward/conversion, optimizer, teachers, caps and quality policy unchanged. No scientific config had been frozen." |
| source_sha256.tests/test_base_headwise_gate_model.py | "5aedad7f5deaf530eb77a15a98b07f495da50608d6c2289c183683594964f91f" |
| source_sha256.tests/test_base_headwise_gate_trainer.py | "2511f0f3c74ea89c0482d8e5ab0ee0ebefccc3707fba8f2145305f286ee85745" |
| total_proposed_scientific_teachers | 200000000 |
| new_scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| total_GPU_ceiling_seconds | 9000 |
| probe_GPU_ceiling_seconds | 180 |
| scientific_configuration_frozen | false |
| scientific_started | false |
| same_original_full_sampler_and_CE_verified | true |
| fullstate_CPU4_vs_2_save_2_both_arms_verified | true |
| partial_update_save_continue_refused | true |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_workflow_preparation.json — paired_gate_durable_probe_science_review_implemented_CUDA_pending</summary>

[原記録](../../reports/phase6/base_headwise_gate_workflow_preparation.json) ／ SHA256: `4eec9292dbeda206c5c49d8a86d507eccb2db7a582d50de40ba8d6f08e443c49` ／ 954 bytes

| 原キー | 保存値 |
|---|---|
| CPU_tests_existing | 33 |
| Base_adopted | false |
| status | "paired_gate_durable_probe_science_review_implemented_CUDA_pending" |
| new_scientific_teacher_tokens | 0 |
| CPU_run_tests | 7 |
| CPU_workflow_tests | 12 |
| new_GPU_seconds | 0 |
| Base_complete | false |
| initial_run_collection_failure | "unmatched closing parenthesis before GPU; corrected; original XML preserved" |

</details>

<details>
<summary>reports/phase6/base_hq_acceptance_review.json — unseen64_content_failed_fixed_extractor_branch_closed</summary>

[原記録](../../reports/phase6/base_hq_acceptance_review.json) ／ SHA256: `4baa195698d639691b73494491c3afcb9db7173ea123a3dba1516f45db0f09ad` ／ 77,663 bytes

| 原キー | 保存値 |
|---|---|
| status | "unseen64_content_failed_fixed_extractor_branch_closed" |
| sample_sha256 | "6451ee32fa0d656812c72361d9a895f48ead0e99c17e4b08af2261a577c5c00f" |
| producer_identity.status | "complete" |
| producer_identity.scientific_teacher_tokens | 0 |
| producer_identity.GPU_seconds | 0 |
| producer_identity.remote_bytes | 14544548 |
| producer_identity.wall_seconds | 46.308177419996355 |
| producer_identity.updated_at | "2026-10-06T15:45:06.009444Z" |
| rubric.grammar | "2 generally grammatical prose or legitimate structured forms;1 recurring broken constructions;0 unintelligible" |
| rubric.coherence | "2 connected topic/progression with locally understandable references;1 unresolved references, incompatible events or mixed fragments;0 unrelated scraps" |
| summary.documents | 64 |
| summary.grammar2 | 57 |
| summary.coherence2 | 54 |
| summary.content_acceptance_passed | false |
| summary.issue_flags.empty_promised_section | 1 |
| summary.issue_flags.empty_examples | 1 |
| summary.issue_flags.closed_list | 1 |
| summary.issue_flags.construction_progress_note | 1 |
| summary.issue_flags.picture_captions | 1 |
| summary.issue_flags.rhetorical_repetition | 1 |
| source_accepted_for_learning | false |
| fixed_extractor_branch_closed | true |
| new_prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| Base_complete | false |
| protected_test_bodies_read | false |
| CPU_seconds | 0.007077916000000073 |
| decision | "Reject this frozen article extraction branch. Retain all64 outcomes; no reroll, post-outcome selector/threshold tuning or large training from these candidates." |
| limitations | "Four eligible source groups, not a global quality rate. Nonblind ratings are not independent quality or factual certification. Near-family/fixed-suite exclusion and useful large-pool supply remain unmeasured. Original/selected exact byte checks do not prove semantic completion; individual readings supply that evidence. A failed source screen does not establish a10M model capacity limit." |

</details>

<details>
<summary>reports/phase6/base_hq_acceptance_sample.json — fixed_unseen64_article_candidates_unreviewed</summary>

[原記録](../../reports/phase6/base_hq_acceptance_sample.json) ／ SHA256: `ae9d17693b130780c6fc0337a6601a303d9d1556f7ad8ac883aef0e69bf1ff27` ／ 11,383 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_unseen64_article_candidates_unreviewed" |
| seed | 2026100731 |
| sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/base-hq-acceptance-20261007/source-sample.json" |
| sample.sha256 | "6451ee32fa0d656812c72361d9a895f48ead0e99c17e4b08af2261a577c5c00f" |
| exclusions.structural_rejection:no_sentence_closed_article_body | 22 |
| body_tokens_in_inspection | 46463 |
| original_body_UTF8_bytes | 171664 |
| remote_bytes | 14544548 |
| wall_seconds | 46.31825581000885 |
| CPU_seconds | 0.6244294789999998 |
| protected_test_bodies_read | false |
| source_accepted | false |
| Base_complete | false |
| new_prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| limitations | "This sample is conditioned on the frozen structural selector and old indexed exclusions. It measures retained-source suitability, not whole-corpus quality, learned quality or global near-family independence. Four uniformly selected source files with one random group each. No raw-versus-cleaned training effect or facts certification yet." |

</details>

<details>
<summary>reports/phase6/base_hq_article_calibration.json — single_contiguous_article_extractor_calibrated_not_accepted</summary>

[原記録](../../reports/phase6/base_hq_article_calibration.json) ／ SHA256: `5b0156022a20e23859f1c066c5b81b0b8769d1c692f86133459acc14ceade21a` ／ 20,318 bytes

| 原キー | 保存値 |
|---|---|
| status | "single_contiguous_article_extractor_calibrated_not_accepted" |
| original_sample_sha256 | "c2e5a885bb87bedcc0adbc8a3f52bf0d13608285e502819957cfde21b8142a8a" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| retained_body_tokens | 32494 |
| retained_original_UTF8_bytes | 119356 |
| rejection_reasons.no_sentence_closed_article_body | 19 |
| rejection_reasons.whole_article_token_length | 3 |
| rejection_reasons.site_operation_body | 5 |
| rejection_reasons.many_extraction_word_breaks | 2 |
| source_documents_split_into_sentences | false |
| CPU_seconds | 0.02396301500266418 |
| CPU_limit_seconds | 30 |
| remote_bytes | 0 |
| new_prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| source_accepted | false |
| Base_complete | false |
| limitations | "Developed after reading the64 raw calibration sources; output count is a structural supply observation, not a held-out pass or global unique-corpus estimate. Formal metadata/genre validity is separate from target-style. Sentence-end detection cannot certify semantic context or truth. Old-family near overlap and fixed eval suite exclusion remain pending. No source/beta/epoch/LR/checkpoint rescue of failed small CE/DPO/news runs." |

</details>

<details>
<summary>reports/phase6/base_hq_content_completion.json — all64_initial_and_unseen_content_complete_frozen_extractor_rejected</summary>

[原記録](../../reports/phase6/base_hq_content_completion.json) ／ SHA256: `0c2f147b973cbd95fb760d38a4dc2d0234050b27ca40f19505464fe69218914a` ／ 12,135 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_initial_and_unseen_content_complete_frozen_extractor_rejected" |
| initial_source_summary.documents | 64 |
| initial_source_summary.grammar2 | 58 |
| initial_source_summary.coherence2 | 53 |
| initial_source_summary.terminal_kinds.empty_heading | 4 |
| initial_source_summary.terminal_kinds.closed_quote | 1 |
| initial_source_summary.terminal_kinds.photo_caption | 1 |
| initial_source_summary.terminal_kinds.closed_list_item | 1 |
| initial_source_summary.issue_flags.encyclopedia_empty_sections | 2 |
| initial_source_summary.issue_flags.encyclopedia_notice_empty_sections | 1 |
| initial_source_summary.issue_flags.encyclopedia_empty_tail | 1 |
| initial_source_summary.issue_flags.encyclopedia_empty_middle_sections | 1 |
| initial_source_summary.issue_flags.intentional_rhetorical_repetition | 1 |
| initial_source_summary.issue_flags.travel_note | 1 |
| initial_source_summary.issue_flags.intentional_summary_repetition | 1 |
| initial_source_summary.issue_flags.glossary | 1 |
| initial_source_summary.natural_complete_prose_and_coherent | 22 |
| initial_source_individual_notes_bound | true |
| calibration_body_tokens | 32494 |
| CPU_tests | "3 passed in0.03s; acceptance scripts compiled before frozen actual retrieval" |
| unseen_acceptance_sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/base-hq-acceptance-20261007/source-sample.json" |
| unseen_acceptance_sample.sha256 | "6451ee32fa0d656812c72361d9a895f48ead0e99c17e4b08af2261a577c5c00f" |
| unseen_acceptance_content_reviewed | 0 |
| source_accepted | false |
| Base_complete | false |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| training_prepared_tokens | 0 |
| acceptance_actual_process_absent | true |
| current_original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| current_original_UI.training_tokens | 10000007168 |
| files.scripts/review_base_hq_source.py.bytes | 6205 |
| files.scripts/base_hq_article_body.py.bytes | 3753 |
| files.scripts/calibrate_base_hq_article_body.py.bytes | 4755 |
| files.scripts/prepare_base_hq_acceptance.py.sha256 | "4d33523524dfb3c9dfe205e1602d0d309434bcd82076a77175026243b6c428ac" |
| files.scripts/prepare_base_hq_acceptance.py.bytes | 4770 |
| files.scripts/inspect_base_hq_acceptance.py.sha256 | "59417a7d10af510aa509fee26ccb69220f3a473600878ecd8dfeeb3925bacd6d" |
| files.scripts/inspect_base_hq_acceptance.py.bytes | 12087 |
| files.tests/test_base_hq_article_body.py.sha256 | "9c656570bf4527b0104babcd8a48666251fe7ff7ed35973fd1e6c49e251aa4c8" |
| files.tests/test_base_hq_article_body.py.bytes | 1685 |
| files.configs/phase6/base_hq_acceptance.json.sha256 | "ac2acc4e7f17c6a2bf21b6d46282bbe9857d2205f16ea278ca07e6242afb3b4d" |
| files.configs/phase6/base_hq_acceptance.json.bytes | 4897 |
| files.reports/phase6/base_hq_source_observations.tsv.bytes | 13470 |
| files.reports/phase6/base_hq_source_content_review.json.bytes | 56217 |
| files.reports/phase6/base_hq_article_calibration.json.bytes | 20318 |
| files.reports/phase6/base_hq_article_tests.xml.sha256 | "b574747c47094cdeb6e104eaa235f492c66bc1dd7140fc4d20f97039fe8cb8eb" |
| files.reports/phase6/base_hq_article_tests.xml.bytes | 663 |
| files.reports/phase6/base_hq_acceptance_sample.json.sha256 | "ae9d17693b130780c6fc0337a6601a303d9d1556f7ad8ac883aef0e69bf1ff27" |
| files.reports/phase6/base_hq_acceptance_sample.json.bytes | 11383 |
| files.reports/phase6/base-hq-content-20261007/acceptance-job.json.sha256 | "bf31ed8a0dc60f7dfd7895af9b9b65081f38dcb8096990c74fe3cf606505695a" |
| files.reports/phase6/base-hq-content-20261007/acceptance-job.json.bytes | 525 |
| files.reports/phase6/base-hq-content-20261007/acceptance-index.json.sha256 | "6ad220290ebc7fe20a291adf7716c14c1eff98035614bd2844694f0b7698a244" |
| files.reports/phase6/base-hq-content-20261007/acceptance-index.json.bytes | 52297 |
| files.scripts/review_base_hq_acceptance.py.sha256 | "fad1b3ac1444a0b99ee8bdac522e6dc0ce597f4a330f071e37af53930f6f167b" |
| files.scripts/review_base_hq_acceptance.py.bytes | 8085 |
| files.reports/phase6/base_hq_acceptance_observations.tsv.sha256 | "f236774563a41dee82c746cd835956736923f7de7b061d07ddfb674bc0ef9e09" |
| files.reports/phase6/base_hq_acceptance_observations.tsv.bytes | 16802 |
| files.reports/phase6/base_hq_acceptance_review.json.sha256 | "4baa195698d639691b73494491c3afcb9db7173ea123a3dba1516f45db0f09ad" |
| files.reports/phase6/base_hq_acceptance_review.json.bytes | 77663 |
| archive.bytes | 78872 |
| limitations | "全64の非blind Codex source適性判定。原親/span一致と個別理由を保存。41/64&lt;54なので固定抽出branch不採用。学習済みBaseの精度・全球品質率・10M容量限界・事実保証ではない。near-family/suite除外と新固有教材の供給量は未測定。" |
| unseen_content_summary.documents | 64 |
| unseen_content_summary.grammar2 | 57 |
| unseen_content_summary.coherence2 | 54 |
| unseen_content_summary.content_acceptance_passed | false |
| unseen_content_summary.issue_flags.empty_promised_section | 1 |
| unseen_content_summary.issue_flags.empty_examples | 1 |
| unseen_content_summary.issue_flags.closed_list | 1 |
| unseen_content_summary.issue_flags.construction_progress_note | 1 |
| unseen_content_summary.issue_flags.picture_captions | 1 |
| unseen_content_summary.issue_flags.rhetorical_repetition | 1 |
| fixed_extractor_branch_closed | true |
| content_acceptance_passed | false |

</details>

<details>
<summary>reports/phase6/base_hq_feasibility_completion.json — source_access_footer_selected_column_feasibility_complete_content_pending</summary>

[原記録](../../reports/phase6/base_hq_feasibility_completion.json) ／ SHA256: `1d1e5f031a2650d4047ca01f251b69460c8055ae8e9cbae9be0b8f8879d21fc7` ／ 4,192 bytes

| 原キー | 保存値 |
|---|---|
| status | "source_access_footer_selected_column_feasibility_complete_content_pending" |
| native_sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007/source-sample.json" |
| native_sample.sha256 | "c2e5a885bb87bedcc0adbc8a3f52bf0d13608285e502819957cfde21b8142a8a" |
| fixed_sample_content_reviewed | 0 |
| source_accepted | false |
| Base_complete | false |
| prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| measured_wall_seconds.metadata | 4.070244378992356 |
| measured_wall_seconds.footer | 5.505988374003209 |
| measured_wall_seconds.sample | 30.97790597198764 |
| sample_remote_bytes | 13793569 |
| CPU_tests | "3 passed in0.45seconds" |
| files.scripts/inspect_base_hq_source.py.bytes | 4623 |
| files.scripts/inspect_base_hq_footer.py.bytes | 3539 |
| files.scripts/inspect_base_hq_sample.py.sha256 | "0f015d551aed82a780f82753ede388177e1f8aea656d450389076269494256bd" |
| files.scripts/inspect_base_hq_sample.py.bytes | 10168 |
| files.scripts/remote_parquet_ranges.py.bytes | 3396 |
| files.tests/test_remote_parquet_ranges.py.sha256 | "f437d9ab9eaa483f53441fcfd80a3366a327318d6de73ecbfe6c4b2344ada169" |
| files.tests/test_remote_parquet_ranges.py.bytes | 2563 |
| files.reports/phase6/base_hq_source_feasibility.json.bytes | 2054 |
| files.reports/phase6/base_hq_footer_inspection.json.bytes | 105491 |
| files.reports/phase6/base_hq_source_sample.json.sha256 | "fd5c943ff9cd18a2fcf6de360150de29b6ee771bc09509d58a046f25935c837a" |
| files.reports/phase6/base_hq_source_sample.json.bytes | 8275 |
| files.reports/phase6/base_hq_range_tests.xml.sha256 | "e72c9dc07787d64d9a7efee0836c9dc5d2673f817ac280b47f5857c4fb690225" |
| files.reports/phase6/base_hq_range_tests.xml.bytes | 618 |
| files.reports/phase6/base-hq-feasibility-20261007/repository.json.bytes | 256745 |
| files.reports/phase6/base-hq-feasibility-20261007/README.md.bytes | 9609 |
| files.reports/phase6/base-hq-feasibility-20261007/sample-plan.json.sha256 | "e66295e0829e9b092f7ebb4c888951588e85f3e35c9572796b7af1e93e0af627" |
| files.reports/phase6/base-hq-feasibility-20261007/sample-plan.json.bytes | 1172 |
| files.reports/phase6/base-hq-feasibility-20261007/sample-index.json.sha256 | "9c6d4066f5b003a53e601828b3927d5a914e35bbc6275f1fe384a4895e1c3dea" |
| files.reports/phase6/base-hq-feasibility-20261007/sample-index.json.bytes | 40181 |
| archive.bytes | 54743 |
| active_GPU_training_job | null |
| current_original_UI.HTTP_checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| current_original_UI.training_tokens | 10000007168 |

</details>

<details>
<summary>reports/phase6/base_hq_footer_inspection.json — pinned_footer_only_observed</summary>

[原記録](../../reports/phase6/base_hq_footer_inspection.json) ／ SHA256: `7978ffa6ab2567708b68db64495c35d5c96d967e3d996aadb94493bfdc0e5b0d` ／ 105,491 bytes

| 原キー | 保存値 |
|---|---|
| status | "pinned_footer_only_observed" |
| file_bytes | 1007743807 |
| remote_bytes | 412484 |
| wall_seconds | 5.505988374003209 |
| prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| Base_complete | false |
| limits.remote_bytes | 4194304 |
| limits.wall_seconds | 30 |

</details>

<details>
<summary>reports/phase6/base_hq_source_content_review.json — all64_original_HQ_source_bodies_individually_read</summary>

[原記録](../../reports/phase6/base_hq_source_content_review.json) ／ SHA256: `516a129ad009e70fb2e215ce1abd7091060a2bf11c45f01ea80e79e2f37df2e5` ／ 56,217 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_original_HQ_source_bodies_individually_read" |
| sample_sha256 | "c2e5a885bb87bedcc0adbc8a3f52bf0d13608285e502819957cfde21b8142a8a" |
| rubric.grammar | "0 unintelligible;1 recurring broken constructions/extraction damage;2 generally grammatical prose or legitimate structured forms" |
| rubric.coherence | "0 unrelated scraps;1 incoherent entity mapping or site fragments without one body;2 connected topic and progression, including structured lists/poems/questions" |
| summary.documents | 64 |
| summary.grammar2 | 58 |
| summary.coherence2 | 53 |
| summary.terminal_kinds.empty_heading | 4 |
| summary.terminal_kinds.closed_quote | 1 |
| summary.terminal_kinds.photo_caption | 1 |
| summary.terminal_kinds.closed_list_item | 1 |
| summary.issue_flags.encyclopedia_empty_sections | 2 |
| summary.issue_flags.encyclopedia_notice_empty_sections | 1 |
| summary.issue_flags.encyclopedia_empty_tail | 1 |
| summary.issue_flags.encyclopedia_empty_middle_sections | 1 |
| summary.issue_flags.intentional_rhetorical_repetition | 1 |
| summary.issue_flags.travel_note | 1 |
| summary.issue_flags.intentional_summary_repetition | 1 |
| summary.issue_flags.glossary | 1 |
| summary.natural_complete_prose_and_coherent | 22 |
| source_accepted_for_learning | false |
| Base_complete | false |
| prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| protected_test_bodies_read | false |
| CPU_seconds | 0.0018352780025452375 |
| decision | "Do not adopt unmodified HQ documents solely from the published classifier score. Many coherent bodies coexist with truncated reviews, UI/booking text, empty headings and mixed scraps. The actual fixed sample supports a bounded original-prose extraction calibration, followed by new untouched source-family acceptance and unique-supply measurement before any controlled training." |
| limitations | "A chosen eligible sample from four groups of one file, after known old exact/URL exclusions; not a global corpus estimate, independent seed, trained model quality or near-family protection proof. No acceptance threshold was predeclared for this HQ content review; descriptive counts are not a retrospective pass. Facts, medical/legal instructions, religious/political claims are not certified by linguistic ratings. Shared ancestry/global near overlap remain pending." |

</details>

<details>
<summary>reports/phase6/base_hq_source_feasibility.json — public_Japanese_HQ_metadata_and_range_observed</summary>

[原記録](../../reports/phase6/base_hq_source_feasibility.json) ／ SHA256: `ae419bffd89ebab34a883d1061ff95df3dae0920fa3de6eae988594d21078b0b` ／ 2,054 bytes

| 原キー | 保存値 |
|---|---|
| status | "public_Japanese_HQ_metadata_and_range_observed" |
| range_HTTP_status | 206 |
| wall_seconds | 4.070244378992356 |
| prepared_training_tokens | 0 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| limitations | "Same FineWeb2 ancestry as current Edu corpus; global source/test overlap must be bound using existing IDs/protected family registries before any learning. Scored HQ documents may still be noisy; source suitability and additional native-token supply are unmeasured." |

</details>

<details>
<summary>reports/phase6/base_hq_source_sample.json — fixed64_TRAIN_candidate_source_sample_unreviewed</summary>

[原記録](../../reports/phase6/base_hq_source_sample.json) ／ SHA256: `fd5c943ff9cd18a2fcf6de360150de29b6ee771bc09509d58a046f25935c837a` ／ 8,275 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed64_TRAIN_candidate_source_sample_unreviewed" |
| sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007/source-sample.json" |
| sample.sha256 | "c2e5a885bb87bedcc0adbc8a3f52bf0d13608285e502819957cfde21b8142a8a" |
| seed | 2026100723 |
| protected_test_bodies_read | false |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| body_tokens_in_inspection | 67194 |
| body_bytes_in_inspection | 238511 |
| native_body_tokens_min | 89 |
| native_body_tokens_max | 10681 |
| native_body_tokens_mean | 1049.90625 |
| first_file_gross_token_extrapolation | 87998942.25 |
| extrapolation_limit | "Mean of64 eligible URL families in four groups of one file; selected rather than all rows, no correction for old overlap/quality/split/near duplicates. Not accepted unique supply or a representative global corpus estimate." |
| remote_bytes | 13793569 |
| wall_seconds | 30.97790597198764 |
| CPU_seconds | 0.45643153499999967 |
| prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| Base_complete | false |
| source_accepted | false |

</details>

<details>
<summary>reports/phase6/base_label_smoothing_preparation.json — native_smoothing_trainer_CPU_protocol_verified_CUDA_not_started</summary>

[原記録](../../reports/phase6/base_label_smoothing_preparation.json) ／ SHA256: `59610e1ed583590075e9e1cfadd43eb40feea2616cc638f053011333e18df658` ／ 2,819 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_smoothing_trainer_CPU_protocol_verified_CUDA_not_started" |
| sources.tests/test_base_label_smoothing.py | "7dc18c1bb9b71674c6d5ad2c2924d5b05551dd147a9141783e34681c0758fdbe" |
| sources.tests/test_base_label_smoothing_trainer.py | "49e0939a59358e91dcde8dd1aeeea28116b663487ef7bf0f5039e67d599e9498" |
| sources.reports/phase6/base_label_smoothing_tests.xml | "c22d731fdf3f8c32dc1e68cb97f8fb9952b39c666738057504134e4f46d424be" |
| sources.reports/phase6/base_label_smoothing_trainer_tests.xml | "8430fed72364ae304693ba5cd948ef761aa89ba1a51a7afcfbc4faed2d0745bc" |
| CPU_tests.reports/phase6/base_label_smoothing_tests.xml.tests | 3 |
| CPU_tests.reports/phase6/base_label_smoothing_tests.xml.reported_suite_seconds | 1.377 |
| CPU_tests.reports/phase6/base_label_smoothing_trainer_tests.xml.tests | 4 |
| CPU_tests.reports/phase6/base_label_smoothing_trainer_tests.xml.reported_suite_seconds | 3.35 |
| CPU_protocol | "Actual tiny-model native initialized weights/logits/tied/RNG unchanged, identical source/CE/EOS/input/physical/digest/full sampler versus CE, smoothed gradient formula and mask, all state/history continuous4 versus save/resume2+2 exact, changed/old recipe and eval-learning refusal." |
| actual_CUDA_probe_passed | false |
| new_GPU_seconds | 0 |
| new_scientific_CE_teachers | 0 |
| new_original_training_tokens | 0 |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_native_hint_CPU_preparation.json — native_hint_CPU13_passed_GPU_workflow_not_yet_implemented</summary>

[原記録](../../reports/phase6/base_native_hint_CPU_preparation.json) ／ SHA256: `eea3bb1abde41977a358c03515b5c0308cbf48b29f204d389c6b4ad61b9a0a96` ／ 2,953 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_hint_CPU13_passed_GPU_workflow_not_yet_implemented" |
| recipe.loss | "sum_one_minus_FP32_unit_feature_dot_over_all_original_gold_positions" |
| recipe.teacher_frozen_eval | true |
| recipe.teacher_forward | "original_embedding_and_first_middle_blocks_no_norm_or_head" |
| tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/tests/test_base_native_hint_trainer.py" |
| tests.sha256 | "bb56fe5c7aae264c0494efe9f85b05a36851c28b3d04a8111fc71b6264bf052a" |
| CPU_result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_hint_trainer_tests.xml" |
| CPU_result.sha256 | "3c39add3d35ebc40050732820f76213f948782ce94a0269b10b0682384d2e400" |
| CPU_result.passed | 13 |
| CPU_result.seconds | 3.669 |
| initial_failure.tests | 13 |
| initial_failure.failures | 2 |
| initial_failure.fixture_only | true |
| initial_failure.test_source.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_hint_tests_initial_failure.py" |
| initial_failure.test_source.sha256 | "1152c65cc8b7d3e37ee94b8453a50646075bc031a9f4aab1d580d58b66676c69" |
| initial_failure.XML.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_hint_trainer_tests_initial_failure.xml" |
| initial_failure.XML.sha256 | "460fb2c62d431a63d1a5c7f5f5a8d8395bf621ca353936735c89a539d09cbd38" |
| CPU_test_seconds_including_failed_run | 6.931 |
| GPU_seconds | 0 |
| scientific_original_gold_tokens | 0 |
| scientific_hint_positions | 0 |
| Base_complete | false |
| Base_adopted | false |
| old_dense_KD_condition_closed | true |
| external_Qwen_transfer_branch_closed | true |

</details>

<details>
<summary>reports/phase6/base_native_hint_closeout_preparation.json — closeout_preparation_verified_not_scientific_completion</summary>

[原記録](../../reports/phase6/base_native_hint_closeout_preparation.json) ／ SHA256: `3b332f8839be17f2ec4e38f931a997c035955934d2ae8e93832c09e5dcf009ca` ／ 5,156 bytes

| 原キー | 保存値 |
|---|---|
| status | "closeout_preparation_verified_not_scientific_completion" |
| GPU_seconds | 0 |
| initial_verifier_failure | "Fixture shared candidate/prior path and changed both reads, so mismatch check could not reject. Fix first candidate read only; production closeout unchanged." |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_native_teacher_KD_science_closeout_preparation.json — closeout_preparation_verified_not_scientific_completion</summary>

[原記録](../../reports/phase6/base_native_teacher_KD_science_closeout_preparation.json) ／ SHA256: `0b1ecee472b9ae9984c96e8b5f5980b60976b19724a2aff3316a19481c46ba55` ／ 810 bytes

| 原キー | 保存値 |
|---|---|
| status | "closeout_preparation_verified_not_scientific_completion" |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_output_mixture_closeout_preparation.json — closeout_prepared_not_completion</summary>

[原記録](../../reports/phase6/base_output_mixture_closeout_preparation.json) ／ SHA256: `a2c8f3c7fd53e37d596c9a8c7e56e98efec9babcdaff4b1c9e04c60fd220bcf2` ／ 7,593 bytes

| 原キー | 保存値 |
|---|---|
| status | "closeout_prepared_not_completion" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_output_mixture_preparation.json — new_paired_output_mixture_CPU_verified_GPU_unstarted</summary>

[原記録](../../reports/phase6/base_output_mixture_preparation.json) ／ SHA256: `6ad54828d1da8298b3b8b48e8a13ee65f8324b7c62371b166c9b14e24a3a9950` ／ 12,421 bytes

| 原キー | 保存値 |
|---|---|
| status | "new_paired_output_mixture_CPU_verified_GPU_unstarted" |
| policy.initialization_seed | 2026100741 |
| policy.additional_decoder_passes | 0 |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_output_mixture_CPU_tests.xml" |
| CPU_tests.sha256 | "92246e00928ca238974b28b05d50dfa7ce7eae29d1a8edbae14209e39d253df7" |
| CPU_test_count | 16 |
| CPU_seconds | 2.215998693000074 |
| source_sha256.tests/test_base_output_mixture.py | "28b22962d833ba2158b2c05c69fd3c409fe4d6cd3bc75196e8d48c6adc1a751e" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| GPU_seconds | 0 |
| new_scientific_teacher_tokens | 0 |
| Base_complete | false |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_CPU_preparation.json — new_fresh_parallel_residual_CPU_prepared_no_GPU_science</summary>

[原記録](../../reports/phase6/base_parallel_residual_CPU_preparation.json) ／ SHA256: `18ef69c95ee157f4d5d3ffb379f3d08e961c5a1abaff92aca498d280b73814e2` ／ 2,611 bytes

| 原キー | 保存値 |
|---|---|
| status | "new_fresh_parallel_residual_CPU_prepared_no_GPU_science" |
| source_sha256.tests/test_base_parallel_residual_model.py | "f049ebadc80877d5ec30a1dca1c96d7b3914150db37b61685f7b9d5662bea175" |
| source_sha256.tests/test_base_parallel_residual_trainer.py | "a7c185a1407f55b7c9a253191a93be6a6601dc0ddc4470cc5e982959691183ef" |
| source_sha256.tests/test_base_parallel_residual_evaluation.py | "4de71a5906d8e47912e8ebdeeea18565db57ebda20bcbc9f55c40c508fbb5194" |
| model_tests | 11 |
| model_seconds | 1.47 |
| trainer_tests | 11 |
| trainer_seconds | 4.25 |
| typed_evaluation_tests | 3 |
| evaluation_seconds | 1.4 |
| total_current_CPU_tests | 25 |
| initial_combined_CPU22_preserved | "reports/phase6/base_parallel_residual_CPU_tests.xml" |
| current_tests | ["reports/phase6/base_parallel_residual_model_tests.xml", "reports/phase6/base_parallel_residual_trainer_tests.xml", "reports/phase6/base_parallel_residual_evaluation_tests.xml"] |
| durable_GPU_probe_implemented | false |
| scientific_runner_implemented | false |
| new_GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| prospective_total_GPU_cap_seconds | 86400 |
| actual_GPU_forecast | null |
| RNG_test_strengthened | "Capture sequential initialization RNG before constructing the parallel arm; current11 trainer tests rerun successfully" |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_closeout_preparation.json — closeout_prepared_not_completion</summary>

[原記録](../../reports/phase6/base_parallel_residual_closeout_preparation.json) ／ SHA256: `db196a6a9340db75904d7d39ec62d286dc5c555970cf2d8c92045d399fb01d47` ／ 9,319 bytes

| 原キー | 保存値 |
|---|---|
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_closeout_tests.xml" |
| CPU_tests.sha256 | "cf0c18b36dcf82136de3059c54e61caf05ea8fc14ddbada8ecb859726c044bb7" |
| test_source.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/tests/test_base_parallel_residual_closeout.py" |
| test_source.sha256 | "21fe3fdba4c49fb5da9371a9fea1a2979a28556a9ac98f65f1e8b35e7fb4794d" |
| status | "closeout_prepared_not_completion" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_probe_preparation.json — own_durable_CUDA_probe_prepared_GPU0</summary>

[原記録](../../reports/phase6/base_parallel_residual_probe_preparation.json) ／ SHA256: `181171892d8bb37baf1c810ff07bfa7d4de3f17db2720ccfb7dabf814b466c6c` ／ 974 bytes

| 原キー | 保存値 |
|---|---|
| prospective_total_GPU_cap_seconds | 86400 |
| Base_complete | false |
| durable_GPU_probe_implemented | true |
| prospective_scientific_gold_each | 2000000000 |
| workflow_tests | "reports/phase6/base_parallel_residual_workflow_tests.xml" |
| own_probe_GPU_cap_seconds | 180 |
| workflow_tests_seconds | 1.4 |
| scientific_runner_implemented | false |
| new_GPU_seconds | 0 |
| current_existing_CPU_tests | 25 |
| status | "own_durable_CUDA_probe_prepared_GPU0" |
| scientific_gold_tokens | 0 |
| new_workflow_CPU_tests | 17 |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_review_preparation.json — actual_cached_control_API_and_live_final_guard_passed</summary>

[原記録](../../reports/phase6/base_residual_dropout_review_preparation.json) ／ SHA256: `b4ce032f55625f4bea74265a5b9790d772df2b93f9997444f36503e51905a6bc` ／ 6,942 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_cached_control_API_and_live_final_guard_passed" |
| CPU_protocol_checks | 18 |
| CPU_protocol_seconds | 2.43 |
| CPU_interface_and_live_guard_seconds | 2.074969239998609 |
| new_GPU_seconds | 0 |
| new_teacher_tokens | 0 |
| scientific_results_read | false |
| scientific_actual_identity.pid | 689085 |
| scientific_actual_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| scientific_actual_identity.start_ticks | "19897021" |
| scientific_process_alive_verified | true |
| scientific_config_sha256 | "bd36050f4ec23798186e020098de54cbffab16f36554c6c0dbc064192875051a" |
| tests_xml_sha256 | "0a8facdc00c824b796c7ee8ee300742d8febbad919db950dd1a196f87f4a9d11" |
| CE_cached_summary.BPB | 0.998487162513845 |
| CE_cached_summary.rates.eos | 19 |
| CE_cached_summary.rates.repetition | 45 |
| CE_cached_summary.rates.unicode_failure | 0 |
| CE_cached_summary.rates.role_leak | 0 |
| CE_cached_summary.rates.empty | 0 |
| CE_cached_summary.grammar2 | 44 |
| CE_cached_summary.relevance2 | 25 |
| CE_cached_summary.coherent | 2 |
| CE_cached_summary.appropriate | 2 |
| CE_cached_summary.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| common256_BPB_identity.point | 0.0 |
| common256_BPB_identity.ci95 | [0.0, 0.0] |
| common256_BPB_identity.documents | 256 |
| common256_BPB_identity.common_bytes | 472055 |
| common256_BPB_identity.control_BPB | 0.998487162513845 |
| common256_BPB_identity.target_BPB | 0.998487162513845 |
| common256_BPB_identity.relative_ratio | 1.0 |
| common256_BPB_identity.degradation_ci_lower_above0 | false |
| common256_BPB_identity.seed | 42 |
| common256_BPB_identity.repetitions | 2000 |
| common256_BPB_identity.direction | "target minus adopted Base; positive means worse" |
| common256_BPB_identity.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact192_semantic_identity.candidate_minus_control.seed | 42 |
| exact192_semantic_identity.candidate_minus_control.repetitions | 2000 |
| exact192_semantic_identity.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact192_semantic_identity.exact_content_pair_clusters | 96 |
| exact192_semantic_identity.new_acceptance_gate | false |
| existing_semantic_summary.exact_content_pair_clusters | 96 |
| existing_semantic_summary.original_nominal_accuracy.point | 0.625 |
| existing_semantic_summary.original_nominal_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| existing_semantic_summary.original_nominal_accuracy.units | 96 |
| existing_semantic_summary.original_nominal_accuracy.examples | 192 |
| existing_semantic_summary.original_nominal_accuracy.unit | "family/prompt" |
| existing_semantic_summary.original_nominal_accuracy.seed | 42 |
| existing_semantic_summary.original_nominal_accuracy.repetitions | 2000 |
| existing_semantic_summary.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.content_cluster_accuracy.point | 0.625 |
| existing_semantic_summary.content_cluster_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| existing_semantic_summary.content_cluster_accuracy.units | 96 |
| existing_semantic_summary.content_cluster_accuracy.examples | 192 |
| existing_semantic_summary.content_cluster_accuracy.unit | "family/prompt" |
| existing_semantic_summary.content_cluster_accuracy.seed | 42 |
| existing_semantic_summary.content_cluster_accuracy.repetitions | 2000 |
| existing_semantic_summary.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.both_contexts_hard_correct.point | 0.2708333333333333 |
| existing_semantic_summary.both_contexts_hard_correct.ci95 | [0.1875, 0.3645833333333333] |
| existing_semantic_summary.both_contexts_hard_correct.units | 96 |
| existing_semantic_summary.both_contexts_hard_correct.examples | 96 |
| existing_semantic_summary.both_contexts_hard_correct.unit | "family/prompt" |
| existing_semantic_summary.both_contexts_hard_correct.seed | 42 |
| existing_semantic_summary.both_contexts_hard_correct.repetitions | 2000 |
| existing_semantic_summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.causality.seed | 42 |
| existing_semantic_summary.categories.causality.repetitions | 2000 |
| existing_semantic_summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.comparison.seed | 42 |
| existing_semantic_summary.categories.comparison.repetitions | 2000 |
| existing_semantic_summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.coreference.seed | 42 |
| existing_semantic_summary.categories.coreference.repetitions | 2000 |
| existing_semantic_summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.negation.seed | 42 |
| existing_semantic_summary.categories.negation.repetitions | 2000 |
| existing_semantic_summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.quantity.seed | 42 |
| existing_semantic_summary.categories.quantity.repetitions | 2000 |
| existing_semantic_summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| existing_semantic_summary.categories.time.seed | 42 |
| existing_semantic_summary.categories.time.repetitions | 2000 |
| existing_semantic_summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| initial_CPU_preflight_failure.path | "reports/phase6/base_residual_dropout_review_initial_API_failure.json" |
| initial_CPU_preflight_failure.sha256 | "bafada7cd04eee404c86f6954653b2b592ee84fb91b565263e0e2992cb714965" |
| initial_CPU_preflight_failure.repair | "Ad-hoc self-API caller uses candidate_minus_control; frozen reviewer/science unchanged" |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_original_context_preparation.json — None</summary>

[原記録](../../reports/phase6/base_residual_original_context_preparation.json) ／ SHA256: `bc2752d57fe72df1b7fa0701ad150a91c6448b5072ec8ae2b2098df4443e22d2` ／ 192,299 bytes

| 原キー | 保存値 |
|---|---|
| CPU_seconds | 0.11366457901021931 |
| original_unit_EOS_targets_used | 0 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_seen_train_preparation.json — six_actual_first_update_TRAIN_windows_bound_no_model_evaluation</summary>

[原記録](../../reports/phase6/base_residual_seen_train_preparation.json) ／ SHA256: `33ba90940e4d7c1b1c17b977c898a563e639e0b8475d683edd0e8e10bb27635e` ／ 47,742 bytes

| 原キー | 保存値 |
|---|---|
| status | "six_actual_first_update_TRAIN_windows_bound_no_model_evaluation" |
| CPU_seconds | 0.37483975500799716 |
| first_committed_history.update | 1 |
| original_next_token_alignment_verified | true |
| first_batch_original_teachers | 9178 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| generated_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| Base_adopted | false |
| limits | "First two distinct first-window bodies per source in the actual first update only. This proves exposure, not repeated memorization, diversity, generalization or current model quality. No unconsumed heldout claim; no checkpoint or full-corpus rehash." |

</details>

<details>
<summary>reports/phase6/base_residual_seen_train_source_notes.json — None</summary>

[原記録](../../reports/phase6/base_residual_seen_train_source_notes.json) ／ SHA256: `7181b2bdd1c413e425866c28de040251763409691b9e8a91f430386fec40db2d` ／ 1,873 bytes

| 原キー | 保存値 |
|---|---|
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_train_dev_history_preparation.json — None</summary>

[原記録](../../reports/phase6/base_residual_train_dev_history_preparation.json) ／ SHA256: `83df631a254e6a89aa0dbc0712a8f4bf3faf7fd42fb04c22b80e81e8324e0acc` ／ 190,981 bytes

| 原キー | 保存値 |
|---|---|
| CPU_seconds | 1.6116049779957393 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| limits | "Only Web and initial consumed windows; do not generalize to all sources or learning history. Repetition judgments are diagnostic observations, not a replacement acceptance criterion. Current checkpoint trained on2B gold, not the discarded six-case memorization probe." |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_CPU_preparation.json — CPU14_and_actual10M_parent_link_parity_passed_no_GPU</summary>

[原記録](../../reports/phase6/base_sigsoftmax_CPU_preparation.json) ／ SHA256: `e3eacc4019d73f4e317c831494b9198efdc91802791e8ad851a32b90e83e078b` ／ 4,438 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU14_and_actual10M_parent_link_parity_passed_no_GPU" |
| tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_tests.xml" |
| tests.sha256 | "8f82bf8d7c277772c6f67f9fd5b0553ada97290eb956be843be361cc7215ee44" |
| tests_passed | 14 |
| tests_seconds | 3.727 |
| recorder_CPU_seconds | 0.33065034801256843 |
| total_CPU_preparation_seconds | 4.057650348012569 |
| CPU_preparation_cap_seconds | 30 |
| real_parent_checks.original_parent_weights | true |
| real_parent_checks.same_parameter_count | true |
| real_parent_checks.tied_vocabulary | true |
| real_parent_checks.installing_link_preserved_RNG | true |
| real_parent_checks.native_FP32_linked_logits | true |
| real_parent_checks.same_weight_FP32_greedy_order | true |
| real_parent_checks.finite_model_scores | true |
| real_parent_checks.source_is_train_only | true |
| diagnostic_valid_tokens | 128 |
| source_sha256.scripts/record_base_sigsoftmax_CPU_preparation.py | "923beca9db67ce4c1b49d39e65128c66a3354a4ebcc0917acd0e42b345bb0672" |
| source_sha256.tests/test_base_sigsoftmax.py | "6afbca4d582ecde61f8b8262a3c439e9b9e17e9f00834668b60d0683ae837d3f" |
| GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| protected_test_used | false |
| GPU_workflow_implemented | false |
| GPU_resume_capacity_budget_proven | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_CPU_preparation_v2.json — CPU14_and_actual10M_parent_link_parity_passed_no_GPU</summary>

[原記録](../../reports/phase6/base_sigsoftmax_CPU_preparation_v2.json) ／ SHA256: `8c861515df0c3694041179547e1dd562fed96ec0acd6f12e1e8a9f5b56f3653d` ／ 5,359 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU14_and_actual10M_parent_link_parity_passed_no_GPU" |
| tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_tests_v2.xml" |
| tests.sha256 | "bf11f1b68722a33ec0a36e4a6b3dfdab781209c96de432fa26ba2e47cb8e9ae6" |
| tests_passed | 14 |
| tests_seconds | 3.228 |
| recorder_CPU_seconds | 0.2659349400200881 |
| total_CPU_preparation_seconds | 7.551585288032657 |
| previous_CPU_preparation.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_CPU_preparation.json" |
| previous_CPU_preparation.sha256 | "e3eacc4019d73f4e317c831494b9198efdc91802791e8ad851a32b90e83e078b" |
| initial_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_tests_initial_CPU.py" |
| initial_tests.sha256 | "6afbca4d582ecde61f8b8262a3c439e9b9e17e9f00834668b60d0683ae837d3f" |
| CPU_preparation_cap_seconds | 30 |
| real_parent_checks.original_parent_weights | true |
| real_parent_checks.same_parameter_count | true |
| real_parent_checks.tied_vocabulary | true |
| real_parent_checks.installing_link_preserved_RNG | true |
| real_parent_checks.native_FP32_linked_logits | true |
| real_parent_checks.same_weight_FP32_greedy_order | true |
| real_parent_checks.finite_model_scores | true |
| real_parent_checks.source_is_train_only | true |
| diagnostic_valid_tokens | 128 |
| source_sha256.scripts/record_base_sigsoftmax_CPU_preparation.py | "af3833d09f3043f6c6f40f845f0b354ef6b1f782ebf03e420c5a7e698642bd3d" |
| source_sha256.tests/test_base_sigsoftmax.py | "a9a72cf038ab1bdafae9874e75c206a3e3aba8d0eba04ef8b8360a0b442dd5ab" |
| GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| protected_test_used | false |
| GPU_workflow_implemented | false |
| GPU_resume_capacity_budget_proven | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_closeout_preparation.json — closeout_preparation_verified_not_scientific_completion</summary>

[原記録](../../reports/phase6/base_sigsoftmax_closeout_preparation.json) ／ SHA256: `b035ac12fa29b9780914250f8e7d58605d8ee25adde30b2b9d41bc527b3e5aec` ／ 5,275 bytes

| 原キー | 保存値 |
|---|---|
| status | "closeout_preparation_verified_not_scientific_completion" |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_source_diagnostics_completion.json — actual_CPU_endpoint_and_read_only_GPU_gradient_diagnostics_complete</summary>

[原記録](../../reports/phase6/base_source_diagnostics_completion.json) ／ SHA256: `ee93258cf032727dd7679fca84f01de209fc95272534103f45bffd9412ed5c5d` ／ 1,235 bytes

| 原キー | 保存値 |
|---|---|
| Base_adopted | false |
| protected_test_used | false |
| CPU_seconds | 0.052992940007243305 |
| status | "actual_CPU_endpoint_and_read_only_GPU_gradient_diagnostics_complete" |
| EOS_scored_teacher_tokens | 2574 |
| optimizer_updates | 0 |
| GPU_seconds | 3.338032489991747 |
| actual_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| archive.bytes | 266072 |
| full_CE_scored_teacher_tokens | 259570 |
| new_scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/base_source_diagnostics_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_source_diagnostics_evidence_manifest.json) ／ SHA256: `04d94d661df70f8c7d5c1198bf1a84818bc1ef6683c3f1386556d04b12be3ea3` ／ 5,832 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 1709698 |
| archive.bytes | 266072 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/base_source_semantic_judge_completion.json — fixed64_classifier_diagnostic_complete_rejected</summary>

[原記録](../../reports/phase6/base_source_semantic_judge_completion.json) ／ SHA256: `6fc014df7ba680b2f0e5f173abf9cc0d04ba3bf476606edbca580898f96a20e5` ／ 4,173 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed64_classifier_diagnostic_complete_rejected" |
| files.scripts/base_source_semantic_judge.py.bytes | 3960 |
| files.scripts/prepare_base_source_semantic_judge.py.bytes | 4966 |
| files.scripts/run_base_source_semantic_judge.py.bytes | 10351 |
| files.scripts/run_base_source_semantic_judge.ps1.bytes | 1902 |
| files.tests/test_base_source_semantic_judge.py.bytes | 1536 |
| files.tests/test_base_source_semantic_judge.py.sha256 | "fc0ddaeccc7b7198344510eaa861e2de0417046f949ebcc25e767ba69e9610fd" |
| files.configs/phase6/base_source_semantic_judge.json.bytes | 5820 |
| files.reports/phase6/base_source_semantic_judge_tests.xml.bytes | 527 |
| files.reports/phase6/base_source_semantic_judge_tests.xml.sha256 | "891ef4ba5cd17837d5c005b496065d57302b5c7814687113770806165d1cbb76" |
| files.reports/phase6/base_source_semantic_judge_result.json.bytes | 127487 |
| files.reports/phase6/base_source_semantic_judge_review.json.bytes | 7163 |
| files.reports/phase6/base_teacher_semantic_signal_proposal.json.bytes | 2700 |
| files.reports/phase6/base_teacher_semantic_signal_proposal.json.sha256 | "8ca8dc67b8d25553ec61d2fe11abba0c076992abc05644e356c453581d6a10b4" |
| files.reports/phase6/base-source-semantic-judge-20261007/job.json.bytes | 761 |
| files.reports/phase6/base-source-semantic-judge-launcher-20261007/launcher.json.bytes | 77 |
| files.reports/phase6/base-source-semantic-judge-launcher-20261007/result.json.bytes | 155 |
| archive.bytes | 34105 |
| all64_prediction_reasons_read | true |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| GPU_seconds | 54.2281782880018 |
| Base_complete | false |
| limitations | "既存64の非blind Codex採点との一致であり、独立人間gold/全source品質率/未知corpusへの汎化は未測定。prompt作成者は全64を以前に読んでいる。4Bのこのclassifier失敗は、日本語の全能力やteacher representationの無効性、10M容量限界を証明しない。" |

</details>

<details>
<summary>reports/phase6/base_source_semantic_judge_result.json — fixed64_judge_complete_rejected</summary>

[原記録](../../reports/phase6/base_source_semantic_judge_result.json) ／ SHA256: `1221592ac412edb42b27de831bb0391155451ca4c04864f40f53119fbaee460d` ／ 127,487 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed64_judge_complete_rejected" |
| original_sample_sha256 | "6451ee32fa0d656812c72361d9a895f48ead0e99c17e4b08af2261a577c5c00f" |
| all64.documents | 64 |
| all64.accepted | 60 |
| all64.accuracy | 0.671875 |
| development.documents | 32 |
| development.accepted | 29 |
| development.accuracy | 0.6875 |
| holdout.documents | 32 |
| holdout.accepted | 31 |
| holdout.accuracy | 0.65625 |
| gate.minimum_accepted | 8 |
| classifier_feasibility_passed | false |
| GPU_seconds | 54.2281782880018 |
| classification_seconds | 49.55091222599731 |
| peak_allocated_bytes | 11565212672 |
| observed_original_body_tokens | 46463 |
| raw_body_tokens_per_second | 937.6820307179489 |
| input_tokens | 75513 |
| generated_tokens | 3786 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| prepared_training_tokens | 0 |
| Base_complete | false |
| protected_test_bodies_read | false |
| no_gold_labels_or_reasons_in_prompt | true |
| new_weight_download_bytes | 0 |
| limitations | "Retrospective nonblind Codex gold, not independent human truth. Prompt author previously read all64. File-separated judge holdout is neither untouched final Base test nor proof of global transfer. No gold reasons/labels/source IDs are given to the model. No model/prompt tuned on outputs. Prior Qwen prose-generation recipe failed and remains closed; this is a different classification mechanism, with no generated training prose." |

</details>

<details>
<summary>reports/phase6/base_source_semantic_judge_review.json — all64_semantic_judge_predictions_read_classifier_rejected</summary>

[原記録](../../reports/phase6/base_source_semantic_judge_review.json) ／ SHA256: `88774050d4a1a139723ad4d296386044b18c62d83c80a98e2cdc0b1d29aa6b70` ／ 7,163 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_semantic_judge_predictions_read_classifier_rejected" |
| classifier_feasibility_passed | false |
| fixed_judge_branch_closed | true |
| all64.documents | 64 |
| all64.accepted | 60 |
| all64.accuracy | 0.671875 |
| development.documents | 32 |
| development.accepted | 29 |
| development.accuracy | 0.6875 |
| holdout.documents | 32 |
| holdout.accepted | 31 |
| holdout.accuracy | 0.65625 |
| per_dimension.complete.documents | 64 |
| per_dimension.boilerplate.documents | 64 |
| per_dimension.grammar.exact_score_agreement | 56 |
| per_dimension.grammar.documents | 64 |
| per_dimension.coherence.exact_score_agreement | 55 |
| per_dimension.coherence.documents | 64 |
| GPU_seconds | 54.2281782880018 |
| peak_allocated_bytes | 11565212672 |
| raw_body_tokens_per_second | 937.6820307179489 |
| evidence_interpretation | "Prompt出力形式の全64成功を採点精度と混同しない。非blind既存Codex labelsとのagreement precisionが64.5%で90%未達。32holdout中31accept、weak12のうち11を誤採用、良い20は全採用。全64では60accept中20false positive、true40、false negative1。" |
| prepared_training_tokens | 0 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| new_weight_download_bytes | 0 |
| protected_test_bodies_read | false |
| limitations | "既存64の非blind Codex採点との一致であり、独立人間gold/全source品質率/未知corpusへの汎化は未測定。prompt作成者は全64を以前に読んでいる。4Bのこのclassifier失敗は、日本語の全能力やteacher representationの無効性、10M容量限界を証明しない。" |

</details>

<details>
<summary>reports/phase6/base_teacher_decay_seed_preparation.json — native_seed43_factory_CPU_verified_no_additional_GPU_started</summary>

[原記録](../../reports/phase6/base_teacher_decay_seed_preparation.json) ／ SHA256: `5511228f0ec2035a6d641a0721c57a4f04b1c8ffb67c4edc472022044ae9b421` ／ 1,531 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_seed43_factory_CPU_verified_no_additional_GPU_started" |
| sources.scripts/base_teacher_decay_seed_protocol.py | "722417614ac91aef754cba1a3b63b2cc4521fec8ee4f1c63ec97c3e85cfd9425" |
| sources.tests/test_base_teacher_decay_seed_protocol.py | "498e9c36fd3b8238b55c7fd6373ce78a344e4373e34e40f79e82e98ef18afa13" |
| sources.reports/phase6/base_teacher_decay_seed_protocol_tests.xml | "de51ccf9ab67ef6f5a40a12700c063718ca8a5ce6b31075ba2242773e52086b9" |
| sources.docs/122_base_native_seed_confirmation_preparation.md | "5f97337527f1e4715b52e5de1461f9e613224b16b1f3ab7e436d70ab9be1769d" |
| CPU_tests.tests | 4 |
| CPU_tests.failures | 0 |
| CPU_tests.seconds | 3.27 |
| own_new_GPU_updates | 0 |
| actual_seed43_training_complete | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_preparation.json — block_Web_constraint_preparation</summary>

[原記録](../../reports/phase6/block_Web_constraint_preparation.json) ／ SHA256: `262061c098175342969c001dc50ce420e2d5a860bd21440d1b0ffcc1d75ded88` ／ 1,688 bytes

| 原キー | 保存値 |
|---|---|
| status | "block_Web_constraint_preparation" |
| CPU_preparation_seconds | 0.11339189999853261 |
| GPU_seconds | 0 |
| scientific_source_CE_teacher_tokens | 0 |
| previous_related_GPU_seconds | 70.56110643898137 |
| total_related_GPU_ceiling_seconds | 2400 |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| does_not_satisfy_old_per_update_contract | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_preparation_portable.json) ／ SHA256: `68434f9300eec64d063955040fc1e1cc22748dcb3058ff122952c614f0348875` ／ 1,912 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/block_Web_constraint_preparation.json.bytes | 1688 |
| files.configs/phase6/block_Web_constraint_probe.json.bytes | 24510 |
| files.reports/phase6/block_Web_constraint_proposal.json.bytes | 12773 |
| files.reports/phase6/block_Web_constraint_tests.xml.bytes | 840 |
| files.reports/phase6/block_Web_constraint_tests.xml.sha256 | "7fe025883075a594e2ecb81d3acef8cb17889fd569be8580cc825dd6835b45fb" |
| files.scripts/record_block_Web_constraint.py.bytes | 9404 |
| files.scripts/define_block_Web_constraint.py.bytes | 4102 |
| files.scripts/block_Web_constraint.py.bytes | 6063 |
| files.scripts/run_block_Web_constraint.py.bytes | 20212 |
| files.scripts/run_block_Web_constraint.ps1.bytes | 3090 |
| files.tests/test_block_Web_constraint.py.bytes | 4132 |
| files.tests/test_block_Web_constraint.py.sha256 | "eb4511a8d9aaf99e468e12d07035b652469aa9a52124467f109d5feb4b98ce08" |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation.json — readonly_compiled_Web_oracle_preparation</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation.json) ／ SHA256: `54d9d7d489003408411187eb0503acb8db7febb8c689b8cb58662cc6d4844fa5` ／ 1,581 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_compiled_Web_oracle_preparation" |
| CPU_preparation_seconds | 0.3315294579952024 |
| GPU_seconds | 0 |
| previous_related_GPU_seconds | 43.74074014197686 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| completion_scope | "Readonly implementation evidence, not qualified Base/adoption." |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation_portable.json) ／ SHA256: `4c638299cfda42213dca6d25f3046606d2372a0366427a0c24ac9e19be47f51c` ／ 1,100 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/compiled_Web_oracle_preparation.json.bytes | 1581 |
| files.configs/phase6/compiled_Web_oracle.json.bytes | 7066 |
| files.scripts/record_compiled_Web_oracle.py.bytes | 6681 |
| files.scripts/probe_compiled_Web_oracle.py.bytes | 12397 |
| files.scripts/probe_compiled_Web_oracle.ps1.bytes | 2616 |

</details>

<details>
<summary>reports/phase6/compiled_Web_oracle_preparation.json — readonly_compiled_Web_oracle_preparation</summary>

[原記録](../../reports/phase6/compiled_Web_oracle_preparation.json) ／ SHA256: `33befb74ddbc38239dac470716b0b549ca10b5dacfbc63166ac6fa4c7b889dbf` ／ 1,581 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_compiled_Web_oracle_preparation" |
| CPU_preparation_seconds | 0.2164402320049703 |
| GPU_seconds | 0 |
| previous_related_GPU_seconds | 43.74074014197686 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| completion_scope | "Readonly implementation evidence, not qualified Base/adoption." |

</details>

<details>
<summary>reports/phase6/compiled_Web_oracle_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/compiled_Web_oracle_preparation_portable.json) ／ SHA256: `e9cbd820c4753192b8eb7ffd4c65d1cea8922b179ad07bd7a934f978f38b3970` ／ 1,100 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/compiled_Web_oracle_preparation.json.bytes | 1581 |
| files.configs/phase6/compiled_Web_oracle.json.bytes | 7066 |
| files.scripts/record_compiled_Web_oracle.py.bytes | 6681 |
| files.scripts/probe_compiled_Web_oracle.py.bytes | 12980 |
| files.scripts/probe_compiled_Web_oracle.ps1.bytes | 2616 |

</details>

<details>
<summary>reports/phase6/complete_document_source_origins.json — None</summary>

[原記録](../../reports/phase6/complete_document_source_origins.json) ／ SHA256: `883bb622232e78a2eb21131e6feb6faedeafc3d66b8de73f300fbb1cead11fc5` ／ 887 bytes

| 原キー | 保存値 |
|---|---|
| sampler.seed | 42 |
| sampler.epoch | 0 |
| sampler.position | 97632 |
| sampler.context | 1024 |
| sampler.blocks | 107422 |
| whole_scientific_run.story | 27265983 |
| whole_scientific_run.web | 472740929 |
| whole_scientific_run.total | 500006912 |
| scientific_story_fraction | 0.05453121216052309 |
| short_EOS_teachers | 607745 |
| old_story_short_EOS_teachers | 1105092 |
| protected_test_used | false |
| checked_at | "2026-10-05T05:38:45.839894Z" |

</details>

<details>
<summary>reports/phase6/condition-diversity-source-20261006/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-source-20261006/content-pilot.json) ／ SHA256: `2dabbfaf1f0ca92b8da265b762bacc5940ce8c3bc84586276a5e4151db03b224` ／ 182,924 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition-diversity-source-20261006/content-review.json — all64_new_nested_condition_content_review_complete</summary>

[原記録](../../reports/phase6/condition-diversity-source-20261006/content-review.json) ／ SHA256: `3191a2d3b87b5da7f1fec1063fd7711aab1afa915c02abf97dd176aa2e674e72` ／ 27,635 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_new_nested_condition_content_review_complete" |
| weak_pairs | 4 |
| maximum_weak_pairs | 10 |
| paired_content_gate_passed | true |
| training_pool_accepted | true |
| notes_sha256 | "46e21213981516134ebcf037aa4aa52c8a777921c71898da8966b7005807e793" |
| source_pairs_sha256 | "8d694f870d777021b040bfeb4b32d4b4ae80e160f30597886bb2598bc792a58a" |
| documents | 2048 |
| newly_prepared_original_tokens | 0 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind selected64 new examples, no global/source-family/near-duplicate/factual guarantee. All512 originals remain identical; global2B original corpus unchanged. No automatic reroll of this sample or selector revision." |

</details>

<details>
<summary>reports/phase6/condition-diversity-source-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-diversity-source-20261006/job.json) ／ SHA256: `d71261ee78857f55dcde79af2f610d254912ecc64d80cd36f7cf46992ba38d36` ／ 530 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| CPU_budget_seconds | 240 |
| documents | 2048 |
| target_documents | 2048 |
| new_GPU_seconds | 0 |
| CPU_seconds | 78.5790633080178 |

</details>

<details>
<summary>reports/phase6/condition-diversity-source-20261006/result.json — bounded_nested_condition_supply_unreviewed</summary>

[原記録](../../reports/phase6/condition-diversity-source-20261006/result.json) ／ SHA256: `a0a2a33ce7666f5cd48be148e112f7964b1b591a29f10d533825d62534f8c7c4` ／ 2,362 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_nested_condition_supply_unreviewed" |
| seed | 2026100654 |
| documents | 2048 |
| original_small_documents | 512 |
| target_documents | 2048 |
| source_pairs_sha256 | "8d694f870d777021b040bfeb4b32d4b4ae80e160f30597886bb2598bc792a58a" |
| content_pilot_documents | 64 |
| attempt_limit | 32000000 |
| CPU_seconds | 78.57879601800232 |
| CPU_limit_seconds | 240 |
| stop_reason | "target_reached" |
| decoded_documents | 1648097 |
| inspected_existing_body_tokens | 215494692 |
| selected_original_body_tokens | 290243 |
| accepted_index.path | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large/.compact-index-8cde6396d433644b/ready.json" |
| accepted_index.sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| newly_prepared_original_tokens | 0 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| training_pool_accepted | false |
| limitations | "Local exact body/document uniqueness; no global/family/factual certification. Whole original train reused from existing2B, not new original corpus tokens. V3 selector unchanged; source cardinality comparison, not V4 content reroll. Only64 new examples will be individually read." |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/source-cases.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/source-cases.json) ／ SHA256: `4e9c11d18395b03aeeb8a9ac7caec86f8ef6f59ca598ca00bf14bac447f85823` ／ 930,998 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/preparation-completion.json — actual_CPU_relation_language2048_fixed64_and_common100M_teachers_complete</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/preparation-completion.json) ／ SHA256: `b48d971d579aa4de85754954278e4caaf5cd03b929d42a7f3249ee9145b17437` ／ 18,636 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU_relation_language2048_fixed64_and_common100M_teachers_complete" |
| job.status | "complete_pending_fixed64_content" |
| job.CPU_limit_seconds | 240 |
| job.scientific_teacher_tokens | 0 |
| job.actual_GPU_seconds | 0 |
| job.protected_test_used | false |
| job.CPU_seconds | 0.38243402299121954 |
| job.changed_documents | 684 |
| source_replacement.changed_documents | 684 |
| source_replacement.other_four_categories_byte_exact | true |
| body_tokens | 85350 |
| body_bytes | 330943 |
| serialized_tokens | 89446 |
| EOS | 2048 |
| original_serialized_tokens | 86309 |
| content_review.unresolved_grammar | 0 |
| content_review.unchanged42_prior_notes_reused | true |
| ordinary_stream_audit.checks.target_sha256 | true |
| ordinary_stream_audit.checks.teachers | true |
| ordinary_stream_audit.checks.EOS | true |
| ordinary_stream_audit.checks.body_bytes | true |
| ordinary_stream_audit.CPU_seconds | 6.478647753014229 |
| CPU_tests.source | "reports/phase6/condition_relation_language_tests.xml" |
| CPU_tests.count | 4 |
| CPU_tests.seconds | 1.16 |
| CPU_tests.comparison | "reports/phase6/condition_relation_comparison_tests.xml" |
| CPU_tests.comparison_count | 4 |
| CPU_tests.comparison_seconds | 2.09 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| new_original_public_corpus_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Preparation evidence only. Same original1024 families/2048 documents with684 language replacements; other1364 full texts identical.128 new local probes and128 old retention are not independent natural-language quality. Actual science is recorded separately." |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/annotations.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/annotations.json) ／ SHA256: `cafdd09d65cad92d21c56eac2e8ec065846c36ac1a658708fec007fc9778c263` ／ 36,702 bytes

| 原キー | 保存値 |
|---|---|
| arms.small512.notes_sha256 | "0d2445b55acddf98c485dca71d4d09c19a0ef1f36e19b1201b5f1706d0666c82" |
| arms.large2048.notes_sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/compare-result.json — actual_both100M_complete_pending_all160_content</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/compare-result.json) ／ SHA256: `c2afbceecf13138bcf66d8dbf0340efe0bab947291f3acdf6f75483c06927fee` ／ 1,483,024 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.small512.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/small512/training/checkpoint-00065244.pt" |
| checkpoints.small512.checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |
| checkpoints.small512.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| checkpoints.small512.binding.arm | "small512" |
| checkpoints.small512.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.small512.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.small512.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.small512.binding.teacher_goals.web | 75000000 |
| checkpoints.small512.binding.teacher_goals.story | 5000000 |
| checkpoints.small512.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.small512.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.small512.binding.optimizer_policy | "inherit" |
| checkpoints.small512.binding.peak_lr | 0.0002 |
| checkpoints.small512.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.small512.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| checkpoints.small512.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| checkpoints.small512.binding.outcome_weight | 1 |
| checkpoints.small512.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| checkpoints.small512.update | 65244 |
| checkpoints.small512.tokens | 2137915392 |
| checkpoints.small512.supervised_tokens | 2120000000 |
| checkpoints.small512.additional_supervised_tokens | 100000000 |
| checkpoints.small512.additional_input_tokens | 100859904 |
| checkpoints.small512.source_teachers.web | 75000000 |
| checkpoints.small512.source_teachers.story | 5000000 |
| checkpoints.small512.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.small512.source_teachers.conditional_textbook | 10000000 |
| checkpoints.small512.source_eos.web | 656229 |
| checkpoints.small512.source_eos.story | 38240 |
| checkpoints.small512.source_eos.ordinary_textbook | 74183 |
| checkpoints.small512.source_eos.conditional_textbook | 70720 |
| checkpoints.small512.source_input_tokens.web | 75674624 |
| checkpoints.small512.source_input_tokens.story | 5039104 |
| checkpoints.small512.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.small512.source_input_tokens.conditional_textbook | 10071040 |
| checkpoints.small512.source_focus_teachers.web | 0 |
| checkpoints.small512.source_focus_teachers.story | 0 |
| checkpoints.small512.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.small512.source_focus_teachers.conditional_textbook | 2618331 |
| checkpoints.small512.focus_teacher_tokens | 2618331 |
| checkpoints.small512.focus_token_digest | "9f4928eecb02c621b9caaa27335854f868d12ae03019d13b350f68b1c970784a" |
| checkpoints.small512.weighted_teacher_mass | 100000000 |
| checkpoints.small512.outcome_weight | 1 |
| checkpoints.small512.training_seconds | 152.38707779403194 |
| checkpoints.small512.completed_at | "2026-10-06T02:39:55.618901Z" |
| checkpoints.large2048.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| checkpoints.large2048.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checkpoints.large2048.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| checkpoints.large2048.binding.arm | "large2048" |
| checkpoints.large2048.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.large2048.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.large2048.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.large2048.binding.teacher_goals.web | 75000000 |
| checkpoints.large2048.binding.teacher_goals.story | 5000000 |
| checkpoints.large2048.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.large2048.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.large2048.binding.optimizer_policy | "inherit" |
| checkpoints.large2048.binding.peak_lr | 0.0002 |
| checkpoints.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.large2048.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| checkpoints.large2048.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| checkpoints.large2048.binding.outcome_weight | 1 |
| checkpoints.large2048.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.large2048.update | 65244 |
| checkpoints.large2048.tokens | 2137915392 |
| checkpoints.large2048.supervised_tokens | 2120000000 |
| checkpoints.large2048.additional_supervised_tokens | 100000000 |
| checkpoints.large2048.additional_input_tokens | 100859904 |
| checkpoints.large2048.source_teachers.web | 75000000 |
| checkpoints.large2048.source_teachers.story | 5000000 |
| checkpoints.large2048.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.large2048.source_teachers.conditional_textbook | 10000000 |
| checkpoints.large2048.source_eos.web | 656229 |
| checkpoints.large2048.source_eos.story | 38240 |
| checkpoints.large2048.source_eos.ordinary_textbook | 74183 |
| checkpoints.large2048.source_eos.conditional_textbook | 70061 |
| checkpoints.large2048.source_input_tokens.web | 75674624 |
| checkpoints.large2048.source_input_tokens.story | 5039104 |
| checkpoints.large2048.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.large2048.source_input_tokens.conditional_textbook | 10071040 |
| checkpoints.large2048.source_focus_teachers.web | 0 |
| checkpoints.large2048.source_focus_teachers.story | 0 |
| checkpoints.large2048.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.large2048.source_focus_teachers.conditional_textbook | 2620780 |
| checkpoints.large2048.focus_teacher_tokens | 2620780 |
| checkpoints.large2048.focus_token_digest | "8e2af3a7a69ecc6ea03b6f189587339877c5cf6d20031ae69100d24ffe4a7d85" |
| checkpoints.large2048.weighted_teacher_mass | 100000000 |
| checkpoints.large2048.outcome_weight | 1 |
| checkpoints.large2048.training_seconds | 151.12010613348684 |
| checkpoints.large2048.completed_at | "2026-10-06T02:43:40.425716Z" |
| evaluations.small512.binding.teacher_goals.web | 75000000 |
| evaluations.small512.binding.teacher_goals.story | 5000000 |
| evaluations.small512.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.small512.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.small512.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.small512.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| evaluations.small512.checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |
| evaluations.small512.body.documents | 256 |
| evaluations.small512.body.limit_documents | 256 |
| evaluations.small512.body.body_nll | 370814.93106746674 |
| evaluations.small512.body.eos_nll | 952.3527011200786 |
| evaluations.small512.body.body_bytes | 472055 |
| evaluations.small512.body.body_tokens | 122343 |
| evaluations.small512.body.bpb | 1.1332850242844945 |
| evaluations.small512.body.seconds | 1.4567046380252577 |
| evaluations.small512.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.small512.generation.max_new_tokens | 64 |
| evaluations.small512.greedy_rates.eos | 42 |
| evaluations.small512.greedy_rates.repetition | 25 |
| evaluations.small512.greedy_rates.unicode_failure | 0 |
| evaluations.small512.greedy_rates.role_leak | 0 |
| evaluations.small512.greedy_rates.empty | 0 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.point | 0.5208333333333334 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.ci95 | [0.4895833333333333, 0.5520833333333334] |
| evaluations.small512.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.primary.hard_accuracy | 0.5208333333333334 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5677083333333334 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.609375] |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5677083333333334 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.macro_f1 | 0.567414967833003 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.mcc | 0.13560071180129693 |
| evaluations.small512.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.small512.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.small512.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.small512.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.small512.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.824773413897281] |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7009063444108762, 0.7945619335347432] |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.small512.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.small512.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.small512.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.small512.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.small512.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.small512.diagnostics.jblimp.raw_pair_accuracy | 0.7915407854984894 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.point | 0.29892761394101874 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.ci95 | [0.2734472743521001, 0.32529043789097406] |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jcqa.primary.hard_accuracy | 0.2993744414655943 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.28865058087578194 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26362823949955316, 0.3163538873994638] |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28865058087578194 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.28791803950963013 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.mcc | 0.11112388185239853 |
| evaluations.small512.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.small512.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.small512.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.small512.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.small512.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.small512.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.small512.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.small512.diagnostics.semantic_both_contexts.correct | 7 |
| evaluations.small512.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.small512.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.small512.protected_test_used | false |
| evaluations.large2048.binding.teacher_goals.web | 75000000 |
| evaluations.large2048.binding.teacher_goals.story | 5000000 |
| evaluations.large2048.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.large2048.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.large2048.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| evaluations.large2048.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| evaluations.large2048.body.documents | 256 |
| evaluations.large2048.body.limit_documents | 256 |
| evaluations.large2048.body.body_nll | 371986.53641319275 |
| evaluations.large2048.body.eos_nll | 947.4765769392252 |
| evaluations.large2048.body.body_bytes | 472055 |
| evaluations.large2048.body.body_tokens | 122343 |
| evaluations.large2048.body.bpb | 1.136865685906886 |
| evaluations.large2048.body.seconds | 1.2853469330002554 |
| evaluations.large2048.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.large2048.generation.max_new_tokens | 64 |
| evaluations.large2048.greedy_rates.eos | 42 |
| evaluations.large2048.greedy_rates.repetition | 20 |
| evaluations.large2048.greedy_rates.unicode_failure | 0 |
| evaluations.large2048.greedy_rates.role_leak | 0 |
| evaluations.large2048.greedy_rates.empty | 0 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.point | 0.5052083333333334 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.53125] |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.primary.hard_accuracy | 0.5052083333333334 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5625 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5625 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5617391304347825 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.mcc | 0.1254363015010636 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8308157099697885] |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.large2048.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.point | 0.29803395889186773 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.ci95 | [0.27211796246648795, 0.32350312779267204] |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2864164432529044 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2605004468275246, 0.3118856121537087] |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28596961572832885 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2851033257946277 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.mcc | 0.107638793111279 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.semantic_both_contexts.correct | 4 |
| evaluations.large2048.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.large2048.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.large2048.protected_test_used | false |
| source_rankings.small512.checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |
| source_rankings.small512.checks.weights_unchanged | true |
| source_rankings.small512.checks.no_gradients | true |
| source_rankings.small512.checks.eval_mode | true |
| source_rankings.small512.checks.RNG_restored | true |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.7109375 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.both_source_matches | 67 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 48 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 81 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 0.7812211504222508 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6982758620689655 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 46 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.576345337949595 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 1.0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.7129205208315206 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.421875 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.45256877369852344 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.6875 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.both_source_matches | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 81 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1839415828794887 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6681034482758621 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 55 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 45 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1386758882201062 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.9921875 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 63 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 1 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.40091374583164896 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.3828125 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 1 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 47 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| source_rankings.small512.summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.10721480551149201 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.671875 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 49 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 74 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 104 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.5281224570389303 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6551724137931034 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 41 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 70 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 93 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.4406658144585357 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.8046875 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 39 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 25 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.0682836635986792 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5390625 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 49 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 42 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.22405236461373257 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.67578125 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 52 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.12953186000167694 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6594827586206896 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 44 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 65 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 94 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1078362710896975 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.8203125 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 42 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 21 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.2334190955764469 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.53125 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 43 |
| source_rankings.small512.summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.04552131665705755 |
| source_rankings.small512.original_outcome_fit.original_history.all128.target_tokens | 4808 |
| source_rankings.small512.original_outcome_fit.original_history.all128.NLL_sum | 6169.855127367961 |
| source_rankings.small512.original_outcome_fit.original_history.all128.token_weighted_mean_NLL | 1.2832477386372632 |
| source_rankings.small512.original_outcome_fit.original_history.nonweak116.target_tokens | 4283 |
| source_rankings.small512.original_outcome_fit.original_history.nonweak116.NLL_sum | 5648.484704847636 |
| source_rankings.small512.original_outcome_fit.original_history.nonweak116.token_weighted_mean_NLL | 1.3188150139732981 |
| source_rankings.small512.original_outcome_fit.original_history.old512_fixed64.target_tokens | 2469 |
| source_rankings.small512.original_outcome_fit.original_history.old512_fixed64.NLL_sum | 334.486156263677 |
| source_rankings.small512.original_outcome_fit.original_history.old512_fixed64.token_weighted_mean_NLL | 0.13547434437572986 |
| source_rankings.small512.original_outcome_fit.original_history.new1536_fixed64.target_tokens | 2339 |
| source_rankings.small512.original_outcome_fit.original_history.new1536_fixed64.NLL_sum | 5835.368971104284 |
| source_rankings.small512.original_outcome_fit.original_history.new1536_fixed64.token_weighted_mean_NLL | 2.4948135831997797 |
| source_rankings.small512.original_outcome_fit.isolated_condition.all128.target_tokens | 4808 |
| source_rankings.small512.original_outcome_fit.isolated_condition.all128.NLL_sum | 8915.968635378154 |
| source_rankings.small512.original_outcome_fit.isolated_condition.all128.token_weighted_mean_NLL | 1.8544027943798158 |
| source_rankings.small512.original_outcome_fit.isolated_condition.nonweak116.target_tokens | 4283 |
| source_rankings.small512.original_outcome_fit.isolated_condition.nonweak116.NLL_sum | 8079.045232942879 |
| source_rankings.small512.original_outcome_fit.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.8863052143224093 |
| source_rankings.small512.original_outcome_fit.isolated_condition.old512_fixed64.target_tokens | 2469 |
| source_rankings.small512.original_outcome_fit.isolated_condition.old512_fixed64.NLL_sum | 2194.8510636424767 |
| source_rankings.small512.original_outcome_fit.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 0.8889635737717605 |
| source_rankings.small512.original_outcome_fit.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| source_rankings.small512.original_outcome_fit.isolated_condition.new1536_fixed64.NLL_sum | 6721.117571735678 |
| source_rankings.small512.original_outcome_fit.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 2.873500458202513 |
| source_rankings.small512.optimizer_updates | 0 |
| source_rankings.small512.scientific_teacher_tokens | 0 |
| source_rankings.small512.protected_test_used | false |
| source_rankings.small512.source_matching_is_not_certified_negative_accuracy | true |
| source_rankings.large2048.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| source_rankings.large2048.checks.weights_unchanged | true |
| source_rankings.large2048.checks.no_gradients | true |
| source_rankings.large2048.checks.eval_mode | true |
| source_rankings.large2048.checks.RNG_restored | true |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.90625 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.both_source_matches | 104 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 24 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 126 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 1.052006538414515 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.9051724137931034 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 94 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 22 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 114 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 1.013731539778425 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.921875 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 54 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.9947544513939663 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.890625 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 50 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 14 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 1.1418362717135704 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.90234375 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.both_source_matches | 104 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 124 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.22674762186808117 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.9008620689655172 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 94 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 21 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 112 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.22493046222783997 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.90625 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 53 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.22492699577031253 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.8984375 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 51 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 13 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.24178601122927187 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.74609375 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 66 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 116 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.6087951194612606 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.7370689655172413 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 55 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.5810864684854096 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.7578125 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 34 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 29 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.6314340865418551 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.734375 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 32 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.5975226413142112 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.734375 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 63 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 62 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 116 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1307308527805075 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.728448275862069 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 56 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 57 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.12703871094364044 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.75 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 32 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 32 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.13797850108877846 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.71875 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 31 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| source_rankings.large2048.summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.12317623941879144 |
| source_rankings.large2048.original_outcome_fit.original_history.all128.target_tokens | 4808 |
| source_rankings.large2048.original_outcome_fit.original_history.all128.NLL_sum | 3085.485443666836 |
| source_rankings.large2048.original_outcome_fit.original_history.all128.token_weighted_mean_NLL | 0.6417399009290424 |
| source_rankings.large2048.original_outcome_fit.original_history.nonweak116.target_tokens | 4283 |
| source_rankings.large2048.original_outcome_fit.original_history.nonweak116.NLL_sum | 2768.4378872357015 |
| source_rankings.large2048.original_outcome_fit.original_history.nonweak116.token_weighted_mean_NLL | 0.6463782132233719 |
| source_rankings.large2048.original_outcome_fit.original_history.old512_fixed64.target_tokens | 2469 |
| source_rankings.large2048.original_outcome_fit.original_history.old512_fixed64.NLL_sum | 1548.6724715106184 |
| source_rankings.large2048.original_outcome_fit.original_history.old512_fixed64.token_weighted_mean_NLL | 0.627246849538525 |
| source_rankings.large2048.original_outcome_fit.original_history.new1536_fixed64.target_tokens | 2339 |
| source_rankings.large2048.original_outcome_fit.original_history.new1536_fixed64.NLL_sum | 1536.8129721562177 |
| source_rankings.large2048.original_outcome_fit.original_history.new1536_fixed64.token_weighted_mean_NLL | 0.6570384660779041 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.all128.target_tokens | 4808 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.all128.NLL_sum | 7303.015933024732 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.all128.token_weighted_mean_NLL | 1.5189301025425814 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.nonweak116.target_tokens | 4283 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.nonweak116.NLL_sum | 6565.750707237799 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.5329793852995095 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.old512_fixed64.target_tokens | 2469 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.old512_fixed64.NLL_sum | 3600.0964089256054 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 1.4581192421731897 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.new1536_fixed64.NLL_sum | 3702.9195240991257 |
| source_rankings.large2048.original_outcome_fit.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 1.5831207884134784 |
| source_rankings.large2048.optimizer_updates | 0 |
| source_rankings.large2048.scientific_teacher_tokens | 0 |
| source_rankings.large2048.protected_test_used | false |
| source_rankings.large2048.source_matching_is_not_certified_negative_accuracy | true |
| status | "actual_both100M_complete_pending_all160_content" |
| scientific_teacher_tokens | 200000000 |
| verification_teacher_tokens | 2599760 |
| verification_GPU_seconds | 21.030304796993732 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 453.00058993601124 |

</details>
