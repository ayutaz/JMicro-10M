# 実行管理・後続準備・その他 — 16/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/progress-result.json) ／ SHA256: `57acfa6c9f1b86e726423670618089df79bf218e7107741fc344560209720ec2` ／ 1,907,972 bytes

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
| checkpoints.hard_body_web_replay.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/checkpoint-00323503.pt" |
| checkpoints.hard_body_web_replay.checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| checkpoints.hard_body_web_replay.binding.config_sha256 | "69f48a2e7c2e6de551cc164d3c12b1a2c42df64679d0c35e97ce0f696b79f872" |
| checkpoints.hard_body_web_replay.binding.arm | "hard_body_web_replay" |
| checkpoints.hard_body_web_replay.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.hard_body_web_replay.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.hard_body_web_replay.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.hard_body_web_replay.binding.teacher_goals.web | 75000000 |
| checkpoints.hard_body_web_replay.binding.teacher_goals.story | 5000000 |
| checkpoints.hard_body_web_replay.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.hard_body_web_replay.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.hard_body_web_replay.binding.optimizer_policy | "inherit" |
| checkpoints.hard_body_web_replay.binding.peak_lr | 1e-05 |
| checkpoints.hard_body_web_replay.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.hard_body_web_replay.binding.study_kind | "historical_parent_staged_CE_parent_mass_weighted_gold_Web_body_replay_100M" |
| checkpoints.hard_body_web_replay.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted parent-mass-weighted gold Web body CE replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| checkpoints.hard_body_web_replay.binding.outcome_weight | 1 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.kind | "frozen-parent-mass-weighted-gold-Web-body-non-EOS-CE-v1" |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.direction | "gold_to_student" |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.temperature | 1.0 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.coefficient | 1.0 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.every_completed_update | 1 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.reference_context | 1024 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.reference_batch | 8 |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.masked_targets | "Gold labels&gt;=8; ignore EOS/BOS/role/padding target positions. Exclude EOS3 only from student vocabulary; retain all other vocabulary IDs." |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.reference_teacher | "Immutable actual historical10.5B parent supplies detached non-EOS probability mass only, not soft targets." |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.hard_body_web_replay.binding.auxiliary_policy.objective | "Mean over valid body positions: (1-parent_P(EOS3))*(-log student_P(gold／non-EOS)). Do not divide by probability mass." |
| checkpoints.hard_body_web_replay.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.hard_body_web_replay.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.hard_body_web_replay.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.hard_body_web_replay.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.hard_body_web_replay.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.hard_body_web_replay.update | 323503 |
| checkpoints.hard_body_web_replay.tokens | 10600546304 |
| checkpoints.hard_body_web_replay.supervised_tokens | 10577786961 |
| checkpoints.hard_body_web_replay.additional_supervised_tokens | 100000000 |
| checkpoints.hard_body_web_replay.additional_input_tokens | 100532224 |
| checkpoints.hard_body_web_replay.source_teachers.web | 75000000 |
| checkpoints.hard_body_web_replay.source_teachers.story | 5000000 |
| checkpoints.hard_body_web_replay.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.hard_body_web_replay.source_teachers.conditional_textbook | 10000000 |
| checkpoints.hard_body_web_replay.source_eos.web | 159170 |
| checkpoints.hard_body_web_replay.source_eos.story | 38240 |
| checkpoints.hard_body_web_replay.source_eos.ordinary_textbook | 74183 |
| checkpoints.hard_body_web_replay.source_eos.conditional_textbook | 234328 |
| checkpoints.hard_body_web_replay.source_input_tokens.web | 75183104 |
| checkpoints.hard_body_web_replay.source_input_tokens.story | 5039104 |
| checkpoints.hard_body_web_replay.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.hard_body_web_replay.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.hard_body_web_replay.source_focus_teachers.web | 0 |
| checkpoints.hard_body_web_replay.source_focus_teachers.story | 0 |
| checkpoints.hard_body_web_replay.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.hard_body_web_replay.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.hard_body_web_replay.focus_teacher_tokens | 1407427 |
| checkpoints.hard_body_web_replay.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.hard_body_web_replay.weighted_teacher_mass | 100000000 |
| checkpoints.hard_body_web_replay.outcome_weight | 1 |
| checkpoints.hard_body_web_replay.training_seconds | 280.8731656332384 |
| checkpoints.hard_body_web_replay.completed_at | "2026-10-06T07:49:27.471709Z" |
| checkpoints.hard_body_web_replay.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| checkpoints.hard_body_web_replay.reference_replay.kind | "frozen-parent-mass-weighted-gold-Web-body-non-EOS-CE-v1" |
| checkpoints.hard_body_web_replay.reference_replay.batch | 8 |
| checkpoints.hard_body_web_replay.reference_replay.context | 1024 |
| checkpoints.hard_body_web_replay.reference_replay.initial_cursor.seed | 42 |
| checkpoints.hard_body_web_replay.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.hard_body_web_replay.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.hard_body_web_replay.reference_replay.initial_cursor.context | 1024 |
| checkpoints.hard_body_web_replay.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.hard_body_web_replay.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.hard_body_web_replay.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.hard_body_web_replay.reference_replay.stream.sampler.seed | 42 |
| checkpoints.hard_body_web_replay.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.hard_body_web_replay.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.hard_body_web_replay.reference_replay.stream.sampler.context | 1024 |
| checkpoints.hard_body_web_replay.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.hard_body_web_replay.reference_replay.updates | 3068 |
| checkpoints.hard_body_web_replay.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.hard_body_web_replay.reference_replay.body_positions | 25026383 |
| checkpoints.hard_body_web_replay.reference_replay.ignored_positions | 106673 |
| checkpoints.hard_body_web_replay.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.hard_body_web_replay.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.hard_body_web_replay.reference_input_tokens | 25133056 |
| checkpoints.hard_body_web_replay.reference_hard_body_target_positions | 25026383 |
| checkpoints.hard_body_web_replay.combined_hard_teacher_positions | 125026383 |
| checkpoints.hard_body_web_replay.combined_student_physical_input_tokens | 125665280 |
| checkpoints.hard_body_web_replay.auxiliary_policy.kind | "frozen-parent-mass-weighted-gold-Web-body-non-EOS-CE-v1" |
| checkpoints.hard_body_web_replay.auxiliary_policy.direction | "gold_to_student" |
| checkpoints.hard_body_web_replay.auxiliary_policy.temperature | 1.0 |
| checkpoints.hard_body_web_replay.auxiliary_policy.coefficient | 1.0 |
| checkpoints.hard_body_web_replay.auxiliary_policy.every_completed_update | 1 |
| checkpoints.hard_body_web_replay.auxiliary_policy.reference_context | 1024 |
| checkpoints.hard_body_web_replay.auxiliary_policy.reference_batch | 8 |
| checkpoints.hard_body_web_replay.auxiliary_policy.masked_targets | "Gold labels&gt;=8; ignore EOS/BOS/role/padding target positions. Exclude EOS3 only from student vocabulary; retain all other vocabulary IDs." |
| checkpoints.hard_body_web_replay.auxiliary_policy.reference_teacher | "Immutable actual historical10.5B parent supplies detached non-EOS probability mass only, not soft targets." |
| checkpoints.hard_body_web_replay.auxiliary_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.hard_body_web_replay.auxiliary_policy.objective | "Mean over valid body positions: (1-parent_P(EOS3))*(-log student_P(gold／non-EOS)). Do not divide by probability mass." |
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
| evaluations.hard_body_web_replay.binding.teacher_goals.web | 75000000 |
| evaluations.hard_body_web_replay.binding.teacher_goals.story | 5000000 |
| evaluations.hard_body_web_replay.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.hard_body_web_replay.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.hard_body_web_replay.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.hard_body_web_replay.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted parent-mass-weighted gold Web body CE replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| evaluations.hard_body_web_replay.binding.auxiliary_policy.every_completed_update | 1 |
| evaluations.hard_body_web_replay.binding.auxiliary_policy.reference_teacher | "Immutable actual historical10.5B parent supplies detached non-EOS probability mass only, not soft targets." |
| evaluations.hard_body_web_replay.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.hard_body_web_replay.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.hard_body_web_replay.checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| evaluations.hard_body_web_replay.body.documents | 256 |
| evaluations.hard_body_web_replay.body.limit_documents | 256 |
| evaluations.hard_body_web_replay.body.body_nll | 322468.44424152374 |
| evaluations.hard_body_web_replay.body.eos_nll | 503.7431419249624 |
| evaluations.hard_body_web_replay.body.body_bytes | 472055 |
| evaluations.hard_body_web_replay.body.body_tokens | 122343 |
| evaluations.hard_body_web_replay.body.bpb | 0.9855284349290349 |
| evaluations.hard_body_web_replay.body.seconds | 1.5233297260128893 |
| evaluations.hard_body_web_replay.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.hard_body_web_replay.generation.max_new_tokens | 64 |
| evaluations.hard_body_web_replay.greedy_rates.eos | 53 |
| evaluations.hard_body_web_replay.greedy_rates.repetition | 15 |
| evaluations.hard_body_web_replay.greedy_rates.unicode_failure | 0 |
| evaluations.hard_body_web_replay.greedy_rates.role_leak | 0 |
| evaluations.hard_body_web_replay.greedy_rates.empty | 0 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.ci95 | [0.515625, 0.6197916666666666] |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6354166666666666] |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5826086956521739 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.mcc | 0.16724840200141816 |
| evaluations.hard_body_web_replay.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.hard_body_web_replay.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8157099697885196] |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6978851963746223, 0.7915407854984894] |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.hard_body_web_replay.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.point | 0.3378016085790885 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.ci95 | [0.3109919571045576, 0.3646112600536193] |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.primary.hard_accuracy | 0.3378016085790885 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.30831099195710454 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28150134048257375, 0.3351206434316354] |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.30831099195710454 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3072216446479012 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.mcc | 0.13613176056156598 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.hard_body_web_replay.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.hard_body_web_replay.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.hard_body_web_replay.diagnostics.semantic_both_contexts.correct | 20 |
| evaluations.hard_body_web_replay.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.hard_body_web_replay.memory.maximum_observed_reserved_bytes | 13046382592 |
| evaluations.hard_body_web_replay.protected_test_used | false |
| mechanism_cached.checkpoints.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/eos_decoupled_web_kl/training/checkpoint-00323503.pt" |
| mechanism_cached.checkpoints.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.checkpoints.binding.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| mechanism_cached.checkpoints.binding.arm | "eos_decoupled_web_kl" |
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
| mechanism_cached.checkpoints.binding.study_kind | "historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M" |
| mechanism_cached.checkpoints.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| mechanism_cached.checkpoints.binding.outcome_weight | 1 |
| mechanism_cached.checkpoints.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| mechanism_cached.checkpoints.binding.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.binding.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| mechanism_cached.checkpoints.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.checkpoints.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
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
| mechanism_cached.checkpoints.training_seconds | 287.5748953077127 |
| mechanism_cached.checkpoints.completed_at | "2026-10-06T07:25:26.363788Z" |
| mechanism_cached.checkpoints.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| mechanism_cached.checkpoints.reference_replay.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
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
| mechanism_cached.checkpoints.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| mechanism_cached.checkpoints.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| mechanism_cached.checkpoints.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.checkpoints.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
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
| mechanism_cached.evaluations.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.evaluations.body.documents | 256 |
| mechanism_cached.evaluations.body.limit_documents | 256 |
| mechanism_cached.evaluations.body.body_nll | 321651.43452215195 |
| mechanism_cached.evaluations.body.eos_nll | 513.1300341412425 |
| mechanism_cached.evaluations.body.body_bytes | 472055 |
| mechanism_cached.evaluations.body.body_tokens | 122343 |
| mechanism_cached.evaluations.body.bpb | 0.9830314888729699 |
| mechanism_cached.evaluations.body.seconds | 1.4468623629945796 |
| mechanism_cached.evaluations.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| mechanism_cached.evaluations.generation.max_new_tokens | 64 |
| mechanism_cached.evaluations.greedy_rates.eos | 44 |
| mechanism_cached.evaluations.greedy_rates.repetition | 20 |
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
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5520833333333334 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.59375] |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.count | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5520833333333334 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5508649766075508 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.mcc | 0.10473644811127698 |
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
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7190332326283988 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6706948640483383, 0.7673716012084593] |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.count | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7190332326283988 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4182776801405975 |
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
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.ci95 | [0.3127792672028597, 0.36642091152815] |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
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
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30903529199025803 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.mcc | 0.13825571947644602 |
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
| mechanism_cached.evaluations.diagnostics.semantic_both_contexts.correct | 19 |
| mechanism_cached.evaluations.memory.maximum_observed_allocated_bytes | 315223040 |
| mechanism_cached.evaluations.memory.maximum_observed_reserved_bytes | 13046382592 |
| mechanism_cached.evaluations.protected_test_used | false |
| mechanism_cached.transfer.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.transfer.checks.weights_unchanged | true |
| mechanism_cached.transfer.checks.no_gradients | true |
| mechanism_cached.transfer.checks.eval_mode | true |
| mechanism_cached.transfer.checks.RNG_restored | true |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 59 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| mechanism_cached.transfer.optimizer_updates | 0 |
| mechanism_cached.transfer.scientific_teacher_tokens | 0 |
| mechanism_cached.transfer.protected_test_used | false |
| mechanism_cached.transfer.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| mechanism_cached.retention.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.retention.checks.weights_unchanged | true |
| mechanism_cached.retention.checks.no_gradients | true |
| mechanism_cached.retention.checks.eval_mode | true |
| mechanism_cached.retention.checks.RNG_restored | true |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 33 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 27 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.625 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 86 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 33 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
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
| transfer.hard_body_web_replay.checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| transfer.hard_body_web_replay.checks.weights_unchanged | true |
| transfer.hard_body_web_replay.checks.no_gradients | true |
| transfer.hard_body_web_replay.checks.eval_mode | true |
| transfer.hard_body_web_replay.checks.RNG_restored | true |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.61328125 |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.all128.both_correct | 40 |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.46875 |
| transfer.hard_body_web_replay.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 45 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 95 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 36 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| transfer.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 48 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 67 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 93 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.453125 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 7 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| transfer.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 31 |
| transfer.hard_body_web_replay.optimizer_updates | 0 |
| transfer.hard_body_web_replay.scientific_teacher_tokens | 0 |
| transfer.hard_body_web_replay.protected_test_used | false |
| transfer.hard_body_web_replay.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
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
| retention.hard_body_web_replay.checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| retention.hard_body_web_replay.checks.weights_unchanged | true |
| retention.hard_body_web_replay.checks.no_gradients | true |
| retention.hard_body_web_replay.checks.eval_mode | true |
| retention.hard_body_web_replay.checks.RNG_restored | true |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5625 |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.all128.both_correct | 20 |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6171875 |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 16 |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.hard_body_web_replay.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 4 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.57421875 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 22 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 103 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 18 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 45 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| retention.hard_body_web_replay.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58984375 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 26 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 99 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.640625 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention.hard_body_web_replay.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| retention.hard_body_web_replay.optimizer_updates | 0 |
| retention.hard_body_web_replay.scientific_teacher_tokens | 0 |
| retention.hard_body_web_replay.protected_test_used | false |
| retention.hard_body_web_replay.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/review.json — gold_Web_replay_CE100M_all80_and_cached_stagedCE100M_reviewed</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/review.json) ／ SHA256: `cb16c30b77a42729eb62fca1686b52b53a081333591d0149775218ee2d2c139d` ／ 14,525 bytes

