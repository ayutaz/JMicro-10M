# 実行管理・後続準備・その他 — 4/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/block_Web_constraint_probe.json — block_Web_constraint_probe</summary>

[原記録](../../reports/phase6/block_Web_constraint_probe.json) ／ SHA256: `ef6abd79fa62ab67c1a3b1ab697367cf1cf1ebd350536981c149190ada4c7491` ／ 966,384 bytes

| 原キー | 保存値 |
|---|---|
| status | "block_Web_constraint_probe" |
| CPU_preparation_seconds | 0.11339189999853261 |
| GPU_seconds | 33.67857302899938 |
| scientific_source_CE_teacher_tokens | 0 |
| previous_related_GPU_seconds | 70.56110643898137 |
| total_related_GPU_ceiling_seconds | 2400 |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| does_not_satisfy_old_per_update_contract | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 33.67857302899938 |
| actual_job.completed_updates | 80 |
| actual_probe.initial_checks.model | true |
| actual_probe.initial_checks.optimizer | true |
| actual_probe.initial_checks.scheduler | true |
| actual_probe.initial_checks.RNG | true |
| actual_probe.initial_checks.Web_cursor | true |
| actual_probe.initial_checks.actual_LR | true |
| actual_probe.initial_checks.same_original_memory_NLL | true |
| actual_probe.reference_body_NLL | 2.5812628269195557 |
| actual_probe.setup_oracle_counts.teacher_observations | 32638 |
| actual_probe.setup_oracle_counts.gradient_teacher_tokens | 0 |
| actual_probe.setup_oracle_counts.physical_input_tokens | 32768 |
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
| actual_probe.gate.checks.history_block_boundary_index | true |
| actual_probe.gate.checks.history_focus_token_digest | true |
| actual_probe.gate.checks.history_source_teachers | true |
| actual_probe.gate.checks.history_gradient_norm | true |
| actual_probe.gate.checks.history_loss | true |
| actual_probe.gate.checks.history_block_boundary_update | true |
| actual_probe.gate.checks.history_valid_input_tokens | true |
| actual_probe.gate.checks.history_additional_teacher_tokens | true |
| actual_probe.gate.checks.history_constraint_valid_only_at_block_boundary | true |
| actual_probe.gate.checks.history_outcome_weight | true |
| actual_probe.gate.checks.history_source_input_tokens | true |
| actual_probe.gate.checks.history_actual_source_eos | true |
| actual_probe.gate.checks.history_token_digest | true |
| actual_probe.gate.checks.history_weighted_teacher_mass | true |
| actual_probe.gate.checks.history_focus_teacher_tokens | true |
| actual_probe.gate.checks.history_removed_prefix_targets | true |
| actual_probe.gate.checks.history_supervised_tokens | true |
| actual_probe.gate.checks.history_reference_suffix_teacher_tokens | true |
| actual_probe.gate.checks.history_lr | true |
| actual_probe.gate.checks.history_source_focus_teachers | true |
| actual_probe.gate.checks.history_accepted_auxiliary | true |
| actual_probe.gate.checks.history_reference_token_digest | true |
| actual_probe.gate.checks.history_actual_source_body_bytes | true |
| actual_probe.gate.checks.history_boundary_constraint | true |
| actual_probe.gate.checks.history_body_bytes_seen | true |
| actual_probe.gate.checks.history_source_body_bytes | true |
| actual_probe.gate.checks.history_physical_input_tokens | true |
| actual_probe.gate.checks.history_source_eos | true |
| actual_probe.gate.checks.history_actual_source_routes | true |
| actual_probe.gate.checks.history_update | true |
| actual_probe.gate.checks.history_source_digests | true |
| actual_probe.gate.checks.history_tokens_seen | true |
| actual_probe.gate.checks.history_actual_source_teachers | true |
| actual_probe.gate.checks.finite | true |
| actual_probe.gate.checks.actual_LR | true |
| actual_probe.gate.checks.boundary_loss_bounded | true |
| actual_probe.gate.checks.two_full20_update_blocks | true |
| actual_probe.gate.verification_teacher_tokens | 2615872 |
| actual_probe.gate.GPU_optimizer_updates | 80 |
| actual_probe.timing.terminal_save_seconds | 0.16710195899941027 |
| actual_probe.timing.verification_teacher_tokens | 2615876 |
| actual_probe.timing.auxiliary.teacher_observations | 130552 |
| actual_probe.timing.auxiliary.gradient_teacher_tokens | 0 |
| actual_probe.timing.auxiliary.physical_input_tokens | 131072 |
| actual_probe.timing.auxiliary.projected_updates | 0 |
| actual_probe.timing.auxiliary.backtracked_updates | 0 |
| actual_probe.timing.auxiliary.accepted_updates | 80 |
| actual_probe.timing.auxiliary.accepted_blocks | 4 |
| actual_probe.passed | true |
| actual_probe.GPU_optimizer_updates | 160 |
| actual_probe.verification_source_CE_teacher_tokens | 5231748 |
| actual_probe.scientific_source_CE_teacher_tokens | 0 |
| actual_probe.cached_projector_control_reused_without_new_GPU | true |
| actual_probe.cached_projector_control.reference_body_NLL | 2.5812628269195557 |
| actual_probe.cached_projector_control.ceiling_body_NLL | 2.607075455188751 |
| actual_probe.cached_projector_control.proposed_body_NLL | 2.881101965904236 |
| actual_probe.cached_projector_control.accepted | true |
| actual_probe.cached_projector_control.gradient_body_NLL | 2.881101965904236 |
| actual_probe.cached_projector_control.final_body_NLL | 2.6045130491256714 |
| actual_probe.cached_projector_control.stored_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| actual_probe.cached_projector_control.stored_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| actual_probe.cached_projector_control.initial_stored_body_NLL | 2.881101965904236 |
| actual_probe.cached_projector_control.auxiliary.teacher_observations | 163190 |
| actual_probe.cached_projector_control.auxiliary.gradient_teacher_tokens | 32638 |
| actual_probe.cached_projector_control.auxiliary.physical_input_tokens | 163840 |
| actual_probe.cached_projector_control.diagnostic_weights_not_adopted_or_saved | true |
| actual_probe.cached_projector_control.original_checkpoint_file_unchanged | true |
| actual_probe.status | "block_probe_complete" |
| actual_probe.GPU_seconds | 33.67857302899938 |
| actual_probe.Base_complete | false |
| actual_probe.Base_adopted | false |
| actual_probe.protected_test_used | false |
| actual_probe.constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| estimated_science_GPU_seconds | 910.3858267189877 |
| estimated_related_total_GPU_seconds | 1014.6255061869684 |
| planning_within_budget | true |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_probe_portable.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_probe_portable.json) ／ SHA256: `d8379ae5eedf1a297e5de47d8d0f1d124982fe20b81b54ef851ba9048d5c3c79` ／ 23,001 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/block_Web_constraint_probe.json.bytes | 966384 |
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
| files.reports/phase6/block-Web-constraint-20261006/probe/job.json.bytes | 537 |
| files.reports/phase6/block-Web-constraint-20261006/probe/latest.json.bytes | 253 |
| files.reports/phase6/block-Web-constraint-20261006/probe/latest.json.sha256 | "197155ab439670a276d924923ada3cc8bf19262f689dc0ca16050e99e93c5afe" |
| files.reports/phase6/block-Web-constraint-20261006/probe/progress-result.json.bytes | 910126 |
| files.reports/phase6/block-Web-constraint-20261006/probe/result.json.bytes | 912225 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/configs/phase6/block_Web_constraint_probe.json.bytes | 24510 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/block_Web_constraint.py.bytes | 6063 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_block_Web_constraint.ps1.bytes | 3090 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_block_Web_constraint.py.bytes | 20212 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_block_Web_constraint.py.bytes | 4132 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_block_Web_constraint.py.sha256 | "eb4511a8d9aaf99e468e12d07035b652469aa9a52124467f109d5feb4b98ce08" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json.bytes | 263 |
| files.reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json.sha256 | "768cabcc3a940cc436273c600b48f30d4bc9c8bf015804a7973763db052c497a" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_proposal.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_proposal.json) ／ SHA256: `b9059bb3fc68e6ec39c4f8ae1d5b68e0adfc7d8c2bb0edea82b4b9c4680dde53` ／ 12,773 bytes

| 原キー | 保存値 |
|---|---|
| references.soft_parameter_anchor_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter_displacement_anchor_completion.json" |
| references.soft_parameter_anchor_failure.sha256 | "cde3ccf0c0cf75db7a7854a8f66f102fb0dffe9c055fc73eb6af3a0b4fbb9002" |
| references.original_masked_staged_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/content-notes.json" |
| references.original_masked_staged_notes.sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| references.accepted_input_ledger.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved_outcome_reference_input.json" |
| references.accepted_input_ledger.sha256 | "fe12f14780541213f584ad45d7facb3c2e87251270bc61f1961bbdeb1984eb68" |
| references.per_update_budget_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/finite_Web_constraint_budget_rejected.json" |
| references.per_update_budget_failure.sha256 | "f6995ae3c8cf449a0d39fa4f611bb8f0fc9db2b4c4852dc883b63cba728db11e" |
| references.compiled_budget_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/compiled_Web_oracle_terminal.json" |
| references.compiled_budget_failure.sha256 | "220de6bd61d0c59a27d57b6304619db161b93c40a76b3b975cf01abeef9c71df" |
| measured_trigger.rank4_vs_full_coherence | [3, 10] |
| measured_trigger.rank4_vs_full_EOS | [13, 23] |
| measured_trigger.rank4_vs_full_repetition | [64, 37] |
| measured_trigger.shared_prefix_Web_BPB | 1.0136221079473724 |
| measured_trigger.original_guard_Web_BPB | 0.9715702494156145 |
| measured_trigger.masked_staged_Web_BPB | 1.0868123573684936 |
| measured_trigger.masked_staged_coherence | 35 |
| measured_trigger.masked_staged_EOS | 79 |
| measured_trigger.masked_staged_repetition | 1 |
| hypothesis | "Constrain the same native FP32/math memory loss at fixed 20-update accepted boundaries; use full source learning between boundaries and amortize loss measurement. This may retain the function without the per-update computation budget failure. Held-out quality remains unproven." |
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
| block_updates | 20 |
| previous_related_GPU_seconds | 70.56110643898137 |
| scope_difference | "Does not satisfy the old per-update constraint contract. Intermediate tentative source updates may exceed the memory ceiling. Only accepted block boundaries are bounded/saved; old per-update budget rejection stays rejected." |
| measured_budget | "3068*measured source update +154*(5 native MATH memory forwards+1 full memory gradient+snapshot/save), warmup,1.3margin+200evaluation; all previous related diagnostics and own probe included within2400 seconds." |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_terminal.json — block_Web_constraint_terminal</summary>

[原記録](../../reports/phase6/block_Web_constraint_terminal.json) ／ SHA256: `ab35ddcf50f48d246bb3e49917a32617a9caae953ed49d2adddf30d08df43ee3` ／ 7,313 bytes

