# 評価・生成・意味診断 — 5/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/compare-result.json — actual_nested2048_25M_and_reused512_control_complete_pending_new80</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/compare-result.json) ／ SHA256: `19462e8ab867036294a966a47847b753edde33c9000e1eb04ae7444bce55e614` ／ 437,432 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/control/training/checkpoint-00062936.pt" |
| checkpoints.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| checkpoints.control.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 18750000 |
| checkpoints.control.binding.teacher_goals.story | 1250000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_input_positive_outcome_CE" |
| checkpoints.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| checkpoints.control.update | 62936 |
| checkpoints.control.tokens | 2062286848 |
| checkpoints.control.supervised_tokens | 2045000000 |
| checkpoints.control.additional_supervised_tokens | 25000000 |
| checkpoints.control.additional_input_tokens | 25231360 |
| checkpoints.control.source_teachers.web | 18750000 |
| checkpoints.control.source_teachers.story | 1250000 |
| checkpoints.control.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.control.source_teachers.conditional_textbook | 2500000 |
| checkpoints.control.source_eos.web | 164131 |
| checkpoints.control.source_eos.story | 9486 |
| checkpoints.control.source_eos.ordinary_textbook | 18576 |
| checkpoints.control.source_eos.conditional_textbook | 17680 |
| checkpoints.control.source_input_tokens.web | 18934784 |
| checkpoints.control.source_input_tokens.story | 1259520 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.control.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 654588 |
| checkpoints.control.focus_teacher_tokens | 654588 |
| checkpoints.control.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| checkpoints.control.weighted_teacher_mass | 25000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 39.79399216850288 |
| checkpoints.control.completed_at | "2026-10-06T01:37:03.185223Z" |
| checkpoints.large2048.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-diversity-comparison-20261006/large2048/training/checkpoint-00062936.pt" |
| checkpoints.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| checkpoints.large2048.binding.config_sha256 | "87b4ed4070fb92d5c97ffbb9563d20ad3d649414d81c11426cabe0540a7f80d0" |
| checkpoints.large2048.binding.arm | "large2048" |
| checkpoints.large2048.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.large2048.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.large2048.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.large2048.binding.teacher_goals.web | 18750000 |
| checkpoints.large2048.binding.teacher_goals.story | 1250000 |
| checkpoints.large2048.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.large2048.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.large2048.binding.optimizer_policy | "inherit" |
| checkpoints.large2048.binding.peak_lr | 0.0002 |
| checkpoints.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.large2048.binding.study_kind | "nested_condition_source_quantity" |
| checkpoints.large2048.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| checkpoints.large2048.binding.outcome_weight | 1 |
| checkpoints.large2048.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.large2048.update | 62936 |
| checkpoints.large2048.tokens | 2062286848 |
| checkpoints.large2048.supervised_tokens | 2045000000 |
| checkpoints.large2048.additional_supervised_tokens | 25000000 |
| checkpoints.large2048.additional_input_tokens | 25231360 |
| checkpoints.large2048.source_teachers.web | 18750000 |
| checkpoints.large2048.source_teachers.story | 1250000 |
| checkpoints.large2048.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.large2048.source_teachers.conditional_textbook | 2500000 |
| checkpoints.large2048.source_eos.web | 164131 |
| checkpoints.large2048.source_eos.story | 9486 |
| checkpoints.large2048.source_eos.ordinary_textbook | 18576 |
| checkpoints.large2048.source_eos.conditional_textbook | 17514 |
| checkpoints.large2048.source_input_tokens.web | 18934784 |
| checkpoints.large2048.source_input_tokens.story | 1259520 |
| checkpoints.large2048.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.large2048.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.large2048.source_focus_teachers.web | 0 |
| checkpoints.large2048.source_focus_teachers.story | 0 |
| checkpoints.large2048.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.large2048.source_focus_teachers.conditional_textbook | 654871 |
| checkpoints.large2048.focus_teacher_tokens | 654871 |
| checkpoints.large2048.focus_token_digest | "45d496b8d5bb369188109cec511fa64f1340374be30badaf9bce3ad77036f014" |
| checkpoints.large2048.weighted_teacher_mass | 25000000 |
| checkpoints.large2048.outcome_weight | 1 |
| checkpoints.large2048.training_seconds | 39.85271529221791 |
| checkpoints.large2048.completed_at | "2026-10-06T02:06:47.967298Z" |
| evaluations.control.binding.teacher_goals.web | 18750000 |
| evaluations.control.binding.teacher_goals.story | 1250000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| evaluations.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| evaluations.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 374176.51803684235 |
| evaluations.control.body.eos_nll | 947.4363566637039 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1435587102961566 |
| evaluations.control.body.seconds | 1.539865662023658 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 44 |
| evaluations.control.greedy_rates.repetition | 26 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.4947916666666667, 0.5572916666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8338368580060423] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7794561933534743] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.2725647899910634, 0.32529043789097406] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2899833679971908 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.11364311165128803 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 8 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.large2048.binding.teacher_goals.web | 18750000 |
| evaluations.large2048.binding.teacher_goals.story | 1250000 |
| evaluations.large2048.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.large2048.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.large2048.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| evaluations.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| evaluations.large2048.body.documents | 256 |
| evaluations.large2048.body.limit_documents | 256 |
| evaluations.large2048.body.body_nll | 373060.9088640213 |
| evaluations.large2048.body.eos_nll | 941.1389634013176 |
| evaluations.large2048.body.body_bytes | 472055 |
| evaluations.large2048.body.body_tokens | 122343 |
| evaluations.large2048.body.bpb | 1.1401491842426266 |
| evaluations.large2048.body.seconds | 1.487570909986971 |
| evaluations.large2048.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.large2048.generation.max_new_tokens | 64 |
| evaluations.large2048.greedy_rates.eos | 42 |
| evaluations.large2048.greedy_rates.repetition | 23 |
| evaluations.large2048.greedy_rates.unicode_failure | 0 |
| evaluations.large2048.greedy_rates.role_leak | 0 |
| evaluations.large2048.greedy_rates.empty | 0 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.ci95 | [0.5104166666666666, 0.578125] |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.625] |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5831524099001303 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.mcc | 0.1668115312456598 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7462235649546828 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6948640483383686, 0.7915407854984894] |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4273356401384083 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.large2048.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.raw_pair_accuracy | 0.7945619335347432 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.point | 0.290437890974084 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.ci95 | [0.2640750670241287, 0.3159070598748883] |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.28328865058087577 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.257372654155496, 0.3092046470062556] |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826998284171443 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.mcc | 0.10451770262852586 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.semantic_both_contexts.correct | 10 |
| evaluations.large2048.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.large2048.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.large2048.protected_test_used | false |
| status | "actual_nested2048_25M_and_reused512_control_complete_pending_new80" |
| scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| total_comparison_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1299890 |
| verification_GPU_seconds | 11.799473121995106 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 113.42645317898132 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/condition-pair-analysis.json — completed_nested_source_fixed_dev_condition_pair_analysis</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/condition-pair-analysis.json) ／ SHA256: `a589905b7a29e7ffddafe94d6c2a75b3bf8cabf5ac33762f86090428cfa8fe17` ／ 186,067 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_nested_source_fixed_dev_condition_pair_analysis" |
| models.control.causality.accuracy | 0.5625 |
| models.control.causality.both_correct | 2 |
| models.control.causality.neither_correct | 0 |
| models.control.comparison.accuracy | 0.5 |
| models.control.comparison.both_correct | 0 |
| models.control.comparison.neither_correct | 0 |
| models.control.coreference.accuracy | 0.4375 |
| models.control.coreference.both_correct | 0 |
| models.control.coreference.neither_correct | 2 |
| models.control.negation.accuracy | 0.5 |
| models.control.negation.both_correct | 0 |
| models.control.negation.neither_correct | 0 |
| models.control.quantity.accuracy | 0.5625 |
| models.control.quantity.both_correct | 3 |
| models.control.quantity.neither_correct | 1 |
| models.control.time.accuracy | 0.59375 |
| models.control.time.both_correct | 3 |
| models.control.time.neither_correct | 0 |
| models.large2048.causality.accuracy | 0.65625 |
| models.large2048.causality.both_correct | 5 |
| models.large2048.causality.neither_correct | 0 |
| models.large2048.comparison.accuracy | 0.5 |
| models.large2048.comparison.both_correct | 0 |
| models.large2048.comparison.neither_correct | 0 |
| models.large2048.coreference.accuracy | 0.46875 |
| models.large2048.coreference.both_correct | 0 |
| models.large2048.coreference.neither_correct | 1 |
| models.large2048.negation.accuracy | 0.5 |
| models.large2048.negation.both_correct | 0 |
| models.large2048.negation.neither_correct | 0 |
| models.large2048.quantity.accuracy | 0.5625 |
| models.large2048.quantity.both_correct | 3 |
| models.large2048.quantity.neither_correct | 1 |
| models.large2048.time.accuracy | 0.5625 |
| models.large2048.time.both_correct | 2 |
| models.large2048.time.neither_correct | 0 |
| models.parent2B.causality.accuracy | 0.625 |
| models.parent2B.causality.both_correct | 4 |
| models.parent2B.causality.neither_correct | 0 |
| models.parent2B.comparison.accuracy | 0.5 |
| models.parent2B.comparison.both_correct | 0 |
| models.parent2B.comparison.neither_correct | 0 |
| models.parent2B.coreference.accuracy | 0.4375 |
| models.parent2B.coreference.both_correct | 0 |
| models.parent2B.coreference.neither_correct | 2 |
| models.parent2B.negation.accuracy | 0.5 |
| models.parent2B.negation.both_correct | 0 |
| models.parent2B.negation.neither_correct | 0 |
| models.parent2B.quantity.accuracy | 0.5625 |
| models.parent2B.quantity.both_correct | 3 |
| models.parent2B.quantity.neither_correct | 1 |
| models.parent2B.time.accuracy | 0.5 |
| models.parent2B.time.both_correct | 1 |
| models.parent2B.time.neither_correct | 1 |
| references.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| references.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| pair_analysis_source_sha256 | "77ef1b192b4b507c60c1d2a560b43ef282925cf5c4bae66dc8158073e854e126" |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| new_original_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |
| CPU_seconds | 0.011879584984853864 |
| limitations | "Same fixed96 dev families, one learned seed; descriptive ranking/context sensitivity, not independent generalization, fluent generation, attention failure or capacity proof. No dev texts enter learning; source quantity comparison uses existing train only." |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/body.json) ／ SHA256: `6647a70fcd8d1afa15c1c34aa8e4b191da99cfc41d330706dddcd1bd3c3a0d88` ／ 67,314 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 373060.9088640213 |
| body.eos_nll | 941.1389634013176 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1401491842426266 |
| body.seconds | 1.487570909986971 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/generation.json) ／ SHA256: `f8b2668a82ad10a905e51bf028f3ccf6cb8f5d3e6023f3f84efaf215bc59cdaa` ／ 91,162 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/jblimp.json) ／ SHA256: `b752e00d691ec863d90627446a3c9347231216a6d279099b1a1cbdf1a186043c` ／ 338,511 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7915407854984894 |
| summary.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7915407854984894 |
| summary.per_token_secondary.accuracy.point | 0.7462235649546828 |
| summary.per_token_secondary.accuracy.ci95 | [0.6948640483383686, 0.7915407854984894] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| summary.per_token_secondary.macro_f1 | 0.4273356401384083 |
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
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/jcqa.json) ／ SHA256: `28bd00d4c4013851181babc6ffe5025fe456f9de07dd3c9758c096a2e411e305` ／ 1,639,653 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.290437890974084 |
| summary.primary.accuracy.ci95 | [0.2640750670241287, 0.3159070598748883] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.291331546023235 |
| summary.per_token_secondary.accuracy.point | 0.28328865058087577 |
| summary.per_token_secondary.accuracy.ci95 | [0.257372654155496, 0.3092046470062556] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| summary.per_token_secondary.macro_f1 | 0.2826998284171443 |
| summary.per_token_secondary.mcc | 0.10451770262852586 |
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
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/result.json) ／ SHA256: `8a02152fb19751744c26c06e9f4e8e3c4d41b26b357e18a9ffd4ec24be836896` ／ 185,925 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 18750000 |
| binding.teacher_goals.story | 1250000 |
| binding.teacher_goals.ordinary_textbook | 2500000 |
| binding.teacher_goals.conditional_textbook | 2500000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 373060.9088640213 |
| body.eos_nll | 941.1389634013176 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1401491842426266 |
| body.seconds | 1.487570909986971 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 42 |
| greedy_rates.repetition | 23 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5104166666666666, 0.578125] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.625] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5831524099001303 |
| diagnostics.semantics.per_token_secondary.mcc | 0.1668115312456598 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7462235649546828 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6948640483383686, 0.7915407854984894] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4273356401384083 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7945619335347432 |
| diagnostics.jcqa.primary.accuracy.point | 0.290437890974084 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2640750670241287, 0.3159070598748883] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.28328865058087577 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.257372654155496, 0.3092046470062556] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826998284171443 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.10451770262852586 |
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
| diagnostics.semantic_both_contexts.correct | 10 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/evaluation/large2048/evaluation/semantics.json) ／ SHA256: `bb408c71da398bb0a73ffc645f0639340e41ee3272eb224d04b88ad7e5d1e16a` ／ 203,468 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5416666666666666 |
| summary.primary.accuracy.ci95 | [0.5104166666666666, 0.578125] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5416666666666666 |
| summary.per_token_secondary.accuracy.point | 0.5833333333333334 |
| summary.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.625] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| summary.per_token_secondary.macro_f1 | 0.5831524099001303 |
| summary.per_token_secondary.mcc | 0.1668115312456598 |
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
<summary>reports/phase6/condition-diversity-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/job.json) ／ SHA256: `62c6c152452063132140ed0f6d837a9ef20f769a5cd791552cc5cec27f96804e` ／ 872 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 113.42645317898132 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 24696536 |
| teacher_budget | 25000000 |
| source_teachers.web | 18521779 |
| source_teachers.story | 1234792 |
| source_teachers.ordinary_textbook | 2469974 |
| source_teachers.conditional_textbook | 2469991 |
| loss | 2.6440489292144775 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/large2048-content-review.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/large2048-content-review.json) ／ SHA256: `dc731a4b17dfd98d312c5a649e7c3248c5fa7f85e6ccfd8c3a0605bba0f33348` ／ 848 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.1401491842426266 |
| rates.eos | 42 |
| rates.repetition | 23 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 59 |
| relevance2 | 50 |
| coherent | 16 |
| appropriate | 27 |
| new_teacher_tokens | 25000000 |
| source_teacher_tokens.web | 18750000 |
| source_teacher_tokens.story | 1250000 |
| source_teacher_tokens.ordinary_textbook | 2500000 |
| source_teacher_tokens.conditional_textbook | 2500000 |
| conditional_source_documents | 2048 |
| notes_sha256 | "166bae110c256cce316fdff557d05b7f9bceb61383c176c6037fd47d1a33ad34" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/large2048/training/latest.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/large2048/training/latest.json) ／ SHA256: `d9284583d09691ae61b17290a41e3b4906d2cce523d8a81fe3f1aa22774c4ebc` ／ 286 bytes

