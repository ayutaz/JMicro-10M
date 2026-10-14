# 学習目的・最適化・正則化 — 14/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/result.json) ／ SHA256: `128a8783bb86ffe5fd33db5dcdcf571fd7c61d7a298028d94d4d8b8ebc8d9df8` ／ 174,173 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 324149.8256213665 |
| body.eos_nll | 555.5783282071352 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9906670746607233 |
| body.seconds | 1.286099833989283 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 67 |
| greedy_rates.repetition | 6 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.47903645833333336, 0.578125] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.4895833333333333 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.453125, 0.5208333333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.4895833333333333 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.4890843923101988 |
| diagnostics.semantics.per_token_secondary.mcc | -0.020874143036171647 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7552870090634441 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7098942598187311, 0.8006042296072508] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7552870090634441 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7764350453172205] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7643504531722054 |
| diagnostics.jcqa.primary.accuracy.point | 0.32171581769436997 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2949061662198391, 0.3485254691689008] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2940125111706881 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.32171581769436997] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2940125111706881 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29296810549471497 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.1178563840532624 |
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
| memory.maximum_observed_allocated_bytes | 315223040 |
| memory.maximum_observed_reserved_bytes | 13325303808 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/evaluation/parameter_anchor/evaluation/semantics.json) ／ SHA256: `54b14ccac8c43c06ca4fdbcfa08f78b7968568a4498aad3b6b19f045afdcf68f` ／ 203,291 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5260416666666666 |
| summary.primary.accuracy.ci95 | [0.47903645833333336, 0.578125] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5260416666666666 |
| summary.per_token_secondary.accuracy.point | 0.4895833333333333 |
| summary.per_token_secondary.accuracy.ci95 | [0.453125, 0.5208333333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.4895833333333333 |
| summary.per_token_secondary.macro_f1 | 0.4890843923101988 |
| summary.per_token_secondary.mcc | -0.020874143036171647 |
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
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/job.json) ／ SHA256: `31ab0b1b1a79e6278c5708e34b55c897f4f532acaf26bb182ba037112684c112` ／ 937 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 481.3385134199925 |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| loss | 0.2783910036087036 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE-content-notes.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE-content-notes.json) ／ SHA256: `366209389693d5b382ab5a4f4001e0dd6c52fd10c33f9304672a195607b51e69` ／ 25,511 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE/training/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE/training/latest.json) ／ SHA256: `dbdf270cb5c138fbb3877ed7d47f4af59c2a8980c29bd97d21bedb0ebe697bdb` ／ 298 bytes

| 原キー | 保存値 |
|---|---|
| update | 326571 |
| tokens_seen | 10701078528 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor-content-notes.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor-content-notes.json) ／ SHA256: `83e3ff51c39594a47db2165e4a79a490d66fed6bddd49e4a6e82c8ae3c83ef34` ／ 27,362 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor/training/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor/training/latest.json) ／ SHA256: `f64731ca4e859455f763c3ea4de85608c80ad7cf12d2f0e80eeb51cbe9e3fd63` ／ 297 bytes

| 原キー | 保存値 |
|---|---|
| update | 326571 |
| tokens_seen | 10701078528 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/job.json) ／ SHA256: `83dfaafcbed785c9d139fa69d1d91fc9986b7f0db6491285bc797c03fc03c04c` ／ 560 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 31.80234105398995 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/timing/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/timing/latest.json) ／ SHA256: `1e2403459328b193f7ed4e37ce68c5f7e19ce798232ece3492bc5872f044d125` ／ 293 bytes

| 原キー | 保存値 |
|---|---|
| update | 323535 |
| tokens_seen | 10601594880 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/timing/latest.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/timing/latest.json) ／ SHA256: `a8c7f4de07b539b47daf23764362d752e67f3141732db5d396f8939df6911b80` ／ 292 bytes

| 原キー | 保存値 |
|---|---|
| update | 323535 |
| tokens_seen | 10601594880 |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/progress-result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/progress-result.json) ／ SHA256: `dcf2dbeda5c397ae1e2efdea3eb620a507c5c35ea9dc00e6dbd117e6381d57af` ／ 157,255 bytes

