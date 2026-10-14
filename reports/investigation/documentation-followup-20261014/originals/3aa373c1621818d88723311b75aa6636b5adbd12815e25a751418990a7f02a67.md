# 評価・生成・意味診断 — 10/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition_diversity_comparison_completion.json — actual_nested2048_25M_and_all160_content_complete_Base_unmet</summary>

[原記録](../../reports/phase6/condition_diversity_comparison_completion.json) ／ SHA256: `676bd6f9a8a5d43f4c01bdd49ef927d84f57c61d90779210f1a47b0c3dfa6c9b` ／ 6,980 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_nested2048_25M_and_all160_content_complete_Base_unmet" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 113.42645317898132 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 24696536 |
| job.teacher_budget | 25000000 |
| job.source_teachers.web | 18521779 |
| job.source_teachers.story | 1234792 |
| job.source_teachers.ordinary_textbook | 2469974 |
| job.source_teachers.conditional_textbook | 2469991 |
| job.loss | 2.6440489292144775 |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| total_comparison_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1299890 |
| new_scientific_input_tokens | 25231360 |
| new_checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-diversity-comparison-20261006/large2048/training/checkpoint-00062936.pt" |
| new_checkpoint.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| new_checkpoint.binding.config_sha256 | "87b4ed4070fb92d5c97ffbb9563d20ad3d649414d81c11426cabe0540a7f80d0" |
| new_checkpoint.binding.arm | "large2048" |
| new_checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| new_checkpoint.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| new_checkpoint.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| new_checkpoint.binding.teacher_goals.web | 18750000 |
| new_checkpoint.binding.teacher_goals.story | 1250000 |
| new_checkpoint.binding.teacher_goals.ordinary_textbook | 2500000 |
| new_checkpoint.binding.teacher_goals.conditional_textbook | 2500000 |
| new_checkpoint.binding.optimizer_policy | "inherit" |
| new_checkpoint.binding.peak_lr | 0.0002 |
| new_checkpoint.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| new_checkpoint.binding.study_kind | "nested_condition_source_quantity" |
| new_checkpoint.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| new_checkpoint.binding.outcome_weight | 1 |
| new_checkpoint.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| new_checkpoint.update | 62936 |
| new_checkpoint.tokens | 2062286848 |
| new_checkpoint.supervised_tokens | 2045000000 |
| new_checkpoint.additional_supervised_tokens | 25000000 |
| new_checkpoint.additional_input_tokens | 25231360 |
| new_checkpoint.source_teachers.web | 18750000 |
| new_checkpoint.source_teachers.story | 1250000 |
| new_checkpoint.source_teachers.ordinary_textbook | 2500000 |
| new_checkpoint.source_teachers.conditional_textbook | 2500000 |
| new_checkpoint.source_eos.web | 164131 |
| new_checkpoint.source_eos.story | 9486 |
| new_checkpoint.source_eos.ordinary_textbook | 18576 |
| new_checkpoint.source_eos.conditional_textbook | 17514 |
| new_checkpoint.source_input_tokens.web | 18934784 |
| new_checkpoint.source_input_tokens.story | 1259520 |
| new_checkpoint.source_input_tokens.ordinary_textbook | 2519040 |
| new_checkpoint.source_input_tokens.conditional_textbook | 2518016 |
| new_checkpoint.source_focus_teachers.web | 0 |
| new_checkpoint.source_focus_teachers.story | 0 |
| new_checkpoint.source_focus_teachers.ordinary_textbook | 0 |
| new_checkpoint.source_focus_teachers.conditional_textbook | 654871 |
| new_checkpoint.focus_teacher_tokens | 654871 |
| new_checkpoint.focus_token_digest | "45d496b8d5bb369188109cec511fa64f1340374be30badaf9bce3ad77036f014" |
| new_checkpoint.weighted_teacher_mass | 25000000 |
| new_checkpoint.outcome_weight | 1 |
| new_checkpoint.training_seconds | 39.85271529221791 |
| new_checkpoint.completed_at | "2026-10-06T02:06:47.967298Z" |
| actual_scientific_GPU_seconds | 113.42645317898132 |
| actual_probe_GPU_seconds | 11.799473121995106 |
| actual_total_GPU_seconds | 125.22592630097643 |
| GPU_ceiling_seconds | 900 |
| portable_text_bytes | 6503493 |
| UI_server.status | "running" |
| UI_server.additional_training_tokens | 0 |
| UI_server.model.training_tokens | 10000007168 |
| UI_server.model.update | 305176 |
| UI_server.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_server.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_server.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| UI_HTTP.training_tokens | 10000007168 |
| UI_HTTP.update | 305176 |
| UI_HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_diversity_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_diversity_comparison_evidence_manifest.json) ／ SHA256: `fada5d46b25e0e113a4688ef09012e7ca68124c7d45aeee4052fc49ac51b04c3` ／ 21,565 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 6503493 |
| archive.bytes | 1604972 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_diversity_comparison_proposal.json — actual_nested2048_source_and_all64_content_and_IDs_prepared_GPU_comparison_not_implemented_not_started</summary>

[原記録](../../reports/phase6/condition_diversity_comparison_proposal.json) ／ SHA256: `21718a8a6cd69240c9d740f4fbd456da29899358760d63c86effbb186913609d` ／ 3,953 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_nested2048_source_and_all64_content_and_IDs_prepared_GPU_comparison_not_implemented_not_started" |
| small_documents | 512 |
| large_target_documents | 2048 |
| CPU_preparation.seed | 2026100654 |
| CPU_preparation.seconds_limit | 240 |
| CPU_preparation.draw_limit | 32000000 |
| CPU_preparation.new_content_pilot | "first64 added rows512..575" |
| CPU_preparation.weak_limit | 10 |
| CPU_preparation.automatic_reroll | false |
| learning.parent_teachers | 2020000000 |
| learning.additional_teachers_each | 25000000 |
| learning.seed | 42 |
| control_reuse.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| control_reuse.teacher_tokens | 25000000 |
| control_reuse.content_notes | "reports/phase6/condition_positive_control_notes.json" |
| new_scientific_teachers | 25000000 |
| total_comparison_teachers | 50000000 |
| new_original_corpus_tokens | 0 |
| GPU_ceiling_seconds | 900 |
| GPU_freeze_condition | "Adequate accepted supply; real continuous4 vs2+2 fullstate resume and continuous timing; measured training+checkpoint+evaluation margin fits cap before science config" |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| teacher_preparation | "reports/phase6/condition_diversity_teacher_preparation.json" |

</details>

<details>
<summary>reports/phase6/condition_diversity_comparison_review.json — nested512_vs2048_same25M_actual_all160_content_complete</summary>

[原記録](../../reports/phase6/condition_diversity_comparison_review.json) ／ SHA256: `dc068ee587688a8d110fc8db59a18a5d0a78d9439f70a43476b1be712ddcf3a7` ／ 4,440 bytes

| 原キー | 保存値 |
|---|---|
| status | "nested512_vs2048_same25M_actual_all160_content_complete" |
| summaries.control.BPB | 1.1435587102961566 |
| summaries.control.rates.eos | 44 |
| summaries.control.rates.repetition | 26 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 54 |
| summaries.control.relevance2 | 43 |
| summaries.control.coherent | 15 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 25000000 |
| summaries.control.source_teacher_tokens.web | 18750000 |
| summaries.control.source_teacher_tokens.story | 1250000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.control.focus_teacher_tokens | 654588 |
| summaries.control.weighted_teacher_mass | 25000000 |
| summaries.control.notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| summaries.control.Base_adopted | false |
| summaries.large2048.BPB | 1.1401491842426266 |
| summaries.large2048.rates.eos | 42 |
| summaries.large2048.rates.repetition | 23 |
| summaries.large2048.rates.unicode_failure | 0 |
| summaries.large2048.rates.role_leak | 0 |
| summaries.large2048.rates.empty | 0 |
| summaries.large2048.grammar2 | 59 |
| summaries.large2048.relevance2 | 50 |
| summaries.large2048.coherent | 16 |
| summaries.large2048.appropriate | 27 |
| summaries.large2048.new_teacher_tokens | 25000000 |
| summaries.large2048.source_teacher_tokens.web | 18750000 |
| summaries.large2048.source_teacher_tokens.story | 1250000 |
| summaries.large2048.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.large2048.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.large2048.conditional_source_documents | 2048 |
| summaries.large2048.notes_sha256 | "166bae110c256cce316fdff557d05b7f9bceb61383c176c6037fd47d1a33ad34" |
| summaries.large2048.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.control.grammar_at_least56 | false |
| absolute_dev_screen.control.coherence_at_least27 | false |
| absolute_dev_screen.control.appropriate_at_least27 | true |
| absolute_dev_screen.control.EOS_at_least37 | true |
| absolute_dev_screen.control.repetition_at_most18 | false |
| absolute_dev_screen.control.no_empty_role_unicode | true |
| absolute_dev_screen.large2048.grammar_at_least56 | true |
| absolute_dev_screen.large2048.coherence_at_least27 | false |
| absolute_dev_screen.large2048.appropriate_at_least27 | true |
| absolute_dev_screen.large2048.EOS_at_least37 | true |
| absolute_dev_screen.large2048.repetition_at_most18 | false |
| absolute_dev_screen.large2048.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.large2048.EOS_at_least8_more | true |
| original_Web.large2048.repetition_no_worse | true |
| original_Web.large2048.no_empty_role_unicode | true |
| original_Web.large2048.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.large2048 | false |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| total_comparison_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1299890 |
| GPU_seconds | 113.42645317898132 |
| verification_GPU_seconds | 11.799473121995106 |
| ordinary_stream_checks.target_sha256 | true |
| ordinary_stream_checks.teachers | true |
| ordinary_stream_checks.EOS | true |
| ordinary_stream_checks.body_bytes | true |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/condition_diversity_condition_pair_analysis.json — completed_nested_source_fixed_dev_condition_pair_analysis</summary>

[原記録](../../reports/phase6/condition_diversity_condition_pair_analysis.json) ／ SHA256: `a589905b7a29e7ffddafe94d6c2a75b3bf8cabf5ac33762f86090428cfa8fe17` ／ 186,067 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_nested_source_fixed_dev_condition_pair_analysis" |
| models.control.causality.accuracy | 0.5625 |
| models.control.causality.both_correct | 2 |
| models.control.causality.neither_correct | 0 |
| models.control.comparison.accuracy | 0.5 |
| models.control.comparison.both_correct | 0 |
| models.control.comparison.neither_correct | 0 |
| models.control.coreference.accuracy | 0.4375 |
| models.control.coreference.both_correct | 0 |
| models.control.coreference.neither_correct | 2 |
| models.control.negation.accuracy | 0.5 |
| models.control.negation.both_correct | 0 |
| models.control.negation.neither_correct | 0 |
| models.control.quantity.accuracy | 0.5625 |
| models.control.quantity.both_correct | 3 |
| models.control.quantity.neither_correct | 1 |
| models.control.time.accuracy | 0.59375 |
| models.control.time.both_correct | 3 |
| models.control.time.neither_correct | 0 |
| models.large2048.causality.accuracy | 0.65625 |
| models.large2048.causality.both_correct | 5 |
| models.large2048.causality.neither_correct | 0 |
| models.large2048.comparison.accuracy | 0.5 |
| models.large2048.comparison.both_correct | 0 |
| models.large2048.comparison.neither_correct | 0 |
| models.large2048.coreference.accuracy | 0.46875 |
| models.large2048.coreference.both_correct | 0 |
| models.large2048.coreference.neither_correct | 1 |
| models.large2048.negation.accuracy | 0.5 |
| models.large2048.negation.both_correct | 0 |
| models.large2048.negation.neither_correct | 0 |
| models.large2048.quantity.accuracy | 0.5625 |
| models.large2048.quantity.both_correct | 3 |
| models.large2048.quantity.neither_correct | 1 |
| models.large2048.time.accuracy | 0.5625 |
| models.large2048.time.both_correct | 2 |
| models.large2048.time.neither_correct | 0 |
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
| references.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| references.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| pair_analysis_source_sha256 | "77ef1b192b4b507c60c1d2a560b43ef282925cf5c4bae66dc8158073e854e126" |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |
| CPU_seconds | 0.011879584984853864 |
| limitations | "Same fixed96 dev families, one learned seed; descriptive ranking/context sensitivity, not independent generalization, fluent generation, attention failure or capacity proof. No dev texts enter learning; source quantity comparison uses existing train only." |

</details>

<details>
<summary>reports/phase6/condition_diversity_large2048_notes.json — None</summary>

[原記録](../../reports/phase6/condition_diversity_large2048_notes.json) ／ SHA256: `166bae110c256cce316fdff557d05b7f9bceb61383c176c6037fd47d1a33ad34` ／ 17,640 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition_positive_active_job.json — None</summary>

