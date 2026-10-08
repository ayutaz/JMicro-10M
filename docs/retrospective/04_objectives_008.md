# 学習目的・最適化・正則化 — 8/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/fisher_parameter_anchor_completion.json — Fisher_parameter_anchor_completion</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_completion.json) ／ SHA256: `fb3b01afe428f18d37df70b66d7e834995457ed22cfca2d5299bdc4d024a8480` ／ 684,491 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_anchor_completion" |
| CPU_preparation_seconds | 0.2640336899785325 |
| field_GPU_seconds | 3.6230295989953447 |
| own_job_GPU_seconds | 257.28610576700885 |
| new_source_CE_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 257.28610576700885 |
| actual_job.teachers | 99767422 |
| actual_job.teacher_budget | 100000000 |
| actual_job.loss | 0.27220389246940613 |
| actual_job.source_teachers.web | 75000000 |
| actual_job.source_teachers.story | 5000000 |
| actual_job.source_teachers.ordinary_textbook | 10000000 |
| actual_job.source_teachers.conditional_textbook | 9767422 |
| actual_result.checkpoints.fisher_anchor.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/checkpoint-00326571.pt" |
| actual_result.checkpoints.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| actual_result.checkpoints.fisher_anchor.binding.config_sha256 | "feaf459349182ed9bd60c2840236b8d79a7ac660d3b98c6a086d06dd589c2cfe" |
| actual_result.checkpoints.fisher_anchor.binding.arm | "fisher_anchor" |
| actual_result.checkpoints.fisher_anchor.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| actual_result.checkpoints.fisher_anchor.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| actual_result.checkpoints.fisher_anchor.binding.teacher_goals.web | 75000000 |
| actual_result.checkpoints.fisher_anchor.binding.teacher_goals.story | 5000000 |
| actual_result.checkpoints.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.binding.study_kind | "fixed_context_conditional_MC_Fisher_parameter_anchor_v1" |
| actual_result.checkpoints.fisher_anchor.binding.parameter_coefficient | 0.04161064039180984 |
| actual_result.checkpoints.fisher_anchor.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| actual_result.checkpoints.fisher_anchor.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_result.checkpoints.fisher_anchor.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| actual_result.checkpoints.fisher_anchor.binding.optimizer_policy | "inherit" |
| actual_result.checkpoints.fisher_anchor.binding.peak_lr | 1e-05 |
| actual_result.checkpoints.fisher_anchor.binding.field_binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| actual_result.checkpoints.fisher_anchor.binding.field_binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| actual_result.checkpoints.fisher_anchor.binding.field_binding.field_tensor_digest | "5e3dda1f062597a173882be729b618beaec1d41c99481976e23a3ab8d6c47c40" |
| actual_result.checkpoints.fisher_anchor.binding.field_binding.artifact_sha256 | "16771b045bbdf2031df964a8b5dbf02fbf6c6d444e0c783e39d8a7a05e9192b3" |
| actual_result.checkpoints.fisher_anchor.binding.field_binding.estimator_config_sha256 | "a5ca482667e649d1a3449681636a04c0494409cc5fce150f5d7f6fd746f069d2" |
| actual_result.checkpoints.fisher_anchor.update | 326571 |
| actual_result.checkpoints.fisher_anchor.tokens | 10701078528 |
| actual_result.checkpoints.fisher_anchor.supervised_tokens | 10677786961 |
| actual_result.checkpoints.fisher_anchor.additional_supervised_tokens | 100000000 |
| actual_result.checkpoints.fisher_anchor.additional_input_tokens | 100532224 |
| actual_result.checkpoints.fisher_anchor.source_teachers.web | 75000000 |
| actual_result.checkpoints.fisher_anchor.source_teachers.story | 5000000 |
| actual_result.checkpoints.fisher_anchor.source_teachers.ordinary_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.source_teachers.conditional_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.source_eos.web | 159447 |
| actual_result.checkpoints.fisher_anchor.source_eos.story | 38240 |
| actual_result.checkpoints.fisher_anchor.source_eos.ordinary_textbook | 74183 |
| actual_result.checkpoints.fisher_anchor.source_eos.conditional_textbook | 234328 |
| actual_result.checkpoints.fisher_anchor.source_input_tokens.web | 75183104 |
| actual_result.checkpoints.fisher_anchor.source_input_tokens.story | 5039104 |
| actual_result.checkpoints.fisher_anchor.source_input_tokens.ordinary_textbook | 10075136 |
| actual_result.checkpoints.fisher_anchor.source_input_tokens.conditional_textbook | 10234880 |
| actual_result.checkpoints.fisher_anchor.source_focus_teachers.web | 0 |
| actual_result.checkpoints.fisher_anchor.source_focus_teachers.story | 0 |
| actual_result.checkpoints.fisher_anchor.source_focus_teachers.ordinary_textbook | 0 |
| actual_result.checkpoints.fisher_anchor.source_focus_teachers.conditional_textbook | 1407427 |
| actual_result.checkpoints.fisher_anchor.focus_teacher_tokens | 1407427 |
| actual_result.checkpoints.fisher_anchor.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| actual_result.checkpoints.fisher_anchor.weighted_teacher_mass | 100000000 |
| actual_result.checkpoints.fisher_anchor.outcome_weight | 1 |
| actual_result.checkpoints.fisher_anchor.training_seconds | 191.09000243237824 |
| actual_result.checkpoints.fisher_anchor.completed_at | "2026-10-06T12:59:19.232803Z" |
| actual_result.checkpoints.fisher_anchor.parameter_coefficient | 0.04161064039180984 |
| actual_result.checkpoints.fisher_anchor.parameter_penalty_teacher_tokens | 0 |
| actual_result.checkpoints.fisher_anchor.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| actual_result.checkpoints.fisher_anchor.sampler.kind | "same-streams-staged-source-order-v1" |
| actual_result.checkpoints.fisher_anchor.sampler.goals.web | 75000000 |
| actual_result.checkpoints.fisher_anchor.sampler.goals.story | 5000000 |
| actual_result.checkpoints.fisher_anchor.sampler.goals.ordinary_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.sampler.goals.conditional_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.sampler.context | 1024 |
| actual_result.checkpoints.fisher_anchor.sampler.seed | 42 |
| actual_result.checkpoints.fisher_anchor.sampler.position | 3068 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.sampler.seed | 42 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.sampler.epoch | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.sampler.position | 10400762 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.sampler.context | 1024 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.web.sampler.blocks | 11939276 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.seed | 42 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.genre | "story" |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.documents | 761448 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.epoch | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.document_position | 38243 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.story.token_offset | 87 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.seed | 42 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.genre | "textbook" |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.documents | 2942232 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.epoch | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.document_position | 74189 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.ordinary_textbook.token_offset | 77 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.conditional_textbook.seed | 42 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| actual_result.checkpoints.fisher_anchor.sampler.streams.conditional_textbook.epoch | 114 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.conditional_textbook.document_position | 871 |
| actual_result.checkpoints.fisher_anchor.sampler.streams.conditional_textbook.token_offset | 23 |
| actual_result.checkpoints.fisher_anchor.sampler.source_teachers.web | 75000000 |
| actual_result.checkpoints.fisher_anchor.sampler.source_teachers.story | 5000000 |
| actual_result.checkpoints.fisher_anchor.sampler.source_teachers.ordinary_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.sampler.source_teachers.conditional_textbook | 10000000 |
| actual_result.checkpoints.fisher_anchor.sampler.source_eos.web | 159447 |
| actual_result.checkpoints.fisher_anchor.sampler.source_eos.story | 38240 |
| actual_result.checkpoints.fisher_anchor.sampler.source_eos.ordinary_textbook | 74183 |
| actual_result.checkpoints.fisher_anchor.sampler.source_eos.conditional_textbook | 234328 |
| actual_result.checkpoints.fisher_anchor.sampler.source_tokens.web | 75183104 |
| actual_result.checkpoints.fisher_anchor.sampler.source_tokens.story | 5039104 |
| actual_result.checkpoints.fisher_anchor.sampler.source_tokens.ordinary_textbook | 10075136 |
| actual_result.checkpoints.fisher_anchor.sampler.source_tokens.conditional_textbook | 10234880 |
| actual_result.checkpoints.fisher_anchor.sampler.source_body_bytes.web | 292167653 |
| actual_result.checkpoints.fisher_anchor.sampler.source_body_bytes.story | 20452979 |
| actual_result.checkpoints.fisher_anchor.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| actual_result.checkpoints.fisher_anchor.sampler.source_body_bytes.conditional_textbook | 37865985 |
| actual_result.checkpoints.fisher_anchor.sampler.source_focus_teachers.web | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.source_focus_teachers.story | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.source_focus_teachers.ordinary_textbook | 0 |
| actual_result.checkpoints.fisher_anchor.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| actual_result.checkpoints.fisher_anchor.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| actual_result.checkpoints.fisher_anchor.source_body_bytes.web | 292167653 |
| actual_result.checkpoints.fisher_anchor.source_body_bytes.story | 20452979 |
| actual_result.checkpoints.fisher_anchor.source_body_bytes.ordinary_textbook | 42739471 |
| actual_result.checkpoints.fisher_anchor.source_body_bytes.conditional_textbook | 37865985 |
| actual_result.checkpoints.fisher_anchor.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| actual_result.evaluations.fisher_anchor.binding.teacher_goals.web | 75000000 |
| actual_result.evaluations.fisher_anchor.binding.teacher_goals.story | 5000000 |
| actual_result.evaluations.fisher_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| actual_result.evaluations.fisher_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| actual_result.evaluations.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| actual_result.evaluations.fisher_anchor.body.documents | 256 |
| actual_result.evaluations.fisher_anchor.body.limit_documents | 256 |
| actual_result.evaluations.fisher_anchor.body.body_nll | 322293.0505590439 |
| actual_result.evaluations.fisher_anchor.body.eos_nll | 579.8090896382928 |
| actual_result.evaluations.fisher_anchor.body.body_bytes | 472055 |
| actual_result.evaluations.fisher_anchor.body.body_tokens | 122343 |
| actual_result.evaluations.fisher_anchor.body.bpb | 0.9849923965523267 |
| actual_result.evaluations.fisher_anchor.body.seconds | 1.5506487939856015 |
| actual_result.evaluations.fisher_anchor.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| actual_result.evaluations.fisher_anchor.generation.max_new_tokens | 64 |
| actual_result.evaluations.fisher_anchor.greedy_rates.eos | 65 |
| actual_result.evaluations.fisher_anchor.greedy_rates.repetition | 7 |
| actual_result.evaluations.fisher_anchor.greedy_rates.unicode_failure | 0 |
| actual_result.evaluations.fisher_anchor.greedy_rates.role_leak | 0 |
| actual_result.evaluations.fisher_anchor.greedy_rates.empty | 0 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.5729166666666666] |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.units | 96 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.examples | 192 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.46875, 0.53125] |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.count | 192 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.macro_f1 | 0.4995112414467253 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.train_majority_accuracy | 0.5 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.negation.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.negation.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.time.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.time.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.causality.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.causality.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.units | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.examples | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7341389728096677 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7824773413897281] |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.count | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7341389728096677 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42334494773519166 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.train_majority_accuracy | null |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.fisher_anchor.diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.point | 0.3221626452189455 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.ci95 | [0.29535299374441465, 0.3489722966934763] |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.units | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2957998212689902 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26899016979445933, 0.32350312779267204] |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.count | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2957998212689902 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29495447835836136 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.mcc | 0.1201864675199048 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.seed | 42 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.fisher_anchor.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.fisher_anchor.diagnostics.semantic_both_contexts.correct | 12 |
| actual_result.evaluations.fisher_anchor.memory.maximum_observed_allocated_bytes | 315223040 |
| actual_result.evaluations.fisher_anchor.memory.maximum_observed_reserved_bytes | 13325303808 |
| actual_result.evaluations.fisher_anchor.protected_test_used | false |
| actual_result.transfer.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| actual_result.transfer.fisher_anchor.checks.weights_unchanged | true |
| actual_result.transfer.fisher_anchor.checks.no_gradients | true |
| actual_result.transfer.fisher_anchor.checks.eval_mode | true |
| actual_result.transfer.fisher_anchor.checks.RNG_restored | true |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 68 |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| actual_result.transfer.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 53 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 73 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 48 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| actual_result.transfer.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| actual_result.transfer.fisher_anchor.optimizer_updates | 0 |
| actual_result.transfer.fisher_anchor.scientific_teacher_tokens | 0 |
| actual_result.transfer.fisher_anchor.protected_test_used | false |
| actual_result.transfer.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.retention.fisher_anchor.checkpoint_sha256 | "233cd0a5782b7c1c1af39a7d1255979c2d1d2497aaa33c8634f4a7c0d9e2ebd7" |
| actual_result.retention.fisher_anchor.checks.weights_unchanged | true |
| actual_result.retention.fisher_anchor.checks.no_gradients | true |
| actual_result.retention.fisher_anchor.checks.eval_mode | true |
| actual_result.retention.fisher_anchor.checks.RNG_restored | true |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 48 |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| actual_result.retention.fisher_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 56 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 65 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 41 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 64 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| actual_result.retention.fisher_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| actual_result.retention.fisher_anchor.optimizer_updates | 0 |
| actual_result.retention.fisher_anchor.scientific_teacher_tokens | 0 |
| actual_result.retention.fisher_anchor.protected_test_used | false |
| actual_result.retention.fisher_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.scientific_teacher_tokens | 100000000 |
| actual_result.reused_control_teacher_tokens | 100000000 |
| actual_result.all_scientific_input_streams_match | true |
| actual_result.status | "Fisher100M_GPU_complete_pending_all80_content_review" |
| actual_result.GPU_seconds | 257.28610576700885 |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| total_new_GPU_seconds | 280.0701394250209 |
| actual_review.status | "Fisher100M_all80_content_matched_control_reviewed" |
| actual_review.summaries.fisher_anchor.BPB | 0.9849923965523267 |
| actual_review.summaries.fisher_anchor.rates.eos | 65 |
| actual_review.summaries.fisher_anchor.rates.repetition | 7 |
| actual_review.summaries.fisher_anchor.rates.unicode_failure | 0 |
| actual_review.summaries.fisher_anchor.rates.role_leak | 0 |
| actual_review.summaries.fisher_anchor.rates.empty | 0 |
| actual_review.summaries.fisher_anchor.grammar2 | 63 |
| actual_review.summaries.fisher_anchor.relevance2 | 66 |
| actual_review.summaries.fisher_anchor.coherent | 28 |
| actual_review.summaries.fisher_anchor.appropriate | 30 |
| actual_review.summaries.fisher_anchor.notes_sha256 | "99ff97f68c8dc524ba2cf62a0bb9f29bf5f73ff24e652ba964af7d1e5ab4549f" |
| actual_review.summaries.uniform_anchor.BPB | 0.9906670746607233 |
| actual_review.summaries.uniform_anchor.rates.eos | 67 |
| actual_review.summaries.uniform_anchor.rates.repetition | 6 |
| actual_review.summaries.uniform_anchor.rates.unicode_failure | 0 |
| actual_review.summaries.uniform_anchor.rates.role_leak | 0 |
| actual_review.summaries.uniform_anchor.rates.empty | 0 |
| actual_review.summaries.uniform_anchor.grammar2 | 59 |
| actual_review.summaries.uniform_anchor.relevance2 | 60 |
| actual_review.summaries.uniform_anchor.coherent | 25 |
| actual_review.summaries.uniform_anchor.appropriate | 29 |
| actual_review.summaries.uniform_anchor.notes_sha256 | "83e3ff51c39594a47db2165e4a79a490d66fed6bddd49e4a6e82c8ae3c83ef34" |
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
| actual_review.accounting.completed_updates | 3068 |
| actual_review.accounting.teachers | 100000000 |
| actual_review.accounting.physical_input_positions | 100532224 |
| actual_review.accounting.parameter_penalty_teacher_tokens | 0 |
| actual_review.accounting.source_teachers.web | 75000000 |
| actual_review.accounting.source_teachers.story | 5000000 |
| actual_review.accounting.source_teachers.ordinary_textbook | 10000000 |
| actual_review.accounting.source_teachers.conditional_textbook | 10000000 |
| actual_review.accounting.source_EOS.web | 159447 |
| actual_review.accounting.source_EOS.story | 38240 |
| actual_review.accounting.source_EOS.ordinary_textbook | 74183 |
| actual_review.accounting.source_EOS.conditional_textbook | 234328 |
| actual_review.quality_comparisons.uniform_anchor.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparisons.uniform_anchor.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparisons.uniform_anchor.checks.EOS_nonworsening | false |
| actual_review.quality_comparisons.uniform_anchor.checks.repetition_nonworsening | false |
| actual_review.quality_comparisons.uniform_anchor.checks.no_empty_role_unicode | true |
| actual_review.quality_comparisons.uniform_anchor.checks.BPB_gate | true |
| actual_review.quality_comparisons.uniform_anchor.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparisons.uniform_anchor.passed | false |
| actual_review.quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| actual_review.quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| actual_review.quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| actual_review.quality_comparisons.strong_staged.checks.BPB_gate | true |
| actual_review.quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparisons.strong_staged.passed | false |
| actual_review.original_Web.EOS_at_least8_more | true |
| actual_review.original_Web.repetition_no_worse | true |
| actual_review.original_Web.no_empty_role_unicode | true |
| actual_review.original_Web.BPB_degradation_at_most1percent | false |
| actual_review.absolute_dev_screen.grammar_at_least56 | true |
| actual_review.absolute_dev_screen.coherence_at_least27 | true |
| actual_review.absolute_dev_screen.appropriate_at_least27 | true |
| actual_review.absolute_dev_screen.EOS_at_least37 | true |
| actual_review.absolute_dev_screen.repetition_at_most18 | true |
| actual_review.absolute_dev_screen.no_empty_role_unicode | true |
| actual_review.eligible_for_final_Base_validation | false |
| actual_review.scientific_teacher_tokens | 100000000 |
| actual_review.reused_control_teacher_tokens | 100000000 |
| actual_review.field_model_sampled_labels | 65276 |
| actual_review.verification_teacher_tokens | 1307952 |
| actual_review.new_total_GPU_seconds | 280.0701394250209 |
| actual_review.Base_complete | false |
| actual_review.Base_adopted | false |
| actual_review.protected_test_used | false |
| eligible_for_final_Base_validation | false |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/content-notes.json" |
| notes.sha256 | "99ff97f68c8dc524ba2cf62a0bb9f29bf5f73ff24e652ba964af7d1e5ab4549f" |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_completion_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_completion_portable.json) ／ SHA256: `1279605712ec5f3e841e181e5552d4011febc23156d512aeb0c1ac06ce72d5e6` ／ 38,455 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_anchor_completion.json.bytes | 684491 |
| files.reports/phase6/fisher_parameter_anchor_completion.json.sha256 | "fb3b01afe428f18d37df70b66d7e834995457ed22cfca2d5299bdc4d024a8480" |
| files.configs/phase6/fisher_parameter_anchor.json.bytes | 22478 |
| files.reports/phase6/fisher_parameter_anchor_proposal.json.bytes | 5455 |
| files.reports/phase6/fisher_parameter_budget_tests.xml.bytes | 388 |
| files.reports/phase6/fisher_parameter_budget_tests.xml.sha256 | "7065564f37f1e48b2f922271c1d7086d59d0e8a2335ed9ecb26c6287d5033f9f" |
| files.scripts/record_fisher_parameter_anchor.py.bytes | 10785 |
| files.scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.scripts/run_fisher_parameter_anchor.py.bytes | 22806 |
| files.scripts/run_fisher_parameter_anchor.ps1.bytes | 3089 |
| files.tests/test_fisher_parameter_budget.py.bytes | 1011 |
| files.tests/test_fisher_parameter_budget.py.sha256 | "4bfaaf96a5f62f8225724e040238736e9cd3bbf1d908c65eb0f639c358d83087" |
| files.scripts/review_fisher_parameter_anchor.py.bytes | 8334 |
| files.scripts/record_fisher_parameter_content.py.bytes | 3341 |
| files.reports/phase6/fisher_parameter_anchor_observations.tsv.bytes | 10965 |
| files.reports/phase6/fisher_parameter_anchor_review.json.bytes | 5149 |
| files.reports/phase6/fisher-parameter-anchor-20261006/compare-result.json.bytes | 633561 |
| files.reports/phase6/fisher-parameter-anchor-20261006/content-notes.json.bytes | 46996 |
| files.reports/phase6/fisher-parameter-anchor-20261006/content-notes.json.sha256 | "99ff97f68c8dc524ba2cf62a0bb9f29bf5f73ff24e652ba964af7d1e5ab4549f" |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/body.json.bytes | 67842 |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/generation.json.bytes | 80761 |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jblimp.json.bytes | 339058 |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/jcqa.json.bytes | 1641670 |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/result.json.bytes | 174630 |
| files.reports/phase6/fisher-parameter-anchor-20261006/evaluation/fisher_anchor/evaluation/semantics.json.bytes | 203816 |
| files.reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/latest.json.bytes | 285 |
| files.reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/latest.json.sha256 | "4e731def2b392a39b1368b55b7cfcef9475e02dbb819035720e55f8d35e37da5" |
| files.reports/phase6/fisher-parameter-anchor-20261006/fisher_anchor/training/metrics.jsonl.bytes | 4125607 |
| files.reports/phase6/fisher-parameter-anchor-20261006/job.json.bytes | 927 |
| files.reports/phase6/fisher-parameter-anchor-20261006/progress-result.json.bytes | 632811 |
| files.reports/phase6/fisher-parameter-anchor-20261006/review.json.bytes | 5149 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/configs/phase6/fisher_parameter_anchor.json.bytes | 22478 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/build_fisher_parameter_field.ps1.bytes | 2617 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/build_fisher_parameter_field.py.bytes | 14359 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/parameter_displacement_anchor_trainer.py.bytes | 8735 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_fisher_parameter_anchor.ps1.bytes | 3089 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_fisher_parameter_anchor.py.bytes | 22806 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_parameter_displacement_anchor_v3.ps1.bytes | 3140 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_parameter_displacement_anchor_v3.py.bytes | 22073 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_fisher_parameter_anchor.py.bytes | 7440 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_fisher_parameter_anchor.py.sha256 | "1f5ab2f00af0ec8fa268ec5f49635ea0eefb65b7b6df84eec2383ede3ec74784" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_fisher_parameter_budget.py.bytes | 1011 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_fisher_parameter_budget.py.sha256 | "4bfaaf96a5f62f8225724e040238736e9cd3bbf1d908c65eb0f639c358d83087" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_parameter_displacement_anchor.py.bytes | 4477 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_parameter_displacement_anchor.py.sha256 | "2ee96ca6b0f2e12a6f9e3c9bd0c40e3cd21de3910545dbe67df357d5b2e7c38e" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/fisher-parameter-anchor-20261006/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0000.json.bytes | 9972 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0016.json.bytes | 9618 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0032.json.bytes | 10257 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0048.json.bytes | 9569 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0064.json.bytes | 10350 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0080.json.bytes | 9760 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0096.json.bytes | 9838 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0112.json.bytes | 10186 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0128.json.bytes | 9860 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0144.json.bytes | 9921 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0160.json.bytes | 10184 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0176.json.bytes | 10029 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0192.json.bytes | 9939 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0208.json.bytes | 9670 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0224.json.bytes | 9836 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0240.json.bytes | 9647 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0256.json.bytes | 9681 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0272.json.bytes | 9655 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0288.json.bytes | 9650 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0304.json.bytes | 9850 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0320.json.bytes | 9372 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0336.json.bytes | 9449 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0352.json.bytes | 9851 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0368.json.bytes | 9596 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0384.json.bytes | 9889 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0400.json.bytes | 9559 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0416.json.bytes | 9923 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0432.json.bytes | 9394 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0448.json.bytes | 9625 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0464.json.bytes | 9469 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0480.json.bytes | 9485 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/0496.json.bytes | 9559 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/bridge/fisher_anchor/result.json.bytes | 186160 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0000.json.bytes | 7985 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0016.json.bytes | 8351 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0032.json.bytes | 7032 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0048.json.bytes | 8178 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0064.json.bytes | 8520 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0080.json.bytes | 7117 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0096.json.bytes | 8097 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0112.json.bytes | 8292 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0128.json.bytes | 7117 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0144.json.bytes | 8202 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0160.json.bytes | 8627 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0176.json.bytes | 6970 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0192.json.bytes | 8179 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0208.json.bytes | 8556 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0224.json.bytes | 7131 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0240.json.bytes | 8361 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0256.json.bytes | 8275 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0272.json.bytes | 8468 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0288.json.bytes | 7156 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0304.json.bytes | 8160 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0320.json.bytes | 8639 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0336.json.bytes | 7157 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0352.json.bytes | 8174 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0368.json.bytes | 8210 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0384.json.bytes | 7071 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0400.json.bytes | 8179 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0416.json.bytes | 8227 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0432.json.bytes | 7152 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0448.json.bytes | 8090 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0464.json.bytes | 8391 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0480.json.bytes | 7066 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/0496.json.bytes | 8109 |
| files.reports/phase6/fisher-parameter-anchor-20261006/transfer/retention/fisher_anchor/result.json.bytes | 182759 |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_launch.json — Fisher_parameter_anchor_launch</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_launch.json) ／ SHA256: `a5911424c85695a9d2961e5c7b0f545f026a366a06ec152e82d6ef6f98de5388` ／ 1,521 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_anchor_launch" |
| CPU_preparation_seconds | 0.2640336899785325 |
| field_GPU_seconds | 3.6230295989953447 |
| own_job_GPU_seconds | 60.503918152011465 |
| new_source_CE_teacher_tokens | 26812706 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "setup" |
| actual_job.GPU_elapsed_seconds | 60.503918152011465 |
| actual_job.teachers | 26812706 |
| actual_job.teacher_budget | 100000000 |
| actual_job.loss | 2.421725273132324 |
| actual_job.source_teachers.web | 26812706 |
| actual_job.source_teachers.story | 0 |
| actual_job.source_teachers.ordinary_textbook | 0 |
| actual_job.source_teachers.conditional_textbook | 0 |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_launch_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_launch_portable.json) ／ SHA256: `0b65af41b188396892cddde399c652860bf048136236627ecf6273cac6f187d4` ／ 1,766 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_anchor_launch.json.bytes | 1521 |
| files.configs/phase6/fisher_parameter_anchor.json.bytes | 22478 |
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
<summary>reports/phase6/fisher_parameter_anchor_probe.json — Fisher_parameter_anchor_probe</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_probe.json) ／ SHA256: `57be0d69cedbe0b28f0ed67f276afd531dfb0ef3fa78d60b5476d56f2c217d95` ／ 86,862 bytes

