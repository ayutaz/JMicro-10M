# 実行管理・後続準備・その他 — 17/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_launch.json — actual_gold_body_replay_CUDA_verified_science_launched</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_launch.json) ／ SHA256: `d2361cbc7dcbe4caede71978ffca07e81fefe3f3ba24460716915a875d4977fc` ／ 4,080 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_gold_body_replay_CUDA_verified_science_launched" |
| full_resume_checks.model | true |
| full_resume_checks.optimizer | true |
| full_resume_checks.scheduler | true |
| full_resume_checks.rng | true |
| full_resume_checks.sampler | true |
| full_resume_checks.lineage | true |
| full_resume_checks.tokens | true |
| full_resume_checks.supervised_tokens | true |
| full_resume_checks.body_bytes | true |
| full_resume_checks.token_digest | true |
| full_resume_checks.focus_token_digest | true |
| full_resume_checks.focus_teacher_tokens | true |
| full_resume_checks.weighted_teacher_mass | true |
| full_resume_checks.update | true |
| full_resume_checks.spec | true |
| full_resume_checks.model_config | true |
| full_resume_checks.pilot_binding | true |
| full_resume_checks.study_binding | true |
| full_resume_checks.hard_replay_state | true |
| full_resume_checks.history_loss | true |
| full_resume_checks.history_gradient_norm | true |
| full_resume_checks.history_lr | true |
| full_resume_checks.history_token_digest | true |
| full_resume_checks.history_source_teachers | true |
| full_resume_checks.history_source_eos | true |
| full_resume_checks.history_source_input_tokens | true |
| full_resume_checks.history_source_body_bytes | true |
| full_resume_checks.history_source_focus_teachers | true |
| full_resume_checks.history_focus_token_digest | true |
| full_resume_checks.history_focus_teacher_tokens | true |
| full_resume_checks.history_weighted_teacher_mass | true |
| full_resume_checks.history_ordinary_CE_loss | true |
| full_resume_checks.history_reference_body_CE_loss | true |
| full_resume_checks.history_combined_hard_teacher_positions | true |
| full_resume_checks.history_reference_non_EOS_teacher_probability_mass | true |
| full_resume_checks.history_reference_input_tokens | true |
| full_resume_checks.history_reference_hard_body_target_positions | true |
| full_resume_checks.history_reference_ignored_positions | true |
| full_resume_checks.history_reference_digest | true |
| full_resume_checks.history_combined_student_physical_input_tokens | true |
| full_resume_checks.finite | true |
| full_resume_checks.no_reheat | true |
| initial_parent_preservation.parent_sampler_lineage | true |
| initial_parent_preservation.frozen_teacher_weights | true |
| initial_parent_preservation.frozen_teacher_eval_no_grad | true |
| actual_verification_optimizer_updates | 40 |
| actual_verification_main_CE_teacher_tokens | 1307967 |
| actual_verification_auxiliary_hard_body_teacher_tokens | 326339 |
| actual_verification_reference_input_tokens | 327680 |
| actual_verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| actual_verification_GPU_seconds | 28.81082727899775 |
| steady_step_seconds | 0.08874443148670252 |
| estimated_science_GPU_seconds_with_margin | 605.5142286956601 |
| estimated_current_study_all_GPU_seconds | 634.3250559746579 |
| current_study_GPU_ceiling_seconds | 900 |
| previous_related_study_GPU_seconds | 795.3523048920615 |
| scientific_main_CE_teacher_budget | 100000000 |
| expected_auxiliary_hard_body_teacher_positions | 25026383 |
| expected_combined_hard_teacher_positions | 125026383 |
| reference_input_budget | 25133056 |
| newly_prepared_source_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_portable.json — native_portable_text_complete</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_portable.json) ／ SHA256: `1b678af360430679013430de010681e2980ab093a9ff802672f9a46acc915cc4` ／ 82,930 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_portable_text_complete" |
| files.configs/phase6/hard_body_web_replay_comparison.json.bytes | 26839 |
| files.configs/phase6/hard_body_web_replay_probe.json.bytes | 25812 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/compare-result.json.bytes | 1908868 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/content-packets/hard_body_web_replay.json.bytes | 102132 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/body.json.bytes | 68747 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/generation.json.bytes | 84701 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/jblimp.json.bytes | 339911 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/jcqa.json.bytes | 1642343 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/result.json.bytes | 180070 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/evaluation/hard_body_web_replay/evaluation/semantics.json.bytes | 204508 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/latest.json.bytes | 300 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/latest.json.sha256 | "484942a10767b9fcef469fc9ad57fd858a52bce10ea75ab1b221c0fe0b94acee" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/metrics.jsonl.bytes | 5043698 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/job.json.bytes | 928 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/initial-parent-preservation.json.bytes | 266 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/job.json.bytes | 601 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/result.json.bytes | 89183 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/latest.json.bytes | 276 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/latest.json.sha256 | "bd797c551259384abf4bed565052b954d4fbb83aed7c95d89732bd8d74237905" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/resume-gate/result.json.bytes | 18738 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/configs/phase6/hard_body_web_replay_probe.json.bytes | 25812 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_resident_web_kl_trainer.py.bytes | 1765 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_resident_web_kl_trainer.py.sha256 | "a95b7941382ae6ecddcafcb2b7a5da014afd2158fc8480603a15d77390ca401e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_accounting.py.bytes | 5141 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_accounting.py.sha256 | "911ac462557e17504af767b60e36edc9160e8e0dd4b140155b887a04a5963a16" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_condition_trainer.py.bytes | 10355 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_condition_trainer.py.sha256 | "40602f92d9abe710442aabb24d60af232956020fe2cccec7917b676ce8621320" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_preservation.py.bytes | 2558 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/eos_decoupled_web_kl_preservation.py.sha256 | "5abe753fcdd5273ee9033b9e3dc8e207124f294d85e6f1dbb0bd8207252571e1" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/hard_body_resident_web_replay_trainer.py.bytes | 1780 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/hard_body_web_replay.py.bytes | 2875 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/hard_body_web_replay_accounting.py.bytes | 5857 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/hard_body_web_replay_trainer.py.bytes | 11169 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/implement_eos_decoupled_web_kl_comparison.py.bytes | 15466 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/implement_eos_decoupled_web_kl_comparison.py.sha256 | "882ec63522835b73aa0784d86d5a6c48da2d3517b63f86f918b7b43a32c08b6e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/implement_hard_body_web_replay_comparison.py.bytes | 16680 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_eos_decoupled_web_kl.py.bytes | 3914 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_eos_decoupled_web_kl.py.sha256 | "e8b5675ce97780dbc39107303742ec9f47dd1b1a9449ea263768baa6ba289f61" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_eos_decoupled_web_kl_content_review.py.bytes | 8828 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_eos_decoupled_web_kl_content_review.py.sha256 | "6a238e79c1c6dc46acb4a3a0015968c0545a3a964b0b8273fb2dafccb1552fe2" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_hard_body_web_replay.py.bytes | 5187 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_hard_body_web_replay_content_review.py.bytes | 8865 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_web_kl_content_review.py.bytes | 8204 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/prepare_web_kl_content_review_v2.py.bytes | 8207 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/propose_eos_decoupled_web_kl_comparison.py.bytes | 7780 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/propose_eos_decoupled_web_kl_comparison.py.sha256 | "d08f915c4bbd93083918c314721480eeaba913cf7a3a58de2d4eaef1ddd2436d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/record_hard_body_web_replay_preparation.py.bytes | 3620 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/resident_web_kl_trainer.py.bytes | 1754 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/resident_web_window.py.bytes | 5562 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_eos_decoupled_web_kl_comparison.py.bytes | 18079 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_eos_decoupled_web_kl_comparison.py.sha256 | "c9d4e717b905e1a4f0e912f086bc2fb5c1374ffae921368186309e329f4ca38f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_hard_body_web_replay_comparison.py.bytes | 18383 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_web_kl_comparison.py.bytes | 15960 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/review_web_kl_comparison_v2.py.bytes | 15966 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_decoupled_web_kl_comparison.ps1.bytes | 3104 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_decoupled_web_kl_comparison.ps1.sha256 | "66bd71ef4bb603e910f1d96a40817cb9ba2a4d2b61b7b2f5be1cefe3219ab166" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_decoupled_web_kl_comparison.py.bytes | 38637 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_decoupled_web_kl_comparison.py.sha256 | "da47dfd8a67520ca40e7de37f2cacc5f3202b810786c844fd06b267994d6cdaf" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_hard_body_web_replay_comparison.ps1.bytes | 3132 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_hard_body_web_replay_comparison.py.bytes | 38204 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_web_kl_comparison.ps1.bytes | 3046 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_web_kl_comparison.py.bytes | 32383 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_web_kl_comparison_v2.ps1.bytes | 3064 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/run_web_kl_comparison_v2.py.bytes | 33340 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/web_kl_comparison_accounting.py.bytes | 4297 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/web_kl_condition_trainer.py.bytes | 9451 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/web_kl_condition_trainer_v2.py.bytes | 9640 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/scripts/web_kl_preservation.py.bytes | 4170 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_comparison.py.bytes | 4233 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_comparison.py.sha256 | "d295f1a172a97eaeaf6f3bc39733a7644d82d21a33e573ec49c05617813739a7" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_condition_trainer.py.bytes | 2776 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_condition_trainer.py.sha256 | "6f1f615742767b64570b8ace6ee482818bcc84e870aa31beef45cb716e72060f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_preservation.py.bytes | 1660 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_eos_decoupled_web_kl_preservation.py.sha256 | "4573df5a12572f84c22560ad0d3f3dd42b41a03af9cff4b8e271481c1da2023e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay.py.bytes | 3147 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay.py.sha256 | "e1bb33d0903ef6e4d3e1f246e147d326612c251c59ea0c925debefddcccf060d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay_comparison.py.bytes | 5023 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay_comparison.py.sha256 | "47dfa164b6f56d447b17f77805a34a87e97e8476614061838a6a8289adea8fc3" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay_trainer.py.bytes | 4535 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_hard_body_web_replay_trainer.py.sha256 | "f0cee4d5a56d9872f1455d8fcb7d9d31311b450fb9b46ca66bfd61c05c6721ed" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_resident_web_window.py.bytes | 1652 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_resident_web_window.py.sha256 | "3c2a119bc34fdcf74fdd90df11db2a6acdc25158114a04f350e7e24280bc0102" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_comparison.py.bytes | 3782 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_comparison.py.sha256 | "4591532fab436e589bba7b0ebc43e8d26795d017d6fc1817d3dd912db3d85e5d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_comparison_v2.py.bytes | 3800 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_comparison_v2.py.sha256 | "5464b5d09458aaef9daa30a91de97c8f66feb6c672501b90e401c9d0ac7d0751" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_condition_trainer.py.bytes | 2563 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_condition_trainer.py.sha256 | "079582542dfcb2362fc1ff2e20147167f56c751dc761f0e1854239e65160656f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_condition_trainer_v2.py.bytes | 2566 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_condition_trainer_v2.py.sha256 | "9c0e140b573ca2d8869507992b5957bf476951a1dfc60ffeca7b45468295d1c8" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_preservation.py.bytes | 2223 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/source/tests/test_web_kl_preservation.py.sha256 | "b39e6455488abb0b57cd7244a8e331d8aca1c731475c72e43be02dc99704c426" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/timing/latest.json.bytes | 274 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/timing/latest.json.sha256 | "aaa70b8bee99faa690079845898e32858fbd6721f1b565f95574046d7960b231" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/probe/timing/metrics.jsonl.bytes | 51325 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/progress-result.json.bytes | 1907972 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/review.json.bytes | 14525 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/configs/phase6/hard_body_web_replay_comparison.json.bytes | 26839 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_resident_web_kl_trainer.py.bytes | 1765 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_resident_web_kl_trainer.py.sha256 | "a95b7941382ae6ecddcafcb2b7a5da014afd2158fc8480603a15d77390ca401e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_accounting.py.bytes | 5141 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_accounting.py.sha256 | "911ac462557e17504af767b60e36edc9160e8e0dd4b140155b887a04a5963a16" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_condition_trainer.py.bytes | 10355 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_condition_trainer.py.sha256 | "40602f92d9abe710442aabb24d60af232956020fe2cccec7917b676ce8621320" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_preservation.py.bytes | 2558 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/eos_decoupled_web_kl_preservation.py.sha256 | "5abe753fcdd5273ee9033b9e3dc8e207124f294d85e6f1dbb0bd8207252571e1" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/hard_body_resident_web_replay_trainer.py.bytes | 1780 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/hard_body_web_replay.py.bytes | 2875 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/hard_body_web_replay_accounting.py.bytes | 5857 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/hard_body_web_replay_trainer.py.bytes | 11169 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/implement_eos_decoupled_web_kl_comparison.py.bytes | 15466 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/implement_eos_decoupled_web_kl_comparison.py.sha256 | "882ec63522835b73aa0784d86d5a6c48da2d3517b63f86f918b7b43a32c08b6e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/implement_hard_body_web_replay_comparison.py.bytes | 16680 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_eos_decoupled_web_kl.py.bytes | 3914 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_eos_decoupled_web_kl.py.sha256 | "e8b5675ce97780dbc39107303742ec9f47dd1b1a9449ea263768baa6ba289f61" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_eos_decoupled_web_kl_content_review.py.bytes | 8828 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_eos_decoupled_web_kl_content_review.py.sha256 | "6a238e79c1c6dc46acb4a3a0015968c0545a3a964b0b8273fb2dafccb1552fe2" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_hard_body_web_replay.py.bytes | 5187 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_hard_body_web_replay_content_review.py.bytes | 8865 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_web_kl_content_review.py.bytes | 8204 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/prepare_web_kl_content_review_v2.py.bytes | 8207 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/propose_eos_decoupled_web_kl_comparison.py.bytes | 7780 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/propose_eos_decoupled_web_kl_comparison.py.sha256 | "d08f915c4bbd93083918c314721480eeaba913cf7a3a58de2d4eaef1ddd2436d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/record_hard_body_web_replay_preparation.py.bytes | 3620 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/resident_web_kl_trainer.py.bytes | 1754 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/resident_web_window.py.bytes | 5562 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_eos_decoupled_web_kl_comparison.py.bytes | 18079 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_eos_decoupled_web_kl_comparison.py.sha256 | "c9d4e717b905e1a4f0e912f086bc2fb5c1374ffae921368186309e329f4ca38f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_hard_body_web_replay_comparison.py.bytes | 18383 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_web_kl_comparison.py.bytes | 15960 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/review_web_kl_comparison_v2.py.bytes | 15966 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_decoupled_web_kl_comparison.ps1.bytes | 3104 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_decoupled_web_kl_comparison.ps1.sha256 | "66bd71ef4bb603e910f1d96a40817cb9ba2a4d2b61b7b2f5be1cefe3219ab166" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_decoupled_web_kl_comparison.py.bytes | 38637 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_decoupled_web_kl_comparison.py.sha256 | "da47dfd8a67520ca40e7de37f2cacc5f3202b810786c844fd06b267994d6cdaf" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_hard_body_web_replay_comparison.ps1.bytes | 3132 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_hard_body_web_replay_comparison.py.bytes | 38204 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_web_kl_comparison.ps1.bytes | 3046 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_web_kl_comparison.py.bytes | 32383 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_web_kl_comparison_v2.ps1.bytes | 3064 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/run_web_kl_comparison_v2.py.bytes | 33340 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/web_kl_comparison_accounting.py.bytes | 4297 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/web_kl_condition_trainer.py.bytes | 9451 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/web_kl_condition_trainer_v2.py.bytes | 9640 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/scripts/web_kl_preservation.py.bytes | 4170 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_comparison.py.bytes | 4233 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_comparison.py.sha256 | "d295f1a172a97eaeaf6f3bc39733a7644d82d21a33e573ec49c05617813739a7" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_condition_trainer.py.bytes | 2776 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_condition_trainer.py.sha256 | "6f1f615742767b64570b8ace6ee482818bcc84e870aa31beef45cb716e72060f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_preservation.py.bytes | 1660 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_eos_decoupled_web_kl_preservation.py.sha256 | "4573df5a12572f84c22560ad0d3f3dd42b41a03af9cff4b8e271481c1da2023e" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay.py.bytes | 3147 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay.py.sha256 | "e1bb33d0903ef6e4d3e1f246e147d326612c251c59ea0c925debefddcccf060d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay_comparison.py.bytes | 5023 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay_comparison.py.sha256 | "47dfa164b6f56d447b17f77805a34a87e97e8476614061838a6a8289adea8fc3" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay_trainer.py.bytes | 4535 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_hard_body_web_replay_trainer.py.sha256 | "f0cee4d5a56d9872f1455d8fcb7d9d31311b450fb9b46ca66bfd61c05c6721ed" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_resident_web_window.py.bytes | 1652 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_resident_web_window.py.sha256 | "3c2a119bc34fdcf74fdd90df11db2a6acdc25158114a04f350e7e24280bc0102" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_comparison.py.bytes | 3782 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_comparison.py.sha256 | "4591532fab436e589bba7b0ebc43e8d26795d017d6fc1817d3dd912db3d85e5d" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_comparison_v2.py.bytes | 3800 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_comparison_v2.py.sha256 | "5464b5d09458aaef9daa30a91de97c8f66feb6c672501b90e401c9d0ac7d0751" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_condition_trainer.py.bytes | 2563 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_condition_trainer.py.sha256 | "079582542dfcb2362fc1ff2e20147167f56c751dc761f0e1854239e65160656f" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_condition_trainer_v2.py.bytes | 2566 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_condition_trainer_v2.py.sha256 | "9c0e140b573ca2d8869507992b5957bf476951a1dfc60ffeca7b45468295d1c8" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_preservation.py.bytes | 2223 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/source/tests/test_web_kl_preservation.py.sha256 | "b39e6455488abb0b57cd7244a8e331d8aca1c731475c72e43be02dc99704c426" |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0000.json.bytes | 9916 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0016.json.bytes | 9572 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0032.json.bytes | 10199 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0048.json.bytes | 9489 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0064.json.bytes | 10293 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0080.json.bytes | 9682 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0096.json.bytes | 9759 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0112.json.bytes | 10123 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0128.json.bytes | 9786 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0144.json.bytes | 9852 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0160.json.bytes | 10121 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0176.json.bytes | 9959 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0192.json.bytes | 9885 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0208.json.bytes | 9596 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0224.json.bytes | 9798 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0240.json.bytes | 9588 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0256.json.bytes | 9589 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0272.json.bytes | 9572 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0288.json.bytes | 9583 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0304.json.bytes | 9761 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0320.json.bytes | 9303 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0336.json.bytes | 9391 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0352.json.bytes | 9764 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0368.json.bytes | 9511 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0384.json.bytes | 9843 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0400.json.bytes | 9481 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0416.json.bytes | 9866 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0432.json.bytes | 9319 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0448.json.bytes | 9566 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0464.json.bytes | 9406 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0480.json.bytes | 9410 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0496.json.bytes | 9482 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/result.json.bytes | 186608 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0000.json.bytes | 7963 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0016.json.bytes | 8311 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0032.json.bytes | 6971 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0048.json.bytes | 8132 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0064.json.bytes | 8494 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0080.json.bytes | 7065 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0096.json.bytes | 8061 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0112.json.bytes | 8234 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0128.json.bytes | 7041 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0144.json.bytes | 8172 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0160.json.bytes | 8592 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0176.json.bytes | 6907 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0192.json.bytes | 8151 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0208.json.bytes | 8492 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0224.json.bytes | 7068 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0240.json.bytes | 8306 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0256.json.bytes | 8237 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0272.json.bytes | 8424 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0288.json.bytes | 7097 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0304.json.bytes | 8137 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0320.json.bytes | 8586 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0336.json.bytes | 7094 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0352.json.bytes | 8150 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0368.json.bytes | 8161 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0384.json.bytes | 7003 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0400.json.bytes | 8140 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0416.json.bytes | 8182 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0432.json.bytes | 7094 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0448.json.bytes | 8071 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0464.json.bytes | 8346 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0480.json.bytes | 7010 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0496.json.bytes | 8052 |
| files.reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/result.json.bytes | 183237 |
| files.reports/phase6/hard_body_web_replay_comparison_completion.json.bytes | 8499 |
| files.reports/phase6/hard_body_web_replay_comparison_completion.json.sha256 | "b6d93193c07f1f1c82df3efd50a7997ff1190aeed3efeb8b992b1af39d266338" |
| files.reports/phase6/hard_body_web_replay_comparison_launch.json.bytes | 4080 |
| files.reports/phase6/hard_body_web_replay_comparison_proposal.json.bytes | 9672 |
| files.reports/phase6/hard_body_web_replay_comparison_review.json.bytes | 14525 |
| files.reports/phase6/hard_body_web_replay_comparison_tests.xml.bytes | 573 |
| files.reports/phase6/hard_body_web_replay_comparison_tests.xml.sha256 | "607e36bf12ee06bbe8880a374fb63a7692275e5df7c962324f3931da95fd3bee" |
| files.reports/phase6/hard_body_web_replay_input_audit.json.bytes | 1955 |
| files.reports/phase6/hard_body_web_replay_notes.json.bytes | 27869 |
| files.reports/phase6/hard_body_web_replay_notes.json.sha256 | "b856804788da0b67ebf95ba5dd76787e9b644e1322bf322a7a56235a6113fcc5" |
| files.reports/phase6/hard_body_web_replay_observations.tsv.bytes | 11757 |
| files.reports/phase6/hard_body_web_replay_probe_input_audit.json.bytes | 1135 |
| files.reports/phase6/hard_body_web_replay_prototype_initial_failure.xml.bytes | 2753 |
| files.reports/phase6/hard_body_web_replay_prototype_initial_failure.xml.sha256 | "aa98cb05642c7c7c667e2c19b7d72e781bcc4544564d409571142e7ff1dbd665" |
| files.reports/phase6/hard_body_web_replay_prototype_tests.xml.bytes | 720 |
| files.reports/phase6/hard_body_web_replay_prototype_tests.xml.sha256 | "fe40f669e34536dd8bef7fa4078ad706476fbcede41863cc769f34134f5c31b7" |
| files.reports/phase6/hard_body_web_replay_runner_initial_failure.xml.bytes | 801 |
| files.reports/phase6/hard_body_web_replay_runner_initial_failure.xml.sha256 | "19bce3b24b5b8dfee754510f312580e7a2e6d797e146aab6a08ca334661c4016" |
| files.reports/phase6/hard_body_web_replay_trainer_preparation.json.bytes | 3882 |
| files.scripts/audit_hard_body_web_replay_inputs.py.bytes | 3654 |
| files.scripts/hard_body_resident_web_replay_trainer.py.bytes | 1780 |
| files.scripts/hard_body_web_replay.py.bytes | 2875 |
| files.scripts/hard_body_web_replay_accounting.py.bytes | 5857 |
| files.scripts/hard_body_web_replay_trainer.py.bytes | 11169 |
| files.scripts/implement_hard_body_web_replay_comparison.py.bytes | 16680 |
| files.scripts/prepare_hard_body_web_replay.py.bytes | 5187 |
| files.scripts/prepare_hard_body_web_replay_content_review.py.bytes | 8865 |
| files.scripts/record_hard_body_web_replay_completion.py.bytes | 7535 |
| files.scripts/record_hard_body_web_replay_completion.py.sha256 | "92a6581f6d2a9beb6d396a227bc60832ea06ec1cdd16fc3201b0d76139bb91db" |
| files.scripts/record_hard_body_web_replay_launch.py.bytes | 3338 |
| files.scripts/record_hard_body_web_replay_preparation.py.bytes | 3620 |
| files.scripts/review_hard_body_web_replay_comparison.py.bytes | 18383 |
| files.scripts/run_hard_body_web_replay_comparison.ps1.bytes | 3132 |
| files.scripts/run_hard_body_web_replay_comparison.py.bytes | 38204 |
| files.tests/test_hard_body_web_replay.py.bytes | 3147 |
| files.tests/test_hard_body_web_replay.py.sha256 | "e1bb33d0903ef6e4d3e1f246e147d326612c251c59ea0c925debefddcccf060d" |
| files.tests/test_hard_body_web_replay_comparison.py.bytes | 5023 |
| files.tests/test_hard_body_web_replay_comparison.py.sha256 | "47dfa164b6f56d447b17f77805a34a87e97e8476614061838a6a8289adea8fc3" |
| files.tests/test_hard_body_web_replay_trainer.py.bytes | 4535 |
| files.tests/test_hard_body_web_replay_trainer.py.sha256 | "f0cee4d5a56d9872f1455d8fcb7d9d31311b450fb9b46ca66bfd61c05c6721ed" |
| raw_bytes | 15569125 |
| archive_bytes | 2739302 |
| checkpoint_tensors_and_data_arrays_excluded | true |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_proposal.json — one_hard_target_replay_comparison_proposed_not_implemented_or_executed</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_proposal.json) ／ SHA256: `a7fd1e97db4b824cf58fc7ccd1162a8103b1999680b80a9e5f89601ecfc30460` ／ 9,672 bytes

