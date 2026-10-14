# 学習目的・最適化・正則化 — 7/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/compare-result.json — Fisher100M_GPU_complete_pending_all80_content_review</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/compare-result.json) ／ SHA256: `3bac8b98a523403c74ebd8ee4e175d7cbfec3291262e7ef71d7aeafc4641297b` ／ 633,561 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.fisher_anchor.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/checkpoint-00326571.pt" |
| checkpoints.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| checkpoints.fisher_anchor.binding.config_sha256 | "feaf459349182ed9bd60c2840236b8d79a7ac660d3b98c6a086d06dd589c2cfe" |
| checkpoints.fisher_anchor.binding.arm | "fisher_anchor" |
| checkpoints.fisher_anchor.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.fisher_anchor.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.fisher_anchor.binding.teacher_goals.web | 75000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.story | 5000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.binding.study_kind | "fixed_context_conditional_MC_Fisher_parameter_anchor_v1" |
| checkpoints.fisher_anchor.binding.parameter_coefficient | 0.04161064039180984 |
| checkpoints.fisher_anchor.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.fisher_anchor.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.fisher_anchor.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.fisher_anchor.binding.optimizer_policy | "inherit" |
| checkpoints.fisher_anchor.binding.peak_lr | 1e-05 |
| checkpoints.fisher_anchor.binding.field_binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.fisher_anchor.binding.field_binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.fisher_anchor.binding.field_binding.field_tensor_digest | "5e3dda1f062597a173882be729b618beaec1d41c99481976e23a3ab8d6c47c40" |
| checkpoints.fisher_anchor.binding.field_binding.artifact_sha256 | "16771b045bbdf2031df964a8b5dbf02fbf6c6d444e0c783e39d8a7a05e9192b3" |
| checkpoints.fisher_anchor.binding.field_binding.estimator_config_sha256 | "a5ca482667e649d1a3449681636a04c0494409cc5fce150f5d7f6fd746f069d2" |
| checkpoints.fisher_anchor.update | 326571 |
| checkpoints.fisher_anchor.tokens | 10701078528 |
| checkpoints.fisher_anchor.supervised_tokens | 10677786961 |
| checkpoints.fisher_anchor.additional_supervised_tokens | 100000000 |
| checkpoints.fisher_anchor.additional_input_tokens | 100532224 |
| checkpoints.fisher_anchor.source_teachers.web | 75000000 |
| checkpoints.fisher_anchor.source_teachers.story | 5000000 |
| checkpoints.fisher_anchor.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.source_teachers.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.source_eos.web | 159447 |
| checkpoints.fisher_anchor.source_eos.story | 38240 |
| checkpoints.fisher_anchor.source_eos.ordinary_textbook | 74183 |
| checkpoints.fisher_anchor.source_eos.conditional_textbook | 234328 |
| checkpoints.fisher_anchor.source_input_tokens.web | 75183104 |
| checkpoints.fisher_anchor.source_input_tokens.story | 5039104 |
| checkpoints.fisher_anchor.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.fisher_anchor.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.fisher_anchor.source_focus_teachers.web | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.story | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.fisher_anchor.focus_teacher_tokens | 1407427 |
| checkpoints.fisher_anchor.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.fisher_anchor.weighted_teacher_mass | 100000000 |
| checkpoints.fisher_anchor.outcome_weight | 1 |
| checkpoints.fisher_anchor.training_seconds | 191.09000243237824 |
| checkpoints.fisher_anchor.completed_at | "2026-10-06T12:59:19.232803Z" |
| checkpoints.fisher_anchor.parameter_coefficient | 0.04161064039180984 |
| checkpoints.fisher_anchor.parameter_penalty_teacher_tokens | 0 |
| checkpoints.fisher_anchor.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.fisher_anchor.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.fisher_anchor.sampler.goals.web | 75000000 |
| checkpoints.fisher_anchor.sampler.goals.story | 5000000 |
| checkpoints.fisher_anchor.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.context | 1024 |
| checkpoints.fisher_anchor.sampler.seed | 42 |
| checkpoints.fisher_anchor.sampler.position | 3068 |
| checkpoints.fisher_anchor.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.fisher_anchor.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.context | 1024 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.fisher_anchor.sampler.streams.story.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.story.genre | "story" |
| checkpoints.fisher_anchor.sampler.streams.story.documents | 761448 |
| checkpoints.fisher_anchor.sampler.streams.story.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.story.document_position | 38243 |
| checkpoints.fisher_anchor.sampler.streams.story.token_offset | 87 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.fisher_anchor.sampler.source_teachers.web | 75000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.story | 5000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.source_eos.web | 159447 |
| checkpoints.fisher_anchor.sampler.source_eos.story | 38240 |
| checkpoints.fisher_anchor.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.fisher_anchor.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.fisher_anchor.sampler.source_tokens.web | 75183104 |
| checkpoints.fisher_anchor.sampler.source_tokens.story | 5039104 |
| checkpoints.fisher_anchor.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.fisher_anchor.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.web | 292167653 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.story | 20452979 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.web | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.story | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.fisher_anchor.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.fisher_anchor.source_body_bytes.web | 292167653 |
| checkpoints.fisher_anchor.source_body_bytes.story | 20452979 |
| checkpoints.fisher_anchor.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.fisher_anchor.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.fisher_anchor.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| evaluations.fisher_anchor.binding.teacher_goals.web | 75000000 |
| evaluations.fisher_anchor.binding.teacher_goals.story | 5000000 |
| evaluations.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| evaluations.fisher_anchor.body.documents | 256 |
| evaluations.fisher_anchor.body.limit_documents | 256 |
| evaluations.fisher_anchor.body.body_nll | 322293.0505590439 |
| evaluations.fisher_anchor.body.eos_nll | 579.8090896382928 |
| evaluations.fisher_anchor.body.body_bytes | 472055 |
| evaluations.fisher_anchor.body.body_tokens | 122343 |
| evaluations.fisher_anchor.body.bpb | 0.9849923965523267 |
| evaluations.fisher_anchor.body.seconds | 1.5506487939856015 |
| evaluations.fisher_anchor.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.fisher_anchor.generation.max_new_tokens | 64 |
| evaluations.fisher_anchor.greedy_rates.eos | 65 |
| evaluations.fisher_anchor.greedy_rates.repetition | 7 |
| evaluations.fisher_anchor.greedy_rates.unicode_failure | 0 |
| evaluations.fisher_anchor.greedy_rates.role_leak | 0 |
| evaluations.fisher_anchor.greedy_rates.empty | 0 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.5729166666666666] |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.46875, 0.53125] |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.macro_f1 | 0.4995112414467253 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7341389728096677 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42334494773519166 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.fisher_anchor.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.point | 0.3221626452189455 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.ci95 | [0.29535299374441465, 0.3489722966934763] |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2957998212689902 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26899016979445933, 0.32350312779267204] |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2957998212689902 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29495447835836136 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.mcc | 0.1201864675199048 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.fisher_anchor.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.fisher_anchor.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.fisher_anchor.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.fisher_anchor.protected_test_used | false |
| transfer.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| transfer.fisher_anchor.checks.weights_unchanged | true |
| transfer.fisher_anchor.checks.no_gradients | true |
| transfer.fisher_anchor.checks.eval_mode | true |
| transfer.fisher_anchor.checks.RNG_restored | true |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 68 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 53 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 73 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.fisher_anchor.optimizer_updates | 0 |
| transfer.fisher_anchor.scientific_teacher_tokens | 0 |
| transfer.fisher_anchor.protected_test_used | false |
| transfer.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| retention.fisher_anchor.checks.weights_unchanged | true |
| retention.fisher_anchor.checks.no_gradients | true |
| retention.fisher_anchor.checks.eval_mode | true |
| retention.fisher_anchor.checks.RNG_restored | true |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 48 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 56 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 65 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 41 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.fisher_anchor.optimizer_updates | 0 |
| retention.fisher_anchor.scientific_teacher_tokens | 0 |
| retention.fisher_anchor.protected_test_used | false |
| retention.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| all_scientific_input_streams_match | true |
| status | "Fisher100M_GPU_complete_pending_all80_content_review" |
| GPU_seconds | 257.28610576700885 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/content-notes.json) ／ SHA256: `99ff97f68c8dc524ba2cf62a0bb9f29bf5f73ff24e652ba964af7d1e5ab4549f` ／ 46,996 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/body.json) ／ SHA256: `e702057f0932d3f0d5ae8dfa94cef8aedf38304ec517f418882cf8ad1110885b` ／ 67,842 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 322293.0505590439 |
| body.eos_nll | 579.8090896382928 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9849923965523267 |
| body.seconds | 1.5506487939856015 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/generation.json) ／ SHA256: `24b8b91f15b5b510ea6140b508e7e778a5211eb006b123701f79d8b7fe34679b` ／ 80,761 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jblimp.json) ／ SHA256: `3b903964f654d826cc56dba106baaf48c7c7028cde4de4c6f15b805f642b6e54` ／ 339,058 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7522658610271903 |
| summary.primary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7522658610271903 |
| summary.per_token_secondary.accuracy.point | 0.7341389728096677 |
| summary.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| summary.per_token_secondary.macro_f1 | 0.42334494773519166 |
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
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jcqa.json) ／ SHA256: `94a7bd741fbd225ec03716da177c793196a22dda4af5596c0ababb3b3b6a5830` ／ 1,641,670 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.3221626452189455 |
| summary.primary.accuracy.ci95 | [0.29535299374441465, 0.3489722966934763] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.32171581769436997 |
| summary.per_token_secondary.accuracy.point | 0.2957998212689902 |
| summary.per_token_secondary.accuracy.ci95 | [0.26899016979445933, 0.32350312779267204] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.2957998212689902 |
| summary.per_token_secondary.macro_f1 | 0.29495447835836136 |
| summary.per_token_secondary.mcc | 0.1201864675199048 |
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
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/result.json) ／ SHA256: `59f7c4742cddfe20e87839400fdaab7d013712a85444ba6df4b9007df9dccca6` ／ 174,630 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 322293.0505590439 |
| body.eos_nll | 579.8090896382928 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9849923965523267 |
| body.seconds | 1.5506487939856015 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 65 |
| greedy_rates.repetition | 7 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.5729166666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.46875, 0.53125] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.4995112414467253 |
| diagnostics.semantics.per_token_secondary.mcc | 0.0 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7341389728096677 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42334494773519166 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| diagnostics.jcqa.primary.accuracy.point | 0.3221626452189455 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.29535299374441465, 0.3489722966934763] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2957998212689902 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26899016979445933, 0.32350312779267204] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2957998212689902 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29495447835836136 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.1201864675199048 |
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
| diagnostics.semantic_both_contexts.correct | 12 |
| memory.maximum_observed_allocated_bytes | 315223040 |
| memory.maximum_observed_reserved_bytes | 13325303808 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/semantics.json) ／ SHA256: `9a85f818375774891129451c85b09b43b46ae70d5a659cdb4ddb5336100fd517` ／ 203,816 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5260416666666666 |
| summary.primary.accuracy.ci95 | [0.4791666666666667, 0.5729166666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5260416666666666 |
| summary.per_token_secondary.accuracy.point | 0.5 |
| summary.per_token_secondary.accuracy.ci95 | [0.46875, 0.53125] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5 |
| summary.per_token_secondary.macro_f1 | 0.4995112414467253 |
| summary.per_token_secondary.mcc | 0.0 |
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
<summary>reports/phase6/fisher-parameter-anchor-20261006/field/job.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/field/job.json) ／ SHA256: `fdf98d477186c23afc164c897d819ab7c47b8d2be794507a17c1ef826427f0fa` ／ 662 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 3.6230295989953447 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/field/result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/field/result.json) ／ SHA256: `1cb28098ac0bd7a4046ddd9e4513fdbf56cc5926dd9de0c545448a27e2a5bb3b` ／ 12,255 bytes

