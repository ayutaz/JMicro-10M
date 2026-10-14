# 教材・供給・品質・量 — 5/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition_source_learning_review.json — actual_both100M_all160_content_source128_complete</summary>

[原記録](../../reports/phase6/condition_source_learning_review.json) ／ SHA256: `8abb695a611c1c9f7437a48f260cd0da4e0c29ca5c4394c65de90e08d54ba38e` ／ 26,896 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_both100M_all160_content_source128_complete" |
| summaries.small512.BPB | 1.1332850242844945 |
| summaries.small512.rates.eos | 42 |
| summaries.small512.rates.repetition | 25 |
| summaries.small512.rates.unicode_failure | 0 |
| summaries.small512.rates.role_leak | 0 |
| summaries.small512.rates.empty | 0 |
| summaries.small512.grammar2 | 56 |
| summaries.small512.relevance2 | 59 |
| summaries.small512.coherent | 13 |
| summaries.small512.appropriate | 31 |
| summaries.small512.new_teacher_tokens | 100000000 |
| summaries.small512.source_teacher_tokens.web | 75000000 |
| summaries.small512.source_teacher_tokens.story | 5000000 |
| summaries.small512.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.small512.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.small512.conditional_source_documents | 512 |
| summaries.small512.notes_sha256 | "0d2445b55acddf98c485dca71d4d09c19a0ef1f36e19b1201b5f1706d0666c82" |
| summaries.small512.Base_adopted | false |
| summaries.large2048.BPB | 1.136865685906886 |
| summaries.large2048.rates.eos | 42 |
| summaries.large2048.rates.repetition | 20 |
| summaries.large2048.rates.unicode_failure | 0 |
| summaries.large2048.rates.role_leak | 0 |
| summaries.large2048.rates.empty | 0 |
| summaries.large2048.grammar2 | 62 |
| summaries.large2048.relevance2 | 74 |
| summaries.large2048.coherent | 12 |
| summaries.large2048.appropriate | 30 |
| summaries.large2048.new_teacher_tokens | 100000000 |
| summaries.large2048.source_teacher_tokens.web | 75000000 |
| summaries.large2048.source_teacher_tokens.story | 5000000 |
| summaries.large2048.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.large2048.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.large2048.conditional_source_documents | 2048 |
| summaries.large2048.notes_sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |
| summaries.large2048.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.small512.grammar_at_least56 | true |
| absolute_dev_screen.small512.coherence_at_least27 | false |
| absolute_dev_screen.small512.appropriate_at_least27 | true |
| absolute_dev_screen.small512.EOS_at_least37 | true |
| absolute_dev_screen.small512.repetition_at_most18 | false |
| absolute_dev_screen.small512.no_empty_role_unicode | true |
| absolute_dev_screen.large2048.grammar_at_least56 | true |
| absolute_dev_screen.large2048.coherence_at_least27 | false |
| absolute_dev_screen.large2048.appropriate_at_least27 | true |
| absolute_dev_screen.large2048.EOS_at_least37 | true |
| absolute_dev_screen.large2048.repetition_at_most18 | false |
| absolute_dev_screen.large2048.no_empty_role_unicode | true |
| original_Web.small512.EOS_at_least8_more | true |
| original_Web.small512.repetition_no_worse | true |
| original_Web.small512.no_empty_role_unicode | true |
| original_Web.small512.BPB_degradation_at_most1percent | false |
| original_Web.large2048.EOS_at_least8_more | true |
| original_Web.large2048.repetition_no_worse | true |
| original_Web.large2048.no_empty_role_unicode | true |
| original_Web.large2048.BPB_degradation_at_most1percent | false |
| learning25M_to100M.small512.checks.coherence_gain_at_least8 | false |
| learning25M_to100M.small512.checks.paired_CI_lower_above0 | false |
| learning25M_to100M.small512.checks.EOS_nonworsening | false |
| learning25M_to100M.small512.checks.repetition_nonworsening | true |
| learning25M_to100M.small512.checks.no_empty_role_unicode | true |
| learning25M_to100M.small512.checks.BPB_gate | true |
| learning25M_to100M.small512.checks.appropriate_completion_not_punctuation | true |
| learning25M_to100M.small512.passed | false |
| learning25M_to100M.large2048.checks.coherence_gain_at_least8 | false |
| learning25M_to100M.large2048.checks.paired_CI_lower_above0 | false |
| learning25M_to100M.large2048.checks.EOS_nonworsening | true |
| learning25M_to100M.large2048.checks.repetition_nonworsening | true |
| learning25M_to100M.large2048.checks.no_empty_role_unicode | true |
| learning25M_to100M.large2048.checks.BPB_gate | true |
| learning25M_to100M.large2048.checks.appropriate_completion_not_punctuation | true |
| learning25M_to100M.large2048.passed | false |
| learning_reference_note | "Same data/parent/nominal recipe with different teacher budgets; historical25M terminal masks differ, not guaranteed exact trajectory prefixes or independent quality replication." |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.7109375 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.both_source_matches | 67 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 48 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 81 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 0.7812211504222508 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6982758620689655 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 46 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.576345337949595 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 1.0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 64 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.7129205208315206 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.421875 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| source_rankings.small512.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.45256877369852344 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.6875 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.both_source_matches | 64 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 81 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1839415828794887 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6681034482758621 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 55 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 45 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1386758882201062 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.9921875 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 63 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 1 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.40091374583164896 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.3828125 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 1 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 47 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| source_rankings.small512.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.10721480551149201 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.671875 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 49 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 74 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 104 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.5281224570389303 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6551724137931034 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 41 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 70 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 93 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.4406658144585357 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.8046875 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 39 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 25 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.0682836635986792 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5390625 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 49 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 42 |
| source_rankings.small512.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.22405236461373257 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.67578125 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 52 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.12953186000167694 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6594827586206896 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 44 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 65 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 94 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1078362710896975 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.8203125 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 42 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 21 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.2334190955764469 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.53125 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 43 |
| source_rankings.small512.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.04552131665705755 |
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
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.90625 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.both_source_matches | 104 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 24 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 126 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 1.052006538414515 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.9051724137931034 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 94 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 22 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 114 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 1.013731539778425 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.921875 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 54 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.9947544513939663 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.890625 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 50 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 14 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.aggregate.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 1.1418362717135704 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.90234375 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.both_source_matches | 104 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 124 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.22674762186808117 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.9008620689655172 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 94 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 21 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 112 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.22493046222783997 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.90625 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 53 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.22492699577031253 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.8984375 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 51 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 13 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.aggregate.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.24178601122927187 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.74609375 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 66 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 116 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.6087951194612606 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.7370689655172413 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 55 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.5810864684854096 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.7578125 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 34 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 29 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.6314340865418551 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.734375 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 32 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| source_rankings.large2048.aggregate.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.5975226413142112 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.734375 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 63 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 62 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 116 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1307308527805075 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.728448275862069 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 56 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 57 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.12703871094364044 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.75 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 32 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 32 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.13797850108877846 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.71875 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 31 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| source_rankings.large2048.aggregate.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.12317623941879144 |
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
| eligible_for_final_Base_validation.small512 | false |
| eligible_for_final_Base_validation.large2048 | false |
| new_scientific_teacher_tokens | 200000000 |
| verification_teacher_tokens | 2599760 |
| GPU_seconds | 453.00058993601124 |
| verification_GPU_seconds | 21.030304796993732 |
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
<summary>reports/phase6/condition_source_learning_small512_notes.json — None</summary>

[原記録](../../reports/phase6/condition_source_learning_small512_notes.json) ／ SHA256: `0d2445b55acddf98c485dca71d4d09c19a0ef1f36e19b1201b5f1706d0666c82` ／ 17,299 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |

</details>

<details>
<summary>reports/phase6/condition_source_ranking_active_job.json — None</summary>

[原記録](../../reports/phase6/condition_source_ranking_active_job.json) ／ SHA256: `b25fb11df434a1b87c8685ae6fe877a5e787aaf1d9d8aa6f34f81c585a78bdb2` ／ 1,624 bytes

| 原キー | 保存値 |
|---|---|
| note | "Terminal complete with actual process absent; never restart. Original10B UI restored/identity/HTTP confirmed. GPU6.925s, optimizer/newteachers0; Base quality remains unmet. Next100M study is separately planned and not started." |
| Base_adopted | false |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 6.92455568301375 |
| job.GPU_budget_seconds | 60 |
| job.optimizer_updates | 0 |
| job.scientific_teacher_tokens | 0 |
| job.protected_test_used | false |
| completion | "reports/phase6/condition_source_ranking_completion.json" |

</details>

<details>
<summary>reports/phase6/condition_source_ranking_completion.json — actual3072_requests_fixed128_original_source_ranking_complete_Base_unmet</summary>

[原記録](../../reports/phase6/condition_source_ranking_completion.json) ／ SHA256: `1c3e9fd6af304219accfd696f7c885068a2f2f9f6f01fd7b042d468bfb670e6b` ／ 4,568 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual3072_requests_fixed128_original_source_ranking_complete_Base_unmet" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 6.92455568301375 |
| job.GPU_budget_seconds | 60 |
| job.optimizer_updates | 0 |
| job.scientific_teacher_tokens | 0 |
| job.protected_test_used | false |
| checks.parent2B.weights_unchanged | true |
| checks.parent2B.RNG_restored | true |
| checks.parent2B.no_gradients | true |
| checks.parent2B.eval_mode | true |
| checks.parent2B.first_request_batched_vs_single_max_NLL_difference | 0.03680562973022461 |
| checks.control512.weights_unchanged | true |
| checks.control512.RNG_restored | true |
| checks.control512.no_gradients | true |
| checks.control512.eval_mode | true |
| checks.control512.first_request_batched_vs_single_max_NLL_difference | 0.06184494495391846 |
| checks.large2048.weights_unchanged | true |
| checks.large2048.RNG_restored | true |
| checks.large2048.no_gradients | true |
| checks.large2048.eval_mode | true |
| checks.large2048.first_request_batched_vs_single_max_NLL_difference | 0.049349069595336914 |
| actual_GPU_seconds | 6.907170138001675 |
| actual_GPU_occupation_seconds | 6.92455568301375 |
| GPU_budget_seconds | 60 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| portable_text_bytes | 7074515 |
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

</details>

<details>
<summary>reports/phase6/condition_source_ranking_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_source_ranking_evidence_manifest.json) ／ SHA256: `921e509eed08bcad52eaf81dfdf6ef3463212e1ca0968a40fe6048246ab02e38` ／ 45,289 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 7074515 |
| archive.bytes | 1239660 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/condition_source_ranking_fit_analysis.json — actual_original_outcome_fit_and_source_exposure_reused</summary>

