# 構成・反復計算・容量 — 2/7

[分野一覧へ](05_architecture.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/base-residual-dropout-probe-evidence-20261007/reports/phase6/base-residual-dropout-probe-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-residual-dropout-probe-evidence-20261007/reports/phase6/base-residual-dropout-probe-20261007/result.json) ／ SHA256: `958055cb1d52b46eaa59d977302abf5cbcdbbeaf1b5e5a2514238b3c1531ffde` ／ 83,242 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| passed | true |
| initial_checks.native_weights | true |
| initial_checks.native_parameters | true |
| initial_checks.native_tied | true |
| initial_checks.initialization_RNG | true |
| initial_checks.training_sites | true |
| initial_checks.native_logits | true |
| initial_checks.inference_RNG_unchanged | true |
| initial_checks.training_masks_active | true |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 0 |
| capacity.16.passed | true |
| capacity.16.peak_VRAM_bytes | 3837475840 |
| capacity.16.context | 1024 |
| capacity.16.loss | 3.281668186187744 |
| capacity.16.gradient_norm | 20.508241653442383 |
| capacity.16.optimizer_updates | 0 |
| capacity.16.teachers | 8192 |
| capacity.16.physical_input_tokens | 16384 |
| capacity.32.passed | true |
| capacity.32.peak_VRAM_bytes | 7465794560 |
| capacity.32.context | 1024 |
| capacity.32.loss | 2.949056386947632 |
| capacity.32.gradient_norm | 5.2433600425720215 |
| capacity.32.optimizer_updates | 0 |
| capacity.32.teachers | 16384 |
| capacity.32.physical_input_tokens | 32768 |
| capacity.48.passed | true |
| capacity.48.peak_VRAM_bytes | 11095129088 |
| capacity.48.context | 1024 |
| capacity.48.loss | 3.3149211406707764 |
| capacity.48.gradient_norm | 8.63879108428955 |
| capacity.48.optimizer_updates | 0 |
| capacity.48.teachers | 24576 |
| capacity.48.physical_input_tokens | 49152 |
| capacity.64.passed | true |
| capacity.64.peak_VRAM_bytes | 14724463616 |
| capacity.64.context | 1024 |
| capacity.64.loss | 3.2554516792297363 |
| capacity.64.gradient_norm | 7.758731842041016 |
| capacity.64.optimizer_updates | 0 |
| capacity.64.teachers | 32768 |
| capacity.64.physical_input_tokens | 65536 |
| timings.16.median_CE_targets_per_second | 16206.0068359375 |
| timings.16.samples | [15497.996148400767, 11631.452093649006, 23097.42484752375, 22154.06492544513, 16206.00718977863] |
| timings.32.median_CE_targets_per_second | 23900.125 |
| timings.32.samples | [28210.169912812737, 23739.40237930112, 23900.12461117922, 26022.526978348345, 20387.039875750263] |
| timings.48.median_CE_targets_per_second | 44579.12109375 |
| timings.48.samples | [91192.06810471634, 75541.42894832653, 32353.501048220878, 44579.12258045542, 38576.80553432277] |
| timings.64.median_CE_targets_per_second | 58060.19140625 |
| timings.64.samples | [62936.584301387426, 99567.88568774423, 58060.192246067476, 43969.88793905881, 41783.34958864278] |
| measured_fastest_resident_batch | 64 |
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
| resume_checks.finite | true |
| resume_checks.all_history_except_timing | true |
| resume_checkpoints.continuous.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-dropout-probe-20261007/resume-gate/continuous.pt" |
| resume_checkpoints.continuous.sha256 | "07d288d5c1e1588e8e8c35eb8d57746c531fa8bdc798c184ed167d80d654e02a" |
| resume_checkpoints.resumed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-dropout-probe-20261007/resume-gate/resumed.pt" |
| resume_checkpoints.resumed.sha256 | "b42c52cdb1ca199b1192e4ce8ce11101e639ae60a6a94f83ac60522aae45e33e" |
| verification_updates | 44 |
| verification_CE_teacher_tokens | 220036 |
| GPU_occupancy_seconds | 9.546564576012315 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-residual-dropout-probe-evidence-20261007/reports/phase6/base_residual_dropout_proposal.json — single_training_only_dropout_hypothesis_before_GPU</summary>

[原記録](../../reports/phase6/base-residual-dropout-probe-evidence-20261007/reports/phase6/base_residual_dropout_proposal.json) ／ SHA256: `782f8179915c876ffdfee42ef2948115e7a5ceb4e0cd77b5c37ca3388311de35` ／ 3,038 bytes

| 原キー | 保存値 |
|---|---|
| status | "single_training_only_dropout_hypothesis_before_GPU" |
| CPU_protocol_limit_seconds | 30 |
| GPU_probe_limit_seconds | 180 |
| scientific_teacher_tokens_proposed | 100000000 |
| hypothesis | "Previously learned original TRAIN targets can fit substantially better without held-out generation transfer. Training-only embedding/residual dropout may reduce co-adaptation and transfer better into the same native predictive vocabulary distribution; success in this Japanese10M setting is unproven." |
| primary_limitation | "General supervised dropout research; not evidence that Japanese10M Base generation or EOS will improve." |
| comparison_completion | "Actual exact100M completed native full-state; same full CE accounting/digest/cursor as cached CE; full Japanese/DEV256 common-byte BPB/new generation80 individual notes, reused CE80 and original strong/Web retention/absolute gates; actual process ended, restored original UI, evidence and commit." |
| probe_completion | "CPU tests then actual finite CUDA/BF16, initial native evaluation/RNG equivalence, training stochastic masks, continuous4 versus2-save-resume2 all state/history, longest1024 window resident capacity and measured source speed. Discard all probe weights." |
| budget_policy | "Freeze scientific GPU budget only after actual matched batch48 throughput and worst-context capacity, with checkpoint/evaluation allowance. Implement persistent scientific command/reviewer first." |
| failed_condition_policy | "Close fixed probability/sites if qualification fails. No probability/sites/LR/source/epoch/head sweep or automatic extension." |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base-residual-initialization-launcher-20261008/launcher.json — None</summary>

[原記録](../../reports/phase6/base-residual-initialization-launcher-20261008/launcher.json) ／ SHA256: `65e99bd46247028fcae0952f744d11c5f912e2936f7ccefb543d79bfb1dc0b31` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-residual-initialization-launcher-20261008/result.json — complete</summary>

[原記録](../../reports/phase6/base-residual-initialization-launcher-20261008/result.json) ／ SHA256: `5f1d4ef006a8f253a995beacdaf8e3dd19fbf11bdd6f874f083ccd946f9024ac` ／ 199 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-residual-original-context-launcher-20261008/launcher.json — None</summary>

[原記録](../../reports/phase6/base-residual-original-context-launcher-20261008/launcher.json) ／ SHA256: `a0fd251679324d9ba6cdb62cd9cecfd6e7895955aa19deafbbcfdfd400ca7e50` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-residual-original-context-launcher-20261008/result.json — complete</summary>

[原記録](../../reports/phase6/base-residual-original-context-launcher-20261008/result.json) ／ SHA256: `e5318c157bb367e1a1889b7d535cbad8019b75b2f301dec4eae103e6197f28ca` ／ 199 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base_attention_saturation_completion.json — readonly_attention_assay_complete_broad_screen_not_passed</summary>

[原記録](../../reports/phase6/base_attention_saturation_completion.json) ／ SHA256: `78a8c02ec4a8a5740b7ee4eb049d5a859ef68d93374932819dd91217534c41ed` ／ 7,939 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_attention_assay_complete_broad_screen_not_passed" |
| source_summaries.parent.web.eligible_head_queries | 37908 |
| source_summaries.parent.textbook.eligible_head_queries | 38272 |
| source_summaries.parent.story.eligible_head_queries | 36764 |
| source_summaries.CE100M.web.eligible_head_queries | 37908 |
| source_summaries.CE100M.textbook.eligible_head_queries | 38272 |
| source_summaries.CE100M.story.eligible_head_queries | 36764 |
| source_summaries.fresh_calibration.web.eligible_head_queries | 37908 |
| source_summaries.fresh_calibration.textbook.eligible_head_queries | 38272 |
| source_summaries.fresh_calibration.story.eligible_head_queries | 36764 |
| all_native_checks.parent.weights_unchanged | true |
| all_native_checks.parent.RNG_unchanged | true |
| all_native_checks.parent.native_tied | true |
| all_native_checks.parent.no_accumulated_grads | true |
| all_native_checks.parent.hooks_removed | true |
| all_native_checks.parent.all_fixed_rows_measured | true |
| all_native_checks.CE100M.weights_unchanged | true |
| all_native_checks.CE100M.RNG_unchanged | true |
| all_native_checks.CE100M.native_tied | true |
| all_native_checks.CE100M.no_accumulated_grads | true |
| all_native_checks.CE100M.hooks_removed | true |
| all_native_checks.CE100M.all_fixed_rows_measured | true |
| all_native_checks.fresh_calibration.weights_unchanged | true |
| all_native_checks.fresh_calibration.RNG_unchanged | true |
| all_native_checks.fresh_calibration.native_tied | true |
| all_native_checks.fresh_calibration.no_accumulated_grads | true |
| all_native_checks.fresh_calibration.hooks_removed | true |
| all_native_checks.fresh_calibration.all_fixed_rows_measured | true |
| fixed_diagnostic_closed | true |
| no_QK_restoration_softcap_sigma_learning_from_negative_screen | true |
| GPU_occupancy_seconds | 3.5264302429859526 |
| GPU_limit_seconds | 90 |
| diagnostic_teacher_positions | 7596 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| interpretation | "All fixed learned source aggregates show zero marked layers; about2percent eligible head-queries are sharply concentrated, mostly on original BOS. This does not prove attention always healthy or context used appropriately; no temporal entropy-collapse/causal generalization evidence." |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| archive.bytes | 4363514 |
| archive.archived_completion_is_pre_bundle_record | true |
| archive.compressed_bundle.bytes | 667323 |

</details>

<details>
<summary>reports/phase6/base_attention_saturation_result.json — complete</summary>

[原記録](../../reports/phase6/base_attention_saturation_result.json) ／ SHA256: `c591cd06a130c0fd7217e7813f745d1a4ad36258979779b240612290e6a84b5f` ／ 1,205,626 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| endpoints.parent.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| endpoints.parent.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| endpoints.parent.sources.web.eligible_head_queries | 37908 |
| endpoints.parent.sources.textbook.eligible_head_queries | 38272 |
| endpoints.parent.sources.story.eligible_head_queries | 36764 |
| endpoints.parent.native_checks.weights_unchanged | true |
| endpoints.parent.native_checks.RNG_unchanged | true |
| endpoints.parent.native_checks.native_tied | true |
| endpoints.parent.native_checks.no_accumulated_grads | true |
| endpoints.parent.native_checks.hooks_removed | true |
| endpoints.parent.native_checks.all_fixed_rows_measured | true |
| endpoints.parent.screen.passed | false |
| endpoints.CE100M.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| endpoints.CE100M.checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| endpoints.CE100M.sources.web.eligible_head_queries | 37908 |
| endpoints.CE100M.sources.textbook.eligible_head_queries | 38272 |
| endpoints.CE100M.sources.story.eligible_head_queries | 36764 |
| endpoints.CE100M.native_checks.weights_unchanged | true |
| endpoints.CE100M.native_checks.RNG_unchanged | true |
| endpoints.CE100M.native_checks.native_tied | true |
| endpoints.CE100M.native_checks.no_accumulated_grads | true |
| endpoints.CE100M.native_checks.hooks_removed | true |
| endpoints.CE100M.native_checks.all_fixed_rows_measured | true |
| endpoints.CE100M.screen.passed | false |
| endpoints.fresh_calibration.checkpoint.kind | "fresh_random_native_calibration_not_learning" |
| endpoints.fresh_calibration.checkpoint.seed | 42 |
| endpoints.fresh_calibration.sources.web.eligible_head_queries | 37908 |
| endpoints.fresh_calibration.sources.textbook.eligible_head_queries | 38272 |
| endpoints.fresh_calibration.sources.story.eligible_head_queries | 36764 |
| endpoints.fresh_calibration.native_checks.weights_unchanged | true |
| endpoints.fresh_calibration.native_checks.RNG_unchanged | true |
| endpoints.fresh_calibration.native_checks.native_tied | true |
| endpoints.fresh_calibration.native_checks.no_accumulated_grads | true |
| endpoints.fresh_calibration.native_checks.hooks_removed | true |
| endpoints.fresh_calibration.native_checks.all_fixed_rows_measured | true |
| endpoints.fresh_calibration.screen.passed | false |
| fixed_diagnostic_closed | true |
| GPU_occupancy_seconds | 3.5264302429859526 |
| peak_allocated_bytes | 104879104 |
| diagnostic_teacher_positions | 7596 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Small index-byte-biased first/last TRAIN windows, FP32 teacher forcing. No temporal training-entropy trajectory, free-generation context dependence or causal quality claim. Saturated specialized heads and attention sinks can be functional." |

</details>

<details>
<summary>reports/phase6/base_capacity_reference_synthesis.json — bounded_parameter_reference_and_cached_evidence_synthesis_complete</summary>