[原記録](../../reports/phase6/condition_positive_active_job.json) ／ SHA256: `4d0bf640f3e854657fbbfa00db980f602a24dee4b2db46c3a14619d10ec03b6c` ／ 7,772 bytes

| 原キー | 保存値 |
|---|---|
| user_scope | "Base only; notify and stop upon actual Base completion; no Chat/quantization" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 224.40080486799707 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 24696377 |
| job.teacher_budget | 25000000 |
| job.source_teachers.web | 18521779 |
| job.source_teachers.story | 1234792 |
| job.source_teachers.ordinary_textbook | 2469974 |
| job.source_teachers.conditional_textbook | 2469832 |
| job.loss | 2.3950376510620117 |
| scientific_config | "configs/phase6/condition_positive_comparison.json" |
| actual_probe_GPU_seconds | 22.01919901598012 |
| verification_teacher_tokens | 2599740 |
| actual_probe_both32checks_passed | true |
| scientific_teacher_budget | 50000000 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| note | "Scientific job complete and PID522579 absent; terminal checkpoints are authoritative25M per arm, job teacher heartbeat is historical. Do not restart a complete job. Base quality unmet; original10B UI523067 restored and HTTP checkpoint verified." |
| scientific_job_live | false |
| terminal_checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/control/training/checkpoint-00062936.pt" |
| terminal_checkpoints.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| terminal_checkpoints.control.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| terminal_checkpoints.control.binding.arm | "control" |
| terminal_checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| terminal_checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| terminal_checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| terminal_checkpoints.control.binding.teacher_goals.web | 18750000 |
| terminal_checkpoints.control.binding.teacher_goals.story | 1250000 |
| terminal_checkpoints.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| terminal_checkpoints.control.binding.teacher_goals.conditional_textbook | 2500000 |
| terminal_checkpoints.control.binding.optimizer_policy | "inherit" |
| terminal_checkpoints.control.binding.peak_lr | 0.0002 |
| terminal_checkpoints.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| terminal_checkpoints.control.binding.study_kind | "same_input_positive_outcome_CE" |
| terminal_checkpoints.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| terminal_checkpoints.control.binding.outcome_weight | 1 |
| terminal_checkpoints.control.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| terminal_checkpoints.control.update | 62936 |
| terminal_checkpoints.control.tokens | 2062286848 |
| terminal_checkpoints.control.supervised_tokens | 2045000000 |
| terminal_checkpoints.control.additional_supervised_tokens | 25000000 |
| terminal_checkpoints.control.additional_input_tokens | 25231360 |
| terminal_checkpoints.control.source_teachers.web | 18750000 |
| terminal_checkpoints.control.source_teachers.story | 1250000 |
| terminal_checkpoints.control.source_teachers.ordinary_textbook | 2500000 |
| terminal_checkpoints.control.source_teachers.conditional_textbook | 2500000 |
| terminal_checkpoints.control.source_eos.web | 164131 |
| terminal_checkpoints.control.source_eos.story | 9486 |
| terminal_checkpoints.control.source_eos.ordinary_textbook | 18576 |
| terminal_checkpoints.control.source_eos.conditional_textbook | 17680 |
| terminal_checkpoints.control.source_input_tokens.web | 18934784 |
| terminal_checkpoints.control.source_input_tokens.story | 1259520 |
| terminal_checkpoints.control.source_input_tokens.ordinary_textbook | 2519040 |
| terminal_checkpoints.control.source_input_tokens.conditional_textbook | 2518016 |
| terminal_checkpoints.control.source_focus_teachers.web | 0 |
| terminal_checkpoints.control.source_focus_teachers.story | 0 |
| terminal_checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| terminal_checkpoints.control.source_focus_teachers.conditional_textbook | 654588 |
| terminal_checkpoints.control.focus_teacher_tokens | 654588 |
| terminal_checkpoints.control.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| terminal_checkpoints.control.weighted_teacher_mass | 25000000 |
| terminal_checkpoints.control.outcome_weight | 1 |
| terminal_checkpoints.control.training_seconds | 39.79399216850288 |
| terminal_checkpoints.control.completed_at | "2026-10-06T01:37:03.185223Z" |
| terminal_checkpoints.positive4.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/positive4/training/checkpoint-00062936.pt" |
| terminal_checkpoints.positive4.checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| terminal_checkpoints.positive4.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| terminal_checkpoints.positive4.binding.arm | "positive4" |
| terminal_checkpoints.positive4.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| terminal_checkpoints.positive4.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| terminal_checkpoints.positive4.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| terminal_checkpoints.positive4.binding.teacher_goals.web | 18750000 |
| terminal_checkpoints.positive4.binding.teacher_goals.story | 1250000 |
| terminal_checkpoints.positive4.binding.teacher_goals.ordinary_textbook | 2500000 |
| terminal_checkpoints.positive4.binding.teacher_goals.conditional_textbook | 2500000 |
| terminal_checkpoints.positive4.binding.optimizer_policy | "inherit" |
| terminal_checkpoints.positive4.binding.peak_lr | 0.0002 |
| terminal_checkpoints.positive4.binding.loss | "normalized positive-outcome CE body+EOS" |
| terminal_checkpoints.positive4.binding.study_kind | "same_input_positive_outcome_CE" |
| terminal_checkpoints.positive4.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| terminal_checkpoints.positive4.binding.outcome_weight | 4 |
| terminal_checkpoints.positive4.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| terminal_checkpoints.positive4.update | 62936 |
| terminal_checkpoints.positive4.tokens | 2062286848 |
| terminal_checkpoints.positive4.supervised_tokens | 2045000000 |
| terminal_checkpoints.positive4.additional_supervised_tokens | 25000000 |
| terminal_checkpoints.positive4.additional_input_tokens | 25231360 |
| terminal_checkpoints.positive4.source_teachers.web | 18750000 |
| terminal_checkpoints.positive4.source_teachers.story | 1250000 |
| terminal_checkpoints.positive4.source_teachers.ordinary_textbook | 2500000 |
| terminal_checkpoints.positive4.source_teachers.conditional_textbook | 2500000 |
| terminal_checkpoints.positive4.source_eos.web | 164131 |
| terminal_checkpoints.positive4.source_eos.story | 9486 |
| terminal_checkpoints.positive4.source_eos.ordinary_textbook | 18576 |
| terminal_checkpoints.positive4.source_eos.conditional_textbook | 17680 |
| terminal_checkpoints.positive4.source_input_tokens.web | 18934784 |
| terminal_checkpoints.positive4.source_input_tokens.story | 1259520 |
| terminal_checkpoints.positive4.source_input_tokens.ordinary_textbook | 2519040 |
| terminal_checkpoints.positive4.source_input_tokens.conditional_textbook | 2518016 |
| terminal_checkpoints.positive4.source_focus_teachers.web | 0 |
| terminal_checkpoints.positive4.source_focus_teachers.story | 0 |
| terminal_checkpoints.positive4.source_focus_teachers.ordinary_textbook | 0 |
| terminal_checkpoints.positive4.source_focus_teachers.conditional_textbook | 654588 |
| terminal_checkpoints.positive4.focus_teacher_tokens | 654588 |
| terminal_checkpoints.positive4.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| terminal_checkpoints.positive4.weighted_teacher_mass | 26963764 |
| terminal_checkpoints.positive4.outcome_weight | 4 |
| terminal_checkpoints.positive4.training_seconds | 39.13245353780803 |
| terminal_checkpoints.positive4.completed_at | "2026-10-06T01:38:57.938574Z" |
| restored_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_UI.training_tokens | 10000007168 |

</details>

<details>
<summary>reports/phase6/condition_positive_comparison_completion.json — actual50M_all160_review_complete_both_candidates_rejected_Base_unmet</summary>

[原記録](../../reports/phase6/condition_positive_comparison_completion.json) ／ SHA256: `bc2eadd79282b7ad5160f2895ce205c242bbe8c4ac140bc89822b59ab1ae671f` ／ 4,296 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual50M_all160_review_complete_both_candidates_rejected_Base_unmet" |
| pair_analysis | "reports/phase6/condition_positive_condition_pair_analysis.json" |
| pair_analysis_sha256 | "ad11415b522d1c128b23bf972e3788298184c1f6189e1b9ab7d7b0524559226b" |
| scientific_teacher_tokens | 50000000 |
| scientific_input_tokens | 50462720 |
| new_original_tokens | 0 |
| verification_teacher_tokens | 2599740 |
| scientific_GPU_seconds | 224.40080486799707 |
| verification_GPU_seconds | 22.01919901598012 |
| combined_GPU_seconds | 246.4200038839772 |
| summaries.control.BPB | 1.1435587102961566 |
| summaries.control.rates.eos | 44 |
| summaries.control.rates.repetition | 26 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 54 |
| summaries.control.relevance2 | 43 |
| summaries.control.coherent | 15 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 25000000 |
| summaries.control.source_teacher_tokens.web | 18750000 |
| summaries.control.source_teacher_tokens.story | 1250000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.control.focus_teacher_tokens | 654588 |
| summaries.control.weighted_teacher_mass | 25000000 |
| summaries.control.notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| summaries.control.Base_adopted | false |
| summaries.positive4.BPB | 1.145197706486869 |
| summaries.positive4.rates.eos | 47 |
| summaries.positive4.rates.repetition | 22 |
| summaries.positive4.rates.unicode_failure | 0 |
| summaries.positive4.rates.role_leak | 0 |
| summaries.positive4.rates.empty | 0 |
| summaries.positive4.grammar2 | 61 |
| summaries.positive4.relevance2 | 45 |
| summaries.positive4.coherent | 9 |
| summaries.positive4.appropriate | 24 |
| summaries.positive4.new_teacher_tokens | 25000000 |
| summaries.positive4.source_teacher_tokens.web | 18750000 |
| summaries.positive4.source_teacher_tokens.story | 1250000 |
| summaries.positive4.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.positive4.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.positive4.focus_teacher_tokens | 654588 |
| summaries.positive4.weighted_teacher_mass | 26963764 |
| summaries.positive4.notes_sha256 | "2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e" |
| summaries.positive4.Base_adopted | false |
| Base_adopted | false |
| Base_complete | false |
| independent_seed_confirmation_complete | false |
| protected_test_used | false |
| restored_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_UI.training_tokens | 10000007168 |

</details>

<details>
<summary>reports/phase6/condition_positive_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_positive_comparison_evidence_manifest.json) ／ SHA256: `5248469e2a4cdae7ddeabd271ea79c06336cd1ee12fa7002170f5508ae4a5dab` ／ 23,344 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 10047232 |
| archive.bytes | 2438906 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_positive_comparison_proposal.json — defined_Base_comparison_commands_and_actual_CUDA_probe_pending</summary>

[原記録](../../reports/phase6/condition_positive_comparison_proposal.json) ／ SHA256: `06e676e203332a72d441f7caf9a6774991ffc7f74c73397f64ae963069082fb8` ／ 4,646 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_Base_comparison_commands_and_actual_CUDA_probe_pending" |
| user_scope | "Base only; notify and stop after completed evidence-qualified Base; no Chat/quantization" |
| reason | "Saved dev margin shifts respond to negation without reversing candidate rankings. Story ratio increase did not pass generation gates. Accepted explicit-opposition train pilot supplies original positive outcomes without invented false alternatives." |
| positive_data.reused_original_body_tokens | 71885 |
| positive_data.copied_serialized_tokens | 72909 |
| positive_data.focus_target_tokens | 18956 |
| positive_data.documents | 512 |
| positive_data.focus_enabled_documents | 504 |
| positive_data.weak_pilot_documents | 8 |
| positive_data.newly_prepared_original_tokens | 0 |
| teachers_per_arm | 25000000 |
| teacher_quota_each_arm.web | 18750000 |
| teacher_quota_each_arm.story | 1250000 |
| teacher_quota_each_arm.ordinary_textbook | 2500000 |
| teacher_quota_each_arm.conditional_textbook | 2500000 |
| combined_GPU_ceiling_seconds | 1800 |
| CUDA_probe_ceiling_seconds | 120 |
| scientific_GPU_budget | "1800 minus actual probe seconds; refuse infeasible measured estimate" |
| completion_condition | "Both25M teacher arms actually finish or a precise finite budget/failure is recorded; evaluate both under unchanged generation/relative improvement/Web BPB criteria. Report paired conditional-family ranking shifts as secondary evidence, never as a substitute for fluent generation. Reject failed candidates; no automatic weight/ratio sweep or long extension." |
| CPU_loss_component_tests | "reports/phase6/condition_positive_loss_tests.xml" |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_positive_comparison_review.json — same_input_positive_CE_actual50M_all160_evidence_complete</summary>

[原記録](../../reports/phase6/condition_positive_comparison_review.json) ／ SHA256: `c9062ff59ff032a18abc05163f85b3e53d8d2b0a79ef5fd028630c2a565d14ea` ／ 4,263 bytes

