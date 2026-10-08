# 学習目的・最適化・正則化 — 16/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/compare-result.json — matched_low_alpha_learning_complete_pending_all80_content</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/compare-result.json) ／ SHA256: `cae85e04aca89793f4f941c286ffe3169ebe01e5253e5bf4a697e82469652a7a` ／ 465,044 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.CE.status | "complete" |
| checkpoints.CE.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/CE/training/checkpoint-00032161.pt" |
| checkpoints.CE.checkpoint_sha256 | "66f9479dc56e756675a1e0db7d48b1533de16908594ce2c475213d3c58d0a7c4" |
| checkpoints.CE.binding.config_sha256 | "8b8de74892c885c1680cf2d7755074b9938809b66dae09f6e276ac446ff43d19" |
| checkpoints.CE.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-quantity-comparison-20261006/large-1000000000/decay/checkpoint-00031391.pt" |
| checkpoints.CE.binding.parent.sha256 | "fb3c725944d820549a3d3c7c6c4ddde75ee536288d351a92e9e0b6e20e513c56" |
| checkpoints.CE.binding.parent.update | 31391 |
| checkpoints.CE.binding.parent.tokens_seen | 1028620288 |
| checkpoints.CE.binding.parent.supervised_tokens | 1020000000 |
| checkpoints.CE.binding.arm | "CE" |
| checkpoints.CE.binding.peak_lr | 0.0002 |
| checkpoints.CE.binding.warmup_updates | 0 |
| checkpoints.CE.binding.optimizer_policy | "inherit" |
| checkpoints.CE.binding.initialization | "completed-parent-objective-fork" |
| checkpoints.CE.binding.curve_mode | "decay" |
| checkpoints.CE.binding.curve_boundaries | [25000000] |
| checkpoints.CE.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.CE.binding.sequence_objective.alpha | 0.0 |
| checkpoints.CE.binding.sequence_objective.every_updates | 4 |
| checkpoints.CE.binding.sequence_objective.prefixes | 8 |
| checkpoints.CE.binding.sequence_objective.prefix_tokens | 32 |
| checkpoints.CE.binding.sequence_objective.max_new_tokens | 64 |
| checkpoints.CE.binding.sequence_objective.ngram | 4 |
| checkpoints.CE.update | 32161 |
| checkpoints.CE.tokens | 1053851648 |
| checkpoints.CE.supervised_tokens | 1045000000 |
| checkpoints.CE.additional_supervised_tokens | 25000000 |
| checkpoints.CE.additional_input_tokens | 25231360 |
| checkpoints.CE.physical_input_tokens | 25231360 |
| checkpoints.CE.source_eos_teachers.web | 0 |
| checkpoints.CE.source_eos_teachers.short | 210607 |
| checkpoints.CE.sampler.kind | "teacher-learning-curve-v1" |
| checkpoints.CE.sampler.mode | "shuffle" |
| checkpoints.CE.sampler.goals.web | 0 |
| checkpoints.CE.sampler.goals.short | 25000000 |
| checkpoints.CE.sampler.position | 770 |
| checkpoints.CE.sampler.web.seed | 42 |
| checkpoints.CE.sampler.web.epoch | 0 |
| checkpoints.CE.sampler.web.position | 0 |
| checkpoints.CE.sampler.web.context | 1024 |
| checkpoints.CE.sampler.web.blocks | 11939276 |
| checkpoints.CE.sampler.short.seed | 42 |
| checkpoints.CE.sampler.short.epoch | 0 |
| checkpoints.CE.sampler.short.position | 1029152 |
| checkpoints.CE.sampler.short.context | 1024 |
| checkpoints.CE.sampler.short.blocks | 1953126 |
| checkpoints.CE.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| checkpoints.CE.sampler.source_tokens.web | 0 |
| checkpoints.CE.sampler.source_tokens.short | 25231360 |
| checkpoints.CE.sampler.source_physical_tokens.web | 0 |
| checkpoints.CE.sampler.source_physical_tokens.short | 25231360 |
| checkpoints.CE.sampler.source_teachers.web | 0 |
| checkpoints.CE.sampler.source_teachers.short | 25000000 |
| checkpoints.CE.sampler.source_eos.web | 0 |
| checkpoints.CE.sampler.source_eos.short | 210607 |
| checkpoints.CE.sampler.boundaries | [25000000] |
| checkpoints.CE.sampler.genre_teachers.web | 18789411 |
| checkpoints.CE.sampler.genre_teachers.story | 1213024 |
| checkpoints.CE.sampler.genre_teachers.textbook | 4997565 |
| checkpoints.CE.sampler.genre_eos.web | 164144 |
| checkpoints.CE.sampler.genre_eos.story | 9399 |
| checkpoints.CE.sampler.genre_eos.textbook | 37064 |
| checkpoints.CE.sampler.genre_tag_mapping.web | 0 |
| checkpoints.CE.sampler.genre_tag_mapping.story | 1 |
| checkpoints.CE.sampler.genre_tag_mapping.textbook | 2 |
| checkpoints.CE.genre_teachers.web | 18789411 |
| checkpoints.CE.genre_teachers.story | 1213024 |
| checkpoints.CE.genre_teachers.textbook | 4997565 |
| checkpoints.CE.genre_eos.web | 164144 |
| checkpoints.CE.genre_eos.story | 9399 |
| checkpoints.CE.genre_eos.textbook | 37064 |
| checkpoints.CE.training_step_seconds | 272.65248792318744 |
| checkpoints.CE.timing_policy | "Sum completed metric update seconds; compile within step included, constructor/saving/evaluation excluded; total occupancy separately recorded" |
| checkpoints.CE.peak_allocated_bytes | 6148549120 |
| checkpoints.CE.sequence_objective.source_sha256.scripts/sequence_objective_trainer.py | "035b08caf9c5f96885ae9599802e9e777ebfc79a3473614085a9dfafebee58ce" |
| checkpoints.CE.sequence_objective.source_sha256.src/jmicro/sequence_unlikelihood.py | "3d54c3544e4e59f086459ce6053e342aa3133c39b990dae48ea1131f084e6cf3" |
| checkpoints.CE.sequence_objective.parent_actual_curve_mode | "decay" |
| checkpoints.CE.sequence_objective.objective.alpha | 0.0 |
| checkpoints.CE.sequence_objective.objective.every_updates | 4 |
| checkpoints.CE.sequence_objective.objective.prefixes | 8 |
| checkpoints.CE.sequence_objective.objective.prefix_tokens | 32 |
| checkpoints.CE.sequence_objective.objective.max_new_tokens | 64 |
| checkpoints.CE.sequence_objective.objective.ngram | 4 |
| checkpoints.CE.sequence_objective.rollout_batches | 192 |
| checkpoints.CE.sequence_objective.skipped_rollouts | 0 |
| checkpoints.CE.sequence_objective.generated_continuations | 1536 |
| checkpoints.CE.sequence_objective.generated_body_tokens | 50320 |
| checkpoints.CE.sequence_objective.generated_EOS | 1137 |
| checkpoints.CE.sequence_objective.negative_token_positions | 17423 |
| checkpoints.CE.sequence_objective.extra_valid_input_tokens | 200386 |
| checkpoints.CE.sequence_objective.extra_physical_input_tokens | 288992 |
| checkpoints.CE.sequence_objective.generated_digest | "b17429c03781aadf3f8af88f48f1885fa9d646f41efc162bb91ea7c0d5d769b5" |
| checkpoints.CE_UL.status | "complete" |
| checkpoints.CE_UL.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-low-alpha-20261006/CE_UL/training/checkpoint-00032161.pt" |
| checkpoints.CE_UL.checkpoint_sha256 | "f1a95ec6a95293c0fecc5c5033c68b0da5fffe38d760234876ae846a003f3a5d" |
| checkpoints.CE_UL.binding.config_sha256 | "cc53b0f7fda68282977ec535d54cbdfa962558085c5cc51eb185c39fe1f57925" |
| checkpoints.CE_UL.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-quantity-comparison-20261006/large-1000000000/decay/checkpoint-00031391.pt" |
| checkpoints.CE_UL.binding.parent.sha256 | "fb3c725944d820549a3d3c7c6c4ddde75ee536288d351a92e9e0b6e20e513c56" |
| checkpoints.CE_UL.binding.parent.update | 31391 |
| checkpoints.CE_UL.binding.parent.tokens_seen | 1028620288 |
| checkpoints.CE_UL.binding.parent.supervised_tokens | 1020000000 |
| checkpoints.CE_UL.binding.arm | "CE_UL" |
| checkpoints.CE_UL.binding.peak_lr | 0.0002 |
| checkpoints.CE_UL.binding.warmup_updates | 0 |
| checkpoints.CE_UL.binding.optimizer_policy | "inherit" |
| checkpoints.CE_UL.binding.initialization | "completed-parent-objective-fork" |
| checkpoints.CE_UL.binding.curve_mode | "decay" |
| checkpoints.CE_UL.binding.curve_boundaries | [25000000] |
| checkpoints.CE_UL.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.CE_UL.binding.sequence_objective.alpha | 0.01 |
| checkpoints.CE_UL.binding.sequence_objective.every_updates | 4 |
| checkpoints.CE_UL.binding.sequence_objective.prefixes | 8 |
| checkpoints.CE_UL.binding.sequence_objective.prefix_tokens | 32 |
| checkpoints.CE_UL.binding.sequence_objective.max_new_tokens | 64 |
| checkpoints.CE_UL.binding.sequence_objective.ngram | 4 |
| checkpoints.CE_UL.update | 32161 |
| checkpoints.CE_UL.tokens | 1053851648 |
| checkpoints.CE_UL.supervised_tokens | 1045000000 |
| checkpoints.CE_UL.additional_supervised_tokens | 25000000 |
| checkpoints.CE_UL.additional_input_tokens | 25231360 |
| checkpoints.CE_UL.physical_input_tokens | 25231360 |
| checkpoints.CE_UL.source_eos_teachers.web | 0 |
| checkpoints.CE_UL.source_eos_teachers.short | 210607 |
| checkpoints.CE_UL.sampler.kind | "teacher-learning-curve-v1" |
| checkpoints.CE_UL.sampler.mode | "shuffle" |
| checkpoints.CE_UL.sampler.goals.web | 0 |
| checkpoints.CE_UL.sampler.goals.short | 25000000 |
| checkpoints.CE_UL.sampler.position | 770 |
| checkpoints.CE_UL.sampler.web.seed | 42 |
| checkpoints.CE_UL.sampler.web.epoch | 0 |
| checkpoints.CE_UL.sampler.web.position | 0 |
| checkpoints.CE_UL.sampler.web.context | 1024 |
| checkpoints.CE_UL.sampler.web.blocks | 11939276 |
| checkpoints.CE_UL.sampler.short.seed | 42 |
| checkpoints.CE_UL.sampler.short.epoch | 0 |
| checkpoints.CE_UL.sampler.short.position | 1029152 |
| checkpoints.CE_UL.sampler.short.context | 1024 |
| checkpoints.CE_UL.sampler.short.blocks | 1953126 |
| checkpoints.CE_UL.sampler.short.mode | "lazy-shuffle-whole-documents-v1" |
| checkpoints.CE_UL.sampler.source_tokens.web | 0 |
| checkpoints.CE_UL.sampler.source_tokens.short | 25231360 |
| checkpoints.CE_UL.sampler.source_physical_tokens.web | 0 |
| checkpoints.CE_UL.sampler.source_physical_tokens.short | 25231360 |
| checkpoints.CE_UL.sampler.source_teachers.web | 0 |
| checkpoints.CE_UL.sampler.source_teachers.short | 25000000 |
| checkpoints.CE_UL.sampler.source_eos.web | 0 |
| checkpoints.CE_UL.sampler.source_eos.short | 210607 |
| checkpoints.CE_UL.sampler.boundaries | [25000000] |
| checkpoints.CE_UL.sampler.genre_teachers.web | 18789411 |
| checkpoints.CE_UL.sampler.genre_teachers.story | 1213024 |
| checkpoints.CE_UL.sampler.genre_teachers.textbook | 4997565 |
| checkpoints.CE_UL.sampler.genre_eos.web | 164144 |
| checkpoints.CE_UL.sampler.genre_eos.story | 9399 |
| checkpoints.CE_UL.sampler.genre_eos.textbook | 37064 |
| checkpoints.CE_UL.sampler.genre_tag_mapping.web | 0 |
| checkpoints.CE_UL.sampler.genre_tag_mapping.story | 1 |
| checkpoints.CE_UL.sampler.genre_tag_mapping.textbook | 2 |
| checkpoints.CE_UL.genre_teachers.web | 18789411 |
| checkpoints.CE_UL.genre_teachers.story | 1213024 |
| checkpoints.CE_UL.genre_teachers.textbook | 4997565 |
| checkpoints.CE_UL.genre_eos.web | 164144 |
| checkpoints.CE_UL.genre_eos.story | 9399 |
| checkpoints.CE_UL.genre_eos.textbook | 37064 |
| checkpoints.CE_UL.training_step_seconds | 271.35607420913584 |
| checkpoints.CE_UL.timing_policy | "Sum completed metric update seconds; compile within step included, constructor/saving/evaluation excluded; total occupancy separately recorded" |
| checkpoints.CE_UL.peak_allocated_bytes | 6148549120 |
| checkpoints.CE_UL.sequence_objective.source_sha256.scripts/sequence_objective_trainer.py | "035b08caf9c5f96885ae9599802e9e777ebfc79a3473614085a9dfafebee58ce" |
| checkpoints.CE_UL.sequence_objective.source_sha256.src/jmicro/sequence_unlikelihood.py | "3d54c3544e4e59f086459ce6053e342aa3133c39b990dae48ea1131f084e6cf3" |
| checkpoints.CE_UL.sequence_objective.parent_actual_curve_mode | "decay" |
| checkpoints.CE_UL.sequence_objective.objective.alpha | 0.01 |
| checkpoints.CE_UL.sequence_objective.objective.every_updates | 4 |
| checkpoints.CE_UL.sequence_objective.objective.prefixes | 8 |
| checkpoints.CE_UL.sequence_objective.objective.prefix_tokens | 32 |
| checkpoints.CE_UL.sequence_objective.objective.max_new_tokens | 64 |
| checkpoints.CE_UL.sequence_objective.objective.ngram | 4 |
| checkpoints.CE_UL.sequence_objective.rollout_batches | 192 |
| checkpoints.CE_UL.sequence_objective.skipped_rollouts | 0 |
| checkpoints.CE_UL.sequence_objective.generated_continuations | 1536 |
| checkpoints.CE_UL.sequence_objective.generated_body_tokens | 63633 |
| checkpoints.CE_UL.sequence_objective.generated_EOS | 980 |
| checkpoints.CE_UL.sequence_objective.negative_token_positions | 23965 |
| checkpoints.CE_UL.sequence_objective.extra_valid_input_tokens | 226370 |
| checkpoints.CE_UL.sequence_objective.extra_physical_input_tokens | 290656 |
| checkpoints.CE_UL.sequence_objective.generated_digest | "5daca697f676eee71103bb2034c4d91363c98c8cd650bfee76134e49f4e78507" |
| evaluations.CE.binding.parent.update | 31391 |
| evaluations.CE.binding.parent.tokens_seen | 1028620288 |
| evaluations.CE.binding.parent.supervised_tokens | 1020000000 |
| evaluations.CE.binding.warmup_updates | 0 |
| evaluations.CE.binding.sequence_objective.every_updates | 4 |
| evaluations.CE.binding.sequence_objective.prefix_tokens | 32 |
| evaluations.CE.binding.sequence_objective.max_new_tokens | 64 |
| evaluations.CE.checkpoint_sha256 | "66f9479dc56e756675a1e0db7d48b1533de16908594ce2c475213d3c58d0a7c4" |
| evaluations.CE.body.documents | 256 |
| evaluations.CE.body.limit_documents | 256 |
| evaluations.CE.body.body_nll | 375666.16901397705 |
| evaluations.CE.body.eos_nll | 975.2455942928791 |
| evaluations.CE.body.body_bytes | 472055 |
| evaluations.CE.body.body_tokens | 122343 |
| evaluations.CE.body.bpb | 1.1481113833477452 |
| evaluations.CE.body.seconds | 1.1879455629969016 |
| evaluations.CE.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.CE.generation.max_new_tokens | 64 |
| evaluations.CE.greedy_rates.eos | 42 |
| evaluations.CE.greedy_rates.repetition | 18 |
| evaluations.CE.greedy_rates.unicode_failure | 0 |
| evaluations.CE.greedy_rates.role_leak | 0 |
| evaluations.CE.greedy_rates.empty | 0 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.ci95 | [0.4895833333333333, 0.5677083333333334] |
| evaluations.CE.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.536328125, 0.6354166666666666] |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5829260345389378 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.mcc | 0.16699314428937317 |
| evaluations.CE.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.CE.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.CE.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.CE.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.CE.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.point | 0.7945619335347432 |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.ci95 | [0.7522658610271903, 0.8368580060422961] |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.primary.hard_accuracy | 0.7945619335347432 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7341389728096677 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42334494773519166 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.CE.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.CE.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.CE.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.CE.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.CE.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE.diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.point | 0.3163538873994638 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.ci95 | [0.28865058087578194, 0.3413985701519212] |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jcqa.primary.hard_accuracy | 0.3163538873994638 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26541554959785524, 0.3154602323503128] |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.28973771095646506 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.mcc | 0.11341567261700596 |
| evaluations.CE.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.CE.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.CE.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.CE.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.CE.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE.diagnostics.semantic_both_contexts.correct | 10 |
| evaluations.CE.memory.maximum_observed_allocated_bytes | 308510720 |
| evaluations.CE.memory.maximum_observed_reserved_bytes | 9474932736 |
| evaluations.CE.protected_test_used | false |
| evaluations.CE_UL.binding.parent.update | 31391 |
| evaluations.CE_UL.binding.parent.tokens_seen | 1028620288 |
| evaluations.CE_UL.binding.parent.supervised_tokens | 1020000000 |
| evaluations.CE_UL.binding.warmup_updates | 0 |
| evaluations.CE_UL.binding.sequence_objective.every_updates | 4 |
| evaluations.CE_UL.binding.sequence_objective.prefix_tokens | 32 |
| evaluations.CE_UL.binding.sequence_objective.max_new_tokens | 64 |
| evaluations.CE_UL.checkpoint_sha256 | "f1a95ec6a95293c0fecc5c5033c68b0da5fffe38d760234876ae846a003f3a5d" |
| evaluations.CE_UL.body.documents | 256 |
| evaluations.CE_UL.body.limit_documents | 256 |
| evaluations.CE_UL.body.body_nll | 380776.64988803864 |
| evaluations.CE_UL.body.eos_nll | 969.3097665756941 |
| evaluations.CE_UL.body.body_bytes | 472055 |
| evaluations.CE_UL.body.body_tokens | 122343 |
| evaluations.CE_UL.body.bpb | 1.163730040948166 |
| evaluations.CE_UL.body.seconds | 1.1632371120067546 |
| evaluations.CE_UL.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.CE_UL.generation.max_new_tokens | 64 |
| evaluations.CE_UL.greedy_rates.eos | 28 |
| evaluations.CE_UL.greedy_rates.repetition | 32 |
| evaluations.CE_UL.greedy_rates.unicode_failure | 0 |
| evaluations.CE_UL.greedy_rates.role_leak | 0 |
| evaluations.CE_UL.greedy_rates.empty | 0 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.ci95 | [0.5416666666666666, 0.609375] |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.6510416666666666] |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6093644033312535 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.mcc | 0.21876186891295196 |
| evaluations.CE_UL.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.CE_UL.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.CE_UL.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.CE_UL.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.point | 0.7371601208459214 |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.ci95 | [0.6918429003021148, 0.7854984894259819] |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.primary.hard_accuracy | 0.7371601208459214 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.6676737160120846 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6163141993957704, 0.7190332326283988] |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.6676737160120846 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4003623188405797 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.CE_UL.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.CE_UL.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.CE_UL.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.CE_UL.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE_UL.diagnostics.jblimp.raw_pair_accuracy | 0.7311178247734139 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.point | 0.26988382484361034 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.ci95 | [0.24483914209115282, 0.2949061662198391] |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jcqa.primary.hard_accuracy | 0.26988382484361034 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.29222520107238603 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2680965147453083, 0.3199285075960679] |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.29222520107238603 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29132496270125 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.mcc | 0.11547593024040104 |
| evaluations.CE_UL.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.CE_UL.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.CE_UL.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.CE_UL.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.CE_UL.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.CE_UL.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.CE_UL.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.CE_UL.memory.maximum_observed_allocated_bytes | 308510720 |
| evaluations.CE_UL.memory.maximum_observed_reserved_bytes | 9474932736 |
| evaluations.CE_UL.protected_test_used | false |
| status | "matched_low_alpha_learning_complete_pending_all80_content" |
| new_scientific_teacher_tokens | 25000000 |
| compared_teacher_tokens | 50000000 |
| verification_teacher_tokens | 779980 |
| verification_GPU_seconds | 47.45826241499162 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| new_scientific_GPU_seconds | 366.1949579840002 |