| 原キー | 保存値 |
|---|---|
| status | "block_Web_constraint_terminal" |
| CPU_preparation_seconds | 0.11339189999853261 |
| GPU_seconds | 193.6470071610238 |
| scientific_source_CE_teacher_tokens | 84961352 |
| previous_related_GPU_seconds | 70.56110643898137 |
| total_related_GPU_ceiling_seconds | 2400 |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| does_not_satisfy_old_per_update_contract | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 193.6470071610238 |
| actual_job.completed_updates | 2600 |
| actual_job.total_updates | 3068 |
| actual_job.actual_teachers | 84961352 |
| actual_job.loss | 2.2298552989959717 |
| actual_job.boundary_constraint.reference_body_NLL | 2.5812628269195557 |
| actual_job.boundary_constraint.ceiling_body_NLL | 2.607075455188751 |
| actual_job.boundary_constraint.proposed_body_NLL | 2.6213528513908386 |
| actual_job.boundary_constraint.accepted | true |
| actual_job.boundary_constraint.gradient_body_NLL | 2.6213528513908386 |
| actual_job.boundary_constraint.final_body_NLL | 2.6070653200149536 |
| actual_job.boundary_constraint.scope | "accepted_block_boundary_only" |
| actual_job.boundary_constraint.block_start_update | 323015 |
| actual_job.boundary_constraint.block_end_update | 323035 |
| actual_job.boundary_constraint.block_source_updates | 20 |
| actual_job.auxiliary.teacher_observations | 5711650 |
| actual_job.auxiliary.gradient_teacher_tokens | 424294 |
| actual_job.auxiliary.physical_input_tokens | 5734400 |
| actual_job.auxiliary.projected_updates | 13 |
| actual_job.auxiliary.backtracked_updates | 13 |
| actual_job.auxiliary.accepted_updates | 2600 |
| actual_job.auxiliary.accepted_blocks | 130 |
| actual_result.finite_rejection.last_rejection.decision.reference_body_NLL | 2.5812628269195557 |
| actual_result.finite_rejection.last_rejection.decision.ceiling_body_NLL | 2.607075455188751 |
| actual_result.finite_rejection.last_rejection.decision.proposed_body_NLL | 2.621283769607544 |
| actual_result.finite_rejection.last_rejection.decision.projected | true |
| actual_result.finite_rejection.last_rejection.decision.backtracked | false |
| actual_result.finite_rejection.last_rejection.decision.accepted | false |
| actual_result.finite_rejection.last_rejection.decision.gradient_body_NLL | 2.621283769607544 |
| actual_result.finite_rejection.last_rejection.decision.gradient_norm_squared | 2.0499785066566316 |
| actual_result.finite_rejection.last_rejection.decision.projection_coefficient | 0.006943549408367611 |
| actual_result.finite_rejection.last_rejection.decision.error | "All four corrected finite proposals violate fixed memory bound" |
| actual_result.finite_rejection.last_rejection.attempted_source_gradient_teacher_tokens | 650524 |
| actual_result.finite_rejection.last_rejection.attempted_source_updates | 20 |
| actual_result.finite_rejection.last_rejection.auxiliary_completed_calls.teacher_observations | 195828 |
| actual_result.finite_rejection.last_rejection.auxiliary_completed_calls.gradient_teacher_tokens | 32638 |
| actual_result.finite_rejection.last_rejection.auxiliary_completed_calls.physical_input_tokens | 196608 |
| actual_result.finite_rejection.last_rejection.restored_last_completed_update | 323035 |
| actual_result.finite_rejection.last_rejection.rollback_scope | "entire_tentative_block" |
| actual_result.finite_rejection.last_valid_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/checkpoint-00323035.pt" |
| actual_result.finite_rejection.last_valid_checkpoint.sha256 | "1db5c4a6505b706aa9497424d6d0309efd00587345c86d03b5a2e48e66bc6744" |
| actual_result.finite_rejection.accepted_source_updates | 2600 |
| actual_result.finite_rejection.accepted_source_CE_teacher_tokens | 84961352 |
| actual_result.finite_rejection.accepted_auxiliary.forward_only_calls | 162 |
| actual_result.finite_rejection.accepted_auxiliary.gradient_calls | 13 |
| actual_result.finite_rejection.accepted_auxiliary.teacher_observations | 5711650 |
| actual_result.finite_rejection.accepted_auxiliary.gradient_teacher_tokens | 424294 |
| actual_result.finite_rejection.accepted_auxiliary.physical_input_tokens | 5734400 |
| actual_result.finite_rejection.accepted_auxiliary.projected_updates | 13 |
| actual_result.finite_rejection.accepted_auxiliary.backtracked_updates | 13 |
| actual_result.finite_rejection.accepted_auxiliary.accepted_updates | 2600 |
| actual_result.finite_rejection.accepted_auxiliary.accepted_blocks | 130 |
| actual_result.status | "block_rejection_branch_complete" |
| actual_result.GPU_seconds | 193.6470071610238 |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| actual_result.constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_terminal_portable.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_terminal_portable.json) ／ SHA256: `83969569dfc5d2ae5e6b5416199ef9ec33d74a706ec0743c8889bd80ada748cb` ／ 43,574 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/block_Web_constraint_terminal.json.bytes | 7313 |
| files.configs/phase6/block_Web_constraint.json.bytes | 24946 |
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
| files.reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/latest.json.bytes | 289 |
| files.reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/latest.json.sha256 | "f6a8a1d739573ab203c5e3abf549ca21d265cb633640acb174ce023a5f3c7244" |
| files.reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/metrics.jsonl.bytes | 10442161 |
| files.reports/phase6/block-Web-constraint-20261006/compare-result.json.bytes | 2934 |
| files.reports/phase6/block-Web-constraint-20261006/job.json.bytes | 2077 |
| files.reports/phase6/block-Web-constraint-20261006/probe/job.json.bytes | 537 |
| files.reports/phase6/block-Web-constraint-20261006/probe/latest.json.bytes | 253 |
| files.reports/phase6/block-Web-constraint-20261006/probe/latest.json.sha256 | "197155ab439670a276d924923ada3cc8bf19262f689dc0ca16050e99e93c5afe" |
| files.reports/phase6/block-Web-constraint-20261006/probe/progress-result.json.bytes | 910126 |
| files.reports/phase6/block-Web-constraint-20261006/probe/result.json.bytes | 912225 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/configs/phase6/block_Web_constraint_probe.json.bytes | 24510 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/block_Web_constraint.py.bytes | 6063 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_block_Web_constraint.ps1.bytes | 3090 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_block_Web_constraint.py.bytes | 20212 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_block_Web_constraint.py.bytes | 4132 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_block_Web_constraint.py.sha256 | "eb4511a8d9aaf99e468e12d07035b652469aa9a52124467f109d5feb4b98ce08" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/block-Web-constraint-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json.bytes | 263 |
| files.reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json.sha256 | "768cabcc3a940cc436273c600b48f30d4bc9c8bf015804a7973763db052c497a" |
| files.reports/phase6/block-Web-constraint-20261006/progress-result.json.bytes | 2468 |
| files.reports/phase6/block-Web-constraint-20261006/source/configs/phase6/block_Web_constraint.json.bytes | 24946 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/block_Web_constraint.py.bytes | 6063 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_block_Web_constraint.ps1.bytes | 3090 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_block_Web_constraint.py.bytes | 20212 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/block-Web-constraint-20261006/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/block-Web-constraint-20261006/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_block_Web_constraint.py.bytes | 4132 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_block_Web_constraint.py.sha256 | "eb4511a8d9aaf99e468e12d07035b652469aa9a52124467f109d5feb4b98ce08" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/block-Web-constraint-20261006/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/job.json) ／ SHA256: `39befaa5b824bf933c106c8663317a9fd097c65f66a66f4b182177a4beb82a0a` ／ 396 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 26.82036629700451 |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/progress-result.json) ／ SHA256: `7870dfba647c1941e8c71ffed3865265a47eb201b8e43ef68b1622f20de520fb` ／ 4,416 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.original_fullparent.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.original_fullparent.reference_checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.original_fullparent.reference_body_NLL | 2.5812628269195557 |
| checkpoints.original_fullparent.candidate_body_NLL | 2.5812628269195557 |
| checkpoints.original_fullparent.NLL_absolute_error | 0.0 |
| checkpoints.original_fullparent.gradient_parity.maximum_absolute | 1.084059476852417e-06 |
| checkpoints.original_fullparent.gradient_parity.global_relative_L2 | 6.839901273786552e-06 |
| checkpoints.original_fullparent.gradient_parity.all_elementwise | true |
| checkpoints.original_fullparent.gradient_parity.passed | true |
| checkpoints.original_fullparent.checks.NLL | true |
| checkpoints.original_fullparent.checks.forward_NLL | true |
| checkpoints.original_fullparent.checks.gradient | true |
| checkpoints.original_fullparent.checks.candidate_bitwise_repeat | true |
| checkpoints.original_fullparent.checks.no_parameter_grads | true |
| checkpoints.original_fullparent.checks.weights_unchanged | true |
| checkpoints.original_fullparent.checks.RNG_unchanged | true |
| checkpoints.original_fullparent.checks.training_state_unchanged | true |
| checkpoints.original_fullparent.checks.native_parameter_identity | true |
| checkpoints.original_fullparent.checks.final_weights_unchanged | true |
| checkpoints.original_fullparent.checks.final_RNG_unchanged | true |
| checkpoints.original_fullparent.checks.final_no_parameter_grads | true |
| checkpoints.original_fullparent.first_gradient_compile_and_warmup_seconds | 14.885353420017054 |
| checkpoints.original_fullparent.first_forward_compile_and_warmup_seconds | 6.402239440998528 |
| checkpoints.original_fullparent.native_parameter_count | 10001152 |
| checkpoints.original_fullparent.timings.forward_only_seconds | [0.04884410300292075, 0.04951516297296621, 0.04921250598272309, 0.049621373997069895] |
| checkpoints.original_fullparent.timings.gradient_seconds | [0.24126400297973305, 0.24022569000953808, 0.2410407879797276, 0.24095823502284475] |
| checkpoints.original_fullparent.reference_counts.forward_only_calls | 0 |
| checkpoints.original_fullparent.reference_counts.gradient_calls | 1 |
| checkpoints.original_fullparent.reference_counts.teacher_observations | 32638 |
| checkpoints.original_fullparent.reference_counts.gradient_teacher_tokens | 32638 |
| checkpoints.original_fullparent.reference_counts.physical_input_tokens | 32768 |
| checkpoints.original_fullparent.candidate_counts.forward_only_calls | 5 |
| checkpoints.original_fullparent.candidate_counts.gradient_calls | 6 |
| checkpoints.original_fullparent.candidate_counts.teacher_observations | 359018 |
| checkpoints.original_fullparent.candidate_counts.gradient_teacher_tokens | 195828 |
| checkpoints.original_fullparent.candidate_counts.physical_input_tokens | 360448 |
| checkpoints.original_fullparent.peak_allocated_bytes | 4825494528 |
| checkpoints.original_fullparent.peak_reserved_bytes | 4980736000 |
| checkpoints.fixed_masked_staged.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| checkpoints.fixed_masked_staged.reference_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checkpoints.fixed_masked_staged.reference_body_NLL | 2.881101965904236 |
| checkpoints.fixed_masked_staged.candidate_body_NLL | 2.8811017870903015 |
| checkpoints.fixed_masked_staged.NLL_absolute_error | 1.7881393432617188e-07 |
| checkpoints.fixed_masked_staged.gradient_parity.maximum_absolute | 2.2649765014648438e-06 |
| checkpoints.fixed_masked_staged.gradient_parity.global_relative_L2 | 1.5501922351871402e-06 |
| checkpoints.fixed_masked_staged.gradient_parity.all_elementwise | true |
| checkpoints.fixed_masked_staged.gradient_parity.passed | true |
| checkpoints.fixed_masked_staged.checks.NLL | true |
| checkpoints.fixed_masked_staged.checks.forward_NLL | true |
| checkpoints.fixed_masked_staged.checks.gradient | true |
| checkpoints.fixed_masked_staged.checks.candidate_bitwise_repeat | true |
| checkpoints.fixed_masked_staged.checks.no_parameter_grads | true |
| checkpoints.fixed_masked_staged.checks.weights_unchanged | true |
| checkpoints.fixed_masked_staged.checks.RNG_unchanged | true |
| checkpoints.fixed_masked_staged.checks.training_state_unchanged | true |
| checkpoints.fixed_masked_staged.checks.native_parameter_identity | true |
| checkpoints.fixed_masked_staged.checks.final_weights_unchanged | true |
| checkpoints.fixed_masked_staged.checks.final_RNG_unchanged | true |
| checkpoints.fixed_masked_staged.checks.final_no_parameter_grads | true |
| checkpoints.fixed_masked_staged.first_gradient_compile_and_warmup_seconds | 0.24305280498811044 |
| checkpoints.fixed_masked_staged.first_forward_compile_and_warmup_seconds | 0.04921789999934845 |
| checkpoints.fixed_masked_staged.native_parameter_count | 10001152 |
| checkpoints.fixed_masked_staged.timings.forward_only_seconds | [0.04852482001297176, 0.04920370600302704, 0.05003663498791866, 0.04912528401473537] |
| checkpoints.fixed_masked_staged.timings.gradient_seconds | [0.24244500600616448, 0.24238196801161394, 0.24193483602721244, 0.24252728698775172] |
| checkpoints.fixed_masked_staged.reference_counts.forward_only_calls | 0 |
| checkpoints.fixed_masked_staged.reference_counts.gradient_calls | 1 |
| checkpoints.fixed_masked_staged.reference_counts.teacher_observations | 32638 |
| checkpoints.fixed_masked_staged.reference_counts.gradient_teacher_tokens | 32638 |
| checkpoints.fixed_masked_staged.reference_counts.physical_input_tokens | 32768 |
| checkpoints.fixed_masked_staged.candidate_counts.forward_only_calls | 5 |
| checkpoints.fixed_masked_staged.candidate_counts.gradient_calls | 6 |
| checkpoints.fixed_masked_staged.candidate_counts.teacher_observations | 359018 |
| checkpoints.fixed_masked_staged.candidate_counts.gradient_teacher_tokens | 195828 |
| checkpoints.fixed_masked_staged.candidate_counts.physical_input_tokens | 360448 |
| checkpoints.fixed_masked_staged.peak_allocated_bytes | 4825494528 |
| checkpoints.fixed_masked_staged.peak_reserved_bytes | 5031067648 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/result.json — readonly_compiled_oracle_complete</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/result.json) ／ SHA256: `e07a122b24bc10c2a12c31d25ffc3bd147c723ffe869c82d344be7c37a343f3e` ／ 5,156 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.original_fullparent.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.original_fullparent.reference_checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.original_fullparent.reference_body_NLL | 2.5812628269195557 |
| checkpoints.original_fullparent.candidate_body_NLL | 2.5812628269195557 |
| checkpoints.original_fullparent.NLL_absolute_error | 0.0 |
| checkpoints.original_fullparent.gradient_parity.maximum_absolute | 1.084059476852417e-06 |
| checkpoints.original_fullparent.gradient_parity.global_relative_L2 | 6.839901273786552e-06 |
| checkpoints.original_fullparent.gradient_parity.all_elementwise | true |
| checkpoints.original_fullparent.gradient_parity.passed | true |
| checkpoints.original_fullparent.checks.NLL | true |
| checkpoints.original_fullparent.checks.forward_NLL | true |
| checkpoints.original_fullparent.checks.gradient | true |
| checkpoints.original_fullparent.checks.candidate_bitwise_repeat | true |
| checkpoints.original_fullparent.checks.no_parameter_grads | true |
| checkpoints.original_fullparent.checks.weights_unchanged | true |
| checkpoints.original_fullparent.checks.RNG_unchanged | true |
| checkpoints.original_fullparent.checks.training_state_unchanged | true |
| checkpoints.original_fullparent.checks.native_parameter_identity | true |
| checkpoints.original_fullparent.checks.final_weights_unchanged | true |
| checkpoints.original_fullparent.checks.final_RNG_unchanged | true |
| checkpoints.original_fullparent.checks.final_no_parameter_grads | true |
| checkpoints.original_fullparent.first_gradient_compile_and_warmup_seconds | 14.885353420017054 |
| checkpoints.original_fullparent.first_forward_compile_and_warmup_seconds | 6.402239440998528 |
| checkpoints.original_fullparent.native_parameter_count | 10001152 |
| checkpoints.original_fullparent.timings.forward_only_seconds | [0.04884410300292075, 0.04951516297296621, 0.04921250598272309, 0.049621373997069895] |
| checkpoints.original_fullparent.timings.gradient_seconds | [0.24126400297973305, 0.24022569000953808, 0.2410407879797276, 0.24095823502284475] |
| checkpoints.original_fullparent.reference_counts.forward_only_calls | 0 |
| checkpoints.original_fullparent.reference_counts.gradient_calls | 1 |
| checkpoints.original_fullparent.reference_counts.teacher_observations | 32638 |
| checkpoints.original_fullparent.reference_counts.gradient_teacher_tokens | 32638 |
| checkpoints.original_fullparent.reference_counts.physical_input_tokens | 32768 |
| checkpoints.original_fullparent.candidate_counts.forward_only_calls | 5 |
| checkpoints.original_fullparent.candidate_counts.gradient_calls | 6 |
| checkpoints.original_fullparent.candidate_counts.teacher_observations | 359018 |
| checkpoints.original_fullparent.candidate_counts.gradient_teacher_tokens | 195828 |
| checkpoints.original_fullparent.candidate_counts.physical_input_tokens | 360448 |
| checkpoints.original_fullparent.peak_allocated_bytes | 4825494528 |
| checkpoints.original_fullparent.peak_reserved_bytes | 4980736000 |
| checkpoints.fixed_masked_staged.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| checkpoints.fixed_masked_staged.reference_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checkpoints.fixed_masked_staged.reference_body_NLL | 2.881101965904236 |
| checkpoints.fixed_masked_staged.candidate_body_NLL | 2.8811017870903015 |
| checkpoints.fixed_masked_staged.NLL_absolute_error | 1.7881393432617188e-07 |
| checkpoints.fixed_masked_staged.gradient_parity.maximum_absolute | 2.2649765014648438e-06 |
| checkpoints.fixed_masked_staged.gradient_parity.global_relative_L2 | 1.5501922351871402e-06 |
| checkpoints.fixed_masked_staged.gradient_parity.all_elementwise | true |
| checkpoints.fixed_masked_staged.gradient_parity.passed | true |
| checkpoints.fixed_masked_staged.checks.NLL | true |
| checkpoints.fixed_masked_staged.checks.forward_NLL | true |
| checkpoints.fixed_masked_staged.checks.gradient | true |
| checkpoints.fixed_masked_staged.checks.candidate_bitwise_repeat | true |
| checkpoints.fixed_masked_staged.checks.no_parameter_grads | true |
| checkpoints.fixed_masked_staged.checks.weights_unchanged | true |
| checkpoints.fixed_masked_staged.checks.RNG_unchanged | true |
| checkpoints.fixed_masked_staged.checks.training_state_unchanged | true |
| checkpoints.fixed_masked_staged.checks.native_parameter_identity | true |
| checkpoints.fixed_masked_staged.checks.final_weights_unchanged | true |
| checkpoints.fixed_masked_staged.checks.final_RNG_unchanged | true |
| checkpoints.fixed_masked_staged.checks.final_no_parameter_grads | true |
| checkpoints.fixed_masked_staged.first_gradient_compile_and_warmup_seconds | 0.24305280498811044 |
| checkpoints.fixed_masked_staged.first_forward_compile_and_warmup_seconds | 0.04921789999934845 |
| checkpoints.fixed_masked_staged.native_parameter_count | 10001152 |
| checkpoints.fixed_masked_staged.timings.forward_only_seconds | [0.04852482001297176, 0.04920370600302704, 0.05003663498791866, 0.04912528401473537] |
| checkpoints.fixed_masked_staged.timings.gradient_seconds | [0.24244500600616448, 0.24238196801161394, 0.24193483602721244, 0.24252728698775172] |
| checkpoints.fixed_masked_staged.reference_counts.forward_only_calls | 0 |
| checkpoints.fixed_masked_staged.reference_counts.gradient_calls | 1 |
| checkpoints.fixed_masked_staged.reference_counts.teacher_observations | 32638 |
| checkpoints.fixed_masked_staged.reference_counts.gradient_teacher_tokens | 32638 |
| checkpoints.fixed_masked_staged.reference_counts.physical_input_tokens | 32768 |
| checkpoints.fixed_masked_staged.candidate_counts.forward_only_calls | 5 |
| checkpoints.fixed_masked_staged.candidate_counts.gradient_calls | 6 |
| checkpoints.fixed_masked_staged.candidate_counts.teacher_observations | 359018 |
| checkpoints.fixed_masked_staged.candidate_counts.gradient_teacher_tokens | 195828 |
| checkpoints.fixed_masked_staged.candidate_counts.physical_input_tokens | 360448 |
| checkpoints.fixed_masked_staged.peak_allocated_bytes | 4825494528 |
| checkpoints.fixed_masked_staged.peak_reserved_bytes | 5031067648 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| status | "readonly_compiled_oracle_complete" |
| passed | true |
| GPU_seconds | 26.82036629700451 |
| maximum_compiled_forward_seconds | 0.05003663498791866 |
| maximum_compiled_gradient_seconds | 0.24252728698775172 |
| estimated_science_with_original_math_acceptance_seconds | 3550.722645004993 |
| estimate_scope | "Planning only; new actual transactional CUDA resume/timing gate remains required." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/configs/phase6/compiled_Web_oracle.json — None</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/configs/phase6/compiled_Web_oracle.json) ／ SHA256: `b20b17acd207958098f66d05a21c9e03bfb609183840237b1108ab5c9a12e59d` ／ 7,066 bytes

