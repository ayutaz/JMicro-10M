# 教材・供給・品質・量 — 6/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/dataset_expansion_review.json — passed</summary>

[原記録](../../reports/phase6/dataset_expansion_review.json) ／ SHA256: `bcebe839220774e15f915739c81102660c4f1892fcce18d9ef084e86bc0d2434` ／ 322,010 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checks.actual_job_complete_exited_budget | true |
| checks.frozen_binding_scientific_verification_scope | true |
| checks.actual_CUDA_stable_decay_continuous_resumed_exact | true |
| checks.actual200M_new_source_train_only_disclosed | true |
| checks.control_finite_checkpoint_full_resume_hash | true |
| checks.control_actual30518_contiguous_finite_updates | true |
| checks.control_final_counters_binding_digest | true |
| checks.control_actual_all_LR_stable_decay | true |
| checks.control_actual_source_routes_short_cursors | true |
| checks.control_actual500M_saved_same_lineage | true |
| checks.control_checkpoint_bound_raw80 | true |
| checks.control_annotations_raw_hash | true |
| checks.control_all80_individual_notes | true |
| checks.control_appropriate_completion_actual_EOS | true |
| checks.control_common256_actual_NLL_BPB | true |
| checks.control_raw_rates_recomputed | true |
| checks.control_Japanese_complete_RNG_isolated | true |
| checks.refined_finite_checkpoint_full_resume_hash | true |
| checks.refined_actual30518_contiguous_finite_updates | true |
| checks.refined_final_counters_binding_digest | true |
| checks.refined_actual_all_LR_stable_decay | true |
| checks.refined_actual_source_routes_short_cursors | true |
| checks.refined_actual500M_saved_same_lineage | true |
| checks.refined_checkpoint_bound_raw80 | true |
| checks.refined_annotations_raw_hash | true |
| checks.refined_all80_individual_notes | true |
| checks.refined_appropriate_completion_actual_EOS | true |
| checks.refined_common256_actual_NLL_BPB | true |
| checks.refined_raw_rates_recomputed | true |
| checks.refined_Japanese_complete_RNG_isolated | true |
| checks.paired_fixed80_and_common_bytes_alignment | true |
| checks.same_actual_Web_routes_tokens_and_final_cursor | true |
| checks.paired_Japanese_IDs_semantics | true |
| checks.paired_Japanese_IDs_jblimp | true |
| checks.paired_Japanese_IDs_jcqa | true |
| summaries.control.BPB | 0.9771545479728297 |
| summaries.control.rates.eos | 34 |
| summaries.control.rates.repetition | 15 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.content.grammar_score2 | 64 |
| summaries.control.content.relevance_score2 | 23 |
| summaries.control.content.coherence_score2 | 15 |
| summaries.control.appropriate_EOS | 20 |
| summaries.control.diagnostics.semantics.primary.accuracy.point | 0.65625 |
| summaries.control.diagnostics.semantics.primary.accuracy.ci95 | [0.6041666666666666, 0.7083333333333334] |
| summaries.control.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.primary.hard_accuracy | 0.65625 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6145833333333334] |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| summaries.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5724991854024112 |
| summaries.control.diagnostics.semantics.per_token_secondary.mcc | 0.14611900125320154 |
| summaries.control.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.control.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.control.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.control.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.control.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.categories.time.seed | 42 |
| summaries.control.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.control.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.control.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.control.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.control.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.control.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| summaries.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| summaries.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7250755287009063 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.676737160120846, 0.7734138972809668] |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7250755287009063 |
| summaries.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4203152364273205 |
| summaries.control.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.control.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.control.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.control.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.control.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.control.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.control.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| summaries.control.diagnostics.jcqa.primary.accuracy.point | 0.35031277926720283 |
| summaries.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.322609472743521, 0.3762287756925827] |
| summaries.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jcqa.primary.hard_accuracy | 0.35031277926720283 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32797140303842715 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3002680965147453, 0.354781054512958] |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32797140303842715 |
| summaries.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3263633055352647 |
| summaries.control.diagnostics.jcqa.per_token_secondary.mcc | 0.15990035066465652 |
| summaries.control.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.control.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.control.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.control.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.control.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.control.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.control.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.control.diagnostics.semantic_both_contexts.correct | 33 |
| summaries.refined.BPB | 0.9773220933922412 |
| summaries.refined.rates.eos | 25 |
| summaries.refined.rates.repetition | 14 |
| summaries.refined.rates.unicode_failure | 0 |
| summaries.refined.rates.role_leak | 0 |
| summaries.refined.rates.empty | 0 |
| summaries.refined.content.grammar_score2 | 65 |
| summaries.refined.content.relevance_score2 | 24 |
| summaries.refined.content.coherence_score2 | 9 |
| summaries.refined.appropriate_EOS | 19 |
| summaries.refined.diagnostics.semantics.primary.accuracy.point | 0.640625 |
| summaries.refined.diagnostics.semantics.primary.accuracy.ci95 | [0.59375, 0.6875] |
| summaries.refined.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.refined.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.refined.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.refined.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.primary.hard_accuracy | 0.640625 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.625] |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.refined.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| summaries.refined.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5832881172002171 |
| summaries.refined.diagnostics.semantics.per_token_secondary.mcc | 0.1667028474261652 |
| summaries.refined.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.refined.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.refined.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.categories.time.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.refined.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.refined.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.refined.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| summaries.refined.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.824773413897281] |
| summaries.refined.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.refined.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.refined.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.refined.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7371601208459214 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6888217522658611, 0.7824773413897281] |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7371601208459214 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42434782608695654 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.refined.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.refined.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.refined.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.refined.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.refined.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.refined.diagnostics.jblimp.raw_pair_accuracy | 0.7764350453172205 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.point | 0.38561215370866847 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.ci95 | [0.3574620196604111, 0.41242180518319926] |
| summaries.refined.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jcqa.primary.hard_accuracy | 0.38605898123324395 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.33109919571045576 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3033958891867739, 0.3583556747095621] |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3315460232350313 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3306505976449266 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.mcc | 0.16442959952983033 |
| summaries.refined.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.refined.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.refined.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.refined.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.refined.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.refined.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.refined.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.refined.diagnostics.semantic_both_contexts.correct | 28 |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| practical.coherence_at_least27 | false |
| practical.appropriate_at_least27 | false |
| practical.EOS_at_least37 | false |
| practical.repetition_at_most18 | true |
| original_Web_gates.EOS_at_least8_more | true |
| original_Web_gates.repetition_no_worse | true |
| original_Web_gates.no_empty_role_unicode | true |
| original_Web_gates.BPB_degradation_at_most1percent | true |
| paired_diagnostics.semantics.point | -0.015625 |
| paired_diagnostics.semantics.ci95 | [-0.057291666666666664, 0.026041666666666668] |
| paired_diagnostics.semantics.units | 96 |
| paired_diagnostics.semantics.examples | 192 |
| paired_diagnostics.semantics.unit | "family/prompt" |
| paired_diagnostics.semantics.seed | 42 |
| paired_diagnostics.semantics.repetitions | 2000 |
| paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jblimp.point | -0.0030211480362537764 |
| paired_diagnostics.jblimp.ci95 | [-0.03323262839879154, 0.02416918429003021] |
| paired_diagnostics.jblimp.units | 331 |
| paired_diagnostics.jblimp.examples | 331 |
| paired_diagnostics.jblimp.unit | "family/prompt" |
| paired_diagnostics.jblimp.seed | 42 |
| paired_diagnostics.jblimp.repetitions | 2000 |
| paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jcqa.point | 0.035299374441465595 |
| paired_diagnostics.jcqa.ci95 | [0.01876675603217158, 0.05138516532618409] |
| paired_diagnostics.jcqa.units | 1119 |
| paired_diagnostics.jcqa.examples | 1119 |
| paired_diagnostics.jcqa.unit | "family/prompt" |
| paired_diagnostics.jcqa.seed | 42 |
| paired_diagnostics.jcqa.repetitions | 2000 |
| paired_diagnostics.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| eligible_for_full | false |
| actual_data.old_pool_tokens | 59963449 |
| actual_data.new_pool_tokens | 200000192 |
| actual_data.new_source_tokens | 140036743 |
| actual_data.retained_source_tokens | 59963449 |
| actual_data.body_tokens_mean | 170.12861093204972 |
| actual_data.old_body_tokens_mean | 88.46211928062915 |
| actual_data.EOS_per_1000_tokens | 5.809609422774954 |
| actual_data.old_EOS_per_1000_tokens | 11.05435079293054 |
| actual_data.length_and_EOS_density_within5percent | false |
| comparison_interpretation | "Amount plus new translated-story source/length/EOS density; not a pure amount-only causal estimate" |
| checked_at | "2026-10-05T08:36:43.846755Z" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/dataset_expansion_source_inspection.json — inspected</summary>

[原記録](../../reports/phase6/dataset_expansion_source_inspection.json) ／ SHA256: `1587b240e582fff05e856be0597dc3353e67e47270ccb0d3af6c474b8e71fbab` ／ 20,419 bytes

