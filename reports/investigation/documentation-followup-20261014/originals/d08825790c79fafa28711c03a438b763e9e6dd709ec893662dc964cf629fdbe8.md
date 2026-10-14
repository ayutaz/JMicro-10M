# 実行管理・後続準備・その他 — 14/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/finite_Web_constraint_probe.json — finite_Web_constraint_probe</summary>

[原記録](../../reports/phase6/finite_Web_constraint_probe.json) ／ SHA256: `be0d195f577d9eb9a242ea49c4d9ad236e9dcbc9d88d779f02f09df9e57518e8` ／ 296,387 bytes

| 原キー | 保存値 |
|---|---|
| status | "finite_Web_constraint_probe" |
| CPU_preparation_seconds | 1.4314053030102514 |
| GPU_seconds | 34.46052590699401 |
| scientific_source_CE_teacher_tokens | 0 |
| total_new_GPU_ceiling_seconds | 2400 |
| memory.body_teachers | 32638 |
| memory.physical_input_tokens | 32768 |
| memory.common_body_bytes | 130336 |
| memory.cached_samples.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-gradient-attribution-20261006/samples.pt" |
| memory.cached_samples.sha256 | "d06b94ba1b78d07aeee70f4fe29b002fc16eaf05c4af2ff4686def02742640c7" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 34.46052590699401 |
| actual_job.completed_updates | 32 |
| actual_probe.initial_checks.model | true |
| actual_probe.initial_checks.optimizer | true |
| actual_probe.initial_checks.scheduler | true |
| actual_probe.initial_checks.RNG | true |
| actual_probe.initial_checks.actual_Web_cursor | true |
| actual_probe.initial_checks.actual_LR | true |
| actual_probe.initial_checks.baseline_finite | true |
| actual_probe.reference_body_NLL | 2.5812628269195557 |
| actual_probe.reference_setup_observations.teacher_observations | 32638 |
| actual_probe.reference_setup_observations.gradient_teacher_tokens | 0 |
| actual_probe.reference_setup_observations.physical_input_tokens | 32768 |
| actual_probe.gate.passed | true |
| actual_probe.gate.checks.version | true |
| actual_probe.gate.checks.spec | true |
| actual_probe.gate.checks.model_config | true |
| actual_probe.gate.checks.model | true |
| actual_probe.gate.checks.optimizer | true |
| actual_probe.gate.checks.scheduler | true |
| actual_probe.gate.checks.rng | true |
| actual_probe.gate.checks.sampler | true |
| actual_probe.gate.checks.update | true |
| actual_probe.gate.checks.tokens | true |
| actual_probe.gate.checks.supervised_tokens | true |
| actual_probe.gate.checks.body_bytes | true |
| actual_probe.gate.checks.token_digest | true |
| actual_probe.gate.checks.focus_token_digest | true |
| actual_probe.gate.checks.focus_teacher_tokens | true |
| actual_probe.gate.checks.weighted_teacher_mass | true |
| actual_probe.gate.checks.shard_manifest_sha256 | true |
| actual_probe.gate.checks.implementation_sha256 | true |
| actual_probe.gate.checks.study_implementation_sha256 | true |
| actual_probe.gate.checks.study_binding | true |
| actual_probe.gate.checks.pilot_binding | true |
| actual_probe.gate.checks.lineage | true |
| actual_probe.gate.checks.auxiliary | true |
| actual_probe.gate.checks.last_constraint | true |
| actual_probe.gate.checks.branch_updates | true |
| actual_probe.gate.checks.branch_tokens | true |
| actual_probe.gate.checks.history_physical_input_tokens | true |
| actual_probe.gate.checks.history_actual_source_routes | true |
| actual_probe.gate.checks.history_outcome_weight | true |
| actual_probe.gate.checks.history_source_digests | true |
| actual_probe.gate.checks.history_actual_source_teachers | true |
| actual_probe.gate.checks.history_token_digest | true |
| actual_probe.gate.checks.history_focus_teacher_tokens | true |
| actual_probe.gate.checks.history_source_teachers | true |
| actual_probe.gate.checks.history_supervised_tokens | true |
| actual_probe.gate.checks.history_source_input_tokens | true |
| actual_probe.gate.checks.history_additional_teacher_tokens | true |
| actual_probe.gate.checks.history_constraint | true |
| actual_probe.gate.checks.history_lr | true |
| actual_probe.gate.checks.history_update | true |
| actual_probe.gate.checks.history_auxiliary | true |
| actual_probe.gate.checks.history_actual_source_eos | true |
| actual_probe.gate.checks.history_focus_token_digest | true |
| actual_probe.gate.checks.history_source_eos | true |
| actual_probe.gate.checks.history_valid_input_tokens | true |
| actual_probe.gate.checks.history_reference_suffix_teacher_tokens | true |
| actual_probe.gate.checks.history_reference_token_digest | true |
| actual_probe.gate.checks.history_source_focus_teachers | true |
| actual_probe.gate.checks.history_source_body_bytes | true |
| actual_probe.gate.checks.history_weighted_teacher_mass | true |
| actual_probe.gate.checks.history_loss | true |
| actual_probe.gate.checks.history_actual_source_body_bytes | true |
| actual_probe.gate.checks.history_tokens_seen | true |
| actual_probe.gate.checks.history_body_bytes_seen | true |
| actual_probe.gate.checks.history_removed_prefix_targets | true |
| actual_probe.gate.checks.history_gradient_norm | true |
| actual_probe.gate.checks.finite | true |
| actual_probe.gate.checks.all_actual_LR | true |
| actual_probe.gate.checks.all_finite_body_bounds | true |
| actual_probe.gate.checks.original_staged_Web_first | true |
| actual_probe.gate.verification_teacher_tokens | 523208 |
| actual_probe.gate.GPU_optimizer_updates | 16 |
| actual_probe.timing.terminal_save_seconds | 0.16950397900654934 |
| actual_probe.timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/finite-Web-constraint-20261006/probe/timing/checkpoint.pt" |
| actual_probe.timing.checkpoint.sha256 | "4194b5b4447c23b84cd7df3d5d1b440c5592df9e366c5565ebca6ff56412cd57" |
| actual_probe.timing.verification_teacher_tokens | 1046365 |
| actual_probe.timing.auxiliary.teacher_observations | 1044416 |
| actual_probe.timing.auxiliary.gradient_teacher_tokens | 0 |
| actual_probe.timing.auxiliary.physical_input_tokens | 1048576 |
| actual_probe.timing.auxiliary.projected_updates | 0 |
| actual_probe.timing.auxiliary.backtracked_updates | 0 |
| actual_probe.timing.auxiliary.accepted_updates | 32 |
| actual_probe.projection_control.reference_body_NLL | 2.5812628269195557 |
| actual_probe.projection_control.ceiling_body_NLL | 2.607075455188751 |
| actual_probe.projection_control.proposed_body_NLL | 2.881101965904236 |
| actual_probe.projection_control.accepted | true |
| actual_probe.projection_control.gradient_body_NLL | 2.881101965904236 |
| actual_probe.projection_control.final_body_NLL | 2.6045130491256714 |
| actual_probe.projection_control.stored_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| actual_probe.projection_control.stored_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| actual_probe.projection_control.initial_stored_body_NLL | 2.881101965904236 |
| actual_probe.projection_control.auxiliary.teacher_observations | 163190 |
| actual_probe.projection_control.auxiliary.gradient_teacher_tokens | 32638 |
| actual_probe.projection_control.auxiliary.physical_input_tokens | 163840 |
| actual_probe.projection_control.diagnostic_weights_not_adopted_or_saved | true |
| actual_probe.projection_control.original_checkpoint_file_unchanged | true |
| actual_probe.oracle_timings.forward_only_seconds | [0.13451141599216498, 0.1261766380048357, 0.12662313701002859, 0.12856960101635195] |
| actual_probe.oracle_timings.gradient_seconds | [0.36841871798969805, 0.30198544199811295, 0.3078891139884945, 0.301658079988556] |
| actual_probe.oracle_timings.auxiliary.teacher_observations | 261104 |
| actual_probe.oracle_timings.auxiliary.gradient_teacher_tokens | 130552 |
| actual_probe.oracle_timings.auxiliary.physical_input_tokens | 262144 |
| actual_probe.passed | true |
| actual_probe.GPU_optimizer_updates | 48 |
| actual_probe.verification_source_CE_teacher_tokens | 1569573 |
| actual_probe.scientific_source_CE_teacher_tokens | 0 |
| actual_probe.status | "finite_constraint_probe_complete" |
| actual_probe.GPU_seconds | 34.46052590699401 |
| actual_probe.Base_complete | false |
| actual_probe.Base_adopted | false |
| actual_probe.protected_test_used | false |
| estimated_science_GPU_seconds_with_margin | 5509.804173578217 |
| estimated_total_GPU_seconds | 5544.264699485211 |
| within_budget | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/finite_Web_constraint_probe_portable.json — None</summary>

