# 学習量・配合・学習順序 — 4/6

[分野一覧へ](03_learning.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/mature_base_condition_comparison_review.json — mature_parent_matched300M_all320_read_and_reviewed</summary>

[原記録](../../reports/phase6/mature_base_condition_comparison_review.json) ／ SHA256: `0697baeb505b3fe36aac77faa1caa4e2f5228f66f514ec8825ae39c38d848dbc` ／ 24,385 bytes

| 原キー | 保存値 |
|---|---|
| status | "mature_parent_matched300M_all320_read_and_reviewed" |
| summaries.parent10B.BPB | 0.9858907549313023 |
| summaries.parent10B.rates.eos | 0 |
| summaries.parent10B.rates.repetition | 53 |
| summaries.parent10B.rates.unicode_failure | 0 |
| summaries.parent10B.rates.role_leak | 0 |
| summaries.parent10B.rates.empty | 0 |
| summaries.parent10B.grammar2 | 48 |
| summaries.parent10B.relevance2 | 67 |
| summaries.parent10B.coherent | 0 |
| summaries.parent10B.appropriate | 0 |
| summaries.parent10B.notes_sha256 | "c7cbc4ac0ea99a4c34c524f032bddc91442627065f7de81fb15ea7d5bb74ce5f" |
| summaries.parent10B.additional_teacher_tokens | 0 |
| summaries.web.BPB | 1.0192702829723963 |
| summaries.web.rates.eos | 45 |
| summaries.web.rates.repetition | 30 |
| summaries.web.rates.unicode_failure | 0 |
| summaries.web.rates.role_leak | 0 |
| summaries.web.rates.empty | 0 |
| summaries.web.grammar2 | 49 |
| summaries.web.relevance2 | 70 |
| summaries.web.coherent | 9 |
| summaries.web.appropriate | 30 |
| summaries.web.notes_sha256 | "e3b99c1bd91e4b30ef6446881088284887f519566b9ff7e08e0657b5365cbddf" |
| summaries.web.additional_teacher_tokens | 100000000 |
| summaries.curriculum.BPB | 1.026258847271704 |
| summaries.curriculum.rates.eos | 47 |
| summaries.curriculum.rates.repetition | 24 |
| summaries.curriculum.rates.unicode_failure | 0 |
| summaries.curriculum.rates.role_leak | 0 |
| summaries.curriculum.rates.empty | 0 |
| summaries.curriculum.grammar2 | 65 |
| summaries.curriculum.relevance2 | 73 |
| summaries.curriculum.coherent | 11 |
| summaries.curriculum.appropriate | 34 |
| summaries.curriculum.notes_sha256 | "b310e22b3a692c76d208ec3df5f9d8aa0f002457d3ddac77e48029aebece6096" |
| summaries.curriculum.additional_teacher_tokens | 100000000 |
| summaries.relation.BPB | 1.026303661748729 |
| summaries.relation.rates.eos | 48 |
| summaries.relation.rates.repetition | 20 |
| summaries.relation.rates.unicode_failure | 0 |
| summaries.relation.rates.role_leak | 0 |
| summaries.relation.rates.empty | 0 |
| summaries.relation.grammar2 | 68 |
| summaries.relation.relevance2 | 73 |
| summaries.relation.coherent | 9 |
| summaries.relation.appropriate | 27 |
| summaries.relation.notes_sha256 | "4265234740cee04d0ca9d7482d090a2b3c8896128f32fe99223f3ce3d3f95c6b" |
| summaries.relation.additional_teacher_tokens | 100000000 |
| comparisons.curriculum-vs-web.checks.coherence_gain_at_least8 | false |
| comparisons.curriculum-vs-web.checks.paired_CI_lower_above0 | false |
| comparisons.curriculum-vs-web.checks.EOS_nonworsening | true |
| comparisons.curriculum-vs-web.checks.repetition_nonworsening | true |
| comparisons.curriculum-vs-web.checks.no_empty_role_unicode | true |
| comparisons.curriculum-vs-web.checks.BPB_gate | true |
| comparisons.curriculum-vs-web.checks.appropriate_completion_not_punctuation | true |
| comparisons.curriculum-vs-web.passed | false |
| comparisons.relation-vs-web.checks.coherence_gain_at_least8 | false |
| comparisons.relation-vs-web.checks.paired_CI_lower_above0 | false |
| comparisons.relation-vs-web.checks.EOS_nonworsening | true |
| comparisons.relation-vs-web.checks.repetition_nonworsening | true |
| comparisons.relation-vs-web.checks.no_empty_role_unicode | true |
| comparisons.relation-vs-web.checks.BPB_gate | true |
| comparisons.relation-vs-web.checks.appropriate_completion_not_punctuation | true |
| comparisons.relation-vs-web.passed | false |
| comparisons.relation-vs-curriculum.checks.coherence_gain_at_least8 | false |
| comparisons.relation-vs-curriculum.checks.paired_CI_lower_above0 | false |
| comparisons.relation-vs-curriculum.checks.EOS_nonworsening | true |
| comparisons.relation-vs-curriculum.checks.repetition_nonworsening | true |
| comparisons.relation-vs-curriculum.checks.no_empty_role_unicode | true |
| comparisons.relation-vs-curriculum.checks.BPB_gate | true |
| comparisons.relation-vs-curriculum.checks.appropriate_completion_not_punctuation | true |
| comparisons.relation-vs-curriculum.passed | false |
| absolute_dev_screen.web.grammar_at_least56 | false |
| absolute_dev_screen.web.coherence_at_least27 | false |
| absolute_dev_screen.web.appropriate_at_least27 | true |
| absolute_dev_screen.web.EOS_at_least37 | true |
| absolute_dev_screen.web.repetition_at_most18 | false |
| absolute_dev_screen.web.no_empty_role_unicode | true |
| absolute_dev_screen.curriculum.grammar_at_least56 | true |
| absolute_dev_screen.curriculum.coherence_at_least27 | false |
| absolute_dev_screen.curriculum.appropriate_at_least27 | true |
| absolute_dev_screen.curriculum.EOS_at_least37 | true |
| absolute_dev_screen.curriculum.repetition_at_most18 | false |
| absolute_dev_screen.curriculum.no_empty_role_unicode | true |
| absolute_dev_screen.relation.grammar_at_least56 | true |
| absolute_dev_screen.relation.coherence_at_least27 | false |
| absolute_dev_screen.relation.appropriate_at_least27 | true |
| absolute_dev_screen.relation.EOS_at_least37 | true |
| absolute_dev_screen.relation.repetition_at_most18 | false |
| absolute_dev_screen.relation.no_empty_role_unicode | true |
| original_Web.web.EOS_at_least8_more | true |
| original_Web.web.repetition_no_worse | true |
| original_Web.web.no_empty_role_unicode | true |
| original_Web.web.BPB_degradation_at_most1percent | false |
| original_Web.curriculum.EOS_at_least8_more | true |
| original_Web.curriculum.repetition_no_worse | true |
| original_Web.curriculum.no_empty_role_unicode | true |
| original_Web.curriculum.BPB_degradation_at_most1percent | false |
| original_Web.relation.EOS_at_least8_more | true |
| original_Web.relation.repetition_no_worse | true |
| original_Web.relation.no_empty_role_unicode | true |
| original_Web.relation.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.web | false |
| eligible_for_final_Base_validation.curriculum | false |
| eligible_for_final_Base_validation.relation | false |
| transfer_aggregates.bridge.web.sum_log_likelihood.all128.accuracy | 0.55078125 |
| transfer_aggregates.bridge.web.sum_log_likelihood.all128.both_correct | 21 |
| transfer_aggregates.bridge.web.sum_log_likelihood.lexical_holdout.accuracy | 0.546875 |
| transfer_aggregates.bridge.web.sum_log_likelihood.lexical_holdout.both_correct | 13 |
| transfer_aggregates.bridge.web.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| transfer_aggregates.bridge.web.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.all128.accuracy | 0.59765625 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.all128.both_correct | 28 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.all128.same_unique_candidate | 97 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.lexical_holdout.accuracy | 0.640625 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.lexical_holdout.both_correct | 20 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 42 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| transfer_aggregates.bridge.web.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 57 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.all128.accuracy | 0.5390625 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 109 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 52 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.structural_holdout.both_correct | 9 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 54 |
| transfer_aggregates.bridge.web.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 57 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.all128.accuracy | 0.44140625 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.all128.both_correct | 9 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.lexical_holdout.both_correct | 9 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.structural_holdout.accuracy | 0.3671875 |
| transfer_aggregates.bridge.curriculum.sum_log_likelihood.structural_holdout.both_correct | 0 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.all128.accuracy | 0.4609375 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.all128.both_correct | 17 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.all128.same_unique_candidate | 84 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.all128.aligned_context_margin_shift | 70 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.lexical_holdout.accuracy | 0.53125 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.lexical_holdout.both_correct | 14 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 40 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.structural_holdout.accuracy | 0.390625 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| transfer_aggregates.bridge.curriculum.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 27 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.all128.accuracy | 0.46875 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.all128.both_correct | 18 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.all128.same_unique_candidate | 84 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 75 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5546875 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 37 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.structural_holdout.accuracy | 0.3828125 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.structural_holdout.both_correct | 1 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer_aggregates.bridge.curriculum.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.all128.accuracy | 0.7421875 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.all128.both_correct | 76 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.lexical_holdout.both_correct | 57 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer_aggregates.bridge.relation.sum_log_likelihood.structural_holdout.both_correct | 19 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.all128.accuracy | 0.7421875 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.all128.both_correct | 76 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.all128.same_unique_candidate | 38 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.all128.aligned_context_margin_shift | 110 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.lexical_holdout.accuracy | 0.953125 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.lexical_holdout.both_correct | 58 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 6 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.structural_holdout.accuracy | 0.53125 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| transfer_aggregates.bridge.relation.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.all128.accuracy | 0.76953125 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.all128.both_correct | 83 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.all128.same_unique_candidate | 31 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 110 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.953125 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.lexical_holdout.both_correct | 58 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 6 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.structural_holdout.both_correct | 25 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 25 |
| transfer_aggregates.bridge.relation.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.all128.accuracy | 0.5703125 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.all128.both_correct | 23 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.lexical_holdout.both_correct | 15 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| transfer_aggregates.bridge.parent10B.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.all128.accuracy | 0.59765625 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.all128.both_correct | 26 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.all128.same_unique_candidate | 101 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6171875 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.lexical_holdout.both_correct | 16 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 48 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.structural_holdout.both_correct | 10 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 54 |
| transfer_aggregates.bridge.parent10B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 57 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.all128.accuracy | 0.59375 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.all128.both_correct | 25 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.all128.same_unique_candidate | 102 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.625 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 56 |
| transfer_aggregates.bridge.parent10B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.retention.web.sum_log_likelihood.all128.accuracy | 0.5546875 |
| transfer_aggregates.retention.web.sum_log_likelihood.all128.both_correct | 21 |
| transfer_aggregates.retention.web.sum_log_likelihood.lexical_holdout.accuracy | 0.59375 |
| transfer_aggregates.retention.web.sum_log_likelihood.lexical_holdout.both_correct | 16 |
| transfer_aggregates.retention.web.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.retention.web.sum_log_likelihood.structural_holdout.both_correct | 5 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.all128.accuracy | 0.5390625 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.all128.both_correct | 16 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.all128.same_unique_candidate | 106 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.all128.aligned_context_margin_shift | 71 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.lexical_holdout.both_correct | 12 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 48 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 35 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer_aggregates.retention.web.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.all128.accuracy | 0.49609375 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.all128.same_unique_candidate | 115 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 75 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.lexical_holdout.both_correct | 6 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 54 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 34 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.structural_holdout.both_correct | 0 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.retention.web.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 41 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.all128.accuracy | 0.75 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.all128.both_correct | 74 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer_aggregates.retention.curriculum.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.all128.accuracy | 0.765625 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.all128.both_correct | 77 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.all128.same_unique_candidate | 42 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.lexical_holdout.both_correct | 54 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| transfer_aggregates.retention.curriculum.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 41 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.all128.accuracy | 0.76171875 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.all128.both_correct | 77 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.all128.same_unique_candidate | 41 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.890625 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.lexical_holdout.both_correct | 53 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 8 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.structural_holdout.both_correct | 24 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.retention.curriculum.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 42 |
| transfer_aggregates.retention.relation.sum_log_likelihood.all128.accuracy | 0.7265625 |
| transfer_aggregates.retention.relation.sum_log_likelihood.all128.both_correct | 64 |
| transfer_aggregates.retention.relation.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| transfer_aggregates.retention.relation.sum_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer_aggregates.retention.relation.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer_aggregates.retention.relation.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.all128.accuracy | 0.73046875 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.all128.both_correct | 65 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.all128.same_unique_candidate | 57 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.lexical_holdout.both_correct | 47 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 14 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| transfer_aggregates.retention.relation.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.all128.both_correct | 61 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.all128.same_unique_candidate | 61 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 104 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| transfer_aggregates.retention.relation.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.all128.accuracy | 0.55859375 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.all128.both_correct | 22 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.lexical_holdout.accuracy | 0.59375 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.lexical_holdout.both_correct | 15 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer_aggregates.retention.parent10B.sum_log_likelihood.structural_holdout.both_correct | 7 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.all128.accuracy | 0.55859375 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.all128.both_correct | 20 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.all128.same_unique_candidate | 103 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 81 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6015625 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.lexical_holdout.both_correct | 15 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.structural_holdout.both_correct | 5 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 56 |
| transfer_aggregates.retention.parent10B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 42 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.all128.accuracy | 0.515625 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.all128.both_correct | 10 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 80 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.546875 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.lexical_holdout.both_correct | 8 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 54 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 41 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.484375 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer_aggregates.retention.parent10B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| new_scientific_teacher_tokens | 300000000 |
| verification_teacher_tokens | 3894822 |
| GPU_seconds | 780.3300344329909 |
| verification_GPU_seconds | 32.73914603400044 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "One learned seed; nonblind content judgment and repeatedly inspected fixeddev. Parent-history comparisons are descriptive; data/order differ. Shared-generator local probes do not prove natural-language quality. Original128 are retention. Independent learned seed/full dev/protected test/adoption remain pending." |

</details>

<details>
<summary>reports/phase6/mature_base_condition_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/mature_base_condition_evidence_manifest.json) ／ SHA256: `ef380fdeefd0453ed4d915d60474547aeadf7d0a4d8e2d32aaaf0aa63a9a34ea` ／ 101,858 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 34493393 |
| archive.bytes | 7343113 |
| checkpoint_tensors_included | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/mature_base_condition_pair_analysis.json — actual_mature_parent_matched300M_fixeddev96_pairs_reused</summary>