| 原キー | 保存値 |
|---|---|
| status | "same_input_positive_CE_actual50M_all160_evidence_complete" |
| summaries.control.BPB | 1.1435587102961566 |
| summaries.control.rates.eos | 44 |
| summaries.control.rates.repetition | 26 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 54 |
| summaries.control.relevance2 | 43 |
| summaries.control.coherent | 15 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 25000000 |
| summaries.control.source_teacher_tokens.web | 18750000 |
| summaries.control.source_teacher_tokens.story | 1250000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.control.focus_teacher_tokens | 654588 |
| summaries.control.weighted_teacher_mass | 25000000 |
| summaries.control.notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| summaries.control.Base_adopted | false |
| summaries.positive4.BPB | 1.145197706486869 |
| summaries.positive4.rates.eos | 47 |
| summaries.positive4.rates.repetition | 22 |
| summaries.positive4.rates.unicode_failure | 0 |
| summaries.positive4.rates.role_leak | 0 |
| summaries.positive4.rates.empty | 0 |
| summaries.positive4.grammar2 | 61 |
| summaries.positive4.relevance2 | 45 |
| summaries.positive4.coherent | 9 |
| summaries.positive4.appropriate | 24 |
| summaries.positive4.new_teacher_tokens | 25000000 |
| summaries.positive4.source_teacher_tokens.web | 18750000 |
| summaries.positive4.source_teacher_tokens.story | 1250000 |
| summaries.positive4.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.positive4.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.positive4.focus_teacher_tokens | 654588 |
| summaries.positive4.weighted_teacher_mass | 26963764 |
| summaries.positive4.notes_sha256 | "2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e" |
| summaries.positive4.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.control.grammar_at_least56 | false |
| absolute_dev_screen.control.coherence_at_least27 | false |
| absolute_dev_screen.control.appropriate_at_least27 | true |
| absolute_dev_screen.control.EOS_at_least37 | true |
| absolute_dev_screen.control.repetition_at_most18 | false |
| absolute_dev_screen.control.no_empty_role_unicode | true |
| absolute_dev_screen.positive4.grammar_at_least56 | true |
| absolute_dev_screen.positive4.coherence_at_least27 | false |
| absolute_dev_screen.positive4.appropriate_at_least27 | false |
| absolute_dev_screen.positive4.EOS_at_least37 | true |
| absolute_dev_screen.positive4.repetition_at_most18 | false |
| absolute_dev_screen.positive4.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.positive4.EOS_at_least8_more | true |
| original_Web.positive4.repetition_no_worse | true |
| original_Web.positive4.no_empty_role_unicode | true |
| original_Web.positive4.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.positive4 | false |
| new_scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 2599740 |
| GPU_seconds | 224.40080486799707 |
| verification_GPU_seconds | 22.01919901598012 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/condition_positive_condition_pair_analysis.json — completed_fixed_dev_condition_pair_analysis</summary>

[原記録](../../reports/phase6/condition_positive_condition_pair_analysis.json) ／ SHA256: `ad11415b522d1c128b23bf972e3788298184c1f6189e1b9ab7d7b0524559226b` ／ 186,024 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_fixed_dev_condition_pair_analysis" |
| models.control.causality.accuracy | 0.5625 |
| models.control.causality.both_correct | 2 |
| models.control.causality.neither_correct | 0 |
| models.control.comparison.accuracy | 0.5 |
| models.control.comparison.both_correct | 0 |
| models.control.comparison.neither_correct | 0 |
| models.control.coreference.accuracy | 0.4375 |
| models.control.coreference.both_correct | 0 |
| models.control.coreference.neither_correct | 2 |
| models.control.negation.accuracy | 0.5 |
| models.control.negation.both_correct | 0 |
| models.control.negation.neither_correct | 0 |
| models.control.quantity.accuracy | 0.5625 |
| models.control.quantity.both_correct | 3 |
| models.control.quantity.neither_correct | 1 |
| models.control.time.accuracy | 0.59375 |
| models.control.time.both_correct | 3 |
| models.control.time.neither_correct | 0 |
| models.positive4.causality.accuracy | 0.6875 |
| models.positive4.causality.both_correct | 6 |
| models.positive4.causality.neither_correct | 0 |
| models.positive4.comparison.accuracy | 0.5 |
| models.positive4.comparison.both_correct | 0 |
| models.positive4.comparison.neither_correct | 0 |
| models.positive4.coreference.accuracy | 0.5 |
| models.positive4.coreference.both_correct | 1 |
| models.positive4.coreference.neither_correct | 1 |
| models.positive4.negation.accuracy | 0.5 |
| models.positive4.negation.both_correct | 0 |
| models.positive4.negation.neither_correct | 0 |
| models.positive4.quantity.accuracy | 0.53125 |
| models.positive4.quantity.both_correct | 2 |
| models.positive4.quantity.neither_correct | 1 |
| models.positive4.time.accuracy | 0.59375 |
| models.positive4.time.both_correct | 3 |
| models.positive4.time.neither_correct | 0 |
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
| references.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| references.positive4.checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.017634991003433242 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| prepared_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |
| limitations | "Reuse of fixed dev96 paired families, one learned seed. Same prediction after a context change is descriptive evidence of candidate preference on these examples, not proof of missing attention or model capacity limits. Positive margin shift is not correct generation. No new training or test; do not train on these evaluation prompts." |

</details>

<details>
<summary>reports/phase6/condition_positive_control_notes.json — None</summary>

[原記録](../../reports/phase6/condition_positive_control_notes.json) ／ SHA256: `790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70` ／ 17,212 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition_positive_positive4_notes.json — None</summary>

[原記録](../../reports/phase6/condition_positive_positive4_notes.json) ／ SHA256: `2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e` ／ 17,255 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition_positive_trainfit_diagnostic_proposal.json — planned_not_implemented_not_launched</summary>

[原記録](../../reports/phase6/condition_positive_trainfit_diagnostic_proposal.json) ／ SHA256: `4581f0d7ef7211f4df7a825d3a43a1fa49ed07d575699542906b4d72f79cbc6c` ／ 1,646 bytes

| 原キー | 保存値 |
|---|---|
| status | "planned_not_implemented_not_launched" |
| documents | 512 |
| GPU_budget_seconds | 60 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| completion_condition | "All fixed512 documents and3 checkpoint hashes measured on identical targets; positive/other/EOS count parity; finite loss; unchanged weight/RNG checks; actual budget and portable evidence. Interrupted partial run is incomplete." |
| limitations | "Train-only teacher forcing can distinguish failure to fit from fit without transfer on these examples, not prove generalization, attention failure or capacity. The saved dev paired analysis remains secondary; no evaluation text enters learning." |

</details>

<details>
<summary>reports/phase6/condition_preservation_completion.json — complete_plan61_preparation_failure_branch</summary>

[原記録](../../reports/phase6/condition_preservation_completion.json) ／ SHA256: `a29af1d580e52cfc589fb73c6f6645054d1c1a23311a7cc3aa432ee1ab84da81` ／ 2,717 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_plan61_preparation_failure_branch" |
| checks.stage1_saved160_source40_diagnosis | true |
| checks.stage2_actual_matched20M_data_builder_complete_exited | true |
| checks.stage2_all80_specific_raw_bound_notes | true |
| checks.stage2_evidence_checks_all_pass | true |
| checks.stage2_unchanged_readiness_condition_failed | true |
| checks.stage3_skipped_per_explicit_preparation_failure_branch | true |
| checks.stage4_judgment_full_not_launched | true |
| checks.original10B_UI_actual_identity_and_HTTP | true |
| checks.scientific_verification_tokens_zero | true |
| checks.results_report_saved | true |
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
| checked_at | "2026-10-05T09:32:56.575629Z" |

</details>

<details>
<summary>reports/phase6/condition_preservation_data_review.json — evidence_audit_passed</summary>

[原記録](../../reports/phase6/condition_preservation_data_review.json) ／ SHA256: `133bdc2821a73168b84c59e6cb144527b9fa892cb1df7ad867dabe38097eb190` ／ 132,740 bytes

| 原キー | 保存値 |
|---|---|
| status | "evidence_audit_passed" |
| checks.actual_builder_complete_exited_within1800 | true |
| checks.saved160_and_source40_diagnosis_completed | true |
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
| checks.selector_related_four_CPU_tests_pass | true |
| preparation_gates.quantity_mean_length_EOS_distribution_matched | true |
| accepted_for_experiment | false |
| summaries.control.tokens | 20000028 |
| summaries.control.documents | 71268 |
| summaries.control.body_bytes | 83700142 |
| summaries.control.body_tokens_mean | 278.6312510523657 |
| summaries.control.EOS_per_1000_tokens | 3.563395011246984 |
| summaries.control.samples_sha256 | "e69e5a5476bf787ec0fb6dc6fc81025b44469f37979b05a94001149a31277715" |
| summaries.refined.tokens | 20000028 |
| summaries.refined.documents | 71268 |
| summaries.refined.body_bytes | 83456687 |
| summaries.refined.body_tokens_mean | 278.6312510523657 |
| summaries.refined.EOS_per_1000_tokens | 3.563395011246984 |
| summaries.refined.samples_sha256 | "74955b6f367169a2b413cf4241dc59e3e9a1df252aabdce227e838e74e971dac" |
| notes_sha256 | "ea8a5c8ae3d9529ed04cbb7e184ed309c43d2a072f9468e34f2f621eddf92333" |
| source_sha256.tests/test_condition_story_quality.py | "34ce23c8a616574aa5c762f3005330af1cff1dea7868e1f5b15e815b7cb825de" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| review_seconds | 0.7701246189972153 |
| preparation_seconds | 13.752109434004524 |
| checked_at | "2026-10-05T09:31:14.377319Z" |
| shared_documents | 10155 |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| protected_test_used | false |
| interpretation | "Same-source heuristic subset contrast; action ending/topic/dialogue composition also changes; not a semantic-quality causal certificate" |

</details>

<details>
<summary>reports/phase6/condition_preservation_delivery.json — verified_delivery_before_commit</summary>

[原記録](../../reports/phase6/condition_preservation_delivery.json) ／ SHA256: `4521f0facc56ce9fcd5f8139545ba3ef17e8507281ccd8286b5fe1b0b12f7cbf` ／ 1,241 bytes

| 原キー | 保存値 |
|---|---|
| status | "verified_delivery_before_commit" |
| checked_at | "2026-10-05T09:38:10.9574885Z" |
| checks.all_preparation_evidence_true | true |
| checks.preparation_gate_failed | true |
| checks.all_completion_branch_checks_true | true |
| checks.all80_individual_notes_saved | true |
| checks.scientific_and_verification_zero | true |
| checks.report_binding_unchanged | true |
| checks.result60_unchanged | true |
| checks.plan61_frozen_unchanged | true |
| checks.all_execution_sources_frozen_and_Windows_text_matches | true |
| checks.local_document_links_exist | true |
| checks.whitespace_check_passed | true |
| checks.git_identity_local_yousan | true |
| completion_sha256 | "a29af1d580e52cfc589fb73c6f6645054d1c1a23311a7cc3aa432ee1ab84da81" |
| source_bytes_note | "Actual Linux frozen bytes checked; Windows normalized text matches. Historical tokenizer CRLF bytes retained unchanged." |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| candidate_adopted | false |

</details>

<details>
<summary>reports/phase6/condition_preservation_diagnosis.json — None</summary>

[原記録](../../reports/phase6/condition_preservation_diagnosis.json) ／ SHA256: `ecc4a7a00340c81cdae48a227d63264f9173b830e959af3af3835a7f73e610a3` ／ 143,703 bytes