| 原キー | 保存値 |
|---|---|
| status | "inspected" |
| source.declared_notes | "---\nlanguage: [ja, en]\nlicense: cdla-sharing-1.0\npretty_name: TinyStories Japanese\ntask_categories:\n  - text-generation\n  - translation\ntags:\n  - tinystories\n  - japanese\n  - english\n  - translation\n  - synthetic\nsize_categories:\n  - 1M&lt;n&lt;10M\nconfigs:\n  - config_name: default\n    data_files:\n      - split: train\n        path:\n          - data/train-00000-of-00004.jsonl\n          - data/train-00001-of-00004.jsonl\n          - data/train-00002-of-00004.jsonl\n          - data/train-00003-of-00004.jsonl\n      - split: validation\n        path:\n          - data/validation-00000-of-00001.jsonl\n---\n\n# TinyStories Japanese\n\nThis dataset is a Japanese translation of the TinyStories dataset.\n\nThe dataset preserves the original TinyStories train/validation split structure and record order. Each record contains the original English story, its SHA-256 hash, and the Japanese translation.\n\n## Dataset structure\n\nEach record has the following fields:\n\n* `text_hash`: SHA-256 hash of `text_en` encoded as UTF-8.\n* `text_en`: Original English TinyStories text.\n* `text_ja`: Japanese translation.\n\nExample:\n\n```json\n{\"text_hash\":\"...\",\"text_en\":\"Once upon a time, ...\",\"text_ja\":\"むかしむかし、...\"}\n```\n\n## Files\n\n```text\ntrain-00000-of-00004.jsonl\ntrain-00001-of-00004.jsonl\ntrain-00002-of-00004.jsonl\ntrain-00003-of-00004.jsonl\nvalidation-00000-of-00001.jsonl\n```\n\nThe files follow the same split structure as the source dataset:\n\n* `train`: 4 JSONL shards\n* `validation`: 1 JSONL shard\n\n## Translation process\n\nThe Japanese translations were generated primarily using `google/gemma-4-26B-A4B` from the original English TinyStories texts.\n\nAfter translation, the records were realigned to the original TinyStories order using `text_hash`, which is the SHA-256 hash of `text_en` encoded as UTF-8.\n\nA small number of missing or problematic records were manually corrected.\n\nThe translations are not fully human-reviewed, and some translation errors, unnatural wording, or artifacts may remain.\n\n## License\n\nThis dataset is released under the Community Data License Agreement – Sharing, Version 1.0 (`CDLA-Sharing-1.0`), following the license of the original TinyStories dataset.\n\n## Credits\n\nJapanese translation, alignment, and dataset preparation: Naoki Shibata.\n\nThis dataset is derived from the original TinyStories dataset. The translations were generated primarily using `google/gemma-4-26B-A4B`.\n\n## Notes\n\nThe translations are not fully human-reviewed. Users should be aware that some translation errors, unnatural wording, or artifacts may remain.\n\nThe field `text_hash` can be used to match records with the original English text.\n" |
| file.bytes | 1348591301 |
| selection.whole_64_384_tokens | 425833 |
| selection.old_selection_tokens | 379 |
| seconds | 27.947294042998692 |
| checked_at | "2026-10-05T07:30:50.198352Z" |
| official_validation_test_acquired | false |

</details>

<details>
<summary>reports/phase6/dataset_expansion_supply.json — pinned_supply_pending_inspection</summary>

[原記録](../../reports/phase6/dataset_expansion_supply.json) ／ SHA256: `584f79bb3d557b2334c95bcfe447e6b1ee48efc68adbef98158251e9c4f989e2` ／ 10,994 bytes

| 原キー | 保存値 |
|---|---|
| status | "pinned_supply_pending_inspection" |
| seconds | 3.412968451011693 |
| sources.shibatch/TinyStories-JA.declared_notes | "---\nlanguage: [ja, en]\nlicense: cdla-sharing-1.0\npretty_name: TinyStories Japanese\ntask_categories:\n  - text-generation\n  - translation\ntags:\n  - tinystories\n  - japanese\n  - english\n  - translation\n  - synthetic\nsize_categories:\n  - 1M&lt;n&lt;10M\nconfigs:\n  - config_name: default\n    data_files:\n      - split: train\n        path:\n          - data/train-00000-of-00004.jsonl\n          - data/train-00001-of-00004.jsonl\n          - data/train-00002-of-00004.jsonl\n          - data/train-00003-of-00004.jsonl\n      - split: validation\n        path:\n          - data/validation-00000-of-00001.jsonl\n---\n\n# TinyStories Japanese\n\nThis dataset is a Japanese translation of the TinyStories dataset.\n\nThe dataset preserves the original TinyStories train/validation split structure and record order. Each record contains the original English story, its SHA-256 hash, and the Japanese translation.\n\n## Dataset structure\n\nEach record has the following fields:\n\n* `text_hash`: SHA-256 hash of `text_en` encoded as UTF-8.\n* `text_en`: Original English TinyStories text.\n* `text_ja`: Japanese translation.\n\nExample:\n\n```json\n{\"text_hash\":\"...\",\"text_en\":\"Once upon a time, ...\",\"text_ja\":\"むかしむかし、...\"}\n```\n\n## Files\n\n```text\ntrain-00000-of-00004.jsonl\ntrain-00001-of-00004.jsonl\ntrain-00002-of-00004.jsonl\ntrain-00003-of-00004.jsonl\nvalidation-00000-of-00001.jsonl\n```\n\nThe files follow the same split structure as the source dataset:\n\n* `train`: 4 JSONL shards\n* `validation`: 1 JSONL shard\n\n## Translation process\n\nThe Japanese translations were generated primarily using `google/gemma-4-26B-A4B` from the original English TinyStories texts.\n\nAfter translation, the records were realigned to the original TinyStories order using `text_hash`, which is the SHA-256 hash of `text_en` encoded as UTF-8.\n\nA small number of missing or problematic records were manually corrected.\n\nThe translations are not fully human-reviewed, and some translation errors, unnatural wording, or artifacts may remain.\n\n## License\n\nThis dataset is released under the Community Data License Agreement – Sharing, Version 1.0 (`CDLA-Sharing-1.0`), following the license of the original TinyStories dataset.\n\n## Credits\n\nJapanese translation, alignment, and dataset preparation: Naoki Shibata.\n\nThis dataset is derived from the original TinyStories dataset. The translations were generated primarily using `google/gemma-4-26B-A4B`.\n\n## Notes\n\nThe translations are not fully human-reviewed. Users should be aware that some translation errors, unnatural wording, or artifacts may remain.\n\nThe field `text_hash` can be used to match records with the original English text.\n" |
| sources.KeisukeMiyamoto/SyntheticTextbook-jp.declared_notes | "---\nlicense: apache-2.0\nlanguage:\n  - ja\npretty_name: SyntheticTextbook-jp\nannotations_creators:\n  - no-annotation\nlanguage_creators:\n  - machine-generated\nmultilinguality:\n  - monolingual\nsource_datasets:\n  - hotchpotch/fineweb-2-edu-japanese\ntask_categories:\n  - text-generation\nmodels:\n  - google/gemma-4-26B-A4B\n  - google/gemma-4-31B\ntags:\n  - japanese\n  - synthetic\n  - textbook\n  - education\n  - continual-pretraining\n  - pretraining\n  - parquet\nsize_categories:\n  - 1M&lt;n&lt;10M\nconfigs:\n  - config_name: default\n    data_files:\n      - split: train\n        path: train-*.parquet\n      - split: validation\n        path: validation.parquet\n      - split: test\n        path: test.parquet\n---\n\n# SyntheticTextbook-jp\n\nSyntheticTextbook-jp is a Japanese synthetic text dataset generated with Gemma 4 26B and Gemma 4 31B. The dataset was created by rewriting noisy source text into textbook-style Japanese for elementary school, junior high school, and high school levels. The rewritten text keeps only general knowledge from the source text.\n\n## Purpose\n\nThe main purpose of this dataset is to help LLMs learn natural Japanese text flow. This dataset is designed around topics that an average Japanese student may learn in school classes.\n## Source Data\n\nThe source text comes from: https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese\n\n## Dataset Size\n\n／ Split ／ Rows ／ Output tokens ／\n／---／---:／---:／\n／ Train ／ 1,067,212 ／ 974.0M ／\n／ Validation ／ 10,889 ／ 10.0M ／\n／ Test ／ 10,889 ／ 10.0M ／\n／ **Total** ／ **1,088,990** ／ **993.9M** ／\n\nRows were shuffled with seed 42 before the 98% train, 1% validation, and 1% test split. Token counts were measured with the Gemma 4 tokenizer.\n\n## Columns\n\n／ Column ／ Description ／\n／---／---／\n／ `source_id` ／ ID of the source text. ／\n／ `url` ／ URL from the source dataset. ／\n／ `source_text` ／ Original noisy source text. ／\n／ `prompt_type` ／ Target school level: `elementary-school`, `junior-high-school`, or `high-school`. ／\n／ `prompt` ／ Input text used for rewriting. ／\n／ `rewrite` ／ Synthetic textbook-style Japanese text. ／\n／ `output_tokens` ／ Number of tokens in `rewrite`. ／\n／ `output_chars` ／ Number of characters in `rewrite`. ／\n\n## Example\n\n```python\nfrom datasets import load_dataset\n\ndataset = load_dataset(\"MK0727/SyntheticTextbook-jp\", split=\"train\")\nprint(dataset[0][\"rewrite\"])\n```\n\n## Notes\n\nThe prompts were designed carefully, but the dataset may still include hallucinations generated by Gemma 4.\n\n---\n\n## Support Lambda\n\n[Lambda](https://github.com/KeisukeMiyamoto1324/lambda) is an open-source project for building small Japanese language models from scratch. As a student, I have funded this project with income from my part-time job, but the growing training costs are becoming difficult to cover.\n\nYour support helps cover GPU costs and develop larger models. Thank you for helping Lambda continue to grow.\n\n### Vast.ai\n\nVast.ai offers affordable cloud GPUs for AI training, with **NVIDIA H100 SXM GPUs available from around $1.54 per hour**. If you purchase credits through the link below, I receive 3% in GPU credits at no extra cost to you.\n\nhttps://cloud.vast.ai/?ref_id=521936\n\n### Ko-fi\n\nSupport Lambda with a donation starting from $5.\n\n&lt;a href=\"https://ko-fi.com/lambda_llm\"&gt;\n  &lt;img src=\"assets/support_me_on_kofi_badge_blue.png\" alt=\"Support Lambda on Ko-fi\" width=\"240\"&gt;\n&lt;/a&gt;\n" |
| official_validation_test_acquired | false |
| preparation_budget_seconds | 1800 |

</details>

<details>
<summary>reports/phase6/document_context_ablation_preparation.json — document_history_ablation_prepared_unstarted</summary>

[原記録](../../reports/phase6/document_context_ablation_preparation.json) ／ SHA256: `05123c87eef3e81ccd32765d2ccd51b27d3ef0ed32639ff7a83212a93bf94074` ／ 2,502 bytes

