# 評価・生成・意味診断 — 11/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition_relation_language_proposal.json — defined_single_relation_language_bridge_not_implemented_not_prepared_not_frozen_not_started</summary>

[原記録](../../reports/phase6/condition_relation_language_proposal.json) ／ SHA256: `ebf4a03f7a239833f9e5d5020ff9c9a6f23acafa0039f2ebac44f52c0a1f709b` ／ 7,807 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_single_relation_language_bridge_not_implemented_not_prepared_not_frozen_not_started" |
| fixeddev_pairs.sha256 | "95d3bb0dbb2dca22f77936f5e36b9f399f96e42acdf09ab7c1fef8ba688500a1" |
| fixeddev_pairs.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition_transfer_condition_pair_analysis.json" |
| observed.coherence | "12/80 to14/80; CI[-.05,.1]" |
| observed.natural_comparison_both_correct | "0/16 to0/16" |
| observed.natural_causality_both_correct | "1/16 to9/16" |
| observed.structural_generator_both_correct | "3/64 to20/64" |
| observed.generator_both_correct | "7/128 to63/128" |
| observed.original_Web_guard_passed | false |
| observed.natural_negation_both_correct | "0/16 to0/16" |
| hypothesis | "Source predicates copy an action record or compare numerical lengths; successful local transfer need not teach negated Japanese predicates, relational directions and contextual continuations. This surface/semantic mismatch is a hypothesis, not a proven sole cause or10M capacity limit." |
| controls.new_public_corpus_tokens | 0 |
| controls.reuse_completed_curriculum100M.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| controls.reuse_completed_curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| controls.reuse_completed_curriculum100M.binding.teacher_goals.web | 75000000 |
| controls.reuse_completed_curriculum100M.binding.teacher_goals.story | 5000000 |
| controls.reuse_completed_curriculum100M.binding.teacher_goals.ordinary_textbook | 10000000 |
| controls.reuse_completed_curriculum100M.binding.teacher_goals.conditional_textbook | 10000000 |
| controls.reuse_completed_curriculum100M.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| controls.reuse_completed_curriculum100M.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| controls.reuse_completed_curriculum100M.update | 65249 |
| controls.reuse_completed_curriculum100M.tokens | 2138079232 |
| controls.reuse_completed_curriculum100M.supervised_tokens | 2120000000 |
| controls.reuse_completed_curriculum100M.additional_supervised_tokens | 100000000 |
| controls.reuse_completed_curriculum100M.additional_input_tokens | 101023744 |
| controls.reuse_completed_curriculum100M.source_teachers.web | 75000000 |
| controls.reuse_completed_curriculum100M.source_teachers.story | 5000000 |
| controls.reuse_completed_curriculum100M.source_teachers.ordinary_textbook | 10000000 |
| controls.reuse_completed_curriculum100M.source_teachers.conditional_textbook | 10000000 |
| controls.reuse_completed_curriculum100M.source_eos.web | 656229 |
| controls.reuse_completed_curriculum100M.source_eos.story | 38240 |
| controls.reuse_completed_curriculum100M.source_eos.ordinary_textbook | 74183 |
| controls.reuse_completed_curriculum100M.source_eos.conditional_textbook | 243066 |
| controls.reuse_completed_curriculum100M.source_input_tokens.web | 75666432 |
| controls.reuse_completed_curriculum100M.source_input_tokens.story | 5039104 |
| controls.reuse_completed_curriculum100M.source_input_tokens.ordinary_textbook | 10075136 |
| controls.reuse_completed_curriculum100M.source_input_tokens.conditional_textbook | 10243072 |
| controls.reuse_completed_curriculum100M.source_focus_teachers.web | 0 |
| controls.reuse_completed_curriculum100M.source_focus_teachers.story | 0 |
| controls.reuse_completed_curriculum100M.source_focus_teachers.ordinary_textbook | 0 |
| controls.reuse_completed_curriculum100M.source_focus_teachers.conditional_textbook | 1460032 |
| controls.reuse_completed_curriculum100M.focus_teacher_tokens | 1460032 |
| controls.reuse_completed_curriculum100M.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| controls.reuse_completed_curriculum100M.weighted_teacher_mass | 100000000 |
| controls.reuse_completed_curriculum100M.training_seconds | 152.96801666589454 |
| controls.new_learning_teachers | 100000000 |
| controls.reused_control_learning_teachers | 100000000 |
| preparation.CPU_limit_seconds | 240 |
| preparation.weak_limit | 10 |
| preparation.documents | 2048 |
| preparation.unchanged_other_four_categories_byte_exact | true |
| preparation.unresolved_grammar_forbidden | true |
| GPU_limit_seconds_including_probe | 900 |
| GPU_precondition | "Related CPU checks; actual continuous4 vs2+2 fullstate/history/finite gate; continuous timing/save/evaluation budget plus30percent margin within total900seconds. Verification weights are discarded. Completed control evaluations are reused; only new probe cases require fresh control scoring." |
| completion | "One new100M actual terminal checkpoint, inherited fullstate/counters/ordinary3 teacher audit, original commonbyte256/472055bytes, Japanese192/331/1119, all new80 individually read with exact prior grade reuse, all retained/new probe families, original relative/absolute/Web1percent gates, terminal PID, portable evidence, original UI restored and local commit." |
| failure_policy | "Reject unqualified material/candidate; do not lower criteria or automatically sweep weights/ratios/operators or extend200M/500M/5B/10B. Choose any later experiment from its evidence under a separately defined comparison." |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_trainfit_diagnostic_completion.json — optimizer0_diagnostic_complete</summary>

[原記録](../../reports/phase6/condition_trainfit_diagnostic_completion.json) ／ SHA256: `c4fb2f8e21ac5c000b8c97b5e1b9c508e47f6c3daf51323caf935311a4cd1c99` ／ 2,162 bytes

| 原キー | 保存値 |
|---|---|
| status | "optimizer0_diagnostic_complete" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 4.704371909989277 |
| job.GPU_budget_seconds | 60 |
| job.optimizer_updates | 0 |
| job.scientific_teacher_tokens | 0 |
| job.protected_test_used | false |
| job.completed_documents | 1536 |
| job.total_documents | 1536 |
| original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.training_tokens | 10000007168 |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_trainfit_diagnostic_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_trainfit_diagnostic_evidence_manifest.json) ／ SHA256: `4e46e4033d2ec30e64a8185512816cfa74e8ffa89ee0182afcfb3b5760d0cec1` ／ 14,407 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 14042315 |
| archive.bytes | 3681803 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_trainfit_diagnostic_review.json — actual512_by3_trainfit_diagnostic_review_complete</summary>