| 原キー | 保存値 |
|---|---|
| status | "gold_Web_replay_CE100M_all80_and_cached_stagedCE100M_reviewed" |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | true |
| mechanism_comparison.checks.repetition_nonworsening | true |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
| mechanism_summary.BPB | 0.9830314888729699 |
| mechanism_summary.rates.eos | 44 |
| mechanism_summary.rates.repetition | 20 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 58 |
| mechanism_summary.relevance2 | 49 |
| mechanism_summary.coherent | 11 |
| mechanism_summary.appropriate | 28 |
| mechanism_summary.notes_sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| previous_related_study_GPU_seconds | 795.3523048920615 |
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
| summaries.hard_body_web_replay.BPB | 0.9855284349290349 |
| summaries.hard_body_web_replay.rates.eos | 53 |
| summaries.hard_body_web_replay.rates.repetition | 15 |
| summaries.hard_body_web_replay.rates.unicode_failure | 0 |
| summaries.hard_body_web_replay.rates.role_leak | 0 |
| summaries.hard_body_web_replay.rates.empty | 0 |
| summaries.hard_body_web_replay.grammar2 | 45 |
| summaries.hard_body_web_replay.relevance2 | 56 |
| summaries.hard_body_web_replay.coherent | 17 |
| summaries.hard_body_web_replay.appropriate | 34 |
| summaries.hard_body_web_replay.notes_sha256 | "b856804788da0b67ebf95ba5dd76787e9b644e1322bf322a7a56235a6113fcc5" |
| summaries.hard_body_web_replay.additional_teacher_tokens | 100000000 |
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
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.all_four_source_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| reference_accounting.reference_hard_body_teacher_tokens | 25026383 |
| reference_accounting.combined_hard_teacher_positions | 125026383 |
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
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.all128.accuracy | 0.61328125 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.all128.both_correct | 40 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.accuracy | 0.46875 |
| transfer_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.both_correct | 7 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.both_correct | 45 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.aligned_context_margin_shift | 95 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.both_correct | 36 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| transfer_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.both_correct | 48 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.same_unique_candidate | 67 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 93 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.accuracy | 0.453125 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.both_correct | 7 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| transfer_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 31 |
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
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.all128.accuracy | 0.5625 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.all128.both_correct | 20 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.accuracy | 0.6171875 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.lexical_holdout.both_correct | 16 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention_aggregates.hard_body_web_replay.sum_log_likelihood.structural_holdout.both_correct | 4 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.accuracy | 0.57421875 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.both_correct | 22 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.same_unique_candidate | 103 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.both_correct | 18 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 45 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| retention_aggregates.hard_body_web_replay.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.accuracy | 0.58984375 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.both_correct | 26 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.same_unique_candidate | 99 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.640625 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention_aggregates.hard_body_web_replay.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| new_scientific_auxiliary_hard_body_teacher_tokens | 25026383 |
| new_scientific_combined_hard_teacher_positions | 125026383 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 349.4322593070101 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_hard_positions | 326339 |
| verification_GPU_seconds | 28.81082727899775 |
| prior_probe_GPU_seconds | 0.0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Gold words replace conditional soft distributions on identical replay windows, with identical frozen parent mass weights and non-EOS vocabulary. Main100M ordinary CE plus separately counted auxiliary gold-body teachers; not equal supervision/information to conditionalKL or plain stagedCE. New corpus0, train overlaps. One seed/nonblind repeated fixeddev; independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0000.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0000.json) ／ SHA256: `ebd5d6d4d1b542873ae88fc0ed62c50c4e03fa14221a27c44d600968fefc7bf5` ／ 9,916 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0016.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0016.json) ／ SHA256: `5365833f2ef2f25d67210e41b2fba7a222ca6bbca765f7b0e11daaff57687ae9` ／ 9,572 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0032.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0032.json) ／ SHA256: `33181306b209c722bb380536213df289fd160bc9cf73758edbdcc914e68943b5` ／ 10,199 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0048.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0048.json) ／ SHA256: `cf6dc934a853ad3d907375d2b544d7b57d9f092dd96e1f5d28db85f3ad2feb4d` ／ 9,489 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0064.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0064.json) ／ SHA256: `0e860916081013ffaa30b4840541e4f7edafec45f9001b46b3ce974fd46dc828` ／ 10,293 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0080.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0080.json) ／ SHA256: `3ec722505ea466b14e7d89e36781d5a96d78454b98b0028bfcf2a947a671bb35` ／ 9,682 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0096.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0096.json) ／ SHA256: `02d9b8ed530e1f29b3a04f4d2ae8ebdd7d59c3af3649ab8557620ca35817a238` ／ 9,759 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0112.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0112.json) ／ SHA256: `8506886415f0e86f23453146604a637191369a44e16a1d000c339e5dbe463174` ／ 10,123 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0128.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0128.json) ／ SHA256: `4acd1a26e38276c2e4edd25fe44abf167238ce2940d1a52bd426807ab2e5f505` ／ 9,786 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0144.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0144.json) ／ SHA256: `e6fcba478d5ad15fe9bbbcb66cd1072496cb67d2fb0571234294e83fb2a0000a` ／ 9,852 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0160.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0160.json) ／ SHA256: `57eaecd9a3a1018d898246cc4428f0ee472026efd73c325c28e1aad4917d3ecf` ／ 10,121 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0176.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0176.json) ／ SHA256: `9e999769ba8431c254edc42f6e2a082b480e2876dfb35f1154113c4823d7515a` ／ 9,959 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0192.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0192.json) ／ SHA256: `520a83eb1927b0f544d985f80c42e7697518f7d256332488aba5cc203b23f021` ／ 9,885 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0208.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0208.json) ／ SHA256: `41b5ef7bd6a654cf8d743b101a706e8d415c56a179d60d3b92818a10ce1ff770` ／ 9,596 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0224.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0224.json) ／ SHA256: `cbdba9339e489adf58ba37d8fba352626161862f5e7f5e2f3dc282ba91ccc1f9` ／ 9,798 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0240.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0240.json) ／ SHA256: `e6520922f5335606d4e25fec8d8a83553b79ef1a726be33fe018da4bb4589895` ／ 9,588 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0256.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0256.json) ／ SHA256: `82b0d2dfd500dadcbec55ce065e8f7ed021dd74feff4c74d2de976255899a169` ／ 9,589 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0272.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0272.json) ／ SHA256: `c7873aa859ccac3fec8d8379e9c4e930787bfd8e4cc35f1b11dbd0faee5169aa` ／ 9,572 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0288.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0288.json) ／ SHA256: `1072e3e7767d983e5c5807c6865564cc2d33055bff7593e380192bc85b534a3b` ／ 9,583 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0304.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0304.json) ／ SHA256: `da5f7783b3e897ed0c55228eb253a4fb2befc9dff5b30fb0dc0b2ffe3cfa5ad9` ／ 9,761 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0320.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0320.json) ／ SHA256: `aa0e69373410a3db39c7a0bd38fa95fc732cc8e2a45e2842a76bddd3369fae70` ／ 9,303 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0336.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0336.json) ／ SHA256: `785e8fd3c6d603e54922217f209d94bf99ae01d51eeb2ef888641d3f9b313512` ／ 9,391 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0352.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0352.json) ／ SHA256: `698b0e20af6d9a33b4a70ab76bd8d9dddbe8c04c3caeb72bd9d0cff027685a22` ／ 9,764 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0368.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0368.json) ／ SHA256: `b10d9bd20bd04b6dae615b6644bf4ea3c057ba76d1901c843e6876864d727c7a` ／ 9,511 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0384.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0384.json) ／ SHA256: `ecc92bafd05c0f252177aae89048b953a54d04b0bc1654326a892947b0f83921` ／ 9,843 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0400.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0400.json) ／ SHA256: `c9031b85ef079151e94c411e15dfd3e7118cfce62b85dab12ffeff109cd30614` ／ 9,481 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0416.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0416.json) ／ SHA256: `48cd627176a9e050b23605bc78b76f1e033ef01c7629bf1def6abd9ba3b0849f` ／ 9,866 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0432.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0432.json) ／ SHA256: `a5735131fc15ff55f097a1c355af92d9e242f7a61e4d10e6be30b530fd655227` ／ 9,319 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0448.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0448.json) ／ SHA256: `60f32fc18ca84a32b4d34f0808d97b3ca89e7a001d6f20bc4d594037310fbaba` ／ 9,566 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0464.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0464.json) ／ SHA256: `ca04152933693875374ccebe369dbe90fdfeaeffc36dd0c5ae77d45144660f37` ／ 9,406 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0480.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0480.json) ／ SHA256: `30266e019698cc232aeb42caeafc5e3cb160916ccabe9840e4e5483dcd98e592` ／ 9,410 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0496.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/0496.json) ／ SHA256: `0bfc4f93a786419630f616430451978414194e0baf8e0bbb302f82b866bd8708` ／ 9,482 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/result.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/bridge/hard_body_web_replay/result.json) ／ SHA256: `f8ccb4eb4fe200c9adaab4475cb40562791e9e3f585ddd9e49f2dcc5562975a0` ／ 186,608 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.61328125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 40 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.46875 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 45 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 95 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 36 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 48 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 67 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 93 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 41 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 62 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.453125 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 7 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 31 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0000.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0000.json) ／ SHA256: `a57cf8273eb1dc0d50a66528e2c55d0759057396a90aa40dbfc801110b315f42` ／ 7,963 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0016.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0016.json) ／ SHA256: `7a5a063c35975c8372425f7e096db06c25f313d81d1283009c8be8aa40c3000f` ／ 8,311 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0032.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0032.json) ／ SHA256: `dacb63621ed31c0422049d6bc8906812be954622365dc2e0f53257e8c19f7e0e` ／ 6,971 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0048.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0048.json) ／ SHA256: `35e5b1732792c9b63c5a7ff70be818d73434a156f42376830f8069d48f8339e3` ／ 8,132 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0064.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0064.json) ／ SHA256: `fb26a29308312f9f947ef543d01f872d8bf8af423847f8361e9260fc529f9265` ／ 8,494 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0080.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0080.json) ／ SHA256: `6ed024b6441141a1f2caadd5cd933e3eb30fd96f4cfcd46b51165bc5ef6c4a5b` ／ 7,065 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0096.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0096.json) ／ SHA256: `60f5c3dc0f1447838a1ffa39ae1469ffa175bbbb034d543d65e8d1d584a12cd7` ／ 8,061 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0112.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0112.json) ／ SHA256: `9865f5cc548768a7867f4205cee0d001c12883bfd3811f744c98a219b47e7b18` ／ 8,234 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0128.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0128.json) ／ SHA256: `96d3c80345d9aec6e920310de1d8dd19c1e5684e8abd4ffd4e2ed485d3814d5b` ／ 7,041 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0144.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0144.json) ／ SHA256: `824cc510b273ddedd09a56b0b6f276c10cc06c84f9168ec71e72492ce748d07e` ／ 8,172 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0160.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0160.json) ／ SHA256: `ae038696075ee7404e2cb0a43691eae66db0b766a257da74f9acf917ae013eba` ／ 8,592 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0176.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0176.json) ／ SHA256: `72183387a5176d4b0b9a4ed7f7a2232b1fb437af83c8d3f8f9ef4421b3bd72c2` ／ 6,907 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0192.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0192.json) ／ SHA256: `b210755cc31720058c5a0fe3464cb347e5bfa11731eddbb540731c27631f5d32` ／ 8,151 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0208.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0208.json) ／ SHA256: `d3530090e7da7a4de58ab3b3194bb1240a9f74ee8f415b47a020d52871eefd85` ／ 8,492 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0224.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0224.json) ／ SHA256: `c8af574321f14011c5c9ff834cf96ef59f33e8fedf6d8e7fd88da2fa2eda3b89` ／ 7,068 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0240.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0240.json) ／ SHA256: `ed2825dc9a814c3d4316f2732aeac874628fb6f2319c7d09ccee3961a54f96fe` ／ 8,306 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0256.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0256.json) ／ SHA256: `4ae58efc283037707b47367b84efccffe0e23ad88d518af85020cd9f51e4d7b3` ／ 8,237 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0272.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0272.json) ／ SHA256: `df68d4d963229a85ae7f2765db2c2d290ae5bebc2e109432267dee8f5022a28c` ／ 8,424 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0288.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0288.json) ／ SHA256: `2dca80eb2370f48dd3cc519b42759b5cd2316831be4b8f1dfbed97dd72d78bd6` ／ 7,097 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0304.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0304.json) ／ SHA256: `d7defa1486074469b8f5c321cfacae123dc07494090cfbd2a2ba4a5e6bcae632` ／ 8,137 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0320.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0320.json) ／ SHA256: `bdf27ec78ee51836d6c542f28470da8c7494ea718d779f908816a24811025480` ／ 8,586 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0336.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0336.json) ／ SHA256: `0a4e70984baa9268c67d1bdf831f34dabf0e59b3b6af532e5b938e2f36b5f436` ／ 7,094 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0352.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0352.json) ／ SHA256: `4ac956cfb6ea5ac08e7022c7de90d7b36e8ea59fa789a2572b29b4d1f6e8ea52` ／ 8,150 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0368.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0368.json) ／ SHA256: `6e915e3993c73ac5db8fba22ed3c0de865d2b62cb7dee5fedbef03f74c973986` ／ 8,161 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0384.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0384.json) ／ SHA256: `cc6f4c7dad1ec22a20f75d5dccdd4d056595dadc4b55723424f9387ed1743eb5` ／ 7,003 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0400.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0400.json) ／ SHA256: `f8731ce5d4f63abd8629085e84d5dd97cbb1799d3574d32946e1713403fb955a` ／ 8,140 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0416.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0416.json) ／ SHA256: `34eebbd372ec0f191ca29b1ee874b6453e6e4449353182d3b74a4826b6006c6a` ／ 8,182 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0432.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0432.json) ／ SHA256: `70d716cdb6234d319711a4cdde156e7309d36030cb71164479272fde8f344eee` ／ 7,094 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0448.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0448.json) ／ SHA256: `c037f05bc9b73be79a58a150d3bc6d11449f02c18c37af126aaab1851ff1012e` ／ 8,071 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0464.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0464.json) ／ SHA256: `6e8e8e67fc94028370eca764087ac132f228ab0485eaeb67ed8b48e080fe5873` ／ 8,346 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0480.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0480.json) ／ SHA256: `6c9bee2d1a9d45ef5eb706bc0121662546b3ad0d24b6df0b5a0ff7db3cc9ead6` ／ 7,010 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0496.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/0496.json) ／ SHA256: `ea3de09b76b02cadba4e1b9083c8cc1310cfc1e919da52b6cb669cec69837a39` ／ 8,052 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/result.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-comparison-20261006/transfer/retention/hard_body_web_replay/result.json) ／ SHA256: `9f48a670a9bdedea9d50d521b34fbd375d0b5dc2c990bcfcaef2ab7d5647b1ce` ／ 183,237 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 20 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6171875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 16 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.57421875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 22 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 103 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 100 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 18 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 45 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58984375 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 26 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 99 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.640625 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 49 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-probe-launcher-20261006/launcher.json) ／ SHA256: `581f5408b261850cef78652815754eef97d66b2dfdc89c75e893354b42b616ca` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/hard-body-web-replay-probe-launcher-20261006/result.json) ／ SHA256: `a8e112bb785069d0eefb0990293ab02cb4e674473ed02122ec964db524499de6` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-train-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/hard-body-web-replay-train-launcher-20261006/launcher.json) ／ SHA256: `723b9bd52027c441368f79ec9cf48cc1a502569aff5ea986c8fdd8daa6850171` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/hard-body-web-replay-train-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/hard-body-web-replay-train-launcher-20261006/result.json) ／ SHA256: `2ef8011b2d9a67f755a0bdb3f1b5d10281024c1110c2674b7bb5cf08dc974b21` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/hard_body_web_replay_comparison_completion.json — gold_body_replay_terminal_pilot_fully_reviewed</summary>