[原記録](../../reports/phase6/finite_Web_constraint_probe_portable.json) ／ SHA256: `33f202c43129d8c9f955f1600315f8ab4cf376db7c9a98fe14ef4f2e62a65c65` ／ 22,467 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/finite_Web_constraint_probe.json.bytes | 296387 |
| files.configs/phase6/finite_Web_constraint_probe.json.bytes | 21911 |
| files.reports/phase6/finite_Web_constraint_proposal.json.bytes | 10513 |
| files.reports/phase6/finite_Web_constraint_tests.xml.bytes | 854 |
| files.reports/phase6/finite_Web_constraint_tests.xml.sha256 | "9b20ecde9552251922c930912e3a4621ef12a8a836bc12e2b7eeb9b7cae26841" |
| files.reports/phase6/finite-Web-constraint-20261006/memory.json.bytes | 2130 |
| files.scripts/record_finite_Web_constraint.py.bytes | 8863 |
| files.scripts/finite_Web_constraint.py.bytes | 16012 |
| files.scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/job.json.bytes | 550 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/latest.json.bytes | 254 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/latest.json.sha256 | "8071081cc9b4e9fb92ae7213ab80e36ab4c8b15dedf0b42dec883266b5fe62eb" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/progress-result.json.bytes | 274931 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/result.json.bytes | 275477 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/configs/phase6/finite_Web_constraint_probe.json.bytes | 21911 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/timing/latest.json.bytes | 264 |
| files.reports/phase6/finite-Web-constraint-20261006/probe/timing/latest.json.sha256 | "4d22fb9f0ca40dc1630a7cc6a2c007b00a000cd1de8c87b7aa5ae6de3245f719" |
| files.reports/phase6/finite-Web-constraint-20261006/probe/timing/metrics.jsonl.bytes | 124625 |

</details>

<details>
<summary>reports/phase6/finite_Web_constraint_proposal.json — None</summary>

[原記録](../../reports/phase6/finite_Web_constraint_proposal.json) ／ SHA256: `e87f562f0653af0ce9be2dd2efa165808a4822c95f3a01c129db47cd75e330a4` ／ 10,513 bytes