| 原キー | 保存値 |
|---|---|
| status | "one_hard_target_replay_comparison_proposed_not_implemented_or_executed" |
| previous_related_KL_studies_GPU_seconds | 795.3523048920615 |
| source_implementation_config_search.limit | "Limited lexical local implementation/config search, not proof about all external or unregistered research." |
| frozen_reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| frozen_reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| main_teacher_quotas.web | 75000000 |
| main_teacher_quotas.story | 5000000 |
| main_teacher_quotas.ordinary_textbook | 10000000 |
| main_teacher_quotas.conditional_textbook | 10000000 |
| main_ordinary_CE_teacher_tokens | 100000000 |
| primary_supervision_control.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/eos_decoupled_web_kl/training/checkpoint-00323503.pt" |
| primary_supervision_control.checkpoint.sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| primary_supervision_control.notes.sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| primary_supervision_control.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos_decoupled_web_kl_notes.json" |
| mandatory_quality_control.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_order_condition_notes.json" |
| mandatory_quality_control.notes.sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| mandatory_quality_control.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| mandatory_quality_control.checkpoint.sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| auxiliary_policy.every_completed_update | 1 |
| auxiliary_policy.direct_EOS_logit_gradient | "Zero for auxiliary objective by vocabulary exclusion; CE main and shared weights may still change EOS." |
| auxiliary_policy.loss | "Mean over valid body positions of (1-frozen_parent_P(EOS3))*[-log student_P(gold_label ／ non-EOS)]" |
| expected_auxiliary_input_tokens | 25133056 |
| expected_combined_student_input_tokens | 125665280 |
| expected_total_hard_teacher_positions | 125026383 |
| accounting_limit | "Same physical replay exposures/body positions as completed conditionalKL, but hard targets replace soft distribution targets and supply additional gold-word supervision. Not equal hard-supervision count or information to the soft-target comparator." |
| newly_prepared_source_tokens | 0 |
| total_new_GPU_ceiling_seconds | 900 |
| reused_control_GPU_seconds | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_review.json — gold_Web_replay_CE100M_all80_and_cached_stagedCE100M_reviewed</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_review.json) ／ SHA256: `cb16c30b77a42729eb62fca1686b52b53a081333591d0149775218ee2d2c139d` ／ 14,525 bytes