| 原キー | 保存値 |
|---|---|
| status | "Fisher_parameter_anchor_probe" |
| CPU_preparation_seconds | 0.2640336899785325 |
| field_GPU_seconds | 3.6230295989953447 |
| own_job_GPU_seconds | 19.161004059016705 |
| new_source_CE_teacher_tokens | 0 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 19.161004059016705 |
| actual_job.completed_updates | 32 |
| actual_probe.gates.fisher_anchor.passed | true |
| actual_probe.gates.fisher_anchor.checks.model | true |
| actual_probe.gates.fisher_anchor.checks.optimizer | true |
| actual_probe.gates.fisher_anchor.checks.scheduler | true |
| actual_probe.gates.fisher_anchor.checks.rng | true |
| actual_probe.gates.fisher_anchor.checks.sampler | true |
| actual_probe.gates.fisher_anchor.checks.lineage | true |
| actual_probe.gates.fisher_anchor.checks.tokens | true |
| actual_probe.gates.fisher_anchor.checks.supervised_tokens | true |
| actual_probe.gates.fisher_anchor.checks.body_bytes | true |
| actual_probe.gates.fisher_anchor.checks.token_digest | true |
| actual_probe.gates.fisher_anchor.checks.focus_token_digest | true |
| actual_probe.gates.fisher_anchor.checks.focus_teacher_tokens | true |
| actual_probe.gates.fisher_anchor.checks.weighted_teacher_mass | true |
| actual_probe.gates.fisher_anchor.checks.update | true |
| actual_probe.gates.fisher_anchor.checks.spec | true |
| actual_probe.gates.fisher_anchor.checks.model_config | true |
| actual_probe.gates.fisher_anchor.checks.pilot_binding | true |
| actual_probe.gates.fisher_anchor.checks.study_binding | true |
| actual_probe.gates.fisher_anchor.checks.history_loss | true |
| actual_probe.gates.fisher_anchor.checks.history_gradient_norm | true |
| actual_probe.gates.fisher_anchor.checks.history_lr | true |
| actual_probe.gates.fisher_anchor.checks.history_token_digest | true |
| actual_probe.gates.fisher_anchor.checks.history_source_teachers | true |
| actual_probe.gates.fisher_anchor.checks.history_source_eos | true |
| actual_probe.gates.fisher_anchor.checks.history_source_input_tokens | true |
| actual_probe.gates.fisher_anchor.checks.history_source_body_bytes | true |
| actual_probe.gates.fisher_anchor.checks.history_source_focus_teachers | true |
| actual_probe.gates.fisher_anchor.checks.history_focus_token_digest | true |
| actual_probe.gates.fisher_anchor.checks.history_focus_teacher_tokens | true |
| actual_probe.gates.fisher_anchor.checks.history_weighted_teacher_mass | true |
| actual_probe.gates.fisher_anchor.checks.finite | true |
| actual_probe.gates.fisher_anchor.checks.no_reheat | true |
| actual_probe.gates.fisher_anchor.checks.history_CE_loss | true |
| actual_probe.gates.fisher_anchor.checks.history_parameter_penalty | true |
| actual_probe.gates.fisher_anchor.checks.history_parameter_coefficient | true |
| actual_probe.gates.fisher_anchor.checks.history_parameter_penalty_teacher_tokens | true |
| actual_probe.gates.fisher_anchor.GPU_optimizer_updates | 8 |
| actual_probe.gates.fisher_anchor.verification_teacher_tokens | 261616 |
| actual_probe.timings.fisher_anchor.verification_teacher_tokens | 1046336 |
| actual_probe.timings.fisher_anchor.terminal_save_seconds | 0.17179205399588682 |
| actual_probe.timings.fisher_anchor.peak_VRAM_bytes | 6269121024 |
| actual_probe.timings.fisher_anchor.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/checkpoint.pt" |
| actual_probe.timings.fisher_anchor.checkpoint.sha256 | "55de749961795456c056665538a61876034ccced3deb606ac2dd031785db5e1a" |
| actual_probe.initial_fullstate_preservation.fisher_anchor.parent_sampler_lineage | true |
| actual_probe.initial_fullstate_preservation.fisher_anchor.all_checks | true |
| actual_probe.passed | true |
| actual_probe.scientific_teacher_tokens | 0 |
| actual_probe.GPU_optimizer_updates | 40 |
| actual_probe.verification_teacher_tokens | 1307952 |
| actual_probe.status | "own_Fisher_probe_complete" |
| actual_probe.GPU_seconds | 19.161004059016705 |
| actual_probe.Base_complete | false |
| actual_probe.Base_adopted | false |
| actual_probe.protected_test_used | false |
| estimated_science_GPU_seconds | 805.3906611135419 |
| estimated_total_GPU_seconds | 828.174694771554 |
| planning_within_budget | true |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_probe_portable.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_probe_portable.json) ／ SHA256: `9017fb9443398618f4de38b4d83e93c8ff68554ffcb272611cdb924c63ed45fd` ／ 23,242 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/fisher_parameter_anchor_probe.json.bytes | 86862 |
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
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/latest.json.bytes | 282 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/latest.json.sha256 | "d365dafb0a2bac30f107b2febd0bbfa61322f8c7bf4be5053116a54c3d74e8f4" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/resume-gate/result.json.bytes | 15618 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/latest.json.bytes | 280 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/latest.json.sha256 | "8fb5b222c79688389e0c1fa971a59ddfc889f0a58ed3f023e50ab474a5292f47" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/fisher_anchor/timing/metrics.jsonl.bytes | 42052 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/job.json.bytes | 549 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/progress-result.json.bytes | 79309 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/result.json.bytes | 79819 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/configs/phase6/fisher_parameter_anchor_probe.json.bytes | 21775 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/build_fisher_parameter_field.ps1.bytes | 2617 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/build_fisher_parameter_field.py.bytes | 14359 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/fisher_parameter_anchor.py.bytes | 13446 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/parameter_displacement_anchor_trainer.py.bytes | 8735 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_fisher_parameter_anchor.ps1.bytes | 3089 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_fisher_parameter_anchor.py.bytes | 22806 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_parameter_displacement_anchor_v3.ps1.bytes | 3140 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_parameter_displacement_anchor_v3.py.bytes | 22073 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_fisher_parameter_anchor.py.bytes | 7440 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_fisher_parameter_anchor.py.sha256 | "1f5ab2f00af0ec8fa268ec5f49635ea0eefb65b7b6df84eec2383ede3ec74784" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_fisher_parameter_budget.py.bytes | 1011 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_fisher_parameter_budget.py.sha256 | "4bfaaf96a5f62f8225724e040238736e9cd3bbf1d908c65eb0f639c358d83087" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_parameter_displacement_anchor.py.bytes | 4477 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_parameter_displacement_anchor.py.sha256 | "2ee96ca6b0f2e12a6f9e3c9bd0c40e3cd21de3910545dbe67df357d5b2e7c38e" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/fisher-parameter-anchor-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_proposal.json — None</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_proposal.json) ／ SHA256: `37636c73e597ae80216f28e6233adcdca61ad79cdf147e47dc3ad32090416860` ／ 5,455 bytes

