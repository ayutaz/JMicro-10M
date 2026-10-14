# 評価・生成・意味診断 — 9/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/compare-result.json — actual_curriculum100M_reused_natural100M_complete_pending_new80</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/compare-result.json) ／ SHA256: `09924bf223ada61c45f45ea6ee95db876d5ff4fb81bcbe58c3705c56d7050cd8` ／ 1,078,725 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checkpoints.control.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| checkpoints.control.binding.arm | "large2048" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.control.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 70061 |
| checkpoints.control.source_input_tokens.web | 75674624 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10071040 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 2620780 |
| checkpoints.control.focus_teacher_tokens | 2620780 |
| checkpoints.control.focus_token_digest | "8e2af3a7a69ecc6ea03b6f189587339877c5cf6d20031ae69100d24ffe4a7d85" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 151.12010613348684 |
| checkpoints.control.completed_at | "2026-10-06T02:43:40.425716Z" |
| checkpoints.curriculum.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.curriculum.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.curriculum.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.curriculum.binding.arm | "curriculum" |
| checkpoints.curriculum.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.curriculum.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.curriculum.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.curriculum.binding.teacher_goals.web | 75000000 |
| checkpoints.curriculum.binding.teacher_goals.story | 5000000 |
| checkpoints.curriculum.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.curriculum.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.curriculum.binding.optimizer_policy | "inherit" |
| checkpoints.curriculum.binding.peak_lr | 0.0002 |
| checkpoints.curriculum.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.curriculum.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.curriculum.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.curriculum.binding.outcome_weight | 1 |
| checkpoints.curriculum.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.curriculum.update | 65249 |
| checkpoints.curriculum.tokens | 2138079232 |
| checkpoints.curriculum.supervised_tokens | 2120000000 |
| checkpoints.curriculum.additional_supervised_tokens | 100000000 |
| checkpoints.curriculum.additional_input_tokens | 101023744 |
| checkpoints.curriculum.source_teachers.web | 75000000 |
| checkpoints.curriculum.source_teachers.story | 5000000 |
| checkpoints.curriculum.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.curriculum.source_teachers.conditional_textbook | 10000000 |
| checkpoints.curriculum.source_eos.web | 656229 |
| checkpoints.curriculum.source_eos.story | 38240 |
| checkpoints.curriculum.source_eos.ordinary_textbook | 74183 |
| checkpoints.curriculum.source_eos.conditional_textbook | 243066 |
| checkpoints.curriculum.source_input_tokens.web | 75666432 |
| checkpoints.curriculum.source_input_tokens.story | 5039104 |
| checkpoints.curriculum.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.curriculum.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.curriculum.source_focus_teachers.web | 0 |
| checkpoints.curriculum.source_focus_teachers.story | 0 |
| checkpoints.curriculum.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.curriculum.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.curriculum.focus_teacher_tokens | 1460032 |
| checkpoints.curriculum.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.curriculum.weighted_teacher_mass | 100000000 |
| checkpoints.curriculum.outcome_weight | 1 |
| checkpoints.curriculum.training_seconds | 152.96801666589454 |
| checkpoints.curriculum.completed_at | "2026-10-06T03:11:09.066152Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| evaluations.control.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 371986.53641319275 |
| evaluations.control.body.eos_nll | 947.4765769392252 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.136865685906886 |
| evaluations.control.body.seconds | 1.2853469330002554 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 42 |
| evaluations.control.greedy_rates.repetition | 20 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5052083333333334 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.53125] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5052083333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5617391304347825 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.1254363015010636 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8308157099697885] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
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
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.29803395889186773 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.27211796246648795, 0.32350312779267204] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2864164432529044 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2605004468275246, 0.3118856121537087] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28596961572832885 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2851033257946277 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.107638793111279 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 4 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.curriculum.binding.teacher_goals.web | 75000000 |
| evaluations.curriculum.binding.teacher_goals.story | 5000000 |
| evaluations.curriculum.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.curriculum.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.curriculum.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.curriculum.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| evaluations.curriculum.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| evaluations.curriculum.body.documents | 256 |
| evaluations.curriculum.body.limit_documents | 256 |
| evaluations.curriculum.body.body_nll | 369821.8238763809 |
| evaluations.curriculum.body.eos_nll | 956.706282325089 |
| evaluations.curriculum.body.body_bytes | 472055 |
| evaluations.curriculum.body.body_tokens | 122343 |
| evaluations.curriculum.body.bpb | 1.1302498889302441 |
| evaluations.curriculum.body.seconds | 1.6376896990113892 |
| evaluations.curriculum.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.curriculum.generation.max_new_tokens | 64 |
| evaluations.curriculum.greedy_rates.eos | 45 |
| evaluations.curriculum.greedy_rates.repetition | 17 |
| evaluations.curriculum.greedy_rates.unicode_failure | 0 |
| evaluations.curriculum.greedy_rates.role_leak | 0 |
| evaluations.curriculum.greedy_rates.empty | 0 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.point | 0.53125 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.primary.hard_accuracy | 0.53125 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5208333333333334 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5203649397197785 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.mcc | 0.041748286072343294 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.curriculum.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8308157099697885] |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.curriculum.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.point | 0.2868632707774799 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.ci95 | [0.26184092940125114, 0.3136729222520107] |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.primary.hard_accuracy | 0.2868632707774799 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2752457551385165 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24932975871313673, 0.30116175156389635] |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2752457551385165 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.27460276425066615 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.mcc | 0.09421259981033882 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.curriculum.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.curriculum.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.curriculum.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.curriculum.protected_test_used | false |
| transfer.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| transfer.parent2B.checks.weights_unchanged | true |
| transfer.parent2B.checks.no_gradients | true |
| transfer.parent2B.checks.eval_mode | true |
| transfer.parent2B.checks.RNG_restored | true |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 1 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer.parent2B.optimizer_updates | 0 |
| transfer.parent2B.scientific_teacher_tokens | 0 |
| transfer.parent2B.protected_test_used | false |
| transfer.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| transfer.natural100M.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| transfer.natural100M.checks.weights_unchanged | true |
| transfer.natural100M.checks.no_gradients | true |
| transfer.natural100M.checks.eval_mode | true |
| transfer.natural100M.checks.RNG_restored | true |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 3 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 14 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer.natural100M.optimizer_updates | 0 |
| transfer.natural100M.scientific_teacher_tokens | 0 |
| transfer.natural100M.protected_test_used | false |
| transfer.natural100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| transfer.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| transfer.curriculum100M.checks.weights_unchanged | true |
| transfer.curriculum100M.checks.no_gradients | true |
| transfer.curriculum100M.checks.eval_mode | true |
| transfer.curriculum100M.checks.RNG_restored | true |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 63 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 66 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer.curriculum100M.optimizer_updates | 0 |
| transfer.curriculum100M.scientific_teacher_tokens | 0 |
| transfer.curriculum100M.protected_test_used | false |
| transfer.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| status | "actual_curriculum100M_reused_natural100M_complete_pending_new80" |
| scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| total_comparison_teacher_tokens | 200000000 |
| verification_teacher_tokens | 1297661 |
| verification_GPU_seconds | 13.408861087023979 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 236.22689373401226 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/condition-pair-analysis.json — actual_curriculum100M_fixeddev_condition_pairs_reused</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/condition-pair-analysis.json) ／ SHA256: `95d3bb0dbb2dca22f77936f5e36b9f399f96e42acdf09ab7c1fef8ba688500a1` ／ 185,873 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_curriculum100M_fixeddev_condition_pairs_reused" |
| models.curriculum100M.causality.accuracy | 0.78125 |
| models.curriculum100M.causality.both_correct | 9 |
| models.curriculum100M.causality.neither_correct | 0 |
| models.curriculum100M.comparison.accuracy | 0.4375 |
| models.curriculum100M.comparison.both_correct | 0 |
| models.curriculum100M.comparison.neither_correct | 2 |
| models.curriculum100M.coreference.accuracy | 0.53125 |
| models.curriculum100M.coreference.both_correct | 1 |
| models.curriculum100M.coreference.neither_correct | 0 |
| models.curriculum100M.negation.accuracy | 0.5 |
| models.curriculum100M.negation.both_correct | 0 |
| models.curriculum100M.negation.neither_correct | 0 |
| models.curriculum100M.quantity.accuracy | 0.5 |
| models.curriculum100M.quantity.both_correct | 1 |
| models.curriculum100M.quantity.neither_correct | 1 |
| models.curriculum100M.time.accuracy | 0.4375 |
| models.curriculum100M.time.both_correct | 1 |
| models.curriculum100M.time.neither_correct | 3 |
| models.natural100M.causality.accuracy | 0.53125 |
| models.natural100M.causality.both_correct | 1 |
| models.natural100M.causality.neither_correct | 0 |
| models.natural100M.comparison.accuracy | 0.5 |
| models.natural100M.comparison.both_correct | 0 |
| models.natural100M.comparison.neither_correct | 0 |
| models.natural100M.coreference.accuracy | 0.46875 |
| models.natural100M.coreference.both_correct | 0 |
| models.natural100M.coreference.neither_correct | 1 |
| models.natural100M.negation.accuracy | 0.5 |
| models.natural100M.negation.both_correct | 0 |
| models.natural100M.negation.neither_correct | 0 |
| models.natural100M.quantity.accuracy | 0.53125 |
| models.natural100M.quantity.both_correct | 2 |
| models.natural100M.quantity.neither_correct | 1 |
| models.natural100M.time.accuracy | 0.5 |
| models.natural100M.time.both_correct | 1 |
| models.natural100M.time.neither_correct | 1 |
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
| references.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| references.natural100M.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.015086653002072126 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Same repeatedly inspected fixeddev96 families and one learned seed. Descriptive context response; not independent fluent continuation quality, causal diagnosis or certified10M capacity. Local generator probes remain separate." |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/job.json) ／ SHA256: `df673c584b0101cd2cb79b3676a584bbeb0bff536cc1dd65540fb94309240b10` ／ 925 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 236.22689373401226 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99914563 |
| teacher_budget | 100000000 |
| source_teachers.web | 74934975 |
| source_teachers.story | 4995784 |
| source_teachers.ordinary_textbook | 9991796 |
| source_teachers.conditional_textbook | 9992008 |
| loss | 2.334336042404175 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/probe/job.json) ／ SHA256: `291a30afd5c0844bac8d352837fe14f94810c15888f42db58cab4fb19341371e` ／ 600 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 13.408861087023979 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/probe/result.json — actual_generated_curriculum_resume_timing_complete</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/probe/result.json) ／ SHA256: `0bde7fb5d801a69520f6d47d974b68cc833f8f654622f2a07c5e78ee9144d6ca` ／ 68,774 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_generated_curriculum_resume_timing_complete" |
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
| gate.verification_teacher_tokens | 259544 |
| timing.verification_teacher_tokens | 1038117 |
| timing.terminal_save_seconds | 0.16548050902201794 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "61bfa65b332bd2fcf0b3a9ee277defdca874f62ccdc1b35720da0837ce9a0b1e" |
| verification_teacher_tokens | 1297661 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 13.408861087023979 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/probe/timing/latest.json) ／ SHA256: `6a335c253944eeb0a54c6578ec7850575fbfac8e32b347fc20d601f8e4e6eefe` ／ 270 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/progress-result.json) ／ SHA256: `51f5379ba878fa96b544ae911e62a01a919f0b6f0cefd42337c486a3d7109dcb` ／ 1,077,911 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-source-learning-100m-20261006/large2048/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checkpoints.control.binding.config_sha256 | "c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e" |
| checkpoints.control.binding.arm | "large2048" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.control.binding.study_kind | "nested_condition_source_quantity_at_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 70061 |
| checkpoints.control.source_input_tokens.web | 75674624 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10071040 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 2620780 |
| checkpoints.control.focus_teacher_tokens | 2620780 |
| checkpoints.control.focus_token_digest | "8e2af3a7a69ecc6ea03b6f189587339877c5cf6d20031ae69100d24ffe4a7d85" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 151.12010613348684 |
| checkpoints.control.completed_at | "2026-10-06T02:43:40.425716Z" |
| checkpoints.curriculum.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.curriculum.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.curriculum.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.curriculum.binding.arm | "curriculum" |
| checkpoints.curriculum.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.curriculum.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.curriculum.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.curriculum.binding.teacher_goals.web | 75000000 |
| checkpoints.curriculum.binding.teacher_goals.story | 5000000 |
| checkpoints.curriculum.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.curriculum.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.curriculum.binding.optimizer_policy | "inherit" |
| checkpoints.curriculum.binding.peak_lr | 0.0002 |
| checkpoints.curriculum.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.curriculum.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.curriculum.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.curriculum.binding.outcome_weight | 1 |
| checkpoints.curriculum.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.curriculum.update | 65249 |
| checkpoints.curriculum.tokens | 2138079232 |
| checkpoints.curriculum.supervised_tokens | 2120000000 |
| checkpoints.curriculum.additional_supervised_tokens | 100000000 |
| checkpoints.curriculum.additional_input_tokens | 101023744 |
| checkpoints.curriculum.source_teachers.web | 75000000 |
| checkpoints.curriculum.source_teachers.story | 5000000 |
| checkpoints.curriculum.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.curriculum.source_teachers.conditional_textbook | 10000000 |
| checkpoints.curriculum.source_eos.web | 656229 |
| checkpoints.curriculum.source_eos.story | 38240 |
| checkpoints.curriculum.source_eos.ordinary_textbook | 74183 |
| checkpoints.curriculum.source_eos.conditional_textbook | 243066 |
| checkpoints.curriculum.source_input_tokens.web | 75666432 |
| checkpoints.curriculum.source_input_tokens.story | 5039104 |
| checkpoints.curriculum.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.curriculum.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.curriculum.source_focus_teachers.web | 0 |
| checkpoints.curriculum.source_focus_teachers.story | 0 |
| checkpoints.curriculum.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.curriculum.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.curriculum.focus_teacher_tokens | 1460032 |
| checkpoints.curriculum.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.curriculum.weighted_teacher_mass | 100000000 |
| checkpoints.curriculum.outcome_weight | 1 |
| checkpoints.curriculum.training_seconds | 152.96801666589454 |
| checkpoints.curriculum.completed_at | "2026-10-06T03:11:09.066152Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control." |
| evaluations.control.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 371986.53641319275 |
| evaluations.control.body.eos_nll | 947.4765769392252 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.136865685906886 |
| evaluations.control.body.seconds | 1.2853469330002554 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 42 |
| evaluations.control.greedy_rates.repetition | 20 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5052083333333334 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.53125] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5052083333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5617391304347825 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.1254363015010636 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8308157099697885] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
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
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.29803395889186773 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.27211796246648795, 0.32350312779267204] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2864164432529044 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2605004468275246, 0.3118856121537087] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28596961572832885 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2851033257946277 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.107638793111279 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 4 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.curriculum.binding.teacher_goals.web | 75000000 |
| evaluations.curriculum.binding.teacher_goals.story | 5000000 |
| evaluations.curriculum.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.curriculum.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.curriculum.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.curriculum.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| evaluations.curriculum.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| evaluations.curriculum.body.documents | 256 |
| evaluations.curriculum.body.limit_documents | 256 |
| evaluations.curriculum.body.body_nll | 369821.8238763809 |
| evaluations.curriculum.body.eos_nll | 956.706282325089 |
| evaluations.curriculum.body.body_bytes | 472055 |
| evaluations.curriculum.body.body_tokens | 122343 |
| evaluations.curriculum.body.bpb | 1.1302498889302441 |
| evaluations.curriculum.body.seconds | 1.6376896990113892 |
| evaluations.curriculum.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.curriculum.generation.max_new_tokens | 64 |
| evaluations.curriculum.greedy_rates.eos | 45 |
| evaluations.curriculum.greedy_rates.repetition | 17 |
| evaluations.curriculum.greedy_rates.unicode_failure | 0 |
| evaluations.curriculum.greedy_rates.role_leak | 0 |
| evaluations.curriculum.greedy_rates.empty | 0 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.point | 0.53125 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.primary.hard_accuracy | 0.53125 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5208333333333334 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5203649397197785 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.mcc | 0.041748286072343294 |
| evaluations.curriculum.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.curriculum.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.curriculum.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.curriculum.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8308157099697885] |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.curriculum.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.curriculum.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.point | 0.2868632707774799 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.ci95 | [0.26184092940125114, 0.3136729222520107] |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.primary.hard_accuracy | 0.2868632707774799 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2752457551385165 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24932975871313673, 0.30116175156389635] |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2752457551385165 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.27460276425066615 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.mcc | 0.09421259981033882 |
| evaluations.curriculum.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.curriculum.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.curriculum.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.curriculum.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.curriculum.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.curriculum.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.curriculum.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.curriculum.protected_test_used | false |
| transfer.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| transfer.parent2B.checks.weights_unchanged | true |
| transfer.parent2B.checks.no_gradients | true |
| transfer.parent2B.checks.eval_mode | true |
| transfer.parent2B.checks.RNG_restored | true |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 1 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer.parent2B.optimizer_updates | 0 |
| transfer.parent2B.scientific_teacher_tokens | 0 |
| transfer.parent2B.protected_test_used | false |
| transfer.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| transfer.natural100M.checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| transfer.natural100M.checks.weights_unchanged | true |
| transfer.natural100M.checks.no_gradients | true |
| transfer.natural100M.checks.eval_mode | true |
| transfer.natural100M.checks.RNG_restored | true |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer.natural100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 3 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer.natural100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 14 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer.natural100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer.natural100M.optimizer_updates | 0 |
| transfer.natural100M.scientific_teacher_tokens | 0 |
| transfer.natural100M.protected_test_used | false |
| transfer.natural100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| transfer.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| transfer.curriculum100M.checks.weights_unchanged | true |
| transfer.curriculum100M.checks.no_gradients | true |
| transfer.curriculum100M.checks.eval_mode | true |
| transfer.curriculum100M.checks.RNG_restored | true |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 63 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 66 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer.curriculum100M.optimizer_updates | 0 |
| transfer.curriculum100M.scientific_teacher_tokens | 0 |
| transfer.curriculum100M.protected_test_used | false |
| transfer.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/review.json — actual_curriculum100M_all80_transfer128_and_reused_natural100M_content_complete</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/review.json) ／ SHA256: `8b5e0d6373ada72b315d81051f93b9afabe9257bd00676592b879d98533daa92` ／ 10,423 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_curriculum100M_all80_transfer128_and_reused_natural100M_content_complete" |
| summaries.control.BPB | 1.136865685906886 |
| summaries.control.rates.eos | 42 |
| summaries.control.rates.repetition | 20 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 62 |
| summaries.control.relevance2 | 74 |
| summaries.control.coherent | 12 |
| summaries.control.appropriate | 30 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.control.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.control.conditional_source_documents | 2048 |
| summaries.control.notes_sha256 | "c20773f49a310b5eceda42b08d14a4a5c64e102b0e7d36aa3cec478dfff310e0" |
| summaries.control.Base_adopted | false |
| summaries.curriculum.BPB | 1.1302498889302441 |
| summaries.curriculum.rates.eos | 45 |
| summaries.curriculum.rates.repetition | 17 |
| summaries.curriculum.rates.unicode_failure | 0 |
| summaries.curriculum.rates.role_leak | 0 |
| summaries.curriculum.rates.empty | 0 |
| summaries.curriculum.grammar2 | 60 |
| summaries.curriculum.relevance2 | 68 |
| summaries.curriculum.coherent | 14 |
| summaries.curriculum.appropriate | 27 |
| summaries.curriculum.new_teacher_tokens | 100000000 |
| summaries.curriculum.source_teacher_tokens.web | 75000000 |
| summaries.curriculum.source_teacher_tokens.story | 5000000 |
| summaries.curriculum.source_teacher_tokens.ordinary_textbook | 10000000 |
| summaries.curriculum.source_teacher_tokens.conditional_textbook | 10000000 |
| summaries.curriculum.conditional_source_documents | 2048 |
| summaries.curriculum.generated_serialized_tokens | 86309 |
| summaries.curriculum.notes_sha256 | "b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6" |
| summaries.curriculum.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | true |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | true |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.sum_log_likelihood.all128.both_correct | 5 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.parent2B.sum_log_likelihood.structural_holdout.both_correct | 1 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.both_correct | 13 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| transfer_aggregates.parent2B.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.sum_log_likelihood.all128.both_correct | 7 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| transfer_aggregates.natural100M.sum_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.both_correct | 6 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.both_correct | 14 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| transfer_aggregates.natural100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.accuracy | 0.7109375 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.all128.both_correct | 63 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.sum_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.both_correct | 66 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.curriculum100M.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.both_correct | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer_aggregates.curriculum100M.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| ordinary_stream_checks.target_sha256 | true |
| ordinary_stream_checks.teachers | true |
| ordinary_stream_checks.EOS | true |
| ordinary_stream_checks.body_bytes | true |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1297661 |
| GPU_seconds | 236.22689373401226 |
| verification_GPU_seconds | 13.408861087023979 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| limitations | "One learned seed, nonblind judgments, repeatedly inspected fixeddev; generator probe scores are not independent natural-language quality. Shorter local material changes length/EOS/lexical distribution together; not one isolated causal operator effect." |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0000.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0000.json) ／ SHA256: `a2f426a329f065697b6f549a6447a5f8419c7eea71001fb05d859d67923f1b03` ／ 7,864 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0016.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0016.json) ／ SHA256: `b33607fde6a4e0e2feef98d108061101fa649130d30a464f047d4209976f5be1` ／ 8,204 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0032.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0032.json) ／ SHA256: `9cab456986908395da544120de5955f7c8f9caee83c93e4ee0a998aa2f6c69f7` ／ 6,886 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0048.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0048.json) ／ SHA256: `c1b3d295efa7c11ba98fba234445cdf7714d760b320a740ad06a9e4468584496` ／ 8,055 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0064.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0064.json) ／ SHA256: `da96a9454b9936b03f9474954fef7c35467552191247d8444c9474a05dcf31b7` ／ 8,353 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0080.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0080.json) ／ SHA256: `aa27edb5f1821303154ad34eb5fbc76422ca57efa8991f650cb0bf1bfcc2ce11` ／ 6,980 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0096.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0096.json) ／ SHA256: `eec6ad1b3dd9ac786cf3b1710cd56bb8233611d47a2a2888953bcfe8894e4d4a` ／ 7,954 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0112.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0112.json) ／ SHA256: `ccbe1cf929969870d805f7cb30741befb4b3c47827c25aafbceb9099ae58f64a` ／ 8,137 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0128.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0128.json) ／ SHA256: `a59d1a53b190e955ec413545856952f83a243d71c14b2394e2fa78fb6374ca2e` ／ 6,978 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0144.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0144.json) ／ SHA256: `5ddd6f81ec03cc285159ff0ad1ab740b20067aa542e947565be17447b7dd7afd` ／ 8,066 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0160.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0160.json) ／ SHA256: `44591efc1179a917598d3e556b2334a4d04bfeb94a65cb48e2272b2132112cd0` ／ 8,463 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0176.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0176.json) ／ SHA256: `73fbdde94288ace64b3b153da312cb583f35a8cbcd30a4b343c602f209d84780` ／ 6,822 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0192.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0192.json) ／ SHA256: `572c47dc503f5a0c65cc9d17bb5e0bdd599af18db8f5a7e389cab54fe7e8b921` ／ 8,067 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0208.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0208.json) ／ SHA256: `03836302bae7bd2e7e1acac8cce81c4cfdeed6c5b2bcc18f0c33076e79b3b81a` ／ 8,388 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0224.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0224.json) ／ SHA256: `79bf77b4918a2656841d417b6109b050e70234a2d6a39a905288c7a3edf3b673` ／ 6,982 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0240.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0240.json) ／ SHA256: `ce6e5b834ed3a4404c45c6703a4fda98b3a37578ce2830038e92a7beb232c87f` ／ 8,222 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0256.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0256.json) ／ SHA256: `57c39ad3a5e827b90b80fd6cf38c9ac6f45b8eecd2e2b865793adf5b64fa97e2` ／ 8,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0272.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0272.json) ／ SHA256: `fe4bef2a1d4bdd67317c18a4ab1ef8fbe90dee4553781af15b29c81ad99cc265` ／ 8,274 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0288.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0288.json) ／ SHA256: `eb170505ff462f87e4bfca3c0c783b0c17e3f6c51597c3c4c517fd890d5f16e8` ／ 6,988 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0304.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0304.json) ／ SHA256: `650099f557e6c011acc5ea8c06a1ee6bdd65cdaf7ca35418939922d460991319` ／ 8,049 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0320.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0320.json) ／ SHA256: `4717837afd26631cfd57914b0c92b87116f1b47a76db6cac7666774ca252d673` ／ 8,451 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0336.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0336.json) ／ SHA256: `b9bab461f2d8e41197e29a639c4325472bf147678ad9c048bf38808666fe6e75` ／ 6,985 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0352.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0352.json) ／ SHA256: `b45d88923e65796817db64fa6b60a2a331c3a57d95f7538399300342443402a2` ／ 8,047 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0368.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0368.json) ／ SHA256: `d8aaa3f59fc9353a22c1fa1863fdaaf350692e665cda3a437db6cd540294d263` ／ 8,031 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0384.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0384.json) ／ SHA256: `4805d0c58d5b6f267439038c30571f1a56c2bb3f05123f0b08ff59c8a0150763` ／ 6,901 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0400.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0400.json) ／ SHA256: `a439fb2c8530049730bdc4c022e23d47b4133b8aefb2cb8f2f71477dbe123a43` ／ 8,035 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0416.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0416.json) ／ SHA256: `ac219d32abbd2811f42aab7771506519bb601db8f1cd0a9f3283eed3168b49e8` ／ 8,044 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0432.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0432.json) ／ SHA256: `e2405ba9aba0930b2975e7d4e0b14edc9208b350c25f2471c1e18cdbb2ef4c0f` ／ 6,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0448.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0448.json) ／ SHA256: `4ed01e80afb5019086907d51883c74c95cfbf7539316d57f3ac4b592a095cfe6` ／ 7,953 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0464.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0464.json) ／ SHA256: `d998a7312a110a34c27e9ddb65c18f1a1d8c5b2fe47a72fcc0df5d2c74402524` ／ 8,199 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0480.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0480.json) ／ SHA256: `37a1ab57b3081d54d2c2f4d64e10b2a7b4db17edf77e04103d8d1f1313fbc848` ／ 6,899 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0496.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/0496.json) ／ SHA256: `bdf39da14891c7dbbc9b1d01e5b3087600d80d198892152c1457259460004b9d` ／ 7,961 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/natural100M/result.json) ／ SHA256: `9a58a643ab6de071619c088e0b97ca8c47cdd7e98b0ddd921ee3220d2e25fcaf` ／ 183,403 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "4ef0dedc2269ae585cd05d39c84fb6afc6676210d231d6ac26bafe622f4de1a3" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.51171875 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 3 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 84 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5234375 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 59 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.546875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 14 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 83 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 52 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 38 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.515625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 3 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 60 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0000.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0000.json) ／ SHA256: `f3417d39a30a195ae53e7498b52a6aa52923fa0081930c410cbc5616bbb9ea98` ／ 7,870 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0016.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0016.json) ／ SHA256: `1ad54bb669f69994bab276949c06eda80a57f9082165e3b3c617df1ea9998021` ／ 8,191 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0032.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0032.json) ／ SHA256: `b70cd493db4c3ff48ea62550d0784a1d3c476c239730be1f1fb6ce9fca3cc968` ／ 6,883 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0048.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0048.json) ／ SHA256: `b6c45761d3c837868f03008147cf498f08676c4227df1e56adb11311b6dc77fe` ／ 8,020 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0064.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0064.json) ／ SHA256: `b36da9d730a4e535ca9f4336dc018ba48fa356a6ff650fa538ebe50d056e544c` ／ 8,365 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0080.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0080.json) ／ SHA256: `ec4231b01dd83dfbc3b3d8a070f34b7470651bfa0c1bd0ae0c9737100e270de0` ／ 6,968 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0096.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0096.json) ／ SHA256: `2ceee920f4adc8544e44571079c246dbda5220ce7d185ecdf226821e2366468a` ／ 7,959 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0112.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0112.json) ／ SHA256: `a781fe1030d170ea4352205d84f935336b1db80b1ce56d7f85cdf7808eb0af0e` ／ 8,131 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0128.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0128.json) ／ SHA256: `1fd3c09ade655b49a6407f9de588222cffd05913de5dd6c405568e46b99d004b` ／ 6,985 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0144.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0144.json) ／ SHA256: `d98401527d452d09cdec4c5b4a2aef1d988c069c864246eb11de9959f82f7fe9` ／ 8,057 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0160.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0160.json) ／ SHA256: `d304329ac164a40a78d4f7fbfc83bec89e5a25a933ac930f45cb817ff11bc2c7` ／ 8,459 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0176.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0176.json) ／ SHA256: `98a72165eb35ff2cba92b0e5018a83d047e158b7d18011f8a019afb07903b734` ／ 6,818 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0192.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0192.json) ／ SHA256: `4593bf9aa96ae3a45df565c2b96cffc05c6496c73f7dbe262a806e8d1bc46e11` ／ 8,067 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0208.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0208.json) ／ SHA256: `b2bd10060f722de03b6fcb28f0e784c8258fcf2b8c17f9a766b7e76d97b5ffdb` ／ 8,391 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0224.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0224.json) ／ SHA256: `147143258b8b2e159af22478ba13fd240a2a93818de79d352eb856a4197307e2` ／ 6,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0240.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0240.json) ／ SHA256: `6beaee47f01dd0f153590f7910aea7312972d722ec0a598c74d554d1fd4ea4bb` ／ 8,229 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0256.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0256.json) ／ SHA256: `04812ccc7cfd7481ff72b95611c7a76eae626ef6f5c47c31106f2150048eb5fa` ／ 8,122 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0272.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0272.json) ／ SHA256: `923711e046a058642151f98d6fed31bd0981e07c6986a553db2e6fb977c95677` ／ 8,284 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0288.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0288.json) ／ SHA256: `75699d7181b9f5f99a5f8a725cdb597367cbf9e40af509c1ffb168d639013ef1` ／ 6,996 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0304.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0304.json) ／ SHA256: `b6acda1d007a1a0f307c3674956fcca9df532bb560f7e5a613a0fe23d72f9b98` ／ 8,055 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0320.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0320.json) ／ SHA256: `dcc6cc9db3818d21d13d9d8d9d498b654febc67282169f9c00a55e67777dc6b4` ／ 8,455 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0336.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0336.json) ／ SHA256: `85d5b4e64397fd646701c2ea45adf1067be01e0dd851d5166a62b2a72f75561b` ／ 6,981 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0352.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0352.json) ／ SHA256: `21bad98363ef53c8c30e2e67ddfaa15e81c23d57ac1ba006956f3c5640e5443d` ／ 8,049 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0368.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0368.json) ／ SHA256: `dfdb85831e2568804af31155746bfaed4a280ffd18ec229b57e2f3816ba89b35` ／ 8,020 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0384.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0384.json) ／ SHA256: `2014880aef2ed8758b2a74b1ec2bb00714416db70bed49e9bf9f14230aa83398` ／ 6,905 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0400.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0400.json) ／ SHA256: `e76bf0027aa4579981cc6412e2757992741e751357e3568c8a2e64fb641ffb97` ／ 8,018 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0416.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0416.json) ／ SHA256: `ff0e05e043488f18014b0937035672696d4da8af5f4e8799c684ce0a68107835` ／ 8,043 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0432.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0432.json) ／ SHA256: `2334a28da24269ff3e34d926c336bfa8d97c6705cd1ffb9aa90e7a6642f4b48b` ／ 6,992 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0448.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0448.json) ／ SHA256: `4262bf8668afb6225a28dc309e697a3765324b166b1e6d052f1ad67add9df53c` ／ 7,976 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0464.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0464.json) ／ SHA256: `f975ff5a57c16196ba0e3eb6e86a0fa6856fc10868881cfefb229591556f30c5` ／ 8,204 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0480.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0480.json) ／ SHA256: `0b761b6c342229c0735718176eda3c9e93ad93d4144aaec817a525ce4ecb1932` ／ 6,899 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0496.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/0496.json) ／ SHA256: `ceed7b5315f015cdc9a6f0c6e9307e584c1c62dab674566dde8eb540e49239fa` ／ 7,966 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/parent2B/result.json) ／ SHA256: `47883953661ad3eba4c2f87b48f7a8803cf517fb61bd4ce6f9417a7afe08eba5` ／ 183,358 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5078125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 5 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 1 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 13 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |

</details>

<details>
<summary>reports/phase6/condition_diversity_active_job.json — None</summary>

[原記録](../../reports/phase6/condition_diversity_active_job.json) ／ SHA256: `d950e4e829b4d73ba9f449396acc509c5605e6dd978f979e80b7a6a0f6fc942e` ／ 4,976 bytes

| 原キー | 保存値 |
|---|---|
| user_scope | "Base only; notify and stop after actual qualified Base completion; Chat/quantization deferred" |
| job.status | "complete" |
| job.GPU_elapsed_seconds | 113.42645317898132 |
| job.Base_adopted | false |
| job.protected_test_used | false |
| job.teachers | 24696536 |
| job.teacher_budget | 25000000 |
| job.source_teachers.web | 18521779 |
| job.source_teachers.story | 1234792 |
| job.source_teachers.ordinary_textbook | 2469974 |
| job.source_teachers.conditional_textbook | 2469991 |
| job.loss | 2.6440489292144775 |
| scientific_config | "configs/phase6/condition_diversity_comparison.json" |
| actual_probe_GPU_seconds | 11.799473121995106 |
| verification_teacher_tokens | 1299890 |
| actual_probe_all32_checks_passed | true |
| new_scientific_teacher_budget | 25000000 |
| reused_control_teacher_tokens | 25000000 |
| total_comparison_teacher_tokens | 50000000 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| note | "Terminal complete and actual process absent; historical heartbeat is not final teacher accounting. Never restart a completed job. New25M and reused25M distinct, original3 stream teachers identical. Final Base quality unmet; original10B UI restored and verified." |
| completed_scientific_teacher_tokens | 25000000 |
| authoritative_final_checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-diversity-comparison-20261006/large2048/training/checkpoint-00062936.pt" |
| authoritative_final_checkpoint.checkpoint_sha256 | "712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93" |
| authoritative_final_checkpoint.binding.config_sha256 | "87b4ed4070fb92d5c97ffbb9563d20ad3d649414d81c11426cabe0540a7f80d0" |
| authoritative_final_checkpoint.binding.arm | "large2048" |
| authoritative_final_checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| authoritative_final_checkpoint.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| authoritative_final_checkpoint.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| authoritative_final_checkpoint.binding.teacher_goals.web | 18750000 |
| authoritative_final_checkpoint.binding.teacher_goals.story | 1250000 |
| authoritative_final_checkpoint.binding.teacher_goals.ordinary_textbook | 2500000 |
| authoritative_final_checkpoint.binding.teacher_goals.conditional_textbook | 2500000 |
| authoritative_final_checkpoint.binding.optimizer_policy | "inherit" |
| authoritative_final_checkpoint.binding.peak_lr | 0.0002 |
| authoritative_final_checkpoint.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| authoritative_final_checkpoint.binding.study_kind | "nested_condition_source_quantity" |
| authoritative_final_checkpoint.binding.sampler_policy | "Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ." |
| authoritative_final_checkpoint.binding.outcome_weight | 1 |
| authoritative_final_checkpoint.binding.positive_manifest_sha256 | "cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280" |
| authoritative_final_checkpoint.update | 62936 |
| authoritative_final_checkpoint.tokens | 2062286848 |
| authoritative_final_checkpoint.supervised_tokens | 2045000000 |
| authoritative_final_checkpoint.additional_supervised_tokens | 25000000 |
| authoritative_final_checkpoint.additional_input_tokens | 25231360 |
| authoritative_final_checkpoint.source_teachers.web | 18750000 |
| authoritative_final_checkpoint.source_teachers.story | 1250000 |
| authoritative_final_checkpoint.source_teachers.ordinary_textbook | 2500000 |
| authoritative_final_checkpoint.source_teachers.conditional_textbook | 2500000 |
| authoritative_final_checkpoint.source_eos.web | 164131 |
| authoritative_final_checkpoint.source_eos.story | 9486 |
| authoritative_final_checkpoint.source_eos.ordinary_textbook | 18576 |
| authoritative_final_checkpoint.source_eos.conditional_textbook | 17514 |
| authoritative_final_checkpoint.source_input_tokens.web | 18934784 |
| authoritative_final_checkpoint.source_input_tokens.story | 1259520 |
| authoritative_final_checkpoint.source_input_tokens.ordinary_textbook | 2519040 |
| authoritative_final_checkpoint.source_input_tokens.conditional_textbook | 2518016 |
| authoritative_final_checkpoint.source_focus_teachers.web | 0 |
| authoritative_final_checkpoint.source_focus_teachers.story | 0 |
| authoritative_final_checkpoint.source_focus_teachers.ordinary_textbook | 0 |
| authoritative_final_checkpoint.source_focus_teachers.conditional_textbook | 654871 |
| authoritative_final_checkpoint.focus_teacher_tokens | 654871 |
| authoritative_final_checkpoint.focus_token_digest | "45d496b8d5bb369188109cec511fa64f1340374be30badaf9bce3ad77036f014" |
| authoritative_final_checkpoint.weighted_teacher_mass | 25000000 |
| authoritative_final_checkpoint.outcome_weight | 1 |
| authoritative_final_checkpoint.training_seconds | 39.85271529221791 |
| authoritative_final_checkpoint.completed_at | "2026-10-06T02:06:47.967298Z" |
| completion | "reports/phase6/condition_diversity_comparison_completion.json" |

</details>