| 原キー | 保存値 |
|---|---|
| status | "gold_Web_replay_CE100M_all80_and_cached_stagedCE100M_reviewed" |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | true |
| mechanism_comparison.checks.repetition_nonworsening | true |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
| mechanism_summary.BPB | 0.9830314888729699 |
| mechanism_summary.rates.eos | 44 |
| mechanism_summary.rates.repetition | 20 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 58 |
| mechanism_summary.relevance2 | 49 |
| mechanism_summary.coherent | 11 |
| mechanism_summary.appropriate | 28 |
| mechanism_summary.notes_sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| previous_related_study_GPU_seconds | 795.3523048920615 |
| summaries.control.BPB | 1.1336128657420816 |
| summaries.control.rates.eos | 76 |
| summaries.control.rates.repetition | 2 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 65 |
| summaries.control.relevance2 | 39 |
| summaries.control.coherent | 23 |
| summaries.control.appropriate | 26 |
| summaries.control.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| summaries.control.additional_teacher_tokens | 100000000 |
| summaries.hard_body_web_replay.BPB | 0.9855284349290349 |
| summaries.hard_body_web_replay.rates.eos | 53 |
| summaries.hard_body_web_replay.rates.repetition | 15 |
| summaries.hard_body_web_replay.rates.unicode_failure | 0 |
| summaries.hard_body_web_replay.rates.role_leak | 0 |
| summaries.hard_body_web_replay.rates.empty | 0 |
| summaries.hard_body_web_replay.grammar2 | 45 |
| summaries.hard_body_web_replay.relevance2 | 56 |
| summaries.hard_body_web_replay.coherent | 17 |
| summaries.hard_body_web_replay.appropriate | 34 |
| summaries.hard_body_web_replay.notes_sha256 | "b856804788da0b67ebf95ba5dd76787e9b644e1322bf322a7a56235a6113fcc5" |
| summaries.hard_body_web_replay.additional_teacher_tokens | 100000000 |
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
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.all_four_source_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| reference_accounting.reference_hard_body_teacher_tokens | 25026383 |
| reference_accounting.combined_hard_teacher_positions | 125026383 |
| reference_accounting.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| reference_accounting.frozen_parent_teacher_digest_verified | true |
| reference_accounting.reference_input_tokens | 25133056 |
| reference_accounting.main_ordinary_CE_teacher_tokens | 100000000 |
| reference_accounting.combined_student_physical_input_tokens | 125665280 |
| reference_accounting.newly_prepared_source_tokens | 0 |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.control.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.sum_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.all128.accuracy | 0.61328125 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.all128.both_correct | 40 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.accuracy | 0.46875 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.both_correct | 7 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.both_correct | 45 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.aligned_context_margin_shift | 95 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.both_correct | 36 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.both_correct | 48 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.same_unique_candidate | 67 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 93 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.accuracy | 0.453125 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.both_correct | 7 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 31 |
| retention_aggregates.control.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention_aggregates.control.sum_log_likelihood.all128.both_correct | 36 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention_aggregates.control.mean_token_log_likelihood.all128.both_correct | 42 |
| retention_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.all128.accuracy | 0.5625 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.all128.both_correct | 20 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.accuracy | 0.6171875 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.both_correct | 16 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.both_correct | 4 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.accuracy | 0.57421875 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.both_correct | 22 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.same_unique_candidate | 103 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.both_correct | 18 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 45 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.accuracy | 0.58984375 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.both_correct | 26 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.same_unique_candidate | 99 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.640625 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| new_scientific_auxiliary_hard_body_teacher_tokens | 25026383 |
| new_scientific_combined_hard_teacher_positions | 125026383 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 349.4322593070101 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_hard_positions | 326339 |
| verification_GPU_seconds | 28.81082727899775 |
| prior_probe_GPU_seconds | 0.0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Gold words replace conditional soft distributions on identical replay windows, with identical frozen parent mass weights and non-EOS vocabulary. Main100M ordinary CE plus separately counted auxiliary gold-body teachers; not equal supervision/information to conditionalKL or plain stagedCE. New corpus0, train overlaps. One seed/nonblind repeated fixeddev; independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_workspace_state.json — science_terminal_and_original_UI_restored</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_workspace_state.json) ／ SHA256: `ef62d08209632c231f1f5d3b772c5f914273587a759d85442f7aa1449d063de5` ／ 1,218 bytes

