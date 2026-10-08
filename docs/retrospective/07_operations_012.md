# 実行管理・後続準備・その他 — 12/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/progress-result.json) ／ SHA256: `d56d64a8e35498061f94442793f6298ecb4c2bce94f45c2b133ac85937cfdf14` ／ 1,918,883 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| checkpoints.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| checkpoints.control.binding.config_sha256 | "03b4ad47fa42b9a669c4588e736648e6339c93b9eb0cf3d08aac22a46cf90a88" |
| checkpoints.control.binding.arm | "source_order" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.control.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 1e-05 |
| checkpoints.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.control.binding.study_kind | "historical_parent_source_order_100M" |
| checkpoints.control.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.control.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.control.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.control.update | 323503 |
| checkpoints.control.tokens | 10600546304 |
| checkpoints.control.supervised_tokens | 10577786961 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100532224 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 159170 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 234328 |
| checkpoints.control.source_input_tokens.web | 75183104 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.control.focus_teacher_tokens | 1407427 |
| checkpoints.control.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 163.39403466315707 |
| checkpoints.control.completed_at | "2026-10-06T06:25:12.649548Z" |
| checkpoints.eos_decoupled_web_kl.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/eos_decoupled_web_kl/training/checkpoint-00323503.pt" |
| checkpoints.eos_decoupled_web_kl.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| checkpoints.eos_decoupled_web_kl.binding.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| checkpoints.eos_decoupled_web_kl.binding.arm | "eos_decoupled_web_kl" |
| checkpoints.eos_decoupled_web_kl.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.eos_decoupled_web_kl.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.eos_decoupled_web_kl.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.eos_decoupled_web_kl.binding.teacher_goals.web | 75000000 |
| checkpoints.eos_decoupled_web_kl.binding.teacher_goals.story | 5000000 |
| checkpoints.eos_decoupled_web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.eos_decoupled_web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.eos_decoupled_web_kl.binding.optimizer_policy | "inherit" |
| checkpoints.eos_decoupled_web_kl.binding.peak_lr | 1e-05 |
| checkpoints.eos_decoupled_web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.eos_decoupled_web_kl.binding.study_kind | "historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M" |
| checkpoints.eos_decoupled_web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| checkpoints.eos_decoupled_web_kl.binding.outcome_weight | 1 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.direction | "parent_to_student" |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.temperature | 1.0 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.coefficient | 1.0 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.every_completed_update | 1 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.reference_context | 1024 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.reference_batch | 8 |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.eos_decoupled_web_kl.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| checkpoints.eos_decoupled_web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.eos_decoupled_web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.eos_decoupled_web_kl.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.eos_decoupled_web_kl.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.eos_decoupled_web_kl.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.eos_decoupled_web_kl.update | 323503 |
| checkpoints.eos_decoupled_web_kl.tokens | 10600546304 |
| checkpoints.eos_decoupled_web_kl.supervised_tokens | 10577786961 |
| checkpoints.eos_decoupled_web_kl.additional_supervised_tokens | 100000000 |
| checkpoints.eos_decoupled_web_kl.additional_input_tokens | 100532224 |
| checkpoints.eos_decoupled_web_kl.source_teachers.web | 75000000 |
| checkpoints.eos_decoupled_web_kl.source_teachers.story | 5000000 |
| checkpoints.eos_decoupled_web_kl.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.eos_decoupled_web_kl.source_teachers.conditional_textbook | 10000000 |
| checkpoints.eos_decoupled_web_kl.source_eos.web | 159170 |
| checkpoints.eos_decoupled_web_kl.source_eos.story | 38240 |
| checkpoints.eos_decoupled_web_kl.source_eos.ordinary_textbook | 74183 |
| checkpoints.eos_decoupled_web_kl.source_eos.conditional_textbook | 234328 |
| checkpoints.eos_decoupled_web_kl.source_input_tokens.web | 75183104 |
| checkpoints.eos_decoupled_web_kl.source_input_tokens.story | 5039104 |
| checkpoints.eos_decoupled_web_kl.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.eos_decoupled_web_kl.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.eos_decoupled_web_kl.source_focus_teachers.web | 0 |
| checkpoints.eos_decoupled_web_kl.source_focus_teachers.story | 0 |
| checkpoints.eos_decoupled_web_kl.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.eos_decoupled_web_kl.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.eos_decoupled_web_kl.focus_teacher_tokens | 1407427 |
| checkpoints.eos_decoupled_web_kl.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.eos_decoupled_web_kl.weighted_teacher_mass | 100000000 |
| checkpoints.eos_decoupled_web_kl.outcome_weight | 1 |
| checkpoints.eos_decoupled_web_kl.training_seconds | 287.5748953077127 |
| checkpoints.eos_decoupled_web_kl.completed_at | "2026-10-06T07:25:26.363788Z" |
| checkpoints.eos_decoupled_web_kl.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| checkpoints.eos_decoupled_web_kl.reference_replay.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.eos_decoupled_web_kl.reference_replay.batch | 8 |
| checkpoints.eos_decoupled_web_kl.reference_replay.context | 1024 |
| checkpoints.eos_decoupled_web_kl.reference_replay.initial_cursor.seed | 42 |
| checkpoints.eos_decoupled_web_kl.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.eos_decoupled_web_kl.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.eos_decoupled_web_kl.reference_replay.initial_cursor.context | 1024 |
| checkpoints.eos_decoupled_web_kl.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.sampler.seed | 42 |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.sampler.context | 1024 |
| checkpoints.eos_decoupled_web_kl.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.eos_decoupled_web_kl.reference_replay.updates | 3068 |
| checkpoints.eos_decoupled_web_kl.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.eos_decoupled_web_kl.reference_replay.body_positions | 25026383 |
| checkpoints.eos_decoupled_web_kl.reference_replay.ignored_positions | 106673 |
| checkpoints.eos_decoupled_web_kl.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.eos_decoupled_web_kl.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.eos_decoupled_web_kl.reference_input_tokens | 25133056 |
| checkpoints.eos_decoupled_web_kl.reference_soft_target_body_positions | 25026383 |
| checkpoints.eos_decoupled_web_kl.combined_student_physical_input_tokens | 125665280 |
| checkpoints.eos_decoupled_web_kl.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.eos_decoupled_web_kl.KL_policy.direction | "parent_to_student" |
| checkpoints.eos_decoupled_web_kl.KL_policy.temperature | 1.0 |
| checkpoints.eos_decoupled_web_kl.KL_policy.coefficient | 1.0 |
| checkpoints.eos_decoupled_web_kl.KL_policy.every_completed_update | 1 |
| checkpoints.eos_decoupled_web_kl.KL_policy.reference_context | 1024 |
| checkpoints.eos_decoupled_web_kl.KL_policy.reference_batch | 8 |
| checkpoints.eos_decoupled_web_kl.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.eos_decoupled_web_kl.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.eos_decoupled_web_kl.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.eos_decoupled_web_kl.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| evaluations.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 370922.2019701004 |
| evaluations.control.body.eos_nll | 404.9141170345247 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1336128657420816 |
| evaluations.control.body.seconds | 1.6409143939963542 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 76 |
| evaluations.control.greedy_rates.repetition | 2 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.control.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.control.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.control.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.26541554959785524 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.26541554959785524 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.26630920464700625 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.26555235832138696 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.08306759781336262 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.control.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.eos_decoupled_web_kl.binding.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| evaluations.eos_decoupled_web_kl.binding.arm | "eos_decoupled_web_kl" |
| evaluations.eos_decoupled_web_kl.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.eos_decoupled_web_kl.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.eos_decoupled_web_kl.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| evaluations.eos_decoupled_web_kl.binding.teacher_goals.web | 75000000 |
| evaluations.eos_decoupled_web_kl.binding.teacher_goals.story | 5000000 |
| evaluations.eos_decoupled_web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.eos_decoupled_web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.eos_decoupled_web_kl.binding.optimizer_policy | "inherit" |
| evaluations.eos_decoupled_web_kl.binding.peak_lr | 1e-05 |
| evaluations.eos_decoupled_web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.eos_decoupled_web_kl.binding.study_kind | "historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M" |
| evaluations.eos_decoupled_web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| evaluations.eos_decoupled_web_kl.binding.outcome_weight | 1 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.direction | "parent_to_student" |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.temperature | 1.0 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.coefficient | 1.0 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.every_completed_update | 1 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.reference_context | 1024 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.reference_batch | 8 |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| evaluations.eos_decoupled_web_kl.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| evaluations.eos_decoupled_web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.eos_decoupled_web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.eos_decoupled_web_kl.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| evaluations.eos_decoupled_web_kl.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| evaluations.eos_decoupled_web_kl.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| evaluations.eos_decoupled_web_kl.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| evaluations.eos_decoupled_web_kl.body.split | "dev" |
| evaluations.eos_decoupled_web_kl.body.documents | 256 |
| evaluations.eos_decoupled_web_kl.body.limit_documents | 256 |
| evaluations.eos_decoupled_web_kl.body.context | 1024 |
| evaluations.eos_decoupled_web_kl.body.stride | 512 |
| evaluations.eos_decoupled_web_kl.body.batch | 16 |
| evaluations.eos_decoupled_web_kl.body.body_nll | 321651.43452215195 |
| evaluations.eos_decoupled_web_kl.body.eos_nll | 513.1300341412425 |
| evaluations.eos_decoupled_web_kl.body.body_bytes | 472055 |
| evaluations.eos_decoupled_web_kl.body.body_tokens | 122343 |
| evaluations.eos_decoupled_web_kl.body.bpb | 0.9830314888729699 |
| evaluations.eos_decoupled_web_kl.body.seconds | 1.4468623629945796 |
| evaluations.eos_decoupled_web_kl.body.evaluator | "batched-heldout-fp32-ce-v1" |
| evaluations.eos_decoupled_web_kl.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.eos_decoupled_web_kl.generation.binding | "{\"binding\": {\"KL_policy\": {\"coefficient\": 1.0, \"direction\": \"parent_to_student\", \"every_completed_update\": 1, \"kind\": \"frozen-parent-Web-body-conditional-non-EOS-KL-v1\", \"masked_targets\": \"labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs.\", \"objective_component\": \"Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only.\", \"reference_batch\": 8, \"reference_context\": 1024, \"reference_teacher\": \"immutable actual historical10.5B parent, no optimizer/gradients\", \"replay_policy\": \"separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test\", \"temperature\": 1.0}, \"arm\": \"eos_decoupled_web_kl\", \"config_sha256\": \"1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017\", \"loss\": \"ordinary original body+EOS CE, outcome weight1\", \"optimizer_policy\": \"inherit\", \"original_web\": {\"manifest_sha256\": \"2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de\", \"path\": \"/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards\"}, \"outcome_weight\": 1, \"parent\": {\"path\": \"/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt\", \"sha256\": \"d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4\"}, \"peak_lr\": 1e-05, \"positive_manifest_sha256\": \"154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936\", \"reference_teacher\": {\"path\": \"/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt\", \"sha256\": \"d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4\"}, \"sampler_policy\": \"Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus.\", \"short_manifest_sha256\": \"8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133\", \"study_kind\": \"historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M\", \"teacher_goals\": {\"conditional_textbook\": 10000000, \"ordinary_textbook\": 10000000, \"story\": 5000000, \"web\": 75000000}}, \"checkpoint_sha256\": \"a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213\"}" |
| evaluations.eos_decoupled_web_kl.generation.suite_sha256 | "93cd3a19f3e62c8d30d1660b431a9525823f58b9ceb1bf90c6ecbac2c19292eb" |
| evaluations.eos_decoupled_web_kl.generation.max_new_tokens | 64 |
| evaluations.eos_decoupled_web_kl.greedy_rates.outputs | 80 |
| evaluations.eos_decoupled_web_kl.greedy_rates.eos | 44 |
| evaluations.eos_decoupled_web_kl.greedy_rates.repetition | 20 |
| evaluations.eos_decoupled_web_kl.greedy_rates.unicode_failure | 0 |
| evaluations.eos_decoupled_web_kl.greedy_rates.role_leak | 0 |
| evaluations.eos_decoupled_web_kl.greedy_rates.empty | 0 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/evaluation/eos_decoupled_web_kl/evaluation/semantics.json" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.complete | true |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.expected | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.count | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.count | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.macro_f1 | 0.5724991854024112 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.mcc | 0.14611900125320154 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5520833333333334 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.59375] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5520833333333334 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5508649766075508 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.mcc | 0.10473644811127698 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.count | 192 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.macro_f1 | 0.4991304347826087 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.mcc | 0.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.chance | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.above_chance_evidence | true |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.point | 0.78125 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.ci95 | [0.65625, 0.90625] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.point | 0.59375 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.ci95 | [0.5, 0.71875] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.point | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.ci95 | [0.40625, 0.59375] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.point | 0.53125 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.ci95 | [0.5, 0.59375] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.point | 0.4375 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.ci95 | [0.3125, 0.59375] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.point | 0.59375 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.ci95 | [0.5, 0.71875] |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.units | 16 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.examples | 32 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.tie_examples | 0 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/evaluation/eos_decoupled_web_kl/evaluation/jblimp.json" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.complete | true |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.expected | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.count | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.point | 0.743202416918429 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.ci95 | [0.6978851963746223, 0.7885196374622356] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.count | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.hard_accuracy | 0.743202416918429 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.macro_f1 | 0.42634315424610053 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.mcc | 0.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7190332326283988 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6706948640483383, 0.7673716012084593] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7190332326283988 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4182776801405975 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.count | 331 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.macro_f1 | 0.3231083844580777 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.mcc | 0.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.chance | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.above_chance_evidence | true |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.point | 0.8181818181818182 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.ci95 | [0.5454545454545454, 1.0] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.units | 11 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.examples | 11 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.point | 0.46153846153846156 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.ci95 | [0.15384615384615385, 0.6923076923076923] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.units | 13 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.examples | 13 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.point | 0.8285714285714286 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.ci95 | [0.7642857142857142, 0.8857142857142857] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.units | 140 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.examples | 140 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.point | 0.7894736842105263 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.ci95 | [0.5789473684210527, 0.9473684210526315] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.units | 19 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.examples | 19 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.point | 0.5081967213114754 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.ci95 | [0.3770491803278688, 0.639344262295082] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.units | 61 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.examples | 61 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.point | 0.4444444444444444 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.ci95 | [0.1111111111111111, 0.7777777777777778] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.units | 9 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.examples | 9 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.point | 0.8 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.ci95 | [0.6571428571428571, 0.9142857142857143] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.units | 35 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.examples | 35 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.point | 1.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.ci95 | [1.0, 1.0] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.units | 23 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.examples | 23 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.point | 0.8571428571428571 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.ci95 | [0.6428571428571429, 1.0] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.units | 14 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.examples | 14 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.point | 0.5 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.ci95 | [0.0, 1.0] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.units | 4 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.examples | 4 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.point | 0.0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.ci95 | [0.0, 0.0] |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.units | 2 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.examples | 2 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.tie_examples | 0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.eos_decoupled_web_kl.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/evaluation/eos_decoupled_web_kl/evaluation/jcqa.json" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.complete | true |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.expected | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.count | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.ci95 | [0.3127792672028597, 0.36642091152815] |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.count | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.macro_f1 | 0.3389950281148806 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.mcc | 0.17467412347871514 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30903529199025803 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.mcc | 0.13825571947644602 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.count | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.macro_f1 | 0.17226221885700888 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.mcc | -0.034285051798449845 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.chance | 0.2 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.above_chance_evidence | true |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.point | 0.33958891867739055 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.ci95 | [0.3127792672028597, 0.36642091152815] |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.units | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.examples | 1119 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.unit | "family/prompt" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.tie_examples | 0 |
| evaluations.eos_decoupled_web_kl.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.eos_decoupled_web_kl.diagnostics.semantic_both_contexts.correct | 19 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantic_both_contexts.total | 96 |
| evaluations.eos_decoupled_web_kl.diagnostics.semantic_both_contexts.fraction | 0.19791666666666666 |
| evaluations.eos_decoupled_web_kl.memory.forward_calls | 3659 |
| evaluations.eos_decoupled_web_kl.memory.cache_releases | 2 |
| evaluations.eos_decoupled_web_kl.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.eos_decoupled_web_kl.memory.maximum_observed_reserved_bytes | 13046382592 |
| evaluations.eos_decoupled_web_kl.memory.policy | "Every32 forwards, release unused cache if reserved&gt;8GiB and unused&gt;4GiB" |
| evaluations.eos_decoupled_web_kl.evaluation_RNG_isolated | true |
| evaluations.eos_decoupled_web_kl.protected_test_used | false |
| evaluations.eos_decoupled_web_kl.completed_at | "2026-10-06T07:26:34.631773Z" |
| mechanism_cached.checkpoints.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v3-20261006/web_kl/training/checkpoint-00323503.pt" |
| mechanism_cached.checkpoints.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| mechanism_cached.checkpoints.binding.config_sha256 | "60fcb3e6236f66bcdea397c09cc0f927212a1e3e3dbe94e23c6ff2a7837db0a9" |
| mechanism_cached.checkpoints.binding.arm | "web_kl" |
| mechanism_cached.checkpoints.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.checkpoints.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.checkpoints.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| mechanism_cached.checkpoints.binding.teacher_goals.web | 75000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.story | 5000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.ordinary_textbook | 10000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.conditional_textbook | 10000000 |
| mechanism_cached.checkpoints.binding.optimizer_policy | "inherit" |
| mechanism_cached.checkpoints.binding.peak_lr | 1e-05 |
| mechanism_cached.checkpoints.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| mechanism_cached.checkpoints.binding.study_kind | "historical_parent_staged_CE_frozen_Web_KL_100M" |
| mechanism_cached.checkpoints.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| mechanism_cached.checkpoints.binding.outcome_weight | 1 |
| mechanism_cached.checkpoints.binding.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| mechanism_cached.checkpoints.binding.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.binding.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| mechanism_cached.checkpoints.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.checkpoints.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.checkpoints.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.checkpoints.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| mechanism_cached.checkpoints.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| mechanism_cached.checkpoints.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| mechanism_cached.checkpoints.update | 323503 |
| mechanism_cached.checkpoints.tokens | 10600546304 |
| mechanism_cached.checkpoints.supervised_tokens | 10577786961 |
| mechanism_cached.checkpoints.additional_supervised_tokens | 100000000 |
| mechanism_cached.checkpoints.additional_input_tokens | 100532224 |
| mechanism_cached.checkpoints.source_teachers.web | 75000000 |
| mechanism_cached.checkpoints.source_teachers.story | 5000000 |
| mechanism_cached.checkpoints.source_teachers.ordinary_textbook | 10000000 |
| mechanism_cached.checkpoints.source_teachers.conditional_textbook | 10000000 |
| mechanism_cached.checkpoints.source_eos.web | 159170 |
| mechanism_cached.checkpoints.source_eos.story | 38240 |
| mechanism_cached.checkpoints.source_eos.ordinary_textbook | 74183 |
| mechanism_cached.checkpoints.source_eos.conditional_textbook | 234328 |
| mechanism_cached.checkpoints.source_input_tokens.web | 75183104 |
| mechanism_cached.checkpoints.source_input_tokens.story | 5039104 |
| mechanism_cached.checkpoints.source_input_tokens.ordinary_textbook | 10075136 |
| mechanism_cached.checkpoints.source_input_tokens.conditional_textbook | 10234880 |
| mechanism_cached.checkpoints.source_focus_teachers.web | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.story | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.ordinary_textbook | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.conditional_textbook | 1407427 |
| mechanism_cached.checkpoints.focus_teacher_tokens | 1407427 |
| mechanism_cached.checkpoints.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| mechanism_cached.checkpoints.weighted_teacher_mass | 100000000 |
| mechanism_cached.checkpoints.outcome_weight | 1 |
| mechanism_cached.checkpoints.training_seconds | 255.1444061366201 |
| mechanism_cached.checkpoints.completed_at | "2026-10-06T07:04:02.917166Z" |
| mechanism_cached.checkpoints.reference_replay.kind | "frozen-parent-Web-body-KL-v1" |
| mechanism_cached.checkpoints.reference_replay.batch | 8 |
| mechanism_cached.checkpoints.reference_replay.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.seed | 42 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.epoch | 0 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.position | 10253920 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.blocks | 11939276 |
| mechanism_cached.checkpoints.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| mechanism_cached.checkpoints.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.seed | 42 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.epoch | 0 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.position | 10278464 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.blocks | 11939276 |
| mechanism_cached.checkpoints.reference_replay.updates | 3068 |
| mechanism_cached.checkpoints.reference_replay.physical_input_tokens | 25133056 |
| mechanism_cached.checkpoints.reference_replay.body_positions | 25026383 |
| mechanism_cached.checkpoints.reference_replay.ignored_positions | 106673 |
| mechanism_cached.checkpoints.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| mechanism_cached.checkpoints.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| mechanism_cached.checkpoints.reference_input_tokens | 25133056 |
| mechanism_cached.checkpoints.reference_soft_target_body_positions | 25026383 |
| mechanism_cached.checkpoints.combined_student_physical_input_tokens | 125665280 |
| mechanism_cached.checkpoints.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| mechanism_cached.checkpoints.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| mechanism_cached.checkpoints.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.evaluations.binding.teacher_goals.web | 75000000 |
| mechanism_cached.evaluations.binding.teacher_goals.story | 5000000 |
| mechanism_cached.evaluations.binding.teacher_goals.ordinary_textbook | 10000000 |
| mechanism_cached.evaluations.binding.teacher_goals.conditional_textbook | 10000000 |
| mechanism_cached.evaluations.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| mechanism_cached.evaluations.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| mechanism_cached.evaluations.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.evaluations.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.evaluations.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.evaluations.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.evaluations.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| mechanism_cached.evaluations.body.documents | 256 |
| mechanism_cached.evaluations.body.limit_documents | 256 |
| mechanism_cached.evaluations.body.body_nll | 321401.2076690197 |
| mechanism_cached.evaluations.body.eos_nll | 635.9188746847212 |
| mechanism_cached.evaluations.body.body_bytes | 472055 |
| mechanism_cached.evaluations.body.body_tokens | 122343 |
| mechanism_cached.evaluations.body.bpb | 0.982266745272942 |
| mechanism_cached.evaluations.body.seconds | 1.3322648800094612 |
| mechanism_cached.evaluations.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| mechanism_cached.evaluations.generation.max_new_tokens | 64 |
| mechanism_cached.evaluations.greedy_rates.eos | 40 |
| mechanism_cached.evaluations.greedy_rates.repetition | 22 |
| mechanism_cached.evaluations.greedy_rates.unicode_failure | 0 |
| mechanism_cached.evaluations.greedy_rates.role_leak | 0 |
| mechanism_cached.evaluations.greedy_rates.empty | 0 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.point | 0.546875 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.5833333333333334] |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.count | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.546875 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5458771715194519 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.mcc | 0.09416472308615167 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.train_majority_accuracy | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.point | 0.743202416918429 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.ci95 | [0.6978851963746223, 0.7885196374622356] |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.hard_accuracy | 0.743202416918429 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6766616314199396, 0.770392749244713] |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.count | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| mechanism_cached.evaluations.diagnostics.jblimp.train_majority_accuracy | null |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.point | 0.340035746201966 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.ci95 | [0.3136729222520107, 0.3672922252010724] |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.hard_accuracy | 0.34048257372654156 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.count | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30891961343493624 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.mcc | 0.13812773034264442 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| mechanism_cached.evaluations.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.semantic_both_contexts.correct | 18 |
| mechanism_cached.evaluations.memory.maximum_observed_allocated_bytes | 315223040 |
| mechanism_cached.evaluations.memory.maximum_observed_reserved_bytes | 13046382592 |
| mechanism_cached.evaluations.protected_test_used | false |
| mechanism_cached.transfer.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| mechanism_cached.transfer.checks.weights_unchanged | true |
| mechanism_cached.transfer.checks.no_gradients | true |
| mechanism_cached.transfer.checks.eval_mode | true |
| mechanism_cached.transfer.checks.RNG_restored | true |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 55 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 67 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 11 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.703125 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.546875 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| mechanism_cached.transfer.optimizer_updates | 0 |
| mechanism_cached.transfer.scientific_teacher_tokens | 0 |
| mechanism_cached.transfer.protected_test_used | false |
| mechanism_cached.transfer.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| mechanism_cached.retention.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| mechanism_cached.retention.checks.weights_unchanged | true |
| mechanism_cached.retention.checks.no_gradients | true |
| mechanism_cached.retention.checks.eval_mode | true |
| mechanism_cached.retention.checks.RNG_restored | true |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 32 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 26 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 34 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| mechanism_cached.retention.optimizer_updates | 0 |
| mechanism_cached.retention.scientific_teacher_tokens | 0 |
| mechanism_cached.retention.protected_test_used | false |
| mechanism_cached.retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| transfer.control.checks.weights_unchanged | true |
| transfer.control.checks.no_gradients | true |
| transfer.control.checks.eval_mode | true |
| transfer.control.checks.RNG_restored | true |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 59 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.control.optimizer_updates | 0 |
| transfer.control.scientific_teacher_tokens | 0 |
| transfer.control.protected_test_used | false |
| transfer.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.eos_decoupled_web_kl.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| transfer.eos_decoupled_web_kl.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| transfer.eos_decoupled_web_kl.cases_sha256 | "4e9c11d18395b03aeeb8a9ac7caec86f8ef6f59ca598ca00bf14bac447f85823" |
| transfer.eos_decoupled_web_kl.checks.weights_unchanged | true |
| transfer.eos_decoupled_web_kl.checks.no_gradients | true |
| transfer.eos_decoupled_web_kl.checks.eval_mode | true |
| transfer.eos_decoupled_web_kl.checks.RNG_restored | true |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.families | 128 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.same_unique_candidate | 70 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| transfer.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 59 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer.eos_decoupled_web_kl.evaluated_requests | 512 |
| transfer.eos_decoupled_web_kl.optimizer_updates | 0 |
| transfer.eos_decoupled_web_kl.scientific_teacher_tokens | 0 |
| transfer.eos_decoupled_web_kl.protected_test_used | false |
| transfer.eos_decoupled_web_kl.suite | "bridge" |
| transfer.eos_decoupled_web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| retention.control.checks.weights_unchanged | true |
| retention.control.checks.no_gradients | true |
| retention.control.checks.eval_mode | true |
| retention.control.checks.RNG_restored | true |
| retention.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 36 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 42 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.control.optimizer_updates | 0 |
| retention.control.scientific_teacher_tokens | 0 |
| retention.control.protected_test_used | false |
| retention.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.eos_decoupled_web_kl.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| retention.eos_decoupled_web_kl.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| retention.eos_decoupled_web_kl.cases_sha256 | "daf92018a167c24db83a4d3bd029d45973bd7f34f3fd452f52419ccc0b651d83" |
| retention.eos_decoupled_web_kl.checks.weights_unchanged | true |
| retention.eos_decoupled_web_kl.checks.no_gradients | true |
| retention.eos_decoupled_web_kl.checks.eval_mode | true |
| retention.eos_decoupled_web_kl.checks.RNG_restored | true |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.families | 128 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 33 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.same_unique_candidate | 89 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 27 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.eos_decoupled_web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.625 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 86 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 33 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 34 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.eos_decoupled_web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.eos_decoupled_web_kl.evaluated_requests | 512 |
| retention.eos_decoupled_web_kl.optimizer_updates | 0 |
| retention.eos_decoupled_web_kl.scientific_teacher_tokens | 0 |
| retention.eos_decoupled_web_kl.protected_test_used | false |
| retention.eos_decoupled_web_kl.suite | "retention" |
| retention.eos_decoupled_web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/review.json — web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/review.json) ／ SHA256: `1f072e9340549db0733bb89f0cfeeac8b80ac4fbea9f9b3bb7e932f45e081af0` ／ 14,245 bytes

