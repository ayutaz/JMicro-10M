# 評価・生成・意味診断 — 7/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/compare-result.json — actual_relation100M_reused_curriculum100M_complete_pending_new80</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/compare-result.json) ／ SHA256: `e12a38269ff4d14e77228a50b80246827b67883845679e259e1254f0b33153da` ／ 1,727,327 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.control.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.control.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.control.binding.arm | "curriculum" |
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
| checkpoints.control.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.control.update | 65249 |
| checkpoints.control.tokens | 2138079232 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 101023744 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 243066 |
| checkpoints.control.source_input_tokens.web | 75666432 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.control.focus_teacher_tokens | 1460032 |
| checkpoints.control.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 152.96801666589454 |
| checkpoints.control.completed_at | "2026-10-06T03:11:09.066152Z" |
| checkpoints.relation.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-relation-comparison-20261006/relation/training/checkpoint-00065249.pt" |
| checkpoints.relation.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| checkpoints.relation.binding.config_sha256 | "248651b0c7a25b3ab9950fce40f0e40a57b21a386201cf47c87eef4717911fac" |
| checkpoints.relation.binding.arm | "relation" |
| checkpoints.relation.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.relation.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.relation.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.relation.binding.teacher_goals.web | 75000000 |
| checkpoints.relation.binding.teacher_goals.story | 5000000 |
| checkpoints.relation.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.relation.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.relation.binding.optimizer_policy | "inherit" |
| checkpoints.relation.binding.peak_lr | 0.0002 |
| checkpoints.relation.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.relation.binding.study_kind | "conditional_relation_language_bridge_100M" |
| checkpoints.relation.binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| checkpoints.relation.binding.outcome_weight | 1 |
| checkpoints.relation.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.relation.update | 65249 |
| checkpoints.relation.tokens | 2138079232 |
| checkpoints.relation.supervised_tokens | 2120000000 |
| checkpoints.relation.additional_supervised_tokens | 100000000 |
| checkpoints.relation.additional_input_tokens | 101023744 |
| checkpoints.relation.source_teachers.web | 75000000 |
| checkpoints.relation.source_teachers.story | 5000000 |
| checkpoints.relation.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.relation.source_teachers.conditional_textbook | 10000000 |
| checkpoints.relation.source_eos.web | 656229 |
| checkpoints.relation.source_eos.story | 38240 |
| checkpoints.relation.source_eos.ordinary_textbook | 74183 |
| checkpoints.relation.source_eos.conditional_textbook | 234328 |
| checkpoints.relation.source_input_tokens.web | 75674624 |
| checkpoints.relation.source_input_tokens.story | 5039104 |
| checkpoints.relation.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.relation.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.relation.source_focus_teachers.web | 0 |
| checkpoints.relation.source_focus_teachers.story | 0 |
| checkpoints.relation.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.relation.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.relation.focus_teacher_tokens | 1407427 |
| checkpoints.relation.focus_token_digest | "c9002bb395ed970e032471a733915ff40ba9febb6866e9ed3df9a57fbc146cc4" |
| checkpoints.relation.weighted_teacher_mass | 100000000 |
| checkpoints.relation.outcome_weight | 1 |
| checkpoints.relation.training_seconds | 152.45355427256436 |
| checkpoints.relation.completed_at | "2026-10-06T03:30:00.690003Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| evaluations.control.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 369821.8238763809 |
| evaluations.control.body.eos_nll | 956.706282325089 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1302498889302441 |
| evaluations.control.body.seconds | 1.6376896990113892 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 45 |
| evaluations.control.greedy_rates.repetition | 17 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.53125 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.53125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5208333333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5203649397197785 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.041748286072343294 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8308157099697885] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.2868632707774799 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.26184092940125114, 0.3136729222520107] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.2868632707774799 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2752457551385165 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24932975871313673, 0.30116175156389635] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2752457551385165 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.27460276425066615 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.09421259981033882 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.relation.binding.teacher_goals.web | 75000000 |
| evaluations.relation.binding.teacher_goals.story | 5000000 |
| evaluations.relation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.relation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.relation.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.relation.binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| evaluations.relation.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| evaluations.relation.body.documents | 256 |
| evaluations.relation.body.limit_documents | 256 |
| evaluations.relation.body.body_nll | 369865.195435524 |
| evaluations.relation.body.eos_nll | 958.2584212049842 |
| evaluations.relation.body.body_bytes | 472055 |
| evaluations.relation.body.body_tokens | 122343 |
| evaluations.relation.body.bpb | 1.13038244113982 |
| evaluations.relation.body.seconds | 1.4164261220139451 |
| evaluations.relation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.relation.generation.max_new_tokens | 64 |
| evaluations.relation.greedy_rates.eos | 35 |
| evaluations.relation.greedy_rates.repetition | 21 |
| evaluations.relation.greedy_rates.unicode_failure | 0 |
| evaluations.relation.greedy_rates.role_leak | 0 |
| evaluations.relation.greedy_rates.empty | 0 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| evaluations.relation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5989583333333334 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6458333333333334] |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5989474540867537 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.mcc | 0.19792740520695654 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.relation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.relation.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7552870090634441 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7069486404833837, 0.8006042296072508] |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7552870090634441 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.43029259896729777 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.relation.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.relation.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.point | 0.29535299374441465 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.ci95 | [0.27031948168007147, 0.3221626452189455] |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.primary.hard_accuracy | 0.2949061662198391 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2837354781054513 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.258266309204647, 0.30966264521894543] |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826779114441843 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.mcc | 0.10444567591303532 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.relation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.semantic_both_contexts.correct | 23 |
| evaluations.relation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.relation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.relation.protected_test_used | false |
| transfer.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| transfer.parent2B.checks.weights_unchanged | true |
| transfer.parent2B.checks.no_gradients | true |
| transfer.parent2B.checks.eval_mode | true |
| transfer.parent2B.checks.RNG_restored | true |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.484375 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 3 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 9 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 113 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 5 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 55 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.5546875 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 21 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 100 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 13 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 53 |
| transfer.parent2B.optimizer_updates | 0 |
| transfer.parent2B.scientific_teacher_tokens | 0 |
| transfer.parent2B.protected_test_used | false |
| transfer.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| transfer.curriculum100M.checks.weights_unchanged | true |
| transfer.curriculum100M.checks.no_gradients | true |
| transfer.curriculum100M.checks.eval_mode | true |
| transfer.curriculum100M.checks.RNG_restored | true |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.578125 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 29 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.58984375 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 32 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5390625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 14 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 41 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 46 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.609375 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 36 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 84 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 94 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 38 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 45 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| transfer.curriculum100M.optimizer_updates | 0 |
| transfer.curriculum100M.scientific_teacher_tokens | 0 |
| transfer.curriculum100M.protected_test_used | false |
| transfer.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| transfer.relation100M.checks.weights_unchanged | true |
| transfer.relation100M.checks.no_gradients | true |
| transfer.relation100M.checks.eval_mode | true |
| transfer.relation100M.checks.RNG_restored | true |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.67578125 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 50 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.68359375 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 51 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 73 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69140625 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 54 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7734375 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 35 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 29 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| transfer.relation100M.optimizer_updates | 0 |
| transfer.relation100M.scientific_teacher_tokens | 0 |
| transfer.relation100M.protected_test_used | false |
| transfer.relation100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| retention.parent2B.checks.weights_unchanged | true |
| retention.parent2B.checks.no_gradients | true |
| retention.parent2B.checks.eval_mode | true |
| retention.parent2B.checks.RNG_restored | true |
| retention.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 5 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 1 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 13 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.parent2B.optimizer_updates | 0 |
| retention.parent2B.scientific_teacher_tokens | 0 |
| retention.parent2B.protected_test_used | false |
| retention.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| retention.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| retention.curriculum100M.checks.weights_unchanged | true |
| retention.curriculum100M.checks.no_gradients | true |
| retention.curriculum100M.checks.eval_mode | true |
| retention.curriculum100M.checks.RNG_restored | true |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 63 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 66 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.curriculum100M.optimizer_updates | 0 |
| retention.curriculum100M.scientific_teacher_tokens | 0 |
| retention.curriculum100M.protected_test_used | false |
| retention.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| retention.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| retention.relation100M.checks.weights_unchanged | true |
| retention.relation100M.checks.no_gradients | true |
| retention.relation100M.checks.eval_mode | true |
| retention.relation100M.checks.RNG_restored | true |
| retention.relation100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 78 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 44 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 80 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.relation100M.optimizer_updates | 0 |
| retention.relation100M.scientific_teacher_tokens | 0 |
| retention.relation100M.protected_test_used | false |
| retention.relation100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| status | "actual_relation100M_reused_curriculum100M_complete_pending_new80" |
| scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| total_comparison_teacher_tokens | 200000000 |
| verification_teacher_tokens | 1297767 |
| verification_GPU_seconds | 12.121268843999133 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 236.8989359900006 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/condition-pair-analysis.json — actual_relation100M_fixeddev_condition_pairs_reused</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/condition-pair-analysis.json) ／ SHA256: `2d254890b91e18b5e9a459079d996e1eb4a60124ffd1e1c180c889844995da13` ／ 185,891 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_relation100M_fixeddev_condition_pairs_reused" |
| models.relation100M.causality.accuracy | 0.6875 |
| models.relation100M.causality.both_correct | 6 |
| models.relation100M.causality.neither_correct | 0 |
| models.relation100M.comparison.accuracy | 0.46875 |
| models.relation100M.comparison.both_correct | 0 |
| models.relation100M.comparison.neither_correct | 1 |
| models.relation100M.coreference.accuracy | 0.53125 |
| models.relation100M.coreference.both_correct | 1 |
| models.relation100M.coreference.neither_correct | 0 |
| models.relation100M.negation.accuracy | 0.875 |
| models.relation100M.negation.both_correct | 12 |
| models.relation100M.negation.neither_correct | 0 |
| models.relation100M.quantity.accuracy | 0.5625 |
| models.relation100M.quantity.both_correct | 3 |
| models.relation100M.quantity.neither_correct | 1 |
| models.relation100M.time.accuracy | 0.5 |
| models.relation100M.time.both_correct | 1 |
| models.relation100M.time.neither_correct | 1 |
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
| references.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| references.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| references.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| CPU_seconds | 0.021571690012933686 |
| actual_GPU_seconds | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Same repeatedly inspected fixeddev96 families and one learned seed. Descriptive context response; not independent fluent continuation quality, causal diagnosis or certified10M capacity. Local generator probes remain separate." |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/body.json) ／ SHA256: `ebf7332de002b79accf92f1a72be7d9d3ab659e05cee5a74f3ebe7fbd44d175e` ／ 67,394 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 369865.195435524 |
| body.eos_nll | 958.2584212049842 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.13038244113982 |
| body.seconds | 1.4164261220139451 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/generation.json) ／ SHA256: `76297e0d8604bee0732b8c4509345f4947749d2635570c3d200520251a09877a` ／ 98,949 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/jblimp.json) ／ SHA256: `19c73cf3098ab1c931dd35bc1129f632ed70e6ff6d1d20504cdd2b7f15af27c6` ／ 338,686 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7854984894259819 |
| summary.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7854984894259819 |
| summary.per_token_secondary.accuracy.point | 0.7552870090634441 |
| summary.per_token_secondary.accuracy.ci95 | [0.7069486404833837, 0.8006042296072508] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7552870090634441 |
| summary.per_token_secondary.macro_f1 | 0.43029259896729777 |
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
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/jcqa.json) ／ SHA256: `629d131fd64f0ba97f397c01e7da979d8aaa7a453dc8cc9eb12fd35d7b20528f` ／ 1,639,685 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.29535299374441465 |
| summary.primary.accuracy.ci95 | [0.27031948168007147, 0.3221626452189455] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.2949061662198391 |
| summary.per_token_secondary.accuracy.point | 0.2837354781054513 |
| summary.per_token_secondary.accuracy.ci95 | [0.258266309204647, 0.30966264521894543] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| summary.per_token_secondary.macro_f1 | 0.2826779114441843 |
| summary.per_token_secondary.mcc | 0.10444567591303532 |
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
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/result.json) ／ SHA256: `e8a661a3f8949dcf86342c4bcf0fa91991c96b57c96eb64e235bd951d747a8ab` ／ 194,681 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 369865.195435524 |
| body.eos_nll | 958.2584212049842 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.13038244113982 |
| body.seconds | 1.4164261220139451 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 35 |
| greedy_rates.repetition | 21 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5989583333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6458333333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5989474540867537 |
| diagnostics.semantics.per_token_secondary.mcc | 0.19792740520695654 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7552870090634441 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7069486404833837, 0.8006042296072508] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7552870090634441 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.43029259896729777 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| diagnostics.jcqa.primary.accuracy.point | 0.29535299374441465 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.27031948168007147, 0.3221626452189455] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.2949061662198391 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2837354781054513 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.258266309204647, 0.30966264521894543] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826779114441843 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.10444567591303532 |
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
| diagnostics.semantic_both_contexts.correct | 23 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/evaluation/relation/evaluation/semantics.json) ／ SHA256: `2832f67be0ac71e0ffcdfe18264ff9272011e1423cac5ea77100188f13628e27` ／ 203,526 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.6041666666666666 |
| summary.primary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.6041666666666666 |
| summary.per_token_secondary.accuracy.point | 0.5989583333333334 |
| summary.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6458333333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| summary.per_token_secondary.macro_f1 | 0.5989474540867537 |
| summary.per_token_secondary.mcc | 0.19792740520695654 |
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
<summary>reports/phase6/condition-relation-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/job.json) ／ SHA256: `2d5180217c3df07bc4fc0e2e26bb02b3d4c57bd3dcfcb3e97c16122cf90b39b8` ／ 924 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 236.8989359900006 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99923211 |
| teacher_budget | 100000000 |
| source_teachers.web | 74941068 |
| source_teachers.story | 4996799 |
| source_teachers.ordinary_textbook | 9992813 |
| source_teachers.conditional_textbook | 9992531 |
| loss | 2.380946397781372 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/probe/job.json) ／ SHA256: `5b4cfc8c5f30b6fb0c3e5b97d01e885ebaa97c536f3cc5763a75bb6617dcbcfd` ／ 600 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 12.121268843999133 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/probe/result.json — actual_generated_curriculum_resume_timing_complete</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/probe/result.json) ／ SHA256: `03ec978d87852f2ef7d5d5e97b02c0784c65c3b7069f2d4240d1e995e94def28` ／ 68,784 bytes

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
| gate.verification_teacher_tokens | 259566 |
| timing.verification_teacher_tokens | 1038201 |
| timing.terminal_save_seconds | 0.180719780997606 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-relation-comparison-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "a46eed7d78538e9bad06e52c76a1a4f23099400f95398776a292d487e4eb514e" |
| verification_teacher_tokens | 1297767 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 12.121268843999133 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/probe/timing/latest.json) ／ SHA256: `5363e176276f21530881a444d54bd6b81fda471182f5f9827d084b6a1bbe432c` ／ 270 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/progress-result.json) ／ SHA256: `70492c432856676902e3b662356bbc78b5ffc54c0d0feef983d0a768d5ad3c8a` ／ 1,726,518 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-transfer-comparison-20261006/curriculum/training/checkpoint-00065249.pt" |
| checkpoints.control.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checkpoints.control.binding.config_sha256 | "ca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b" |
| checkpoints.control.binding.arm | "curriculum" |
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
| checkpoints.control.binding.study_kind | "self_contained_conditional_curriculum_replacement_100M" |
| checkpoints.control.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311" |
| checkpoints.control.update | 65249 |
| checkpoints.control.tokens | 2138079232 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 101023744 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 243066 |
| checkpoints.control.source_input_tokens.web | 75666432 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10243072 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 1460032 |
| checkpoints.control.focus_teacher_tokens | 1460032 |
| checkpoints.control.focus_token_digest | "a65727863872e01b99a904bfcc6c768c32273eb868b70017a4340a4153f66d48" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 152.96801666589454 |
| checkpoints.control.completed_at | "2026-10-06T03:11:09.066152Z" |
| checkpoints.relation.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-relation-comparison-20261006/relation/training/checkpoint-00065249.pt" |
| checkpoints.relation.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| checkpoints.relation.binding.config_sha256 | "248651b0c7a25b3ab9950fce40f0e40a57b21a386201cf47c87eef4717911fac" |
| checkpoints.relation.binding.arm | "relation" |
| checkpoints.relation.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.relation.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.relation.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.relation.binding.teacher_goals.web | 75000000 |
| checkpoints.relation.binding.teacher_goals.story | 5000000 |
| checkpoints.relation.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.relation.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.relation.binding.optimizer_policy | "inherit" |
| checkpoints.relation.binding.peak_lr | 0.0002 |
| checkpoints.relation.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.relation.binding.study_kind | "conditional_relation_language_bridge_100M" |
| checkpoints.relation.binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| checkpoints.relation.binding.outcome_weight | 1 |
| checkpoints.relation.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.relation.update | 65249 |
| checkpoints.relation.tokens | 2138079232 |
| checkpoints.relation.supervised_tokens | 2120000000 |
| checkpoints.relation.additional_supervised_tokens | 100000000 |
| checkpoints.relation.additional_input_tokens | 101023744 |
| checkpoints.relation.source_teachers.web | 75000000 |
| checkpoints.relation.source_teachers.story | 5000000 |
| checkpoints.relation.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.relation.source_teachers.conditional_textbook | 10000000 |
| checkpoints.relation.source_eos.web | 656229 |
| checkpoints.relation.source_eos.story | 38240 |
| checkpoints.relation.source_eos.ordinary_textbook | 74183 |
| checkpoints.relation.source_eos.conditional_textbook | 234328 |
| checkpoints.relation.source_input_tokens.web | 75674624 |
| checkpoints.relation.source_input_tokens.story | 5039104 |
| checkpoints.relation.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.relation.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.relation.source_focus_teachers.web | 0 |
| checkpoints.relation.source_focus_teachers.story | 0 |
| checkpoints.relation.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.relation.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.relation.focus_teacher_tokens | 1407427 |
| checkpoints.relation.focus_token_digest | "c9002bb395ed970e032471a733915ff40ba9febb6866e9ed3df9a57fbc146cc4" |
| checkpoints.relation.weighted_teacher_mass | 100000000 |
| checkpoints.relation.outcome_weight | 1 |
| checkpoints.relation.training_seconds | 152.45355427256436 |
| checkpoints.relation.completed_at | "2026-10-06T03:30:00.690003Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| evaluations.control.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 369821.8238763809 |
| evaluations.control.body.eos_nll | 956.706282325089 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1302498889302441 |
| evaluations.control.body.seconds | 1.6376896990113892 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 45 |
| evaluations.control.greedy_rates.repetition | 17 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.53125 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.53125 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5208333333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5203649397197785 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.041748286072343294 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8308157099697885] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.2868632707774799 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.26184092940125114, 0.3136729222520107] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.2868632707774799 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2752457551385165 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24932975871313673, 0.30116175156389635] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2752457551385165 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.27460276425066615 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.09421259981033882 |
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
| evaluations.control.diagnostics.semantic_both_contexts.correct | 12 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.relation.binding.teacher_goals.web | 75000000 |
| evaluations.relation.binding.teacher_goals.story | 5000000 |
| evaluations.relation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.relation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.relation.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.relation.binding.sampler_policy | "Fresh seed42 source fork from same2B+20M Adam/RNG parent; original3 teachers equal. Only negation/comparison language changes within same2048/facts/labels; other4 full texts fixed. Length/EOS/lexical and interleaving differences reported." |
| evaluations.relation.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| evaluations.relation.body.documents | 256 |
| evaluations.relation.body.limit_documents | 256 |
| evaluations.relation.body.body_nll | 369865.195435524 |
| evaluations.relation.body.eos_nll | 958.2584212049842 |
| evaluations.relation.body.body_bytes | 472055 |
| evaluations.relation.body.body_tokens | 122343 |
| evaluations.relation.body.bpb | 1.13038244113982 |
| evaluations.relation.body.seconds | 1.4164261220139451 |
| evaluations.relation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.relation.generation.max_new_tokens | 64 |
| evaluations.relation.greedy_rates.eos | 35 |
| evaluations.relation.greedy_rates.repetition | 21 |
| evaluations.relation.greedy_rates.unicode_failure | 0 |
| evaluations.relation.greedy_rates.role_leak | 0 |
| evaluations.relation.greedy_rates.empty | 0 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.ci95 | [0.5572916666666666, 0.6510416666666666] |
| evaluations.relation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5989583333333334 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6458333333333334] |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5989583333333334 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5989474540867537 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.mcc | 0.19792740520695654 |
| evaluations.relation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.relation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.relation.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.relation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.relation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.point | 0.7854984894259819 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7552870090634441 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7069486404833837, 0.8006042296072508] |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7552870090634441 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.43029259896729777 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.relation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.relation.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.relation.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.relation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.jblimp.raw_pair_accuracy | 0.8006042296072508 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.point | 0.29535299374441465 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.ci95 | [0.27031948168007147, 0.3221626452189455] |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.primary.hard_accuracy | 0.2949061662198391 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2837354781054513 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.258266309204647, 0.30966264521894543] |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28328865058087577 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2826779114441843 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.mcc | 0.10444567591303532 |
| evaluations.relation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.relation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.relation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.relation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.relation.diagnostics.semantic_both_contexts.correct | 23 |
| evaluations.relation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.relation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.relation.protected_test_used | false |
| transfer.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| transfer.parent2B.checks.weights_unchanged | true |
| transfer.parent2B.checks.no_gradients | true |
| transfer.parent2B.checks.eval_mode | true |
| transfer.parent2B.checks.RNG_restored | true |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 7 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.484375 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 3 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 9 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 113 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5078125 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 5 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.515625 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 4 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 55 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.5546875 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 21 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 100 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 13 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 47 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| transfer.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 53 |
| transfer.parent2B.optimizer_updates | 0 |
| transfer.parent2B.scientific_teacher_tokens | 0 |
| transfer.parent2B.protected_test_used | false |
| transfer.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| transfer.curriculum100M.checks.weights_unchanged | true |
| transfer.curriculum100M.checks.no_gradients | true |
| transfer.curriculum100M.checks.eval_mode | true |
| transfer.curriculum100M.checks.RNG_restored | true |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.578125 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 29 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 11 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.58984375 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 32 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 87 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.5390625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 14 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 41 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 46 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 51 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.609375 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 36 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 84 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 94 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.578125 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 38 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 45 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| transfer.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| transfer.curriculum100M.optimizer_updates | 0 |
| transfer.curriculum100M.scientific_teacher_tokens | 0 |
| transfer.curriculum100M.protected_test_used | false |
| transfer.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| transfer.relation100M.checks.weights_unchanged | true |
| transfer.relation100M.checks.no_gradients | true |
| transfer.relation100M.checks.eval_mode | true |
| transfer.relation100M.checks.RNG_restored | true |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.67578125 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 50 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 18 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.68359375 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 51 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 73 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| transfer.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69140625 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 54 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 69 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 114 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7734375 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 35 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 29 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 40 |
| transfer.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| transfer.relation100M.optimizer_updates | 0 |
| transfer.relation100M.scientific_teacher_tokens | 0 |
| transfer.relation100M.protected_test_used | false |
| transfer.relation100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.parent2B.checkpoint_sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| retention.parent2B.checks.weights_unchanged | true |
| retention.parent2B.checks.no_gradients | true |
| retention.parent2B.checks.eval_mode | true |
| retention.parent2B.checks.RNG_restored | true |
| retention.parent2B.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.all128.both_correct | 5 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5 |
| retention.parent2B.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 1 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.51171875 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 6 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 119 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.515625 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 4 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 58 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.53515625 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 13 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 111 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 82 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5625 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 11 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 50 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 39 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5078125 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 2 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 61 |
| retention.parent2B.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| retention.parent2B.optimizer_updates | 0 |
| retention.parent2B.scientific_teacher_tokens | 0 |
| retention.parent2B.protected_test_used | false |
| retention.parent2B.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| retention.curriculum100M.checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| retention.curriculum100M.checks.weights_unchanged | true |
| retention.curriculum100M.checks.no_gradients | true |
| retention.curriculum100M.checks.eval_mode | true |
| retention.curriculum100M.checks.RNG_restored | true |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 63 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 66 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| retention.curriculum100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| retention.curriculum100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.curriculum100M.optimizer_updates | 0 |
| retention.curriculum100M.scientific_teacher_tokens | 0 |
| retention.curriculum100M.protected_test_used | false |
| retention.curriculum100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |
| retention.relation100M.checkpoint_sha256 | "3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319a" |
| retention.relation100M.checks.weights_unchanged | true |
| retention.relation100M.checks.no_gradients | true |
| retention.relation100M.checks.eval_mode | true |
| retention.relation100M.checks.RNG_restored | true |
| retention.relation100M.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.relation100M.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 45 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 78 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.relation100M.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 44 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 80 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.7421875 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 31 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.relation100M.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 50 |
| retention.relation100M.optimizer_updates | 0 |
| retention.relation100M.scientific_teacher_tokens | 0 |
| retention.relation100M.protected_test_used | false |
| retention.relation100M.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/relation-content-review.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/relation-content-review.json) ／ SHA256: `5794db0f6b4f21f380a43179d7daf697c3c92bf585cb9fb801fad69d91a7bff6` ／ 950 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.13038244113982 |
| rates.eos | 35 |
| rates.repetition | 21 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 60 |
| relevance2 | 68 |
| coherent | 10 |
| appropriate | 21 |
| new_teacher_tokens | 100000000 |
| source_teacher_tokens.web | 75000000 |
| source_teacher_tokens.story | 5000000 |
| source_teacher_tokens.ordinary_textbook | 10000000 |
| source_teacher_tokens.conditional_textbook | 10000000 |
| conditional_source_documents | 2048 |
| generated_serialized_tokens | 89446 |
| notes_sha256 | "bfb81e36fed0748573541e7d0c128f312ff49422ea0988b93617f20b702da13e" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/relation/training/latest.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/relation/training/latest.json) ／ SHA256: `5cc3161f1810263799b79a2a87bf02309d607b6374bf5ff1124a2f60e7ab0a66` ／ 284 bytes

| 原キー | 保存値 |
|---|---|
| update | 65249 |
| tokens_seen | 2138079232 |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/retention-cases.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/retention-cases.json) ／ SHA256: `daf92018a167c24db83a4d3bd029d45973bd7f34f3fd452f52419ccc0b651d83` ／ 856,180 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>