| 原キー | 保存値 |
|---|---|
| GPU_budget_seconds | 120 |
| numerical_tolerances.body_NLL_absolute | 2e-06 |
| memory_binding.body_teachers | 32638 |
| memory_binding.physical_input_tokens | 32768 |
| memory_binding.common_body_bytes | 130336 |
| memory_binding.cached_samples.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-gradient-attribution-20261006/samples.pt" |
| memory_binding.cached_samples.sha256 | "d06b94ba1b78d07aeee70f4fe29b002fc16eaf05c4af2ff4686def02742640c7" |
| checkpoints.original_fullparent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.original_fullparent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.fixed_masked_staged.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| checkpoints.fixed_masked_staged.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| old_source_sha256.tests/test_finite_Web_constraint.py | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |
| previous_related_GPU_seconds | 43.74074014197686 |
| future_science_total_GPU_ceiling_seconds | 2400 |
| completion | "Both preselected weights: strict original MATH NLL/gradient parity, bitwise repeat, unchanged native weights/RNG/grad, four actual forward and gradient timings; compile warm-up counted. No optimizer, alternate compile mode/dtype/backend/checkpoint rescue." |
| scope | "TRAIN implementation probe; not future global equivalence, quality, or science authorization." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| CPU_preparation_seconds | 0.3315294579952024 |

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-launcher-20261006/launcher.json) ／ SHA256: `640ecdc802edfccc29707f81953e614d5cd78204716adfe5ed9aadc01bcaace8` ／ 109 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/compiled-Web-oracle-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/compiled-Web-oracle-launcher-20261006/result.json) ／ SHA256: `05eb45edb33c30a174e09db84748159c29d1691897b42bb8e7f9fe14655bb659` ／ 181 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/compiled_Web_oracle_terminal.json — readonly_compiled_Web_oracle_terminal</summary>