[原記録](../../reports/phase6/base_capacity_reference_synthesis.json) ／ SHA256: `ba603b7bd2d90b54300eee86815f6ed7fa10cf1c250e38420b1998ac5c52fe14` ／ 22,807 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_parameter_reference_and_cached_evidence_synthesis_complete" |
| CPU_seconds | 6.392987811006606 |
| CPU_wall_limit_seconds | 30 |
| GPU_seconds | 0 |
| new_CE_teacher_tokens | 0 |
| optimizer_updates | 0 |
| public_config.config.bos_token_id | 50256 |
| public_config.config.eos_token_id | 50256 |
| public_config.config.gradient_checkpointing | false |
| published_counts.published.token_embedding_parameters | 12865792 |
| published_counts.published.physical_vocab_size | 50257 |
| published_counts.paper_top10K_vocabulary_counterfactual.token_embedding_parameters | 2560000 |
| published_counts.paper_top10K_vocabulary_counterfactual.physical_vocab_size | 10000 |
| JMicro.token_embedding_parameters | 1048576 |
| JMicro.native_config.status | "phase5_ablation" |
| paper.interpretation | "The paper below10M claim and its public model name cannot be substituted for measured public-config total parameters. Published config has vocabulary50257 and max_position_embeddings2048; 10K calculation remains an explicitly labeled counterfactual." |
| cached_evidence.architecture.current.BPB | 2.1037092890318485 |
| cached_evidence.architecture.current.rates.eos | 54 |
| cached_evidence.architecture.current.rates.repetition | 4 |
| cached_evidence.architecture.current.rates.unicode_failure | 1 |
| cached_evidence.architecture.current.rates.role_leak | 0 |
| cached_evidence.architecture.current.rates.empty | 0 |
| cached_evidence.architecture.current.grammar2 | 16 |
| cached_evidence.architecture.current.relevance2 | 0 |
| cached_evidence.architecture.current.coherent | 0 |
| cached_evidence.architecture.current.appropriate | 0 |
| cached_evidence.architecture.current.scientific_teachers | 300000000 |
| cached_evidence.architecture.fewer_layers_more_FFN.BPB | 2.166974904561069 |
| cached_evidence.architecture.fewer_layers_more_FFN.rates.eos | 59 |
| cached_evidence.architecture.fewer_layers_more_FFN.rates.repetition | 7 |
| cached_evidence.architecture.fewer_layers_more_FFN.rates.unicode_failure | 0 |
| cached_evidence.architecture.fewer_layers_more_FFN.rates.role_leak | 0 |
| cached_evidence.architecture.fewer_layers_more_FFN.rates.empty | 0 |
| cached_evidence.architecture.fewer_layers_more_FFN.coherent | 0 |
| cached_evidence.architecture.fewer_layers_more_FFN.appropriate | 2 |
| cached_evidence.architecture.fewer_layers_more_FFN.grammar2 | 18 |
| cached_evidence.architecture.fewer_layers_more_FFN.relevance2 | 8 |
| cached_evidence.architecture.fewer_layers_more_FFN.scientific_teachers | 300000000 |
| cached_evidence.architecture.wider_fewer_layers.BPB | 2.2215441668867637 |
| cached_evidence.architecture.wider_fewer_layers.rates.eos | 52 |
| cached_evidence.architecture.wider_fewer_layers.rates.repetition | 6 |
| cached_evidence.architecture.wider_fewer_layers.rates.unicode_failure | 2 |
| cached_evidence.architecture.wider_fewer_layers.rates.role_leak | 0 |
| cached_evidence.architecture.wider_fewer_layers.rates.empty | 0 |
| cached_evidence.architecture.wider_fewer_layers.coherent | 0 |
| cached_evidence.architecture.wider_fewer_layers.appropriate | 0 |
| cached_evidence.architecture.wider_fewer_layers.grammar2 | 22 |
| cached_evidence.architecture.wider_fewer_layers.relevance2 | 4 |
| cached_evidence.architecture.wider_fewer_layers.scientific_teachers | 300000000 |
| cached_evidence.amount_learning.large-100000000.prepared_tokens | 500000785 |
| cached_evidence.amount_learning.large-100000000.stable_teachers | 100000000 |
| cached_evidence.amount_learning.large-100000000.decay_teachers | 20000000 |
| cached_evidence.amount_learning.large-100000000.BPB | 1.2317801684014853 |
| cached_evidence.amount_learning.large-100000000.rates.eos | 31 |
| cached_evidence.amount_learning.large-100000000.rates.repetition | 20 |
| cached_evidence.amount_learning.large-100000000.rates.unicode_failure | 0 |
| cached_evidence.amount_learning.large-100000000.rates.role_leak | 0 |
| cached_evidence.amount_learning.large-100000000.rates.empty | 0 |
| cached_evidence.amount_learning.large-100000000.grammar2 | 32 |
| cached_evidence.amount_learning.large-100000000.relevance2 | 16 |
| cached_evidence.amount_learning.large-100000000.coherent | 9 |
| cached_evidence.amount_learning.large-100000000.appropriate | 13 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.additional_input_tokens | 100499456 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.physical_input_tokens | 100499456 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.genre_teachers.web | 80072899 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.genre_teachers.story | 19927101 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.genre_eos.web | 341553 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.genre_eos.story | 153391 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.kind | "teacher-learning-curve-v1" |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.mode | "shuffle" |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.goals.web | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.goals.short | 2000000000 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.position | 3067 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.web.seed | 42 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.web.epoch | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.web.position | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.web.context | 1024 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.web.blocks | 11939276 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.seed | 42 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.epoch | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.position | 98144 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.context | 1024 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.blocks | 488282 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_tokens.web | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_tokens.short | 100499456 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_physical_tokens.web | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_physical_tokens.short | 100499456 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_teachers.web | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_teachers.short | 100000000 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_eos.web | 0 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.source_eos.short | 494944 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.boundaries | [100000000, 500000000, 1000000000, 2000000000] |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.genre_teachers.web | 80072899 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.genre_teachers.story | 19927101 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.genre_eos.web | 341553 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.sampler.genre_eos.story | 153391 |
| cached_evidence.amount_learning.large-100000000.stable_exposure.training_step_seconds | 149.84240358773968 |
| cached_evidence.amount_learning.large-100000000.branch_step_seconds | 31.27268365502823 |
| cached_evidence.amount_learning.large-100000000.peak_allocated_bytes | 6149073408 |
| cached_evidence.amount_learning.large-500000000.prepared_tokens | 500000785 |
| cached_evidence.amount_learning.large-500000000.stable_teachers | 500000000 |
| cached_evidence.amount_learning.large-500000000.decay_teachers | 20000000 |
| cached_evidence.amount_learning.large-500000000.BPB | 1.1674766352036285 |
| cached_evidence.amount_learning.large-500000000.rates.eos | 26 |
| cached_evidence.amount_learning.large-500000000.rates.repetition | 30 |
| cached_evidence.amount_learning.large-500000000.rates.unicode_failure | 0 |
| cached_evidence.amount_learning.large-500000000.rates.role_leak | 0 |
| cached_evidence.amount_learning.large-500000000.rates.empty | 0 |
| cached_evidence.amount_learning.large-500000000.grammar2 | 30 |
| cached_evidence.amount_learning.large-500000000.relevance2 | 18 |
| cached_evidence.amount_learning.large-500000000.coherent | 9 |
| cached_evidence.amount_learning.large-500000000.appropriate | 14 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.additional_input_tokens | 502497280 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.physical_input_tokens | 502497280 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.genre_teachers.web | 400275722 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.genre_teachers.story | 99724278 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.genre_eos.web | 1706217 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.genre_eos.story | 765375 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.kind | "teacher-learning-curve-v1" |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.mode | "shuffle" |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.goals.web | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.goals.short | 2000000000 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.position | 15335 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.web.seed | 42 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.web.epoch | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.web.position | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.web.context | 1024 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.web.blocks | 11939276 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.seed | 42 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.epoch | 1 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.position | 2438 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.context | 1024 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.blocks | 488282 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_tokens.web | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_tokens.short | 502497280 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_physical_tokens.web | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_physical_tokens.short | 502497280 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_teachers.web | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_teachers.short | 500000000 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_eos.web | 0 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.source_eos.short | 2471592 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.boundaries | [100000000, 500000000, 1000000000, 2000000000] |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.genre_teachers.web | 400275722 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.genre_teachers.story | 99724278 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.genre_eos.web | 1706217 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.sampler.genre_eos.story | 765375 |
| cached_evidence.amount_learning.large-500000000.stable_exposure.training_step_seconds | 747.2675421598688 |
| cached_evidence.amount_learning.large-500000000.branch_step_seconds | 31.235672848983086 |
| cached_evidence.amount_learning.large-500000000.peak_allocated_bytes | 6149073408 |
| cached_evidence.amount_learning.large-1000000000.prepared_tokens | 500000785 |
| cached_evidence.amount_learning.large-1000000000.stable_teachers | 1000000000 |
| cached_evidence.amount_learning.large-1000000000.decay_teachers | 20000000 |
| cached_evidence.amount_learning.large-1000000000.BPB | 1.152110186840399 |
| cached_evidence.amount_learning.large-1000000000.rates.eos | 37 |
| cached_evidence.amount_learning.large-1000000000.rates.repetition | 20 |
| cached_evidence.amount_learning.large-1000000000.rates.unicode_failure | 0 |
| cached_evidence.amount_learning.large-1000000000.rates.role_leak | 0 |
| cached_evidence.amount_learning.large-1000000000.rates.empty | 0 |
| cached_evidence.amount_learning.large-1000000000.grammar2 | 36 |
| cached_evidence.amount_learning.large-1000000000.relevance2 | 26 |
| cached_evidence.amount_learning.large-1000000000.coherent | 14 |
| cached_evidence.amount_learning.large-1000000000.appropriate | 22 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.additional_input_tokens | 1004994560 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.physical_input_tokens | 1004994560 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.genre_teachers.web | 800540240 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.genre_teachers.story | 199459760 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.genre_eos.web | 3412372 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.genre_eos.story | 1530741 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.kind | "teacher-learning-curve-v1" |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.mode | "shuffle" |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.goals.web | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.goals.short | 2000000000 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.position | 30670 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.web.seed | 42 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.web.epoch | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.web.position | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.web.context | 1024 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.web.blocks | 11939276 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.seed | 42 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.epoch | 2 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.position | 4876 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.context | 1024 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.blocks | 488282 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_tokens.web | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_tokens.short | 1004994560 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_physical_tokens.web | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_physical_tokens.short | 1004994560 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_teachers.web | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_teachers.short | 1000000000 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_eos.web | 0 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.source_eos.short | 4943113 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.boundaries | [100000000, 500000000, 1000000000, 2000000000] |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.genre_teachers.web | 800540240 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.genre_teachers.story | 199459760 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.genre_eos.web | 3412372 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.sampler.genre_eos.story | 1530741 |
| cached_evidence.amount_learning.large-1000000000.stable_exposure.training_step_seconds | 1493.398161706922 |
| cached_evidence.amount_learning.large-1000000000.branch_step_seconds | 31.190525577199878 |
| cached_evidence.amount_learning.large-1000000000.peak_allocated_bytes | 6149073408 |
| cached_evidence.amount_learning.large-2000000000.prepared_tokens | 500000785 |
| cached_evidence.amount_learning.large-2000000000.stable_teachers | 2000000000 |
| cached_evidence.amount_learning.large-2000000000.decay_teachers | 20000000 |
| cached_evidence.amount_learning.large-2000000000.BPB | 1.1385898259344385 |
| cached_evidence.amount_learning.large-2000000000.rates.eos | 40 |
| cached_evidence.amount_learning.large-2000000000.rates.repetition | 21 |
| cached_evidence.amount_learning.large-2000000000.rates.unicode_failure | 0 |
| cached_evidence.amount_learning.large-2000000000.rates.role_leak | 0 |
| cached_evidence.amount_learning.large-2000000000.rates.empty | 0 |
| cached_evidence.amount_learning.large-2000000000.grammar2 | 43 |
| cached_evidence.amount_learning.large-2000000000.relevance2 | 32 |
| cached_evidence.amount_learning.large-2000000000.coherent | 21 |
| cached_evidence.amount_learning.large-2000000000.appropriate | 27 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.additional_input_tokens | 2009956352 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.physical_input_tokens | 2009956352 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.genre_teachers.web | 1601099555 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.genre_teachers.story | 398900445 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.genre_eos.web | 6824396 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.genre_eos.story | 3061263 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.kind | "teacher-learning-curve-v1" |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.mode | "shuffle" |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.goals.web | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.goals.short | 2000000000 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.position | 61339 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.web.seed | 42 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.web.epoch | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.web.position | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.web.context | 1024 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.web.blocks | 11939276 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.seed | 42 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.epoch | 4 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.position | 9720 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.context | 1024 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.blocks | 488282 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_tokens.web | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_tokens.short | 2009956352 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_physical_tokens.web | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_physical_tokens.short | 2009956352 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_teachers.web | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_teachers.short | 2000000000 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_eos.web | 0 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.source_eos.short | 9885659 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.boundaries | [100000000, 500000000, 1000000000, 2000000000] |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.genre_teachers.web | 1601099555 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.genre_teachers.story | 398900445 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.genre_eos.web | 6824396 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.sampler.genre_eos.story | 3061263 |
| cached_evidence.amount_learning.large-2000000000.stable_exposure.training_step_seconds | 2985.552511660542 |
| cached_evidence.amount_learning.large-2000000000.branch_step_seconds | 31.16602130087267 |
| cached_evidence.amount_learning.large-2000000000.peak_allocated_bytes | 6149073408 |
| cached_evidence.amount_learning.small-1000000000.prepared_tokens | 100000157 |
| cached_evidence.amount_learning.small-1000000000.stable_teachers | 1000000000 |
| cached_evidence.amount_learning.small-1000000000.decay_teachers | 20000000 |
| cached_evidence.amount_learning.small-1000000000.BPB | 1.1594794747119588 |
| cached_evidence.amount_learning.small-1000000000.rates.eos | 34 |
| cached_evidence.amount_learning.small-1000000000.rates.repetition | 21 |
| cached_evidence.amount_learning.small-1000000000.rates.unicode_failure | 0 |
| cached_evidence.amount_learning.small-1000000000.rates.role_leak | 0 |
| cached_evidence.amount_learning.small-1000000000.rates.empty | 0 |
| cached_evidence.amount_learning.small-1000000000.grammar2 | 32 |
| cached_evidence.amount_learning.small-1000000000.relevance2 | 33 |
| cached_evidence.amount_learning.small-1000000000.coherent | 9 |
| cached_evidence.amount_learning.small-1000000000.appropriate | 26 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.additional_input_tokens | 1004994560 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.physical_input_tokens | 1004994560 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.genre_teachers.web | 800533113 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.genre_teachers.story | 199466887 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.genre_eos.web | 3412374 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.genre_eos.story | 1531010 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.kind | "teacher-learning-curve-v1" |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.mode | "shuffle" |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.goals.web | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.goals.short | 1000000000 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.position | 30670 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.web.seed | 42 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.web.epoch | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.web.position | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.web.context | 1024 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.web.blocks | 11939276 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.seed | 42 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.epoch | 10 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.position | 4880 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.context | 1024 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.blocks | 97656 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_tokens.web | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_tokens.short | 1004994560 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_physical_tokens.web | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_physical_tokens.short | 1004994560 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_teachers.web | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_teachers.short | 1000000000 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_eos.web | 0 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.source_eos.short | 4943384 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.boundaries | [100000000, 500000000, 1000000000] |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.genre_teachers.web | 800533113 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.genre_teachers.story | 199466887 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.genre_eos.web | 3412374 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.sampler.genre_eos.story | 1531010 |
| cached_evidence.amount_learning.small-1000000000.stable_exposure.training_step_seconds | 1490.3816702104814 |
| cached_evidence.amount_learning.small-1000000000.branch_step_seconds | 31.103675052785547 |
| cached_evidence.amount_learning.small-1000000000.peak_allocated_bytes | 6149073408 |
| cached_evidence.projection_summary.BPB | 1.0007222231116217 |
| cached_evidence.projection_summary.rates.eos | 21 |
| cached_evidence.projection_summary.rates.repetition | 47 |
| cached_evidence.projection_summary.rates.unicode_failure | 0 |
| cached_evidence.projection_summary.rates.role_leak | 0 |
| cached_evidence.projection_summary.rates.empty | 0 |
| cached_evidence.projection_summary.grammar2 | 57 |
| cached_evidence.projection_summary.relevance2 | 25 |
| cached_evidence.projection_summary.coherent | 4 |
| cached_evidence.projection_summary.appropriate | 3 |
| cached_evidence.projection_summary.notes_sha256 | "f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1" |
| cached_evidence.trainfit.focus_body_mean_nll.positive4 | 0.0806008015652098 |
| cached_evidence.trainfit.focus_body_mean_nll.parent2B | 2.0209250986011997 |
| cached_evidence.trainfit.focus_body_mean_nll.control | 0.5429198795562881 |
| cached_evidence.trainfit.interpretation | "Previously completed512 TRAIN example fit improved on all504 focus-enabled documents; fixed-dev generation coherence fell15 to9. Fitting these TRAIN targets is possible without demonstrated transfer; does not establish full capacity sufficiency or sole cause." |
| cached_evidence.generalization.interpreted_scope | "Existing held-out source-local DEV64 / greedy16 per model; four earlier actual endpoints. Strong train fit and weak transfer are already measured, not new GPU evidence. Closed mechanism not rescued." |
| cached_evidence.generalization.limitations | "Repeated nonblind source-local DEV; broad Web overlap uncertified. Already completed diagnostic must not be rerun." |
| conclusions | ["The public TinyStories-8M token embedding alone exceeds the complete JMicro-10M parameter budget. Its name is not a matched total-parameter control.", "This does not refute the paper claim; paper describes a restricted tokenizer and different architecture/context and data.", "Completed local depth/width/FFN comparison jointly changed allocations on a small material/budget. Its negative result does not prove all10M architectures incapable. Do not repeat that sweep.", "More data/teachers has improved some BPB and choice metrics while free generation and stop behavior sometimes worsened. An increase alone is not a qualified Base recipe.", "Closed contrast/projection mechanisms do not satisfy the unchanged generation and Web-retention criteria. Do not extend or rescue them."] |
| new_scientific_recipe_selected | false |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_capacity_reference_synthesis_proposal.json — bounded_readonly_reference_synthesis_before_new_GPU</summary>

[原記録](../../reports/phase6/base_capacity_reference_synthesis_proposal.json) ／ SHA256: `e597087d17d390e637272cc4addd24e59013bfa4f54dff0b5d7a73474c292062` ／ 1,815 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_readonly_reference_synthesis_before_new_GPU" |
| CPU_wall_limit_seconds | 30 |
| GPU_limit_seconds | 0 |
| optimizer_updates | 0 |
| teacher_tokens | 0 |
| completion_condition | "Save pinned public config/revision and measured CPU parameter counts; summarize existing causal limits; either select one genuinely untested hypothesis with defined comparison, or explicitly leave new GPU launch unselected. No quality gate changes or conclusion of impossibility." |

</details>

<details>
<summary>reports/phase6/base_context_mixing_comparison_completion.json — ContextMixing100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_context_mixing_comparison_completion.json) ／ SHA256: `36938e83837962706b0d67951533a79a83ee0ac949c7bdd533ca46ce8310a2bc` ／ 5,489 bytes

| 原キー | 保存値 |
|---|---|
| status | "ContextMixing100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_updates | 17698 |
| GPU_occupancy_seconds | 1823.2489165220177 |
| GPU_cap_seconds | 4072 |
| probe_GPU_seconds | 10.469572045985842 |
| total_GPU_seconds_including_probe | 1833.7184885680035 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-context-mixing-comparison-20261007/context_mixing/checkpoint-00017698.pt" |
| checkpoint_sha256 | "1490a80e327e6b6476d3cf6e44cdcbdb8a26dea4671f5b639963cc5221ba6c6b" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_context_mixing_notes.json" |
| notes.sha256 | "c0f154397920815184bf76d27c12eac51bd23340190d829372d288412c3ebf69" |
| reused_control_GPU_seconds | 0 |
| summaries.context_mixing.BPB | 1.007637929885986 |
| summaries.context_mixing.rates.eos | 11 |
| summaries.context_mixing.rates.repetition | 53 |
| summaries.context_mixing.rates.unicode_failure | 0 |
| summaries.context_mixing.rates.role_leak | 0 |
| summaries.context_mixing.rates.empty | 0 |
| summaries.context_mixing.grammar2 | 43 |
| summaries.context_mixing.relevance2 | 24 |
| summaries.context_mixing.coherent | 1 |
| summaries.context_mixing.appropriate | 4 |
| summaries.context_mixing.notes_sha256 | "c0f154397920815184bf76d27c12eac51bd23340190d829372d288412c3ebf69" |
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
| eligible_for_final_Base_validation | false |
| fixed_ContextMixing_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 107768551 |
| archive.compressed_bundle.bytes | 46995094 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_context_mixing_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_context_mixing_comparison_evidence_manifest.json) ／ SHA256: `4fab143af39f943bbc104ad239a1d90071251142c84a5eb3c41a9c414ed6d7d7` ／ 9,326 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_context_mixing_comparison_review.json — ContextMixing_native100M_and_all80_reviewed</summary>

[原記録](../../reports/phase6/base_context_mixing_comparison_review.json) ／ SHA256: `d5f6d90dd19b214d7675b8e1e62c6e2c8189fc8a39d8e686d0543507fffd79a2` ／ 4,801 bytes