| 原キー | 保存値 |
|---|---|
| passed | true |
| checks.weights_unchanged | true |
| checks.RNG_unchanged | true |
| checks.parameter_grads_unchanged | true |
| checks.native_unique_10M | true |
| checks.native_unique119 | true |
| checks.exact_cost | true |
| settings.seed | 2026100647 |
| settings.sampled_vocabulary | "full_native_4096" |
| accounting.sampled_score_labels | 65276 |
| accounting.physical_context_tokens | 65536 |
| accounting.ordinary_source_CE_teacher_tokens | 0 |
| accounting.optimizer_updates | 0 |
| sampled_labels_tensor_digest | "2bf7550ba830b50f61ad22f4fc3ca3930960aa2619d3016ad9d564b71ac3f1f0" |
| GPU_seconds | 3.6230295989953447 |
| Base_complete | false |
| scientific_launched | false |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/latest.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/latest.json) ／ SHA256: `4e731def2b392a39b1368b55b7cfcef9475e02dbb819035720e55f8d35e37da5` ／ 285 bytes

| 原キー | 保存値 |
|---|---|
| update | 326571 |
| tokens_seen | 10701078528 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/job.json) ／ SHA256: `6b0592860f717588b5985bc831faf2287762a0aace7adef09040739d1c95a26c` ／ 927 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 257.28610576700885 |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| loss | 0.27220389246940613 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/latest.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/latest.json) ／ SHA256: `8fb5b222c79688389e0c1fa971a59ddfc889f0a58ed3f023e50ab474a5292f47` ／ 280 bytes