</details>

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/evaluation/CE_UL/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/evaluation/CE_UL/evaluation/generation.json) ／ SHA256: `0467fe6333eb922978aa9b4e26a662a822317da42580682b898da611c422aaba` ／ 107,176 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/job.json) ／ SHA256: `67fc141e995e17bf0b9d3db1afe86e6a1631968c67e9b926a82a4fa32ed023a2` ／ 764 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| gpu_elapsed_seconds | 366.1949579840002 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 24695654 |
| teacher_budget | 25000000 |
| loss | 2.635779619216919 |

</details>

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/probe/job.json) ／ SHA256: `c7ca4d10ace1520bb8ff3166fdbc79af502cb40365aac064895f8f5f0a3b20ef` ／ 666 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| gpu_elapsed_seconds | 47.45826241499162 |
| Base_adopted | false |
| protected_test_used | false |
| index_documents | 16500000 |
| index_total_documents | 16693716 |
| completed_updates | 16 |

</details>

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/probe/result.json — actual_low_alpha_resume_and_continuous_timing_complete</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/probe/result.json) ／ SHA256: `539fa11c3eaf722ba94e146afaee7603518324f7246d3e97a5bb1788e982a38c` ／ 45,943 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_low_alpha_resume_and_continuous_timing_complete" |
| passed | true |
| gate.passed | true |
| gate.checks.model | true |
| gate.checks.optimizer | true |
| gate.checks.scheduler | true |
| gate.checks.rng | true |
| gate.checks.sampler | true |
| gate.checks.lineage | true |
| gate.checks.tokens | true |
| gate.checks.supervised_tokens | true |
| gate.checks.body_bytes | true |
| gate.checks.token_digest | true |
| gate.checks.update | true |
| gate.checks.spec | true |
| gate.checks.model_config | true |
| gate.checks.pilot_binding | true |
| gate.checks.history_loss | true |
| gate.checks.history_sequence_UL | true |
| gate.checks.history_optimization_loss | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_lr | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_sequence_objective | true |
| gate.checks.finite | true |
| gate.checks.actual_rollout | true |
| gate.checks.unchanged_control_input_trajectory | true |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 260038 |
| gate.verification_input_tokens | 262144 |
| timing.GPU_optimizer_updates | 16 |
| timing.verification_teacher_tokens | 519942 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-low-alpha-20261006/probe/timing/checkpoint-00031407.pt" |
| timing.checkpoint_sha256 | "4f0f88543b4551299d230d6f98841cf1773ff60129d2ac2d11d746aca0605323" |
| verification_teacher_tokens | 779980 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 47.45826241499162 |