[原記録](../../reports/phase6/condition_trainfit_diagnostic_review.json) ／ SHA256: `abc2a05db3f159e9984f63c58a74a91cc20dbb75bc2ec15ef24867e82ee4aa29` ／ 6,740 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual512_by3_trainfit_diagnostic_review_complete" |
| summary.absolute.parent2B.focus_body.tokens | 18956 |
| summary.absolute.parent2B.focus_body.nll_sum | 38308.656169084345 |
| summary.absolute.parent2B.focus_body.mean_nll | 2.0209250986011997 |
| summary.absolute.parent2B.other_body.tokens | 52929 |
| summary.absolute.parent2B.other_body.nll_sum | 112861.09513833707 |
| summary.absolute.parent2B.other_body.mean_nll | 2.132311117503393 |
| summary.absolute.parent2B.EOS.tokens | 512 |
| summary.absolute.parent2B.EOS.nll_sum | 19.632498978811782 |
| summary.absolute.parent2B.EOS.mean_nll | 0.03834472456799176 |
| summary.absolute.control.focus_body.tokens | 18956 |
| summary.absolute.control.focus_body.nll_sum | 10291.589236868997 |
| summary.absolute.control.focus_body.mean_nll | 0.5429198795562881 |
| summary.absolute.control.other_body.tokens | 52929 |
| summary.absolute.control.other_body.nll_sum | 47014.97718621402 |
| summary.absolute.control.other_body.mean_nll | 0.8882649811297024 |
| summary.absolute.control.EOS.tokens | 512 |
| summary.absolute.control.EOS.nll_sum | 3.520820114765229 |
| summary.absolute.control.EOS.mean_nll | 0.006876601786650838 |
| summary.absolute.positive4.focus_body.tokens | 18956 |
| summary.absolute.positive4.focus_body.nll_sum | 1527.8687944701169 |
| summary.absolute.positive4.focus_body.mean_nll | 0.0806008015652098 |
| summary.absolute.positive4.other_body.tokens | 52929 |
| summary.absolute.positive4.other_body.nll_sum | 43378.79789323751 |
| summary.absolute.positive4.other_body.mean_nll | 0.8195657936714752 |
| summary.absolute.positive4.EOS.tokens | 512 |
| summary.absolute.positive4.EOS.nll_sum | 3.269683505182911 |
| summary.absolute.positive4.EOS.mean_nll | 0.006386100596060373 |
| summary.paired_deltas.parent2B-&gt;control.focus_body.documents | 504 |
| summary.paired_deltas.parent2B-&gt;control.focus_body.improved_documents | 504 |
| summary.paired_deltas.parent2B-&gt;control.focus_body.mean_document_delta | -1.4715183502675948 |
| summary.paired_deltas.parent2B-&gt;control.focus_body.median_document_delta | -1.460397604878323 |
| summary.paired_deltas.parent2B-&gt;control.focus_body.token_weighted_delta | -1.4780052190449116 |
| summary.paired_deltas.parent2B-&gt;control.other_body.documents | 512 |
| summary.paired_deltas.parent2B-&gt;control.other_body.improved_documents | 512 |
| summary.paired_deltas.parent2B-&gt;control.other_body.mean_document_delta | -1.230554497241752 |
| summary.paired_deltas.parent2B-&gt;control.other_body.median_document_delta | -1.2364465576391395 |
| summary.paired_deltas.parent2B-&gt;control.other_body.token_weighted_delta | -1.2440461363736905 |
| summary.paired_deltas.parent2B-&gt;control.EOS.documents | 512 |
| summary.paired_deltas.parent2B-&gt;control.EOS.improved_documents | 421 |
| summary.paired_deltas.parent2B-&gt;control.EOS.mean_document_delta | -0.031468122781340924 |
| summary.paired_deltas.parent2B-&gt;control.EOS.median_document_delta | -0.00150430275243707 |
| summary.paired_deltas.parent2B-&gt;control.EOS.token_weighted_delta | -0.031468122781340924 |
| summary.paired_deltas.parent2B-&gt;positive4.focus_body.documents | 504 |
| summary.paired_deltas.parent2B-&gt;positive4.focus_body.improved_documents | 504 |
| summary.paired_deltas.parent2B-&gt;positive4.focus_body.mean_document_delta | -1.9077975160828031 |
| summary.paired_deltas.parent2B-&gt;positive4.focus_body.median_document_delta | -1.9093948516633787 |
| summary.paired_deltas.parent2B-&gt;positive4.focus_body.token_weighted_delta | -1.94032429703599 |
| summary.paired_deltas.parent2B-&gt;positive4.other_body.documents | 512 |
| summary.paired_deltas.parent2B-&gt;positive4.other_body.improved_documents | 512 |
| summary.paired_deltas.parent2B-&gt;positive4.other_body.mean_document_delta | -1.2982318055338697 |
| summary.paired_deltas.parent2B-&gt;positive4.other_body.median_document_delta | -1.3102021759793552 |
| summary.paired_deltas.parent2B-&gt;positive4.other_body.token_weighted_delta | -1.3127453238319178 |
| summary.paired_deltas.parent2B-&gt;positive4.EOS.documents | 512 |
| summary.paired_deltas.parent2B-&gt;positive4.EOS.improved_documents | 402 |
| summary.paired_deltas.parent2B-&gt;positive4.EOS.mean_document_delta | -0.03195862397193139 |
| summary.paired_deltas.parent2B-&gt;positive4.EOS.median_document_delta | -0.0012537539550976362 |
| summary.paired_deltas.parent2B-&gt;positive4.EOS.token_weighted_delta | -0.03195862397193139 |
| summary.paired_deltas.control-&gt;positive4.focus_body.documents | 504 |
| summary.paired_deltas.control-&gt;positive4.focus_body.improved_documents | 504 |
| summary.paired_deltas.control-&gt;positive4.focus_body.mean_document_delta | -0.4362791658152084 |
| summary.paired_deltas.control-&gt;positive4.focus_body.median_document_delta | -0.42214949819569686 |
| summary.paired_deltas.control-&gt;positive4.focus_body.token_weighted_delta | -0.4623190779910783 |
| summary.paired_deltas.control-&gt;positive4.other_body.documents | 512 |
| summary.paired_deltas.control-&gt;positive4.other_body.improved_documents | 497 |
| summary.paired_deltas.control-&gt;positive4.other_body.mean_document_delta | -0.06767730829211746 |
| summary.paired_deltas.control-&gt;positive4.other_body.median_document_delta | -0.06472813026829882 |
| summary.paired_deltas.control-&gt;positive4.other_body.token_weighted_delta | -0.06869918745822723 |
| summary.paired_deltas.control-&gt;positive4.EOS.documents | 512 |
| summary.paired_deltas.control-&gt;positive4.EOS.improved_documents | 211 |
| summary.paired_deltas.control-&gt;positive4.EOS.mean_document_delta | -0.0004905011905904644 |
| summary.paired_deltas.control-&gt;positive4.EOS.median_document_delta | 5.738238542107865e-05 |
| summary.paired_deltas.control-&gt;positive4.EOS.token_weighted_delta | -0.0004905011905904644 |
| checks.parent2B.weights_unchanged | true |
| checks.parent2B.RNG_restored | true |
| checks.parent2B.no_gradients | true |
| checks.parent2B.eval_mode | true |
| checks.parent2B.first_document_batched_vs_single_max_NLL_difference | 0.0 |
| checks.control.weights_unchanged | true |
| checks.control.RNG_restored | true |
| checks.control.no_gradients | true |
| checks.control.eval_mode | true |
| checks.control.first_document_batched_vs_single_max_NLL_difference | 0.0 |
| checks.positive4.weights_unchanged | true |
| checks.positive4.RNG_restored | true |
| checks.positive4.no_gradients | true |
| checks.positive4.eval_mode | true |
| checks.positive4.first_document_batched_vs_single_max_NLL_difference | 0.0 |
| actual_GPU_seconds | 4.703986317006638 |
| GPU_occupation_seconds | 4.704371909989277 |
| target_documents | 512 |
| measured_checkpoint_documents | 1536 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| actual_conditional_teacher_tokens.control | 2500000 |
| actual_conditional_teacher_tokens.positive4 | 2500000 |
| conditional_teacher_exposures.control | 34.53181761675207 |
| conditional_teacher_exposures.positive4 | 34.53181761675207 |
| heldout_content.control.coherent | 15 |
| heldout_content.control.appropriate | 27 |
| heldout_content.control.grammar2 | 54 |
| heldout_content.control.rates.eos | 44 |
| heldout_content.control.rates.repetition | 26 |
| heldout_content.control.rates.unicode_failure | 0 |
| heldout_content.control.rates.role_leak | 0 |
| heldout_content.control.rates.empty | 0 |
| heldout_content.positive4.coherent | 9 |
| heldout_content.positive4.appropriate | 24 |
| heldout_content.positive4.grammar2 | 61 |
| heldout_content.positive4.rates.eos | 47 |
| heldout_content.positive4.rates.repetition | 22 |
| heldout_content.positive4.rates.unicode_failure | 0 |
| heldout_content.positive4.rates.role_leak | 0 |
| heldout_content.positive4.rates.empty | 0 |
| interpretation | "Original positive targets fit substantially better after weight4 than ordinary CE on every504 focus-enabled document, while fixed-dev generation coherence drops15-&gt;9. This supports fitting without demonstrated transfer on these data/one seed. It does not prove the sole cause, capacity limit, independent generalization or incompatible counterfactual labels." |

</details>

<details>
<summary>reports/phase6/condition_transfer_active_job.json — actual100M_complete_all80_original_gates_failed_not_active</summary>

[原記録](../../reports/phase6/condition_transfer_active_job.json) ／ SHA256: `ae6c9c6c8bf102cb51db769f3231bc5c3b298335fb3e3c6b8c4759d0216a4aad` ／ 5,345 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual100M_complete_all80_original_gates_failed_not_active" |
| user_scope | "Base only; report actual qualified Base and stop before Chat/quantization" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 236.22689373401226 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 99914563 |
| job.teacher_budget | 100000000 |
| job.source_teachers.web | 74934975 |
| job.source_teachers.story | 4995784 |
| job.source_teachers.ordinary_textbook | 9991796 |
| job.source_teachers.conditional_textbook | 9992008 |
| job.loss | 2.334336042404175 |
| scientific_config | "configs/phase6/condition_transfer_comparison.json" |
| reused_control_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| reused_control_checkpoint.sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| probe_checks.model | true |
| probe_checks.optimizer | true |
| probe_checks.scheduler | true |
| probe_checks.rng | true |
| probe_checks.sampler | true |
| probe_checks.lineage | true |
| probe_checks.tokens | true |
| probe_checks.supervised_tokens | true |
| probe_checks.body_bytes | true |
| probe_checks.token_digest | true |
| probe_checks.focus_token_digest | true |
| probe_checks.focus_teacher_tokens | true |
| probe_checks.weighted_teacher_mass | true |
| probe_checks.update | true |
| probe_checks.spec | true |
| probe_checks.model_config | true |
| probe_checks.pilot_binding | true |
| probe_checks.study_binding | true |
| probe_checks.history_loss | true |
| probe_checks.history_gradient_norm | true |
| probe_checks.history_lr | true |
| probe_checks.history_token_digest | true |
| probe_checks.history_source_teachers | true |
| probe_checks.history_source_eos | true |
| probe_checks.history_source_input_tokens | true |
| probe_checks.history_source_body_bytes | true |
| probe_checks.history_source_focus_teachers | true |
| probe_checks.history_focus_token_digest | true |
| probe_checks.history_focus_teacher_tokens | true |
| probe_checks.history_weighted_teacher_mass | true |
| probe_checks.finite | true |
| probe_checks.no_reheat | true |
| probe_GPU_seconds | 13.408861087023979 |
| probe_verification_teachers | 1297661 |
| measured_timing.steady_step_seconds | 0.053743930999189615 |
| measured_timing.teachers_per_update | 32441.15625 |
| measured_timing.estimated_updates | 3083 |
| measured_timing.warmup_seconds | 1.5270993670565076 |
| measured_timing.save_seconds | 2.316727126308251 |
| measured_timing.estimated_training_seconds | 169.53636576386634 |
| estimated_science_seconds_with_margin | 560.3972754930262 |
| GPU_total_ceiling_seconds | 900 |
| native_checkpoint_and_completed_update_resume | true |
| Base_adopted | false |
| protected_test_used | false |
| completion | "reports/phase6/condition_transfer_comparison_completion.json" |

</details>

<details>
<summary>reports/phase6/condition_transfer_comparison_completion.json — actual_generated_curriculum100M_and_all80_original_gates_complete_Base_quality_unmet</summary>