| 原キー | 保存値 |
|---|---|
| references.soft_parameter_anchor_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter_displacement_anchor_completion.json" |
| references.soft_parameter_anchor_failure.sha256 | "cde3ccf0c0cf75db7a7854a8f66f102fb0dffe9c055fc73eb6af3a0b4fbb9002" |
| references.original_masked_staged_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/content-notes.json" |
| references.original_masked_staged_notes.sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| references.accepted_input_ledger.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved_outcome_reference_input.json" |
| references.accepted_input_ledger.sha256 | "fe12f14780541213f584ad45d7facb3c2e87251270bc61f1961bbdeb1984eb68" |
| measured_trigger.rank4_vs_full_coherence | [3, 10] |
| measured_trigger.rank4_vs_full_EOS | [13, 23] |
| measured_trigger.rank4_vs_full_repetition | [64, 37] |
| measured_trigger.shared_prefix_Web_BPB | 1.0136221079473724 |
| measured_trigger.original_guard_Web_BPB | 0.9715702494156145 |
| measured_trigger.masked_staged_Web_BPB | 1.0868123573684936 |
| measured_trigger.masked_staged_coherence | 35 |
| measured_trigger.masked_staged_EOS | 79 |
| measured_trigger.masked_staged_repetition | 1 |
| hypothesis | "Preserve the actual TRAIN Web prediction function while applying full-capacity staged outcome learning. A soft parameter penalty/frozen low-rank backbone did not enforce that constraint. Fixed small-memory fit is not held-out Web retention or natural quality." |
| CE_teacher_tokens | 91641755 |
| reference_teacher_tokens | 100000000 |
| physical_input_tokens | 100532224 |
| updates | 3068 |
| memory.loss | "Original body IDs&gt;=8 only; exclude EOS/BOS/structural/ignored targets" |
| teacher_accounting | "91,641,755 ordinary source-CE teachers if completed; separately count memory projection-gradient targets, finite-loss target observations, rejected-proposal source/auxiliary exposure and all physical input. Total gradient teachers may exceed CE budget. Never claim matched total supervision or equal GPU budget to cached control." |
| CPU_preparation_ceiling_seconds | 60 |
| probe_GPU_ceiling_seconds | 120 |
| total_new_GPU_ceiling_seconds | 2400 |
| completion | "Actual accepted3068 source updates with whole91,641,755 CE teachers plus separately measured auxiliary teachers, or explicit finite rejection/rollback/budget branch. Only completed candidate gets unchanged dev256/Japanese192/331/1119/greedy80 and all80 raw-bound individual review. Terminal actual PID, original UI restoration, portable evidence and local commit." |
| protected_test_used | false |
| failure_policy | "End this sole functional constraint recipe; no memory/ceiling/margin/projector/LR/source/mask/order/CP/decoder salvage sweep or automatic training extension." |
| limitations | ["Small fixed TRAIN memory can overfit and cannot guarantee held-out retention", "Projected gradient adds repeated TRAIN feedback/supervision; report its cost and do not attribute solely to clipping", "The completed one-seed nonblind Base failures do not prove a universal10M/LoRA capacity limit", "First-order memory prediction alone is not the finite acceptance oracle", "No natural quality or final adoption evidence exists for this new recipe"] |
| GPU_seconds_so_far | 0 |
| new_CE_teacher_tokens_so_far | 0 |
| new_memory_projection_teacher_tokens_so_far | 0 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/finite_Web_oracle_efficiency_terminal.json — readonly_oracle_efficiency_terminal</summary>