| 原キー | 保存値 |
|---|---|
| status | "ContextMixing_native100M_and_all80_reviewed" |
| summaries.context_mixing.BPB | 1.007637929885986 |
| summaries.context_mixing.rates.eos | 11 |
| summaries.context_mixing.rates.repetition | 53 |
| summaries.context_mixing.rates.unicode_failure | 0 |
| summaries.context_mixing.rates.role_leak | 0 |
| summaries.context_mixing.rates.empty | 0 |
| summaries.context_mixing.grammar2 | 43 |
| summaries.context_mixing.relevance2 | 24 |
| summaries.context_mixing.coherent | 1 |
| summaries.context_mixing.appropriate | 4 |
| summaries.context_mixing.notes_sha256 | "c0f154397920815184bf76d27c12eac51bd23340190d829372d288412c3ebf69" |
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
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | false |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| scientific_CE_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| GPU_seconds | 1823.2489165220177 |
| probe_GPU_seconds | 10.469572045985842 |
| context_mixing.updates | 17698 |
| context_mixing.eligible_positions | 101805988 |
| context_mixing.prediction_physical_inputs | 370838917 |
| notes_sha256 | "c0f154397920815184bf76d27c12eac51bd23340190d829372d288412c3ebf69" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single seed and mature-parent history-mixing transition; repeated nonblind DEV; additional prediction compute. Fixed greedy variant is not full on-policy sampling or a likelihood-consistent objective. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required." |

</details>

<details>
<summary>reports/phase6/base_context_mixing_notes.json — None</summary>

[原記録](../../reports/phase6/base_context_mixing_notes.json) ／ SHA256: `c0f154397920815184bf76d27c12eac51bd23340190d829372d288412c3ebf69` ／ 19,556 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_context_mixing_probe_completion.json — ContextMixing_native_CUDA_verification_closed_science_started</summary>

[原記録](../../reports/phase6/base_context_mixing_probe_completion.json) ／ SHA256: `c1544c0b00492c7d51bfd7eaa176157fcb2765ba6a62300846dba393b56d3cd3` ／ 3,527 bytes

| 原キー | 保存値 |
|---|---|
| status | "ContextMixing_native_CUDA_verification_closed_science_started" |
| initial_checks.native_parent_weights | true |
| initial_checks.tied_native_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.all_parameters_once | true |
| resume_source_checks.kind | true |
| resume_source_checks.spec | true |
| resume_source_checks.binding | true |
| resume_source_checks.lineage | true |
| resume_source_checks.model_config | true |
| resume_source_checks.model | true |
| resume_source_checks.optimizer | true |
| resume_source_checks.scheduler | true |
| resume_source_checks.RNG | true |
| resume_source_checks.sampler | true |
| resume_source_checks.counters | true |
| resume_source_checks.context_mixing | true |
| resume_source_checks.context_mixing_RNG | true |
| resume_source_checks.finite_native_model_and_mixing_state | true |
| resume_source_checks.history_except_timing | true |
| resume_source_checks.same_original_stream | true |
| resume_source_checks.full_sampler_matches_AdamW | true |
| resume_source_checks.real_input_changes | true |
| resume_source_checks.prediction_forward_not_additional_supervision | true |
| GPU_seconds | 10.469572045985842 |
| verification_updates | 48 |
| verification_original_teacher_positions | 298097 |
| capacity_forward_backward_original_positions | 24576 |
| median_original_teachers_per_second | 40992.2117596508 |
| worst_peak_VRAM_bytes | 11078919680 |
| total_GPU_cap_seconds | 7200 |
| scientific_GPU_cap_seconds | 4072 |
| scientific_config_sha256 | "e1b2b64d9b57ccd1dc1ba341eb5a389c424842a7ce735583365da9ed2518b782" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Verification updates and worst-shape forward/backward are not scientific teacher budget or model quality. Original gold teachers match CE, but inputs mix5percent predictions and prediction forwards add compute. Different compute; single fixed history-mixing transition; fixed repeated DEV." |
| CPU_closeout_seconds | 0.10992721101501957 |

</details>

<details>
<summary>reports/phase6/base_context_mixing_probe_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_context_mixing_probe_evidence_manifest.json) ／ SHA256: `add2766e7d16f55e90da241a81e8be3650d24a362b4e4b4c1caf644e552c06e0` ／ 4,225 bytes

| 原キー | 保存値 |
|---|---|
| model_checkpoints_in_archive | false |

</details>

<details>
<summary>reports/phase6/base_context_mixing_proposal.json — CPU_protocol_verified_GPU_comparison_not_started</summary>

[原記録](../../reports/phase6/base_context_mixing_proposal.json) ／ SHA256: `f7943aba7de09b0f249d09bc315e6d0624e41b1b0cf201279ae810e6b24a80f8` ／ 9,800 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_protocol_verified_GPU_comparison_not_started" |
| hypothesis | "Does training on a small proportion of model-predicted history, while retaining original gold labels, reduce native greedy repetition and improve coherent continuations?" |
| mechanism.prediction_passes | 1 |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seed | 42 |
| original_gold_teacher_tokens | 100000000 |
| new_unique_dataset_tokens | 0 |
| cached_control.no_GPU_rerun | true |
| budgets.CPU_preparation_seconds | 60 |
| budgets.CUDA_probe_seconds | 180 |
| budgets.total_GPU_seconds | 7200 |
| budgets.science_budget | "Ceil(100M/measured median original teachers per second*1.3+900); plus actual probe must fit total cap" |
| budgets.accounting | "Prediction forwards/input positions are additional compute, not teachers; original clean CE input/digest and full sampler match cached CE. Report mixed-input digest and actual replacements separately." |
| acceptance | "Native CUDA/BF16 worst1024/512 batch48 finite forward/backward and full continuous4 vs2+save/resume+2, including dedicated mixing RNG, exact source and committed history, before any science. Then complete100M, common256-document BPB, Japanese192/331/1119 and all80 individually read raw-bound continuations. All matched CE/strong/absolute/historical Web gates unchanged. Only qualified candidates proceed to independent trainedseed/full DEV/protected final TEST/adoption." |
| failure | "Close failed finite/state/budget or final quality condition. No mixing probability/pass/decoder/LR/source/parent/batch/teacher/cap rescue or automatic extension." |
| limitations | "Fixed greedy one-pass variant, not a full sequential sampled rollout or a likelihood-consistent objective. Replaced histories can contradict original gold, especially names/numbers; byte-piece replacements may lack a standalone valid UTF8 rendering. Papers on other tasks do not prove Japanese10M benefit. One seed/mature parent/repeated nonblind DEV. Additional compute differs from cached CE." |
| references.base_muon_comparison_review.json.status | "Muon_native100M_and_all80_reviewed" |
| references.base_muon_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_muon_comparison_completion.json" |
| references.base_muon_comparison_completion.json.sha256 | "cfa43645b777d9dd5e685cfbce25e4175278c5aeec9d91a2033a3ba82e94cbad" |
| references.base_muon_comparison_completion.json.status | "Muon100M_review_complete_rejected" |
| references.base_decode_cached_evidence_review.json.status | "cached_trained_decode_evidence_reviewed" |
| references.root_cause_summary.json.status | "diagnostic_scope_complete_quality_unmet" |
| references.sequence_objective_comparison_review.json.status | "matched_CE_sequence_UL_learning_and_all160_content_evidence_complete" |
| references.sequence_objective_low_alpha_review.json.status | "matched_reused_CE_and_actual_low_alpha25M_all80_complete" |
| references.sequence_objective_diagnostic_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence_objective_diagnostic_completion.json" |
| references.sequence_objective_diagnostic_completion.json.sha256 | "4f11a2a2ca974db485ae988bad39b64f05c3fb8de85f976f85e1b4cafe40f4b7" |
| references.sequence_objective_diagnostic_completion.json.status | "actual_train_only_diagnosis_complete_next_comparison_planned" |
| references.base_preference_comparison_review.json.status | "Base_preference_all160_native_state_and_content_reviewed" |
| references.base_generalization_diagnostic_review.json.status | "source_local_generalization_all64_content_reviewed" |
| references.base_next_two_token_comparison_review.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_next_two_token_comparison_review.json" |
| references.base_next_two_token_comparison_review.json.sha256 | "b3589e13181de3a87db5da396bccf4514cade6e6a4ea27c822cba8ffed5f7c65" |
| references.base_next_two_token_comparison_review.json.status | "new80_and_reused80_next_two_comparison_reviewed" |
| source_sha256.tests/test_base_context_mixing_trainer.py | "874408b6350044073fde8afbc79a807b3cdb0faf4d5d449fd32577173ac57955" |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_context_mixing_trainer_tests.xml" |
| CPU_tests.sha256 | "aa2413c5bc5bcc7916a021c9ecb8260efa941c2f7088c61eab5c8a420c4aa494" |
| CPU_tests.passed | 9 |
| initial_fixture_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_context_mixing_initial_fixture_failure_tests.xml" |
| initial_fixture_failure.sha256 | "20d4238618440717fa5b833c53ea1a4745b0f13a4e438220ef3e8e11658f0856" |
| initial_fixture_failure.cause | "Repeated-character tied random fixture copied all selected inputs; no changed-input coverage. Preserved failed receipt; stress predictor now has stronger attention output while preserving tied weights and the original assertion." |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_context_mixing_prototype_completion.json — CPU_history_mixing_protocol_verified_cuda_pending</summary>

[原記録](../../reports/phase6/base_context_mixing_prototype_completion.json) ／ SHA256: `8eca2dd4762c2b94c4f41d98cb3e9ec9402f1707f680f854c934ed9281ec8c73` ／ 2,823 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_history_mixing_protocol_verified_cuda_pending" |
| actual_CPU_checks_passed | 9 |
| CPU_test_seconds | 4.53 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| source_sha256.tests/test_base_context_mixing_trainer.py | "874408b6350044073fde8afbc79a807b3cdb0faf4d5d449fd32577173ac57955" |
| checks | ["Causal previous-position predictions; boundary/PAD retention and no future prediction use", "Zero-mixing exact clean CE weights/Adam/scheduler/global RNG/sampler/source counters", "Actual changed-input coverage with tied imperfect predictor, unchanged gold/source quotas/digest", "Continuous4 vs2+save/resume+2 full state and committed history, dedicated mixing RNG", "Five wrong recipe/uncommitted counter/source/RNG cases rejected"] |
| initial_fixture_failure_preserved | true |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| previous_scientific_job_absent | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_context_mixing_science_start.json — native_ContextMixing100M_science_live</summary>

[原記録](../../reports/phase6/base_context_mixing_science_start.json) ／ SHA256: `1109d6c5ee6234518b81ab4cee04b345d67146894b3f1feee77076f500b4cc3f` ／ 2,120 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_ContextMixing100M_science_live" |
| scientific_config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/base_context_mixing_comparison.json" |
| scientific_config.sha256 | "e1b2b64d9b57ccd1dc1ba341eb5a389c424842a7ce735583365da9ed2518b782" |
| snapshot.status | "running" |
| snapshot.GPU_occupancy_seconds | 25.33425600201008 |
| snapshot.Base_complete | false |
| snapshot.memory_policy.visible_device_bytes | 25756696576 |
| snapshot.memory_policy.allocator_allowance_bytes | 23181026918 |
| snapshot.memory_policy.expected_worst_peak_bytes | 11078919680 |
| snapshot.completed_updates | 220 |
| snapshot.original_teachers | 1242231 |
| snapshot.CE_loss | 2.835667133331299 |
| target_original_teacher_tokens | 100000000 |
| control_reused_original_teacher_tokens | 100000000 |
| new_unique_dataset_tokens | 0 |
| GPU_cap_seconds | 4072 |
| cumulative_total_cap_seconds | 7200 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_active_job.json — actual_paired_Base_gate_science_running</summary>

[原記録](../../reports/phase6/base_headwise_gate_active_job.json) ／ SHA256: `c646d02defb49853f450daba4b96cb3f766f606392f07d1c63afd790029b00cf` ／ 1,524 bytes

| 原キー | 保存値 |
|---|---|
| scientific_target_total | 200000000 |
| GPU_budget_seconds | 6838 |
| original_teachers_observed | 2257843 |
| probe_GPU_seconds | 16.90010014099971 |
| CE_loss_observed | 2.4608047008514404 |
| scientific_target_each | 100000000 |
| status | "actual_paired_Base_gate_science_running" |
| Base_adopted | false |
| Base_complete | false |
| completed_updates | 400 |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_comparison_completion.json — paired_gate200M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_headwise_gate_comparison_completion.json) ／ SHA256: `2a2286904d41c9f7c6c6b195e74f7d578827ebcdff2d73b77c82d031e2745a08` ／ 7,528 bytes

| 原キー | 保存値 |
|---|---|
| status | "paired_gate200M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 200000000 |
| scientific_updates.static_half | 17698 |
| scientific_updates.query_headwise | 17698 |
| checkpoints.static_half.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-headwise-gate-comparison-20261007/static_half/checkpoint-00017698.pt" |
| checkpoints.static_half.sha256 | "5ae7d58dd8ed529679139a75237a40c3f92fbb6ff37cbb98d33a99e779fac886" |
| checkpoints.query_headwise.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-headwise-gate-comparison-20261007/query_headwise/checkpoint-00017698.pt" |
| checkpoints.query_headwise.sha256 | "c2d8c730632093bbc10ff2adfff2cbe37e3372d3f957110db141bf4ad66c34aa" |
| GPU_occupancy_seconds | 2986.0847258079993 |
| GPU_cap_seconds | 6838 |
| probe_GPU_seconds | 16.90010014099971 |
| total_GPU_seconds_including_probe | 3002.984825948999 |
| notes.static_half.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_static_half_notes.json" |
| notes.static_half.sha256 | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| notes.query_headwise.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_query_headwise_notes.json" |
| notes.query_headwise.sha256 | "36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a" |
| reused_control_GPU_seconds | 0 |
| added_physical_parameters_each | 13312 |
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
| summaries.static_half.BPB | 0.9984722020725625 |
| summaries.static_half.rates.eos | 19 |
| summaries.static_half.rates.repetition | 45 |
| summaries.static_half.rates.unicode_failure | 0 |
| summaries.static_half.rates.role_leak | 0 |
| summaries.static_half.rates.empty | 0 |
| summaries.static_half.grammar2 | 41 |
| summaries.static_half.relevance2 | 27 |
| summaries.static_half.coherent | 1 |
| summaries.static_half.appropriate | 2 |
| summaries.static_half.notes_sha256 | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| summaries.query_headwise.BPB | 0.9983496829108776 |
| summaries.query_headwise.rates.eos | 17 |
| summaries.query_headwise.rates.repetition | 48 |
| summaries.query_headwise.rates.unicode_failure | 0 |
| summaries.query_headwise.rates.role_leak | 0 |
| summaries.query_headwise.rates.empty | 0 |
| summaries.query_headwise.grammar2 | 40 |
| summaries.query_headwise.relevance2 | 28 |
| summaries.query_headwise.coherent | 1 |
| summaries.query_headwise.appropriate | 2 |
| summaries.query_headwise.notes_sha256 | "36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a" |
| summaries.cached_CE.BPB | 0.998487162513845 |
| summaries.cached_CE.rates.eos | 19 |
| summaries.cached_CE.rates.repetition | 45 |
| summaries.cached_CE.rates.unicode_failure | 0 |
| summaries.cached_CE.rates.role_leak | 0 |
| summaries.cached_CE.rates.empty | 0 |
| summaries.cached_CE.grammar2 | 44 |
| summaries.cached_CE.relevance2 | 25 |
| summaries.cached_CE.coherent | 2 |
| summaries.cached_CE.appropriate | 2 |
| summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| eligible_for_final_Base_validation | false |
| fixed_headwise_gate_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 212028151 |
| archive.compressed_bundle.bytes | 90886926 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_headwise_gate_comparison_evidence_manifest.json) ／ SHA256: `7c1b3ddd96223f49554981a378e72028eff448f4ec60f66dd24b2233e95962e6` ／ 23,410 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_comparison_review.json — paired_headwise_gate100M_all160_reviewed</summary>

[原記録](../../reports/phase6/base_headwise_gate_comparison_review.json) ／ SHA256: `6343c4a9aecc2af70ed122f1bb4b2f6b4a06d074e3a1792d7e90e5b0e5e94a5f` ／ 5,689 bytes