| 原キー | 保存値 |
|---|---|
| hypothesis | "Replace the completed uniform L2 field by TRAIN conditional model-sampled diagonal Fisher importance; protect sensitive coordinates and allow less sensitive coordinates to adapt." |
| source_teacher_goals.web | 75000000 |
| source_teacher_goals.story | 5000000 |
| source_teacher_goals.ordinary_textbook | 10000000 |
| source_teacher_goals.conditional_textbook | 10000000 |
| source_CE_teacher_tokens | 100000000 |
| full_conditional_setup_and_body_and_EOS | true |
| field_settings.seed | 2026100647 |
| field_settings.sampled_vocabulary | "full_native_4096" |
| field_GPU_ceiling_seconds | 120 |
| own_CUDA_trainer_probe_ceiling_seconds | 120 |
| total_new_GPU_ceiling_seconds | 1800 |
| completion | "One full100M candidate, same dev256/Japanese192-331-1119/native greedy80/all80 raw-bound content; unchanged relative, absolute and historical Web1% gates. Qualified recipe only proceeds to independent learning seed/full dev/protected test/adoption." |
| references.uniform_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter_displacement_anchor_completion.json" |
| references.uniform_completion.sha256 | "cde3ccf0c0cf75db7a7854a8f66f102fb0dffe9c055fc73eb6af3a0b4fbb9002" |
| references.block_failure.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/block_Web_constraint_failure_analysis.json" |
| references.block_failure.sha256 | "d540682d8e1a8d826e9550c536884abdd3c0c6e93654289d0819206b7ec476c3" |
| references.CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/fisher_parameter_anchor_tests.xml" |
| references.CPU_tests.sha256 | "c06c70206f682dd7f32df0254cf35949831afb6cd75876cfff97061bf3f7aad8" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| field_GPU_seconds_so_far | 0 |
| source_CE_teacher_tokens_so_far | 0 |
| scientific_launched | false |

