# 評価・生成・意味診断 — 8/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/review.json — actual_relation100M_all80_bridge128_retention128_and_reused_curriculum100M_complete</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/review.json) ／ SHA256: `1eeba0f26a076ca1bd5a15a717c1066f935375e3a83ef5b6dd3d8bade1a9e5cc` ／ 16,832 bytes

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
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0000.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0000.json) ／ SHA256: `c9eea004e3984702044cec932f1d339c7ce80e32da033e94a53a1fa1fdcbf0ee` ／ 9,778 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0016.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0016.json) ／ SHA256: `4c97a60de4800bf6be1d349b7b7748697906274ea3fe9e271f3eba7b67c233ab` ／ 9,426 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0032.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0032.json) ／ SHA256: `58d764a1df99a4c1a1ab1f3dcaa19a1c7766a2bd8e59d193f5b499fb6b9a1d24` ／ 10,019 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0048.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0048.json) ／ SHA256: `977443e3a4af103021fa1cee231e400470b88b52e47784a897f2c3c3429df068` ／ 9,329 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0064.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0064.json) ／ SHA256: `875088d359062489670307405edfd701f53162e50403b879b4933570a7b22a87` ／ 10,120 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0080.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0080.json) ／ SHA256: `917bbbc739238ac998676e85904ce05282dedb20113bd29883b177b1b7e3b4fa` ／ 9,518 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0096.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0096.json) ／ SHA256: `5b7cbb206039bac72e91a63be747afdd7a21021f08909afd59bc6e176e02fb2b` ／ 9,618 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0112.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0112.json) ／ SHA256: `f3b8d76a3161f239eecd523480650985c7209061e00810323d91a18533bfa587` ／ 9,968 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0128.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0128.json) ／ SHA256: `a0e923029687e5fa40ae3b30e76e24fd091677b460f2a070fbcd8826bc5b4090` ／ 9,622 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0144.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0144.json) ／ SHA256: `1d19548c516a9ade0ea3e4d81710f9b550f1d434baaf095b295eb0c4cd19f5c3` ／ 9,681 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0160.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0160.json) ／ SHA256: `f03652086b85d6f1ad2faeb5410d506a29d7076cc1009ae3127d483723f2ec31` ／ 9,964 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0176.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0176.json) ／ SHA256: `e5a79a7eb9189f4b5dc53c71c286c4c0cd435a86f323984bb5eeeee5ebcbb70d` ／ 9,793 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0192.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0192.json) ／ SHA256: `8dfbe64f9d447cd3f3220cb7c5a06efd43a9f7c5a1c0e50fb60d4f9dbbaaa6f1` ／ 9,708 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0208.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0208.json) ／ SHA256: `c47e03ff59c0cf6ac863c7cbecd5b3b6f3a8873c1607eeac765702e0da91893d` ／ 9,446 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0224.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0224.json) ／ SHA256: `69ae890576dd0057393b3dfb6276947750393c4230dcc78511d2631d1a8960ab` ／ 9,617 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0240.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0240.json) ／ SHA256: `4446c1032e9dc9ecc8e8bae2189c0a786535d76739e2605326431d05a4d9f743` ／ 9,443 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0256.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0256.json) ／ SHA256: `1cd716bc7804914da09370bd679cc37739b5aaedbc83aaa94cb2ea7a16445246` ／ 9,371 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0272.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0272.json) ／ SHA256: `15150e4879faa81a9707a4221056109986a44178f9a50d5d25a659fbed315cd7` ／ 9,347 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0288.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0288.json) ／ SHA256: `77c129643f43a5691c74d294a2b5f51fd2a311136d72b3e8e58edf2d633377aa` ／ 9,368 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0304.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0304.json) ／ SHA256: `80088efc60186ea92230f1dffacac54a1da851872f5e053c92c8fbb1b0d2b023` ／ 9,545 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0320.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0320.json) ／ SHA256: `5b47e42fe3f252e762e1aafbc7ee244e1cd635709b7f977001d5ee11e736a629` ／ 9,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0336.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0336.json) ／ SHA256: `4c406dfda83ba9b49ac0a16d62c6fb84e17177249282ec2ef6c78ca18f3211d0` ／ 9,183 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0352.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0352.json) ／ SHA256: `3bc002581a85e881f8f5234341320d49219893c1ad35934d5683e6ac4a404e1a` ／ 9,519 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0368.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0368.json) ／ SHA256: `78c295f7aca8b99e985e1a58e5f705200ff6fc9431c65bf3ad2a35dda206e6bb` ／ 9,291 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0384.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0384.json) ／ SHA256: `bf818c7d6c0a03bae5fc69cf702679aae3f7a6c079073c94efaeebdc2e7a6a72` ／ 9,620 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0400.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0400.json) ／ SHA256: `fd2b0ed76bef87c45820ed68043fbd99c109909e72861ebcf4540ba1e0731556` ／ 9,301 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0416.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0416.json) ／ SHA256: `9a6cef4b90207ad2a6f6dbc82bd1d7e8b8d819f96e7ee0f974159f87c59a637b` ／ 9,627 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0432.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0432.json) ／ SHA256: `a57e4c549cd86ce2b13e9b4605b1fb91f7eabc222c59f3f032b55a5d23d2bd3f` ／ 9,079 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0448.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0448.json) ／ SHA256: `0004e71f4492e943eaaea538d03ccf5b4f29df5b964f9b496e35a45d267dd732` ／ 9,348 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0464.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0464.json) ／ SHA256: `3fe85212a93a56f5267eec82f7cbb32ebc872193aecd7ae7769af2b4ab461fca` ／ 9,179 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0480.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0480.json) ／ SHA256: `7d12b58c347bc15a7119df9b99ceb9f6049215680f9d237f933fda9363eb99b9` ／ 9,204 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0496.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/0496.json) ／ SHA256: `99d30111fd6e2108b38dc2d73fb3f8c20dda169138cfc01d268cca37b212234f` ／ 9,277 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/parent2B/result.json) ／ SHA256: `b2d5446f260737e205fee8f04c758000a9d2bcd51466c9b0d74cfa20a0266bfb` ／ 186,476 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.484375 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 3 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 9 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 113 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5078125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 5 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 55 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.5546875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 21 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 100 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 13 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 53 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0000.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0000.json) ／ SHA256: `4c1b38485b1673c16658a5ee11aa48aca43c068fdccfe9230d72eeb0bdba85b6` ／ 9,965 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0016.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0016.json) ／ SHA256: `70e0e1215be0e5e5c62b5576f35a5f23b3bee270f47820c43d8b47e39762b191` ／ 9,657 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0032.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0032.json) ／ SHA256: `81c1679c6c3429d1eac7e371110291e131b0c063e245d36475e14f264eeb4e04` ／ 10,258 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0048.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0048.json) ／ SHA256: `0c0bcd8f8b2832b359cdb845fa84f324541f30c93ee59a4eb3b12523cccc2db1` ／ 9,543 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0064.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0064.json) ／ SHA256: `fc7af3fbafd656f60304c82796557fe9982c4b4c6306f277a6264e95f45c777d` ／ 10,363 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0080.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0080.json) ／ SHA256: `dc7baca4bf7245271081a17458ec107610d4b78f220c29e7006e574331bb1f3a` ／ 9,748 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0096.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0096.json) ／ SHA256: `9ddb6870641c8d51212cda995eb610aa50500dcbfcd0a6fb500378346e8088b3` ／ 9,839 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0112.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0112.json) ／ SHA256: `d2a218026433c9bb35067b1157404429a422b0a0ca7ecaaef12ebb783bd60c61` ／ 10,181 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0128.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0128.json) ／ SHA256: `6dafbb7b277b10cae0fa3a4dd2201815a015f626254365f97daf4a75d2c1d602` ／ 9,843 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0144.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0144.json) ／ SHA256: `b826e9bd1816073cce666428260d0baece5b944f2060842f35463ad33529f93a` ／ 9,932 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0160.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0160.json) ／ SHA256: `4f55ff5ab5760fa64b446e484b082514b7aba99648ff632c671e70617b25eac7` ／ 10,209 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0176.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0176.json) ／ SHA256: `a77f03412891b0d06272f6eb2a54c554085c1ea04a98006cd7766eb2f3201a50` ／ 10,023 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0192.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0192.json) ／ SHA256: `4bcbe9ef178a4f3ae761ba8221ca6e99e3c8d2cc8e30c88c3e3dce39a9364c25` ／ 9,928 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0208.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0208.json) ／ SHA256: `b9cf84b5a8c3b2436ee928f4ab61b08cf678847c2e888ee1d909f5fb7575a1ba` ／ 9,690 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0224.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0224.json) ／ SHA256: `a48dbaa826163b92dcc9bc37cd9e1d42f1e4009c09bd850609affce2ce71c60a` ／ 9,863 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0240.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0240.json) ／ SHA256: `4523f2c1939e93b10c6801f75ced378f387fd2371cdbb328aaeaa76187b6338c` ／ 9,671 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0256.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0256.json) ／ SHA256: `728978906b8be4263c54a8f8863f8dd1351d79f2e76c1971ba7de4b981b03d1d` ／ 9,664 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0272.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0272.json) ／ SHA256: `b5a3b4a84be0769cf554bbede1903f76e9b8f827a6a649e38bfa19e984b2191a` ／ 9,665 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0288.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0288.json) ／ SHA256: `3c7fb3fe9912784caa8cc4fdf383e0756746e573935ba101068d46820af3fb76` ／ 9,647 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0304.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0304.json) ／ SHA256: `f270ff82cc7badacc3de922a614622276170140145a9580813a22219320e3a75` ／ 9,863 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0320.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0320.json) ／ SHA256: `df80bfbd70215a7182606554db14b83e4553aaf61cb661f34a09eb59890d1926` ／ 9,383 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0336.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0336.json) ／ SHA256: `3dd0d50c87dc2755edbf58efe449e8f7def763595c997e1916b03ad5cce17557` ／ 9,475 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0352.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0352.json) ／ SHA256: `e92d5dc90481b08d11b687f21b5dfe1e0d1224b10210a9dd5e3f3c06986e6a63` ／ 9,834 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0368.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0368.json) ／ SHA256: `27a58214672f1e188c6199ee2b7006a468bfe937f010ab548615c116a45092dd` ／ 9,576 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0384.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0384.json) ／ SHA256: `46b5d55a77a7948f4100f3b66ce9bde596c6f0e27d65b96f8f75feb23ed3f493` ／ 9,928 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0400.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0400.json) ／ SHA256: `f53bf9c3966a5d096e68af25136e9c381fe1980bd2f98c2ba0b43285a25fdb26` ／ 9,575 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0416.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0416.json) ／ SHA256: `1f0911de0301c0af41254741e1ac55e0dc6fa6a3360b75ff828272efd578fe25` ／ 9,928 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0432.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0432.json) ／ SHA256: `0f7932293e2e27f8567fe56a43045e08a53bfe9203c17ac705493e8d2456162e` ／ 9,396 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0448.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0448.json) ／ SHA256: `b736edafed7c40c4a291a0609a947abf6612d785ba05dc688240c98ccb83b015` ／ 9,647 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0464.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0464.json) ／ SHA256: `9216b08625587630062ef01bbeeb6f0f30685f8df9afa064319ae0d4121440c1` ／ 9,464 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0480.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0480.json) ／ SHA256: `4b671ea67e7e71fd488be82ad56113ca914ebe3038e3455629cf227b73add0ce` ／ 9,503 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0496.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/0496.json) ／ SHA256: `2e6cb689fdbe7981d3815d2efebd2a28af60ce9ec770cd0ce903a84cd94b6b69` ／ 9,567 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/bridge/relation100M/result.json) ／ SHA256: `3d78274c8a8856b6cfddc3103dce70faa4eede9606c2e47d1255b357bbad0ffa` ／ 185,847 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.67578125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 50 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 18 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.68359375 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 51 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 73 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 114 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69140625 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 54 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 114 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7734375 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 35 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 29 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0000.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0000.json) ／ SHA256: `de0f7c9eb9dc548a72ee38759093cb527a26cc15ef6a8fe9714de32d0a54dd78` ／ 8,000 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0016.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0016.json) ／ SHA256: `632306d99eb9fd5751dca1796ff7008771d21c7c67e4e2063079ada391e1dfe6` ／ 8,349 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0032.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0032.json) ／ SHA256: `145c76ed216b5b3989d066c64e125fe998301cb0908fa2051924d037dcb23475` ／ 7,030 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0048.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0048.json) ／ SHA256: `f4ecbf5873a32f92c0d41f3213065c4c96677280ce3d0d58476adbf88c110592` ／ 8,160 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0064.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0064.json) ／ SHA256: `0bbc7f08ecd2fc56a211451eb19a29d3df6b8f6b293d3f1a9746633b9c820b55` ／ 8,539 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0080.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0080.json) ／ SHA256: `a44afce1342491d5418293ca916a1600e4bdf8f6180dafe947afcf845bc9f37e` ／ 7,111 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0096.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0096.json) ／ SHA256: `7c6f7ad958f35c5eba366a1072e29027dd218b3e5c51e853b21cc978d69f4bba` ／ 8,107 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0112.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0112.json) ／ SHA256: `ebb068c5ec684da043a52e878b87967ed66913dd58b055fcae9d52326bfd824c` ／ 8,294 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0128.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0128.json) ／ SHA256: `f3abef5e644000ef8f0602cddd63ec17ff2206281cd7feaa4d7431dd072ba855` ／ 7,119 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0144.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0144.json) ／ SHA256: `d3d700c67d1cf1c89d19649c20dc95533951140ac5d6a2cfab12781c3952fd4a` ／ 8,198 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0160.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0160.json) ／ SHA256: `b0379d33803f5c1999cb5b9416ccdefea959eb7f96da31d172c4613860c9dd95` ／ 8,658 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0176.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0176.json) ／ SHA256: `87c89599f5921e5a1f226cfa346a65150d826cd49040837bcea339a1730c86d7` ／ 6,959 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0192.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0192.json) ／ SHA256: `20543407017288a5f73531346ffa272212b5167692fe5c544e592370d869a51d` ／ 8,213 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0208.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0208.json) ／ SHA256: `4d9c59fb0abf8444ac61d69e0bcf44ecaf7763d2bbdde057c88ad6a12e8b853c` ／ 8,538 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0224.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0224.json) ／ SHA256: `7cfa02ca4e637bc5c68384ab02d98405b98d5212ee7077a062edcf5eacc05f22` ／ 7,137 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0240.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0240.json) ／ SHA256: `b616dd84f5dc9d717aba6a480d9d47db4d50fe3c27ead3622507c8de02dfbd08` ／ 8,365 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0256.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0256.json) ／ SHA256: `e34eddfce12795fe8dc8f3f4b6e0593b0a3abd4b617a3683e4cb47c1cdffa7bc` ／ 8,311 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0272.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0272.json) ／ SHA256: `9ebab4391738b2804c6c426a515b6531e02620a461504d6a0d6f111b4179520e` ／ 8,470 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0288.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0288.json) ／ SHA256: `0260538b74093de17c3dba3d66a4ff05663b06ec3d87798383f95a06dc578964` ／ 7,136 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0304.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0304.json) ／ SHA256: `cd28334e83c88fc74b509dbb85abbf70cef0c9927e16b900173126bf3f722fdb` ／ 8,219 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0320.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0320.json) ／ SHA256: `0002d8fc2d391b429c71e872cfbba23a420948d17b70811dc472477e12def1aa` ／ 8,639 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0336.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0336.json) ／ SHA256: `d6704880dec0d25da464966c8d78eb7595b79bb80ba359e35f912669af6bb824` ／ 7,130 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0352.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0352.json) ／ SHA256: `60c3bdd65a8fdd62046df0a4611068b04a48c4dcaac197e7aa4bd6fbf8964599` ／ 8,227 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0368.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0368.json) ／ SHA256: `02e0546375dc1dd6c7b959b7f223eceb69c045a9a59339374e932d3ea421dfb2` ／ 8,203 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0384.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0384.json) ／ SHA256: `c4bbf816e28b404ea1098ec7c3d05aa32a9f088be4207335fe397c1deca836c1` ／ 7,070 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0400.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0400.json) ／ SHA256: `87fc1c177010635041ff90e9e5409b70ecd55e538c4273edaa31673258a40f54` ／ 8,197 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0416.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0416.json) ／ SHA256: `55692daea5df16660cf761932d30c4d828f053d02b12e79ff7ed7e497cfc6505` ／ 8,213 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0432.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0432.json) ／ SHA256: `058a5f76896e519becefc479db884c0b9c5999c1773af1ea8d83703bc205daf5` ／ 7,130 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0448.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0448.json) ／ SHA256: `6b98ecd9be2af7da2f10e0a7d2c78bad9b2c72d315152ed3e18f7b1ce0677a73` ／ 8,141 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0464.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0464.json) ／ SHA256: `58f5f06553088991903eba0fd786210ac5cc2ac4ce985926894dd088b112df67` ／ 8,388 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0480.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0480.json) ／ SHA256: `e472273c3be481650d72fbce42b5433bc29ee00db93a4a56b021ae3e4d32fb82` ／ 7,046 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0496.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/0496.json) ／ SHA256: `aab3f889ec1400de7bb822cec0c288b9f5598e31e5265844110e3d428cf7c3f6` ／ 8,130 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/transfer/retention/relation100M/result.json) ／ SHA256: `8e8ff6f436d804c944e632fe77697630ee16da3765de9462d35e5aa2e5f704df` ／ 182,436 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.578125 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 45 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 78 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 44 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 80 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/content-notes.json) ／ SHA256: `8fc03ade52cb710ef1da5558124c708d2975e00e7638dc03d82f2da0aef3f599` ／ 24,750 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/content-pilot.json) ／ SHA256: `659e491977bb57d91ccc1f31e94e3c66ba78b9de20d48488546f6a1ae0075f96` ／ 88,180 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/content-review.json — all64_relation_language_source_review_complete</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/content-review.json) ／ SHA256: `a929eeda49d4ed13198090c597a903149910a654f425ecd464ade8479622b825` ／ 24,593 bytes

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
<summary>reports/phase6/condition-relation-language-20261006/data/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/content-notes.json) ／ SHA256: `8fc03ade52cb710ef1da5558124c708d2975e00e7638dc03d82f2da0aef3f599` ／ 24,750 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/data/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/content-pilot.json) ／ SHA256: `659e491977bb57d91ccc1f31e94e3c66ba78b9de20d48488546f6a1ae0075f96` ／ 88,180 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/data/content-review.json — all64_relation_language_source_review_complete</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/content-review.json) ／ SHA256: `a929eeda49d4ed13198090c597a903149910a654f425ecd464ade8479622b825` ／ 24,593 bytes

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
<summary>reports/phase6/condition-relation-language-20261006/data/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/manifest.json) ／ SHA256: `154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936` ／ 660,151 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100662 |
| original_train_selection_seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 85350 |
| generated_body_bytes | 330943 |
| serialized_tokens | 89446 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| replacement_checks.changed_documents | 684 |
| replacement_checks.other_four_categories_byte_exact | true |
| replacement_checks.original_selected_families_facts_labels_order_preserved | true |
| replacement_checks.all24_train_structures | true |
| replacement_checks.all2048_train_bodies_unique | true |
| replacement_checks.lexical_entities_disjoint | true |
| replacement_checks.new_held_grammatical_forms_disjoint | true |
| replacement_checks.all128_new_probe_families_disjoint | true |
| replacement_checks.probe_bodies_absent_from_train | true |
| replacement_checks.original128_retention_probes_not_new_heldout_evidence | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| new_local_serialized_tokens | 89446 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| training_pool_accepted | false |
| loss_policy | "All body+EOS ordinary CE weight1; focus annotates outcomes but does not replace supervision." |
| limitations | "Only negation/comparison language replaced in the same selected2048; changes token length/lexical/EOS density together.128 new two-category probes share authored semantics; original128 are retention, not newly held-out grammar after replacement. Not independent natural-language quality or external truth certification." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/data/retention-probes.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/retention-probes.json) ／ SHA256: `daf92018a167c24db83a4d3bd029d45973bd7f34f3fd452f52419ccc0b651d83` ／ 856,180 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/data/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/data/transfer-probes.json) ／ SHA256: `4e9c11d18395b03aeeb8a9ac7caec86f8ef6f59ca598ca00bf14bac447f85823` ／ 930,998 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/job.json — complete_pending_fixed64_content</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/job.json) ／ SHA256: `a038381efe4112afa886b15624d1f42349b80550d3ade5d7d3b3aedf2f324d20` ／ 907 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_fixed64_content" |
| CPU_limit_seconds | 240 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| CPU_seconds | 0.38243402299121954 |
| changed_documents | 684 |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/manifest.json) ／ SHA256: `154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936` ／ 660,151 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100662 |
| original_train_selection_seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 85350 |
| generated_body_bytes | 330943 |
| serialized_tokens | 89446 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| replacement_checks.changed_documents | 684 |
| replacement_checks.other_four_categories_byte_exact | true |
| replacement_checks.original_selected_families_facts_labels_order_preserved | true |
| replacement_checks.all24_train_structures | true |
| replacement_checks.all2048_train_bodies_unique | true |
| replacement_checks.lexical_entities_disjoint | true |
| replacement_checks.new_held_grammatical_forms_disjoint | true |
| replacement_checks.all128_new_probe_families_disjoint | true |
| replacement_checks.probe_bodies_absent_from_train | true |
| replacement_checks.original128_retention_probes_not_new_heldout_evidence | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| new_local_serialized_tokens | 89446 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| training_pool_accepted | false |
| loss_policy | "All body+EOS ordinary CE weight1; focus annotates outcomes but does not replace supervision." |
| limitations | "Only negation/comparison language replaced in the same selected2048; changes token length/lexical/EOS density together.128 new two-category probes share authored semantics; original128 are retention, not newly held-out grammar after replacement. Not independent natural-language quality or external truth certification." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/ordinary-stream-audit.json — actual_relation_vs_curriculum100M_original3_teachers_identical</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/ordinary-stream-audit.json) ／ SHA256: `ed88dfc596707ec75c287c62f16d5acd2bfd681a385308a27c506dcba738248c` ／ 3,290 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_relation_vs_curriculum100M_original3_teachers_identical" |
| actual_generated.teachers.web | 75000000 |
| actual_generated.teachers.story | 5000000 |
| actual_generated.teachers.ordinary_textbook | 10000000 |
| actual_generated.EOS.web | 656229 |
| actual_generated.EOS.story | 38240 |
| actual_generated.EOS.ordinary_textbook | 74183 |
| actual_generated.body_bytes.web | 299907916 |
| actual_generated.body_bytes.story | 20452979 |
| actual_generated.body_bytes.ordinary_textbook | 42739471 |
| actual_generated.physical_inputs.web | 75674624 |
| actual_generated.physical_inputs.story | 5039104 |
| actual_generated.physical_inputs.ordinary_textbook | 10075136 |
| actual_generated.physical_inputs.conditional_textbook | 10234880 |
| actual_generated.total_updates | 3083 |
| previous_control.teachers.web | 75000000 |
| previous_control.teachers.story | 5000000 |
| previous_control.teachers.ordinary_textbook | 10000000 |
| previous_control.EOS.web | 656229 |
| previous_control.EOS.story | 38240 |
| previous_control.EOS.ordinary_textbook | 74183 |
| previous_control.body_bytes.web | 299907916 |
| previous_control.body_bytes.story | 20452979 |
| previous_control.body_bytes.ordinary_textbook | 42739471 |
| previous_control.physical_inputs.web | 75666432 |
| previous_control.physical_inputs.story | 5039104 |
| previous_control.physical_inputs.ordinary_textbook | 10075136 |
| previous_control.physical_inputs.conditional_textbook | 10243072 |
| previous_control.total_updates | 3083 |
| checks.target_sha256 | true |
| checks.teachers | true |
| checks.EOS | true |
| checks.body_bytes | true |
| CPU_seconds | 6.478647753014229 |
| CPU_limit_seconds | 30 |
| accepted_generated_review_sha256 | "a929eeda49d4ed13198090c597a903149910a654f425ecd464ade8479622b825" |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "CPU actual sampler replay, not GPU learning. Conditional interleaving/padding and own targets differ; original3 supervision equal." |