[原記録](../../reports/phase6/condition_source_ranking_fit_analysis.json) ／ SHA256: `1f0283bd5f2378f0bf7d404590bc99da43708db882804b7634da80439e9496e0` ／ 9,090 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_original_outcome_fit_and_source_exposure_reused" |
| groups.parent2B.original_history.all128.target_tokens | 4808 |
| groups.parent2B.original_history.all128.target_bytes | 21049 |
| groups.parent2B.original_history.all128.NLL_sum | 9601.601461775372 |
| groups.parent2B.original_history.all128.token_weighted_mean_NLL | 1.997005295710352 |
| groups.parent2B.original_history.all128.byte_weighted_mean_NLL | 0.45615475612976253 |
| groups.parent2B.original_history.nonweak116.target_tokens | 4283 |
| groups.parent2B.original_history.nonweak116.target_bytes | 18760 |
| groups.parent2B.original_history.nonweak116.NLL_sum | 8659.847857533417 |
| groups.parent2B.original_history.nonweak116.token_weighted_mean_NLL | 2.02191171084133 |
| groups.parent2B.original_history.nonweak116.byte_weighted_mean_NLL | 0.46161235914357235 |
| groups.parent2B.original_history.old512_fixed64.target_tokens | 2469 |
| groups.parent2B.original_history.old512_fixed64.target_bytes | 10619 |
| groups.parent2B.original_history.old512_fixed64.NLL_sum | 4784.432037736846 |
| groups.parent2B.original_history.old512_fixed64.token_weighted_mean_NLL | 1.9378015543689129 |
| groups.parent2B.original_history.old512_fixed64.byte_weighted_mean_NLL | 0.4505539163515252 |
| groups.parent2B.original_history.new1536_fixed64.target_tokens | 2339 |
| groups.parent2B.original_history.new1536_fixed64.target_bytes | 10430 |
| groups.parent2B.original_history.new1536_fixed64.NLL_sum | 4817.169424038526 |
| groups.parent2B.original_history.new1536_fixed64.token_weighted_mean_NLL | 2.059499539990819 |
| groups.parent2B.original_history.new1536_fixed64.byte_weighted_mean_NLL | 0.461857087635525 |
| groups.parent2B.isolated_condition.all128.target_tokens | 4808 |
| groups.parent2B.isolated_condition.all128.target_bytes | 21049 |
| groups.parent2B.isolated_condition.all128.NLL_sum | 10952.7603997397 |
| groups.parent2B.isolated_condition.all128.token_weighted_mean_NLL | 2.2780283693302206 |
| groups.parent2B.isolated_condition.all128.byte_weighted_mean_NLL | 0.5203458786517031 |
| groups.parent2B.isolated_condition.nonweak116.target_tokens | 4283 |
| groups.parent2B.isolated_condition.nonweak116.target_bytes | 18760 |
| groups.parent2B.isolated_condition.nonweak116.NLL_sum | 9877.44885770241 |
| groups.parent2B.isolated_condition.nonweak116.token_weighted_mean_NLL | 2.3061986592814403 |
| groups.parent2B.isolated_condition.nonweak116.byte_weighted_mean_NLL | 0.5265164636301924 |
| groups.parent2B.isolated_condition.old512_fixed64.target_tokens | 2469 |
| groups.parent2B.isolated_condition.old512_fixed64.target_bytes | 10619 |
| groups.parent2B.isolated_condition.old512_fixed64.NLL_sum | 5438.827116015873 |
| groups.parent2B.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 2.2028461385240474 |
| groups.parent2B.isolated_condition.old512_fixed64.byte_weighted_mean_NLL | 0.5121788413236532 |
| groups.parent2B.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| groups.parent2B.isolated_condition.new1536_fixed64.target_bytes | 10430 |
| groups.parent2B.isolated_condition.new1536_fixed64.NLL_sum | 5513.933283723827 |
| groups.parent2B.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 2.357389176453111 |
| groups.parent2B.isolated_condition.new1536_fixed64.byte_weighted_mean_NLL | 0.5286609092736172 |
| groups.control512.original_history.all128.target_tokens | 4808 |
| groups.control512.original_history.all128.target_bytes | 21049 |
| groups.control512.original_history.all128.NLL_sum | 6470.193862619083 |
| groups.control512.original_history.all128.token_weighted_mean_NLL | 1.3457141977161156 |
| groups.control512.original_history.all128.byte_weighted_mean_NLL | 0.30738723277205965 |
| groups.control512.original_history.nonweak116.target_tokens | 4283 |
| groups.control512.original_history.nonweak116.target_bytes | 18760 |
| groups.control512.original_history.nonweak116.NLL_sum | 5889.945110626463 |
| groups.control512.original_history.nonweak116.token_weighted_mean_NLL | 1.3751914804171055 |
| groups.control512.original_history.nonweak116.byte_weighted_mean_NLL | 0.3139629589886174 |
| groups.control512.original_history.old512_fixed64.target_tokens | 2469 |
| groups.control512.original_history.old512_fixed64.target_bytes | 10619 |
| groups.control512.original_history.old512_fixed64.NLL_sum | 1245.904858193744 |
| groups.control512.original_history.old512_fixed64.token_weighted_mean_NLL | 0.5046192216256558 |
| groups.control512.original_history.old512_fixed64.byte_weighted_mean_NLL | 0.11732788946169546 |
| groups.control512.original_history.new1536_fixed64.target_tokens | 2339 |
| groups.control512.original_history.new1536_fixed64.target_bytes | 10430 |
| groups.control512.original_history.new1536_fixed64.NLL_sum | 5224.289004425339 |
| groups.control512.original_history.new1536_fixed64.token_weighted_mean_NLL | 2.23355665003221 |
| groups.control512.original_history.new1536_fixed64.byte_weighted_mean_NLL | 0.5008906044511351 |
| groups.control512.isolated_condition.all128.target_tokens | 4808 |
| groups.control512.isolated_condition.all128.target_bytes | 21049 |
| groups.control512.isolated_condition.all128.NLL_sum | 9092.132624877451 |
| groups.control512.isolated_condition.all128.token_weighted_mean_NLL | 1.8910425592507178 |
| groups.control512.isolated_condition.all128.byte_weighted_mean_NLL | 0.43195081119661033 |
| groups.control512.isolated_condition.nonweak116.target_tokens | 4283 |
| groups.control512.isolated_condition.nonweak116.target_bytes | 18760 |
| groups.control512.isolated_condition.nonweak116.NLL_sum | 8228.181863171752 |
| groups.control512.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.9211258144225432 |
| groups.control512.isolated_condition.nonweak116.byte_weighted_mean_NLL | 0.43860244473196974 |
| groups.control512.isolated_condition.old512_fixed64.target_tokens | 2469 |
| groups.control512.isolated_condition.old512_fixed64.target_bytes | 10619 |
| groups.control512.isolated_condition.old512_fixed64.NLL_sum | 2957.1354123363108 |
| groups.control512.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 1.1977057158105755 |
| groups.control512.isolated_condition.old512_fixed64.byte_weighted_mean_NLL | 0.27847588401321316 |
| groups.control512.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| groups.control512.isolated_condition.new1536_fixed64.target_bytes | 10430 |
| groups.control512.isolated_condition.new1536_fixed64.NLL_sum | 6134.9972125411405 |
| groups.control512.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 2.622914584241616 |
| groups.control512.isolated_condition.new1536_fixed64.byte_weighted_mean_NLL | 0.5882068276645389 |
| groups.large2048.original_history.all128.target_tokens | 4808 |
| groups.large2048.original_history.all128.target_bytes | 21049 |
| groups.large2048.original_history.all128.NLL_sum | 7405.598574211555 |
| groups.large2048.original_history.all128.token_weighted_mean_NLL | 1.540265926416713 |
| groups.large2048.original_history.all128.byte_weighted_mean_NLL | 0.35182662236740725 |
| groups.large2048.original_history.nonweak116.target_tokens | 4283 |
| groups.large2048.original_history.nonweak116.target_bytes | 18760 |
| groups.large2048.original_history.nonweak116.NLL_sum | 6664.728659841636 |
| groups.large2048.original_history.nonweak116.token_weighted_mean_NLL | 1.55608887691843 |
| groups.large2048.original_history.nonweak116.byte_weighted_mean_NLL | 0.35526272173995926 |
| groups.large2048.original_history.old512_fixed64.target_tokens | 2469 |
| groups.large2048.original_history.old512_fixed64.target_bytes | 10619 |
| groups.large2048.original_history.old512_fixed64.NLL_sum | 3714.2601234061976 |
| groups.large2048.original_history.old512_fixed64.token_weighted_mean_NLL | 1.5043580896744422 |
| groups.large2048.original_history.old512_fixed64.byte_weighted_mean_NLL | 0.34977494334741477 |
| groups.large2048.original_history.new1536_fixed64.target_tokens | 2339 |
| groups.large2048.original_history.new1536_fixed64.target_bytes | 10430 |
| groups.large2048.original_history.new1536_fixed64.NLL_sum | 3691.3384508053578 |
| groups.large2048.original_history.new1536_fixed64.token_weighted_mean_NLL | 1.5781694958552193 |
| groups.large2048.original_history.new1536_fixed64.byte_weighted_mean_NLL | 0.3539154794636009 |
| groups.large2048.isolated_condition.all128.target_tokens | 4808 |
| groups.large2048.isolated_condition.all128.target_bytes | 21049 |
| groups.large2048.isolated_condition.all128.NLL_sum | 9140.913556609934 |
| groups.large2048.isolated_condition.all128.token_weighted_mean_NLL | 1.901188343720868 |
| groups.large2048.isolated_condition.all128.byte_weighted_mean_NLL | 0.4342683052216226 |
| groups.large2048.isolated_condition.nonweak116.target_tokens | 4283 |
| groups.large2048.isolated_condition.nonweak116.target_bytes | 18760 |
| groups.large2048.isolated_condition.nonweak116.NLL_sum | 8239.00285781536 |
| groups.large2048.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.9236523132886667 |
| groups.large2048.isolated_condition.nonweak116.byte_weighted_mean_NLL | 0.4391792568131855 |
| groups.large2048.isolated_condition.old512_fixed64.target_tokens | 2469 |
| groups.large2048.isolated_condition.old512_fixed64.target_bytes | 10619 |
| groups.large2048.isolated_condition.old512_fixed64.NLL_sum | 4541.669510551328 |
| groups.large2048.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 1.8394773230260544 |
| groups.large2048.isolated_condition.old512_fixed64.byte_weighted_mean_NLL | 0.42769276867419986 |
| groups.large2048.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| groups.large2048.isolated_condition.new1536_fixed64.target_bytes | 10430 |
| groups.large2048.isolated_condition.new1536_fixed64.NLL_sum | 4599.244046058606 |
| groups.large2048.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 1.9663292202046199 |
| groups.large2048.isolated_condition.new1536_fixed64.byte_weighted_mean_NLL | 0.44096299578701875 |
| exposure.control512.conditional_teacher_tokens | 2500000 |
| exposure.large2048.conditional_teacher_tokens | 2500000 |
| CPU_seconds | 0.2608455269946717 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Fixed selected train128 and original source-matching targets, not heldout quality, incompatible negatives, total corpus fit or causal proof of exposure insufficiency. Complete and isolated contexts have different histories; primary Base scoring/gates unchanged." |

</details>

<details>
<summary>reports/phase6/condition_source_ranking_review.json — actual_fixed128_source_ranking_all3072_requests_reviewed</summary>

