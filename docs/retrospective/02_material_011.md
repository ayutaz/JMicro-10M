# 教材・供給・品質・量 — 11/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json — source_order100M_and_cached_same_parent_mixed100M_complete</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json) ／ SHA256: `cbca7936ebf395b1d5ccd45022ee4cb85de704a636c8bdae48ff2c24a8adc303` ／ 1,280,987 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.control.binding.config_sha256 | "8201c995e37421869d43361fe9b381e0bd90ee16bfd8b54fca90f93b093dc99d" |
| checkpoints.control.binding.arm | "historical_parent" |
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
| checkpoints.control.binding.study_kind | "historical_Web_parent_inherited_condition_100M" |
| checkpoints.control.binding.sampler_policy | "Continue actual historical sampler/web cursor without reset and actual terminalLR0.00001 without reheat. Same fresh seed42 short streams and100M quota; parent Web amount/order/Adam/RNG/scheduler and LR differ from original10B control, not pure LR causality." |
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
| checkpoints.control.focus_token_digest | "5b1ced584789d2ec8c193a801cbc0667411d83be9c2a69ee56f433f191901fb7" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 160.61181519835372 |
| checkpoints.control.completed_at | "2026-10-06T05:37:50.948190Z" |
| checkpoints.source_order.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| checkpoints.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| checkpoints.source_order.binding.config_sha256 | "03b4ad47fa42b9a669c4588e736648e6339c93b9eb0cf3d08aac22a46cf90a88" |
| checkpoints.source_order.binding.arm | "source_order" |
| checkpoints.source_order.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.source_order.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.source_order.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.source_order.binding.teacher_goals.web | 75000000 |
| checkpoints.source_order.binding.teacher_goals.story | 5000000 |
| checkpoints.source_order.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.source_order.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.source_order.binding.optimizer_policy | "inherit" |
| checkpoints.source_order.binding.peak_lr | 1e-05 |
| checkpoints.source_order.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.source_order.binding.study_kind | "historical_parent_source_order_100M" |
| checkpoints.source_order.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| checkpoints.source_order.binding.outcome_weight | 1 |
| checkpoints.source_order.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.source_order.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.source_order.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.source_order.update | 323503 |
| checkpoints.source_order.tokens | 10600546304 |
| checkpoints.source_order.supervised_tokens | 10577786961 |
| checkpoints.source_order.additional_supervised_tokens | 100000000 |
| checkpoints.source_order.additional_input_tokens | 100532224 |
| checkpoints.source_order.source_teachers.web | 75000000 |
| checkpoints.source_order.source_teachers.story | 5000000 |
| checkpoints.source_order.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.source_order.source_teachers.conditional_textbook | 10000000 |
| checkpoints.source_order.source_eos.web | 159170 |
| checkpoints.source_order.source_eos.story | 38240 |
| checkpoints.source_order.source_eos.ordinary_textbook | 74183 |
| checkpoints.source_order.source_eos.conditional_textbook | 234328 |
| checkpoints.source_order.source_input_tokens.web | 75183104 |
| checkpoints.source_order.source_input_tokens.story | 5039104 |
| checkpoints.source_order.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.source_order.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.source_order.source_focus_teachers.web | 0 |
| checkpoints.source_order.source_focus_teachers.story | 0 |
| checkpoints.source_order.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.source_order.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.source_order.focus_teacher_tokens | 1407427 |
| checkpoints.source_order.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.source_order.weighted_teacher_mass | 100000000 |
| checkpoints.source_order.outcome_weight | 1 |
| checkpoints.source_order.training_seconds | 163.39403466315707 |
| checkpoints.source_order.completed_at | "2026-10-06T06:25:12.649548Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Continue actual historical sampler/web cursor without reset and actual terminalLR0.00001 without reheat. Same fresh seed42 short streams and100M quota; parent Web amount/order/Adam/RNG/scheduler and LR differ from original10B control, not pure LR causality." |
| evaluations.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 318964.4687771797 |
| evaluations.control.body.eos_nll | 585.5442152023315 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 0.9748195810331843 |
| evaluations.control.body.seconds | 1.4293269719928503 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 30 |
| evaluations.control.greedy_rates.repetition | 31 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.609375 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.5572916666666666, 0.6614583333333334] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5755342667649226 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.15819299929208316 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7613293051359517 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.716012084592145, 0.8037009063444104] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7613293051359517 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6646525679758308, 0.7673716012084593] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7613293051359517 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.34584450402144773 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.31814119749776587, 0.3726541554959786] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.34584450402144773 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28150134048257375, 0.3360142984807864] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30832257226998305 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.13674011601633387 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 25 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.source_order.binding.teacher_goals.web | 75000000 |
| evaluations.source_order.binding.teacher_goals.story | 5000000 |
| evaluations.source_order.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.source_order.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.source_order.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.source_order.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| evaluations.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| evaluations.source_order.body.documents | 256 |
| evaluations.source_order.body.limit_documents | 256 |
| evaluations.source_order.body.body_nll | 370922.2019701004 |
| evaluations.source_order.body.eos_nll | 404.9141170345247 |
| evaluations.source_order.body.body_bytes | 472055 |
| evaluations.source_order.body.body_tokens | 122343 |
| evaluations.source_order.body.bpb | 1.1336128657420816 |
| evaluations.source_order.body.seconds | 1.6409143939963542 |
| evaluations.source_order.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.source_order.generation.max_new_tokens | 64 |
| evaluations.source_order.greedy_rates.eos | 76 |
| evaluations.source_order.greedy_rates.repetition | 2 |
| evaluations.source_order.greedy_rates.unicode_failure | 0 |
| evaluations.source_order.greedy_rates.role_leak | 0 |
| evaluations.source_order.greedy_rates.empty | 0 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.point | 0.5625 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.source_order.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.point | 0.26541554959785524 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.primary.hard_accuracy | 0.26541554959785524 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.26630920464700625 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.26555235832138696 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.mcc | 0.08306759781336262 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.source_order.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.source_order.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.source_order.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.source_order.protected_test_used | false |
| transfer.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| transfer.control.checks.weights_unchanged | true |
| transfer.control.checks.no_gradients | true |
| transfer.control.checks.eval_mode | true |
| transfer.control.checks.RNG_restored | true |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 61 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 66 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 57 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 109 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 39 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer.control.optimizer_updates | 0 |
| transfer.control.scientific_teacher_tokens | 0 |
| transfer.control.protected_test_used | false |
| transfer.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| transfer.source_order.checks.weights_unchanged | true |
| transfer.source_order.checks.no_gradients | true |
| transfer.source_order.checks.eval_mode | true |
| transfer.source_order.checks.RNG_restored | true |
| transfer.source_order.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.all128.both_correct | 59 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.source_order.optimizer_updates | 0 |
| transfer.source_order.scientific_teacher_tokens | 0 |
| transfer.source_order.protected_test_used | false |
| transfer.source_order.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| retention.control.checks.weights_unchanged | true |
| retention.control.checks.no_gradients | true |
| retention.control.checks.eval_mode | true |
| retention.control.checks.RNG_restored | true |
| retention.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65625 |
| retention.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.67578125 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 48 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 77 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.671875 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 49 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 74 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 15 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.control.optimizer_updates | 0 |
| retention.control.scientific_teacher_tokens | 0 |
| retention.control.protected_test_used | false |
| retention.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| retention.source_order.checks.weights_unchanged | true |
| retention.source_order.checks.no_gradients | true |
| retention.source_order.checks.eval_mode | true |
| retention.source_order.checks.RNG_restored | true |
| retention.source_order.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention.source_order.summary.aggregate.sum_log_likelihood.all128.both_correct | 36 |
| retention.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 42 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.source_order.optimizer_updates | 0 |
| retention.source_order.scientific_teacher_tokens | 0 |
| retention.source_order.protected_test_used | false |
| retention.source_order.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| status | "source_order100M_and_cached_same_parent_mixed100M_complete" |
| scientific_teacher_tokens | 100000000 |
| total_comparison_teachers | 200000000 |
| Base_adopted | false |
| protected_test_used | false |
| GPU_seconds | 224.47794540700852 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/content-packets/source_order.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/content-packets/source_order.json) ／ SHA256: `59dad851e4830976ab01bb9aa7c6c25a945d027fa63268fd1a262e2a0cf528e0` ／ 88,033 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/body.json) ／ SHA256: `aa121beb633cf8a79ff09236d89cdeac49d0019a91ce5298970779e5ec3c4e24` ／ 67,724 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 370922.2019701004 |
| body.eos_nll | 404.9141170345247 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1336128657420816 |
| body.seconds | 1.6409143939963542 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json) ／ SHA256: `d5b5a7c6b5d971de9bc46c77f52ac5ea19132cab7b97f034c274974cdbe2620e` ／ 72,995 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/jblimp.json) ／ SHA256: `7b6c366e18bfab79cea493d2471dfb374c31e1d6365d31e19c2a15d5198479f2` ／ 338,818 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7824773413897281 |
| summary.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7824773413897281 |
| summary.per_token_secondary.accuracy.point | 0.743202416918429 |
| summary.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.743202416918429 |
| summary.per_token_secondary.macro_f1 | 0.42634315424610053 |
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
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/jcqa.json) ／ SHA256: `886042bd291b7bb358fda3093a474db6fe7e5bb5f762193f16980c3d1bae97eb` ／ 1,643,927 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.26541554959785524 |
| summary.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.26541554959785524 |
| summary.per_token_secondary.accuracy.point | 0.26630920464700625 |
| summary.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| summary.per_token_secondary.macro_f1 | 0.26555235832138696 |
| summary.per_token_secondary.mcc | 0.08306759781336262 |
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
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/result.json) ／ SHA256: `e1d6912d177d366dab409003ba83fc66b16af9debca75f395e4bc8ca32dc5941` ／ 165,918 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 370922.2019701004 |
| body.eos_nll | 404.9141170345247 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1336128657420816 |
| body.seconds | 1.6409143939963542 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 76 |
| greedy_rates.repetition | 2 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5625 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| diagnostics.jcqa.primary.accuracy.point | 0.26541554959785524 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.26541554959785524 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.26630920464700625 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.26555235832138696 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.08306759781336262 |
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
| diagnostics.semantic_both_contexts.correct | 14 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/semantics.json) ／ SHA256: `dbb4a9c320d7ffbb45e6e4e41906b131d7c47d450f51a8ab664f623f39d72ea4` ／ 203,658 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5625 |
| summary.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5625 |
| summary.per_token_secondary.accuracy.point | 0.5 |
| summary.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5 |
| summary.per_token_secondary.macro_f1 | 0.5 |
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
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/job.json) ／ SHA256: `1a5e32c93d8eacbd6020797958372226812c74e2df389ca223d6f39484c2f1cf` ／ 935 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 224.47794540700852 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |
| loss | 0.29509732127189636 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/progress-result.json) ／ SHA256: `1de3d34c7a3b268fa73032798f789d88ddd63f961dac0a6ec420064e625d72c0` ／ 1,280,564 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.control.binding.config_sha256 | "8201c995e37421869d43361fe9b381e0bd90ee16bfd8b54fca90f93b093dc99d" |
| checkpoints.control.binding.arm | "historical_parent" |
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
| checkpoints.control.binding.study_kind | "historical_Web_parent_inherited_condition_100M" |
| checkpoints.control.binding.sampler_policy | "Continue actual historical sampler/web cursor without reset and actual terminalLR0.00001 without reheat. Same fresh seed42 short streams and100M quota; parent Web amount/order/Adam/RNG/scheduler and LR differ from original10B control, not pure LR causality." |
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
| checkpoints.control.focus_token_digest | "5b1ced584789d2ec8c193a801cbc0667411d83be9c2a69ee56f433f191901fb7" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 160.61181519835372 |
| checkpoints.control.completed_at | "2026-10-06T05:37:50.948190Z" |
| checkpoints.source_order.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| checkpoints.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| checkpoints.source_order.binding.config_sha256 | "03b4ad47fa42b9a669c4588e736648e6339c93b9eb0cf3d08aac22a46cf90a88" |
| checkpoints.source_order.binding.arm | "source_order" |
| checkpoints.source_order.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.source_order.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.source_order.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.source_order.binding.teacher_goals.web | 75000000 |
| checkpoints.source_order.binding.teacher_goals.story | 5000000 |
| checkpoints.source_order.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.source_order.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.source_order.binding.optimizer_policy | "inherit" |
| checkpoints.source_order.binding.peak_lr | 1e-05 |
| checkpoints.source_order.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.source_order.binding.study_kind | "historical_parent_source_order_100M" |
| checkpoints.source_order.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| checkpoints.source_order.binding.outcome_weight | 1 |
| checkpoints.source_order.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.source_order.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.source_order.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.source_order.update | 323503 |
| checkpoints.source_order.tokens | 10600546304 |
| checkpoints.source_order.supervised_tokens | 10577786961 |
| checkpoints.source_order.additional_supervised_tokens | 100000000 |
| checkpoints.source_order.additional_input_tokens | 100532224 |
| checkpoints.source_order.source_teachers.web | 75000000 |
| checkpoints.source_order.source_teachers.story | 5000000 |
| checkpoints.source_order.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.source_order.source_teachers.conditional_textbook | 10000000 |
| checkpoints.source_order.source_eos.web | 159170 |
| checkpoints.source_order.source_eos.story | 38240 |
| checkpoints.source_order.source_eos.ordinary_textbook | 74183 |
| checkpoints.source_order.source_eos.conditional_textbook | 234328 |
| checkpoints.source_order.source_input_tokens.web | 75183104 |
| checkpoints.source_order.source_input_tokens.story | 5039104 |
| checkpoints.source_order.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.source_order.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.source_order.source_focus_teachers.web | 0 |
| checkpoints.source_order.source_focus_teachers.story | 0 |
| checkpoints.source_order.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.source_order.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.source_order.focus_teacher_tokens | 1407427 |
| checkpoints.source_order.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.source_order.weighted_teacher_mass | 100000000 |
| checkpoints.source_order.outcome_weight | 1 |
| checkpoints.source_order.training_seconds | 163.39403466315707 |
| checkpoints.source_order.completed_at | "2026-10-06T06:25:12.649548Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Continue actual historical sampler/web cursor without reset and actual terminalLR0.00001 without reheat. Same fresh seed42 short streams and100M quota; parent Web amount/order/Adam/RNG/scheduler and LR differ from original10B control, not pure LR causality." |
| evaluations.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 318964.4687771797 |
| evaluations.control.body.eos_nll | 585.5442152023315 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 0.9748195810331843 |
| evaluations.control.body.seconds | 1.4293269719928503 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 30 |
| evaluations.control.greedy_rates.repetition | 31 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.609375 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.5572916666666666, 0.6614583333333334] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5755342667649226 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.15819299929208316 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7613293051359517 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.716012084592145, 0.8037009063444104] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7613293051359517 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6646525679758308, 0.7673716012084593] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7613293051359517 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.34584450402144773 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.31814119749776587, 0.3726541554959786] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.34584450402144773 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28150134048257375, 0.3360142984807864] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30832257226998305 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.13674011601633387 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 25 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.source_order.binding.teacher_goals.web | 75000000 |
| evaluations.source_order.binding.teacher_goals.story | 5000000 |
| evaluations.source_order.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.source_order.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.source_order.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.source_order.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| evaluations.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| evaluations.source_order.body.documents | 256 |
| evaluations.source_order.body.limit_documents | 256 |
| evaluations.source_order.body.body_nll | 370922.2019701004 |
| evaluations.source_order.body.eos_nll | 404.9141170345247 |
| evaluations.source_order.body.body_bytes | 472055 |
| evaluations.source_order.body.body_tokens | 122343 |
| evaluations.source_order.body.bpb | 1.1336128657420816 |
| evaluations.source_order.body.seconds | 1.6409143939963542 |
| evaluations.source_order.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.source_order.generation.max_new_tokens | 64 |
| evaluations.source_order.greedy_rates.eos | 76 |
| evaluations.source_order.greedy_rates.repetition | 2 |
| evaluations.source_order.greedy_rates.unicode_failure | 0 |
| evaluations.source_order.greedy_rates.role_leak | 0 |
| evaluations.source_order.greedy_rates.empty | 0 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.point | 0.5625 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.source_order.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.source_order.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.source_order.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.source_order.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.source_order.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.source_order.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.source_order.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.point | 0.26541554959785524 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.primary.hard_accuracy | 0.26541554959785524 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.26630920464700625 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.26555235832138696 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.mcc | 0.08306759781336262 |
| evaluations.source_order.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.source_order.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.source_order.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.source_order.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.source_order.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.source_order.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.source_order.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.source_order.protected_test_used | false |
| transfer.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| transfer.control.checks.weights_unchanged | true |
| transfer.control.checks.no_gradients | true |
| transfer.control.checks.eval_mode | true |
| transfer.control.checks.RNG_restored | true |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 61 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 66 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 57 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 109 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 39 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer.control.optimizer_updates | 0 |
| transfer.control.scientific_teacher_tokens | 0 |
| transfer.control.protected_test_used | false |
| transfer.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| transfer.source_order.checks.weights_unchanged | true |
| transfer.source_order.checks.no_gradients | true |
| transfer.source_order.checks.eval_mode | true |
| transfer.source_order.checks.RNG_restored | true |
| transfer.source_order.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.all128.both_correct | 59 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.source_order.optimizer_updates | 0 |
| transfer.source_order.scientific_teacher_tokens | 0 |
| transfer.source_order.protected_test_used | false |
| transfer.source_order.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.control.checkpoint_sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| retention.control.checks.weights_unchanged | true |
| retention.control.checks.no_gradients | true |
| retention.control.checks.eval_mode | true |
| retention.control.checks.RNG_restored | true |
| retention.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65625 |
| retention.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.67578125 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 48 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 77 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.671875 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 49 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 74 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 15 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.control.optimizer_updates | 0 |
| retention.control.scientific_teacher_tokens | 0 |
| retention.control.protected_test_used | false |
| retention.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.source_order.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| retention.source_order.checks.weights_unchanged | true |
| retention.source_order.checks.no_gradients | true |
| retention.source_order.checks.eval_mode | true |
| retention.source_order.checks.RNG_restored | true |
| retention.source_order.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention.source_order.summary.aggregate.sum_log_likelihood.all128.both_correct | 36 |
| retention.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention.source_order.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.source_order.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 42 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.source_order.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.source_order.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.source_order.optimizer_updates | 0 |
| retention.source_order.scientific_teacher_tokens | 0 |
| retention.source_order.protected_test_used | false |
| retention.source_order.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/review.json — source_order100M_all80_and_cached_same_parent_mixed100M_reviewed</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/review.json) ／ SHA256: `d4efc7530850a2a1fe15695c227c4bc6adabb9a7007fbd81091bf20f4900306d` ／ 12,003 bytes