| 原キー | 保存値 |
|---|---|
| category_totals.control.common_sense.relevance_below2 | 7 |
| category_totals.control.common_sense.coherence0 | 7 |
| category_totals.control.conversation.relevance_below2 | 5 |
| category_totals.control.conversation.coherence0 | 2 |
| category_totals.control.daily.relevance_below2 | 5 |
| category_totals.control.daily.coherence0 | 4 |
| category_totals.control.description.relevance_below2 | 7 |
| category_totals.control.description.coherence0 | 3 |
| category_totals.control.grammar.count | 8 |
| category_totals.control.grammar.relevance_below2 | 5 |
| category_totals.control.grammar.coherence0 | 3 |
| category_totals.control.local_context.relevance_below2 | 6 |
| category_totals.control.local_context.coherence0 | 4 |
| category_totals.control.numbers.relevance_below2 | 8 |
| category_totals.control.numbers.coherence0 | 6 |
| category_totals.control.proper_names.relevance_below2 | 4 |
| category_totals.control.proper_names.coherence0 | 6 |
| category_totals.control.punctuation.relevance_below2 | 4 |
| category_totals.control.punctuation.coherence0 | 4 |
| category_totals.control.short_story.relevance_below2 | 6 |
| category_totals.control.short_story.coherence0 | 3 |
| category_totals.refined.common_sense.relevance_below2 | 4 |
| category_totals.refined.common_sense.coherence0 | 5 |
| category_totals.refined.conversation.relevance_below2 | 7 |
| category_totals.refined.conversation.coherence0 | 4 |
| category_totals.refined.daily.relevance_below2 | 7 |
| category_totals.refined.daily.coherence0 | 5 |
| category_totals.refined.description.relevance_below2 | 6 |
| category_totals.refined.description.coherence0 | 4 |
| category_totals.refined.grammar.count | 8 |
| category_totals.refined.grammar.relevance_below2 | 4 |
| category_totals.refined.grammar.coherence0 | 3 |
| category_totals.refined.local_context.relevance_below2 | 7 |
| category_totals.refined.local_context.coherence0 | 7 |
| category_totals.refined.numbers.relevance_below2 | 8 |
| category_totals.refined.numbers.coherence0 | 8 |
| category_totals.refined.proper_names.relevance_below2 | 3 |
| category_totals.refined.proper_names.coherence0 | 5 |
| category_totals.refined.punctuation.relevance_below2 | 5 |
| category_totals.refined.punctuation.coherence0 | 4 |
| category_totals.refined.short_story.relevance_below2 | 5 |
| category_totals.refined.short_story.coherence0 | 3 |
| source_samples.seed | 20261005 |
| source_samples.method | "uniform reservoir over all retained and accepted new train stories" |
| source_individual_notes.status | "inspected_accepted_for_bounded_comparison" |
| source_individual_notes.accepted_for_experiment | true |
| source_individual_notes.ready_sha256 | "afd3906d8aad023c4784136fcdfe141d7823df8303eb30ac0b79dd242660d97b" |
| source_individual_notes.manifest_sha256 | "a33ad89783d7b9c2f65eadc96ceca06d19c1e397b0dc95852b148d408cec7b12" |
| source_individual_notes.samples_sha256 | "48a04f9ac0945cd5dca808eb28775a696bfb46e08697ddade2005f0ed88f5099" |
| source_individual_notes.reviewer_sha256 | "0aef6cfd0c995ed947373fdc2ea9e76dae7b7b67c3791842d8446744811243fc" |
| source_individual_notes.weak_examples | 18 |
| source_individual_notes.comparison_interpretation | "Amount plus new source/length/EOS density, not amount-only; all old stories retained" |
| source_individual_notes.source_selection | "Existing retained selector unchanged; new translated full-story selector32–512 tokens/2–24sentences/4gram repetition&lt;=0.15" |
| source_individual_notes.content_limit | "Nonblind Codex sample diagnosis. Weak causality, translation artifacts, fantasy and violent stories remain; not factual or child-safe certification. Whole-corpus independent overlap audit incomplete." |
| source_individual_notes.original_validation_test_used | false |
| source_individual_notes.independent_human_certification | false |
| source_individual_notes.checked_at | "2026-10-05T07:36:53.675410Z" |
| protected_test_used | false |
| scientific_training_tokens | 0 |
| CPU_seconds | 0.0022155879996716976 |

</details>

<details>
<summary>reports/phase6/condition_preservation_judgment.json — None</summary>

[原記録](../../reports/phase6/condition_preservation_judgment.json) ／ SHA256: `0f68f917a9c9a14a83863a8efb2d1f0bf319a5f21dc1387dca236f319e732ebb` ／ 900 bytes

| 原キー | 保存値 |
|---|---|
| decision | "preparation_rejected_no_GPU" |
| failed_gates | ["candidate_weak_at_most10_of40"] |
| scientific_training_tokens | 0 |
| verification_tokens | 0 |
| candidate_adopted | false |
| interpretation | "Sample count21→12 is not evidence of model improvement or all-pool semantic quality. Stage3/full skipped under the unchanged preparation-failure branch." |
| checked_at | "2026-10-05T09:32:56.575324Z" |

</details>

<details>
<summary>reports/phase6/condition_preservation_prepare_job.json — complete</summary>

[原記録](../../reports/phase6/condition_preservation_prepare_job.json) ／ SHA256: `5a7b3cc005d53a11163e434da40ccc61cf32ce31ec80f855446f3cc8efb977c9` ／ 1,416 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.target_tokens | 20000000 |
| binding.seed | 202610061 |
| binding.budget_seconds | 1800 |
| binding.scope | "Prepared translation-only train stream after unchanged common base selector/family/local exclusion; candidate adds frozen heuristic exclusions" |
| elapsed_seconds | 13.752109434004524 |
| eligible | 247265 |
| tokens | 20000028 |
| tokens_per_pool | 20000028 |

</details>

<details>
<summary>reports/phase6/condition_preservation_ready.json — ready_pending_content_review</summary>

[原記録](../../reports/phase6/condition_preservation_ready.json) ／ SHA256: `898a07a5efdeb8364364a301cf1b00e37be4026983ccb49f958e0d93b2974b3d` ／ 26,212 bytes