[原記録](../../reports/phase6/compiled_Web_oracle_terminal.json) ／ SHA256: `220de6bd61d0c59a27d57b6304619db161b93c40a76b3b975cf01abeef9c71df` ／ 8,547 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_compiled_Web_oracle_terminal" |
| CPU_preparation_seconds | 0.2164402320049703 |
| GPU_seconds | 26.82036629700451 |
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
| unlaunched_setup_correction.reason | "Separate first no_grad and autograd compiler specializations before steady timings; both warmups stay in real GPU cost." |
| unlaunched_setup_correction.GPU_seconds | 0 |
| unlaunched_setup_correction.source.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/scripts/probe_compiled_Web_oracle.py" |
| unlaunched_setup_correction.source.sha256 | "524913823a28d4c811b8243def54de6edc18e0804c9845e6785d202f2deec9bf" |
| unlaunched_setup_correction.config.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/configs/phase6/compiled_Web_oracle.json" |
| unlaunched_setup_correction.config.sha256 | "b20b17acd207958098f66d05a21c9e03bfb609183840237b1108ab5c9a12e59d" |
| unlaunched_setup_correction.old_files_preserved | true |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 26.82036629700451 |
| actual_result.checkpoints.original_fullparent.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| actual_result.checkpoints.original_fullparent.reference_checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| actual_result.checkpoints.original_fullparent.reference_body_NLL | 2.5812628269195557 |
| actual_result.checkpoints.original_fullparent.candidate_body_NLL | 2.5812628269195557 |
| actual_result.checkpoints.original_fullparent.NLL_absolute_error | 0.0 |
| actual_result.checkpoints.original_fullparent.gradient_parity.maximum_absolute | 1.084059476852417e-06 |
| actual_result.checkpoints.original_fullparent.gradient_parity.global_relative_L2 | 6.839901273786552e-06 |
| actual_result.checkpoints.original_fullparent.gradient_parity.all_elementwise | true |
| actual_result.checkpoints.original_fullparent.gradient_parity.passed | true |
| actual_result.checkpoints.original_fullparent.checks.NLL | true |
| actual_result.checkpoints.original_fullparent.checks.forward_NLL | true |
| actual_result.checkpoints.original_fullparent.checks.gradient | true |
| actual_result.checkpoints.original_fullparent.checks.candidate_bitwise_repeat | true |
| actual_result.checkpoints.original_fullparent.checks.no_parameter_grads | true |
| actual_result.checkpoints.original_fullparent.checks.weights_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.RNG_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.training_state_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.native_parameter_identity | true |
| actual_result.checkpoints.original_fullparent.checks.final_weights_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.final_RNG_unchanged | true |
| actual_result.checkpoints.original_fullparent.checks.final_no_parameter_grads | true |
| actual_result.checkpoints.original_fullparent.first_gradient_compile_and_warmup_seconds | 14.885353420017054 |
| actual_result.checkpoints.original_fullparent.first_forward_compile_and_warmup_seconds | 6.402239440998528 |
| actual_result.checkpoints.original_fullparent.native_parameter_count | 10001152 |
| actual_result.checkpoints.original_fullparent.timings.forward_only_seconds | [0.04884410300292075, 0.04951516297296621, 0.04921250598272309, 0.049621373997069895] |
| actual_result.checkpoints.original_fullparent.timings.gradient_seconds | [0.24126400297973305, 0.24022569000953808, 0.2410407879797276, 0.24095823502284475] |
| actual_result.checkpoints.original_fullparent.reference_counts.forward_only_calls | 0 |
| actual_result.checkpoints.original_fullparent.reference_counts.gradient_calls | 1 |
| actual_result.checkpoints.original_fullparent.reference_counts.teacher_observations | 32638 |
| actual_result.checkpoints.original_fullparent.reference_counts.gradient_teacher_tokens | 32638 |
| actual_result.checkpoints.original_fullparent.reference_counts.physical_input_tokens | 32768 |
| actual_result.checkpoints.original_fullparent.candidate_counts.forward_only_calls | 5 |
| actual_result.checkpoints.original_fullparent.candidate_counts.gradient_calls | 6 |
| actual_result.checkpoints.original_fullparent.candidate_counts.teacher_observations | 359018 |
| actual_result.checkpoints.original_fullparent.candidate_counts.gradient_teacher_tokens | 195828 |
| actual_result.checkpoints.original_fullparent.candidate_counts.physical_input_tokens | 360448 |
| actual_result.checkpoints.original_fullparent.peak_allocated_bytes | 4825494528 |
| actual_result.checkpoints.original_fullparent.peak_reserved_bytes | 4980736000 |
| actual_result.checkpoints.fixed_masked_staged.reference_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| actual_result.checkpoints.fixed_masked_staged.reference_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| actual_result.checkpoints.fixed_masked_staged.reference_body_NLL | 2.881101965904236 |
| actual_result.checkpoints.fixed_masked_staged.candidate_body_NLL | 2.8811017870903015 |
| actual_result.checkpoints.fixed_masked_staged.NLL_absolute_error | 1.7881393432617188e-07 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.maximum_absolute | 2.2649765014648438e-06 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.global_relative_L2 | 1.5501922351871402e-06 |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.all_elementwise | true |
| actual_result.checkpoints.fixed_masked_staged.gradient_parity.passed | true |
| actual_result.checkpoints.fixed_masked_staged.checks.NLL | true |
| actual_result.checkpoints.fixed_masked_staged.checks.forward_NLL | true |
| actual_result.checkpoints.fixed_masked_staged.checks.gradient | true |
| actual_result.checkpoints.fixed_masked_staged.checks.candidate_bitwise_repeat | true |
| actual_result.checkpoints.fixed_masked_staged.checks.no_parameter_grads | true |
| actual_result.checkpoints.fixed_masked_staged.checks.weights_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.RNG_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.training_state_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.native_parameter_identity | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_weights_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_RNG_unchanged | true |
| actual_result.checkpoints.fixed_masked_staged.checks.final_no_parameter_grads | true |
| actual_result.checkpoints.fixed_masked_staged.first_gradient_compile_and_warmup_seconds | 0.24305280498811044 |
| actual_result.checkpoints.fixed_masked_staged.first_forward_compile_and_warmup_seconds | 0.04921789999934845 |
| actual_result.checkpoints.fixed_masked_staged.native_parameter_count | 10001152 |
| actual_result.checkpoints.fixed_masked_staged.timings.forward_only_seconds | [0.04852482001297176, 0.04920370600302704, 0.05003663498791866, 0.04912528401473537] |
| actual_result.checkpoints.fixed_masked_staged.timings.gradient_seconds | [0.24244500600616448, 0.24238196801161394, 0.24193483602721244, 0.24252728698775172] |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.forward_only_calls | 0 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.gradient_calls | 1 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.teacher_observations | 32638 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.gradient_teacher_tokens | 32638 |
| actual_result.checkpoints.fixed_masked_staged.reference_counts.physical_input_tokens | 32768 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.forward_only_calls | 5 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.gradient_calls | 6 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.teacher_observations | 359018 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.gradient_teacher_tokens | 195828 |
| actual_result.checkpoints.fixed_masked_staged.candidate_counts.physical_input_tokens | 360448 |
| actual_result.checkpoints.fixed_masked_staged.peak_allocated_bytes | 4825494528 |
| actual_result.checkpoints.fixed_masked_staged.peak_reserved_bytes | 5031067648 |
| actual_result.optimizer_updates | 0 |
| actual_result.new_source_CE_teacher_tokens | 0 |
| actual_result.status | "readonly_compiled_oracle_complete" |
| actual_result.passed | true |
| actual_result.GPU_seconds | 26.82036629700451 |
| actual_result.maximum_compiled_forward_seconds | 0.05003663498791866 |
| actual_result.maximum_compiled_gradient_seconds | 0.24252728698775172 |
| actual_result.estimated_science_with_original_math_acceptance_seconds | 3550.722645004993 |
| actual_result.estimate_scope | "Planning only; new actual transactional CUDA resume/timing gate remains required." |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| planning_within_budget | false |
| completion_scope | "Readonly implementation evidence, not qualified Base/adoption." |

</details>

<details>
<summary>reports/phase6/compiled_Web_oracle_terminal_portable.json — None</summary>

[原記録](../../reports/phase6/compiled_Web_oracle_terminal_portable.json) ／ SHA256: `3e22a8108141c70f406685ff9545522b3b9b27241bb941ddb07d8df9f768caa3` ／ 4,698 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/compiled_Web_oracle_terminal.json.bytes | 8547 |
| files.configs/phase6/compiled_Web_oracle.json.bytes | 7066 |
| files.scripts/record_compiled_Web_oracle.py.bytes | 7228 |
| files.scripts/probe_compiled_Web_oracle.py.bytes | 12980 |
| files.scripts/probe_compiled_Web_oracle.ps1.bytes | 2616 |
| files.reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/configs/phase6/compiled_Web_oracle.json.bytes | 7066 |
| files.reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation.json.bytes | 1581 |
| files.reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation_evidence.tar.gz.bytes | 10720 |
| files.reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/reports/phase6/compiled_Web_oracle_preparation_portable.json.bytes | 1100 |
| files.reports/phase6/compiled-Web-oracle-20261006/unlaunched-setup-v1/scripts/probe_compiled_Web_oracle.py.bytes | 12397 |
| files.reports/phase6/compiled-Web-oracle-20261006/job.json.bytes | 396 |
| files.reports/phase6/compiled-Web-oracle-20261006/progress-result.json.bytes | 4416 |
| files.reports/phase6/compiled-Web-oracle-20261006/result.json.bytes | 5156 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/configs/phase6/compiled_Web_oracle.json.bytes | 7066 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/finite_Web_constraint.py.bytes | 16012 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/probe_compiled_Web_oracle.ps1.bytes | 2616 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/probe_compiled_Web_oracle.py.bytes | 12980 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/probe_finite_Web_oracle_efficiency.ps1.bytes | 2652 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/probe_finite_Web_oracle_efficiency.py.bytes | 14444 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/run_finite_Web_constraint.ps1.bytes | 3095 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/scripts/run_finite_Web_constraint.py.bytes | 27095 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/tests/test_finite_Web_constraint.py.bytes | 5693 |
| files.reports/phase6/compiled-Web-oracle-20261006/source/tests/test_finite_Web_constraint.py.sha256 | "c5b4e67e6fe9fe0c44b3e3a8e156c8944683c6542eae7891de2dfac554e7898e" |

</details>

<details>
<summary>reports/phase6/complete_document_annotations.json — None</summary>

[原記録](../../reports/phase6/complete_document_annotations.json) ／ SHA256: `f4b1e0c332f3c1e14731c3778060940491e98c4f68f5f848abf2e975179337d4` ／ 15,114 bytes

| 原キー | 保存値 |
|---|---|
| rubric.grammar | "0 broken syntax;1 partial/awkward;2 locally natural Japanese; cap-ending fragment alone is not grammar0" |
| rubric.relevance | "0 loses supplied subject/condition/topic;1 partial fit;2 preserves prefix and conditions" |
| rubric.coherence | "0 strong loops/contradiction/incoherent;1 weak/redundant development;2 coherent meaningful development" |
| rubric.completion | "1 only actual natural EOS with meaningful topic-relevant ending; cap ending0" |

</details>

<details>
<summary>reports/phase6/complete_document_completion.json — passed</summary>