| 原キー | 保存値 |
|---|---|
| update | 62936 |
| tokens_seen | 2062286848 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/ordinary-stream-audit.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/ordinary-stream-audit.json) ／ SHA256: `522bdba95934c9b24790ee4ccc5b2934ce4cf58407b6dcbb2fa69b5ed4592266` ／ 2,105 bytes

| 原キー | 保存値 |
|---|---|
| small.teachers.web | 18750000 |
| small.teachers.story | 1250000 |
| small.teachers.ordinary_textbook | 2500000 |
| small.EOS.web | 164131 |
| small.EOS.story | 9486 |
| small.EOS.ordinary_textbook | 18576 |
| small.body_bytes.web | 74986646 |
| small.body_bytes.story | 5116702 |
| small.body_bytes.ordinary_textbook | 10682428 |
| small.physical_inputs.web | 18934784 |
| small.physical_inputs.story | 1259520 |
| small.physical_inputs.ordinary_textbook | 2519040 |
| small.physical_inputs.conditional_textbook | 2518016 |
| small.total_updates | 770 |
| large.teachers.web | 18750000 |
| large.teachers.story | 1250000 |
| large.teachers.ordinary_textbook | 2500000 |
| large.EOS.web | 164131 |
| large.EOS.story | 9486 |
| large.EOS.ordinary_textbook | 18576 |
| large.body_bytes.web | 74986646 |
| large.body_bytes.story | 5116702 |
| large.body_bytes.ordinary_textbook | 10682428 |
| large.physical_inputs.web | 18934784 |
| large.physical_inputs.story | 1259520 |
| large.physical_inputs.ordinary_textbook | 2519040 |
| large.physical_inputs.conditional_textbook | 2518016 |
| large.total_updates | 770 |
| checks.target_sha256 | true |
| checks.teachers | true |
| checks.EOS | true |
| checks.body_bytes | true |
| CPU_seconds | 3.7522688489989378 |
| CPU_limit_seconds | 30 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/probe/job.json) ／ SHA256: `47c160deb9261cc8a349189d448ba0deed531ed15410f30c08deac74c40c2264` ／ 601 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 11.799473121995106 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/probe/result.json — actual2048_resume_timing_complete</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/probe/result.json) ／ SHA256: `d770165c062d29d3a9f0dec6c6854d2f2d07f75ae229a69e1f7277d7a5dd3866` ／ 68,792 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual2048_resume_timing_complete" |
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
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 259984 |
| timing.verification_teacher_tokens | 1039906 |
| timing.terminal_save_seconds | 0.16138963898993097 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-diversity-comparison-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "0eef077b6f3906241b1b762c81d0dd4271879b231873534237ea759a95795881" |
| verification_teacher_tokens | 1299890 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 11.799473121995106 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/probe/timing/latest.json) ／ SHA256: `cbc3d4dc88073833a6f7a19b61aa4c407d920218eef6de3b4cf7d9d5878188e1` ／ 271 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/progress-result.json) ／ SHA256: `4243d98805eed298216f455b0bc4a75bb82bc2e29d9409cf82ee7e50222a9ecb` ／ 436,620 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/control/training/checkpoint-00062936.pt" |
| checkpoints.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| checkpoints.control.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 18750000 |
| checkpoints.control.binding.teacher_goals.story | 1250000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_input_positive_outcome_CE" |
| checkpoints.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| checkpoints.control.update | 62936 |
| checkpoints.control.tokens | 2062286848 |
| checkpoints.control.supervised_tokens | 2045000000 |
| checkpoints.control.additional_supervised_tokens | 25000000 |
| checkpoints.control.additional_input_tokens | 25231360 |
| checkpoints.control.source_teachers.web | 18750000 |
| checkpoints.control.source_teachers.story | 1250000 |
| checkpoints.control.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.control.source_teachers.conditional_textbook | 2500000 |
| checkpoints.control.source_eos.web | 164131 |
| checkpoints.control.source_eos.story | 9486 |
| checkpoints.control.source_eos.ordinary_textbook | 18576 |
| checkpoints.control.source_eos.conditional_textbook | 17680 |
| checkpoints.control.source_input_tokens.web | 18934784 |
| checkpoints.control.source_input_tokens.story | 1259520 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.control.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 654588 |
| checkpoints.control.focus_teacher_tokens | 654588 |
| checkpoints.control.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| checkpoints.control.weighted_teacher_mass | 25000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 39.79399216850288 |
| checkpoints.control.completed_at | "2026-10-06T01:37:03.185223Z" |
| checkpoints.large2048.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-diversity-comparison-20261006/large2048/training/checkpoint-00062936.pt" |
| checkpoints.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| checkpoints.large2048.binding.config_sha256 | "87b4ed4070fb92d5c97ffbb9563d20ad3d649414d81c11426cabe0540a7f80d0" |
| checkpoints.large2048.binding.arm | "large2048" |
| checkpoints.large2048.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.large2048.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.large2048.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.large2048.binding.teacher_goals.web | 18750000 |
| checkpoints.large2048.binding.teacher_goals.story | 1250000 |
| checkpoints.large2048.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.large2048.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.large2048.binding.optimizer_policy | "inherit" |
| checkpoints.large2048.binding.peak_lr | 0.0002 |
| checkpoints.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.large2048.binding.study_kind | "nested_condition_source_quantity" |
| checkpoints.large2048.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| checkpoints.large2048.binding.outcome_weight | 1 |
| checkpoints.large2048.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.large2048.update | 62936 |
| checkpoints.large2048.tokens | 2062286848 |
| checkpoints.large2048.supervised_tokens | 2045000000 |
| checkpoints.large2048.additional_supervised_tokens | 25000000 |
| checkpoints.large2048.additional_input_tokens | 25231360 |
| checkpoints.large2048.source_teachers.web | 18750000 |
| checkpoints.large2048.source_teachers.story | 1250000 |
| checkpoints.large2048.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.large2048.source_teachers.conditional_textbook | 2500000 |
| checkpoints.large2048.source_eos.web | 164131 |
| checkpoints.large2048.source_eos.story | 9486 |
| checkpoints.large2048.source_eos.ordinary_textbook | 18576 |
| checkpoints.large2048.source_eos.conditional_textbook | 17514 |
| checkpoints.large2048.source_input_tokens.web | 18934784 |
| checkpoints.large2048.source_input_tokens.story | 1259520 |
| checkpoints.large2048.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.large2048.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.large2048.source_focus_teachers.web | 0 |
| checkpoints.large2048.source_focus_teachers.story | 0 |
| checkpoints.large2048.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.large2048.source_focus_teachers.conditional_textbook | 654871 |
| checkpoints.large2048.focus_teacher_tokens | 654871 |
| checkpoints.large2048.focus_token_digest | "45d496b8d5bb369188109cec511fa64f1340374be30badaf9bce3ad77036f014" |
| checkpoints.large2048.weighted_teacher_mass | 25000000 |
| checkpoints.large2048.outcome_weight | 1 |
| checkpoints.large2048.training_seconds | 39.85271529221791 |
| checkpoints.large2048.completed_at | "2026-10-06T02:06:47.967298Z" |
| evaluations.control.binding.teacher_goals.web | 18750000 |
| evaluations.control.binding.teacher_goals.story | 1250000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| evaluations.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| evaluations.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 374176.51803684235 |
| evaluations.control.body.eos_nll | 947.4363566637039 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1435587102961566 |
| evaluations.control.body.seconds | 1.539865662023658 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 44 |
| evaluations.control.greedy_rates.repetition | 26 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.4947916666666667, 0.5572916666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8338368580060423] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7794561933534743] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.2725647899910634, 0.32529043789097406] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2899833679971908 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.11364311165128803 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 8 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.large2048.binding.teacher_goals.web | 18750000 |
| evaluations.large2048.binding.teacher_goals.story | 1250000 |
| evaluations.large2048.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.large2048.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.large2048.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.large2048.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| evaluations.large2048.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| evaluations.large2048.body.documents | 256 |
| evaluations.large2048.body.limit_documents | 256 |
| evaluations.large2048.body.body_nll | 373060.9088640213 |
| evaluations.large2048.body.eos_nll | 941.1389634013176 |
| evaluations.large2048.body.body_bytes | 472055 |
| evaluations.large2048.body.body_tokens | 122343 |
| evaluations.large2048.body.bpb | 1.1401491842426266 |
| evaluations.large2048.body.seconds | 1.487570909986971 |
| evaluations.large2048.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.large2048.generation.max_new_tokens | 64 |
| evaluations.large2048.greedy_rates.eos | 42 |
| evaluations.large2048.greedy_rates.repetition | 23 |
| evaluations.large2048.greedy_rates.unicode_failure | 0 |
| evaluations.large2048.greedy_rates.role_leak | 0 |
| evaluations.large2048.greedy_rates.empty | 0 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.ci95 | [0.5104166666666666, 0.578125] |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.625] |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5831524099001303 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.mcc | 0.1668115312456598 |
| evaluations.large2048.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.large2048.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.large2048.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.large2048.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7462235649546828 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6948640483383686, 0.7915407854984894] |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4273356401384083 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.large2048.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.large2048.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.large2048.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.jblimp.raw_pair_accuracy | 0.7945619335347432 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.point | 0.290437890974084 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.ci95 | [0.2640750670241287, 0.3159070598748883] |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.28328865058087577 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.257372654155496, 0.3092046470062556] |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826998284171443 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.mcc | 0.10451770262852586 |
| evaluations.large2048.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.large2048.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.large2048.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.large2048.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.large2048.diagnostics.semantic_both_contexts.correct | 10 |
| evaluations.large2048.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.large2048.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.large2048.protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-diversity-comparison-20261006/review.json — nested512_vs2048_same25M_actual_all160_content_complete</summary>

