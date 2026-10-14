# 実行管理・後続準備・その他 — 3/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/base_next_two_token_comparison_completion.json — next_two100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_next_two_token_comparison_completion.json) ／ SHA256: `88f53f937394d1bec453ba658dac25310d8d888ec7959443ba3e7b0692e2e411` ／ 6,748 bytes

| 原キー | 保存値 |
|---|---|
| status | "next_two100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_next_two_positions | 99150521 |
| total_scientific_label_positions | 199150521 |
| scientific_updates | 17698 |
| GPU_occupancy_seconds | 1571.6345395829994 |
| GPU_cap_seconds | 3793 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-next-two-token-comparison-20261007/next_two/checkpoint-00017698.pt" |
| checkpoint_sha256 | "4d76e678f57d61fc6c6f1617b322dd04f6846ca69a7568cb70cec706c0a0b024" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_next_two_token_notes.json" |
| notes.sha256 | "f6a0e318a48f84a50f38564747cbc89fc7a34cc85e0cbfa0c58f4a89d0fd0068" |
| reused_control_GPU_seconds | 0 |
| accounting.completed_updates | 17698 |
| accounting.optimizer_updates | 17698 |
| accounting.auxiliary_optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.supervised_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 0 |
| accounting.auxiliary_pairs | 0 |
| accounting.physical_input_tokens | 370838917 |
| accounting.original_body_bytes | 405882136 |
| accounting.next_two_teacher_positions | 99150521 |
| accounting.next_two_EOS_targets | 844255 |
| accounting.next_two_body_bytes | 402501249 |
| accounting.auxiliary_physical_hidden_positions | 370838917 |
| accounting.source_next_two_teachers.web | 74337872 |
| accounting.source_next_two_teachers.textbook | 19850872 |
| accounting.source_next_two_teachers.story | 4961777 |
| accounting.source_next_two_EOS.web | 657415 |
| accounting.source_next_two_EOS.textbook | 148618 |
| accounting.source_next_two_EOS.story | 38222 |
| summaries.next_two.BPB | 1.000046907103982 |
| summaries.next_two.rates.eos | 19 |
| summaries.next_two.rates.repetition | 45 |
| summaries.next_two.rates.unicode_failure | 0 |
| summaries.next_two.rates.role_leak | 0 |
| summaries.next_two.rates.empty | 0 |
| summaries.next_two.grammar2 | 45 |
| summaries.next_two.relevance2 | 23 |
| summaries.next_two.coherent | 1 |
| summaries.next_two.appropriate | 1 |
| summaries.next_two.notes_sha256 | "f6a0e318a48f84a50f38564747cbc89fc7a34cc85e0cbfa0c58f4a89d0fd0068" |
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
| fixed_next_two_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 109070455 |
| archive.compressed_bundle.bytes | 46920058 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_next_two_token_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_next_two_token_comparison_evidence_manifest.json) ／ SHA256: `adcc0f73b126da07332121da2f1006a3f46c117448da3fc4d391cc8a2b983898` ／ 9,819 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_next_two_token_comparison_review.json — new80_and_reused80_next_two_comparison_reviewed</summary>

[原記録](../../reports/phase6/base_next_two_token_comparison_review.json) ／ SHA256: `b3589e13181de3a87db5da396bccf4514cade6e6a4ea27c822cba8ffed5f7c65` ／ 12,380 bytes

| 原キー | 保存値 |
|---|---|
| status | "new80_and_reused80_next_two_comparison_reviewed" |
| summaries.next_two.BPB | 1.000046907103982 |
| summaries.next_two.rates.eos | 19 |
| summaries.next_two.rates.repetition | 45 |
| summaries.next_two.rates.unicode_failure | 0 |
| summaries.next_two.rates.role_leak | 0 |
| summaries.next_two.rates.empty | 0 |
| summaries.next_two.grammar2 | 45 |
| summaries.next_two.relevance2 | 23 |
| summaries.next_two.coherent | 1 |
| summaries.next_two.appropriate | 1 |
| summaries.next_two.notes_sha256 | "f6a0e318a48f84a50f38564747cbc89fc7a34cc85e0cbfa0c58f4a89d0fd0068" |
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
| strong_and_matched_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.CE.checks.EOS_nonworsening | true |
| strong_and_matched_quality.CE.checks.repetition_nonworsening | true |
| strong_and_matched_quality.CE.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.CE.checks.BPB_gate | true |
| strong_and_matched_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.CE.passed | false |
| strong_and_matched_quality.strong_staged.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.strong_staged.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.strong_staged.checks.EOS_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.repetition_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.strong_staged.checks.BPB_gate | true |
| strong_and_matched_quality.strong_staged.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.00155974459013704 |
| paired_common_byte_BPB.CE.ci95 | [0.0012701265474345657, 0.001840494489296493] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.000046907103982 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0015621078053825 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "next_two minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.next_two.exact_content_pair_clusters | 96 |
| exact_content_semantics.next_two.original_nominal_accuracy.point | 0.609375 |
| exact_content_semantics.next_two.original_nominal_accuracy.ci95 | [0.5625, 0.65625] |
| exact_content_semantics.next_two.original_nominal_accuracy.units | 96 |
| exact_content_semantics.next_two.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.next_two.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.next_two.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.next_two.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.next_two.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.content_cluster_accuracy.point | 0.609375 |
| exact_content_semantics.next_two.content_cluster_accuracy.ci95 | [0.5625, 0.65625] |
| exact_content_semantics.next_two.content_cluster_accuracy.units | 96 |
| exact_content_semantics.next_two.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.next_two.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.next_two.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.next_two.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.next_two.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.both_contexts_hard_correct.point | 0.25 |
| exact_content_semantics.next_two.both_contexts_hard_correct.ci95 | [0.16666666666666666, 0.3333333333333333] |
| exact_content_semantics.next_two.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.next_two.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.next_two.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.next_two.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.next_two.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.next_two.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.causality.seed | 42 |
| exact_content_semantics.next_two.categories.causality.repetitions | 2000 |
| exact_content_semantics.next_two.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.comparison.seed | 42 |
| exact_content_semantics.next_two.categories.comparison.repetitions | 2000 |
| exact_content_semantics.next_two.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.coreference.seed | 42 |
| exact_content_semantics.next_two.categories.coreference.repetitions | 2000 |
| exact_content_semantics.next_two.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.negation.seed | 42 |
| exact_content_semantics.next_two.categories.negation.repetitions | 2000 |
| exact_content_semantics.next_two.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.quantity.seed | 42 |
| exact_content_semantics.next_two.categories.quantity.repetitions | 2000 |
| exact_content_semantics.next_two.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.next_two.categories.time.seed | 42 |
| exact_content_semantics.next_two.categories.time.repetitions | 2000 |
| exact_content_semantics.next_two.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | -0.015625 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.041666666666666664, 0.005208333333333333] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 17698 |
| accounting.optimizer_updates | 17698 |
| accounting.auxiliary_optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.supervised_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 0 |
| accounting.auxiliary_pairs | 0 |
| accounting.physical_input_tokens | 370838917 |
| accounting.original_body_bytes | 405882136 |
| accounting.next_two_teacher_positions | 99150521 |
| accounting.next_two_EOS_targets | 844255 |
| accounting.next_two_body_bytes | 402501249 |
| accounting.auxiliary_physical_hidden_positions | 370838917 |
| accounting.source_next_two_teachers.web | 74337872 |
| accounting.source_next_two_teachers.textbook | 19850872 |
| accounting.source_next_two_teachers.story | 4961777 |
| accounting.source_next_two_EOS.web | 657415 |
| accounting.source_next_two_EOS.textbook | 148618 |
| accounting.source_next_two_EOS.story | 38222 |
| history.committed_updates | 17698 |
| history.optimizer_updates | 17698 |
| history.observed_completed_attempt_updates | 17698 |
| history.auxiliary_optimizer_updates | 17698 |
| history.raw_metrics./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-next-two-token-comparison-20261007/next_two/metrics-701073-20668823.jsonl | "1d97e80c6de300c4aa5c052ec5a2d7886e2eff44a9d5ceaf8a1bd37bc9201149" |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.auxiliary_input_tokens | true |
| common_CE_checks.CE.auxiliary_pairs | true |
| common_CE_checks.CE.physical_input_tokens | true |
| common_CE_checks.CE.full_sampler | true |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 100000000 |
| reused_control_GPU_seconds | 0 |
| probe_verification_updates | 48 |
| probe_verification_CE_teachers | 279240 |
| probe_verification_next_two_positions | 253920 |
| scientific_next_two_positions | 99150521 |
| total_scientific_label_positions | 199150521 |
| GPU_occupancy_seconds | 1571.6345395829994 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "Single learned seed, repeated nonblind DEV, same native parameters/CE input and teacher stream; additional future gold positions, train-only parameters and GPU overhead differ; not equal-total-label efficiency. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored." |

</details>

<details>
<summary>reports/phase6/base_next_two_token_content_review.json — None</summary>

[原記録](../../reports/phase6/base_next_two_token_content_review.json) ／ SHA256: `4ae2a1fe03a32d42587e571217b3e097671827b8d536a4a29a34624bc7f57e2e` ／ 724 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.000046907103982 |
| rates.eos | 19 |
| rates.repetition | 45 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 45 |
| relevance2 | 23 |
| coherent | 1 |
| appropriate | 1 |
| notes_sha256 | "f6a0e318a48f84a50f38564747cbc89fc7a34cc85e0cbfa0c58f4a89d0fd0068" |
| scope | "new80_content_only_final_comparison_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/base_next_two_token_notes.json — None</summary>

[原記録](../../reports/phase6/base_next_two_token_notes.json) ／ SHA256: `f6a0e318a48f84a50f38564747cbc89fc7a34cc85e0cbfa0c58f4a89d0fd0068` ／ 25,190 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_next_two_token_probe_completion.json — native_next_two_probe_complete_science_budget_ready</summary>

[原記録](../../reports/phase6/base_next_two_token_probe_completion.json) ／ SHA256: `37923fad49ab1c9ecd3c2db36c4ea9aad2c265c690d349ff684a876e4b43e2da` ／ 4,440 bytes

| 原キー | 保存値 |
|---|---|
| status | "native_next_two_probe_complete_science_budget_ready" |
| initial_checks.native_logits | true |
| initial_checks.native_weights | true |
| initial_checks.native_RNG | true |
| initial_checks.native_parameters | true |
| initial_checks.train_only_parameters | true |
| initial_checks.native_tied | true |
| initial_checks.auxiliary_not_native_module | true |
| all_resume_and_source_checks.kind | true |
| all_resume_and_source_checks.spec | true |
| all_resume_and_source_checks.binding | true |
| all_resume_and_source_checks.lineage | true |
| all_resume_and_source_checks.model_config | true |
| all_resume_and_source_checks.model | true |
| all_resume_and_source_checks.optimizer | true |
| all_resume_and_source_checks.scheduler | true |
| all_resume_and_source_checks.RNG | true |
| all_resume_and_source_checks.sampler | true |
| all_resume_and_source_checks.counters | true |
| all_resume_and_source_checks.auxiliary_model | true |
| all_resume_and_source_checks.finite_native_optimizer | true |
| all_resume_and_source_checks.finite_auxiliary_model | true |
| all_resume_and_source_checks.all_history_except_timing | true |
| all_resume_and_source_checks.auxiliary_accounting | true |
| all_resume_and_source_checks.original_control_stream | true |
| all_resume_and_source_checks.full_original_control_sampler | true |
| capacity.passed | true |
| capacity.context | 1024 |
| capacity.original_targets | 24576 |
| capacity.next_two_targets | 24528 |
| capacity.peak_VRAM_bytes | 11987593728 |
| capacity.combined_loss | 2.95133113861084 |
| capacity.gradient_norm | 3.189606189727783 |
| capacity.optimizer_updates | 0 |
| median_original_teachers_per_second | 44940.797203392896 |
| all_timing_updates | 32 |
| GPU_occupancy_seconds | 10.010668233997421 |
| GPU_limit_seconds | 180 |
| science_cap_seconds | 3793 |
| maximum_scientific_GPU_seconds | 3965 |
| science_budget_eligible | true |
| fixed_next_two_protocol_closed | false |
| verification_updates | 48 |
| verification_original_teacher_positions | 279240 |
| verification_next_two_positions | 253920 |
| scientific_teacher_positions | 0 |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| interpretation | "Actual native and train-only head forward/backward, all-state save/resume and original stream evidence only. Short measured median is a budget forecast, not science completion or Japanese generation improvement. Include additional future positions/parameters/compute separately." |
| archive.bytes | 1182383 |
| archive.archived_completion_is_pre_bundle_record | true |
| archive.compressed_bundle.bytes | 343096 |

</details>

<details>
<summary>reports/phase6/base_next_two_token_proposal.json — fixed_next_two_auxiliary_proposal_CPU_verified_not_GPU_learning</summary>

[原記録](../../reports/phase6/base_next_two_token_proposal.json) ／ SHA256: `2e2f95a581157893c567736b74ce29f866db1d15aec23bdcda0c8fb2e185a98d` ／ 9,105 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_next_two_auxiliary_proposal_CPU_verified_not_GPU_learning" |
| previous_attention_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_attention_saturation_completion.json" |
| previous_attention_completion.sha256 | "78a8c02ec4a8a5740b7ee4eb049d5a859ef68d93374932819dd91217534c41ed" |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_next_two_token_trainer_tests.xml" |
| CPU_tests.sha256 | "a180e37751e6dd275488e5b6194eb3f6dc466d6bec62d202c72b5bd5c71ae01b" |
| source_references.scripts/base_next_two_token_trainer.py.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/base_next_two_token_trainer.py" |
| source_references.scripts/base_next_two_token_trainer.py.sha256 | "6a22b3644317b5c2ef3cdb543f25c13c3c9f007e0b208675abbfa97c9a9ca582" |
| source_references.scripts/prepare_base_next_two_token_proposal.py.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/scripts/prepare_base_next_two_token_proposal.py" |
| source_references.scripts/prepare_base_next_two_token_proposal.py.sha256 | "4bc6f1c8fdc82885b99b26327916b3c8bc1ddba4d418253990f44505c7765487" |
| source_references.tests/test_base_next_two_token_trainer.py.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/tests/test_base_next_two_token_trainer.py" |
| source_references.tests/test_base_next_two_token_trainer.py.sha256 | "34d8c6ce54ff0c862ff742c990ed739ada4ffdb7a62304b0d86d49634f9fbe6b" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| control.checkpoint_sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| control.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural_context_contrast_CE_notes.json" |
| control.notes.sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| control.reused_without_GPU_or_regrading | true |
| hypothesis | "The learned model may fit local next-token likelihood without developing enough reusable context features. Future-gold supervision is a distinct objective from failed InfoNCE/ranking/UL/dropout/uniform smoothing; not a claim that this is the unique cause." |
| mechanism.next_token_CE_weight | 1.0 |
| mechanism.auxiliary_seed | 19042 |
| mechanism.teacher_policy | "Only accepted original TRAIN gold; no generated targets, fabricated labels, dev/test, Chat roles or repeated Tokenizer training" |
| seed | 42 |
| CPU_preparation_cap_seconds | 30 |
| GPU_probe_cap_seconds | 180 |
| maximum_scientific_GPU_seconds | 3965 |
| science_budget_rule | "Only after own CUDA/BF16 finite full shape, all native+aux model/Adam/scheduler/RNG/sampler/counters/history4 continuous versus2 saved/resumed2 and actual stable batch48: ceil(100M/measured_median_original_teacher_speed*1.3+900)&lt;=3965. Freeze science cap from actual measurements; no cap increase or new control GPU." |
| research_and_adoption | "Unchanged relative coherence+8 and positive paired CI, EOS/rep nonworsening,1percent BPB/no errors versus cached CE; also unchanged strong/absolute/historical Web. Only eligible quality candidate proceeds to independent learned seed/full DEV/protected TEST/adoption; researcher marker or native code is not Base completion." |
| failure_policy | "One next-two contextual head/coefficient0.1. On failed protocol/budget/transfer, close this fixed condition. No horizon/coefficient/head sharing/architecture/LR/source/parent/epoch/teacher rescue or automatic extension." |
| completion | "Persisted exited native GPU100M, exact all original and auxiliary state/counters, own real CUDA resume, same fixed metrics and all80 content, unchanged gate review, evidence archive/UI restoration/local commit. Stop and notify only actual qualified Base; no Chat/quantization." |
| literature.limitations | "Their sizes include nonembedding parameter labels, training may use up to90epochs and a test-metric epoch oracle, and parameter-matched trunk/head allocation differs. Not10M total Japanese evidence, no protected-test tuning/epoch oracle or exact replication here." |
| local_novelty_scope.top_level_files_examined | 820 |
| local_novelty_scope.exact_marker_matches | [] |
| implementation_status | "Core train-only head/trainer and five CPU checks implemented. Dedicated CUDA probe, scientific runner/evaluator/reviewer not yet implemented; do not invoke absent commands." |
| actual_GPU_learning_seconds | 0 |
| scientific_teacher_positions | 0 |
| preparation_CPU_seconds | 0.8898089140129741 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_next_two_token_science_start.json — actual_native_CUDA_next_two100M_started_quality_pending</summary>