| 原キー | 保存値 |
|---|---|
| status | "document_history_ablation_prepared_unstarted" |
| checkpoints.original_fullparent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.original_fullparent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.completed_masked_mixed.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoints.completed_masked_mixed.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| CPU_preparation_seconds | 0.1385533559951 |
| GPU_seconds | 0 |
| GPU_ceiling_seconds | 30 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/document_context_ablation_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/document_context_ablation_preparation_portable.json) ／ SHA256: `782187569aa286eb3557b933dc7b2dd106757de74c6341025b6316206165ba8c` ／ 1,986 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/document_context_ablation_preparation.json.bytes | 2502 |
| files.reports/phase6/document_context_ablation_preparation.json.sha256 | "05123c87eef3e81ccd32765d2ccd51b27d3ef0ed32639ff7a83212a93bf94074" |
| files.configs/phase6/document_context_ablation.json.bytes | 4061 |
| files.configs/phase6/document_context_ablation.json.sha256 | "c8ad5c4b0500176bf4a5838d8fdd5c95ea2ee33b88676081cc04f33042ce3c7a" |
| files.reports/phase6/document_context_ablation_proposal.json.bytes | 7929 |
| files.reports/phase6/document_context_ablation_proposal.json.sha256 | "e4c900ad2714b99bcb6e473a0b38543e864faade308d251421a69c1c68344813" |
| files.reports/phase6/document_context_ablation_tests.xml.bytes | 702 |
| files.reports/phase6/document_context_ablation_tests.xml.sha256 | "45b918d71f230fbc46d09604b5d1a1c99ab1ddcd57ffc9eb615336fc1ce10076" |
| files.scripts/record_document_context_ablation.py.bytes | 9636 |
| files.scripts/record_document_context_ablation.py.sha256 | "1f06a9657db4484267111fb676f326d971948ec41af19900969feafe008a4935" |
| files.scripts/document_context_ablation.py.bytes | 4385 |
| files.scripts/document_context_ablation.py.sha256 | "a3f1d44c73a323bc9e2a9472d82ee48e26d80c7bc03b87c754bcc96936c1517f" |
| files.scripts/diagnose_document_context_ablation.py.bytes | 15889 |
| files.scripts/diagnose_document_context_ablation.py.sha256 | "c15b2e7f5b47bdedc41276fda7105add6904fb50937adb6bba40696ff5bc65fb" |
| files.scripts/diagnose_document_context_ablation.ps1.bytes | 2528 |
| files.scripts/diagnose_document_context_ablation.ps1.sha256 | "f323f84f8cda100fca652c06a6246e22d83fca9010a5a5a71b2d5eac02b8fda1" |
| files.tests/test_document_context_ablation.py.bytes | 3087 |
| files.tests/test_document_context_ablation.py.sha256 | "8a8b2c1139d28c36566d16835f7c0d42a56bbf62fcb8d8d5950083ea9b16694e" |
| files.scripts/source_gradient_attribution.py.bytes | 6629 |
| raw_bytes | 57348 |

</details>

<details>
<summary>reports/phase6/early_exposure_preparation_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/early_exposure_preparation_evidence_manifest.json) ／ SHA256: `1a0551250e29ece5e53a2e45c0ea4517732a5aef3565c4b38e7842f83d5546ff` ／ 27,393 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 2128479 |
| archive.bytes | 654957 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/eos_complete_100m_preparation.json — prepared_and_content_reviewed_before_GPU_training</summary>

[原記録](../../reports/phase6/eos_complete_100m_preparation.json) ／ SHA256: `de818d3788e7be8246e2a289b46cdb147bbeb20a6125c91e03d5ed073b2a1fd3` ／ 11,297 bytes

| 原キー | 保存値 |
|---|---|
| status | "prepared_and_content_reviewed_before_GPU_training" |
| pool.status | "ready_train_only_complete_units" |
| pool.selection.body_tokens_min | 32 |
| pool.selection.body_tokens_max | 64 |
| pool.selection.arbitrary_truncation_EOS | false |
| pool.documents | 445501 |
| pool.tokens | 21000010 |
| pool.parent_documents | 94157 |
| pool.body_tokens_mean | 45.13796377561442 |
| pool.seconds | 4.577704413999982 |
| pool.content_limit | "Conservative complete sentence boundaries; semantic quality is not certified by blind human review" |
| targeted_tests | 22 |
| tests_sha256 | "e259d968956b7021c7b1ea891888e0b027f9c008f303cd6d0ed166197a9d9a36" |
| GPU_training_tokens | 0 |
| preserved_previous_CPU_preparations | ["reports/phase6/eos-complete-100m-20261004", "reports/phase6/eos-complete-100m-20261004-r1"] |
| worker_cleanup.reason | "Pool.terminate SIGTERM inherited parent cooperative handler; idle workers failed to exit after completed extraction." |
| worker_cleanup.training_started | false |

</details>

<details>
<summary>reports/phase6/eos_decoupled_web_kl_trainer_preparation.json — actual_CPU_math_and_fullstate_fixture_passed_not_GPU_quality_evidence</summary>

[原記録](../../reports/phase6/eos_decoupled_web_kl_trainer_preparation.json) ／ SHA256: `5cd5c8cf06a67efcabc896b8f21bad534bb823286a4e756473ed507dff742b27` ／ 2,909 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU_math_and_fullstate_fixture_passed_not_GPU_quality_evidence" |
| tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos_decoupled_web_kl_prototype_tests.xml" |
| tests.sha256 | "12332f60841409f37ba165d05ca30ec524a45549e3eac2d2f5f7f1dd254f325b" |
| source_sha256.scripts/eos_decoupled_web_kl_preservation.py | "5abe753fcdd5273ee9033b9e3dc8e207124f294d85e6f1dbb0bd8207252571e1" |
| source_sha256.scripts/eos_decoupled_web_kl_condition_trainer.py | "40602f92d9abe710442aabb24d60af232956020fe2cccec7917b676ce8621320" |
| source_sha256.scripts/eos_decoupled_resident_web_kl_trainer.py | "a95b7941382ae6ecddcafcb2b7a5da014afd2158fc8480603a15d77390ca401e" |
| source_sha256.scripts/prepare_eos_decoupled_web_kl.py | "e8b5675ce97780dbc39107303742ec9f47dd1b1a9449ea263768baa6ba289f61" |
| source_sha256.scripts/propose_eos_decoupled_web_kl_comparison.py | "d08f915c4bbd93083918c314721480eeaba913cf7a3a58de2d4eaef1ddd2436d" |
| source_sha256.tests/test_eos_decoupled_web_kl_preservation.py | "4573df5a12572f84c22560ad0d3f3dd42b41a03af9cff4b8e271481c1da2023e" |
| source_sha256.tests/test_eos_decoupled_web_kl_condition_trainer.py | "6f1f615742767b64570b8ace6ee482818bcc84e870aa31beef45cb716e72060f" |
| CPU_fixture.continuous4_vs2plus2_all_state_equal | true |
| CPU_fixture.main_input_tokens | 96 |
| CPU_fixture.reference_input_tokens | 64 |
| CPU_fixture.parent_Adam_model_RNG_and_actualLR_preserved | true |
| CPU_fixture.frozen_teacher_verified | true |
| CPU_fixture.new_probability_mass_saved_resumed_and_history_equal | true |
| initial_failure | "Identical logits produced -1.8694e-8 KL from subtracting FP32 normalizers; preserved XML. Compute teacher conditional logsoftmax directly, preserving the exact mathematical component and exact-zero identical-logit check. Tests not weakened." |
| actual_GPU_seconds | 0 |
| actual_scientific_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/final_base_dev_preparation.json — conditional_full_dev_commands_and_content_review_ready</summary>

[原記録](../../reports/phase6/final_base_dev_preparation.json) ／ SHA256: `ba0435a838a0d73db1fd16f63db1ed16990e43fa2982aeea28325df2b2be4b12` ／ 1,762 bytes

| 原キー | 保存値 |
|---|---|
| status | "conditional_full_dev_commands_and_content_review_ready" |
| evaluation.full_dev_documents | 89416 |
| evaluation.full_dev_body_bytes | 164344743 |
| evaluation.full_dev_body_tokens | 42003934 |
| evaluation.long_max_new_tokens | [128, 512] |
| evaluation.GPU_budget_seconds | 3000 |
| tests.PowerShell_parser | true |
| tests.passed | 7 |
| tests.path | "reports/phase6/final_base_dev_tests.xml" |
| tests.CLI_help | true |
| tests.seconds | 0.96 |
| additional_training_tokens | 0 |
| protected_test_used | false |
| independent_training_seed_confirmed | false |
| Base_adopted | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/final_base_test_preparation.json — conditional_fixed_recipe_final_Base_test_commands_ready</summary>

[原記録](../../reports/phase6/final_base_test_preparation.json) ／ SHA256: `c4b1b1ac9a5d5c29743abaea80554ffd415e282b747c167ba2b63b5b5fd42546` ／ 1,776 bytes

| 原キー | 保存値 |
|---|---|
| status | "conditional_fixed_recipe_final_Base_test_commands_ready" |
| test_scope.full_test_body | true |
| test_scope.primary_test_families | 20 |
| test_scope.raw_outputs | 100 |
| test_scope.decoding | ["greedy suppressed", "greedy unsuppressed", "sampling42", "sampling43", "sampling44"] |
| test_scope.max_new_tokens | 64 |
| test_scope.GPU_budget_seconds | 1200 |
| criteria.grammar_2_rate | 0.7 |
| criteria.coherence_2_rate | 0.3375 |
| criteria.appropriate_completion_rate | 0.3375 |
| criteria.repetition_max_rate | 0.225 |
| criteria.all100_raw_failures_zero | true |
| tests.passed | 19 |
| tests.seconds | 1.86 |
| tests.path | "reports/phase6/final_base_test_protocol_tests.xml" |
| tests.CLI_help | true |
| tests.PowerShell_parser | true |
| actual_CUDA_test_evaluations | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/finite-parameter-displacement-20261006/preparation-job.json — complete</summary>

[原記録](../../reports/phase6/finite-parameter-displacement-20261006/preparation-job.json) ／ SHA256: `153a043a65bd867167ebdd1eff5b6e60970d37718e4c7b9bfc5a3f83359a48ed` ／ 456 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| CPU_ceiling_seconds | 30 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| CPU_seconds | 0.33230250197811984 |

</details>

<details>
<summary>reports/phase6/finite_Web_constraint_preparation.json — finite_Web_constraint_preparation</summary>

[原記録](../../reports/phase6/finite_Web_constraint_preparation.json) ／ SHA256: `5f9fb8f4897f872949a9231011bf4c548d6af56b9eac930961dba2172b58b6b6` ／ 3,914 bytes

| 原キー | 保存値 |
|---|---|
| status | "finite_Web_constraint_preparation" |
| CPU_preparation_seconds | 1.4314053030102514 |
| GPU_seconds | 0 |
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
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/finite_Web_constraint_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/finite_Web_constraint_preparation_portable.json) ／ SHA256: `a7fd1a07f9605bb049e6d2bdf84fb81878a3c8c08cc43c30583038d5ffa8b62d` ／ 1,942 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/finite_Web_constraint_preparation.json.bytes | 3914 |
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

</details>

<details>
<summary>reports/phase6/finite_Web_oracle_efficiency_preparation.json — readonly_oracle_efficiency_preparation</summary>