[原記録](../../reports/phase6/condition_transfer_comparison_completion.json) ／ SHA256: `3e80212a1cac7a9f601dc7700edc2c9f8dbeb239dfb39386e32dce311dd5267a` ／ 21,234 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_generated_curriculum100M_and_all80_original_gates_complete_Base_quality_unmet" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 236.22689373401226 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 99914563 |
| job.teacher_budget | 100000000 |
| job.source_teachers.web | 74934975 |
| job.source_teachers.story | 4995784 |
| job.source_teachers.ordinary_textbook | 9991796 |
| job.source_teachers.conditional_textbook | 9992008 |
| job.loss | 2.334336042404175 |
| condition_pair_analysis.sha256 | "95d3bb0dbb2dca22f77936f5e36b9f399f96e42acdf09ab7c1fef8ba688500a1" |
| condition_pair_analysis.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition_transfer_condition_pair_analysis.json" |
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checkpoints.control.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| checkpoints.control.binding.arm | "large2048" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.control.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 70061 |
| checkpoints.control.source_input_tokens.web | 75674624 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10071040 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 2620780 |
| checkpoints.control.focus_teacher_tokens | 2620780 |
| checkpoints.control.focus_token_digest | "8e2af3a7a69ecc6ea03b6f189587339877c5cf6d20031ae69100d24ffe4a7d85" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 151.12010613348684 |
| checkpoints.control.completed_at | "2026-10-06T02:43:40.425716Z" |
| checkpoints.curriculum.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.curriculum.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.curriculum.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.curriculum.binding.arm | "curriculum" |
| checkpoints.curriculum.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.curriculum.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.curriculum.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.curriculum.binding.teacher_goals.web | 75000000 |
| checkpoints.curriculum.binding.teacher_goals.story | 5000000 |
| checkpoints.curriculum.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.curriculum.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.curriculum.binding.optimizer_policy | "inherit" |
| checkpoints.curriculum.binding.peak_lr | 0.0002 |
| checkpoints.curriculum.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.curriculum.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.curriculum.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.curriculum.binding.outcome_weight | 1 |
| checkpoints.curriculum.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.curriculum.update | 65249 |
| checkpoints.curriculum.tokens | 2138079232 |
| checkpoints.curriculum.supervised_tokens | 2120000000 |
| checkpoints.curriculum.additional_supervised_tokens | 100000000 |
| checkpoints.curriculum.additional_input_tokens | 101023744 |
| checkpoints.curriculum.source_teachers.web | 75000000 |
| checkpoints.curriculum.source_teachers.story | 5000000 |
| checkpoints.curriculum.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.curriculum.source_teachers.conditional_textbook | 10000000 |
| checkpoints.curriculum.source_eos.web | 656229 |
| checkpoints.curriculum.source_eos.story | 38240 |
| checkpoints.curriculum.source_eos.ordinary_textbook | 74183 |
| checkpoints.curriculum.source_eos.conditional_textbook | 243066 |
| checkpoints.curriculum.source_input_tokens.web | 75666432 |
| checkpoints.curriculum.source_input_tokens.story | 5039104 |
| checkpoints.curriculum.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.curriculum.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.curriculum.source_focus_teachers.web | 0 |
| checkpoints.curriculum.source_focus_teachers.story | 0 |
| checkpoints.curriculum.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.curriculum.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.curriculum.focus_teacher_tokens | 1460032 |
| checkpoints.curriculum.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.curriculum.weighted_teacher_mass | 100000000 |
| checkpoints.curriculum.outcome_weight | 1 |
| checkpoints.curriculum.training_seconds | 152.96801666589454 |
| checkpoints.curriculum.completed_at | "2026-10-06T03:11:09.066152Z" |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| additional_input_tokens | 101023744 |
| actual_training_seconds | 152.96801666589454 |
| verification_updates | 40 |
| verification_teacher_tokens | 1297661 |
| scientific_GPU_seconds | 236.22689373401226 |
| verification_GPU_seconds | 13.408861087023979 |
| total_GPU_seconds | 249.63575482103624 |
| GPU_limit_seconds | 900 |
| completed_checkpoint_is_authoritative | "Job teachers99914563 is a periodic heartbeat; completed checkpoint has exactly100000000 additional teachers and3083 updates." |
| summaries.control.BPB | 1.136865685906886 |
| summaries.control.rates.eos | 42 |
| summaries.control.rates.repetition | 20 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 62 |
| summaries.control.relevance2 | 74 |
| summaries.control.coherent | 12 |
| summaries.control.appropriate | 30 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.control.conditional_source_documents | 2048 |
| summaries.control.notes_sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |
| summaries.control.Base_adopted | false |
| summaries.curriculum.BPB | 1.1302498889302441 |
| summaries.curriculum.rates.eos | 45 |
| summaries.curriculum.rates.repetition | 17 |
| summaries.curriculum.rates.unicode_failure | 0 |
| summaries.curriculum.rates.role_leak | 0 |
| summaries.curriculum.rates.empty | 0 |
| summaries.curriculum.grammar2 | 60 |
| summaries.curriculum.relevance2 | 68 |
| summaries.curriculum.coherent | 14 |
| summaries.curriculum.appropriate | 27 |
| summaries.curriculum.new_teacher_tokens | 100000000 |
| summaries.curriculum.source_teacher_tokens.web | 75000000 |
| summaries.curriculum.source_teacher_tokens.story | 5000000 |
| summaries.curriculum.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.curriculum.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.curriculum.conditional_source_documents | 2048 |
| summaries.curriculum.generated_serialized_tokens | 86309 |
| summaries.curriculum.notes_sha256 | "b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6" |
| summaries.curriculum.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.both_correct | 5 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.both_correct | 1 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.both_correct | 7 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.both_correct | 14 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.accuracy | 0.7109375 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.both_correct | 63 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.both_correct | 66 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| archive.bytes | 2929870 |
| checkpoint_tensors_copied_to_Windows | false |
| restored_original_UI.server.status | "running" |
| restored_original_UI.server.additional_training_tokens | 0 |
| restored_original_UI.server.model.training_tokens | 10000007168 |
| restored_original_UI.server.model.update | 305176 |
| restored_original_UI.server.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| restored_original_UI.server.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_original_UI.server.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| restored_original_UI.HTTP.training_tokens | 10000007168 |
| restored_original_UI.HTTP.update | 305176 |
| restored_original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| restored_original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| related_CPU_checks | "4 meaningful tests passed2.74seconds; PS syntax passed; actualCUDA32 checks and first4 timing trajectory passed" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| independent_learning_seed_used | false |
| requested_five_steps_complete | false |
| limitations | "One learned seed, nonblind judgments, repeatedly inspected fixeddev; generator probe scores are not independent natural-language quality. Shorter local material changes length/EOS/lexical distribution together; not one isolated causal operator effect." |

</details>

<details>
<summary>reports/phase6/condition_transfer_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_transfer_comparison_evidence_manifest.json) ／ SHA256: `89fb2c37f11434b2fc29c2623d540739c2bb4b67ffe37f81a3443d4a50cd5672` ／ 49,695 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 13217315 |
| archive.bytes | 2929870 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_transfer_comparison_review.json — actual_curriculum100M_all80_transfer128_and_reused_natural100M_content_complete</summary>

[原記録](../../reports/phase6/condition_transfer_comparison_review.json) ／ SHA256: `8b5e0d6373ada72b315d81051f93b9afabe9257bd00676592b879d98533daa92` ／ 10,423 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_curriculum100M_all80_transfer128_and_reused_natural100M_content_complete" |
| summaries.control.BPB | 1.136865685906886 |
| summaries.control.rates.eos | 42 |
| summaries.control.rates.repetition | 20 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 62 |
| summaries.control.relevance2 | 74 |
| summaries.control.coherent | 12 |
| summaries.control.appropriate | 30 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.control.conditional_source_documents | 2048 |
| summaries.control.notes_sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |
| summaries.control.Base_adopted | false |
| summaries.curriculum.BPB | 1.1302498889302441 |
| summaries.curriculum.rates.eos | 45 |
| summaries.curriculum.rates.repetition | 17 |
| summaries.curriculum.rates.unicode_failure | 0 |
| summaries.curriculum.rates.role_leak | 0 |
| summaries.curriculum.rates.empty | 0 |
| summaries.curriculum.grammar2 | 60 |
| summaries.curriculum.relevance2 | 68 |
| summaries.curriculum.coherent | 14 |
| summaries.curriculum.appropriate | 27 |
| summaries.curriculum.new_teacher_tokens | 100000000 |
| summaries.curriculum.source_teacher_tokens.web | 75000000 |
| summaries.curriculum.source_teacher_tokens.story | 5000000 |
| summaries.curriculum.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.curriculum.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.curriculum.conditional_source_documents | 2048 |
| summaries.curriculum.generated_serialized_tokens | 86309 |
| summaries.curriculum.notes_sha256 | "b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6" |
| summaries.curriculum.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.both_correct | 5 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.both_correct | 1 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.both_correct | 7 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.both_correct | 14 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.accuracy | 0.7109375 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.both_correct | 63 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.both_correct | 66 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| ordinary_stream_checks.target_sha256 | true |
| ordinary_stream_checks.teachers | true |
| ordinary_stream_checks.EOS | true |
| ordinary_stream_checks.body_bytes | true |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1297661 |
| GPU_seconds | 236.22689373401226 |
| verification_GPU_seconds | 13.408861087023979 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| limitations | "One learned seed, nonblind judgments, repeatedly inspected fixeddev; generator probe scores are not independent natural-language quality. Shorter local material changes length/EOS/lexical distribution together; not one isolated causal operator effect." |

</details>

<details>
<summary>reports/phase6/condition_transfer_condition_pair_analysis.json — actual_curriculum100M_fixeddev_condition_pairs_reused</summary>

[原記録](../../reports/phase6/condition_transfer_condition_pair_analysis.json) ／ SHA256: `95d3bb0dbb2dca22f77936f5e36b9f399f96e42acdf09ab7c1fef8ba688500a1` ／ 185,873 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_curriculum100M_fixeddev_condition_pairs_reused" |
| models.curriculum100M.causality.accuracy | 0.78125 |
| models.curriculum100M.causality.both_correct | 9 |
| models.curriculum100M.causality.neither_correct | 0 |
| models.curriculum100M.comparison.accuracy | 0.4375 |
| models.curriculum100M.comparison.both_correct | 0 |
| models.curriculum100M.comparison.neither_correct | 2 |
| models.curriculum100M.coreference.accuracy | 0.53125 |
| models.curriculum100M.coreference.both_correct | 1 |
| models.curriculum100M.coreference.neither_correct | 0 |
| models.curriculum100M.negation.accuracy | 0.5 |
| models.curriculum100M.negation.both_correct | 0 |
| models.curriculum100M.negation.neither_correct | 0 |
| models.curriculum100M.quantity.accuracy | 0.5 |
| models.curriculum100M.quantity.both_correct | 1 |
| models.curriculum100M.quantity.neither_correct | 1 |
| models.curriculum100M.time.accuracy | 0.4375 |
| models.curriculum100M.time.both_correct | 1 |
| models.curriculum100M.time.neither_correct | 3 |
| models.natural100M.causality.accuracy | 0.53125 |
| models.natural100M.causality.both_correct | 1 |
| models.natural100M.causality.neither_correct | 0 |
| models.natural100M.comparison.accuracy | 0.5 |
| models.natural100M.comparison.both_correct | 0 |
| models.natural100M.comparison.neither_correct | 0 |
| models.natural100M.coreference.accuracy | 0.46875 |
| models.natural100M.coreference.both_correct | 0 |
| models.natural100M.coreference.neither_correct | 1 |
| models.natural100M.negation.accuracy | 0.5 |
| models.natural100M.negation.both_correct | 0 |
| models.natural100M.negation.neither_correct | 0 |
| models.natural100M.quantity.accuracy | 0.53125 |
| models.natural100M.quantity.both_correct | 2 |
| models.natural100M.quantity.neither_correct | 1 |
| models.natural100M.time.accuracy | 0.5 |
| models.natural100M.time.both_correct | 1 |
| models.natural100M.time.neither_correct | 1 |
| models.parent2B.causality.accuracy | 0.625 |
| models.parent2B.causality.both_correct | 4 |
| models.parent2B.causality.neither_correct | 0 |
| models.parent2B.comparison.accuracy | 0.5 |
| models.parent2B.comparison.both_correct | 0 |
| models.parent2B.comparison.neither_correct | 0 |
| models.parent2B.coreference.accuracy | 0.4375 |
| models.parent2B.coreference.both_correct | 0 |
| models.parent2B.coreference.neither_correct | 2 |
| models.parent2B.negation.accuracy | 0.5 |
| models.parent2B.negation.both_correct | 0 |
| models.parent2B.negation.neither_correct | 0 |
| models.parent2B.quantity.accuracy | 0.5625 |
| models.parent2B.quantity.both_correct | 3 |
| models.parent2B.quantity.neither_correct | 1 |
| models.parent2B.time.accuracy | 0.5 |
| models.parent2B.time.both_correct | 1 |
| models.parent2B.time.neither_correct | 1 |
| references.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| references.natural100M.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.015086653002072126 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Same repeatedly inspected fixeddev96 families and one learned seed. Descriptive context response; not independent fluent continuation quality, causal diagnosis or certified10M capacity. Local generator probes remain separate." |