[原記録](../../reports/phase6/condition_source_ranking_review.json) ／ SHA256: `19b4f669f081f5e40063afd2281783a8778ecbb57c0e604c3fb8b8ec076c9c44` ／ 27,903 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_fixed128_source_ranking_all3072_requests_reviewed" |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.families | 128 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.39453125 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.both_source_matches | 6 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 89 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 20 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | -0.46432823295447667 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.375 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 3 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 81 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 16 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | -0.48869514457500995 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.390625 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 4 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 42 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 12 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | -0.4957910392916062 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.3984375 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 2 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 47 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 8 |
| aggregate.parent2B.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.39895391741057323 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.36328125 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.both_source_matches | 6 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 81 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 18 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | -0.09792374948174296 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.34051724137931033 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 4 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 71 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 14 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | -0.10882601633547408 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.3671875 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 3 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 41 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 10 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | -0.10421613160315646 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.359375 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 40 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 8 |
| aggregate.parent2B.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.0938518624205434 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.56640625 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 22 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 101 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.08480717352904232 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.5646551724137931 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 19 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 93 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 75 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.07639658276082928 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.5703125 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 12 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 49 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 40 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.07789940341657675 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5625 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 52 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 45 |
| aggregate.parent2B.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.10132465784111977 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.55859375 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 22 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 99 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.01853484412937223 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.5560344827586207 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 20 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 89 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 73 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.016690000424702034 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.5625 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 12 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 48 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 39 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.015866548423907417 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5546875 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 51 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 43 |
| aggregate.parent2B.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.021927603292462655 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.families | 128 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.67578125 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.both_source_matches | 61 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 78 |
| aggregate.control512.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 0.34334522696191483 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6637931034482759 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 53 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 48 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 69 |
| aggregate.control512.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.25963181479525776 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.9296875 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 56 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 7 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| aggregate.control512.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.7936281841226969 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.421875 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 5 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 44 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 15 |
| aggregate.control512.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.5005344200500502 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.65625 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.both_source_matches | 58 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 52 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 77 |
| aggregate.control512.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.0908126295961239 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6379310344827587 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 50 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 48 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 67 |
| aggregate.control512.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.06746864681994508 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.9296875 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 55 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 9 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| aggregate.control512.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.19246134172419743 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.3828125 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 43 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 14 |
| aggregate.control512.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.10624647673463161 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.65625 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 44 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 80 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 104 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.30815716620262884 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6422413793103449 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 37 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 75 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 93 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.2917698770551882 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.78125 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 36 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 28 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 59 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.6307088374825051 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.53125 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 8 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 52 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 45 |
| aggregate.control512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.14468504320952136 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.6640625 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 44 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.07126612129229146 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6551724137931034 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 38 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 76 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 92 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.06581136871483982 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.7890625 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 37 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 27 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 59 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.13828708850017968 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5390625 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 7 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 55 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 44 |
| aggregate.control512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.029637452636163686 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.families | 128 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.4375 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.both_source_matches | 12 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 88 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 41 |
| aggregate.large2048.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | -0.2704968454546765 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.4267241379310345 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 9 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 81 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 34 |
| aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | -0.32745079513403286 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.421875 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 8 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 38 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 19 |
| aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | -0.2704968454546765 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.453125 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 4 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 50 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 22 |
| aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.24927798588359007 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.44921875 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.both_source_matches | 13 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 42 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | -0.05918249472301755 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.43103448275862066 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 9 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 82 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 35 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | -0.07293068193030627 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.4453125 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 10 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 37 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 21 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | -0.060834403225861505 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.453125 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 52 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 21 |
| aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.054450844137619345 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.58203125 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 27 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 95 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 94 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.15975499832826745 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.5818965517241379 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 24 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 87 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 83 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.13766184561687267 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.5859375 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 15 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 45 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 48 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.11708750162380754 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.578125 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 12 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 50 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 46 |
| aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.17991315593240542 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.5859375 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 27 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 96 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 95 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.032536766142733986 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.5775862068965517 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 23 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 88 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 84 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.0312392771106077 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.578125 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 14 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 46 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 48 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.025580743548818508 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.59375 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 13 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 50 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 47 |
| aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.040740175916408966 |
| checks.parent2B.weights_unchanged | true |
| checks.parent2B.RNG_restored | true |
| checks.parent2B.no_gradients | true |
| checks.parent2B.eval_mode | true |
| checks.parent2B.first_request_batched_vs_single_max_NLL_difference | 0.03680562973022461 |
| checks.control512.weights_unchanged | true |
| checks.control512.RNG_restored | true |
| checks.control512.no_gradients | true |
| checks.control512.eval_mode | true |
| checks.control512.first_request_batched_vs_single_max_NLL_difference | 0.06184494495391846 |
| checks.large2048.weights_unchanged | true |
| checks.large2048.RNG_restored | true |
| checks.large2048.no_gradients | true |
| checks.large2048.eval_mode | true |
| checks.large2048.first_request_batched_vs_single_max_NLL_difference | 0.049349069595336914 |
| GPU_seconds | 6.907170138001675 |
| GPU_occupation_seconds | 6.92455568301375 |
| joint_tokenization_differences | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| tokenization | "Unchanged raw prefix and outcome encoded separately so each candidate has common target IDs. Exact concatenated UTF8 bytes checked. joint_tokenization_equal recorded; not asserted to be original whole-document token segmentation." |
| limitations | "Labels identify which continuation occurs in the original source; neither alternative is certified impossible. Source-matching rank is not factual correctness or heldout Base quality. Isolated prefixes may remove necessary history; report this limitation rather than interpreting all differences as causal. Fixed previously selected train128, one learned seed; history removal is not a minimal causal intervention; source original matching is not incompatible-negative accuracy or fluent heldout generation." |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/condition_source_transfer_evidence_manifest.json) ／ SHA256: `3ce40a1f4d9d7f4a895595ffa14c867b40bdd02faf0e1d6d11310d93cd3ebaa1` ／ 11,354 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 24721903 |
| archive.bytes | 3401611 |
| model_checkpoint_tensors_included | false |
| raw_generator_and_prior_failure_preserved | true |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_preparation.json — complete_pending_fixed64_content</summary>

[原記録](../../reports/phase6/condition_source_transfer_preparation.json) ／ SHA256: `9ef58017856f77ec825b9bd2e9c5b936d6ab7646e745cdf931e672d843fbe4de` ／ 2,239 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_fixed64_content" |
| job.status | "complete_pending_fixed64_content" |
| job.CPU_limit_seconds | 240 |
| job.scientific_teacher_tokens | 0 |
| job.actual_GPU_seconds | 0 |
| job.protected_test_used | false |
| job.CPU_seconds | 0.275927627022611 |
| job.checks.local_exact_train_body_unique | true |
| job.checks.all24_train_structures | true |
| job.checks.lexical_entities_disjoint | true |
| job.checks.structural_template_ids_disjoint | true |
| job.checks.all128_probe_family_ids_disjoint | true |
| job.checks.probe_complete_bodies_absent_from_train | true |
| documents | 2048 |
| generated_body_tokens | 82127 |
| generated_body_bytes | 320314 |
| serialized_tokens | 86223 |
| source_transfer_requests_per_checkpoint | 512 |
| CPU_seconds | 0.275927627022611 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_preparation_completion.json — actual_curriculum_preparation_fixed64_and_common100M_teacher_audit_complete_GPU_not_started</summary>

[原記録](../../reports/phase6/condition_source_transfer_preparation_completion.json) ／ SHA256: `0157716c6409151bfb06bb6f4a6ed56846bb4fed2e49dc9b97961a6509381516` ／ 5,223 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_curriculum_preparation_fixed64_and_common100M_teacher_audit_complete_GPU_not_started" |
| documents | 2048 |
| paired_train_families | 1024 |
| generated_body_tokens | 82213 |
| generated_body_bytes | 321088 |
| serialized_tokens | 86309 |
| EOS_targets | 2048 |
| newly_prepared_original_corpus_tokens | 0 |
| new_local_serialized_tokens | 86309 |
| transfer_requests_per_checkpoint | 512 |
| v1_CPU_seconds | 0.275927627022611 |
| v2_CPU_seconds | 0.34430652399896644 |
| CPU_limit_each_seconds | 240 |
| common100M_teacher_audit_CPU_seconds | 6.371515109000029 |
| ordinary_teacher_checks.target_sha256 | true |
| ordinary_teacher_checks.teachers | true |
| ordinary_teacher_checks.EOS | true |
| ordinary_teacher_checks.body_bytes | true |
| v1_weak_documents | 2 |
| v1_unresolved_grammar_documents | 2 |
| v1_training_pool_accepted | false |
| v2_changed_train_documents | 86 |
| v2_weak_documents | 0 |
| v2_unresolved_grammar_documents | 0 |
| v2_training_pool_accepted | true |
| v1_tests.CPU_seconds | 0.9 |
| v1_tests.passed | 4 |
| v2_tests.CPU_seconds | 1.04 |
| v2_tests.passed | 5 |
| initial_test_failure | "A literal test assertion only accepted 加えた while the valid receiver template says 受け取った. Preserve original XML; corrected form-specific expected phrase, retaining all exact numeric outcome assertions." |
| portable_uncompressed_bytes | 24721903 |
| archive_bytes | 3401611 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| new_scientific_recipe_frozen | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| UI_HTTP.training_tokens | 10000007168 |
| UI_HTTP.update | 305176 |
| UI_HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| limitations | "Generated24 structures and1024 paired families are not2048 independent domains or newly downloaded public corpus.128 probes share generator rules, structural holds include changed numeric ranges/AND/OR; not independent natural-language generalization. Shorter data changesEOS density/length and lexical distribution as a bundled curriculum replacement; no unique causal claim." |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_proposal.json — defined_single_curriculum_replacement_not_implemented_not_prepared_not_frozen_not_started</summary>