[原記録](../../reports/phase6/finite_Web_oracle_efficiency_preparation.json) ／ SHA256: `f9ba3bc9d7cd75d061659c165e63c4ceaf5832a07d8e8aff39c48cb6081c4b54` ／ 1,527 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_oracle_efficiency_preparation" |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| CPU_preparation_seconds | 0.22917144899838604 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| new_source_CE_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| completion_scope | "Implementation diagnostic, not Base quality/adoption." |

</details>

<details>
<summary>reports/phase6/finite_Web_oracle_efficiency_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/finite_Web_oracle_efficiency_preparation_portable.json) ／ SHA256: `fbca709de372e5823bb9254ff7708ae33d992ab0b3619826af9346c3acf71a36` ／ 1,154 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/finite_Web_oracle_efficiency_preparation.json.bytes | 1527 |
| files.configs/phase6/finite_Web_oracle_efficiency.json.bytes | 6128 |
| files.scripts/record_finite_Web_oracle_efficiency.py.bytes | 6372 |
| files.scripts/probe_finite_Web_oracle_efficiency.py.bytes | 14444 |
| files.scripts/probe_finite_Web_oracle_efficiency.ps1.bytes | 2652 |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_preparation.json — Fisher_parameter_anchor_preparation</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_preparation.json) ／ SHA256: `90412b297333bf72cc0d97dd4da41ee22fa93582d400dcc806c91f3bbd5e6c18` ／ 1,516 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_anchor_preparation" |
| CPU_preparation_seconds | 0.2640336899785325 |
| field_GPU_seconds | 3.6230295989953447 |
| own_job_GPU_seconds | 0 |
| new_source_CE_teacher_tokens | 0 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_preparation_portable.json) ／ SHA256: `f0da3c85b84ac2a419bc956e00e33b1acd40e1fb0f73d9904532555fa6056a34` ／ 1,782 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_anchor_preparation.json.bytes | 1516 |
| files.configs/phase6/fisher_parameter_anchor_probe.json.bytes | 21775 |
| files.reports/phase6/fisher_parameter_anchor_proposal.json.bytes | 5455 |
| files.reports/phase6/fisher_parameter_budget_tests.xml.bytes | 388 |
| files.reports/phase6/fisher_parameter_budget_tests.xml.sha256 | "7065564f37f1e48b2f922271c1d7086d59d0e8a2335ed9ecb26c6287d5033f9f" |
| files.scripts/record_fisher_parameter_anchor.py.bytes | 8066 |
| files.scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.scripts/run_fisher_parameter_anchor.py.bytes | 22806 |
| files.scripts/run_fisher_parameter_anchor.ps1.bytes | 3089 |
| files.tests/test_fisher_parameter_budget.py.bytes | 1011 |
| files.tests/test_fisher_parameter_budget.py.sha256 | "4bfaaf96a5f62f8225724e040238736e9cd3bbf1d908c65eb0f639c358d83087" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_field_preparation.json — Fisher_parameter_field_preparation</summary>

[原記録](../../reports/phase6/fisher_parameter_field_preparation.json) ／ SHA256: `3d92e45ded98f9dc5def12f0b0b68041e7b05da749555718dc2fd200d34fc894` ／ 1,649 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_field_preparation" |
| CPU_preparation_seconds | 0.28030768601456657 |
| GPU_seconds | 0 |
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

</details>

<details>
<summary>reports/phase6/fisher_parameter_field_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_field_preparation_portable.json) ／ SHA256: `9a51641ef42840e260b95f7a13660f63532fd559bf8b1388a4ba761e554be702` ／ 1,774 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_field_preparation.json.bytes | 1649 |
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

</details>

<details>
<summary>reports/phase6/gated_shared_comparison_preparation.json — gated_shared_comparison_preparation</summary>

[原記録](../../reports/phase6/gated_shared_comparison_preparation.json) ／ SHA256: `7f097b33536d81002ec3b5d3118337b7f0b1bdfc53377240960b4b74544525d1` ／ 1,607 bytes

| 原キー | 保存値 |
|---|---|
| status | "gated_shared_comparison_preparation" |
| CPU_preparation_seconds | 0.11724215900176205 |
| verification_GPU_seconds | 47.25850116199581 |
| verification_teacher_tokens | 1307952 |
| scientific_GPU_seconds | 0 |
| new_source_CE_teacher_tokens | 0 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/gated_shared_comparison_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/gated_shared_comparison_preparation_portable.json) ／ SHA256: `0ad5a57b83d7ea23396304cad3c27516b3e7d70b46e78498fe3e44336248d9e7` ／ 2,107 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/gated_shared_comparison_preparation.json.bytes | 1607 |
| files.configs/phase6/gated_shared_comparison.json.bytes | 23473 |
| files.reports/phase6/gated_shared_proposal.json.bytes | 6875 |
| files.scripts/record_gated_shared_comparison.py.bytes | 9610 |
| files.scripts/run_gated_shared_comparison.py.bytes | 15245 |
| files.scripts/run_gated_shared_comparison.ps1.bytes | 2625 |
| files.scripts/review_gated_shared_comparison.py.bytes | 9878 |
| files.scripts/record_gated_shared_content.py.bytes | 3337 |
| files.tests/test_gated_shared_science.py.bytes | 1413 |
| files.tests/test_gated_shared_science.py.sha256 | "a9464c372c9a72af26302ed61f1dee9e8ec44f9ea1826adebecc21e9758f5101" |
| files.reports/phase6/gated_shared_science_tests.xml.bytes | 379 |
| files.reports/phase6/gated_shared_science_tests.xml.sha256 | "4a10e05aea35e10e579479e952444df3cae3daf23afdb0aab0f34a96a0ebdcfd" |
| files.reports/phase6/gated_shared_science_tests_initial_failure.xml.bytes | 2417 |
| files.reports/phase6/gated_shared_science_tests_initial_failure.xml.sha256 | "f32c5b4d03884b61b350ff52ddf62f3e146f3271fd54a784ad79258e920e5287" |

</details>

<details>
<summary>reports/phase6/gated_shared_preparation.json — gated_shared_preparation</summary>

[原記録](../../reports/phase6/gated_shared_preparation.json) ／ SHA256: `ce72122ecdb8336092016ae4d4e808f9c7b2a141bd50fe5871d6b91a8ad65717` ／ 1,684 bytes

| 原キー | 保存値 |
|---|---|
| status | "gated_shared_preparation" |
| CPU_preparation_seconds | 0.11882039500051178 |
| GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/gated_shared_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/gated_shared_preparation_portable.json) ／ SHA256: `101001330c8ed618a36f67f03a1a110746ba55bdf0502c9b8cc79bd6b94ae61d` ／ 2,178 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/gated_shared_preparation.json.bytes | 1684 |
| files.configs/phase6/gated_shared_probe.json.bytes | 34724 |
| files.reports/phase6/gated_shared_proposal.json.bytes | 6875 |
| files.scripts/record_gated_shared_probe.py.bytes | 7439 |
| files.reports/phase6/gated_shared_tests.xml.bytes | 788 |
| files.reports/phase6/gated_shared_tests.xml.sha256 | "4812fe0c1b891425cf6bef94fc16533d6c28deaf86970a80436453d00011e39b" |
| files.scripts/gated_shared_model.py.bytes | 5977 |
| files.scripts/gated_shared_trainer.py.bytes | 3154 |
| files.scripts/gated_shared_evaluation.py.bytes | 833 |
| files.scripts/define_gated_shared_comparison.py.bytes | 6758 |
| files.scripts/probe_gated_shared_comparison.py.bytes | 15755 |
| files.scripts/probe_gated_shared_comparison.ps1.bytes | 2629 |
| files.tests/test_gated_shared.py.bytes | 5686 |
| files.tests/test_gated_shared.py.sha256 | "99b900c005ca41740664fa5b62087740f5033e499ff81b9a7a6eb9776d9b6162" |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_trainer_preparation.json — actual_CPU_gold_CE_and_fullstate_fixture_passed_not_GPU_quality</summary>

[原記録](../../reports/phase6/hard_body_web_replay_trainer_preparation.json) ／ SHA256: `c6490ca3b2bced1a5ad6e8d513900efd6429a7f26a456dfa6ebc85d448c4f4cf` ／ 3,882 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU_gold_CE_and_fullstate_fixture_passed_not_GPU_quality" |
| auxiliary_policy.every_completed_update | 1 |
| auxiliary_policy.reference_teacher | "Immutable actual historical10.5B parent supplies detached non-EOS probability mass only, not soft targets." |
| tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/hard_body_web_replay_prototype_tests.xml" |
| tests.sha256 | "fe40f669e34536dd8bef7fa4078ad706476fbcede41863cc769f34134f5c31b7" |
| source_sha256.tests/test_hard_body_web_replay.py | "e1bb33d0903ef6e4d3e1f246e147d326612c251c59ea0c925debefddcccf060d" |
| source_sha256.tests/test_hard_body_web_replay_trainer.py | "f0cee4d5a56d9872f1455d8fcb7d9d31311b450fb9b46ca66bfd61c05c6721ed" |
| CPU_fixture.continuous4_vs2plus2_all_state_equal | true |
| CPU_fixture.main_input_tokens | 96 |
| CPU_fixture.reference_input_tokens | 64 |
| CPU_fixture.parent_model_Adam_scheduler_RNG_actualLR_preserved | true |
| CPU_fixture.frozen_teacher_verified | true |
| CPU_fixture.separate_hard_targets_and_probability_mass_saved_resumed | true |
| CPU_fixture.all4_main_and_replay_input_protocols_equal_soft_control | true |
| CPU_fixture.corrupt_hard_target_count_and_soft_checkpoint_rejected | true |
| initial_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/hard_body_web_replay_prototype_initial_failure.xml" |
| initial_failure.sha256 | "aa98cb05642c7c7c667e2c19b7d72e781bcc4544564d409571142e7ff1dbd665" |
| initial_failure_explanation | "A generic teacher-body-logit permutation changed FP32 reduction rounding by9.5367431640625e-7; no production math changed. Retain original XML. Control teacher non-EOS mass exactly in FP32 with two different saturated body distributions, retain bitwise loss equality and exact-mass checks. Nondegenerate mass/actual-gold/mask/gradient tests also remain. No scientific acceptance changed." |
| CPU_test_seconds | 0.853 |
| actual_GPU_seconds | 0 |
| actual_scientific_teacher_tokens | 0 |
| newly_prepared_source_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/historical_parent_condition_preparation_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/historical_parent_condition_preparation_evidence_manifest.json) ／ SHA256: `7faf66f17f6a21fc2984788497a4d1b7a27e25d07819a8b63c53915bafb9389c` ／ 69,810 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 3465628 |
| archive.bytes | 1055574 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_preparation.json — fourth_order_target_cell_own_CUDA_complete_science_frozen_unstarted</summary>