| 原キー | 保存値 |
|---|---|
| status | "ready_pending_content_review" |
| binding.target_tokens | 20000000 |
| binding.seed | 202610061 |
| binding.budget_seconds | 1800 |
| binding.scope | "Prepared translation-only train stream after unchanged common base selector/family/local exclusion; candidate adds frozen heuristic exclusions" |
| totals.control.tokens | 20000028 |
| totals.control.documents | 71268 |
| totals.control.body_bytes | 83700142 |
| totals.refined.tokens | 20000028 |
| totals.refined.documents | 71268 |
| totals.refined.body_bytes | 83456687 |
| supply.eligible_histogram.293 | 2097 |
| supply.eligible_histogram.253 | 2230 |
| supply.eligible_histogram.191 | 536 |
| supply.eligible_histogram.291 | 2170 |
| supply.eligible_histogram.230 | 1628 |
| supply.eligible_histogram.254 | 2354 |
| supply.eligible_histogram.180 | 416 |
| supply.eligible_histogram.287 | 2207 |
| supply.eligible_histogram.224 | 1443 |
| supply.eligible_histogram.200 | 728 |
| supply.eligible_histogram.274 | 2448 |
| supply.eligible_histogram.323 | 1440 |
| supply.eligible_histogram.397 | 238 |
| supply.eligible_histogram.356 | 736 |
| supply.eligible_histogram.342 | 914 |
| supply.eligible_histogram.383 | 403 |
| supply.eligible_histogram.261 | 2317 |
| supply.eligible_histogram.267 | 2458 |
| supply.eligible_histogram.378 | 415 |
| supply.eligible_histogram.268 | 2359 |
| supply.eligible_histogram.327 | 1285 |
| supply.eligible_histogram.326 | 1310 |
| supply.eligible_histogram.276 | 2453 |
| supply.eligible_histogram.317 | 1550 |
| supply.eligible_histogram.321 | 1403 |
| supply.eligible_histogram.273 | 2409 |
| supply.eligible_histogram.353 | 773 |
| supply.eligible_histogram.388 | 319 |
| supply.eligible_histogram.366 | 578 |
| supply.eligible_histogram.336 | 1110 |
| supply.eligible_histogram.320 | 1501 |
| supply.eligible_histogram.304 | 1925 |
| supply.eligible_histogram.280 | 2338 |
| supply.eligible_histogram.340 | 1014 |
| supply.eligible_histogram.290 | 2189 |
| supply.eligible_histogram.156 | 262 |
| supply.eligible_histogram.312 | 1697 |
| supply.eligible_histogram.384 | 386 |
| supply.eligible_histogram.334 | 1160 |
| supply.eligible_histogram.478 | 22 |
| supply.eligible_histogram.275 | 2370 |
| supply.eligible_histogram.302 | 1846 |
| supply.eligible_histogram.188 | 495 |
| supply.eligible_histogram.292 | 2163 |
| supply.eligible_histogram.329 | 1270 |
| supply.eligible_histogram.387 | 329 |
| supply.eligible_histogram.311 | 1764 |
| supply.eligible_histogram.309 | 1769 |
| supply.eligible_histogram.322 | 1402 |
| supply.eligible_histogram.251 | 2223 |
| supply.eligible_histogram.379 | 430 |
| supply.eligible_histogram.239 | 1894 |
| supply.eligible_histogram.246 | 2123 |
| supply.eligible_histogram.324 | 1310 |
| supply.eligible_histogram.197 | 698 |
| supply.eligible_histogram.367 | 581 |
| supply.eligible_histogram.338 | 1051 |
| supply.eligible_histogram.257 | 2418 |
| supply.eligible_histogram.337 | 1042 |
| supply.eligible_histogram.187 | 490 |
| supply.eligible_histogram.349 | 855 |
| supply.eligible_histogram.264 | 2442 |
| supply.eligible_histogram.269 | 2363 |
| supply.eligible_histogram.300 | 1971 |
| supply.eligible_histogram.297 | 2002 |
| supply.eligible_histogram.218 | 1255 |
| supply.eligible_histogram.244 | 2012 |
| supply.eligible_histogram.272 | 2436 |
| supply.eligible_histogram.255 | 2288 |
| supply.eligible_histogram.286 | 2197 |
| supply.eligible_histogram.328 | 1350 |
| supply.eligible_histogram.226 | 1535 |
| supply.eligible_histogram.210 | 1015 |
| supply.eligible_histogram.362 | 629 |
| supply.eligible_histogram.332 | 1145 |
| supply.eligible_histogram.427 | 105 |
| supply.eligible_histogram.278 | 2406 |
| supply.eligible_histogram.234 | 1749 |
| supply.eligible_histogram.240 | 1912 |
| supply.eligible_histogram.411 | 148 |
| supply.eligible_histogram.270 | 2489 |
| supply.eligible_histogram.347 | 828 |
| supply.eligible_histogram.258 | 2369 |
| supply.eligible_histogram.186 | 490 |
| supply.eligible_histogram.265 | 2395 |
| supply.eligible_histogram.301 | 1952 |
| supply.eligible_histogram.355 | 731 |
| supply.eligible_histogram.285 | 2300 |
| supply.eligible_histogram.262 | 2342 |
| supply.eligible_histogram.249 | 2195 |
| supply.eligible_histogram.308 | 1728 |
| supply.eligible_histogram.252 | 2194 |
| supply.eligible_histogram.146 | 174 |
| supply.eligible_histogram.295 | 2073 |
| supply.eligible_histogram.306 | 1858 |
| supply.eligible_histogram.296 | 2098 |
| supply.eligible_histogram.227 | 1548 |
| supply.eligible_histogram.198 | 644 |
| supply.eligible_histogram.250 | 2213 |
| supply.eligible_histogram.277 | 2390 |
| supply.eligible_histogram.222 | 1309 |
| supply.eligible_histogram.428 | 105 |
| supply.eligible_histogram.266 | 2321 |
| supply.eligible_histogram.203 | 776 |
| supply.eligible_histogram.196 | 609 |
| supply.eligible_histogram.233 | 1742 |
| supply.eligible_histogram.314 | 1608 |
| supply.eligible_histogram.316 | 1580 |
| supply.eligible_histogram.235 | 1746 |
| supply.eligible_histogram.206 | 902 |
| supply.eligible_histogram.284 | 2337 |
| supply.eligible_histogram.199 | 698 |
| supply.eligible_histogram.181 | 473 |
| supply.eligible_histogram.237 | 1830 |
| supply.eligible_histogram.205 | 846 |
| supply.eligible_histogram.207 | 869 |
| supply.eligible_histogram.245 | 2142 |
| supply.eligible_histogram.241 | 1920 |
| supply.eligible_histogram.229 | 1591 |
| supply.eligible_histogram.165 | 314 |
| supply.eligible_histogram.330 | 1247 |
| supply.eligible_histogram.243 | 2011 |
| supply.eligible_histogram.231 | 1699 |
| supply.eligible_histogram.282 | 2348 |
| supply.eligible_histogram.238 | 1862 |
| supply.eligible_histogram.175 | 370 |
| supply.eligible_histogram.148 | 171 |
| supply.eligible_histogram.256 | 2318 |
| supply.eligible_histogram.164 | 317 |
| supply.eligible_histogram.193 | 584 |
| supply.eligible_histogram.331 | 1202 |
| supply.eligible_histogram.217 | 1215 |
| supply.eligible_histogram.177 | 416 |
| supply.eligible_histogram.377 | 451 |
| supply.eligible_histogram.283 | 2330 |
| supply.eligible_histogram.208 | 912 |
| supply.eligible_histogram.369 | 508 |
| supply.eligible_histogram.213 | 1037 |
| supply.eligible_histogram.173 | 362 |
| supply.eligible_histogram.305 | 1857 |
| supply.eligible_histogram.345 | 926 |
| supply.eligible_histogram.225 | 1508 |
| supply.eligible_histogram.212 | 1033 |
| supply.eligible_histogram.130 | 96 |
| supply.eligible_histogram.315 | 1563 |
| supply.eligible_histogram.471 | 29 |
| supply.eligible_histogram.201 | 767 |
| supply.eligible_histogram.289 | 2215 |
| supply.eligible_histogram.216 | 1147 |
| supply.eligible_histogram.248 | 2169 |
| supply.eligible_histogram.368 | 532 |
| supply.eligible_histogram.242 | 2031 |
| supply.eligible_histogram.391 | 319 |
| supply.eligible_histogram.307 | 1769 |
| supply.eligible_histogram.409 | 181 |
| supply.eligible_histogram.341 | 913 |
| supply.eligible_histogram.204 | 764 |
| supply.eligible_histogram.190 | 543 |
| supply.eligible_histogram.263 | 2351 |
| supply.eligible_histogram.319 | 1439 |
| supply.eligible_histogram.310 | 1616 |
| supply.eligible_histogram.350 | 766 |
| supply.eligible_histogram.346 | 890 |
| supply.eligible_histogram.223 | 1398 |
| supply.eligible_histogram.371 | 522 |
| supply.eligible_histogram.351 | 792 |
| supply.eligible_histogram.430 | 98 |
| supply.eligible_histogram.219 | 1206 |
| supply.eligible_histogram.360 | 636 |
| supply.eligible_histogram.313 | 1669 |
| supply.eligible_histogram.375 | 465 |
| supply.eligible_histogram.281 | 2329 |
| supply.eligible_histogram.418 | 149 |
| supply.eligible_histogram.161 | 271 |
| supply.eligible_histogram.359 | 692 |
| supply.eligible_histogram.214 | 1071 |
| supply.eligible_histogram.202 | 800 |
| supply.eligible_histogram.228 | 1532 |
| supply.eligible_histogram.424 | 110 |
| supply.eligible_histogram.288 | 2305 |
| supply.eligible_histogram.220 | 1256 |
| supply.eligible_histogram.370 | 525 |
| supply.eligible_histogram.413 | 180 |
| supply.eligible_histogram.373 | 448 |
| supply.eligible_histogram.398 | 241 |
| supply.eligible_histogram.232 | 1673 |
| supply.eligible_histogram.348 | 838 |
| supply.eligible_histogram.168 | 303 |
| supply.eligible_histogram.260 | 2423 |
| supply.eligible_histogram.279 | 2353 |
| supply.eligible_histogram.385 | 334 |
| supply.eligible_histogram.374 | 478 |
| supply.eligible_histogram.303 | 1883 |
| supply.eligible_histogram.259 | 2387 |
| supply.eligible_histogram.298 | 2092 |
| supply.eligible_histogram.153 | 223 |
| supply.eligible_histogram.271 | 2474 |
| supply.eligible_histogram.325 | 1334 |
| supply.eligible_histogram.171 | 353 |
| supply.eligible_histogram.158 | 259 |
| supply.eligible_histogram.215 | 1069 |
| supply.eligible_histogram.139 | 152 |
| supply.eligible_histogram.152 | 199 |
| supply.eligible_histogram.386 | 346 |
| supply.eligible_histogram.143 | 172 |
| supply.eligible_histogram.126 | 76 |
| supply.eligible_histogram.131 | 100 |
| supply.eligible_histogram.335 | 1164 |
| supply.eligible_histogram.294 | 2106 |
| supply.eligible_histogram.381 | 376 |
| supply.eligible_histogram.136 | 117 |
| supply.eligible_histogram.174 | 373 |
| supply.eligible_histogram.96 | 17 |
| supply.eligible_histogram.195 | 637 |
| supply.eligible_histogram.361 | 581 |
| supply.eligible_histogram.339 | 989 |
| supply.eligible_histogram.421 | 132 |
| supply.eligible_histogram.354 | 718 |
| supply.eligible_histogram.389 | 296 |
| supply.eligible_histogram.318 | 1541 |
| supply.eligible_histogram.406 | 240 |
| supply.eligible_histogram.211 | 1011 |
| supply.eligible_histogram.343 | 940 |
| supply.eligible_histogram.352 | 765 |
| supply.eligible_histogram.392 | 281 |
| supply.eligible_histogram.333 | 1163 |
| supply.eligible_histogram.184 | 509 |
| supply.eligible_histogram.182 | 456 |
| supply.eligible_histogram.221 | 1340 |
| supply.eligible_histogram.157 | 198 |
| supply.eligible_histogram.167 | 308 |
| supply.eligible_histogram.178 | 426 |
| supply.eligible_histogram.393 | 295 |
| supply.eligible_histogram.189 | 530 |
| supply.eligible_histogram.382 | 391 |
| supply.eligible_histogram.236 | 1754 |
| supply.eligible_histogram.434 | 77 |
| supply.eligible_histogram.365 | 554 |
| supply.eligible_histogram.410 | 170 |
| supply.eligible_histogram.404 | 183 |
| supply.eligible_histogram.172 | 354 |
| supply.eligible_histogram.363 | 597 |
| supply.eligible_histogram.499 | 13 |
| supply.eligible_histogram.194 | 606 |
| supply.eligible_histogram.247 | 2153 |
| supply.eligible_histogram.447 | 57 |
| supply.eligible_histogram.358 | 625 |
| supply.eligible_histogram.394 | 274 |
| supply.eligible_histogram.183 | 456 |
| supply.eligible_histogram.299 | 1917 |
| supply.eligible_histogram.133 | 112 |
| supply.eligible_histogram.344 | 927 |
| supply.eligible_histogram.419 | 125 |
| supply.eligible_histogram.185 | 504 |
| supply.eligible_histogram.122 | 65 |
| supply.eligible_histogram.209 | 946 |
| supply.eligible_histogram.150 | 239 |
| supply.eligible_histogram.407 | 219 |
| supply.eligible_histogram.401 | 202 |
| supply.eligible_histogram.357 | 696 |
| supply.eligible_histogram.159 | 246 |
| supply.eligible_histogram.372 | 486 |
| supply.eligible_histogram.451 | 53 |
| supply.eligible_histogram.438 | 92 |
| supply.eligible_histogram.176 | 372 |
| supply.eligible_histogram.160 | 269 |
| supply.eligible_histogram.432 | 88 |
| supply.eligible_histogram.144 | 182 |
| supply.eligible_histogram.163 | 260 |
| supply.eligible_histogram.192 | 559 |
| supply.eligible_histogram.138 | 141 |
| supply.eligible_histogram.497 | 8 |
| supply.eligible_histogram.462 | 39 |
| supply.eligible_histogram.364 | 581 |
| supply.eligible_histogram.479 | 25 |
| supply.eligible_histogram.400 | 207 |
| supply.eligible_histogram.105 | 23 |
| supply.eligible_histogram.162 | 309 |
| supply.eligible_histogram.395 | 252 |
| supply.eligible_histogram.125 | 82 |
| supply.eligible_histogram.132 | 98 |
| supply.eligible_histogram.145 | 157 |
| supply.eligible_histogram.480 | 23 |
| supply.eligible_histogram.426 | 110 |
| supply.eligible_histogram.490 | 16 |
| supply.eligible_histogram.405 | 193 |
| supply.eligible_histogram.390 | 306 |
| supply.eligible_histogram.458 | 45 |
| supply.eligible_histogram.98 | 10 |
| supply.eligible_histogram.140 | 149 |
| supply.eligible_histogram.149 | 193 |
| supply.eligible_histogram.147 | 204 |
| supply.eligible_histogram.412 | 168 |
| supply.eligible_histogram.376 | 451 |
| supply.eligible_histogram.473 | 36 |
| supply.eligible_histogram.429 | 96 |
| supply.eligible_histogram.399 | 255 |
| supply.eligible_histogram.135 | 110 |
| supply.eligible_histogram.439 | 61 |
| supply.eligible_histogram.179 | 394 |
| supply.eligible_histogram.142 | 163 |
| supply.eligible_histogram.141 | 130 |
| supply.eligible_histogram.408 | 192 |
| supply.eligible_histogram.423 | 111 |
| supply.eligible_histogram.441 | 72 |
| supply.eligible_histogram.151 | 210 |
| supply.eligible_histogram.170 | 322 |
| supply.eligible_histogram.154 | 228 |
| supply.eligible_histogram.113 | 43 |
| supply.eligible_histogram.396 | 220 |
| supply.eligible_histogram.443 | 63 |
| supply.eligible_histogram.440 | 72 |
| supply.eligible_histogram.442 | 66 |
| supply.eligible_histogram.414 | 147 |
| supply.eligible_histogram.123 | 53 |
| supply.eligible_histogram.431 | 89 |
| supply.eligible_histogram.403 | 211 |
| supply.eligible_histogram.166 | 302 |
| supply.eligible_histogram.380 | 388 |
| supply.eligible_histogram.121 | 58 |
| supply.eligible_histogram.475 | 26 |
| supply.eligible_histogram.169 | 299 |
| supply.eligible_histogram.511 | 10 |
| supply.eligible_histogram.155 | 222 |
| supply.eligible_histogram.457 | 57 |
| supply.eligible_histogram.450 | 60 |
| supply.eligible_histogram.422 | 116 |
| supply.eligible_histogram.120 | 58 |
| supply.eligible_histogram.487 | 13 |
| supply.eligible_histogram.116 | 55 |
| supply.eligible_histogram.402 | 177 |
| supply.eligible_histogram.476 | 25 |
| supply.eligible_histogram.137 | 128 |
| supply.eligible_histogram.464 | 35 |
| supply.eligible_histogram.425 | 100 |
| supply.eligible_histogram.104 | 27 |
| supply.eligible_histogram.459 | 34 |
| supply.eligible_histogram.436 | 82 |
| supply.eligible_histogram.420 | 123 |
| supply.eligible_histogram.91 | 5 |
| supply.eligible_histogram.417 | 144 |
| supply.eligible_histogram.491 | 13 |
| supply.eligible_histogram.127 | 84 |
| supply.eligible_histogram.466 | 23 |
| supply.eligible_histogram.416 | 136 |
| supply.eligible_histogram.445 | 55 |
| supply.eligible_histogram.456 | 57 |
| supply.eligible_histogram.415 | 135 |
| supply.eligible_histogram.453 | 54 |
| supply.eligible_histogram.114 | 39 |
| supply.eligible_histogram.119 | 47 |
| supply.eligible_histogram.477 | 26 |
| supply.eligible_histogram.112 | 31 |
| supply.eligible_histogram.461 | 26 |
| supply.eligible_histogram.446 | 68 |
| supply.eligible_histogram.455 | 42 |
| supply.eligible_histogram.134 | 131 |
| supply.eligible_histogram.502 | 12 |
| supply.eligible_histogram.505 | 8 |
| supply.eligible_histogram.437 | 85 |
| supply.eligible_histogram.118 | 59 |
| supply.eligible_histogram.463 | 42 |
| supply.eligible_histogram.115 | 47 |
| supply.eligible_histogram.109 | 31 |
| supply.eligible_histogram.110 | 31 |
| supply.eligible_histogram.128 | 88 |
| supply.eligible_histogram.117 | 66 |
| supply.eligible_histogram.108 | 29 |
| supply.eligible_histogram.433 | 91 |
| supply.eligible_histogram.481 | 23 |
| supply.eligible_histogram.107 | 25 |
| supply.eligible_histogram.435 | 89 |
| supply.eligible_histogram.468 | 25 |
| supply.eligible_histogram.452 | 55 |
| supply.eligible_histogram.467 | 30 |
| supply.eligible_histogram.465 | 26 |
| supply.eligible_histogram.444 | 65 |
| supply.eligible_histogram.488 | 18 |
| supply.eligible_histogram.474 | 32 |
| supply.eligible_histogram.484 | 21 |
| supply.eligible_histogram.472 | 29 |
| supply.eligible_histogram.124 | 75 |
| supply.eligible_histogram.100 | 17 |
| supply.eligible_histogram.103 | 25 |
| supply.eligible_histogram.93 | 10 |
| supply.eligible_histogram.469 | 33 |
| supply.eligible_histogram.507 | 4 |
| supply.eligible_histogram.129 | 99 |
| supply.eligible_histogram.106 | 28 |
| supply.eligible_histogram.448 | 64 |
| supply.eligible_histogram.89 | 4 |
| supply.eligible_histogram.485 | 13 |
| supply.eligible_histogram.94 | 9 |
| supply.eligible_histogram.486 | 11 |
| supply.eligible_histogram.460 | 40 |
| supply.eligible_histogram.111 | 33 |
| supply.eligible_histogram.489 | 17 |
| supply.eligible_histogram.454 | 51 |
| supply.eligible_histogram.503 | 9 |
| supply.eligible_histogram.92 | 5 |
| supply.eligible_histogram.90 | 11 |
| supply.eligible_histogram.470 | 24 |
| supply.eligible_histogram.512 | 2 |
| supply.eligible_histogram.492 | 8 |
| supply.eligible_histogram.498 | 13 |
| supply.eligible_histogram.494 | 6 |
| supply.eligible_histogram.509 | 10 |
| supply.eligible_histogram.86 | 7 |
| supply.eligible_histogram.449 | 59 |
| supply.eligible_histogram.495 | 7 |
| supply.eligible_histogram.504 | 7 |
| supply.eligible_histogram.482 | 17 |
| supply.eligible_histogram.102 | 20 |
| supply.eligible_histogram.95 | 7 |
| supply.eligible_histogram.101 | 20 |
| supply.eligible_histogram.496 | 15 |
| supply.eligible_histogram.85 | 5 |
| supply.eligible_histogram.500 | 10 |
| supply.eligible_histogram.501 | 10 |
| supply.eligible_histogram.99 | 11 |
| supply.eligible_histogram.75 | 1 |
| supply.eligible_histogram.97 | 12 |
| supply.eligible_histogram.506 | 7 |
| supply.eligible_histogram.508 | 2 |
| supply.eligible_histogram.88 | 1 |
| supply.eligible_histogram.87 | 4 |
| supply.eligible_histogram.78 | 2 |
| supply.eligible_histogram.84 | 2 |
| supply.eligible_histogram.493 | 6 |
| supply.eligible_histogram.510 | 4 |
| supply.eligible_histogram.83 | 3 |
| supply.eligible_histogram.483 | 10 |
| supply.eligible_histogram.76 | 2 |
| supply.eligible_histogram.79 | 3 |
| supply.eligible_histogram.70 | 2 |
| supply.eligible_histogram.82 | 3 |
| supply.eligible_histogram.80 | 1 |
| supply.eligible_tokens | 86847717 |
| supply.target_tokens | 20000000 |
| supply.possible_tokens | 20000028 |
| body_tokens_mean | 278.6312510523657 |
| EOS_per_1000_tokens | 3.563395011246984 |
| matched_quantity_length_sequence_EOS_positions | true |
| official_validation_test_acquired | false |
| control_candidate_shared_documents | 10155 |
| interpretation | "Same-source heuristic subset contrast; action ending/topic/dialogue composition also changes; not a semantic-quality causal certificate" |
| seconds | 13.75133356101287 |