[原記録](../../reports/phase6/finite_Web_oracle_efficiency_terminal.json) ／ SHA256: `14f7a04f41dd81764d49d732bf34c038977008690e6320c5883b5093b9570b8d` ／ 8,317 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_oracle_efficiency_terminal" |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| CPU_preparation_seconds | 0.22917144899838604 |
| GPU_seconds | 9.28021423498285 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 9.28021423498285 |
| actual_result.checkpoints.original_fullparent.reference_body_NLL | 2.5812628269195557 |
| actual_result.checkpoints.original_fullparent.candidate_body_NLL | 2.5812628269195557 |
| actual_result.checkpoints.original_fullparent.NLL_absolute_error | 0.0 |
| actual_result.checkpoints.original_fullparent.gradient_parity.maximum_absolute | 8.530914783477783e-07 |
| actual_result.checkpoints.original_fullparent.gradient_parity.global_relative_L2 | 6.3803901568322135e-06 |
| actual_result.checkpoints.original_fullparent.gradient_parity.all_elementwise | true |
| actual_result.checkpoints.original_fullparent.gradient_parity.passed | true |
| actual_result.checkpoints.original_fullparent.checks.NLL | true |
| actual_result.checkpoints.original_fullparent.checks.gradient | true |
| actual_result.checkpoints.original_fullparent.checks.candidate_bitwise_repeat | true |
| actual_result.checkpoints.original_fullparent.checks.no_parameter_grads | true |
| actual_result.checkpoints.original_fullparent.checks.weights_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.RNG_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.training_state_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.unique_tied_parameters | true |
| actual_result.checkpoints.original_fullparent.checks.final_weights_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.final_RNG_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.final_no_parameter_grads | true |
| actual_result.checkpoints.original_fullparent.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| actual_result.checkpoints.original_fullparent.reference_checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| actual_result.checkpoints.original_fullparent.parameter_count | 10001152 |
| actual_result.checkpoints.original_fullparent.timings.math.forward_only_seconds | [0.12665017799008638, 0.12938208901323378, 0.12722719000885263, 0.12616211900603957] |
| actual_result.checkpoints.original_fullparent.timings.math.gradient_seconds | [0.30325723602436483, 0.30523274600273, 0.30643148900708184, 0.3001381900103297] |
| actual_result.checkpoints.original_fullparent.timings.efficient.forward_only_seconds | [0.06325060399831273, 0.06352483999216929, 0.06352941298973747, 0.06331209899508394] |
| actual_result.checkpoints.original_fullparent.timings.efficient.gradient_seconds | [0.2767075079900678, 0.27962842100532725, 0.27749541398952715, 0.2767780289868824] |
| actual_result.checkpoints.original_fullparent.reference_counts.forward_only_calls | 4 |
| actual_result.checkpoints.original_fullparent.reference_counts.gradient_calls | 5 |
| actual_result.checkpoints.original_fullparent.reference_counts.teacher_observations | 293742 |
| actual_result.checkpoints.original_fullparent.reference_counts.gradient_teacher_tokens | 163190 |
| actual_result.checkpoints.original_fullparent.reference_counts.physical_input_tokens | 294912 |
| actual_result.checkpoints.original_fullparent.candidate_counts.forward_only_calls | 4 |
| actual_result.checkpoints.original_fullparent.candidate_counts.gradient_calls | 6 |
| actual_result.checkpoints.original_fullparent.candidate_counts.teacher_observations | 326380 |
| actual_result.checkpoints.original_fullparent.candidate_counts.gradient_teacher_tokens | 195828 |
| actual_result.checkpoints.original_fullparent.candidate_counts.physical_input_tokens | 327680 |
| actual_result.checkpoints.original_fullparent.peak_allocated_bytes | 4826018816 |
| actual_result.checkpoints.original_fullparent.peak_reserved_bytes | 4980736000 |
| actual_result.checkpoints.fixed_masked_staged.reference_body_NLL | 2.881101965904236 |
| actual_result.checkpoints.fixed_masked_staged.candidate_body_NLL | 2.8811018466949463 |
| actual_result.checkpoints.fixed_masked_staged.NLL_absolute_error | 1.1920928955078125e-07 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.maximum_absolute | 2.0563602447509766e-06 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.global_relative_L2 | 1.4672964010969208e-06 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.all_elementwise | true |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.passed | true |
| actual_result.checkpoints.fixed_masked_staged.checks.NLL | true |
| actual_result.checkpoints.fixed_masked_staged.checks.gradient | true |
| actual_result.checkpoints.fixed_masked_staged.checks.candidate_bitwise_repeat | true |
| actual_result.checkpoints.fixed_masked_staged.checks.no_parameter_grads | true |
| actual_result.checkpoints.fixed_masked_staged.checks.weights_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.RNG_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.training_state_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.unique_tied_parameters | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_weights_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_RNG_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_no_parameter_grads | true |
| actual_result.checkpoints.fixed_masked_staged.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| actual_result.checkpoints.fixed_masked_staged.reference_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| actual_result.checkpoints.fixed_masked_staged.parameter_count | 10001152 |
| actual_result.checkpoints.fixed_masked_staged.timings.math.forward_only_seconds | [0.12872026200057007, 0.12598686999990605, 0.1258545439923182, 0.12592013602261432] |
| actual_result.checkpoints.fixed_masked_staged.timings.math.gradient_seconds | [0.30286951700691134, 0.3001236419950146, 0.3008890470082406, 0.30126800801372156] |
| actual_result.checkpoints.fixed_masked_staged.timings.efficient.forward_only_seconds | [0.0635836289729923, 0.06366468602209352, 0.08057154400739819, 0.07232264499180019] |
| actual_result.checkpoints.fixed_masked_staged.timings.efficient.gradient_seconds | [0.27699917400605045, 0.28518324400647543, 0.27969609599676915, 0.27709314599633217] |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.forward_only_calls | 4 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.gradient_calls | 5 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.teacher_observations | 293742 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.gradient_teacher_tokens | 163190 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.physical_input_tokens | 294912 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.forward_only_calls | 4 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.gradient_calls | 6 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.teacher_observations | 326380 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.gradient_teacher_tokens | 195828 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.physical_input_tokens | 327680 |
| actual_result.checkpoints.fixed_masked_staged.peak_allocated_bytes | 4866547712 |
| actual_result.checkpoints.fixed_masked_staged.peak_reserved_bytes | 5066719232 |
| actual_result.optimizer_updates | 0 |
| actual_result.new_source_CE_teacher_tokens | 0 |
| actual_result.status | "readonly_oracle_efficiency_complete" |
| actual_result.passed | true |
| actual_result.GPU_seconds | 9.28021423498285 |
| actual_result.maximum_fast_forward_seconds | 0.08057154400739819 |
| actual_result.maximum_fast_gradient_seconds | 0.28518324400647543 |
| actual_result.illustrative_optimized_science_estimate_seconds | 3887.0250965992686 |
| actual_result.estimate_scope | "Single implementation estimate from retained source timing; excludes future exact-math acceptance audits/new transactional CUDA gate. Not a scientific launch authorization." |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| scientific_config_created | false |
| completion_scope | "Implementation diagnostic, not Base quality/adoption." |

</details>

<details>
<summary>reports/phase6/finite_Web_oracle_efficiency_terminal_portable.json — None</summary>

[原記録](../../reports/phase6/finite_Web_oracle_efficiency_terminal_portable.json) ／ SHA256: `f74ab0ac40062b873d4cd0e6300448f79a6ff8c940e343707865a6000f6d4a2e` ／ 3,258 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/finite_Web_oracle_efficiency_terminal.json.bytes | 8317 |
| files.configs/phase6/finite_Web_oracle_efficiency.json.bytes | 6128 |
| files.scripts/record_finite_Web_oracle_efficiency.py.bytes | 6843 |
| files.scripts/probe_finite_Web_oracle_efficiency.py.bytes | 14444 |
| files.scripts/probe_finite_Web_oracle_efficiency.ps1.bytes | 2652 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/job.json.bytes | 395 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/progress-result.json.bytes | 4934 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/result.json.bytes | 5646 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/configs/phase6/finite_Web_oracle_efficiency.json.bytes | 6128 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/scripts/probe_finite_Web_oracle_efficiency.ps1.bytes | 2652 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/scripts/probe_finite_Web_oracle_efficiency.py.bytes | 14444 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/finite-Web-oracle-efficiency-20261006/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-field-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-field-launcher-20261006/launcher.json) ／ SHA256: `be24f8552f24a68f39e4918bd1160aa9a0385116d8b7a4ab895475fbfef376b0` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/fisher-parameter-field-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-field-launcher-20261006/result.json) ／ SHA256: `79cc50805d74ffa100a808d7c2189189b84256bd225ce2dabab7b4bebb8e8243` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_field_terminal.json — Fisher_parameter_field_terminal</summary>

