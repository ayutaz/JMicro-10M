# 実行管理・後続準備・その他 — 25/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/compare-result.json — web_KL_CE100M_and_cached_stagedCE100M_complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/compare-result.json) ／ SHA256: `5f0d6cb280e34259b88e41b0628f3d6e9bc5c84e012060a4663c4ba4bcedcb99` ／ 1,271,226 bytes

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
| checkpoints.web_kl.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v3-20261006/web_kl/training/checkpoint-00323503.pt" |
| checkpoints.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| checkpoints.web_kl.binding.config_sha256 | "60fcb3e6236f66bcdea397c09cc0f927212a1e3e3dbe94e23c6ff2a7837db0a9" |
| checkpoints.web_kl.binding.arm | "web_kl" |
| checkpoints.web_kl.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.web_kl.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.web_kl.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.web_kl.binding.teacher_goals.web | 75000000 |
| checkpoints.web_kl.binding.teacher_goals.story | 5000000 |
| checkpoints.web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.web_kl.binding.optimizer_policy | "inherit" |
| checkpoints.web_kl.binding.peak_lr | 1e-05 |
| checkpoints.web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.web_kl.binding.study_kind | "historical_parent_staged_CE_frozen_Web_KL_100M" |
| checkpoints.web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| checkpoints.web_kl.binding.outcome_weight | 1 |
| checkpoints.web_kl.binding.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.binding.KL_policy.direction | "parent_to_student" |
| checkpoints.web_kl.binding.KL_policy.temperature | 1.0 |
| checkpoints.web_kl.binding.KL_policy.coefficient | 1.0 |
| checkpoints.web_kl.binding.KL_policy.every_completed_update | 1 |
| checkpoints.web_kl.binding.KL_policy.reference_context | 1024 |
| checkpoints.web_kl.binding.KL_policy.reference_batch | 8 |
| checkpoints.web_kl.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| checkpoints.web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.web_kl.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.web_kl.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.web_kl.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.web_kl.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.web_kl.update | 323503 |
| checkpoints.web_kl.tokens | 10600546304 |
| checkpoints.web_kl.supervised_tokens | 10577786961 |
| checkpoints.web_kl.additional_supervised_tokens | 100000000 |
| checkpoints.web_kl.additional_input_tokens | 100532224 |
| checkpoints.web_kl.source_teachers.web | 75000000 |
| checkpoints.web_kl.source_teachers.story | 5000000 |
| checkpoints.web_kl.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.web_kl.source_teachers.conditional_textbook | 10000000 |
| checkpoints.web_kl.source_eos.web | 159170 |
| checkpoints.web_kl.source_eos.story | 38240 |
| checkpoints.web_kl.source_eos.ordinary_textbook | 74183 |
| checkpoints.web_kl.source_eos.conditional_textbook | 234328 |
| checkpoints.web_kl.source_input_tokens.web | 75183104 |
| checkpoints.web_kl.source_input_tokens.story | 5039104 |
| checkpoints.web_kl.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.web_kl.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.web_kl.source_focus_teachers.web | 0 |
| checkpoints.web_kl.source_focus_teachers.story | 0 |
| checkpoints.web_kl.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.web_kl.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.web_kl.focus_teacher_tokens | 1407427 |
| checkpoints.web_kl.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.web_kl.weighted_teacher_mass | 100000000 |
| checkpoints.web_kl.outcome_weight | 1 |
| checkpoints.web_kl.training_seconds | 255.1444061366201 |
| checkpoints.web_kl.completed_at | "2026-10-06T07:04:02.917166Z" |
| checkpoints.web_kl.reference_replay.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.reference_replay.batch | 8 |
| checkpoints.web_kl.reference_replay.context | 1024 |
| checkpoints.web_kl.reference_replay.initial_cursor.seed | 42 |
| checkpoints.web_kl.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.web_kl.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.web_kl.reference_replay.initial_cursor.context | 1024 |
| checkpoints.web_kl.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.web_kl.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.web_kl.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.web_kl.reference_replay.stream.sampler.seed | 42 |
| checkpoints.web_kl.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.web_kl.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.web_kl.reference_replay.stream.sampler.context | 1024 |
| checkpoints.web_kl.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.web_kl.reference_replay.updates | 3068 |
| checkpoints.web_kl.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.web_kl.reference_replay.body_positions | 25026383 |
| checkpoints.web_kl.reference_replay.ignored_positions | 106673 |
| checkpoints.web_kl.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.web_kl.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.web_kl.reference_input_tokens | 25133056 |
| checkpoints.web_kl.reference_soft_target_body_positions | 25026383 |
| checkpoints.web_kl.combined_student_physical_input_tokens | 125665280 |
| checkpoints.web_kl.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.KL_policy.direction | "parent_to_student" |
| checkpoints.web_kl.KL_policy.temperature | 1.0 |
| checkpoints.web_kl.KL_policy.coefficient | 1.0 |
| checkpoints.web_kl.KL_policy.every_completed_update | 1 |
| checkpoints.web_kl.KL_policy.reference_context | 1024 |
| checkpoints.web_kl.KL_policy.reference_batch | 8 |
| checkpoints.web_kl.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| checkpoints.web_kl.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.web_kl.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
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
| evaluations.web_kl.binding.teacher_goals.web | 75000000 |
| evaluations.web_kl.binding.teacher_goals.story | 5000000 |
| evaluations.web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| evaluations.web_kl.binding.KL_policy.every_completed_update | 1 |
| evaluations.web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| evaluations.web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| evaluations.web_kl.body.documents | 256 |
| evaluations.web_kl.body.limit_documents | 256 |
| evaluations.web_kl.body.body_nll | 321401.2076690197 |
| evaluations.web_kl.body.eos_nll | 635.9188746847212 |
| evaluations.web_kl.body.body_bytes | 472055 |
| evaluations.web_kl.body.body_tokens | 122343 |
| evaluations.web_kl.body.bpb | 0.982266745272942 |
| evaluations.web_kl.body.seconds | 1.3322648800094612 |
| evaluations.web_kl.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.web_kl.generation.max_new_tokens | 64 |
| evaluations.web_kl.greedy_rates.eos | 40 |
| evaluations.web_kl.greedy_rates.repetition | 22 |
| evaluations.web_kl.greedy_rates.unicode_failure | 0 |
| evaluations.web_kl.greedy_rates.role_leak | 0 |
| evaluations.web_kl.greedy_rates.empty | 0 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.point | 0.546875 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.5833333333333334] |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.546875 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5458771715194519 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.mcc | 0.09416472308615167 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.web_kl.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.point | 0.743202416918429 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.ci95 | [0.6978851963746223, 0.7885196374622356] |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.primary.hard_accuracy | 0.743202416918429 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6766616314199396, 0.770392749244713] |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.web_kl.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.point | 0.340035746201966 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.ci95 | [0.3136729222520107, 0.3672922252010724] |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.primary.hard_accuracy | 0.34048257372654156 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30891961343493624 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.mcc | 0.13812773034264442 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.web_kl.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.semantic_both_contexts.correct | 18 |
| evaluations.web_kl.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.web_kl.memory.maximum_observed_reserved_bytes | 13046382592 |
| evaluations.web_kl.protected_test_used | false |
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
| transfer.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| transfer.web_kl.checks.weights_unchanged | true |
| transfer.web_kl.checks.no_gradients | true |
| transfer.web_kl.checks.eval_mode | true |
| transfer.web_kl.checks.RNG_restored | true |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 55 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 67 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.703125 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer.web_kl.optimizer_updates | 0 |
| transfer.web_kl.scientific_teacher_tokens | 0 |
| transfer.web_kl.protected_test_used | false |
| transfer.web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
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
| retention.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| retention.web_kl.checks.weights_unchanged | true |
| retention.web_kl.checks.no_gradients | true |
| retention.web_kl.checks.eval_mode | true |
| retention.web_kl.checks.RNG_restored | true |
| retention.web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 32 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 26 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 34 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.web_kl.optimizer_updates | 0 |
| retention.web_kl.scientific_teacher_tokens | 0 |
| retention.web_kl.protected_test_used | false |
| retention.web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| status | "web_KL_CE100M_and_cached_stagedCE100M_complete" |
| scientific_teacher_tokens | 100000000 |
| total_comparison_teachers | 200000000 |
| reference_input_tokens | 25133056 |
| Base_adopted | false |
| protected_test_used | false |
| GPU_seconds | 333.1955945980153 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/content-packets/web_kl.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/content-packets/web_kl.json) ／ SHA256: `435979ad521e1369ecfcbe2eef4c3c0b41d35b8b12c7409d215599d1eb061293` ／ 108,776 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/job.json) ／ SHA256: `984fe078a15dc81a28071de5d2dec88a2a44ed2efb9af4cdea96ea56130cee46` ／ 918 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 333.1955945980153 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |
| loss | 0.34220007061958313 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/probe/initial-parent-preservation.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/probe/initial-parent-preservation.json) ／ SHA256: `7e3baba2df7953d4543f1aa8dfb9201879154985b785d86eb0d487734d738771` ／ 266 bytes