[原記録](../../reports/phase6/base_next_two_token_science_start.json) ／ SHA256: `b1f61bcbe6b31f57513a838995fd750875fcff6e7badd34862f79a8886cf553c` ／ 2,030 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_native_CUDA_next_two100M_started_quality_pending" |
| Base_complete | false |
| protected_test_used | false |
| Base_adopted | false |
| GPU_budget_seconds | 3793 |
| current_heartbeat.status | "running" |
| current_heartbeat.GPU_occupancy_seconds | 56.60378505900735 |
| current_heartbeat.Base_complete | false |
| current_heartbeat.resident_memory_policy.visible_device_bytes | 25756696576 |
| current_heartbeat.resident_memory_policy.allocator_allowance_bytes | 23181026918 |
| current_heartbeat.resident_memory_policy.expected_worst_peak_bytes | 11987593728 |
| current_heartbeat.scientific_CE_teacher_tokens | 3280269 |
| current_heartbeat.local_update | 580 |
| current_heartbeat.loss | 3.3076095581054688 |
| current_heartbeat.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-next-two-token-comparison-20261007/next_two/checkpoint-00000500.pt" |

</details>

<details>
<summary>reports/phase6/base_only_stop_boundary.json — None</summary>

[原記録](../../reports/phase6/base_only_stop_boundary.json) ／ SHA256: `227ef4f70b3e18b394f737aaf5479c54a33de9012f475a34fa7e8464b66c648e` ／ 1,191 bytes

| 原キー | 保存値 |
|---|---|
| active_scope | "Base training, evaluation, improvement and evidence-qualified adoption only" |
| historical_five_step_goal_complete | false |
| Base_complete | false |
| latest_Base_quality_passed | false |

</details>

<details>
<summary>reports/phase6/base_parent_baseline_audit.json — completed_CPU_two_documented_parent_and_registered_route_audit</summary>

[原記録](../../reports/phase6/base_parent_baseline_audit.json) ／ SHA256: `fcd258ab59263edaccbb4b19cd42e21aea97c2eb32f059a1bb3324f4bebabcbe` ／ 34,649 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_CPU_two_documented_parent_and_registered_route_audit" |
| CPU_seconds | 0.3233729990024585 |
| GPU_seconds | 0 |
| new_scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| states.originalWeb10B.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| states.originalWeb10B.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| states.originalWeb10B.update | 305176 |
| states.originalWeb10B.input_tokens | 10000007168 |
| states.originalWeb10B.teacher_tokens | 9978838479 |
| states.originalWeb10B.body_bytes | 38873077273 |
| states.originalWeb10B.optimizer_step_range | [305176.0, 305176.0] |
| states.originalWeb10B.scheduler._step_count | 305177 |
| states.originalWeb10B.scheduler._get_lr_called_within_step | false |
| states.originalWeb10B.sampler_kind | "original_block_sampler" |
| states.originalWeb10B.sampler_keys | ["blocks", "context", "epoch", "position", "seed"] |
| states.originalWeb10B.sampler_position | 9765632 |
| states.originalWeb10B.model_config.status | "phase5_ablation" |
| states.originalWeb10B.lineage.parent_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/stable/checkpoint-00289917.pt" |
| states.originalWeb10B.lineage.parent_update | 289917 |
| states.originalWeb10B.lineage.parent_tokens | 9500000256 |
| states.originalWeb10B.lineage.parent_spec.seed | 42 |
| states.originalWeb10B.lineage.parent_spec.schedule_updates | 289917 |
| states.originalWeb10B.lineage.parent_token_digest | "7a8cc70bc3704f86d215f63705764e4a6dbc4c97f29221ff0b51944c1eb6a2a0" |
| states.originalWeb10B.complete_optimizer_scheduler_RNG_sampler_present | true |
| states.historicalWeb.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| states.historicalWeb.checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| states.historicalWeb.update | 320435 |
| states.historicalWeb.input_tokens | 10500014080 |
| states.historicalWeb.teacher_tokens | 10477786961 |
| states.historicalWeb.body_bytes | 40816800491 |
| states.historicalWeb.optimizer_step_range | [320435.0, 320435.0] |
| states.historicalWeb.scheduler._step_count | 320436 |
| states.historicalWeb.scheduler._get_lr_called_within_step | false |
| states.historicalWeb.sampler_kind | "eos-pilot-mixture-v1" |
| states.historicalWeb.sampler_keys | ["kind", "position", "routes", "short", "source_eos", "source_tokens", "web"] |
| states.historicalWeb.sampler_position | 15259 |
| states.historicalWeb.model_config.status | "phase5_ablation" |
| states.historicalWeb.lineage.parent_update | 305176 |
| states.historicalWeb.lineage.parent_tokens | 10000007168 |
| states.historicalWeb.lineage.parent_spec.seed | 42 |
| states.historicalWeb.lineage.parent_spec.schedule_updates | 305176 |
| states.historicalWeb.lineage.parent_spec.decay_updates | 15259 |
| states.historicalWeb.lineage.parent_token_digest | "2eeede097b4260035c80f9817d6b8383b089e2f00a8ed577db467221c803d4e8" |
| states.historicalWeb.lineage.parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| states.historicalWeb.lineage.parent_checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| states.historicalWeb.lineage.parent_checkpoint.update | 305176 |
| states.historicalWeb.lineage.parent_checkpoint.tokens_seen | 10000007168 |
| states.historicalWeb.complete_optimizer_scheduler_RNG_sampler_present | true |
| quality.originalWeb10B.BPB | 0.9858907549313023 |
| quality.originalWeb10B.greedy_rates.eos | 0 |
| quality.originalWeb10B.greedy_rates.repetition | 53 |
| quality.originalWeb10B.greedy_rates.unicode_failure | 0 |
| quality.originalWeb10B.greedy_rates.role_leak | 0 |
| quality.originalWeb10B.greedy_rates.empty | 0 |
| quality.originalWeb10B.original_Web_guard_passes | false |
| quality.historicalWeb.BPB | 0.9715702494156145 |
| quality.historicalWeb.greedy_rates.eos | 0 |
| quality.historicalWeb.greedy_rates.repetition | 62 |
| quality.historicalWeb.greedy_rates.unicode_failure | 0 |
| quality.historicalWeb.greedy_rates.role_leak | 0 |
| quality.historicalWeb.greedy_rates.empty | 0 |
| quality.historicalWeb.original_Web_guard_passes | true |
| historical_Web_extra_input_tokens | 500006912 |
| historical_Web_extra_teacher_tokens | 498948482 |
| historical_Web_extra_updates | 15259 |
| existing_lowLR.parents.continuation.update | 308251 |
| existing_lowLR.parents.continuation.tokens_seen | 10100768768 |
| existing_lowLR.parents.fresh.update | 3075 |
| existing_lowLR.parents.fresh.tokens_seen | 100761600 |
| existing_lowLR.continuation_BPB | 1.0898779879735516 |
| existing_lowLR.continuation_coherent | 4 |
| registered_configs.configs/phase6/complete_document_500m.json | "2e0ec1f3f5aec4ff3d9dc08a2a8b3799ebb205a5ef24faa5a0747be09fde8413" |
| registered_configs.configs/phase6/eos_5b_finish_100m.json | "ec768ac1ad0b258077fdf34f7e839975324c6232982f7b3884962fe68965762f" |
| registered_configs.configs/phase6/eos_complete_100m.json | "56e0ec36d507bc6a2f153e5c65495ca00f67c468046b331c088497f85c059c29" |
| registered_configs.configs/phase6/eos_complete_100m_full_bpb.json | "070581297ceab0d391ed1e34e741a8571eb90f416d47cb97d00b536252c8e2ea" |
| registered_configs.configs/phase6/eos_complete_evaluation_recovery.json | "605e90b2e6df08058883b423d3c6d3d257be4b7723cccf4ee7393b975b3a70bc" |
| registered_configs.configs/phase6/eos_low_lr_100m.json | "c51dbfe3f7db561bc5f3a93a38be68dbf35dbc5db5bd24f10685070d6d10e290" |
| registered_configs.configs/phase6/eos_short_pilot.json | "3cd5739578f0a7c8ef833fd5c4a98643b73e5c2ef295299f90bbc9639798fd42" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parent_budget_inventory.json | "3c5acfbfcd63f1acd992fac9892919225e2fa7744a5fbab084034bd08208a9cf" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/complete_document_500m.json | "2e0ec1f3f5aec4ff3d9dc08a2a8b3799ebb205a5ef24faa5a0747be09fde8413" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_5b_finish_100m.json | "ec768ac1ad0b258077fdf34f7e839975324c6232982f7b3884962fe68965762f" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_complete_100m.json | "56e0ec36d507bc6a2f153e5c65495ca00f67c468046b331c088497f85c059c29" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_complete_100m_full_bpb.json | "070581297ceab0d391ed1e34e741a8571eb90f416d47cb97d00b536252c8e2ea" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_complete_evaluation_recovery.json | "605e90b2e6df08058883b423d3c6d3d257be4b7723cccf4ee7393b975b3a70bc" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_low_lr_100m.json | "c51dbfe3f7db561bc5f3a93a38be68dbf35dbc5db5bd24f10685070d6d10e290" |
| references./home/aihub_ubuntu/src/japanese-tiny-llm-10m/configs/phase6/eos_short_pilot.json | "3cd5739578f0a7c8ef833fd5c4a98643b73e5c2ef295299f90bbc9639798fd42" |
| Base_adopted | false |
| Base_complete | false |
| protected_test_used | false |
| limitations | "Exactly two preselected documented checkpoints, saved evaluations and registered phase6 config parents. No new model scoring, external experiment discovery or favorable checkpoint search. No direct parent match in the registry does not prove no unregistered experiment exists. Parent states differ in Web amount/order, Adam/RNG/sampler/scheduler and actual LR; comparison of inherited routes is not a pure parent-weight or LR causal effect. Original10B failing the unchanged historical BPB guard does not invalidate other independent quality failures or justify relaxing any gate." |

</details>

<details>
<summary>reports/phase6/base_parent_baseline_audit_proposal.json — defined_bounded_CPU_parent_and_guard_route_audit_not_executed</summary>

[原記録](../../reports/phase6/base_parent_baseline_audit_proposal.json) ／ SHA256: `ad1ba6c588acc737a1e7c985a12f9959ed864cadaaf20def88e2ba4358355e1f` ／ 3,811 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_bounded_CPU_parent_and_guard_route_audit_not_executed" |
| scope | "Read only two explicitly documented parent/guard fullstate metadata and their saved evaluations, and the completed LR-recovery/500M Web branch provenance. Check config recordedLR vs actual optimizer groups, body/input/teacher/byte budgets, sampler/Adam/scheduler lineage and completed comparisons. No broad checkpoint scan, forward/backward, tokenization/corpus audit or new scoring. Historical guard stays unchanged; do not select a favorable checkpoint by outcome." |
| CPU_limit_seconds | 30 |
| GPU_seconds | 0 |
| new_scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| completion | "Persist a small table linking actual parent/guard SHA and budgets/LR/quality; explicitly identify whether the proposed parent route is genuinely untested or a duplicate. If duplicate or not justified, reject it and do not launch a speculative repeated sweep. A new training proposal requires a defined matched comparison and measured budget; no automatic extension." |
| limitations | "Descriptive state/provenance audit cannot prove quality improves with a different parent. Low LR with100% short-only material is not automatically equivalent to75% original Web plus three short sources. The current query intervention reduced train last-entity correlation but still failed both quality and its predefined secondary mechanism screen." |
| Base_adopted | false |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_parent_budget_inventory.json — actual_parent_budget_and_checkpoint_interface_readonly_inventory</summary>

[原記録](../../reports/phase6/base_parent_budget_inventory.json) ／ SHA256: `3c5acfbfcd63f1acd992fac9892919225e2fa7744a5fbab084034bd08208a9cf` ／ 45,921 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_parent_budget_and_checkpoint_interface_readonly_inventory" |
| records.textbook2B.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| records.textbook2B.checkpoint.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| records.textbook2B.update | 62166 |
| records.textbook2B.input_tokens | 2037055488 |
| records.textbook2B.supervised_tokens | 2020000000 |
| records.textbook2B.model_config.status | "phase5_ablation" |
| records.textbook2B.scheduler._step_count | 62167 |
| records.textbook2B.scheduler._get_lr_called_within_step | false |
| records.textbook2B.spec.seed | 42 |
| records.textbook2B.spec.schedule_updates | 161550 |
| records.textbook2B.spec.pilot_schedule.parent_update | 61550 |
| records.textbook2B.spec.pilot_schedule.stable_updates | 1 |
| records.textbook2B.spec.pilot_schedule.decay_updates | 1 |
| records.textbook2B.spec.teacher_schedule.goals.web | 0 |
| records.textbook2B.spec.teacher_schedule.goals.short | 20000000 |
| records.textbook2B.spec.teacher_schedule.stable_fraction | 0.9 |
| records.textbook2B.spec.teacher_schedule.minimum_lr_ratio | 0.1 |
| records.textbook2B.spec.curve_schedule.teachers | 20000000 |
| records.originalWeb10B.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| records.originalWeb10B.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| records.originalWeb10B.update | 305176 |
| records.originalWeb10B.input_tokens | 10000007168 |
| records.originalWeb10B.supervised_tokens | 9978838479 |
| records.originalWeb10B.model_config.status | "phase5_ablation" |
| records.originalWeb10B.scheduler._step_count | 305177 |
| records.originalWeb10B.scheduler._get_lr_called_within_step | false |
| records.originalWeb10B.spec.seed | 42 |
| records.originalWeb10B.spec.schedule_updates | 305176 |
| records.originalWeb10B.spec.decay_updates | 15259 |
| records.originalWeb10B.sampler_keys | ["blocks", "context", "epoch", "position", "seed"] |
| records.historicalWeb.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| records.historicalWeb.checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| records.historicalWeb.update | 320435 |
| records.historicalWeb.input_tokens | 10500014080 |
| records.historicalWeb.supervised_tokens | 10477786961 |
| records.historicalWeb.model_config.status | "phase5_ablation" |
| records.historicalWeb.scheduler._step_count | 320436 |
| records.historicalWeb.scheduler._get_lr_called_within_step | false |
| records.historicalWeb.spec.seed | 42 |
| records.historicalWeb.spec.schedule_updates | 320435 |
| records.historicalWeb.spec.pilot_schedule.parent_update | 305176 |
| records.historicalWeb.spec.pilot_schedule.stable_updates | 14500 |
| records.historicalWeb.spec.pilot_schedule.decay_updates | 759 |
| records.historicalWeb.sampler_keys | ["kind", "position", "routes", "short", "source_eos", "source_tokens", "web"] |
| original_Web_BPB | 0.9715702494156145 |
| original_Web_rates.eos | 0 |
| original_Web_rates.repetition | 62 |
| original_Web_rates.unicode_failure | 0 |
| original_Web_rates.role_leak | 0 |
| original_Web_rates.empty | 0 |
| CPU_seconds | 0.2921081979875453 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| initial_schema_assumption_repaired | "Initial read expected checkpoint in evaluation; actual evaluator stores only SHA. Resolve path from authoritative training result and require matching SHA. No fallback checkpoint or new GPU." |
| limitations | "Read-only metadata/hash evidence, not re-evaluation or matched learning-budget quality. Different historical parents also differ in data/source/order/learning amount. HistoricalWeb quality guard is not an equal-budget2B or100M causal control." |

</details>

<details>
<summary>reports/phase6/base_preference_comparison_completion.json — Base_preference_fixed_comparison_completed</summary>

[原記録](../../reports/phase6/base_preference_comparison_completion.json) ／ SHA256: `84b8e6b73a6a875702eb2b66f9c36a7e1b2753e267fed22271adb8296fe4a239` ／ 12,477 bytes