[原記録](../../reports/phase6/condition-diversity-comparison-20261006/review.json) ／ SHA256: `dc068ee587688a8d110fc8db59a18a5d0a78d9439f70a43476b1be712ddcf3a7` ／ 4,440 bytes

| 原キー | 保存値 |
|---|---|
| status | "nested512_vs2048_same25M_actual_all160_content_complete" |
| summaries.control.BPB | 1.1435587102961566 |
| summaries.control.rates.eos | 44 |
| summaries.control.rates.repetition | 26 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 54 |
| summaries.control.relevance2 | 43 |
| summaries.control.coherent | 15 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 25000000 |
| summaries.control.source_teacher_tokens.web | 18750000 |
| summaries.control.source_teacher_tokens.story | 1250000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.control.focus_teacher_tokens | 654588 |
| summaries.control.weighted_teacher_mass | 25000000 |
| summaries.control.notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| summaries.control.Base_adopted | false |
| summaries.large2048.BPB | 1.1401491842426266 |
| summaries.large2048.rates.eos | 42 |
| summaries.large2048.rates.repetition | 23 |
| summaries.large2048.rates.unicode_failure | 0 |
| summaries.large2048.rates.role_leak | 0 |
| summaries.large2048.rates.empty | 0 |
| summaries.large2048.grammar2 | 59 |
| summaries.large2048.relevance2 | 50 |
| summaries.large2048.coherent | 16 |
| summaries.large2048.appropriate | 27 |
| summaries.large2048.new_teacher_tokens | 25000000 |
| summaries.large2048.source_teacher_tokens.web | 18750000 |
| summaries.large2048.source_teacher_tokens.story | 1250000 |
| summaries.large2048.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.large2048.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.large2048.conditional_source_documents | 2048 |
| summaries.large2048.notes_sha256 | "166bae110c256cce316fdff557d05b7f9bceb61383c176c6037fd47d1a33ad34" |
| summaries.large2048.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.control.grammar_at_least56 | false |
| absolute_dev_screen.control.coherence_at_least27 | false |
| absolute_dev_screen.control.appropriate_at_least27 | true |
| absolute_dev_screen.control.EOS_at_least37 | true |
| absolute_dev_screen.control.repetition_at_most18 | false |
| absolute_dev_screen.control.no_empty_role_unicode | true |
| absolute_dev_screen.large2048.grammar_at_least56 | true |
| absolute_dev_screen.large2048.coherence_at_least27 | false |
| absolute_dev_screen.large2048.appropriate_at_least27 | true |
| absolute_dev_screen.large2048.EOS_at_least37 | true |
| absolute_dev_screen.large2048.repetition_at_most18 | false |
| absolute_dev_screen.large2048.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.large2048.EOS_at_least8_more | true |
| original_Web.large2048.repetition_no_worse | true |
| original_Web.large2048.no_empty_role_unicode | true |
| original_Web.large2048.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.large2048 | false |
| new_scientific_teacher_tokens | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| total_comparison_teacher_tokens | 50000000 |
| verification_teacher_tokens | 1299890 |
| GPU_seconds | 113.42645317898132 |
| verification_GPU_seconds | 11.799473121995106 |
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
<summary>reports/phase6/condition-diversity-positive-20261006/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-diversity-positive-20261006/manifest.json) ／ SHA256: `cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280` ／ 553,775 bytes