| 原キー | 保存値 |
|---|---|
| gates.matched_staged_CE.passed | true |
| gates.matched_staged_CE.checks.model | true |
| gates.matched_staged_CE.checks.optimizer | true |
| gates.matched_staged_CE.checks.scheduler | true |
| gates.matched_staged_CE.checks.rng | true |
| gates.matched_staged_CE.checks.sampler | true |
| gates.matched_staged_CE.checks.lineage | true |
| gates.matched_staged_CE.checks.tokens | true |
| gates.matched_staged_CE.checks.supervised_tokens | true |
| gates.matched_staged_CE.checks.body_bytes | true |
| gates.matched_staged_CE.checks.token_digest | true |
| gates.matched_staged_CE.checks.focus_token_digest | true |
| gates.matched_staged_CE.checks.focus_teacher_tokens | true |
| gates.matched_staged_CE.checks.weighted_teacher_mass | true |
| gates.matched_staged_CE.checks.update | true |
| gates.matched_staged_CE.checks.spec | true |
| gates.matched_staged_CE.checks.model_config | true |
| gates.matched_staged_CE.checks.pilot_binding | true |
| gates.matched_staged_CE.checks.study_binding | true |
| gates.matched_staged_CE.checks.history_loss | true |
| gates.matched_staged_CE.checks.history_gradient_norm | true |
| gates.matched_staged_CE.checks.history_lr | true |
| gates.matched_staged_CE.checks.history_token_digest | true |
| gates.matched_staged_CE.checks.history_source_teachers | true |
| gates.matched_staged_CE.checks.history_source_eos | true |
| gates.matched_staged_CE.checks.history_source_input_tokens | true |
| gates.matched_staged_CE.checks.history_source_body_bytes | true |
| gates.matched_staged_CE.checks.history_source_focus_teachers | true |
| gates.matched_staged_CE.checks.history_focus_token_digest | true |
| gates.matched_staged_CE.checks.history_focus_teacher_tokens | true |
| gates.matched_staged_CE.checks.history_weighted_teacher_mass | true |
| gates.matched_staged_CE.checks.finite | true |
| gates.matched_staged_CE.checks.no_reheat | true |
| gates.matched_staged_CE.checks.history_CE_loss | true |
| gates.matched_staged_CE.checks.history_parameter_penalty | true |
| gates.matched_staged_CE.checks.history_parameter_coefficient | true |
| gates.matched_staged_CE.checks.history_parameter_penalty_teacher_tokens | true |
| gates.matched_staged_CE.GPU_optimizer_updates | 8 |
| gates.matched_staged_CE.verification_teacher_tokens | 261616 |
| gates.parameter_anchor.passed | true |
| gates.parameter_anchor.checks.model | true |
| gates.parameter_anchor.checks.optimizer | true |
| gates.parameter_anchor.checks.scheduler | true |
| gates.parameter_anchor.checks.rng | true |
| gates.parameter_anchor.checks.sampler | true |
| gates.parameter_anchor.checks.lineage | true |
| gates.parameter_anchor.checks.tokens | true |
| gates.parameter_anchor.checks.supervised_tokens | true |
| gates.parameter_anchor.checks.body_bytes | true |
| gates.parameter_anchor.checks.token_digest | true |
| gates.parameter_anchor.checks.focus_token_digest | true |
| gates.parameter_anchor.checks.focus_teacher_tokens | true |
| gates.parameter_anchor.checks.weighted_teacher_mass | true |
| gates.parameter_anchor.checks.update | true |
| gates.parameter_anchor.checks.spec | true |
| gates.parameter_anchor.checks.model_config | true |
| gates.parameter_anchor.checks.pilot_binding | true |
| gates.parameter_anchor.checks.study_binding | true |
| gates.parameter_anchor.checks.history_loss | true |
| gates.parameter_anchor.checks.history_gradient_norm | true |
| gates.parameter_anchor.checks.history_lr | true |
| gates.parameter_anchor.checks.history_token_digest | true |
| gates.parameter_anchor.checks.history_source_teachers | true |
| gates.parameter_anchor.checks.history_source_eos | true |
| gates.parameter_anchor.checks.history_source_input_tokens | true |
| gates.parameter_anchor.checks.history_source_body_bytes | true |
| gates.parameter_anchor.checks.history_source_focus_teachers | true |
| gates.parameter_anchor.checks.history_focus_token_digest | true |
| gates.parameter_anchor.checks.history_focus_teacher_tokens | true |
| gates.parameter_anchor.checks.history_weighted_teacher_mass | true |
| gates.parameter_anchor.checks.finite | true |
| gates.parameter_anchor.checks.no_reheat | true |
| gates.parameter_anchor.checks.history_CE_loss | true |
| gates.parameter_anchor.checks.history_parameter_penalty | true |
| gates.parameter_anchor.checks.history_parameter_coefficient | true |
| gates.parameter_anchor.checks.history_parameter_penalty_teacher_tokens | true |
| gates.parameter_anchor.GPU_optimizer_updates | 8 |
| gates.parameter_anchor.verification_teacher_tokens | 261616 |
| timings.matched_staged_CE.verification_teacher_tokens | 1046336 |
| timings.matched_staged_CE.terminal_save_seconds | 0.17116341899964027 |
| timings.matched_staged_CE.peak_VRAM_bytes | 6229116416 |
| timings.matched_staged_CE.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/timing/checkpoint.pt" |
| timings.matched_staged_CE.checkpoint.sha256 | "309d40e73e92009e6240f3317517b621810a37df74b56d3eaf93573d3e1be2b6" |
| timings.parameter_anchor.verification_teacher_tokens | 1046336 |
| timings.parameter_anchor.terminal_save_seconds | 0.1693566159810871 |
| timings.parameter_anchor.peak_VRAM_bytes | 6229116416 |
| timings.parameter_anchor.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/timing/checkpoint.pt" |
| timings.parameter_anchor.checkpoint.sha256 | "124925d67094972c244dcff89633c0e4732a8b658533a6be5b5562861dfca0e6" |
| initial_fullstate_preservation.matched_staged_CE.parent_sampler_lineage | true |
| initial_fullstate_preservation.matched_staged_CE.all_checks | true |
| initial_fullstate_preservation.parameter_anchor.parent_sampler_lineage | true |
| initial_fullstate_preservation.parameter_anchor.all_checks | true |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/probe/result.json — own_two_arm_probe_complete</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/probe/result.json) ／ SHA256: `8370aafec79f7d8058ad0e6893e12fe1886cd36fa04241a5d19c52bc63f0b537` ／ 157,765 bytes