| 原キー | 保存値 |
|---|---|
| parent_sampler_lineage | true |
| frozen_teacher_weights | true |
| frozen_teacher_eval_no_grad | true |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/probe/job.json) ／ SHA256: `22fbd66cdb6ad981cbb3ad297c856baec5cf6ccd92a4e0d2a956e12989464186` ／ 590 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 28.69179393700324 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/probe/result.json — actual_web_KL_resume_timing_complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/probe/result.json) ／ SHA256: `2ae3dc69455fb14dbfdfb5b74405930eb18b70df61b06de311c51743e974db0e` ／ 83,803 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_web_KL_resume_timing_complete" |
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
| gate.checks.focus_token_digest | true |
| gate.checks.focus_teacher_tokens | true |
| gate.checks.weighted_teacher_mass | true |
| gate.checks.update | true |
| gate.checks.spec | true |
| gate.checks.model_config | true |
| gate.checks.pilot_binding | true |
| gate.checks.study_binding | true |
| gate.checks.KL_state | true |
| gate.checks.history_loss | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_lr | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_ordinary_CE_loss | true |
| gate.checks.history_reference_KL_loss | true |
| gate.checks.history_reference_input_tokens | true |
| gate.checks.history_reference_soft_target_body_positions | true |
| gate.checks.history_reference_ignored_positions | true |
| gate.checks.history_reference_digest | true |
| gate.checks.history_combined_student_physical_input_tokens | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 261602 |
| gate.verification_reference_input_tokens | 65536 |
| gate.verification_reference_soft_positions | 65276 |
| timing.verification_teacher_tokens | 1046365 |
| timing.terminal_save_seconds | 0.18183695801417343 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v3-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "697e8cda12abe128705270758f0eeb83f0f9c08d61de85fc6f68cbb506ee9a49" |
| timing.reference_input_tokens | 262144 |
| verification_teacher_tokens | 1307967 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| initial_parent_preservation.parent_sampler_lineage | true |
| initial_parent_preservation.frozen_teacher_weights | true |
| initial_parent_preservation.frozen_teacher_eval_no_grad | true |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| GPU_seconds | 28.69179393700324 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/probe/timing/latest.json) ／ SHA256: `0b97cdbd51e0940568b63415a014a09ebd27aa0781342929f678f70b16f1d982` ／ 263 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/progress-result.json) ／ SHA256: `07aea54419c6b9ea3b77df58b063ee9090e3bf971e2964fb1ffa0d8b7b0db97f` ／ 1,270,726 bytes

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
| checkpoints.web_kl.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v3-20261006/web_kl/training/checkpoint-00323503.pt" |
| checkpoints.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| checkpoints.web_kl.binding.config_sha256 | "60fcb3e6236f66bcdea397c09cc0f927212a1e3e3dbe94e23c6ff2a7837db0a9" |
| checkpoints.web_kl.binding.arm | "web_kl" |
| checkpoints.web_kl.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.web_kl.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.web_kl.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.web_kl.binding.teacher_goals.web | 75000000 |
| checkpoints.web_kl.binding.teacher_goals.story | 5000000 |
| checkpoints.web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.web_kl.binding.optimizer_policy | "inherit" |
| checkpoints.web_kl.binding.peak_lr | 1e-05 |
| checkpoints.web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.web_kl.binding.study_kind | "historical_parent_staged_CE_frozen_Web_KL_100M" |
| checkpoints.web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| checkpoints.web_kl.binding.outcome_weight | 1 |
| checkpoints.web_kl.binding.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.binding.KL_policy.direction | "parent_to_student" |
| checkpoints.web_kl.binding.KL_policy.temperature | 1.0 |
| checkpoints.web_kl.binding.KL_policy.coefficient | 1.0 |
| checkpoints.web_kl.binding.KL_policy.every_completed_update | 1 |
| checkpoints.web_kl.binding.KL_policy.reference_context | 1024 |
| checkpoints.web_kl.binding.KL_policy.reference_batch | 8 |
| checkpoints.web_kl.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| checkpoints.web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.web_kl.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.web_kl.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.web_kl.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.web_kl.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.web_kl.update | 323503 |
| checkpoints.web_kl.tokens | 10600546304 |
| checkpoints.web_kl.supervised_tokens | 10577786961 |
| checkpoints.web_kl.additional_supervised_tokens | 100000000 |
| checkpoints.web_kl.additional_input_tokens | 100532224 |
| checkpoints.web_kl.source_teachers.web | 75000000 |
| checkpoints.web_kl.source_teachers.story | 5000000 |
| checkpoints.web_kl.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.web_kl.source_teachers.conditional_textbook | 10000000 |
| checkpoints.web_kl.source_eos.web | 159170 |
| checkpoints.web_kl.source_eos.story | 38240 |
| checkpoints.web_kl.source_eos.ordinary_textbook | 74183 |
| checkpoints.web_kl.source_eos.conditional_textbook | 234328 |
| checkpoints.web_kl.source_input_tokens.web | 75183104 |
| checkpoints.web_kl.source_input_tokens.story | 5039104 |
| checkpoints.web_kl.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.web_kl.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.web_kl.source_focus_teachers.web | 0 |
| checkpoints.web_kl.source_focus_teachers.story | 0 |
| checkpoints.web_kl.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.web_kl.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.web_kl.focus_teacher_tokens | 1407427 |
| checkpoints.web_kl.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.web_kl.weighted_teacher_mass | 100000000 |
| checkpoints.web_kl.outcome_weight | 1 |
| checkpoints.web_kl.training_seconds | 255.1444061366201 |
| checkpoints.web_kl.completed_at | "2026-10-06T07:04:02.917166Z" |
| checkpoints.web_kl.reference_replay.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.reference_replay.batch | 8 |
| checkpoints.web_kl.reference_replay.context | 1024 |
| checkpoints.web_kl.reference_replay.initial_cursor.seed | 42 |
| checkpoints.web_kl.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.web_kl.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.web_kl.reference_replay.initial_cursor.context | 1024 |
| checkpoints.web_kl.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.web_kl.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.web_kl.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.web_kl.reference_replay.stream.sampler.seed | 42 |
| checkpoints.web_kl.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.web_kl.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.web_kl.reference_replay.stream.sampler.context | 1024 |
| checkpoints.web_kl.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.web_kl.reference_replay.updates | 3068 |
| checkpoints.web_kl.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.web_kl.reference_replay.body_positions | 25026383 |
| checkpoints.web_kl.reference_replay.ignored_positions | 106673 |
| checkpoints.web_kl.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.web_kl.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.web_kl.reference_input_tokens | 25133056 |
| checkpoints.web_kl.reference_soft_target_body_positions | 25026383 |
| checkpoints.web_kl.combined_student_physical_input_tokens | 125665280 |
| checkpoints.web_kl.KL_policy.kind | "frozen-parent-Web-body-KL-v1" |
| checkpoints.web_kl.KL_policy.direction | "parent_to_student" |
| checkpoints.web_kl.KL_policy.temperature | 1.0 |
| checkpoints.web_kl.KL_policy.coefficient | 1.0 |
| checkpoints.web_kl.KL_policy.every_completed_update | 1 |
| checkpoints.web_kl.KL_policy.reference_context | 1024 |
| checkpoints.web_kl.KL_policy.reference_batch | 8 |
| checkpoints.web_kl.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization" |
| checkpoints.web_kl.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.web_kl.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
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
| evaluations.web_kl.binding.teacher_goals.web | 75000000 |
| evaluations.web_kl.binding.teacher_goals.story | 5000000 |
| evaluations.web_kl.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.web_kl.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.web_kl.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.web_kl.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| evaluations.web_kl.binding.KL_policy.every_completed_update | 1 |
| evaluations.web_kl.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| evaluations.web_kl.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.web_kl.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| evaluations.web_kl.body.documents | 256 |
| evaluations.web_kl.body.limit_documents | 256 |
| evaluations.web_kl.body.body_nll | 321401.2076690197 |
| evaluations.web_kl.body.eos_nll | 635.9188746847212 |
| evaluations.web_kl.body.body_bytes | 472055 |
| evaluations.web_kl.body.body_tokens | 122343 |
| evaluations.web_kl.body.bpb | 0.982266745272942 |
| evaluations.web_kl.body.seconds | 1.3322648800094612 |
| evaluations.web_kl.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.web_kl.generation.max_new_tokens | 64 |
| evaluations.web_kl.greedy_rates.eos | 40 |
| evaluations.web_kl.greedy_rates.repetition | 22 |
| evaluations.web_kl.greedy_rates.unicode_failure | 0 |
| evaluations.web_kl.greedy_rates.role_leak | 0 |
| evaluations.web_kl.greedy_rates.empty | 0 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.point | 0.546875 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.5833333333333334] |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.546875 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5458771715194519 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.mcc | 0.09416472308615167 |
| evaluations.web_kl.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.web_kl.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.web_kl.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.web_kl.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.point | 0.743202416918429 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.ci95 | [0.6978851963746223, 0.7885196374622356] |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.primary.hard_accuracy | 0.743202416918429 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6766616314199396, 0.770392749244713] |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.web_kl.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.web_kl.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.point | 0.340035746201966 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.ci95 | [0.3136729222520107, 0.3672922252010724] |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.primary.hard_accuracy | 0.34048257372654156 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30891961343493624 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.mcc | 0.13812773034264442 |
| evaluations.web_kl.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.web_kl.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.web_kl.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.web_kl.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.web_kl.diagnostics.semantic_both_contexts.correct | 18 |
| evaluations.web_kl.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.web_kl.memory.maximum_observed_reserved_bytes | 13046382592 |
| evaluations.web_kl.protected_test_used | false |
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
| transfer.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| transfer.web_kl.checks.weights_unchanged | true |
| transfer.web_kl.checks.no_gradients | true |
| transfer.web_kl.checks.eval_mode | true |
| transfer.web_kl.checks.RNG_restored | true |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| transfer.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 55 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 67 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.703125 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| transfer.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| transfer.web_kl.optimizer_updates | 0 |
| transfer.web_kl.scientific_teacher_tokens | 0 |
| transfer.web_kl.protected_test_used | false |
| transfer.web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
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
| retention.web_kl.checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| retention.web_kl.checks.weights_unchanged | true |
| retention.web_kl.checks.no_gradients | true |
| retention.web_kl.checks.eval_mode | true |
| retention.web_kl.checks.RNG_restored | true |
| retention.web_kl.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.all128.both_correct | 32 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 26 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.web_kl.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention.web_kl.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 34 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.web_kl.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.web_kl.optimizer_updates | 0 |
| retention.web_kl.scientific_teacher_tokens | 0 |
| retention.web_kl.protected_test_used | false |
| retention.web_kl.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/review.json — web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/review.json) ／ SHA256: `9ce6206323c2b1d481c936616ba60626332ca3955e7e18101ea9cfe056a3ee84` ／ 12,764 bytes