</details>

<details>
<summary>reports/phase6/fisher_parameter_anchor_review.json — Fisher100M_all80_content_matched_control_reviewed</summary>

[原記録](../../reports/phase6/fisher_parameter_anchor_review.json) ／ SHA256: `df7cd9bbd111c24a1c01f3a7c2f8d12962c72d1bf983977e5876f986809466e7` ／ 5,149 bytes

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
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/body.json) ／ SHA256: `5d0892ca43dfd06cfecc8ad7122ac5b5c43a54521a6127320a33b7671bb2ae10` ／ 68,996 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 326708.58645915985 |
| body.eos_nll | 507.838469048962 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.998487162513845 |
| body.seconds | 1.3521321459847968 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/generation.json) ／ SHA256: `73a952a4e08ca8cfffa229fdb8c8f497d0373ff0646ca4b4f5cecd90a27e644b` ／ 121,142 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/jblimp.json) ／ SHA256: `3c74ab05e770b8d30b99a577b2e8ee5128cd5d04f9667ff5ce0ba8b0ac435698` ／ 340,175 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7734138972809668 |
| summary.primary.accuracy.ci95 | [0.7280966767371602, 0.8187311178247734] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7734138972809668 |
| summary.per_token_secondary.accuracy.point | 0.7220543806646526 |
| summary.per_token_secondary.accuracy.ci95 | [0.6706948640483383, 0.770392749244713] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| summary.per_token_secondary.macro_f1 | 0.4192982456140351 |
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
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/jcqa.json) ／ SHA256: `1439491708ba20b1ff149503119e1a22838f55bbea74b5cf55999f3fd3d7ab0d` ／ 1,641,828 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.35031277926720283 |
| summary.primary.accuracy.ci95 | [0.322609472743521, 0.3771224307417337] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.35031277926720283 |
| summary.per_token_secondary.accuracy.point | 0.3136729222520107 |
| summary.per_token_secondary.accuracy.ci95 | [0.2868632707774799, 0.34048257372654156] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.3136729222520107 |
| summary.per_token_secondary.macro_f1 | 0.31250231880924895 |
| summary.per_token_secondary.mcc | 0.14198756684666586 |
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
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/result.json) ／ SHA256: `252dc5201d586694ee83b788c5f954f025e4ccfe14d5ee14e1b630d153cc8435` ／ 220,898 bytes