[原記録](../../reports/phase6/hard_body_web_replay_comparison_completion.json) ／ SHA256: `b6d93193c07f1f1c82df3efd50a7997ff1190aeed3efeb8b992b1af39d266338` ／ 8,499 bytes

| 原キー | 保存値 |
|---|---|
| status | "gold_body_replay_terminal_pilot_fully_reviewed" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
| ordinary_CE_teacher_tokens | 100000000 |
| main_input_tokens | 100532224 |
| auxiliary_gold_body_teacher_positions | 25026383 |
| combined_hard_teacher_positions | 125026383 |
| reference_input_tokens | 25133056 |
| reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| reference_downweighted_EOS_probability_mass | 44490.3701171875 |
| combined_student_input_tokens | 125665280 |
| verification_CE_teacher_tokens | 1307967 |
| verification_reference_input_tokens | 327680 |
| verification_reference_body_positions | 326339 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| training_seconds | 280.8731656332384 |
| science_GPU_seconds | 349.4322593070101 |
| verification_GPU_seconds | 28.81082727899775 |
| current_study_all_GPU_seconds | 378.24308658600785 |
| current_study_GPU_ceiling_seconds | 900 |
| previous_related_study_GPU_seconds | 795.3523048920615 |
| cumulative_related_GPU_seconds | 1173.5953914780694 |
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
| summaries.hard_body_web_replay.BPB | 0.9855284349290349 |
| summaries.hard_body_web_replay.rates.eos | 53 |
| summaries.hard_body_web_replay.rates.repetition | 15 |
| summaries.hard_body_web_replay.rates.unicode_failure | 0 |
| summaries.hard_body_web_replay.rates.role_leak | 0 |
| summaries.hard_body_web_replay.rates.empty | 0 |
| summaries.hard_body_web_replay.grammar2 | 45 |
| summaries.hard_body_web_replay.relevance2 | 56 |
| summaries.hard_body_web_replay.coherent | 17 |
| summaries.hard_body_web_replay.appropriate | 34 |
| summaries.hard_body_web_replay.notes_sha256 | "b856804788da0b67ebf95ba5dd76787e9b644e1322bf322a7a56235a6113fcc5" |
| summaries.hard_body_web_replay.additional_teacher_tokens | 100000000 |
| mechanism_summary.BPB | 0.9830314888729699 |
| mechanism_summary.rates.eos | 44 |
| mechanism_summary.rates.repetition | 20 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 58 |
| mechanism_summary.relevance2 | 49 |
| mechanism_summary.coherent | 11 |
| mechanism_summary.appropriate | 28 |
| mechanism_summary.notes_sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | true |
| mechanism_comparison.checks.repetition_nonworsening | true |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
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
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.all_four_source_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| reference_accounting.reference_hard_body_teacher_tokens | 25026383 |
| reference_accounting.combined_hard_teacher_positions | 125026383 |
| reference_accounting.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| reference_accounting.frozen_parent_teacher_digest_verified | true |
| reference_accounting.reference_input_tokens | 25133056 |
| reference_accounting.main_ordinary_CE_teacher_tokens | 100000000 |
| reference_accounting.combined_student_physical_input_tokens | 125665280 |
| reference_accounting.newly_prepared_source_tokens | 0 |
| paired_likelihood.against_staged_CE.body_NLL_better | 256 |
| paired_likelihood.against_staged_CE.body_NLL_worse | 0 |
| paired_likelihood.against_staged_CE.gold_EOS_NLL_better | 55 |
| paired_likelihood.against_staged_CE.gold_EOS_NLL_worse | 201 |
| paired_likelihood.against_staged_CE.body_bytes | 472055 |
| paired_likelihood.against_staged_CE.body_tokens | 122343 |
| paired_likelihood.against_staged_CE.GPU_seconds | 0 |
| paired_likelihood.against_conditional_KL.body_NLL_better | 53 |
| paired_likelihood.against_conditional_KL.body_NLL_worse | 203 |
| paired_likelihood.against_conditional_KL.gold_EOS_NLL_better | 160 |
| paired_likelihood.against_conditional_KL.gold_EOS_NLL_worse | 96 |
| paired_likelihood.against_conditional_KL.body_bytes | 472055 |
| paired_likelihood.against_conditional_KL.body_tokens | 122343 |
| paired_likelihood.against_conditional_KL.GPU_seconds | 0 |
| eligible_for_final_Base_validation | false |
| newly_prepared_source_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Repeated fixeddev/nonblind one learned seed. Same main/replay windows and parent mass weights; real gold-word targets replace soft conditional distributions, so supervision/information differs even with same input exposure. No new corpus. Original stronger stagedCE is mandatory quality control; improvement over failed conditionalKL alone cannot qualify Base." |

</details>