[原記録](../../reports/phase6/mature_base_condition_pair_analysis.json) ／ SHA256: `d9c3e0320c5bb6e87590afca799084d19c3735eb1770d58a2c021b5074e921cc` ／ 247,539 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_mature_parent_matched300M_fixeddev96_pairs_reused" |
| models.parent10B.causality.accuracy | 0.5 |
| models.parent10B.causality.both_correct | 0 |
| models.parent10B.causality.neither_correct | 0 |
| models.parent10B.comparison.accuracy | 0.46875 |
| models.parent10B.comparison.both_correct | 0 |
| models.parent10B.comparison.neither_correct | 1 |
| models.parent10B.coreference.accuracy | 0.53125 |
| models.parent10B.coreference.both_correct | 2 |
| models.parent10B.coreference.neither_correct | 1 |
| models.parent10B.negation.accuracy | 1.0 |
| models.parent10B.negation.both_correct | 16 |
| models.parent10B.negation.neither_correct | 0 |
| models.parent10B.quantity.accuracy | 0.625 |
| models.parent10B.quantity.both_correct | 5 |
| models.parent10B.quantity.neither_correct | 1 |
| models.parent10B.time.accuracy | 0.4375 |
| models.parent10B.time.both_correct | 0 |
| models.parent10B.time.neither_correct | 2 |
| models.web.causality.accuracy | 0.5625 |
| models.web.causality.both_correct | 2 |
| models.web.causality.neither_correct | 0 |
| models.web.comparison.accuracy | 0.53125 |
| models.web.comparison.both_correct | 1 |
| models.web.comparison.neither_correct | 0 |
| models.web.coreference.accuracy | 0.625 |
| models.web.coreference.both_correct | 5 |
| models.web.coreference.neither_correct | 1 |
| models.web.negation.accuracy | 0.71875 |
| models.web.negation.both_correct | 7 |
| models.web.negation.neither_correct | 0 |
| models.web.quantity.accuracy | 0.59375 |
| models.web.quantity.both_correct | 3 |
| models.web.quantity.neither_correct | 0 |
| models.web.time.accuracy | 0.46875 |
| models.web.time.both_correct | 0 |
| models.web.time.neither_correct | 1 |
| models.curriculum.causality.accuracy | 0.90625 |
| models.curriculum.causality.both_correct | 13 |
| models.curriculum.causality.neither_correct | 0 |
| models.curriculum.comparison.accuracy | 0.5 |
| models.curriculum.comparison.both_correct | 0 |
| models.curriculum.comparison.neither_correct | 0 |
| models.curriculum.coreference.accuracy | 0.40625 |
| models.curriculum.coreference.both_correct | 0 |
| models.curriculum.coreference.neither_correct | 3 |
| models.curriculum.negation.accuracy | 0.5 |
| models.curriculum.negation.both_correct | 0 |
| models.curriculum.negation.neither_correct | 0 |
| models.curriculum.quantity.accuracy | 0.59375 |
| models.curriculum.quantity.both_correct | 3 |
| models.curriculum.quantity.neither_correct | 0 |
| models.curriculum.time.accuracy | 0.46875 |
| models.curriculum.time.both_correct | 1 |
| models.curriculum.time.neither_correct | 2 |
| models.relation.causality.accuracy | 0.84375 |
| models.relation.causality.both_correct | 11 |
| models.relation.causality.neither_correct | 0 |
| models.relation.comparison.accuracy | 0.53125 |
| models.relation.comparison.both_correct | 1 |
| models.relation.comparison.neither_correct | 0 |
| models.relation.coreference.accuracy | 0.4375 |
| models.relation.coreference.both_correct | 0 |
| models.relation.coreference.neither_correct | 2 |
| models.relation.negation.accuracy | 1.0 |
| models.relation.negation.both_correct | 16 |
| models.relation.negation.neither_correct | 0 |
| models.relation.quantity.accuracy | 0.46875 |
| models.relation.quantity.both_correct | 0 |
| models.relation.quantity.neither_correct | 1 |
| models.relation.time.accuracy | 0.5625 |
| models.relation.time.both_correct | 2 |
| models.relation.time.neither_correct | 0 |
| references.parent10B.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| references.web.checkpoint_sha256 | "05dad9f101e11673c63e19dd3deeab9f8efad446a1247df5e45ef7d55fb78da9" |
| references.curriculum.checkpoint_sha256 | "4f5cb96c503fdc7c185025e0efbd7277faafb792a6a73d0b34255f246e12ddeb" |
| references.relation.checkpoint_sha256 | "cb77b164390d4d2520006ff49395d4f635a6a673ac3f562192fe2e13d4b07bbe" |
| CPU_seconds | 0.02975088098901324 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Repeatedly inspected fixeddev and one learned seed; descriptive context response, separate from fluent generation and local generator probes. Not an isolated parent-training-amount causal comparison." |