</details>

<details>
<summary>reports/phase6/sequence-objective-low-alpha-20261006/review.json — matched_reused_CE_and_actual_low_alpha25M_all80_complete</summary>

[原記録](../../reports/phase6/sequence-objective-low-alpha-20261006/review.json) ／ SHA256: `7e22e03ae51e402c65cbf8c769596be93c51c356039cd904f05d5515c1285257` ／ 3,263 bytes

| 原キー | 保存値 |
|---|---|
| status | "matched_reused_CE_and_actual_low_alpha25M_all80_complete" |
| summary.CE_teachers | 25000000 |
| summary.BPB | 1.163730040948166 |
| summary.rates.eos | 28 |
| summary.rates.repetition | 32 |
| summary.rates.unicode_failure | 0 |
| summary.rates.role_leak | 0 |
| summary.rates.empty | 0 |
| summary.grammar2 | 29 |
| summary.relevance2 | 13 |
| summary.coherent | 7 |
| summary.appropriate | 10 |
| summary.notes_sha256 | "f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5" |
| summary.Base_adopted | false |
| objective_comparison.checks.coherence_gain_at_least8 | false |
| objective_comparison.checks.paired_CI_lower_above0 | false |
| objective_comparison.checks.EOS_nonworsening | false |
| objective_comparison.checks.repetition_nonworsening | false |
| objective_comparison.checks.no_empty_role_unicode | true |
| objective_comparison.checks.BPB_gate | false |
| objective_comparison.checks.appropriate_completion_not_punctuation | true |
| objective_comparison.passed | false |
| practical.checks.grammar_at_least56 | false |
| practical.checks.coherence_at_least27 | false |
| practical.checks.appropriate_at_least27 | false |
| practical.checks.EOS_at_least37 | false |
| practical.checks.repetition_at_most18 | false |
| practical.checks.no_empty_role_unicode | true |
| practical.original_Web.EOS_at_least8_more | true |
| practical.original_Web.repetition_no_worse | true |
| practical.original_Web.no_empty_role_unicode | true |
| practical.original_Web.BPB_degradation_at_most1percent | false |
| practical.absolute_screen_pass | false |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| compared_teacher_tokens | 50000000 |
| verification_teacher_tokens | 779980 |
| new_scientific_GPU_seconds | 366.1949579840002 |
| verification_GPU_seconds | 47.45826241499162 |
| extra_generation_accounting.objective.every_updates | 4 |
| extra_generation_accounting.objective.prefix_tokens | 32 |
| extra_generation_accounting.objective.max_new_tokens | 64 |
| extra_generation_accounting.skipped_rollouts | 0 |
| extra_generation_accounting.generated_body_tokens | 63633 |
| extra_generation_accounting.generated_EOS | 980 |
| extra_generation_accounting.negative_token_positions | 23965 |
| extra_generation_accounting.extra_valid_input_tokens | 226370 |
| extra_generation_accounting.extra_physical_input_tokens | 290656 |
| notes_sha256 | "f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5" |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_UL_candidate_inspection.json — saved_raw_repetition_candidates_inspected_no_model_update</summary>

[原記録](../../reports/phase6/sequence_objective_CE_UL_candidate_inspection.json) ／ SHA256: `677d33e71cae310c74cab04b9f94372f08995ca42875176454c5e870f9b5e1d8` ／ 19,553 bytes

| 原キー | 保存値 |
|---|---|
| status | "saved_raw_repetition_candidates_inspected_no_model_update" |
| notes.path | "reports/phase6/sequence_objective_CE_UL_notes.json" |
| notes.sha256 | "62082d5592ba0bd0c73e457b542682feed516684c6df48ee7134a6ea6617bb98" |
| candidate_tokens | 1178 |
| candidate_rows_with_coherence2 | 0 |
| noncandidate_rows_with_coherence_below2 | 13 |
| candidate_rows_with_appropriate_completion | 4 |
| interpretation | "Generated 4-gram candidates are not a new failure threshold; legitimate repeats can exist. Noncandidate incoherence cannot be assumed fixed by repetition loss." |
| science_teacher_tokens | 0 |
| GPU_training_updates | 0 |
| protected_test_used | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_UL_content_review.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_UL_content_review.json) ／ SHA256: `9918947069fc13a14118defed2405646665ec419cce493121250e3b7db244483` ／ 629 bytes

| 原キー | 保存値 |
|---|---|
| CE_teachers | 25000000 |
| BPB | 1.2457162146538936 |
| rates.eos | 32 |
| rates.repetition | 7 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 20 |
| relevance2 | 6 |
| coherent | 0 |
| appropriate | 6 |
| notes_sha256 | "62082d5592ba0bd0c73e457b542682feed516684c6df48ee7134a6ea6617bb98" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_UL_generation.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_UL_generation.json) ／ SHA256: `1ab29bb9e456243d49bbdbf5f3e3e39f083d300770866dab8ae4c19bdb511396` ／ 112,703 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_UL_notes.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_UL_notes.json) ／ SHA256: `62082d5592ba0bd0c73e457b542682feed516684c6df48ee7134a6ea6617bb98` ／ 18,057 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_candidate_inspection.json — saved_raw_repetition_candidates_inspected_no_model_update</summary>

[原記録](../../reports/phase6/sequence_objective_CE_candidate_inspection.json) ／ SHA256: `a6e969563f7cc425447b1705c74756722e1cdac161868a9258de28ffbfff219d` ／ 19,481 bytes

| 原キー | 保存値 |
|---|---|
| status | "saved_raw_repetition_candidates_inspected_no_model_update" |
| notes.path | "reports/phase6/sequence_objective_CE_notes.json" |
| notes.sha256 | "6dd838612006ad7fdc33649f2f75dd16d6175ad7b65cfef4a92edbfe7cc3f430" |
| candidate_tokens | 1517 |
| candidate_rows_with_coherence2 | 1 |
| noncandidate_rows_with_coherence_below2 | 20 |
| candidate_rows_with_appropriate_completion | 3 |
| interpretation | "Generated 4-gram candidates are not a new failure threshold; legitimate repeats can exist. Noncandidate incoherence cannot be assumed fixed by repetition loss." |
| science_teacher_tokens | 0 |
| GPU_training_updates | 0 |
| protected_test_used | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_content_review.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_content_review.json) ／ SHA256: `293b5785f6f83c8f8cb772e31cc723a66a010626b54cd6e72f9939045baa0003` ／ 632 bytes

| 原キー | 保存値 |
|---|---|
| CE_teachers | 25000000 |
| BPB | 1.1481113833477452 |
| rates.eos | 42 |
| rates.repetition | 18 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 39 |
| relevance2 | 39 |
| coherent | 12 |
| appropriate | 22 |
| notes_sha256 | "6dd838612006ad7fdc33649f2f75dd16d6175ad7b65cfef4a92edbfe7cc3f430" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_generation.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_generation.json) ／ SHA256: `d2321dc359fbf3e0d1292f509debe26cb42767c1790dba8d2694de967e7c0871` ／ 93,207 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/sequence_objective_CE_notes.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_CE_notes.json) ／ SHA256: `6dd838612006ad7fdc33649f2f75dd16d6175ad7b65cfef4a92edbfe7cc3f430` ／ 17,421 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/sequence_objective_active_job.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_active_job.json) ／ SHA256: `5fe92bc75f550bf255dec6a6b917235111d5c5e8b78cba08bd2abb450390462e` ／ 2,391 bytes

| 原キー | 保存値 |
|---|---|
| job.status | "complete" |
| job.gpu_elapsed_seconds | 727.2658636560082 |
| job.protected_test_used | false |
| job.Base_adopted | false |
| job.teachers | 24695654 |
| job.teacher_budget | 25000000 |
| job.loss | 2.636685609817505 |
| latest_CE_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/CE/training/checkpoint-00032161.pt" |
| latest_CE_checkpoint.sha256 | "66f9479dc56e756675a1e0db7d48b1533de16908594ce2c475213d3c58d0a7c4" |
| latest_CE_checkpoint.update | 32161 |
| latest_CE_checkpoint.tokens_seen | 1053851648 |
| verification_teacher_tokens | 1559884 |
| verification_GPU_seconds | 103.8341657530109 |
| scientific_CE_teacher_budget_per_arm | 25000000 |
| Base_adopted | false |
| Chat_adopted | false |
| latest_CE_UL_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/CE_UL/training/checkpoint-00032161.pt" |
| latest_CE_UL_checkpoint.sha256 | "b80efc504f0d1c76a3bc85fc7ed2baee171516532c3d94a65447b356011463e2" |
| latest_CE_UL_checkpoint.update | 32161 |
| latest_CE_UL_checkpoint.tokens_seen | 1053851648 |

</details>

<details>
<summary>reports/phase6/sequence_objective_actual_probe_job.json — complete</summary>

[原記録](../../reports/phase6/sequence_objective_actual_probe_job.json) ／ SHA256: `c0130fbbacb6028bb4aafda94a3774a278869de63872697efe4f2eb0f9af5daa` ／ 572 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| gpu_elapsed_seconds | 54.62399182700028 |
| protected_test_used | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_actual_probe_result.json — actual_CUDA_objective_measurement_and_resume_complete</summary>

[原記録](../../reports/phase6/sequence_objective_actual_probe_result.json) ／ SHA256: `5f9b6929dd3cd6037633fc231a221c5189cce282b3827cdaca463050d5f865c9` ／ 34,310 bytes

| 原キー | 保存値 |
|---|---|
| gates.CE.passed | true |
| gates.CE.checks.model | true |
| gates.CE.checks.optimizer | true |
| gates.CE.checks.scheduler | true |
| gates.CE.checks.rng | true |
| gates.CE.checks.sampler | true |
| gates.CE.checks.lineage | true |
| gates.CE.checks.tokens | true |
| gates.CE.checks.supervised_tokens | true |
| gates.CE.checks.body_bytes | true |
| gates.CE.checks.token_digest | true |
| gates.CE.checks.update | true |
| gates.CE.checks.spec | true |
| gates.CE.checks.model_config | true |
| gates.CE.checks.pilot_binding | true |
| gates.CE.checks.history_loss | true |
| gates.CE.checks.history_sequence_UL | true |
| gates.CE.checks.history_optimization_loss | true |
| gates.CE.checks.history_gradient_norm | true |
| gates.CE.checks.history_lr | true |
| gates.CE.checks.history_token_digest | true |
| gates.CE.checks.history_source_teachers | true |
| gates.CE.checks.history_sequence_objective | true |
| gates.CE.checks.finite | true |
| gates.CE.checks.actual_rollout_both_routes | true |
| gates.CE.GPU_optimizer_updates | 8 |
| gates.CE.verification_teacher_tokens | 260038 |
| gates.CE.verification_input_tokens | 262144 |
| gates.CE_UL.passed | true |
| gates.CE_UL.checks.model | true |
| gates.CE_UL.checks.optimizer | true |
| gates.CE_UL.checks.scheduler | true |
| gates.CE_UL.checks.rng | true |
| gates.CE_UL.checks.sampler | true |
| gates.CE_UL.checks.lineage | true |
| gates.CE_UL.checks.tokens | true |
| gates.CE_UL.checks.supervised_tokens | true |
| gates.CE_UL.checks.body_bytes | true |
| gates.CE_UL.checks.token_digest | true |
| gates.CE_UL.checks.update | true |
| gates.CE_UL.checks.spec | true |
| gates.CE_UL.checks.model_config | true |
| gates.CE_UL.checks.pilot_binding | true |
| gates.CE_UL.checks.history_loss | true |
| gates.CE_UL.checks.history_sequence_UL | true |
| gates.CE_UL.checks.history_optimization_loss | true |
| gates.CE_UL.checks.history_gradient_norm | true |
| gates.CE_UL.checks.history_lr | true |
| gates.CE_UL.checks.history_token_digest | true |
| gates.CE_UL.checks.history_source_teachers | true |
| gates.CE_UL.checks.history_sequence_objective | true |
| gates.CE_UL.checks.finite | true |
| gates.CE_UL.checks.actual_rollout_both_routes | true |
| gates.CE_UL.GPU_optimizer_updates | 8 |
| gates.CE_UL.verification_teacher_tokens | 260038 |
| gates.CE_UL.verification_input_tokens | 262144 |
| status | "actual_CUDA_objective_measurement_and_resume_complete" |
| passed | true |
| verification_teacher_tokens | 520076 |
| scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/sequence_objective_annotations.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_annotations.json) ／ SHA256: `856aa648e2ae657fbb1319547026a97049119b11bd165a10a94ad44e2d4a6e1a` ／ 40,512 bytes