| 原キー | 保存値 |
|---|---|
| documents | 2048 |
| original_body_tokens | 290243 |
| original_body_bytes | 1253324 |
| serialized_tokens | 294339 |
| EOS_targets | 2048 |
| known_weak_pilot_documents_with_focus_disabled | 12 |
| focus_enabled_documents | 2036 |
| source_pairs_sha256 | "8d694f870d777021b040bfeb4b32d4b4ae80e160f30597886bb2598bc792a58a" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| nested_small_actual_checks.tokens | true |
| nested_small_actual_checks.focus | true |
| nested_small_actual_checks.offsets | true |
| nested_small_actual_checks.lengths | true |
| nested_small_actual_checks.metadata | true |
| newly_prepared_original_tokens | 0 |
| copied_existing_serialized_tokens | 294339 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| limitations | "All source already in original2B; local exact body uniqueness only; only64 new/64 old individually reviewed. No global/family/factual certification, no retokenization or source rewrite." |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/annotations.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/annotations.json) ／ SHA256: `f6e3ef20851c329e2287b3d24e507699ea4d3d2ec858345fcdd6e8aeb3f035dc` ／ 37,188 bytes

| 原キー | 保存値 |
|---|---|
| arms.control.notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| arms.positive4.notes_sha256 | "2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e" |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/compare-result.json — both_actual25M_learning_evaluations_complete_pending_all160_content</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/compare-result.json) ／ SHA256: `f94e88e51747a9fc5a99cb773062af8fd5cb30930a1da29e58ed3c10c4e8dff8` ／ 437,690 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/control/training/checkpoint-00062936.pt" |
| checkpoints.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| checkpoints.control.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 18750000 |
| checkpoints.control.binding.teacher_goals.story | 1250000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_input_positive_outcome_CE" |
| checkpoints.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| checkpoints.control.update | 62936 |
| checkpoints.control.tokens | 2062286848 |
| checkpoints.control.supervised_tokens | 2045000000 |
| checkpoints.control.additional_supervised_tokens | 25000000 |
| checkpoints.control.additional_input_tokens | 25231360 |
| checkpoints.control.source_teachers.web | 18750000 |
| checkpoints.control.source_teachers.story | 1250000 |
| checkpoints.control.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.control.source_teachers.conditional_textbook | 2500000 |
| checkpoints.control.source_eos.web | 164131 |
| checkpoints.control.source_eos.story | 9486 |
| checkpoints.control.source_eos.ordinary_textbook | 18576 |
| checkpoints.control.source_eos.conditional_textbook | 17680 |
| checkpoints.control.source_input_tokens.web | 18934784 |
| checkpoints.control.source_input_tokens.story | 1259520 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.control.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 654588 |
| checkpoints.control.focus_teacher_tokens | 654588 |
| checkpoints.control.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| checkpoints.control.weighted_teacher_mass | 25000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 39.79399216850288 |
| checkpoints.control.completed_at | "2026-10-06T01:37:03.185223Z" |
| checkpoints.positive4.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/positive4/training/checkpoint-00062936.pt" |
| checkpoints.positive4.checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| checkpoints.positive4.binding.config_sha256 | "5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9" |
| checkpoints.positive4.binding.arm | "positive4" |
| checkpoints.positive4.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.positive4.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.positive4.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.positive4.binding.teacher_goals.web | 18750000 |
| checkpoints.positive4.binding.teacher_goals.story | 1250000 |
| checkpoints.positive4.binding.teacher_goals.ordinary_textbook | 2500000 |
| checkpoints.positive4.binding.teacher_goals.conditional_textbook | 2500000 |
| checkpoints.positive4.binding.optimizer_policy | "inherit" |
| checkpoints.positive4.binding.peak_lr | 0.0002 |
| checkpoints.positive4.binding.loss | "normalized positive-outcome CE body+EOS" |
| checkpoints.positive4.binding.study_kind | "same_input_positive_outcome_CE" |
| checkpoints.positive4.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoints.positive4.binding.outcome_weight | 4 |
| checkpoints.positive4.binding.positive_manifest_sha256 | "7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc" |
| checkpoints.positive4.update | 62936 |
| checkpoints.positive4.tokens | 2062286848 |
| checkpoints.positive4.supervised_tokens | 2045000000 |
| checkpoints.positive4.additional_supervised_tokens | 25000000 |
| checkpoints.positive4.additional_input_tokens | 25231360 |
| checkpoints.positive4.source_teachers.web | 18750000 |
| checkpoints.positive4.source_teachers.story | 1250000 |
| checkpoints.positive4.source_teachers.ordinary_textbook | 2500000 |
| checkpoints.positive4.source_teachers.conditional_textbook | 2500000 |
| checkpoints.positive4.source_eos.web | 164131 |
| checkpoints.positive4.source_eos.story | 9486 |
| checkpoints.positive4.source_eos.ordinary_textbook | 18576 |
| checkpoints.positive4.source_eos.conditional_textbook | 17680 |
| checkpoints.positive4.source_input_tokens.web | 18934784 |
| checkpoints.positive4.source_input_tokens.story | 1259520 |
| checkpoints.positive4.source_input_tokens.ordinary_textbook | 2519040 |
| checkpoints.positive4.source_input_tokens.conditional_textbook | 2518016 |
| checkpoints.positive4.source_focus_teachers.web | 0 |
| checkpoints.positive4.source_focus_teachers.story | 0 |
| checkpoints.positive4.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.positive4.source_focus_teachers.conditional_textbook | 654588 |
| checkpoints.positive4.focus_teacher_tokens | 654588 |
| checkpoints.positive4.focus_token_digest | "d4ce6d3868cbda941dd0129cb30661c13680ccaef9948c91bbc06a54fe8d7751" |
| checkpoints.positive4.weighted_teacher_mass | 26963764 |
| checkpoints.positive4.outcome_weight | 4 |
| checkpoints.positive4.training_seconds | 39.13245353780803 |
| checkpoints.positive4.completed_at | "2026-10-06T01:38:57.938574Z" |
| evaluations.control.binding.teacher_goals.web | 18750000 |
| evaluations.control.binding.teacher_goals.story | 1250000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.control.binding.loss | "normalized positive-outcome CE body+EOS" |
| evaluations.control.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| evaluations.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 374176.51803684235 |
| evaluations.control.body.eos_nll | 947.4363566637039 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1435587102961566 |
| evaluations.control.body.seconds | 1.539865662023658 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 44 |
| evaluations.control.greedy_rates.repetition | 26 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.4947916666666667, 0.5572916666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8338368580060423] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7794561933534743] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.2725647899910634, 0.32529043789097406] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.29848078641644327 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2899833679971908 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.11364311165128803 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 8 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.positive4.binding.teacher_goals.web | 18750000 |
| evaluations.positive4.binding.teacher_goals.story | 1250000 |
| evaluations.positive4.binding.teacher_goals.ordinary_textbook | 2500000 |
| evaluations.positive4.binding.teacher_goals.conditional_textbook | 2500000 |
| evaluations.positive4.binding.loss | "normalized positive-outcome CE body+EOS" |
| evaluations.positive4.binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| evaluations.positive4.checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| evaluations.positive4.body.documents | 256 |
| evaluations.positive4.body.limit_documents | 256 |
| evaluations.positive4.body.body_nll | 374712.80347824097 |
| evaluations.positive4.body.eos_nll | 944.6387304514647 |
| evaluations.positive4.body.body_bytes | 472055 |
| evaluations.positive4.body.body_tokens | 122343 |
| evaluations.positive4.body.bpb | 1.145197706486869 |
| evaluations.positive4.body.seconds | 1.284524454997154 |
| evaluations.positive4.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.positive4.generation.max_new_tokens | 64 |
| evaluations.positive4.greedy_rates.eos | 47 |
| evaluations.positive4.greedy_rates.repetition | 22 |
| evaluations.positive4.greedy_rates.unicode_failure | 0 |
| evaluations.positive4.greedy_rates.role_leak | 0 |
| evaluations.positive4.greedy_rates.empty | 0 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.point | 0.5520833333333334 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.ci95 | [0.515625, 0.5885416666666666] |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.primary.hard_accuracy | 0.5520833333333334 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
| evaluations.positive4.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.positive4.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.positive4.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.positive4.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.positive4.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7764350453172205] |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.positive4.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.positive4.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.positive4.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.positive4.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.positive4.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.positive4.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.point | 0.2993744414655943 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.ci95 | [0.2734584450402145, 0.3261840929401251] |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jcqa.primary.hard_accuracy | 0.2993744414655943 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2900528226748983 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.mcc | 0.1136717024098022 |
| evaluations.positive4.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.positive4.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.positive4.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.positive4.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.positive4.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.positive4.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.positive4.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.positive4.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.positive4.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.positive4.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.positive4.protected_test_used | false |
| matched_input_teacher_checks.tokens | true |
| matched_input_teacher_checks.supervised_tokens | true |
| matched_input_teacher_checks.source_teachers | true |
| matched_input_teacher_checks.source_eos | true |
| matched_input_teacher_checks.source_input_tokens | true |
| matched_input_teacher_checks.source_focus_teachers | true |
| matched_input_teacher_checks.focus_teacher_tokens | true |
| matched_input_teacher_checks.focus_token_digest | true |
| matched_input_teacher_checks.input_label_digest | true |
| matched_input_teacher_checks.sampler | true |
| status | "both_actual25M_learning_evaluations_complete_pending_all160_content" |
| scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 2599740 |
| verification_GPU_seconds | 22.01919901598012 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 224.40080486799707 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/condition-pair-analysis.json — completed_fixed_dev_condition_pair_analysis</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/condition-pair-analysis.json) ／ SHA256: `ad11415b522d1c128b23bf972e3788298184c1f6189e1b9ab7d7b0524559226b` ／ 186,024 bytes