</details>

<details>
<summary>reports/phase6/mature_base_curriculum_notes.json — None</summary>

[原記録](../../reports/phase6/mature_base_curriculum_notes.json) ／ SHA256: `b310e22b3a692c76d208ec3df5f9d8aa0f002457d3ddac77e48029aebece6096` ／ 22,874 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/mature_base_distribution_diagnostic.json — actual_CPU_distribution_and_all320_source_span_diagnostic_complete</summary>

[原記録](../../reports/phase6/mature_base_distribution_diagnostic.json) ／ SHA256: `69f46f91a70cf54fcbeef0a8a4699d8b301d2f91405b286af4501eef8bc4e6c2` ／ 173,276 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU_distribution_and_all320_source_span_diagnostic_complete" |
| references.pairs.sha256 | "d9c3e0320c5bb6e87590afca799084d19c3735eb1770d58a2c021b5074e921cc" |
| references.pairs.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_condition_pair_analysis.json" |
| references.parent10B_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_parent10B_notes.json" |
| references.parent10B_notes.sha256 | "c7cbc4ac0ea99a4c34c524f032bddc91442627065f7de81fb15ea7d5bb74ce5f" |
| references.web_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_web_notes.json" |
| references.web_notes.sha256 | "e3b99c1bd91e4b30ef6446881088284887f519566b9ff7e08e0657b5365cbddf" |
| references.curriculum_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_curriculum_notes.json" |
| references.curriculum_notes.sha256 | "b310e22b3a692c76d208ec3df5f9d8aa0f002457d3ddac77e48029aebece6096" |
| references.relation_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_relation_notes.json" |
| references.relation_notes.sha256 | "4265234740cee04d0ca9d7482d090a2b3c8896128f32fe99223f3ce3d3f95c6b" |
| sampled_summaries.original_web.sampling | "uniform without replacement aligned token blocks" |
| sampled_summaries.original_web.source | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| sampled_summaries.original_web.blocks | 256 |
| sampled_summaries.original_web.physical_inputs | 262144 |
| sampled_summaries.original_web.teachers | 261571 |
| sampled_summaries.original_web.EOS | 573 |
| sampled_summaries.original_web.masked_BOS | 573 |
| sampled_summaries.original_web.body_tokens | 260998 |
| sampled_summaries.original_web.body_bytes | 1028017 |
| sampled_summaries.original_web.EOS_fraction_of_teachers | 0.002190609815308272 |
| sampled_summaries.original_web.sampled_inputs_per_EOS | 457.4938917975567 |
| sampled_summaries.original_web.between_EOS_gap_quantiles | [90.0, 267.0, 365.0, 486.0, 843.0] |
| sampled_summaries.original_web.between_EOS_gap_count | 317 |
| sampled_summaries.original_web.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| sampled_summaries.web.sampling | "fresh deterministic per-document source shuffle" |
| sampled_summaries.web.source | "web" |
| sampled_summaries.web.blocks | 256 |
| sampled_summaries.web.physical_inputs | 262144 |
| sampled_summaries.web.teachers | 259832 |
| sampled_summaries.web.EOS | 2312 |
| sampled_summaries.web.masked_BOS | 2312 |
| sampled_summaries.web.body_tokens | 257520 |
| sampled_summaries.web.body_bytes | 1037160 |
| sampled_summaries.web.EOS_fraction_of_teachers | 0.008898057206194772 |
| sampled_summaries.web.sampled_inputs_per_EOS | 113.3840830449827 |
| sampled_summaries.web.between_EOS_gap_quantiles | [66.0, 75.0, 89.0, 118.0, 654.0] |
| sampled_summaries.web.between_EOS_gap_count | 2056 |
| sampled_summaries.web.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| sampled_summaries.story.sampling | "fresh deterministic per-document source shuffle" |
| sampled_summaries.story.source | "story" |
| sampled_summaries.story.blocks | 64 |
| sampled_summaries.story.physical_inputs | 65536 |
| sampled_summaries.story.teachers | 65036 |
| sampled_summaries.story.EOS | 500 |
| sampled_summaries.story.masked_BOS | 500 |
| sampled_summaries.story.body_tokens | 64536 |
| sampled_summaries.story.body_bytes | 266865 |
| sampled_summaries.story.EOS_fraction_of_teachers | 0.007688049695553232 |
| sampled_summaries.story.sampled_inputs_per_EOS | 131.072 |
| sampled_summaries.story.between_EOS_gap_quantiles | [46.0, 74.0, 94.0, 121.0, 503.0] |
| sampled_summaries.story.between_EOS_gap_count | 436 |
| sampled_summaries.story.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| sampled_summaries.textbook.sampling | "fresh deterministic per-document source shuffle" |
| sampled_summaries.textbook.source | "textbook" |
| sampled_summaries.textbook.blocks | 64 |
| sampled_summaries.textbook.physical_inputs | 65536 |
| sampled_summaries.textbook.teachers | 65074 |
| sampled_summaries.textbook.EOS | 462 |
| sampled_summaries.textbook.masked_BOS | 462 |
| sampled_summaries.textbook.body_tokens | 64612 |
| sampled_summaries.textbook.body_bytes | 278098 |
| sampled_summaries.textbook.EOS_fraction_of_teachers | 0.007099609675139072 |
| sampled_summaries.textbook.sampled_inputs_per_EOS | 141.85281385281385 |
| sampled_summaries.textbook.between_EOS_gap_quantiles | [67.0, 105.25, 128.0, 154.0, 307.0] |
| sampled_summaries.textbook.between_EOS_gap_count | 398 |
| sampled_summaries.textbook.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| sampled_summaries.curriculum.sampling | "fresh deterministic per-document source shuffle" |
| sampled_summaries.curriculum.source | "curriculum" |
| sampled_summaries.curriculum.blocks | 64 |
| sampled_summaries.curriculum.physical_inputs | 65536 |
| sampled_summaries.curriculum.teachers | 63983 |
| sampled_summaries.curriculum.EOS | 1553 |
| sampled_summaries.curriculum.masked_BOS | 1553 |
| sampled_summaries.curriculum.body_tokens | 62430 |
| sampled_summaries.curriculum.body_bytes | 243894 |
| sampled_summaries.curriculum.EOS_fraction_of_teachers | 0.024272072269196504 |
| sampled_summaries.curriculum.sampled_inputs_per_EOS | 42.19961365099807 |
| sampled_summaries.curriculum.between_EOS_gap_quantiles | [23.0, 34.0, 38.0, 47.0, 76.0] |
| sampled_summaries.curriculum.between_EOS_gap_count | 1489 |
| sampled_summaries.curriculum.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| sampled_summaries.relation.sampling | "fresh deterministic per-document source shuffle" |
| sampled_summaries.relation.source | "relation" |
| sampled_summaries.relation.blocks | 64 |
| sampled_summaries.relation.physical_inputs | 65536 |
| sampled_summaries.relation.teachers | 64037 |
| sampled_summaries.relation.EOS | 1499 |
| sampled_summaries.relation.masked_BOS | 1499 |
| sampled_summaries.relation.body_tokens | 62538 |
| sampled_summaries.relation.body_bytes | 242821 |
| sampled_summaries.relation.EOS_fraction_of_teachers | 0.023408342052251042 |
| sampled_summaries.relation.sampled_inputs_per_EOS | 43.71981320880587 |
| sampled_summaries.relation.between_EOS_gap_quantiles | [23.0, 33.0, 38.0, 52.0, 76.0] |
| sampled_summaries.relation.between_EOS_gap_count | 1435 |
| sampled_summaries.relation.limitation | "EOS gaps wholly within sampled blocks only; long documents are censored. These are sampled teacher/byte statistics, not whole-corpus unique volume or an unbiased document-length estimate." |
| source_span_aggregates.parent10B.curriculum.outputs_with_24token_span | 0 |
| source_span_aggregates.parent10B.curriculum.coherent2_with_span | 0 |
| source_span_aggregates.parent10B.curriculum.longest_tokens | 0 |
| source_span_aggregates.parent10B.relation.outputs_with_24token_span | 0 |
| source_span_aggregates.parent10B.relation.coherent2_with_span | 0 |
| source_span_aggregates.parent10B.relation.longest_tokens | 0 |
| source_span_aggregates.web.curriculum.outputs_with_24token_span | 0 |
| source_span_aggregates.web.curriculum.coherent2_with_span | 0 |
| source_span_aggregates.web.curriculum.longest_tokens | 0 |
| source_span_aggregates.web.relation.outputs_with_24token_span | 0 |
| source_span_aggregates.web.relation.coherent2_with_span | 0 |
| source_span_aggregates.web.relation.longest_tokens | 0 |
| source_span_aggregates.curriculum.curriculum.outputs_with_24token_span | 2 |
| source_span_aggregates.curriculum.curriculum.coherent2_with_span | 2 |
| source_span_aggregates.curriculum.curriculum.longest_tokens | 52 |
| source_span_aggregates.curriculum.relation.outputs_with_24token_span | 2 |
| source_span_aggregates.curriculum.relation.coherent2_with_span | 2 |
| source_span_aggregates.curriculum.relation.longest_tokens | 52 |
| source_span_aggregates.relation.curriculum.outputs_with_24token_span | 2 |
| source_span_aggregates.relation.curriculum.coherent2_with_span | 2 |
| source_span_aggregates.relation.curriculum.longest_tokens | 42 |
| source_span_aggregates.relation.relation.outputs_with_24token_span | 2 |
| source_span_aggregates.relation.relation.coherent2_with_span | 2 |
| source_span_aggregates.relation.relation.longest_tokens | 42 |
| sampled_targets_sha256 | "1423071c75d4684170f7720b84b975711f564f27fd73cfdb66bf7b93ae6b43fd" |
| CPU_seconds | 3.4061204390018247 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Posthoc train distribution diagnostic, different sampling units, fixed small sample. EOS gaps are censored at block edges. Shared exact body spans do not prove whole-document copying, leakage or causal interference. No new forward pass or quality evaluation; existing nonblind notes reused." |