| 原キー | 保存値 |
|---|---|
| status | "Base_preference_fixed_comparison_completed" |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 267.53127299799235 |
| actual_job.teachers | 1917300 |
| actual_job.teacher_budget | 2000000 |
| actual_job.loss | 0.008548618294298649 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_review.status | "Base_preference_all160_native_state_and_content_reviewed" |
| actual_review.summaries.chosen_CE.BPB | 1.2221178517492344 |
| actual_review.summaries.chosen_CE.rates.eos | 57 |
| actual_review.summaries.chosen_CE.rates.repetition | 3 |
| actual_review.summaries.chosen_CE.rates.unicode_failure | 1 |
| actual_review.summaries.chosen_CE.rates.role_leak | 0 |
| actual_review.summaries.chosen_CE.rates.empty | 0 |
| actual_review.summaries.chosen_CE.grammar2 | 29 |
| actual_review.summaries.chosen_CE.relevance2 | 15 |
| actual_review.summaries.chosen_CE.coherent | 4 |
| actual_review.summaries.chosen_CE.appropriate | 8 |
| actual_review.summaries.chosen_CE.notes_sha256 | "23751d2a4c1c95a4dfeba074679f2329deb9dc2962790329f624f3d05485917d" |
| actual_review.summaries.chosen_CE_DPO.BPB | 1.2236346693225277 |
| actual_review.summaries.chosen_CE_DPO.rates.eos | 57 |
| actual_review.summaries.chosen_CE_DPO.rates.repetition | 3 |
| actual_review.summaries.chosen_CE_DPO.rates.unicode_failure | 1 |
| actual_review.summaries.chosen_CE_DPO.rates.role_leak | 0 |
| actual_review.summaries.chosen_CE_DPO.rates.empty | 0 |
| actual_review.summaries.chosen_CE_DPO.grammar2 | 30 |
| actual_review.summaries.chosen_CE_DPO.relevance2 | 16 |
| actual_review.summaries.chosen_CE_DPO.coherent | 6 |
| actual_review.summaries.chosen_CE_DPO.appropriate | 12 |
| actual_review.summaries.chosen_CE_DPO.notes_sha256 | "438c4e1b9beb917bfea9d73d5bca7e129cc928556c950937f711fb6cfcc97592" |
| actual_review.summaries.strong_staged.BPB | 1.1336128657420816 |
| actual_review.summaries.strong_staged.rates.eos | 76 |
| actual_review.summaries.strong_staged.rates.repetition | 2 |
| actual_review.summaries.strong_staged.rates.unicode_failure | 0 |
| actual_review.summaries.strong_staged.rates.role_leak | 0 |
| actual_review.summaries.strong_staged.rates.empty | 0 |
| actual_review.summaries.strong_staged.grammar2 | 65 |
| actual_review.summaries.strong_staged.relevance2 | 39 |
| actual_review.summaries.strong_staged.coherent | 23 |
| actual_review.summaries.strong_staged.appropriate | 26 |
| actual_review.summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| actual_review.quality_comparison.chosen_CE.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparison.chosen_CE.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparison.chosen_CE.checks.EOS_nonworsening | false |
| actual_review.quality_comparison.chosen_CE.checks.repetition_nonworsening | false |
| actual_review.quality_comparison.chosen_CE.checks.no_empty_role_unicode | false |
| actual_review.quality_comparison.chosen_CE.checks.BPB_gate | false |
| actual_review.quality_comparison.chosen_CE.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparison.chosen_CE.passed | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.EOS_nonworsening | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.repetition_nonworsening | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.no_empty_role_unicode | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.BPB_gate | false |
| actual_review.quality_comparison.chosen_CE_DPO.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparison.chosen_CE_DPO.passed | false |
| actual_review.matched_objective_quality.checks.coherence_gain_at_least8 | false |
| actual_review.matched_objective_quality.checks.paired_CI_lower_above0 | false |
| actual_review.matched_objective_quality.checks.EOS_nonworsening | true |
| actual_review.matched_objective_quality.checks.repetition_nonworsening | true |
| actual_review.matched_objective_quality.checks.no_empty_role_unicode | false |
| actual_review.matched_objective_quality.checks.BPB_gate | true |
| actual_review.matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| actual_review.matched_objective_quality.passed | false |
| actual_review.absolute_dev_screen.chosen_CE.grammar_at_least56 | false |
| actual_review.absolute_dev_screen.chosen_CE.coherence_at_least27 | false |
| actual_review.absolute_dev_screen.chosen_CE.appropriate_at_least27 | false |
| actual_review.absolute_dev_screen.chosen_CE.EOS_at_least37 | true |
| actual_review.absolute_dev_screen.chosen_CE.repetition_at_most18 | true |
| actual_review.absolute_dev_screen.chosen_CE.no_empty_role_unicode | false |
| actual_review.absolute_dev_screen.chosen_CE_DPO.grammar_at_least56 | false |
| actual_review.absolute_dev_screen.chosen_CE_DPO.coherence_at_least27 | false |
| actual_review.absolute_dev_screen.chosen_CE_DPO.appropriate_at_least27 | false |
| actual_review.absolute_dev_screen.chosen_CE_DPO.EOS_at_least37 | true |
| actual_review.absolute_dev_screen.chosen_CE_DPO.repetition_at_most18 | true |
| actual_review.absolute_dev_screen.chosen_CE_DPO.no_empty_role_unicode | false |
| actual_review.original_Web.chosen_CE.EOS_at_least8_more | true |
| actual_review.original_Web.chosen_CE.repetition_no_worse | true |
| actual_review.original_Web.chosen_CE.no_empty_role_unicode | false |
| actual_review.original_Web.chosen_CE.BPB_degradation_at_most1percent | false |
| actual_review.original_Web.chosen_CE_DPO.EOS_at_least8_more | true |
| actual_review.original_Web.chosen_CE_DPO.repetition_no_worse | true |
| actual_review.original_Web.chosen_CE_DPO.no_empty_role_unicode | false |
| actual_review.original_Web.chosen_CE_DPO.BPB_degradation_at_most1percent | false |
| actual_review.eligible_for_final_Base_validation.chosen_CE | false |
| actual_review.eligible_for_final_Base_validation.chosen_CE_DPO | false |
| actual_review.accounting.common_Web.completed_updates | 184 |
| actual_review.accounting.common_Web.positive_teacher_tokens | 6000000 |
| actual_review.accounting.common_Web.physical_input_positions | 6029312 |
| actual_review.accounting.common_Web.CE_body_bytes | 23365802 |
| actual_review.accounting.common_Web.sampler.kind | "Base_preference_common_Web_exact_v1" |
| actual_review.accounting.common_Web.sampler.goals.web | 6000000 |
| actual_review.accounting.common_Web.sampler.context | 1024 |
| actual_review.accounting.common_Web.sampler.position | 184 |
| actual_review.accounting.common_Web.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| actual_review.accounting.common_Web.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_review.accounting.common_Web.sampler.streams.web.sampler.seed | 42 |
| actual_review.accounting.common_Web.sampler.streams.web.sampler.epoch | 0 |
| actual_review.accounting.common_Web.sampler.streams.web.sampler.position | 10259808 |
| actual_review.accounting.common_Web.sampler.streams.web.sampler.context | 1024 |
| actual_review.accounting.common_Web.sampler.streams.web.sampler.blocks | 11939276 |
| actual_review.accounting.common_Web.sampler.source_teachers.web | 6000000 |
| actual_review.accounting.common_Web.sampler.source_eos.web | 12812 |
| actual_review.accounting.common_Web.sampler.source_tokens.web | 6029312 |
| actual_review.accounting.common_Web.sampler.source_body_bytes.web | 23365802 |
| actual_review.accounting.common_Web.sampler.source_focus_teachers.web | 0 |
| actual_review.accounting.chosen_CE.completed_updates | 439 |
| actual_review.accounting.chosen_CE.positive_teacher_tokens | 2000000 |
| actual_review.accounting.chosen_CE.physical_input_positions | 10472784 |
| actual_review.accounting.chosen_CE.CE_body_bytes | 7509150 |
| actual_review.accounting.chosen_CE.sampler.kind | "fixed_group_role_free_positive_quota_full_active_DPO_v1" |
| actual_review.accounting.chosen_CE.sampler.goal | 2000000 |
| actual_review.accounting.chosen_CE.sampler.batch | 56 |
| actual_review.accounting.chosen_CE.sampler.span | 213 |
| actual_review.accounting.chosen_CE.sampler.data_digest | "2b0220ab90f172f4e14bb3db2184dcf3f54b6586c420525b26ca204d7c0e9570" |
| actual_review.accounting.chosen_CE.sampler.reference_digest | "1b3e76f36472ab739796e2860f58c93e63b5fcc274e9900ff68f2d2c02d2aad7" |
| actual_review.accounting.chosen_CE.sampler.epoch | 439 |
| actual_review.accounting.chosen_CE.sampler.group_position | 0 |
| actual_review.accounting.chosen_CE.sampler.position | 439 |
| actual_review.accounting.chosen_CE.sampler.teachers | 2000000 |
| actual_review.accounting.chosen_CE.sampler.EOS | 24535 |
| actual_review.accounting.chosen_CE.sampler.body_bytes | 7509150 |
| actual_review.accounting.chosen_CE.sampler.physical | 10472784 |
| actual_review.accounting.chosen_CE.sampler.valid | 4870705 |
| actual_review.accounting.chosen_CE.sampler.scored_chosen | 2000038 |
| actual_review.accounting.chosen_CE.sampler.scored_rejected | 1570304 |
| actual_review.accounting.chosen_CE.sampler.active_pair_exposures | 24536 |
| actual_review.accounting.chosen_CE.sampler.auxiliary_digest | "4c6e1b7f3a6ba38cffee1a264f2e909ff7f9d676194f5b5de44417a2926fb8d0" |
| actual_review.accounting.chosen_CE_DPO.completed_updates | 439 |
| actual_review.accounting.chosen_CE_DPO.positive_teacher_tokens | 2000000 |
| actual_review.accounting.chosen_CE_DPO.physical_input_positions | 10472784 |
| actual_review.accounting.chosen_CE_DPO.CE_body_bytes | 7509150 |
| actual_review.accounting.chosen_CE_DPO.sampler.kind | "fixed_group_role_free_positive_quota_full_active_DPO_v1" |
| actual_review.accounting.chosen_CE_DPO.sampler.goal | 2000000 |
| actual_review.accounting.chosen_CE_DPO.sampler.batch | 56 |
| actual_review.accounting.chosen_CE_DPO.sampler.span | 213 |
| actual_review.accounting.chosen_CE_DPO.sampler.data_digest | "2b0220ab90f172f4e14bb3db2184dcf3f54b6586c420525b26ca204d7c0e9570" |
| actual_review.accounting.chosen_CE_DPO.sampler.reference_digest | "1b3e76f36472ab739796e2860f58c93e63b5fcc274e9900ff68f2d2c02d2aad7" |
| actual_review.accounting.chosen_CE_DPO.sampler.epoch | 439 |
| actual_review.accounting.chosen_CE_DPO.sampler.group_position | 0 |
| actual_review.accounting.chosen_CE_DPO.sampler.position | 439 |
| actual_review.accounting.chosen_CE_DPO.sampler.teachers | 2000000 |
| actual_review.accounting.chosen_CE_DPO.sampler.EOS | 24535 |
| actual_review.accounting.chosen_CE_DPO.sampler.body_bytes | 7509150 |
| actual_review.accounting.chosen_CE_DPO.sampler.physical | 10472784 |
| actual_review.accounting.chosen_CE_DPO.sampler.valid | 4870705 |
| actual_review.accounting.chosen_CE_DPO.sampler.scored_chosen | 2000038 |
| actual_review.accounting.chosen_CE_DPO.sampler.scored_rejected | 1570304 |
| actual_review.accounting.chosen_CE_DPO.sampler.active_pair_exposures | 24536 |
| actual_review.accounting.chosen_CE_DPO.sampler.auxiliary_digest | "4c6e1b7f3a6ba38cffee1a264f2e909ff7f9d676194f5b5de44417a2926fb8d0" |
| actual_review.matched_exposure.matched_updates | 439 |
| actual_review.scientific_positive_teacher_tokens | 10000000 |
| actual_review.common_positive_teacher_tokens | 6000000 |
| actual_review.positive_teacher_tokens_per_arm | 8000000 |
| actual_review.verification_teacher_tokens | 1694058 |
| actual_review.new_total_GPU_seconds | 303.6357959379966 |
| actual_review.diagnostic_GPU_seconds_separate | 69.95700160900014 |
| actual_review.Base_complete | false |
| actual_review.Base_adopted | false |
| actual_review.protected_test_used | false |
| actual_review.limitations | "Only56 TRAIN pairs/4565 positive positions repeatedly exposed, about438 passes; not new2M source. Original8 weak rows excluded before preference labeling. Sequence length/genre and fixed stale negatives; one learned seed/nonblind repeated dev. Earlier seven numerical failures retained." |
| scientific_GPU_seconds | 267.53127299799235 |
| total_new_GPU_seconds | 303.6357959379966 |
| scientific_positive_teacher_tokens | 10000000 |
| common_positive_teacher_tokens | 6000000 |
| positive_teacher_tokens_per_arm | 8000000 |
| eligible_for_final_Base_validation.chosen_CE | false |
| eligible_for_final_Base_validation.chosen_CE_DPO | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_preference_comparison_completion_portable.json — None</summary>

[原記録](../../reports/phase6/base_preference_comparison_completion_portable.json) ／ SHA256: `df062fd05a20e39289d300131a5e7c5aef2a81c36eca6c5e7febd57c4bead1aa` ／ 41,155 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/base_preference_comparison_completion.json.bytes | 12477 |
| files.reports/phase6/base_preference_comparison_completion.json.sha256 | "84b8e6b73a6a875702eb2b66f9c36a7e1b2753e267fed22271adb8296fe4a239" |
| files.configs/phase6/base_preference_comparison.json.bytes | 13108 |
| files.reports/phase6/base_preference_comparison_proposal.json.bytes | 5297 |
| files.scripts/record_base_preference_completion.py.bytes | 5357 |
| files.scripts/record_base_preference_completion.py.sha256 | "3ba4c40f49ac06046131791b3a8bbd151e5b4b1f2a9cb72b0407cd5cee75a74b" |
| files.scripts/run_base_preference_comparison.py.bytes | 17918 |
| files.scripts/run_base_preference_comparison.ps1.bytes | 2641 |
| files.scripts/base_preference_accounting.py.bytes | 6777 |
| files.scripts/review_base_preference_comparison.py.bytes | 8992 |
| files.scripts/record_base_preference_content.py.bytes | 3537 |
| files.tests/test_base_preference_science.py.bytes | 2865 |
| files.tests/test_base_preference_science.py.sha256 | "f354ad6714b82fc04466f2228d8e077471d02b7a5c9881e8b0b6305688b0d6a2" |
| files.reports/phase6/base_preference_science_tests.xml.bytes | 679 |
| files.reports/phase6/base_preference_science_tests.xml.sha256 | "3ba1a8fb6f097cfd5ae2365dbd6a525a359610c5ac8793c08a594202718865fe" |
| files.reports/phase6/base_preference_comparison_review.json.bytes | 9001 |
| files.reports/phase6/base_preference_chosen_CE_observations.tsv.bytes | 10661 |
| files.reports/phase6/base_preference_chosen_CE_DPO_observations.tsv.bytes | 10599 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE/training/latest.json.bytes | 284 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE/training/latest.json.sha256 | "ce9b785d756612afa6ce07524027d0319d90cbd3b4e8f63027172195d8f789a8" |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE/training/metrics.jsonl.bytes | 412339 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE-content-notes.json.bytes | 22805 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE-content-notes.json.sha256 | "23751d2a4c1c95a4dfeba074679f2329deb9dc2962790329f624f3d05485917d" |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE_DPO/training/latest.json.bytes | 288 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE_DPO/training/latest.json.sha256 | "0c78cce13c05b728712ad07d6286f26cfbc023fd4f94bb9ae68db34eb3852e2f" |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE_DPO/training/metrics.jsonl.bytes | 413797 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE_DPO-content-notes.json.bytes | 22747 |
| files.reports/phase6/base-preference-comparison-20261006/chosen_CE_DPO-content-notes.json.sha256 | "438c4e1b9beb917bfea9d73d5bca7e129cc928556c950937f711fb6cfcc97592" |
| files.reports/phase6/base-preference-comparison-20261006/common_Web/training/latest.json.bytes | 285 |
| files.reports/phase6/base-preference-comparison-20261006/common_Web/training/latest.json.sha256 | "5fb8e08904782c9192d5f43647e4ba5b22799b18a332f0b177e5703433b1e410" |
| files.reports/phase6/base-preference-comparison-20261006/common_Web/training/metrics.jsonl.bytes | 155776 |
| files.reports/phase6/base-preference-comparison-20261006/compare-result.json.bytes | 1294649 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/body.json.bytes | 67489 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/generation.json.bytes | 91512 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/jblimp.json.bytes | 339135 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/jcqa.json.bytes | 1643435 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/result.json.bytes | 186525 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE/evaluation/semantics.json.bytes | 203379 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/body.json.bytes | 67477 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/generation.json.bytes | 92652 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/jblimp.json.bytes | 339184 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/jcqa.json.bytes | 1643131 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/result.json.bytes | 187835 |
| files.reports/phase6/base-preference-comparison-20261006/evaluation/chosen_CE_DPO/evaluation/semantics.json.bytes | 203382 |
| files.reports/phase6/base-preference-comparison-20261006/job.json.bytes | 729 |
| files.reports/phase6/base-preference-comparison-20261006/progress-result.json.bytes | 1294095 |
| files.reports/phase6/base-preference-comparison-20261006/review.json.bytes | 9001 |
| files.reports/phase6/base-preference-comparison-20261006/shared-reference.json.bytes | 4209 |
| files.reports/phase6/base-preference-comparison-20261006/source/configs/phase6/base_preference_comparison.json.bytes | 13108 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/base_preference_accounting.py.bytes | 6777 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/base_preference_loss.py.bytes | 2501 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/base_preference_loss.py.sha256 | "5efea442ad8843d7f99fbfe7101b09b2f8a98d7c7f8cf5f073ff0eff4638f423" |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/base_preference_trainer.py.bytes | 17632 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/probe_base_preference.ps1.bytes | 2603 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/probe_base_preference.py.bytes | 16043 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/probe_livedoor_base.py.bytes | 16328 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/record_base_preference_content.py.bytes | 3537 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/record_parameter_displacement_anchor_content.py.bytes | 27824 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/review_base_preference_comparison.py.bytes | 8992 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/review_matched_story_study.py.bytes | 14571 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/review_parameter_displacement_anchor.py.bytes | 12207 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/review_textbook_quantity_comparison.py.bytes | 8984 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_base_preference_comparison.ps1.bytes | 2641 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_base_preference_comparison.py.bytes | 17918 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/base-preference-comparison-20261006/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/base-preference-comparison-20261006/source/tests/test_base_preference_science.py.bytes | 2865 |
| files.reports/phase6/base-preference-comparison-20261006/source/tests/test_base_preference_science.py.sha256 | "f354ad6714b82fc04466f2228d8e077471d02b7a5c9881e8b0b6305688b0d6a2" |
| files.reports/phase6/base-preference-comparison-20261006/source/tests/test_base_preference_trainer.py.bytes | 4288 |
| files.reports/phase6/base-preference-comparison-20261006/source/tests/test_base_preference_trainer.py.sha256 | "0f6aa5da8d4c7ce86a06aa2d5d7ae86aa5ab7f53e51c6070e062babcd16fd6a9" |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0000.json.bytes | 9749 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0016.json.bytes | 9401 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0032.json.bytes | 10051 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0048.json.bytes | 9331 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0064.json.bytes | 10112 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0080.json.bytes | 9523 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0096.json.bytes | 9614 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0112.json.bytes | 9946 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0128.json.bytes | 9633 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0144.json.bytes | 9679 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0160.json.bytes | 9967 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0176.json.bytes | 9778 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0192.json.bytes | 9708 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0208.json.bytes | 9429 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0224.json.bytes | 9600 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0240.json.bytes | 9421 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0256.json.bytes | 9390 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0272.json.bytes | 9373 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0288.json.bytes | 9389 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0304.json.bytes | 9574 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0320.json.bytes | 9147 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0336.json.bytes | 9230 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0352.json.bytes | 9540 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0368.json.bytes | 9306 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0384.json.bytes | 9612 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0400.json.bytes | 9286 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0416.json.bytes | 9664 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0432.json.bytes | 9150 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0448.json.bytes | 9382 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0464.json.bytes | 9187 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0480.json.bytes | 9187 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/0496.json.bytes | 9287 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE/result.json.bytes | 186389 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0000.json.bytes | 9732 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0016.json.bytes | 9380 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0032.json.bytes | 10048 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0048.json.bytes | 9304 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0064.json.bytes | 10106 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0080.json.bytes | 9532 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0096.json.bytes | 9611 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0112.json.bytes | 9951 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0128.json.bytes | 9623 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0144.json.bytes | 9671 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0160.json.bytes | 9977 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0176.json.bytes | 9772 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0192.json.bytes | 9713 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0208.json.bytes | 9442 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0224.json.bytes | 9605 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0240.json.bytes | 9420 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0256.json.bytes | 9388 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0272.json.bytes | 9358 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0288.json.bytes | 9385 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0304.json.bytes | 9564 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0320.json.bytes | 9126 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0336.json.bytes | 9195 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0352.json.bytes | 9540 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0368.json.bytes | 9293 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0384.json.bytes | 9590 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0400.json.bytes | 9280 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0416.json.bytes | 9635 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0432.json.bytes | 9136 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0448.json.bytes | 9359 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0464.json.bytes | 9175 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0480.json.bytes | 9176 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/0496.json.bytes | 9262 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/bridge/chosen_CE_DPO/result.json.bytes | 186396 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0000.json.bytes | 7843 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0016.json.bytes | 8194 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0032.json.bytes | 6882 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0048.json.bytes | 8041 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0064.json.bytes | 8365 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0080.json.bytes | 6977 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0096.json.bytes | 7954 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0112.json.bytes | 8133 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0128.json.bytes | 6965 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0144.json.bytes | 8051 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0160.json.bytes | 8476 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0176.json.bytes | 6840 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0192.json.bytes | 8053 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0208.json.bytes | 8369 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0224.json.bytes | 6983 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0240.json.bytes | 8233 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0256.json.bytes | 8117 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0272.json.bytes | 8291 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0288.json.bytes | 6998 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0304.json.bytes | 8038 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0320.json.bytes | 8467 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0336.json.bytes | 7009 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0352.json.bytes | 8024 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0368.json.bytes | 8036 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0384.json.bytes | 6904 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0400.json.bytes | 8023 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0416.json.bytes | 8063 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0432.json.bytes | 6997 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0448.json.bytes | 7933 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0464.json.bytes | 8209 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0480.json.bytes | 6895 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/0496.json.bytes | 7940 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE/result.json.bytes | 183065 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0000.json.bytes | 7839 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0016.json.bytes | 8189 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0032.json.bytes | 6888 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0048.json.bytes | 8033 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0064.json.bytes | 8362 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0080.json.bytes | 6974 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0096.json.bytes | 7954 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0112.json.bytes | 8121 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0128.json.bytes | 6965 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0144.json.bytes | 8039 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0160.json.bytes | 8479 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0176.json.bytes | 6835 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0192.json.bytes | 8056 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0208.json.bytes | 8378 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0224.json.bytes | 6976 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0240.json.bytes | 8215 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0256.json.bytes | 8103 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0272.json.bytes | 8280 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0288.json.bytes | 6993 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0304.json.bytes | 8034 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0320.json.bytes | 8450 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0336.json.bytes | 7002 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0352.json.bytes | 8020 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0368.json.bytes | 8034 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0384.json.bytes | 6908 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0400.json.bytes | 8027 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0416.json.bytes | 8039 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0432.json.bytes | 6999 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0448.json.bytes | 7949 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0464.json.bytes | 8198 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0480.json.bytes | 6913 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/0496.json.bytes | 7939 |
| files.reports/phase6/base-preference-comparison-20261006/transfer/retention/chosen_CE_DPO/result.json.bytes | 183121 |
| raw_source_pairs_and_tensors_native_only | true |