| 原キー | 保存値 |
|---|---|
| status | "science_terminal_and_original_UI_restored" |
| checked_at | "2026-10-06T07:56:15.7709910Z" |
| HTTP_model.training_tokens | 10000007168 |
| HTTP_model.update | 305176 |
| HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_input_audit.json — None</summary>

[原記録](../../reports/phase6/hard_body_web_replay_input_audit.json) ／ SHA256: `6482e47bb323c586a1cc87546a0e8eceb5fc5053bbb58fe50fbcbfcc99e762a3` ／ 1,955 bytes

| 原キー | 保存値 |
|---|---|
| all32.updates | 32 |
| all32.all_parent_non_EOS_probability_masses_equal | true |
| all32.gold_body_teacher_positions | 261063 |
| all32.non_EOS_parent_probability_mass | 260614.552734375 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_source_tokens | 0 |
| limitations | "Equal inputs/mass are not equal supervision: current targets are gold words, control targets are conditional soft distributions. No quality or sole-cause proof." |
| all3068.updates | 3068 |
| all3068.all_parent_non_EOS_probability_masses_equal | true |
| all3068.gold_body_teacher_positions | 25026383 |
| all3068.non_EOS_parent_probability_mass | 24981892.629882812 |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_notes.json — None</summary>

[原記録](../../reports/phase6/hard_body_web_replay_notes.json) ／ SHA256: `b856804788da0b67ebf95ba5dd76787e9b644e1322bf322a7a56235a6113fcc5` ／ 27,869 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_probe_input_audit.json — None</summary>