| 原キー | 保存値 |
|---|---|
| status | "web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed" |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | true |
| mechanism_comparison.checks.repetition_nonworsening | true |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
| mechanism_summary.BPB | 0.982266745272942 |
| mechanism_summary.rates.eos | 40 |
| mechanism_summary.rates.repetition | 22 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 58 |
| mechanism_summary.relevance2 | 47 |
| mechanism_summary.coherent | 9 |
| mechanism_summary.appropriate | 25 |
| mechanism_summary.notes_sha256 | "66129a961bc6e66e641b4560db6dfcafeba078ad4497e018152cc6f73354ebd7" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| previous_related_study_GPU_seconds | 401.47591929804184 |
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
| summaries.eos_decoupled_web_kl.BPB | 0.9830314888729699 |
| summaries.eos_decoupled_web_kl.rates.outputs | 80 |
| summaries.eos_decoupled_web_kl.rates.eos | 44 |
| summaries.eos_decoupled_web_kl.rates.repetition | 20 |
| summaries.eos_decoupled_web_kl.rates.unicode_failure | 0 |
| summaries.eos_decoupled_web_kl.rates.role_leak | 0 |
| summaries.eos_decoupled_web_kl.rates.empty | 0 |
| summaries.eos_decoupled_web_kl.grammar2 | 58 |
| summaries.eos_decoupled_web_kl.relevance2 | 49 |
| summaries.eos_decoupled_web_kl.coherent | 11 |
| summaries.eos_decoupled_web_kl.appropriate | 28 |
| summaries.eos_decoupled_web_kl.generation_sha256 | "c3805846c57796df38fe32c4ea4f4e7a834cc2ef62f4128348a5df5d00984db6" |
| summaries.eos_decoupled_web_kl.notes_sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| summaries.eos_decoupled_web_kl.Japanese.semantics | 0.5729166666666666 |
| summaries.eos_decoupled_web_kl.Japanese.jblimp | 0.743202416918429 |
| summaries.eos_decoupled_web_kl.Japanese.jcqa | 0.33958891867739055 |
| summaries.eos_decoupled_web_kl.additional_teacher_tokens | 100000000 |
| summaries.eos_decoupled_web_kl.independent_human_blind | false |
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
| absolute_dev_screen.appropriate_at_least27 | true |
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
| reference_accounting.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| reference_accounting.frozen_parent_teacher_digest_verified | true |
| reference_accounting.reference_input_tokens | 25133056 |
| reference_accounting.main_ordinary_CE_teacher_tokens | 100000000 |
| reference_accounting.combined_student_physical_input_tokens | 125665280 |
| reference_accounting.newly_prepared_source_tokens | 0 |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.control.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.sum_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.families | 128 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.accuracy | 0.6953125 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.both_correct | 54 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.same_unique_candidate | 70 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.both_correct | 12 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| transfer_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.both_correct | 54 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| retention_aggregates.control.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention_aggregates.control.sum_log_likelihood.all128.both_correct | 36 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention_aggregates.control.mean_token_log_likelihood.all128.both_correct | 42 |
| retention_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.families | 128 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.accuracy | 0.60546875 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.both_correct | 33 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.same_unique_candidate | 89 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.both_correct | 27 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.both_correct | 6 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention_aggregates.eos_decoupled_web_kl.sum_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.accuracy | 0.625 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.both_correct | 37 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.same_unique_candidate | 86 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 33 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention_aggregates.eos_decoupled_web_kl.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.both_correct | 34 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention_aggregates.eos_decoupled_web_kl.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 364.78950252200593 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| verification_GPU_seconds | 29.086883072013734 |
| prior_probe_GPU_seconds | 0.0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Additional separately counted Web reference soft targets; not equal total supervision or pure isolated objective effect. One learned seed; nonblind repeated fixeddev. Same parent/model/Adam/RNG/scheduler/actualLR and four primary streams/terminal cursors/ordinaryCE quotas/order. Adds frozen-parent distribution targets on separately counted overlapping trainWeb replay. Shared-generator bridge is local; old128 retention overlaps training forms. Independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0000.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0000.json) ／ SHA256: `5080f10707b20a78278e39405c572fed1a74d68114e374339217cae77ad1425a` ／ 9,935 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0016.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0016.json) ／ SHA256: `7ddb8122f92e8aae349847b8b47142de00a3f130659c587929fe43cf9db0a08d` ／ 9,583 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0032.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0032.json) ／ SHA256: `03896ec10100a10fef80b98268f01738a2c417b8a7d161439c3a63836cd3695c` ／ 10,228 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0048.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0048.json) ／ SHA256: `15e5c5cd7f426804ddfe6d8c61e9788c4d67487424df6699d297cf65f87e6a85` ／ 9,520 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0064.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0064.json) ／ SHA256: `7f945466e0e6d7ea737a8fa646b79c02ba860c41a97bcb38376ff901b78c0f95` ／ 10,305 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0080.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0080.json) ／ SHA256: `300449847997d674c18ce7c86e3c51dfa1f08333465774af436036843060b0b4` ／ 9,691 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0096.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0096.json) ／ SHA256: `fa6ac72d9160ca0a64c32ffadf0852e8b75ac97e20e6d06a5770bf7bde7fc001` ／ 9,800 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0112.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0112.json) ／ SHA256: `44e71544544724bb5ff0b4f8312e4e8e23fbd5827a4297bb318f52c0de1ef3db` ／ 10,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0128.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0128.json) ／ SHA256: `811c37edd2f6a17f22ac061f6e98a36922112c67be2aa8c4f89d1a2b7d22544e` ／ 9,808 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0144.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0144.json) ／ SHA256: `82d788c594f81a5a8a5d2bc28ce5a0264d909b8cfc98b3a7231f0f9ef29b7e33` ／ 9,870 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0160.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0160.json) ／ SHA256: `4bad72e6170c598d4b353f8d4407bc6e9ab9fc4ad385ec4fedd825db8bbe34a7` ／ 10,165 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0176.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0176.json) ／ SHA256: `5e737e982cb68e3bf81f2f24999093ba583701c8bd5cd9157ff87b7ab8d394d1` ／ 9,983 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0192.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0192.json) ／ SHA256: `7d31989721003fff5dd6ef2996e7540b6a59963028eb391a4d6f2e736768be79` ／ 9,909 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0208.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0208.json) ／ SHA256: `12b903625efb77b11622c34425c805a83d1ac062d710230930bffb7ea9d3b280` ／ 9,622 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0224.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0224.json) ／ SHA256: `1da17ec5b8077db86a178cf5519fce89f08825f6d263e78b9f3a87ba2192102f` ／ 9,820 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0240.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0240.json) ／ SHA256: `f6525877217d201fd52b2bdae3e4e6c93f9bdf309b414f1e50c8b881e86ece77` ／ 9,626 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0256.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0256.json) ／ SHA256: `e9b0ea771aae1e3345b887cfd116091fc8687417269f98831b5ae732419438c2` ／ 9,616 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0272.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0272.json) ／ SHA256: `bb850cc3adbb546756e350b92660306cf8df44a5acf81361e93e7ddba72a4508` ／ 9,596 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0288.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0288.json) ／ SHA256: `d845f3539bc278e3f5d7121442dbf5e54eea99fbd696f7b1d5d6510c65941d59` ／ 9,611 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0304.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0304.json) ／ SHA256: `1cf898ef93ede850b3bc8c1377465260f49b0b58ae849032a3cad3ffb11bc4c6` ／ 9,817 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0320.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0320.json) ／ SHA256: `b758eef636f2aac85a108c29bc2f3f9220999aeb4fda4fc02e596ec8ea19a0d0` ／ 9,324 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0336.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0336.json) ／ SHA256: `55efbecd71b9c06c0e429219110d354e05e91788a33a04bafb70d4e77f068ad6` ／ 9,429 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0352.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0352.json) ／ SHA256: `f7e90f597acac4000b40cc3c97e7757538a102f0807c0c37283b3a3286f3f271` ／ 9,791 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0368.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0368.json) ／ SHA256: `eadfe966d98d77e67f2eced3154555a65a07a7978cd7888e8f8a24a1fb760b71` ／ 9,542 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0384.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0384.json) ／ SHA256: `89582944602baf04469abcf207552cbcd50b8fa8240174e066db91b06c3a6229` ／ 9,866 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0400.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0400.json) ／ SHA256: `0516e5bfba1d6f89121acb1ec24bcf7b3f29faa745b049cd46863bd58f42b9e3` ／ 9,511 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0416.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0416.json) ／ SHA256: `026107d75e0f23f5ee2f3e22975775e6cf7c30fda3599ddbe70a3d79225a992b` ／ 9,892 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0432.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0432.json) ／ SHA256: `4bf9f67993c9504181f8c3122e1063d66a934fe25e83cbaaf4c97ce10e10d174` ／ 9,337 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0448.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0448.json) ／ SHA256: `dd0068610b9d08c5fb9c9fb24947b440575bad7bb2ef0bcea5cbcc9f1b123fb6` ／ 9,588 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0464.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0464.json) ／ SHA256: `972baabea42d6453e52d19aadcb60f36550e3af5be602a1b4daf4efe9f654242` ／ 9,404 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0480.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0480.json) ／ SHA256: `8d8a796344e3b346bd039422cb54ed531303771e4fdad580b5e4b54ac68fc439` ／ 9,452 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0496.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/0496.json) ／ SHA256: `cad94babfca404c6ea5517455da23aab2d8d52290315bdde925ec65cf56396ba` ／ 9,494 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/result.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/bridge/eos_decoupled_web_kl/result.json) ／ SHA256: `c09fcaba4d3ec6450607bb84d3f38db506cb452292145d7ea1b69b41faafc28f` ／ 186,335 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 59 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0000.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0000.json) ／ SHA256: `3a2bc0131a27f33b0686ba5fd01ce95bccea3cf702b08cae23d8efde326cbde1` ／ 7,975 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0016.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0016.json) ／ SHA256: `64e6743180521e4e7c6d9eba3d27588a91604d6f5e12421e108f7a3a13801a33` ／ 8,324 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0032.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0032.json) ／ SHA256: `b2a6e1b5689ff1688ed02f208673bfaf0e771c896be638fa6cd37e23309e8d27` ／ 6,984 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0048.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0048.json) ／ SHA256: `13e9ae8d956813e37ead257c683f53fd095b09ce00b219a8778b3ec138a90a95` ／ 8,160 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0064.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0064.json) ／ SHA256: `a2753b05f6bf57e3f621dd122d97972f7818477f71e39825f5a0f137f59904bc` ／ 8,499 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0080.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0080.json) ／ SHA256: `b2b4882ed45feb7d4814338049dde1c5cea782d613943842fdd37010ad701fea` ／ 7,085 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0096.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0096.json) ／ SHA256: `00c10f0c2b0865f277df53da4b3c4461f46124b7fb36391ef568b834aa5aa6ba` ／ 8,069 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0112.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0112.json) ／ SHA256: `4ab50dcc8778e68b811d25d11f43f59fb0d7ab27e5fe848880d59df32cf443ed` ／ 8,275 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0128.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0128.json) ／ SHA256: `6c48aea466707eb982021ba31fddc5bbd36c4a5ae7575c3e2d866d93764a6563` ／ 7,087 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0144.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0144.json) ／ SHA256: `5a88aa877422c2b4ae6d8f6c809c7906a63b8c28a3c6ce1103e5f5a2e9ecdf5f` ／ 8,183 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0160.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0160.json) ／ SHA256: `f555802cf1a45e23bf91b9ab808bda23c3a83464f6129fd2641f68d1b3aab644` ／ 8,624 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0176.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0176.json) ／ SHA256: `56af5a5fc96680615b4f1e452765482c4fa6f05e4cf847022430b19511bc5076` ／ 6,919 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0192.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0192.json) ／ SHA256: `84c8eb9bf421bdb1ff027fd9042380671e73542949b7c1a924fb5ad49b1b53d9` ／ 8,168 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>

<details>
<summary>reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0208.json — None</summary>

[原記録](../../reports/phase6/eos-decoupled-web-kl-comparison-20261006/transfer/retention/eos_decoupled_web_kl/0208.json) ／ SHA256: `b6e70327057b58ea16c9fb302c752fd76a29e05e1f8a1402c1a84e3e7453f3ef` ／ 8,517 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |

</details>