[原記録](../../reports/phase6/complete_document_completion.json) ／ SHA256: `3f793cdcc873c22dfdcbaf32e0366a1346ed09e6f0a0d6c4e9157aa39e8bc1d8` ／ 14,544 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checks.stage1_actual_builder_complete_exited_budget | true |
| checks.stage1_actual100to120M_whole_train_data | true |
| checks.stage1_new_stream_and_index_hashes | true |
| checks.stage1_random40_content_actual_binding | true |
| checks.stage1_random40_actual_original_full_documents_no_slicing | true |
| checks.stage2_actual_completed_job_exited_not_proposal | true |
| checks.stage2_new_data_actual_save_resume_separate_account | true |
| checks.stage2_actual_related_tests_passed | true |
| checks.stage3_primary_actual_state_raw_and80_review | true |
| checks.stage3_ineligible_full_not_started | true |
| checks.stage4_judgment_matches_actual_gate_and_report | true |
| checks.stage4_no_false_project_quality_completion | true |
| checks.stage4_actual_data_learning_amounts_reported | true |
| checks.stage4_actual_original_UI_process_live | true |
| checks.stage4_HTTP_original10B_idle | true |
| checks.frozen_source_scripts/run_complete_document_500m.py | true |
| checks.frozen_source_scripts/run_complete_document_500m.ps1 | true |
| checks.frozen_source_scripts/review_complete_document_500m.py | true |
| checks.frozen_source_scripts/prepare_complete_document_pool.py | true |
| checks.frozen_source_src/jmicro/whole_short_text.py | true |
| checks.frozen_source_scripts/run_story20_budget.py | true |
| checks.frozen_source_scripts/run_story20_budget.ps1 | true |
| checks.frozen_source_scripts/prepare_story20_budget.py | true |
| checks.frozen_source_scripts/prepare_story20_budget.ps1 | true |
| checks.frozen_source_scripts/review_story20_budget.py | true |
| checks.frozen_source_scripts/run_story20_low_lr.py | true |
| checks.frozen_source_scripts/run_story20_low_lr.ps1 | true |
| checks.frozen_source_scripts/run_story10_low_lr.py | true |
| checks.frozen_source_scripts/run_story10_low_lr.ps1 | true |
| checks.frozen_source_scripts/run_story10_comparison.py | true |
| checks.frozen_source_scripts/run_story10_comparison.ps1 | true |
| checks.frozen_source_scripts/run_complete_text_comparison.py | true |
| checks.frozen_source_scripts/run_complete_text_comparison.ps1 | true |
| checks.frozen_source_src/jmicro/coherent_units.py | true |
| checks.frozen_source_scripts/prepare_coherent_text.py | true |
| checks.frozen_source_scripts/inspect_complete_text_data.py | true |
| checks.frozen_source_scripts/prepare_story_text.py | true |
| checks.frozen_source_src/jmicro/eos_pilot.py | true |
| checks.frozen_source_src/jmicro/low_lr_pilot.py | true |
| checks.frozen_source_scripts/run_eos_short_pilot.py | true |
| checks.frozen_source_scripts/run_eos_complete_100m.py | true |
| checks.frozen_source_scripts/evaluate_japanese_base.py | true |
| checks.frozen_source_src/jmicro/japanese_evaluation.py | true |
| checks.frozen_source_src/jmicro/readiness.py | true |
| checks.frozen_source_src/jmicro/evaluation_memory.py | true |
| checks.frozen_source_src/jmicro/tokenizer.py | true |
| checks.frozen_source_scripts/evaluate_complete_text_full.py | true |
| checks.frozen_source_scripts/evaluate_complete_text_full.ps1 | true |
| checks.frozen_source_scripts/run_eos_5b_finish.py | true |
| checks.frozen_source_scripts/compare_base_10b.py | true |
| checks.frozen_source_scripts/compare_base_5b.py | true |
| checked_at | "2026-10-05T05:42:02.268243Z" |
| source_sha256./home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards/manifest.json | "2d7b3d0b21fa9267c8f3bf8121f1a156f68f843c9676c2b2b004b01ab77d30de" |
| source_sha256./home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards/ready.json | "2b51642a195d9b64846ba306835953fbb2d6bf323587d301b5c6deea162dd722" |
| source_sha256./home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards/samples.json | "889b2f16350ca95fc78c2a5cf7c814b08e3275a64f6c444e6ac6524c6958c965" |
| source_sha256./home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards/content-review.json | "c4ce6f48a0df4eb7d276ca1ff10f322fb85253a28e2767f2729463da1b7f21fc" |
| source_sha256./home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/job.json | "b1dc916da9631d66e05497231d24161b5152b26575d890573ff1311352d55089" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/result.json | "97154381b58016d4fcafe970a1846b244c9f8b9ec32176c86934f67dd5964fb4" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/review.json | "c308c50a4ffc4936b7c2cd2fbfaea21428ae0ad0dd5232f2f9977a3dfc231b06" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/annotations.json | "f4b1e0c332f3c1e14731c3778060940491e98c4f68f5f848abf2e975179337d4" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/screen-job.json | "52a0da3c060ebe6cad898bfdfd608aa8050d561e371810336e104ee236006c9e" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/judgment.json | "0891327e4e52e5bf696d93acf8fb4fd753c17e9061417be279ccd054b2e85be4" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/tests.xml | "d191c71c76aba1e068605cfa22822eaee7fd4dc9f6c2093598abd8a2add8320b" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/docs/55_complete_document_500m_results.md | "98c9ad88e8bdbd13fff444c46c4663be50c9f3a2e528bbd29374b8f3a0a0d3c9" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/complete_document_500m.json | "2e0ec1f3f5aec4ff3d9dc08a2a8b3799ebb205a5ef24faa5a0747be09fde8413" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/schemas/configs/phase6/complete_document_500m.schema.json | "1cf6fecaf7b86fe10986d9eb98028b3f322d95d7c24d2cb41c84ace88150138f" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/result/coherent20/evaluation/result.json | "338fa68df832a8fddfa63c6038c1b8f9c840ccbd9d8ee508c617494f4498a455" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/coherent20-full.json | "65b1e23a790b6c59c0838fcadcb9aae8e99565c7fd10327dd1ea7ae535e0e471" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_complete_document_500m.py | "ce6dc949a84dd398854d4561bdcec6949b4baec9024a16555497e8cfdd317b47" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_complete_document_500m.ps1 | "ccda171c89065f2aa90c441963f5ee10214e1a91789a1e3b5eebf4c55963d3a0" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/review_complete_document_500m.py | "cae0ce182c434d447fc0321e4a5b58f1566f353a090db1d34f57be1807c0a464" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/prepare_complete_document_pool.py | "e83f8b0f2d3647104c682359aa6579e3e292a26e125927a177d3bd4df9265fc8" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256./home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| UI.status | "running" |
| UI.additional_training_tokens | 0 |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| HTTP_model.training_tokens | 10000007168 |
| HTTP_model.update | 305176 |
| HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| stage4_adopted | false |
| scientific_tokens | 500006912 |
| verification_tokens | 262144 |
| protected_test_used | false |
| local_commit_checked_separately_after_delivery | true |

</details>

<details>
<summary>reports/phase6/complete_document_data.json — None</summary>

[原記録](../../reports/phase6/complete_document_data.json) ／ SHA256: `82b66ec0511254074dc6095c1f0bd8296af5fc8a8c80d163957e51699669c2d8` ／ 71,117 bytes

| 原キー | 保存値 |
|---|---|
| ready.status | "ready_pending_content_inspection" |
| ready.binding.budget_seconds | 1800 |
| ready.binding.seed | 20261005 |
| ready.binding.continuation.reason | "Initial bounded extraction yielded76.77M in44.48s; read unseen remainder without weakening quality or amount gates" |
| ready.totals.tokens | 110000202 |
| ready.totals.documents | 668680 |
| ready.totals.body_bytes | 435662538 |
| ready.by_source.story.tokens | 30000063 |
| ready.by_source.story.documents | 343891 |
| ready.by_source.story.body_bytes | 117359445 |
| ready.by_source.web.tokens | 80000139 |
| ready.by_source.web.documents | 324789 |
| ready.by_source.web.body_bytes | 318303093 |
| ready.scan.story_scan_tokens | 40000000 |
| ready.scan.story_scan_documents | 442235 |
| ready.scan.web_scan_tokens | 6840000000 |
| ready.scan.web_scan_documents | 14513719 |
| ready.body_tokens_mean | 162.50350242268348 |
| ready.EOS_per_1000_tokens | 6.078897927841987 |
| ready.whole_original_documents | true |
| ready.new_Web_source_tokens | 0 |
| ready.independently_unique_tokens | "not certified; existing Web is reused and broad overlap audit incomplete" |
| ready.seconds | 73.34042250600032 |
| samples.seed | 20261005 |
| samples.method | "uniform reservoir over all accepted whole documents" |
| content_review.accepted_for_experiment | true |
| content_review.samples_sha256 | "889b2f16350ca95fc78c2a5cf7c814b08e3275a64f6c444e6ac6524c6958c965" |
| content_review.decision | "Accepted only for the bounded data-composition comparison: complete original documents, topical breadth and no slicing; eight weak examples remain, so semantic quality or factual accuracy is not certified." |
| actual_preparation_job.status | "complete" |
| actual_preparation_job.binding.budget_seconds | 1800 |
| actual_preparation_job.binding.seed | 20261005 |
| actual_preparation_job.binding.continuation.reason | "Initial bounded extraction yielded76.77M in44.48s; read unseen remainder without weakening quality or amount gates" |
| actual_preparation_job.elapsed_seconds | 73.3408106479983 |
| actual_preparation_job.counts.story_scan_tokens | 40000000 |
| actual_preparation_job.counts.story_scan_documents | 442235 |
| actual_preparation_job.counts.web_scan_tokens | 6840000000 |
| actual_preparation_job.counts.web_scan_documents | 14513719 |
| actual_preparation_job.totals.tokens | 110000202 |
| actual_preparation_job.totals.documents | 668680 |
| actual_preparation_job.totals.body_bytes | 435662538 |
| actual_preparation_job.by_source.story.tokens | 30000063 |
| actual_preparation_job.by_source.story.documents | 343891 |
| actual_preparation_job.by_source.story.body_bytes | 117359445 |
| actual_preparation_job.by_source.web.tokens | 80000139 |
| actual_preparation_job.by_source.web.documents | 324789 |
| actual_preparation_job.by_source.web.body_bytes | 318303093 |

</details>

<details>
<summary>reports/phase6/complete_document_judgment.json — complete_stages1to4</summary>

[原記録](../../reports/phase6/complete_document_judgment.json) ／ SHA256: `0891327e4e52e5bf696d93acf8fb4fd753c17e9061417be279ccd054b2e85be4` ／ 2,145 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_stages1to4" |
| adopted | false |
| decision | "Reject new110M whole-document composition; saved story20%500M remains research candidate; Base/Chat quality unmet" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/whole20/checkpoint-00320435.pt" |
| checkpoint_sha256 | "b10e43919204b84fc39fa74f2bfe4d4b48497f82151374c9a4414914e8a8b00d" |
| prepared_short_tokens | 110000202 |
| model_training_input_tokens | 10500014080 |
| scientific_tokens | 500006912 |
| verification_tokens | 262144 |
| GPU_seconds | 853.6776972000007 |
| protected_test_used | false |
| next_proposal.primary_GPU_budget_seconds | 1800 |
| next_proposal.conditional_full_GPU_budget_seconds | 1800 |
| next_proposal.completion_condition | "Same original gates plus coherent/appropriate endings&gt;=27of80, paired coherence lower95percent&gt;0, EOS&gt;=37/repetition&lt;=18; full only when eligible, report/local commit/restore original UI/stop" |

</details>

<details>
<summary>reports/phase6/complete_document_result.json — complete_scientific_primary_and_content_review</summary>