[原記録](../../reports/phase6/fisher_parameter_field_terminal.json) ／ SHA256: `f84cd868c3c52fc0a15dd010fa134f6bb6b378bf72450a75611cae02ccd53d34` ／ 15,884 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_field_terminal" |
| CPU_preparation_seconds | 0.28030768601456657 |
| GPU_seconds | 3.6230295989953447 |
| source_CE_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 3.6230295989953447 |
| actual_field.passed | true |
| actual_field.checks.weights_unchanged | true |
| actual_field.checks.RNG_unchanged | true |
| actual_field.checks.parameter_grads_unchanged | true |
| actual_field.checks.native_unique_10M | true |
| actual_field.checks.native_unique119 | true |
| actual_field.checks.exact_cost | true |
| actual_field.settings.seed | 2026100647 |
| actual_field.settings.sampled_vocabulary | "full_native_4096" |
| actual_field.accounting.sampled_score_labels | 65276 |
| actual_field.accounting.physical_context_tokens | 65536 |
| actual_field.accounting.ordinary_source_CE_teacher_tokens | 0 |
| actual_field.accounting.optimizer_updates | 0 |
| actual_field.sampled_labels_tensor_digest | "2bf7550ba830b50f61ad22f4fc3ca3930960aa2619d3016ad9d564b71ac3f1f0" |
| actual_field.GPU_seconds | 3.6230295989953447 |
| actual_field.Base_complete | false |
| actual_field.scientific_launched | false |

</details>

<details>
<summary>reports/phase6/fisher_parameter_field_terminal_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_field_terminal_portable.json) ／ SHA256: `34c4ca8fea7cf4b40b582cc1d3aca35dca9e19826997d75269997e545d41faff` ／ 21,160 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_field_terminal.json.bytes | 15884 |
| files.configs/phase6/fisher_parameter_field.json.bytes | 13419 |
| files.reports/phase6/fisher_parameter_anchor_proposal.json.bytes | 5455 |
| files.scripts/record_fisher_parameter_field.py.bytes | 6452 |
| files.reports/phase6/fisher_parameter_anchor_tests.xml.bytes | 873 |
| files.reports/phase6/fisher_parameter_anchor_tests.xml.sha256 | "c06c70206f682dd7f32df0254cf35949831afb6cd75876cfff97061bf3f7aad8" |
| files.scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.scripts/build_fisher_parameter_field.py.bytes | 14359 |
| files.scripts/build_fisher_parameter_field.ps1.bytes | 2617 |
| files.tests/test_fisher_parameter_anchor.py.bytes | 7440 |
| files.tests/test_fisher_parameter_anchor.py.sha256 | "1f5ab2f00af0ec8fa268ec5f49635ea0eefb65b7b6df84eec2383ede3ec74784" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/job.json.bytes | 662 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/result.json.bytes | 12255 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/configs/phase6/fisher_parameter_field.json.bytes | 13419 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/reports/phase6/fisher_parameter_anchor_proposal.json.bytes | 5455 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/build_fisher_parameter_field.ps1.bytes | 2617 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/build_fisher_parameter_field.py.bytes | 14359 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/parameter_displacement_anchor_trainer.py.bytes | 8735 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_parameter_displacement_anchor_v3.ps1.bytes | 3140 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_parameter_displacement_anchor_v3.py.bytes | 22073 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_fisher_parameter_anchor.py.bytes | 7440 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_fisher_parameter_anchor.py.sha256 | "1f5ab2f00af0ec8fa268ec5f49635ea0eefb65b7b6df84eec2383ede3ec74784" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_parameter_displacement_anchor.py.bytes | 4477 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_parameter_displacement_anchor.py.sha256 | "2ee96ca6b0f2e12a6f9e3c9bd0c40e3cd21de3910545dbe67df357d5b2e7c38e" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/fisher-parameter-anchor-20261006/field/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |

</details>

<details>
<summary>reports/phase6/five_step_progress.json — Base_headwise_gate_CPU_verified_CUDA_science_pending</summary>

[原記録](../../reports/phase6/five_step_progress.json) ／ SHA256: `6964a91501c532143362419e46bbe8058f03426c33744240d4ee316b6201cfa6` ／ 63,685 bytes