</details>

<details>
<summary>reports/phase6/mature_base_distribution_diagnostic_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/mature_base_distribution_diagnostic_evidence_manifest.json) ／ SHA256: `0bfa9014e9dbb23daa80626406d12ca46f9a7707668f9864141100194c327b65` ／ 1,915 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 864957 |
| archive.bytes | 68652 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/mature_base_distribution_diagnostic_proposal.json — defined_posthoc_CPU_distribution_diagnostic_not_implemented_not_started</summary>

[原記録](../../reports/phase6/mature_base_distribution_diagnostic_proposal.json) ／ SHA256: `3ef344f05ae64e6bb15e244f7166560e3f6631b9227d4a47f5408cb9557bd121` ／ 2,851 bytes

| 原キー | 保存値 |
|---|---|
| GPU_limit_seconds | 0 |
| pair_evidence.sha256 | "d9c3e0320c5bb6e87590afca799084d19c3735eb1770d58a2c021b5074e921cc" |
| pair_evidence.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/mature_base_condition_pair_analysis.json" |
| hypothesis | "The selected whole-unit source distribution and its EOS/length statistics differ from the parent Web training stream. Conditional source exposure and shared boilerplate may favor recognizable source templates over context-sensitive continuation. These are distribution/interference hypotheses, not proven unique causes or capacity limits." |
| protected_test_used | false |
| Base_adopted | false |
| completion | "One raw SHA-bound CPU report linking original vs selected material, source span counts, all source/case/result identities, actual elapsed time and limitations, no weights/optimizer change. Decide one retention/fluency comparison before GPU; do not automatically train or relax criteria." |
| status | "defined_posthoc_CPU_distribution_diagnostic_not_implemented_not_started" |
| sample_recipe | "Seed2026100631. At most256 context1024 blocks from original parent Web token arrays and selected cached Web GenreStream, plus64 blocks per story/ordinary/curriculum/relation stream. Separate uniform sample and fresh deterministic fork; report sample teacher/EOS/body/bytes counts, not whole-corpus volume. Exact frozen parent material/manifest only; compact cache reuse; no13GB index parse/global dedup." |
| CPU_limit_seconds | 30 |
| new_learning_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/mature_base_parent10B_notes.json — None</summary>

[原記録](../../reports/phase6/mature_base_parent10B_notes.json) ／ SHA256: `c7cbc4ac0ea99a4c34c524f032bddc91442627065f7de81fb15ea7d5bb74ce5f` ／ 21,867 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/mature_base_relation_notes.json — None</summary>

[原記録](../../reports/phase6/mature_base_relation_notes.json) ／ SHA256: `4265234740cee04d0ca9d7482d090a2b3c8896128f32fe99223f3ce3d3f95c6b` ／ 23,954 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/mature_base_web_notes.json — None</summary>

[原記録](../../reports/phase6/mature_base_web_notes.json) ／ SHA256: `e3b99c1bd91e4b30ef6446881088284887f519566b9ff7e08e0657b5365cbddf` ／ 21,552 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion." |

</details>

<details>
<summary>reports/phase6/natural_learning_annotations.json — None</summary>

[原記録](../../reports/phase6/natural_learning_annotations.json) ／ SHA256: `4de71f307b555edc1bf5bc81d33f3759ce62cd31965e082d29d43b6f10a0e3e5` ／ 35,948 bytes

| 原キー | 保存値 |
|---|---|
| review_scope | "All160 actual raw continuations read individually; grammar/relevance/coherence0-2, actual meaningful EOS completion0-1; no scoring by EOS alone" |

</details>

<details>
<summary>reports/phase6/natural_learning_completion.json — completed_requested_four_stage_branch</summary>

