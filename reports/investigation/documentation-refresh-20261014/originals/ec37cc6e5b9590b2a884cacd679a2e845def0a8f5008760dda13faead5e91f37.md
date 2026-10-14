# 教材・供給・品質・量 — 3/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/review.json — actual_both100M_all160_content_source128_complete</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/review.json) ／ SHA256: `8abb695a611c1c9f7437a48f260cd0da4e0c29ca5c4394c65de90e08d54ba38e` ／ 26,896 bytes

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
<summary>reports/phase6/condition-source-learning-100m-20261006/small512-content-review.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/small512-content-review.json) ／ SHA256: `3c98bdf883d66e158dec2a89c016ceb23ee4b393e7fd4a22e1f52c75da0cb3cb` ／ 910 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.1332850242844945 |
| rates.eos | 42 |
| rates.repetition | 25 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 56 |
| relevance2 | 59 |
| coherent | 13 |
| appropriate | 31 |
| new_teacher_tokens | 100000000 |
| source_teacher_tokens.web | 75000000 |
| source_teacher_tokens.story | 5000000 |
| source_teacher_tokens.ordinary_textbook | 10000000 |
| source_teacher_tokens.conditional_textbook | 10000000 |
| conditional_source_documents | 512 |
| notes_sha256 | "0d2445b55acddf98c485dca71d4d09c19a0ef1f36e19b1201b5f1706d0666c82" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/small512/training/latest.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/small512/training/latest.json) ／ SHA256: `31bf74f511e5464baf584d8f3dd8a8a8c2ee4453f9fabbe759133511afb0d27b` ／ 285 bytes