[原記録](../../reports/phase6/hard_body_web_replay_probe_input_audit.json) ／ SHA256: `467737fface78ac64c945147978ac6812258e8023ede0a7e2bb0f1378b4f60d5` ／ 1,135 bytes

| 原キー | 保存値 |
|---|---|
| all32.updates | 32 |
| all32.all_parent_non_EOS_probability_masses_equal | true |
| all32.gold_body_teacher_positions | 261063 |
| all32.non_EOS_parent_probability_mass | 260614.552734375 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_source_tokens | 0 |
| limitations | "Equal inputs/mass are not equal supervision: current targets are gold words, control targets are conditional soft distributions. No quality or sole-cause proof." |

</details>

<details>
<summary>reports/phase6/historical_binding.json — None</summary>

[原記録](../../reports/phase6/historical_binding.json) ／ SHA256: `9137130b9c371a730d26ab12fc74ea4873dd18a027de98c1b4695cf89cda9438` ／ 6,683 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase5/documentation_update_20261003.json | "4bbc45a5c0658cd8f844a6a190b6d6dd96ea29491a992eff2bfe69e275cbc486" |
| files.reports/phase1/verification.json | "85b9d7ad2de4963dcdcec9b15c596d764b7ed844398dbc2c4649e8633af738f8" |
| files.reports/phase5/failed_attempts.json | "7be4a0776d5f2d77daebff5ace343fabe61edf4b7b7a72a7ba6d276dcc4bade5" |
| files.reports/phase3/cli_checks.json | "9427063c0e6405b20183a2101a4a42de5b46c75f5fdca574fff09448823da94f" |
| files.reports/phase5/resource_budget.json | "ed53ef6ad3fc4017d64dd2e53cb601b9c486531e36834430a1faedeb9a8547d8" |
| files.reports/phase2/tokenizer_comparison.json | "36a8896cc03629f560b04bf5584f35d35e18cf1d89e0d0836278ba83c3300037" |
| files.reports/phase3/completion_audit.json | "ae5c790bc5f5879b71d80ef2af57e4b735deb6a2fb50b6165ad1bfa8735941f3" |
| files.reports/phase5/performance_status.md | "0200cc482df66d1a7a053118e483013528c12987ee174f35ce80aa369d9bae4c" |
| files.reports/phase0/completion_audit.json | "454553e866be6d580616d397c7c243b9f3860f15412807b4d0a8fd1f87ed4171" |
| files.reports/phase2/tokenizer_contract_report.json | "ee70eb1aa38573654498318b8e186af673e71443958362a7dd56d721105f487e" |
| files.reports/phase5/tokenizer_model_comparison.json | "7d3cd62a8e2d7db8b7c44b59937695cffd91461b94c32f7c486e62faf52c5bd5" |
| files.reports/phase5/auditor_contract_checks.json | "de6d3056e9e7dc176859a3109994c647b9b5ad238066f026b660e025e7b59085" |
| files.reports/phase2/tokenizer_training_candidates.json | "7262b5e7325e49125561ee33eccdd6a6f607bab4d9e41a3b95f5ca2b8a8b4059" |
| files.reports/phase4/resource_budget.md | "f5e1f87082c019b1489a504456ac2117e089071960c4d1a08e228f2a6a4becfd" |
| files.reports/phase5/documentation_audit.json | "26037f9f7722513ab80562e3c68ea328c2a02f10e8efddf083da7ffdbbabe953" |
| files.reports/phase5/tokenizer_baseline_comparison.json | "aa077033dd5c9152734553629c16681b4a7ad9f0657decb046803bbfb9642037" |
| files.reports/phase1/completion_audit.json | "407d156013eda48b06449d352a3772fd519b4edf13740ca96fdbb7451c74ee49" |
| files.reports/phase5/tests.xml | "f7efe820a64237dfd65225ca7b5eeb80880ddb7841d439e922e7c5b6121feaf5" |
| files.reports/phase5/process_completion.json | "564126b5fce5e4ad1aaa2b2c0a001baeeda87f5168b0db5031a5fa0dc5d80ebc" |
| files.reports/phase3/tests.xml | "747abf6abb7a681abc2a44631c20c78250be83677803847b43fccd14173999b3" |
| files.reports/phase5/completion_audit.json | "148b5be13cc56de114392d5a41c74b2b95253e53eaf6424ba592f1a420c4ae21" |