[原記録](../../reports/phase6/natural_learning_completion.json) ／ SHA256: `fe2f77a6e5f4399d0229001de51807f56d37efa60b671b27fa0a7dea5615525c` ／ 56,403 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_requested_four_stage_branch" |
| reports.diagnostic.status | "passed_learning_evidence" |
| reports.diagnostic.summaries.adam-inherit.teacher_tokens | 8000000 |
| reports.diagnostic.summaries.adam-inherit.physical_input | 19496960 |
| reports.diagnostic.summaries.adam-inherit.updates | 595 |
| reports.diagnostic.summaries.adam-inherit.train.documents | 64 |
| reports.diagnostic.summaries.adam-inherit.train.teacher_targets | 2236 |
| reports.diagnostic.summaries.adam-inherit.train.teacher_correct | 2236 |
| reports.diagnostic.summaries.adam-inherit.train.teacher_accuracy | 1.0 |
| reports.diagnostic.summaries.adam-inherit.train.eos | 64 |
| reports.diagnostic.summaries.adam-inherit.train.appropriate_gold_eos | 64 |
| reports.diagnostic.summaries.adam-inherit.train.appropriate_fraction | 1.0 |
| reports.diagnostic.summaries.adam-inherit.dev.documents | 128 |
| reports.diagnostic.summaries.adam-inherit.dev.teacher_targets | 4472 |
| reports.diagnostic.summaries.adam-inherit.dev.teacher_correct | 4471 |
| reports.diagnostic.summaries.adam-inherit.dev.teacher_accuracy | 0.9997763864042933 |
| reports.diagnostic.summaries.adam-inherit.dev.eos | 128 |
| reports.diagnostic.summaries.adam-inherit.dev.appropriate_gold_eos | 127 |
| reports.diagnostic.summaries.adam-inherit.dev.appropriate_fraction | 0.9921875 |
| reports.diagnostic.summaries.adam-inherit.diagnostic_pass | true |
| reports.diagnostic.summaries.adam-inherit.training_seconds | 73.92264497099677 |
| reports.diagnostic.summaries.adam-inherit.peak_allocated_bytes | 10076272128 |
| reports.diagnostic.summaries.adam-inherit.EOS_teachers.web | 0 |
| reports.diagnostic.summaries.adam-inherit.EOS_teachers.short | 152290 |
| reports.diagnostic.summaries.adam-fresh.teacher_tokens | 8000000 |
| reports.diagnostic.summaries.adam-fresh.physical_input | 19496960 |
| reports.diagnostic.summaries.adam-fresh.updates | 595 |
| reports.diagnostic.summaries.adam-fresh.train.documents | 64 |
| reports.diagnostic.summaries.adam-fresh.train.teacher_targets | 2236 |
| reports.diagnostic.summaries.adam-fresh.train.teacher_correct | 2236 |
| reports.diagnostic.summaries.adam-fresh.train.teacher_accuracy | 1.0 |
| reports.diagnostic.summaries.adam-fresh.train.eos | 64 |
| reports.diagnostic.summaries.adam-fresh.train.appropriate_gold_eos | 64 |
| reports.diagnostic.summaries.adam-fresh.train.appropriate_fraction | 1.0 |
| reports.diagnostic.summaries.adam-fresh.dev.documents | 128 |
| reports.diagnostic.summaries.adam-fresh.dev.teacher_targets | 4472 |
| reports.diagnostic.summaries.adam-fresh.dev.teacher_correct | 4472 |
| reports.diagnostic.summaries.adam-fresh.dev.teacher_accuracy | 1.0 |
| reports.diagnostic.summaries.adam-fresh.dev.eos | 128 |
| reports.diagnostic.summaries.adam-fresh.dev.appropriate_gold_eos | 128 |
| reports.diagnostic.summaries.adam-fresh.dev.appropriate_fraction | 1.0 |
| reports.diagnostic.summaries.adam-fresh.diagnostic_pass | true |
| reports.diagnostic.summaries.adam-fresh.training_seconds | 74.37676723299955 |
| reports.diagnostic.summaries.adam-fresh.peak_allocated_bytes | 10076272128 |
| reports.diagnostic.summaries.adam-fresh.EOS_teachers.web | 0 |
| reports.diagnostic.summaries.adam-fresh.EOS_teachers.short | 152290 |
| reports.diagnostic.verification_teacher_tokens | 215168 |
| reports.diagnostic.scientific_teacher_tokens | 16000000 |
| reports.diagnostic.gpu_seconds | 186.757103217009 |
| reports.diagnostic.protected_test_used | false |
| reports.diagnostic.checked_at | "2026-10-05T13:16:03.136291Z" |
| reports.compare.status | "passed_learning_content_evidence" |
| reports.compare.summaries.mixed-control.teacher_tokens | 25000000 |
| reports.compare.summaries.mixed-control.physical_input | 25165824 |
| reports.compare.summaries.mixed-control.updates | 768 |
| reports.compare.summaries.mixed-control.train.documents | 64 |
| reports.compare.summaries.mixed-control.train.teacher_targets | 2236 |
| reports.compare.summaries.mixed-control.train.teacher_correct | 874 |
| reports.compare.summaries.mixed-control.train.teacher_accuracy | 0.39087656529516995 |
| reports.compare.summaries.mixed-control.train.eos | 30 |
| reports.compare.summaries.mixed-control.train.appropriate_gold_eos | 0 |
| reports.compare.summaries.mixed-control.train.appropriate_fraction | 0.0 |
| reports.compare.summaries.mixed-control.dev.documents | 128 |
| reports.compare.summaries.mixed-control.dev.teacher_targets | 4472 |
| reports.compare.summaries.mixed-control.dev.teacher_correct | 1815 |
| reports.compare.summaries.mixed-control.dev.teacher_accuracy | 0.4058586762075134 |
| reports.compare.summaries.mixed-control.dev.eos | 36 |
| reports.compare.summaries.mixed-control.dev.appropriate_gold_eos | 0 |
| reports.compare.summaries.mixed-control.dev.appropriate_fraction | 0.0 |
| reports.compare.summaries.mixed-control.diagnostic_pass | false |
| reports.compare.summaries.mixed-control.training_seconds | 51.36899270499998 |
| reports.compare.summaries.mixed-control.peak_allocated_bytes | 6149073408 |
| reports.compare.summaries.mixed-control.EOS_teachers.web | 42190 |
| reports.compare.summaries.mixed-control.EOS_teachers.short | 92079 |
| reports.compare.summaries.mixed-control.BPB | 0.9821879082414368 |
| reports.compare.summaries.mixed-control.rates.eos | 10 |
| reports.compare.summaries.mixed-control.rates.repetition | 48 |
| reports.compare.summaries.mixed-control.rates.unicode_failure | 1 |
| reports.compare.summaries.mixed-control.rates.role_leak | 0 |
| reports.compare.summaries.mixed-control.rates.empty | 0 |
| reports.compare.summaries.mixed-control.grammar_score2 | 10 |
| reports.compare.summaries.mixed-control.relevance_score2 | 38 |
| reports.compare.summaries.mixed-control.coherent | 0 |
| reports.compare.summaries.mixed-control.appropriate | 0 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.point | 0.6145833333333334 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.units | 96 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.examples | 192 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.primary.hard_accuracy | 0.6145833333333334 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.point | 0.5989583333333334 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.units | 96 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.examples | 192 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.count | 192 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.macro_f1 | 0.5988603988603989 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.mcc | 0.19801337650222875 |
| reports.compare.summaries.mixed-control.Japanese.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.point | 0.5 |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.units | 96 |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.examples | 192 |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.unigram_control.hard_accuracy | 0.5 |
| reports.compare.summaries.mixed-control.Japanese.semantics.train_majority_accuracy | 0.5 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.negation.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.negation.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.quantity.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.quantity.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.time.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.time.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.comparison.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.comparison.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.coreference.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.coreference.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.causality.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.causality.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.point | 0.7734138972809668 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8187311178247734] |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.units | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.examples | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.primary.hard_accuracy | 0.7734138972809668 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.point | 0.7250755287009063 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.ci95 | [0.676737160120846, 0.7734138972809668] |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.units | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.examples | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.count | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.hard_accuracy | 0.7250755287009063 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.macro_f1 | 0.4203152364273205 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.mcc | 0.0 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.units | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.examples | 331 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.train_majority_accuracy | null |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.island effects.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.island effects.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.binding.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.binding.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.argument structure.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.argument structure.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.ellipsis.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.ellipsis.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.filler-gap.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.filler-gap.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.morphology.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.morphology.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.nominal structure.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.nominal structure.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.quantifiers.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.quantifiers.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.control/raising.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.control/raising.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-control.Japanese.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.point | 0.30384271671134944 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.ci95 | [0.2779267202859696, 0.32978105451295786] |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.units | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.primary.hard_accuracy | 0.30384271671134944 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.33603663985701504] |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.units | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.count | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.macro_f1 | 0.3084781711234873 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.mcc | 0.13698891971743338 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.units | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.train_majority_accuracy | 0.21179624664879357 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.categories.commonsense.seed | 42 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.categories.commonsense.repetitions | 2000 |
| reports.compare.summaries.mixed-control.Japanese.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-control.Japanese.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-control.Japanese.semantic_both_contexts.correct | 25 |
| reports.compare.summaries.mixed-natural.teacher_tokens | 25000000 |
| reports.compare.summaries.mixed-natural.physical_input | 25165824 |
| reports.compare.summaries.mixed-natural.updates | 768 |
| reports.compare.summaries.mixed-natural.train.documents | 64 |
| reports.compare.summaries.mixed-natural.train.teacher_targets | 2236 |
| reports.compare.summaries.mixed-natural.train.teacher_correct | 2236 |
| reports.compare.summaries.mixed-natural.train.teacher_accuracy | 1.0 |
| reports.compare.summaries.mixed-natural.train.eos | 64 |
| reports.compare.summaries.mixed-natural.train.appropriate_gold_eos | 64 |
| reports.compare.summaries.mixed-natural.train.appropriate_fraction | 1.0 |
| reports.compare.summaries.mixed-natural.dev.documents | 128 |
| reports.compare.summaries.mixed-natural.dev.teacher_targets | 4472 |
| reports.compare.summaries.mixed-natural.dev.teacher_correct | 4472 |
| reports.compare.summaries.mixed-natural.dev.teacher_accuracy | 1.0 |
| reports.compare.summaries.mixed-natural.dev.eos | 128 |
| reports.compare.summaries.mixed-natural.dev.appropriate_gold_eos | 128 |
| reports.compare.summaries.mixed-natural.dev.appropriate_fraction | 1.0 |
| reports.compare.summaries.mixed-natural.diagnostic_pass | true |
| reports.compare.summaries.mixed-natural.training_seconds | 39.08503212999494 |
| reports.compare.summaries.mixed-natural.peak_allocated_bytes | 6149073408 |
| reports.compare.summaries.mixed-natural.EOS_teachers.web | 42190 |
| reports.compare.summaries.mixed-natural.EOS_teachers.short | 96513 |
| reports.compare.summaries.mixed-natural.BPB | 0.983213353200905 |
| reports.compare.summaries.mixed-natural.rates.eos | 26 |
| reports.compare.summaries.mixed-natural.rates.repetition | 30 |
| reports.compare.summaries.mixed-natural.rates.unicode_failure | 0 |
| reports.compare.summaries.mixed-natural.rates.role_leak | 0 |
| reports.compare.summaries.mixed-natural.rates.empty | 0 |
| reports.compare.summaries.mixed-natural.grammar_score2 | 25 |
| reports.compare.summaries.mixed-natural.relevance_score2 | 44 |
| reports.compare.summaries.mixed-natural.coherent | 7 |
| reports.compare.summaries.mixed-natural.appropriate | 8 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.point | 0.5989583333333334 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.ci95 | [0.546875, 0.6458333333333334] |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.units | 96 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.examples | 192 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.primary.hard_accuracy | 0.5989583333333334 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.point | 0.6041666666666666 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.units | 96 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.examples | 192 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.count | 192 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.hard_accuracy | 0.6041666666666666 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.macro_f1 | 0.6041237113402061 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.mcc | 0.20837855928270652 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.point | 0.5 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.units | 96 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.examples | 192 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.unigram_control.hard_accuracy | 0.5 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.train_majority_accuracy | 0.5 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.negation.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.negation.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.quantity.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.quantity.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.time.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.time.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.comparison.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.comparison.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.coreference.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.coreference.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.causality.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.causality.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.point | 0.7643504531722054 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.ci95 | [0.7219788519637462, 0.8096676737160121] |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.units | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.examples | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.primary.hard_accuracy | 0.7643504531722054 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.ci95 | [0.676737160120846, 0.7765105740181264] |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.units | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.examples | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.count | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.mcc | 0.0 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.units | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.examples | 331 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.train_majority_accuracy | null |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.island effects.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.island effects.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.binding.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.binding.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.argument structure.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.argument structure.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.morphology.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.morphology.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.control/raising.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.control/raising.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-natural.Japanese.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.point | 0.2957998212689902 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.ci95 | [0.2707774798927614, 0.32171581769436997] |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.units | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.primary.hard_accuracy | 0.2957998212689902 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.point | 0.30116175156389635 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.ci95 | [0.2752457551385165, 0.32797140303842715] |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.units | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.count | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.hard_accuracy | 0.30116175156389635 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.macro_f1 | 0.30049807915888843 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.mcc | 0.12688841102912485 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.units | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.examples | 1119 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.train_majority_accuracy | 0.21179624664879357 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.categories.commonsense.seed | 42 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.categories.commonsense.repetitions | 2000 |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.summaries.mixed-natural.Japanese.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| reports.compare.summaries.mixed-natural.Japanese.semantic_both_contexts.correct | 24 |
| reports.compare.quality.checks.coherence_gain_at_least8 | false |
| reports.compare.quality.checks.paired_CI_lower_above0 | true |
| reports.compare.quality.checks.EOS_nonworsening | true |
| reports.compare.quality.checks.repetition_nonworsening | true |
| reports.compare.quality.checks.no_empty_role_unicode | true |
| reports.compare.quality.checks.BPB_gate | true |
| reports.compare.quality.checks.appropriate_completion_not_punctuation | true |
| reports.compare.quality.passed | false |
| reports.compare.practical.coherence_at_least27 | false |
| reports.compare.practical.appropriate_at_least27 | false |
| reports.compare.practical.EOS_at_least37 | false |
| reports.compare.practical.repetition_at_most18 | false |
| reports.compare.original_Web_gates.EOS_at_least8_more | true |
| reports.compare.original_Web_gates.repetition_no_worse | true |
| reports.compare.original_Web_gates.no_empty_role_unicode | true |
| reports.compare.original_Web_gates.BPB_degradation_at_most1percent | false |
| reports.compare.eligible_for_expansion | false |
| reports.compare.scientific_teacher_tokens | 50000000 |
| reports.compare.gpu_seconds | 297.5269214879954 |
| reports.compare.paired_Japanese_differences.semantics.point | -0.015625 |
| reports.compare.paired_Japanese_differences.semantics.ci95 | [-0.0625, 0.03125] |
| reports.compare.paired_Japanese_differences.semantics.units | 96 |
| reports.compare.paired_Japanese_differences.semantics.examples | 192 |
| reports.compare.paired_Japanese_differences.semantics.unit | "family/prompt" |
| reports.compare.paired_Japanese_differences.semantics.seed | 42 |
| reports.compare.paired_Japanese_differences.semantics.repetitions | 2000 |
| reports.compare.paired_Japanese_differences.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.paired_Japanese_differences.jblimp.point | -0.00906344410876133 |
| reports.compare.paired_Japanese_differences.jblimp.ci95 | [-0.03927492447129909, 0.01812688821752266] |
| reports.compare.paired_Japanese_differences.jblimp.units | 331 |
| reports.compare.paired_Japanese_differences.jblimp.examples | 331 |
| reports.compare.paired_Japanese_differences.jblimp.unit | "family/prompt" |
| reports.compare.paired_Japanese_differences.jblimp.seed | 42 |
| reports.compare.paired_Japanese_differences.jblimp.repetitions | 2000 |
| reports.compare.paired_Japanese_differences.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.paired_Japanese_differences.jcqa.point | -0.00804289544235925 |
| reports.compare.paired_Japanese_differences.jcqa.ci95 | [-0.01876675603217158, 0.002680965147453083] |
| reports.compare.paired_Japanese_differences.jcqa.units | 1119 |
| reports.compare.paired_Japanese_differences.jcqa.examples | 1119 |
| reports.compare.paired_Japanese_differences.jcqa.unit | "family/prompt" |
| reports.compare.paired_Japanese_differences.jcqa.seed | 42 |
| reports.compare.paired_Japanese_differences.jcqa.repetitions | 2000 |
| reports.compare.paired_Japanese_differences.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| reports.compare.protected_test_used | false |
| reports.compare.checked_at | "2026-10-05T13:16:04.781531Z" |
| new_scientific_teacher_tokens | 66000000 |
| verification_teacher_tokens | 215168 |
| gpu_seconds | 484.2840247050044 |
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
| cpu_tests | 4 |
| checkpoints_and_raw_retained | true |
| protected_test_used | false |
| precision_failures_result72_unchanged | true |