| 原キー | 保存値 |
|---|---|
| update | 323535 |
| tokens_seen | 10601594880 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/job.json) ／ SHA256: `6ecf222c4b68f5a7daaf47c7679f168e1b31ceac7167dadbab5d3d0304e632ee` ／ 549 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 19.161004059016705 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/progress-result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/progress-result.json) ／ SHA256: `db2fbe1520d83d0f655d8752d8f8867928e2e7854416a08d86d1ab2ebe337c87` ／ 79,309 bytes

| 原キー | 保存値 |
|---|---|
| gates.fisher_anchor.passed | true |
| gates.fisher_anchor.checks.model | true |
| gates.fisher_anchor.checks.optimizer | true |
| gates.fisher_anchor.checks.scheduler | true |
| gates.fisher_anchor.checks.rng | true |
| gates.fisher_anchor.checks.sampler | true |
| gates.fisher_anchor.checks.lineage | true |
| gates.fisher_anchor.checks.tokens | true |
| gates.fisher_anchor.checks.supervised_tokens | true |
| gates.fisher_anchor.checks.body_bytes | true |
| gates.fisher_anchor.checks.token_digest | true |
| gates.fisher_anchor.checks.focus_token_digest | true |
| gates.fisher_anchor.checks.focus_teacher_tokens | true |
| gates.fisher_anchor.checks.weighted_teacher_mass | true |
| gates.fisher_anchor.checks.update | true |
| gates.fisher_anchor.checks.spec | true |
| gates.fisher_anchor.checks.model_config | true |
| gates.fisher_anchor.checks.pilot_binding | true |
| gates.fisher_anchor.checks.study_binding | true |
| gates.fisher_anchor.checks.history_loss | true |
| gates.fisher_anchor.checks.history_gradient_norm | true |
| gates.fisher_anchor.checks.history_lr | true |
| gates.fisher_anchor.checks.history_token_digest | true |
| gates.fisher_anchor.checks.history_source_teachers | true |
| gates.fisher_anchor.checks.history_source_eos | true |
| gates.fisher_anchor.checks.history_source_input_tokens | true |
| gates.fisher_anchor.checks.history_source_body_bytes | true |
| gates.fisher_anchor.checks.history_source_focus_teachers | true |
| gates.fisher_anchor.checks.history_focus_token_digest | true |
| gates.fisher_anchor.checks.history_focus_teacher_tokens | true |
| gates.fisher_anchor.checks.history_weighted_teacher_mass | true |
| gates.fisher_anchor.checks.finite | true |
| gates.fisher_anchor.checks.no_reheat | true |
| gates.fisher_anchor.checks.history_CE_loss | true |
| gates.fisher_anchor.checks.history_parameter_penalty | true |
| gates.fisher_anchor.checks.history_parameter_coefficient | true |
| gates.fisher_anchor.checks.history_parameter_penalty_teacher_tokens | true |
| gates.fisher_anchor.GPU_optimizer_updates | 8 |
| gates.fisher_anchor.verification_teacher_tokens | 261616 |
| timings.fisher_anchor.verification_teacher_tokens | 1046336 |
| timings.fisher_anchor.terminal_save_seconds | 0.17179205399588682 |
| timings.fisher_anchor.peak_VRAM_bytes | 6269121024 |
| timings.fisher_anchor.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/checkpoint.pt" |
| timings.fisher_anchor.checkpoint.sha256 | "55de749961795456c056665538a61876034ccced3deb606ac2dd031785db5e1a" |
| initial_fullstate_preservation.fisher_anchor.parent_sampler_lineage | true |
| initial_fullstate_preservation.fisher_anchor.all_checks | true |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/probe/result.json — own_Fisher_probe_complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/probe/result.json) ／ SHA256: `164e712ade4445aebefcb961531ef04ef7d82c60a0ad96dd6628a0e3d2f55d2a` ／ 79,819 bytes