</details>

<details>
<summary>reports/phase6/condition_query_balance_active_job.json — complete_no_scientific_GPU_job</summary>

[原記録](../../reports/phase6/condition_query_balance_active_job.json) ／ SHA256: `0a4912c89fca7ff54f0ecb8adcd9c216edd7366f896ee71bb264d296ed2b3e53` ／ 2,629 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_no_scientific_GPU_job" |
| actual_identity.status | "complete" |
| actual_identity.GPU_elapsed_seconds | 253.21383405599045 |
| actual_identity.Base_adopted | false |
| actual_identity.protected_test_used | false |
| actual_identity.teachers | 99765470 |
| actual_identity.teacher_budget | 100000000 |
| actual_identity.source_teachers.web | 74823740 |
| actual_identity.source_teachers.story | 4988661 |
| actual_identity.source_teachers.ordinary_textbook | 9976547 |
| actual_identity.source_teachers.conditional_textbook | 9976522 |
| actual_identity.loss | 2.312191963195801 |
| scientific_process_live | false |
| scientific_teacher_tokens_completed | 100000000 |
| total_new_GPU_seconds | 270.0936576749955 |
| GPU_limit_seconds_including_probe | 900 |
| actual_UI.model.training_tokens | 10000007168 |
| actual_UI.model.update | 305176 |
| actual_UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| actual_UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| actual_UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_UI.scientific_process_absent | true |
| Base_adopted | false |
| Base_complete | false |
| protected_test_used | false |
| completion | "reports/phase6/condition_query_balance_comparison_completion.json" |

</details>

<details>
<summary>reports/phase6/condition_query_balance_comparison_completion.json — actual_same_parent_query_balanced100M_and_all80_complete_candidate_rejected</summary>

[原記録](../../reports/phase6/condition_query_balance_comparison_completion.json) ／ SHA256: `ef7ddc408cd4f8c67ea9b40b5967f7c6ee390bc0401dde09c23ee9c359e0f2ee` ／ 9,326 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_same_parent_query_balanced100M_and_all80_complete_candidate_rejected" |
| actual_scientific_process_absent | true |
| actual_identity.status | "complete" |
| actual_identity.GPU_elapsed_seconds | 253.21383405599045 |
| actual_identity.Base_adopted | false |
| actual_identity.protected_test_used | false |
| actual_identity.teachers | 99765470 |
| actual_identity.teacher_budget | 100000000 |
| actual_identity.source_teachers.web | 74823740 |
| actual_identity.source_teachers.story | 4988661 |
| actual_identity.source_teachers.ordinary_textbook | 9976547 |
| actual_identity.source_teachers.conditional_textbook | 9976522 |
| actual_identity.loss | 2.312191963195801 |
| checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-query-balance-comparison-20261006/query_balanced/training/checkpoint-00308244.pt" |
| checkpoint.checkpoint_sha256 | "001b12678273465d1468ae737a9a6b4c0c7d502ccd649c5dbb5446f834109a4e" |
| checkpoint.binding.config_sha256 | "aa65e594d47b996df3dbe3e7aa42466cfc3d13604e84a75afd8950c708ff0297" |
| checkpoint.binding.arm | "query_balanced" |
| checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| checkpoint.binding.parent.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| checkpoint.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoint.binding.teacher_goals.web | 75000000 |
| checkpoint.binding.teacher_goals.story | 5000000 |
| checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint.binding.optimizer_policy | "inherit" |
| checkpoint.binding.peak_lr | 0.0002 |
| checkpoint.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoint.binding.study_kind | "comparison_query_balance_same100M" |
| checkpoint.binding.sampler_policy | "Actual original Web parent cursor and fresh seed42 streams remain. Same2048 conditional IDs/order; only172 train queries/targets change, not heldout forms. Query words/target entities/lengths can differ; not pure position causality." |
| checkpoint.binding.outcome_weight | 1 |
| checkpoint.binding.positive_manifest_sha256 | "fd39c41e2ba270c104cb560c7a9a73ff8ea2f237132f02d4e137cfe8750ca987" |
| checkpoint.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoint.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.update | 308244 |
| checkpoint.tokens | 10100539392 |
| checkpoint.supervised_tokens | 10078838479 |
| checkpoint.additional_supervised_tokens | 100000000 |
| checkpoint.additional_input_tokens | 100532224 |
| checkpoint.source_teachers.web | 75000000 |
| checkpoint.source_teachers.story | 5000000 |
| checkpoint.source_teachers.ordinary_textbook | 10000000 |
| checkpoint.source_teachers.conditional_textbook | 10000000 |
| checkpoint.source_eos.web | 159044 |
| checkpoint.source_eos.story | 38240 |
| checkpoint.source_eos.ordinary_textbook | 74183 |
| checkpoint.source_eos.conditional_textbook | 234328 |
| checkpoint.source_input_tokens.web | 75183104 |
| checkpoint.source_input_tokens.story | 5039104 |
| checkpoint.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoint.source_input_tokens.conditional_textbook | 10234880 |
| checkpoint.source_focus_teachers.web | 0 |
| checkpoint.source_focus_teachers.story | 0 |
| checkpoint.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.source_focus_teachers.conditional_textbook | 1407426 |
| checkpoint.focus_teacher_tokens | 1407426 |
| checkpoint.focus_token_digest | "7fb17043657b5ac1ae6a0bfc526b60996429b232622157be785d1a4c18932a3b" |
| checkpoint.weighted_teacher_mass | 100000000 |
| checkpoint.outcome_weight | 1 |
| checkpoint.training_seconds | 160.27298541355412 |
| checkpoint.completed_at | "2026-10-06T05:12:57.070235Z" |
| new_scientific_teacher_tokens | 100000000 |
| new_scientific_input_tokens | 100532224 |
| scientific_optimizer_updates | 3068 |
| training_seconds | 160.27298541355412 |
| GPU_seconds | 253.21383405599045 |
| verification_GPU_seconds | 16.879823619005037 |
| total_new_GPU_seconds | 270.0936576749955 |
| verification_teacher_tokens | 1304156 |
| GPU_limit_seconds | 900 |
| reused_control_teachers | 100000000 |
| independent_learned_seed | false |
| summaries.control.BPB | 0.9909362016606469 |
| summaries.control.rates.eos | 34 |
| summaries.control.rates.repetition | 21 |
| summaries.control.rates.unicode_failure | 1 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 72 |
| summaries.control.relevance2 | 68 |
| summaries.control.coherent | 12 |
| summaries.control.appropriate | 26 |
| summaries.control.notes_sha256 | "3992ec51e542cfc38cbb57c68b43540400ae1a7f37b1729c7e5fee5292c12ccc" |
| summaries.control.additional_teacher_tokens | 100000000 |
| summaries.query_balanced.BPB | 0.9908565345182468 |
| summaries.query_balanced.rates.eos | 35 |
| summaries.query_balanced.rates.repetition | 25 |
| summaries.query_balanced.rates.unicode_failure | 1 |
| summaries.query_balanced.rates.role_leak | 0 |
| summaries.query_balanced.rates.empty | 0 |
| summaries.query_balanced.grammar2 | 74 |
| summaries.query_balanced.relevance2 | 69 |
| summaries.query_balanced.coherent | 10 |
| summaries.query_balanced.appropriate | 24 |
| summaries.query_balanced.notes_sha256 | "9814abaac7e6b5878ec69e9e3237434781d3df1819a095908f0362aea0da4a9c" |
| summaries.query_balanced.additional_teacher_tokens | 100000000 |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | false |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| mechanism_screen.control.both_correct | 1 |
| mechanism_screen.candidate.both_correct | 4 |
| mechanism_screen.passed | false |
| mechanism_screen.secondary_only | true |
| retained_source_checks.three_unchanged_sources_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| exact_prior_notes_reused | 37 |
| eligible_for_final_Base_validation | false |
| Base_adopted | false |
| Base_complete | false |
| protected_test_used | false |
| archive.bytes | 3953663 |
| actual_UI.model.training_tokens | 10000007168 |
| actual_UI.model.update | 305176 |
| actual_UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| actual_UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| actual_UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_UI.scientific_process_absent | true |

</details>

<details>
<summary>reports/phase6/condition_query_balance_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_query_balance_comparison_evidence_manifest.json) ／ SHA256: `9ec7285542c323b4f0a2da3844c589fc60dbd7baa8651444c4f777500e42189a` ／ 70,486 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 21370074 |
| archive.bytes | 3953663 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_query_balance_comparison_review.json — query_balanced100M_all80_and_reused_original_Web100M_reviewed</summary>

[原記録](../../reports/phase6/condition_query_balance_comparison_review.json) ／ SHA256: `825912e1e51db49d453912e5f431c49b9e31509115e5079e65a32e746310ca38` ／ 12,198 bytes

| 原キー | 保存値 |
|---|---|
| status | "query_balanced100M_all80_and_reused_original_Web100M_reviewed" |
| summaries.control.BPB | 0.9909362016606469 |
| summaries.control.rates.eos | 34 |
| summaries.control.rates.repetition | 21 |
| summaries.control.rates.unicode_failure | 1 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 72 |
| summaries.control.relevance2 | 68 |
| summaries.control.coherent | 12 |
| summaries.control.appropriate | 26 |
| summaries.control.notes_sha256 | "3992ec51e542cfc38cbb57c68b43540400ae1a7f37b1729c7e5fee5292c12ccc" |
| summaries.control.additional_teacher_tokens | 100000000 |
| summaries.query_balanced.BPB | 0.9908565345182468 |
| summaries.query_balanced.rates.eos | 35 |
| summaries.query_balanced.rates.repetition | 25 |
| summaries.query_balanced.rates.unicode_failure | 1 |
| summaries.query_balanced.rates.role_leak | 0 |
| summaries.query_balanced.rates.empty | 0 |
| summaries.query_balanced.grammar2 | 74 |
| summaries.query_balanced.relevance2 | 69 |
| summaries.query_balanced.coherent | 10 |
| summaries.query_balanced.appropriate | 24 |
| summaries.query_balanced.notes_sha256 | "9814abaac7e6b5878ec69e9e3237434781d3df1819a095908f0362aea0da4a9c" |
| summaries.query_balanced.additional_teacher_tokens | 100000000 |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | false |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | false |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | false |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.three_unchanged_sources_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| mechanism_screen.control.both_correct | 1 |
| mechanism_screen.candidate.both_correct | 4 |
| mechanism_screen.passed | false |
| mechanism_screen.secondary_only | true |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.control.sum_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.control.sum_log_likelihood.all128.both_correct | 57 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.9296875 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 55 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.34375 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.both_correct | 57 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9375 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 56 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.3359375 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 1 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 61 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 45 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 57 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.359375 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 4 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 38 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| transfer_aggregates.query_balanced.sum_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.query_balanced.sum_log_likelihood.all128.both_correct | 52 |
| transfer_aggregates.query_balanced.sum_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| transfer_aggregates.query_balanced.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer_aggregates.query_balanced.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.query_balanced.sum_log_likelihood.structural_holdout.both_correct | 4 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.all128.both_correct | 52 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.both_correct | 50 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.accuracy | 0.390625 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.all128.accuracy | 0.640625 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.all128.both_correct | 53 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.all128.same_unique_candidate | 58 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.both_correct | 50 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.accuracy | 0.3984375 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| transfer_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| retention_aggregates.control.sum_log_likelihood.all128.accuracy | 0.69921875 |
| retention_aggregates.control.sum_log_likelihood.all128.both_correct | 60 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 18 |
| retention_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| retention_aggregates.control.mean_token_log_likelihood.all128.both_correct | 65 |
| retention_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 55 |
| retention_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 56 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 21 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 42 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 62 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 59 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8125 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 42 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 56 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 39 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention_aggregates.query_balanced.sum_log_likelihood.all128.accuracy | 0.703125 |
| retention_aggregates.query_balanced.sum_log_likelihood.all128.both_correct | 60 |
| retention_aggregates.query_balanced.sum_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| retention_aggregates.query_balanced.sum_log_likelihood.lexical_holdout.both_correct | 41 |
| retention_aggregates.query_balanced.sum_log_likelihood.structural_holdout.accuracy | 0.609375 |
| retention_aggregates.query_balanced.sum_log_likelihood.structural_holdout.both_correct | 19 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.all128.accuracy | 0.71875 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.all128.both_correct | 64 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.all128.same_unique_candidate | 56 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.all128.aligned_context_margin_shift | 96 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 19 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention_aggregates.query_balanced.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 41 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.all128.both_correct | 63 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.all128.same_unique_candidate | 57 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.both_correct | 42 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 19 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.accuracy | 0.625 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 38 |
| retention_aggregates.query_balanced.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 42 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1304156 |
| GPU_seconds | 253.21383405599045 |
| verification_GPU_seconds | 16.879823619005037 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "One learned seed; nonblind repeated fixeddev. Three source streams and original Web cursor are unchanged. Only172 comparison training queries and targets change; question words, target entities and per-document token lengths can differ, not a pure position intervention. Same shared-generator bridge is local; old128 retention overlaps training forms. Independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/condition_query_balance_content_review.json — None</summary>