| 原キー | 保存値 |
|---|---|
| requested_scope | "Latest user boundary: qualified Base only; notify and stop; Chat/quantization deferred" |
| last_updated_at | "2026-10-06T17:06:22.3947217Z" |
| current_user_scope | "Base only; notify and stop after actual Base completion; Chat and quantization deferred by user2026-10-06" |
| source_condition_pair_review | "reports/phase6/source-condition-pairs-20261006/content-review.json" |
| condition_positive_scientific_config | "configs/phase6/condition_positive_comparison.json" |
| condition_positive_comparison_completion | "reports/phase6/condition_positive_comparison_completion.json" |
| web_KL_completion | "reports/phase6/web_kl_comparison_completion.json" |
| web_KL_quality_passed | false |
| EOS_component_diagnostic | "reports/phase6/web_kl_EOS_component_diagnostic.json" |
| conditional_non_EOS_KL_proposal | "reports/phase6/eos_decoupled_web_kl_comparison_proposal.json" |
| conditional_non_EOS_KL_preparation | "reports/phase6/eos_decoupled_web_kl_trainer_preparation.json" |
| conditional_non_EOS_KL_launch | "reports/phase6/eos_decoupled_web_kl_comparison_launch.json" |
| conditional_non_EOS_KL_completion | "reports/phase6/eos_decoupled_web_kl_comparison_completion.json" |
| conditional_non_EOS_KL_quality_passed | false |
| hard_gold_Web_replay_active_job.status | "complete_actual_process_absent" |
| hard_gold_Web_replay_completion | "reports/phase6/hard_body_web_replay_comparison_completion.json" |
| hard_gold_Web_replay_quality_passed | false |
| context_prior_diagnostic_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_prior_diagnostic_completion.json" |
| context_prior_diagnostic_completion.sha256 | "37667dc1fe9bd746c4e3579b89c84a210726cd0f4f6968eb3b4db556404f0f37" |
| context_outcome_ranking_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_outcome_ranking_comparison_completion.json" |
| context_outcome_ranking_completion.sha256 | "776e31556a91d30494dfd0e67e45514726af22941d69e05c937be24d6246cd4f" |
| context_outcome_ranking_workspace_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_outcome_ranking_workspace_completion.json" |
| context_outcome_ranking_workspace_completion.sha256 | "e4094d40ea18e31e64e68555502a08705979349f4742f0474f496a0cb0e5beda" |
| anchored_context_outcome_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/anchored_context_outcome_comparison_completion.json" |
| anchored_context_outcome_completion.sha256 | "c3256b77a030760a88e48e1da0105094073d105d167928bd2cf0e0d27137c509" |
| anchored_context_outcome_workspace_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/anchored_context_outcome_workspace_completion.json" |
| anchored_context_outcome_workspace_completion.sha256 | "176be0b95b2bd8a1731a66e198eac665c75630f68ed3c39b50290777e13c9452" |
| decision_span_diagnostic_proposal.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/decision_span_diagnostic_proposal.json" |
| decision_span_diagnostic_proposal.sha256 | "1cb6a550ab3410429de7043da763048285c51b89199f949154748212c2fb919a" |
| decision_span_diagnostic_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/decision_span_diagnostic_completion.json" |
| decision_span_diagnostic_completion.sha256 | "4b517d3f097953b81be6250ec4837d9eb8463939a395883d63d98ccb9a03d103" |
| narrative_condition_source_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/narrative_condition_source_completion.json" |
| narrative_condition_source_completion.sha256 | "c8867ea87161a3a8f7d9f0fcf754ded93367cf2844f84d7ef04a5e981d46beab" |
| natural_story_source_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural_story_source_completion.json" |
| natural_story_source_completion.sha256 | "2eebe34e8a2ef934660c30eb5d23fc74b99acd5568b7d18f7415cf98c68bd151" |
| translated_story_source_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/translated_story_source_completion.json" |
| translated_story_source_completion.sha256 | "c010b24599f78c1692b81859e8e6cc43a00361a290af3209dd335c70bff73225" |
| weight_average_active_job.status | "complete_actual_process_absent" |
| weight_average_active_job.GPU_ceiling_seconds | 300 |
| weight_average_active_job.Base_complete | false |
| weight_average_active_job.science_tokens | 0 |
| weight_average_comparison_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/weight_average_comparison_completion.json" |
| weight_average_comparison_completion.sha256 | "e3e0ca62c5ea8d7a6c0a5d0d425ba722eedec07ebbfad76f443b2f5ab5250838" |
| finite_parameter_displacement_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/finite_parameter_displacement_completion.json" |
| finite_parameter_displacement_completion.sha256 | "05c13ec9d854b524e73b198130a45c6b4401d16daec89dea93b16a18b33303d6" |
| parameter_displacement_anchor_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter_displacement_anchor_completion.json" |
| parameter_displacement_anchor_completion.sha256 | "cde3ccf0c0cf75db7a7854a8f66f102fb0dffe9c055fc73eb6af3a0b4fbb9002" |
| conditional_prefix_mask_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional_prefix_mask_completion.json" |
| conditional_prefix_mask_completion.sha256 | "60d9bed29315da95b0242fd41badd69e9e3ce7358a4b78fe9af5e8efd7fde62c" |
| shared_prefix_web_loss_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/shared_prefix_web_loss_completion.json" |
| shared_prefix_web_loss_completion.sha256 | "a4943b817005078235f00a784af1783122fbe7b43f8adfde5055ca1a98288758" |
| interleaved_outcome_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved_outcome_completion.json" |
| interleaved_outcome_completion.sha256 | "a34c30d48ee095f248720cebd91a2d61a07fd68c3058cddd57f0967212ea7d02" |
| source_gradient_attribution_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_gradient_attribution_completion.json" |
| source_gradient_attribution_completion.sha256 | "fd7c6d9a74bb305c240daf59a76fd468d81c5de922da8e5de073fc999f6dd279" |
| document_context_ablation_proposal.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/document_context_ablation_proposal.json" |
| document_context_ablation_proposal.sha256 | "e4c900ad2714b99bcb6e473a0b38543e864faade308d251421a69c1c68344813" |
| document_context_ablation_preparation.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/document_context_ablation_preparation.json" |
| document_context_ablation_preparation.sha256 | "05123c87eef3e81ccd32765d2ccd51b27d3ef0ed32639ff7a83212a93bf94074" |
| document_context_ablation_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/document_context_ablation_completion.json" |
| document_context_ablation_completion.sha256 | "152c3c69efdb44aa9a868554c915aa08f8b9743eb54d4cf0235ac5c14e2689f9" |
| low_rank_base_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/low_rank_base_v2_completion.json" |
| low_rank_base_completion.sha256 | "be0f34b5cef57216180654ff2fb511bb2096a8ebfc808f822bf89852661a6119" |
| finite_Web_constraint_budget_rejected.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/finite_Web_constraint_budget_rejected.json" |
| finite_Web_constraint_budget_rejected.sha256 | "f6995ae3c8cf449a0d39fa4f611bb8f0fc9db2b4c4852dc883b63cba728db11e" |
| block_Web_constraint_failure_analysis.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block_Web_constraint_failure_analysis.json" |
| block_Web_constraint_failure_analysis.sha256 | "d540682d8e1a8d826e9550c536884abdd3c0c6e93654289d0819206b7ec476c3" |
| fisher_parameter_anchor_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher_parameter_anchor_completion.json" |
| fisher_parameter_anchor_completion.sha256 | "fb3b01afe428f18d37df70b66d7e834995457ed22cfca2d5299bdc4d024a8480" |
| gated_shared_comparison_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/gated_shared_comparison_completion.json" |
| gated_shared_comparison_completion.sha256 | "9ef8553215231de40e7d9c541aa7d2c50507fae28c50cbb514bf288274d21647" |
| readout_adapter_probe_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout_adapter_probe_failure.json" |
| readout_adapter_probe_failure.sha256 | "00557382c7126d14821362527053abe18ac9f26f2992620537f605c48942b529" |
| readout_adapter_probe_failure_v2.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout_adapter_probe_failure_v2.json" |
| readout_adapter_probe_failure_v2.sha256 | "075ff505924210a533298117543ea64a32f87171bea923c97e058e31ea7a8f97" |
| readout_adapter_comparison_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout_adapter_comparison_completion.json" |
| readout_adapter_comparison_completion.sha256 | "59ad7cc3eca2b0d7493d7ff7e700a2faea59ceb098fc78c6f3393834d0bf2d31" |
| news_probe_failure_v1.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor_base_probe_failure_v1.json" |
| news_probe_failure_v1.sha256 | "dd7f3b6e0017eccb5e1bbb77ed1f6143bac1897683b7a105dd1fbbdb1eaec5ef" |
| news_probe_passed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor_base_probe_passed.json" |
| news_probe_passed.sha256 | "204241e6ec0b2c5572b415ad9aeaba0bf0be61cae2a07c0b38539820bf495bde" |
| livedoor_base_comparison_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor_base_comparison_completion.json" |
| livedoor_base_comparison_completion.sha256 | "1dfb188b73d55296c3fa4c621ecc9ab3c78a2740526d697b748d535221a29cf9" |
| Base_preference_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_preference_comparison_completion.json" |
| Base_preference_completion.sha256 | "84b8e6b73a6a875702eb2b66f9c36a7e1b2753e267fed22271adb8296fe4a239" |
| Base_generalization_prepared.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_generalization_prepared.json" |
| Base_generalization_prepared.sha256 | "21e38126422825c2b689d0a12a2a705c61e9e81f35ac79086a81f6fb2ee563e2" |
| Base_HQ_content_and_unseen_acceptance.path | "reports/phase6/base_hq_content_completion.json" |
| Base_HQ_content_and_unseen_acceptance.sha256 | "0c2f147b973cbd95fb760d38a4dc2d0234050b27ca40f19505464fe69218914a" |
| Base_HQ_unseen_content.source_accepted | false |
| Base_HQ_unseen_content.fixed_extractor_closed | true |
| Base_HQ_unseen_content.GPU_seconds | 0 |
| Base_source_semantic_classifier.classifier_accepted | false |
| Base_source_semantic_classifier.branch_closed | true |
| Base_source_semantic_classifier.GPU_seconds | 54.2281782880018 |
| Base_teacher_semantic_signal_proposal.path | "reports/phase6/base_teacher_semantic_signal_proposal.json" |
| Base_teacher_semantic_signal_proposal.sha256 | "8ca8dc67b8d25553ec61d2fe11abba0c076992abc05644e356c453581d6a10b4" |
| Base_teacher_semantic_signal_proposal.status | "executed_completed_conservative_gate_failed_branch_closed" |
| Base_teacher_semantic_signal_proposal.GPU_seconds | 7.486655257001985 |
| Base_teacher_semantic_signal_completion.path | "reports/phase6/teacher_semantic_signal_completion.json" |
| Base_teacher_semantic_signal_completion.sha256 | "270938beee47546142982e1f4c2f47e5801437c7b485b540c9e0c6025fd41bd6" |
| Base_teacher_semantic_signal_completion.cases | 192 |
| Base_teacher_semantic_signal_completion.effective_content_clusters | 64 |
| Base_teacher_semantic_signal_completion.paired_ci95 | [0.0, 0.22] |
| Base_teacher_semantic_signal_completion.conservative_gate | false |
| Base_teacher_semantic_signal_completion.teacher_transfer_branch_closed | true |
| Base_teacher_semantic_signal_completion.GPU_seconds | 7.486655257001985 |
| Base_teacher_semantic_signal_completion.actual_pid | 670149 |
| Base_teacher_semantic_signal_completion.actual_process_absent | true |
| Base_natural_context_contrast.probe_pairs | 64 |
| Base_natural_context_contrast.CPU_seconds | 0.3058010560052935 |
| Base_natural_context_contrast.loss_implemented | true |
| Base_natural_context_contrast.GPU_probe_started | true |
| Base_natural_context_contrast.scientific_training_started | true |
| Base_natural_context_contrast.scientific_teacher_tokens | 141421257 |
| Base_natural_context_contrast.GPU_probe_completed | true |
| current_active_scientific_jobs | ["reports/phase6/natural-context-contrast-comparison-20261007/job.json"] |
| Base_natural_context_contrast_probe_completion.path | "reports/phase6/natural_context_contrast_probe_completion.json" |
| Base_natural_context_contrast_probe_completion.sha256 | "f799a6b6d5dd660abf88aff319a0dcd242f0ac484e08177a6009d90e4cbe82c0" |
| Base_natural_context_contrast_probe_completion.actual_pid | 673463 |
| Base_natural_context_contrast_probe_completion.actual_process_absent | true |
| Base_natural_context_contrast_probe_completion.GPU_occupancy_seconds | 12.507994213985512 |
| Base_natural_context_contrast_probe_completion.verification_updates | 64 |
| Base_natural_context_contrast_probe_completion.verification_CE_teacher_tokens | 367840 |
| Base_natural_context_contrast_probe_completion.actual_CUDA_full_state_checks | 26 |
| Base_natural_context_contrast_probe_completion.measured_batch | 64 |
| Base_natural_context_contrast_probe_completion.actual_GPU_maximum_claimed | false |
| Base_natural_context_contrast_probe_completion.scientific_teacher_tokens | 0 |
| Base_natural_context_contrast_probe_completion.long_job_sampler_or_command_complete | false |
| Base_natural_context_contrast_corpus_completion.path | "reports/phase6/natural_context_contrast_corpus_completion.json" |
| Base_natural_context_contrast_corpus_completion.sha256 | "e01f5438eb81fd33784e8419b1a9b1f8d09df233441f61267a6bb834ca7b0693" |
| Base_natural_context_contrast_corpus_completion.CPU_tests | 6 |
| Base_natural_context_contrast_corpus_completion.actual_CUDA_checks | 26 |
| Base_natural_context_contrast_corpus_completion.probe_GPU_seconds | 86.68890912199276 |
| Base_natural_context_contrast_corpus_completion.verification_updates | 112 |
| Base_natural_context_contrast_corpus_completion.verification_CE_teachers | 833974 |
| Base_natural_context_contrast_corpus_completion.resident_batch | 48 |
| Base_natural_context_contrast_corpus_completion.long_command_implemented | true |
| Base_natural_context_contrast_scientific_job.actual_identity.pid | 676378 |
| Base_natural_context_contrast_scientific_job.actual_identity.start_ticks | "18891158" |
| Base_natural_context_contrast_scientific_job.actual_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| Base_natural_context_contrast_scientific_job.actual_process_last_verified_live | true |
| Base_natural_context_contrast_scientific_job.config | "configs/phase6/natural_context_contrast_comparison.json" |
| Base_natural_context_contrast_scientific_job.config_sha256 | "70b87bf762f3225fd83f40d3bde301c13e5a4b4243372e541af1a1e38e88bc29" |
| Base_natural_context_contrast_scientific_job.run | "reports/phase6/natural-context-contrast-comparison-20261007" |
| Base_natural_context_contrast_scientific_job.stage | "contrast-training" |
| Base_natural_context_contrast_scientific_job.CE_teacher_tokens_at_snapshot | 41421257 |
| Base_natural_context_contrast_scientific_job.latest_checkpoint_at_snapshot | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/contrast/checkpoint-00007250.pt" |
| Base_natural_context_contrast_scientific_job.GPU_budget_seconds | 5229 |
| Base_natural_context_contrast_scientific_job.Base_complete | false |
| Base_natural_context_contrast_scientific_job.snapshot_at | "2026-10-06T17:34:34.252216Z" |
| Base_natural_context_contrast_scientific_job.completed_arms | ["CE"] |
| Base_natural_context_contrast_review_preparation.Base_complete | false |
| Base_natural_context_contrast_review_preparation.CPU_tests | 8 |
| Base_natural_context_contrast_review_preparation.scientific_teacher_tokens | 0 |
| Base_natural_context_contrast_review_preparation.GPU_seconds | 0 |
| Base_natural_context_contrast_CE_completion.eligible_for_final_Base_validation | false |
| Base_natural_context_contrast_CE_completion.sha256 | "9039e82b17bedab5f1f0814248f2517b9b4c4417337cc0bf8cb394675c486269" |
| Base_natural_context_contrast_CE_completion.appropriate | 2 |
| Base_natural_context_contrast_CE_completion.scientific_CE_teacher_tokens | 100000000 |
| Base_natural_context_contrast_CE_completion.path | "reports/phase6/natural_context_contrast_CE_completion.json" |
| Base_natural_context_contrast_CE_completion.EOS | 19 |
| Base_natural_context_contrast_CE_completion.coherent | 2 |
| Base_natural_context_contrast_CE_completion.all80_individually_read | true |
| Base_natural_context_contrast_CE_completion.BPB | 0.998487162513845 |
| Base_natural_context_contrast_CE_completion.Base_complete | false |
| Base_natural_context_contrast_CE_completion.repetition | 45 |
| Base_natural_semantic_suite_identity.new_GPU_seconds | 0 |
| Base_natural_semantic_suite_identity.CPU_tests | 3 |
| Base_natural_semantic_suite_identity.Base_complete | false |
| Base_natural_semantic_suite_identity.legacy_teacher_suite_content_clusters | 64 |
| status | "Base_headwise_gate_CPU_verified_CUDA_science_pending" |
| latest_Base_preparation.sha256 | "29744d73eba32555a85ecfe468a31433eb4654d95a038d17bd7b07062dd20461" |
| latest_Base_preparation.path | "reports/phase6/base_headwise_gate_preparation_v2.json" |
| Base_complete | false |
| Base_adopted | false |
| current_status | "Base_fresh_parallel_residual_each2B_science_running_not_adopted" |
| updated_at | "2026-10-07T09:58:35.0921903Z" |
| last_completed_job.GPU_budget_seconds | 6880 |

</details>

<details>
<summary>reports/phase6/generation_transfer_review.json — None</summary>

[原記録](../../reports/phase6/generation_transfer_review.json) ／ SHA256: `f34ecb9e31146ce7ee0380c9ff68da982c4462fdc018acda3713518a9c94da60` ／ 240,594 bytes

| 原キー | 保存値 |
|---|---|
| decision | "Length matters on trained narrative examples; official Web dev still fails after256. Prefer short complete curriculum with explanation/general Japanese and continuation-vs-fresh strategy; no EOS-weight-only experiment now." |
| numerical_failures72 | "unresolved; no new evidence requires changing frozen model/trainer numerics" |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |

</details>