</details>

<details>
<summary>reports/phase6/base_preference_comparison_proposal.json — None</summary>

[原記録](../../reports/phase6/base_preference_comparison_proposal.json) ／ SHA256: `5777de99ab6bdac553550721d7a03d4f1bdcdd4a97a409a719f504e6e756df90` ／ 5,297 bytes

| 原キー | 保存値 |
|---|---|
| news_pairs.path | "/home/aihub_ubuntu/jmicro-data/phase6/base-preference-diagnostic-20261006/pairs.json" |
| news_pairs.sha256 | "9123be8b267519b4accf2af1c650b9737365b1e57b992fa8ab41bd0805d8dec2" |
| source_weak_pair_policy | "Exclude precisely8 pre-rollout original-source weak rows. All56 other rows individually support original over generated loop; no new source/selector/reroll." |
| fixed_pair_count | 56 |
| fixed_positive_completion_teacher_positions | 4565 |
| shared_Web_positive_teacher_tokens | 6000000 |
| positive_completion_teacher_tokens_per_arm | 2000000 |
| positive_teacher_tokens_per_arm | 8000000 |
| new_unique_scientific_positive_teacher_tokens | 10000000 |
| positive_completion_exposure_passes | 438.1161007667032 |
| own_GPU_probe_ceiling_seconds | 180 |
| total_new_study_GPU_ceiling_seconds | 1800 |
| diagnostic_GPU_seconds_separate | 69.95700160900014 |
| completion | "Single finite2M completion comparison per arm and full quality judgement; reject failed recipe. No beta/coefficient/source/epoch/LR/decoder/parent/checkpoint rescue sweep." |
| scientific_config_frozen | false |
| Base_complete | false |
| protected_test_used | false |
| evidence_limits | "Measured64-gradient DPO/CE norm8.693 and cosine.5584 are preliminary not a56-scale guarantee. Alpha.1 is one predeclared perturbation of the new objective, not optimized or a safety bound. DPO is not guaranteed to preserve Web BPB or fix free generation. Limited curated source/style and repeated dev remain." |

</details>

<details>
<summary>reports/phase6/base_preference_comparison_review.json — Base_preference_all160_native_state_and_content_reviewed</summary>

[原記録](../../reports/phase6/base_preference_comparison_review.json) ／ SHA256: `6e6106743644ba83a931d23ce696a72a11951dd80901c7997ea3eb070c8c06a5` ／ 9,001 bytes

| 原キー | 保存値 |
|---|---|
| status | "Base_preference_all160_native_state_and_content_reviewed" |
| summaries.chosen_CE.BPB | 1.2221178517492344 |
| summaries.chosen_CE.rates.eos | 57 |
| summaries.chosen_CE.rates.repetition | 3 |
| summaries.chosen_CE.rates.unicode_failure | 1 |
| summaries.chosen_CE.rates.role_leak | 0 |
| summaries.chosen_CE.rates.empty | 0 |
| summaries.chosen_CE.grammar2 | 29 |
| summaries.chosen_CE.relevance2 | 15 |
| summaries.chosen_CE.coherent | 4 |
| summaries.chosen_CE.appropriate | 8 |
| summaries.chosen_CE.notes_sha256 | "23751d2a4c1c95a4dfeba074679f2329deb9dc2962790329f624f3d05485917d" |
| summaries.chosen_CE_DPO.BPB | 1.2236346693225277 |
| summaries.chosen_CE_DPO.rates.eos | 57 |
| summaries.chosen_CE_DPO.rates.repetition | 3 |
| summaries.chosen_CE_DPO.rates.unicode_failure | 1 |
| summaries.chosen_CE_DPO.rates.role_leak | 0 |
| summaries.chosen_CE_DPO.rates.empty | 0 |
| summaries.chosen_CE_DPO.grammar2 | 30 |
| summaries.chosen_CE_DPO.relevance2 | 16 |
| summaries.chosen_CE_DPO.coherent | 6 |
| summaries.chosen_CE_DPO.appropriate | 12 |
| summaries.chosen_CE_DPO.notes_sha256 | "438c4e1b9beb917bfea9d73d5bca7e129cc928556c950937f711fb6cfcc97592" |
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
| quality_comparison.chosen_CE.checks.coherence_gain_at_least8 | false |
| quality_comparison.chosen_CE.checks.paired_CI_lower_above0 | false |
| quality_comparison.chosen_CE.checks.EOS_nonworsening | false |
| quality_comparison.chosen_CE.checks.repetition_nonworsening | false |
| quality_comparison.chosen_CE.checks.no_empty_role_unicode | false |
| quality_comparison.chosen_CE.checks.BPB_gate | false |
| quality_comparison.chosen_CE.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.chosen_CE.passed | false |
| quality_comparison.chosen_CE_DPO.checks.coherence_gain_at_least8 | false |
| quality_comparison.chosen_CE_DPO.checks.paired_CI_lower_above0 | false |
| quality_comparison.chosen_CE_DPO.checks.EOS_nonworsening | false |
| quality_comparison.chosen_CE_DPO.checks.repetition_nonworsening | false |
| quality_comparison.chosen_CE_DPO.checks.no_empty_role_unicode | false |
| quality_comparison.chosen_CE_DPO.checks.BPB_gate | false |
| quality_comparison.chosen_CE_DPO.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.chosen_CE_DPO.passed | false |
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | true |
| matched_objective_quality.checks.repetition_nonworsening | true |
| matched_objective_quality.checks.no_empty_role_unicode | false |
| matched_objective_quality.checks.BPB_gate | true |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
| absolute_dev_screen.chosen_CE.grammar_at_least56 | false |
| absolute_dev_screen.chosen_CE.coherence_at_least27 | false |
| absolute_dev_screen.chosen_CE.appropriate_at_least27 | false |
| absolute_dev_screen.chosen_CE.EOS_at_least37 | true |
| absolute_dev_screen.chosen_CE.repetition_at_most18 | true |
| absolute_dev_screen.chosen_CE.no_empty_role_unicode | false |
| absolute_dev_screen.chosen_CE_DPO.grammar_at_least56 | false |
| absolute_dev_screen.chosen_CE_DPO.coherence_at_least27 | false |
| absolute_dev_screen.chosen_CE_DPO.appropriate_at_least27 | false |
| absolute_dev_screen.chosen_CE_DPO.EOS_at_least37 | true |
| absolute_dev_screen.chosen_CE_DPO.repetition_at_most18 | true |
| absolute_dev_screen.chosen_CE_DPO.no_empty_role_unicode | false |
| original_Web.chosen_CE.EOS_at_least8_more | true |
| original_Web.chosen_CE.repetition_no_worse | true |
| original_Web.chosen_CE.no_empty_role_unicode | false |
| original_Web.chosen_CE.BPB_degradation_at_most1percent | false |
| original_Web.chosen_CE_DPO.EOS_at_least8_more | true |
| original_Web.chosen_CE_DPO.repetition_no_worse | true |
| original_Web.chosen_CE_DPO.no_empty_role_unicode | false |
| original_Web.chosen_CE_DPO.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.chosen_CE | false |
| eligible_for_final_Base_validation.chosen_CE_DPO | false |
| accounting.common_Web.completed_updates | 184 |
| accounting.common_Web.positive_teacher_tokens | 6000000 |
| accounting.common_Web.physical_input_positions | 6029312 |
| accounting.common_Web.CE_body_bytes | 23365802 |
| accounting.common_Web.sampler.kind | "Base_preference_common_Web_exact_v1" |
| accounting.common_Web.sampler.goals.web | 6000000 |
| accounting.common_Web.sampler.context | 1024 |
| accounting.common_Web.sampler.position | 184 |
| accounting.common_Web.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| accounting.common_Web.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| accounting.common_Web.sampler.streams.web.sampler.seed | 42 |
| accounting.common_Web.sampler.streams.web.sampler.epoch | 0 |
| accounting.common_Web.sampler.streams.web.sampler.position | 10259808 |
| accounting.common_Web.sampler.streams.web.sampler.context | 1024 |
| accounting.common_Web.sampler.streams.web.sampler.blocks | 11939276 |
| accounting.common_Web.sampler.source_teachers.web | 6000000 |
| accounting.common_Web.sampler.source_eos.web | 12812 |
| accounting.common_Web.sampler.source_tokens.web | 6029312 |
| accounting.common_Web.sampler.source_body_bytes.web | 23365802 |
| accounting.common_Web.sampler.source_focus_teachers.web | 0 |
| accounting.chosen_CE.completed_updates | 439 |
| accounting.chosen_CE.positive_teacher_tokens | 2000000 |
| accounting.chosen_CE.physical_input_positions | 10472784 |
| accounting.chosen_CE.CE_body_bytes | 7509150 |
| accounting.chosen_CE.sampler.kind | "fixed_group_role_free_positive_quota_full_active_DPO_v1" |
| accounting.chosen_CE.sampler.goal | 2000000 |
| accounting.chosen_CE.sampler.batch | 56 |
| accounting.chosen_CE.sampler.span | 213 |
| accounting.chosen_CE.sampler.data_digest | "2b0220ab90f172f4e14bb3db2184dcf3f54b6586c420525b26ca204d7c0e9570" |
| accounting.chosen_CE.sampler.reference_digest | "1b3e76f36472ab739796e2860f58c93e63b5fcc274e9900ff68f2d2c02d2aad7" |
| accounting.chosen_CE.sampler.epoch | 439 |
| accounting.chosen_CE.sampler.group_position | 0 |
| accounting.chosen_CE.sampler.position | 439 |
| accounting.chosen_CE.sampler.teachers | 2000000 |
| accounting.chosen_CE.sampler.EOS | 24535 |
| accounting.chosen_CE.sampler.body_bytes | 7509150 |
| accounting.chosen_CE.sampler.physical | 10472784 |
| accounting.chosen_CE.sampler.valid | 4870705 |
| accounting.chosen_CE.sampler.scored_chosen | 2000038 |
| accounting.chosen_CE.sampler.scored_rejected | 1570304 |
| accounting.chosen_CE.sampler.active_pair_exposures | 24536 |
| accounting.chosen_CE.sampler.auxiliary_digest | "4c6e1b7f3a6ba38cffee1a264f2e909ff7f9d676194f5b5de44417a2926fb8d0" |
| accounting.chosen_CE_DPO.completed_updates | 439 |
| accounting.chosen_CE_DPO.positive_teacher_tokens | 2000000 |
| accounting.chosen_CE_DPO.physical_input_positions | 10472784 |
| accounting.chosen_CE_DPO.CE_body_bytes | 7509150 |
| accounting.chosen_CE_DPO.sampler.kind | "fixed_group_role_free_positive_quota_full_active_DPO_v1" |
| accounting.chosen_CE_DPO.sampler.goal | 2000000 |
| accounting.chosen_CE_DPO.sampler.batch | 56 |
| accounting.chosen_CE_DPO.sampler.span | 213 |
| accounting.chosen_CE_DPO.sampler.data_digest | "2b0220ab90f172f4e14bb3db2184dcf3f54b6586c420525b26ca204d7c0e9570" |
| accounting.chosen_CE_DPO.sampler.reference_digest | "1b3e76f36472ab739796e2860f58c93e63b5fcc274e9900ff68f2d2c02d2aad7" |
| accounting.chosen_CE_DPO.sampler.epoch | 439 |
| accounting.chosen_CE_DPO.sampler.group_position | 0 |
| accounting.chosen_CE_DPO.sampler.position | 439 |
| accounting.chosen_CE_DPO.sampler.teachers | 2000000 |
| accounting.chosen_CE_DPO.sampler.EOS | 24535 |
| accounting.chosen_CE_DPO.sampler.body_bytes | 7509150 |
| accounting.chosen_CE_DPO.sampler.physical | 10472784 |
| accounting.chosen_CE_DPO.sampler.valid | 4870705 |
| accounting.chosen_CE_DPO.sampler.scored_chosen | 2000038 |
| accounting.chosen_CE_DPO.sampler.scored_rejected | 1570304 |
| accounting.chosen_CE_DPO.sampler.active_pair_exposures | 24536 |
| accounting.chosen_CE_DPO.sampler.auxiliary_digest | "4c6e1b7f3a6ba38cffee1a264f2e909ff7f9d676194f5b5de44417a2926fb8d0" |
| matched_exposure.matched_updates | 439 |
| scientific_positive_teacher_tokens | 10000000 |
| common_positive_teacher_tokens | 6000000 |
| positive_teacher_tokens_per_arm | 8000000 |
| verification_teacher_tokens | 1694058 |
| new_total_GPU_seconds | 303.6357959379966 |
| diagnostic_GPU_seconds_separate | 69.95700160900014 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Only56 TRAIN pairs/4565 positive positions repeatedly exposed, about438 passes; not new2M source. Original8 weak rows excluded before preference labeling. Sequence length/genre and fixed stale negatives; one learned seed/nonblind repeated dev. Earlier seven numerical failures retained." |