[原記録](../../reports/phase6/condition_query_balance_content_review.json) ／ SHA256: `f88c083fafe4a798b778945c9bb672f5d7f980b840b64d76a6d13e3ed36c0af3` ／ 722 bytes

| 原キー | 保存値 |
|---|---|
| weak_documents | 0 |
| unresolved_grammar_documents | 0 |
| paired_states_consistent | true |
| training_pool_accepted | true |
| notes_sha256 | "3ce83f54349fe4af19081a55c41d7b958409b397c976db81055a32f78d14b55b" |
| Base_adopted | false |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_query_balance_notes.json — None</summary>

[原記録](../../reports/phase6/condition_query_balance_notes.json) ／ SHA256: `9814abaac7e6b5878ec69e9e3237434781d3df1819a095908f0362aea0da4a9c` ／ 26,803 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/condition_query_balance_proposal.json — single_evidence_defined_train_query_intervention_pending_material_preparation</summary>

[原記録](../../reports/phase6/condition_query_balance_proposal.json) ／ SHA256: `97f605dff158d1fc5d06180c0ceb973515dbe5db156b9ad0efec516572b4b9c6` ／ 7,268 bytes

| 原キー | 保存値 |
|---|---|
| status | "single_evidence_defined_train_query_intervention_pending_material_preparation" |
| observed.structural_comparison_both_correct | "1/32;22/32 both reversed; positive context response3/32" |
| observed.normalized_comparison_both_correct | "0/32 token and byte normalization; equal-token-length0/21" |
| observed.gold_dev_EOS | "2.361645-&gt;2.291431 mean NLL;143/256 improved; candidate requests contain noEOS" |
| hypothesis | "The accepted local comparison source permits a last-mentioned-entity heuristic on88.9% of its examples; all targets select longer. A balanced requested-property intervention can remove much of this correlation without exposing heldout grammar. This is an evidence-guided hypothesis, not proof of the model decision rule or sole Base failure cause." |
| seed | 2026100671 |
| changed_documents | 172 |
| CPU_limit_seconds | 120 |
| tokenizer.path | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer.sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_teacher_tokens_each | 100000000 |
| new_scientific_teacher_tokens | 100000000 |
| new_GPU_ceiling_seconds | 900 |
| measured_budget_condition | "Own actual same-source continuous/resumed4 vs2+2 full optimizer/model/scheduler/RNG/sampler/history/source digest checks, and32 stable finite timings. Include all verification/warmup/save/evaluation/read-only probes within900 cumulative GPU seconds. Do not launch science until measurement supports the fixed100M experiment." |
| completion | "Terminal durable job/source/config/PID/budget/history/full checkpoint/evaluations/all80 notes/review/archive/UI restored/verified local commit. If candidate fails, preserve failure and do not automatically extend, sweep ratio/query variants/weights/LR, scan favorable checkpoints or relax gates. If quality passes, independent learned seed/full dev/protected test/adoption remain required before Base completion." |
| Base_adopted | false |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition_relation_active_job.json — actual100M_complete_all80_failed_original_quality_not_active</summary>

[原記録](../../reports/phase6/condition_relation_active_job.json) ／ SHA256: `6980e6617585f2c02120806866d19d021889a92f12f2418e6cdbc490d784f4ba` ／ 4,915 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual100M_complete_all80_failed_original_quality_not_active" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 236.8989359900006 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 99923211 |
| job.teacher_budget | 100000000 |
| job.source_teachers.web | 74941068 |
| job.source_teachers.story | 4996799 |
| job.source_teachers.ordinary_textbook | 9992813 |
| job.source_teachers.conditional_textbook | 9992531 |
| job.loss | 2.380946397781372 |
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
| verification_teachers | 1297767 |
| verification_GPU_seconds | 12.121268843999133 |
| measured_timing.steady_step_seconds | 0.04902140950434841 |
| measured_timing.teachers_per_update | 32443.78125 |
| measured_timing.estimated_updates | 3083 |
| measured_timing.warmup_seconds | 1.3394289619463962 |
| measured_timing.save_seconds | 2.530076933966484 |
| measured_timing.estimated_training_seconds | 155.00251139781903 |
| estimated_science_seconds | 551.5032648171648 |
| total_GPU_limit | 900 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| checkpoint_model_Adam_scheduler_RNG_sampler_and_counters_saved | true |
| Base_adopted | false |
| protected_test_used | false |
| completion | "reports/phase6/condition_relation_comparison_completion.json" |

</details>

<details>
<summary>reports/phase6/condition_relation_comparison_completion.json — actual_relation100M_original80_bridge128_retention128_complete_Base_quality_unmet</summary>

[原記録](../../reports/phase6/condition_relation_comparison_completion.json) ／ SHA256: `f98ab54af48bd462e7a1646fb95ed4b7d96e07d82f9f4f724f1c860ca825fd5f` ／ 27,939 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_relation100M_original80_bridge128_retention128_complete_Base_quality_unmet" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 236.8989359900006 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 99923211 |
| job.teacher_budget | 100000000 |
| job.source_teachers.web | 74941068 |
| job.source_teachers.story | 4996799 |
| job.source_teachers.ordinary_textbook | 9992813 |
| job.source_teachers.conditional_textbook | 9992531 |
| job.loss | 2.380946397781372 |
| pairs.sha256 | "2d254890b91e18b5e9a459079d996e1eb4a60124ffd1e1c180c889844995da13" |
| pairs.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition_relation_condition_pair_analysis.json" |
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.control.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.control.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.control.binding.arm | "curriculum" |
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
| checkpoints.control.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.control.update | 65249 |
| checkpoints.control.tokens | 2138079232 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 101023744 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 243066 |
| checkpoints.control.source_input_tokens.web | 75666432 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.control.focus_teacher_tokens | 1460032 |
| checkpoints.control.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 152.96801666589454 |
| checkpoints.control.completed_at | "2026-10-06T03:11:09.066152Z" |
| checkpoints.relation.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-relation-comparison-20261006/relation/training/checkpoint-00065249.pt" |
| checkpoints.relation.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| checkpoints.relation.binding.config_sha256 | "248651b0c7a25b3ab9950fce40f0e40a57b21a386201cf47c87eef4717911fac" |
| checkpoints.relation.binding.arm | "relation" |
| checkpoints.relation.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.relation.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.relation.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.relation.binding.teacher_goals.web | 75000000 |
| checkpoints.relation.binding.teacher_goals.story | 5000000 |
| checkpoints.relation.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.relation.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.relation.binding.optimizer_policy | "inherit" |
| checkpoints.relation.binding.peak_lr | 0.0002 |
| checkpoints.relation.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.relation.binding.study_kind | "conditional_relation_language_bridge_100M" |
| checkpoints.relation.binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| checkpoints.relation.binding.outcome_weight | 1 |
| checkpoints.relation.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.relation.update | 65249 |
| checkpoints.relation.tokens | 2138079232 |
| checkpoints.relation.supervised_tokens | 2120000000 |
| checkpoints.relation.additional_supervised_tokens | 100000000 |
| checkpoints.relation.additional_input_tokens | 101023744 |
| checkpoints.relation.source_teachers.web | 75000000 |
| checkpoints.relation.source_teachers.story | 5000000 |
| checkpoints.relation.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.relation.source_teachers.conditional_textbook | 10000000 |
| checkpoints.relation.source_eos.web | 656229 |
| checkpoints.relation.source_eos.story | 38240 |
| checkpoints.relation.source_eos.ordinary_textbook | 74183 |
| checkpoints.relation.source_eos.conditional_textbook | 234328 |
| checkpoints.relation.source_input_tokens.web | 75674624 |
| checkpoints.relation.source_input_tokens.story | 5039104 |
| checkpoints.relation.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.relation.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.relation.source_focus_teachers.web | 0 |
| checkpoints.relation.source_focus_teachers.story | 0 |
| checkpoints.relation.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.relation.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.relation.focus_teacher_tokens | 1407427 |
| checkpoints.relation.focus_token_digest | "c9002bb395ed970e032471a733915ff40ba9febb6866e9ed3df9a57fbc146cc4" |
| checkpoints.relation.weighted_teacher_mass | 100000000 |
| checkpoints.relation.outcome_weight | 1 |
| checkpoints.relation.training_seconds | 152.45355427256436 |
| checkpoints.relation.completed_at | "2026-10-06T03:30:00.690003Z" |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| additional_input_tokens | 101023744 |
| new_updates | 3083 |
| actual_training_seconds | 152.45355427256436 |
| verification_updates | 40 |
| verification_teacher_tokens | 1297767 |
| scientific_GPU_seconds | 236.8989359900006 |
| verification_GPU_seconds | 12.121268843999133 |
| total_GPU_seconds | 249.02020483399974 |
| GPU_ceiling_seconds | 900 |
| summaries.control.BPB | 1.1302498889302441 |
| summaries.control.rates.eos | 45 |
| summaries.control.rates.repetition | 17 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 60 |
| summaries.control.relevance2 | 68 |
| summaries.control.coherent | 14 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.control.conditional_source_documents | 2048 |
| summaries.control.generated_serialized_tokens | 86309 |
| summaries.control.notes_sha256 | "b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6" |
| summaries.control.Base_adopted | false |
| summaries.relation.BPB | 1.13038244113982 |
| summaries.relation.rates.eos | 35 |
| summaries.relation.rates.repetition | 21 |
| summaries.relation.rates.unicode_failure | 0 |
| summaries.relation.rates.role_leak | 0 |
| summaries.relation.rates.empty | 0 |
| summaries.relation.grammar2 | 60 |
| summaries.relation.relevance2 | 68 |
| summaries.relation.coherent | 10 |
| summaries.relation.appropriate | 21 |
| summaries.relation.new_teacher_tokens | 100000000 |
| summaries.relation.source_teacher_tokens.web | 75000000 |
| summaries.relation.source_teacher_tokens.story | 5000000 |
| summaries.relation.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.relation.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.relation.conditional_source_documents | 2048 |
| summaries.relation.generated_serialized_tokens | 89446 |
| summaries.relation.notes_sha256 | "bfb81e36fed0748573541e7d0c128f312ff49422ea0988b93617f20b702da13e" |
| summaries.relation.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| bridge_transfer.parent2B.sum_log_likelihood.all128.accuracy | 0.5 |
| bridge_transfer.parent2B.sum_log_likelihood.all128.both_correct | 7 |
| bridge_transfer.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.484375 |
| bridge_transfer.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 3 |
| bridge_transfer.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| bridge_transfer.parent2B.sum_log_likelihood.structural_holdout.both_correct | 4 |
| bridge_transfer.parent2B.mean_token_log_likelihood.all128.families | 128 |
| bridge_transfer.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| bridge_transfer.parent2B.mean_token_log_likelihood.all128.both_correct | 9 |
| bridge_transfer.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 113 |
| bridge_transfer.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| bridge_transfer.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5078125 |
| bridge_transfer.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 5 |
| bridge_transfer.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| bridge_transfer.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| bridge_transfer.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| bridge_transfer.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| bridge_transfer.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| bridge_transfer.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 55 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.5546875 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.all128.both_correct | 21 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 100 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 13 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| bridge_transfer.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 53 |
| bridge_transfer.curriculum100M.sum_log_likelihood.all128.accuracy | 0.578125 |
| bridge_transfer.curriculum100M.sum_log_likelihood.all128.both_correct | 29 |
| bridge_transfer.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| bridge_transfer.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 11 |
| bridge_transfer.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| bridge_transfer.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 18 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.58984375 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.all128.both_correct | 32 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5390625 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 14 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 41 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 46 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.640625 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| bridge_transfer.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.609375 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 36 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 84 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 94 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 38 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 45 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.640625 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| bridge_transfer.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| bridge_transfer.relation100M.sum_log_likelihood.all128.accuracy | 0.67578125 |
| bridge_transfer.relation100M.sum_log_likelihood.all128.both_correct | 50 |
| bridge_transfer.relation100M.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| bridge_transfer.relation100M.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| bridge_transfer.relation100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| bridge_transfer.relation100M.sum_log_likelihood.structural_holdout.both_correct | 18 |
| bridge_transfer.relation100M.mean_token_log_likelihood.all128.families | 128 |
| bridge_transfer.relation100M.mean_token_log_likelihood.all128.accuracy | 0.68359375 |
| bridge_transfer.relation100M.mean_token_log_likelihood.all128.both_correct | 51 |
| bridge_transfer.relation100M.mean_token_log_likelihood.all128.same_unique_candidate | 73 |
| bridge_transfer.relation100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 114 |
| bridge_transfer.relation100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.relation100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| bridge_transfer.relation100M.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| bridge_transfer.relation100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| bridge_transfer.relation100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge_transfer.relation100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.relation100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| bridge_transfer.relation100M.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| bridge_transfer.relation100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| bridge_transfer.relation100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.all128.families | 128 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.all128.accuracy | 0.69140625 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.all128.both_correct | 54 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 114 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7734375 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 35 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 29 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| bridge_transfer.relation100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.parent2B.sum_log_likelihood.all128.accuracy | 0.5078125 |
| retention.parent2B.sum_log_likelihood.all128.both_correct | 5 |
| retention.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| retention.parent2B.sum_log_likelihood.structural_holdout.both_correct | 1 |
| retention.parent2B.mean_token_log_likelihood.all128.families | 128 |
| retention.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| retention.parent2B.mean_token_log_likelihood.all128.both_correct | 6 |
| retention.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| retention.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| retention.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| retention.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| retention.parent2B.mean_byte_log_likelihood.all128.both_correct | 13 |
| retention.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| retention.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| retention.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| retention.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| retention.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.curriculum100M.sum_log_likelihood.all128.accuracy | 0.7109375 |
| retention.curriculum100M.sum_log_likelihood.all128.both_correct | 63 |
| retention.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| retention.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| retention.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| retention.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.mean_token_log_likelihood.all128.both_correct | 66 |
| retention.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| retention.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| retention.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| retention.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| retention.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 64 |
| retention.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| retention.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.relation100M.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.relation100M.sum_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.sum_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.relation100M.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.mean_token_log_likelihood.all128.families | 128 |
| retention.relation100M.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.mean_token_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.mean_token_log_likelihood.all128.same_unique_candidate | 78 |
| retention.relation100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.relation100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.relation100M.mean_byte_log_likelihood.all128.families | 128 |
| retention.relation100M.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.mean_byte_log_likelihood.all128.both_correct | 44 |
| retention.relation100M.mean_byte_log_likelihood.all128.same_unique_candidate | 80 |
| retention.relation100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention.relation100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.relation100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| related_checks | "Source4CPU tests1.16s, trainer/accounting/budget4CPU tests2.09s, actualCUDA32 checks and first4 timing trajectory; all passed. CPU ordinary3 replay6.479s." |
| archive.bytes | 3287540 |
| checkpoint_tensors_copied_to_Windows | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| original_UI.server.status | "running" |
| original_UI.server.additional_training_tokens | 0 |
| original_UI.server.model.training_tokens | 10000007168 |
| original_UI.server.model.update | 305176 |
| original_UI.server.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.server.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.server.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| independent_learningseed_used | false |
| requested_five_steps_complete | false |
| limitations | "One learned seed, nonblind judgments, repeatedly inspected fixeddev; local generator probes are not independent natural-language quality. Only negation/comparison language replaced, with token lengths/lexical/EOS-density effects. Original128 are retention, not new grammar holdouts. OriginalWeb BPB reference0.971570 comes from a historical10B arm; final1percent guard is retained, not an equal-budget100M control." |