| 原キー | 保存値 |
|---|---|
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoint_sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 326708.58645915985 |
| body.eos_nll | 507.838469048962 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.998487162513845 |
| body.seconds | 1.3521321459847968 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 19 |
| greedy_rates.repetition | 45 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.625 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.578125, 0.6770833333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.625 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.6302083333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5871866750129277 |
| diagnostics.semantics.per_token_secondary.mcc | 0.17825740078487468 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7734138972809668 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8187311178247734] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7734138972809668 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6706948640483383, 0.770392749244713] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7764350453172205 |
| diagnostics.jcqa.primary.accuracy.point | 0.35031277926720283 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.322609472743521, 0.3771224307417337] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.35031277926720283 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3136729222520107 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2868632707774799, 0.34048257372654156] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3136729222520107 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.31250231880924895 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.14198756684666586 |
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
| diagnostics.semantic_both_contexts.correct | 26 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 11957960704 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/evaluation/semantics.json) ／ SHA256: `8aad81baed129c979ea6d50bbdefac0aa8908c69d15f24092b04173e5018ebc9` ／ 205,058 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.625 |
| summary.primary.accuracy.ci95 | [0.578125, 0.6770833333333334] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.625 |
| summary.per_token_secondary.accuracy.point | 0.5885416666666666 |
| summary.per_token_secondary.accuracy.ci95 | [0.546875, 0.6302083333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| summary.per_token_secondary.macro_f1 | 0.5871866750129277 |
| summary.per_token_secondary.mcc | 0.17825740078487468 |
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
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/manifest.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/manifest.json) ／ SHA256: `d998f56b0ce5f29c95b8dbe2f2bbcbddc913118a77e0eeaeee47a16107157616` ／ 2,668 bytes