</details>

<details>
<summary>reports/phase6/base_preference_prelaunch_geometry_field/unused_original_config.json — None</summary>

[原記録](../../reports/phase6/base_preference_prelaunch_geometry_field/unused_original_config.json) ／ SHA256: `ab2169ee42e55f1e1e40c6dcafe287effcb3baea6b1b6a67f0dcc1be6986a367` ／ 4,041 bytes

| 原キー | 保存値 |
|---|---|
| references.sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/livedoor-leads-20261006/sample64.json" |
| references.sample.sha256 | "15bb8043577705292c4a20ccb0400b6847179794d0d9c1e0c6c4913def9fa82a" |
| references.CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_preference_loss_tests.xml" |
| references.CPU_tests.sha256 | "fc8aab172ec530ca74eb501ce42c8a97deb19ffe061f43a67f6a4ec9a43db74b" |
| tokenizer.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/artifacts/phase2/4096/tokenizer.model" |
| tokenizer.sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| source_sha256.scripts/base_preference_loss.py | "5efea442ad8843d7f99fbfe7101b09b2f8a98d7c7f8cf5f073ff0eff4638f423" |
| source_sha256.tests/test_base_preference_loss.py | "ee6063949335852b3ecfe3b66b15acbce902b20fe2f9f0ae8ccf92fcdccd4775" |
| GPU_budget_seconds | 180 |
| CPU_preparation_seconds | 0.01130435400409624 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| protected_test_used | false |
| completion | "All64 original train pairs and raw generation/reference scores; fixed-reference DPO versus chosen-CE gradient geometry and read-only proof. Individually review generated pairs before any learning. No source/beta/LR/decoder/parent reroll." |
| limitations | "Source accepted at64-sample level includes8 weak originals; chosen suffix is not automatically a better continuation. Unequal sequence lengths and source genre matter. TRAIN-only/one model/nonblind/one beta; no general quality or KL-preservation guarantee. Old numerical7 failures preserved." |

</details>

<details>
<summary>reports/phase6/base_preference_science_launch.json — None</summary>

[原記録](../../reports/phase6/base_preference_science_launch.json) ／ SHA256: `c21e4b2357dee629b81f089b008632be7ad6ca5d93758956460d4ae84a073500` ／ 927 bytes

| 原キー | 保存値 |
|---|---|
| actual_job.status | "running" |
| actual_job.GPU_elapsed_seconds | 30.46311739401426 |
| actual_job.teachers | 273900 |
| actual_job.teacher_budget | 2000000 |
| actual_job.loss | 2.0212080478668213 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_preference_science_prepared.json — Base_preference_science_prepared</summary>

[原記録](../../reports/phase6/base_preference_science_prepared.json) ／ SHA256: `39ed60211658713ae37bad2d5471e526a0a827c52f545a861bc53acd1ee0e03f` ／ 3,651 bytes

| 原キー | 保存値 |
|---|---|
| status | "Base_preference_science_prepared" |
| actual_probe_job.status | "complete" |
| actual_probe_job.GPU_elapsed_seconds | 36.104522940004244 |
| actual_probe_job.completed_updates | 32 |
| probe_GPU_seconds | 36.104522940004244 |
| verification_updates | 152 |
| verification_teacher_tokens | 1694058 |
| selected_pair_batch | 56 |
| measured_timing.common.step_seconds | 0.13807362399529666 |
| measured_timing.common.teachers_per_update | 32698.375 |
| measured_timing.common.teachers_per_second | 236818.40205131314 |
| measured_timing.common.warmup_seconds | 1.073399668064667 |
| measured_timing.common.save_seconds | 0.16575832400121726 |
| measured_timing.pair.chosen_CE.step_seconds | 0.10567368600459304 |
| measured_timing.pair.chosen_CE.teachers_per_update | 4565.0 |
| measured_timing.pair.chosen_CE.teachers_per_second | 43199.023073744065 |
| measured_timing.pair.chosen_CE.warmup_seconds | 0.15122421400155872 |
| measured_timing.pair.chosen_CE.save_seconds | 0.16815711601520889 |
| measured_timing.pair.chosen_CE_DPO.step_seconds | 0.10522683600720484 |
| measured_timing.pair.chosen_CE_DPO.teachers_per_update | 4565.0 |
| measured_timing.pair.chosen_CE_DPO.teachers_per_second | 43382.46946517936 |
| measured_timing.pair.chosen_CE_DPO.warmup_seconds | 0.18579686095472425 |
| measured_timing.pair.chosen_CE_DPO.save_seconds | 0.18355330999474972 |
| measured_timing.updates.common | 184 |
| measured_timing.updates.chosen_CE | 446 |
| measured_timing.updates.chosen_CE_DPO | 446 |
| measured_timing.training_save_warmup_seconds | 122.2642483014497 |
| measured_timing.reference_cache_seconds | 0.35120013999403454 |
| estimated_total_GPU_seconds | 795.504605913881 |
| new_scientific_positive_teacher_tokens | 0 |
| diagnostic_GPU_seconds_separate | 69.95700160900014 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_preference_science_prepared_portable.json — None</summary>

[原記録](../../reports/phase6/base_preference_science_prepared_portable.json) ／ SHA256: `ec71893f11c156ecdcb76aa9b1773e5836a9376f982cb0072716bfce46fa780b` ／ 8,534 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/base_preference_science_prepared.json.bytes | 3651 |
| files.reports/phase6/base_preference_science_prepared.json.sha256 | "39ed60211658713ae37bad2d5471e526a0a827c52f545a861bc53acd1ee0e03f" |
| files.configs/phase6/base_preference_comparison.json.bytes | 13108 |
| files.configs/phase6/base_preference_probe.json.bytes | 5605 |
| files.reports/phase6/base_preference_comparison_proposal.json.bytes | 5297 |
| files.scripts/record_base_preference_progress.py.bytes | 4742 |
| files.scripts/run_base_preference_comparison.py.bytes | 17918 |
| files.scripts/run_base_preference_comparison.ps1.bytes | 2641 |
| files.scripts/base_preference_accounting.py.bytes | 6777 |
| files.scripts/review_base_preference_comparison.py.bytes | 8992 |
| files.scripts/record_base_preference_content.py.bytes | 3537 |
| files.tests/test_base_preference_science.py.bytes | 2865 |
| files.tests/test_base_preference_science.py.sha256 | "f354ad6714b82fc04466f2228d8e077471d02b7a5c9881e8b0b6305688b0d6a2" |
| files.reports/phase6/base_preference_science_tests.xml.bytes | 679 |
| files.reports/phase6/base_preference_science_tests.xml.sha256 | "3ba1a8fb6f097cfd5ae2365dbd6a525a359610c5ac8793c08a594202718865fe" |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch56/latest.json.bytes | 270 |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch56/latest.json.sha256 | "73f6fcf62a03f4cb869a4f6d118f64bdf9fc2ca82a14ad82d0e2c9065ddf6116" |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch56/metrics.jsonl.bytes | 29676 |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch8/latest.json.bytes | 269 |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch8/latest.json.sha256 | "fee900a09ff7839fe56de8852227eaa8b950c37919cfd8a068d59c7815055b25" |
| files.reports/phase6/base-preference-comparison-20261006/probe/DPO-batch8/metrics.jsonl.bytes | 29419 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE/latest.json.bytes | 268 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE/latest.json.sha256 | "14daa4f420880d473a2aa510df9ec8270ab4a76051dc0d4a62c98b16faf04a01" |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE/metrics.jsonl.bytes | 29580 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE-resume/latest.json.bytes | 276 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE-resume/latest.json.sha256 | "eeb16cbfb61395e568f5966a1ee65f17b0611b29a54e57822e473030a52b436f" |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE-resume/result.json.bytes | 10682 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE_DPO-resume/latest.json.bytes | 280 |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE_DPO-resume/latest.json.sha256 | "db242e93328560c4b8dc0e1dcea01d6d3a8970dcc53bca7ea98d3356bfa61bc8" |
| files.reports/phase6/base-preference-comparison-20261006/probe/chosen_CE_DPO-resume/result.json.bytes | 10683 |
| files.reports/phase6/base-preference-comparison-20261006/probe/common/latest.json.bytes | 265 |
| files.reports/phase6/base-preference-comparison-20261006/probe/common/latest.json.sha256 | "c11fe3d76e5c9715b434a51907cf746eb1810697bdeb2a328a410d7fe5dd8567" |
| files.reports/phase6/base-preference-comparison-20261006/probe/common/metrics.jsonl.bytes | 26880 |
| files.reports/phase6/base-preference-comparison-20261006/probe/common-resume/latest.json.bytes | 273 |
| files.reports/phase6/base-preference-comparison-20261006/probe/common-resume/latest.json.sha256 | "98ea2087721d77d24ce3d6a111f090598b357941cae39f45300f5338e83e31c2" |
| files.reports/phase6/base-preference-comparison-20261006/probe/common-resume/result.json.bytes | 10454 |
| files.reports/phase6/base-preference-comparison-20261006/probe/job.json.bytes | 578 |
| files.reports/phase6/base-preference-comparison-20261006/probe/reference-56.json.bytes | 4031 |
| files.reports/phase6/base-preference-comparison-20261006/probe/reference-8.json.bytes | 4618 |
| files.reports/phase6/base-preference-comparison-20261006/probe/result.json.bytes | 229740 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/configs/phase6/base_preference_probe.json.bytes | 5605 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/base_preference_loss.py.bytes | 2501 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/base_preference_loss.py.sha256 | "5efea442ad8843d7f99fbfe7101b09b2f8a98d7c7f8cf5f073ff0eff4638f423" |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/base_preference_trainer.py.bytes | 17632 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/probe_base_preference.ps1.bytes | 2603 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/probe_base_preference.py.bytes | 16043 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/probe_livedoor_base.py.bytes | 16328 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/tests/test_base_preference_trainer.py.bytes | 4288 |
| files.reports/phase6/base-preference-comparison-20261006/probe/source/tests/test_base_preference_trainer.py.sha256 | "0f6aa5da8d4c7ce86a06aa2d5d7ae86aa5ab7f53e51c6070e062babcd16fd6a9" |
| raw_source_pairs_and_tensors_native_only | true |

</details>

<details>
<summary>reports/phase6/base_sam_comparison_completion.json — SAM100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_sam_comparison_completion.json) ／ SHA256: `2f31f34c1235d3f13589e54c44fe695e748d63a11af1103c249de2fd44e28693` ／ 5,618 bytes

| 原キー | 保存値 |
|---|---|
| status | "SAM100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_updates | 17698 |
| scientific_repeated_teacher_evaluations | 100000000 |
| SAM.updates | 17698 |
| SAM.repeated_teacher_positions | 100000000 |
| SAM.repeated_physical_inputs | 370838917 |
| GPU_occupancy_seconds | 2618.2922464020085 |
| GPU_cap_seconds | 5398 |
| probe_GPU_seconds | 12.272191274008946 |
| total_GPU_seconds_including_probe | 2630.5644376760174 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-sam-comparison-20261007/sam/checkpoint-00017698.pt" |
| checkpoint_sha256 | "a78317d515cf29490ae979c1505b9a3cf9f05b8d78ab5ade6d8a7950e2ed50e8" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sam_notes.json" |
| notes.sha256 | "2de393a2b409acce5461730443e200e0e82ed5c93719d23ea87a8830344c4b3e" |
| reused_control_GPU_seconds | 0 |
| summaries.sam.BPB | 0.9994859554644886 |
| summaries.sam.rates.eos | 12 |
| summaries.sam.rates.repetition | 44 |
| summaries.sam.rates.unicode_failure | 0 |
| summaries.sam.rates.role_leak | 0 |
| summaries.sam.rates.empty | 0 |
| summaries.sam.grammar2 | 22 |
| summaries.sam.relevance2 | 23 |
| summaries.sam.coherent | 1 |
| summaries.sam.appropriate | 3 |
| summaries.sam.notes_sha256 | "2de393a2b409acce5461730443e200e0e82ed5c93719d23ea87a8830344c4b3e" |
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
| fixed_SAM_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 106105504 |
| archive.compressed_bundle.bytes | 46390369 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_sam_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_sam_comparison_evidence_manifest.json) ／ SHA256: `afc60d2881c1dfce23c71876eaf5c794507a4390afc11613e79f6261cc1866a9` ／ 8,858 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_sam_comparison_review.json — SAM_native100M_and_all80_reviewed</summary>

[原記録](../../reports/phase6/base_sam_comparison_review.json) ／ SHA256: `75bba8464675fbc542f4480d84bc90df4ceb1d69607f0d959414e2513bb0688f` ／ 5,300 bytes

| 原キー | 保存値 |
|---|---|
| status | "SAM_native100M_and_all80_reviewed" |
| summaries.sam.BPB | 0.9994859554644886 |
| summaries.sam.rates.eos | 12 |
| summaries.sam.rates.repetition | 44 |
| summaries.sam.rates.unicode_failure | 0 |
| summaries.sam.rates.role_leak | 0 |
| summaries.sam.rates.empty | 0 |
| summaries.sam.grammar2 | 22 |
| summaries.sam.relevance2 | 23 |
| summaries.sam.coherent | 1 |
| summaries.sam.appropriate | 3 |
| summaries.sam.notes_sha256 | "2de393a2b409acce5461730443e200e0e82ed5c93719d23ea87a8830344c4b3e" |
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
| matched_objective_quality.checks.repetition_nonworsening | true |
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
| GPU_seconds | 2618.2922464020085 |
| probe_GPU_seconds | 12.272191274008946 |
| SAM.updates | 17698 |
| SAM.repeated_teacher_positions | 100000000 |
| SAM.repeated_physical_inputs | 370838917 |
| scientific_repeated_teacher_evaluations | 100000000 |
| notes_sha256 | "2de393a2b409acce5461730443e200e0e82ed5c93719d23ea87a8830344c4b3e" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single seed and mature-parent optimizer transition; repeated nonblind DEV; second same-batch gradient and extra compute differ. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required." |
| reviewer_import_repair.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sam_reviewer_import_repair.json" |
| reviewer_import_repair.sha256 | "4e642a1ac5367bfceff0779d824e1206e1fbfd805af700e65a8003c47a715006" |
| reviewer_import_repair.original_reviewer_sha256 | "83e91d074562cea8fb92082f77514ceaa5345752eeae3ff037dd0cbffcfeaa1d" |
| reviewer_import_repair.wrapper_sha256 | "22ed2073f0c7c28f5314fa530a917fb4cf939d883d95c27484bfef2f654c30dd" |
| reviewer_import_repair.scientific_result_sha256 | "d97061e73dfd5fdfd4a950ee62ba0a953672a2c46f0bced9ae7e719c88a79ee9" |
| reviewer_import_repair.config_sha256 | "f8c956f16d7cb00c77ce8208191eb9bf2532f5766745c303b79f6591498414f2" |
| reviewer_import_repair.policy_sha256 | "47916dec587249a19c41eb85c1e4be28494313620fb5aad4ff6c3d8ff537ab45" |

</details>

<details>
<summary>reports/phase6/base_sam_notes.json — None</summary>

[原記録](../../reports/phase6/base_sam_notes.json) ／ SHA256: `2de393a2b409acce5461730443e200e0e82ed5c93719d23ea87a8830344c4b3e` ／ 15,833 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_sam_probe_launch.json — actual_SAM_CUDA_gate_passed_native100M_science_live</summary>