[原記録](../../reports/phase6/complete_document_result.json) ／ SHA256: `5e67ff5f49482e73f8df31b6fa64f47371e00b68b0144f133250f391e2bd5cdf` ／ 261,562 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_scientific_primary_and_content_review" |
| source_result_status | "complete_pending_content_review" |
| trained.status | "complete" |
| trained.binding.parent.update | 305176 |
| trained.binding.parent.tokens_seen | 10000007168 |
| trained.binding.source_sha256.scripts/run_complete_document_500m.py | "ce6dc949a84dd398854d4561bdcec6949b4baec9024a16555497e8cfdd317b47" |
| trained.binding.source_sha256.scripts/run_complete_document_500m.ps1 | "ccda171c89065f2aa90c441963f5ee10214e1a91789a1e3b5eebf4c55963d3a0" |
| trained.binding.source_sha256.scripts/review_complete_document_500m.py | "cae0ce182c434d447fc0321e4a5b58f1566f353a090db1d34f57be1807c0a464" |
| trained.binding.source_sha256.scripts/prepare_complete_document_pool.py | "e83f8b0f2d3647104c682359aa6579e3e292a26e125927a177d3bd4df9265fc8" |
| trained.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| trained.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| trained.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| trained.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| trained.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| trained.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| trained.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| trained.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| trained.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| trained.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| trained.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| trained.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| trained.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/whole20/checkpoint-00320435.pt" |
| trained.checkpoint_sha256 | "b10e43919204b84fc39fa74f2bfe4d4b48497f82151374c9a4414914e8a8b00d" |
| trained.update | 320435 |
| trained.tokens | 10500014080 |
| trained.additional_input_tokens | 500006912 |
| trained.source_tokens.web | 400031744 |
| trained.source_tokens.short | 99975168 |
| trained.source_eos_teachers.web | 846893 |
| trained.source_eos_teachers.short | 607745 |
| trained.sampler.kind | "eos-pilot-mixture-v1" |
| trained.sampler.position | 15259 |
| trained.sampler.web.seed | 42 |
| trained.sampler.web.epoch | 0 |
| trained.sampler.web.position | 10156288 |
| trained.sampler.web.context | 1024 |
| trained.sampler.web.blocks | 11939276 |
| trained.sampler.short.seed | 42 |
| trained.sampler.short.epoch | 0 |
| trained.sampler.short.position | 97632 |
| trained.sampler.short.context | 1024 |
| trained.sampler.short.blocks | 107422 |
| trained.sampler.source_tokens.web | 400031744 |
| trained.sampler.source_tokens.short | 99975168 |
| trained.sampler.source_eos.web | 846893 |
| trained.sampler.source_eos.short | 607745 |
| trained.training_seconds | 745.5102910599962 |
| trained.checkpoint_role | "result" |
| scientific_tokens | 500006912 |
| verification_tokens | 262144 |
| resume_gate.passed | true |
| resume_gate.checks.model | true |
| resume_gate.checks.optimizer | true |
| resume_gate.checks.scheduler | true |
| resume_gate.checks.rng | true |
| resume_gate.checks.sampler | true |
| resume_gate.checks.tokens | true |
| resume_gate.checks.supervised_tokens | true |
| resume_gate.checks.body_bytes | true |
| resume_gate.checks.token_digest | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.model_config | true |
| resume_gate.checks.implementation_sha256 | true |
| resume_gate.checks.pilot_implementation_sha256 | true |
| resume_gate.checks.pilot_binding | true |
| resume_gate.checks.update | true |
| resume_gate.checks.lineage | true |
| resume_gate.checks.history_loss | true |
| resume_gate.checks.history_gradient_norm | true |
| resume_gate.checks.history_lr | true |
| resume_gate.checks.history_tokens_seen | true |
| resume_gate.checks.history_supervised_tokens | true |
| resume_gate.checks.history_body_bytes_seen | true |
| resume_gate.checks.history_token_digest | true |
| resume_gate.checks.finite_losses_gradients | true |
| resume_gate.checks.two_short_two_web_updates | true |
| resume_gate.binding.parent.update | 305176 |
| resume_gate.binding.parent.tokens_seen | 10000007168 |
| resume_gate.binding.source_sha256.scripts/run_complete_document_500m.py | "ce6dc949a84dd398854d4561bdcec6949b4baec9024a16555497e8cfdd317b47" |
| resume_gate.binding.source_sha256.scripts/run_complete_document_500m.ps1 | "ccda171c89065f2aa90c441963f5ee10214e1a91789a1e3b5eebf4c55963d3a0" |
| resume_gate.binding.source_sha256.scripts/review_complete_document_500m.py | "cae0ce182c434d447fc0321e4a5b58f1566f353a090db1d34f57be1807c0a464" |
| resume_gate.binding.source_sha256.scripts/prepare_complete_document_pool.py | "e83f8b0f2d3647104c682359aa6579e3e292a26e125927a177d3bd4df9265fc8" |
| resume_gate.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| resume_gate.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| resume_gate.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| resume_gate.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| resume_gate.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| resume_gate.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| resume_gate.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| resume_gate.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| resume_gate.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| resume_gate.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| resume_gate.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| resume_gate.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| resume_gate.seconds | 10.27900094800134 |
| resume_gate.GPU_optimizer_updates | 8 |
| resume_gate.input_tokens | 262144 |
| resume_gate.schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| resume_gate.checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/complete-document-500m-20261005/resume-gate/resumed.pt"] |
| GPU_seconds | 853.6776972000007 |
| summary.grammar_score2 | 17 |
| summary.relevance_score2 | 15 |
| summary.coherence_score2 | 9 |
| summary.appropriate_EOS | 8 |
| rates.eos | 17 |
| rates.repetition | 31 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| BPB | 0.9728888646548877 |
| conditional_full.reason | "New improvement gates against saved story500M all failed; no eligible full job launched" |
| source_origins.sampler.seed | 42 |
| source_origins.sampler.epoch | 0 |
| source_origins.sampler.position | 97632 |
| source_origins.sampler.context | 1024 |
| source_origins.sampler.blocks | 107422 |
| source_origins.whole_scientific_run.story | 27265983 |
| source_origins.whole_scientific_run.web | 472740929 |
| source_origins.whole_scientific_run.total | 500006912 |
| source_origins.scientific_story_fraction | 0.05453121216052309 |
| source_origins.short_EOS_teachers | 607745 |
| source_origins.old_story_short_EOS_teachers | 1105092 |
| source_origins.protected_test_used | false |
| source_origins.checked_at | "2026-10-05T05:38:45.839894Z" |
| UI.status | "running" |
| UI.additional_training_tokens | 0 |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/complete_document_review.json — passed</summary>

[原記録](../../reports/phase6/complete_document_review.json) ／ SHA256: `c308c50a4ffc4936b7c2cd2fbfaea21428ae0ad0dd5232f2f9977a3dfc231b06` ／ 151,889 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checks.actual_job_complete_exited_within_budget | true |
| checks.actual_new_data_CUDA_exact_save_resume | true |
| checks.single500M_scientific_budget | true |
| checks.fixed80_exact_IDs_and_prefixes | true |
| checks.annotations_bound_to_actual_raw_generation | true |
| checks.all80_individual_content_notes | true |
| checks.appropriate_completion_only_actual_EOS | true |
| checks.actual_checkpoint_finite_full_state_hash | true |
| checks.all15259_actual_contiguous_finite_updates | true |
| checks.checkpoint_all_resume_states_and_counters | true |
| checks.fixed_saved_control_schedule_and_LR | true |
| checks.source_tokens_and_routes_actual | true |
| checks.actual_short_exposure_and_cursor_disclosed | true |
| checks.common256_body_bytes_tokens_actual_NLL | true |
| checks.raw_rates_recomputed | true |
| checks.all_Japanese_diagnostics_complete_and_RNG_isolated | true |
| checks.matched_saved_controls_same_schedule_parent_budget | true |
| checks.controls_fixed80_alignment_d18e3e17 | true |
| checks.controls_fixed80_alignment_f336806b | true |
| checks.paired_actual_diagnostic_IDs_semantics | true |
| checks.paired_actual_diagnostic_IDs_jblimp | true |
| checks.paired_actual_diagnostic_IDs_jcqa | true |
| summary.grammar_score2 | 17 |
| summary.relevance_score2 | 15 |
| summary.coherence_score2 | 9 |
| summary.appropriate_EOS | 8 |
| rates.eos | 17 |
| rates.repetition | 31 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| BPB | 0.9728888646548877 |
| diagnostics.semantics.primary.accuracy.point | 0.640625 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.59375, 0.6875] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.640625 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.6041666666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.6458333333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.6041666666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6037797328119909 |
| diagnostics.semantics.per_token_secondary.mcc | 0.20874143036171647 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7734138972809668 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7310422960725076, 0.8157099697885196] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7734138972809668 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7129909365558912 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6646525679758308, 0.7613293051359517] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7129909365558912 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41622574955908287 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7613293051359517 |
| diagnostics.jcqa.primary.accuracy.point | 0.338248436103664 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3109919571045576, 0.3632707774798928] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.3386952636282395 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3221626452189455 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2957998212689902, 0.34898346738159064] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.322609472743521 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.32138613069088134 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.15318978654059767 |
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
| diagnostics.semantic_both_contexts.correct | 28 |
| original_selection.original_mixture.EOS_at_least8_more | true |
| original_selection.original_mixture.repetition_no_worse | true |
| original_selection.original_mixture.no_empty_role_unicode | true |
| original_selection.original_mixture.BPB_degradation_at_most1percent | true |
| original_selection.coherence_gain_at_least8 | true |
| original_selection.paired_coherence_CI_lower_above0 | true |
| original_selection.coherence_difference_count | 9 |
| original_selection.paired_CI95 | [0.05, 0.1875] |
| original_selection.eligible_for_full | true |
| new_improvement.coherence_gain_over_story_at_least8 | false |
| new_improvement.paired_CI_lower_above0 | false |
| new_improvement.EOS_no_worse_than_story | false |
| new_improvement.repetition_no_worse_than_story | false |
| new_improvement.appropriate_completion_at_least27 | false |
| paired_coherence_vs_story.difference_count | -10 |
| paired_coherence_vs_story.CI95 | [-0.225, -0.025] |
| paired_coherence_vs_story.clustered.point | -0.125 |
| paired_coherence_vs_story.clustered.ci95 | [-0.225, -0.025] |
| paired_coherence_vs_story.clustered.units | 80 |
| paired_coherence_vs_story.clustered.examples | 80 |
| paired_coherence_vs_story.clustered.unit | "family/prompt" |
| paired_coherence_vs_story.clustered.seed | 42 |
| paired_coherence_vs_story.clustered.repetitions | 2000 |
| paired_coherence_vs_story.clustered.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics_vs_story.semantics.point | 0.020833333333333332 |
| paired_diagnostics_vs_story.semantics.ci95 | [-0.005208333333333333, 0.052083333333333336] |
| paired_diagnostics_vs_story.semantics.units | 96 |
| paired_diagnostics_vs_story.semantics.examples | 192 |
| paired_diagnostics_vs_story.semantics.unit | "family/prompt" |
| paired_diagnostics_vs_story.semantics.seed | 42 |
| paired_diagnostics_vs_story.semantics.repetitions | 2000 |
| paired_diagnostics_vs_story.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics_vs_story.jblimp.point | -0.012084592145015106 |
| paired_diagnostics_vs_story.jblimp.ci95 | [-0.03625377643504532, 0.015105740181268883] |
| paired_diagnostics_vs_story.jblimp.units | 331 |
| paired_diagnostics_vs_story.jblimp.examples | 331 |
| paired_diagnostics_vs_story.jblimp.unit | "family/prompt" |
| paired_diagnostics_vs_story.jblimp.seed | 42 |
| paired_diagnostics_vs_story.jblimp.repetitions | 2000 |
| paired_diagnostics_vs_story.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics_vs_story.jcqa.point | 0.003127792672028597 |
| paired_diagnostics_vs_story.jcqa.ci95 | [-0.009830205540661306, 0.016543789097408338] |
| paired_diagnostics_vs_story.jcqa.units | 1119 |
| paired_diagnostics_vs_story.jcqa.examples | 1119 |
| paired_diagnostics_vs_story.jcqa.unit | "family/prompt" |
| paired_diagnostics_vs_story.jcqa.seed | 42 |
| paired_diagnostics_vs_story.jcqa.repetitions | 2000 |
| paired_diagnostics_vs_story.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| eligible_for_full | false |
| checked_at | "2026-10-05T05:37:20.922286Z" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/complete_text_10b_choice_comparison.json — complete</summary>