| 原キー | 保存値 |
|---|---|
| arms.CE.notes_sha256 | "6dd838612006ad7fdc33649f2f75dd16d6175ad7b65cfef4a92edbfe7cc3f430" |
| arms.CE_UL.notes_sha256 | "62082d5592ba0bd0c73e457b542682feed516684c6df48ee7134a6ea6617bb98" |

</details>

<details>
<summary>reports/phase6/sequence_objective_budget_freeze_rejection.json — actual_probe_passed_first_scientific_budget_freeze_rejected_pending_continuous_timing</summary>

[原記録](../../reports/phase6/sequence_objective_budget_freeze_rejection.json) ／ SHA256: `ad602d88539315a20c0512f2132e6e69ac056e910d51329d729d9282bf75a1e9` ／ 1,324 bytes

| 原キー | 保存値 |
|---|---|
| verification_teacher_tokens | 520076 |
| CUDA_checks_per_arm | 24 |
| probe_actual_optimizer_updates | 16 |
| protected_test_used | false |
| status | "actual_probe_passed_first_scientific_budget_freeze_rejected_pending_continuous_timing" |
| Base_adopted | false |
| frozen_scientific_recipe_created | false |
| requested_five_steps_complete | false |
| Chat_adopted | false |
| probe_GPU_seconds | 54.62399182700028 |
| scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/sequence_objective_comparison_completion.json — matched25M_CE_sequence_UL_actual_learning_all160_and_accounting_complete_candidates_rejected</summary>

[原記録](../../reports/phase6/sequence_objective_comparison_completion.json) ／ SHA256: `6ee3b18eb81343fe4a055ca543175c95dfff0a866cc7ac28cf53e890330901fa` ／ 3,728 bytes

| 原キー | 保存値 |
|---|---|
| status | "matched25M_CE_sequence_UL_actual_learning_all160_and_accounting_complete_candidates_rejected" |
| job.status | "complete" |
| job.gpu_elapsed_seconds | 727.2658636560082 |
| job.protected_test_used | false |
| job.Base_adopted | false |
| job.teachers | 24695654 |
| job.teacher_budget | 25000000 |
| job.loss | 2.636685609817505 |
| scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1559884 |
| scientific_GPU_seconds | 727.2658636560082 |
| verification_GPU_seconds | 103.8341657530109 |
| total_study_GPU_seconds | 831.100029409019 |
| ui.status | "running" |
| ui.additional_training_tokens | 0 |
| ui.model.training_tokens | 10000007168 |
| ui.model.update | 305176 |
| ui.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| verified_HTTP_model.training_tokens | 10000007168 |
| verified_HTTP_model.update | 305176 |
| verified_HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| verified_HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| verified_HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| decision | "Reject alpha0.1 token4gram sequence UL: automatic repetition18-&gt;7 but coherence12-&gt;0, appropriate22-&gt;6, EOS42-&gt;32 and BPB1.148111-&gt;1.245716. No automatic10B extension or Chat" |

</details>

<details>
<summary>reports/phase6/sequence_objective_comparison_review.json — matched_CE_sequence_UL_learning_and_all160_content_evidence_complete</summary>

[原記録](../../reports/phase6/sequence_objective_comparison_review.json) ／ SHA256: `7fef26f2a1671a9b7c9a4df533dcff05b55f525b373bf79b24d182cdef4dd6a7` ／ 5,697 bytes

| 原キー | 保存値 |
|---|---|
| status | "matched_CE_sequence_UL_learning_and_all160_content_evidence_complete" |
| summaries.CE.CE_teachers | 25000000 |
| summaries.CE.BPB | 1.1481113833477452 |
| summaries.CE.rates.eos | 42 |
| summaries.CE.rates.repetition | 18 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 39 |
| summaries.CE.relevance2 | 39 |
| summaries.CE.coherent | 12 |
| summaries.CE.appropriate | 22 |
| summaries.CE.notes_sha256 | "6dd838612006ad7fdc33649f2f75dd16d6175ad7b65cfef4a92edbfe7cc3f430" |
| summaries.CE.Base_adopted | false |
| summaries.CE_UL.CE_teachers | 25000000 |
| summaries.CE_UL.BPB | 1.2457162146538936 |
| summaries.CE_UL.rates.eos | 32 |
| summaries.CE_UL.rates.repetition | 7 |
| summaries.CE_UL.rates.unicode_failure | 0 |
| summaries.CE_UL.rates.role_leak | 0 |
| summaries.CE_UL.rates.empty | 0 |
| summaries.CE_UL.grammar2 | 20 |
| summaries.CE_UL.relevance2 | 6 |
| summaries.CE_UL.coherent | 0 |
| summaries.CE_UL.appropriate | 6 |
| summaries.CE_UL.notes_sha256 | "62082d5592ba0bd0c73e457b542682feed516684c6df48ee7134a6ea6617bb98" |
| summaries.CE_UL.Base_adopted | false |
| objective_comparison.checks.coherence_gain_at_least8 | false |
| objective_comparison.checks.paired_CI_lower_above0 | false |
| objective_comparison.checks.EOS_nonworsening | false |
| objective_comparison.checks.repetition_nonworsening | true |
| objective_comparison.checks.no_empty_role_unicode | true |
| objective_comparison.checks.BPB_gate | false |
| objective_comparison.checks.appropriate_completion_not_punctuation | true |
| objective_comparison.passed | false |
| practical.CE.checks.grammar_at_least56 | false |
| practical.CE.checks.coherence_at_least27 | false |
| practical.CE.checks.appropriate_at_least27 | false |
| practical.CE.checks.EOS_at_least37 | true |
| practical.CE.checks.repetition_at_most18 | true |
| practical.CE.checks.no_empty_role_unicode | true |
| practical.CE.original_Web.EOS_at_least8_more | true |
| practical.CE.original_Web.repetition_no_worse | true |
| practical.CE.original_Web.no_empty_role_unicode | true |
| practical.CE.original_Web.BPB_degradation_at_most1percent | false |
| practical.CE.absolute_screen_pass | false |
| practical.CE.Base_adopted | false |
| practical.CE.final_seed_full_test_pending | true |
| practical.CE_UL.checks.grammar_at_least56 | false |
| practical.CE_UL.checks.coherence_at_least27 | false |
| practical.CE_UL.checks.appropriate_at_least27 | false |
| practical.CE_UL.checks.EOS_at_least37 | false |
| practical.CE_UL.checks.repetition_at_most18 | true |
| practical.CE_UL.checks.no_empty_role_unicode | true |
| practical.CE_UL.original_Web.EOS_at_least8_more | true |
| practical.CE_UL.original_Web.repetition_no_worse | true |
| practical.CE_UL.original_Web.no_empty_role_unicode | true |
| practical.CE_UL.original_Web.BPB_degradation_at_most1percent | false |
| practical.CE_UL.absolute_screen_pass | false |
| practical.CE_UL.Base_adopted | false |
| practical.CE_UL.final_seed_full_test_pending | true |
| extra_generation_accounting.CE.objective.every_updates | 4 |
| extra_generation_accounting.CE.objective.prefix_tokens | 32 |
| extra_generation_accounting.CE.objective.max_new_tokens | 64 |
| extra_generation_accounting.CE.skipped_rollouts | 0 |
| extra_generation_accounting.CE.generated_body_tokens | 50320 |
| extra_generation_accounting.CE.generated_EOS | 1137 |
| extra_generation_accounting.CE.negative_token_positions | 17423 |
| extra_generation_accounting.CE.extra_valid_input_tokens | 200386 |
| extra_generation_accounting.CE.extra_physical_input_tokens | 288992 |
| extra_generation_accounting.CE_UL.objective.every_updates | 4 |
| extra_generation_accounting.CE_UL.objective.prefix_tokens | 32 |
| extra_generation_accounting.CE_UL.objective.max_new_tokens | 64 |
| extra_generation_accounting.CE_UL.skipped_rollouts | 0 |
| extra_generation_accounting.CE_UL.generated_body_tokens | 74404 |
| extra_generation_accounting.CE_UL.generated_EOS | 1053 |
| extra_generation_accounting.CE_UL.negative_token_positions | 15118 |
| extra_generation_accounting.CE_UL.extra_valid_input_tokens | 248188 |
| extra_generation_accounting.CE_UL.extra_physical_input_tokens | 289760 |
| scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1559884 |
| scientific_GPU_seconds | 727.2658636560082 |
| verification_GPU_seconds | 103.8341657530109 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_continuous_timing_job.json — complete</summary>

[原記録](../../reports/phase6/sequence_objective_continuous_timing_job.json) ／ SHA256: `4eaf84579c858829f9379dfdbc3ab9cd8f4e9355134df3faa352a55316d1dcd2` ／ 587 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| gpu_elapsed_seconds | 27.58766164899862 |
| scientific_teacher_tokens | 0 |
| completed_updates | 16 |
| total_updates | 16 |

</details>

<details>
<summary>reports/phase6/sequence_objective_continuous_timing_result.json — actual_continuous_timing_complete</summary>

[原記録](../../reports/phase6/sequence_objective_continuous_timing_result.json) ／ SHA256: `dfe51752dba5cd2d25921ea60d62fbf3f5cda395fa228f271077d221f7f7ff2f` ／ 62,369 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_continuous_timing_complete" |
| arms.CE.verification_teacher_tokens | 519904 |
| arms.CE.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/continuous-timing/CE/checkpoint-00031411.pt" |
| arms.CE.checkpoint_sha256 | "86a25c4ef643e9c3e2519380f2718e904966bfbd0a1e5f45d7f80f56b2cfeda3" |
| arms.CE.recovered_without_updates | true |
| arms.CE_UL.verification_teacher_tokens | 519904 |
| arms.CE_UL.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/continuous-timing-v2/CE_UL/checkpoint-00031411.pt" |
| arms.CE_UL.checkpoint_sha256 | "646498e966348a6a713ee36b2f0b1dd3fcf480a3d301a39dacdbcfd5cb9c5898" |
| verification_teacher_tokens | 1039808 |
| recovered_GPU_seconds | 21.622512277011992 |
| scientific_teacher_tokens | 0 |
| Base_adopted | false |
| protected_test_used | false |
| weights_used_for_scientific_parent | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_diagnostic_completion.json — actual_train_only_diagnosis_complete_next_comparison_planned</summary>