| 原キー | 保存値 |
|---|---|
| total_bytes | 2664967.0 |
| scope | "Completed CE arm only; overall scientific contrast training remains live" |
| Base_complete | false |
| native_checkpoint_tensors_retained | true |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-CE-evidence-20261007/train-result.json — complete</summary>

[原記録](../../reports/phase6/natural-context-contrast-CE-evidence-20261007/train-result.json) ／ SHA256: `dc3eae3f5b34bc7c09165ad34cb0f3dac1da9c6ff88c451fc2f9590980383ae2` ／ 17,394 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| checkpoint_sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| scientific_CE_teacher_tokens | 100000000 |
| counters.update | 17698 |
| counters.supervised_tokens | 100000000 |
| counters.CE_input_tokens | 102655467 |
| counters.auxiliary_input_tokens | 0 |
| counters.auxiliary_pairs | 0 |
| counters.physical_input_tokens | 370838917 |
| counters.original_body_bytes | 405882136 |
| counters.token_digest | "a1ab017092f823d69e033d96868136ebeb0a55f13e2cb1cfd039e3c7d920a1c9" |
| counters.source_teachers.web | 75000000 |
| counters.source_teachers.textbook | 20000000 |
| counters.source_teachers.story | 5000000 |
| counters.source_EOS.web | 657450 |
| counters.source_EOS.textbook | 148625 |
| counters.source_EOS.story | 38222 |
| sampler.kind | "bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1" |
| sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| sampler.binding.index_size | 12861257655 |
| sampler.binding.index_mtime_ns | 1791234945567297288 |
| sampler.binding.stream_size | 4000002624 |
| sampler.binding.stream_mtime_ns | 1791234945514053852 |
| sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| sampler.seed | 42 |
| sampler.goals.web | 75000000 |
| sampler.goals.textbook | 20000000 |
| sampler.goals.story | 5000000 |
| sampler.consumed.web | 75000000 |
| sampler.consumed.textbook | 20000000 |
| sampler.consumed.story | 5000000 |
| sampler.pending.web | [] |
| sampler.pending.textbook | [] |
| sampler.pending.story | [] |
| sampler.draws | 2656558 |
| sampler.documents_drawn | 844300 |
| sampler.windows_emitted | 849479 |
| sampler.auxiliary_reasons.original_sentence_or_LF_boundary | 676390 |
| sampler.auxiliary_reasons.no_original_codec_stable_sentence_pair | 167910 |
| parent_CE_teacher_tokens | 9978838479 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/manifest.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/manifest.json) ／ SHA256: `25c9cee9533db218f1f72b3c1dfe793542f26ade995aaacf1b5981d87decf837` ／ 2,795 bytes