[原記録](../../reports/phase6/complete_text_10b_choice_comparison.json) ／ SHA256: `dc71ec81f16b373eda8f1c7c6466d06b974c872844d4178ea3586f5389f60d27` ／ 5,391 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| source_sha256.reports/phase6/complete-text-10b-100m-20261004/coherent20/evaluation/semantics.json | "8d6920fa9aacf201a96b61ee202caa04431ea9a07fc63d206235f7ff047c96eb" |
| source_sha256.reports/phase6/complete-text-10b-100m-20261004/coherent20/evaluation/jblimp.json | "d2b522ebf83463fde742da55a632c52d375f20f8f2faf420844b4f9b3388c068" |
| source_sha256.reports/phase6/complete-text-10b-100m-20261004/coherent20/evaluation/jcqa.json | "656ce5b8aee57e83c1350a4ba73305ade23a8a3c7b20e514234a26731312486a" |
| paired_differences_from_web.semantics.short20.point | 0.005208333333333333 |
| paired_differences_from_web.semantics.short20.ci95 | [-0.026041666666666668, 0.036458333333333336] |
| paired_differences_from_web.semantics.short20.units | 96 |
| paired_differences_from_web.semantics.short20.examples | 192 |
| paired_differences_from_web.semantics.short20.unit | "family/prompt" |
| paired_differences_from_web.semantics.short20.seed | 42 |
| paired_differences_from_web.semantics.short20.repetitions | 2000 |
| paired_differences_from_web.semantics.short20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.semantics.short20.both_contexts_difference.point | 0.020833333333333332 |
| paired_differences_from_web.semantics.short20.both_contexts_difference.ci95 | [-0.03125, 0.07291666666666667] |
| paired_differences_from_web.semantics.short20.both_contexts_difference.units | 96 |
| paired_differences_from_web.semantics.short20.both_contexts_difference.examples | 96 |
| paired_differences_from_web.semantics.short20.both_contexts_difference.unit | "family/prompt" |
| paired_differences_from_web.semantics.short20.both_contexts_difference.seed | 42 |
| paired_differences_from_web.semantics.short20.both_contexts_difference.repetitions | 2000 |
| paired_differences_from_web.semantics.short20.both_contexts_difference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.semantics.coherent20.point | 0.015625 |
| paired_differences_from_web.semantics.coherent20.ci95 | [-0.010416666666666666, 0.041666666666666664] |
| paired_differences_from_web.semantics.coherent20.units | 96 |
| paired_differences_from_web.semantics.coherent20.examples | 192 |
| paired_differences_from_web.semantics.coherent20.unit | "family/prompt" |
| paired_differences_from_web.semantics.coherent20.seed | 42 |
| paired_differences_from_web.semantics.coherent20.repetitions | 2000 |
| paired_differences_from_web.semantics.coherent20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.point | 0.03125 |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.ci95 | [-0.020833333333333332, 0.08333333333333333] |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.units | 96 |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.examples | 96 |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.unit | "family/prompt" |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.seed | 42 |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.repetitions | 2000 |
| paired_differences_from_web.semantics.coherent20.both_contexts_difference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.jblimp.short20.point | 0.021148036253776436 |
| paired_differences_from_web.jblimp.short20.ci95 | [-0.006117824773413893, 0.04841389728096636] |
| paired_differences_from_web.jblimp.short20.units | 331 |
| paired_differences_from_web.jblimp.short20.examples | 331 |
| paired_differences_from_web.jblimp.short20.unit | "family/prompt" |
| paired_differences_from_web.jblimp.short20.seed | 42 |
| paired_differences_from_web.jblimp.short20.repetitions | 2000 |
| paired_differences_from_web.jblimp.short20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.jblimp.coherent20.point | 0.015105740181268883 |
| paired_differences_from_web.jblimp.coherent20.ci95 | [-0.01812688821752266, 0.045317220543806644] |
| paired_differences_from_web.jblimp.coherent20.units | 331 |
| paired_differences_from_web.jblimp.coherent20.examples | 331 |
| paired_differences_from_web.jblimp.coherent20.unit | "family/prompt" |
| paired_differences_from_web.jblimp.coherent20.seed | 42 |
| paired_differences_from_web.jblimp.coherent20.repetitions | 2000 |
| paired_differences_from_web.jblimp.coherent20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.jcqa.short20.point | -0.028150134048257374 |
| paired_differences_from_web.jcqa.short20.ci95 | [-0.04245978552278821, -0.01385165326184093] |
| paired_differences_from_web.jcqa.short20.units | 1119 |
| paired_differences_from_web.jcqa.short20.examples | 1119 |
| paired_differences_from_web.jcqa.short20.unit | "family/prompt" |
| paired_differences_from_web.jcqa.short20.seed | 42 |
| paired_differences_from_web.jcqa.short20.repetitions | 2000 |
| paired_differences_from_web.jcqa.short20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_differences_from_web.jcqa.coherent20.point | 0.01966041108132261 |
| paired_differences_from_web.jcqa.coherent20.ci95 | [-0.0008936550491510277, 0.041108132260947276] |
| paired_differences_from_web.jcqa.coherent20.units | 1119 |
| paired_differences_from_web.jcqa.coherent20.examples | 1119 |
| paired_differences_from_web.jcqa.coherent20.unit | "family/prompt" |
| paired_differences_from_web.jcqa.coherent20.seed | 42 |
| paired_differences_from_web.jcqa.coherent20.repetitions | 2000 |
| paired_differences_from_web.jcqa.coherent20.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| additional_training_tokens | 0 |
| limits | "Secondary diagnostic; one training seed. Cluster paired bootstrap by existing frozen family, not evidence of practical Base quality." |

</details>

<details>
<summary>reports/phase6/complete_text_10b_comparison_completion.json — completed_stages1_to3</summary>

[原記録](../../reports/phase6/complete_text_10b_comparison_completion.json) ／ SHA256: `456efef5b53f36da46f625384252e11fd2d95b6d730d79fb0ad80644357244da` ／ 13,048 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_stages1_to3" |
| checked_at | "2026-10-04T15:30:56.021643Z" |
| scope | "Bounded inspection, candidate pool, matched three-arm training, diagnostics, prespecified conditional full/long evaluation, report/local commit, parent UI restoration and stop" |
| stage2_pool_tokens | 25000067 |
| scientific_tokens | 300023808 |
| verification_tokens | 262144 |
| primary_checks | 35 |
| conditional_checks | 43 |
| GPU_seconds.primary | 774.6238302259999 |
| GPU_seconds.conditional_including_retired | 1956.8038584469978 |
| GPU_seconds.retired | 831.3550438079983 |
| GPU_seconds.total | 2731.4276886729976 |
| GPU_seconds.original_total_budget | 4800 |
| ui.status | "running" |
| ui.verified_HTTP_model.training_tokens | 10000007168 |
| ui.verified_HTTP_model.update | 305176 |
| ui.verified_HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui.verified_HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui.verified_HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| adoption.candidate_passes_all_full_conditions | false |
| adoption.reason | "parent full BPB regression exceeds +0.001" |
| adoption.parent_BPB | 0.9540184727984398 |
| adoption.candidate_BPB | 0.955764691289243 |
| adoption.difference | 0.001746218490803253 |
| adoption.quality_targets_achieved | false |
| adoption.independent_human_blind | "not performed" |
| protected_test_used | false |
| additional_conditional_training_tokens | 0 |
| limitations | ["Codex content diagnosis is not independent human blind", "source/style/length/EOS density confounded", "existing Web and broad benchmark overlap unknown", "independent full12.23B audit remains incomplete", "long EOS is not semantic ending certification", "100M screen does not reject training insufficiency"] |
| frozen_current_sources.scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| frozen_current_sources.scripts/run_eos_short_pilot.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/inspect_complete_text_data.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/readiness.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/prepare_story_text.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/evaluate_japanese_base.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/shards.py.hash_scope | "CRLF normalized per implementation_hashes" |
| frozen_current_sources.scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| frozen_current_sources.scripts/prepare_coherent_text.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/evaluate_complete_text_full.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| frozen_current_sources.src/jmicro/tokenizer.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/compare_base_10b.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/evaluation_memory.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/model.py.hash_scope | "CRLF normalized per implementation_hashes" |
| frozen_current_sources.src/jmicro/low_lr_pilot.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/compare_base_5b.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/japanese_evaluation.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| frozen_current_sources.scripts/run_eos_complete_100m.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/evaluate_complete_text_full.ps1.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/run_complete_text_comparison.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.scripts/run_complete_text_comparison.ps1.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| frozen_current_sources.src/jmicro/eos_pilot.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.uv.lock.hash_scope | "CRLF normalized per implementation_hashes" |
| frozen_current_sources.src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| frozen_current_sources.src/jmicro/coherent_units.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |
| frozen_current_sources.src/jmicro/training.py.hash_scope | "CRLF normalized per implementation_hashes" |
| frozen_current_sources.scripts/run_eos_5b_finish.py.sha256 | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| frozen_current_sources.scripts/run_eos_5b_finish.py.hash_scope | "Linux raw bytes; Windows raw or LF execution copy" |

</details>

<details>
<summary>reports/phase6/complete_text_10b_comparison_launch.json — None</summary>

[原記録](../../reports/phase6/complete_text_10b_comparison_launch.json) ／ SHA256: `1f69277d8eee54b13ec62f30fe47d3ce41cabdfc74806a68f1f8f6f2dbb43bce` ／ 448 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/complete_text_10b_comparison_review.json — passed</summary>