[原記録](../../reports/phase6/sequence_objective_diagnostic_completion.json) ／ SHA256: `cd07b42066ddb5c12b74cc16bd9733c1619fd1ef69dedbe8e8d464203e1b470f` ／ 2,298 bytes

| 原キー | 保存値 |
|---|---|
| ui.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.gpu_elapsed_seconds | 25.557537383996532 |
| actual_job.optimizer_updates | 0 |
| actual_job.scientific_teacher_tokens | 0 |
| limitations | "One fixed first32K train window with8 document-head prefixes; not representative corpus, not whole-training causality, not independent quality evaluation" |
| next_comparison.gpu_budget | "not yet measured/frozen; prior complete pair used831.100029 seconds including verification, not a promised new runtime" |
| next_comparison.teacher_tokens_per_condition | 25000000 |
| next_comparison.status | "planned_not_frozen_not_started" |
| status | "actual_train_only_diagnosis_complete_next_comparison_planned" |

</details>

<details>
<summary>reports/phase6/sequence_objective_evidence_manifest.json — completed_text_evidence_archive</summary>

[原記録](../../reports/phase6/sequence_objective_evidence_manifest.json) ／ SHA256: `f5f0abcaf7bf30ff9455f9a238df3cd9273c5fd45b2eab85cbaa4a0d17117639` ／ 18,557 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_text_evidence_archive" |
| uncompressed_bytes | 8773723 |
| checkpoint_tensors_included | false |
| native_checkpoints_retained | true |
| scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1559884 |

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_active_job.json — complete</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_active_job.json) ／ SHA256: `b5c94c35027cf7a4521108bf4426561adec4bea2f7b940d2b2acf2b14249f5c8` ／ 1,064 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| Chat_adopted | false |
| actual_job.status | "complete" |
| actual_job.gpu_elapsed_seconds | 366.1949579840002 |
| actual_job.Base_adopted | false |
| actual_job.protected_test_used | false |
| actual_job.teachers | 24695654 |
| actual_job.teacher_budget | 25000000 |
| actual_job.loss | 2.635779619216919 |
| Base_adopted | false |
| completion | "reports/phase6/sequence_objective_low_alpha_completion.json" |

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_completion.json — actual_low_alpha25M_and_all80_complete_candidate_rejected</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_completion.json) ／ SHA256: `df2397ac435333f2cfc8c7f26bf0160b241e0f879f620bd386e5218f4c3008e5` ／ 3,063 bytes

| 原キー | 保存値 |
|---|---|
| Chat_adopted | false |
| actual_job.status | "complete" |
| actual_job.gpu_elapsed_seconds | 366.1949579840002 |
| actual_job.Base_adopted | false |
| actual_job.protected_test_used | false |
| actual_job.teachers | 24695654 |
| actual_job.teacher_budget | 25000000 |
| actual_job.loss | 2.635779619216919 |
| requested_five_steps_complete | false |
| status | "actual_low_alpha25M_and_all80_complete_candidate_rejected" |
| UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| protected_test_used | false |
| new_scientific_teacher_tokens | 25000000 |
| Base_adopted | false |
| verification_teacher_tokens | 779980 |
| next_action.status | "defined_research_not_implemented_not_started" |
| next_action.comparison_GPU_ceiling_proposal | 2700 |
| next_action.hypothesis | "2B prepared corpus has only ~50.4percent of shuffled token blocks consumed at1B teachers; test whether reaching roughly one full coverage improves unseen generation" |
| archive.bytes | 1268979 |
| archive.uncompressed_bytes | 6710697 |
| reused_control_teacher_tokens | 25000000 |
| new_total_GPU_seconds | 413.6532203989918 |

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_content_review.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_content_review.json) ／ SHA256: `c8d84a61d9727a216f590aa93521897c6135b4519ac48cf6ac1f127688ae0050` ／ 631 bytes

| 原キー | 保存値 |
|---|---|
| CE_teachers | 25000000 |
| BPB | 1.163730040948166 |
| rates.eos | 28 |
| rates.repetition | 32 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 29 |
| relevance2 | 13 |
| coherent | 7 |
| appropriate | 10 |
| notes_sha256 | "f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_evidence_manifest.json — completed_text_evidence_archive</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_evidence_manifest.json) ／ SHA256: `c9c060f1acd6d150f89e0fe30ada0126add155500bc3f482587a9820dab10e10` ／ 13,709 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_text_evidence_archive" |
| uncompressed_bytes | 6710697 |
| checkpoint_tensors_included | false |
| native_checkpoints_retained | true |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| verification_teacher_tokens | 779980 |

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_notes.json — None</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_notes.json) ／ SHA256: `f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5` ／ 11,779 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/sequence_objective_low_alpha_review.json — matched_reused_CE_and_actual_low_alpha25M_all80_complete</summary>

[原記録](../../reports/phase6/sequence_objective_low_alpha_review.json) ／ SHA256: `7e22e03ae51e402c65cbf8c769596be93c51c356039cd904f05d5515c1285257` ／ 3,263 bytes

| 原キー | 保存値 |
|---|---|
| status | "matched_reused_CE_and_actual_low_alpha25M_all80_complete" |
| summary.CE_teachers | 25000000 |
| summary.BPB | 1.163730040948166 |
| summary.rates.eos | 28 |
| summary.rates.repetition | 32 |
| summary.rates.unicode_failure | 0 |
| summary.rates.role_leak | 0 |
| summary.rates.empty | 0 |
| summary.grammar2 | 29 |
| summary.relevance2 | 13 |
| summary.coherent | 7 |
| summary.appropriate | 10 |
| summary.notes_sha256 | "f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5" |
| summary.Base_adopted | false |
| objective_comparison.checks.coherence_gain_at_least8 | false |
| objective_comparison.checks.paired_CI_lower_above0 | false |
| objective_comparison.checks.EOS_nonworsening | false |
| objective_comparison.checks.repetition_nonworsening | false |
| objective_comparison.checks.no_empty_role_unicode | true |
| objective_comparison.checks.BPB_gate | false |
| objective_comparison.checks.appropriate_completion_not_punctuation | true |
| objective_comparison.passed | false |
| practical.checks.grammar_at_least56 | false |
| practical.checks.coherence_at_least27 | false |
| practical.checks.appropriate_at_least27 | false |
| practical.checks.EOS_at_least37 | false |
| practical.checks.repetition_at_most18 | false |
| practical.checks.no_empty_role_unicode | true |
| practical.original_Web.EOS_at_least8_more | true |
| practical.original_Web.repetition_no_worse | true |
| practical.original_Web.no_empty_role_unicode | true |
| practical.original_Web.BPB_degradation_at_most1percent | false |
| practical.absolute_screen_pass | false |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| compared_teacher_tokens | 50000000 |
| verification_teacher_tokens | 779980 |
| new_scientific_GPU_seconds | 366.1949579840002 |
| verification_GPU_seconds | 47.45826241499162 |
| extra_generation_accounting.objective.every_updates | 4 |
| extra_generation_accounting.objective.prefix_tokens | 32 |
| extra_generation_accounting.objective.max_new_tokens | 64 |
| extra_generation_accounting.skipped_rollouts | 0 |
| extra_generation_accounting.generated_body_tokens | 63633 |
| extra_generation_accounting.generated_EOS | 980 |
| extra_generation_accounting.negative_token_positions | 23965 |
| extra_generation_accounting.extra_valid_input_tokens | 226370 |
| extra_generation_accounting.extra_physical_input_tokens | 290656 |
| notes_sha256 | "f4a2ae7586b9f4f42bfb0648e9cff8f668d973d692f80e8c0879a250115b16c5" |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/sequence_objective_timing_failure.json — continuous_timing_failed_after_CE16_saved</summary>

[原記録](../../reports/phase6/sequence_objective_timing_failure.json) ／ SHA256: `51cdf4c79502ee70aa5ca9c2135aba64b038a208797b44b9fd632595a5975326` ／ 1,762 bytes

| 原キー | 保存値 |
|---|---|
| status | "continuous_timing_failed_after_CE16_saved" |
| job.status | "failed" |
| job.gpu_elapsed_seconds | 21.622512277011992 |
| job.scientific_teacher_tokens | 0 |
| job.completed_updates | 16 |
| job.total_updates | 16 |
| CE_saved_updates | 16 |
| CE_latest.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/sequence-objective-comparison-20261006/continuous-timing/CE/checkpoint-00031411.pt" |
| CE_latest.sha256 | "86a25c4ef643e9c3e2519380f2718e904966bfbd0a1e5f45d7f80f56b2cfeda3" |
| CE_latest.update | 31411 |
| CE_latest.tokens_seen | 1029275648 |
| original_probe_GPU_seconds | 54.62399182700028 |
| spent_probe_plus_timing_GPU_seconds | 76.24650410401227 |
| repair_implemented | false |
| scientific_teacher_tokens | 0 |
| scientific_recipe_frozen | false |
| Base_adopted | false |
| Chat_adopted | false |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/dev-only-encoded.json — None</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/dev-only-encoded.json) ／ SHA256: `e3f38383537f2c31853603c2efc3cc21acac8ec0bccddb0fa53a9a578920d1c8` ／ 750,846 bytes

| 原キー | 保存値 |
|---|---|
| selection.dev_bytes_sha256 | "7098881e4723f59c2ca34506adf8d6cda11ef16dd2ea824504dfdc47eeffa7d3" |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/job.json) ／ SHA256: `61431efcf45b18eb4b8b95ad5f2058473a8d1ea8338c0df5053e3e7e1d326d35` ／ 764 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 7.486655257001985 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| teacher_context_signal_passed | true |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/launcher-launcher.json — None</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/launcher-launcher.json) ／ SHA256: `2b1db4b3ec0b6cd71a657e36d209f157bc5c6b2e6a80caaf1bfde5b5d6607ba0` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/launcher-result.json — complete</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/launcher-result.json) ／ SHA256: `2198166c8182bfe9bfd03dfc4854c88f72fa2b6e1cc8813e78355a48c52096a4` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/manifest.json — None</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/manifest.json) ／ SHA256: `fb9ed7a5b824668dd62e8b90aa2b7bbaff6d2bc2eedd3b04b0cc9649fe04ead5` ／ 5,939 bytes

| 原キー | 保存値 |
|---|---|
| notes | "Frozen inference sources/results retained. Corrected content-alias review is authoritative for the decision. Original nominal signal_passed=true and raw scores remain historical. No model tensors/full TRAIN articles/protected TEST record bodies in archive." |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/native10M-complete.json — None</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/native10M-complete.json) ／ SHA256: `2923145f41bfb2377baac6aa7fbd3493cc0130da80377f3b466cae2e6eef2903` ／ 322,718 bytes

| 原キー | 保存値 |
|---|---|
| stats.seconds_including_load | 0.5025798630085774 |
| stats.scoring_seconds | 0.3171835629909765 |
| stats.peak_allocated_bytes | 136497152 |
| stats.summary.accuracy.point | 0.6197916666666666 |
| stats.summary.accuracy.ci95 | [0.5677083333333334, 0.671875] |
| stats.summary.accuracy.units | 96 |
| stats.summary.accuracy.examples | 192 |
| stats.summary.accuracy.unit | "family/prompt" |
| stats.summary.accuracy.seed | 42 |
| stats.summary.accuracy.repetitions | 2000 |
| stats.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.both_contexts_hard_correct.point | 0.28125 |
| stats.summary.both_contexts_hard_correct.ci95 | [0.19791666666666666, 0.375] |
| stats.summary.both_contexts_hard_correct.units | 96 |
| stats.summary.both_contexts_hard_correct.examples | 96 |
| stats.summary.both_contexts_hard_correct.unit | "family/prompt" |
| stats.summary.both_contexts_hard_correct.seed | 42 |
| stats.summary.both_contexts_hard_correct.repetitions | 2000 |
| stats.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.negation.seed | 42 |
| stats.summary.categories.negation.repetitions | 2000 |
| stats.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.quantity.seed | 42 |
| stats.summary.categories.quantity.repetitions | 2000 |
| stats.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.time.seed | 42 |
| stats.summary.categories.time.repetitions | 2000 |
| stats.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.comparison.seed | 42 |
| stats.summary.categories.comparison.repetitions | 2000 |
| stats.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.coreference.seed | 42 |
| stats.summary.categories.coreference.repetitions | 2000 |
| stats.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.causality.seed | 42 |
| stats.summary.categories.causality.repetitions | 2000 |
| stats.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.total_choice_tokens | 1842 |
| stats.summary.total_common_choice_bytes | 5798 |
| stats.summary.static_candidate_preference_case_accuracy | 0.5 |
| stats.summary.static_candidate_preference_both_correct | 0 |
| stats.total_forward_tokens | 11204 |