[原記録](../../reports/phase6/base_sam_probe_launch.json) ／ SHA256: `08f066e788abb606033867e3fddba153a8271915e8943b3f429d9bc80e89bf40` ／ 4,164 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_SAM_CUDA_gate_passed_native100M_science_live" |
| scientific_actual_identity.pid | 721383 |
| scientific_actual_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| scientific_actual_identity.start_ticks | "22188114" |
| scientific_config_sha256 | "f8c956f16d7cb00c77ce8208191eb9bf2532f5766745c303b79f6591498414f2" |
| probe_GPU_seconds | 12.272191274008946 |
| scientific_GPU_cap_seconds | 5398 |
| total_GPU_cap_seconds | 7200 |
| initial_checks.native_parent_weights | true |
| initial_checks.tied_native_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.all_parameters_once | true |
| resume_and_source_checks.kind | true |
| resume_and_source_checks.spec | true |
| resume_and_source_checks.binding | true |
| resume_and_source_checks.lineage | true |
| resume_and_source_checks.model_config | true |
| resume_and_source_checks.model | true |
| resume_and_source_checks.optimizer | true |
| resume_and_source_checks.scheduler | true |
| resume_and_source_checks.RNG | true |
| resume_and_source_checks.sampler | true |
| resume_and_source_checks.counters | true |
| resume_and_source_checks.SAM | true |
| resume_and_source_checks.finite_hybrid_model_buffers | true |
| resume_and_source_checks.history_except_timing | true |
| resume_and_source_checks.same_original_stream | true |
| resume_and_source_checks.full_sampler_matches_AdamW | true |
| capacity.context | 1024 |
| capacity.target_stride | 512 |
| capacity.batch | 48 |
| capacity.original_target_positions | 24576 |
| capacity.repeated_target_positions | 24576 |
| capacity.peak_VRAM_bytes | 10745064960 |
| capacity.optimizer_updates | 0 |
| capacity.exact_restoration | true |
| capacity.CE_loss | 2.2666423320770264 |
| capacity.perturbed_CE_loss | 2.432004928588867 |
| capacity.first_gradient_norm | 3.162024974822998 |
| capacity.gradient_norm | 3.5102455615997314 |
| capacity.perturbation_L2 | 0.05000000447034836 |
| verification_updates | 47 |
| verification_original_teacher_positions | 273521 |
| verification_repeated_teacher_evaluations | 250313 |
| exact_planned_completed_updates | 17698 |
| scientific_original_teacher_positions | 100000000 |
| scientific_repeated_teacher_evaluations | 100000000 |
| cached_control_GPU_repeated | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_sam_probe_launch_archive.json — None</summary>

[原記録](../../reports/phase6/base_sam_probe_launch_archive.json) ／ SHA256: `457f2f3767f44119ebc66b5fd162d7ab2ef48e1c22a7f040f87ae11005bef943` ／ 326 bytes

| 原キー | 保存値 |
|---|---|
| archive.bytes | 162014 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_sam_probe_launch_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_sam_probe_launch_evidence_manifest.json) ／ SHA256: `2b072c06185bfda07244f71f9ce05ce01c5076ff4510a8faa2effa0a8be88de3` ／ 3,544 bytes

| 原キー | 保存値 |
|---|---|
| probe_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_sam_proposal.json — None</summary>

[原記録](../../reports/phase6/base_sam_proposal.json) ／ SHA256: `7e041842040eb564b54d9effd06d44d1df56263e4a26f3c808a8294aef5551d6` ／ 5,211 bytes

| 原キー | 保存値 |
|---|---|
| references.base_failure_route_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_failure_route_synthesis.json" |
| references.base_failure_route_synthesis.json.sha256 | "2384411b47272b53b9e4eda981a69ff67e335069ca125a43e551c892515826b2" |
| references.base_muon_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_muon_comparison_completion.json" |
| references.base_muon_comparison_completion.json.sha256 | "cfa43645b777d9dd5e685cfbce25e4175278c5aeec9d91a2033a3ba82e94cbad" |
| references.base_on_policy_teacher_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_on_policy_teacher_comparison_completion.json" |
| references.base_on_policy_teacher_comparison_completion.json.sha256 | "022131b4a404867cc07ec69876ea069dfed03c91cafc8f96a33b1d96d834bfa5" |
| references.base_gradient_precision_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_gradient_precision_completion.json" |
| references.base_gradient_precision_completion.json.sha256 | "5e9112fb2ee9899dde5b670f48ba0d8ecf386c322f32a3d3ea181282f993d713" |
| literature_limit | "The NLP paper reports task finetuning/choice/QA gains on larger models. It does not prove free Japanese10M continuation quality; this is a local Base full-body/EOS study, no Chat/SFT." |
| recipe.second_batch | "identical_original_ids_targets_masks" |
| seed | 42 |
| original_teachers | 100000000 |
| repeated_SAM_teacher_evaluations | 100000000 |
| new_unique_dataset_tokens | 0 |
| control_reused_GPU_seconds | 0 |
| total_GPU_cap_seconds | 7200 |
| probe_GPU_cap_seconds | 180 |
| CPU_checks.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sam_trainer_tests.xml" |
| CPU_checks.sha256 | "1ff4fb144ae9f7dd31b10ae0e013517e9c208c94ed37aa723a9e161abd13af75" |
| acceptance | "Actual CPU and CUDA continuous4 vs2-save-resume2/full state, two-pass worst48x1024 finite gradients/restoration before science. Forecast ceil(exact17698 updates*mean32 measured two-pass seconds*1.3+900) plus actual probe within7200. Same cachedCE100M source and fullsampler, same256 commonbyte/Japanese192,331,1119/all80 raw-bound content, unchanged matched/strong/absolute/historicalWeb gates. Only qualified candidate gets independent learnedseed/fullDEV/protected finalTEST/adoption." |
| failure | "Close this one fixed condition on finite/state/radius/budget or quality failure. No rho/adaptive/period/optimizer/LR/parent/data/batch/decoder/cap rescue or extension." |
| limitations | "One conservative-LR mature-parent transition, extra second-pass compute, repeated nonblind DEV. Negative result does not disprove all SAM; local fit/likelihood is not useful Base quality." |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_sam_reviewer_import_repair.json — None</summary>

[原記録](../../reports/phase6/base_sam_reviewer_import_repair.json) ／ SHA256: `4e642a1ac5367bfceff0779d824e1206e1fbfd805af700e65a8003c47a715006` ／ 1,098 bytes

| 原キー | 保存値 |
|---|---|
| scientific_result_sha256 | "d97061e73dfd5fdfd4a950ee62ba0a953672a2c46f0bced9ae7e719c88a79ee9" |
| original_failure | "NameError: name 'math' is not defined" |
| failed_command | "uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_base_sam.py --template" |
| failed_stage | "Original all-history finite SAM guard; no notes or quality review created" |
| repair | "Bind standard-library math in original reviewer module globals only" |
| scientific_settings_changed | false |
| new_GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_sam_science_launch_snapshot.json — running</summary>

[原記録](../../reports/phase6/base_sam_science_launch_snapshot.json) ／ SHA256: `fc41ab80972a6e8aa08b4d54a580e19e8a3695ded7967130f36270885fb68b4c` ／ 980 bytes

| 原キー | 保存値 |
|---|---|
| status | "running" |
| GPU_occupancy_seconds | 28.37088393099839 |
| Base_complete | false |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 10745064960 |
| completed_updates | 180 |
| original_teachers | 1017618 |
| CE_loss | 2.7248172760009766 |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_comparison_completion.json — sigsoftmax100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_sigsoftmax_comparison_completion.json) ／ SHA256: `b30ea93293262f6a232b09251381f165129882bdf03afc12de0ca11e3fb23dd3` ／ 6,412 bytes

| 原キー | 保存値 |
|---|---|
| status | "sigsoftmax100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_updates | 17698 |
| scientific_sigsoftmax_positions | 100000000 |
| sigsoftmax_recipe.loss | "mean_hard_gold_NLL_under_sigsoftmax_probabilities" |
| sigsoftmax_recipe.teacher | false |
| GPU_occupancy_seconds | 1475.0260333089973 |
| GPU_cap_seconds | 3809 |
| probe_GPU_seconds | 9.708268066984601 |
| total_GPU_seconds_including_probe | 1484.7343013759819 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-sigsoftmax-comparison-20261007/sigsoftmax/checkpoint-00017698.pt" |
| checkpoint_sha256 | "d677598963b2a0e1fb283ea850f7f6e9cf7fd7cfe69564937d73d7133554b4f1" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_notes.json" |
| notes.sha256 | "8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881" |
| reused_control_GPU_seconds | 0 |
| summaries.sigsoftmax.BPB | 1.0010402885413023 |
| summaries.sigsoftmax.rates.eos | 19 |
| summaries.sigsoftmax.rates.repetition | 48 |
| summaries.sigsoftmax.rates.unicode_failure | 0 |
| summaries.sigsoftmax.rates.role_leak | 0 |
| summaries.sigsoftmax.rates.empty | 0 |
| summaries.sigsoftmax.grammar2 | 40 |
| summaries.sigsoftmax.relevance2 | 29 |
| summaries.sigsoftmax.coherent | 1 |
| summaries.sigsoftmax.appropriate | 1 |
| summaries.sigsoftmax.notes_sha256 | "8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881" |
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
| fixed_sigsoftmax_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 106533794 |
| archive.compressed_bundle.bytes | 45562803 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_sigsoftmax_comparison_evidence_manifest.json) ／ SHA256: `93b2b2a2d3662891f59d75809992382a2d92e70ecb1ff13653e2f6fb1e2579bc` ／ 11,536 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_comparison_review.json — sigsoftmax_native100M_and_all80_reviewed</summary>

[原記録](../../reports/phase6/base_sigsoftmax_comparison_review.json) ／ SHA256: `3a8eba1a996380225b21f5bfefc774ad7c15a7ddd9fa9463ccb5e3f998fe6524` ／ 5,143 bytes

| 原キー | 保存値 |
|---|---|
| status | "sigsoftmax_native100M_and_all80_reviewed" |
| summaries.sigsoftmax.BPB | 1.0010402885413023 |
| summaries.sigsoftmax.rates.eos | 19 |
| summaries.sigsoftmax.rates.repetition | 48 |
| summaries.sigsoftmax.rates.unicode_failure | 0 |
| summaries.sigsoftmax.rates.role_leak | 0 |
| summaries.sigsoftmax.rates.empty | 0 |
| summaries.sigsoftmax.grammar2 | 40 |
| summaries.sigsoftmax.relevance2 | 29 |
| summaries.sigsoftmax.coherent | 1 |
| summaries.sigsoftmax.appropriate | 1 |
| summaries.sigsoftmax.notes_sha256 | "8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881" |
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
| matched_objective_quality.checks.EOS_nonworsening | true |
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
| GPU_seconds | 1475.0260333089973 |
| probe_GPU_seconds | 9.708268066984601 |
| sigsoftmax_recipe.loss | "mean_hard_gold_NLL_under_sigsoftmax_probabilities" |
| sigsoftmax_recipe.teacher | false |
| scientific_sigsoftmax_positions | 100000000 |
| notes_sha256 | "8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single seed and mature-parent output-link transition; repeated nonblind DEV; normalized output probability link differs; same hard gold and native head. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required." |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_notes.json — None</summary>

[原記録](../../reports/phase6/base_sigsoftmax_notes.json) ／ SHA256: `8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881` ／ 26,060 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_probe_launch.json — actual_sigsoftmax_CUDA_gate_passed_native100M_science_live</summary>

[原記録](../../reports/phase6/base_sigsoftmax_probe_launch.json) ／ SHA256: `602960f15e08341386c12eaa5c1cd28df60cb25df16d0ea46d5a6360f650c558` ／ 4,146 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_sigsoftmax_CUDA_gate_passed_native100M_science_live" |
| scientific_actual_identity.pid | 740850 |
| scientific_actual_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| scientific_actual_identity.start_ticks | "23633274" |
| scientific_config_sha256 | "e5af1299b5f89d2ad346f0292b2a660f0146a448958aaca40d5a3e43c441fbac" |
| probe_GPU_seconds | 9.708268066984601 |
| scientific_GPU_cap_seconds | 3809 |
| total_GPU_cap_seconds | 4800 |
| initial_checks.native_parent_weights | true |
| initial_checks.tied_native_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.all_parameters_once | true |
| initial_checks.typed_BF16_full_link_once | true |
| initial_checks.same_weight_BF16_greedy_order | true |
| initial_checks.typed_BF16_cache_link_once | true |
| initial_checks.tagged_link | true |
| resume_and_source_checks.kind | true |
| resume_and_source_checks.spec | true |
| resume_and_source_checks.binding | true |
| resume_and_source_checks.lineage | true |
| resume_and_source_checks.model_config | true |
| resume_and_source_checks.model | true |
| resume_and_source_checks.optimizer | true |
| resume_and_source_checks.scheduler | true |
| resume_and_source_checks.RNG | true |
| resume_and_source_checks.sampler | true |
| resume_and_source_checks.counters | true |
| resume_and_source_checks.finite_hybrid_model_buffers | true |
| resume_and_source_checks.history_except_timing | true |
| resume_and_source_checks.same_original_stream | true |
| resume_and_source_checks.full_sampler_matches_AdamW | true |
| capacity.context | 1024 |
| capacity.target_stride | 512 |
| capacity.batch | 48 |
| capacity.original_target_positions | 24576 |
| capacity.peak_VRAM_bytes | 11510365184 |
| capacity.optimizer_updates | 0 |
| capacity.unchanged_weights | true |
| capacity.sigsoftmax_NLL_loss | 2.255953788757324 |
| capacity.gradient_norm | 3.2309505939483643 |
| capacity.decoder_forwards | 1 |
| capacity.output_probability_link | "sigsoftmax_exp_z_times_sigmoid_z_FP32_v1" |
| verification_updates | 47 |
| verification_original_teacher_positions | 273521 |
| verification_linked_probability_positions | 250313 |
| exact_planned_completed_updates | 17698 |
| scientific_original_teacher_positions | 100000000 |
| scientific_sigsoftmax_positions | 100000000 |
| cached_control_GPU_repeated | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_probe_launch_archive.json — None</summary>

[原記録](../../reports/phase6/base_sigsoftmax_probe_launch_archive.json) ／ SHA256: `1dae26b1075014746e2316a39a5bfaced3b5d3c0dab2e4b7ffaeb18a956134e8` ／ 333 bytes

| 原キー | 保存値 |
|---|---|
| archive.bytes | 380246 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_probe_launch_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_sigsoftmax_probe_launch_evidence_manifest.json) ／ SHA256: `0e9f3af1c6bd61e5afbd7dc5d85348dcb901d434e169904bd8d7380c98ae98b0` ／ 7,221 bytes

| 原キー | 保存値 |
|---|---|
| probe_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_proposal.json — prospective_fixed_output_link_comparison_before_implementation</summary>

[原記録](../../reports/phase6/base_sigsoftmax_proposal.json) ／ SHA256: `12c2f24b5287419ef57314c71edc73f5292d6414d07df09fb3c3294c04f4cbe4` ／ 7,888 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_fixed_output_link_comparison_before_implementation" |
| references.base_completed_objective_studies_v2_20261007.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_completed_objective_studies_v2_20261007.json" |
| references.base_completed_objective_studies_v2_20261007.json.sha256 | "37335ff5e0c06335569336c7c3dfbef7ccd71d6321a0c891e6e753f254f03771" |
| references.base_native_hint_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_hint_comparison_completion.json" |
| references.base_native_hint_comparison_completion.json.sha256 | "4428ed56bed8c08287feee48da26c52dc5b5c365a9e131d988559bff17df31b4" |
| references.base_native_teacher_KD_science_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_teacher_KD_science_comparison_completion.json" |
| references.base_native_teacher_KD_science_comparison_completion.json.sha256 | "94ddf90c0e90215ce1e0666da90c90e140822a01d31133c5f1ae4881add5698a" |
| references.base_embedding_gradient_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_embedding_gradient_completion.json" |
| references.base_embedding_gradient_completion.json.sha256 | "1fd5cae17e1116c87c52db5f68dd3b85d76e538c9268ae17b872801ec2923cf7" |
| references.base_failure_route_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_failure_route_synthesis.json" |
| references.base_failure_route_synthesis.json.sha256 | "2384411b47272b53b9e4eda981a69ff67e335069ca125a43e551c892515826b2" |
| references.base_capacity_reference_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_capacity_reference_synthesis.json" |
| references.base_capacity_reference_synthesis.json.sha256 | "ba603b7bd2d90b54300eee86815f6ed7fa10cf1c250e38420b1998ac5c52fe14" |
| limitation | "A256-dimensional linear head can restrict attainable distributions, but this is not evidence that its rank causes current repetitions. Sigsoftmax is an established hypothesis, not novel mathematics, and does not guarantee coherent prose." |
| recipe.loss | "mean_hard_original_body_and_EOS_NLL_under_sigsoftmax_probabilities" |
| recipe.teacher | false |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seed | 42 |
| resource.total_GPU_cap_seconds | 4800 |
| resource.probe_GPU_cap_seconds | 180 |
| resource.CPU_preparation_cap_seconds | 30 |
| failure | "Close on numerics/resume/metadata/capacity/budget or quality failure; no shift/temperature/learned calibration/variant/parent/LR/source/batch/backend/decoder/cap rescue or automatic extension." |
| implementation.CPU_tests_run | false |
| implementation.GPU_probe | false |
| new_GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_rating_reuse.json — None</summary>

[原記録](../../reports/phase6/base_sigsoftmax_rating_reuse.json) ／ SHA256: `b68e307295d9305495e05a3c0b7e8f94726d9b760ebc21ececc1528be1e72700` ／ 14,936 bytes

| 原キー | 保存値 |
|---|---|
| candidate_notes_sha256 | "8e197ba8ab5e9351d6f9c2963ff96d0a44d7c8d8122c26266d9d3cc0f9a0a881" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| scope | "Mechanical exact id/prefix/text/stop and score audit after current80 reading; not new human or blind ratings." |

</details>

<details>
<summary>reports/phase6/base_sigsoftmax_science_launch_snapshot.json — running</summary>