[原記録](../../reports/phase6/condition_source_transfer_proposal.json) ／ SHA256: `190fe6b1d73febd476e13089783b866df22ac6f60f9712b5218b86f8fc2cbd21` ／ 9,913 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_single_curriculum_replacement_not_implemented_not_prepared_not_frozen_not_started" |
| pair_evidence.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition_source_learning_condition_pair_analysis.json" |
| pair_evidence.sha256 | "f0e491565562a2a84a1e266d39a011e77c23311b5665c3679f6ef398a3729f01" |
| prior_small_synthetic_limit | "Prior64-family conditional memorization and25M transfer did not qualify Base; do not repeat that fixed tiny curriculum or mistake rename recall for generalization. Require structural and lexical diversification and predeclared family-disjoint source transfer probes." |
| natural_control.checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| natural_control.checkpoint.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| natural_control.checkpoint.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| natural_control.checkpoint.binding.arm | "large2048" |
| natural_control.checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| natural_control.checkpoint.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| natural_control.checkpoint.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| natural_control.checkpoint.binding.teacher_goals.web | 75000000 |
| natural_control.checkpoint.binding.teacher_goals.story | 5000000 |
| natural_control.checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| natural_control.checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| natural_control.checkpoint.binding.optimizer_policy | "inherit" |
| natural_control.checkpoint.binding.peak_lr | 0.0002 |
| natural_control.checkpoint.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| natural_control.checkpoint.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| natural_control.checkpoint.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| natural_control.checkpoint.binding.outcome_weight | 1 |
| natural_control.checkpoint.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| natural_control.checkpoint.update | 65244 |
| natural_control.checkpoint.tokens | 2137915392 |
| natural_control.checkpoint.supervised_tokens | 2120000000 |
| natural_control.checkpoint.additional_supervised_tokens | 100000000 |
| natural_control.checkpoint.additional_input_tokens | 100859904 |
| natural_control.checkpoint.source_teachers.web | 75000000 |
| natural_control.checkpoint.source_teachers.story | 5000000 |
| natural_control.checkpoint.source_teachers.ordinary_textbook | 10000000 |
| natural_control.checkpoint.source_teachers.conditional_textbook | 10000000 |
| natural_control.checkpoint.source_eos.web | 656229 |
| natural_control.checkpoint.source_eos.story | 38240 |
| natural_control.checkpoint.source_eos.ordinary_textbook | 74183 |
| natural_control.checkpoint.source_eos.conditional_textbook | 70061 |
| natural_control.checkpoint.source_input_tokens.web | 75674624 |
| natural_control.checkpoint.source_input_tokens.story | 5039104 |
| natural_control.checkpoint.source_input_tokens.ordinary_textbook | 10075136 |
| natural_control.checkpoint.source_input_tokens.conditional_textbook | 10071040 |
| natural_control.checkpoint.source_focus_teachers.web | 0 |
| natural_control.checkpoint.source_focus_teachers.story | 0 |
| natural_control.checkpoint.source_focus_teachers.ordinary_textbook | 0 |
| natural_control.checkpoint.source_focus_teachers.conditional_textbook | 2620780 |
| natural_control.checkpoint.focus_teacher_tokens | 2620780 |
| natural_control.checkpoint.focus_token_digest | "8e2af3a7a69ecc6ea03b6f189587339877c5cf6d20031ae69100d24ffe4a7d85" |
| natural_control.checkpoint.weighted_teacher_mass | 100000000 |
| natural_control.checkpoint.outcome_weight | 1 |
| natural_control.checkpoint.training_seconds | 151.12010613348684 |
| natural_control.checkpoint.completed_at | "2026-10-06T02:43:40.425716Z" |
| natural_control.generation_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition_source_learning_large2048_notes.json" |
| natural_control.generation_notes.sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |
| natural_control.teachers | 100000000 |
| natural_control.documents | 2048 |
| curriculum.train_documents | 2048 |
| curriculum.CPU_preparation_limit_seconds | 240 |
| scientific_teacher_tokens_new | 100000000 |
| comparison_total_teacher_tokens | 200000000 |
| source_teacher_tokens_each.ordinary_textbook | 10000000 |
| source_teacher_tokens_each.conditional_textbook | 10000000 |
| source_teacher_tokens_each.web | 75000000 |
| source_teacher_tokens_each.story | 5000000 |
| loss | "Plain Base full body+EOS CE; outcome_weight1" |
| scope_note | "Replace conditional curriculum source only at the recipe level. Length, EOS density and target diversity will change together and must be measured; this tests curriculum replacement, not an isolated proof that one operator, EOS or length causes improvement." |
| GPU_ceiling_seconds | 900 |
| probe_ceiling_seconds | 120 |
| original_measured_100M_train_seconds | 151.12010613348684 |
| illustrative_science_estimate_seconds | 536.4561379735329 |
| budget_condition | "Illustrative estimate is not a measured frozen budget for shorter new data. Implement missing commands, CPU resume/state checks, then realCUDA continuous4vs2+2/timing/save/warmup and finitebatch; freeze science budget including all128 source transfer probes and fixeddev evaluations before starting." |
| completion_condition | "Accepted prepared data/fixed64, bounded realCUDA/save-resume/science100M, all80/source128/full fixeddev results and old natural100M comparison, original gates and actual job exit, portable evidence/restored UI/localcommit." |
| failure_boundary | "One curriculum replacement comparison only; no automatic200M/500M, weight or ratio sweep. If train and declared heldout-domain probes learn but originaldev remains poor, report distribution transfer limits and reassess the next one-factor design; do not claim10M impossible." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| new_prepared_tokens | 0 |
| new_scientific_teacher_tokens_already_run | 0 |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_v1_content_review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition_source_transfer_v1_content_review.json) ／ SHA256: `aa6401064c3cb2edb086947ba4dd8f1156d962f36ea455c78f52020ec4167ff1` ／ 24,561 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 2 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 2 |
| training_pool_accepted | false |
| notes_sha256 | "0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_v2_content_review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition_source_transfer_v2_content_review.json) ／ SHA256: `3fc35cf431b369f1504aac965d56f70fc52a0a937f50e20649ef9895f3b3c85f` ／ 24,684 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 0 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 0 |
| training_pool_accepted | true |
| notes_sha256 | "bcc942b95376275da658d3e7a9db977ed8cd8303665196e3a7fce82040af72d8" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition_source_transfer_v2_preparation.json — complete_pending_fixed64_content</summary>

[原記録](../../reports/phase6/condition_source_transfer_v2_preparation.json) ／ SHA256: `9fec44c086fcabc9264d98bd71a494b358a81a28e7941488ee26f8f68b61e26d` ／ 2,249 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_fixed64_content" |
| job.status | "complete_pending_fixed64_content" |
| job.CPU_limit_seconds | 240 |
| job.scientific_teacher_tokens | 0 |
| job.actual_GPU_seconds | 0 |
| job.protected_test_used | false |
| job.CPU_seconds | 0.34430652399896644 |
| job.checks.local_exact_train_body_unique | true |
| job.checks.all24_train_structures | true |
| job.checks.lexical_entities_disjoint | true |
| job.checks.structural_template_ids_disjoint | true |
| job.checks.all128_probe_family_ids_disjoint | true |
| job.checks.probe_complete_bodies_absent_from_train | true |
| documents | 2048 |
| generated_body_tokens | 82213 |
| generated_body_bytes | 321088 |
| serialized_tokens | 86309 |
| source_transfer_requests_per_checkpoint | 512 |
| CPU_seconds | 0.34430652399896644 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition_v2_source_notes.json — None</summary>

[原記録](../../reports/phase6/condition_v2_source_notes.json) ／ SHA256: `0da4bd64439ffa8ae8752bc70cf9a9566cf24b32c7bdb663288d3cb1dbb855e7` ／ 17,986 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/conditional-content-pilot-20261006/source-sample.json — None</summary>

[原記録](../../reports/phase6/conditional-content-pilot-20261006/source-sample.json) ／ SHA256: `9b6e4d04cf5062054b360b417ad36c98f50ea9d36902dcf6fb3cf09e41963f9f` ／ 241,751 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_preparation.json — actual_masked_CUDA_resume_timing_complete_science_frozen_unstarted</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_preparation.json) ／ SHA256: `f33b711b0bcce453ca7263fb8524b75dc0e868578e49425b4496d68254147be6` ／ 5,637 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_masked_CUDA_resume_timing_complete_science_frozen_unstarted" |
| actual_probe_job.status | "complete" |
| actual_probe_job.GPU_elapsed_seconds | 17.082726756983902 |
| actual_probe_job.completed_updates | 32 |
| resume_checks.version | true |
| resume_checks.spec | true |
| resume_checks.model_config | true |
| resume_checks.model | true |
| resume_checks.optimizer | true |
| resume_checks.scheduler | true |
| resume_checks.rng | true |
| resume_checks.sampler | true |
| resume_checks.update | true |
| resume_checks.tokens | true |
| resume_checks.supervised_tokens | true |
| resume_checks.body_bytes | true |
| resume_checks.token_digest | true |
| resume_checks.focus_token_digest | true |
| resume_checks.focus_teacher_tokens | true |
| resume_checks.weighted_teacher_mass | true |
| resume_checks.shard_manifest_sha256 | true |
| resume_checks.implementation_sha256 | true |
| resume_checks.study_implementation_sha256 | true |
| resume_checks.loss_implementation_sha256 | true |
| resume_checks.study_binding | true |
| resume_checks.pilot_binding | true |
| resume_checks.lineage | true |
| resume_checks.branch_updates | true |
| resume_checks.branch_tokens | true |
| resume_checks.history_lr | true |
| resume_checks.history_weighted_teacher_mass | true |
| resume_checks.history_outcome_weight | true |
| resume_checks.history_focus_token_digest | true |
| resume_checks.history_actual_source_routes | true |
| resume_checks.history_physical_input_tokens | true |
| resume_checks.history_removed_prefix_targets | true |
| resume_checks.history_source_focus_teachers | true |
| resume_checks.history_source_input_tokens | true |
| resume_checks.history_loss | true |
| resume_checks.history_valid_input_tokens | true |
| resume_checks.history_body_bytes_seen | true |
| resume_checks.history_source_eos | true |
| resume_checks.history_source_teachers | true |
| resume_checks.history_additional_teacher_tokens | true |
| resume_checks.history_reference_token_digest | true |
| resume_checks.history_actual_source_body_bytes | true |
| resume_checks.history_actual_source_teachers | true |
| resume_checks.history_gradient_norm | true |
| resume_checks.history_focus_teacher_tokens | true |
| resume_checks.history_actual_source_eos | true |
| resume_checks.history_supervised_tokens | true |
| resume_checks.history_tokens_seen | true |
| resume_checks.history_reference_suffix_teacher_tokens | true |
| resume_checks.history_source_body_bytes | true |
| resume_checks.history_update | true |
| resume_checks.history_token_digest | true |
| resume_checks.finite | true |
| resume_checks.no_reheat | true |
| resume_checks.transition_included | true |
| resume_checks.actual_conditional_mask_active | true |
| verification_optimizer_updates | 48 |
| verification_teacher_tokens | 653485 |
| verification_input_tokens | 1572864 |
| scientific_teacher_tokens | 0 |
| scientific_optimizer_updates | 0 |
| GPU_seconds | 17.082726756983902 |
| previous_related_GPU_seconds_preserved | 2858.847923864086 |
| related_GPU_seconds | 2875.93065062107 |
| CPU_preparation_seconds | 2.868701503990451 |
| remaining_updates | 318 |
| predicted_actual_masked_teachers | 1801392 |
| original_reference_suffix_teachers | 10159637 |
| remaining_physical_input_tokens | 10420224 |
| own_measured_timing.steady_step_seconds | 0.05191548449511174 |
| own_measured_timing.estimated_updates | 318 |
| own_measured_timing.warmup_seconds | 1.3690772049885709 |
| own_measured_timing.save_seconds | 0.5254408170003444 |
| own_measured_timing.estimated_training_seconds | 18.40364209143445 |
| estimated_science_GPU_seconds_with_margin | 223.92473471886478 |
| total_GPU_ceiling_seconds | 600 |
| matched_teacher_budget | false |
| initial_CPU_failure.xml.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional_prefix_mask_tests_initial_failure.xml" |
| initial_CPU_failure.xml.sha256 | "8697dc4fc87c25769fc09c5aaf2263dbc98f12058ea5e428ef9a5ddc8edebd69" |
| initial_CPU_failure.failures | 1 |
| initial_CPU_failure.reason | "Test fixture had no terminal padding; increased its test-only terminal batch to guarantee padding. Three tests then passed including zero-focus conditional EOS retention. No GPU before passes." |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_preparation_portable.json) ／ SHA256: `928c1e76608ebbeaf1329766656149b248c307fe5142f839788896133c94f315` ／ 3,511 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/conditional_prefix_mask_preparation.json.bytes | 5637 |
| files.configs/phase6/conditional_prefix_mask.json.bytes | 18078 |
| files.configs/phase6/conditional_prefix_mask_probe.json.bytes | 17454 |
| files.reports/phase6/conditional_prefix_mask_proposal.json.bytes | 6313 |
| files.reports/phase6/conditional_prefix_mask_reference_input.json.bytes | 416371 |
| files.scripts/record_conditional_prefix_mask_preparation.py.bytes | 7094 |
| files.scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.scripts/run_conditional_prefix_mask.py.bytes | 24674 |
| files.scripts/run_conditional_prefix_mask.ps1.bytes | 3109 |
| files.tests/test_conditional_prefix_mask.py.bytes | 5430 |
| files.tests/test_conditional_prefix_mask.py.sha256 | "6063bdac436aaea64860228e4c8af1945c93639ea8706758685688bf95158fd0" |
| files.reports/phase6/conditional_prefix_mask_tests.xml.bytes | 703 |
| files.reports/phase6/conditional_prefix_mask_tests.xml.sha256 | "3dd7ff7170b72e7e421c01daed7868fe60f374166b447908fc64b79be9b0f090" |
| files.reports/phase6/conditional_prefix_mask_tests_initial_failure.xml.bytes | 2467 |
| files.reports/phase6/conditional_prefix_mask_tests_initial_failure.xml.sha256 | "8697dc4fc87c25769fc09c5aaf2263dbc98f12058ea5e428ef9a5ddc8edebd69" |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/job.json.bytes | 542 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/result.json.bytes | 179337 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json.bytes | 268 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json.sha256 | "f59cf223dad31bd609b3fa583bccad26df932c065c769fd1776ce58d1398dba6" |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/result.json.bytes | 58834 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/metrics.jsonl.bytes | 82582 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json.bytes | 266 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json.sha256 | "f30b45ad19decd079082b1779bde955715a99d3e9fdaf3e6ef4f2fbe9c1cc36d" |
| raw_bytes | 839077 |