</details>

<details>
<summary>reports/phase6/condition-relation-language-20261006/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-relation-language-20261006/transfer-probes.json) ／ SHA256: `4e9c11d18395b03aeeb8a9ac7caec86f8ef6f59ca598ca00bf14bac447f85823` ／ 930,998 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/job.json) ／ SHA256: `5b6b6b3a9b2e03e5d321e949458ab75c6256086e5dd14681c7b5652b0788e206` ／ 681 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 4.704371909989277 |
| GPU_budget_seconds | 60 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| completed_documents | 1536 |
| total_documents | 1536 |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0000.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0000.json) ／ SHA256: `7b0c293ea5b9be3c680cfdf574ca8af8dbf100af521f43703d83b96e8d3a3b7d` ／ 311,472 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0032.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0032.json) ／ SHA256: `781e7ad1bca07f8c9b7a487f0ed7461db4faa7e98ae8aaee824391aaea59af53` ／ 287,698 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0064.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0064.json) ／ SHA256: `18f3db89d68ea7438a3b9afe95543a5f1d603d6401713410641022d2f589f56d` ／ 287,659 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0096.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0096.json) ／ SHA256: `c2a9feea2782c98ef9f05bd0815c0f233091a5596080527b778489cbe1a6631d` ／ 295,133 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0128.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0128.json) ／ SHA256: `5617b80a49de46b0999ee90467f236f9a129253b7f89bd79096f43f0fc890a00` ／ 271,871 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0160.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0160.json) ／ SHA256: `6dd7f6eb64f4ff9b305b838c7d4169a34de6c6663eae99ed65b024b3e36951a2` ／ 302,175 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0192.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0192.json) ／ SHA256: `73def3d9de4803c3792d0e307cdef3b6eba700cd8550f219d7d0caac48ebe7f4` ／ 271,988 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0224.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0224.json) ／ SHA256: `a830689ad2fbd6cd547054010bf58206baf8c59cf99bae79bfec31931f7b1e6a` ／ 271,247 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0256.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0256.json) ／ SHA256: `296c16bac7056913a5407b2fb3dc512d79874bc3f708c20efd64f6f611ad5bd4` ／ 296,723 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0288.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0288.json) ／ SHA256: `d3b714684cf655e5669815c2e99c06d4e327238d72c163fd276b61fdc827369d` ／ 279,665 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0320.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0320.json) ／ SHA256: `fdded37edb4e1f70c75182f55cc0b7082b5b7f43847de1f4e354e80615a8af0a` ／ 282,444 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0352.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0352.json) ／ SHA256: `32023eb0240258c9a2e9ec87b58ab09779b1f3eb7ce473f3382be2c8942e75c2` ／ 260,513 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0384.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0384.json) ／ SHA256: `3e26dd4db9939ccd439b828852ae04766821e090189301a16bc27e7167fbe202` ／ 273,765 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0416.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0416.json) ／ SHA256: `570627168e67f71b9469a290828ed360121c4e71c8e34b931531c3c84376827c` ／ 267,791 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0448.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0448.json) ／ SHA256: `a24f26838a8db9621868e23e1d290841d5e9fbb0323d58fa8b787b14e0cee3a5` ／ 258,431 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0480.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/control/0480.json) ／ SHA256: `bb5d975e8537a747a17786f4f8788e3f4d56d6609aa2bc8d8550503b62550fff` ／ 239,538 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0000.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0000.json) ／ SHA256: `7b16f257b7fc652fff09caab96d974b45557f8ce00238e4a5a16df65c043fd5c` ／ 308,696 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0032.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0032.json) ／ SHA256: `6fe6e4c3e3581cb570a80f4f1affa5534e62d236ee6b116c381ac600a2a4e0ab` ／ 285,367 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0064.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0064.json) ／ SHA256: `fc575e24eb1fa1b97b13100edf99744885b523a95fc76aae7fcc228bcf707a27` ／ 285,301 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0096.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0096.json) ／ SHA256: `d3b116f3c728cfacd761755d22caa3edb120fbd4e95f0e2cf2cfd4998a0464ad` ／ 292,625 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0128.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0128.json) ／ SHA256: `beff553243cc7454ca8b1a89754752ed29d1d6df3d08ca75c795c4e5f107afe2` ／ 269,589 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0160.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0160.json) ／ SHA256: `429782ee90317fa78a143bf5bc12432cdd601d2556c7be1cc5f69082832b094d` ／ 299,640 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0192.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0192.json) ／ SHA256: `b940afed55acf1e886b8a161816eb0546c5d73c977500e91e2777c2b75700498` ／ 269,713 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0224.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0224.json) ／ SHA256: `5b3f6ad37c5e919d3a3e8001eb4203cb2686fdaa299cc926b88d4f2f6b2bb379` ／ 268,919 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0256.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0256.json) ／ SHA256: `2919eab9ee772cbb6cf8a5f7101fcfed43f20e3227507f724747699735a1cb5a` ／ 294,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0288.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0288.json) ／ SHA256: `273c2b4338458451a1b5bf50d416a56355188fca7b2f70de35cca13fc9cb9b45` ／ 277,329 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0320.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0320.json) ／ SHA256: `26fac29ca2f7f21828d41b282918bbde2d3587c933ab2aea793dc346028956cf` ／ 280,052 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0352.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0352.json) ／ SHA256: `1b02cd5c1dc7541eac1b59ff4c58a8fde1a004dd2ae8eea7267d2f97b2efaf2a` ／ 258,319 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0384.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0384.json) ／ SHA256: `9406d5f7588f55e2d608cddf02e473b716c8272c4ebed3b0492d7dcc6f456ef5` ／ 271,470 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0416.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0416.json) ／ SHA256: `355f9f780103d0cc2f86661f39d05b9f24c7128c8ae66e68228c5c4a437dfd7b` ／ 265,508 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0448.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0448.json) ／ SHA256: `3a1cd5a980899b82f6f2c41828c8e18dd575b25a5b497e6533dbc78992e94c77` ／ 256,245 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0480.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/parent2B/0480.json) ／ SHA256: `2473e8e03d4b05d79083406af5a73673788fc626db4d4c46df595e47bb3f770b` ／ 237,514 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0000.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0000.json) ／ SHA256: `eb216a478b6cb22784f377d38daa323ddc2c4b0798ae97e904eea79ef19ff833` ／ 312,467 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0032.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0032.json) ／ SHA256: `587ea30e33d6c4c4b59ac28aed49d076444b9afda5f958ec7061a95df9253083` ／ 288,906 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0064.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0064.json) ／ SHA256: `dd793d562eb4bf9e2b46575ed0b001b8379085435d08bbddbcd14cb6546f77df` ／ 288,826 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0096.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0096.json) ／ SHA256: `7c080c4efb17c348d944e1a39bf2dd44fc1f43268c0a88de35dabcd10ab599cc` ／ 296,230 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0128.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0128.json) ／ SHA256: `35b27442f7bdc59d5953800b5ce4b829d6243579da8e595b04beb28a5db52671` ／ 273,018 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0160.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0160.json) ／ SHA256: `a60dd858b886f943be9529249c76de14d2edd834b00d72b0f4b9f1fce21fa22d` ／ 303,315 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0192.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0192.json) ／ SHA256: `fbf7e5fab160c32c9f5bf590e3caea689b454a90e509b6cc44fe4aba44e1cae0` ／ 273,074 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0224.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0224.json) ／ SHA256: `8722797b194880910dc4e6b751c9acd4d804cb44bd1375dbfeb26feda5c15c20` ／ 272,423 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0256.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0256.json) ／ SHA256: `030e28fd39450f6f527920b7d73d6a69a3d4df3ee24658cb9d194da2a8812c5b` ／ 297,863 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0288.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0288.json) ／ SHA256: `25f5dfea1466fbac29f4505cc4bbe48d5c1e70d7f1a71b297b891e29bab9a34d` ／ 280,754 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0320.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0320.json) ／ SHA256: `a7fba887a2ccdf200824e22a1cca3841edaffa258cec15c11043d87f4c729195` ／ 283,527 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0352.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0352.json) ／ SHA256: `08b1342401f58c0892a1c783a3a34e43db0c3630e51545f40afa2f36d3c76e51` ／ 261,465 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0384.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0384.json) ／ SHA256: `05b4d5add7ef8bcc0217db2ddfe697475fff03e7f3895aa6611f6569c34459cb` ／ 274,912 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0416.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0416.json) ／ SHA256: `4b85013322b8265c26d323394dd3246bb93692b87a13564e0452be9a64b14c66` ／ 268,712 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0448.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0448.json) ／ SHA256: `48dfa0882849b3ba4dc5265909dc18b114dc09d92bea2d24af309febec8e349d` ／ 259,465 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0480.json — None</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/outputs/positive4/0480.json) ／ SHA256: `3d2860bc4c72bf042f20b3577fd7a75b1099418e8263a0dc61f788088da3e424` ／ 240,452 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/result.json — all512_original_targets_3_checkpoints_measured</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/result.json) ／ SHA256: `b079bf4a07a085008881a784571f4a1551a59751c5545cf6b9cfcadd9820151a` ／ 5,394 bytes