| 原キー | 保存値 |
|---|---|
| status | "paired_headwise_gate100M_all160_reviewed" |
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
| summaries.static_half.BPB | 0.9984722020725625 |
| summaries.static_half.rates.eos | 19 |
| summaries.static_half.rates.repetition | 45 |
| summaries.static_half.rates.unicode_failure | 0 |
| summaries.static_half.rates.role_leak | 0 |
| summaries.static_half.rates.empty | 0 |
| summaries.static_half.grammar2 | 41 |
| summaries.static_half.relevance2 | 27 |
| summaries.static_half.coherent | 1 |
| summaries.static_half.appropriate | 2 |
| summaries.static_half.notes_sha256 | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| summaries.query_headwise.BPB | 0.9983496829108776 |
| summaries.query_headwise.rates.eos | 17 |
| summaries.query_headwise.rates.repetition | 48 |
| summaries.query_headwise.rates.unicode_failure | 0 |
| summaries.query_headwise.rates.role_leak | 0 |
| summaries.query_headwise.rates.empty | 0 |
| summaries.query_headwise.grammar2 | 40 |
| summaries.query_headwise.relevance2 | 28 |
| summaries.query_headwise.coherent | 1 |
| summaries.query_headwise.appropriate | 2 |
| summaries.query_headwise.notes_sha256 | "36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a" |
| summaries.cached_CE.BPB | 0.998487162513845 |
| summaries.cached_CE.rates.eos | 19 |
| summaries.cached_CE.rates.repetition | 45 |
| summaries.cached_CE.rates.unicode_failure | 0 |
| summaries.cached_CE.rates.role_leak | 0 |
| summaries.cached_CE.rates.empty | 0 |
| summaries.cached_CE.grammar2 | 44 |
| summaries.cached_CE.relevance2 | 25 |
| summaries.cached_CE.coherent | 2 |
| summaries.cached_CE.appropriate | 2 |
| summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| quality_comparisons.new_static.checks.coherence_gain_at_least8 | false |
| quality_comparisons.new_static.checks.paired_CI_lower_above0 | false |
| quality_comparisons.new_static.checks.EOS_nonworsening | false |
| quality_comparisons.new_static.checks.repetition_nonworsening | false |
| quality_comparisons.new_static.checks.no_empty_role_unicode | true |
| quality_comparisons.new_static.checks.BPB_gate | true |
| quality_comparisons.new_static.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.new_static.passed | false |
| quality_comparisons.strong.checks.coherence_gain_at_least8 | false |
| quality_comparisons.strong.checks.paired_CI_lower_above0 | false |
| quality_comparisons.strong.checks.EOS_nonworsening | false |
| quality_comparisons.strong.checks.repetition_nonworsening | false |
| quality_comparisons.strong.checks.no_empty_role_unicode | true |
| quality_comparisons.strong.checks.BPB_gate | true |
| quality_comparisons.strong.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.strong.passed | false |
| quality_comparisons.cached_native.checks.coherence_gain_at_least8 | false |
| quality_comparisons.cached_native.checks.paired_CI_lower_above0 | false |
| quality_comparisons.cached_native.checks.EOS_nonworsening | false |
| quality_comparisons.cached_native.checks.repetition_nonworsening | false |
| quality_comparisons.cached_native.checks.no_empty_role_unicode | true |
| quality_comparisons.cached_native.checks.BPB_gate | true |
| quality_comparisons.cached_native.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.cached_native.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| scientific_CE_teacher_tokens | 200000000 |
| reused_control_teacher_tokens | 100000000 |
| GPU_seconds | 2986.0847258079993 |
| probe_GPU_seconds | 16.90010014099971 |
| notes_sha256.static_half | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| notes_sha256.query_headwise | "36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single mature parent and training seed; altered parameterization/13312 added physical parameters, candidate gate learning freedom. Fixed repeated nonblind DEV, not independent human or final TEST. Independent learnedseed/fullDEV/protectedTEST/adoption pending." |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_parent_CPU_parity.json — actual_original10B_CPU_conversion_all24_exact_no_learning</summary>

[原記録](../../reports/phase6/base_headwise_gate_parent_CPU_parity.json) ／ SHA256: `f6af579f2fd09bb4eaad85d5e34864bcdfe79293a7a38c8666dc27e47323968c` ／ 16,930 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_original10B_CPU_conversion_all24_exact_no_learning" |
| source_sha256.tests/test_base_headwise_gate_model.py | "7780b1748c9fa739e9a0f565e3366510efb0b9cd4960792154bad0055eda8c14" |
| CPU_seconds | 1.304993769000248 |
| CPU_ceiling_seconds | 30 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| UI_unchanged.model.training_tokens | 10000007168 |
| UI_unchanged.model.update | 305176 |
| UI_unchanged.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_unchanged.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_unchanged.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_probe_completion.json — own_paired_CUDA_passed_and_exited_science_frozen_not_started</summary>

[原記録](../../reports/phase6/base_headwise_gate_probe_completion.json) ／ SHA256: `f24606a9e50efc6763eac8b984b1384d256d1904e63c111033c1b91a67576c07` ／ 3,901 bytes

| 原キー | 保存値 |
|---|---|
| GPU_ceiling_seconds | 9000 |
| status | "own_paired_CUDA_passed_and_exited_science_frozen_not_started" |
| arm_budget_seconds.static_half | 3946 |
| arm_budget_seconds.query_headwise | 2892 |
| Base_adopted | false |
| GPU_seconds | 16.90010014099971 |
| verification_original_teacher_positions | 500626 |
| common_source_checks.update | true |
| common_source_checks.token_digest | true |
| common_source_checks.supervised_tokens | true |
| common_source_checks.source_teachers | true |
| common_source_checks.source_EOS | true |
| common_source_checks.CE_input_tokens | true |
| common_source_checks.original_body_bytes | true |
| common_source_checks.auxiliary_input_tokens | true |
| common_source_checks.auxiliary_pairs | true |
| common_source_checks.physical_input_tokens | true |
| common_source_checks.full_sampler | true |
| common_source_checks.initial_actual_CE_equal | true |
| common_source_checks.all32_full_original_draws_equal | true |
| new_scientific_teacher_tokens | 0 |
| forecast_plus_probe_seconds | 6854.900100141 |
| verification_updates | 86 |
| Base_complete | false |
| scientific_config_sha256 | "3c5a2f4a051b09f02077eb69eab9a0796486f86c2467009c53af29286a04f5e2" |
| UI_identity.status | "running" |
| UI_identity.additional_training_tokens | 0 |
| UI_identity.model.training_tokens | 10000007168 |
| UI_identity.model.update | 305176 |
| UI_identity.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_identity.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_identity.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| UI_model.training_tokens | 10000007168 |
| UI_model.update | 305176 |
| UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| all_initial_checks.paired_initial_weights | true |
| all_initial_checks.global_RNG_equal | true |
| all_initial_checks.tied_vocab_both | true |
| all_initial_checks.equal_actual10014464 | true |
| all_initial_checks.actual_parameters_once_both | true |
| all_initial_checks.fresh_AdamW_both | true |
| all_initial_checks.full_initial_sampler_equal | true |
| all_initial_checks.conversion_gate_zero_both | true |
| all_initial_checks.conversion_original_nongate_weights | true |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_proposal.json — paired_static_vs_query_headwise_gate_defined_CPU_validated_GPU_unstarted</summary>

[原記録](../../reports/phase6/base_headwise_gate_proposal.json) ／ SHA256: `15a06e61ef89b52dbfad517bdc849579d4ba83610f10efd6a45222871dd7a67e` ／ 8,899 bytes

| 原キー | 保存値 |
|---|---|
| status | "paired_static_vs_query_headwise_gate_defined_CPU_validated_GPU_unstarted" |
| hypothesis | "Add input-dependent nonlinearity between SDPA and output projection while retaining the parent function at initialization. Existing probability/optimizer changes have not delivered coherent generation. This is a literature-grounded adaptation hypothesis, not a diagnosed attention sink or proven remedy." |
| count_scope | "Both arms approximately10M and have exactly equal physical parameters; original native10,001,152 remains frozen. Static gates have zero gradients and stay zero. Not a same-inference-architecture claim." |
| teacher_policy | "Each exact100M original Web75M/textbook20M/story5M body+EOS teachers, OriginalTrainCorpusSampler including full metadata; original masks/draws/sequence order/fullstate. No new data, tokenization or role targets." |
| references.CPU_parity.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_parent_CPU_parity.json" |
| references.CPU_parity.sha256 | "f6af579f2fd09bb4eaad85d5e34864bcdfe79293a7a38c8666dc27e47323968c" |
| references.CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_model_tests.xml" |
| references.CPU_tests.sha256 | "d99f9100a5f53b5d627abfe438d3b942f6b2c21deeda579770e8efc14eeae17c" |
| references.initial_CPU_fixture_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_model_tests_initial.xml" |
| references.initial_CPU_fixture_failure.sha256 | "f056fc3b4d7714840e16bc29d3ddf16d860b3f256a7280fa4b228be2071dfd11" |
| source_sha256.tests/test_base_headwise_gate_model.py | "7780b1748c9fa739e9a0f565e3366510efb0b9cd4960792154bad0055eda8c14" |
| CPU_model_tests | 15 |
| probe_GPU_ceiling_seconds | 180 |
| total_GPU_ceiling_seconds | 9000 |
| prospective_budget_formula | "For EACH arm ceil(100M*sum(all32 completed step seconds)/sum(all32 original gold)*1.3+900 evaluation/save reserve); SUM both plus actual probe must fit9000. No subset timing or old FFN/MHA cap replacement." |
| before_GPU | ["Own trainer: exact all-parameter partition, partial-update refusal, typed config/arm/parent, full optimizer/scheduler/RNG/sampler/counters save/resume and original CE/mask/quotas CPU checks", "Own typed evaluator/runner/heartbeat/checkpoint/launcher and unchanged reviewer", "Own persisted CUDA4vs2+2 allstate/fullhistory and BF16 finite maximum48x1024, resident90percent limit, paired all32 timings and cumulative forecast"] |
| completion | "Both exited exact100M and all automatic evaluations/all160 content plus unchanged acceptance/archive/original idleUI/local commit, or explicit own numerical/state/resource-gate failure without science. Only a qualified candidate proceeds to independent trainedseed/fullDEV/protectedTEST/adoption." |
| failure | "Close this fixed headwise/query/zero-init/doubled-o_proj/parent/source/teacher/LR recipe on failure. No elementwise/head-share/bias/gain/init/LR/parent/source/batch/backend/decoder/teacher/cap rescue or automatic extension." |
| limitations | ["Mature-weight adaptation and added13,312 parameters differ from the paper setup", "Function-preserving conversion does not preserve native Adam dynamics; a new static matched arm is essential", "Repeated nonblind fixedDEV is not independent human/blind or final TEST", "Negative saturation marker does not diagnose a gating benefit; no capacity/improvement guarantee"] |
| scientific_configuration_frozen | false |
| scientific_started | false |
| GPU_seconds | 0 |
| new_scientific_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_query_headwise_notes.json — None</summary>

[原記録](../../reports/phase6/base_headwise_gate_query_headwise_notes.json) ／ SHA256: `36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a` ／ 16,834 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_headwise_gate_rating_reuse.json — None</summary>

[原記録](../../reports/phase6/base_headwise_gate_rating_reuse.json) ／ SHA256: `ff71e20c19717a6b7b321deb71f2a2e8d72ad272137c3e99a73916e367c777b0` ／ 45,292 bytes

| 原キー | 保存値 |
|---|---|
| arms.static_half.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_static_half_notes.json" |
| arms.static_half.notes.sha256 | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| arms.query_headwise.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_headwise_gate_query_headwise_notes.json" |
| arms.query_headwise.notes.sha256 | "36625ae14341af8c59971f698a9a78e6fc7643898749f0479c798edf8372575a" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| scope | "Exact text rating consistency, not independent human or new quality evaluation" |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_static_half_content_review.json — static_half_exact100M_autoevaluation_all80_individual_content_done_candidate_pending</summary>

[原記録](../../reports/phase6/base_headwise_gate_static_half_content_review.json) ／ SHA256: `5599b41b0c41ae371561e383a081d4bf2b9e36e957c7893863ca269dfcc0d1cb` ／ 1,420 bytes

| 原キー | 保存値 |
|---|---|
| rates.eos | 19 |
| rates.repetition | 45 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| BPB | 0.9984722020725625 |
| status | "static_half_exact100M_autoevaluation_all80_individual_content_done_candidate_pending" |
| training_teacher_tokens | 100000000 |
| grammar2 | 41 |
| relevance2 | 27 |
| notes_sha256 | "89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072" |
| common_dev_bytes | 472055 |
| checkpoint_sha256 | "5ae7d58dd8ed529679139a75237a40c3f92fbb6ff37cbb98d33a99e779fac886" |
| Base_complete | false |
| training_updates | 17698 |
| common_dev_documents | 256 |
| appropriate_completion | 2 |
| coherent2 | 1 |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_headwise_gate_static_half_notes.json — None</summary>

[原記録](../../reports/phase6/base_headwise_gate_static_half_notes.json) ／ SHA256: `89706f0a299407f3d846f90b8123529896cebe94ac7b7f85e3b0bd751113c072` ／ 17,166 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_kv_allocation_bucketed_completion.json — grouped_native_speed_prototype_complete_budget_not_ready</summary>

[原記録](../../reports/phase6/base_kv_allocation_bucketed_completion.json) ／ SHA256: `604dc6d65f15ffe2b7b78e3783cf6538b85799bc85134c1facb0c5fb26f613da` ／ 6,481 bytes

| 原キー | 保存値 |
|---|---|
| status | "grouped_native_speed_prototype_complete_budget_not_ready" |
| actual_paired_speed.GQA.flat_median_original_teachers_per_second | 53777.26789456038 |
| actual_paired_speed.GQA.grouped_median_original_teachers_per_second | 65778.03933244816 |
| actual_paired_speed.GQA.measured_ratio | 1.22315695660511 |
| actual_paired_speed.GQA.flat_physical_inputs | 1314080 |
| actual_paired_speed.GQA.grouped_physical_inputs | 435022 |
| actual_paired_speed.GQA.timed_original_teacher_positions | 308066 |
| actual_paired_speed.GQA.all_timing_steps_per_route | 32 |
| actual_paired_speed.GQA.grouped_data_wait_median_seconds | 0.005691619007848203 |
| actual_paired_speed.MHA.flat_median_original_teachers_per_second | 86100.55117972211 |
| actual_paired_speed.MHA.grouped_median_original_teachers_per_second | 68382.84114781811 |
| actual_paired_speed.MHA.measured_ratio | 0.7942207130019305 |
| actual_paired_speed.MHA.flat_physical_inputs | 1314080 |
| actual_paired_speed.MHA.grouped_physical_inputs | 435022 |
| actual_paired_speed.MHA.timed_original_teacher_positions | 308066 |
| actual_paired_speed.MHA.all_timing_steps_per_route | 32 |
| actual_paired_speed.MHA.grouped_data_wait_median_seconds | 0.005700765483197756 |
| native_numerical.GQA.loss_absolute_error | 1.1771917343139648e-06 |
| native_numerical.GQA.original_logical_teachers | 9178 |
| native_numerical.GQA.grouped_physical_inputs | 12734 |
| native_numerical.GQA.flat_physical_inputs | 32160 |
| native_numerical.GQA.passed | true |
| native_numerical.MHA.loss_absolute_error | 1.0911375284194946e-05 |
| native_numerical.MHA.original_logical_teachers | 9178 |
| native_numerical.MHA.grouped_physical_inputs | 12734 |
| native_numerical.MHA.flat_physical_inputs | 32160 |
| native_numerical.MHA.passed | true |
| native_full_context_capacity.GQA.passed | true |
| native_full_context_capacity.GQA.peak_VRAM_bytes | 17791501312 |
| native_full_context_capacity.GQA.context | 1024 |
| native_full_context_capacity.GQA.teachers | 40960 |
| native_full_context_capacity.GQA.physical_input_tokens | 81920 |
| native_full_context_capacity.GQA.loss | 8.290778160095215 |
| native_full_context_capacity.GQA.gradient_norm | 7.374273777008057 |
| native_full_context_capacity.GQA.optimizer_updates | 0 |
| native_full_context_capacity.MHA.passed | true |
| native_full_context_capacity.MHA.peak_VRAM_bytes | 17137935360 |
| native_full_context_capacity.MHA.context | 1024 |
| native_full_context_capacity.MHA.teachers | 40960 |
| native_full_context_capacity.MHA.physical_input_tokens | 81920 |
| native_full_context_capacity.MHA.loss | 8.295169830322266 |
| native_full_context_capacity.MHA.gradient_norm | 5.448677062988281 |
| native_full_context_capacity.MHA.optimizer_updates | 0 |
| all_resume_checks.GQA.kind | true |
| all_resume_checks.GQA.spec | true |
| all_resume_checks.GQA.binding | true |
| all_resume_checks.GQA.lineage | true |
| all_resume_checks.GQA.model_config | true |
| all_resume_checks.GQA.model | true |
| all_resume_checks.GQA.optimizer | true |
| all_resume_checks.GQA.scheduler | true |
| all_resume_checks.GQA.RNG | true |
| all_resume_checks.GQA.sampler | true |
| all_resume_checks.GQA.counters | true |
| all_resume_checks.GQA.finite | true |
| all_resume_checks.GQA.all_history_except_timing | true |
| all_resume_checks.MHA.kind | true |
| all_resume_checks.MHA.spec | true |
| all_resume_checks.MHA.binding | true |
| all_resume_checks.MHA.lineage | true |
| all_resume_checks.MHA.model_config | true |
| all_resume_checks.MHA.model | true |
| all_resume_checks.MHA.optimizer | true |
| all_resume_checks.MHA.scheduler | true |
| all_resume_checks.MHA.RNG | true |
| all_resume_checks.MHA.sampler | true |
| all_resume_checks.MHA.counters | true |
| all_resume_checks.MHA.finite | true |
| all_resume_checks.MHA.all_history_except_timing | true |
| full_original_source_sampler_identical | true |
| physical_padding_work_differs | true |
| bit_identical_old_CUDA_update_claimed | false |
| GPU_occupancy_seconds | 31.330358052975498 |
| total_actual_prototype_GPU_seconds | 55.82967330899555 |
| fixed_total_prototype_GPU_ceiling | 180 |
| forecast_all_new_GPU_seconds | 13489.829673308996 |
| fixed_all_new_GPU_ceiling | 9000 |
| science_caps_seconds.GQA | 6830 |
| science_caps_seconds.MHA | 6604 |
| science_budget_eligible | false |
| no_hidden_teacher_reduction_or_cap_increase | true |
| verification_updates | 156 |
| verification_teacher_positions | 1497876 |
| scientific_teacher_positions | 0 |
| interpretation | "Measured objective-preserving PAD efficiency on fixed32-step streams; floating accumulation differs within frozen native numerical tolerance. First-source short timing is a budget forecast, not full300M measurement or learned model quality. Flat-budget failure remains preserved." |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| archive.bytes | 3456783 |
| archive.archived_completion_is_pre_bundle_record | true |
| archive.compressed_bundle.bytes | 962478 |

</details>

<details>
<summary>reports/phase6/base_kv_allocation_probe_completion.json — paired_native_probe_complete_300M_protocol_closed_budget_exceeded</summary>

[原記録](../../reports/phase6/base_kv_allocation_probe_completion.json) ／ SHA256: `3c5bdaf0f6918eaeef7409396e5773a35efe2836c7a4a78eaa11180bd3a3f57e` ／ 4,130 bytes