</details>

<details>
<summary>reports/phase6/natural_learning_diagnostic_review.json — passed_learning_evidence</summary>

[原記録](../../reports/phase6/natural_learning_diagnostic_review.json) ／ SHA256: `c17879bb34a26dcedb8c78f1e14e8c2e703c106e2b60d1788a7c9b6d0053d981` ／ 2,830 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_learning_evidence" |
| summaries.adam-inherit.teacher_tokens | 8000000 |
| summaries.adam-inherit.physical_input | 19496960 |
| summaries.adam-inherit.updates | 595 |
| summaries.adam-inherit.train.documents | 64 |
| summaries.adam-inherit.train.teacher_targets | 2236 |
| summaries.adam-inherit.train.teacher_correct | 2236 |
| summaries.adam-inherit.train.teacher_accuracy | 1.0 |
| summaries.adam-inherit.train.eos | 64 |
| summaries.adam-inherit.train.appropriate_gold_eos | 64 |
| summaries.adam-inherit.train.appropriate_fraction | 1.0 |
| summaries.adam-inherit.dev.documents | 128 |
| summaries.adam-inherit.dev.teacher_targets | 4472 |
| summaries.adam-inherit.dev.teacher_correct | 4471 |
| summaries.adam-inherit.dev.teacher_accuracy | 0.9997763864042933 |
| summaries.adam-inherit.dev.eos | 128 |
| summaries.adam-inherit.dev.appropriate_gold_eos | 127 |
| summaries.adam-inherit.dev.appropriate_fraction | 0.9921875 |
| summaries.adam-inherit.diagnostic_pass | true |
| summaries.adam-inherit.training_seconds | 73.92264497099677 |
| summaries.adam-inherit.peak_allocated_bytes | 10076272128 |
| summaries.adam-inherit.EOS_teachers.web | 0 |
| summaries.adam-inherit.EOS_teachers.short | 152290 |
| summaries.adam-fresh.teacher_tokens | 8000000 |
| summaries.adam-fresh.physical_input | 19496960 |
| summaries.adam-fresh.updates | 595 |
| summaries.adam-fresh.train.documents | 64 |
| summaries.adam-fresh.train.teacher_targets | 2236 |
| summaries.adam-fresh.train.teacher_correct | 2236 |
| summaries.adam-fresh.train.teacher_accuracy | 1.0 |
| summaries.adam-fresh.train.eos | 64 |
| summaries.adam-fresh.train.appropriate_gold_eos | 64 |
| summaries.adam-fresh.train.appropriate_fraction | 1.0 |
| summaries.adam-fresh.dev.documents | 128 |
| summaries.adam-fresh.dev.teacher_targets | 4472 |
| summaries.adam-fresh.dev.teacher_correct | 4472 |
| summaries.adam-fresh.dev.teacher_accuracy | 1.0 |
| summaries.adam-fresh.dev.eos | 128 |
| summaries.adam-fresh.dev.appropriate_gold_eos | 128 |
| summaries.adam-fresh.dev.appropriate_fraction | 1.0 |
| summaries.adam-fresh.diagnostic_pass | true |
| summaries.adam-fresh.training_seconds | 74.37676723299955 |
| summaries.adam-fresh.peak_allocated_bytes | 10076272128 |
| summaries.adam-fresh.EOS_teachers.web | 0 |
| summaries.adam-fresh.EOS_teachers.short | 152290 |
| verification_teacher_tokens | 215168 |
| scientific_teacher_tokens | 16000000 |
| gpu_seconds | 186.757103217009 |
| protected_test_used | false |
| checked_at | "2026-10-05T13:16:03.136291Z" |

</details>

<details>
<summary>reports/phase6/natural_learning_judgment.json — candidate_rejected_expansion_not_launched</summary>

[原記録](../../reports/phase6/natural_learning_judgment.json) ／ SHA256: `52de986fb754ce77d465fc92719ea2a73f25631a497ec99a763606d7fbf16f4a` ／ 815 bytes

| 原キー | 保存値 |
|---|---|
| completed_scope | "Four-stage contract through fixed quality rejection branch" |
| reason | "Coherent7/80 below27 and gain7 below8; appropriate8 below27; EOS26 below37; repetition30 above18; original Web BPB gate failed" |
| expansion_teacher_tokens | 0 |
| adopted | false |
| eligible_for_expansion | false |
| status | "candidate_rejected_expansion_not_launched" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/natural_learning_ready.json — None</summary>

[原記録](../../reports/phase6/natural_learning_ready.json) ／ SHA256: `4e157943f82e46b7049e4284112f0d49118438b4aed96203f296da2ccd6607b6` ／ 55,002 bytes