| 原キー | 保存値 |
|---|---|
| limitations | "Actual checkpoint tensors and complete corpus remain at bound WSL paths; this archive retains all64 original token pairs, raw3-model matrices, terminal identity and comparison source." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/CE.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/CE.json) ／ SHA256: `c02f7ddd4756d8abc8326b8d25aa8c1137b197fa43b16017dd766ecaf546d475` ／ 135,661 bytes

| 原キー | 保存値 |
|---|---|
| pairs | 64 |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| checkpoint.size | 124373565 |
| checkpoint.mtime_ns | 1791307063680713152 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/cases.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/cases.json) ／ SHA256: `1d34e15bce7e5105b10d26dfacc11e856e3fd63943de006c24e136c1b112b3a9` ／ 482,408 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/contrast.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/contrast.json) ／ SHA256: `5b96f79bbcea59145dc48d9ec6c8bde68bc0d2c894cc2e13a8a4ea0128ec2446` ／ 135,964 bytes

| 原キー | 保存値 |
|---|---|
| pairs | 64 |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/contrast/checkpoint-00017698.pt" |
| checkpoint.sha256 | "b3c88153624b9d9c1e9114314c7c19f7feeaf5e4c51650b3e78f0dd40c407707" |
| checkpoint.size | 124373565 |
| checkpoint.mtime_ns | 1791309374331361221 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/job.json — complete</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/job.json) ／ SHA256: `a02868c0d5428e46ce95f265a0e80099fe0f693961decbf1c1734cca96fb798e` ／ 563 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_limit_seconds | 60 |
| GPU_occupancy_seconds | 1.501790620997781 |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/original.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/original.json) ／ SHA256: `9000f05e61c1c6cacc2571856abae14b2e84ddccbab2be0b835ec23f7aaa8d3e` ／ 135,608 bytes

| 原キー | 保存値 |
|---|---|
| pairs | 64 |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| checkpoint.size | 120181763 |
| checkpoint.mtime_ns | 1791114231712428007 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/result.json — complete</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/result.json) ／ SHA256: `2bd3ac5eeeae4ab2a31c1782674cb6fe8f5546375e3e234f5ee61182888836b9` ／ 467,038 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| results.original.pairs | 64 |
| results.original.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| results.original.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| results.original.checkpoint.size | 120181763 |
| results.original.checkpoint.mtime_ns | 1791114231712428007 |
| results.CE.pairs | 64 |
| results.CE.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| results.CE.checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| results.CE.checkpoint.size | 124373565 |
| results.CE.checkpoint.mtime_ns | 1791307063680713152 |
| results.contrast.pairs | 64 |
| results.contrast.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/contrast/checkpoint-00017698.pt" |
| results.contrast.checkpoint.sha256 | "b3c88153624b9d9c1e9114314c7c19f7feeaf5e4c51650b3e78f0dd40c407707" |
| results.contrast.checkpoint.size | 124373565 |
| results.contrast.checkpoint.mtime_ns | 1791309374331361221 |
| GPU_occupancy_seconds | 1.501790620997781 |
| GPU_limit_seconds | 60 |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "One retrospective constructed64 DEV retrieval packet, repeated data and unknown near-family correlations. Other documents are distractors, not certified wrong factual endings. Both retrieval directions share64 cases; do not count128 independent examples. Retrieval success is not generation or next-token quality." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/review.json — all_three_fixed_DEV64_retrieval_models_reviewed</summary>

[原記録](../../reports/phase6/natural-context-contrast-dev-transfer-evidence-20261007/run/review.json) ／ SHA256: `32c309825a5944068a4937777de182f4c03f49b23a93406751e95295270ac2b0` ／ 16,215 bytes