| 原キー | 保存値 |
|---|---|
| update | 65244 |
| tokens_seen | 2137915392 |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0000.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0000.json) ／ SHA256: `0d0432e94feaee747e4da458fc90dd1c463a2fed938b16d5356523de6a43f229` ／ 19,041 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0016.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0016.json) ／ SHA256: `93ce4ab65030ca8138172ab712db8ce0e9175fae1ce2466ee6b9bde127d9d76e` ／ 12,417 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0032.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0032.json) ／ SHA256: `6137d9e90e095d37265134418598f2c38154af7e9f43a38b3a3269bf77bce6ac` ／ 15,247 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0048.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0048.json) ／ SHA256: `31067b76752c53f21672bc35c1670c272e0a97936147a400ee128a0c62f071fb` ／ 16,462 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0064.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0064.json) ／ SHA256: `5467e376b4b42e05ed26607c268d26c37ce52d9e30b7a45aa5024975ac85efe3` ／ 16,024 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0080.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0080.json) ／ SHA256: `0fac7b892d704927b603b3ed87cca9886fab53625770ed2223b52b899509089e` ／ 16,272 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0096.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0096.json) ／ SHA256: `9ee8482279d8d5429e3b02a34a0f4dc148ef6bc5f1f85681271d21626a6d4c28` ／ 20,100 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0112.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0112.json) ／ SHA256: `1e81fada92054fc000446296faed20f2d93b81d9835e3405346d9b2ebc127a18` ／ 16,983 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0128.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0128.json) ／ SHA256: `0ce346b419bef60d734fd35c348e97fc5830b2daaad7e56fb6a9fdb8e482b0c2` ／ 11,135 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0144.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0144.json) ／ SHA256: `03fd3297db9b01f87024c61380b17a4295b10dd0c1662fb74b3e75993c99a204` ／ 11,570 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0160.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0160.json) ／ SHA256: `c8ab7824d676fdc38ac70d70ed1be06d505822a09437ce882ec92e89ecf6091a` ／ 20,483 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0176.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0176.json) ／ SHA256: `ce58dda930cefa4a9851d8ee8c63ec836c6c0e9a7e0171f4d15857c5c5e98bed` ／ 19,035 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0192.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0192.json) ／ SHA256: `e01bb3eb4a36e0f85a0246b3b33826ca4b8eaa5757b80710d7c2878f6f7661ec` ／ 14,416 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0208.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0208.json) ／ SHA256: `fd7d2c174640029e8403a93c54e304d134419f71c63693e3841034f5c81754fd` ／ 12,599 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0224.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0224.json) ／ SHA256: `e4e77e1db1569e857673e7aeccbeb49edd743af0d35314fdfaf406966d8fd3c2` ／ 12,515 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0240.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0240.json) ／ SHA256: `0e86543d2b38f6eeeb61b758fe266fec8344dae3801f0c2b5282c6c795f0ff80` ／ 14,769 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0256.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0256.json) ／ SHA256: `e5d3039582681f947f11439ac1b5443436a00ebecfaf59949ca96f9e9bc1dc68` ／ 10,930 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0272.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0272.json) ／ SHA256: `513ee9ff4522a5de93d4fa33efeab7d8b883919c025c6caab602dcf242a6518b` ／ 23,876 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0288.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0288.json) ／ SHA256: `214a71c9622e6e0a0d6e7e62a85dd3ff9738ccefe4a29828c0273d34ce8e7b6b` ／ 19,233 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0304.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0304.json) ／ SHA256: `01430be76d1d0510dee5abc87b89ee9e9d6370bfc66908942f4e4996c9ece589` ／ 19,091 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0320.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0320.json) ／ SHA256: `d2d06266a900cf1d7cbf3a4e6829394ff29c335acc86c43744c127c861aae67b` ／ 17,086 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0336.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0336.json) ／ SHA256: `338ea40694fcc15506fb4bd7be5d9cf7e4830d45f7c000262f7ff742766c1ae5` ／ 12,105 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0352.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0352.json) ／ SHA256: `ea8de6a5dcdeb3d7be4588b9d099dd682452a56aed1106847bf8c06091e04858` ／ 25,870 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0368.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0368.json) ／ SHA256: `f83df7f8443fe1a93fe15caeaad81f3412cd256db86854be1ebf4280fa2f87d3` ／ 20,806 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0384.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0384.json) ／ SHA256: `529a1d5b729db46c32d5dcbf6b4db138504093175776cee1d0932d711b5b91a8` ／ 25,510 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0400.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0400.json) ／ SHA256: `e0bb05219571de2b6611c19e78dfb461766328f33df3a9f0cec86aead5332fb3` ／ 13,427 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0416.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0416.json) ／ SHA256: `87626e3b3cc8ead324406f6c0a727dc685c6e6b04273c61beba597250c68d948` ／ 11,088 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0432.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0432.json) ／ SHA256: `f4b1fbc2831261090c7d4b4b6b6d5c56bfb5c578a154390c7cdb55adc1767604` ／ 13,469 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0448.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0448.json) ／ SHA256: `1f1306699fbf8a1eaf6f0528809964475d979aadd28afb941ae418d60b7df928` ／ 15,733 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0464.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0464.json) ／ SHA256: `bdfbaa71eda785d0048e22595ddc513159d8bf4900896f0bf68b9cb5210bbe23` ／ 14,916 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0480.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0480.json) ／ SHA256: `d44ff3f5ded842cbf92cc801cee69faa75c838ebe743c8227d98feabeb278a8b` ／ 20,407 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0496.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0496.json) ／ SHA256: `278b745439ff141dcef3e039a546d74b2fe1c891555d81b687c6010ac8b135b2` ／ 20,087 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0512.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0512.json) ／ SHA256: `d41110ff89fff721493c930c324f0a526e5dc1d5175d05b39a89a9f7e92c727d` ／ 15,658 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0528.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0528.json) ／ SHA256: `611a38241ae0a0ed6c311234a379b685bd52eb9b6cb298323562ba495a5d2e39` ／ 14,933 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0544.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0544.json) ／ SHA256: `e0f2bbf00cb0e063329601946ade449b7cac83e3688689707dadeda85397508b` ／ 23,426 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0560.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0560.json) ／ SHA256: `36ca248f72f830b6e5904ffe8b7104946c5bf650008af4eac20f37321ef21376` ／ 14,673 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0576.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0576.json) ／ SHA256: `ed9e37f952ae4739e7c68e1d495b043f77f449f6ebf049aba66b60f74ddb016b` ／ 16,406 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0592.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0592.json) ／ SHA256: `676f2b8068508a32c4e954d734285849f3085be2559f355ffa9ec5c43e1ec22f` ／ 19,103 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0608.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0608.json) ／ SHA256: `fa47a863d4e1450fa4bee76386ee85d8417e4fa38f05bd91058b21275d04b306` ／ 15,557 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0624.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0624.json) ／ SHA256: `3ec77da859b7fbfc453684dd1d02ec1c556b587ea4ab54ea82295524c764166b` ／ 10,923 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0640.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0640.json) ／ SHA256: `c7edb01bcf5cd619db8567fdf9b17410bc034734767cb666dfd90591133b7c86` ／ 19,961 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0656.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0656.json) ／ SHA256: `b3222d9e2188005ef10ae7b9f3627280ffdebe0a508cad48138c9ddd4165aa89` ／ 18,586 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0672.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0672.json) ／ SHA256: `0fb9d54e689c561ca1fbcc8b218d34c0de500adfaf2ae3c625da6d37a14a172b` ／ 17,948 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0688.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0688.json) ／ SHA256: `c23078bbe5ba1a2f983cf17a8e74d4abed227302c29e288a9a493ebc69f3908e` ／ 10,964 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0704.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0704.json) ／ SHA256: `0040bee24e550657c7f9f3393860687632c06c299ffcc4eebcedee0b6e4572ae` ／ 14,634 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0720.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0720.json) ／ SHA256: `b3f139fb731a78e63de0ee3c9868b5eb29936f1bdfc1a84c6424db38a35075a9` ／ 22,650 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0736.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0736.json) ／ SHA256: `b76c981267b732ebbe01619f5e81d7871e5589773da800f28b22b6ccbd6119aa` ／ 11,924 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0752.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0752.json) ／ SHA256: `0ae56e94c3769068e448a48e4ffc475c6fa484abaf5163fe6a13d7a1541ffec0` ／ 13,758 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0768.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0768.json) ／ SHA256: `0a58c237eff7f4a8b618d12d8f1cec39783c9d80140059daf3b2eac8b8c10452` ／ 18,708 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0784.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0784.json) ／ SHA256: `c7b1a554fd8af2a14680a454b71d7c358efa038955439dfa05348909094255c2` ／ 12,255 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0800.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0800.json) ／ SHA256: `2a05791f0eecedc9928bc5c628d4ef1c6430e9b6f57544874ae9ebc7841fca61` ／ 15,804 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0816.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0816.json) ／ SHA256: `f09c5a2e6f9715d21b67db87693512c1b12f5a3b0d685d2cb921dd36d0bf5492` ／ 14,262 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0832.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0832.json) ／ SHA256: `bf0887322cf2f7b42bde78bc9655438846801b63cec19419c00efbf147b95f7c` ／ 21,662 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0848.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0848.json) ／ SHA256: `7680b208a8e43c34ff38121719db57418d6d6cb258c7b420830b3117a2704fb0` ／ 17,294 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0864.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0864.json) ／ SHA256: `465b43afdd2cc915a9eec6f8dc42396f9c64bfbf32b8333ade40a30d0070299c` ／ 16,876 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0880.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0880.json) ／ SHA256: `b493e2d7525d3a2cf6d408fb20e0279cb0f831c13fd78349607e2a74a5f891f6` ／ 12,899 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0896.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0896.json) ／ SHA256: `c073ca2613f93d7d4f02aa8d43b1ddb833320a3e7ab0d6de89ae5aea06a5704b` ／ 16,142 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0912.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0912.json) ／ SHA256: `0de24ae8f4358ba18225c72852ef193589e57d2a1dffbfb885a75996f0888354` ／ 16,510 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0928.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0928.json) ／ SHA256: `67430c1ce7d0024c19332dc6b8c698efe66ac104bdc19b4bac237a90e599237a` ／ 12,283 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0944.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0944.json) ／ SHA256: `73e66a5f2cb70275b5d82828a691113e8cb4e97ca3f3407de10621b22002b95c` ／ 10,319 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0960.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0960.json) ／ SHA256: `ccbdf86be4d9c34c92fc5297129bd05ee842834f1527f63a1e4c71bd2420c040` ／ 13,256 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0976.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0976.json) ／ SHA256: `25ff29ae2e5fa89f6527c3d32c7cb1a9e65373c8c0cbd70eb57fef08346efb74` ／ 17,523 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0992.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/0992.json) ／ SHA256: `587c2f68fc347dd66dc2509a3aea70d76debeff23fba4fb911daed05d8a0e2dd` ／ 18,713 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/1008.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/1008.json) ／ SHA256: `b1d0bc2369f6e1bc5f516017a4c8b8df359490b5b59c4de97ebaee42db74d9b9` ／ 14,928 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/result.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/large2048/result.json) ／ SHA256: `52ad3e6f61b8db5950b1caaa4fa4d3a3ab8dc349f0c74da8da656a392e1a20b6` ／ 454,547 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.90625 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.both_source_matches | 104 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 24 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.ties | 0 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 126 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 1.052006538414515 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.9051724137931034 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 94 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 22 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 114 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 1.013731539778425 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.921875 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 54 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.9947544513939663 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.890625 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 50 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 14 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 63 |
| summary.aggregate.large2048.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 1.1418362717135704 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.90234375 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.both_source_matches | 104 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 124 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.22674762186808117 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.9008620689655172 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 94 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 21 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 112 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.22493046222783997 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.90625 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 53 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 10 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 63 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.22492699577031253 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.8984375 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 51 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 13 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 61 |
| summary.aggregate.large2048.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.24178601122927187 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.74609375 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 66 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 116 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.6087951194612606 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.7370689655172413 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 55 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.5810864684854096 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.7578125 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 34 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 29 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 0.6314340865418551 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.734375 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 32 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| summary.aggregate.large2048.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.5975226413142112 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.734375 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 63 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 62 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 116 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1307308527805075 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.728448275862069 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 56 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 57 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 104 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.12703871094364044 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.75 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 32 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 32 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 61 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.13797850108877846 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.71875 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 31 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 30 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 55 |
| summary.aggregate.large2048.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.12317623941879144 |
| original_outcome_fit.original_history.all128.target_tokens | 4808 |
| original_outcome_fit.original_history.all128.NLL_sum | 3085.485443666836 |
| original_outcome_fit.original_history.all128.token_weighted_mean_NLL | 0.6417399009290424 |
| original_outcome_fit.original_history.nonweak116.target_tokens | 4283 |
| original_outcome_fit.original_history.nonweak116.NLL_sum | 2768.4378872357015 |
| original_outcome_fit.original_history.nonweak116.token_weighted_mean_NLL | 0.6463782132233719 |
| original_outcome_fit.original_history.old512_fixed64.target_tokens | 2469 |
| original_outcome_fit.original_history.old512_fixed64.NLL_sum | 1548.6724715106184 |
| original_outcome_fit.original_history.old512_fixed64.token_weighted_mean_NLL | 0.627246849538525 |
| original_outcome_fit.original_history.new1536_fixed64.target_tokens | 2339 |
| original_outcome_fit.original_history.new1536_fixed64.NLL_sum | 1536.8129721562177 |
| original_outcome_fit.original_history.new1536_fixed64.token_weighted_mean_NLL | 0.6570384660779041 |
| original_outcome_fit.isolated_condition.all128.target_tokens | 4808 |
| original_outcome_fit.isolated_condition.all128.NLL_sum | 7303.015933024732 |
| original_outcome_fit.isolated_condition.all128.token_weighted_mean_NLL | 1.5189301025425814 |
| original_outcome_fit.isolated_condition.nonweak116.target_tokens | 4283 |
| original_outcome_fit.isolated_condition.nonweak116.NLL_sum | 6565.750707237799 |
| original_outcome_fit.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.5329793852995095 |
| original_outcome_fit.isolated_condition.old512_fixed64.target_tokens | 2469 |
| original_outcome_fit.isolated_condition.old512_fixed64.NLL_sum | 3600.0964089256054 |
| original_outcome_fit.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 1.4581192421731897 |
| original_outcome_fit.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| original_outcome_fit.isolated_condition.new1536_fixed64.NLL_sum | 3702.9195240991257 |
| original_outcome_fit.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 1.5831207884134784 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| source_matching_is_not_certified_negative_accuracy | true |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0000.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0000.json) ／ SHA256: `7217f4f521c2f607a332c2b9c9c609903111c40c62230c6476152b4d41b72601` ／ 19,137 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0016.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0016.json) ／ SHA256: `7627b33311ff9f946894320ba7984bb413a1f1ad86d26b393084dd31a7b720c5` ／ 12,497 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0032.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0032.json) ／ SHA256: `4000d3f3e2bc634b9a26e16db4a0e5784b4ca50fdc9e5b0eafc1284b39d176c8` ／ 15,330 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0048.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0048.json) ／ SHA256: `a2c9447b7dc1203272853fe3aaeebac91b262319510691e819fca5a9d68a2921` ／ 16,530 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0064.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0064.json) ／ SHA256: `9dfdb9aefd1e2f5a319fccd1ceafde4db6a30d37c70db4b777542e013dd7f565` ／ 16,118 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0080.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0080.json) ／ SHA256: `72493471e817adafe3d033261e564b3a05e616707e67a5778221f7912ea2d7c2` ／ 16,359 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0096.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0096.json) ／ SHA256: `861ac7bd871f70a1ff262234e08d8977794802954afb623560637fc6f43d6835` ／ 20,264 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0112.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0112.json) ／ SHA256: `b2cfebd483ebc3fbbb3fabf9d9429396a14ffe4c7d56893ed45ed17cd6f281da` ／ 17,057 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0128.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0128.json) ／ SHA256: `e624c15ab4221688fc3188bd1f7015f991498192c5c1d5e4a3fc4a507a85d81b` ／ 11,196 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0144.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0144.json) ／ SHA256: `c2086f03e9900fb8f75fc91842a910d129f71717bc3b2943d033f72d063443c3` ／ 11,614 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0160.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0160.json) ／ SHA256: `62024dcfe72dda7ee25bc83cfdd163604126e68007947cf5828e9b78b1dca23b` ／ 20,614 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0176.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0176.json) ／ SHA256: `2a88a7a66fc79d0f0641f57a3e062bfb6a59f647d8a6012f437c0225e2c63b9c` ／ 19,199 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0192.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0192.json) ／ SHA256: `17215fe1b3868c116ff3dfb2eb1e21f4b7b1aece4c79e7dd263d5f22e87a74e8` ／ 14,497 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0208.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0208.json) ／ SHA256: `ff06f17015449fec0e128e3669fa87a90bcd973abc12cbd5001ed1f890d4c1b4` ／ 12,692 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0224.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0224.json) ／ SHA256: `e10abdbcd235d2c87340aaf51dc5f62ed29272cd9e04fe12ea394a894d7e7e5b` ／ 12,605 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0240.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0240.json) ／ SHA256: `91751cd081f0ea808cef3498b20e4f89b0326107416346d643a041a30db061fc` ／ 14,853 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0256.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0256.json) ／ SHA256: `4e167047cbf084f3b8dcff992d7a3da794c6dca255c90213f2037c9ed723ed65` ／ 10,946 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0272.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0272.json) ／ SHA256: `5b89d8a7a83dd435cc39f6e5943a0624536ace4cf915c30cb893bef1c2e33365` ／ 24,001 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0288.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0288.json) ／ SHA256: `66ffaee515188d725d24c7169b07424857cf1e7acfea5a65f4f6b41a6a93f4d3` ／ 19,343 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0304.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0304.json) ／ SHA256: `fcce4d6496f4e88013bd23166419b4256277b7a7011d412faf9c049dfb6f84e3` ／ 19,241 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0320.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0320.json) ／ SHA256: `108bf7ba56545e03b7cef174f599ed64de1bb0cb036899b890581827df7727dd` ／ 17,211 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0336.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0336.json) ／ SHA256: `cf29c646fd46759a5f19505deae3dbdff94cecfbc60a894f9d748c34f5a7299a` ／ 12,167 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0352.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0352.json) ／ SHA256: `789a772d3272ff721d6e2d5051fe19d075447c4126891f904c25dbb1f20287b0` ／ 26,103 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0368.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0368.json) ／ SHA256: `5cb8b523391736eaf073da529df0fd3f69e36cc69ebaa75d8b310f606d8a2d28` ／ 20,955 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0384.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0384.json) ／ SHA256: `ed31ce6d59b54be0a471144208342df91aa3d1918ef0e4166c289d5dc0f05b63` ／ 25,674 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0400.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0400.json) ／ SHA256: `eb858727228d2aded2107c5f0fe2f8717e67a0eeee716135d8688ad750a55c52` ／ 13,523 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0416.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0416.json) ／ SHA256: `6ba437df473505743a46f410b394a0c2bb98e4a231853230d6823ed07d68bdc1` ／ 11,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0432.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0432.json) ／ SHA256: `1e75e047fe09e2bd44555eec9ab96e868a87f71ebe129cb360612843754cd566` ／ 13,532 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0448.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0448.json) ／ SHA256: `7913a6860096a7718683835b577b30748714f317c67de1e7f11157f6ccad00c7` ／ 15,798 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0464.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0464.json) ／ SHA256: `cf9691d768b8f1102e2e0d6c9a9d7957f214caef9291b4a0ed75d313fc8e9d7c` ／ 15,020 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0480.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0480.json) ／ SHA256: `20ac07d79aac826f339d807d833296bd06bbb510e9a169931488c1592447befa` ／ 20,589 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0496.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0496.json) ／ SHA256: `025418f1f0d1e63bddf2ead7fd79198e574e1744933277d231bf28877c19d9e0` ／ 20,243 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0512.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0512.json) ／ SHA256: `c1ef31c2907f00cfe47042c7ce19578d04843855e12582450f08b740476f2a7a` ／ 15,604 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0528.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0528.json) ／ SHA256: `86c9cfe2817208f97db9014e22f3479d3890f1ce461e95d0bbe709205740450e` ／ 14,854 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0544.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0544.json) ／ SHA256: `b700c20da1cbbd5e77d7c94718ae394f7dec148b660c4d3bf07715021b87ee98` ／ 23,273 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0560.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0560.json) ／ SHA256: `ea540d7013ee06a94c8065e711a6c0ae8ea105cb21f9358f5085fbeb5d6522c5` ／ 14,601 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0576.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0576.json) ／ SHA256: `d63db4b353d6ecd68b6d5dea48ccfb9272ffd8d4095ea99c38591a340bd27115` ／ 16,329 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0592.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0592.json) ／ SHA256: `727aa6e0a9ba02b34fc470e28a187f8c955bf73857f18b73a3824379da757145` ／ 19,008 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0608.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0608.json) ／ SHA256: `4413d3cbb25319c44ad7df5925cb60972a784e20dc6f215d892d56b376276ca4` ／ 15,453 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0624.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0624.json) ／ SHA256: `71b5129c3b0d1276c7364893ad59e9ac09613be583410d8124b3401d5419f19a` ／ 10,901 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0640.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0640.json) ／ SHA256: `82f18fd844ebd5be910afa33d787d66aef456e377caa7b6ef8d425c6753fb9cd` ／ 19,836 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0656.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0656.json) ／ SHA256: `663acd13a27da197da16bda9788ebb1917b1e64dd9e74722ad9b3c1fda5cbeb5` ／ 18,461 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0672.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0672.json) ／ SHA256: `70aa757fd6267a45a7dc26db1c58a64c893ba42dacbe216f88b0939cede58b11` ／ 17,867 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0688.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0688.json) ／ SHA256: `d95553b71951f3790ef1ca07f560f0e675060833a789e4514ca8277e358f6d9e` ／ 10,950 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0704.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0704.json) ／ SHA256: `5d609953c7a965a8dd1fbd76159cc3a0c27f8b19b616e06d0bc876ea03dea4c9` ／ 14,535 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0720.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0720.json) ／ SHA256: `6c6ff52839df8b2f1a60e72b355642c1cc20d7e6bf631c56e9833e42650feef2` ／ 22,483 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0736.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0736.json) ／ SHA256: `7b6cb433285ffbd398d5daacec5caa7dd8952c06f35d41790a65597ef5e4796c` ／ 11,876 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0752.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0752.json) ／ SHA256: `1283544907effebc71695c150d2b8c7e663d1aa503518471f15f31b60ff02de8` ／ 13,709 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0768.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0768.json) ／ SHA256: `edf8331883efe7e56496936f5fdee1adb91199ce38e9906e3418489aab9a7062` ／ 18,617 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0784.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0784.json) ／ SHA256: `e31d7d8d079d296b1b130e74e4a0791ff13d2e08ed6cf44d3eb129bcafabffe2` ／ 12,221 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0800.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0800.json) ／ SHA256: `7ee70136baefafc00869b256e61ebe094cc47eeed1e433970bd5c69d23c5c8a5` ／ 15,751 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0816.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0816.json) ／ SHA256: `d5a8b82b163aedcbb9ec424882825c5a8f065eb0fbe469a91a9ff03fabf7b5fd` ／ 14,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0832.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0832.json) ／ SHA256: `b9a865edeb1b97261273d4716e27b35472959ba029fc24ad1cf181fc66358f59` ／ 21,577 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0848.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0848.json) ／ SHA256: `bdba793bd5ace3563ab5b379aaf18f5e5fd32439cb9c02f61b984c8d2464795c` ／ 17,198 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0864.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0864.json) ／ SHA256: `342b7d25b1c6950374d61cc81b385154504cd4377a3a4fee4d50d98927b8b2c5` ／ 16,813 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0880.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0880.json) ／ SHA256: `1e47783eeb54796d578b825e76fa1031ab5f85907665f403a7745676325a624c` ／ 12,857 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0896.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0896.json) ／ SHA256: `c00fb309ceebf4d9344e974dc58f6d92852f06786042aec4573e41fa2004574d` ／ 16,095 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0912.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0912.json) ／ SHA256: `e858593fa7988da425d1e4f6ccf1be3d2fb4bf87fc530c36ad7e434d7729ef31` ／ 16,409 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0928.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0928.json) ／ SHA256: `91f282dd07b0b64c8b1e5d0571e552cdc5fc3c9ca936bcf7ae59ebd37267ea6b` ／ 12,260 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0944.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0944.json) ／ SHA256: `a89981a65b808054ad415f9d4140c180f1be5d6ba45919fa0947a66c80907847` ／ 10,259 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0960.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0960.json) ／ SHA256: `d798e1aefe506c8a688503ea17f0d7b8df20f008cda4471dbc4ca121fb349b9d` ／ 13,233 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0976.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0976.json) ／ SHA256: `c7b28cf0cf1bcea071b9a466b994e37af765e07e117c27008edf56d1ba81cdb4` ／ 17,469 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0992.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/0992.json) ／ SHA256: `6e55e2ab32ef3e1a61ca09e196745c7fbdd563b2a53d4f5914f61d5d49301fb0` ／ 18,637 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/1008.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/1008.json) ／ SHA256: `80607cfec987833efba61652444b9df45109e4368b88890d0309b603521ac8ba` ／ 14,880 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |

</details>

<details>
<summary>reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/result.json — None</summary>

[原記録](../../reports/phase6/condition-source-learning-100m-20261006/source-ranking/small512/result.json) ／ SHA256: `8b0457baa36f0e135067490aa7d2d6ce57a6c2961da598c46c708bcf02f23d46` ／ 453,734 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.source_matching_fraction | 0.7109375 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.both_source_matches | 67 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.same_unique_candidate | 48 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.ties | 0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.aligned_context_margin_shift | 81 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.all128.median_context_margin_shift | 0.7812211504222508 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6982758620689655 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.both_source_matches | 58 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.same_unique_candidate | 46 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.576345337949595 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 1.0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.both_source_matches | 64 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.7129205208315206 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.421875 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 3 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| summary.aggregate.small512.original_history.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.45256877369852344 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.source_matching_fraction | 0.6875 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.both_source_matches | 64 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.ties | 0 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 81 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.1839415828794887 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6681034482758621 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.both_source_matches | 55 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 45 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 72 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1386758882201062 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.9921875 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 63 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 1 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 64 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.40091374583164896 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.3828125 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 1 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 47 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 17 |
| summary.aggregate.small512.original_history.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | -0.10721480551149201 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.source_matching_fraction | 0.671875 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.both_source_matches | 49 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.same_unique_candidate | 74 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.aligned_context_margin_shift | 104 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.all128.median_context_margin_shift | 0.5281224570389303 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.source_matching_fraction | 0.6551724137931034 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.both_source_matches | 41 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.same_unique_candidate | 70 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.aligned_context_margin_shift | 93 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.nonweak116.median_context_margin_shift | 0.4406658144585357 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.source_matching_fraction | 0.8046875 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.both_source_matches | 39 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.same_unique_candidate | 25 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.old512_fixed64.median_context_margin_shift | 1.0682836635986792 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.source_matching_fraction | 0.5390625 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.same_unique_candidate | 49 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 42 |
| summary.aggregate.small512.isolated_condition.mean_token_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.22405236461373257 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.source_matching_fraction | 0.67578125 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.both_source_matches | 52 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.all128.median_context_margin_shift | 0.12953186000167694 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.families | 116 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.source_matching_fraction | 0.6594827586206896 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.both_source_matches | 44 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.same_unique_candidate | 65 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.aligned_context_margin_shift | 94 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.nonweak116.median_context_margin_shift | 0.1078362710896975 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.families | 64 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.source_matching_fraction | 0.8203125 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.both_source_matches | 42 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.same_unique_candidate | 21 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.aligned_context_margin_shift | 62 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.old512_fixed64.median_context_margin_shift | 0.2334190955764469 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.families | 64 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.source_matching_fraction | 0.53125 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.both_source_matches | 10 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.same_unique_candidate | 48 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.ties | 0 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.aligned_context_margin_shift | 43 |
| summary.aggregate.small512.isolated_condition.mean_byte_log_likelihood.new1536_fixed64.median_context_margin_shift | 0.04552131665705755 |
| original_outcome_fit.original_history.all128.target_tokens | 4808 |
| original_outcome_fit.original_history.all128.NLL_sum | 6169.855127367961 |
| original_outcome_fit.original_history.all128.token_weighted_mean_NLL | 1.2832477386372632 |
| original_outcome_fit.original_history.nonweak116.target_tokens | 4283 |
| original_outcome_fit.original_history.nonweak116.NLL_sum | 5648.484704847636 |
| original_outcome_fit.original_history.nonweak116.token_weighted_mean_NLL | 1.3188150139732981 |
| original_outcome_fit.original_history.old512_fixed64.target_tokens | 2469 |
| original_outcome_fit.original_history.old512_fixed64.NLL_sum | 334.486156263677 |
| original_outcome_fit.original_history.old512_fixed64.token_weighted_mean_NLL | 0.13547434437572986 |
| original_outcome_fit.original_history.new1536_fixed64.target_tokens | 2339 |
| original_outcome_fit.original_history.new1536_fixed64.NLL_sum | 5835.368971104284 |
| original_outcome_fit.original_history.new1536_fixed64.token_weighted_mean_NLL | 2.4948135831997797 |
| original_outcome_fit.isolated_condition.all128.target_tokens | 4808 |
| original_outcome_fit.isolated_condition.all128.NLL_sum | 8915.968635378154 |
| original_outcome_fit.isolated_condition.all128.token_weighted_mean_NLL | 1.8544027943798158 |
| original_outcome_fit.isolated_condition.nonweak116.target_tokens | 4283 |
| original_outcome_fit.isolated_condition.nonweak116.NLL_sum | 8079.045232942879 |
| original_outcome_fit.isolated_condition.nonweak116.token_weighted_mean_NLL | 1.8863052143224093 |
| original_outcome_fit.isolated_condition.old512_fixed64.target_tokens | 2469 |
| original_outcome_fit.isolated_condition.old512_fixed64.NLL_sum | 2194.8510636424767 |
| original_outcome_fit.isolated_condition.old512_fixed64.token_weighted_mean_NLL | 0.8889635737717605 |
| original_outcome_fit.isolated_condition.new1536_fixed64.target_tokens | 2339 |
| original_outcome_fit.isolated_condition.new1536_fixed64.NLL_sum | 6721.117571735678 |
| original_outcome_fit.isolated_condition.new1536_fixed64.token_weighted_mean_NLL | 2.873500458202513 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| source_matching_is_not_certified_negative_accuracy | true |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/fit-analysis.json — actual_original_outcome_fit_and_source_exposure_reused</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/fit-analysis.json) ／ SHA256: `1f0283bd5f2378f0bf7d404590bc99da43708db882804b7634da80439e9496e0` ／ 9,090 bytes

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
<summary>reports/phase6/condition-source-ranking-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/job.json) ／ SHA256: `563a998e0b84ae387d62a93dfc1d4af11f51308772447b11a766d5d5909faec4` ／ 673 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 6.92455568301375 |
| GPU_budget_seconds | 60 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0000.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0000.json) ／ SHA256: `0aaf1facc8beea84bf3ab54c5236b552a36c7d2017facdd4246ca38c50687b06` ／ 19,055 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0016.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0016.json) ／ SHA256: `02217010be6cd217ac464efa7f553a27243f4e59f8da556fb1325fe2f80795c3` ／ 12,397 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0032.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0032.json) ／ SHA256: `609edeac6b3cdae93599f8b201b7acbca0e353260f2dd25319fff9091f0d8d0d` ／ 15,251 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0048.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0048.json) ／ SHA256: `28b940a43eb5fec7ef22ac2057bef35e5da9ef5ebec9027d5c701bba667eacb0` ／ 16,463 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0064.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0064.json) ／ SHA256: `7993c15060b3b378a8af5cd116af503b684ec883e6ee4d3430fceb79c8efd195` ／ 16,014 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0080.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0080.json) ／ SHA256: `c822ca9ce96e43e8368b1199e86bc58dae4187b72d7f1bb2d1fa818c9c9c9848` ／ 16,279 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0096.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0096.json) ／ SHA256: `eb71a829e483699565833a9159da2defb24b5f81b2607c0f1411cb626c4d9569` ／ 20,092 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0112.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0112.json) ／ SHA256: `887d738d39b79ee476280909f50359afcc2f5f39bcf7607b7dd54634d19c0f11` ／ 16,987 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0128.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0128.json) ／ SHA256: `3b16355cdbe2812ea55eab3c9bd9b182bc848809ba4e5bae8a58c8b93a91dc89` ／ 11,127 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0144.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0144.json) ／ SHA256: `0b891f2516dd245cbcbc14586675ff7a57c18a1c3f8fa2cd64d57e2bddde35ae` ／ 11,566 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0160.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0160.json) ／ SHA256: `2a1c0fbf385db40e9af1de875894754373992b13457a877e4e7f52edf06e290d` ／ 20,503 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0176.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0176.json) ／ SHA256: `7cff2b6e179bc4a24676ee3d3a60ed3c2c1628b7b24254f0e0ad5ad0ec87e7b8` ／ 19,053 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0192.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0192.json) ／ SHA256: `ecc0a995b5f8e702494ac4dc43fed0b7beb33db31e1195cd86a59b866e0621d8` ／ 14,419 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0208.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0208.json) ／ SHA256: `05bd9b83e65a51d4897d965dd40d381d3148c379eead78d32219f4ccf8217880` ／ 12,614 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0224.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0224.json) ／ SHA256: `3e63b870a6b36d2ca2a2fbaed78a34fe58b642c4ba1dc274c8213b5b987feacd` ／ 12,525 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0240.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0240.json) ／ SHA256: `f6172b8e26a2c7c4461d6cf1b5f7b51ec7d04108c8bd428354ba3e2377c99598` ／ 14,766 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0256.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0256.json) ／ SHA256: `a7c55ce285a7ffd5e6b8a8f6581d79ca5fc8febceee5847db4305c4fbfeb11dc` ／ 10,930 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0272.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0272.json) ／ SHA256: `cfe59046e1579aaeb362be3e0e3fe9ed93c272a00d3cde0d83b4e1b8d6d63c8b` ／ 23,891 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0288.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0288.json) ／ SHA256: `c2feb8066e94372c3bb9f004a0e26dce904be362d0d235a309018dc4aea78066` ／ 19,230 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0304.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0304.json) ／ SHA256: `e9cf4a54acb186fd88564a15da5e3173b0332e9f8ede23303f10e14ec2d95979` ／ 19,119 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0320.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0320.json) ／ SHA256: `53512289ae949f7f0861f4f94307bd0f93cd56ae504781e81ed16f47ac6d02ed` ／ 17,072 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0336.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0336.json) ／ SHA256: `ae92ecd3c8deccb666d5331d1eb3954316e1092619a80d6af43fc3278a0f41b3` ／ 12,090 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0352.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0352.json) ／ SHA256: `5799c722f5a606a71926d1d2e345c0f7b968bfd2e3d4587b13678de0887d78e6` ／ 25,889 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0368.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0368.json) ／ SHA256: `416ade61a5663e4dbf83d3a71b4cdd918a8eb4e8d7565c92ce092db961a438ee` ／ 20,812 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0384.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0384.json) ／ SHA256: `59906366f18b7562d7867cda36e8723f31a67f2c070281e83c7f6d554c3650dd` ／ 25,509 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0400.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0400.json) ／ SHA256: `10c677b76ad4b822877c27d3fd77ead826b3ca33000918efb25c4098c5248a12` ／ 13,458 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0416.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0416.json) ／ SHA256: `8092ac2928daa35d0ae125168432448606a147caa95cb14e962c3d022fcb1b60` ／ 11,067 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0432.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0432.json) ／ SHA256: `924c654e89871c097ecdbf47ecf806a9bd74063cc11b975d1323f5f4c73b1b5b` ／ 13,463 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0448.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0448.json) ／ SHA256: `805a6c0e90774a79ec279fda9daebaec41c40cfb0c448f1947d5c6efb4eda2a7` ／ 15,711 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0464.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0464.json) ／ SHA256: `01082144c35ed2694e7f234fbc2eecffec8f27faff520490569dbc11f4afd455` ／ 14,961 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0480.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0480.json) ／ SHA256: `a862656109fcc58fb4196f27fab92b0cd7a16adbb502048b61dfc8151df40230` ／ 20,410 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0496.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0496.json) ／ SHA256: `211320144ebf244fa57721e028e1efd9cb957ef67ec8bafdd9125f28c20e0ae3` ／ 20,129 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0512.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0512.json) ／ SHA256: `f51eff8550699b32ce4a775c2979269e701465ce9574f5337efda3cce65bdcd2` ／ 15,575 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0528.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0528.json) ／ SHA256: `48a255d783d317d645d3a6196110c85b6eda912992e3ee5701d03d3f1f295af9` ／ 14,812 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0544.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0544.json) ／ SHA256: `950869ff5aa7b7728dce4592d5c07054c892d714f9e6b32d9f35fb51bd3f5479` ／ 23,243 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0560.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0560.json) ／ SHA256: `ef1b609f8e8ab788709a5d8a4e7b9c3be5e2a55c7283a5e2f3ab1a827365570c` ／ 14,597 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0576.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0576.json) ／ SHA256: `2c0b7d1edca3c15dc854f3a7fe632cdffefcf2a9b49a78714273a2172e878038` ／ 16,297 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0592.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0592.json) ／ SHA256: `175b3df1b84138647098fe92a1eb8a642fcfce2aaa23b536db7dd05cdef01928` ／ 19,004 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0608.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0608.json) ／ SHA256: `d09da8828b00309ef5b738c53f98c41d968f8f010403bc1e411f8c9b5d76964f` ／ 15,456 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0624.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0624.json) ／ SHA256: `d1fab1c9680a8a48af2cca3e848993066f3655ce20e93cf6e4a915666a7c182f` ／ 10,880 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0640.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0640.json) ／ SHA256: `e8940cc7dcb38262bffeef4c01669db2615dee61b92a694c54279c4f6dc827e2` ／ 19,811 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0656.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0656.json) ／ SHA256: `ae7bed7ce6b709540cd60cd90636c49511fe305be9d71834bbd010d97a7ff250` ／ 18,477 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0672.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0672.json) ／ SHA256: `da18dc9e83b8665c01b4f402ecf69ec7f0c5228a1db9d8f5fd2a169d8e636154` ／ 17,826 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0688.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0688.json) ／ SHA256: `92ee061f3b555d3055b199cf014c5cbe396ddf6373a3ac2d35bb20b067b49733` ／ 10,941 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0704.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0704.json) ／ SHA256: `88e1231f136b5a70e6ef848ed8c3d0f196bcb9afc85cb5755aff41eb31c8a1e4` ／ 14,526 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0720.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0720.json) ／ SHA256: `4c3b6ef704308f8384809bc2c2bc102efb079601457ae02adf5230d4bfab2902` ／ 22,450 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0736.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0736.json) ／ SHA256: `b9568cc518a3f0184994a80cb8f57e95820963bd6737c16efb7ea95e6cf46c27` ／ 11,870 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0752.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0752.json) ／ SHA256: `9778de567c5116aa1376daed4b4cdc633e708bdf1c1fa9fffd2da5710ce0bad0` ／ 13,677 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0768.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0768.json) ／ SHA256: `25d370c98828207936ea381ab6dbb193ae011d31ae9a77eaa07d82dbd6ff0de7` ／ 18,609 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0784.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0784.json) ／ SHA256: `c204d35c73f61c888c636402652b9efdf6ab89d961aef713c41d264908a5ad38` ／ 12,222 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0800.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0800.json) ／ SHA256: `aec38671edc5a0c2e793c7eaa6b0cfcb914f11b7bc9cea3a557ed55d387a9432` ／ 15,724 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0816.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0816.json) ／ SHA256: `e2e121143bd255c859fc5b3a62d756fda2137817d448aed6cb3daebe7c1d54c2` ／ 14,188 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0832.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0832.json) ／ SHA256: `a6da6865e8fd4190edd59b0279e12061a3c0da7dae13e35591c882964f4f5a9b` ／ 21,574 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0848.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0848.json) ／ SHA256: `5ff0cb640c5c325f0bbd47ea09eeceb9ef8ea0d94a2040bbf3050ed726f6f322` ／ 17,185 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0864.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0864.json) ／ SHA256: `564d3c6e24a6e63471786100a4258788c752529bcc95e27d860a77c002759fa7` ／ 16,772 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0880.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0880.json) ／ SHA256: `9a20e876fd306f4f3f3de74b5ba83a8de4aa49a4951dfa52ab92a4236aeac985` ／ 12,814 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0896.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0896.json) ／ SHA256: `b8137044caf4204d670102e6d063b9bafbd9ab64d6e7c7bb55de0680d01570dc` ／ 16,086 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0912.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0912.json) ／ SHA256: `1b0293372af61a08df377f577d0223e932a3c7ae6d89ae7425b220fcb2125e02` ／ 16,407 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0928.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0928.json) ／ SHA256: `e132c8c3506fe10dff4c206979192069f00ce689bd841ba4deaea0b4def25c6c` ／ 12,246 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0944.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0944.json) ／ SHA256: `ec5fbfee430061146fc5bae08275ac0162f7c7de10f8606d3dd9ead18338ec74` ／ 10,261 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0960.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0960.json) ／ SHA256: `dc6b74b4cfb7a087771200e58e14623696c187ae840993b73a8eaa959b5cdf1f` ／ 13,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0976.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0976.json) ／ SHA256: `af3028903c1373bd09254f2cc7eafc5fa1846e09ac806b21d6276e695ad41ced` ／ 17,422 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/0992.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/0992.json) ／ SHA256: `e4cdfb539933c00188337ddac9286d2cd1760d9f8c6c6eb64c0596f7352af95f` ／ 18,613 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/control512/1008.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/control512/1008.json) ／ SHA256: `ee781103bc4a6d739a7080fa4d36d814c0716d0472b5327bf4bf1ab702624dd6` ／ 14,885 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0000.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0000.json) ／ SHA256: `5da2728af6797112d17a3860eaad8d3d22bb01ecadb53dcd49e755d184e2eb9e` ／ 18,947 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0016.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0016.json) ／ SHA256: `acceeb9bea4a925e0cd980dc37fdf6d125fcbcc1fe372e50e493ef05b61a38d0` ／ 12,361 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0032.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0032.json) ／ SHA256: `1e6d73742e4ef15d5b20d9a41456d9bf2c465d34f52556172a98231d78c4ab5c` ／ 15,197 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0048.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0048.json) ／ SHA256: `3478d80ad11e2450b5145a6f01af4752eaa261cf9ebe83501a9d3d2a414d3734` ／ 16,378 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0064.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0064.json) ／ SHA256: `c1745f80056f57e0e087a1b906f241e3377c9b56685be7ed87ce18935fe75eaa` ／ 15,929 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0080.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0080.json) ／ SHA256: `c88edf7a8019987ec3f846b432e282f33d209ca84bedbc9613ca6ae2211f7e2e` ／ 16,154 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0096.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0096.json) ／ SHA256: `95dd91d3a6e0285dec6b34d2e25c6534b505d45b01a2984e0ce453fc9f0e45e5` ／ 20,008 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0112.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0112.json) ／ SHA256: `54c7c5a812fc49328a5bd1b1d44972e984567010eab7e16adb88abe5d11973b0` ／ 16,884 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0128.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0128.json) ／ SHA256: `263302be693316734ae9879705d58820af057696c3e0cb5ed7731c7f996e31cc` ／ 11,078 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0144.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0144.json) ／ SHA256: `407457ed040086697f4ee6cc683145f7887f5fb55de11bdb411acd24ad88c2cd` ／ 11,533 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0160.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0160.json) ／ SHA256: `4a3ed2c2ef03b0a9d82ae90c7caa49db67a8755f8b7351b322e8c90a6427409a` ／ 20,373 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0176.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0176.json) ／ SHA256: `a274ab5ebabc154a50937f2fa22eb5a68be831d0728df6eede42fd28a790772c` ／ 18,921 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0192.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0192.json) ／ SHA256: `a7e0848ec715494fb0cf76cde7931baafa2bce91fa565d4e5eacb63316e5e6de` ／ 14,323 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0208.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0208.json) ／ SHA256: `72b50d42b653c4dddf842e9862b415a2fa53e82c977bdf109ce70aa801087dac` ／ 12,553 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0224.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0224.json) ／ SHA256: `16c62cbd872df34d92cb33cbc840c7058c82489cd7496949044f8d07eeebe31b` ／ 12,449 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>

<details>
<summary>reports/phase6/condition-source-ranking-20261006/outputs/large2048/0240.json — None</summary>

[原記録](../../reports/phase6/condition-source-ranking-20261006/outputs/large2048/0240.json) ／ SHA256: `9eb2119162602b208b89c20f8bcb4b487c34a6a581369757bf6bdca2e7e27abe` ／ 14,721 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |

</details>