| 原キー | 保存値 |
|---|---|
| status | "paired_native_probe_complete_300M_protocol_closed_budget_exceeded" |
| all_resume_checks.GQA.kind | true |
| all_resume_checks.GQA.spec | true |
| all_resume_checks.GQA.binding | true |
| all_resume_checks.GQA.lineage | true |
| all_resume_checks.GQA.model_config | true |
| all_resume_checks.GQA.model | true |
| all_resume_checks.GQA.optimizer | true |
| all_resume_checks.GQA.scheduler | true |
| all_resume_checks.GQA.RNG | true |
| all_resume_checks.GQA.sampler | true |
| all_resume_checks.GQA.counters | true |
| all_resume_checks.GQA.finite | true |
| all_resume_checks.GQA.token_schedule_accounting | true |
| all_resume_checks.GQA.all_history_except_timing | true |
| all_resume_checks.MHA.kind | true |
| all_resume_checks.MHA.spec | true |
| all_resume_checks.MHA.binding | true |
| all_resume_checks.MHA.lineage | true |
| all_resume_checks.MHA.model_config | true |
| all_resume_checks.MHA.model | true |
| all_resume_checks.MHA.optimizer | true |
| all_resume_checks.MHA.scheduler | true |
| all_resume_checks.MHA.RNG | true |
| all_resume_checks.MHA.sampler | true |
| all_resume_checks.MHA.counters | true |
| all_resume_checks.MHA.finite | true |
| all_resume_checks.MHA.token_schedule_accounting | true |
| all_resume_checks.MHA.all_history_except_timing | true |
| GPU_occupancy_seconds | 24.499315256020054 |
| forecast_all_new_GPU_seconds | 12145.49931525602 |
| fixed_all_new_GPU_ceiling | 9000 |
| science_budget_eligible | false |
| fixed_300M_allocation_protocol_closed | true |
| no_cap_increase_or_hidden_teacher_reduction | true |
| verification_updates | 90 |
| verification_teacher_positions | 803658 |
| scientific_teacher_positions | 0 |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| interpretation | "Native finite capacity/resume evidence is not learned model quality. Short first-source timings are a forecast; they do not prove full300M duration. Keep measured ceilings and all quality gates." |
| archive.bytes | 2924089 |
| archive.archived_completion_is_pre_bundle_record | true |
| archive.compressed_bundle.bytes | 796941 |

</details>

<details>
<summary>reports/phase6/base_kv_allocation_proposal.json — fixed_attention_allocation_proposal_CPU_counted_not_GPU_learning</summary>

[原記録](../../reports/phase6/base_kv_allocation_proposal.json) ／ SHA256: `50a1a07e82ffe17b6046374b2cb9e00f5a0a03cfdd72b5d5b76cbb08b6149f2f` ／ 10,720 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_attention_allocation_proposal_CPU_counted_not_GPU_learning" |
| causal_limit | "Opposition/cancellation are local observations, but the summed gradient supports both head paths in all26 group/source aggregates. This does not justify head-PCGrad, prove GQA causality or guarantee MHA quality." |
| variants.GQA.status | "phase5_ablation" |
| variants.MHA.status | "CPU_parameter_count_only" |
| actual_CPU_meta_parameter_counts.GQA | 10001152 |
| actual_CPU_meta_parameter_counts.MHA | 10054400 |
| interpretation | "Joint attention-versus-FFN allocation: KV2/FFN640 versus KV4/FFN560. Same13 layers/hidden256/query4/head64/Tokenizer4096/NoNorm/SwiGLU/RoPE1024/tied embeddings. Not isolated KV causality or exactly equal parameter count." |
| primary_teacher_tokens_per_arm | 300000000 |
| total_new_teacher_tokens | 600000000 |
| optimizer.seed | 42 |
| probe.total_GPU_cap_seconds | 180 |
| probe.warmup_steps | 3 |
| probe.timed_steps | 5 |
| probe.worst_teacher_stride | 512 |
| absolute_all_new_GPU_ceiling_seconds | 9000 |
| science_budget_rule | "After actual probe only: sum ceil(300M/measured_median_original_teachers_per_second*1.3+900) for both arms plus actual prototype GPU &lt;=9000s. Otherwise do not launch or raise the cap." |
| CPU_preparation_ceiling_seconds | 30 |
| protected_test_used | false |
| failure_policy | "One MHA4/FFN560 configuration. No KV/head/FFN/depth/width/Tokenizer/LR/source/checkpoint/epoch rescue or automatic teacher extension. Close allocation if research transfer screen fails. A positive signal needs a separate measured continuation contract, never automatic Base adoption." |
| completion | "Actual exited bounded two-arm300M jobs, exact teacher/full native state/source accounting, own CUDA resume, fixed evaluations and all160 individual contents, comparisons/decision, negative evidence/UI restoration/local commit. Code/random weights/probe do not complete the study or Base." |
| required_before_GPU_learning | ["CE-only source parity and meaningful CPU state checks", "Own fresh trainer/runner/evaluator/reviewer and durable launcher", "Measured CUDA/BF16 stable batch and full save/resume for both native architectures", "Freeze science source/config/budget after actual protocol passes and process inspection"] |
| implementation_status | "Scientific commands not yet implemented; do not invoke nonexistent commands." |
| actual_GPU_learning_seconds | 0 |
| actual_scientific_teacher_tokens | 0 |
| preparation_CPU_seconds | 1.1062847759749275 |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_active_job.json — fresh_paired_residual4B_review_complete_rejected_Base_pending</summary>

[原記録](../../reports/phase6/base_parallel_residual_active_job.json) ／ SHA256: `0055290807a77be73d22c4064c55f0359472c5f6f8cd1cb24cfb2e6bdcaccb45` ／ 106,546 bytes