</details>

<details>
<summary>reports/phase6/hub_artifacts_verification.json — passed</summary>

[原記録](../../reports/phase6/hub_artifacts_verification.json) ／ SHA256: `060cd7cc6f48b7c946b996a098a5c3235456e9317a26606ac3fc60eef7762b57` ／ 121 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |

</details>

<details>
<summary>reports/phase6/improved-base-5b-20261006_annotations.json — None</summary>

[原記録](../../reports/phase6/improved-base-5b-20261006_annotations.json) ／ SHA256: `55c126012dca1c70b00e0f9c29aab1ef2673bd6a7c34a891298f760087a06ff9` ／ 38,296 bytes

| 原キー | 保存値 |
|---|---|
| arms.large-2000000000.notes_sha256 | "46f6e00c6b4df7d42e52dd12a5c9bbfadeaf8b8799b56ed415e1ac357163e5a4" |
| arms.large-5000000000.notes_sha256 | "3bdb8688313324f45acb6c49813986240b34a17a64e0f1cf2441fcdcafbb21f6" |

</details>

<details>
<summary>reports/phase6/improved-base-5b-20261006_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/improved-base-5b-20261006_evidence_manifest.json) ／ SHA256: `831b0a853407105349554a28465d9f9cc25bb4d5e3bba7c2b6a896755db86620` ／ 6,790 bytes