| 原キー | 保存値 |
|---|---|
| status | "web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed" |
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
| transfer_aggregates.web_kl.sum_log_likelihood.all128.accuracy | 0.6953125 |
| transfer_aggregates.web_kl.sum_log_likelihood.all128.both_correct | 54 |
| transfer_aggregates.web_kl.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| transfer_aggregates.web_kl.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer_aggregates.web_kl.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| transfer_aggregates.web_kl.sum_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.all128.both_correct | 55 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.all128.same_unique_candidate | 67 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| transfer_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.all128.accuracy | 0.703125 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.all128.both_correct | 57 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| transfer_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
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
| retention_aggregates.web_kl.sum_log_likelihood.all128.accuracy | 0.60546875 |
| retention_aggregates.web_kl.sum_log_likelihood.all128.both_correct | 32 |
| retention_aggregates.web_kl.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| retention_aggregates.web_kl.sum_log_likelihood.lexical_holdout.both_correct | 26 |
| retention_aggregates.web_kl.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention_aggregates.web_kl.sum_log_likelihood.structural_holdout.both_correct | 6 |
| retention_aggregates.web_kl.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.web_kl.mean_token_log_likelihood.all128.accuracy | 0.62890625 |
| retention_aggregates.web_kl.mean_token_log_likelihood.all128.both_correct | 37 |
| retention_aggregates.web_kl.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| retention_aggregates.web_kl.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| retention_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| retention_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.web_kl.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| retention_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| retention_aggregates.web_kl.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.all128.both_correct | 34 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention_aggregates.web_kl.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 333.1955945980153 |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| verification_GPU_seconds | 28.69179393700324 |
| prior_probe_GPU_seconds | 39.5885307630233 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Additional separately counted Web reference soft targets; not equal total supervision or pure isolated objective effect. One learned seed; nonblind repeated fixeddev. Same parent/model/Adam/RNG/scheduler/actualLR and four primary streams/terminal cursors/ordinaryCE quotas/order. Adds frozen-parent distribution targets on separately counted overlapping trainWeb replay. Shared-generator bridge is local; old128 retention overlaps training forms. Independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0000.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0000.json) ／ SHA256: `dae06f5f72c9300366ace3afce365c595381e3e159e047047d664bd562294474` ／ 9,941 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0016.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0016.json) ／ SHA256: `4968ebc65975964d6e7e8efb478f47d67c087b345d82a847fc20abacaa15187a` ／ 9,584 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0032.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0032.json) ／ SHA256: `0d1e457420d50859f1627cda82e10816019e1f7f93ef586e14f9237786fc86bc` ／ 10,209 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0048.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0048.json) ／ SHA256: `7da8acde4f57b38e343f1756ea08ca223607ae48db8db52292b8757989cd8e04` ／ 9,530 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0064.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0064.json) ／ SHA256: `c813161748dc2bcebf767f3106757899c3d5f91810a81445389786f2f241b695` ／ 10,308 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0080.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0080.json) ／ SHA256: `fb34d0f1de00b5d405671c9f606c6f1ca08e15d4001aa4e1205723126d550642` ／ 9,701 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0096.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0096.json) ／ SHA256: `2e4885f5aa8337865687bba066e0ce8d9c465abb239716cf4835f1fb125c6de7` ／ 9,802 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0112.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0112.json) ／ SHA256: `1dbdadbcebc99d3182c38f40a1e6421ff2cb39ebc879cbc53d3ef2229c369ca5` ／ 10,139 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0128.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0128.json) ／ SHA256: `ce1c4bafa4596cdd2fc75a6f0920cbb1c79d237905ef8461600610720e49ce66` ／ 9,818 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0144.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0144.json) ／ SHA256: `71fa065ebb3e89f29cd2229db161436967cf7cf22bbf16b3bcd7371ff5e5fdf2` ／ 9,874 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0160.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0160.json) ／ SHA256: `ef11e0adb310609f10dae9309f1200ce798eebc8e89184b213c966bf352a24a7` ／ 10,173 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0176.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0176.json) ／ SHA256: `0e883d9a7628c7bfbb4c04b5e19ec12f4962061e48561ef8ba2032656cb49679` ／ 9,976 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0192.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0192.json) ／ SHA256: `f6451477ff882b6005631a800ddf9676c3c7f98e6134a77d895f75fe943e002a` ／ 9,902 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0208.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0208.json) ／ SHA256: `dab1af0a94a88e3b13af9ab455382558079556bc80c9b9655797fbfb16f4cab2` ／ 9,610 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0224.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0224.json) ／ SHA256: `76083862c1a72eeae4dcb91bd9b533f074c09be16fb704194680e6c2ef505d7b` ／ 9,812 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0240.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0240.json) ／ SHA256: `df5e5cf2174353e627d170a9a3a8c4864454250e5a9402bb2115f3ca153e607a` ／ 9,625 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0256.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0256.json) ／ SHA256: `dfb8f5a261484a01ced8b29eaec9bdf2e429fb2cbfb56c29947ac723867fd85e` ／ 9,622 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0272.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0272.json) ／ SHA256: `faf1afae23613adff8aa12473e7d2ec51e8b56b2f3728230f82c6b7f40fb2b92` ／ 9,589 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0288.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0288.json) ／ SHA256: `bf3b97de4b2cacc8980607b74a331707ed231eabc72daa0f2fc0b9c0cf9a726a` ／ 9,621 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0304.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0304.json) ／ SHA256: `daa59bf2d4986a978a6fb846a41ba92c14821f64a2c57ff6cfe31fed59e91004` ／ 9,811 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0320.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0320.json) ／ SHA256: `7259fce63447ccb413824b7b1c92a671a87d144e21f12ec22f6fceecdf0e3841` ／ 9,329 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0336.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0336.json) ／ SHA256: `353b42b79e41c1814b64a24573c568126bb831efa9a0ff135d855990b3beff0c` ／ 9,426 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0352.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0352.json) ／ SHA256: `46d6f60101182cc0fb8860b59551ae85fe1179cc8cef634a08f57db9f3dee432` ／ 9,794 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0368.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0368.json) ／ SHA256: `34fb2ca97f06b2a294279a3d6f3dd3cf46cbaa3cf18f24421eecb376465c984b` ／ 9,544 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0384.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0384.json) ／ SHA256: `91a3b5ae2bcc4d68b38d367704fe17038963e5c2670c70552c71fcbc71f58215` ／ 9,849 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0400.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0400.json) ／ SHA256: `b5ed2f6afe056c9d5c22f510aa269107216de95006f0ed4da4a83fd119564e11` ／ 9,531 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0416.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0416.json) ／ SHA256: `cfa18f11cfe0f71c77a5920b35496b21bdd9f4e870738a0d560965de467db8c5` ／ 9,878 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0432.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0432.json) ／ SHA256: `10b86f82a49b404473155a7efb7d2ed78eb07b7cf936cc8f695793d4908d6562` ／ 9,335 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0448.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0448.json) ／ SHA256: `1c0d63c07dd9de702db9ccc782a301bc3ed2fc0a7960c6ee442be68a230d867c` ／ 9,597 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0464.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0464.json) ／ SHA256: `c332c07a01affe5a6b8b98f7976b1409c86f9e8e6af0e0a1ad669740e4c70d53` ／ 9,415 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0480.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0480.json) ／ SHA256: `281dd8ca6b620573f7bc6593ca89552b89dcbeab8151f257775e647321fe7a66` ／ 9,435 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0496.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/0496.json) ／ SHA256: `913d42e76a992ee626531bea2a2c7fdc98896a00014e33503e201a2d3078448c` ／ 9,495 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/result.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/bridge/web_kl/result.json) ／ SHA256: `80a6d8b0d9dcf38b56dc45bfc21d5b9307cf366b5070f140c5227a22be09c67b` ／ 186,330 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.69140625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 55 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 67 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 20 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 11 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 36 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.703125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.546875 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 48 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0000.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0000.json) ／ SHA256: `8f95047164a4caf7105faeb99c641175d5604e05cbc7a83a96ae0d1915cb94ce` ／ 7,968 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0016.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0016.json) ／ SHA256: `7e3b9495ea10536a877d769e97d5e8512e4cfa36798b1ea8da8d287cd99866dc` ／ 8,325 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0032.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0032.json) ／ SHA256: `77dd447cd840d8320dd1e092de93faacbdcb09743b7c63030d77e74447ba450a` ／ 6,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0048.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0048.json) ／ SHA256: `fee7bdf953ccb1b27640883bf6165ebe2216c7f1fb4158e62fb7b8688ca8dca2` ／ 8,167 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0064.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0064.json) ／ SHA256: `06596f1b624997e07163af68a7d75b1e2220e118d0453f3f63f90c321ce49b57` ／ 8,501 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0080.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0080.json) ／ SHA256: `bfc159775ec5a3f0a40e3161557af5daf5fa096d268c95ee4f28408b49c4db6a` ／ 7,076 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0096.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0096.json) ／ SHA256: `516d47ff258ac5798f7eff38d1dfa10dc2990eae58a9b3a74f1bdf54180495fb` ／ 8,084 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0112.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0112.json) ／ SHA256: `15f59436db42c714509035f93aaf543bede3c81f17d85305f72ac349e49dad43` ／ 8,270 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0128.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0128.json) ／ SHA256: `28afe99cb3eb3dcecec1c52f57632b6ba4238c1d45b93eb8f26070df236af2e8` ／ 7,080 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0144.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0144.json) ／ SHA256: `28ef8e17ab43af4fef6048b68b28f82539637b905fedb021ff582b65852bacee` ／ 8,164 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0160.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0160.json) ／ SHA256: `16587f435a611cedb383402a6125f31381e649d90f27919b88e25cfd9d2d8c56` ／ 8,607 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0176.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0176.json) ／ SHA256: `694a0d4db6b191c38f190e88c5c49f354579dd62e0bdb1b1f9e5aefc880610c5` ／ 6,933 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0192.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0192.json) ／ SHA256: `d36f35cec9583d76bfdc82bb77b2023c12e4362ad3ccc816007a239e38da84f1` ／ 8,181 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0208.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0208.json) ／ SHA256: `433b3b01587dbff449a69aa74fc7242e1e81bb30f5da234a798c6ab3d8090917` ／ 8,519 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0224.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0224.json) ／ SHA256: `28395245d3fb0dc9b980e8bc64ed2b17db54b02a0a492b5afd2b9a327008af7e` ／ 7,088 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0240.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0240.json) ／ SHA256: `028743ce7adc078deff6447059d3c08d1f5b28e1f76f32ba5442b8e8a171afcc` ／ 8,317 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0256.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0256.json) ／ SHA256: `f2dc64f9aa2b7c71eb901943d0d7e95589022471c46f310717492d57939b744e` ／ 8,237 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0272.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0272.json) ／ SHA256: `2e6d7bdbae86011cda895b3da1659947c0cfdcf6bb00ee0145ff4c79040dfcd4` ／ 8,440 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0288.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0288.json) ／ SHA256: `73daf56cff394333b80c867d97c18462c9d830d392e80cc2c17101caf4527a7c` ／ 7,125 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0304.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v3-20261006/transfer/retention/web_kl/0304.json) ／ SHA256: `af6dd92ae4b3a8456773c818d7491c2a1385d2e7fa63d1e535ff06cb4ae0aa60` ／ 8,152 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc" |

</details>