</details>

<details>
<summary>reports/phase6/condition_v2_calibration.json — fixed32_pending_individual_diagnosis</summary>

[原記録](../../reports/phase6/condition_v2_calibration.json) ／ SHA256: `614fa4a5a63e8d58a6f78ca2af56e7563051ba0583fd6caf45e6f880f5369978` ／ 70,741 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed32_pending_individual_diagnosis" |
| seed | 202610064 |
| seconds | 0.2221215469908202 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_v2_calibration_notes.json — None</summary>

[原記録](../../reports/phase6/condition_v2_calibration_notes.json) ／ SHA256: `37b5b49a4f3f55f5df12e9e7b4e362eca566f0c3d0f5c605e00a014c833e1fde` ／ 7,120 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition_v2_calibration_review.json — calibration_completed</summary>

[原記録](../../reports/phase6/condition_v2_calibration_review.json) ／ SHA256: `7fcd6ba14e227584f559bbd8ce38f772284f505909b64a1e24194ecb15945687` ／ 72,253 bytes

| 原キー | 保存値 |
|---|---|
| status | "calibration_completed" |
| notes_sha256 | "37b5b49a4f3f55f5df12e9e7b4e362eca566f0c3d0f5c605e00a014c833e1fde" |
| interpretation | "Train calibration used to develop rules; counts are training diagnostics, not held-out estimates. Frozen unseen40 each decide preparation readiness." |
| additional_scientific_training_tokens | 0 |
| protected_test_used | false |
| checked_at | "2026-10-05T09:52:04.175226Z" |

</details>

<details>
<summary>reports/phase6/condition_v2_completion.json — complete_authorized_four_steps_preparation_failure_branch</summary>

[原記録](../../reports/phase6/condition_v2_completion.json) ／ SHA256: `5960c2843df1cb54b0d95e38d9285df075c3540a14abb7711ef98caf883b41dc` ／ 3,016 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_authorized_four_steps_preparation_failure_branch" |
| checks.stage1_fixed32_disjoint_all_specific_notes | true |
| checks.stage1_frozen_actual_v1_v2_calibration_binding | true |
| checks.stage2_actual_builder_complete_exited_budget | true |
| checks.stage2_all_data_evidence_passed_exact_pools | true |
| checks.stage2_known_old_and_calibration_excluded_frozen | true |
| checks.stage2_all80_raw_bound_individual_notes_no_redraw | true |
| checks.stage2_actual_unchanged_preparation_conditions_failed | true |
| checks.stage3_skipped_per_preparation_failure_branch | true |
| checks.stage4_full_not_launched | true |
| checks.original10B_UI_actual_process_and_HTTP | true |
| checks.frozen_runtime_sources_preserved | true |
| checks.all_source_and_note_files_bound | true |
| checks.stage4_results_and_judgment_saved | true |
| checked_at | "2026-10-05T10:07:31.199500Z" |
| original_UI.status | "running" |
| original_UI.additional_training_tokens | 0 |
| original_UI.model.training_tokens | 10000007168 |
| original_UI.model.update | 305176 |
| original_UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| HTTP_model.training_tokens | 10000007168 |
| HTTP_model.update | 305176 |
| HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| candidate_adopted | false |

</details>

<details>
<summary>reports/phase6/condition_v2_data_review.json — evidence_audit_passed</summary>

[原記録](../../reports/phase6/condition_v2_data_review.json) ／ SHA256: `2f49b7707022b608126b3f8c5b0b4e2ca762202328f6126c16964e858ff6698e` ／ 135,690 bytes

| 原キー | 保存値 |
|---|---|
| status | "evidence_audit_passed" |
| checks.actual_builder_complete_exited_within1800 | true |
| checks.disjoint_fixed32_calibration_review_completed | true |
| checks.frozen_builder_selector_diagnosis_hashes | true |
| checks.common_pinned_train_only_whole_source_contract | true |
| checks.accepted_input_manifest_ready_hashes | true |
| checks.control_manifest_stream_index_hashes | true |
| checks.control_whole_offsets_unique_train_translation_family | true |
| checks.control_actual_whole_BOS_EOS_positions | true |
| checks.control_fixed40_random_slots_no_reroll | true |
| checks.control_all40_individual_semantic_notes | true |
| checks.control_sample0_raw_and_source_identity | true |
| checks.control_sample1_raw_and_source_identity | true |
| checks.control_sample2_raw_and_source_identity | true |
| checks.control_sample3_raw_and_source_identity | true |
| checks.control_sample4_raw_and_source_identity | true |
| checks.control_sample5_raw_and_source_identity | true |
| checks.control_sample6_raw_and_source_identity | true |
| checks.control_sample7_raw_and_source_identity | true |
| checks.control_sample8_raw_and_source_identity | true |
| checks.control_sample9_raw_and_source_identity | true |
| checks.control_sample10_raw_and_source_identity | true |
| checks.control_sample11_raw_and_source_identity | true |
| checks.control_sample12_raw_and_source_identity | true |
| checks.control_sample13_raw_and_source_identity | true |
| checks.control_sample14_raw_and_source_identity | true |
| checks.control_sample15_raw_and_source_identity | true |
| checks.control_sample16_raw_and_source_identity | true |
| checks.control_sample17_raw_and_source_identity | true |
| checks.control_sample18_raw_and_source_identity | true |
| checks.control_sample19_raw_and_source_identity | true |
| checks.control_sample20_raw_and_source_identity | true |
| checks.control_sample21_raw_and_source_identity | true |
| checks.control_sample22_raw_and_source_identity | true |
| checks.control_sample23_raw_and_source_identity | true |
| checks.control_sample24_raw_and_source_identity | true |
| checks.control_sample25_raw_and_source_identity | true |
| checks.control_sample26_raw_and_source_identity | true |
| checks.control_sample27_raw_and_source_identity | true |
| checks.control_sample28_raw_and_source_identity | true |
| checks.control_sample29_raw_and_source_identity | true |
| checks.control_sample30_raw_and_source_identity | true |
| checks.control_sample31_raw_and_source_identity | true |
| checks.control_sample32_raw_and_source_identity | true |
| checks.control_sample33_raw_and_source_identity | true |
| checks.control_sample34_raw_and_source_identity | true |
| checks.control_sample35_raw_and_source_identity | true |
| checks.control_sample36_raw_and_source_identity | true |
| checks.control_sample37_raw_and_source_identity | true |
| checks.control_sample38_raw_and_source_identity | true |
| checks.control_sample39_raw_and_source_identity | true |
| checks.control_actual_totals_match_ready | true |
| checks.refined_manifest_stream_index_hashes | true |
| checks.refined_whole_offsets_unique_train_translation_family | true |
| checks.refined_actual_whole_BOS_EOS_positions | true |
| checks.refined_fixed40_random_slots_no_reroll | true |
| checks.refined_all40_individual_semantic_notes | true |
| checks.refined_sample0_raw_and_source_identity | true |
| checks.refined_sample1_raw_and_source_identity | true |
| checks.refined_sample2_raw_and_source_identity | true |
| checks.refined_sample3_raw_and_source_identity | true |
| checks.refined_sample4_raw_and_source_identity | true |
| checks.refined_sample5_raw_and_source_identity | true |
| checks.refined_sample6_raw_and_source_identity | true |
| checks.refined_sample7_raw_and_source_identity | true |
| checks.refined_sample8_raw_and_source_identity | true |
| checks.refined_sample9_raw_and_source_identity | true |
| checks.refined_sample10_raw_and_source_identity | true |
| checks.refined_sample11_raw_and_source_identity | true |
| checks.refined_sample12_raw_and_source_identity | true |
| checks.refined_sample13_raw_and_source_identity | true |
| checks.refined_sample14_raw_and_source_identity | true |
| checks.refined_sample15_raw_and_source_identity | true |
| checks.refined_sample16_raw_and_source_identity | true |
| checks.refined_sample17_raw_and_source_identity | true |
| checks.refined_sample18_raw_and_source_identity | true |
| checks.refined_sample19_raw_and_source_identity | true |
| checks.refined_sample20_raw_and_source_identity | true |
| checks.refined_sample21_raw_and_source_identity | true |
| checks.refined_sample22_raw_and_source_identity | true |
| checks.refined_sample23_raw_and_source_identity | true |
| checks.refined_sample24_raw_and_source_identity | true |
| checks.refined_sample25_raw_and_source_identity | true |
| checks.refined_sample26_raw_and_source_identity | true |
| checks.refined_sample27_raw_and_source_identity | true |
| checks.refined_sample28_raw_and_source_identity | true |
| checks.refined_sample29_raw_and_source_identity | true |
| checks.refined_sample30_raw_and_source_identity | true |
| checks.refined_sample31_raw_and_source_identity | true |
| checks.refined_sample32_raw_and_source_identity | true |
| checks.refined_sample33_raw_and_source_identity | true |
| checks.refined_sample34_raw_and_source_identity | true |
| checks.refined_sample35_raw_and_source_identity | true |
| checks.refined_sample36_raw_and_source_identity | true |
| checks.refined_sample37_raw_and_source_identity | true |
| checks.refined_sample38_raw_and_source_identity | true |
| checks.refined_sample39_raw_and_source_identity | true |
| checks.refined_actual_totals_match_ready | true |
| checks.paired_exact_quantity_length_sequence_EOS_positions | true |
| checks.declared_length_density_overlap_recomputed | true |
| checks.unchanged_quality_interpretation_and_incomplete_audits | true |
| checks.selector_related_five_CPU_tests_pass | true |
| preparation_gates.quantity_mean_length_EOS_distribution_matched | true |
| accepted_for_experiment | false |
| summaries.control.tokens | 20000072 |
| summaries.control.documents | 71268 |
| summaries.control.body_bytes | 83690260 |
| summaries.control.body_tokens_mean | 278.6318684402537 |
| summaries.control.EOS_per_1000_tokens | 3.5633871718061814 |
| summaries.control.samples_sha256 | "7ab2938f630eda235fe131730e630dd889645c59c633a190630965c4aebd9bf1" |
| summaries.refined.tokens | 20000072 |
| summaries.refined.documents | 71268 |
| summaries.refined.body_bytes | 83216801 |
| summaries.refined.body_tokens_mean | 278.6318684402537 |
| summaries.refined.EOS_per_1000_tokens | 3.5633871718061814 |
| summaries.refined.samples_sha256 | "56ffa7ee48bfcc4a16ce28d51919553b153fdeb6ede6d6788bd94858d2b631b0" |
| notes_sha256 | "0da4bd64439ffa8ae8752bc70cf9a9566cf24b32c7bdb663288d3cb1dbb855e7" |
| source_sha256.tests/test_condition_story_quality_v2.py | "a2f007a5e8cbfaeccc45ae185835e751f7b29afe0a53782b80dac015d29a87e7" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| review_seconds | 0.7284380900091492 |
| preparation_seconds | 20.1605532829999 |
| checked_at | "2026-10-05T10:06:55.000675Z" |
| shared_documents | 10232 |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| protected_test_used | false |
| interpretation | "Same-source heuristic subset contrast; action ending/topic/dialogue composition also changes; not a semantic-quality causal certificate" |