| 原キー | 保存値 |
|---|---|
| pools.memory64.documents | 64 |
| pools.memory64.unique_tokens | 3426 |
| pools.natural1000.documents | 1000 |
| pools.natural1000.unique_tokens | 52791 |
| pools.expanded9192.documents | 9192 |
| pools.expanded9192.unique_tokens | 501559 |
| heldout_documents | 128 |
| maximum_input_tokens | 66 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/natural_learning_review.json — passed_learning_content_evidence</summary>

[原記録](../../reports/phase6/natural_learning_review.json) ／ SHA256: `c88227648bd0262dbea8205e0d3ceecc781dc848fa8056d00519a75e3d9d5782` ／ 45,272 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_learning_content_evidence" |
| summaries.mixed-control.teacher_tokens | 25000000 |
| summaries.mixed-control.physical_input | 25165824 |
| summaries.mixed-control.updates | 768 |
| summaries.mixed-control.train.documents | 64 |
| summaries.mixed-control.train.teacher_targets | 2236 |
| summaries.mixed-control.train.teacher_correct | 874 |
| summaries.mixed-control.train.teacher_accuracy | 0.39087656529516995 |
| summaries.mixed-control.train.eos | 30 |
| summaries.mixed-control.train.appropriate_gold_eos | 0 |
| summaries.mixed-control.train.appropriate_fraction | 0.0 |
| summaries.mixed-control.dev.documents | 128 |
| summaries.mixed-control.dev.teacher_targets | 4472 |
| summaries.mixed-control.dev.teacher_correct | 1815 |
| summaries.mixed-control.dev.teacher_accuracy | 0.4058586762075134 |
| summaries.mixed-control.dev.eos | 36 |
| summaries.mixed-control.dev.appropriate_gold_eos | 0 |
| summaries.mixed-control.dev.appropriate_fraction | 0.0 |
| summaries.mixed-control.diagnostic_pass | false |
| summaries.mixed-control.training_seconds | 51.36899270499998 |
| summaries.mixed-control.peak_allocated_bytes | 6149073408 |
| summaries.mixed-control.EOS_teachers.web | 42190 |
| summaries.mixed-control.EOS_teachers.short | 92079 |
| summaries.mixed-control.BPB | 0.9821879082414368 |
| summaries.mixed-control.rates.eos | 10 |
| summaries.mixed-control.rates.repetition | 48 |
| summaries.mixed-control.rates.unicode_failure | 1 |
| summaries.mixed-control.rates.role_leak | 0 |
| summaries.mixed-control.rates.empty | 0 |
| summaries.mixed-control.grammar_score2 | 10 |
| summaries.mixed-control.relevance_score2 | 38 |
| summaries.mixed-control.coherent | 0 |
| summaries.mixed-control.appropriate | 0 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.point | 0.6145833333333334 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.units | 96 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.examples | 192 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.primary.hard_accuracy | 0.6145833333333334 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.point | 0.5989583333333334 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.count | 192 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.macro_f1 | 0.5988603988603989 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.mcc | 0.19801337650222875 |
| summaries.mixed-control.Japanese.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.units | 96 |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.examples | 192 |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.mixed-control.Japanese.semantics.train_majority_accuracy | 0.5 |
| summaries.mixed-control.Japanese.semantics.categories.negation.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.negation.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.categories.quantity.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.quantity.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.categories.time.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.time.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.categories.comparison.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.comparison.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.categories.coreference.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.coreference.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.categories.causality.seed | 42 |
| summaries.mixed-control.Japanese.semantics.categories.causality.repetitions | 2000 |
| summaries.mixed-control.Japanese.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.point | 0.7734138972809668 |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8187311178247734] |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.units | 331 |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.examples | 331 |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.primary.hard_accuracy | 0.7734138972809668 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.point | 0.7250755287009063 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.ci95 | [0.676737160120846, 0.7734138972809668] |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.count | 331 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.hard_accuracy | 0.7250755287009063 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.macro_f1 | 0.4203152364273205 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.mixed-control.Japanese.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.units | 331 |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.mixed-control.Japanese.jblimp.train_majority_accuracy | null |
| summaries.mixed-control.Japanese.jblimp.categories.island effects.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.island effects.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.binding.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.binding.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.argument structure.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.ellipsis.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.filler-gap.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.morphology.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.morphology.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.nominal structure.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.quantifiers.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.categories.control/raising.seed | 42 |
| summaries.mixed-control.Japanese.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.mixed-control.Japanese.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-control.Japanese.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.point | 0.30384271671134944 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.ci95 | [0.2779267202859696, 0.32978105451295786] |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.units | 1119 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.examples | 1119 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jcqa.primary.hard_accuracy | 0.30384271671134944 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.33603663985701504] |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.count | 1119 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.macro_f1 | 0.3084781711234873 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.mcc | 0.13698891971743338 |
| summaries.mixed-control.Japanese.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-control.Japanese.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.mixed-control.Japanese.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.mixed-control.Japanese.jcqa.categories.commonsense.seed | 42 |
| summaries.mixed-control.Japanese.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.mixed-control.Japanese.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-control.Japanese.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-control.Japanese.semantic_both_contexts.correct | 25 |
| summaries.mixed-natural.teacher_tokens | 25000000 |
| summaries.mixed-natural.physical_input | 25165824 |
| summaries.mixed-natural.updates | 768 |
| summaries.mixed-natural.train.documents | 64 |
| summaries.mixed-natural.train.teacher_targets | 2236 |
| summaries.mixed-natural.train.teacher_correct | 2236 |
| summaries.mixed-natural.train.teacher_accuracy | 1.0 |
| summaries.mixed-natural.train.eos | 64 |
| summaries.mixed-natural.train.appropriate_gold_eos | 64 |
| summaries.mixed-natural.train.appropriate_fraction | 1.0 |
| summaries.mixed-natural.dev.documents | 128 |
| summaries.mixed-natural.dev.teacher_targets | 4472 |
| summaries.mixed-natural.dev.teacher_correct | 4472 |
| summaries.mixed-natural.dev.teacher_accuracy | 1.0 |
| summaries.mixed-natural.dev.eos | 128 |
| summaries.mixed-natural.dev.appropriate_gold_eos | 128 |
| summaries.mixed-natural.dev.appropriate_fraction | 1.0 |
| summaries.mixed-natural.diagnostic_pass | true |
| summaries.mixed-natural.training_seconds | 39.08503212999494 |
| summaries.mixed-natural.peak_allocated_bytes | 6149073408 |
| summaries.mixed-natural.EOS_teachers.web | 42190 |
| summaries.mixed-natural.EOS_teachers.short | 96513 |
| summaries.mixed-natural.BPB | 0.983213353200905 |
| summaries.mixed-natural.rates.eos | 26 |
| summaries.mixed-natural.rates.repetition | 30 |
| summaries.mixed-natural.rates.unicode_failure | 0 |
| summaries.mixed-natural.rates.role_leak | 0 |
| summaries.mixed-natural.rates.empty | 0 |
| summaries.mixed-natural.grammar_score2 | 25 |
| summaries.mixed-natural.relevance_score2 | 44 |
| summaries.mixed-natural.coherent | 7 |
| summaries.mixed-natural.appropriate | 8 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.point | 0.5989583333333334 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.ci95 | [0.546875, 0.6458333333333334] |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.units | 96 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.examples | 192 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.primary.hard_accuracy | 0.5989583333333334 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.point | 0.6041666666666666 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.count | 192 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.hard_accuracy | 0.6041666666666666 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.macro_f1 | 0.6041237113402061 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.mcc | 0.20837855928270652 |
| summaries.mixed-natural.Japanese.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.units | 96 |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.examples | 192 |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.mixed-natural.Japanese.semantics.train_majority_accuracy | 0.5 |
| summaries.mixed-natural.Japanese.semantics.categories.negation.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.negation.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.categories.quantity.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.quantity.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.categories.time.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.time.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.categories.comparison.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.comparison.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.categories.coreference.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.coreference.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.categories.causality.seed | 42 |
| summaries.mixed-natural.Japanese.semantics.categories.causality.repetitions | 2000 |
| summaries.mixed-natural.Japanese.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.point | 0.7643504531722054 |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.ci95 | [0.7219788519637462, 0.8096676737160121] |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.units | 331 |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.examples | 331 |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.primary.hard_accuracy | 0.7643504531722054 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.ci95 | [0.676737160120846, 0.7765105740181264] |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.count | 331 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.mixed-natural.Japanese.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.units | 331 |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.mixed-natural.Japanese.jblimp.train_majority_accuracy | null |
| summaries.mixed-natural.Japanese.jblimp.categories.island effects.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.island effects.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.binding.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.binding.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.argument structure.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.morphology.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.morphology.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.categories.control/raising.seed | 42 |
| summaries.mixed-natural.Japanese.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-natural.Japanese.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.point | 0.2957998212689902 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.ci95 | [0.2707774798927614, 0.32171581769436997] |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.units | 1119 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.examples | 1119 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jcqa.primary.hard_accuracy | 0.2957998212689902 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.point | 0.30116175156389635 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.ci95 | [0.2752457551385165, 0.32797140303842715] |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.count | 1119 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.hard_accuracy | 0.30116175156389635 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.macro_f1 | 0.30049807915888843 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.mcc | 0.12688841102912485 |
| summaries.mixed-natural.Japanese.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.mixed-natural.Japanese.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.mixed-natural.Japanese.jcqa.categories.commonsense.seed | 42 |
| summaries.mixed-natural.Japanese.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.mixed-natural.Japanese.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.mixed-natural.Japanese.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.mixed-natural.Japanese.semantic_both_contexts.correct | 24 |
| quality.checks.coherence_gain_at_least8 | false |
| quality.checks.paired_CI_lower_above0 | true |
| quality.checks.EOS_nonworsening | true |
| quality.checks.repetition_nonworsening | true |
| quality.checks.no_empty_role_unicode | true |
| quality.checks.BPB_gate | true |
| quality.checks.appropriate_completion_not_punctuation | true |
| quality.passed | false |
| practical.coherence_at_least27 | false |
| practical.appropriate_at_least27 | false |
| practical.EOS_at_least37 | false |
| practical.repetition_at_most18 | false |
| original_Web_gates.EOS_at_least8_more | true |
| original_Web_gates.repetition_no_worse | true |
| original_Web_gates.no_empty_role_unicode | true |
| original_Web_gates.BPB_degradation_at_most1percent | false |
| eligible_for_expansion | false |
| scientific_teacher_tokens | 50000000 |
| gpu_seconds | 297.5269214879954 |
| paired_Japanese_differences.semantics.point | -0.015625 |
| paired_Japanese_differences.semantics.ci95 | [-0.0625, 0.03125] |
| paired_Japanese_differences.semantics.units | 96 |
| paired_Japanese_differences.semantics.examples | 192 |
| paired_Japanese_differences.semantics.unit | "family/prompt" |
| paired_Japanese_differences.semantics.seed | 42 |
| paired_Japanese_differences.semantics.repetitions | 2000 |
| paired_Japanese_differences.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_Japanese_differences.jblimp.point | -0.00906344410876133 |
| paired_Japanese_differences.jblimp.ci95 | [-0.03927492447129909, 0.01812688821752266] |
| paired_Japanese_differences.jblimp.units | 331 |
| paired_Japanese_differences.jblimp.examples | 331 |
| paired_Japanese_differences.jblimp.unit | "family/prompt" |
| paired_Japanese_differences.jblimp.seed | 42 |
| paired_Japanese_differences.jblimp.repetitions | 2000 |
| paired_Japanese_differences.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_Japanese_differences.jcqa.point | -0.00804289544235925 |
| paired_Japanese_differences.jcqa.ci95 | [-0.01876675603217158, 0.002680965147453083] |
| paired_Japanese_differences.jcqa.units | 1119 |
| paired_Japanese_differences.jcqa.examples | 1119 |
| paired_Japanese_differences.jcqa.unit | "family/prompt" |
| paired_Japanese_differences.jcqa.seed | 42 |
| paired_Japanese_differences.jcqa.repetitions | 2000 |
| paired_Japanese_differences.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| protected_test_used | false |
| checked_at | "2026-10-05T13:16:04.781531Z" |