</details>

<details>
<summary>reports/phase6/condition_relation_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_relation_comparison_evidence_manifest.json) ／ SHA256: `9ef40592538b8e2a49b4ae33fcd55b117177084bbbcd4d1fb90ca4f5fdae0a09` ／ 61,141 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 16226705 |
| archive.bytes | 3287540 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_relation_comparison_review.json — actual_relation100M_all80_bridge128_retention128_and_reused_curriculum100M_complete</summary>

[原記録](../../reports/phase6/condition_relation_comparison_review.json) ／ SHA256: `1eeba0f26a076ca1bd5a15a717c1066f935375e3a83ef5b6dd3d8bade1a9e5cc` ／ 16,832 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_relation100M_all80_bridge128_retention128_and_reused_curriculum100M_complete" |
| summaries.control.BPB | 1.1302498889302441 |
| summaries.control.rates.eos | 45 |
| summaries.control.rates.repetition | 17 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 60 |
| summaries.control.relevance2 | 68 |
| summaries.control.coherent | 14 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.control.conditional_source_documents | 2048 |
| summaries.control.generated_serialized_tokens | 86309 |
| summaries.control.notes_sha256 | "b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6" |
| summaries.control.Base_adopted | false |
| summaries.relation.BPB | 1.13038244113982 |
| summaries.relation.rates.eos | 35 |
| summaries.relation.rates.repetition | 21 |
| summaries.relation.rates.unicode_failure | 0 |
| summaries.relation.rates.role_leak | 0 |
| summaries.relation.rates.empty | 0 |
| summaries.relation.grammar2 | 60 |
| summaries.relation.relevance2 | 68 |
| summaries.relation.coherent | 10 |
| summaries.relation.appropriate | 21 |
| summaries.relation.new_teacher_tokens | 100000000 |
| summaries.relation.source_teacher_tokens.web | 75000000 |
| summaries.relation.source_teacher_tokens.story | 5000000 |
| summaries.relation.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.relation.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.relation.conditional_source_documents | 2048 |
| summaries.relation.generated_serialized_tokens | 89446 |
| summaries.relation.notes_sha256 | "bfb81e36fed0748573541e7d0c128f312ff49422ea0988b93617f20b702da13e" |
| summaries.relation.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
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
| transfer_aggregates.parent2B.sum_log_likelihood.all128.accuracy | 0.5 |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.both_correct | 7 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.484375 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 3 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.both_correct | 9 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 113 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 5 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 55 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.5546875 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.both_correct | 21 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 100 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 13 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 53 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.accuracy | 0.578125 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.both_correct | 29 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.58984375 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.both_correct | 32 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5390625 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 14 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 41 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.609375 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 36 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 84 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 94 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 38 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 45 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| transfer_aggregates.relation100M.sum_log_likelihood.all128.accuracy | 0.67578125 |
| transfer_aggregates.relation100M.sum_log_likelihood.all128.both_correct | 50 |
| transfer_aggregates.relation100M.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer_aggregates.relation100M.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer_aggregates.relation100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.relation100M.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.all128.accuracy | 0.68359375 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.all128.both_correct | 51 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.all128.same_unique_candidate | 73 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| transfer_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.all128.accuracy | 0.69140625 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.all128.both_correct | 54 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7734375 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 35 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 29 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| ordinary_stream_checks.target_sha256 | true |
| ordinary_stream_checks.teachers | true |
| ordinary_stream_checks.EOS | true |
| ordinary_stream_checks.body_bytes | true |
| retention_aggregates.parent2B.sum_log_likelihood.all128.accuracy | 0.5078125 |
| retention_aggregates.parent2B.sum_log_likelihood.all128.both_correct | 5 |
| retention_aggregates.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention_aggregates.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| retention_aggregates.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| retention_aggregates.parent2B.sum_log_likelihood.structural_holdout.both_correct | 1 |
| retention_aggregates.parent2B.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| retention_aggregates.parent2B.mean_token_log_likelihood.all128.both_correct | 6 |
| retention_aggregates.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| retention_aggregates.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| retention_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| retention_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| retention_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.all128.both_correct | 13 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention_aggregates.curriculum100M.sum_log_likelihood.all128.accuracy | 0.7109375 |
| retention_aggregates.curriculum100M.sum_log_likelihood.all128.both_correct | 63 |
| retention_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| retention_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| retention_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 20 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.all128.both_correct | 66 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| retention_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 64 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.relation100M.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention_aggregates.relation100M.sum_log_likelihood.all128.both_correct | 45 |
| retention_aggregates.relation100M.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention_aggregates.relation100M.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.relation100M.sum_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention_aggregates.relation100M.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention_aggregates.relation100M.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.relation100M.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.relation100M.mean_token_log_likelihood.all128.both_correct | 45 |
| retention_aggregates.relation100M.mean_token_log_likelihood.all128.same_unique_candidate | 78 |
| retention_aggregates.relation100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention_aggregates.relation100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention_aggregates.relation100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.all128.both_correct | 44 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.all128.same_unique_candidate | 80 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.relation100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1297767 |
| GPU_seconds | 236.8989359900006 |
| verification_GPU_seconds | 12.121268843999133 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| limitations | "One learned seed, nonblind judgments, repeatedly inspected fixeddev; local generator probes are not independent natural-language quality. Only negation/comparison language replaced, with token lengths/lexical/EOS-density effects. Original128 are retention, not new grammar holdouts. OriginalWeb BPB reference0.971570 comes from a historical10B arm; final1percent guard is retained, not an equal-budget100M control." |

</details>

<details>
<summary>reports/phase6/condition_relation_condition_pair_analysis.json — actual_relation100M_fixeddev_condition_pairs_reused</summary>

[原記録](../../reports/phase6/condition_relation_condition_pair_analysis.json) ／ SHA256: `2d254890b91e18b5e9a459079d996e1eb4a60124ffd1e1c180c889844995da13` ／ 185,891 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_relation100M_fixeddev_condition_pairs_reused" |
| models.relation100M.causality.accuracy | 0.6875 |
| models.relation100M.causality.both_correct | 6 |
| models.relation100M.causality.neither_correct | 0 |
| models.relation100M.comparison.accuracy | 0.46875 |
| models.relation100M.comparison.both_correct | 0 |
| models.relation100M.comparison.neither_correct | 1 |
| models.relation100M.coreference.accuracy | 0.53125 |
| models.relation100M.coreference.both_correct | 1 |
| models.relation100M.coreference.neither_correct | 0 |
| models.relation100M.negation.accuracy | 0.875 |
| models.relation100M.negation.both_correct | 12 |
| models.relation100M.negation.neither_correct | 0 |
| models.relation100M.quantity.accuracy | 0.5625 |
| models.relation100M.quantity.both_correct | 3 |
| models.relation100M.quantity.neither_correct | 1 |
| models.relation100M.time.accuracy | 0.5 |
| models.relation100M.time.both_correct | 1 |
| models.relation100M.time.neither_correct | 1 |
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
| references.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| references.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.021571690012933686 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Same repeatedly inspected fixeddev96 families and one learned seed. Descriptive context response; not independent fluent continuation quality, causal diagnosis or certified10M capacity. Local generator probes remain separate." |

</details>

<details>
<summary>reports/phase6/condition_relation_language_content_review.json — all64_relation_language_source_review_complete</summary>

[原記録](../../reports/phase6/condition_relation_language_content_review.json) ／ SHA256: `a929eeda49d4ed13198090c597a903149910a654f425ecd464ade8479622b825` ／ 24,593 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_relation_language_source_review_complete" |
| weak_documents | 0 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 0 |
| training_pool_accepted | true |
| notes_sha256 | "8fc03ade52cb710ef1da5558124c708d2975e00e7638dc03d82f2da0aef3f599" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind64/32 pairs; local authored material, not independent human or model quality proof." |

</details>

<details>
<summary>reports/phase6/condition_relation_language_notes.json — None</summary>

[原記録](../../reports/phase6/condition_relation_language_notes.json) ／ SHA256: `bfb81e36fed0748573541e7d0c128f312ff49422ea0988b93617f20b702da13e` ／ 18,289 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |

</details>