| 原キー | 保存値 |
|---|---|
| prospective_total_GPU_cap_seconds | 86400 |
| Base_complete | false |
| scientific_original_gold_each | 2000000000 |
| maximum_cumulative_science_GPU_seconds | 81736 |
| own_probe_GPU_seconds | 21.3907036060009 |
| heartbeat_every_updates | 20 |
| status | "fresh_paired_residual4B_review_complete_rejected_Base_pending" |
| job_snapshot.status | "complete" |
| job_snapshot.GPU_occupancy_seconds | 52093.681041047006 |
| job_snapshot.cumulative_GPU_ledger_closed | true |
| job_snapshot.Base_complete | false |
| job_snapshot.memory_policy.visible_device_bytes | 25756696576 |
| job_snapshot.memory_policy.allocator_allowance_bytes | 23181026918 |
| job_snapshot.memory_policy.expected_worst_peak_bytes | 17791499264 |
| job_snapshot.completed_updates | 212080 |
| job_snapshot.original_teachers | 1999868016 |
| job_snapshot.CE_loss | 2.5558743476867676 |
| job_snapshot.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| checkpoint_every_updates | 2000 |
| scientific_original_gold_total | 4000000000 |
| Base_adopted | false |
| first_checkpoint_verification | "reports/phase6/base_parallel_residual_first_checkpoint_verification.json" |
| sequential_100m_milestone.GPU_occupancy_seconds | 1451.7218110850008 |
| sequential_100m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00010000.pt" |
| sequential_100m_milestone.completed_updates | 11180 |
| sequential_100m_milestone.original_teachers | 105299687 |
| sequential_100m_milestone.current_CE_loss | 2.9926531314849854 |
| sequential_100m_milestone.Base_complete | false |
| sequential_200m_milestone.original_teachers | 206140134 |
| sequential_200m_milestone.GPU_occupancy_seconds | 2755.307826397002 |
| sequential_200m_milestone.current_CE_loss | 2.983218193054199 |
| sequential_200m_milestone.completed_updates | 21880 |
| sequential_200m_milestone.Base_complete | false |
| sequential_200m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00020000.pt" |
| sequential_300m_milestone.original_teachers | 303086178 |
| sequential_300m_milestone.completed_updates | 32160 |
| sequential_300m_milestone.current_CE_loss | 2.833634853363037 |
| sequential_300m_milestone.GPU_occupancy_seconds | 4004.7015123160018 |
| sequential_300m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00032000.pt" |
| sequential_300m_milestone.checkpoint_bytes | 124374525 |
| sequential_300m_milestone.Base_complete | false |
| sequential_400m_milestone.original_teachers | 404328211 |
| sequential_400m_milestone.completed_updates | 42900 |
| sequential_400m_milestone.current_CE_loss | 2.908163547515869 |
| sequential_400m_milestone.GPU_occupancy_seconds | 5312.325280296001 |
| sequential_400m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00042000.pt" |
| sequential_400m_milestone.checkpoint_bytes | 124374461 |
| sequential_400m_milestone.Base_complete | false |
| sequential_500m_milestone.original_teachers | 501946870 |
| sequential_500m_milestone.completed_updates | 53260 |
| sequential_500m_milestone.current_CE_loss | 2.927281141281128 |
| sequential_500m_milestone.GPU_occupancy_seconds | 6576.700487800001 |
| sequential_500m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00052000.pt" |
| sequential_500m_milestone.checkpoint_bytes | 124374397 |
| sequential_500m_milestone.Base_complete | false |
| sequential_600m_milestone.original_teachers | 601894200 |
| sequential_600m_milestone.completed_updates | 63860 |
| sequential_600m_milestone.current_CE_loss | 2.853844165802002 |
| sequential_600m_milestone.GPU_occupancy_seconds | 7864.0987305160015 |
| sequential_600m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00062000.pt" |
| sequential_600m_milestone.checkpoint_bytes | 124374461 |
| sequential_600m_milestone.Base_complete | false |
| sequential_700m_milestone.original_teachers | 702906249 |
| sequential_700m_milestone.completed_updates | 74560 |
| sequential_700m_milestone.current_CE_loss | 2.843104124069214 |
| sequential_700m_milestone.GPU_occupancy_seconds | 9176.763652823 |
| sequential_700m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00074000.pt" |
| sequential_700m_milestone.checkpoint_bytes | 124374525 |
| sequential_700m_milestone.Base_complete | false |
| sequential_800m_milestone.original_teachers | 802202171 |
| sequential_800m_milestone.completed_updates | 85080 |
| sequential_800m_milestone.current_CE_loss | 2.8714520931243896 |
| sequential_800m_milestone.GPU_occupancy_seconds | 10464.981423135 |
| sequential_800m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00084000.pt" |
| sequential_800m_milestone.checkpoint_bytes | 124374461 |
| sequential_800m_milestone.Base_complete | false |
| sequential_900m_milestone.original_teachers | 901899764 |
| sequential_900m_milestone.completed_updates | 95660 |
| sequential_900m_milestone.current_CE_loss | 2.878662586212158 |
| sequential_900m_milestone.GPU_occupancy_seconds | 11757.873787513 |
| sequential_900m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00094000.pt" |
| sequential_900m_milestone.checkpoint_bytes | 124374525 |
| sequential_900m_milestone.Base_complete | false |
| sequential_1000m_milestone.original_teachers | 1000881919 |
| sequential_1000m_milestone.completed_updates | 106160 |
| sequential_1000m_milestone.current_CE_loss | 2.9097299575805664 |
| sequential_1000m_milestone.GPU_occupancy_seconds | 13029.276230158 |
| sequential_1000m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00106000.pt" |
| sequential_1000m_milestone.checkpoint_bytes | 124374525 |
| sequential_1000m_milestone.Base_complete | false |
| sequential_1100m_milestone.original_teachers | 1100882951 |
| sequential_1100m_milestone.completed_updates | 116760 |
| sequential_1100m_milestone.current_CE_loss | 2.758920192718506 |
| sequential_1100m_milestone.GPU_occupancy_seconds | 14323.970477911 |
| sequential_1100m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00116000.pt" |
| sequential_1100m_milestone.checkpoint_bytes | 124374397 |
| sequential_1100m_milestone.Base_complete | false |
| sequential_1200m_milestone.original_teachers | 1201132483 |
| sequential_1200m_milestone.completed_updates | 127400 |
| sequential_1200m_milestone.current_CE_loss | 2.7948102951049805 |
| sequential_1200m_milestone.GPU_occupancy_seconds | 15612.454642992001 |
| sequential_1200m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00126000.pt" |
| sequential_1200m_milestone.checkpoint_bytes | 124374461 |
| sequential_1200m_milestone.Base_complete | false |
| sequential_1300m_milestone.original_teachers | 1301054553 |
| sequential_1300m_milestone.completed_updates | 138000 |
| sequential_1300m_milestone.current_CE_loss | 2.556943416595459 |
| sequential_1300m_milestone.GPU_occupancy_seconds | 16893.832896197 |
| sequential_1300m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00138000.pt" |
| sequential_1300m_milestone.checkpoint_bytes | 124374525 |
| sequential_1300m_milestone.Base_complete | false |
| sequential_1400m_milestone.original_teachers | 1400914701 |
| sequential_1400m_milestone.completed_updates | 148580 |
| sequential_1400m_milestone.current_CE_loss | 2.707296848297119 |
| sequential_1400m_milestone.GPU_occupancy_seconds | 18185.953382393 |
| sequential_1400m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00148000.pt" |
| sequential_1400m_milestone.checkpoint_bytes | 124374525 |
| sequential_1400m_milestone.Base_complete | false |
| sequential_1500m_milestone.original_teachers | 1501020091 |
| sequential_1500m_milestone.completed_updates | 159200 |
| sequential_1500m_milestone.current_CE_loss | 2.6731574535369873 |
| sequential_1500m_milestone.GPU_occupancy_seconds | 19477.735565965002 |
| sequential_1500m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00158000.pt" |
| sequential_1500m_milestone.checkpoint_bytes | 124374525 |
| sequential_1500m_milestone.Base_complete | false |
| sequential_1600m_milestone.original_teachers | 1600782290 |
| sequential_1600m_milestone.completed_updates | 169780 |
| sequential_1600m_milestone.current_CE_loss | 2.5481982231140137 |
| sequential_1600m_milestone.GPU_occupancy_seconds | 20769.276825652003 |
| sequential_1600m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00168000.pt" |
| sequential_1600m_milestone.checkpoint_bytes | 124374525 |
| sequential_1600m_milestone.Base_complete | false |
| sequential_1700m_milestone.original_teachers | 1701006515 |
| sequential_1700m_milestone.completed_updates | 180400 |
| sequential_1700m_milestone.current_CE_loss | 2.470109462738037 |
| sequential_1700m_milestone.GPU_occupancy_seconds | 22067.807397401997 |
| sequential_1700m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00180000.pt" |
| sequential_1700m_milestone.checkpoint_bytes | 124374525 |
| sequential_1700m_milestone.Base_complete | false |
| sequential_1800m_milestone.original_teachers | 1801147629 |
| sequential_1800m_milestone.completed_updates | 191020 |
| sequential_1800m_milestone.current_CE_loss | 2.4768755435943604 |
| sequential_1800m_milestone.GPU_occupancy_seconds | 23359.408588413 |
| sequential_1800m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00190000.pt" |
| sequential_1800m_milestone.checkpoint_bytes | 124374525 |
| sequential_1800m_milestone.Base_complete | false |
| sequential_1900m_milestone.original_teachers | 1900965709 |
| sequential_1900m_milestone.completed_updates | 201600 |
| sequential_1900m_milestone.current_CE_loss | 2.5439364910125732 |
| sequential_1900m_milestone.GPU_occupancy_seconds | 24642.810096195 |
| sequential_1900m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00200000.pt" |
| sequential_1900m_milestone.checkpoint_bytes | 124374461 |
| sequential_1900m_milestone.Base_complete | false |
| sequential_2b_training_completion.observed_at | "2026-10-07T18:30:11.6618694Z" |
| sequential_2b_training_completion.status | "sequential_training_complete_evaluation_and_parallel_arm_pending" |
| sequential_2b_training_completion.actual_process_identity.start_ticks | "1498217" |
| sequential_2b_training_completion.actual_process_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| sequential_2b_training_completion.actual_process_identity.pid | 31561 |
| sequential_2b_training_completion.training_result | "reports/phase6/base_parallel_residual_sequential_training_result.json" |
| sequential_2b_training_completion.training_result_sha256 | "a55959a821d9880609be22576b86d1f7f9ee7c373fb98378eb3de6a2ffc36b54" |
| sequential_2b_training_completion.scientific_CE_teacher_tokens | 2000000000 |
| sequential_2b_training_completion.counters.update | 212095 |
| sequential_2b_training_completion.counters.supervised_tokens | 2000000000 |
| sequential_2b_training_completion.counters.CE_input_tokens | 2053285089 |
| sequential_2b_training_completion.counters.auxiliary_input_tokens | 0 |
| sequential_2b_training_completion.counters.auxiliary_pairs | 0 |
| sequential_2b_training_completion.counters.physical_input_tokens | 8620194616 |
| sequential_2b_training_completion.counters.original_body_bytes | 8118116484 |
| sequential_2b_training_completion.counters.token_digest | "50452c1e5fccc0928a4b1acce06171b4a869c4251c6efc645348430e6b41d51d" |
| sequential_2b_training_completion.counters.source_teachers.web | 1500000000 |
| sequential_2b_training_completion.counters.source_teachers.textbook | 400000000 |
| sequential_2b_training_completion.counters.source_teachers.story | 100000000 |
| sequential_2b_training_completion.counters.source_EOS.web | 13131989 |
| sequential_2b_training_completion.counters.source_EOS.textbook | 2967040 |
| sequential_2b_training_completion.counters.source_EOS.story | 764589 |
| sequential_2b_training_completion.scheduler.kind | "original_teacher_end_position_warmup_cosine_v1" |
| sequential_2b_training_completion.scheduler.total | 2000000000 |
| sequential_2b_training_completion.scheduler.warmup | 5000000 |
| sequential_2b_training_completion.scheduler.peak | 0.002 |
| sequential_2b_training_completion.scheduler.final | 1e-05 |
| sequential_2b_training_completion.scheduler.tokens | 2000000000 |
| sequential_2b_training_completion.scheduler.last_lr | 1e-05 |
| sequential_2b_training_completion.spec.kind | "fresh_equal_parameter_residual_connectivity_original_TRAIN_gold_token_schedule_v1" |
| sequential_2b_training_completion.spec.batch | 80 |
| sequential_2b_training_completion.spec.seed | 42 |
| sequential_2b_training_completion.spec.optimizer | "fresh_AdamW_actual_residual_parameters_once" |
| sequential_2b_training_completion.spec.weight_decay | 0.1 |
| sequential_2b_training_completion.spec.gradient_clip | 1.0 |
| sequential_2b_training_completion.spec.dtype | "bf16" |
| sequential_2b_training_completion.spec.backend | "flash" |
| sequential_2b_training_completion.spec.actual_unique_parameters | 10001152 |
| sequential_2b_training_completion.spec.goals.web | 1500000000 |
| sequential_2b_training_completion.spec.goals.textbook | 400000000 |
| sequential_2b_training_completion.spec.goals.story | 100000000 |
| sequential_2b_training_completion.spec.scheduler.kind | "original_teacher_end_position_warmup_cosine_v1" |
| sequential_2b_training_completion.spec.scheduler.total | 2000000000 |
| sequential_2b_training_completion.spec.scheduler.warmup | 5000000 |
| sequential_2b_training_completion.spec.scheduler.peak | 0.002 |
| sequential_2b_training_completion.spec.scheduler.final | 1e-05 |
| sequential_2b_training_completion.spec.head_policy | "only_original_supervised_states" |
| sequential_2b_training_completion.spec.CE_policy | "document_local1024_context512_original_targets_once" |
| sequential_2b_training_completion.spec.contrast | false |
| sequential_2b_training_completion.spec.arm | "sequential" |
| sequential_2b_training_completion.spec.residual_policy.kind | "same_input_attention_FFN_separate_native_RMSNorm_v1" |
| sequential_2b_training_completion.spec.residual_policy.formula | "x+Attention(RMS1(x))+SwiGLU(RMS2(x))" |
| sequential_2b_training_completion.spec.residual_policy.norm_weights_tied | false |
| sequential_2b_training_completion.spec.residual_policy.residual_gain | 1.0 |
| sequential_2b_training_completion.spec.residual_policy.additional_parameters | 0 |
| sequential_2b_training_completion.spec.residual_policy.physical_block_invocations | 1 |
| sequential_2b_training_completion.spec.residual_policy.initialization | "identical_fresh_native_matrices" |
| sequential_2b_training_completion.spec.model_class | "JMicroModel" |
| sequential_2b_training_completion.lineage.kind | "fresh_equal_parameter_residual_connectivity_original_TRAIN_gold_token_schedule_v1" |
| sequential_2b_training_completion.lineage.initialization | "fresh_native_seed" |
| sequential_2b_training_completion.lineage.seed | 42 |
| sequential_2b_training_completion.lineage.parent | null |
| sequential_2b_training_completion.lineage.learned_parent_weights_used | false |
| sequential_2b_training_completion.lineage.probe_weights_used | false |
| sequential_2b_training_completion.lineage.weights_role | "scientific_fresh_paired_residual" |
| sequential_2b_training_completion.lineage.arm | "sequential" |
| sequential_2b_training_completion.lineage.residual_initialization | "identical_native_initial_weights_no_extra_RNG" |
| sequential_2b_training_completion.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| sequential_2b_training_completion.checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| sequential_2b_training_completion.checkpoint_bytes | 124374525 |
| sequential_2b_training_completion.quality_evaluation_complete | false |
| sequential_2b_training_completion.Base_complete | false |
| parallel_training_started.observed_at | "2026-10-07T18:32:10.2327279Z" |
| parallel_training_started.actual_process_identity.start_ticks | "1498217" |
| parallel_training_started.actual_process_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| parallel_training_started.actual_process_identity.pid | 31561 |
| parallel_training_started.original_teachers | 6209424 |
| parallel_training_started.completed_updates | 660 |
| parallel_training_started.CE_loss | 3.897742748260498 |
| parallel_training_started.GPU_occupancy_seconds | 26109.006321903 |
| parallel_training_started.sequential_automated_evaluation_completed_at | "2026-10-07T18:30:48.48705Z" |
| parallel_training_started.sequential_automated_evaluation_result | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/evaluation/sequential/evaluation/result.json" |
| parallel_training_started.sequential_automated_evaluation_result_sha256 | "8ca51cf98d9b787619bd08805f6745c736bb1aa3d565f9dad4b1a13dd69fe2bb" |
| parallel_training_started.personally_read_current_generation_cases | 0 |
| parallel_training_started.comparison_quality_review_complete | false |
| parallel_training_started.Base_complete | false |
| parallel_100m_milestone.original_teachers | 101147290 |
| parallel_100m_milestone.completed_updates | 10740 |
| parallel_100m_milestone.current_CE_loss | 2.9728496074676514 |
| parallel_100m_milestone.GPU_occupancy_seconds | 27338.895913399003 |
| parallel_100m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00010000.pt" |
| parallel_100m_milestone.checkpoint_bytes | 124374589 |
| parallel_100m_milestone.Base_complete | false |
| parallel_200m_milestone.original_teachers | 201414263 |
| parallel_200m_milestone.completed_updates | 21380 |
| parallel_200m_milestone.current_CE_loss | 2.864327907562256 |
| parallel_200m_milestone.GPU_occupancy_seconds | 28643.869075332997 |
| parallel_200m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00020000.pt" |
| parallel_200m_milestone.checkpoint_bytes | 124374589 |
| parallel_200m_milestone.Base_complete | false |
| parallel_300m_milestone.original_teachers | 300453604 |
| parallel_300m_milestone.completed_updates | 31880 |
| parallel_300m_milestone.current_CE_loss | 2.9040210247039795 |
| parallel_300m_milestone.GPU_occupancy_seconds | 29926.521876381 |
| parallel_300m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00030000.pt" |
| parallel_300m_milestone.checkpoint_bytes | 124374589 |
| parallel_300m_milestone.Base_complete | false |
| parallel_400m_milestone.original_teachers | 402825272 |
| parallel_400m_milestone.completed_updates | 42740 |
| parallel_400m_milestone.current_CE_loss | 2.9991376399993896 |
| parallel_400m_milestone.GPU_occupancy_seconds | 31258.061234326004 |
| parallel_400m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00042000.pt" |
| parallel_400m_milestone.checkpoint_bytes | 124374589 |
| parallel_400m_milestone.Base_complete | false |
| parallel_500m_milestone.original_teachers | 501569904 |
| parallel_500m_milestone.completed_updates | 53220 |
| parallel_500m_milestone.current_CE_loss | 2.874835729598999 |
| parallel_500m_milestone.GPU_occupancy_seconds | 32544.473051484998 |
| parallel_500m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00052000.pt" |
| parallel_500m_milestone.checkpoint_bytes | 124374525 |
| parallel_500m_milestone.Base_complete | false |
| parallel_600m_milestone.original_teachers | 601512945 |
| parallel_600m_milestone.completed_updates | 63820 |
| parallel_600m_milestone.current_CE_loss | 2.8758490085601807 |
| parallel_600m_milestone.GPU_occupancy_seconds | 33838.727391715 |
| parallel_600m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00062000.pt" |
| parallel_600m_milestone.checkpoint_bytes | 124374589 |
| parallel_600m_milestone.Base_complete | false |
| parallel_700m_milestone.original_teachers | 702716196 |
| parallel_700m_milestone.completed_updates | 74540 |
| parallel_700m_milestone.current_CE_loss | 2.9488236904144287 |
| parallel_700m_milestone.GPU_occupancy_seconds | 35157.642079436 |
| parallel_700m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00074000.pt" |
| parallel_700m_milestone.checkpoint_bytes | 124374653 |
| parallel_700m_milestone.Base_complete | false |
| parallel_800m_milestone.original_teachers | 803327900 |
| parallel_800m_milestone.completed_updates | 85200 |
| parallel_800m_milestone.current_CE_loss | 2.7950315475463867 |
| parallel_800m_milestone.GPU_occupancy_seconds | 36467.686707752 |
| parallel_800m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00084000.pt" |
| parallel_800m_milestone.checkpoint_bytes | 124374589 |
| parallel_800m_milestone.Base_complete | false |
| parallel_900m_milestone.original_teachers | 900956808 |
| parallel_900m_milestone.completed_updates | 95560 |
| parallel_900m_milestone.current_CE_loss | 2.826275587081909 |
| parallel_900m_milestone.GPU_occupancy_seconds | 37738.638926194006 |
| parallel_900m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00094000.pt" |
| parallel_900m_milestone.checkpoint_bytes | 124374589 |
| parallel_900m_milestone.Base_complete | false |
| parallel_1000m_milestone.original_teachers | 1000881919 |
| parallel_1000m_milestone.completed_updates | 106160 |
| parallel_1000m_milestone.current_CE_loss | 2.91886568069458 |
| parallel_1000m_milestone.GPU_occupancy_seconds | 39027.520733599 |
| parallel_1000m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00106000.pt" |
| parallel_1000m_milestone.checkpoint_bytes | 124374653 |
| parallel_1000m_milestone.Base_complete | false |
| parallel_1100m_milestone.original_teachers | 1100882951 |
| parallel_1100m_milestone.completed_updates | 116760 |
| parallel_1100m_milestone.current_CE_loss | 2.787705659866333 |
| parallel_1100m_milestone.GPU_occupancy_seconds | 40328.637204112005 |
| parallel_1100m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00116000.pt" |
| parallel_1100m_milestone.checkpoint_bytes | 124374525 |
| parallel_1100m_milestone.Base_complete | false |
| parallel_1200m_milestone.original_teachers | 1202067427 |
| parallel_1200m_milestone.completed_updates | 127500 |
| parallel_1200m_milestone.current_CE_loss | 2.5836093425750732 |
| parallel_1200m_milestone.GPU_occupancy_seconds | 41635.417433644005 |
| parallel_1200m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00126000.pt" |
| parallel_1200m_milestone.checkpoint_bytes | 124374589 |
| parallel_1200m_milestone.Base_complete | false |
| parallel_1300m_milestone.original_teachers | 1301054553 |
| parallel_1300m_milestone.completed_updates | 138000 |
| parallel_1300m_milestone.current_CE_loss | 2.5816733837127686 |
| parallel_1300m_milestone.GPU_occupancy_seconds | 42913.308666888 |
| parallel_1300m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00138000.pt" |
| parallel_1300m_milestone.checkpoint_bytes | 124374589 |
| parallel_1300m_milestone.Base_complete | false |
| parallel_1400m_milestone.original_teachers | 1401288720 |
| parallel_1400m_milestone.completed_updates | 148620 |
| parallel_1400m_milestone.current_CE_loss | 2.627995252609253 |
| parallel_1400m_milestone.GPU_occupancy_seconds | 44217.50037858701 |
| parallel_1400m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00148000.pt" |
| parallel_1400m_milestone.checkpoint_bytes | 124374589 |
| parallel_1400m_milestone.Base_complete | false |
| parallel_1500m_milestone.original_teachers | 1501020091 |
| parallel_1500m_milestone.completed_updates | 159200 |
| parallel_1500m_milestone.current_CE_loss | 2.674556016921997 |
| parallel_1500m_milestone.GPU_occupancy_seconds | 45512.553783990996 |
| parallel_1500m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00158000.pt" |
| parallel_1500m_milestone.checkpoint_bytes | 124374653 |
| parallel_1500m_milestone.Base_complete | false |
| parallel_1600m_milestone.original_teachers | 1601352045 |
| parallel_1600m_milestone.completed_updates | 169840 |
| parallel_1600m_milestone.current_CE_loss | 2.601228713989258 |
| parallel_1600m_milestone.GPU_occupancy_seconds | 46819.759224851994 |
| parallel_1600m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00168000.pt" |
| parallel_1600m_milestone.checkpoint_bytes | 124374653 |
| parallel_1600m_milestone.Base_complete | false |
| parallel_1700m_milestone.original_teachers | 1701195865 |
| parallel_1700m_milestone.completed_updates | 180420 |
| parallel_1700m_milestone.current_CE_loss | 2.5465474128723145 |
| parallel_1700m_milestone.GPU_occupancy_seconds | 48121.339457483 |
| parallel_1700m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00180000.pt" |
| parallel_1700m_milestone.checkpoint_bytes | 124374653 |
| parallel_1700m_milestone.Base_complete | false |
| parallel_1800m_milestone.original_teachers | 1800773310 |
| parallel_1800m_milestone.completed_updates | 190980 |
| parallel_1800m_milestone.current_CE_loss | 2.4837656021118164 |
| parallel_1800m_milestone.GPU_occupancy_seconds | 49412.857339672 |
| parallel_1800m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00190000.pt" |
| parallel_1800m_milestone.checkpoint_bytes | 124374589 |
| parallel_1800m_milestone.Base_complete | false |
| parallel_1900m_milestone.original_teachers | 1900781319 |
| parallel_1900m_milestone.completed_updates | 201580 |
| parallel_1900m_milestone.current_CE_loss | 2.458820343017578 |
| parallel_1900m_milestone.GPU_occupancy_seconds | 50704.9133877 |
| parallel_1900m_milestone.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00200000.pt" |
| parallel_1900m_milestone.checkpoint_bytes | 124374589 |
| parallel_1900m_milestone.Base_complete | false |
| both_2b_autoevaluation_completion.observed_at | "2026-10-08T01:47:04.7831423Z" |
| both_2b_autoevaluation_completion.actual_process_absent | true |
| both_2b_autoevaluation_completion.durable_launcher_exit_code | 0 |
| both_2b_autoevaluation_completion.result_path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/result.json" |
| both_2b_autoevaluation_completion.result_sha256 | "4c6f9057c685450ee32eafedcd64538676f868022a81317fb7d3d584edfe3f2a" |
| both_2b_autoevaluation_completion.scientific_CE_teacher_tokens | 4000000000 |
| both_2b_autoevaluation_completion.GPU_occupancy_seconds | 52093.681041047006 |
| both_2b_autoevaluation_completion.total_GPU_seconds_including_probe | 52115.071744653 |
| both_2b_autoevaluation_completion.cumulative_GPU_ledger_closed | true |
| both_2b_autoevaluation_completion.paired_stream_checks.full_counters | true |
| both_2b_autoevaluation_completion.paired_stream_checks.full_sampler | true |
| both_2b_autoevaluation_completion.paired_stream_checks.full_scheduler | true |
| both_2b_autoevaluation_completion.parallel_training_result_sha256 | "ae6ceb456354523b7a26e6a9d4c9a5d632b78955d643599526745a36f73a3fad" |
| both_2b_autoevaluation_completion.parallel_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| both_2b_autoevaluation_completion.parallel_checkpoint_sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| both_2b_autoevaluation_completion.current160_individually_read | 0 |
| both_2b_autoevaluation_completion.quality_review_complete | false |
| both_2b_autoevaluation_completion.Base_complete | false |
| both_2b_autoevaluation_completion.read_only_CPU_terminal_fullstate_and_history_audit_passed | true |
| both_2b_autoevaluation_completion.all160_unscored_templates_created | true |
| both_2b_autoevaluation_completion.original_10b_UI_restored.observed_at | "2026-10-08T01:47:42.4080257Z" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.identity.pid | 73540 |
| both_2b_autoevaluation_completion.original_10b_UI_restored.identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.identity.start_ticks | "6707984" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.actual_alive | true |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.name | "JMicro-10M" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.kind | "Base / 文章の続き" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.parameters | 10001152 |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.training_tokens | 10000007168 |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.update | 305176 |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.device | "NVIDIA GeForce RTX 4090" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.precision | "BF16 / math attention" |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.context | 1024 |
| both_2b_autoevaluation_completion.original_10b_UI_restored.model.busy | false |
| closeout.status | "fresh_paired_residual4B_review_complete" |
| closeout.scientific_CE_teacher_tokens | 4000000000 |
| closeout.checkpoints.sequential.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| closeout.checkpoints.sequential.sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| closeout.checkpoints.parallel.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| closeout.checkpoints.parallel.sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| closeout.residual_policy.physical_block_invocations | 1 |
| closeout.added_physical_parameters_each | 0 |
| closeout.GPU_occupancy_seconds | 52093.681041047006 |
| closeout.GPU_cap_seconds | 81736 |
| closeout.total_GPU_seconds_including_probe | 52115.071744653 |
| closeout.summaries.strong_staged.BPB | 1.1336128657420816 |
| closeout.summaries.strong_staged.rates.eos | 76 |
| closeout.summaries.strong_staged.rates.repetition | 2 |
| closeout.summaries.strong_staged.rates.unicode_failure | 0 |
| closeout.summaries.strong_staged.rates.role_leak | 0 |
| closeout.summaries.strong_staged.rates.empty | 0 |
| closeout.summaries.strong_staged.grammar2 | 65 |
| closeout.summaries.strong_staged.relevance2 | 39 |
| closeout.summaries.strong_staged.coherent | 23 |
| closeout.summaries.strong_staged.appropriate | 26 |
| closeout.summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| closeout.summaries.sequential.BPB | 1.1063855998175087 |
| closeout.summaries.sequential.rates.eos | 20 |
| closeout.summaries.sequential.rates.repetition | 27 |
| closeout.summaries.sequential.rates.unicode_failure | 0 |
| closeout.summaries.sequential.rates.role_leak | 0 |
| closeout.summaries.sequential.rates.empty | 0 |
| closeout.summaries.sequential.grammar2 | 23 |
| closeout.summaries.sequential.relevance2 | 30 |
| closeout.summaries.sequential.coherent | 3 |
| closeout.summaries.sequential.appropriate | 7 |
| closeout.summaries.sequential.notes_sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| closeout.summaries.parallel.BPB | 1.102009028125384 |
| closeout.summaries.parallel.rates.eos | 22 |
| closeout.summaries.parallel.rates.repetition | 28 |
| closeout.summaries.parallel.rates.unicode_failure | 0 |
| closeout.summaries.parallel.rates.role_leak | 0 |
| closeout.summaries.parallel.rates.empty | 0 |
| closeout.summaries.parallel.grammar2 | 20 |
| closeout.summaries.parallel.relevance2 | 38 |
| closeout.summaries.parallel.coherent | 2 |
| closeout.summaries.parallel.appropriate | 7 |
| closeout.summaries.parallel.notes_sha256 | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| closeout.summaries.cached_CE.BPB | 0.998487162513845 |
| closeout.summaries.cached_CE.rates.eos | 19 |
| closeout.summaries.cached_CE.rates.repetition | 45 |
| closeout.summaries.cached_CE.rates.unicode_failure | 0 |
| closeout.summaries.cached_CE.rates.role_leak | 0 |
| closeout.summaries.cached_CE.rates.empty | 0 |
| closeout.summaries.cached_CE.grammar2 | 44 |
| closeout.summaries.cached_CE.relevance2 | 25 |
| closeout.summaries.cached_CE.coherent | 2 |
| closeout.summaries.cached_CE.appropriate | 2 |
| closeout.summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| closeout.eligible_for_final_Base_validation | false |
| closeout.fixed_parallel_residual_condition_closed | true |
| closeout.archive.bytes | 3612897752 |
| closeout.UI_restored.model.training_tokens | 10000007168 |
| closeout.UI_restored.model.update | 305176 |
| closeout.UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| closeout.UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| closeout.UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| closeout.Base_complete | false |
| closeout.Base_adopted | false |
| closeout.protected_test_scored | false |
| quality_review.summaries.strong_staged.BPB | 1.1336128657420816 |
| quality_review.summaries.strong_staged.rates.eos | 76 |
| quality_review.summaries.strong_staged.rates.repetition | 2 |
| quality_review.summaries.strong_staged.rates.unicode_failure | 0 |
| quality_review.summaries.strong_staged.rates.role_leak | 0 |
| quality_review.summaries.strong_staged.rates.empty | 0 |
| quality_review.summaries.strong_staged.grammar2 | 65 |
| quality_review.summaries.strong_staged.relevance2 | 39 |
| quality_review.summaries.strong_staged.coherent | 23 |
| quality_review.summaries.strong_staged.appropriate | 26 |
| quality_review.summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| quality_review.summaries.sequential.BPB | 1.1063855998175087 |
| quality_review.summaries.sequential.rates.eos | 20 |
| quality_review.summaries.sequential.rates.repetition | 27 |
| quality_review.summaries.sequential.rates.unicode_failure | 0 |
| quality_review.summaries.sequential.rates.role_leak | 0 |
| quality_review.summaries.sequential.rates.empty | 0 |
| quality_review.summaries.sequential.grammar2 | 23 |
| quality_review.summaries.sequential.relevance2 | 30 |
| quality_review.summaries.sequential.coherent | 3 |
| quality_review.summaries.sequential.appropriate | 7 |
| quality_review.summaries.sequential.notes_sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| quality_review.summaries.parallel.BPB | 1.102009028125384 |
| quality_review.summaries.parallel.rates.eos | 22 |
| quality_review.summaries.parallel.rates.repetition | 28 |
| quality_review.summaries.parallel.rates.unicode_failure | 0 |
| quality_review.summaries.parallel.rates.role_leak | 0 |
| quality_review.summaries.parallel.rates.empty | 0 |
| quality_review.summaries.parallel.grammar2 | 20 |
| quality_review.summaries.parallel.relevance2 | 38 |
| quality_review.summaries.parallel.coherent | 2 |
| quality_review.summaries.parallel.appropriate | 7 |
| quality_review.summaries.parallel.notes_sha256 | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| quality_review.summaries.cached_CE.BPB | 0.998487162513845 |
| quality_review.summaries.cached_CE.rates.eos | 19 |
| quality_review.summaries.cached_CE.rates.repetition | 45 |
| quality_review.summaries.cached_CE.rates.unicode_failure | 0 |
| quality_review.summaries.cached_CE.rates.role_leak | 0 |
| quality_review.summaries.cached_CE.rates.empty | 0 |
| quality_review.summaries.cached_CE.grammar2 | 44 |
| quality_review.summaries.cached_CE.relevance2 | 25 |
| quality_review.summaries.cached_CE.coherent | 2 |
| quality_review.summaries.cached_CE.appropriate | 2 |
| quality_review.summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| quality_review.eligible_for_final_Base_validation | false |
| portable_archive.bytes | 1861470787 |
| failure_diagnostic.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_failure_pair_diagnostic.json" |
| failure_diagnostic.sha256 | "c594226cbc1439521c3898d22d9e27b4cf931c0a5f38b25f3ccc8d11753db85b" |
| failure_diagnostic.all80_paired | true |
| failure_diagnostic.old_scores_changed | false |
| failure_diagnostic.GPU_seconds | 0 |
| next_diagnostic_preparation.GPU_evaluation_started | true |
| next_diagnostic_preparation.GPU_cap_seconds | 180 |
| seen_TRAIN_diagnostic_completion.status | "exited_all6_teacher_free_diagnostic_and_content_review_complete" |
| seen_TRAIN_diagnostic_completion.created_at | "2026-10-08T02:25:01.884482Z" |
| seen_TRAIN_diagnostic_completion.result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_seen_train_diagnostic.json" |
| seen_TRAIN_diagnostic_completion.result.sha256 | "fe771c1ba34b538374ae8e67f61a7b318c3a022fd56d34d9a473a8dba7a30469" |
| seen_TRAIN_diagnostic_completion.config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/base_residual_seen_train_diagnostic.json" |
| seen_TRAIN_diagnostic_completion.config.sha256 | "cc1ce990800bd230ffba9e555a816de3d092d6c83a8c0e804fee3ae82559f3eb" |
| seen_TRAIN_diagnostic_completion.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_seen_train_content_notes.json" |
| seen_TRAIN_diagnostic_completion.notes.sha256 | "e780423a79a4cf413ea4304aee88a54408ea2947c524bf089ade19d379dd3f06" |
| seen_TRAIN_diagnostic_completion.reviewer_source.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/complete_base_residual_seen_train.py" |
| seen_TRAIN_diagnostic_completion.reviewer_source.sha256 | "832ede2fc58067eca010e935eb7c7df3edcce628357d9cc5c96512b72d6bcc8e" |
| seen_TRAIN_diagnostic_completion.actual_identity.pid | 105914 |
| seen_TRAIN_diagnostic_completion.actual_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| seen_TRAIN_diagnostic_completion.actual_identity.start_ticks | "6897573" |
| seen_TRAIN_diagnostic_completion.actual_process_absent_verified | true |
| seen_TRAIN_diagnostic_completion.cumulative_GPU_ledger_closed | true |
| seen_TRAIN_diagnostic_completion.GPU_seconds | 10.066053368005669 |
| seen_TRAIN_diagnostic_completion.GPU_cap_seconds | 180 |
| seen_TRAIN_diagnostic_completion.additional_training_tokens | 0 |
| seen_TRAIN_diagnostic_completion.optimizer_updates | 0 |
| seen_TRAIN_diagnostic_completion.all6_generated_texts_individually_read | true |
| seen_TRAIN_diagnostic_completion.independent_human_blind | false |
| seen_TRAIN_diagnostic_completion.aggregated.paired_original_positions | 312 |
| seen_TRAIN_diagnostic_completion.aggregated.teacher_mean_NLL | 2.00945954951217 |
| seen_TRAIN_diagnostic_completion.aggregated.free_mean_NLL_on_same_original_positions | 11.351060840028087 |
| seen_TRAIN_diagnostic_completion.aggregated.teacher_argmax_accuracy | 0.5792682926829268 |
| seen_TRAIN_diagnostic_completion.aggregated.teacher_target_count | 328 |
| seen_TRAIN_diagnostic_completion.aggregated.free_generated_tokens | 348 |
| seen_TRAIN_diagnostic_completion.aggregated.free_EOS | 4 |
| seen_TRAIN_diagnostic_completion.aggregated.free_grammar2 | 4 |
| seen_TRAIN_diagnostic_completion.aggregated.free_coherence2 | 1 |
| seen_TRAIN_diagnostic_completion.aggregated.free_appropriate_completion | 3 |
| seen_TRAIN_diagnostic_completion.aggregated.free_automatic_repetition | 1 |
| seen_TRAIN_diagnostic_completion.aggregated.true_gold_EOS_positions_scored | 3 |
| seen_TRAIN_diagnostic_completion.source_preparation.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_seen_train_preparation.json" |
| seen_TRAIN_diagnostic_completion.source_preparation.sha256 | "33ba90940e4d7c1b1c17b977c898a563e639e0b8475d683edd0e8e10bb27635e" |
| seen_TRAIN_diagnostic_completion.UI_restored.identity.pid | 105986 |
| seen_TRAIN_diagnostic_completion.UI_restored.identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| seen_TRAIN_diagnostic_completion.UI_restored.identity.start_ticks | "6898966" |
| seen_TRAIN_diagnostic_completion.UI_restored.actual_alive | true |
| seen_TRAIN_diagnostic_completion.UI_restored.model.name | "JMicro-10M" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.kind | "Base / 文章の続き" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.parameters | 10001152 |
| seen_TRAIN_diagnostic_completion.UI_restored.model.training_tokens | 10000007168 |
| seen_TRAIN_diagnostic_completion.UI_restored.model.update | 305176 |
| seen_TRAIN_diagnostic_completion.UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.device | "NVIDIA GeForce RTX 4090" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.precision | "BF16 / math attention" |
| seen_TRAIN_diagnostic_completion.UI_restored.model.context | 1024 |
| seen_TRAIN_diagnostic_completion.UI_restored.model.busy | false |
| seen_TRAIN_diagnostic_completion.limitations | "Six previously exposed units, one model and nonblind reused TRAIN content; not heldout quality or repeated memorization proof. Gold/free NLL compare the same original targets at common positions only. Natural alternative completions may diverge from that reference without being erroneous. No artificial EOS; unavailable goldEOS is null. Neither source ordering nor data quantity is causally tested." |
| seen_TRAIN_diagnostic_completion.original80_scores_changed | false |
| seen_TRAIN_diagnostic_completion.quality_criteria_changed | false |
| seen_TRAIN_diagnostic_completion.Base_complete | false |
| seen_TRAIN_diagnostic_completion.Base_adopted | false |
| seen_TRAIN_diagnostic_completion.Chat_started | false |
| seen_TRAIN_diagnostic_completion.quantization_started | false |
| seen_TRAIN_diagnostic_completion.protected_test_scored | false |
| seen_TRAIN_diagnostic_completion.CPU_seconds | 0.025753859998076223 |
| norm_gain_screen.GPU_seconds | 0 |
| norm_gain_screen.selective_decay_training_started | false |
| capacity_control_proposal.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_capacity_control_proposal.json" |
| capacity_control_proposal.sha256 | "524c4001bd53d999f96562e59074459a3041261980f7be460c1f7c9337ee5fc3" |
| capacity_control_proposal.implemented | true |
| capacity_control_proposal.learning_started | true |
| capacity_control_proposal.max_original_teacher_tokens | 3000000 |
| capacity_control_proposal.max_cumulative_GPU_seconds | 300 |
| capacity_control_completion.status | "complete" |
| capacity_control_completion.created_at | "2026-10-08T02:52:03.933711Z" |
| capacity_control_completion.result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_capacity_control.json" |
| capacity_control_completion.result.sha256 | "0e789ffc64df5694d530eff36ec1907bad0eaebe72847a4e0d2b76147a7dac41" |
| capacity_control_completion.config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/base_residual_capacity_control_r2.json" |
| capacity_control_completion.config.sha256 | "a2fbcbceb5bdbd2db593999ceb068a8c69c0fb81bb870cef87928cce631e4b10" |
| capacity_control_completion.process_exited | true |
| capacity_control_completion.prior_failed_process_exited | true |
| capacity_control_completion.launcher_exit_code | 0 |
| capacity_control_completion.GPU_seconds | 18.944145809990005 |
| capacity_control_completion.GPU_cap_seconds | 300 |
| capacity_control_completion.first_failed_gate_GPU_seconds | 3.1996772790007526 |
| capacity_control_completion.repaired_process_GPU_seconds | 15.744468530989252 |
| capacity_control_completion.verification_updates | 16 |
| capacity_control_completion.verification_teacher_tokens | 161984 |
| capacity_control_completion.original_unique_teacher_tokens | 756 |
| capacity_control_completion.diagnostic_learning_teacher_tokens | 252176 |
| capacity_control_completion.completed_updates | 25 |
| capacity_control_completion.initial_full_teacher_correct | 422 |
| capacity_control_completion.initial_conditioned_teacher_correct | 352 |
| capacity_control_completion.final_full_teacher_correct | 751 |
| capacity_control_completion.full_teacher_argmax_theoretical_upper_bound | 751 |
| capacity_control_completion.final_conditioned_teacher_correct | 612 |
| capacity_control_completion.conditioned_teacher_targets | 612 |
| capacity_control_completion.capacity_control_passed | true |
| capacity_control_completion.all6_raw_continuations_individually_read | true |
| capacity_control_completion.content_reading_notes | "All six originals reproduced, including awkward source wording and source factual claims; exact memorization is neither correctness of those claims nor quality on new prompts. Source roughness was retained, not edited away." |
| capacity_control_completion.counters.update | 25 |
| capacity_control_completion.counters.supervised_tokens | 252176 |
| capacity_control_completion.counters.EOS_targets | 2000 |
| capacity_control_completion.counters.completed_original_body_bytes | 1081117 |
| capacity_control_completion.counters.CE_input_tokens | 252176 |
| capacity_control_completion.counters.physical_input_tokens | 636000 |
| capacity_control_completion.counters.source_teacher_tokens.web | 128856 |
| capacity_control_completion.counters.source_teacher_tokens.textbook | 76700 |
| capacity_control_completion.counters.source_teacher_tokens.story | 46620 |
| capacity_control_completion.counters.token_digest | "a731ea9cd1ea219051bdc9fffddeaa84f274ffb3bbc1c8b43e125610529b21ad" |
| capacity_control_completion.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-capacity-control-r2-20261008/latest.pt" |
| capacity_control_completion.checkpoint.sha256 | "f17a18e8594253b46b54970821c28132c76592ea2dd9dba9904ba037ee63154d" |
| capacity_control_completion.restored_UI_identity.pid | 107866 |
| capacity_control_completion.restored_UI_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| capacity_control_completion.restored_UI_identity.start_ticks | "7102445" |
| capacity_control_completion.restored_UI_model.name | "JMicro-10M" |
| capacity_control_completion.restored_UI_model.kind | "Base / 文章の続き" |
| capacity_control_completion.restored_UI_model.parameters | 10001152 |
| capacity_control_completion.restored_UI_model.training_tokens | 10000007168 |
| capacity_control_completion.restored_UI_model.update | 305176 |
| capacity_control_completion.restored_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| capacity_control_completion.restored_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| capacity_control_completion.restored_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| capacity_control_completion.restored_UI_model.device | "NVIDIA GeForce RTX 4090" |
| capacity_control_completion.restored_UI_model.precision | "BF16 / math attention" |
| capacity_control_completion.restored_UI_model.context | 1024 |
| capacity_control_completion.restored_UI_model.busy | false |
| capacity_control_completion.scientific_Base_teacher_tokens | 0 |
| capacity_control_completion.Base_complete | false |
| capacity_control_completion.Base_adopted | false |
| capacity_control_completion.Chat_started | false |
| capacity_control_completion.quantization_started | false |
| capacity_control_completion.protected_test_scored | false |
| capacity_control_completion.conclusion | "The corrected current sequential2B learning/evaluation path can memorize these six already-seen TRAIN units and stop at original EOS. An end-to-end inability to learn these examples is unsupported. This does not establish generalization, explain corpus-wide repetition, validate all data quality or qualify Base." |
| capacity_control_completion.next_action | "Use the current same-checkpoint TRAIN versus separate DEV teacher/free diagnostics to separate broad underfitting from generation degradation. Define one bounded comparison and decision rule before any new GPU training; reuse existing six-case and historical diagnostics, no corpus rescan or quantity-only extension." |
| train_DEV_history_completion.status | "complete" |
| train_DEV_history_completion.created_at | "2026-10-08T03:02:53.668418Z" |
| train_DEV_history_completion.result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_train_dev_history.json" |
| train_DEV_history_completion.result.sha256 | "c760be4eca41ddd689d56b8078d699a1592e0b746fecb777b3b77b52a7be041e" |
| train_DEV_history_completion.config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/base_residual_train_dev_history.json" |
| train_DEV_history_completion.config.sha256 | "bb155ca928f1e58d1cacd5e540f80a9e126da19f0554b5b2fad0c7b260c33c07" |
| train_DEV_history_completion.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_train_dev_history_content_notes.json" |
| train_DEV_history_completion.notes.sha256 | "b12e0b136ab48a901698060e7888ee9f019721694e455b56d141684cb88de577" |
| train_DEV_history_completion.process_exited | true |
| train_DEV_history_completion.launcher_exit_code | 0 |
| train_DEV_history_completion.GPU_seconds | 53.500711676999344 |
| train_DEV_history_completion.GPU_cap_seconds | 120 |
| train_DEV_history_completion.checks.weights_unchanged | true |
| train_DEV_history_completion.checks.RNG_unchanged | true |
| train_DEV_history_completion.checks.eval_mode_unchanged | true |
| train_DEV_history_completion.checks.all32_same_first_prefix_exact | true |
| train_DEV_history_completion.populations.TRAIN.documents | 16 |
| train_DEV_history_completion.populations.TRAIN.teacher_targets | 903 |
| train_DEV_history_completion.populations.TRAIN.teacher_original_argmax_correct | 436 |
| train_DEV_history_completion.populations.TRAIN.teacher_original_argmax_accuracy | 0.48283499446290146 |
| train_DEV_history_completion.populations.TRAIN.teacher_mean_NLL | 2.558186787413917 |
| train_DEV_history_completion.populations.TRAIN.teacher_body_targets | 892 |
| train_DEV_history_completion.populations.TRAIN.teacher_body_mean_NLL | 2.586085458288423 |
| train_DEV_history_completion.populations.TRAIN.teacher_gold_EOS_unobserved | 5 |
| train_DEV_history_completion.populations.TRAIN.free_EOS | 8 |
| train_DEV_history_completion.populations.TRAIN.free_automatic_repetition | 5 |
| train_DEV_history_completion.populations.TRAIN.free_Unicode_errors | 0 |
| train_DEV_history_completion.populations.TRAIN.free_role_leak | 0 |
| train_DEV_history_completion.populations.TRAIN.free_empty | 0 |
| train_DEV_history_completion.populations.TRAIN.common_positions | 823 |
| train_DEV_history_completion.populations.TRAIN.common_teacher_NLL | 2.572555955830586 |
| train_DEV_history_completion.populations.TRAIN.common_free_original_reference_NLL | 10.82217379615564 |
| train_DEV_history_completion.populations.TRAIN.manual_diagnostic_observations.premise.maintained | 10 |
| train_DEV_history_completion.populations.TRAIN.manual_diagnostic_observations.premise.violated | 0 |
| train_DEV_history_completion.populations.TRAIN.manual_diagnostic_observations.premise.unclear | 6 |
| train_DEV_history_completion.populations.TRAIN.manual_diagnostic_observations.nonprogressive_repetition | 16 |
| train_DEV_history_completion.populations.TRAIN.manual_diagnostic_observations.appropriate_end | 1 |
| train_DEV_history_completion.populations.DEV.documents | 16 |
| train_DEV_history_completion.populations.DEV.teacher_targets | 978 |
| train_DEV_history_completion.populations.DEV.teacher_original_argmax_correct | 450 |
| train_DEV_history_completion.populations.DEV.teacher_original_argmax_accuracy | 0.4601226993865031 |
| train_DEV_history_completion.populations.DEV.teacher_mean_NLL | 2.637304196155249 |
| train_DEV_history_completion.populations.DEV.teacher_body_targets | 973 |
| train_DEV_history_completion.populations.DEV.teacher_body_mean_NLL | 2.625721544373912 |
| train_DEV_history_completion.populations.DEV.teacher_gold_EOS_unobserved | 11 |
| train_DEV_history_completion.populations.DEV.free_EOS | 4 |
| train_DEV_history_completion.populations.DEV.free_automatic_repetition | 5 |
| train_DEV_history_completion.populations.DEV.free_Unicode_errors | 0 |
| train_DEV_history_completion.populations.DEV.free_role_leak | 0 |
| train_DEV_history_completion.populations.DEV.free_empty | 0 |
| train_DEV_history_completion.populations.DEV.common_positions | 918 |
| train_DEV_history_completion.populations.DEV.common_teacher_NLL | 2.684084259401168 |
| train_DEV_history_completion.populations.DEV.common_free_original_reference_NLL | 10.721288487650728 |
| train_DEV_history_completion.populations.DEV.manual_diagnostic_observations.premise.maintained | 8 |
| train_DEV_history_completion.populations.DEV.manual_diagnostic_observations.premise.violated | 0 |
| train_DEV_history_completion.populations.DEV.manual_diagnostic_observations.premise.unclear | 8 |
| train_DEV_history_completion.populations.DEV.manual_diagnostic_observations.nonprogressive_repetition | 16 |
| train_DEV_history_completion.populations.DEV.manual_diagnostic_observations.appropriate_end | 2 |
| train_DEV_history_completion.descriptive_fit_gap.mean_DEV_minus_TRAIN | 0.11075813219869393 |
| train_DEV_history_completion.descriptive_fit_gap.bootstrap95CI | [-0.2578728060934418, 0.5019889472172607] |
| train_DEV_history_completion.descriptive_fit_gap.bootstrap_seed | 42 |
| train_DEV_history_completion.descriptive_fit_gap.bootstrap_samples | 10000 |
| train_DEV_history_completion.descriptive_fit_gap.predeclared_mean_threshold | 0.25 |
| train_DEV_history_completion.descriptive_fit_gap.screen_triggered | false |
| train_DEV_history_completion.descriptive_fit_gap.interpretation | "Small length-matched observational samples only; non-trigger is not proof of sufficient learning or absence of overfitting." |
| train_DEV_history_completion.restored_UI_identity.pid | 108841 |
| train_DEV_history_completion.restored_UI_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| train_DEV_history_completion.restored_UI_identity.start_ticks | "7152852" |
| train_DEV_history_completion.restored_UI_model.name | "JMicro-10M" |
| train_DEV_history_completion.restored_UI_model.kind | "Base / 文章の続き" |
| train_DEV_history_completion.restored_UI_model.parameters | 10001152 |
| train_DEV_history_completion.restored_UI_model.training_tokens | 10000007168 |
| train_DEV_history_completion.restored_UI_model.update | 305176 |
| train_DEV_history_completion.restored_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| train_DEV_history_completion.restored_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| train_DEV_history_completion.restored_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| train_DEV_history_completion.restored_UI_model.device | "NVIDIA GeForce RTX 4090" |
| train_DEV_history_completion.restored_UI_model.precision | "BF16 / math attention" |
| train_DEV_history_completion.restored_UI_model.context | 1024 |
| train_DEV_history_completion.restored_UI_model.busy | false |
| train_DEV_history_completion.scientific_teacher_tokens | 0 |
| train_DEV_history_completion.optimizer_updates | 0 |
| train_DEV_history_completion.Base_complete | false |
| train_DEV_history_completion.Base_adopted | false |
| train_DEV_history_completion.Chat_started | false |
| train_DEV_history_completion.quantization_started | false |
| train_DEV_history_completion.protected_test_scored | false |
| train_DEV_history_completion.limits | "Only Web and initial consumed windows; do not generalize to all sources or learning history. Repetition judgments are diagnostic observations, not a replacement acceptance criterion. Current checkpoint trained on2B gold, not the discarded six-case memorization probe." |
| boundary_counterfactual_proposal.GPU_cap_seconds | 30 |
| boundary_counterfactual_proposal.GPU_started | true |
| boundary_counterfactual_completion.status | "complete" |
| boundary_counterfactual_completion.created_at | "2026-10-08T03:10:26.634907Z" |
| boundary_counterfactual_completion.result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_boundary_counterfactual.json" |
| boundary_counterfactual_completion.result.sha256 | "6824507ad4118098b5e29eea2fbecf6c388732477210956136e922e30fe2d821" |
| boundary_counterfactual_completion.config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/base_residual_boundary_counterfactual.json" |
| boundary_counterfactual_completion.config.sha256 | "2693eab4097f101b5d68b047bf6ae6780bee41f37fabd9fa65307a7572b83f16" |
| boundary_counterfactual_completion.process_exited | true |
| boundary_counterfactual_completion.launcher_exit_code | 0 |
| boundary_counterfactual_completion.GPU_seconds | 2.3952718090004055 |
| boundary_counterfactual_completion.GPU_cap_seconds | 30 |
| boundary_counterfactual_completion.checks.weights_unchanged | true |
| boundary_counterfactual_completion.checks.RNG_unchanged | true |
| boundary_counterfactual_completion.checks.eval_mode_unchanged | true |
| boundary_counterfactual_completion.checks.all96_next_token_only | true |
| boundary_counterfactual_completion.all96_context_event_bindings_verified | true |
| boundary_counterfactual_completion.identical_original_counterfactual_prediction_checks | 31 |
| boundary_counterfactual_completion.summaries.all.units | 32 |
| boundary_counterfactual_completion.summaries.all.median_EOS_probability_difference | 0.8986915070563555 |
| boundary_counterfactual_completion.summaries.all.mean_EOS_probability_difference | 0.586995554729981 |
| boundary_counterfactual_completion.summaries.all.positive_differences | 27 |
| boundary_counterfactual_completion.summaries.all.median_no_trailing_LF_EOS_probability | 0.05019144341349602 |
| boundary_counterfactual_completion.summaries.all.median_one_LF_EOS_probability | 0.9548971951007843 |
| boundary_counterfactual_completion.summaries.all.no_trailing_LF_EOS_rank1 | 0 |
| boundary_counterfactual_completion.summaries.all.one_LF_EOS_rank1 | 24 |
| boundary_counterfactual_completion.summaries.all.no_trailing_LF_top1_is_LF | 29 |
| boundary_counterfactual_completion.summaries.TRAIN.units | 16 |
| boundary_counterfactual_completion.summaries.TRAIN.median_EOS_probability_difference | 0.927004024386406 |
| boundary_counterfactual_completion.summaries.TRAIN.mean_EOS_probability_difference | 0.829160287801642 |
| boundary_counterfactual_completion.summaries.TRAIN.positive_differences | 15 |
| boundary_counterfactual_completion.summaries.TRAIN.median_no_trailing_LF_EOS_probability | 0.05140066333115101 |
| boundary_counterfactual_completion.summaries.TRAIN.median_one_LF_EOS_probability | 0.9736657738685608 |
| boundary_counterfactual_completion.summaries.TRAIN.no_trailing_LF_EOS_rank1 | 0 |
| boundary_counterfactual_completion.summaries.TRAIN.one_LF_EOS_rank1 | 15 |
| boundary_counterfactual_completion.summaries.TRAIN.no_trailing_LF_top1_is_LF | 16 |
| boundary_counterfactual_completion.summaries.DEV.units | 16 |
| boundary_counterfactual_completion.summaries.DEV.median_EOS_probability_difference | 0.16867672548050905 |
| boundary_counterfactual_completion.summaries.DEV.mean_EOS_probability_difference | 0.34483082165832 |
| boundary_counterfactual_completion.summaries.DEV.positive_differences | 12 |
| boundary_counterfactual_completion.summaries.DEV.median_no_trailing_LF_EOS_probability | 0.0477202907204628 |
| boundary_counterfactual_completion.summaries.DEV.median_one_LF_EOS_probability | 0.3135595843195915 |
| boundary_counterfactual_completion.summaries.DEV.no_trailing_LF_EOS_rank1 | 0 |
| boundary_counterfactual_completion.summaries.DEV.one_LF_EOS_rank1 | 9 |
| boundary_counterfactual_completion.summaries.DEV.no_trailing_LF_top1_is_LF | 13 |
| boundary_counterfactual_completion.prespecified_strong_LF_cue_screen | true |
| boundary_counterfactual_completion.median_probability_difference_threshold | 0.25 |
| boundary_counterfactual_completion.minimum_positive_differences | 24 |
| boundary_counterfactual_completion.restored_UI_identity.pid | 110930 |
| boundary_counterfactual_completion.restored_UI_identity.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| boundary_counterfactual_completion.restored_UI_identity.start_ticks | "7213791" |
| boundary_counterfactual_completion.restored_UI_model.name | "JMicro-10M" |
| boundary_counterfactual_completion.restored_UI_model.kind | "Base / 文章の続き" |
| boundary_counterfactual_completion.restored_UI_model.parameters | 10001152 |
| boundary_counterfactual_completion.restored_UI_model.training_tokens | 10000007168 |
| boundary_counterfactual_completion.restored_UI_model.update | 305176 |
| boundary_counterfactual_completion.restored_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| boundary_counterfactual_completion.restored_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| boundary_counterfactual_completion.restored_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| boundary_counterfactual_completion.restored_UI_model.device | "NVIDIA GeForce RTX 4090" |
| boundary_counterfactual_completion.restored_UI_model.precision | "BF16 / math attention" |
| boundary_counterfactual_completion.restored_UI_model.context | 1024 |
| boundary_counterfactual_completion.restored_UI_model.busy | false |
| boundary_counterfactual_completion.interpretation | "Same-body trailing LF changes measured next-token EOS preference within these frozen weights; a positive screen establishes local marker sensitivity only. No new free-generation or Base-quality improvement measured. Original DEV/test bytes and all quality gates unchanged." |
| boundary_counterfactual_completion.scientific_teacher_tokens | 0 |
| boundary_counterfactual_completion.optimizer_updates | 0 |
| boundary_counterfactual_completion.Base_complete | false |
| boundary_counterfactual_completion.Base_adopted | false |
| boundary_counterfactual_completion.Chat_started | false |
| boundary_counterfactual_completion.quantization_started | false |
| boundary_counterfactual_completion.protected_test_scored | false |
| boundary_stop_path_analysis.uncached_two_step_paths | 21 |
| boundary_stop_path_analysis.new_GPU | 0 |
| consumed_unit_provenance.Web_paragraph_teacher_fraction | 0.8154970315116457 |
| consumed_unit_provenance.Web_noninitial_slice_teacher_fraction | 0.7359144804722518 |
| original_context_diagnostic_proposal.GPU_cap_seconds | 60 |
| original_context_diagnostic_proposal.GPU_started | true |
| original_context_completion.path | "reports/phase6/base_residual_original_context_completion.json" |
| original_context_completion.sha256 | "2581220368261734b04467ac84846dfdee7061dab465fb52595dffbd132469c5" |
| original_context_completion.GPU_seconds | 22.96236798800237 |
| original_context_completion.new_context_units | 14 |
| original_context_completion.mean_BODY_NLL_improvement | 0.1142410210216264 |
| original_context_completion.bootstrap95CI | [0.03722156005696978, 0.20032746828517192] |
| original_context_completion.prespecified_context_benefit_screen | false |
| original_context_completion.fixed_diagnostic_closed | true |
| original_context_completion.new_free_EOS | 0 |
| original_context_completion.new_free_semantic_repetition | 14 |
| original_context_completion.new_free_appropriate_end | 0 |
| original_context_completion.Base_complete | false |
| current_scientific_GPU_job | null |
| restored_current_UI_model.training_tokens | 10000007168 |
| restored_current_UI_model.update | 305176 |
| restored_current_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| restored_current_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_current_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| grouping_pilot_completion | "reports/phase6/base_gradient_accumulation_pilot_completion.json" |
| initialization_pilot_completion | "reports/phase6/base_residual_initialization_pilot_completion.json" |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_comparison_completion.json — fresh_paired_residual4B_review_complete</summary>