</details>

<details>
<summary>reports/phase6/realistic_curriculum_content_v1_notes.json — None</summary>

[原記録](../../reports/phase6/realistic_curriculum_content_v1_notes.json) ／ SHA256: `a505de28fdc3ab50b005a3552086d9a3b81a5712bcbfe0e47a75eadb1315efa1` ／ 6,856 bytes

| 原キー | 保存値 |
|---|---|
| scope | "Fixed64 source-readiness review; Codex nonblind, not independent human certification" |

</details>

<details>
<summary>reports/phase6/realistic_curriculum_v1_content-review.json — content_readiness_failed</summary>

[原記録](../../reports/phase6/realistic_curriculum_v1_content-review.json) ／ SHA256: `9aa0527eb3620821610a3826d4508370eb4d22b677d0f6a24314dd97d742052e` ／ 32,681 bytes

| 原キー | 保存値 |
|---|---|
| status | "content_readiness_failed" |
| documents | 64 |
| weak_documents | 33 |
| maximum_weak_documents | 10 |
| passed | false |
| sample_sha256 | "827045c51cf944e9cede6a87def668840de2f9712caf2d4961c12fcc0630e3f8" |
| notes_sha256 | "a505de28fdc3ab50b005a3552086d9a3b81a5712bcbfe0e47a75eadb1315efa1" |
| limitation | "Readiness of sampled language and local coherence, not fact verification or a full corpus audit" |

</details>

<details>
<summary>reports/phase6/realistic_curriculum_v1_prepare-job.json — complete</summary>

[原記録](../../reports/phase6/realistic_curriculum_v1_prepare-job.json) ／ SHA256: `3449dcb6c092d9aa5c2acae28d28e9427a14891d1ca899618e919676c75fa6c7` ／ 1,709 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.max_source_tokens | 2000000000 |
| binding.CPU_budget_seconds | 600 |
| binding.seed | 2026100601 |
| binding.protected_test_used | false |
| seconds | 23.65160534500319 |
| counts.scanned_tokens | 160000000 |
| tokens.train_explanation | 7000020 |
| tokens.train_daily | 3000028 |
| tokens.dev_explanation | 350001 |
| tokens.dev_daily | 150047 |

</details>

<details>
<summary>reports/phase6/realistic_curriculum_v1_ready.json — prepared_pending_content_review</summary>

[原記録](../../reports/phase6/realistic_curriculum_v1_ready.json) ／ SHA256: `c7a7338c2bd3a03f50c7c31c54e268d272c5bff36ac200e403db5f98dc498156` ／ 3,516 bytes

| 原キー | 保存値 |
|---|---|
| status | "prepared_pending_content_review" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.max_source_tokens | 2000000000 |
| binding.CPU_budget_seconds | 600 |
| binding.seed | 2026100601 |
| binding.protected_test_used | false |
| splits.train.tokens | 10000048 |
| splits.train.documents | 139809 |
| splits.train.body_bytes | 40232033 |
| splits.dev.tokens | 500048 |
| splits.dev.documents | 7043 |
| splits.dev.body_bytes | 2007482 |
| splits.test.tokens | 0 |
| splits.test.documents | 0 |
| splits.test.body_bytes | 0 |
| splits.test.stream_sha256 | "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" |
| splits.test.index_sha256 | "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570" |
| sample_sha256 | "827045c51cf944e9cede6a87def668840de2f9712caf2d4961c12fcc0630e3f8" |
| tokens_by_group.train_explanation | 7000020 |
| tokens_by_group.train_daily | 3000028 |
| tokens_by_group.dev_explanation | 350001 |
| tokens_by_group.dev_daily | 150047 |
| CPU_seconds | 23.651269016001606 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/body.json) ／ SHA256: `2e3b49f5bd68ecb62fcdea96f19e50e37d2e2dabc7ec8733efa1f347141f3ea0` ／ 67,247 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 371464.0153236389 |
| body.eos_nll | 937.1099682152271 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1352687563443153 |
| body.seconds | 1.2746439430047758 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/generation.json) ／ SHA256: `48e7ff07a43f88969bdc33f32af6f4ff65e736e86b209d028748726d0c8868c9` ／ 95,470 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/jblimp.json) ／ SHA256: `a37dd89e521f28453dce7f3b3c3429385f92ada512e2a74df2d49a723b1622d5` ／ 338,466 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7915407854984894 |
| summary.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7915407854984894 |
| summary.per_token_secondary.accuracy.point | 0.7522658610271903 |
| summary.per_token_secondary.accuracy.ci95 | [0.7038519637462236, 0.7976586102719029] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7522658610271903 |
| summary.per_token_secondary.macro_f1 | 0.42931034482758623 |
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
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/jcqa.json) ／ SHA256: `3622141292e2425c959f2b00909855efc1cb69efb4ba84a0b5f1a2e4d6804034` ／ 1,639,521 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.2975871313672922 |
| summary.primary.accuracy.ci95 | [0.2716711349419124, 0.32439678284182305] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.2975871313672922 |
| summary.per_token_secondary.accuracy.point | 0.2931188561215371 |
| summary.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.3199285075960679] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.2931188561215371 |
| summary.per_token_secondary.macro_f1 | 0.29246767346523195 |
| summary.per_token_secondary.mcc | 0.11684593804862778 |
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
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/result.json) ／ SHA256: `00f2c33bf0fc86ef23e6766760b5c10dd64ed1ce4095de9c292febb7e576cb88` ／ 190,562 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 60000000 |
| binding.teacher_goals.textbook | 20000000 |
| binding.teacher_goals.story | 20000000 |
| binding.loss | "CE body+EOS" |
| binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 371464.0153236389 |
| body.eos_nll | 937.1099682152271 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1352687563443153 |
| body.seconds | 1.2746439430047758 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 38 |
| greedy_rates.repetition | 21 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.53125, 0.609375] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7522658610271903 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7038519637462236, 0.7976586102719029] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7522658610271903 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42931034482758623 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.8066465256797583 |
| diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2716711349419124, 0.32439678284182305] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2931188561215371 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.3199285075960679] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2931188561215371 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29246767346523195 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.11684593804862778 |
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
| diagnostics.semantic_both_contexts.correct | 15 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>