| 原キー | 保存値 |
|---|---|
| bytes | 14094878 |
| limitation | "Tensor checkpoints/data remain at bound WSL paths; research/dev evidence does not adopt Base" |

</details>

<details>
<summary>reports/phase6/improved-base-5b-20261006_review.json — improved_base_stage_evidence_complete</summary>

[原記録](../../reports/phase6/improved-base-5b-20261006_review.json) ／ SHA256: `3dc9ca68480c11eaafa035ce4569a857ebae14c8bc310cd56ce9810631e9e10b` ／ 2,254 bytes

| 原キー | 保存値 |
|---|---|
| status | "improved_base_stage_evidence_complete" |
| summary.prepared_tokens | 500000785 |
| summary.stable_teachers | 5000000000 |
| summary.decay_teachers | 20000000 |
| summary.BPB | 1.1272183453882345 |
| summary.rates.eos | 34 |
| summary.rates.repetition | 18 |
| summary.rates.unicode_failure | 0 |
| summary.rates.role_leak | 0 |
| summary.rates.empty | 0 |
| summary.grammar2 | 35 |
| summary.relevance2 | 31 |
| summary.coherent | 15 |
| summary.appropriate | 24 |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| notes_sha256 | "3bdb8688313324f45acb6c49813986240b34a17a64e0f1cf2441fcdcafbb21f6" |
| scientific_stable_teachers | 3000000000 |
| scientific_decay_teachers | 20000000 |
| verification_teacher_tokens | 521760 |
| GPU_seconds | 4681.7914982520015 |
| protected_test_used | false |
| numerical_failures72_unchanged | true |
| Base_adopted | false |
| requested_five_steps_complete | false |
| final_seed_full_evaluation_test_pending | true |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/compare-result.json — masked_suffix_GPU_complete_pending_all80_content_review</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/compare-result.json) ／ SHA256: `e3b5f1c8ac5845872592b761cf6d8d4d1a8ef5be9522e0e3cb5fbdc815714824` ／ 626,133 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| checkpoint.binding.config_sha256 | "4f91703748a2f3f83b40ef0e291266537cc494dac0b65359c3b8eec1d86c22e9" |
| checkpoint.binding.arm | "interleaved_outcome_EOS" |
| checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoint.binding.study_kind | "original_mixed_order_fixed_conditional_outcome_EOS_v1" |
| checkpoint.binding.teacher_goals.web | 75000000 |
| checkpoint.binding.teacher_goals.story | 5000000 |
| checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint.binding.target_rule | "conditional outcome+EOS only; original reference quotas stop input" |
| checkpoint.binding.optimizer_policy | "inherit" |
| checkpoint.binding.peak_lr | 1e-05 |
| checkpoint.updates | 3068 |
| checkpoint.additional_supervised_tokens | 91641755 |
| checkpoint.additional_input_tokens | 100532224 |
| checkpoint.actual_body_bytes | 361357103 |
| checkpoint.reference_suffix_teacher_tokens | 100000000 |
| checkpoint.actual_source_accounting.teachers.web | 75000000 |
| checkpoint.actual_source_accounting.teachers.story | 5000000 |
| checkpoint.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| checkpoint.actual_source_accounting.eos.web | 159170 |
| checkpoint.actual_source_accounting.eos.story | 38240 |
| checkpoint.actual_source_accounting.eos.ordinary_textbook | 74183 |
| checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| checkpoint.actual_source_accounting.body_bytes.web | 292149840 |
| checkpoint.actual_source_accounting.body_bytes.story | 20452979 |
| checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| checkpoint.actual_source_accounting.focus.web | 0 |
| checkpoint.actual_source_accounting.focus.story | 0 |
| checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.kind | "original-Web-retention-short-source-quotas-v1" |
| checkpoint.sampler.goals.web | 75000000 |
| checkpoint.sampler.goals.story | 5000000 |
| checkpoint.sampler.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.context | 1024 |
| checkpoint.sampler.seed | 42 |
| checkpoint.sampler.position | 3068 |
| checkpoint.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.streams.web.sampler.seed | 42 |
| checkpoint.sampler.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.streams.web.sampler.position | 10327341 |
| checkpoint.sampler.streams.web.sampler.context | 1024 |
| checkpoint.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.streams.story.seed | 42 |
| checkpoint.sampler.streams.story.genre | "story" |
| checkpoint.sampler.streams.story.documents | 761448 |
| checkpoint.sampler.streams.story.epoch | 0 |
| checkpoint.sampler.streams.story.document_position | 38243 |
| checkpoint.sampler.streams.story.token_offset | 87 |
| checkpoint.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoint.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoint.sampler.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoint.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoint.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoint.sampler.source_teachers.web | 75000000 |
| checkpoint.sampler.source_teachers.story | 5000000 |
| checkpoint.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoint.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoint.sampler.source_eos.web | 159170 |
| checkpoint.sampler.source_eos.story | 38240 |
| checkpoint.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoint.sampler.source_eos.conditional_textbook | 234328 |
| checkpoint.sampler.source_tokens.web | 75183104 |
| checkpoint.sampler.source_tokens.story | 5039104 |
| checkpoint.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoint.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoint.sampler.source_body_bytes.web | 292149840 |
| checkpoint.sampler.source_body_bytes.story | 20452979 |
| checkpoint.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoint.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoint.sampler.source_focus_teachers.web | 0 |
| checkpoint.sampler.source_focus_teachers.story | 0 |
| checkpoint.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 159170 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 38240 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 74183 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 292149840 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 20452979 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 42739471 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "original-Web-retention-short-source-quotas-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10253920 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| checkpoint.sampler.prefix_mask_accounting.reference_policy | "interleaved" |
| checkpoint.token_digest | "d5e3ff03c09fd0e95a1a2b3e2160e24b02f007e10b564a2385c4aaed4c97dac4" |
| checkpoint.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| checkpoint.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| checkpoint.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| checkpoint.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| checkpoint.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| checkpoint.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| checkpoint.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| checkpoint.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| checkpoint.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| checkpoint.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| checkpoint.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| checkpoint.training_seconds | 168.67648764658952 |
| evaluation.binding.teacher_goals.web | 75000000 |
| evaluation.binding.teacher_goals.story | 5000000 |
| evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluation.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| evaluation.body.documents | 256 |
| evaluation.body.limit_documents | 256 |
| evaluation.body.body_nll | 318400.7202720642 |
| evaluation.body.eos_nll | 583.9714539796114 |
| evaluation.body.body_bytes | 472055 |
| evaluation.body.body_tokens | 122343 |
| evaluation.body.bpb | 0.9730966521951491 |
| evaluation.body.seconds | 1.621353958005784 |
| evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluation.generation.max_new_tokens | 64 |
| evaluation.greedy_rates.eos | 22 |
| evaluation.greedy_rates.repetition | 35 |
| evaluation.greedy_rates.unicode_failure | 0 |
| evaluation.greedy_rates.role_leak | 0 |
| evaluation.greedy_rates.empty | 0 |
| evaluation.diagnostics.semantics.primary.accuracy.point | 0.6145833333333334 |
| evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5729166666666666, 0.65625] |
| evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6145833333333334 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.59375 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6302083333333334] |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.59375 |
| evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.592156862745098 |
| evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.18898223650461363 |
| evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.time.seed | 42 |
| evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8157099697885196] |
| evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7129909365558912 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6646525679758308, 0.7643504531722054] |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7129909365558912 |
| evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41622574955908287 |
| evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| evaluation.diagnostics.jcqa.primary.accuracy.point | 0.353887399463807 |
| evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.3270554066130474, 0.3806970509383378] |
| evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.353887399463807 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3109919571045576 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28328865058087577, 0.3378016085790885] |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3109919571045576 |
| evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3101668649340549 |
| evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.13894601295959533 |
| evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.semantic_both_contexts.correct | 22 |
| evaluation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluation.protected_test_used | false |
| bridge.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| bridge.checks.weights_unchanged | true |
| bridge.checks.no_gradients | true |
| bridge.checks.eval_mode | true |
| bridge.checks.RNG_restored | true |
| bridge.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62109375 |
| bridge.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.765625 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 35 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 10 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62109375 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 37 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 26 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 7 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 49 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 39 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 10 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 40 |
| bridge.optimizer_updates | 0 |
| bridge.scientific_teacher_tokens | 0 |
| bridge.protected_test_used | false |
| bridge.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| retention.checks.weights_unchanged | true |
| retention.checks.no_gradients | true |
| retention.checks.eval_mode | true |
| retention.checks.RNG_restored | true |
| retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.640625 |
| retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 41 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 80 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.71875 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 31 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.64453125 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 42 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 81 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 29 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| retention.optimizer_updates | 0 |
| retention.scientific_teacher_tokens | 0 |
| retention.protected_test_used | false |
| retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| scientific_teacher_tokens | 91641755 |
| scientific_optimizer_updates | 3068 |
| matched_masked_recipe_teacher_budget | true |
| matched_original_hard_teacher_budget | false |
| status | "masked_suffix_GPU_complete_pending_all80_content_review" |
| GPU_seconds | 261.29975055900286 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/content-notes.json) ／ SHA256: `dc9dfd4e3861267fa9b0c8b2df2cb8865aece002b6f6f2863b1e27c9d6760ca4` ／ 24,791 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/latest.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/latest.json) ／ SHA256: `76eebb8fe5eb754f494fb4c827e91774033c468eb76c4021f294176f7711ec5a` ／ 297 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/job.json) ／ SHA256: `822491cb044e834760c7080daed7e065c080058209c93ca0275abf44b922420c` ／ 815 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 261.29975055900286 |
| completed_updates | 3060 |
| total_updates | 3068 |
| actual_teachers | 91426867 |
| reference_teachers | 99765337 |
| loss | 2.5054211616516113 |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/probe/job.json) ／ SHA256: `9850e819e7abe8219a5853f5ac88ae1e7618ac83acb89150d641cb8d00622253` ／ 544 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 17.989334398997016 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/probe/result.json — own_masked_CUDA_probe_complete</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/probe/result.json) ／ SHA256: `03c991b3c8b9f17ff01c9efc1f70a477171dd2fe20729146e5624cb2678921e3` ／ 241,567 bytes