[原記録](../../reports/phase6/base_parallel_residual_comparison_completion.json) ／ SHA256: `427561834d6d8549646f9c91c946a6019813f70d08431079472e16d097a627f6` ／ 6,427 bytes

| 原キー | 保存値 |
|---|---|
| status | "fresh_paired_residual4B_review_complete" |
| scientific_CE_teacher_tokens | 4000000000 |
| checkpoints.sequential.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| checkpoints.sequential.sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| checkpoints.parallel.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| checkpoints.parallel.sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| residual_policy.physical_block_invocations | 1 |
| added_physical_parameters_each | 0 |
| GPU_occupancy_seconds | 52093.681041047006 |
| GPU_cap_seconds | 81736 |
| total_GPU_seconds_including_probe | 52115.071744653 |
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
| summaries.sequential.BPB | 1.1063855998175087 |
| summaries.sequential.rates.eos | 20 |
| summaries.sequential.rates.repetition | 27 |
| summaries.sequential.rates.unicode_failure | 0 |
| summaries.sequential.rates.role_leak | 0 |
| summaries.sequential.rates.empty | 0 |
| summaries.sequential.grammar2 | 23 |
| summaries.sequential.relevance2 | 30 |
| summaries.sequential.coherent | 3 |
| summaries.sequential.appropriate | 7 |
| summaries.sequential.notes_sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| summaries.parallel.BPB | 1.102009028125384 |
| summaries.parallel.rates.eos | 22 |
| summaries.parallel.rates.repetition | 28 |
| summaries.parallel.rates.unicode_failure | 0 |
| summaries.parallel.rates.role_leak | 0 |
| summaries.parallel.rates.empty | 0 |
| summaries.parallel.grammar2 | 20 |
| summaries.parallel.relevance2 | 38 |
| summaries.parallel.coherent | 2 |
| summaries.parallel.appropriate | 7 |
| summaries.parallel.notes_sha256 | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| summaries.cached_CE.BPB | 0.998487162513845 |
| summaries.cached_CE.rates.eos | 19 |
| summaries.cached_CE.rates.repetition | 45 |
| summaries.cached_CE.rates.unicode_failure | 0 |
| summaries.cached_CE.rates.role_leak | 0 |
| summaries.cached_CE.rates.empty | 0 |
| summaries.cached_CE.grammar2 | 44 |
| summaries.cached_CE.relevance2 | 25 |
| summaries.cached_CE.coherent | 2 |
| summaries.cached_CE.appropriate | 2 |
| summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| eligible_for_final_Base_validation | false |
| fixed_parallel_residual_condition_closed | true |
| archive.bytes | 3612897752 |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_comparison_evidence_manifest.json) ／ SHA256: `c8e4341ac72efcb1f2b502e0a3120c1c40c5f76351479387957009328141eb08` ／ 17,230 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>