</details>

<details>
<summary>reports/phase6/condition_v2_delivery.json — verified_delivery_before_commit</summary>

[原記録](../../reports/phase6/condition_v2_delivery.json) ／ SHA256: `2aca683282412ab33b479785e43cc80c604a28cc69440549929abb64d6c4d7ae` ／ 1,180 bytes

| 原キー | 保存値 |
|---|---|
| status | "verified_delivery_before_commit" |
| checked_at | "2026-10-05T10:07:31.4911670Z" |
| checks.all101_data_evidence | true |
| checks.both_preparation_gates_failed | true |
| checks.all13_completion_checks | true |
| checks.all80_individual_raw_notes | true |
| checks.scientific_and_verification_zero | true |
| checks.report65_binding | true |
| checks.result63_unchanged | true |
| checks.result60_unchanged | true |
| checks.execution64_contract_unchanged | true |
| checks.source_frozen_and_Windows_Linux_text_sync | true |
| checks.local_links_exist | true |
| checks.local_git_identity | true |
| completion_sha256 | "5960c2843df1cb54b0d95e38d9285df075c3540a14abb7711ef98caf883b41dc" |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| candidate_adopted | false |
| source_bytes_note | "Actual Linux frozen hashes verified; Windows normalized text agrees; historical tokenizer CRLF bytes preserved." |

</details>

<details>
<summary>reports/phase6/condition_v2_judgment.json — None</summary>

[原記録](../../reports/phase6/condition_v2_judgment.json) ／ SHA256: `a9c0ed4a0b24d9b1a26e873e10234a8df26ba374354f54cc2f85e664be748345` ／ 1,110 bytes

| 原キー | 保存値 |
|---|---|
| decision | "preparation_rejected_no_GPU" |
| failed_gates | ["candidate_weak_less_than_control", "candidate_weak_at_most10_of40"] |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| GPU_evaluation_started | false |
| candidate_adopted | false |
| interpretation | "Development calibration improvement did not transfer to the unseen fixed40 under unchanged readiness. Nonblind small samples do not establish population worsening. 100M hypothesis remains untested." |
| checked_at | "2026-10-05T10:07:31.193502Z" |

</details>

<details>
<summary>reports/phase6/condition_v2_prepare_job.json — complete</summary>

[原記録](../../reports/phase6/condition_v2_prepare_job.json) ／ SHA256: `7e9ef31d20e463bf501ecfe768ff66867b73123cbb43cc89c3d4aec587843467` ／ 12,971 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.target_tokens | 20000000 |
| binding.seed | 202610065 |
| binding.budget_seconds | 1800 |
| binding.scope | "Translation train with unchanged common base/family/local exclusion; both exclude all prior inspected/calibration rows; candidate adds frozen v2 condition and closing proxies" |
| elapsed_seconds | 20.1605532829999 |
| eligible | 106569 |
| tokens | 20000072 |
| tokens_per_pool | 20000072 |

</details>

<details>
<summary>reports/phase6/condition_v2_ready.json — ready_pending_content_review</summary>

[原記録](../../reports/phase6/condition_v2_ready.json) ／ SHA256: `111d7c57fc05011edfc1db138068cbb737a1413fb9234bd5f463da93e25988bd` ／ 38,030 bytes