| 原キー | 保存値 |
|---|---|
| gates.fisher_anchor.passed | true |
| gates.fisher_anchor.checks.model | true |
| gates.fisher_anchor.checks.optimizer | true |
| gates.fisher_anchor.checks.scheduler | true |
| gates.fisher_anchor.checks.rng | true |
| gates.fisher_anchor.checks.sampler | true |
| gates.fisher_anchor.checks.lineage | true |
| gates.fisher_anchor.checks.tokens | true |
| gates.fisher_anchor.checks.supervised_tokens | true |
| gates.fisher_anchor.checks.body_bytes | true |
| gates.fisher_anchor.checks.token_digest | true |
| gates.fisher_anchor.checks.focus_token_digest | true |
| gates.fisher_anchor.checks.focus_teacher_tokens | true |
| gates.fisher_anchor.checks.weighted_teacher_mass | true |
| gates.fisher_anchor.checks.update | true |
| gates.fisher_anchor.checks.spec | true |
| gates.fisher_anchor.checks.model_config | true |
| gates.fisher_anchor.checks.pilot_binding | true |
| gates.fisher_anchor.checks.study_binding | true |
| gates.fisher_anchor.checks.history_loss | true |
| gates.fisher_anchor.checks.history_gradient_norm | true |
| gates.fisher_anchor.checks.history_lr | true |
| gates.fisher_anchor.checks.history_token_digest | true |
| gates.fisher_anchor.checks.history_source_teachers | true |
| gates.fisher_anchor.checks.history_source_eos | true |
| gates.fisher_anchor.checks.history_source_input_tokens | true |
| gates.fisher_anchor.checks.history_source_body_bytes | true |
| gates.fisher_anchor.checks.history_source_focus_teachers | true |
| gates.fisher_anchor.checks.history_focus_token_digest | true |
| gates.fisher_anchor.checks.history_focus_teacher_tokens | true |
| gates.fisher_anchor.checks.history_weighted_teacher_mass | true |
| gates.fisher_anchor.checks.finite | true |
| gates.fisher_anchor.checks.no_reheat | true |
| gates.fisher_anchor.checks.history_CE_loss | true |
| gates.fisher_anchor.checks.history_parameter_penalty | true |
| gates.fisher_anchor.checks.history_parameter_coefficient | true |
| gates.fisher_anchor.checks.history_parameter_penalty_teacher_tokens | true |
| gates.fisher_anchor.GPU_optimizer_updates | 8 |
| gates.fisher_anchor.verification_teacher_tokens | 261616 |
| timings.fisher_anchor.verification_teacher_tokens | 1046336 |
| timings.fisher_anchor.terminal_save_seconds | 0.17179205399588682 |
| timings.fisher_anchor.peak_VRAM_bytes | 6269121024 |
| timings.fisher_anchor.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/checkpoint.pt" |
| timings.fisher_anchor.checkpoint.sha256 | "55de749961795456c056665538a61876034ccced3deb606ac2dd031785db5e1a" |
| initial_fullstate_preservation.fisher_anchor.parent_sampler_lineage | true |
| initial_fullstate_preservation.fisher_anchor.all_checks | true |
| passed | true |
| scientific_teacher_tokens | 0 |
| GPU_optimizer_updates | 40 |
| verification_teacher_tokens | 1307952 |
| status | "own_Fisher_probe_complete" |
| GPU_seconds | 19.161004059016705 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/progress-result.json) ／ SHA256: `c9d012cbdaaf6e0ec80c356bb9d9317644411a4398b797dfa5feefacfb8818ff` ／ 632,811 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.fisher_anchor.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/checkpoint-00326571.pt" |
| checkpoints.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| checkpoints.fisher_anchor.binding.config_sha256 | "feaf459349182ed9bd60c2840236b8d79a7ac660d3b98c6a086d06dd589c2cfe" |
| checkpoints.fisher_anchor.binding.arm | "fisher_anchor" |
| checkpoints.fisher_anchor.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.fisher_anchor.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.fisher_anchor.binding.teacher_goals.web | 75000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.story | 5000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.binding.study_kind | "fixed_context_conditional_MC_Fisher_parameter_anchor_v1" |
| checkpoints.fisher_anchor.binding.parameter_coefficient | 0.04161064039180984 |
| checkpoints.fisher_anchor.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.fisher_anchor.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.fisher_anchor.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.fisher_anchor.binding.optimizer_policy | "inherit" |
| checkpoints.fisher_anchor.binding.peak_lr | 1e-05 |
| checkpoints.fisher_anchor.binding.field_binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.fisher_anchor.binding.field_binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.fisher_anchor.binding.field_binding.field_tensor_digest | "5e3dda1f062597a173882be729b618beaec1d41c99481976e23a3ab8d6c47c40" |
| checkpoints.fisher_anchor.binding.field_binding.artifact_sha256 | "16771b045bbdf2031df964a8b5dbf02fbf6c6d444e0c783e39d8a7a05e9192b3" |
| checkpoints.fisher_anchor.binding.field_binding.estimator_config_sha256 | "a5ca482667e649d1a3449681636a04c0494409cc5fce150f5d7f6fd746f069d2" |
| checkpoints.fisher_anchor.update | 326571 |
| checkpoints.fisher_anchor.tokens | 10701078528 |
| checkpoints.fisher_anchor.supervised_tokens | 10677786961 |
| checkpoints.fisher_anchor.additional_supervised_tokens | 100000000 |
| checkpoints.fisher_anchor.additional_input_tokens | 100532224 |
| checkpoints.fisher_anchor.source_teachers.web | 75000000 |
| checkpoints.fisher_anchor.source_teachers.story | 5000000 |
| checkpoints.fisher_anchor.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.source_teachers.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.source_eos.web | 159447 |
| checkpoints.fisher_anchor.source_eos.story | 38240 |
| checkpoints.fisher_anchor.source_eos.ordinary_textbook | 74183 |
| checkpoints.fisher_anchor.source_eos.conditional_textbook | 234328 |
| checkpoints.fisher_anchor.source_input_tokens.web | 75183104 |
| checkpoints.fisher_anchor.source_input_tokens.story | 5039104 |
| checkpoints.fisher_anchor.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.fisher_anchor.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.fisher_anchor.source_focus_teachers.web | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.story | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.fisher_anchor.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.fisher_anchor.focus_teacher_tokens | 1407427 |
| checkpoints.fisher_anchor.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.fisher_anchor.weighted_teacher_mass | 100000000 |
| checkpoints.fisher_anchor.outcome_weight | 1 |
| checkpoints.fisher_anchor.training_seconds | 191.09000243237824 |
| checkpoints.fisher_anchor.completed_at | "2026-10-06T12:59:19.232803Z" |
| checkpoints.fisher_anchor.parameter_coefficient | 0.04161064039180984 |
| checkpoints.fisher_anchor.parameter_penalty_teacher_tokens | 0 |
| checkpoints.fisher_anchor.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.fisher_anchor.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.fisher_anchor.sampler.goals.web | 75000000 |
| checkpoints.fisher_anchor.sampler.goals.story | 5000000 |
| checkpoints.fisher_anchor.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.context | 1024 |
| checkpoints.fisher_anchor.sampler.seed | 42 |
| checkpoints.fisher_anchor.sampler.position | 3068 |
| checkpoints.fisher_anchor.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.fisher_anchor.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.context | 1024 |
| checkpoints.fisher_anchor.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.fisher_anchor.sampler.streams.story.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.story.genre | "story" |
| checkpoints.fisher_anchor.sampler.streams.story.documents | 761448 |
| checkpoints.fisher_anchor.sampler.streams.story.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.story.document_position | 38243 |
| checkpoints.fisher_anchor.sampler.streams.story.token_offset | 87 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.fisher_anchor.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.fisher_anchor.sampler.source_teachers.web | 75000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.story | 5000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.fisher_anchor.sampler.source_eos.web | 159447 |
| checkpoints.fisher_anchor.sampler.source_eos.story | 38240 |
| checkpoints.fisher_anchor.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.fisher_anchor.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.fisher_anchor.sampler.source_tokens.web | 75183104 |
| checkpoints.fisher_anchor.sampler.source_tokens.story | 5039104 |
| checkpoints.fisher_anchor.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.fisher_anchor.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.web | 292167653 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.story | 20452979 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.fisher_anchor.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.web | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.story | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.fisher_anchor.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.fisher_anchor.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.fisher_anchor.source_body_bytes.web | 292167653 |
| checkpoints.fisher_anchor.source_body_bytes.story | 20452979 |
| checkpoints.fisher_anchor.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.fisher_anchor.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.fisher_anchor.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| evaluations.fisher_anchor.binding.teacher_goals.web | 75000000 |
| evaluations.fisher_anchor.binding.teacher_goals.story | 5000000 |
| evaluations.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| evaluations.fisher_anchor.body.documents | 256 |
| evaluations.fisher_anchor.body.limit_documents | 256 |
| evaluations.fisher_anchor.body.body_nll | 322293.0505590439 |
| evaluations.fisher_anchor.body.eos_nll | 579.8090896382928 |
| evaluations.fisher_anchor.body.body_bytes | 472055 |
| evaluations.fisher_anchor.body.body_tokens | 122343 |
| evaluations.fisher_anchor.body.bpb | 0.9849923965523267 |
| evaluations.fisher_anchor.body.seconds | 1.5506487939856015 |
| evaluations.fisher_anchor.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.fisher_anchor.generation.max_new_tokens | 64 |
| evaluations.fisher_anchor.greedy_rates.eos | 65 |
| evaluations.fisher_anchor.greedy_rates.repetition | 7 |
| evaluations.fisher_anchor.greedy_rates.unicode_failure | 0 |
| evaluations.fisher_anchor.greedy_rates.role_leak | 0 |
| evaluations.fisher_anchor.greedy_rates.empty | 0 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.5729166666666666] |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.46875, 0.53125] |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.macro_f1 | 0.4995112414467253 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7341389728096677 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42334494773519166 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.fisher_anchor.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.point | 0.3221626452189455 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.ci95 | [0.29535299374441465, 0.3489722966934763] |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2957998212689902 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26899016979445933, 0.32350312779267204] |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2957998212689902 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29495447835836136 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.mcc | 0.1201864675199048 |
| evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.fisher_anchor.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.fisher_anchor.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.fisher_anchor.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.fisher_anchor.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.fisher_anchor.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.fisher_anchor.protected_test_used | false |
| transfer.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| transfer.fisher_anchor.checks.weights_unchanged | true |
| transfer.fisher_anchor.checks.no_gradients | true |
| transfer.fisher_anchor.checks.eval_mode | true |
| transfer.fisher_anchor.checks.RNG_restored | true |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 68 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 53 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 73 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.fisher_anchor.optimizer_updates | 0 |
| transfer.fisher_anchor.scientific_teacher_tokens | 0 |
| transfer.fisher_anchor.protected_test_used | false |
| transfer.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| retention.fisher_anchor.checks.weights_unchanged | true |
| retention.fisher_anchor.checks.no_gradients | true |
| retention.fisher_anchor.checks.eval_mode | true |
| retention.fisher_anchor.checks.RNG_restored | true |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 48 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 56 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 65 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 41 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.fisher_anchor.optimizer_updates | 0 |
| retention.fisher_anchor.scientific_teacher_tokens | 0 |
| retention.fisher_anchor.protected_test_used | false |
| retention.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/review.json — Fisher100M_all80_content_matched_control_reviewed</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/review.json) ／ SHA256: `df7cd9bbd111c24a1c01f3a7c2f8d12962c72d1bf983977e5876f986809466e7` ／ 5,149 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher100M_all80_content_matched_control_reviewed" |
| summaries.fisher_anchor.BPB | 0.9849923965523267 |
| summaries.fisher_anchor.rates.eos | 65 |
| summaries.fisher_anchor.rates.repetition | 7 |
| summaries.fisher_anchor.rates.unicode_failure | 0 |
| summaries.fisher_anchor.rates.role_leak | 0 |
| summaries.fisher_anchor.rates.empty | 0 |
| summaries.fisher_anchor.grammar2 | 63 |
| summaries.fisher_anchor.relevance2 | 66 |
| summaries.fisher_anchor.coherent | 28 |
| summaries.fisher_anchor.appropriate | 30 |
| summaries.fisher_anchor.notes_sha256 | "99ff97f68c8dc524ba2cf62a0bb9f29bf5f73ff24e652ba964af7d1e5ab4549f" |
| summaries.uniform_anchor.BPB | 0.9906670746607233 |
| summaries.uniform_anchor.rates.eos | 67 |
| summaries.uniform_anchor.rates.repetition | 6 |
| summaries.uniform_anchor.rates.unicode_failure | 0 |
| summaries.uniform_anchor.rates.role_leak | 0 |
| summaries.uniform_anchor.rates.empty | 0 |
| summaries.uniform_anchor.grammar2 | 59 |
| summaries.uniform_anchor.relevance2 | 60 |
| summaries.uniform_anchor.coherent | 25 |
| summaries.uniform_anchor.appropriate | 29 |
| summaries.uniform_anchor.notes_sha256 | "83e3ff51c39594a47db2165e4a79a490d66fed6bddd49e4a6e82c8ae3c83ef34" |
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
| accounting.completed_updates | 3068 |
| accounting.teachers | 100000000 |
| accounting.physical_input_positions | 100532224 |
| accounting.parameter_penalty_teacher_tokens | 0 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_teachers.ordinary_textbook | 10000000 |
| accounting.source_teachers.conditional_textbook | 10000000 |
| accounting.source_EOS.web | 159447 |
| accounting.source_EOS.story | 38240 |
| accounting.source_EOS.ordinary_textbook | 74183 |
| accounting.source_EOS.conditional_textbook | 234328 |
| quality_comparisons.uniform_anchor.checks.coherence_gain_at_least8 | false |
| quality_comparisons.uniform_anchor.checks.paired_CI_lower_above0 | false |
| quality_comparisons.uniform_anchor.checks.EOS_nonworsening | false |
| quality_comparisons.uniform_anchor.checks.repetition_nonworsening | false |
| quality_comparisons.uniform_anchor.checks.no_empty_role_unicode | true |
| quality_comparisons.uniform_anchor.checks.BPB_gate | true |
| quality_comparisons.uniform_anchor.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.uniform_anchor.passed | false |
| quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| quality_comparisons.strong_staged.checks.BPB_gate | true |
| quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.strong_staged.passed | false |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | true |
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| eligible_for_final_Base_validation | false |
| scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| field_model_sampled_labels | 65276 |
| verification_teacher_tokens | 1307952 |
| new_total_GPU_seconds | 280.0701394250209 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0000.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0000.json) ／ SHA256: `618c3c5ea16bd382007237c20f5c9138b30ab83c71f09915157eb5a763b057a8` ／ 9,972 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0016.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0016.json) ／ SHA256: `3e6fdad8a36e435c7e3a690d0fd885e1c92a0a88f7e54248fded5931a2da6da4` ／ 9,618 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0032.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0032.json) ／ SHA256: `3eed04719c428a768a174a537f67bd448c6e583bf0d0731eed9cd8866e913480` ／ 10,257 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0048.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0048.json) ／ SHA256: `cdd04fea2f56979fce0fe40c7b0e629bfb91460c742b06de516eb9bdc9dee86e` ／ 9,569 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0064.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0064.json) ／ SHA256: `636d6ca156eda1378166dcacf72cf5cdac761f9be4572c00486449aab0aa1366` ／ 10,350 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0080.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0080.json) ／ SHA256: `7bbd1ee34192c1ee1fa9718f03696b71b9081b660e2a0882b50b160fb7221938` ／ 9,760 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0096.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0096.json) ／ SHA256: `29f1710c389f7092a779b98a95cd49234016b45e194910d230cbecd83884e78c` ／ 9,838 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0112.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0112.json) ／ SHA256: `c9aed97e41f3234e167d39bf18c6a1e06b91bc30f771b58589485f1d7e1b20db` ／ 10,186 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0128.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0128.json) ／ SHA256: `8d1dd7b2003492d7b575fb80f1404ce0014475989d93c0dc4f39051ab2767a4f` ／ 9,860 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0144.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0144.json) ／ SHA256: `19be46462b77d24a6f801acc5a704e5e6bd9bbd12de75af0d02d301555c53a26` ／ 9,921 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0160.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0160.json) ／ SHA256: `21491182f50dad851d68768d70314fca53a8e29f57ea27e7f371bb15a6e51d13` ／ 10,184 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0176.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0176.json) ／ SHA256: `9302b7fb5e4914dc4843deacf25fb5d36f2469fc3a9bcb305de4e86b2d391bbb` ／ 10,029 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0192.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0192.json) ／ SHA256: `383f44814ad94bfdf456b3b3a95d897456d0cdc841bcf7763561e9171c239d31` ／ 9,939 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0208.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0208.json) ／ SHA256: `f993493ccf1e79ede2c773c88591e62376e58dafa14839be1d7c79f700901793` ／ 9,670 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0224.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0224.json) ／ SHA256: `6ff9568b9994c6fb6ffbb8a956b19cdb355be9eae9c895566303549c1bc27c6d` ／ 9,836 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0240.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0240.json) ／ SHA256: `c745e7143b0134154d182f55bb57679e7dc723bffe311243dc3263b3f58e5e52` ／ 9,647 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0256.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0256.json) ／ SHA256: `a1f5e66b7dd79b0515902284be31a4dfe23265c582e251a865d94aeea647bd19` ／ 9,681 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0272.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0272.json) ／ SHA256: `1a140290828b663585ce25a03a73a2d35404b1a9662ed803d8637cc6aa2af566` ／ 9,655 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0288.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0288.json) ／ SHA256: `719472069d7f76244a4b3d8916dc1b5dad428de515e37781d2d10236cbc57326` ／ 9,650 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0304.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0304.json) ／ SHA256: `06da2bd58ac43115dcf090818c633e14474b23c6dffa7587d16807f73114890b` ／ 9,850 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0320.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0320.json) ／ SHA256: `ca436a12cd5a458e57b87b76e0ecc26493761376c70bebe937999181bb52328e` ／ 9,372 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0336.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0336.json) ／ SHA256: `8ebc85baa52c8d12e7653eac06e09bd27166cd388770a9efd9d76a76c1a5caaa` ／ 9,449 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0352.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0352.json) ／ SHA256: `f52001540fdbf01d754e2f9476b86f93d39a8df1573331b5d2f2b09dea84a354` ／ 9,851 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0368.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0368.json) ／ SHA256: `a14d078944b7781a12ed8bb189f0a68828c554c5d5dde77aa23cc6294ebfd86a` ／ 9,596 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0384.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0384.json) ／ SHA256: `fb1c0ec18f9ec1fbc1b6abf2e5971af7f2d92eee8ac49c4ee021e747a616baec` ／ 9,889 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0400.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0400.json) ／ SHA256: `966ea1a8986790653fb80781719b926b2d6d20c8ac0c27b8d3c4520bc98e1af8` ／ 9,559 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0416.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0416.json) ／ SHA256: `c658f111d22bb674784592faf8c80a3a36bc6a4a5494b4f65165af4fba878cc6` ／ 9,923 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0432.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0432.json) ／ SHA256: `ecc034f5b710e03a99b1bc67036f0760a148c6128c2e5250538bf63b40a8f93d` ／ 9,394 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0448.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0448.json) ／ SHA256: `45fff2be54d73702e6f0db7a4b6bc518d46d14fba3529cc2e2748ee55dc77930` ／ 9,625 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0464.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0464.json) ／ SHA256: `b26bc36351ff96bcea2745987ff5dfe2da224fccc7e1c22cde0e3832eb0502ac` ／ 9,469 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0480.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0480.json) ／ SHA256: `dc67e8787f0390d1b17a3b2ebb4f2650e0258937ee9069fd864166ffa663f67b` ／ 9,485 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0496.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0496.json) ／ SHA256: `34bd2d0cada6cc588bcc531afc1b554459daa24270e166efbe1e51cbc8f5dd6d` ／ 9,559 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/result.json) ／ SHA256: `2bda525136b96a37247b38d32f767fc86414460c57e5ecbf69128418e9318111` ／ 186,160 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 68 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 53 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 73 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0000.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0000.json) ／ SHA256: `1699a49608f9ec2637d4582cab5fbf06f64b1dbfdbfae26ea420f42de24dfd84` ／ 7,985 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0016.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0016.json) ／ SHA256: `38847cf240a524870038f23f8e43d84e72d8e07eff4dece25313222d7e97ab87` ／ 8,351 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0032.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0032.json) ／ SHA256: `2a278897a4817cee2031ed2fce40254a1ef99999be8c09f68bebd615369fbf35` ／ 7,032 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0048.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0048.json) ／ SHA256: `f94bc6859ca553d71aacf0936099ec63de9e955603c4f70b7a674dcfae780f6b` ／ 8,178 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0064.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0064.json) ／ SHA256: `d00c8565f7636d804b648607dca2529bde419793aedfb7e87a69bb3a99eb69d4` ／ 8,520 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0080.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0080.json) ／ SHA256: `0c0d355a27d8130851299d4abeaf6fe3ae76cced9a158e3afefebb357b79f736` ／ 7,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0096.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0096.json) ／ SHA256: `a5c722a5ac81af3cf403f2d9fe471f6fb505498a8a26987dc21a4560bf0c9761` ／ 8,097 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0112.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0112.json) ／ SHA256: `cf3a5338aa046e6fbd11d2b86920de67359883ab01a244fe5d95de658a960e4b` ／ 8,292 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0128.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0128.json) ／ SHA256: `d75b7e8bf89aff518113fd39d363157c445106803d316eecfedbd3bf859af32c` ／ 7,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0144.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0144.json) ／ SHA256: `6171f24c4ff646bf2fe0cc35507848aba1975bfeea96260bec1b4a04525e5132` ／ 8,202 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0160.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0160.json) ／ SHA256: `67e3016dfbdb44034a1bb08369a3a1a706bc94f2d6351471cf9f0770bf4ab393` ／ 8,627 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0176.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0176.json) ／ SHA256: `457c1d666193b2d08764595d0c93ef0fa0c00849fd8ebd0dec2dcce17ff31ce6` ／ 6,970 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0192.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0192.json) ／ SHA256: `bee6cd4119f848f456aae90d2f0c3a595a58aa6ca3348338b5286c38ff1a9263` ／ 8,179 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0208.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0208.json) ／ SHA256: `6648b4104ae4e9db8c2a3153e2980a6cda6f40efa37f3d5cf723ad0e6e635d53` ／ 8,556 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0224.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0224.json) ／ SHA256: `f640bd2cdbc97ad0e6bbeeffaad6e9f59ed6f4e79868a9f45110e938e044306a` ／ 7,131 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0240.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0240.json) ／ SHA256: `42df116f872a5124848409e57ba0e93be68f8d14d4faf02e305604ff8797d582` ／ 8,361 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0256.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0256.json) ／ SHA256: `30b3e254e31c2aabe83810f91c1ee0abedb5cb079c1baad1bc8e9fece3cb8289` ／ 8,275 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0272.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0272.json) ／ SHA256: `bd85c5ecd36095b68c30ff22295c4684a1dbe40a653ace8025818b0f9f94895b` ／ 8,468 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0288.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0288.json) ／ SHA256: `9731a28090cd3ccdbbf2cffb93dbf76475cf48062dcc3228e480af0c054d9ebf` ／ 7,156 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0304.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0304.json) ／ SHA256: `9aab1e0315934769d0e1bb819cec5afc19766c7c3da7dc12148d613f570b84f5` ／ 8,160 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0320.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0320.json) ／ SHA256: `2e8aae239f9d71d665bdc6a58288c3a5435678fe517dde8049a2fbe31a474dfe` ／ 8,639 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0336.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0336.json) ／ SHA256: `c071f348277195539bc4daa29cb455a90dbaf79b8bb4f9baf54ed6b4e552154c` ／ 7,157 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0352.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0352.json) ／ SHA256: `046c4a87aacca3a287c83669a7866588e87e676efa4a5a1e97b52b3577a7bf3a` ／ 8,174 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0368.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0368.json) ／ SHA256: `938d99486432b12f992945754b8eaf5d201e1a57e630acbbb658fb7b55a093bf` ／ 8,210 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0384.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0384.json) ／ SHA256: `300c692ac04173fa4425e521fa2e3a2a73201bb930bf052de75a8167f2233ed1` ／ 7,071 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0400.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0400.json) ／ SHA256: `e74b9cc1cfac913458f3212ee77eadab2017a2ac407050e8fc444d84f658d9c2` ／ 8,179 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0416.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0416.json) ／ SHA256: `1d225c431d0b08d54bd9f4a2f911e60b1ab8efbdc8a2e761876e697b3bf98c58` ／ 8,227 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0432.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0432.json) ／ SHA256: `6d796601425b6506ce5f57f4bc08ac4c2d70a74180d3efc5f53edf388ee0353e` ／ 7,152 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0448.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0448.json) ／ SHA256: `38b7554d218da7544ed5d83cb92536fe76505bffb61858b6077a0cf317efdadf` ／ 8,090 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0464.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0464.json) ／ SHA256: `a6c2a0f9a07eeb5a37729ce187c348c62bfa9a9b0700760bb5dba232589c0771` ／ 8,391 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0480.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0480.json) ／ SHA256: `37033f03ea6d6fa523a0141545b4a2d42dac26ee895a3b12d50bef50bf5cd605` ／ 7,066 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0496.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0496.json) ／ SHA256: `1d96f9d59cb239b41bcce06178bde3de947967c8e335ba813fed6e36656f635d` ／ 8,109 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/result.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/result.json) ／ SHA256: `b23a71522489d7cd78437cedbf0f5c1000a8b6ae8690ac77ea626adf9dd38b0c` ／ 182,759 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 48 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 56 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 65 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 41 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 64 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-probe-launcher-20261006/launcher.json) ／ SHA256: `8a19c7b266cb2f53f20d0631b14feb1bae07dd270054bbe5839fc6a1c9ca94db` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-probe-launcher-20261006/result.json) ／ SHA256: `e4d5167ebfe7dbac0f9d9f7e36162626dfc1d351cd79b7eb643c7e1f5c0439e0` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-train-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-train-launcher-20261006/launcher.json) ／ SHA256: `43dd036c7792074bdb6cbd315495797187bf7a8e690afb8f4157d486095044ac` ／ 96 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/fisher-parameter-anchor-train-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/fisher-parameter-anchor-train-launcher-20261006/result.json) ／ SHA256: `fae0a67cea64fc8983bd1ab4d5677ead590bbc2504f8fd38419f23e085f4ef3d` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>