</details>

<details>
<summary>reports/phase6/context_outcome_ranking_input_preparation.json — actual_all1024_train_families_prepared_no_learning</summary>

[原記録](../../reports/phase6/context_outcome_ranking_input_preparation.json) ／ SHA256: `eb08669a40c056305e4651ebf7b3e3a9453c8c06c5e2bbe0fd9748ef113a484b` ／ 1,690 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_all1024_train_families_prepared_no_learning" |
| CPU_elapsed_seconds | 0.21555141601129435 |
| CPU_ceiling_seconds | 60 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_original_corpus_tokens | 0 |
| whole_joint_tokenization_equal_rows | 4096 |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/context_outcome_ranking_preparation.json — actual_CPU_inputs_and_three_loss_full_resume_complete_GPU_not_started</summary>

[原記録](../../reports/phase6/context_outcome_ranking_preparation.json) ／ SHA256: `9c1cadcc3a3cf4bbd5c147e2302bbe562122e406c8c1a58ccc8617757b2ef957` ／ 4,279 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU_inputs_and_three_loss_full_resume_complete_GPU_not_started" |
| source_sha256.tests/test_context_outcome_ranking.py | "0fe0a22929a78c5dfbb59ca7006df2a48443a6100ff88d7e94ab9c5cf9365850" |
| source_sha256.tests/test_context_outcome_ranking_trainer.py | "0daac24053a1388858bd02ce71ac371b7e63cac779ec713f7afea5e350ebb435" |
| CPU_tests.context_prior_analysis_tests.xml.evidence.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_prior_analysis_tests.xml" |
| CPU_tests.context_prior_analysis_tests.xml.evidence.sha256 | "7a6d82317413f433ff0ed841520a329b6a538fe9c27d99240fc8bebf592cb883" |
| CPU_tests.context_prior_analysis_tests.xml.tests | 2 |
| CPU_tests.context_prior_analysis_tests.xml.seconds | 1.32 |
| CPU_tests.context_prior_analysis_tests.xml.device | "CPU" |
| CPU_tests.context_prior_analysis_tests.xml.actual_GPU_training | false |
| CPU_tests.context_outcome_ranking_tests.xml.evidence.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_outcome_ranking_tests.xml" |
| CPU_tests.context_outcome_ranking_tests.xml.evidence.sha256 | "0930600134b5e92da03683d8d56ff295980296718014b0b152a88765ea73edf5" |
| CPU_tests.context_outcome_ranking_tests.xml.tests | 2 |
| CPU_tests.context_outcome_ranking_tests.xml.seconds | 0.883 |
| CPU_tests.context_outcome_ranking_tests.xml.device | "CPU" |
| CPU_tests.context_outcome_ranking_tests.xml.actual_GPU_training | false |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.evidence.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context_outcome_ranking_trainer_tests.xml" |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.evidence.sha256 | "e7a909c95f0259eb28bfa941ff761c322d7be6d3d6d01496a65e235151f89428" |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.tests | 1 |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.seconds | 2.202 |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.device | "CPU" |
| CPU_tests.context_outcome_ranking_trainer_tests.xml.actual_GPU_training | false |
| actual_maximum_input_tokens | 74 |
| new_original_corpus_tokens | 0 |
| CPU_input_preparation_seconds | 0.21555141601129435 |
| GPU_training_seconds | 0 |
| scientific_teacher_tokens | 0 |
| scientific_optimizer_updates | 0 |
| full_resume_CPU | "Actual tiny model/Adam/scheduler/RNG/main sampler/Web sampler/ranking sampler, all ledgers and digests: continuous4 equals2+2. One Adam update after all3 backward paths; control primary/reference inputs unchanged. This fixture does not qualify CUDA or10M quality." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_acquisition.json — raw_acquired_preparation_running</summary>

[原記録](../../reports/phase6/corpus_10b_acquisition.json) ／ SHA256: `4d79d26f8007e2afaa9c358ad5d1370e287ae78aaa2d5b06fd1fec96c353c0b2` ／ 594 bytes

| 原キー | 保存値 |
|---|---|
| status | "raw_acquired_preparation_running" |
| raw_bytes | 34578335182.0 |
| elapsed_seconds | 609.103981212 |
| requested_train_tokens | 10000000000 |
| prepared_train_tokens | null |
| training_started | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_audit_early_timing.json — measured_early_bands_full_audit_pending</summary>

[原記録](../../reports/phase6/corpus_10b_audit_early_timing.json) ／ SHA256: `2aa5ffcd303860819b39d7894e92cb0a27bb9f8e3469e4dae3abc91b5ad8f8a8` ／ 1,271 bytes

| 原キー | 保存値 |
|---|---|
| status | "measured_early_bands_full_audit_pending" |
| mean_band_and_transition_seconds | 366.3655600096663 |
| eta_limitations | ["Only early bands; group/candidate counts vary", "First timing includes transition from raw stage", "Token/index/membership/loader duration not measured"] |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_cached_audit_start.json — full_independent_cached_audit_running</summary>

[原記録](../../reports/phase6/corpus_10b_cached_audit_start.json) ／ SHA256: `a9fc8ca32f316a19efe7f8f39a0d789d5cc592e49e5056e5b276338c9b9e4a87` ／ 3,735 bytes

| 原キー | 保存値 |
|---|---|
| status | "full_independent_cached_audit_running" |
| job.status | "running" |
| job.prior_cumulative_seconds | 9975.722686174999 |
| retired_v3.status | "failed" |
| retired_v3.prior_cumulative_seconds | 680.553657957 |
| retired_v3.failure | "InterruptedError: Pipeline interrupted by signal2; preserve all checkpoints" |
| retired_v3.cumulative_seconds | 9975.722686174999 |
| handoff.status | "cached_audit_running" |
| handoff.prior_identity.status | "running" |
| handoff.prior_identity.prior_cumulative_seconds | 680.553657957 |
| full_audit_passed | false |
| actual_loader_checked | false |
| training_started | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_cost_probe.json — readonly_prefix_probe_complete</summary>

[原記録](../../reports/phase6/corpus_10b_cost_probe.json) ／ SHA256: `de7c81e951a2eabbb36c8101664bcfc7340a04daf850c0df6ff14b7cf7d2bc3a` ／ 601 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_prefix_probe_complete" |
| eligible_records | 2030242 |
| sort_seconds | 0.794282062999855 |
| candidate_pairs | 95870 |
| tested_pairs | 3000 |
| verified_tested_pairs | 7 |
| tested_pair_seconds | 0.17502870299995266 |
| elapsed_seconds | 4.486302260000002 |
| scope | "Committed prefix and first3000 ordered band0 pairs only; not full audit or random pair sample" |
| extrapolation_limit | "Candidate growth need not be linear; use as resource planning evidence only" |

</details>

<details>
<summary>reports/phase6/corpus_10b_dedup_complete.json — builder_dedup_complete_export_running</summary>

[原記録](../../reports/phase6/corpus_10b_dedup_complete.json) ／ SHA256: `b178f7a821efce4a8a7b037e9cffa4471c847e79a4adf2cef1e063c544852b56` ／ 2,752 bytes

| 原キー | 保存値 |
|---|---|
| status | "builder_dedup_complete_export_running" |
| dedup.verified_pairs | 707772 |
| dedup.count_scope | "Sum of within-band spanning verified links; not serial global link count" |
| parallel.status | "verified_components_built" |
| parallel.elapsed_seconds | 3808.7133201530005 |
| parallel.candidate_pairs | 185955238 |
| export_progress.splits.train.tokens | 3656609051 |
| export_progress.splits.train.documents | 7758100 |
| export_progress.splits.train.body_bytes | 14248612159 |
| export_progress.splits.dev.tokens | 202637982 |
| export_progress.splits.dev.documents | 430181 |
| export_progress.splits.dev.body_bytes | 789607807 |
| export_progress.splits.test.tokens | 203247408 |
| export_progress.splits.test.documents | 431751 |
| export_progress.splits.test.body_bytes | 791955019 |
| export_progress.seconds | 360.53741034799987 |
| job.status | "running" |
| job.prior_cumulative_seconds | 680.553657957 |

</details>

<details>
<summary>reports/phase6/corpus_10b_edges_audit_half.json — first_sixteen_serial_bands_passed_pending_full_audit</summary>

[原記録](../../reports/phase6/corpus_10b_edges_audit_half.json) ／ SHA256: `18642e5993fe119578f67d93059b5865a878e8f8e9240317e091d65442996c40` ／ 2,458 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_sixteen_serial_bands_passed_pending_full_audit" |
| first_sixteen_bands_and_transition_seconds | 4437.676946141999 |
| eta_scope | "Conditional edge-stage arithmetic only; later band candidate volumes differ; full token/membership/index audit and loader not included" |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_edges_audit_quarter.json — first_eight_serial_bands_passed_pending_full_audit</summary>

[原記録](../../reports/phase6/corpus_10b_edges_audit_quarter.json) ／ SHA256: `7173433ccca53eb476b9108c0cc1f0c021f18bc1910906ad6620b3c9e92c626e` ／ 1,640 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_eight_serial_bands_passed_pending_full_audit" |
| first_eight_bands_and_transition_seconds | 2344.359541592001 |
| eta_scope | "Conditional edge-stage arithmetic only; remaining band candidates vary; full token/membership/index audit and loader not included" |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_edges_audit_start.json — first_serial_edge_band_passed_pending_full_audit</summary>

[原記録](../../reports/phase6/corpus_10b_edges_audit_start.json) ／ SHA256: `4f2ebd6255c6998e2b78b1fbb6d6c8f9131884884018eaabf5feb645eecffadc` ／ 770 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_serial_edge_band_passed_pending_full_audit" |
| audit_progress_snapshot.seconds | 4041.9948947079993 |
| first_band_and_transition_seconds | 374.9102230869994 |
| scope | "Original independent serial near-candidate/Jaccard rebuild; first band completed; all32 bands and component/token comparisons still pending" |
| prior_cumulative_seconds | 9975.722686174999 |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_edges_audit_three_quarters.json — first_twenty_four_serial_bands_passed_pending_full_audit</summary>

[原記録](../../reports/phase6/corpus_10b_edges_audit_three_quarters.json) ／ SHA256: `ec5acc540f2abb4c973749bee3224739f90feb1f393ecedba4a6c2fd1667b49e` ／ 3,341 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_twenty_four_serial_bands_passed_pending_full_audit" |
| first_twenty_four_bands_and_transition_seconds | 7098.827559537998 |
| band23_seconds | 967.1556669370002 |
| eta_scope | "Conditional edge-stage arithmetic only; band23 actually took16minutes and remaining band volumes vary; all-token/membership/index audit and loader not included" |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_edges_audit_twenty_eight.json — first_twenty_eight_serial_bands_passed_pending_full_audit</summary>

[原記録](../../reports/phase6/corpus_10b_edges_audit_twenty_eight.json) ／ SHA256: `824ce0236afc36947d73d6a3bf98c2a684e20965312044b32324707cbc6c7d88` ／ 3,563 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_twenty_eight_serial_bands_passed_pending_full_audit" |
| largest_group_band27_seconds | 987.9681150760007 |
| full_audit_passed | false |
| actual_loader_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_eta_probe.json — readonly_prefix_probe_complete</summary>