[原記録](../../reports/phase6/base_sigsoftmax_science_launch_snapshot.json) ／ SHA256: `8a5468ca0dce9d8a13aaf9ace73ea4851d0105258fd758fbfd0a5acebde49fe4` ／ 994 bytes

| 原キー | 保存値 |
|---|---|
| status | "running" |
| GPU_occupancy_seconds | 21.05286440398777 |
| Base_complete | false |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 11510365184 |
| completed_updates | 220 |
| original_teachers | 1242231 |
| CE_loss | 2.5468883514404297 |

</details>

<details>
<summary>reports/phase6/base_storage_reader_completion_20261007.json — storage_expanded_reader_comparison_complete</summary>

[原記録](../../reports/phase6/base_storage_reader_completion_20261007.json) ／ SHA256: `1820f5391a56a1bbf5d73e6e1f4bb45626a0357a061e77a371d348841a220046` ／ 4,299 bytes

| 原キー | 保存値 |
|---|---|
| status | "storage_expanded_reader_comparison_complete" |
| disk.total_bytes | 2163361103872 |
| disk.used_bytes | 1014755119104 |
| disk.available_bytes | 1038638051328 |
| disk_limit_not_physical_preallocation | true |
| accepted_source_binding_after_restart.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| accepted_source_binding_after_restart.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| accepted_source_binding_after_restart.index_size | 12861257655 |
| accepted_source_binding_after_restart.index_mtime_ns | 1791234945567297288 |
| accepted_source_binding_after_restart.stream_size | 4000002624 |
| accepted_source_binding_after_restart.stream_mtime_ns | 1791234945514053852 |
| accepted_source_binding_after_restart.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| accepted_source_binding_after_restart.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| accepted_source_identity_checked_by_all8_samplers | true |
| warm_cycle_median_supply_seconds.buffered | 0.16781778000017766 |
| warm_cycle_median_supply_seconds.mmap | 0.18899241549988233 |
| mmap_reader_selection_eligible | false |
| reader_adopted_for_training | false |
| decision | "Prototype failed the prospective10% speedup criterion on this cohort; retain existing buffered reader. No universal mmap failure claim or architecture timing claim." |
| UI.HTTP_model.training_tokens | 10000007168 |
| UI.HTTP_model.update | 305176 |
| UI.HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| UI.checkpoint_rehash | false |
| new_scientific_gold_tokens | 0 |
| new_unique_dataset_tokens | 0 |
| new_GPU_training_seconds | 0 |
| independent_trained_seed_done | false |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| old_FFN_and_MHA_caps_remain_closed | true |

</details>

<details>
<summary>reports/phase6/base_token_geometry_TRAIN_payload.json — None</summary>

[原記録](../../reports/phase6/base_token_geometry_TRAIN_payload.json) ／ SHA256: `e844f1bf96569844d9ff2effd1564cd65633a083902b24872aefc7f61fa01ba4` ／ 23,092 bytes

| 原キー | 保存値 |
|---|---|
| sampler_seed | 2026100703 |
| prepared_new_corpus_tokens | 0 |
| scientific_teacher_positions | 0 |

</details>

<details>
<summary>reports/phase6/base_token_geometry_completion.json — completed_readonly_token_geometry_screen</summary>

[原記録](../../reports/phase6/base_token_geometry_completion.json) ／ SHA256: `0b9be2e9b78020b732e84f273e9c70b788ed1bfede6f64e107befe61df507f5b` ／ 9,737 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_readonly_token_geometry_screen" |
| GPU_seconds | 1.3437756189960055 |
| GPU_cap_seconds | 120 |
| CPU_preparation_seconds | 0.3310242229781579 |
| actual_CUDA_readonly_checks.parent.model_eval | true |
| actual_CUDA_readonly_checks.parent.no_parameter_grads | true |
| actual_CUDA_readonly_checks.parent.native_count | true |
| actual_CUDA_readonly_checks.parent.model_config_unchanged | true |
| actual_CUDA_readonly_checks.parent.weights_unchanged | true |
| actual_CUDA_readonly_checks.parent.RNG_unchanged | true |
| actual_CUDA_readonly_checks.cached_CE.model_eval | true |
| actual_CUDA_readonly_checks.cached_CE.no_parameter_grads | true |
| actual_CUDA_readonly_checks.cached_CE.native_count | true |
| actual_CUDA_readonly_checks.cached_CE.model_config_unchanged | true |
| actual_CUDA_readonly_checks.cached_CE.weights_unchanged | true |
| actual_CUDA_readonly_checks.cached_CE.RNG_unchanged | true |
| actual_CUDA_readonly_checks.strong_staged.model_eval | true |
| actual_CUDA_readonly_checks.strong_staged.no_parameter_grads | true |
| actual_CUDA_readonly_checks.strong_staged.native_count | true |
| actual_CUDA_readonly_checks.strong_staged.model_config_unchanged | true |
| actual_CUDA_readonly_checks.strong_staged.weights_unchanged | true |
| actual_CUDA_readonly_checks.strong_staged.RNG_unchanged | true |
| models.parent.web.all_body_offdiagonal.ordered_pairs | 32976 |
| models.parent.web.all_body_offdiagonal.cosine_above095_pairs | 12 |
| models.parent.web.primary_distinct_ID_separated4.ordered_pairs | 30666 |
| models.parent.web.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.parent.web.documents | 4 |
| models.parent.textbook.all_body_offdiagonal.ordered_pairs | 56686 |
| models.parent.textbook.all_body_offdiagonal.cosine_above095_pairs | 20 |
| models.parent.textbook.primary_distinct_ID_separated4.ordered_pairs | 53162 |
| models.parent.textbook.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.parent.textbook.documents | 4 |
| models.parent.story.all_body_offdiagonal.ordered_pairs | 40824 |
| models.parent.story.all_body_offdiagonal.cosine_above095_pairs | 40 |
| models.parent.story.primary_distinct_ID_separated4.ordered_pairs | 37968 |
| models.parent.story.primary_distinct_ID_separated4.cosine_above095_pairs | 4 |
| models.parent.story.documents | 4 |
| models.cached_CE.web.all_body_offdiagonal.ordered_pairs | 32976 |
| models.cached_CE.web.all_body_offdiagonal.cosine_above095_pairs | 12 |
| models.cached_CE.web.primary_distinct_ID_separated4.ordered_pairs | 30666 |
| models.cached_CE.web.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.cached_CE.web.documents | 4 |
| models.cached_CE.textbook.all_body_offdiagonal.ordered_pairs | 56686 |
| models.cached_CE.textbook.all_body_offdiagonal.cosine_above095_pairs | 16 |
| models.cached_CE.textbook.primary_distinct_ID_separated4.ordered_pairs | 53162 |
| models.cached_CE.textbook.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.cached_CE.textbook.documents | 4 |
| models.cached_CE.story.all_body_offdiagonal.ordered_pairs | 40824 |
| models.cached_CE.story.all_body_offdiagonal.cosine_above095_pairs | 38 |
| models.cached_CE.story.primary_distinct_ID_separated4.ordered_pairs | 37968 |
| models.cached_CE.story.primary_distinct_ID_separated4.cosine_above095_pairs | 4 |
| models.cached_CE.story.documents | 4 |
| models.strong_staged.web.all_body_offdiagonal.ordered_pairs | 32976 |
| models.strong_staged.web.all_body_offdiagonal.cosine_above095_pairs | 0 |
| models.strong_staged.web.primary_distinct_ID_separated4.ordered_pairs | 30666 |
| models.strong_staged.web.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.strong_staged.web.documents | 4 |
| models.strong_staged.textbook.all_body_offdiagonal.ordered_pairs | 56686 |
| models.strong_staged.textbook.all_body_offdiagonal.cosine_above095_pairs | 2 |
| models.strong_staged.textbook.primary_distinct_ID_separated4.ordered_pairs | 53162 |
| models.strong_staged.textbook.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.strong_staged.textbook.documents | 4 |
| models.strong_staged.story.all_body_offdiagonal.ordered_pairs | 40824 |
| models.strong_staged.story.all_body_offdiagonal.cosine_above095_pairs | 0 |
| models.strong_staged.story.primary_distinct_ID_separated4.ordered_pairs | 37968 |
| models.strong_staged.story.primary_distinct_ID_separated4.cosine_above095_pairs | 0 |
| models.strong_staged.story.documents | 4 |
| fixed_decision.passed | false |
| fixed_decision.parent_and_CE_shared_marked_sources | [] |
| fixed_decision.marked_sources.parent | [] |
| fixed_decision.marked_sources.cached_CE | [] |
| fixed_decision.marked_sources.strong_staged | [] |
| fixed_decision.rule | "FP32 normalized final native states; body IDs&gt;=8; distinct input IDs; absolute position separation&gt;=4; cosine&gt;.95 in&gt;=25percent ordered eligible pairs; same&gt;=two sources in both original parent and cached CE" |
| fixed_decision.causal_proof | false |
| fixed_decision.Base_quality_gate | false |
| fixed_decision.global_isotropy_proof | false |
| fixed_decision.limitation | "Twelve fixed short TRAIN units; pooled pairs are correlated, not independent samples. A negative rules out this prespecified severe marker here, not all geometry effects. A positive only permits implementing one independent matched study." |
| fixed_severe_marker_condition_closed | true |
| new_scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 754435 |
| archive.compressed_bundle.bytes | 219684 |
| interpretation | "No severe marker in these fixed short TRAIN units. Not proof of globally isotropic states, absence of every geometric effect, causal sufficiency or useful Base quality." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_token_geometry_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_token_geometry_evidence_manifest.json) ／ SHA256: `63e873f5dd6be9e12f85a278707bf9f69606c72a79636aeec30d9184240c6ff0` ／ 4,624 bytes

| 原キー | 保存値 |
|---|---|
| original_native_checkpoints_preserved | true |

</details>

<details>
<summary>reports/phase6/base_token_geometry_proposal.json — prospective_severe_token_geometry_screen_before_GPU</summary>

[原記録](../../reports/phase6/base_token_geometry_proposal.json) ／ SHA256: `66353299b08d13e0118533ca105da73015e2919ef0d44874b13bffad88045b61` ／ 6,976 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_severe_token_geometry_screen_before_GPU" |
| references.base_completed_objective_studies_v3_20261007.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_completed_objective_studies_v3_20261007.json" |
| references.base_completed_objective_studies_v3_20261007.json.sha256 | "716b4ef75300e630d76467e75146734777dfd31c8023fb2449548ffb0f1f7252" |
| references.base_sigsoftmax_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sigsoftmax_comparison_completion.json" |
| references.base_sigsoftmax_comparison_completion.json.sha256 | "b30ea93293262f6a232b09251381f165129882bdf03afc12de0ca11e3fb23dd3" |
| references.base_kv_allocation_bucketed_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_kv_allocation_bucketed_completion.json" |
| references.base_kv_allocation_bucketed_completion.json.sha256 | "604dc6d65f15ffe2b7b78e3783cf6538b85799bc85134c1facb0c5fb26f613da" |
| references.base_embedding_gradient_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_embedding_gradient_completion.json" |
| references.base_embedding_gradient_completion.json.sha256 | "1fd5cae17e1116c87c52db5f68dd3b85d76e538c9268ae17b872801ec2923cf7" |
| references.base_attention_saturation_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_attention_saturation_completion.json" |
| references.base_attention_saturation_completion.json.sha256 | "78a8c02ec4a8a5740b7ee4eb049d5a859ef68d93374932819dd91217534c41ed" |
| prefix_tokens_at_most | 128 |
| budgets.CPU_preparation_cap_seconds | 30 |
| budgets.GPU_cap_seconds | 120 |
| budgets.optimizer_updates | 0 |
| budgets.new_gold_tokens | 0 |
| completion | "Actual exited bounded read-only CUDA result/all12units on all3models; original weights/no grads/RNG/parameters unchanged; finite pair metrics/denominators and fixed decision; restore original UI/portable evidence/local commit." |
| scope | "Correlated token pairs in twelve short TRAIN prefixes; not global rank/causal proof. Does not infer useful Japanese quality, data futility or10M capacity ceiling." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| new_GPU_seconds | 0 |
| new_scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/base_wsl_storage_expansion_before_20261007.json — None</summary>

[原記録](../../reports/phase6/base_wsl_storage_expansion_before_20261007.json) ／ SHA256: `38d79977619467b604ca01c9725dadf41c01b6c9815151370779965f17162bb0` ／ 426 bytes

| 原キー | 保存値 |
|---|---|
| windows_C_available_bytes | 2115392581632 |
| captured_at | "2026-10-07T07:06:54.6441814Z" |
| base_complete | false |
| windows_C_total_bytes | 3999613841408 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/latest.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/latest.json) ／ SHA256: `f6a8a1d739573ab203c5e3abf549ca21d265cb633640acb174ce023a5f3c7244` ／ 289 bytes

| 原キー | 保存値 |
|---|---|
| update | 323035 |
| tokens_seen | 10585210880 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/compare-result.json — block_rejection_branch_complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/compare-result.json) ／ SHA256: `9002fe5fea414833a0805bbbca27dcbe546f02a66ed222bab76402a4865fc6d8` ／ 2,934 bytes

| 原キー | 保存値 |
|---|---|
| finite_rejection.last_rejection.decision.reference_body_NLL | 2.5812628269195557 |
| finite_rejection.last_rejection.decision.ceiling_body_NLL | 2.607075455188751 |
| finite_rejection.last_rejection.decision.proposed_body_NLL | 2.621283769607544 |
| finite_rejection.last_rejection.decision.projected | true |
| finite_rejection.last_rejection.decision.backtracked | false |
| finite_rejection.last_rejection.decision.accepted | false |
| finite_rejection.last_rejection.decision.gradient_body_NLL | 2.621283769607544 |
| finite_rejection.last_rejection.decision.gradient_norm_squared | 2.0499785066566316 |
| finite_rejection.last_rejection.decision.projection_coefficient | 0.006943549408367611 |
| finite_rejection.last_rejection.decision.error | "All four corrected finite proposals violate fixed memory bound" |
| finite_rejection.last_rejection.attempted_source_gradient_teacher_tokens | 650524 |
| finite_rejection.last_rejection.attempted_source_updates | 20 |
| finite_rejection.last_rejection.auxiliary_completed_calls.teacher_observations | 195828 |
| finite_rejection.last_rejection.auxiliary_completed_calls.gradient_teacher_tokens | 32638 |
| finite_rejection.last_rejection.auxiliary_completed_calls.physical_input_tokens | 196608 |
| finite_rejection.last_rejection.restored_last_completed_update | 323035 |
| finite_rejection.last_rejection.rollback_scope | "entire_tentative_block" |
| finite_rejection.last_valid_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/checkpoint-00323035.pt" |
| finite_rejection.last_valid_checkpoint.sha256 | "1db5c4a6505b706aa9497424d6d0309efd00587345c86d03b5a2e48e66bc6744" |
| finite_rejection.accepted_source_updates | 2600 |
| finite_rejection.accepted_source_CE_teacher_tokens | 84961352 |
| finite_rejection.accepted_auxiliary.forward_only_calls | 162 |
| finite_rejection.accepted_auxiliary.gradient_calls | 13 |
| finite_rejection.accepted_auxiliary.teacher_observations | 5711650 |
| finite_rejection.accepted_auxiliary.gradient_teacher_tokens | 424294 |
| finite_rejection.accepted_auxiliary.physical_input_tokens | 5734400 |
| finite_rejection.accepted_auxiliary.projected_updates | 13 |
| finite_rejection.accepted_auxiliary.backtracked_updates | 13 |
| finite_rejection.accepted_auxiliary.accepted_updates | 2600 |
| finite_rejection.accepted_auxiliary.accepted_blocks | 130 |
| status | "block_rejection_branch_complete" |
| GPU_seconds | 193.6470071610238 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/job.json) ／ SHA256: `caf1252899da66d77f3ac8c2f700fb7f0cfe4d251c987f2f081dbdadc76c98c8` ／ 2,077 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 193.6470071610238 |
| completed_updates | 2600 |
| total_updates | 3068 |
| actual_teachers | 84961352 |
| loss | 2.2298552989959717 |
| boundary_constraint.reference_body_NLL | 2.5812628269195557 |
| boundary_constraint.ceiling_body_NLL | 2.607075455188751 |
| boundary_constraint.proposed_body_NLL | 2.6213528513908386 |
| boundary_constraint.accepted | true |
| boundary_constraint.gradient_body_NLL | 2.6213528513908386 |
| boundary_constraint.final_body_NLL | 2.6070653200149536 |
| boundary_constraint.scope | "accepted_block_boundary_only" |
| boundary_constraint.block_start_update | 323015 |
| boundary_constraint.block_end_update | 323035 |
| boundary_constraint.block_source_updates | 20 |
| auxiliary.teacher_observations | 5711650 |
| auxiliary.gradient_teacher_tokens | 424294 |
| auxiliary.physical_input_tokens | 5734400 |
| auxiliary.projected_updates | 13 |
| auxiliary.backtracked_updates | 13 |
| auxiliary.accepted_updates | 2600 |
| auxiliary.accepted_blocks | 130 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/probe/job.json) ／ SHA256: `2a74895d26c1490b0941bf52476f1db778066144be2d31e54b485bbaea50d134` ／ 537 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 33.67857302899938 |
| completed_updates | 80 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/probe/latest.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/probe/latest.json) ／ SHA256: `197155ab439670a276d924923ada3cc8bf19262f689dc0ca16050e99e93c5afe` ／ 253 bytes