[原記録](../../reports/phase6/complete_text_10b_comparison_review.json) ／ SHA256: `b3e3abfbfecb9d10f67071c58eec6771dd066108d5152ba0e504b9c2fd0aa34a` ／ 3,398 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-04T14:41:08.314097Z" |
| checks.relevant_CPU_tests_pass | true |
| checks.data_pool_25M_to_50M | true |
| checks.data_inspection_100_each | true |
| checks.EOS_BOS_packing_checks | true |
| checks.actual_CUDA_exact_resume | true |
| checks.GPU_within_frozen_budget | true |
| checks.scientific_total_tokens | true |
| checks.verification_tokens_separate | true |
| checks.original_suite_and_protected_test | true |
| checks.all240_content_reviewed | true |
| checks.web_checkpoint_and_binding | true |
| checks.web_finite_model_optimizer | true |
| checks.web_matched_budget | true |
| checks.web_finite_loss_gradient | true |
| checks.web_source_accounting_no_short_epoch | true |
| checks.web_saved_resume_state | true |
| checks.web_evaluation_binding | true |
| checks.web_complete_diagnostics | true |
| checks.short20_checkpoint_and_binding | true |
| checks.short20_finite_model_optimizer | true |
| checks.short20_matched_budget | true |
| checks.short20_finite_loss_gradient | true |
| checks.short20_source_accounting_no_short_epoch | true |
| checks.short20_saved_resume_state | true |
| checks.short20_evaluation_binding | true |
| checks.short20_complete_diagnostics | true |
| checks.coherent20_checkpoint_and_binding | true |
| checks.coherent20_finite_model_optimizer | true |
| checks.coherent20_matched_budget | true |
| checks.coherent20_finite_loss_gradient | true |
| checks.coherent20_source_accounting_no_short_epoch | true |
| checks.coherent20_saved_resume_state | true |
| checks.coherent20_evaluation_binding | true |
| checks.coherent20_complete_diagnostics | true |
| checks.GPU_job_terminal_and_actual_process_exited | true |
| summaries.web.grammar_score2 | 25 |
| summaries.web.relevance_score2 | 26 |
| summaries.web.coherence_score2 | 0 |
| summaries.web.appropriate_EOS | 0 |
| summaries.short20.grammar_score2 | 32 |
| summaries.short20.relevance_score2 | 29 |
| summaries.short20.coherence_score2 | 1 |
| summaries.short20.appropriate_EOS | 1 |
| summaries.coherent20.count | 80 |
| summaries.coherent20.grammar_score2 | 59 |
| summaries.coherent20.relevance_score2 | 23 |
| summaries.coherent20.coherence_score2 | 10 |
| summaries.coherent20.appropriate_EOS | 9 |
| summaries.coherent20.character4_repeat_mean | 0.377017677101203 |
| candidate_checks.short20.original_mixture_checks.EOS_at_least8_more | false |
| candidate_checks.short20.original_mixture_checks.repetition_no_worse | true |
| candidate_checks.short20.original_mixture_checks.no_empty_role_unicode | true |
| candidate_checks.short20.original_mixture_checks.BPB_degradation_at_most1percent | true |
| candidate_checks.short20.original_mixture_checks.no_punctuation_only_stops | true |
| candidate_checks.short20.coherence_gain_at_least8 | false |
| candidate_checks.short20.paired_coherence_CI_lower_above0 | false |
| candidate_checks.short20.coherence_difference_count | 1 |
| candidate_checks.short20.paired_CI95 | [0.0, 0.0375] |
| candidate_checks.short20.eligible_for_conditional_full | false |
| candidate_checks.coherent20.original_mixture_checks.EOS_at_least8_more | true |
| candidate_checks.coherent20.original_mixture_checks.repetition_no_worse | true |
| candidate_checks.coherent20.original_mixture_checks.no_empty_role_unicode | true |
| candidate_checks.coherent20.original_mixture_checks.BPB_degradation_at_most1percent | true |
| candidate_checks.coherent20.original_mixture_checks.no_punctuation_only_stops | true |
| candidate_checks.coherent20.coherence_gain_at_least8 | true |
| candidate_checks.coherent20.paired_coherence_CI_lower_above0 | true |
| candidate_checks.coherent20.coherence_difference_count | 10 |
| candidate_checks.coherent20.paired_CI95 | [0.0625, 0.2] |
| candidate_checks.coherent20.eligible_for_conditional_full | true |
| protected_test_used | false |
| completion_scope | "stages1–3 only; experiment completion is separate from model adoption" |

</details>

<details>
<summary>reports/phase6/complete_text_10b_content_review.json — None</summary>

[原記録](../../reports/phase6/complete_text_10b_content_review.json) ／ SHA256: `33d1dcdd2ac228777c7fe87e8dbca9cddad3659d22e06e8ee0ffb61194e73761` ／ 539,745 bytes

| 原キー | 保存値 |
|---|---|
| rubric.grammar | "0: broken syntax; 1: partial/awkward; 2: locally natural Japanese. Cap-ending byte fragment alone is not grammar0." |
| rubric.relevance | "0: loses subject/condition/topic; 1: partial fit; 2: preserves supplied prefix and conditions." |
| rubric.coherence | "0: strong loops/contradiction/incoherent development; 1: partly sensible but redundant or weak; 2: coherent meaningful development." |
| rubric.completion | "0: not an appropriate learned content ending; 1: natural EOS with meaningful topic-relevant completion. Cap ending is0." |
| summary.web.grammar_score2 | 25 |
| summary.web.relevance_score2 | 26 |
| summary.web.coherence_score2 | 0 |
| summary.web.appropriate_EOS | 0 |
| summary.short20.grammar_score2 | 32 |
| summary.short20.relevance_score2 | 29 |
| summary.short20.coherence_score2 | 1 |
| summary.short20.appropriate_EOS | 1 |
| summary.coherent20.count | 80 |
| summary.coherent20.grammar_score2 | 59 |
| summary.coherent20.relevance_score2 | 23 |
| summary.coherent20.coherence_score2 | 10 |
| summary.coherent20.appropriate_EOS | 9 |
| summary.coherent20.character4_repeat_mean | 0.377017677101203 |
| checks.short20.original_mixture_checks.EOS_at_least8_more | false |
| checks.short20.original_mixture_checks.repetition_no_worse | true |
| checks.short20.original_mixture_checks.no_empty_role_unicode | true |
| checks.short20.original_mixture_checks.BPB_degradation_at_most1percent | true |
| checks.short20.original_mixture_checks.no_punctuation_only_stops | true |
| checks.short20.coherence_gain_at_least8 | false |
| checks.short20.paired_coherence_CI_lower_above0 | false |
| checks.short20.coherence_difference_count | 1 |
| checks.short20.paired_CI95 | [0.0, 0.0375] |
| checks.short20.eligible_for_conditional_full | false |
| checks.coherent20.original_mixture_checks.EOS_at_least8_more | true |
| checks.coherent20.original_mixture_checks.repetition_no_worse | true |
| checks.coherent20.original_mixture_checks.no_empty_role_unicode | true |
| checks.coherent20.original_mixture_checks.BPB_degradation_at_most1percent | true |
| checks.coherent20.original_mixture_checks.no_punctuation_only_stops | true |
| checks.coherent20.coherence_gain_at_least8 | true |
| checks.coherent20.paired_coherence_CI_lower_above0 | true |
| checks.coherent20.coherence_difference_count | 10 |
| checks.coherent20.paired_CI95 | [0.0625, 0.2] |
| checks.coherent20.eligible_for_conditional_full | true |

</details>

<details>
<summary>reports/phase6/complete_text_10b_full_launch.json — None</summary>

[原記録](../../reports/phase6/complete_text_10b_full_launch.json) ／ SHA256: `1407bf98e4faf4c1dcb9836348e01821029a808be803392047f2853542dd166a` ／ 449 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/complete_text_10b_full_r1_launch.json — None</summary>

[原記録](../../reports/phase6/complete_text_10b_full_r1_launch.json) ／ SHA256: `bea6e7b18d5b2978cc562bd8042db79ccc415b989aabe503502c624a27c2acb3` ／ 538 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/complete_text_10b_full_result.json — complete</summary>

[原記録](../../reports/phase6/complete_text_10b_full_result.json) ／ SHA256: `32349586eefc8536ae6212223204bc5b5cf8de76ac476aee752e58a5916eb26d` ／ 7,552 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| summary.web.training_input_tokens | 10100015104 |
| summary.web.full_dev_BPB | 0.9489573248509644 |
| summary.web.fixed80.eos | 0 |
| summary.web.fixed80.repetition | 60 |
| summary.web.fixed80.unicode_failure | 0 |
| summary.web.fixed80.role_leak | 0 |
| summary.web.fixed80.empty | 0 |
| summary.web.all400.eos | 6 |
| summary.web.all400.repetition | 124 |
| summary.web.all400.unicode_failure | 0 |
| summary.web.all400.role_leak | 0 |
| summary.web.all400.empty | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.repetition | 60 |
| summary.web.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.repetition | 60 |
| summary.web.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed42.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed42.repetition | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed44.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| summary.coherent20.label | "coherent20" |
| summary.coherent20.training_input_tokens | 10100015104 |
| summary.coherent20.full_dev_BPB | 0.955764691289243 |
| summary.coherent20.fixed80.outputs | 80 |
| summary.coherent20.fixed80.eos | 24 |
| summary.coherent20.fixed80.repetition | 24 |
| summary.coherent20.fixed80.unicode_failure | 0 |
| summary.coherent20.fixed80.role_leak | 0 |
| summary.coherent20.fixed80.empty | 0 |
| summary.coherent20.all400.outputs | 400 |
| summary.coherent20.all400.eos | 137 |
| summary.coherent20.all400.repetition | 53 |
| summary.coherent20.all400.unicode_failure | 0 |
| summary.coherent20.all400.role_leak | 0 |
| summary.coherent20.all400.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.eos | 24 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.repetition | 24 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.eos | 24 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.repetition | 24 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.eos | 27 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.repetition | 1 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.eos | 31 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.eos | 31 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.repetition | 2 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| parent.training_input_tokens | 10000007168 |
| parent.full_dev_BPB | 0.9540184727984398 |
| parent.fixed80.eos | 0 |
| parent.fixed80.repetition | 53 |
| parent.fixed80.unicode_failure | 0 |
| parent.fixed80.role_leak | 0 |
| parent.fixed80.empty | 0 |
| parent.all400.eos | 9 |
| parent.all400.repetition | 112 |
| parent.all400.unicode_failure | 0 |
| parent.all400.role_leak | 0 |
| parent.all400.empty | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed42.eos | 4 |
| parent.generation_groups.sampling-suppressed1-seed42.repetition | 3 |
| parent.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed44.eos | 3 |
| parent.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| parent.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| long_generation.web.conditions.128.natural_eos | 0 |
| long_generation.web.conditions.128.raw_utf8_failure | 0 |
| long_generation.web.conditions.512.natural_eos | 0 |
| long_generation.web.conditions.512.raw_utf8_failure | 0 |
| long_generation.coherent20.complete | true |
| long_generation.coherent20.conditions.128.count | 20 |
| long_generation.coherent20.conditions.128.expected | 20 |
| long_generation.coherent20.conditions.128.natural_eos | 10 |
| long_generation.coherent20.conditions.128.mean_char4_repeat | 0.46478906651733964 |
| long_generation.coherent20.conditions.128.same_sentence_repeat | 8 |
| long_generation.coherent20.conditions.128.raw_utf8_failure | 0 |
| long_generation.coherent20.conditions.512.count | 20 |
| long_generation.coherent20.conditions.512.expected | 20 |
| long_generation.coherent20.conditions.512.natural_eos | 10 |
| long_generation.coherent20.conditions.512.mean_char4_repeat | 0.5512562266891472 |
| long_generation.coherent20.conditions.512.same_sentence_repeat | 9 |
| long_generation.coherent20.conditions.512.raw_utf8_failure | 0 |
| checks.original_full_mixture.EOS_at_least8_more | true |
| checks.original_full_mixture.repetition_no_worse | true |
| checks.original_full_mixture.no_empty_role_unicode | true |
| checks.original_full_mixture.BPB_degradation_at_most1percent | true |
| checks.original_full_mixture.no_punctuation_only_stops | true |
| checks.parent_growth.full_BPB_no_major_regression | false |
| checks.parent_growth.fixed_repetition_not8_worse | true |
| checks.parent_growth.raw_unicode_empty_role_zero_all400 | true |
| checks.all400_candidate_raw_failures_zero | true |
| candidate_passes_all_full_conditions | false |
| additional_training_tokens | 0 |
| protected_test_used | false |
| GPU_seconds | 1956.8038584469978 |

</details>