</details>

<details>
<summary>reports/phase6/teacher-semantic-signal-evidence-20261007/teacher-complete.json — None</summary>

[原記録](../../reports/phase6/teacher-semantic-signal-evidence-20261007/teacher-complete.json) ／ SHA256: `688feb7c39d34511be0778397703a34aea8127ce2f9f57916a63f19c624d5d7e` ／ 328,707 bytes

| 原キー | 保存値 |
|---|---|
| stats.seconds_including_load | 6.923847411002498 |
| stats.scoring_seconds | 2.496359552053036 |
| stats.peak_allocated_bytes | 8282029568 |
| stats.summary.accuracy.point | 0.7291666666666666 |
| stats.summary.accuracy.ci95 | [0.6770833333333334, 0.7760416666666666] |
| stats.summary.accuracy.units | 96 |
| stats.summary.accuracy.examples | 192 |
| stats.summary.accuracy.unit | "family/prompt" |
| stats.summary.accuracy.seed | 42 |
| stats.summary.accuracy.repetitions | 2000 |
| stats.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.both_contexts_hard_correct.point | 0.4583333333333333 |
| stats.summary.both_contexts_hard_correct.ci95 | [0.3541666666666667, 0.5520833333333334] |
| stats.summary.both_contexts_hard_correct.units | 96 |
| stats.summary.both_contexts_hard_correct.examples | 96 |
| stats.summary.both_contexts_hard_correct.unit | "family/prompt" |
| stats.summary.both_contexts_hard_correct.seed | 42 |
| stats.summary.both_contexts_hard_correct.repetitions | 2000 |
| stats.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.negation.seed | 42 |
| stats.summary.categories.negation.repetitions | 2000 |
| stats.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.quantity.seed | 42 |
| stats.summary.categories.quantity.repetitions | 2000 |
| stats.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.time.seed | 42 |
| stats.summary.categories.time.repetitions | 2000 |
| stats.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.comparison.seed | 42 |
| stats.summary.categories.comparison.repetitions | 2000 |
| stats.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.coreference.seed | 42 |
| stats.summary.categories.coreference.repetitions | 2000 |
| stats.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.categories.causality.seed | 42 |
| stats.summary.categories.causality.repetitions | 2000 |
| stats.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| stats.summary.total_choice_tokens | 1878 |
| stats.summary.total_common_choice_bytes | 5798 |
| stats.summary.static_candidate_preference_case_accuracy | 0.5 |
| stats.summary.static_candidate_preference_both_correct | 0 |
| stats.total_forward_tokens | 10748 |

</details>

<details>
<summary>reports/phase6/teacher_semantic_signal_completion.json — complete_teacher_transfer_branch_closed_native_contrastive_probe_prepared</summary>

[原記録](../../reports/phase6/teacher_semantic_signal_completion.json) ／ SHA256: `270938beee47546142982e1f4c2f47e5801437c7b485b540c9e0c6025fd41bd6` ／ 2,499 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_teacher_transfer_branch_closed_native_contrastive_probe_prepared" |
| exact_content_pair_clusters | 64 |
| teacher_correct | 140 |
| native_correct | 119 |
| paired_difference.point | 0.109375 |
| paired_difference.ci95 | [0.0, 0.22] |
| paired_difference.units | 64 |
| paired_difference.examples | 192 |
| paired_difference.unit | "family/prompt" |
| paired_difference.seed | 42 |
| paired_difference.repetitions | 2000 |
| paired_difference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_gate_passed | true |
| conservative_gate_passed | false |
| teacher_transfer_branch_closed | true |
| GPU_seconds | 7.486655257001985 |
| tests.passed | 4 |
| tests.CPU_seconds | 0.82 |
| tests.XML | "reports/phase6/teacher_semantic_signal_tests.xml" |
| native_contrast_preparation.GPU_probe_started | false |
| native_contrast_preparation.pairs | 64 |
| native_contrast_preparation.CPU_seconds | 0.3058010560052935 |
| current_UI.training_tokens | 10000007168 |
| current_UI.HTTP_original_checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_JSON_decoded | false |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/teacher_semantic_signal_job.json — complete</summary>

[原記録](../../reports/phase6/teacher_semantic_signal_job.json) ／ SHA256: `61431efcf45b18eb4b8b95ad5f2058473a8d1ea8338c0df5053e3e7e1d326d35` ／ 764 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 7.486655257001985 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| teacher_context_signal_passed | true |

</details>

<details>
<summary>reports/phase6/teacher_semantic_signal_result.json — all192_matched_teacher_native_semantic_diagnostic_complete</summary>

[原記録](../../reports/phase6/teacher_semantic_signal_result.json) ／ SHA256: `355795703951b6f739a27a1cfedf812bb9962886f727bcf587254efedf1c2007` ／ 752,244 bytes

| 原キー | 保存値 |
|---|---|
| status | "all192_matched_teacher_native_semantic_diagnostic_complete" |
| selection.dev_bytes_sha256 | "7098881e4723f59c2ca34506adf8d6cda11ef16dd2ea824504dfdc47eeffa7d3" |
| teacher_model | "Qwen/Qwen3-4B-Instruct-2507" |
| teacher_revision | "cdbee75f17c01a7cc42f958dc650907174af0554" |
| native_checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| models.teacher.seconds_including_load | 6.923847411002498 |
| models.teacher.scoring_seconds | 2.496359552053036 |
| models.teacher.peak_allocated_bytes | 8282029568 |
| models.teacher.all_gradients_none | true |
| models.teacher.eval_mode | true |
| models.teacher.summary.cases | 192 |
| models.teacher.summary.accuracy.point | 0.7291666666666666 |
| models.teacher.summary.accuracy.ci95 | [0.6770833333333334, 0.7760416666666666] |
| models.teacher.summary.accuracy.units | 96 |
| models.teacher.summary.accuracy.examples | 192 |
| models.teacher.summary.accuracy.unit | "family/prompt" |
| models.teacher.summary.accuracy.seed | 42 |
| models.teacher.summary.accuracy.repetitions | 2000 |
| models.teacher.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.both_contexts_hard_correct.point | 0.4583333333333333 |
| models.teacher.summary.both_contexts_hard_correct.ci95 | [0.3541666666666667, 0.5520833333333334] |
| models.teacher.summary.both_contexts_hard_correct.units | 96 |
| models.teacher.summary.both_contexts_hard_correct.examples | 96 |
| models.teacher.summary.both_contexts_hard_correct.unit | "family/prompt" |
| models.teacher.summary.both_contexts_hard_correct.seed | 42 |
| models.teacher.summary.both_contexts_hard_correct.repetitions | 2000 |
| models.teacher.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.ties | 0 |
| models.teacher.summary.categories.negation.point | 0.5 |
| models.teacher.summary.categories.negation.ci95 | [0.5, 0.5] |
| models.teacher.summary.categories.negation.units | 16 |
| models.teacher.summary.categories.negation.examples | 32 |
| models.teacher.summary.categories.negation.unit | "family/prompt" |
| models.teacher.summary.categories.negation.seed | 42 |
| models.teacher.summary.categories.negation.repetitions | 2000 |
| models.teacher.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.categories.quantity.point | 0.65625 |
| models.teacher.summary.categories.quantity.ci95 | [0.5625, 0.78125] |
| models.teacher.summary.categories.quantity.units | 16 |
| models.teacher.summary.categories.quantity.examples | 32 |
| models.teacher.summary.categories.quantity.unit | "family/prompt" |
| models.teacher.summary.categories.quantity.seed | 42 |
| models.teacher.summary.categories.quantity.repetitions | 2000 |
| models.teacher.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.categories.time.point | 0.96875 |
| models.teacher.summary.categories.time.ci95 | [0.90625, 1.0] |
| models.teacher.summary.categories.time.units | 16 |
| models.teacher.summary.categories.time.examples | 32 |
| models.teacher.summary.categories.time.unit | "family/prompt" |
| models.teacher.summary.categories.time.seed | 42 |
| models.teacher.summary.categories.time.repetitions | 2000 |
| models.teacher.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.categories.comparison.point | 0.6875 |
| models.teacher.summary.categories.comparison.ci95 | [0.5625, 0.8125] |
| models.teacher.summary.categories.comparison.units | 16 |
| models.teacher.summary.categories.comparison.examples | 32 |
| models.teacher.summary.categories.comparison.unit | "family/prompt" |
| models.teacher.summary.categories.comparison.seed | 42 |
| models.teacher.summary.categories.comparison.repetitions | 2000 |
| models.teacher.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.categories.coreference.point | 0.5625 |
| models.teacher.summary.categories.coreference.ci95 | [0.5, 0.65625] |
| models.teacher.summary.categories.coreference.units | 16 |
| models.teacher.summary.categories.coreference.examples | 32 |
| models.teacher.summary.categories.coreference.unit | "family/prompt" |
| models.teacher.summary.categories.coreference.seed | 42 |
| models.teacher.summary.categories.coreference.repetitions | 2000 |
| models.teacher.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.categories.causality.point | 1.0 |
| models.teacher.summary.categories.causality.ci95 | [1.0, 1.0] |
| models.teacher.summary.categories.causality.units | 16 |
| models.teacher.summary.categories.causality.examples | 32 |
| models.teacher.summary.categories.causality.unit | "family/prompt" |
| models.teacher.summary.categories.causality.seed | 42 |
| models.teacher.summary.categories.causality.repetitions | 2000 |
| models.teacher.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.teacher.summary.total_choice_tokens | 1878 |
| models.teacher.summary.total_common_choice_bytes | 5798 |
| models.teacher.summary.chance_case | 0.5 |
| models.teacher.summary.independent_random_both_chance | 0.25 |
| models.teacher.summary.static_candidate_preference_case_accuracy | 0.5 |
| models.teacher.summary.static_candidate_preference_both_correct | 0 |
| models.teacher.model_specific_BOS | 151643 |
| models.teacher.total_forward_tokens | 10748 |
| models.native10M.seconds_including_load | 0.5025798630085774 |
| models.native10M.scoring_seconds | 0.3171835629909765 |
| models.native10M.peak_allocated_bytes | 136497152 |
| models.native10M.summary.accuracy.point | 0.6197916666666666 |
| models.native10M.summary.accuracy.ci95 | [0.5677083333333334, 0.671875] |
| models.native10M.summary.accuracy.units | 96 |
| models.native10M.summary.accuracy.examples | 192 |
| models.native10M.summary.accuracy.unit | "family/prompt" |
| models.native10M.summary.accuracy.seed | 42 |
| models.native10M.summary.accuracy.repetitions | 2000 |
| models.native10M.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.both_contexts_hard_correct.point | 0.28125 |
| models.native10M.summary.both_contexts_hard_correct.ci95 | [0.19791666666666666, 0.375] |
| models.native10M.summary.both_contexts_hard_correct.units | 96 |
| models.native10M.summary.both_contexts_hard_correct.examples | 96 |
| models.native10M.summary.both_contexts_hard_correct.unit | "family/prompt" |
| models.native10M.summary.both_contexts_hard_correct.seed | 42 |
| models.native10M.summary.both_contexts_hard_correct.repetitions | 2000 |
| models.native10M.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.negation.seed | 42 |
| models.native10M.summary.categories.negation.repetitions | 2000 |
| models.native10M.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.quantity.seed | 42 |
| models.native10M.summary.categories.quantity.repetitions | 2000 |
| models.native10M.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.time.seed | 42 |
| models.native10M.summary.categories.time.repetitions | 2000 |
| models.native10M.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.comparison.seed | 42 |
| models.native10M.summary.categories.comparison.repetitions | 2000 |
| models.native10M.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.coreference.seed | 42 |
| models.native10M.summary.categories.coreference.repetitions | 2000 |
| models.native10M.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.categories.causality.seed | 42 |
| models.native10M.summary.categories.causality.repetitions | 2000 |
| models.native10M.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| models.native10M.summary.total_choice_tokens | 1842 |
| models.native10M.summary.total_common_choice_bytes | 5798 |
| models.native10M.summary.static_candidate_preference_case_accuracy | 0.5 |
| models.native10M.summary.static_candidate_preference_both_correct | 0 |
| models.native10M.total_forward_tokens | 11204 |
| comparison.paired_teacher_minus_student_accuracy.point | 0.109375 |
| comparison.paired_teacher_minus_student_accuracy.ci95 | [0.020833333333333332, 0.18763020833333263] |
| comparison.paired_teacher_minus_student_accuracy.units | 96 |
| comparison.paired_teacher_minus_student_accuracy.examples | 192 |
| comparison.paired_teacher_minus_student_accuracy.unit | "family/prompt" |
| comparison.paired_teacher_minus_student_accuracy.seed | 42 |
| comparison.paired_teacher_minus_student_accuracy.repetitions | 2000 |
| comparison.paired_teacher_minus_student_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| teacher_context_signal_passed | true |
| GPU_seconds | 7.486655257001985 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| new_prepared_training_tokens | 0 |
| Base_complete | false |
| protected_test_records_JSON_decoded | false |
| EOS_scored | false |
| limitations | "大きな公開modelは学習データ・architecture・tokenizer・post-trainingが異なるためpure parameter-size対照ではない。dev診断をBase採用/教師の無汚染証明/hidden-state転移の成功としない。 These are constructed dev cases, not independent human evaluation or global task capability. Pretraining contamination of the external teacher is unknown. Likelihood ability is not proof that hidden-state transfer works." |