[原記録](../../reports/phase6/interleaved_outcome_preparation.json) ／ SHA256: `51c98ddb8fc60ac299d70dc149507cbf0113293218061f189726013c0c51256f` ／ 5,429 bytes

| 原キー | 保存値 |
|---|---|
| status | "fourth_order_target_cell_own_CUDA_complete_science_frozen_unstarted" |
| actual_probe_job.status | "complete" |
| actual_probe_job.GPU_elapsed_seconds | 17.989334398997016 |
| actual_probe_job.completed_updates | 32 |
| initial_fullstate_preservation.actual_parent_sampler_lineage | true |
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
| resume_checks.history_loss | true |
| resume_checks.history_source_eos | true |
| resume_checks.history_body_bytes_seen | true |
| resume_checks.history_reference_suffix_teacher_tokens | true |
| resume_checks.history_gradient_norm | true |
| resume_checks.history_source_input_tokens | true |
| resume_checks.history_token_digest | true |
| resume_checks.history_reference_token_digest | true |
| resume_checks.history_source_teachers | true |
| resume_checks.history_additional_teacher_tokens | true |
| resume_checks.history_actual_source_eos | true |
| resume_checks.history_supervised_tokens | true |
| resume_checks.history_tokens_seen | true |
| resume_checks.history_focus_teacher_tokens | true |
| resume_checks.history_source_focus_teachers | true |
| resume_checks.history_actual_source_teachers | true |
| resume_checks.history_actual_source_body_bytes | true |
| resume_checks.history_actual_source_routes | true |
| resume_checks.history_valid_input_tokens | true |
| resume_checks.history_update | true |
| resume_checks.history_source_digests | true |
| resume_checks.history_physical_input_tokens | true |
| resume_checks.history_source_body_bytes | true |
| resume_checks.history_focus_token_digest | true |
| resume_checks.history_removed_prefix_targets | true |
| resume_checks.history_lr | true |
| resume_checks.history_weighted_teacher_mass | true |
| resume_checks.history_outcome_weight | true |
| resume_checks.finite | true |
| resume_checks.no_reheat | true |
| resume_checks.mixed_sources_present | true |
| resume_checks.actual_conditional_mask_active | true |
| verification_optimizer_updates | 48 |
| verification_teacher_tokens | 1433919 |
| verification_input_tokens | 1572864 |
| scientific_teacher_tokens | 0 |
| scientific_optimizer_updates | 0 |
| GPU_seconds | 17.989334398997016 |
| previous_related_GPU_seconds_preserved | 2928.6630077910663 |
| related_GPU_seconds | 2946.6523421900633 |
| CPU_preparation_seconds | 28.6093455600203 |
| remaining_updates | 3068 |
| actual_hard_teachers_predicted | 91641755 |
| reference_quota_teachers | 100000000 |
| physical_input_tokens_predicted | 100532224 |
| own_measured_timing.steady_step_seconds | 0.05013709749619011 |
| own_measured_timing.estimated_updates | 3068 |
| own_measured_timing.warmup_seconds | 1.353256055037491 |
| own_measured_timing.save_seconds | 2.72545900195837 |
| own_measured_timing.estimated_training_seconds | 157.8993301753071 |
| estimated_science_GPU_seconds_with_margin | 405.26912922789927 |
| total_new_GPU_ceiling_seconds | 900 |
| same_per_source_input_masked_targets_EOS_and_cursors | true |
| synthetic_CPU_historical_counts_are_not_actual10_5B_CPU_learning | true |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_preparation_portable.json — None</summary>

[原記録](../../reports/phase6/interleaved_outcome_preparation_portable.json) ／ SHA256: `343de39bdef989542b7dac89ea0879b4e6eaea19c8bff37236fb9a52e7778cca` ／ 3,648 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/interleaved_outcome_preparation.json.bytes | 5429 |
| files.configs/phase6/interleaved_outcome_order.json.bytes | 18858 |
| files.configs/phase6/interleaved_outcome_order_probe.json.bytes | 18236 |
| files.reports/phase6/interleaved_outcome_order_proposal.json.bytes | 7457 |
| files.reports/phase6/interleaved_outcome_reference_input.json.bytes | 2649095 |
| files.scripts/record_interleaved_outcome_preparation.py.bytes | 7263 |
| files.scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.tests/test_interleaved_outcome.py.bytes | 5013 |
| files.tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/interleaved_outcome_tests.xml.bytes | 718 |
| files.reports/phase6/interleaved_outcome_tests.xml.sha256 | "2bc59d153863f9b57babaa1fbdf88dd22637b4baee05d6d210d65ebbef985bf5" |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/job.json.bytes | 544 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/result.json.bytes | 241567 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json.bytes | 270 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json.sha256 | "01f95c57c65be222970611a5d04b67d781eaa85bae9e4f5e227dca29833db1f0" |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/result.json.bytes | 79841 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json.bytes | 268 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json.sha256 | "38614bc57c4a10e7a669cb211c3b188812d344694241d3e4fac81c8ad4f6ec90" |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/metrics.jsonl.bytes | 113367 |
| raw_bytes | 3199369 |

</details>

<details>
<summary>reports/phase6/larger_material_comparison_preparation.json — CPU_commands_verified_actual_GPU_config_not_frozen</summary>

[原記録](../../reports/phase6/larger_material_comparison_preparation.json) ／ SHA256: `b831fb19e958daf7db70c7c6aaacaf007329419672f923b79eb542ab0d1a9ffa` ／ 1,789 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_commands_verified_actual_GPU_config_not_frozen" |
| stable_teachers_per_arm | 1000000000 |
| scientific_teachers | 2040000000 |
| GPU_budget_policy | "Measured completed prior native1B curve:2.04B/throughput*1.3+900seconds; ceiling7200; actual value only frozen after prepared64 passes" |
| tests | 9 |
| test_seconds | 2.59 |
| PowerShell_syntax_passed | true |
| CLI_help_passed | true |
| actual_GPU_teacher_tokens | 0 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/larger_material_preparation.json — CPU_builder_verified_preparation_not_started_quality_pending</summary>

[原記録](../../reports/phase6/larger_material_preparation.json) ／ SHA256: `aa183b9243e08296fadae0bc9553a207cf19bc754ef71d29607ff2452fa82db6` ／ 2,390 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_builder_verified_preparation_not_started_quality_pending" |
| small_prepared_targets.web | 475000000 |
| small_prepared_targets.story | 25000000 |
| CPU_budget_seconds | 1800 |
| seed | 2026100621 |
| CPU_tests | 7 |
| CPU_test_seconds | 0.86 |
| PowerShell_syntax_passed | true |
| previous_cache_probe_preflight_correction | "Cache blob filenames differed from content SHA256; reuse actual completed source hash verification with pinned revision/cache mapping/size; no repeated5.37GB scan" |
| unused_raw_story_exact_capacity_unmeasured | true |
| new_prepared_tokens | 0 |
| new_GPU_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/larger_material_supply_inventory.json — manifest_only_supply_inventory_not_material_preparation</summary>

[原記録](../../reports/phase6/larger_material_supply_inventory.json) ／ SHA256: `385c825aeeebb6d6bc3573dc6f845e77c20ec64363f6495f5db3bb8a3e8a883d` ／ 1,744 bytes

| 原キー | 保存値 |
|---|---|
| status | "manifest_only_supply_inventory_not_material_preparation" |
| sources.web.train_tokens | 12225819077 |
| sources.web.train_documents | 25879667 |
| sources.story.train_tokens | 200000192 |
| sources.story.train_documents | 1161923 |
| current_selected_material_tokens | 500000785 |
| limits | ["Existing tokenized story source alone cannot supply2B at20percent without repeated records", "Existing prepared source counts are upper bounds before whole-unit/family/dev filtering", "Unused pinned raw train capacity has not been measured; additional processing may supply some of the deficit", "Acquisition/preparation and learning tokens stay distinct; newsource/mixture changes are confounds", "No full-corpus stream scan/dedup or protected-test acquisition"] |
| new_GPU_jobs | 0 |
| Base_adopted | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/larger_material_v1_stopped_job.json — failed</summary>

[原記録](../../reports/phase6/larger_material_v1_stopped_job.json) ／ SHA256: `bd8ec2223b7b2954866e851581b7bff939fd33a28a7b6eeb63d321893f4f92cb` ／ 2,711 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| binding.small_prepared_targets.web | 475000000 |
| binding.small_prepared_targets.story | 25000000 |
| binding.seed | 2026100621 |
| binding.CPU_budget_seconds | 1800 |
| binding.tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.processing_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.processing_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.processing_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.scope | "Five items stage5 material supply only; matched95/5 mixture in500M/2B; quantity comparison within new mixture, old80/20 separate; no GPU/adoption" |
| seconds | 462.848794584992 |
| counts.web_scan_tokens | 5492000000 |
| prepared_tokens.dev_web | 1900000 |
| prepared_tokens.large_web | 475232624 |
| prepared_tokens.small_web | 118808156 |

</details>

<details>
<summary>reports/phase6/larger_material_v3_active_job.json — running_CPU_only_verified_actual_process</summary>

[原記録](../../reports/phase6/larger_material_v3_active_job.json) ／ SHA256: `d86971726160e43f200f5b51a7d972c08a810a4301aa7fad2b15a399d666bf07` ／ 4,859 bytes

| 原キー | 保存値 |
|---|---|
| status | "running_CPU_only_verified_actual_process" |
| prepare_job.status | "running" |
| prepare_job.binding.small_prepared_targets.web | 475000000 |
| prepare_job.binding.small_prepared_targets.story | 25000000 |
| prepare_job.binding.seed | 2026100621 |
| prepare_job.binding.CPU_budget_seconds | 1800 |
| prepare_job.binding.tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| prepare_job.binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| prepare_job.binding.processing_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| prepare_job.binding.processing_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| prepare_job.binding.processing_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| prepare_job.binding.scope | "Five items stage5 material supply only; matched95/5 mixture in500M/2B; quantity comparison within new mixture, old80/20 separate; no GPU/adoption" |
| prepare_job.binding.prior_stopped_CPU_job_sha256 | "bd8ec2223b7b2954866e851581b7bff939fd33a28a7b6eeb63d321893f4f92cb" |
| prepare_job.binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006/sample32.json | "283bce1a01e141f90d455fc63091570685a33a3ae8e1e043d09e2fb7eae28278" |
| prepare_job.binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006-first32-corrected/sample32.json | "50d7f81a7e754abe0ec5511ffc632bc26b3f49c910b61d612680a59e738c5ef0" |
| prepare_job.seconds | 456.1608370729955 |
| prepare_job.counts.web_scan_tokens | 3600000000 |
| prepare_job.prepared_tokens.dev_web | 1900038 |
| prepare_job.prepared_tokens.large_web | 638440172 |
| prepare_job.prepared_tokens.small_web | 159610043 |
| UI_original_checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| new_GPU_teacher_tokens | 0 |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/larger_material_v3_completed_job.json — complete</summary>