[原記録](../../reports/phase6/corpus_10b_eta_probe.json) ／ SHA256: `e6705250e1dd40b19504d84155546228ea99b5206e14165c65ce3d0f399e62d6` ／ 1,672 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_prefix_probe_complete" |
| eligible_records | 12908957 |
| sort_seconds | 10.056163702000049 |
| candidate_pairs | 3722286 |
| tested_pairs | 3000 |
| verified_tested_pairs | 139 |
| tested_pair_seconds | 0.6979916259997481 |
| elapsed_seconds | 39.52968452899995 |
| scope | "Committed prefix and first3000 ordered band0 pairs only; not full audit or random pair sample" |
| extrapolation_limit | "Candidate growth need not be linear; use as resource planning evidence only" |
| estimated_remaining.limitation | "Full-corpus candidate/check ratio, token export speed and independent serial audit speed are not yet measured; total may exceed this range" |
| storage_snapshot.wsl_available_bytes | 798100324352 |
| storage_snapshot.windows_C_free_bytes | 2771564781568 |

</details>

<details>
<summary>reports/phase6/corpus_10b_feature_cache_integration.json — passed_all_candidate_scores_and_components</summary>

[原記録](../../reports/phase6/corpus_10b_feature_cache_integration.json) ／ SHA256: `4379d538c09e9dfc072aac0850239d89c2e956b9e1be8c87f2a7d5ee44dcfea6` ／ 1,795 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_all_candidate_scores_and_components" |
| large_group_adoption_minimum_speedup | 2.0 |
| large_group_gate_passed | true |
| adoption_gate_passed | true |
| runtime_budget_seconds | 180 |
| scope | "All pairs in all32bands of fixed real1M prefix; not full corpus audit or end-to-end ETA" |
| audit_fixture_integration.status | "passed" |
| audit_fixture_integration.same_checks_and_split_counts | true |
| audit_fixture_integration.decorator_restored_after_success_and_failure | true |
| audit_fixture_integration.full_suite_passed | 107 |
| audit_fixture_integration.full_suite_failures | 0 |
| audit_fixture_integration.full_suite_skipped | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_feature_cache_probe.json — passed_actual_group_sample_scores</summary>

[原記録](../../reports/phase6/corpus_10b_feature_cache_probe.json) ／ SHA256: `59d25daf72a8a06fd816dd964259b84128d1ac21277a0353e62b80bd3c0c7bdf` ／ 5,910 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_actual_group_sample_scores" |
| minimum_adoption_speedup | 2.0 |
| sampled_adoption_gate_passed | true |
| runtime_budget_seconds | 360 |
| elapsed_seconds | 82.94768754399956 |
| scope | "Fixed32920 actual pairs from each measured largest group plus bounded whole-group retention; not full pair or full corpus audit; full1M integration comparison required before adoption" |
| relevant_tests.command | "uv run --frozen --extra hub --extra data --extra ml --extra export pytest -q tests/test_feature_cache.py" |
| relevant_tests.passed | 2 |
| relevant_tests.scope | "Hot reuse and bounded eviction/oversize equivalence; full integration comparison remains pending" |

</details>

<details>
<summary>reports/phase6/corpus_10b_gpu_dedup_assessment.json — source_review_only_gpu_speed_unmeasured</summary>

[原記録](../../reports/phase6/corpus_10b_gpu_dedup_assessment.json) ／ SHA256: `be700d85a7ced3228a2895d4328b7137952ed732bf4aeacfdbf0d15d0dcae680` ／ 3,350 bytes

| 原キー | 保存値 |
|---|---|
| status | "source_review_only_gpu_speed_unmeasured" |
| current_implementation.largest_group_potential_pairs_before_component_skips | 25038426 |
| existing_measured_optimization.large_group_sample_speedups | [2.8360961725925997, 2.8992674981394613, 2.6756171550604497] |
| existing_measured_optimization.scope | "32920 fixed pairs per actual large group; not whole audit speed" |
| gpu_candidate_inference.approach | "Encode actual shingle strings with collision-free IDs per group, then batch set intersection/cardinality computations on GPU; preserve all candidates, original acceptance and component results" |
| gpu_candidate_inference.library_candidate | "cuGraph selected-pair Jaccard on a document/shingle graph, or a dedicated exact set-intersection kernel" |
| gpu_candidate_inference.limitations | "Python set objects and SQLite text loads do not become GPU operations automatically. Encoding, graph/array construction, transfers, VRAM batching and threshold precision need measurement and validation. No dependency compatibility or GPU speed benchmark has been performed." |
| gpu_candidate_inference.speedup_claim | null |
| decision | "Keep the healthy frozen audit running. Do not restart it for an unmeasured GPU replacement. Retain the candidate for a separate future bounded comparison." |
| future_comparison_conditions.scope | "Fixed actual large-group pairs plus the existing complete 1M/all32-band component comparison" |
| future_comparison_conditions.acceptance | "All candidate coverage, original threshold decisions and final component/duplicate representatives identical; measure CPU baseline and total wall time" |
| future_comparison_conditions.bounded_pair_probe_runtime_seconds | 180 |
| future_comparison_conditions.candidate_adoption_minimum_end_to_end_speedup | 2.0 |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_ingestion.json — ingestion_bindings_checked_dedup_running</summary>

[原記録](../../reports/phase6/corpus_10b_ingestion.json) ／ SHA256: `3f0a77decda4dc9542d000474ec10d2673a5839faaefc719ded325e9aba73b02` ／ 3,406 bytes

| 原キー | 保存値 |
|---|---|
| status | "ingestion_bindings_checked_dedup_running" |
| complete.bindings.code.src/jmicro/tokenizer.py | "a437038f3c403b3473e662092205d036a4b18a9d0e2d26d9737f2a460b2443d5" |
| complete.elapsed_seconds | 2691.384231676 |
| job.status | "running" |
| job.prior_cumulative_seconds | 680.553657957 |
| signature_bytes | 14954627072 |
| parallel_scope.records | 29208256 |
| parallel_scope.eligible_records | 28998779 |
| parallel_scope.ids_sha256 | "8d37aac375926c1f0ca0279f62aa81bb486be8245f149251c6fcba0ede059513" |
| parallel_scope.bands | 32 |
| scope | "Ingested files/rows/signature-size/process checks only; no full corpus dedup, tokens, audit or readiness claim" |

</details>

<details>
<summary>reports/phase6/corpus_10b_jaccard_probe.json — passed_all_candidate_scores_and_components</summary>

[原記録](../../reports/phase6/corpus_10b_jaccard_probe.json) ／ SHA256: `dceb164b89772b31cb80a57f0ab42f89f88532ccc73c2c6802710b91b8d11457` ／ 1,156 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_all_candidate_scores_and_components" |
| adoption_minimum_speedup | 1.5 |
| adoption_gate_passed | false |
| runtime_budget_seconds | 180 |
| scope | "All pairs in all32bands of fixed real1M prefix; not full corpus audit or end-to-end ETA" |
| decision | "Do not adopt: measured1.4677x is below the preset1.5x minimum. Live pipeline and independent audit remain unchanged." |

</details>

<details>
<summary>reports/phase6/corpus_10b_loader_ready.json — passed_actual_training_loader</summary>

[原記録](../../reports/phase6/corpus_10b_loader_ready.json) ／ SHA256: `8e4c74df75be2b8ffb796119a5e16ae2eeef70d6a26e09ebf62f1467458c962d` ／ 1,907 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_actual_training_loader" |
| target_train_tokens | 10000000000 |
| prepared_splits.train.tokens | 12225819077 |
| prepared_splits.train.documents | 25879667 |
| prepared_splits.train.body_bytes | 47525339486 |
| prepared_splits.train.stream_sha256 | "e7e76fe564965a612a8f126b490a63101cd5af999efaede26d14413f2a467b97" |
| prepared_splits.train.index_sha256 | "55eab1644d974ac8a4f1695301a8756048158a10ab71297b0ac3bc6637bcfd17" |
| prepared_splits.dev.tokens | 678132065 |
| prepared_splits.dev.documents | 1435451 |
| prepared_splits.dev.body_bytes | 2635935411 |
| prepared_splits.dev.stream_sha256 | "3ff6ecd6f3538fa8b57cdd7967c61026f26cfdc771b8eb3ff4bd55710b0fc17a" |
| prepared_splits.dev.index_sha256 | "7a421c7c437a36810bec714dc0d362ce9ba61393db37141a2207bb7fec408548" |
| prepared_splits.test.tokens | 679399996 |
| prepared_splits.test.documents | 1438276 |
| prepared_splits.test.body_bytes | 2641106123 |
| prepared_splits.test.stream_sha256 | "8f77e0761dea7898829440c6c810c1c825484a1629cde9d521ae232fd44d546b" |
| prepared_splits.test.index_sha256 | "bf1577b1885eeff66eb0a3d96c4cc9b2db66ce9f036d5c67768eef8135bab865" |
| validation_scope | "built_export_and_actual_train_loader" |
| full_independent_audit_passed | false |
| sampler_replay_exact | true |
| training_updates | 0 |
| test_usage | "none; train loader only" |
| elapsed_seconds | 49.14671259800161 |

</details>

<details>
<summary>reports/phase6/corpus_10b_parallel_probe.json — passed_exact_components_and_candidate_coverage</summary>

[原記録](../../reports/phase6/corpus_10b_parallel_probe.json) ／ SHA256: `58d677cbb1eb54312d6269cc76e327c74b10e0e505f56b8d5cb6708e26982c7a` ／ 467 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_exact_components_and_candidate_coverage" |
| reference_seconds | 30.004361300000028 |
| parallel_seconds | 9.135031848999915 |
| candidate_pairs | 524480 |
| runtime_budget_seconds | 480 |
| scope | "Fixed real1M prefix; every one of32bands and all1M parent representatives compared; not a full10B audit" |

</details>

<details>
<summary>reports/phase6/corpus_10b_pending_bands.json — readonly_pending_band_counts_complete</summary>

[原記録](../../reports/phase6/corpus_10b_pending_bands.json) ／ SHA256: `f2df6c5d7b52fdeefc551e78d6e01d9413b7a8cdca89212f390a3a0d3732cddf` ／ 1,130 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_pending_band_counts_complete" |
| eligible_records | 28998779 |
| elapsed_seconds | 68.44688856599987 |
| runtime_budget_seconds | 180 |
| scope | "Full actual signature equality candidate counts for bands pending at start only; not completed verification, token count or audit" |

</details>

<details>
<summary>reports/phase6/corpus_10b_preflight.json — implementation_verified_real_corpus_pending</summary>

[原記録](../../reports/phase6/corpus_10b_preflight.json) ／ SHA256: `ae4af67126e0dcf6dc1e7cb1ab66219f874ba80040c64764d493148d1ff130ab` ／ 2,374 bytes

| 原キー | 保存値 |
|---|---|
| status | "implementation_verified_real_corpus_pending" |
| source_sha256.docs/autonomous_status.md | "324534936d50082303c00653fc545dac46de7bdde9ece20e738c5caebaaeca78" |
| source_sha256.tests/test_large_corpus.py | "693b5ca50384ca41521c388bd5b816064886cec78de7453776453f8fa94adba4" |
| tests.skipped | 0 |
| tests.errors | 0 |
| tests.passed | 105 |
| tests.failures | 0 |
| target_train_tokens | 10000000000 |
| training_started | false |
| completion_claim | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_prior_bulk_preserved.json — passed_prior_bulk_preserved</summary>

[原記録](../../reports/phase6/corpus_10b_prior_bulk_preserved.json) ／ SHA256: `8e0cc4987df1ed69a87f115aa21c73af4f2b0a2eed0ceee6d8193ab834145677` ／ 9,468 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_prior_bulk_preserved" |
| evidence_bindings./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/repetition_diagnosis_review.json | "d197ebb6c62483f33bac5b426e3223f6ce77786e66391842934aceae96b98f67" |
| checker_sha256 | "ace063371788d065ca8128c00364c4121f3c9d028f66b73649d204621efec2ae" |
| files_checked | 37 |
| bytes_checked | 9058888985 |
| checkpoints_checked | 19 |
| elapsed_seconds | 6.535649559000376 |
| scope | "All scheduled stable/decay Base checkpoints, pilot checkpoint, both old shard manifests and all train/dev/test streams/indexes/token byte tables, protected expanded corpus and pinned T4K Tokenizer; byte preservation only" |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_prior_files_preserved.json — prior_windows_source_config_evaluation_reports_hash_checked</summary>