| 原キー | 保存値 |
|---|---|
| status | "source_order100M_all80_and_cached_same_parent_mixed100M_reviewed" |
| summaries.control.BPB | 0.9748195810331843 |
| summaries.control.rates.eos | 30 |
| summaries.control.rates.repetition | 31 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 69 |
| summaries.control.relevance2 | 51 |
| summaries.control.coherent | 4 |
| summaries.control.appropriate | 18 |
| summaries.control.notes_sha256 | "12ff1008589c4f7de7439e99dd4e8d53aea429b2c164c898b4866b3a10431934" |
| summaries.control.additional_teacher_tokens | 100000000 |
| summaries.source_order.BPB | 1.1336128657420816 |
| summaries.source_order.rates.eos | 76 |
| summaries.source_order.rates.repetition | 2 |
| summaries.source_order.rates.unicode_failure | 0 |
| summaries.source_order.rates.role_leak | 0 |
| summaries.source_order.rates.empty | 0 |
| summaries.source_order.grammar2 | 65 |
| summaries.source_order.relevance2 | 39 |
| summaries.source_order.coherent | 23 |
| summaries.source_order.appropriate | 26 |
| summaries.source_order.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| summaries.source_order.additional_teacher_tokens | 100000000 |
| quality_comparison.checks.coherence_gain_at_least8 | true |
| quality_comparison.checks.paired_CI_lower_above0 | true |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | false |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
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
| eligible_for_final_Base_validation | false |
| transfer_aggregates.control.sum_log_likelihood.all128.accuracy | 0.72265625 |
| transfer_aggregates.control.sum_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 61 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 21 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.73828125 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 66 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 57 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 109 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 21 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 39 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.source_order.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.source_order.sum_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.source_order.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.source_order.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.source_order.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.source_order.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.source_order.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.source_order.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.source_order.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.source_order.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer_aggregates.source_order.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.source_order.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.source_order.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.source_order.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.source_order.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer_aggregates.source_order.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| retention_aggregates.control.sum_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.control.sum_log_likelihood.all128.both_correct | 45 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.67578125 |
| retention_aggregates.control.mean_token_log_likelihood.all128.both_correct | 48 |
| retention_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 77 |
| retention_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 34 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.671875 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 49 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 74 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 34 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 28 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 15 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.source_order.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention_aggregates.source_order.sum_log_likelihood.all128.both_correct | 36 |
| retention_aggregates.source_order.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention_aggregates.source_order.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention_aggregates.source_order.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.source_order.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.source_order.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.source_order.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention_aggregates.source_order.mean_token_log_likelihood.all128.both_correct | 42 |
| retention_aggregates.source_order.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention_aggregates.source_order.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.source_order.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention_aggregates.source_order.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.source_order.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.source_order.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.source_order.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.source_order.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.source_order.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.source_order.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.source_order.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention_aggregates.source_order.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention_aggregates.source_order.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention_aggregates.source_order.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention_aggregates.source_order.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 224.47794540700852 |
| verification_GPU_seconds | 20.29770903699682 |
| failed_probe_GPU_seconds | 0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "One learned seed; nonblind repeated fixeddev. Same parent/model/Adam/RNG/scheduler/actualLR and four source streams/terminal cursors/teacher quotas, cross-source ordering differs. Stage boundaries may share an update; source recency and gradient-update grouping change together. Shared-generator bridge is local; old128 retention overlaps training forms. Independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/latest.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/latest.json) ／ SHA256: `862132a35a69e624582af251efb54b2ddcff3fd69ee625cf320a56fa9c5e0a69` ／ 297 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0000.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0000.json) ／ SHA256: `37c36429665eca45a1283bb84c1809cb69c1a98ba20ed2b13b8e74dc319ecdf9` ／ 9,963 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0016.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0016.json) ／ SHA256: `ede3bb6624e2d5bb98c0b9e13d1aa7b0e4705af4f377bfd079a2be98b936e0b9` ／ 9,619 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0032.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0032.json) ／ SHA256: `53955b5ca9ca80ae1f05845f9bff19148d4f6054a67c9b7842bc874598c495e7` ／ 10,245 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0048.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0048.json) ／ SHA256: `bc4bdbadecba81a5fd22a6c11a221c7ce2915a23697c1b3a712a64960307ddf7` ／ 9,544 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0064.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0064.json) ／ SHA256: `f53aba908f8b314aaa017b74300ef18347826a253ceaec1c9d47577d4be4c46c` ／ 10,319 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0080.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0080.json) ／ SHA256: `cba0d30d018fdeb980804a1f7e53c639bac9b20bf64de5a7cb51dbe38141f409` ／ 9,732 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0096.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0096.json) ／ SHA256: `d86f9a3e5d934ca58e25f8286043293dbe43500e6f33e3ffbcdff8d9e2295328` ／ 9,802 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0112.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0112.json) ／ SHA256: `bb634f4f2812d156d0317c8703a137a99462d326814af97240388ae934172d97` ／ 10,166 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0128.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0128.json) ／ SHA256: `86fa8305d301cb7724932e72a6a18424899f544c19f60fc5d50fa122ad50f853` ／ 9,839 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0144.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0144.json) ／ SHA256: `b499e51868cb5f7b97751ca8820b12e310a0dbdd6586936bf28fa78a8f856d78` ／ 9,886 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0160.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0160.json) ／ SHA256: `537a25aa92e79306d24f1b36e9419682ff14c2be5c83c022f37fa81dcd74b9e8` ／ 10,167 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0176.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0176.json) ／ SHA256: `aea4e96da01b06e5de7d932e4c55c8871f7e378bde13ff5387eced4db554cb65` ／ 10,007 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0192.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0192.json) ／ SHA256: `8127a676ea3fbba57e854e8a1084dc9482d352a0051bc2b12b0e409358812d83` ／ 9,900 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0208.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0208.json) ／ SHA256: `c49a5afca703e7e8976ab9a06f9b4b25353832f9a02899abe5b0e3af8ca0fb74` ／ 9,671 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0224.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0224.json) ／ SHA256: `e88dc28fae1ca11ad54f4625d99964f5b44c4304f54d925b35bfb27db0e5cf21` ／ 9,842 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0240.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-v2-20261006/transfer/bridge/source_order/0240.json) ／ SHA256: `0d1b26ee6c21a0a129c38525e78d962f3dc748da15feddaedb793a012616ae0b` ／ 9,660 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |

</details>