| 原キー | 保存値 |
|---|---|
| initial_fullstate_preservation.actual_parent_sampler_lineage | true |
| gate.passed | true |
| gate.checks.version | true |
| gate.checks.spec | true |
| gate.checks.model_config | true |
| gate.checks.model | true |
| gate.checks.optimizer | true |
| gate.checks.scheduler | true |
| gate.checks.rng | true |
| gate.checks.sampler | true |
| gate.checks.update | true |
| gate.checks.tokens | true |
| gate.checks.supervised_tokens | true |
| gate.checks.body_bytes | true |
| gate.checks.token_digest | true |
| gate.checks.focus_token_digest | true |
| gate.checks.focus_teacher_tokens | true |
| gate.checks.weighted_teacher_mass | true |
| gate.checks.shard_manifest_sha256 | true |
| gate.checks.implementation_sha256 | true |
| gate.checks.study_implementation_sha256 | true |
| gate.checks.loss_implementation_sha256 | true |
| gate.checks.study_binding | true |
| gate.checks.pilot_binding | true |
| gate.checks.lineage | true |
| gate.checks.branch_updates | true |
| gate.checks.branch_tokens | true |
| gate.checks.history_loss | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_body_bytes_seen | true |
| gate.checks.history_reference_suffix_teacher_tokens | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_reference_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_additional_teacher_tokens | true |
| gate.checks.history_actual_source_eos | true |
| gate.checks.history_supervised_tokens | true |
| gate.checks.history_tokens_seen | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_actual_source_teachers | true |
| gate.checks.history_actual_source_body_bytes | true |
| gate.checks.history_actual_source_routes | true |
| gate.checks.history_valid_input_tokens | true |
| gate.checks.history_update | true |
| gate.checks.history_source_digests | true |
| gate.checks.history_physical_input_tokens | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_removed_prefix_targets | true |
| gate.checks.history_lr | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_outcome_weight | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.checks.mixed_sources_present | true |
| gate.checks.actual_conditional_mask_active | true |
| gate.GPU_optimizer_updates | 16 |
| gate.verification_teacher_tokens | 478390 |
| timing.verification_teacher_tokens | 955529 |
| timing.terminal_save_seconds | 0.19467564299702644 |
| timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint.sha256 | "eca29d9bc5e449eae473f159f974e3e860e3cebd923c6938b4294c55215868b5" |
| timing.peak_VRAM_bytes | 6149106176 |
| passed | true |
| GPU_optimizer_updates | 48 |
| verification_teacher_tokens | 1433919 |
| scientific_teacher_tokens | 0 |
| status | "own_masked_CUDA_probe_complete" |
| GPU_seconds | 17.989334398997016 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json) ／ SHA256: `38614bc57c4a10e7a669cb211c3b188812d344694241d3e4fac81c8ad4f6ec90` ／ 268 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>