[原記録](../../reports/phase6/corpus_10b_prior_files_preserved.json) ／ SHA256: `9109790cec8ae6f79dd5ea3d65ad34b7b34e842fa5df01fecfe9f42577869f6c` ／ 592 bytes

| 原キー | 保存値 |
|---|---|
| status | "prior_windows_source_config_evaluation_reports_hash_checked" |
| checked_at_utc | "2026-10-03T14:00:37.4736455Z" |
| files_checked | 225 |
| passed | true |
| scope | "All225 files in the immutable pre-investigation baseline; bulk Linux corpus/shards/checkpoints are separate audit evidence" |

</details>

<details>
<summary>reports/phase6/corpus_10b_progress.json — real_ingestion_running_not_dataset_complete</summary>

[原記録](../../reports/phase6/corpus_10b_progress.json) ／ SHA256: `a0ada634e9e88f8f51348da1fe29f3bb122114ab6c970657362efa87b483d402` ／ 804 bytes

| 原キー | 保存値 |
|---|---|
| status | "real_ingestion_running_not_dataset_complete" |
| observed_progress.seconds | 198.49008887600007 |
| committed_checkpoint.records | 1322469 |
| committed_checkpoint.completed_file | "train-00004-of-00283.parquet" |
| committed_checkpoint.completed_at | "2026-10-03T11:27:50.483746Z" |
| wsl_free_bytes_approx | 859000000000 |

</details>

<details>
<summary>reports/phase6/corpus_10b_raw_audit_complete.json — all_raw_reconstructed_pending_edges_and_tokens</summary>

[原記録](../../reports/phase6/corpus_10b_raw_audit_complete.json) ／ SHA256: `ed6000f55ac96c3b80e32095e7d69aa42ed814f19e807a45c714b1612efb6010` ／ 1,450 bytes

| 原キー | 保存値 |
|---|---|
| status | "all_raw_reconstructed_pending_edges_and_tokens" |
| audit_progress_snapshot.seconds | 3667.084671621 |
| checks_passed_to_checkpoint | ["full_sqlite_integrity_check", "all_128_pinned_raw_hashes_and_sizes", "all_source_payload_filter_protection_fields", "all_record_signatures_recomputed", "all_exact_representatives_and_signature_eligibility"] |
| scope | "Frozen independent auditor checkpoint; all128 raw files and protected records compared; not full final audit" |
| full_audit_passed | false |
| training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_raw_audit_progress.json — initial_sqlite_check_passed_all_raw_reconstruction_running</summary>

[原記録](../../reports/phase6/corpus_10b_raw_audit_progress.json) ／ SHA256: `9b75f0755a9fff59ff931db377b35feafbd7288b801d5cbd813e060e47980067` ／ 1,533 bytes

| 原キー | 保存値 |
|---|---|
| status | "initial_sqlite_check_passed_all_raw_reconstruction_running" |
| job.status | "running" |
| job.prior_cumulative_seconds | 9975.722686174999 |
| audit_progress.seconds | 1647.9231901969997 |
| proof_scope | "Frozen auditor reached audit_raw checkpoint only after full SQLite integrity_check returned ok, all protected records and reported raw files passed complete source/filter/payload/signature comparisons" |
| full_corpus_audit_passed | false |
| actual_loader_checked | false |
| training_started | false |

</details>

<details>
<summary>reports/phase6/corpus_10b_ready_review.json — ready_under_user_requested_reduced_validation</summary>

[原記録](../../reports/phase6/corpus_10b_ready_review.json) ／ SHA256: `07a33810efea63f081121c5bb2f63c92246745e1f3558e237bbf27fed56ae9cc` ／ 3,771 bytes

| 原キー | 保存値 |
|---|---|
| status | "ready_under_user_requested_reduced_validation" |
| scope | "At least10B actual local train tokens; model training is a separately authorized follow-up" |
| prepared_splits.train.tokens | 12225819077 |
| prepared_splits.train.documents | 25879667 |
| prepared_splits.train.body_bytes | 47525339486 |
| prepared_splits.train.stream_sha256 | "e7e76fe564965a612a8f126b490a63101cd5af999efaede26d14413f2a467b97" |
| prepared_splits.train.index_sha256 | "55eab1644d974ac8a4f1695301a8756048158a10ab71297b0ac3bc6637bcfd17" |
| prepared_splits.dev.tokens | 678132065 |
| prepared_splits.dev.documents | 1435451 |
| prepared_splits.dev.body_bytes | 2635935411 |
| prepared_splits.dev.stream_sha256 | "3ff6ecd6f3538fa8b57cdd7967c61026f26cfdc771b8eb3ff4bd55710b0fc17a" |
| prepared_splits.dev.index_sha256 | "7a421c7c437a36810bec714dc0d362ce9ba61393db37141a2207bb7fec408548" |
| prepared_splits.test.tokens | 679399996 |
| prepared_splits.test.documents | 1438276 |
| prepared_splits.test.body_bytes | 2641106123 |
| prepared_splits.test.stream_sha256 | "8f77e0761dea7898829440c6c810c1c825484a1629cde9d521ae232fd44d546b" |
| prepared_splits.test.index_sha256 | "bf1577b1885eeff66eb0a3d96c4cc9b2db66ce9f036d5c67768eef8135bab865" |
| validation_scope | "built_export_and_actual_train_loader" |
| full_independent_audit_passed | false |
| builder_checks | "All32LSH bands built; all exported documents encoded/decoded and canonical hashes checked during export; split/protection rules unchanged" |
| independent_checks | "Full SQLite integrity and all128raw hashes/source/filter/payload/signatures reconstructed;29of32serial near bands completed before user-requested stop" |
| omitted_checks | "Remaining independent near reconstruction, all global representatives, and independent full corpus re-tokenization/accounting" |
| actual_loader.elapsed_seconds | 49.14671259800161 |
| actual_loader.sampler_replay_exact | true |
| actual_loader.status | "passed_actual_training_loader" |
| data_preparation_training_updates | 0 |

</details>

<details>
<summary>reports/phase6/corpus_10b_validation_policy.json — audit_stopped_by_user</summary>

[原記録](../../reports/phase6/corpus_10b_validation_policy.json) ／ SHA256: `3ab581d84d99e512064ef00f57c699ac5a6a10e015eb38f1c95d17b7e0c2d35f` ／ 943 bytes

| 原キー | 保存値 |
|---|---|
| status | "audit_stopped_by_user" |
| reason | "User requested reduced redundant validation and faster transition to training" |
| validation_scope | "built_export_and_actual_train_loader" |
| audit_progress_at_stop.seconds | 12666.492965845 |
| full_independent_audit_passed | false |
| skipped | "Remaining independent duplicate reconstruction and full serial re-tokenization; builder checks are retained" |

</details>

<details>
<summary>reports/phase6/corpus_audit.json — passed</summary>

[原記録](../../reports/phase6/corpus_audit.json) ／ SHA256: `c2438917afd00064e1e7bbbde309e6587ea276d09995195488e7a96da03203e2` ／ 1,613 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| dedup_edges.lsh_candidate_pairs | 1384688 |
| split_documents.train | 1604292 |
| split_documents.test | 89485 |
| split_documents.dev | 89416 |
| stream_tokens.train | 756087912 |
| stream_tokens.test | 42230751 |
| stream_tokens.dev | 42182766 |
| body_tokens.train | 752879328 |
| body_tokens.test | 42051781 |
| body_tokens.dev | 42003934 |
| body_bytes.train | 2946200160 |
| body_bytes.test | 164539509 |
| body_bytes.dev | 164344743 |
| full_round_trip_documents | 1783193 |
| all_checks.pinned_raw_sha256 | true |
| all_checks.source_and_terms_binding | true |
| all_checks.source_unchanged | true |
| all_checks.all_raw_record_reconstruction | true |
| all_checks.all_signatures_recomputed | true |
| all_checks.all_detected_near_and_url_edges_rebuilt | true |
| all_checks.cluster_split_disjoint | true |
| all_checks.normalized_exact_and_detected_near_dedup | true |
| all_checks.pilot_and_fixed_suite_cluster_exclusion | true |
| all_checks.corpus_full_membership_and_payload | true |
| all_checks.all_shard_tokens_indexes_and_roundtrips | true |
| all_checks.500m_unique_train_stream_tokens | true |
| elapsed_seconds | 846.862373723 |
| near_recall_limitation | "128 permutations / 32x4 bands / Unicode rolling5 avalanche32; true 5-gram Jaccard &gt;=0.85 verifies candidates. LSH recall is probabilistic." |
| test_usage | "structural_integrity_only; no model evaluation or selection" |

</details>

<details>
<summary>reports/phase6/corpus_manifest.json — built_not_audited</summary>

[原記録](../../reports/phase6/corpus_manifest.json) ／ SHA256: `196d602e0c926e79ff57302fc8b181304bbbeeef7a50b9af2161a5c02b04a971` ／ 3,480 bytes

| 原キー | 保存値 |
|---|---|
| status | "built_not_audited" |
| counts.lsh_candidate_pairs | 1384688 |
| split_documents.train | 1604292 |
| split_documents.test | 89485 |
| split_documents.dev | 89416 |
| splits.train.tokens | 756087912 |
| splits.train.documents | 1604292 |
| splits.train.body_bytes | 2946200160 |
| splits.dev.tokens | 42182766 |
| splits.dev.documents | 89416 |
| splits.dev.body_bytes | 164344743 |
| splits.test.tokens | 42230751 |
| splits.test.documents | 89485 |
| splits.test.body_bytes | 164539509 |
| splits.test.stream_sha256 | "0c2b16e029821940b7b337542b4124cada44c5359b3b569c8fefc26c9adcbbe5" |
| splits.test.index_sha256 | "1199ba509f1f1d83e4ae33905e515e9528cf7bd0fb93db81a733c58fd5419394" |
| elapsed_seconds | 652.7186187770001 |
| source_sha256.src/jmicro/tokenizer.py | "a437038f3c403b3473e662092205d036a4b18a9d0e2d26d9737f2a460b2443d5" |
| near_scope | "128 permutations / 32x4 bands / Unicode rolling5 avalanche32; true 5-gram Jaccard &gt;=0.85 verifies candidates. LSH recall is probabilistic." |

</details>

<details>
<summary>reports/phase6/dataset_expansion_annotations.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_annotations.json) ／ SHA256: `582cbd6ecb65594b9666d9dd0199f8dd26a23d89ef25b939dbace4dae61c74ef` ／ 35,268 bytes

| 原キー | 保存値 |
|---|---|
| limitations | "Single nonblind reviewer; no independent human review; no grading by regex" |

</details>

<details>
<summary>reports/phase6/dataset_expansion_categories.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_categories.json) ／ SHA256: `2cb6f3c41ebe4bffc1f34b95f796f04f0a57ddbd0be01b4788d06d8f5d5c97a3` ／ 3,011 bytes