| 原キー | 保存値 |
|---|---|
| gates.matched_staged_CE.passed | true |
| gates.matched_staged_CE.checks.model | true |
| gates.matched_staged_CE.checks.optimizer | true |
| gates.matched_staged_CE.checks.scheduler | true |
| gates.matched_staged_CE.checks.rng | true |
| gates.matched_staged_CE.checks.sampler | true |
| gates.matched_staged_CE.checks.lineage | true |
| gates.matched_staged_CE.checks.tokens | true |
| gates.matched_staged_CE.checks.supervised_tokens | true |
| gates.matched_staged_CE.checks.body_bytes | true |
| gates.matched_staged_CE.checks.token_digest | true |
| gates.matched_staged_CE.checks.focus_token_digest | true |
| gates.matched_staged_CE.checks.focus_teacher_tokens | true |
| gates.matched_staged_CE.checks.weighted_teacher_mass | true |
| gates.matched_staged_CE.checks.update | true |
| gates.matched_staged_CE.checks.spec | true |
| gates.matched_staged_CE.checks.model_config | true |
| gates.matched_staged_CE.checks.pilot_binding | true |
| gates.matched_staged_CE.checks.study_binding | true |
| gates.matched_staged_CE.checks.history_loss | true |
| gates.matched_staged_CE.checks.history_gradient_norm | true |
| gates.matched_staged_CE.checks.history_lr | true |
| gates.matched_staged_CE.checks.history_token_digest | true |
| gates.matched_staged_CE.checks.history_source_teachers | true |
| gates.matched_staged_CE.checks.history_source_eos | true |
| gates.matched_staged_CE.checks.history_source_input_tokens | true |
| gates.matched_staged_CE.checks.history_source_body_bytes | true |
| gates.matched_staged_CE.checks.history_source_focus_teachers | true |
| gates.matched_staged_CE.checks.history_focus_token_digest | true |
| gates.matched_staged_CE.checks.history_focus_teacher_tokens | true |
| gates.matched_staged_CE.checks.history_weighted_teacher_mass | true |
| gates.matched_staged_CE.checks.finite | true |
| gates.matched_staged_CE.checks.no_reheat | true |
| gates.matched_staged_CE.checks.history_CE_loss | true |
| gates.matched_staged_CE.checks.history_parameter_penalty | true |
| gates.matched_staged_CE.checks.history_parameter_coefficient | true |
| gates.matched_staged_CE.checks.history_parameter_penalty_teacher_tokens | true |
| gates.matched_staged_CE.GPU_optimizer_updates | 8 |
| gates.matched_staged_CE.verification_teacher_tokens | 261616 |
| gates.parameter_anchor.passed | true |
| gates.parameter_anchor.checks.model | true |
| gates.parameter_anchor.checks.optimizer | true |
| gates.parameter_anchor.checks.scheduler | true |
| gates.parameter_anchor.checks.rng | true |
| gates.parameter_anchor.checks.sampler | true |
| gates.parameter_anchor.checks.lineage | true |
| gates.parameter_anchor.checks.tokens | true |
| gates.parameter_anchor.checks.supervised_tokens | true |
| gates.parameter_anchor.checks.body_bytes | true |
| gates.parameter_anchor.checks.token_digest | true |
| gates.parameter_anchor.checks.focus_token_digest | true |
| gates.parameter_anchor.checks.focus_teacher_tokens | true |
| gates.parameter_anchor.checks.weighted_teacher_mass | true |
| gates.parameter_anchor.checks.update | true |
| gates.parameter_anchor.checks.spec | true |
| gates.parameter_anchor.checks.model_config | true |
| gates.parameter_anchor.checks.pilot_binding | true |
| gates.parameter_anchor.checks.study_binding | true |
| gates.parameter_anchor.checks.history_loss | true |
| gates.parameter_anchor.checks.history_gradient_norm | true |
| gates.parameter_anchor.checks.history_lr | true |
| gates.parameter_anchor.checks.history_token_digest | true |
| gates.parameter_anchor.checks.history_source_teachers | true |
| gates.parameter_anchor.checks.history_source_eos | true |
| gates.parameter_anchor.checks.history_source_input_tokens | true |
| gates.parameter_anchor.checks.history_source_body_bytes | true |
| gates.parameter_anchor.checks.history_source_focus_teachers | true |
| gates.parameter_anchor.checks.history_focus_token_digest | true |
| gates.parameter_anchor.checks.history_focus_teacher_tokens | true |
| gates.parameter_anchor.checks.history_weighted_teacher_mass | true |
| gates.parameter_anchor.checks.finite | true |
| gates.parameter_anchor.checks.no_reheat | true |
| gates.parameter_anchor.checks.history_CE_loss | true |
| gates.parameter_anchor.checks.history_parameter_penalty | true |
| gates.parameter_anchor.checks.history_parameter_coefficient | true |
| gates.parameter_anchor.checks.history_parameter_penalty_teacher_tokens | true |
| gates.parameter_anchor.GPU_optimizer_updates | 8 |
| gates.parameter_anchor.verification_teacher_tokens | 261616 |
| timings.matched_staged_CE.verification_teacher_tokens | 1046336 |
| timings.matched_staged_CE.terminal_save_seconds | 0.17116341899964027 |
| timings.matched_staged_CE.peak_VRAM_bytes | 6229116416 |
| timings.matched_staged_CE.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/probe/matched_staged_CE/timing/checkpoint.pt" |
| timings.matched_staged_CE.checkpoint.sha256 | "309d40e73e92009e6240f3317517b621810a37df74b56d3eaf93573d3e1be2b6" |
| timings.parameter_anchor.verification_teacher_tokens | 1046336 |
| timings.parameter_anchor.terminal_save_seconds | 0.1693566159810871 |
| timings.parameter_anchor.peak_VRAM_bytes | 6229116416 |
| timings.parameter_anchor.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/probe/parameter_anchor/timing/checkpoint.pt" |
| timings.parameter_anchor.checkpoint.sha256 | "124925d67094972c244dcff89633c0e4732a8b658533a6be5b5562861dfca0e6" |
| initial_fullstate_preservation.matched_staged_CE.parent_sampler_lineage | true |
| initial_fullstate_preservation.matched_staged_CE.all_checks | true |
| initial_fullstate_preservation.parameter_anchor.parent_sampler_lineage | true |
| initial_fullstate_preservation.parameter_anchor.all_checks | true |
| passed | true |
| scientific_teacher_tokens | 0 |
| GPU_optimizer_updates | 80 |
| verification_teacher_tokens | 2615904 |
| status | "own_two_arm_probe_complete" |
| GPU_seconds | 31.80234105398995 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/progress-result.json) ／ SHA256: `ebcc4fc16ecefb8c19c73f76065a39cb7a2ddbc0e487e9b1f8a2bd5a1ef78915` ／ 1,256,802 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.matched_staged_CE.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/matched_staged_CE/training/checkpoint-00326571.pt" |
| checkpoints.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| checkpoints.matched_staged_CE.binding.config_sha256 | "7fb897e9905eceaecc754a4d323f2e8d90c68e47e592872c8f20cf980721e249" |
| checkpoints.matched_staged_CE.binding.arm | "matched_staged_CE" |
| checkpoints.matched_staged_CE.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.matched_staged_CE.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.matched_staged_CE.binding.teacher_goals.web | 75000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.story | 5000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.binding.study_kind | "mixed_fullstate_matched_staged_parameter_displacement_v1" |
| checkpoints.matched_staged_CE.binding.parameter_coefficient | 0.0 |
| checkpoints.matched_staged_CE.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.matched_staged_CE.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.matched_staged_CE.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.matched_staged_CE.binding.optimizer_policy | "inherit" |
| checkpoints.matched_staged_CE.binding.peak_lr | 1e-05 |
| checkpoints.matched_staged_CE.update | 326571 |
| checkpoints.matched_staged_CE.tokens | 10701078528 |
| checkpoints.matched_staged_CE.supervised_tokens | 10677786961 |
| checkpoints.matched_staged_CE.additional_supervised_tokens | 100000000 |
| checkpoints.matched_staged_CE.additional_input_tokens | 100532224 |
| checkpoints.matched_staged_CE.source_teachers.web | 75000000 |
| checkpoints.matched_staged_CE.source_teachers.story | 5000000 |
| checkpoints.matched_staged_CE.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.source_teachers.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.source_eos.web | 159447 |
| checkpoints.matched_staged_CE.source_eos.story | 38240 |
| checkpoints.matched_staged_CE.source_eos.ordinary_textbook | 74183 |
| checkpoints.matched_staged_CE.source_eos.conditional_textbook | 234328 |
| checkpoints.matched_staged_CE.source_input_tokens.web | 75183104 |
| checkpoints.matched_staged_CE.source_input_tokens.story | 5039104 |
| checkpoints.matched_staged_CE.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.matched_staged_CE.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.matched_staged_CE.source_focus_teachers.web | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.story | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.matched_staged_CE.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.matched_staged_CE.focus_teacher_tokens | 1407427 |
| checkpoints.matched_staged_CE.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.matched_staged_CE.weighted_teacher_mass | 100000000 |
| checkpoints.matched_staged_CE.outcome_weight | 1 |
| checkpoints.matched_staged_CE.training_seconds | 183.06313274789136 |
| checkpoints.matched_staged_CE.completed_at | "2026-10-06T10:16:39.374828Z" |
| checkpoints.matched_staged_CE.parameter_coefficient | 0.0 |
| checkpoints.matched_staged_CE.parameter_penalty_teacher_tokens | 0 |
| checkpoints.matched_staged_CE.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.matched_staged_CE.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.matched_staged_CE.sampler.goals.web | 75000000 |
| checkpoints.matched_staged_CE.sampler.goals.story | 5000000 |
| checkpoints.matched_staged_CE.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.context | 1024 |
| checkpoints.matched_staged_CE.sampler.seed | 42 |
| checkpoints.matched_staged_CE.sampler.position | 3068 |
| checkpoints.matched_staged_CE.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.matched_staged_CE.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.context | 1024 |
| checkpoints.matched_staged_CE.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.matched_staged_CE.sampler.streams.story.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.story.genre | "story" |
| checkpoints.matched_staged_CE.sampler.streams.story.documents | 761448 |
| checkpoints.matched_staged_CE.sampler.streams.story.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.story.document_position | 38243 |
| checkpoints.matched_staged_CE.sampler.streams.story.token_offset | 87 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.matched_staged_CE.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.matched_staged_CE.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.matched_staged_CE.sampler.source_teachers.web | 75000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.story | 5000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.matched_staged_CE.sampler.source_eos.web | 159447 |
| checkpoints.matched_staged_CE.sampler.source_eos.story | 38240 |
| checkpoints.matched_staged_CE.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.matched_staged_CE.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.matched_staged_CE.sampler.source_tokens.web | 75183104 |
| checkpoints.matched_staged_CE.sampler.source_tokens.story | 5039104 |
| checkpoints.matched_staged_CE.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.matched_staged_CE.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.web | 292167653 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.story | 20452979 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.matched_staged_CE.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.web | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.story | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.matched_staged_CE.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.matched_staged_CE.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.matched_staged_CE.source_body_bytes.web | 292167653 |
| checkpoints.matched_staged_CE.source_body_bytes.story | 20452979 |
| checkpoints.matched_staged_CE.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.matched_staged_CE.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.matched_staged_CE.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| checkpoints.parameter_anchor.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/parameter-displacement-anchor-v3-20261006/parameter_anchor/training/checkpoint-00326571.pt" |
| checkpoints.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| checkpoints.parameter_anchor.binding.config_sha256 | "7fb897e9905eceaecc754a4d323f2e8d90c68e47e592872c8f20cf980721e249" |
| checkpoints.parameter_anchor.binding.arm | "parameter_anchor" |
| checkpoints.parameter_anchor.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.parameter_anchor.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.parameter_anchor.binding.teacher_goals.web | 75000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.story | 5000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.binding.study_kind | "mixed_fullstate_matched_staged_parameter_displacement_v1" |
| checkpoints.parameter_anchor.binding.parameter_coefficient | 0.04161064039180984 |
| checkpoints.parameter_anchor.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.parameter_anchor.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.parameter_anchor.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.parameter_anchor.binding.optimizer_policy | "inherit" |
| checkpoints.parameter_anchor.binding.peak_lr | 1e-05 |
| checkpoints.parameter_anchor.update | 326571 |
| checkpoints.parameter_anchor.tokens | 10701078528 |
| checkpoints.parameter_anchor.supervised_tokens | 10677786961 |
| checkpoints.parameter_anchor.additional_supervised_tokens | 100000000 |
| checkpoints.parameter_anchor.additional_input_tokens | 100532224 |
| checkpoints.parameter_anchor.source_teachers.web | 75000000 |
| checkpoints.parameter_anchor.source_teachers.story | 5000000 |
| checkpoints.parameter_anchor.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.source_teachers.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.source_eos.web | 159447 |
| checkpoints.parameter_anchor.source_eos.story | 38240 |
| checkpoints.parameter_anchor.source_eos.ordinary_textbook | 74183 |
| checkpoints.parameter_anchor.source_eos.conditional_textbook | 234328 |
| checkpoints.parameter_anchor.source_input_tokens.web | 75183104 |
| checkpoints.parameter_anchor.source_input_tokens.story | 5039104 |
| checkpoints.parameter_anchor.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.parameter_anchor.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.parameter_anchor.source_focus_teachers.web | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.story | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.parameter_anchor.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.parameter_anchor.focus_teacher_tokens | 1407427 |
| checkpoints.parameter_anchor.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.parameter_anchor.weighted_teacher_mass | 100000000 |
| checkpoints.parameter_anchor.outcome_weight | 1 |
| checkpoints.parameter_anchor.training_seconds | 172.07054460450308 |
| checkpoints.parameter_anchor.completed_at | "2026-10-06T10:20:34.571311Z" |
| checkpoints.parameter_anchor.parameter_coefficient | 0.04161064039180984 |
| checkpoints.parameter_anchor.parameter_penalty_teacher_tokens | 0 |
| checkpoints.parameter_anchor.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.parameter_anchor.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.parameter_anchor.sampler.goals.web | 75000000 |
| checkpoints.parameter_anchor.sampler.goals.story | 5000000 |
| checkpoints.parameter_anchor.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.context | 1024 |
| checkpoints.parameter_anchor.sampler.seed | 42 |
| checkpoints.parameter_anchor.sampler.position | 3068 |
| checkpoints.parameter_anchor.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.parameter_anchor.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.context | 1024 |
| checkpoints.parameter_anchor.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.parameter_anchor.sampler.streams.story.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.story.genre | "story" |
| checkpoints.parameter_anchor.sampler.streams.story.documents | 761448 |
| checkpoints.parameter_anchor.sampler.streams.story.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.story.document_position | 38243 |
| checkpoints.parameter_anchor.sampler.streams.story.token_offset | 87 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.parameter_anchor.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.parameter_anchor.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.parameter_anchor.sampler.source_teachers.web | 75000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.story | 5000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.parameter_anchor.sampler.source_eos.web | 159447 |
| checkpoints.parameter_anchor.sampler.source_eos.story | 38240 |
| checkpoints.parameter_anchor.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.parameter_anchor.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.parameter_anchor.sampler.source_tokens.web | 75183104 |
| checkpoints.parameter_anchor.sampler.source_tokens.story | 5039104 |
| checkpoints.parameter_anchor.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.parameter_anchor.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.web | 292167653 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.story | 20452979 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.parameter_anchor.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.web | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.story | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.parameter_anchor.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.parameter_anchor.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.parameter_anchor.source_body_bytes.web | 292167653 |
| checkpoints.parameter_anchor.source_body_bytes.story | 20452979 |
| checkpoints.parameter_anchor.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.parameter_anchor.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.parameter_anchor.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| evaluations.matched_staged_CE.binding.teacher_goals.web | 75000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.story | 5000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.matched_staged_CE.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| evaluations.matched_staged_CE.body.documents | 256 |
| evaluations.matched_staged_CE.body.limit_documents | 256 |
| evaluations.matched_staged_CE.body.body_nll | 338873.8658795357 |
| evaluations.matched_staged_CE.body.eos_nll | 526.858716275543 |
| evaluations.matched_staged_CE.body.body_bytes | 472055 |
| evaluations.matched_staged_CE.body.body_tokens | 122343 |
| evaluations.matched_staged_CE.body.bpb | 1.0356667036495277 |
| evaluations.matched_staged_CE.body.seconds | 1.3664823299914133 |
| evaluations.matched_staged_CE.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.matched_staged_CE.generation.max_new_tokens | 64 |
| evaluations.matched_staged_CE.greedy_rates.eos | 69 |
| evaluations.matched_staged_CE.greedy_rates.repetition | 6 |
| evaluations.matched_staged_CE.greedy_rates.unicode_failure | 0 |
| evaluations.matched_staged_CE.greedy_rates.role_leak | 0 |
| evaluations.matched_staged_CE.greedy_rates.empty | 0 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.point | 0.5416666666666666 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.ci95 | [0.5, 0.5833333333333334] |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.primary.hard_accuracy | 0.5416666666666666 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4739583333333333, 0.5260416666666666] |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.macro_f1 | 0.49978289188015634 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.matched_staged_CE.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.point | 0.7613293051359517 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.ci95 | [0.716012084592145, 0.8066465256797583] |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.primary.hard_accuracy | 0.7613293051359517 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.matched_staged_CE.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.matched_staged_CE.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.ci95 | [0.27164879356568367, 0.3235254691689007] |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2806076854334227 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.25466934763181415, 0.30654602323503116] |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2806076854334227 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2797558541778977 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.mcc | 0.1012522601643278 |
| evaluations.matched_staged_CE.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.matched_staged_CE.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.matched_staged_CE.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.matched_staged_CE.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.matched_staged_CE.diagnostics.semantic_both_contexts.correct | 13 |
| evaluations.matched_staged_CE.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.matched_staged_CE.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.matched_staged_CE.protected_test_used | false |
| evaluations.parameter_anchor.binding.teacher_goals.web | 75000000 |
| evaluations.parameter_anchor.binding.teacher_goals.story | 5000000 |
| evaluations.parameter_anchor.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.parameter_anchor.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| evaluations.parameter_anchor.body.documents | 256 |
| evaluations.parameter_anchor.body.limit_documents | 256 |
| evaluations.parameter_anchor.body.body_nll | 324149.8256213665 |
| evaluations.parameter_anchor.body.eos_nll | 555.5783282071352 |
| evaluations.parameter_anchor.body.body_bytes | 472055 |
| evaluations.parameter_anchor.body.body_tokens | 122343 |
| evaluations.parameter_anchor.body.bpb | 0.9906670746607233 |
| evaluations.parameter_anchor.body.seconds | 1.286099833989283 |
| evaluations.parameter_anchor.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.parameter_anchor.generation.max_new_tokens | 64 |
| evaluations.parameter_anchor.greedy_rates.eos | 67 |
| evaluations.parameter_anchor.greedy_rates.repetition | 6 |
| evaluations.parameter_anchor.greedy_rates.unicode_failure | 0 |
| evaluations.parameter_anchor.greedy_rates.role_leak | 0 |
| evaluations.parameter_anchor.greedy_rates.empty | 0 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.ci95 | [0.47903645833333336, 0.578125] |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.point | 0.4895833333333333 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.453125, 0.5208333333333334] |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.4895833333333333 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.macro_f1 | 0.4890843923101988 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.mcc | -0.020874143036171647 |
| evaluations.parameter_anchor.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.point | 0.7552870090634441 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.ci95 | [0.7098942598187311, 0.8006042296072508] |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.primary.hard_accuracy | 0.7552870090634441 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7764350453172205] |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.parameter_anchor.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.parameter_anchor.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.jblimp.raw_pair_accuracy | 0.7643504531722054 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.point | 0.32171581769436997 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.ci95 | [0.2949061662198391, 0.3485254691689008] |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.primary.hard_accuracy | 0.32171581769436997 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2940125111706881 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.32171581769436997] |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2940125111706881 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29296810549471497 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.mcc | 0.1178563840532624 |
| evaluations.parameter_anchor.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.parameter_anchor.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.parameter_anchor.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.parameter_anchor.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.parameter_anchor.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.parameter_anchor.memory.maximum_observed_allocated_bytes | 315223040 |
| evaluations.parameter_anchor.memory.maximum_observed_reserved_bytes | 13325303808 |
| evaluations.parameter_anchor.protected_test_used | false |
| transfer.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| transfer.matched_staged_CE.checks.weights_unchanged | true |
| transfer.matched_staged_CE.checks.no_gradients | true |
| transfer.matched_staged_CE.checks.eval_mode | true |
| transfer.matched_staged_CE.checks.RNG_restored | true |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.75 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.both_correct | 74 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 49 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 25 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.74609375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 73 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 45 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| transfer.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.75390625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 75 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 43 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 31 |
| transfer.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| transfer.matched_staged_CE.optimizer_updates | 0 |
| transfer.matched_staged_CE.scientific_teacher_tokens | 0 |
| transfer.matched_staged_CE.protected_test_used | false |
| transfer.matched_staged_CE.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| transfer.parameter_anchor.checks.weights_unchanged | true |
| transfer.parameter_anchor.checks.no_gradients | true |
| transfer.parameter_anchor.checks.eval_mode | true |
| transfer.parameter_anchor.checks.RNG_restored | true |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7421875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 70 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 47 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| transfer.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 69 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 21 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| transfer.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7421875 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 50 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.parameter_anchor.optimizer_updates | 0 |
| transfer.parameter_anchor.scientific_teacher_tokens | 0 |
| transfer.parameter_anchor.protected_test_used | false |
| transfer.parameter_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.matched_staged_CE.checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| retention.matched_staged_CE.checks.weights_unchanged | true |
| retention.matched_staged_CE.checks.no_gradients | true |
| retention.matched_staged_CE.checks.eval_mode | true |
| retention.matched_staged_CE.checks.RNG_restored | true |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.all128.both_correct | 47 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.matched_staged_CE.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7109375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 66 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 19 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69921875 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| retention.matched_staged_CE.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.matched_staged_CE.optimizer_updates | 0 |
| retention.matched_staged_CE.scientific_teacher_tokens | 0 |
| retention.matched_staged_CE.protected_test_used | false |
| retention.matched_staged_CE.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.parameter_anchor.checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| retention.parameter_anchor.checks.weights_unchanged | true |
| retention.parameter_anchor.checks.no_gradients | true |
| retention.parameter_anchor.checks.eval_mode | true |
| retention.parameter_anchor.checks.RNG_restored | true |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.all128.both_correct | 47 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.parameter_anchor.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 14 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 39 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.578125 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 44 |
| retention.parameter_anchor.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6953125 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 56 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 66 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 40 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 23 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 57 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 43 |
| retention.parameter_anchor.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| retention.parameter_anchor.optimizer_updates | 0 |
| retention.parameter_anchor.scientific_teacher_tokens | 0 |
| retention.parameter_anchor.protected_test_used | false |
| retention.parameter_anchor.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/review.json — both100M_all160_content_accounting_and_double_controls_reviewed</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/review.json) ／ SHA256: `d1360f469c2410dadf288e6a987996fa4a65137d1b610c034f11e4a79ee02c2b` ／ 5,491 bytes