[原記録](../../reports/phase6/larger_material_v3_completed_job.json) ／ SHA256: `7197aa1c844d033beacf2f2f261e1f306d690de016a18e18d3f6044de8219a01` ／ 3,880 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.small_prepared_targets.web | 475000000 |
| binding.small_prepared_targets.story | 25000000 |
| binding.seed | 2026100621 |
| binding.CPU_budget_seconds | 1800 |
| binding.tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.processing_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.processing_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.processing_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.scope | "Five items stage5 material supply only; matched95/5 mixture in500M/2B; quantity comparison within new mixture, old80/20 separate; no GPU/adoption" |
| binding.prior_stopped_CPU_job_sha256 | "bd8ec2223b7b2954866e851581b7bff939fd33a28a7b6eeb63d321893f4f92cb" |
| binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006/sample32.json | "283bce1a01e141f90d455fc63091570685a33a3ae8e1e043d09e2fb7eae28278" |
| binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006-first32-corrected/sample32.json | "50d7f81a7e754abe0ec5511ffc632bc26b3f49c910b61d612680a59e738c5ef0" |
| seconds | 1420.1500192569947 |
| counts.web_scan_tokens | 10876000000 |
| counts.story_scan_tokens | 200000192 |
| prepared_tokens.dev_web | 1900038 |
| prepared_tokens.large_web | 1900000168 |
| prepared_tokens.small_web | 475000042 |
| prepared_tokens.dev_story | 100039 |
| prepared_tokens.large_story | 100000888 |
| prepared_tokens.small_story | 25000222 |

</details>

<details>
<summary>reports/phase6/larger_material_v3_completion.json — preparation_complete_content_rejected</summary>

[原記録](../../reports/phase6/larger_material_v3_completion.json) ／ SHA256: `973d86492c28c69a47a1daf7940a7c2056224e7322398ead94c061a5e3103312` ／ 891 bytes

| 原キー | 保存値 |
|---|---|
| status | "preparation_complete_content_rejected" |
| prepared_tokens.large | 2000001056 |
| prepared_tokens.small | 500000264 |
| CPU_seconds | 1420.1500192569947 |
| weak_documents | 11 |
| documents | 64 |
| Base_adopted | false |
| Chat_GPU_teacher_tokens | 0 |
| GPU_scientific_teacher_tokens | 0 |
| requested_five_steps_complete | false |
| sample_sha256 | "35d15a386dabd2e846ab4f62ee5297e951928e0ce09021a3206642d96944a321" |
| notes_sha256 | "5e06d5ba2aac458b0084ff2c237c61967db68c05482114723bc0cf3a3857215d" |

</details>

<details>
<summary>reports/phase6/larger_material_v3_content_notes.json — None</summary>

[原記録](../../reports/phase6/larger_material_v3_content_notes.json) ／ SHA256: `5e06d5ba2aac458b0084ff2c237c61967db68c05482114723bc0cf3a3857215d` ／ 10,659 bytes

| 原キー | 保存値 |
|---|---|
| sample_sha256 | "35d15a386dabd2e846ab4f62ee5297e951928e0ce09021a3206642d96944a321" |

</details>

<details>
<summary>reports/phase6/larger_material_v3_content_review.json — fixed_content_review_complete</summary>

[原記録](../../reports/phase6/larger_material_v3_content_review.json) ／ SHA256: `200dd50e83ec306b5fdb64e2d13c83404908af07667173eb543a76e3deddfe38` ／ 97,093 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_content_review_complete" |
| passed | false |
| weak_documents | 11 |
| documents | 64 |
| sample_sha256 | "35d15a386dabd2e846ab4f62ee5297e951928e0ce09021a3206642d96944a321" |
| notes_sha256 | "5e06d5ba2aac458b0084ff2c237c61967db68c05482114723bc0cf3a3857215d" |
| pools.small.splits.train.tokens | 500000264 |
| pools.small.splits.train.documents | 4319789 |
| pools.small.splits.train.body_bytes | 1980876131 |
| pools.large.splits.train.tokens | 2000001056 |
| pools.large.splits.train.documents | 17279156 |
| pools.large.splits.train.body_bytes | 7923251433 |
| pools.dev.splits.dev.tokens | 2000077 |
| pools.dev.splits.dev.documents | 17453 |
| pools.dev.splits.dev.body_bytes | 7952099 |
| limitations | "No independent corpus-wide near-duplicate, site/author or factual audit; material readiness does not prove model quality" |
| decision | "Failed unchanged content criterion; preserve all64 and revise prospectively" |
| Base_adopted | false |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/larger_material_v3_preparation.json — frozen_CPU_verified_before_launch</summary>

[原記録](../../reports/phase6/larger_material_v3_preparation.json) ／ SHA256: `931f27c94f16270c403ba40ff8b6be5379a8faad35e8d42a2a37c1c3bbcf3430` ／ 3,056 bytes

| 原キー | 保存値 |
|---|---|
| status | "frozen_CPU_verified_before_launch" |
| small_prepared_targets.story | 25000000 |
| small_prepared_targets.web | 475000000 |
| CPU_budget_seconds | 1800 |
| seed | 2026100621 |
| tests | 7 |
| test_seconds | 1.36 |
| PowerShell_syntax_passed | true |
| capacity_caveat | "Estimate before local duplicates/protected prefixes/group discard; actual prepared2B and fixed64 quality still required" |
| probe_initial_failure | "First32 can return units when oldfirst4 had none; inherited parity assertion corrected once, failed run/source retained separately" |
| Base_adopted | false |
| Chat_adopted | false |
| GPU_teacher_tokens | 0 |
| new_prepared_ready_tokens | 0 |
| requested_five_steps_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/larger_material_v3_ready.json — prepared_pending_fixed_content_review</summary>

[原記録](../../reports/phase6/larger_material_v3_ready.json) ／ SHA256: `7cec9f21b86d4acf82a827cfffcfdb9b8549df4453f60e4acb7accd8c7845eef` ／ 209,978 bytes

| 原キー | 保存値 |
|---|---|
| status | "prepared_pending_fixed_content_review" |
| binding.small_prepared_targets.web | 475000000 |
| binding.small_prepared_targets.story | 25000000 |
| binding.seed | 2026100621 |
| binding.CPU_budget_seconds | 1800 |
| binding.tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.processing_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.processing_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.processing_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.scope | "Five items stage5 material supply only; matched95/5 mixture in500M/2B; quantity comparison within new mixture, old80/20 separate; no GPU/adoption" |
| binding.prior_stopped_CPU_job_sha256 | "bd8ec2223b7b2954866e851581b7bff939fd33a28a7b6eeb63d321893f4f92cb" |
| binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006/sample32.json | "283bce1a01e141f90d455fc63091570685a33a3ae8e1e043d09e2fb7eae28278" |
| binding.calibration_examples_sha256.reports/phase6/larger-web-supply-20261006-first32-corrected/sample32.json | "50d7f81a7e754abe0ec5511ffc632bc26b3f49c910b61d612680a59e738c5ef0" |
| pools.small.splits.train.tokens | 500000264 |
| pools.small.splits.train.documents | 4319789 |
| pools.small.splits.train.body_bytes | 1980876131 |
| pools.large.splits.train.tokens | 2000001056 |
| pools.large.splits.train.documents | 17279156 |
| pools.large.splits.train.body_bytes | 7923251433 |
| pools.dev.splits.dev.tokens | 2000077 |
| pools.dev.splits.dev.documents | 17453 |
| pools.dev.splits.dev.body_bytes | 7952099 |
| prepared_tokens.dev_web | 1900038 |
| prepared_tokens.large_web | 1900000168 |
| prepared_tokens.small_web | 475000042 |
| prepared_tokens.dev_story | 100039 |
| prepared_tokens.large_story | 100000888 |
| prepared_tokens.small_story | 25000222 |
| source_length_EOS_histograms_exact_ratio | true |
| sample_sha256 | "35d15a386dabd2e846ab4f62ee5297e951928e0ce09021a3206642d96944a321" |
| CPU_seconds | 1420.1464666109969 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/larger_story_supply_draws.json — None</summary>

[原記録](../../reports/phase6/larger_story_supply_draws.json) ／ SHA256: `5eb7b73e032e488aa2583b4e8fcacaff07d8eb3e00d09709421c81ae388cd549` ／ 956,391 bytes

| 原キー | 保存値 |
|---|---|
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.samples_per_file | 600 |
| binding.seed | 20261006 |
| binding.CPU_budget_seconds | 600.0 |
| binding.verification | "Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans" |
| binding.scope | "Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test" |

</details>

<details>
<summary>reports/phase6/larger_story_supply_job.json — complete</summary>

[原記録](../../reports/phase6/larger_story_supply_job.json) ／ SHA256: `a5d6ef07c0ef92f30e1e9f757a69d9e03d588a2913bc5aa00ae6cfaebfcb5fa0` ／ 3,185 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.samples_per_file | 600 |
| binding.seed | 20261006 |
| binding.CPU_budget_seconds | 600.0 |
| binding.verification | "Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans" |
| binding.scope | "Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test" |
| CPU_seconds | 0.3451098180084955 |

</details>

<details>
<summary>reports/phase6/larger_story_supply_recipe.json — None</summary>

[原記録](../../reports/phase6/larger_story_supply_recipe.json) ／ SHA256: `6930d9fac9a611023f0624d054afea6768ab8fa68a12f5d9fb4c0262afee1826` ／ 2,717 bytes

| 原キー | 保存値 |
|---|---|
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| samples_per_file | 600 |
| seed | 20261006 |
| CPU_budget_seconds | 600.0 |
| verification | "Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans" |
| scope | "Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test" |

</details>

<details>
<summary>reports/phase6/larger_story_supply_result.json — bounded_supply_estimate_complete_not_prepared_or_distinct</summary>