| 原キー | 保存値 |
|---|---|
| status | "all_three_fixed_DEV64_retrieval_models_reviewed" |
| GPU_occupancy_seconds | 1.501790620997781 |
| paired_document_differences.CE_minus_original.point | 0.0078125 |
| paired_document_differences.CE_minus_original.CI95 | [-0.015625, 0.03125] |
| paired_document_differences.CE_minus_original.document_units | 64 |
| paired_document_differences.CE_minus_original.directions_correlated | true |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | -0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired_document_differences.contrast_minus_CE.point | 0.109375 |
| paired_document_differences.contrast_minus_CE.CI95 | [0.0390625, 0.1953125] |
| paired_document_differences.contrast_minus_CE.document_units | 64 |
| paired_document_differences.contrast_minus_CE.directions_correlated | true |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired_document_differences.contrast_minus_original.point | 0.1171875 |
| paired_document_differences.contrast_minus_original.CI95 | [0.046875, 0.1953125] |
| paired_document_differences.contrast_minus_original.document_units | 64 |
| paired_document_differences.contrast_minus_original.directions_correlated | true |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| conclusion | "Contrast transfers some observed document-pair discrimination to this fixed DEV packet. Original failed generation and retention outcomes remain unchanged; retrieval does not certify appropriate next-token continuation, semantic reasoning or Base quality." |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| one_shot_diagnostic_closed | true |
| limitations | "Retrospective diagnostic, fixed64 documents and unknown near-family correlations. Bootstrap resamples document pairs, not128 independent directions, and is not an independent seed or natural-Japanese population guarantee. Variance is retained from actual scoring; matrices do not reconstruct feature coordinates." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-final-evidence-20261007/manifest.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-final-evidence-20261007/manifest.json) ／ SHA256: `87bf59297038a6b7ecec688c7ad9f2f521e63ac5c9270a69d40fc8469d8453c3` ／ 3,552 bytes

| 原キー | 保存値 |
|---|---|
| limitations | "Original checkpoint tensors, complete metrics and training corpus remain in WSL; this portable archive preserves terminal metadata, contrast raw evaluations and all160 review." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_comparison_review.json — all160_context_comparison_reviewed</summary>

[原記録](../../reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_comparison_review.json) ／ SHA256: `d034f4f5c20d67c6d94e5052f569670fce2fd5e166fd0d625b16c1def003c674` ／ 7,099 bytes

| 原キー | 保存値 |
|---|---|
| status | "all160_context_comparison_reviewed" |
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
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| strong_relative_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_relative_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_relative_quality.CE.checks.EOS_nonworsening | false |
| strong_relative_quality.CE.checks.repetition_nonworsening | false |
| strong_relative_quality.CE.checks.no_empty_role_unicode | true |
| strong_relative_quality.CE.checks.BPB_gate | true |
| strong_relative_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_relative_quality.CE.passed | false |
| strong_relative_quality.contrast.checks.coherence_gain_at_least8 | false |
| strong_relative_quality.contrast.checks.paired_CI_lower_above0 | false |
| strong_relative_quality.contrast.checks.EOS_nonworsening | false |
| strong_relative_quality.contrast.checks.repetition_nonworsening | false |
| strong_relative_quality.contrast.checks.no_empty_role_unicode | true |
| strong_relative_quality.contrast.checks.BPB_gate | true |
| strong_relative_quality.contrast.checks.appropriate_completion_not_punctuation | true |
| strong_relative_quality.contrast.passed | false |
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | true |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
| absolute_dev_screen.CE.grammar_at_least56 | false |
| absolute_dev_screen.CE.coherence_at_least27 | false |
| absolute_dev_screen.CE.appropriate_at_least27 | false |
| absolute_dev_screen.CE.EOS_at_least37 | false |
| absolute_dev_screen.CE.repetition_at_most18 | false |
| absolute_dev_screen.CE.no_empty_role_unicode | true |
| absolute_dev_screen.contrast.grammar_at_least56 | false |
| absolute_dev_screen.contrast.coherence_at_least27 | false |
| absolute_dev_screen.contrast.appropriate_at_least27 | false |
| absolute_dev_screen.contrast.EOS_at_least37 | false |
| absolute_dev_screen.contrast.repetition_at_most18 | false |
| absolute_dev_screen.contrast.no_empty_role_unicode | true |
| historical_Web.CE.EOS_at_least8_more | true |
| historical_Web.CE.repetition_no_worse | true |
| historical_Web.CE.no_empty_role_unicode | true |
| historical_Web.CE.BPB_degradation_at_most1percent | false |
| historical_Web.contrast.EOS_at_least8_more | false |
| historical_Web.contrast.repetition_no_worse | true |
| historical_Web.contrast.no_empty_role_unicode | true |
| historical_Web.contrast.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.CE | false |
| eligible_for_final_Base_validation.contrast | false |
| accounting.CE.completed_updates | 17698 |
| accounting.CE.CE_teacher_tokens | 100000000 |
| accounting.CE.auxiliary_input_tokens | 0 |
| accounting.CE.auxiliary_pairs | 0 |
| accounting.CE.CE_input_tokens | 102655467 |
| accounting.CE.physical_input_tokens | 370838917 |
| accounting.CE.source_teachers.web | 75000000 |
| accounting.CE.source_teachers.textbook | 20000000 |
| accounting.CE.source_teachers.story | 5000000 |
| accounting.CE.source_EOS.web | 657450 |
| accounting.CE.source_EOS.textbook | 148625 |
| accounting.CE.source_EOS.story | 38222 |
| accounting.CE.original_body_bytes | 405882136 |
| accounting.contrast.completed_updates | 17698 |
| accounting.contrast.CE_teacher_tokens | 100000000 |
| accounting.contrast.auxiliary_input_tokens | 86885793 |
| accounting.contrast.auxiliary_pairs | 676384 |
| accounting.contrast.CE_input_tokens | 102655467 |
| accounting.contrast.physical_input_tokens | 683893095 |
| accounting.contrast.source_teachers.web | 75000000 |
| accounting.contrast.source_teachers.textbook | 20000000 |
| accounting.contrast.source_teachers.story | 5000000 |
| accounting.contrast.source_EOS.web | 657450 |
| accounting.contrast.source_EOS.textbook | 148625 |
| accounting.contrast.source_EOS.story | 38222 |
| accounting.contrast.original_body_bytes | 405882136 |
| common_CE_checks.token_digest | true |
| common_CE_checks.supervised_tokens | true |
| common_CE_checks.source_teachers | true |
| common_CE_checks.source_EOS | true |
| common_CE_checks.CE_input_tokens | true |
| common_CE_checks.original_body_bytes | true |
| scientific_CE_teacher_tokens | 200000000 |
| probe_updates_separate | 112 |
| GPU_occupancy_seconds | 3762.997766413988 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "One learned seed and repeated nonblind DEV; source draws are exposure, not unique supply. The evaluator marks no protected TEST cases evaluated; its task loader may decode the suite JSON. Diagnostic CUDA resume updates and auxiliary input are separate from scientific CE teachers." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_contrast_content_review.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_contrast_content_review.json) ／ SHA256: `462948e714351a500915180a817e8a35b4237c5d031ff4d08665623f78165a39` ／ 772 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.0028900182891256 |
| rates.eos | 6 |
| rates.repetition | 53 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 48 |
| relevance2 | 26 |
| coherent | 0 |
| appropriate | 3 |
| notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| scope | "one_arm_content_only_comparison_and_final_validation_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_contrast_notes.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-final-evidence-20261007/natural_context_contrast_contrast_notes.json) ／ SHA256: `fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47` ／ 20,780 bytes

| 原キー | 保存値 |
|---|---|

</details>