| 原キー | 保存値 |
|---|---|
| status | "ready_pending_content_review" |
| binding.target_tokens | 20000000 |
| binding.seed | 202610065 |
| binding.budget_seconds | 1800 |
| binding.scope | "Translation train with unchanged common base/family/local exclusion; both exclude all prior inspected/calibration rows; candidate adds frozen v2 condition and closing proxies" |
| totals.control.tokens | 20000072 |
| totals.control.documents | 71268 |
| totals.control.body_bytes | 83690260 |
| totals.refined.tokens | 20000072 |
| totals.refined.documents | 71268 |
| totals.refined.body_bytes | 83216801 |
| supply.eligible_histogram.253 | 1520 |
| supply.eligible_histogram.191 | 371 |
| supply.eligible_histogram.291 | 1486 |
| supply.eligible_histogram.230 | 1102 |
| supply.eligible_histogram.254 | 1622 |
| supply.eligible_histogram.180 | 278 |
| supply.eligible_histogram.287 | 1493 |
| supply.eligible_histogram.224 | 1016 |
| supply.eligible_histogram.200 | 513 |
| supply.eligible_histogram.323 | 971 |
| supply.eligible_histogram.356 | 485 |
| supply.eligible_histogram.383 | 258 |
| supply.eligible_histogram.342 | 607 |
| supply.eligible_histogram.378 | 267 |
| supply.eligible_histogram.268 | 1581 |
| supply.eligible_histogram.327 | 892 |
| supply.eligible_histogram.326 | 889 |
| supply.eligible_histogram.276 | 1649 |
| supply.eligible_histogram.321 | 941 |
| supply.eligible_histogram.273 | 1662 |
| supply.eligible_histogram.366 | 365 |
| supply.eligible_histogram.336 | 730 |
| supply.eligible_histogram.304 | 1303 |
| supply.eligible_histogram.290 | 1508 |
| supply.eligible_histogram.156 | 172 |
| supply.eligible_histogram.274 | 1676 |
| supply.eligible_histogram.312 | 1140 |
| supply.eligible_histogram.188 | 341 |
| supply.eligible_histogram.292 | 1477 |
| supply.eligible_histogram.387 | 210 |
| supply.eligible_histogram.311 | 1186 |
| supply.eligible_histogram.322 | 918 |
| supply.eligible_histogram.379 | 284 |
| supply.eligible_histogram.246 | 1454 |
| supply.eligible_histogram.324 | 852 |
| supply.eligible_histogram.367 | 379 |
| supply.eligible_histogram.338 | 691 |
| supply.eligible_histogram.257 | 1625 |
| supply.eligible_histogram.293 | 1418 |
| supply.eligible_histogram.337 | 694 |
| supply.eligible_histogram.349 | 549 |
| supply.eligible_histogram.264 | 1691 |
| supply.eligible_histogram.300 | 1339 |
| supply.eligible_histogram.297 | 1345 |
| supply.eligible_histogram.218 | 865 |
| supply.eligible_histogram.244 | 1393 |
| supply.eligible_histogram.272 | 1629 |
| supply.eligible_histogram.255 | 1576 |
| supply.eligible_histogram.328 | 877 |
| supply.eligible_histogram.362 | 415 |
| supply.eligible_histogram.427 | 68 |
| supply.eligible_histogram.278 | 1622 |
| supply.eligible_histogram.234 | 1190 |
| supply.eligible_histogram.240 | 1314 |
| supply.eligible_histogram.411 | 101 |
| supply.eligible_histogram.270 | 1659 |
| supply.eligible_histogram.347 | 520 |
| supply.eligible_histogram.258 | 1622 |
| supply.eligible_histogram.186 | 332 |
| supply.eligible_histogram.265 | 1657 |
| supply.eligible_histogram.301 | 1288 |
| supply.eligible_histogram.355 | 463 |
| supply.eligible_histogram.285 | 1559 |
| supply.eligible_histogram.397 | 156 |
| supply.eligible_histogram.262 | 1597 |
| supply.eligible_histogram.249 | 1511 |
| supply.eligible_histogram.252 | 1511 |
| supply.eligible_histogram.306 | 1265 |
| supply.eligible_histogram.296 | 1423 |
| supply.eligible_histogram.334 | 760 |
| supply.eligible_histogram.198 | 448 |
| supply.eligible_histogram.250 | 1538 |
| supply.eligible_histogram.277 | 1662 |
| supply.eligible_histogram.428 | 73 |
| supply.eligible_histogram.266 | 1577 |
| supply.eligible_histogram.203 | 556 |
| supply.eligible_histogram.196 | 402 |
| supply.eligible_histogram.233 | 1205 |
| supply.eligible_histogram.314 | 1087 |
| supply.eligible_histogram.226 | 1041 |
| supply.eligible_histogram.316 | 1058 |
| supply.eligible_histogram.206 | 625 |
| supply.eligible_histogram.181 | 328 |
| supply.eligible_histogram.237 | 1234 |
| supply.eligible_histogram.205 | 597 |
| supply.eligible_histogram.239 | 1287 |
| supply.eligible_histogram.269 | 1626 |
| supply.eligible_histogram.284 | 1567 |
| supply.eligible_histogram.241 | 1322 |
| supply.eligible_histogram.229 | 1097 |
| supply.eligible_histogram.165 | 206 |
| supply.eligible_histogram.243 | 1364 |
| supply.eligible_histogram.282 | 1550 |
| supply.eligible_histogram.267 | 1673 |
| supply.eligible_histogram.238 | 1292 |
| supply.eligible_histogram.175 | 238 |
| supply.eligible_histogram.164 | 226 |
| supply.eligible_histogram.331 | 789 |
| supply.eligible_histogram.217 | 831 |
| supply.eligible_histogram.308 | 1160 |
| supply.eligible_histogram.210 | 712 |
| supply.eligible_histogram.283 | 1607 |
| supply.eligible_histogram.295 | 1397 |
| supply.eligible_histogram.280 | 1578 |
| supply.eligible_histogram.173 | 259 |
| supply.eligible_histogram.345 | 644 |
| supply.eligible_histogram.225 | 1043 |
| supply.eligible_histogram.130 | 76 |
| supply.eligible_histogram.315 | 1032 |
| supply.eligible_histogram.251 | 1538 |
| supply.eligible_histogram.193 | 411 |
| supply.eligible_histogram.471 | 14 |
| supply.eligible_histogram.256 | 1590 |
| supply.eligible_histogram.201 | 536 |
| supply.eligible_histogram.289 | 1493 |
| supply.eligible_histogram.216 | 771 |
| supply.eligible_histogram.368 | 340 |
| supply.eligible_histogram.242 | 1382 |
| supply.eligible_histogram.391 | 213 |
| supply.eligible_histogram.204 | 496 |
| supply.eligible_histogram.263 | 1610 |
| supply.eligible_histogram.319 | 953 |
| supply.eligible_histogram.310 | 1107 |
| supply.eligible_histogram.350 | 480 |
| supply.eligible_histogram.317 | 1036 |
| supply.eligible_histogram.223 | 951 |
| supply.eligible_histogram.227 | 1044 |
| supply.eligible_histogram.371 | 339 |
| supply.eligible_histogram.222 | 921 |
| supply.eligible_histogram.351 | 513 |
| supply.eligible_histogram.231 | 1188 |
| supply.eligible_histogram.430 | 60 |
| supply.eligible_histogram.302 | 1233 |
| supply.eligible_histogram.305 | 1245 |
| supply.eligible_histogram.313 | 1117 |
| supply.eligible_histogram.281 | 1563 |
| supply.eligible_histogram.360 | 420 |
| supply.eligible_histogram.418 | 103 |
| supply.eligible_histogram.161 | 184 |
| supply.eligible_histogram.359 | 467 |
| supply.eligible_histogram.228 | 1069 |
| supply.eligible_histogram.288 | 1546 |
| supply.eligible_histogram.219 | 828 |
| supply.eligible_histogram.220 | 874 |
| supply.eligible_histogram.373 | 274 |
| supply.eligible_histogram.398 | 152 |
| supply.eligible_histogram.232 | 1148 |
| supply.eligible_histogram.348 | 577 |
| supply.eligible_histogram.168 | 208 |
| supply.eligible_histogram.374 | 329 |
| supply.eligible_histogram.259 | 1606 |
| supply.eligible_histogram.271 | 1666 |
| supply.eligible_histogram.235 | 1171 |
| supply.eligible_histogram.213 | 731 |
| supply.eligible_histogram.279 | 1616 |
| supply.eligible_histogram.171 | 242 |
| supply.eligible_histogram.261 | 1562 |
| supply.eligible_histogram.158 | 182 |
| supply.eligible_histogram.215 | 728 |
| supply.eligible_histogram.139 | 97 |
| supply.eligible_histogram.152 | 130 |
| supply.eligible_histogram.386 | 213 |
| supply.eligible_histogram.187 | 337 |
| supply.eligible_histogram.208 | 616 |
| supply.eligible_histogram.143 | 111 |
| supply.eligible_histogram.248 | 1493 |
| supply.eligible_histogram.197 | 472 |
| supply.eligible_histogram.335 | 759 |
| supply.eligible_histogram.294 | 1434 |
| supply.eligible_histogram.381 | 250 |
| supply.eligible_histogram.303 | 1280 |
| supply.eligible_histogram.195 | 448 |
| supply.eligible_histogram.361 | 360 |
| supply.eligible_histogram.339 | 630 |
| supply.eligible_histogram.330 | 830 |
| supply.eligible_histogram.421 | 87 |
| supply.eligible_histogram.329 | 820 |
| supply.eligible_histogram.354 | 465 |
| supply.eligible_histogram.346 | 561 |
| supply.eligible_histogram.406 | 159 |
| supply.eligible_histogram.211 | 686 |
| supply.eligible_histogram.275 | 1616 |
| supply.eligible_histogram.343 | 618 |
| supply.eligible_histogram.392 | 176 |
| supply.eligible_histogram.182 | 328 |
| supply.eligible_histogram.167 | 211 |
| supply.eligible_histogram.214 | 745 |
| supply.eligible_histogram.146 | 124 |
| supply.eligible_histogram.184 | 349 |
| supply.eligible_histogram.245 | 1465 |
| supply.eligible_histogram.178 | 287 |
| supply.eligible_histogram.393 | 181 |
| supply.eligible_histogram.298 | 1358 |
| supply.eligible_histogram.320 | 1022 |
| supply.eligible_histogram.260 | 1684 |
| supply.eligible_histogram.325 | 873 |
| supply.eligible_histogram.382 | 256 |
| supply.eligible_histogram.434 | 53 |
| supply.eligible_histogram.353 | 496 |
| supply.eligible_histogram.365 | 358 |
| supply.eligible_histogram.236 | 1224 |
| supply.eligible_histogram.318 | 1023 |
| supply.eligible_histogram.333 | 772 |
| supply.eligible_histogram.410 | 110 |
| supply.eligible_histogram.340 | 662 |
| supply.eligible_histogram.309 | 1153 |
| supply.eligible_histogram.404 | 113 |
| supply.eligible_histogram.352 | 479 |
| supply.eligible_histogram.363 | 405 |
| supply.eligible_histogram.212 | 671 |
| supply.eligible_histogram.341 | 615 |
| supply.eligible_histogram.307 | 1183 |
| supply.eligible_histogram.194 | 419 |
| supply.eligible_histogram.447 | 35 |
| supply.eligible_histogram.394 | 171 |
| supply.eligible_histogram.183 | 317 |
| supply.eligible_histogram.299 | 1302 |
| supply.eligible_histogram.199 | 466 |
| supply.eligible_histogram.286 | 1493 |
| supply.eligible_histogram.375 | 292 |
| supply.eligible_histogram.344 | 610 |
| supply.eligible_histogram.419 | 83 |
| supply.eligible_histogram.385 | 214 |
| supply.eligible_histogram.189 | 372 |
| supply.eligible_histogram.358 | 387 |
| supply.eligible_histogram.185 | 352 |
| supply.eligible_histogram.122 | 40 |
| supply.eligible_histogram.177 | 290 |
| supply.eligible_histogram.209 | 668 |
| supply.eligible_histogram.150 | 170 |
| supply.eligible_histogram.332 | 760 |
| supply.eligible_histogram.401 | 127 |
| supply.eligible_histogram.357 | 453 |
| supply.eligible_histogram.159 | 163 |
| supply.eligible_histogram.451 | 39 |
| supply.eligible_histogram.438 | 53 |
| supply.eligible_histogram.160 | 176 |
| supply.eligible_histogram.432 | 58 |
| supply.eligible_histogram.247 | 1478 |
| supply.eligible_histogram.172 | 238 |
| supply.eligible_histogram.190 | 370 |
| supply.eligible_histogram.369 | 329 |
| supply.eligible_histogram.377 | 302 |
| supply.eligible_histogram.202 | 552 |
| supply.eligible_histogram.144 | 125 |
| supply.eligible_histogram.163 | 177 |
| supply.eligible_histogram.176 | 253 |
| supply.eligible_histogram.174 | 251 |
| supply.eligible_histogram.131 | 63 |
| supply.eligible_histogram.207 | 602 |
| supply.eligible_histogram.138 | 103 |
| supply.eligible_histogram.409 | 114 |
| supply.eligible_histogram.372 | 302 |
| supply.eligible_histogram.105 | 14 |
| supply.eligible_histogram.162 | 218 |
| supply.eligible_histogram.395 | 154 |
| supply.eligible_histogram.125 | 55 |
| supply.eligible_histogram.145 | 107 |
| supply.eligible_histogram.480 | 13 |
| supply.eligible_histogram.490 | 9 |
| supply.eligible_histogram.405 | 136 |
| supply.eligible_histogram.390 | 194 |
| supply.eligible_histogram.458 | 25 |
| supply.eligible_histogram.148 | 114 |
| supply.eligible_histogram.149 | 138 |
| supply.eligible_histogram.132 | 60 |
| supply.eligible_histogram.221 | 891 |
| supply.eligible_histogram.364 | 388 |
| supply.eligible_histogram.147 | 131 |
| supply.eligible_histogram.389 | 185 |
| supply.eligible_histogram.388 | 212 |
| supply.eligible_histogram.376 | 292 |
| supply.eligible_histogram.133 | 82 |
| supply.eligible_histogram.473 | 23 |
| supply.eligible_histogram.429 | 69 |
| supply.eligible_histogram.153 | 144 |
| supply.eligible_histogram.399 | 158 |
| supply.eligible_histogram.135 | 71 |
| supply.eligible_histogram.141 | 93 |
| supply.eligible_histogram.179 | 266 |
| supply.eligible_histogram.370 | 355 |
| supply.eligible_histogram.426 | 66 |
| supply.eligible_histogram.192 | 388 |
| supply.eligible_histogram.151 | 140 |
| supply.eligible_histogram.157 | 125 |
| supply.eligible_histogram.126 | 58 |
| supply.eligible_histogram.154 | 155 |
| supply.eligible_histogram.113 | 28 |
| supply.eligible_histogram.396 | 131 |
| supply.eligible_histogram.443 | 41 |
| supply.eligible_histogram.440 | 49 |
| supply.eligible_histogram.400 | 123 |
| supply.eligible_histogram.408 | 115 |
| supply.eligible_histogram.442 | 44 |
| supply.eligible_histogram.384 | 253 |
| supply.eligible_histogram.431 | 54 |
| supply.eligible_histogram.403 | 123 |
| supply.eligible_histogram.441 | 47 |
| supply.eligible_histogram.380 | 248 |
| supply.eligible_histogram.121 | 34 |
| supply.eligible_histogram.475 | 16 |
| supply.eligible_histogram.170 | 214 |
| supply.eligible_histogram.169 | 205 |
| supply.eligible_histogram.423 | 76 |
| supply.eligible_histogram.511 | 9 |
| supply.eligible_histogram.407 | 142 |
| supply.eligible_histogram.414 | 98 |
| supply.eligible_histogram.457 | 35 |
| supply.eligible_histogram.422 | 72 |
| supply.eligible_histogram.487 | 11 |
| supply.eligible_histogram.140 | 98 |
| supply.eligible_histogram.413 | 111 |
| supply.eligible_histogram.116 | 34 |
| supply.eligible_histogram.402 | 114 |
| supply.eligible_histogram.476 | 13 |
| supply.eligible_histogram.425 | 60 |
| supply.eligible_histogram.412 | 106 |
| supply.eligible_histogram.166 | 215 |
| supply.eligible_histogram.104 | 17 |
| supply.eligible_histogram.459 | 20 |
| supply.eligible_histogram.420 | 70 |
| supply.eligible_histogram.91 | 4 |
| supply.eligible_histogram.491 | 9 |
| supply.eligible_histogram.424 | 73 |
| supply.eligible_histogram.127 | 62 |
| supply.eligible_histogram.466 | 16 |
| supply.eligible_histogram.136 | 71 |
| supply.eligible_histogram.464 | 21 |
| supply.eligible_histogram.456 | 39 |
| supply.eligible_histogram.416 | 91 |
| supply.eligible_histogram.155 | 152 |
| supply.eligible_histogram.453 | 34 |
| supply.eligible_histogram.114 | 29 |
| supply.eligible_histogram.119 | 30 |
| supply.eligible_histogram.461 | 20 |
| supply.eligible_histogram.142 | 107 |
| supply.eligible_histogram.446 | 44 |
| supply.eligible_histogram.455 | 27 |
| supply.eligible_histogram.436 | 52 |
| supply.eligible_histogram.445 | 34 |
| supply.eligible_histogram.505 | 5 |
| supply.eligible_histogram.437 | 52 |
| supply.eligible_histogram.118 | 39 |
| supply.eligible_histogram.463 | 31 |
| supply.eligible_histogram.115 | 29 |
| supply.eligible_histogram.109 | 21 |
| supply.eligible_histogram.117 | 42 |
| supply.eligible_histogram.108 | 19 |
| supply.eligible_histogram.123 | 37 |
| supply.eligible_histogram.433 | 66 |
| supply.eligible_histogram.481 | 14 |
| supply.eligible_histogram.107 | 18 |
| supply.eligible_histogram.435 | 58 |
| supply.eligible_histogram.128 | 67 |
| supply.eligible_histogram.112 | 18 |
| supply.eligible_histogram.452 | 39 |
| supply.eligible_histogram.439 | 42 |
| supply.eligible_histogram.467 | 20 |
| supply.eligible_histogram.134 | 95 |
| supply.eligible_histogram.465 | 20 |
| supply.eligible_histogram.417 | 97 |
| supply.eligible_histogram.484 | 12 |
| supply.eligible_histogram.124 | 45 |
| supply.eligible_histogram.137 | 95 |
| supply.eligible_histogram.488 | 10 |
| supply.eligible_histogram.100 | 13 |
| supply.eligible_histogram.103 | 19 |
| supply.eligible_histogram.93 | 5 |
| supply.eligible_histogram.507 | 4 |
| supply.eligible_histogram.106 | 18 |
| supply.eligible_histogram.415 | 85 |
| supply.eligible_histogram.474 | 17 |
| supply.eligible_histogram.129 | 66 |
| supply.eligible_histogram.444 | 42 |
| supply.eligible_histogram.450 | 41 |
| supply.eligible_histogram.448 | 39 |
| supply.eligible_histogram.96 | 12 |
| supply.eligible_histogram.468 | 16 |
| supply.eligible_histogram.89 | 3 |
| supply.eligible_histogram.478 | 13 |
| supply.eligible_histogram.486 | 7 |
| supply.eligible_histogram.477 | 19 |
| supply.eligible_histogram.460 | 24 |
| supply.eligible_histogram.489 | 10 |
| supply.eligible_histogram.469 | 19 |
| supply.eligible_histogram.454 | 36 |
| supply.eligible_histogram.503 | 6 |
| supply.eligible_histogram.479 | 14 |
| supply.eligible_histogram.485 | 9 |
| supply.eligible_histogram.92 | 4 |
| supply.eligible_histogram.110 | 15 |
| supply.eligible_histogram.512 | 1 |
| supply.eligible_histogram.492 | 3 |
| supply.eligible_histogram.111 | 23 |
| supply.eligible_histogram.509 | 7 |
| supply.eligible_histogram.86 | 6 |
| supply.eligible_histogram.449 | 49 |
| supply.eligible_histogram.495 | 5 |
| supply.eligible_histogram.504 | 3 |
| supply.eligible_histogram.102 | 10 |
| supply.eligible_histogram.95 | 7 |
| supply.eligible_histogram.101 | 12 |
| supply.eligible_histogram.482 | 9 |
| supply.eligible_histogram.120 | 34 |
| supply.eligible_histogram.462 | 21 |
| supply.eligible_histogram.98 | 6 |
| supply.eligible_histogram.496 | 12 |
| supply.eligible_histogram.499 | 8 |
| supply.eligible_histogram.472 | 18 |
| supply.eligible_histogram.85 | 3 |
| supply.eligible_histogram.500 | 8 |
| supply.eligible_histogram.94 | 4 |
| supply.eligible_histogram.99 | 6 |
| supply.eligible_histogram.75 | 1 |
| supply.eligible_histogram.498 | 6 |
| supply.eligible_histogram.502 | 10 |
| supply.eligible_histogram.97 | 9 |
| supply.eligible_histogram.501 | 7 |
| supply.eligible_histogram.506 | 5 |
| supply.eligible_histogram.470 | 15 |
| supply.eligible_histogram.88 | 1 |
| supply.eligible_histogram.87 | 3 |
| supply.eligible_histogram.78 | 2 |
| supply.eligible_histogram.84 | 2 |
| supply.eligible_histogram.493 | 5 |
| supply.eligible_histogram.510 | 3 |
| supply.eligible_histogram.83 | 3 |
| supply.eligible_histogram.483 | 6 |
| supply.eligible_histogram.90 | 6 |
| supply.eligible_histogram.497 | 4 |
| supply.eligible_histogram.508 | 1 |
| supply.eligible_histogram.79 | 3 |
| supply.eligible_histogram.70 | 1 |
| supply.eligible_histogram.494 | 3 |
| supply.eligible_histogram.82 | 1 |
| supply.eligible_histogram.76 | 1 |
| supply.eligible_tokens | 58421317 |
| supply.target_tokens | 20000000 |
| supply.possible_tokens | 20000072 |
| body_tokens_mean | 278.6318684402537 |
| EOS_per_1000_tokens | 3.5633871718061814 |
| matched_quantity_length_sequence_EOS_positions | true |
| official_validation_test_acquired | false |
| control_candidate_shared_documents | 10232 |
| interpretation | "Same-source heuristic subset contrast; action ending/topic/dialogue composition also changes; not a semantic-quality causal certificate" |
| seconds | 20.159706099992036 |