[原記録](../../reports/phase6/larger_story_supply_result.json) ／ SHA256: `af900ca53698d88c3f2e08e025480de0ff4e032e35168f40ca3801b70ce04646` ／ 4,679 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_supply_estimate_complete_not_prepared_or_distinct" |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.samples_per_file | 600 |
| binding.seed | 20261006 |
| binding.CPU_budget_seconds | 600.0 |
| binding.verification | "Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans" |
| binding.scope | "Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test" |
| files.data/train-00000-of-00004.jsonl.accepted_draws | 118 |
| files.data/train-00000-of-00004.jsonl.estimated_eligible_tokens | 36935853.00935569 |
| files.data/train-00001-of-00004.jsonl.accepted_draws | 116 |
| files.data/train-00001-of-00004.jsonl.estimated_eligible_tokens | 36137197.83865205 |
| files.data/train-00002-of-00004.jsonl.accepted_draws | 135 |
| files.data/train-00002-of-00004.jsonl.estimated_eligible_tokens | 41790564.60948412 |
| files.data/train-00003-of-00004.jsonl.accepted_draws | 135 |
| files.data/train-00003-of-00004.jsonl.estimated_eligible_tokens | 42088174.82764218 |
| estimated_eligible_tokens | 156951790.28513405 |
| bootstrap_repetitions | 2000 |
| note | "Monte Carlo uncertainty for byte-uniform draws in fixed files; includes possible duplicate/reused records, not distinct supply or independent family quality" |
| retained_prepared_tokens | 59963449 |
| target_story_tokens_for2B | 400000000 |
| counts.accepted_train | 504 |
| new_acquired_bytes | 0 |
| new_prepared_tokens | 0 |
| GPU_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| CPU_seconds | 0.34481309400871396 |

</details>

<details>
<summary>reports/phase6/larger_story_supply_sample32.json — None</summary>

[原記録](../../reports/phase6/larger_story_supply_sample32.json) ／ SHA256: `6f8bb2ce8f2c3cf1dc9d77a50e3887b18d46edbe7de79705c324f30b3aa54c30` ／ 53,692 bytes

| 原キー | 保存値 |
|---|---|
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.samples_per_file | 600 |
| binding.seed | 20261006 |
| binding.CPU_budget_seconds | 600.0 |
| binding.verification | "Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans" |
| binding.scope | "Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test" |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_failed_job.json — failed</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_failed_job.json) ／ SHA256: `2d7565cadb85eaa8fb3edd330a1dadb33b2afaa775b7faf1fe138caa54b291da` ／ 2,344 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |
| CPU_seconds | 0.03748317599820439 |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_failed_recipe.json — None</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_failed_recipe.json) ／ SHA256: `51d6087811ec9214dc2ff0cfbfa808fceab870b5a749414b6451c8b6078addd7` ／ 1,969 bytes

| 原キー | 保存値 |
|---|---|
| original_train_tokens | 12225819077 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seed | 2026100622 |
| CPU_budget_seconds | 600.0 |
| source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_job.json — complete</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_job.json) ／ SHA256: `8e9c33cfb4959650ba715613ce9ab37b2dbf04ac43b2676595b1307a6d1632f1` ／ 2,365 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |
| CPU_seconds | 1.454047280989471 |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_recipe.json — None</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_recipe.json) ／ SHA256: `ee92238cdb41d26529b4b712710e38db4837a441659e1ecd51096f9f80f7dfe1` ／ 1,969 bytes

| 原キー | 保存値 |
|---|---|
| original_train_tokens | 12225819077 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seed | 2026100622 |
| CPU_budget_seconds | 600.0 |
| source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_result.json — bounded_supply_comparison_complete_not_prepared_or_distinct</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_result.json) ／ SHA256: `86ae69905ac9c251c2848f3c1b512b751520024cf56a4e289db0e16e59182df8` ／ 3,002 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_supply_comparison_complete_not_prepared_or_distinct" |
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |
| estimates.first_eligible_unit.estimated_train_tokens | 1048561247.8222233 |
| estimates.first_eligible_unit.bootstrap_ci95 | [989974070.2384483, 1109702142.1953793] |
| estimates.all_eligible_first32.estimated_train_tokens | 2213306228.7708454 |
| estimates.all_eligible_first32.bootstrap_ci95 | [2136527286.8689826, 2292379994.652727] |
| target_web_train_tokens | 1900000000 |
| new_prepared_tokens | 0 |
| GPU_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| CPU_seconds | 1.453696864991798 |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first32_sample32.json — None</summary>

[原記録](../../reports/phase6/larger_web_supply_first32_sample32.json) ／ SHA256: `50d7f81a7e754abe0ec5511ffc632bc26b3f49c910b61d612680a59e738c5ef0` ／ 75,974 bytes

| 原キー | 保存値 |
|---|---|
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first4_job.json — complete</summary>

[原記録](../../reports/phase6/larger_web_supply_first4_job.json) ／ SHA256: `5d8762892d505e82795da0c161faef38e6a5996059bfa7f1ca8922a6b9c23dab` ／ 2,366 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |
| CPU_seconds | 3.3681155590020353 |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first4_recipe.json — None</summary>

[原記録](../../reports/phase6/larger_web_supply_first4_recipe.json) ／ SHA256: `517e1596a3ccb22a484bf4d3f812e8e436ec64e9798b30703adfbd7ef3a89598` ／ 1,969 bytes

| 原キー | 保存値 |
|---|---|
| original_train_tokens | 12225819077 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| seed | 2026100622 |
| CPU_budget_seconds | 600.0 |
| source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first4_result.json — bounded_supply_comparison_complete_not_prepared_or_distinct</summary>

[原記録](../../reports/phase6/larger_web_supply_first4_result.json) ／ SHA256: `39c8600e48598c77784c9d850777a85a285c260e42f7fd6b09cf82a47c427bb3` ／ 3,008 bytes

| 原キー | 保存値 |
|---|---|
| status | "bounded_supply_comparison_complete_not_prepared_or_distinct" |
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |
| estimates.first_eligible_unit.estimated_train_tokens | 1048561247.8222233 |
| estimates.first_eligible_unit.bootstrap_ci95 | [989974070.2384483, 1109702142.1953793] |
| estimates.all_eligible_first_four.estimated_train_tokens | 1325096202.7248025 |
| estimates.all_eligible_first_four.bootstrap_ci95 | [1258366941.8450072, 1394775053.5696075] |
| target_web_train_tokens | 1900000000 |
| new_prepared_tokens | 0 |
| GPU_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| requested_five_steps_complete | false |
| CPU_seconds | 3.3678280110034393 |

</details>

<details>
<summary>reports/phase6/larger_web_supply_first4_sample32.json — None</summary>

[原記録](../../reports/phase6/larger_web_supply_first4_sample32.json) ／ SHA256: `283bce1a01e141f90d455fc63091570685a33a3ae8e1e043d09e2fb7eae28278` ／ 85,102 bytes

| 原キー | 保存値 |
|---|---|
| binding.original_train_tokens | 12225819077 |
| binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| binding.seed | 2026100622 |
| binding.CPU_budget_seconds | 600.0 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.sample_policy | "Uniform native token offsets; containing BOS/EOS record; selected train tokens/original record tokens; oversized ineligible documents contribute zero" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-20261006/probe/job.json — failed_or_interrupted</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-20261006/probe/job.json) ／ SHA256: `621244d374d6c1b6bff1a18df6291516b9a32abac4677988a10a543cc5694f56` ／ 759 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed_or_interrupted" |
| GPU_elapsed_seconds | 1.419417480006814 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/authored_news/training/latest.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/authored_news/training/latest.json) ／ SHA256: `999a574d626c4119da49782c8e469a1d286f4359da956deb49bdffdc1431b468` ／ 289 bytes