| 原キー | 保存値 |
|---|---|
| status | "all512_original_targets_3_checkpoints_measured" |
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
| GPU_seconds | 4.703986317006638 |
| evaluated_documents | 1536 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| limitations | "Train-only teacher forcing can distinguish failure to fit from fit without transfer on these examples, not prove generalization, attention failure or capacity. The saved dev paired analysis remains secondary; no evaluation text enters learning." |

</details>

<details>
<summary>reports/phase6/condition-trainfit-diagnostic-20261006/review.json — actual512_by3_trainfit_diagnostic_review_complete</summary>

[原記録](../../reports/phase6/condition-trainfit-diagnostic-20261006/review.json) ／ SHA256: `abc2a05db3f159e9984f63c58a74a91cc20dbb75bc2ec15ef24867e82ee4aa29` ／ 6,740 bytes

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
<summary>reports/phase6/condition-transfer-comparison-20261006/annotations.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/annotations.json) ／ SHA256: `adecb731c1873cc585698c0840c1f29a7d7792b9b1fd732f9aaa4cf202c5df93` ／ 37,260 bytes

| 原キー | 保存値 |
|---|---|
| control_notes.reviewer | "Codex nonblind; all80 individually read" |
| control_notes.independent_human_blind | false |
| control_notes.generation_sha256 | "5f02dd36439eca9b8013ac2fc1ae9220be1358f0f9be11f53c1e6be853c1ac99" |
| control_notes.rubric_consistency_reuse.keys | ["id", "prefix", "text", "stop_reason"] |
| control_notes.rubric_consistency_reuse.all_current_outputs_individually_read | true |
| control_notes.rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |
| curriculum_notes.reviewer | "Codex nonblind; all80 individually read" |
| curriculum_notes.independent_human_blind | false |
| curriculum_notes.generation_sha256 | "f4a01f16fda39a368f5160c2ac938d168b7df4cea5f46fc5f11eb49627555913" |
| curriculum_notes.rubric_consistency_reuse.keys | ["id", "prefix", "text", "stop_reason"] |
| curriculum_notes.rubric_consistency_reuse.all_current_outputs_individually_read | true |
| curriculum_notes.rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |

</details>