</details>

<details>
<summary>reports/phase6/teacher_semantic_signal_review.json — all192_raw_bound_semantic_comparison_review_complete</summary>

[原記録](../../reports/phase6/teacher_semantic_signal_review.json) ／ SHA256: `6e9f2be405ed295467504b73a80f90514a43f722bc3f9423e0d4084330eedbb6` ／ 61,226 bytes

| 原キー | 保存値 |
|---|---|
| status | "all192_raw_bound_semantic_comparison_review_complete" |
| effective_exact_content_pair_families | 64 |
| original_nominal_summary.teacher.seconds_including_load | 6.923847411002498 |
| original_nominal_summary.teacher.scoring_seconds | 2.496359552053036 |
| original_nominal_summary.teacher.peak_allocated_bytes | 8282029568 |
| original_nominal_summary.teacher.all_gradients_none | true |
| original_nominal_summary.teacher.eval_mode | true |
| original_nominal_summary.teacher.summary.cases | 192 |
| original_nominal_summary.teacher.summary.accuracy.point | 0.7291666666666666 |
| original_nominal_summary.teacher.summary.accuracy.ci95 | [0.6770833333333334, 0.7760416666666666] |
| original_nominal_summary.teacher.summary.accuracy.units | 96 |
| original_nominal_summary.teacher.summary.accuracy.examples | 192 |
| original_nominal_summary.teacher.summary.accuracy.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.accuracy.seed | 42 |
| original_nominal_summary.teacher.summary.accuracy.repetitions | 2000 |
| original_nominal_summary.teacher.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.point | 0.4583333333333333 |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.ci95 | [0.3541666666666667, 0.5520833333333334] |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.units | 96 |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.examples | 96 |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.seed | 42 |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.repetitions | 2000 |
| original_nominal_summary.teacher.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.ties | 0 |
| original_nominal_summary.teacher.summary.categories.negation.point | 0.5 |
| original_nominal_summary.teacher.summary.categories.negation.ci95 | [0.5, 0.5] |
| original_nominal_summary.teacher.summary.categories.negation.units | 16 |
| original_nominal_summary.teacher.summary.categories.negation.examples | 32 |
| original_nominal_summary.teacher.summary.categories.negation.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.negation.seed | 42 |
| original_nominal_summary.teacher.summary.categories.negation.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.categories.quantity.point | 0.65625 |
| original_nominal_summary.teacher.summary.categories.quantity.ci95 | [0.5625, 0.78125] |
| original_nominal_summary.teacher.summary.categories.quantity.units | 16 |
| original_nominal_summary.teacher.summary.categories.quantity.examples | 32 |
| original_nominal_summary.teacher.summary.categories.quantity.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.quantity.seed | 42 |
| original_nominal_summary.teacher.summary.categories.quantity.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.categories.time.point | 0.96875 |
| original_nominal_summary.teacher.summary.categories.time.ci95 | [0.90625, 1.0] |
| original_nominal_summary.teacher.summary.categories.time.units | 16 |
| original_nominal_summary.teacher.summary.categories.time.examples | 32 |
| original_nominal_summary.teacher.summary.categories.time.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.time.seed | 42 |
| original_nominal_summary.teacher.summary.categories.time.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.categories.comparison.point | 0.6875 |
| original_nominal_summary.teacher.summary.categories.comparison.ci95 | [0.5625, 0.8125] |
| original_nominal_summary.teacher.summary.categories.comparison.units | 16 |
| original_nominal_summary.teacher.summary.categories.comparison.examples | 32 |
| original_nominal_summary.teacher.summary.categories.comparison.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.comparison.seed | 42 |
| original_nominal_summary.teacher.summary.categories.comparison.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.categories.coreference.point | 0.5625 |
| original_nominal_summary.teacher.summary.categories.coreference.ci95 | [0.5, 0.65625] |
| original_nominal_summary.teacher.summary.categories.coreference.units | 16 |
| original_nominal_summary.teacher.summary.categories.coreference.examples | 32 |
| original_nominal_summary.teacher.summary.categories.coreference.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.coreference.seed | 42 |
| original_nominal_summary.teacher.summary.categories.coreference.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.categories.causality.point | 1.0 |
| original_nominal_summary.teacher.summary.categories.causality.ci95 | [1.0, 1.0] |
| original_nominal_summary.teacher.summary.categories.causality.units | 16 |
| original_nominal_summary.teacher.summary.categories.causality.examples | 32 |
| original_nominal_summary.teacher.summary.categories.causality.unit | "family/prompt" |
| original_nominal_summary.teacher.summary.categories.causality.seed | 42 |
| original_nominal_summary.teacher.summary.categories.causality.repetitions | 2000 |
| original_nominal_summary.teacher.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.teacher.summary.total_choice_tokens | 1878 |
| original_nominal_summary.teacher.summary.total_common_choice_bytes | 5798 |
| original_nominal_summary.teacher.summary.chance_case | 0.5 |
| original_nominal_summary.teacher.summary.independent_random_both_chance | 0.25 |
| original_nominal_summary.teacher.summary.static_candidate_preference_case_accuracy | 0.5 |
| original_nominal_summary.teacher.summary.static_candidate_preference_both_correct | 0 |
| original_nominal_summary.teacher.model_specific_BOS | 151643 |
| original_nominal_summary.teacher.total_forward_tokens | 10748 |
| original_nominal_summary.native10M.seconds_including_load | 0.5025798630085774 |
| original_nominal_summary.native10M.scoring_seconds | 0.3171835629909765 |
| original_nominal_summary.native10M.peak_allocated_bytes | 136497152 |
| original_nominal_summary.native10M.summary.accuracy.point | 0.6197916666666666 |
| original_nominal_summary.native10M.summary.accuracy.ci95 | [0.5677083333333334, 0.671875] |
| original_nominal_summary.native10M.summary.accuracy.units | 96 |
| original_nominal_summary.native10M.summary.accuracy.examples | 192 |
| original_nominal_summary.native10M.summary.accuracy.unit | "family/prompt" |
| original_nominal_summary.native10M.summary.accuracy.seed | 42 |
| original_nominal_summary.native10M.summary.accuracy.repetitions | 2000 |
| original_nominal_summary.native10M.summary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.point | 0.28125 |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.ci95 | [0.19791666666666666, 0.375] |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.units | 96 |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.examples | 96 |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.unit | "family/prompt" |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.seed | 42 |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.repetitions | 2000 |
| original_nominal_summary.native10M.summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.negation.seed | 42 |
| original_nominal_summary.native10M.summary.categories.negation.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.quantity.seed | 42 |
| original_nominal_summary.native10M.summary.categories.quantity.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.time.seed | 42 |
| original_nominal_summary.native10M.summary.categories.time.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.comparison.seed | 42 |
| original_nominal_summary.native10M.summary.categories.comparison.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.coreference.seed | 42 |
| original_nominal_summary.native10M.summary.categories.coreference.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.categories.causality.seed | 42 |
| original_nominal_summary.native10M.summary.categories.causality.repetitions | 2000 |
| original_nominal_summary.native10M.summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_nominal_summary.native10M.summary.total_choice_tokens | 1842 |
| original_nominal_summary.native10M.summary.total_common_choice_bytes | 5798 |
| original_nominal_summary.native10M.summary.static_candidate_preference_case_accuracy | 0.5 |
| original_nominal_summary.native10M.summary.static_candidate_preference_both_correct | 0 |
| original_nominal_summary.native10M.total_forward_tokens | 11204 |
| effective_content_cluster_summary.teacher.accuracy.point | 0.7291666666666666 |
| effective_content_cluster_summary.teacher.accuracy.ci95 | [0.6666666666666666, 0.7957044107965766] |
| effective_content_cluster_summary.teacher.accuracy.units | 64 |
| effective_content_cluster_summary.teacher.accuracy.examples | 192 |
| effective_content_cluster_summary.teacher.accuracy.unit | "family/prompt" |
| effective_content_cluster_summary.teacher.accuracy.seed | 42 |
| effective_content_cluster_summary.teacher.accuracy.repetitions | 2000 |
| effective_content_cluster_summary.teacher.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.point | 0.4583333333333333 |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.ci95 | [0.3333333333333333, 0.5914088215931533] |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.units | 64 |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.examples | 96 |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.unit | "family/prompt" |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.seed | 42 |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.repetitions | 2000 |
| effective_content_cluster_summary.teacher.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| effective_content_cluster_summary.native10M.accuracy.point | 0.6197916666666666 |
| effective_content_cluster_summary.native10M.accuracy.ci95 | [0.5537491420727522, 0.6836806892568348] |
| effective_content_cluster_summary.native10M.accuracy.units | 64 |
| effective_content_cluster_summary.native10M.accuracy.examples | 192 |
| effective_content_cluster_summary.native10M.accuracy.unit | "family/prompt" |
| effective_content_cluster_summary.native10M.accuracy.seed | 42 |
| effective_content_cluster_summary.native10M.accuracy.repetitions | 2000 |
| effective_content_cluster_summary.native10M.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.point | 0.28125 |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.ci95 | [0.16161616161616163, 0.40014851485148434] |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.units | 64 |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.examples | 96 |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.unit | "family/prompt" |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.seed | 42 |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.repetitions | 2000 |
| effective_content_cluster_summary.native10M.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| effective_paired_teacher_minus_native_accuracy.point | 0.109375 |
| effective_paired_teacher_minus_native_accuracy.ci95 | [0.0, 0.22] |
| effective_paired_teacher_minus_native_accuracy.units | 64 |
| effective_paired_teacher_minus_native_accuracy.examples | 192 |
| effective_paired_teacher_minus_native_accuracy.unit | "family/prompt" |
| effective_paired_teacher_minus_native_accuracy.seed | 42 |
| effective_paired_teacher_minus_native_accuracy.repetitions | 2000 |
| effective_paired_teacher_minus_native_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| original_signal_gate_passed | true |
| conservative_context_signal_gate_passed | false |
| categories.negation.teacher | 0.5 |
| categories.quantity.teacher | 0.65625 |
| categories.time.teacher | 0.96875 |
| categories.comparison.teacher | 0.6875 |
| categories.coreference.teacher | 0.5625 |
| categories.causality.teacher | 1.0 |
| GPU_seconds | 7.486655257001985 |
| no_new_GPU_or_training_for_alias_adjustment | true |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| Base_complete | false |
| protected_test_records_JSON_decoded | false |
| decision | "Do not proceed to knowledge-transfer training on this diagnostic: the conservative content-cluster gate is not met." |
| limitations | "Exact duplicate family aliases are clustered while all192 original case weights and historic outcomes are retained. Constructed templates remain correlated beyond exact duplicates; CIs describe this dev packet, not a population of natural Japanese tasks. External teacher differs in data/tokenizer/architecture/post-training and contamination is unknown. The teacher is worse on negation/coreference; transfer can regress those skills and must keep retention/whole-Base gates. This is not Base adoption or knowledge-transfer success." |
| next_action_pointer_repaired | "Corrected an unconditional future-probe pointer to follow the unchanged false conservative gate; outcomes, statistics and adoption criteria unchanged." |