| 原キー | 保存値 |
|---|---|
| update | 320475 |
| tokens_seen | 10501324800 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/probe/progress-result.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/probe/progress-result.json) ／ SHA256: `1e8d794808a418f7b23582b5b93d642e80ab842c5b4e2c8b7a70cef6e16273d7` ／ 910,126 bytes

| 原キー | 保存値 |
|---|---|
| initial_checks.model | true |
| initial_checks.optimizer | true |
| initial_checks.scheduler | true |
| initial_checks.RNG | true |
| initial_checks.Web_cursor | true |
| initial_checks.actual_LR | true |
| initial_checks.same_original_memory_NLL | true |
| reference_body_NLL | 2.5812628269195557 |
| setup_oracle_counts.teacher_observations | 32638 |
| setup_oracle_counts.gradient_teacher_tokens | 0 |
| setup_oracle_counts.physical_input_tokens | 32768 |
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
| gate.checks.study_binding | true |
| gate.checks.pilot_binding | true |
| gate.checks.lineage | true |
| gate.checks.auxiliary | true |
| gate.checks.last_constraint | true |
| gate.checks.branch_updates | true |
| gate.checks.branch_tokens | true |
| gate.checks.history_block_boundary_index | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_loss | true |
| gate.checks.history_block_boundary_update | true |
| gate.checks.history_valid_input_tokens | true |
| gate.checks.history_additional_teacher_tokens | true |
| gate.checks.history_constraint_valid_only_at_block_boundary | true |
| gate.checks.history_outcome_weight | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_actual_source_eos | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_removed_prefix_targets | true |
| gate.checks.history_supervised_tokens | true |
| gate.checks.history_reference_suffix_teacher_tokens | true |
| gate.checks.history_lr | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_accepted_auxiliary | true |
| gate.checks.history_reference_token_digest | true |
| gate.checks.history_actual_source_body_bytes | true |
| gate.checks.history_boundary_constraint | true |
| gate.checks.history_body_bytes_seen | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_physical_input_tokens | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_actual_source_routes | true |
| gate.checks.history_update | true |
| gate.checks.history_source_digests | true |
| gate.checks.history_tokens_seen | true |
| gate.checks.history_actual_source_teachers | true |
| gate.checks.finite | true |
| gate.checks.actual_LR | true |
| gate.checks.boundary_loss_bounded | true |
| gate.checks.two_full20_update_blocks | true |
| gate.verification_teacher_tokens | 2615872 |
| gate.GPU_optimizer_updates | 80 |
| timing.terminal_save_seconds | 0.16710195899941027 |
| timing.verification_teacher_tokens | 2615876 |
| timing.auxiliary.teacher_observations | 130552 |
| timing.auxiliary.gradient_teacher_tokens | 0 |
| timing.auxiliary.physical_input_tokens | 131072 |
| timing.auxiliary.projected_updates | 0 |
| timing.auxiliary.backtracked_updates | 0 |
| timing.auxiliary.accepted_updates | 80 |
| timing.auxiliary.accepted_blocks | 4 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/probe/result.json — block_probe_complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/probe/result.json) ／ SHA256: `3f418b197c206c384d9b04410a83746db12887c19dde4c588c1ad1e6e55669e4` ／ 912,225 bytes

| 原キー | 保存値 |
|---|---|
| initial_checks.model | true |
| initial_checks.optimizer | true |
| initial_checks.scheduler | true |
| initial_checks.RNG | true |
| initial_checks.Web_cursor | true |
| initial_checks.actual_LR | true |
| initial_checks.same_original_memory_NLL | true |
| reference_body_NLL | 2.5812628269195557 |
| setup_oracle_counts.teacher_observations | 32638 |
| setup_oracle_counts.gradient_teacher_tokens | 0 |
| setup_oracle_counts.physical_input_tokens | 32768 |
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
| gate.checks.study_binding | true |
| gate.checks.pilot_binding | true |
| gate.checks.lineage | true |
| gate.checks.auxiliary | true |
| gate.checks.last_constraint | true |
| gate.checks.branch_updates | true |
| gate.checks.branch_tokens | true |
| gate.checks.history_block_boundary_index | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_loss | true |
| gate.checks.history_block_boundary_update | true |
| gate.checks.history_valid_input_tokens | true |
| gate.checks.history_additional_teacher_tokens | true |
| gate.checks.history_constraint_valid_only_at_block_boundary | true |
| gate.checks.history_outcome_weight | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_actual_source_eos | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_removed_prefix_targets | true |
| gate.checks.history_supervised_tokens | true |
| gate.checks.history_reference_suffix_teacher_tokens | true |
| gate.checks.history_lr | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_accepted_auxiliary | true |
| gate.checks.history_reference_token_digest | true |
| gate.checks.history_actual_source_body_bytes | true |
| gate.checks.history_boundary_constraint | true |
| gate.checks.history_body_bytes_seen | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_physical_input_tokens | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_actual_source_routes | true |
| gate.checks.history_update | true |
| gate.checks.history_source_digests | true |
| gate.checks.history_tokens_seen | true |
| gate.checks.history_actual_source_teachers | true |
| gate.checks.finite | true |
| gate.checks.actual_LR | true |
| gate.checks.boundary_loss_bounded | true |
| gate.checks.two_full20_update_blocks | true |
| gate.verification_teacher_tokens | 2615872 |
| gate.GPU_optimizer_updates | 80 |
| timing.terminal_save_seconds | 0.16710195899941027 |
| timing.verification_teacher_tokens | 2615876 |
| timing.auxiliary.teacher_observations | 130552 |
| timing.auxiliary.gradient_teacher_tokens | 0 |
| timing.auxiliary.physical_input_tokens | 131072 |
| timing.auxiliary.projected_updates | 0 |
| timing.auxiliary.backtracked_updates | 0 |
| timing.auxiliary.accepted_updates | 80 |
| timing.auxiliary.accepted_blocks | 4 |
| passed | true |
| GPU_optimizer_updates | 160 |
| verification_source_CE_teacher_tokens | 5231748 |
| scientific_source_CE_teacher_tokens | 0 |
| cached_projector_control_reused_without_new_GPU | true |
| cached_projector_control.reference_body_NLL | 2.5812628269195557 |
| cached_projector_control.ceiling_body_NLL | 2.607075455188751 |
| cached_projector_control.proposed_body_NLL | 2.881101965904236 |
| cached_projector_control.accepted | true |
| cached_projector_control.gradient_body_NLL | 2.881101965904236 |
| cached_projector_control.final_body_NLL | 2.6045130491256714 |
| cached_projector_control.stored_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| cached_projector_control.stored_checkpoint.sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| cached_projector_control.initial_stored_body_NLL | 2.881101965904236 |
| cached_projector_control.auxiliary.teacher_observations | 163190 |
| cached_projector_control.auxiliary.gradient_teacher_tokens | 32638 |
| cached_projector_control.auxiliary.physical_input_tokens | 163840 |
| cached_projector_control.diagnostic_weights_not_adopted_or_saved | true |
| cached_projector_control.original_checkpoint_file_unchanged | true |
| status | "block_probe_complete" |
| GPU_seconds | 33.67857302899938 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/probe/timing/latest.json) ／ SHA256: `768cabcc3a940cc436273c600b48f30d4bc9c8bf015804a7973763db052c497a` ／ 263 bytes

| 原キー | 保存値 |
|---|---|
| update | 320515 |
| tokens_seen | 10502635520 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-20261006/progress-result.json) ／ SHA256: `be5c18da942575416507727c8b1db62051d2c61225f9e738dfc6d75b2d22db2a` ／ 2,468 bytes

| 原キー | 保存値 |
|---|---|
| finite_rejection.last_rejection.decision.reference_body_NLL | 2.5812628269195557 |
| finite_rejection.last_rejection.decision.ceiling_body_NLL | 2.607075455188751 |
| finite_rejection.last_rejection.decision.proposed_body_NLL | 2.621283769607544 |
| finite_rejection.last_rejection.decision.projected | true |
| finite_rejection.last_rejection.decision.backtracked | false |
| finite_rejection.last_rejection.decision.accepted | false |
| finite_rejection.last_rejection.decision.gradient_body_NLL | 2.621283769607544 |
| finite_rejection.last_rejection.decision.gradient_norm_squared | 2.0499785066566316 |
| finite_rejection.last_rejection.decision.projection_coefficient | 0.006943549408367611 |
| finite_rejection.last_rejection.decision.error | "All four corrected finite proposals violate fixed memory bound" |
| finite_rejection.last_rejection.attempted_source_gradient_teacher_tokens | 650524 |
| finite_rejection.last_rejection.attempted_source_updates | 20 |
| finite_rejection.last_rejection.auxiliary_completed_calls.teacher_observations | 195828 |
| finite_rejection.last_rejection.auxiliary_completed_calls.gradient_teacher_tokens | 32638 |
| finite_rejection.last_rejection.auxiliary_completed_calls.physical_input_tokens | 196608 |
| finite_rejection.last_rejection.restored_last_completed_update | 323035 |
| finite_rejection.last_rejection.rollback_scope | "entire_tentative_block" |
| finite_rejection.last_valid_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/checkpoint-00323035.pt" |
| finite_rejection.last_valid_checkpoint.sha256 | "1db5c4a6505b706aa9497424d6d0309efd00587345c86d03b5a2e48e66bc6744" |
| finite_rejection.accepted_source_updates | 2600 |
| finite_rejection.accepted_source_CE_teacher_tokens | 84961352 |
| finite_rejection.accepted_auxiliary.forward_only_calls | 162 |
| finite_rejection.accepted_auxiliary.gradient_calls | 13 |
| finite_rejection.accepted_auxiliary.teacher_observations | 5711650 |
| finite_rejection.accepted_auxiliary.gradient_teacher_tokens | 424294 |
| finite_rejection.accepted_auxiliary.physical_input_tokens | 5734400 |
| finite_rejection.accepted_auxiliary.projected_updates | 13 |
| finite_rejection.accepted_auxiliary.backtracked_updates | 13 |
| finite_rejection.accepted_auxiliary.accepted_updates | 2600 |
| finite_rejection.accepted_auxiliary.accepted_blocks | 130 |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-probe-launcher-20261006/launcher.json) ／ SHA256: `00193c9c919c4eb92960b2c20ee72eb43551707d23d7bc90e922adc5261c4114` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/block-Web-constraint-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-probe-launcher-20261006/result.json) ／ SHA256: `eff809e0401b442987ba7e6350cf6595e92ab9222536010b1396379128bb30c4` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/block-Web-constraint-train-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/block-Web-constraint-train-launcher-20261006/launcher.json) ／ SHA256: `51eab3b362c6bf12c3164af56246f2f1a544c8580d7c07492644e6ed3c810e84` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/block-Web-constraint-train-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/block-Web-constraint-train-launcher-20261006/result.json) ／ SHA256: `ce915ddb0b1518cfb431566d19dc260fc1479f92ccb7eb42d36aee082a152ffb` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_failure_analysis.json — fixed20_rejection_nonlinear_correction_residual_analyzed</summary>

[原記録](../../reports/phase6/block_Web_constraint_failure_analysis.json) ／ SHA256: `d540682d8e1a8d826e9550c536884abdd3c0c6e93654289d0819206b7ec476c3` ／ 4,578 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed20_rejection_nonlinear_correction_residual_analyzed" |
| accepted_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block-Web-constraint-20261006/block_Web_constraint/training/checkpoint-00323035.pt" |
| accepted_checkpoint.sha256 | "1db5c4a6505b706aa9497424d6d0309efd00587345c86d03b5a2e48e66bc6744" |
| accepted_source_updates | 2600 |
| accepted_source_CE_teachers | 84961352 |
| accepted_source_by_genre.web | 75000000 |
| accepted_source_by_genre.story | 5000000 |
| accepted_source_by_genre.ordinary_textbook | 4961352 |
| accepted_source_by_genre.conditional_textbook | 0 |
| accepted_auxiliary.forward_only_calls | 162 |
| accepted_auxiliary.gradient_calls | 13 |
| accepted_auxiliary.teacher_observations | 5711650 |
| accepted_auxiliary.gradient_teacher_tokens | 424294 |
| accepted_auxiliary.physical_input_tokens | 5734400 |
| accepted_auxiliary.projected_updates | 13 |
| accepted_auxiliary.backtracked_updates | 13 |
| accepted_auxiliary.accepted_updates | 2600 |
| accepted_auxiliary.accepted_blocks | 130 |
| rejected_source_gradient_teacher_exposures | 650524 |
| rejected_auxiliary.teacher_observations | 195828 |
| rejected_auxiliary.gradient_teacher_tokens | 32638 |
| rejected_auxiliary.physical_input_tokens | 196608 |
| accepted_source_plus_auxiliary_gradient_teachers | 85385646 |
| all_science_accepted_and_rejected_gradient_teacher_exposures | 86068808 |
| own_probe_source_CE_teachers | 5231748 |
| safe_boundary_body_NLL | 2.6070653200149536 |
| ceiling_body_NLL | 2.607075455188751 |
| proposed_body_NLL | 2.621283769607544 |
| linear_predicted_corrected_body_NLL | 2.607049642560482 |
| actual_corrected_body_NLL | 2.608679234981537 |
| intended_linear_NLL_reduction | 0.01423412704706184 |
| actual_NLL_reduction | 0.01260453462600708 |
| final_fixed_backtrack_body_NLL | 2.607168734073639 |
| interpretation | "Stored finite observations show the one-gradient correction undershot its linear target. All fixed corrected/backtracked proposals fail the actual limit; prior saved boundary remains feasible. This diagnoses this solver/trial set, not impossibility of every learning solution or model capacity/data quantity." |
| all_saved_boundary_losses_bounded | true |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| actual_science_GPU_seconds | 193.6470071610238 |
| own_probe_GPU_seconds | 33.67857302899938 |
| previous_related_GPU_seconds | 70.56110643898137 |
| new_GPU_seconds | 0 |
| new_learning_teacher_tokens | 0 |
| CPU_seconds | 0.31125860000611283 |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_failure_analysis_portable.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_failure_analysis_portable.json) ／ SHA256: `db9c28b8d898abf768f1398222f481a51d91c6bb16b6558b149da9ecf9c4924b` ／ 593 bytes

| 原キー | 保存値 |
|---|---|
| files.scripts/analyze_block_Web_rejection.py.bytes | 10823 |
| files.reports/phase6/block_Web_constraint_failure_analysis.json.bytes | 4578 |
| files.reports/phase6/block_Web_constraint_failure_analysis.json.sha256 | "d540682d8e1a8d826e9550c536884abdd3c0c6e93654289d0819206b7ec476c3" |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_launch.json — block_Web_constraint_launch</summary>

[原記録](../../reports/phase6/block_Web_constraint_launch.json) ／ SHA256: `7658babad6d18eff834c73144dc0a5262bea722c6845c2cd6361c17dc83cf995` ／ 2,593 bytes

| 原キー | 保存値 |
|---|---|
| status | "block_Web_constraint_launch" |
| CPU_preparation_seconds | 0.11339189999853261 |
| GPU_seconds | 101.82545424500131 |
| scientific_source_CE_teacher_tokens | 45777941 |
| previous_related_GPU_seconds | 70.56110643898137 |
| total_related_GPU_ceiling_seconds | 2400 |
| constraint_scope | "Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling." |
| does_not_satisfy_old_per_update_contract | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "setup" |
| actual_job.GPU_elapsed_seconds | 101.82545424500131 |
| actual_job.completed_updates | 1400 |
| actual_job.total_updates | 3068 |
| actual_job.actual_teachers | 45777941 |
| actual_job.loss | 2.5648303031921387 |
| actual_job.boundary_constraint.reference_body_NLL | 2.5812628269195557 |
| actual_job.boundary_constraint.ceiling_body_NLL | 2.607075455188751 |
| actual_job.boundary_constraint.proposed_body_NLL | 2.5727208852767944 |
| actual_job.boundary_constraint.accepted | true |
| actual_job.boundary_constraint.final_body_NLL | 2.5727208852767944 |
| actual_job.boundary_constraint.scope | "accepted_block_boundary_only" |
| actual_job.boundary_constraint.block_start_update | 321815 |
| actual_job.boundary_constraint.block_end_update | 321835 |
| actual_job.boundary_constraint.block_source_updates | 20 |
| actual_job.auxiliary.teacher_observations | 2284660 |
| actual_job.auxiliary.gradient_teacher_tokens | 0 |
| actual_job.auxiliary.physical_input_tokens | 2293760 |
| actual_job.auxiliary.projected_updates | 0 |
| actual_job.auxiliary.backtracked_updates | 0 |
| actual_job.auxiliary.accepted_updates | 1400 |
| actual_job.auxiliary.accepted_blocks | 70 |
| teacher_count_scope | "Observed accepted block updates at heartbeat, not final total." |
| verification_GPU_seconds | 33.67857302899938 |

</details>

<details>
<summary>reports/phase6/block_Web_constraint_launch_portable.json — None</summary>

[原記録](../../reports/phase6/block_Web_constraint_launch_portable.json) ／ SHA256: `5e7cff42cb7835bdfad399bc3c75b2eb6794686ec8ff7d88de948f902ca90990` ／ 1,896 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/block_Web_constraint_launch.json.bytes | 2593 |
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

</details>