| 原キー | 保存値 |
|---|---|
| update | 323499 |
| tokens_seen | 10600415232 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/compare-result.json — news100M_GPU_complete_pending_all80_content</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/compare-result.json) ／ SHA256: `a14c85b75bc3d21174e9570f5ab5291bed08296224712e14ffc66a051c28e40c` ／ 637,347 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.authored_news.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/authored_news/training/checkpoint-00323499.pt" |
| checkpoints.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| checkpoints.authored_news.binding.config_sha256 | "9e27df5b8ea2ba6aadb2e8fd1bc48f052a68b743ddd6f991a17ab89e64132d6e" |
| checkpoints.authored_news.binding.arm | "authored_news" |
| checkpoints.authored_news.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00322685.pt" |
| checkpoints.authored_news.binding.parent.sha256 | "1398ad1364d60e88382bca26e711e45b8b981275dc56d77fdae295674df297c7" |
| checkpoints.authored_news.binding.original_parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.authored_news.binding.original_parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.authored_news.binding.teacher_goals.web | 1428122 |
| checkpoints.authored_news.binding.teacher_goals.authored_news | 25000000 |
| checkpoints.authored_news.binding.study_kind | "authored_Japanese_news_vs_synthetic_native_Base100M_v1" |
| checkpoints.authored_news.binding.optimizer_policy | "inherit_native" |
| checkpoints.authored_news.binding.scientific | true |
| checkpoints.authored_news.update | 323499 |
| checkpoints.authored_news.tokens | 10600415232 |
| checkpoints.authored_news.supervised_tokens | 10577786961 |
| checkpoints.authored_news.additional_supervised_tokens | 26428122 |
| checkpoints.authored_news.additional_input_tokens | 26673152 |
| checkpoints.authored_news.source_teachers.web | 1428122 |
| checkpoints.authored_news.source_teachers.authored_news | 25000000 |
| checkpoints.authored_news.source_eos.web | 3064 |
| checkpoints.authored_news.source_eos.authored_news | 238510 |
| checkpoints.authored_news.source_input_tokens.web | 1434624 |
| checkpoints.authored_news.source_input_tokens.authored_news | 25238528 |
| checkpoints.authored_news.source_focus_teachers.web | 0 |
| checkpoints.authored_news.source_focus_teachers.authored_news | 0 |
| checkpoints.authored_news.focus_teacher_tokens | 0 |
| checkpoints.authored_news.focus_token_digest | "179baab1310e5fefbd4b7a09268deaadddd0308d06e996169063717ac048e9b1" |
| checkpoints.authored_news.weighted_teacher_mass | 26428122 |
| checkpoints.authored_news.outcome_weight | 1 |
| checkpoints.authored_news.training_seconds | 45.90560058527626 |
| checkpoints.authored_news.completed_at | "2026-10-06T14:29:11.203754Z" |
| checkpoints.authored_news.sampler.kind | "exact_staged_Web_then_authored_news_quota_v1" |
| checkpoints.authored_news.sampler.goals.web | 1428122 |
| checkpoints.authored_news.sampler.goals.authored_news | 25000000 |
| checkpoints.authored_news.sampler.source_order | ["web", "authored_news"] |
| checkpoints.authored_news.sampler.context | 1024 |
| checkpoints.authored_news.sampler.seed | 42 |
| checkpoints.authored_news.sampler.position | 814 |
| checkpoints.authored_news.sampler.source_teachers.web | 1428122 |
| checkpoints.authored_news.sampler.source_teachers.authored_news | 25000000 |
| checkpoints.authored_news.sampler.source_eos.web | 3064 |
| checkpoints.authored_news.sampler.source_eos.authored_news | 238510 |
| checkpoints.authored_news.sampler.source_tokens.web | 1434624 |
| checkpoints.authored_news.sampler.source_tokens.authored_news | 25238528 |
| checkpoints.authored_news.sampler.source_body_bytes.web | 5562565 |
| checkpoints.authored_news.sampler.source_body_bytes.authored_news | 92210860 |
| checkpoints.authored_news.sampler.source_focus_teachers.web | 0 |
| checkpoints.authored_news.sampler.source_focus_teachers.authored_news | 0 |
| checkpoints.authored_news.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.authored_news.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.authored_news.sampler.streams.web.sampler.seed | 42 |
| checkpoints.authored_news.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.authored_news.sampler.streams.web.sampler.position | 10327321 |
| checkpoints.authored_news.sampler.streams.web.sampler.context | 1024 |
| checkpoints.authored_news.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.authored_news.sampler.streams.authored_news.kind | "fresh_authored_news_contiguous_block_shuffle_v1" |
| checkpoints.authored_news.sampler.streams.authored_news.manifest_sha256 | "600d8e04e0ea266aef6d7180b6e95639f7260e910dc6a55b7a6ae7eeb7c38bfa" |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.seed | 42 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.epoch | 47 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.position | 160 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.context | 1024 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.blocks | 521 |
| checkpoints.authored_news.source_body_bytes.web | 5562565 |
| checkpoints.authored_news.source_body_bytes.authored_news | 92210860 |
| checkpoints.authored_news.token_digest | "7a1d151a6be3cc79ca9143fa703e0ef02e89c203eb91b734e6418bce13ece3f9" |
| checkpoints.authored_news.model_config.schema_version | 1 |
| checkpoints.authored_news.model_config.architecture | "decoder_only_transformer" |
| checkpoints.authored_news.model_config.hidden_size | 256 |
| checkpoints.authored_news.model_config.num_attention_heads | 4 |
| checkpoints.authored_news.model_config.num_key_value_heads | 2 |
| checkpoints.authored_news.model_config.head_dim | 64 |
| checkpoints.authored_news.model_config.activation | "swiglu" |
| checkpoints.authored_news.model_config.norm | "rmsnorm" |
| checkpoints.authored_news.model_config.rms_norm_eps | 1e-06 |
| checkpoints.authored_news.model_config.qk_norm_type | "none" |
| checkpoints.authored_news.model_config.qk_norm_before_rope | true |
| checkpoints.authored_news.model_config.attention_scale | 0.125 |
| checkpoints.authored_news.model_config.rope_theta | 10000 |
| checkpoints.authored_news.model_config.rope_layout | "half_split" |
| checkpoints.authored_news.model_config.rotary_dim | 64 |
| checkpoints.authored_news.model_config.max_position_embeddings | 1024 |
| checkpoints.authored_news.model_config.tie_word_embeddings | true |
| checkpoints.authored_news.model_config.attention_bias | false |
| checkpoints.authored_news.model_config.mlp_bias | false |
| checkpoints.authored_news.model_config.dropout | 0.0 |
| checkpoints.authored_news.model_config.initializer_std | 0.02 |
| checkpoints.authored_news.model_config.norm_initial_gain | 1.0 |
| checkpoints.authored_news.model_config.status | "phase5_ablation" |
| checkpoints.authored_news.model_config.name | "JMicro-10M-T4K-NoQKNorm" |
| checkpoints.authored_news.model_config.vocab_size | 4096 |
| checkpoints.authored_news.model_config.num_hidden_layers | 13 |
| checkpoints.authored_news.model_config.intermediate_size | 640 |
| checkpoints.authored_news.model_config.expected_parameter_count | 10001152 |
| checkpoints.authored_news.unique_parameters | 10001152 |
| checkpoints.authored_news.reused_prefix_teacher_tokens | 73571878 |
| checkpoints.authored_news.total_teacher_tokens_from_original_parent | 100000000 |
| checkpoints.authored_news.pure_Web_continuation_matched_updates | 43 |
| evaluations.authored_news.binding.teacher_goals.web | 1428122 |
| evaluations.authored_news.binding.teacher_goals.authored_news | 25000000 |
| evaluations.authored_news.binding.scientific | true |
| evaluations.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| evaluations.authored_news.body.documents | 256 |
| evaluations.authored_news.body.limit_documents | 256 |
| evaluations.authored_news.body.body_nll | 334242.09346342087 |
| evaluations.authored_news.body.eos_nll | 314.84866300038993 |
| evaluations.authored_news.body.body_bytes | 472055 |
| evaluations.authored_news.body.body_tokens | 122343 |
| evaluations.authored_news.body.bpb | 1.0215110753959236 |
| evaluations.authored_news.body.seconds | 1.6565144920023158 |
| evaluations.authored_news.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.authored_news.generation.max_new_tokens | 64 |
| evaluations.authored_news.greedy_rates.eos | 49 |
| evaluations.authored_news.greedy_rates.repetition | 24 |
| evaluations.authored_news.greedy_rates.unicode_failure | 0 |
| evaluations.authored_news.greedy_rates.role_leak | 0 |
| evaluations.authored_news.greedy_rates.empty | 0 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.point | 0.59375 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.640625] |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.6354166666666666] |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5884411884411884 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.mcc | 0.17716986318620467 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.authored_news.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.authored_news.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.point | 0.37890974084003576 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.ci95 | [0.3512064343163539, 0.4075067024128686] |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.primary.hard_accuracy | 0.37890974084003576 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3418230563002681 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.31500223413762285, 0.36907953529937443] |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.34100536204466153 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.mcc | 0.17689830849780755 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.authored_news.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.semantic_both_contexts.correct | 20 |
| evaluations.authored_news.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.authored_news.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.authored_news.protected_test_used | false |
| transfer.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| transfer.authored_news.checks.weights_unchanged | true |
| transfer.authored_news.checks.no_gradients | true |
| transfer.authored_news.checks.eval_mode | true |
| transfer.authored_news.checks.RNG_restored | true |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5859375 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 27 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 22 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 5 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.61328125 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 30 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 97 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6796875 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 24 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 39 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58203125 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 22 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 105 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.625 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 5 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 59 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| transfer.authored_news.optimizer_updates | 0 |
| transfer.authored_news.scientific_teacher_tokens | 0 |
| transfer.authored_news.protected_test_used | false |
| transfer.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| retention.authored_news.checks.weights_unchanged | true |
| retention.authored_news.checks.no_gradients | true |
| retention.authored_news.checks.eval_mode | true |
| retention.authored_news.checks.RNG_restored | true |
| retention.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5703125 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 24 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.625 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 17 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.5625 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 19 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 106 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 78 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6015625 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 13 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 51 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.515625 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 10 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 80 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 9 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 1 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 57 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 37 |
| retention.authored_news.optimizer_updates | 0 |
| retention.authored_news.scientific_teacher_tokens | 0 |
| retention.authored_news.protected_test_used | false |
| retention.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| status | "news100M_GPU_complete_pending_all80_content" |
| GPU_seconds | 115.1166807099944 |
| scientific_teacher_tokens | 26428122 |
| reused_prefix_teacher_tokens | 73571878 |
| total_teacher_tokens_from_original_parent | 100000000 |
| exact_same_scientific_sources_as_control | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/content-notes.json) ／ SHA256: `9f338300b1275a5bbdacef5c9082a26c2f7b0522cf497b2c3939354aa62e199b` ／ 22,154 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/body.json) ／ SHA256: `aa2e0d991409fa05f42a58716c8107ad2b576a3a7227d71af5056808e019ce9f` ／ 67,223 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 334242.09346342087 |
| body.eos_nll | 314.84866300038993 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0215110753959236 |
| body.seconds | 1.6565144920023158 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/generation.json) ／ SHA256: `b70889bac6cf7f171c11a4e00f1efae155efbe498d6df19bd473bca0e3412b98` ／ 83,524 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/jblimp.json) ／ SHA256: `2ee5173a145c6032a6b58e314d8662e330df7fdf93bc55d5c2e8d894cb35da12` ／ 338,339 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.770392749244713 |
| summary.primary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.770392749244713 |
| summary.per_token_secondary.accuracy.point | 0.716012084592145 |
| summary.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.716012084592145 |
| summary.per_token_secondary.macro_f1 | 0.41725352112676056 |
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
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/jcqa.json) ／ SHA256: `9d3d857109ee5cf3782e8cfe048947ecf1cfad62650241451482ea609081ebca` ／ 1,640,376 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.37890974084003576 |
| summary.primary.accuracy.ci95 | [0.3512064343163539, 0.4075067024128686] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.37890974084003576 |
| summary.per_token_secondary.accuracy.point | 0.3418230563002681 |
| summary.per_token_secondary.accuracy.ci95 | [0.31500223413762285, 0.36907953529937443] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| summary.per_token_secondary.macro_f1 | 0.34100536204466153 |
| summary.per_token_secondary.mcc | 0.17689830849780755 |
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
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/result.json) ／ SHA256: `52b4111a700937201d57b813c0be1a803e5d6c52467170f5a0c1e7834c468aef` ／ 177,342 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 1428122 |
| binding.teacher_goals.authored_news | 25000000 |
| binding.scientific | true |
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 334242.09346342087 |
| body.eos_nll | 314.84866300038993 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0215110753959236 |
| body.seconds | 1.6565144920023158 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 49 |
| greedy_rates.repetition | 24 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.59375 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.640625] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.6354166666666666] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5884411884411884 |
| diagnostics.semantics.per_token_secondary.mcc | 0.17716986318620467 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| diagnostics.jcqa.primary.accuracy.point | 0.37890974084003576 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3512064343163539, 0.4075067024128686] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.37890974084003576 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3418230563002681 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.31500223413762285, 0.36907953529937443] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.34100536204466153 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.17689830849780755 |
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
| diagnostics.semantic_both_contexts.correct | 20 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>