</details>

<details>
<summary>reports/phase6/conditional-content-pilot-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/conditional-content-pilot-20261006/content-notes.json) ／ SHA256: `ddc77c826394de03051720b682787c4da0add70713b9dcca386ba0116af31c7f` ／ 30,393 bytes

| 原キー | 保存値 |
|---|---|
| sample_sha256 | "9b6e4d04cf5062054b360b417ad36c98f50ea9d36902dcf6fb3cf09e41963f9f" |
| interpretation | "Inspection only; no new quality thresholds or training-pool acceptance. Potential issues are local nonblind observations, not external factual certification. Normal creative stories and descriptive text are not weak merely for lacking contrastive conditions." |

</details>

<details>
<summary>reports/phase6/conditional-content-pilot-20261006/content-review.json — all96_normalized_train_content_observations_complete</summary>

[原記録](../../reports/phase6/conditional-content-pilot-20261006/content-review.json) ／ SHA256: `4d3e0344c36fcbf1bbc383dbc29a1b0e848b952b3e2946dd0e67330a8cc6a2aa` ／ 2,846 bytes

| 原キー | 保存値 |
|---|---|
| status | "all96_normalized_train_content_observations_complete" |
| summary.story.documents | 32 |
| summary.story.grammar2 | 31 |
| summary.textbook.documents | 32 |
| summary.textbook.grammar2 | 32 |
| summary.web.documents | 32 |
| summary.web.grammar2 | 29 |
| sample_sha256 | "9b6e4d04cf5062054b360b417ad36c98f50ea9d36902dcf6fb3cf09e41963f9f" |
| notes_sha256 | "ddc77c826394de03051720b682787c4da0add70713b9dcca386ba0116af31c7f" |
| training_pool_accepted | false |
| newly_prepared_tokens | 0 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| conclusion | "Causal/outcome stories are present and mostly locally coherent; the sample does not support calling all training material broken. Explicit alternate conditions with different outcomes are a smaller subset. Next inspect bounded source-grounded paired supply before selecting a conditional-discrimination learning comparison." |
| limitations | "Fixed32/source,64..512 tokens, nonblind observations; category absence is not poor text. Local text-internal relation and possible factual/introductory issues are distinct. No whole-corpus prevalence, source-family independence, factual truth or model-capacity proof. No acceptance criterion changed." |

</details>

<details>
<summary>reports/phase6/conditional-content-pilot-20261006/result.json — fixed96_train_content_inspection_ready_unreviewed</summary>