| 原キー | 保存値 |
|---|---|
| status | "completed_fixed_dev_condition_pair_analysis" |
| models.control.causality.accuracy | 0.5625 |
| models.control.causality.both_correct | 2 |
| models.control.causality.neither_correct | 0 |
| models.control.comparison.accuracy | 0.5 |
| models.control.comparison.both_correct | 0 |
| models.control.comparison.neither_correct | 0 |
| models.control.coreference.accuracy | 0.4375 |
| models.control.coreference.both_correct | 0 |
| models.control.coreference.neither_correct | 2 |
| models.control.negation.accuracy | 0.5 |
| models.control.negation.both_correct | 0 |
| models.control.negation.neither_correct | 0 |
| models.control.quantity.accuracy | 0.5625 |
| models.control.quantity.both_correct | 3 |
| models.control.quantity.neither_correct | 1 |
| models.control.time.accuracy | 0.59375 |
| models.control.time.both_correct | 3 |
| models.control.time.neither_correct | 0 |
| models.positive4.causality.accuracy | 0.6875 |
| models.positive4.causality.both_correct | 6 |
| models.positive4.causality.neither_correct | 0 |
| models.positive4.comparison.accuracy | 0.5 |
| models.positive4.comparison.both_correct | 0 |
| models.positive4.comparison.neither_correct | 0 |
| models.positive4.coreference.accuracy | 0.5 |
| models.positive4.coreference.both_correct | 1 |
| models.positive4.coreference.neither_correct | 1 |
| models.positive4.negation.accuracy | 0.5 |
| models.positive4.negation.both_correct | 0 |
| models.positive4.negation.neither_correct | 0 |
| models.positive4.quantity.accuracy | 0.53125 |
| models.positive4.quantity.both_correct | 2 |
| models.positive4.quantity.neither_correct | 1 |
| models.positive4.time.accuracy | 0.59375 |
| models.positive4.time.both_correct | 3 |
| models.positive4.time.neither_correct | 0 |
| models.parent2B.causality.accuracy | 0.625 |
| models.parent2B.causality.both_correct | 4 |
| models.parent2B.causality.neither_correct | 0 |
| models.parent2B.comparison.accuracy | 0.5 |
| models.parent2B.comparison.both_correct | 0 |
| models.parent2B.comparison.neither_correct | 0 |
| models.parent2B.coreference.accuracy | 0.4375 |
| models.parent2B.coreference.both_correct | 0 |
| models.parent2B.coreference.neither_correct | 2 |
| models.parent2B.negation.accuracy | 0.5 |
| models.parent2B.negation.both_correct | 0 |
| models.parent2B.negation.neither_correct | 0 |
| models.parent2B.quantity.accuracy | 0.5625 |
| models.parent2B.quantity.both_correct | 3 |
| models.parent2B.quantity.neither_correct | 1 |
| models.parent2B.time.accuracy | 0.5 |
| models.parent2B.time.both_correct | 1 |
| models.parent2B.time.neither_correct | 1 |
| references.control.checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| references.positive4.checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.017634991003433242 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| prepared_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| Chat_adopted | false |
| requested_five_steps_complete | false |
| limitations | "Reuse of fixed dev96 paired families, one learned seed. Same prediction after a context change is descriptive evidence of candidate preference on these examples, not proof of missing attention or model capacity limits. Positive margin shift is not correct generation. No new training or test; do not train on these evaluation prompts." |

</details>