| 原キー | 保存値 |
|---|---|
| categories.control.common_sense.coherence2 | 0 |
| categories.control.common_sense.relevance2 | 1 |
| categories.control.common_sense.appropriate_EOS | 0 |
| categories.control.conversation.coherence2 | 3 |
| categories.control.conversation.relevance2 | 3 |
| categories.control.conversation.appropriate_EOS | 3 |
| categories.control.daily.coherence2 | 3 |
| categories.control.daily.relevance2 | 3 |
| categories.control.daily.appropriate_EOS | 1 |
| categories.control.description.coherence2 | 0 |
| categories.control.description.relevance2 | 1 |
| categories.control.description.appropriate_EOS | 2 |
| categories.control.grammar.count | 8 |
| categories.control.grammar.coherence2 | 2 |
| categories.control.grammar.relevance2 | 3 |
| categories.control.grammar.appropriate_EOS | 2 |
| categories.control.local_context.coherence2 | 2 |
| categories.control.local_context.relevance2 | 2 |
| categories.control.local_context.appropriate_EOS | 0 |
| categories.control.numbers.coherence2 | 0 |
| categories.control.numbers.relevance2 | 0 |
| categories.control.numbers.appropriate_EOS | 1 |
| categories.control.proper_names.coherence2 | 1 |
| categories.control.proper_names.relevance2 | 4 |
| categories.control.proper_names.appropriate_EOS | 2 |
| categories.control.punctuation.coherence2 | 2 |
| categories.control.punctuation.relevance2 | 4 |
| categories.control.punctuation.appropriate_EOS | 4 |
| categories.control.short_story.coherence2 | 2 |
| categories.control.short_story.relevance2 | 2 |
| categories.control.short_story.appropriate_EOS | 5 |
| categories.refined.common_sense.coherence2 | 1 |
| categories.refined.common_sense.relevance2 | 4 |
| categories.refined.common_sense.appropriate_EOS | 2 |
| categories.refined.conversation.coherence2 | 1 |
| categories.refined.conversation.relevance2 | 1 |
| categories.refined.conversation.appropriate_EOS | 2 |
| categories.refined.daily.coherence2 | 0 |
| categories.refined.daily.relevance2 | 1 |
| categories.refined.daily.appropriate_EOS | 1 |
| categories.refined.description.coherence2 | 1 |
| categories.refined.description.relevance2 | 2 |
| categories.refined.description.appropriate_EOS | 1 |
| categories.refined.grammar.count | 8 |
| categories.refined.grammar.coherence2 | 1 |
| categories.refined.grammar.relevance2 | 4 |
| categories.refined.grammar.appropriate_EOS | 3 |
| categories.refined.local_context.coherence2 | 0 |
| categories.refined.local_context.relevance2 | 1 |
| categories.refined.local_context.appropriate_EOS | 1 |
| categories.refined.numbers.coherence2 | 0 |
| categories.refined.numbers.relevance2 | 0 |
| categories.refined.numbers.appropriate_EOS | 0 |
| categories.refined.proper_names.coherence2 | 3 |
| categories.refined.proper_names.relevance2 | 5 |
| categories.refined.proper_names.appropriate_EOS | 2 |
| categories.refined.punctuation.coherence2 | 1 |
| categories.refined.punctuation.relevance2 | 3 |
| categories.refined.punctuation.appropriate_EOS | 3 |
| categories.refined.short_story.coherence2 | 1 |
| categories.refined.short_story.relevance2 | 3 |
| categories.refined.short_story.appropriate_EOS | 4 |
| semantic_families.control.both_contexts_correct | 33 |
| semantic_families.refined.both_contexts_correct | 28 |
| note | "Descriptive categories only; not new acceptance gates." |

</details>

<details>
<summary>reports/phase6/dataset_expansion_completion.json — complete_requested_stages1_to3</summary>

[原記録](../../reports/phase6/dataset_expansion_completion.json) ／ SHA256: `10caf1feeed2808ac722f55fa87252cd87180e5e16be636d187c54fa84cb8540` ／ 3,337 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_requested_stages1_to3" |
| checks.stage1_actual_builder_complete_exited_within1800 | true |
| checks.stage1_actual200M_with140M_new_source | true |
| checks.stage1_train_only_whole_source_contract | true |
| checks.stage1_manifest_and_new_stream_hash | true |
| checks.stage1_complete40_individual_source_notes | true |
| checks.stage1_length_EOS_source_changes_frozen_disclosed | true |
| checks.stage2_actual_scientific_job_complete_exited | true |
| checks.stage2_two1B_scientific_and_verification_separate | true |
| checks.stage2_actual_CUDA_save_resume_exact | true |
| checks.stage2_actual_matching_routes_schedule_and_midpoints | true |
| checks.stage3_all_primary_evidence_checks_pass | true |
| checks.stage3_correct_applied_LR_reviewer_provenance | true |
| checks.stage3_LR_audit_real_scheduler_tests | true |
| checks.stage3_all160_individual_content_reviews | true |
| checks.stage3_Japanese192_331_1119_and_common256 | true |
| checks.stage3_ineligible_full_not_launched | true |
| checks.stage3_unchanged_gates_actual_judgment | true |
| checks.stage3_GPU_budget_scientific_scope_and_test_exclusion | true |
| checks.original10B_UI_actual_process_and_HTTP_restored | true |
| checks.final_results_report_saved | true |
| checked_at | "2026-10-05T08:39:58.109002Z" |
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
| scientific_tokens | 2000027648 |
| verification_tokens | 262144 |
| candidate_adopted | false |

</details>

<details>
<summary>reports/phase6/dataset_expansion_control_LR_review.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_control_LR_review.json) ／ SHA256: `3467b6db35124d8d4529922e439ca123f0e2bc9feb1182f8276a8825a652eb23` ／ 346 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| actual_updates | 30518 |
| checkpoint_sha256 | "fd10dc1b358327bdbd8d3d58118c2cb096fc53d02b036f070e453911edf2b82a" |
| checked_at | "2026-10-05T08:06:14.393965Z" |

</details>

<details>
<summary>reports/phase6/dataset_expansion_control_training.json — complete</summary>

[原記録](../../reports/phase6/dataset_expansion_control_training.json) ／ SHA256: `6c7ec9aa61d23e1bebd774d976134cfebf925a3cd7015dd38353fd6adda23594` ／ 398,389 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.tests/test_expanded_stories.py | "d70527997b5ff8c7b64563010052415a4c3e65d0a9eb2f663c5721f60f844aa3" |
| binding.source_sha256.tests/test_dataset_expansion_budget.py | "bf566b664b5c67737bdd536ea94f85dd54b09fbe1a9b9e61916a759f57021c56" |
| binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/dataset-expansion-1b-20261005/control/checkpoint-00335694.pt" |
| checkpoint_sha256 | "fd10dc1b358327bdbd8d3d58118c2cb096fc53d02b036f070e453911edf2b82a" |
| update | 335694 |
| tokens | 11000020992 |
| additional_input_tokens | 1000013824 |
| source_tokens.web | 800063488 |
| source_tokens.short | 199950336 |
| source_eos_teachers.web | 1693843 |
| source_eos_teachers.short | 2210250 |
| sampler.kind | "eos-pilot-mixture-v1" |
| sampler.position | 30518 |
| sampler.web.seed | 42 |
| sampler.web.epoch | 0 |
| sampler.web.position | 10546944 |
| sampler.web.context | 1024 |
| sampler.web.blocks | 11939276 |
| sampler.short.seed | 42 |
| sampler.short.epoch | 3 |
| sampler.short.position | 19590 |
| sampler.short.context | 1024 |
| sampler.short.blocks | 58558 |
| sampler.source_tokens.web | 800063488 |
| sampler.source_tokens.short | 199950336 |
| sampler.source_eos.web | 1693843 |
| sampler.source_eos.short | 2210250 |
| training_seconds | 1479.136023664003 |
| checkpoint_role | "result" |
| pool.short_updates | 6102 |
| schedule.parent_update | 305176 |
| schedule.stable_updates | 29000 |
| schedule.decay_updates | 1518 |

</details>

<details>
<summary>reports/phase6/dataset_expansion_data_ready.json — ready_pending_content_inspection</summary>

[原記録](../../reports/phase6/dataset_expansion_data_ready.json) ／ SHA256: `afd3906d8aad023c4784136fcdfe141d7823df8303eb30ac0b79dd242660d97b` ／ 11,640 bytes

| 原キー | 保存値 |
|---|---|
| status | "ready_pending_content_inspection" |
| binding.target_tokens | 200000000 |
| binding.budget_seconds | 1800 |
| binding.seed | 20261005 |
| binding.scope | "Retain all old whole stories; add distinct train translations, 32–512 body tokens,2–24 sentences,4gram repetition&lt;=0.15" |
| totals.tokens | 200000192 |
| totals.documents | 1161923 |
| totals.body_bytes | 822869721 |
| by_source.retained.tokens | 59963449 |
| by_source.retained.documents | 662857 |
| by_source.retained.body_bytes | 236846913 |
| by_source.translation.tokens | 140036743 |
| by_source.translation.documents | 499066 |
| by_source.translation.body_bytes | 586022808 |
| body_tokens_mean | 170.12861093204972 |
| old_body_tokens_mean | 88.46211928062915 |
| EOS_per_1000_tokens | 5.809609422774954 |
| old_EOS_per_1000_tokens | 11.05435079293054 |
| length_and_EOS_density_within5percent | false |
| whole_original_documents | true |
| copied_old_tokens | 59963449 |
| new_source_tokens | 140036743 |
| official_validation_test_acquired | false |
| seconds | 145.02082676101418 |

</details>

<details>
<summary>reports/phase6/dataset_expansion_data_review.json — inspected_accepted_for_bounded_comparison</summary>

[原記録](../../reports/phase6/dataset_expansion_data_review.json) ／ SHA256: `d428ebfa8b64a0d114769d2c9ae11eb62f880bf494350b58ff03a1e21d3ccdf7` ／ 13,418 bytes

| 原キー | 保存値 |
|---|---|
| status | "inspected_accepted_for_bounded_comparison" |
| accepted_for_experiment | true |
| samples_sha256 | "48a04f9ac0945cd5dca808eb28775a696bfb46e08697ddade2005f0ed88f5099" |
| comparison_interpretation | "Amount plus new source/length/EOS density, not amount-only; all old stories retained" |
| content_limit | "Nonblind Codex sample diagnosis. Weak causality, translation artifacts, fantasy and violent stories remain; not factual or child-safe certification. Whole-corpus independent overlap audit incomplete." |
| original_validation_test_used | false |
| checked_at | "2026-10-05T07:36:53.675410Z" |

</details>

<details>
<summary>reports/phase6/dataset_expansion_generation_control.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_generation_control.json) ／ SHA256: `380d77995dad4c2e74dd3b09197746219e729ae8bdefd025e7aabc0ad5ade231` ／ 113,830 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/dataset_expansion_generation_refined.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_generation_refined.json) ／ SHA256: `1c52a8dd00b208aeaf691da746a94249f0b417862f37b33c63334722367dee9a` ／ 115,238 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/dataset_expansion_judgment.json — None</summary>

[原記録](../../reports/phase6/dataset_expansion_judgment.json) ／ SHA256: `560d053cdc4c97218a507266dd2a43a45ba0301aef49492e5344dd0e45f43feb` ／ 1,575 bytes

| 原キー | 保存値 |
|---|---|
| candidate_adopted | false |
| failed_quality_gates | ["coherence_gain_at_least8", "paired_CI_lower_above0", "EOS_nonworsening"] |
| failed_practical_gates | ["coherence_at_least27", "appropriate_at_least27", "EOS_at_least37"] |
| interpretation | "Amount plus new translated-story source/length/EOS density; not a pure amount-only causal estimate" |
| limitations | ["Single training seed", "Codex nonblind diagnosis, no independent human blind review", "Repeated dev use; no protected test evaluation", "Main Web independent overlap audit incomplete", "Mixed synthetic source, length and EOS density; not amount-only causality"] |
| scientific_tokens | 2000027648 |
| verification_tokens | 262144 |
| protected_test_used | false |

</details>