[原記録](../../reports/phase6/conditional-content-pilot-20261006/result.json) ／ SHA256: `ea665cc37645a3a99b1171596b67d0669a96b3b02577b3c09c2c37caf514019c` ／ 2,036 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed96_train_content_inspection_ready_unreviewed" |
| CPU_seconds | 0.45141482999315485 |
| CPU_ceiling_seconds | 30 |
| seed | 2026100643 |
| documents | 96 |
| source_documents.web | 32 |
| source_documents.story | 32 |
| source_documents.textbook | 32 |
| body_tokens | 11984 |
| body_bytes | 49645 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| sample_sha256 | "9b6e4d04cf5062054b360b417ad36c98f50ea9d36902dcf6fb3cf09e41963f9f" |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_tokens | 0 |
| content_acceptance_complete | false |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| completion_condition | "Personally read all96 normalized train documents and record grammatical completeness, explicit negation/quantity/time/comparison/entity/causal conditions and outcome links. Distinguish absent conditions from broken conditions. Select one supported train-only comparison or record insufficient evidence; never use dev prompts as training examples." |
| limitations | "Uniform document draws restricted to64..512 body tokens and fixed32/source. Decoded normalized train bodies, not raw original source bytes. This small nonblind inspection cannot estimate whole-corpus quality, distinct source-family supply or global deduplication. No new data or GPU learning." |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/compare-result.json — masked_suffix_GPU_complete_pending_all80_content_review</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/compare-result.json) ／ SHA256: `f27236c59a63cdd95470c894b4774e98b65c8a39dbc6e259be85548227110811` ／ 555,424 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| checkpoint.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checkpoint.binding.config_sha256 | "0a363551b149a330ce2a92851baa4057eeede146ef0505e384bef8931a831aab" |
| checkpoint.binding.arm | "outcome_EOS_only" |
| checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323185.pt" |
| checkpoint.binding.parent.sha256 | "ad4747898bc6492e1165edee6b870b09c8be9be944e03a9e4450fde406cb3f34" |
| checkpoint.binding.study_kind | "original_staged_suffix_conditional_prefix_mask_v1" |
| checkpoint.binding.teacher_goals.web | 75000000 |
| checkpoint.binding.teacher_goals.story | 5000000 |
| checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint.binding.target_rule | "conditional outcome+EOS only; original reference quotas stop input" |
| checkpoint.binding.optimizer_policy | "inherit" |
| checkpoint.binding.peak_lr | 1e-05 |
| checkpoint.updates | 318 |
| checkpoint.additional_supervised_tokens | 1801392 |
| checkpoint.additional_input_tokens | 10420224 |
| checkpoint.actual_body_bytes | 6695119 |
| checkpoint.reference_suffix_teacher_tokens | 10159637 |
| checkpoint.actual_source_accounting.teachers.web | 0 |
| checkpoint.actual_source_accounting.teachers.story | 0 |
| checkpoint.actual_source_accounting.teachers.ordinary_textbook | 159637 |
| checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| checkpoint.actual_source_accounting.eos.web | 0 |
| checkpoint.actual_source_accounting.eos.story | 0 |
| checkpoint.actual_source_accounting.eos.ordinary_textbook | 1202 |
| checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| checkpoint.actual_source_accounting.body_bytes.web | 0 |
| checkpoint.actual_source_accounting.body_bytes.story | 0 |
| checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| checkpoint.actual_source_accounting.focus.web | 0 |
| checkpoint.actual_source_accounting.focus.story | 0 |
| checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.kind | "same-streams-staged-source-order-v1" |
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
| checkpoint.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 159637 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 1202 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 680306 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "same-streams-staged-source-order-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 2750 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10327318 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 38243 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 87 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 72981 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 147 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 9840363 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 159170 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 38240 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 72981 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 75159552 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 5039104 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 9913344 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 292149840 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 20452979 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 42059165 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "c5731598e03dc91f7936673de06845eb53faf096030791578799fc99201f5c6f" |
| checkpoint.token_digest | "129220e93aed4e2e31b67a9daefab3af9585bc905502ec0f42a859986922a2b6" |
| checkpoint.reference_token_digest | "c5731598e03dc91f7936673de06845eb53faf096030791578799fc99201f5c6f" |
| checkpoint.training_seconds | 18.131375385826686 |
| evaluation.binding.teacher_goals.web | 75000000 |
| evaluation.binding.teacher_goals.story | 5000000 |
| evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluation.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| evaluation.body.documents | 256 |
| evaluation.body.limit_documents | 256 |
| evaluation.body.body_nll | 355608.9075078964 |
| evaluation.body.eos_nll | 263.3683707138989 |
| evaluation.body.body_bytes | 472055 |
| evaluation.body.body_tokens | 122343 |
| evaluation.body.bpb | 1.0868123573684936 |
| evaluation.body.seconds | 1.4028304950043093 |
| evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluation.generation.max_new_tokens | 64 |
| evaluation.greedy_rates.eos | 79 |
| evaluation.greedy_rates.repetition | 1 |
| evaluation.greedy_rates.unicode_failure | 0 |
| evaluation.greedy_rates.role_leak | 0 |
| evaluation.greedy_rates.empty | 0 |
| evaluation.diagnostics.semantics.primary.accuracy.point | 0.6145833333333334 |
| evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6145833333333334 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6145833333333334] |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5781135555977539 |
| evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.15625847779496568 |
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
| evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7583081570996979 |
| evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7129909365558912, 0.8036253776435045] |
| evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7583081570996979 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
| evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| evaluation.diagnostics.jcqa.primary.accuracy.point | 0.291331546023235 |
| evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.26541554959785524, 0.31637622877569244] |
| evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.27658623771224305 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.3033958891867739] |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2770330652368186 |
| evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2761556488098438 |
| evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.09662606000210362 |
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
| evaluation.diagnostics.semantic_both_contexts.correct | 25 |
| evaluation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluation.protected_test_used | false |
| bridge.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| bridge.checks.weights_unchanged | true |
| bridge.checks.no_gradients | true |
| bridge.checks.eval_mode | true |
| bridge.checks.RNG_restored | true |
| bridge.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| bridge.summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.70703125 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 21 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.46875 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 14 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7109375 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 15 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| bridge.optimizer_updates | 0 |
| bridge.scientific_teacher_tokens | 0 |
| bridge.protected_test_used | false |
| bridge.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| retention.checks.weights_unchanged | true |
| retention.checks.no_gradients | true |
| retention.checks.eval_mode | true |
| retention.checks.RNG_restored | true |
| retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 64 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 16 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.75390625 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 57 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 49 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 15 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.74609375 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 66 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 59 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.625 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.optimizer_updates | 0 |
| retention.scientific_teacher_tokens | 0 |
| retention.protected_test_used | false |
| retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| scientific_teacher_tokens | 1801392 |
| scientific_optimizer_updates | 318 |
| matched_teacher_budget | false |
| status | "masked_suffix_GPU_complete_pending_all80_content_review" |
| GPU_seconds | 50.63884665700607 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/content-notes.json) ／ SHA256: `8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613` ／ 24,260 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/body.json) ／ SHA256: `897e349c27f891502ddbddbfe3a68c7cc4b64e568a4ba53baa9992e129ec2628` ／ 67,183 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 355608.9075078964 |
| body.eos_nll | 263.3683707138989 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0868123573684936 |
| body.seconds | 1.4028304950043093 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json) ／ SHA256: `dd966fb8ca316e9f51ee1395b8902fccb4845f43fb940aa09a35c7ee7fd08c5a` ／ 50,283 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jblimp.json) ／ SHA256: `e3d3130476757fd5189831eac9203c0d96ffc99035066f7f35c0ce4ed5162af0` ／ 338,266 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7583081570996979 |
| summary.primary.accuracy.ci95 | [0.7129909365558912, 0.8036253776435045] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7583081570996979 |
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
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jcqa.json) ／ SHA256: `e15b8a078132d84c7203afe0314e5dc17d41dad03bc9a2da1336dd72d49f3c46` ／ 1,641,835 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.291331546023235 |
| summary.primary.accuracy.ci95 | [0.26541554959785524, 0.31637622877569244] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.291331546023235 |
| summary.per_token_secondary.accuracy.point | 0.27658623771224305 |
| summary.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.3033958891867739] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.2770330652368186 |
| summary.per_token_secondary.macro_f1 | 0.2761556488098438 |
| summary.per_token_secondary.mcc | 0.09662606000210362 |
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
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/result.json) ／ SHA256: `cf853457f80a95ae6e4eb5164b7b0c2f7c70ae217aeca6e9fa8638694dc57ded` ／ 140,105 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 355608.9075078964 |
| body.eos_nll | 263.3683707138989 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0868123573684936 |
| body.seconds | 1.4028304950043093 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 79 |
| greedy_rates.repetition | 1 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.6145833333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6145833333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5781135555977539 |
| diagnostics.semantics.per_token_secondary.mcc | 0.15625847779496568 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7583081570996979 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7129909365558912, 0.8036253776435045] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7583081570996979 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| diagnostics.jcqa.primary.accuracy.point | 0.291331546023235 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.26541554959785524, 0.31637622877569244] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.27658623771224305 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.3033958891867739] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2770330652368186 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2761556488098438 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.09662606000210362 |
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
| diagnostics.semantic_both_contexts.correct | 25 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/semantics.json) ／ SHA256: `4b7571f44a05e4799dc6ca30d86b5aa27eaadcf75dfc88dbddc89b0d0aecbccc` ／ 202,951 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.6145833333333334 |
| summary.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.6145833333333334 |
| summary.per_token_secondary.accuracy.point | 0.578125 |
| summary.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6145833333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.578125 |
| summary.per_token_secondary.macro_f1 | 0.5781135555977539 |
| summary.per_token_secondary.mcc | 0.15625847779496568 |
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
<summary>reports/phase6/conditional-prefix-mask-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/job.json) ／ SHA256: `c742c30061ed5038d316e9d3b54079c4c771b58ca22d9b36cf5bd4fc50450f5e` ／ 802 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 50.63884665700607 |
| completed_updates | 300 |
| total_updates | 318 |
| actual_teachers | 1710803 |
| reference_teachers | 9606866 |
| loss | 0.06465114653110504 |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/latest.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/latest.json) ／ SHA256: `5adae3a062451d6e77c90991552a392d873cfb8e3cf852556325c39d39e90d37` ／ 288 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/probe/job.json) ／ SHA256: `4b68392e85addf4b395ca943566a38352889d4e4557a0e89a8de23019d1d569c` ／ 542 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 17.082726756983902 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/probe/result.json — own_masked_CUDA_probe_complete</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/probe/result.json) ／ SHA256: `4a8836858de3de36e91866c537c7ce009849d294301fb7eef0196b8177c46386` ／ 179,337 bytes

| 原キー | 保存値 |
|---|---|
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
| gate.checks.history_lr | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_outcome_weight | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_actual_source_routes | true |
| gate.checks.history_physical_input_tokens | true |
| gate.checks.history_removed_prefix_targets | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_loss | true |
| gate.checks.history_valid_input_tokens | true |
| gate.checks.history_body_bytes_seen | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_additional_teacher_tokens | true |
| gate.checks.history_reference_token_digest | true |
| gate.checks.history_actual_source_body_bytes | true |
| gate.checks.history_actual_source_teachers | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_actual_source_eos | true |
| gate.checks.history_supervised_tokens | true |
| gate.checks.history_tokens_seen | true |
| gate.checks.history_reference_suffix_teacher_tokens | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_update | true |
| gate.checks.history_token_digest | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.checks.transition_included | true |
| gate.checks.actual_conditional_mask_active | true |
| gate.GPU_optimizer_updates | 16 |
| gate.verification_teacher_tokens | 351618 |
| timing.verification_teacher_tokens | 301867 |
| timing.terminal_save_seconds | 0.1751469390001148 |
| timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint.sha256 | "a1f7f14ad46ef7c2590da344358a0f0be6c913ba38f3823b6a8f5458de8f1544" |
| timing.peak_VRAM_bytes | 6149106176 |
| passed | true |
| GPU_optimizer_updates | 48 |
| verification_teacher_tokens | 653485 |
| scientific_teacher_tokens | 0 |
| status | "own_masked_CUDA_probe_complete" |
| GPU_seconds | 17.082726756983902 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json) ／ SHA256: `f30b45ad19decd079082b1779bde955715a99d3e9fdaf3e6ef4f2fbe9c1cc36d` ／ 266 bytes

| 原キー | 保存値 |
|---|---|
| update | 323217 |
| tokens_seen | 10591174656 |

</details>