</details>

<details>
<summary>reports/phase6/web_kl_EOS_component_diagnostic.json — actual_CPU16_train_window_EOS_component_diagnostic_complete</summary>

[原記録](../../reports/phase6/web_kl_EOS_component_diagnostic.json) ／ SHA256: `07432ad723d2e1be2267ccd3e1633de8a50ab99ea62beb2f29ca3ff9ec4a3e93` ／ 6,327 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU16_train_window_EOS_component_diagnostic_complete" |
| source_sha256.scripts/diagnose_web_kl_eos_component.py | "56c0bd57f149dd5011983235c7c5f6b18184fac6116ec0a76a0e9a61c98ea844" |
| source_sha256.scripts/web_kl_eos_decomposition.py | "5b60964952db3b81e8b3394bb561057b7f80dcbac08d34a9971e8a5d2125215d" |
| source_sha256.tests/test_web_kl_eos_decomposition.py | "0ce9cda43ab877868d3624fd7d41975980bea67bc4245de39a2fcabd53e63c75" |
| physical_input_tokens | 16384 |
| results.staged_CE.EOS_mass_KL.mean | 0.013618256547452306 |
| results.staged_CE.EOS_mass_KL.quantiles | [4.2115160210351e-14, 2.729340676561054e-07, 2.639163267845803e-06, 2.5497295664734825e-05, 4.975801787216803] |
| results.staged_CE.weighted_conditional_non_EOS_KL.mean | 0.48952366029168776 |
| results.staged_CE.weighted_conditional_non_EOS_KL.quantiles | [5.682912973087056e-06, 0.12782112431816528, 0.3287723459273261, 0.6165211421617567, 11.65251701779297] |
| results.staged_CE.parent_EOS_probability.mean | 0.0018135968412875117 |
| results.staged_CE.parent_EOS_probability.quantiles | [2.4041046914342617e-10, 1.1226483897228767e-06, 6.03755568297929e-06, 4.191233322992931e-05, 0.8292607418661353] |
| results.staged_CE.student_EOS_probability.mean | 0.01081806552018662 |
| results.staged_CE.student_EOS_probability.quantiles | [4.9655418037711394e-11, 6.73503954095807e-07, 4.049319529414161e-06, 3.22185301764926e-05, 0.9959061727267919] |
| results.staged_CE.EOS_logit_KL_derivative.mean | 0.009004468678899109 |
| results.staged_CE.EOS_logit_KL_derivative.quantiles | [-0.36903349545447856, -5.270678813847222e-06, -1.3429745997044943e-07, 4.141424613453116e-06, 0.9524116588148166] |
| results.staged_CE.EOS_gradient_position_counts.positive | 7386 |
| results.staged_CE.EOS_gradient_position_counts.negative | 8934 |
| results.staged_CE.EOS_gradient_position_counts.zero | 0 |
| results.staged_CE_parent_KL.EOS_mass_KL.mean | 0.00021607731409352093 |
| results.staged_CE_parent_KL.EOS_mass_KL.quantiles | [3.997901703588955e-15, 6.239238547843307e-08, 5.168829092284908e-07, 4.09731398490194e-06, 0.14512986684224768] |
| results.staged_CE_parent_KL.weighted_conditional_non_EOS_KL.mean | 0.029941325537571166 |
| results.staged_CE_parent_KL.weighted_conditional_non_EOS_KL.quantiles | [7.106736125815322e-07, 0.007342089288851716, 0.018262281168301316, 0.03442683572083462, 2.7042919613320526] |
| results.staged_CE_parent_KL.parent_EOS_probability.mean | 0.0018135968412875117 |
| results.staged_CE_parent_KL.parent_EOS_probability.quantiles | [2.4041046914342617e-10, 1.1226483897228767e-06, 6.03755568297929e-06, 4.191233322992931e-05, 0.8292607418661353] |
| results.staged_CE_parent_KL.student_EOS_probability.mean | 0.0016391239363889502 |
| results.staged_CE_parent_KL.student_EOS_probability.quantiles | [3.191257087459707e-10, 1.711751111712247e-06, 9.295435808464713e-06, 6.018777125860324e-05, 0.7121796456430152] |
| results.staged_CE_parent_KL.EOS_logit_KL_derivative.mean | -0.0001744729048985614 |
| results.staged_CE_parent_KL.EOS_logit_KL_derivative.quantiles | [-0.18634314001451668, 7.17768339301587e-08, 1.314351969990275e-06, 1.0075728894734274e-05, 0.20511024322139357] |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.positive | 13377 |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.negative | 2943 |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.zero | 0 |
| CPU_elapsed_seconds | 9.290633116994286 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_source_tokens | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Small overlapping train-replay window, FP32 diagnostic and shared weights; an EOS-gradient sign does not prove unique cause of free generation failure or generalization. No teacher/coefficient/temperature/order/LR/source sweep is authorized by this diagnostic." |

</details>

<details>
<summary>reports/phase6/web_kl_comparison_completion.json — parent_Web_KL_terminal_pilot_reviewed</summary>

[原記録](../../reports/phase6/web_kl_comparison_completion.json) ／ SHA256: `dccf2d4af86b828c7141611ea4ab75084d972a36fef62961800251278cad927c` ／ 6,228 bytes

| 原キー | 保存値 |
|---|---|
| status | "parent_Web_KL_terminal_pilot_reviewed" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v3-20261006/web_kl/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| ordinary_CE_teacher_tokens | 100000000 |
| main_input_tokens | 100532224 |
| reference_input_tokens | 25133056 |
| combined_student_input_tokens | 125665280 |
| known_verification_teacher_tokens | 2615934 |
| known_verification_reference_input_tokens | 655360 |
| known_verification_reference_soft_positions | 652678 |
| failed_first_executed_update_count | "unknown; missing terminal checkpoint is not proof of zero updates" |
| science_GPU_seconds | 333.1955945980153 |
| all_verification_GPU_seconds | 68.28032470002654 |
| all_GPU_seconds | 401.47591929804184 |
| total_GPU_ceiling_seconds | 900 |
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
| summaries.web_kl.BPB | 0.982266745272942 |
| summaries.web_kl.rates.eos | 40 |
| summaries.web_kl.rates.repetition | 22 |
| summaries.web_kl.rates.unicode_failure | 0 |
| summaries.web_kl.rates.role_leak | 0 |
| summaries.web_kl.rates.empty | 0 |
| summaries.web_kl.grammar2 | 58 |
| summaries.web_kl.relevance2 | 47 |
| summaries.web_kl.coherent | 9 |
| summaries.web_kl.appropriate | 25 |
| summaries.web_kl.notes_sha256 | "66129a961bc6e66e641b4560db6dfcafeba078ad4497e018152cc6f73354ebd7" |
| summaries.web_kl.additional_teacher_tokens | 100000000 |
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
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.all_four_source_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| reference_accounting.frozen_parent_teacher_digest_verified | true |
| reference_accounting.reference_input_tokens | 25133056 |
| reference_accounting.main_ordinary_CE_teacher_tokens | 100000000 |
| reference_accounting.combined_student_physical_input_tokens | 125665280 |
| reference_accounting.newly_prepared_source_tokens | 0 |
| paired_likelihood_diagnostic.body_NLL_worse | 0 |
| paired_likelihood_diagnostic.body_NLL_better | 256 |
| paired_likelihood_diagnostic.gold_EOS_NLL_better | 33 |
| paired_likelihood_diagnostic.gold_EOS_NLL_worse | 223 |
| paired_likelihood_diagnostic.body_bytes | 472055 |
| paired_likelihood_diagnostic.body_tokens | 122343 |
| paired_likelihood_diagnostic.GPU_seconds | 0 |
| paired_likelihood_diagnostic.note | "Existing paired raw likelihoods only; true-end gold EOS is not proof of appropriate generated stopping." |
| eligible_for_final_Base_validation | false |
| newly_prepared_source_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/web_kl_comparison_launch.json — actual_resident_CUDA_verified_science_launched</summary>

[原記録](../../reports/phase6/web_kl_comparison_launch.json) ／ SHA256: `bba4395ac40b362af707b014fab742b29f373b6fec2ebcdd39a52a041c515a42` ／ 3,621 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_resident_CUDA_verified_science_launched" |
| initial_parent_preservation.parent_sampler_lineage | true |
| initial_parent_preservation.frozen_teacher_weights | true |
| initial_parent_preservation.frozen_teacher_eval_no_grad | true |
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
| full_resume_checks.KL_state | true |
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
| full_resume_checks.history_reference_KL_loss | true |
| full_resume_checks.history_reference_input_tokens | true |
| full_resume_checks.history_reference_soft_target_body_positions | true |
| full_resume_checks.history_reference_ignored_positions | true |
| full_resume_checks.history_reference_digest | true |
| full_resume_checks.history_combined_student_physical_input_tokens | true |
| full_resume_checks.finite | true |
| full_resume_checks.no_reheat | true |
| all32_v2_update_trajectory_identical | true |
| previous_step_seconds | 0.18295786051021423 |
| resident_step_seconds | 0.08078513699001633 |
| prior_GPU_seconds | 39.5885307630233 |
| resident_probe_GPU_seconds | 28.69179393700324 |
| known_verification_teacher_tokens | 2615934 |
| known_verification_reference_input_tokens | 655360 |
| known_verification_reference_soft_positions | 652678 |
| failed_v1_executed_update_count | "unknown; missing terminal checkpoint is not proof of zero updates" |
| estimated_science_GPU_seconds_with_margin | 574.2763272235491 |
| estimated_all_GPU_seconds | 642.5566519235756 |
| total_GPU_ceiling_seconds | 900 |
| scientific_ordinary_CE_budget | 100000000 |
| scientific_reference_input_budget | 25133056 |
| newly_prepared_source_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>