| 原キー | 保存値 |
|---|---|
| status | "both100M_all160_content_accounting_and_double_controls_reviewed" |
| summaries.matched_staged_CE.BPB | 1.0356667036495277 |
| summaries.matched_staged_CE.rates.eos | 69 |
| summaries.matched_staged_CE.rates.repetition | 6 |
| summaries.matched_staged_CE.rates.unicode_failure | 0 |
| summaries.matched_staged_CE.rates.role_leak | 0 |
| summaries.matched_staged_CE.rates.empty | 0 |
| summaries.matched_staged_CE.grammar2 | 65 |
| summaries.matched_staged_CE.relevance2 | 52 |
| summaries.matched_staged_CE.coherent | 32 |
| summaries.matched_staged_CE.appropriate | 37 |
| summaries.matched_staged_CE.notes_sha256 | "366209389693d5b382ab5a4f4001e0dd6c52fd10c33f9304672a195607b51e69" |
| summaries.parameter_anchor.BPB | 0.9906670746607233 |
| summaries.parameter_anchor.rates.eos | 67 |
| summaries.parameter_anchor.rates.repetition | 6 |
| summaries.parameter_anchor.rates.unicode_failure | 0 |
| summaries.parameter_anchor.rates.role_leak | 0 |
| summaries.parameter_anchor.rates.empty | 0 |
| summaries.parameter_anchor.grammar2 | 59 |
| summaries.parameter_anchor.relevance2 | 60 |
| summaries.parameter_anchor.coherent | 25 |
| summaries.parameter_anchor.appropriate | 29 |
| summaries.parameter_anchor.notes_sha256 | "83e3ff51c39594a47db2165e4a79a490d66fed6bddd49e4a6e82c8ae3c83ef34" |
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
| accounting.matched_staged_CE.completed_updates | 3068 |
| accounting.matched_staged_CE.teachers | 100000000 |
| accounting.matched_staged_CE.physical_input_positions | 100532224 |
| accounting.matched_staged_CE.parameter_penalty_teacher_tokens | 0 |
| accounting.matched_staged_CE.source_teachers.web | 75000000 |
| accounting.matched_staged_CE.source_teachers.story | 5000000 |
| accounting.matched_staged_CE.source_teachers.ordinary_textbook | 10000000 |
| accounting.matched_staged_CE.source_teachers.conditional_textbook | 10000000 |
| accounting.matched_staged_CE.source_EOS.web | 159447 |
| accounting.matched_staged_CE.source_EOS.story | 38240 |
| accounting.matched_staged_CE.source_EOS.ordinary_textbook | 74183 |
| accounting.matched_staged_CE.source_EOS.conditional_textbook | 234328 |
| accounting.parameter_anchor.completed_updates | 3068 |
| accounting.parameter_anchor.teachers | 100000000 |
| accounting.parameter_anchor.physical_input_positions | 100532224 |
| accounting.parameter_anchor.parameter_penalty_teacher_tokens | 0 |
| accounting.parameter_anchor.source_teachers.web | 75000000 |
| accounting.parameter_anchor.source_teachers.story | 5000000 |
| accounting.parameter_anchor.source_teachers.ordinary_textbook | 10000000 |
| accounting.parameter_anchor.source_teachers.conditional_textbook | 10000000 |
| accounting.parameter_anchor.source_EOS.web | 159447 |
| accounting.parameter_anchor.source_EOS.story | 38240 |
| accounting.parameter_anchor.source_EOS.ordinary_textbook | 74183 |
| accounting.parameter_anchor.source_EOS.conditional_textbook | 234328 |
| quality_comparisons.matched_staged_CE.checks.coherence_gain_at_least8 | false |
| quality_comparisons.matched_staged_CE.checks.paired_CI_lower_above0 | false |
| quality_comparisons.matched_staged_CE.checks.EOS_nonworsening | false |
| quality_comparisons.matched_staged_CE.checks.repetition_nonworsening | true |
| quality_comparisons.matched_staged_CE.checks.no_empty_role_unicode | true |
| quality_comparisons.matched_staged_CE.checks.BPB_gate | true |
| quality_comparisons.matched_staged_CE.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.matched_staged_CE.passed | false |
| quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| quality_comparisons.strong_staged.checks.BPB_gate | true |
| quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.strong_staged.passed | false |
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
| scientific_teacher_tokens | 200000000 |
| actual_GPU_seconds | 481.3385134199925 |
| probe_and_failed_GPU_seconds | 33.6804799370002 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0000.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0000.json) ／ SHA256: `7a6f178448bab03dd705ae7347fe593f7d6907f7f7e059dfc487b651ac4b9a26` ／ 9,987 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0016.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0016.json) ／ SHA256: `d5af1c95a7d72dac579cf676117b1428b6b5a7d62fadc7bf8da4dae1dc03ed75` ／ 9,623 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0032.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0032.json) ／ SHA256: `c685657e6d8aa0bb42ab5911aee862eea75d70edfc6f20bd2602455c5b2792fe` ／ 10,265 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0048.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0048.json) ／ SHA256: `f98338d047493231ee6b32f1691a0d6ff15e3ee4f13c34e6763eeca920e07314` ／ 9,568 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0064.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0064.json) ／ SHA256: `7fdd6deb3e50acce6dd90758b00ceb0f62d0a99035f88aa88eb7c8623b2c570c` ／ 10,336 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0080.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0080.json) ／ SHA256: `5906457923fef6834f68b5f13314da09dd0d886fd19d4b7e4d2c7ca2ca83b975` ／ 9,754 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0096.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0096.json) ／ SHA256: `a7b9eab2536a8783906f9d366df7171ef18b5ffa259e80ad05c1ccea24257450` ／ 9,857 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0112.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0112.json) ／ SHA256: `993fa2445c26c3093745b89dc16de9786cf63c39b58865a4060bc3c43a60822c` ／ 10,184 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0128.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0128.json) ／ SHA256: `588334a06cb2ed0db268047d1961f836b49c38687e8824f9f0d2da04574c733b` ／ 9,851 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0144.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0144.json) ／ SHA256: `a0ed41dc267a8b3ec4dfdf402a242f5610fa354295543759724a19c7432a90a5` ／ 9,929 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0160.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0160.json) ／ SHA256: `655dd2104959d43181a0435547a9ed8867d957da675443ba137501af10f7e94b` ／ 10,191 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0176.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0176.json) ／ SHA256: `36af5b80c1b0511eda0001d589f6a42e86a1093ec33a87d99c98b9fb464c7ec3` ／ 10,027 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0192.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0192.json) ／ SHA256: `778cd3c132a3208f91d32725067cdeee88c664f66c7782e46eaa91e877e49c3c` ／ 9,935 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0208.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0208.json) ／ SHA256: `ce3852cb9e78e87e77caf9de6d90892db3df4d8b702a7efc7451c7652f6eed78` ／ 9,689 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0224.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0224.json) ／ SHA256: `3121a8d16e5aa34d9754bf5541336b14dbb2660a03f35c51767b0379cf17790a` ／ 9,856 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0240.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0240.json) ／ SHA256: `5b1c9d41f387b0b73d755db097bd9e588fb37f3b8a6fab679dfd99cdfc51070d` ／ 9,682 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0256.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0256.json) ／ SHA256: `27cce0933eca2a667eb466e61f23f21d0d0b6378b7149cf30826a5020c62bb19` ／ 9,683 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0272.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0272.json) ／ SHA256: `53ae8320aede823c3766581a5b2f16a86e5eb71a995458caeca9f081b77015ae` ／ 9,641 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0288.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0288.json) ／ SHA256: `d8e3a56ad1a0ebd170e1899f28ea19058e0a04442931deb6475fd6af417696ae` ／ 9,689 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0304.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0304.json) ／ SHA256: `5bb8f190d7b56694aec6f3a69d06bc0d5a2ae8308977d5d8accd1476447b86be` ／ 9,866 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0320.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0320.json) ／ SHA256: `149a5df4e26daab10e7cc5a21b101d0274fb3df4a7f5f5828ff5e5ddebabb6a3` ／ 9,392 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0336.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0336.json) ／ SHA256: `0aa46b24439bc3313f5083d5dcda6fc8b9b271f214e6a6e3f92e4be1c720c335` ／ 9,491 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0352.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0352.json) ／ SHA256: `5cea7e84c6280cf19001a952933b67ca5b8ea21f9bf861836828b34b1ab0d954` ／ 9,861 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0368.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0368.json) ／ SHA256: `97fd76d4d710b280a932c862e42a500d9e7391279c22c1d7e44d12de51da4b4a` ／ 9,606 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0384.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0384.json) ／ SHA256: `80730db5d0cf22ed723732dee501a59709e8079361914348b29053ebe595e3fd` ／ 9,917 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0400.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0400.json) ／ SHA256: `096fd527f22943d0b3bb512f8e3416a22ce77b20590e8b32968e7e2d3b7dec4c` ／ 9,585 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0416.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0416.json) ／ SHA256: `69d044454b98dab4b91d004a6b6299e46ed88f342aaf9038e5901cc05091d359` ／ 9,947 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0432.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0432.json) ／ SHA256: `bbed00981e4e4bb4c54ab38cf917d173db3390ff48854583b850aeaa4fcbf91f` ／ 9,406 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0448.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0448.json) ／ SHA256: `ee8474859c492cbd595461ed11e551832bd3a0b9bbdeba79fc2205ae3de0323a` ／ 9,654 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0464.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0464.json) ／ SHA256: `3b0c814f7a03f875a62d7822bc8611ae4287448d9d4e1d265ea1e1ad54b73688` ／ 9,474 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0480.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0480.json) ／ SHA256: `4680100824194b9dfe6b79af3ac2d9de7315cdbce20975199739bea8871895d5` ／ 9,499 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0496.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/0496.json) ／ SHA256: `5ba0965b065445ad13c2ca9623eca7c0fcc3f67fa55f05f793b068d49dcb56f2` ／ 9,579 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/matched_staged_CE/result.json) ／ SHA256: `d2d78d35baf606245994be2c4f3d14897e2b69a52c276fa18458a4b7f2daca27` ／ 186,165 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.75 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 74 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 49 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 25 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.74609375 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 73 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 45 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.75390625 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 75 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 43 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.90625 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 52 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 12 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 31 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 39 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0000.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0000.json) ／ SHA256: `9a62ae5bfdcfb9ffcdf918f34423e1135000db2c0ac799157fcf02226be9a832` ／ 9,967 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0016.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0016.json) ／ SHA256: `4214e18c57bed3dec6059c88b1f0818dc80e8cef9e27911d80ae5d6d53e5f5f8` ／ 9,622 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0032.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0032.json) ／ SHA256: `1313e0a895da302349759ea7b03ea5ad5ab8c447d84604d33e9e5f0362bfa457` ／ 10,278 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0048.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0048.json) ／ SHA256: `5295ba9f8b7aff301fda0bcb3de30d5b8ff519dc7e3d8d686b23004cf0abb4d3` ／ 9,547 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0064.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0064.json) ／ SHA256: `a8f7eddad0b447c3d0ec673d3f54e1ec2c0899a160081e1e164521b42e57b7b6` ／ 10,351 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0080.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0080.json) ／ SHA256: `50bef8dcb205e10824001967f1402db02873aed5b5b74b902840576a4b94f697` ／ 9,738 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0096.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0096.json) ／ SHA256: `a33e8e16a7e270908e1f317bcee0e98349f5c0d4043b1e795e51b57abe93f234` ／ 9,836 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0112.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0112.json) ／ SHA256: `eeb93b97e9792abff743a75e10a4769392f54521d7d0aaeb7b91ec3b4ff7d0e8` ／ 10,171 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0128.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0128.json) ／ SHA256: `2816161dfb0cae3b715c57040401aafc1e0031bcac82cd363a4ad82a7a8549a2` ／ 9,850 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0144.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0144.json) ／ SHA256: `07001f3c157f195e681eff7e1ec48c689c6c200fd60cfcd8865ecb2ddbfa2ded` ／ 9,929 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0160.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0160.json) ／ SHA256: `eb1c734e0a87489fea65e58acdfa1160ad6963cc5677738808d154e31c71bb0a` ／ 10,211 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0176.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0176.json) ／ SHA256: `531755e7dc8c439da5c88eb738447564f045db056862254acbc1f366746ebd0a` ／ 10,014 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0192.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0192.json) ／ SHA256: `f49d15b60617ce83e848ddc8e99657dc2653d4a6e67c97aa98757a99db190dd5` ／ 9,936 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0208.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0208.json) ／ SHA256: `61fc4ff7521928b680308c03911fb42001667909848d9c3640964b7e5d623733` ／ 9,665 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0224.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0224.json) ／ SHA256: `66204d3844d4d50711d2ee6e9462d0adf09c1f461167894a4ae5d1738b9b88a2` ／ 9,839 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0240.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0240.json) ／ SHA256: `35dd7a4fcdaa193f192e64ecf3afefe9e2f5d787d23e5bc21051bdeec4b1dc96` ／ 9,682 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0256.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0256.json) ／ SHA256: `8a55e97f8303f236cfd442e4b0140edea5fb73ff871f3cd90b570bc05c7125f5` ／ 9,675 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0272.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0272.json) ／ SHA256: `20fd46b8f8e0b2d0751160a4f303e524793461b2dcfd5f5de706f4e733ffb5e5` ／ 9,648 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0288.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0288.json) ／ SHA256: `972a8f76b8b43014da7c30b80ee90a637a4cafafafcc9b7c1db868e407b524f6` ／ 9,652 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0304.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0304.json) ／ SHA256: `82251589d803fb9a889f2523104ec9afde7d0795c01e680d3df13524e292aa1d` ／ 9,854 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0320.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0320.json) ／ SHA256: `157a6fa3551d9767e1dec6ae8e20e5cd558dd1eb833f4f7d9338ba0ee7aa4160` ／ 9,358 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0336.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0336.json) ／ SHA256: `285d488891dcef28cc24b073cc6ba76cd15e2324771683629828156cdd683e73` ／ 9,473 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0352.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0352.json) ／ SHA256: `1e9a752965ca255aa2ebd6f5db3f2703d271182b29fee7bb9c7f813b0b8140f2` ／ 9,835 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0368.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0368.json) ／ SHA256: `1a0b60a42ef3800ca28e170e4c5e66489475a582247bbd4c779644a5f2768806` ／ 9,583 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0384.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0384.json) ／ SHA256: `962a466944a26b4e14199fcfd0d394e30e46805a13b437cbe0d0aaf0eed3da3e` ／ 9,904 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0400.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0400.json) ／ SHA256: `d0c3515c7ce3a4321e6c7ecfcfb51a60d72a614099f04a0bd7ae1bb3c1d5bd60` ／ 9,554 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0416.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0416.json) ／ SHA256: `a614ca48809313271a20b8df5e4ba1152f8628fd75fc0a328c6e511f5a59a6bb` ／ 9,925 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0432.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0432.json) ／ SHA256: `b8f57d21e95f513e96d092c046f74f3c360225adae35557c9af5688a24b8ea3e` ／ 9,392 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0448.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0448.json) ／ SHA256: `a1aa72f248fe0401c1e11fe5499bc1d79b5509f2f07d09ad73c0e26fe078a2bf` ／ 9,626 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0464.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0464.json) ／ SHA256: `14edbe8e23a4118babd01b6883f23419beb939d4fed0da05ba956b137fc872c8` ／ 9,450 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0480.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0480.json) ／ SHA256: `65b21776c692790ec64b11c9fe91cbd65ef68d43534bc957a5a331d059a289c0` ／ 9,472 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0496.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/0496.json) ／ SHA256: `62d1a504662ca94981d29ad028c6b212fa288aa1c7c0f6300ea0b8720d60f9db` ／ 9,561 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/bridge/parameter_anchor/result.json) ／ SHA256: `c387584093ea40b9548b3c2338ac63b0ed9af2dc6e0ee8a362cd753d5efe06f3` ／ 186,181 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7421875 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 70 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 47 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6171875 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.73828125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 69 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 48 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 16 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 21 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7421875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 50 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 107 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0000.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0000.json) ／ SHA256: `48938cba27d694daa0dda5c5f5c80345c060b444408f37ee2925bc47d93e9f92` ／ 8,006 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0016.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0016.json) ／ SHA256: `c53c9147f817db5ffc4b8d037fa0b055365d0e1ff06dc2d5e706d91f938647c6` ／ 8,356 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0032.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0032.json) ／ SHA256: `7d2db0ea653a63e2287548b1b18a165fe90856731074f6d48aa0a75e555d87d4` ／ 7,037 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0048.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0048.json) ／ SHA256: `70d5af955b7844955efa99a11becfe983424a7519773d66bf3f7df7473e05a73` ／ 8,175 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0064.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0064.json) ／ SHA256: `d395b916aac24e505b8acee507bc7122fd6aa1c5b605a8b00fdb4438e0bc7a20` ／ 8,526 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0080.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0080.json) ／ SHA256: `b3c588531efa12963945f4ddfd0c6c8fbcf42bed88c9d0f08daed9bc59f3ea35` ／ 7,128 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0096.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0096.json) ／ SHA256: `9836a59ce844ddabdfb1d884408b7504db4643c6c6cf97a5a5e0b4fbc4e5f848` ／ 8,099 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0112.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0112.json) ／ SHA256: `929420489d0881bd51c8902851a41a780a1ed502cb535d84245ce796022ae8c3` ／ 8,279 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0128.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0128.json) ／ SHA256: `1e0e0c3bfe8c1fb28223108f85cb6c4be6491fabf574dd3ec651338137aea9e8` ／ 7,132 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0144.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0144.json) ／ SHA256: `e5d6e7787e99e10e4265894c46a473bc1cba97c1a6f8175d2efea9d1d93eb262` ／ 8,188 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0160.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0160.json) ／ SHA256: `d75bfa88a90037ed502040869e5b38b42c5fd084b431698dce96063ba8844ff2` ／ 8,661 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0176.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0176.json) ／ SHA256: `1b6e92f345caad43d82c609630bfc2c70926e9cc24dce2908d1dbb7eacbd68f1` ／ 6,971 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0192.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0192.json) ／ SHA256: `398f8fa8a8a5f9c8ab14c478bb34113d975bb99770de24a7bfb2bdbb969ff213` ／ 8,202 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0208.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0208.json) ／ SHA256: `963fda9051ca4ea76f34cc628864adbba9ea204e58820fafbda9188bbfc8be8f` ／ 8,534 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0224.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0224.json) ／ SHA256: `f85cfc2932ea6c74731f5d411090493cf92680ae62fba89b536b5547bd04dc21` ／ 7,140 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0240.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0240.json) ／ SHA256: `c56794da3253a6f7b9dbd088e2ab0f5690a33ccbe0aade0afaf8257657762270` ／ 8,354 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0256.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0256.json) ／ SHA256: `231963973bbba4e011e1d476c3250166be736de4b7694b1acefbeab0590d0d63` ／ 8,298 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0272.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0272.json) ／ SHA256: `bf4b216b005d3302492b7188fbd4fc80886730a322996f426a2ec3a58fb4c84a` ／ 8,477 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0288.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0288.json) ／ SHA256: `d10154d3785a9ce9ce6a742f4e62dcee9776ae92790e3c88cf7157af4ad3ceb1` ／ 7,173 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0304.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0304.json) ／ SHA256: `c70bf254911ddb4e0e8081f05d6f22595aba9beb540df69a1832715381ce22a1` ／ 8,177 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0320.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0320.json) ／ SHA256: `be9c2c89aa0ed3208246414e10a5f997174c73cc5822cc5bafe38fedfbe45912` ／ 8,650 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0336.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0336.json) ／ SHA256: `7f682b9a61f233424e5095f62f9f04f72958f6e9c0f86b7fb27618ac9713dcf4` ／ 7,164 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0352.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0352.json) ／ SHA256: `1dfa8018857de8675b7808a8a062f9c0c84ed059ef0fc02f58db50f518642e54` ／ 8,189 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0368.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0368.json) ／ SHA256: `40d5ca37da7bc1c29c27783da97ca808a654c76d775f7ea946e5da85e68eb95d` ／ 8,224 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0384.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0384.json) ／ SHA256: `bbe5a6876d9b3fa1034b39b12382a500d1417b6b5821d4e5057b5927f3076ec9` ／ 7,089 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0400.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0400.json) ／ SHA256: `2cdfe342a05486edea1db965cff9e958c6b7057f761409f432d791904a121ca6` ／ 8,185 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0416.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0416.json) ／ SHA256: `f8d9224ba118f540457a46f6c198ccdaab3b7d150001b5a9c5191985bec35b02` ／ 8,231 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0432.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0432.json) ／ SHA256: `e7d0b4a8dfdf2d87af6463aed9d91db9845e1be92bac311406ca8fc7e868d823` ／ 7,181 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0448.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0448.json) ／ SHA256: `8a145c4f2832e9a419ef8960168e334c8c6bbe98bc9bb77431243b54b281a440` ／ 8,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0464.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0464.json) ／ SHA256: `0771ca8e69131830732cbdb86852e117a2d7df0d74afe38482150120dca75d58` ／ 8,390 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0480.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0480.json) ／ SHA256: `300aee6ab7eff7d13907d1b258ae662a852bda6b6cd58812dd139026fddd80cb` ／ 7,074 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0496.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/0496.json) ／ SHA256: `2e998bf92e4701d143cc25403346860947304c46ffa9d4236bf8a6d410639388` ／ 8,116 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/result.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/matched_staged_CE/result.json) ／ SHA256: `f18752e42a6b7dd55295d9b08900c47a57eb2ec26f390e64d3a8606962511bab` ／ 182,730 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "68b5593558881f37b2314fe4cfa3f182009492679c6c3a39fa8b9a8e6c90a271" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.66015625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 47 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7578125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 34 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7109375 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 58 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 66 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8359375 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 19 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 14 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.69921875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 57 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.84375 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 45 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 12 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0000.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0000.json) ／ SHA256: `ea1642103d427eb14c7f43586aa26798f073348b733dbd8a5e199a980433db20` ／ 7,977 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0016.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0016.json) ／ SHA256: `362aa2b15cd6f4608845680b3b569ba8badf49a47923cf6257f1adce9d70b969` ／ 8,343 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0032.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0032.json) ／ SHA256: `102f7943b646456dae5028e650cc29c877f3aeefc49d92b2a1e8b20d3e5e324f` ／ 7,023 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0048.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0048.json) ／ SHA256: `3bc31a8253088942212cfc50dd702e008573dd2d50416c26d1c4897e03209322` ／ 8,163 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0064.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0064.json) ／ SHA256: `e61d73c212c51bdf4144284761ab8ce4b2061dcb88d1838fc65f946dcf1f362a` ／ 8,532 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0080.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0080.json) ／ SHA256: `cbb2ca480ee75938e0a3b785000ebb4e00a62e69f6e1e01f705a65aac9cd093d` ／ 7,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0096.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0096.json) ／ SHA256: `4c6cdc64365b75efc1329b015ec918dee4b661f06a21362ab5c6c7913aeb666b` ／ 8,092 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0112.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0112.json) ／ SHA256: `f9c0a32c0b38a9a4248364ad17520bf2226affff6a37629b95dd9466667e94a2` ／ 8,275 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0128.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0128.json) ／ SHA256: `39c480547f891417ae990b7e82394b9ac998030fed581ae3481f5041c01d5678` ／ 7,106 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>

<details>
<summary>reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0144.json — None</summary>

[原記録](../../reports/phase6/parameter-displacement-anchor-v3-20261006/transfer/retention/parameter_anchor/0144.json) ／ SHA256: `6fbb44e7e092956aa7483f3d74ce38538dbee965f1ec811d42329940424695a7` ／ 8,192 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d5dc0d8ade482b57fd6b65736bb5d8b993a976e4543a6c6ade0c8085911dfb19" |

</details>
