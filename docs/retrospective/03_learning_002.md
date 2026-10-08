# 学習量・配合・学習順序 — 2/6

[分野一覧へ](03_learning.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/evaluation/curriculum/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/evaluation/curriculum/evaluation/result.json) ／ SHA256: `b5d6039d23c27a089f24a59984766c200f9daa2772ed619e68e099e1e676da1e` ／ 189,790 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Fresh explicit source fork from same2B+20M parent; original3 supervised target sequences equal; locally generated conditional bodies replace natural2048. Same seed42; conditional length/EOS/lexical distribution and row interleaving differ." |
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 369821.8238763809 |
| body.eos_nll | 956.706282325089 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1302498889302441 |
| body.seconds | 1.6376896990113892 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 45 |
| greedy_rates.repetition | 17 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.53125 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.53125 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5208333333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5203649397197785 |
| diagnostics.semantics.per_token_secondary.mcc | 0.041748286072343294 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8308157099697885] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7492447129909365 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4283246977547496 |
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
| diagnostics.jcqa.primary.accuracy.point | 0.2868632707774799 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.26184092940125114, 0.3136729222520107] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.2868632707774799 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2752457551385165 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24932975871313673, 0.30116175156389635] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2752457551385165 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.27460276425066615 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.09421259981033882 |
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
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/evaluation/curriculum/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/evaluation/curriculum/evaluation/semantics.json) ／ SHA256: `9c560cfb16700ad18974d7b5d7f2bf447e3a3140a4f3ce6dad35e269fdb7c7a3` ／ 203,496 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.53125 |
| summary.primary.accuracy.ci95 | [0.484375, 0.5729166666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.53125 |
| summary.per_token_secondary.accuracy.point | 0.5208333333333334 |
| summary.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5625] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5208333333333334 |
| summary.per_token_secondary.macro_f1 | 0.5203649397197785 |
| summary.per_token_secondary.mcc | 0.041748286072343294 |
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
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0000.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0000.json) ／ SHA256: `dba31e6626f78c9cb76a8047fbc9a01d3cded5c1be3849449ffef44f7a71db26` ／ 8,058 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0016.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0016.json) ／ SHA256: `b9080985ed4745070ac5afbe09e53e14d304e22e13bf2b4bf27546952fdd6af3` ／ 8,384 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0032.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0032.json) ／ SHA256: `3cf613fc722974a2effa8f8b8c1e8c40f53ce38ecc6dff4db033f22e4e366e73` ／ 7,054 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0048.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0048.json) ／ SHA256: `64561c253821edb43fbf03653bb39a71222a6429f6784b5ed105bc8be4610919` ／ 8,225 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0064.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0064.json) ／ SHA256: `2421c4435557beee748b3f5b51cb94298b13454045f69f8d16c83185235fafcc` ／ 8,573 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0080.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0080.json) ／ SHA256: `b9ec4b16dacd798cd740b867f8dd85adb51f2b9f47827e6c0f79954c63f20f23` ／ 7,109 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0096.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0096.json) ／ SHA256: `9358c064d3582829af194a42c541d070c6ccef2c5f4827a993561a787f8c4c57` ／ 8,147 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0112.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0112.json) ／ SHA256: `069d97b9376b844b91fb0a261da0a2ac0826b73fee3af28824bd041be8f464a6` ／ 8,347 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0128.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0128.json) ／ SHA256: `905e7806f1f9b7ed6e08d0c2f6b16f53d247e79f7fa718cffebe352e608b13d0` ／ 7,127 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0144.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0144.json) ／ SHA256: `38d064f00152d543c9c236cdf01b5d9c5db752a7a4e65738e392b2f4a7abcd62` ／ 8,232 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0160.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0160.json) ／ SHA256: `684acc0c0ec8707dcbc6fcdd51a1eac371329b1c3fc96b3b2dff1ab7897471ee` ／ 8,689 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0176.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0176.json) ／ SHA256: `9a768d48008e90cd25c3296729fe256e69aaad09f3d5c8a2ba074b5cfb14ac1e` ／ 6,961 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0192.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0192.json) ／ SHA256: `e6c537fe76639c8249bec1280f9c5f11dbd4865fa2b39417aad5a0e464a6e56d` ／ 8,240 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0208.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0208.json) ／ SHA256: `9fc937fd465aa95dea52133746c1cbea948b0aabd76b08236aa118919d621823` ／ 8,591 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0224.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0224.json) ／ SHA256: `9fcf88a7f9b23b41661d037abf156cf259d7d46ad7934efe1fc9274d130c0428` ／ 7,147 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0240.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0240.json) ／ SHA256: `60f2f85256b6edc6c15f0d605639e13de9825970d33c5b32b07b84c5dc1b24c3` ／ 8,417 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0256.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0256.json) ／ SHA256: `b7e339359d9d315a4104420f1de66475aec25c0ecfeeeb0872aed53af11579c8` ／ 8,292 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0272.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0272.json) ／ SHA256: `3c3e57e910f5229419c2cd3717151a0578ffcb57ffc6b7772b644c2cd878c983` ／ 8,510 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0288.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0288.json) ／ SHA256: `40df29da988c68a0a12ac82aeb6f641f7c009c357b2812a699d4e71459e8a52a` ／ 7,133 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0304.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0304.json) ／ SHA256: `56ec766508b3884cf820b69d40dc45cea2c014ed6d6044a0fe642c15316710c3` ／ 8,211 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0320.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0320.json) ／ SHA256: `34d37d8236a8f5478171bf50284dfa59b87b0b0acf7ac4b61e3793af648e89b0` ／ 8,651 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0336.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0336.json) ／ SHA256: `b40a56a996302b7e5595ef04acabcc8cd268e3804a65e023ba0a3249c9e8fc8b` ／ 7,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0352.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0352.json) ／ SHA256: `4611710a7410686b87398f5a8a788d9dfdee07f153aa7f043743c3a63ba36df2` ／ 8,246 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0368.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0368.json) ／ SHA256: `2ef0a1c12a7de8bcfe12a44c47c8eee5626a5b958ba3722c03646414ef0b27fb` ／ 8,238 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0384.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0384.json) ／ SHA256: `36ce273fe14765c4e0f4e4a6a8332a6735d7ecd096502c69cb81d8c5d3e89245` ／ 7,060 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0400.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0400.json) ／ SHA256: `851130467c0877fb625e04add501386fb78141d426c79eb18d4d0a6c50cb9812` ／ 8,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0416.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0416.json) ／ SHA256: `507eef929c004a81a92a6944487b635cc7e00c4c750ec15b394b8d7d87b93336` ／ 8,263 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0432.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0432.json) ／ SHA256: `de2c9c3fcc02b63ba0c0d7d661665ec957c83fa8392a39e54a4346e6bb8fa5c9` ／ 7,156 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0448.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0448.json) ／ SHA256: `e1828ad3c3262b2ec03262c49e43de9a2407260566a6c95fb810cb898f13fc22` ／ 8,129 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0464.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0464.json) ／ SHA256: `d28bfa059fb5f163dc47ea0b28f44b501570ed87d459b19624b68a2277c69b86` ／ 8,410 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0480.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0480.json) ／ SHA256: `6d7967188a830b91f69e420db68a028410c8f85f4dc326c5001096db839bfe50` ／ 7,057 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0496.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/0496.json) ／ SHA256: `8e656bea7f58aad97b8119f271f6bf1f2d4d9d46799366751899e225b3ea3e10` ／ 8,140 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |

</details>

<details>
<summary>reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/result.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-comparison-20261006/transfer/curriculum100M/result.json) ／ SHA256: `81c8f7fa08db5d8fe50f7d73fc206034e9cc9aa52e1363e0b4008ffc13bb2ec4` ／ 182,531 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "be7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2e" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 63 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8203125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 43 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 20 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.71484375 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 66 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 51 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 44 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 22 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 64 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 55 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 44 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 20 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not untouched real-world Japanese quality or Base adoption." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/content-notes.json) ／ SHA256: `bcc942b95376275da658d3e7a9db977ed8cd8303665196e3a7fce82040af72d8` ／ 23,791 bytes

| 原キー | 保存値 |
|---|---|
| consistency_reuse.prior_notes_sha256 | "0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f" |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/content-pilot.json) ／ SHA256: `c281c1d035f49a0dde88c23c95034b1158232a85623fb9c4a1fe7f89a64a0e90` ／ 87,568 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/content-review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/content-review.json) ／ SHA256: `3fc35cf431b369f1504aac965d56f70fc52a0a937f50e20649ef9895f3b3c85f` ／ 24,684 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 0 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 0 |
| training_pool_accepted | true |
| notes_sha256 | "bcc942b95376275da658d3e7a9db977ed8cd8303665196e3a7fce82040af72d8" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-notes.json) ／ SHA256: `bcc942b95376275da658d3e7a9db977ed8cd8303665196e3a7fce82040af72d8` ／ 23,791 bytes

| 原キー | 保存値 |
|---|---|
| consistency_reuse.prior_notes_sha256 | "0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f" |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-pilot.json) ／ SHA256: `c281c1d035f49a0dde88c23c95034b1158232a85623fb9c4a1fe7f89a64a0e90` ／ 87,568 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/data/content-review.json) ／ SHA256: `3fc35cf431b369f1504aac965d56f70fc52a0a937f50e20649ef9895f3b3c85f` ／ 24,684 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 0 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 0 |
| training_pool_accepted | true |
| notes_sha256 | "bcc942b95376275da658d3e7a9db977ed8cd8303665196e3a7fce82040af72d8" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/data/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/data/manifest.json) ／ SHA256: `b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311` ／ 647,762 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 82213 |
| generated_body_bytes | 321088 |
| serialized_tokens | 86309 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_checks.local_exact_train_body_unique | true |
| actual_checks.all24_train_structures | true |
| actual_checks.lexical_entities_disjoint | true |
| actual_checks.structural_template_ids_disjoint | true |
| actual_checks.all128_probe_family_ids_disjoint | true |
| actual_checks.probe_complete_bodies_absent_from_train | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| single_repair.prior_manifest_sha256 | "43f6c4a144c1d8d25f8b2ab25f8a9fd5904bf3316c459e8abc2ee0fd44ac3960" |
| single_repair.prior_review_sha256 | "aa6401064c3cb2edb086947ba4dd8f1156d962f36ea455c78f52020ec4167ff1" |
| single_repair.changed_train_documents | 86 |
| single_repair.original_facts_labels_ids_order_preserved | true |
| single_repair.all128_probe_facts_choices_preserved | true |
| single_repair.seed_unchanged | true |
| single_repair.fixed_first64_ids_unchanged | true |
| single_repair.correction | "negation-2 only: その内容は、 -&gt; その記録によると、. Specific observed grammatical topic connection; no answer, fact or selection changes." |
| new_local_serialized_tokens | 86309 |
| science_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| loss_policy | "Full body plusEOS CE, outcome weight1. Mask annotates positive continuation spans only; no negative learning, no roles, no synthetic QA formatting." |
| limitations | "24 hand-authored structures share programmatic rules;2048 documents are not2048 independent semantic domains.128 generator probes also share program logic; not independent human/real-world generalization or Base quality proof. Length/EOS/lexical distribution differs from natural2048." |
| training_pool_accepted | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/data/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/data/transfer-probes.json) ／ SHA256: `daf92018a167c24db83a4d3bd029d45973bd7f34f3fd452f52419ccc0b651d83` ／ 856,180 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/job.json — complete_pending_fixed64_content</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/job.json) ／ SHA256: `d4b8613520fd60839e56abc7747c943f87fe827d3cdfe76f29234b0cf5a7b33a` ／ 1,170 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_fixed64_content" |
| CPU_limit_seconds | 240 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| CPU_seconds | 0.34430652399896644 |
| checks.local_exact_train_body_unique | true |
| checks.all24_train_structures | true |
| checks.lexical_entities_disjoint | true |
| checks.structural_template_ids_disjoint | true |
| checks.all128_probe_family_ids_disjoint | true |
| checks.probe_complete_bodies_absent_from_train | true |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/manifest.json) ／ SHA256: `b5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311` ／ 647,762 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 82213 |
| generated_body_bytes | 321088 |
| serialized_tokens | 86309 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_checks.local_exact_train_body_unique | true |
| actual_checks.all24_train_structures | true |
| actual_checks.lexical_entities_disjoint | true |
| actual_checks.structural_template_ids_disjoint | true |
| actual_checks.all128_probe_family_ids_disjoint | true |
| actual_checks.probe_complete_bodies_absent_from_train | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| single_repair.prior_manifest_sha256 | "43f6c4a144c1d8d25f8b2ab25f8a9fd5904bf3316c459e8abc2ee0fd44ac3960" |
| single_repair.prior_review_sha256 | "aa6401064c3cb2edb086947ba4dd8f1156d962f36ea455c78f52020ec4167ff1" |
| single_repair.changed_train_documents | 86 |
| single_repair.original_facts_labels_ids_order_preserved | true |
| single_repair.all128_probe_facts_choices_preserved | true |
| single_repair.seed_unchanged | true |
| single_repair.fixed_first64_ids_unchanged | true |
| single_repair.correction | "negation-2 only: その内容は、 -&gt; その記録によると、. Specific observed grammatical topic connection; no answer, fact or selection changes." |
| new_local_serialized_tokens | 86309 |
| science_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| loss_policy | "Full body plusEOS CE, outcome weight1. Mask annotates positive continuation spans only; no negative learning, no roles, no synthetic QA formatting." |
| limitations | "24 hand-authored structures share programmatic rules;2048 documents are not2048 independent semantic domains.128 generator probes also share program logic; not independent human/real-world generalization or Base quality proof. Length/EOS/lexical distribution differs from natural2048." |
| training_pool_accepted | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/ordinary-stream-audit.json — actual_generated_vs_natural100M_ordinary_teacher_sequences_identical</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/ordinary-stream-audit.json) ／ SHA256: `d8291d3e1c6ff087aef680e3e6e3e9ddfab012fa57d2a48fa54af66d8d61c800` ／ 3,427 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_generated_vs_natural100M_ordinary_teacher_sequences_identical" |
| actual_generated.teachers.web | 75000000 |
| actual_generated.teachers.story | 5000000 |
| actual_generated.teachers.ordinary_textbook | 10000000 |
| actual_generated.EOS.web | 656229 |
| actual_generated.EOS.story | 38240 |
| actual_generated.EOS.ordinary_textbook | 74183 |
| actual_generated.body_bytes.web | 299907916 |
| actual_generated.body_bytes.story | 20452979 |
| actual_generated.body_bytes.ordinary_textbook | 42739471 |
| actual_generated.physical_inputs.web | 75666432 |
| actual_generated.physical_inputs.story | 5039104 |
| actual_generated.physical_inputs.ordinary_textbook | 10075136 |
| actual_generated.physical_inputs.conditional_textbook | 10243072 |
| actual_generated.total_updates | 3083 |
| previous_natural.teachers.web | 75000000 |
| previous_natural.teachers.story | 5000000 |
| previous_natural.teachers.ordinary_textbook | 10000000 |
| previous_natural.EOS.web | 656229 |
| previous_natural.EOS.story | 38240 |
| previous_natural.EOS.ordinary_textbook | 74183 |
| previous_natural.body_bytes.web | 299907916 |
| previous_natural.body_bytes.story | 20452979 |
| previous_natural.body_bytes.ordinary_textbook | 42739471 |
| previous_natural.physical_inputs.web | 75674624 |
| previous_natural.physical_inputs.story | 5039104 |
| previous_natural.physical_inputs.ordinary_textbook | 10075136 |
| previous_natural.physical_inputs.conditional_textbook | 10071040 |
| previous_natural.total_updates | 3078 |
| checks.target_sha256 | true |
| checks.teachers | true |
| checks.EOS | true |
| checks.body_bytes | true |
| CPU_seconds | 6.371515109000029 |
| CPU_limit_seconds | 30 |
| accepted_generated_review_sha256 | "3fc35cf431b369f1504aac965d56f70fc52a0a937f50e20649ef9895f3b3c85f" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| limitations | "CPU replay observes actual teacher IDs/counts/EOS/byte lengths, not model updates or GPU quality. Conditional row interleaving/length/EOS distribution differs. Ordinary physical input padding beyond quotas can differ while supervised target sequences are equal." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/single-repair.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/single-repair.json) ／ SHA256: `ab034015982b2b3d8f7a29ad987b38b393dd0cb686b9cd9267a345d91eafd046` ／ 2,306 bytes

| 原キー | 保存値 |
|---|---|
| changed_train_documents | 86 |
| seed_unchanged | true |
| correction | "negation-2 only: その内容は、 -&gt; その記録によると、. Specific observed grammatical topic connection; no answer, fact or selection changes." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006-v2/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006-v2/transfer-probes.json) ／ SHA256: `daf92018a167c24db83a4d3bd029d45973bd7f34f3fd452f52419ccc0b651d83` ／ 856,180 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/content-notes.json) ／ SHA256: `0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f` ／ 23,423 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/content-pilot.json) ／ SHA256: `ec6048ba08d654be082cdc6fdb051146c6302cbaabd97f19e31b5d20dac5e65b` ／ 87,532 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/content-review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/content-review.json) ／ SHA256: `aa6401064c3cb2edb086947ba4dd8f1156d962f36ea455c78f52020ec4167ff1` ／ 24,561 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 2 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 2 |
| training_pool_accepted | false |
| notes_sha256 | "0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/data/content-notes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/data/content-notes.json) ／ SHA256: `0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f` ／ 23,423 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/data/content-pilot.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/data/content-pilot.json) ／ SHA256: `ec6048ba08d654be082cdc6fdb051146c6302cbaabd97f19e31b5d20dac5e65b` ／ 87,532 bytes

| 原キー | 保存値 |
|---|---|
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/data/content-review.json — all64_generated_content_review_complete</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/data/content-review.json) ／ SHA256: `aa6401064c3cb2edb086947ba4dd8f1156d962f36ea455c78f52020ec4167ff1` ／ 24,561 bytes

| 原キー | 保存値 |
|---|---|
| status | "all64_generated_content_review_complete" |
| weak_documents | 2 |
| maximum_weak_documents | 10 |
| paired_content_gate_passed | true |
| unresolved_grammar_documents | 2 |
| training_pool_accepted | false |
| notes_sha256 | "0e6195b961512601396e1a3eef213de83d9323841593524066723d64e04b083f" |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| Base_adopted | false |
| limitations | "Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/data/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/data/manifest.json) ／ SHA256: `43f6c4a144c1d8d25f8b2ab25f8a9fd5904bf3316c459e8abc2ee0fd44ac3960` ／ 645,119 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 82127 |
| generated_body_bytes | 320314 |
| serialized_tokens | 86223 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_checks.local_exact_train_body_unique | true |
| actual_checks.all24_train_structures | true |
| actual_checks.lexical_entities_disjoint | true |
| actual_checks.structural_template_ids_disjoint | true |
| actual_checks.all128_probe_family_ids_disjoint | true |
| actual_checks.probe_complete_bodies_absent_from_train | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| new_local_serialized_tokens | 86223 |
| science_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| loss_policy | "Full body plusEOS CE, outcome weight1. Mask annotates positive continuation spans only; no negative learning, no roles, no synthetic QA formatting." |
| limitations | "24 hand-authored structures share programmatic rules;2048 documents are not2048 independent semantic domains.128 generator probes also share program logic; not independent human/real-world generalization or Base quality proof. Length/EOS/lexical distribution differs from natural2048." |
| training_pool_accepted | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/data/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/data/transfer-probes.json) ／ SHA256: `7744f8b783889135f41226a02f4e34d474809b66a748d01951fba9ef0edbbabd` ／ 855,850 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/job.json — complete_pending_fixed64_content</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/job.json) ／ SHA256: `ccbb5ac2b0d6ff14dbb036662b5ac6637372c792296ca8c9a0a63be7fb0662a2` ／ 1,165 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_fixed64_content" |
| CPU_limit_seconds | 240 |
| scientific_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| CPU_seconds | 0.275927627022611 |
| checks.local_exact_train_body_unique | true |
| checks.all24_train_structures | true |
| checks.lexical_entities_disjoint | true |
| checks.structural_template_ids_disjoint | true |
| checks.all128_probe_family_ids_disjoint | true |
| checks.probe_complete_bodies_absent_from_train | true |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/manifest.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/manifest.json) ／ SHA256: `43f6c4a144c1d8d25f8b2ab25f8a9fd5904bf3316c459e8abc2ee0fd44ac3960` ／ 645,119 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100660 |
| documents | 2048 |
| generated_body_tokens | 82127 |
| generated_body_bytes | 320314 |
| serialized_tokens | 86223 |
| EOS_targets | 2048 |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_checks.local_exact_train_body_unique | true |
| actual_checks.all24_train_structures | true |
| actual_checks.lexical_entities_disjoint | true |
| actual_checks.structural_template_ids_disjoint | true |
| actual_checks.all128_probe_family_ids_disjoint | true |
| actual_checks.probe_complete_bodies_absent_from_train | true |
| leakage.protected_test_opened | false |
| leakage.limitations | "Literal bounded check is not semantic/template equivalence certification. Six broad abilities follow known dev failures; selection is exploratory, not untouched evaluation." |
| newly_prepared_original_corpus_tokens | 0 |
| new_local_serialized_tokens | 86223 |
| science_teacher_tokens | 0 |
| actual_GPU_seconds | 0 |
| protected_test_used | false |
| loss_policy | "Full body plusEOS CE, outcome weight1. Mask annotates positive continuation spans only; no negative learning, no roles, no synthetic QA formatting." |
| limitations | "24 hand-authored structures share programmatic rules;2048 documents are not2048 independent semantic domains.128 generator probes also share program logic; not independent human/real-world generalization or Base quality proof. Length/EOS/lexical distribution differs from natural2048." |
| training_pool_accepted | false |

</details>

<details>
<summary>reports/phase6/condition-transfer-curriculum-20261006/transfer-probes.json — None</summary>

[原記録](../../reports/phase6/condition-transfer-curriculum-20261006/transfer-probes.json) ／ SHA256: `7744f8b783889135f41226a02f4e34d474809b66a748d01951fba9ef0edbbabd` ／ 855,850 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/condition_learning_annotations.json — None</summary>

[原記録](../../reports/phase6/condition_learning_annotations.json) ／ SHA256: `38f54c687695e6a13aad125ba4558bee5257714dc592e50bc21385e69a40e23f` ／ 202,681 bytes

| 原キー | 保存値 |
|---|---|
| arms.compact.raw_by_id.base-001.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-002.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-004.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-005.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-006.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-007.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-009.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-010.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-011.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-012.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-014.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-015.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-016.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-017.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-019.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-020.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-021.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-022.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-024.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-025.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-026.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-027.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-029.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-030.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-031.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-032.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-034.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-035.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-036.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-037.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-039.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-040.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-041.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-042.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-044.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-045.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-046.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-047.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-049.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-050.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-051.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-052.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-054.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-055.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-056.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-057.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-059.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-060.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-061.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-062.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-064.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-065.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-066.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-067.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-069.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-070.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-071.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-072.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-074.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-075.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-076.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-077.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-079.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-080.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-081.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-082.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-084.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-085.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-086.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-087.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-089.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-090.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-091.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-092.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-094.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-095.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-096.stop_reason | "stop_id" |
| arms.compact.raw_by_id.base-097.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-099.stop_reason | "max_new_tokens" |
| arms.compact.raw_by_id.base-100.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-001.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-002.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-004.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-005.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-006.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-007.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-009.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-010.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-011.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-012.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-014.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-015.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-016.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-017.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-019.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-020.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-021.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-022.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-024.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-025.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-026.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-027.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-029.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-030.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-031.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-032.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-034.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-035.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-036.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-037.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-039.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-040.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-041.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-042.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-044.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-045.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-046.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-047.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-049.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-050.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-051.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-052.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-054.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-055.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-056.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-057.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-059.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-060.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-061.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-062.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-064.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-065.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-066.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-067.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-069.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-070.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-071.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-072.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-074.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-075.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-076.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-077.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-079.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-080.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-081.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-082.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-084.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-085.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-086.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-087.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-089.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-090.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-091.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-092.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-094.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-095.stop_reason | "max_new_tokens" |
| arms.expanded.raw_by_id.base-096.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-097.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-099.stop_reason | "stop_id" |
| arms.expanded.raw_by_id.base-100.stop_reason | "stop_id" |

</details>

<details>
<summary>reports/phase6/condition_learning_completion.json — complete_plan66_stages1_to4_with_actual_learning_failed_diagnostic_branch</summary>

[原記録](../../reports/phase6/condition_learning_completion.json) ／ SHA256: `d375ecb8464c4b2ad964a5c85eb3a2dce8d04c449f431a446ba126076cf6c792` ／ 3,191 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_plan66_stages1_to4_with_actual_learning_failed_diagnostic_branch" |
| checks.stage1_fixed_real_1000_5000_whole_documents | true |
| checks.stage1_fixed100_unseen_names_structure_and_eval_separation | true |
| checks.stage1_relevant_CPU5_tests_no_failures | true |
| checks.stage2_real_two_finite_checkpointed_24969216_train_and_dev_evals | true |
| checks.stage2_actual_CUDA_full_state_resume_gate | true |
| checks.stage3_actual_same_budget_expansion_failed_goal_not_rerolled | true |
| checks.stage3_real_bound_packed_vs_isolated_probe_no_learning | true |
| checks.stage4_all_new_Japanese_and160_raw_bound_content_evidence | true |
| checks.stage4_unchanged_adoption_failed_full_not_started | true |
| checks.actual_scientific_job_exited | true |
| checks.actual_tokens_GPU_budgets_separate | true |
| checks.actual_each_train_within_frozen_180s | true |
| checks.original10B_UI_actual_identity_HTTP | true |
| checks.stage4_results_report_real_and_frozen_sources_intact | true |
| scientific_tokens | 49938432 |
| verification_tokens | 262144 |
| original_UI.status | "running" |
| original_UI.additional_training_tokens | 0 |
| original_UI.model.training_tokens | 10000007168 |
| original_UI.model.update | 305176 |
| original_UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| HTTP_model.training_tokens | 10000007168 |
| HTTP_model.update | 305176 |
| HTTP_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| HTTP_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| HTTP_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checked_at | "2026-10-05T10:38:47.480884Z" |

</details>

<details>
<summary>reports/phase6/condition_learning_judgment.json — None</summary>

[原記録](../../reports/phase6/condition_learning_judgment.json) ／ SHA256: `1a0632cdfb3bd8a3b38c0a35bf954e04f025dbf6a29ffb8572d60bd3f877d544` ／ 1,337 bytes

| 原キー | 保存値 |
|---|---|
| candidate_adopted | false |
| decision | "diagnostic_learning_complete_both_goals_missed_candidates_rejected" |
| train_dev.compact.train.correct | 75 |
| train_dev.compact.train.accuracy | 0.75 |
| train_dev.compact.train.pairs | 50 |
| train_dev.compact.train.both_correct | 25 |
| train_dev.compact.train.both_accuracy | 0.5 |
| train_dev.compact.dev.correct | 65 |
| train_dev.compact.dev.accuracy | 0.65 |
| train_dev.compact.dev.pairs | 50 |
| train_dev.compact.dev.both_correct | 16 |
| train_dev.compact.dev.both_accuracy | 0.32 |
| train_dev.expanded.train.correct | 68 |
| train_dev.expanded.train.accuracy | 0.68 |
| train_dev.expanded.train.pairs | 50 |
| train_dev.expanded.train.both_correct | 19 |
| train_dev.expanded.train.both_accuracy | 0.38 |
| train_dev.expanded.dev.correct | 61 |
| train_dev.expanded.dev.accuracy | 0.61 |
| train_dev.expanded.dev.pairs | 50 |
| train_dev.expanded.dev.both_correct | 14 |
| train_dev.expanded.dev.both_accuracy | 0.28 |
| matched100m_hypothesis | "Not executed because frozen prerequisite failed" |
| checked_at | "2026-10-05T10:38:47.480398Z" |

</details>

<details>
<summary>reports/phase6/condition_learning_packing_probe.json — complete</summary>

[原記録](../../reports/phase6/condition_learning_packing_probe.json) ／ SHA256: `219e2314acfe3ae6e51cb99999164ef8ef512747a29c2a36ac47105b7baf6db6` ／ 88,650 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| additional_learning_tokens | 0 |
| arms.compact.checkpoint_sha256 | "68b8d24641796430cf10bda25b14abfb41984f36fabd8dcbaf480f5d83af7f7b" |
| arms.compact.boundary_crossing_skipped | ["train-quantity-0002-1", "train-negation-0005-0", "train-time-0005-0", "train-cause-0001-1", "train-cause-0008-1"] |
| arms.compact.isolated_correct | 72 |
| arms.compact.packed_correct | 95 |
| arms.compact.isolated_expected_nll_per_token | 0.39867671696056844 |
| arms.compact.packed_expected_nll_per_token | 2.079700999815738e-06 |
| arms.compact.forward_input_tokens | 96080 |
| arms.expanded.checkpoint_sha256 | "472a759050660cbc68d76d438c413dd491df5f36bc73a960f4a5c38d75a35d6c" |
| arms.expanded.boundary_crossing_skipped | ["train-quantity-0001-1", "train-negation-0009-1", "train-time-0006-0", "train-cause-0005-1"] |
| arms.expanded.isolated_correct | 65 |
| arms.expanded.packed_correct | 96 |
| arms.expanded.isolated_expected_nll_per_token | 0.450596213008137 |
| arms.expanded.packed_expected_nll_per_token | 0.0002778432988556063 |
| arms.expanded.forward_input_tokens | 97644 |
| GPU_wall_seconds | 2.3190775490074884 |
| interpretation | "Original fixed block context vs standalone document, on same retained train targets. This detects context dependence; it does not isolate prior-document shortcuts from absolute position or all numerical differences." |

</details>

<details>
<summary>reports/phase6/condition_learning_ready.json — None</summary>

[原記録](../../reports/phase6/condition_learning_ready.json) ／ SHA256: `c28707dcab9f2e09b75fe7a552d990deb5ded20322e65f9b0c22989ad01a2fff` ／ 11,272 bytes

| 原キー | 保存値 |
|---|---|
| pools.compact.unique_tokens | 55273 |
| pools.compact.documents | 1000 |
| pools.compact.mean_body_tokens | 53.273 |
| pools.compact.EOS_per_1000_tokens | 18.092015993342137 |
| pools.expanded.unique_tokens | 280724 |
| pools.expanded.documents | 5000 |
| pools.expanded.mean_body_tokens | 54.1448 |
| pools.expanded.EOS_per_1000_tokens | 17.811088471238655 |
| dev_documents | 100 |
| shared_train_documents | 276 |
| limits | "Authored mechanistic entailment; no independent human/blind validation; amount, lexical diversity, length and EOS density can differ" |

</details>

<details>
<summary>reports/phase6/condition_learning_review.json — passed_evidence_audit</summary>

[原記録](../../reports/phase6/condition_learning_review.json) ／ SHA256: `b23125bbf9581c5b145b23589aaefd621b23b92fc7fd5738268c85765e8c83f2` ／ 305,316 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_evidence_audit" |
| checks.actual_complete_job_exited_within_budget | true |
| checks.frozen_run_binding | true |
| checks.actual_CUDA_all_resume_state_and_losses | true |
| checks.frozen_conditional_100M_branch | true |
| checks.scientific_verification_separate_accounting | true |
| checks.protected_test_unused | true |
| checks.compact_finite_hash_bound_all_resume_state | true |
| checks.compact_actual_finite_contiguous_updates | true |
| checks.compact_actual_tokens_binding_digest | true |
| checks.compact_actual_base_objective_not_chat_or_answer_only | true |
| checks.compact_actual_LR_stable_decay | true |
| checks.compact_actual_train_only_source_routes | true |
| checks.compact_actual_fixed_dev80_raw_checkpoint_binding | true |
| checks.compact_all80_individual_raw_bound_content_reviews | true |
| checks.compact_appropriate_completion_actual_EOS | true |
| checks.compact_same_dev256_common_byte_BPB | true |
| checks.compact_complete_Japanese_diagnostics_RNG_isolated | true |
| checks.compact_raw_rates_recomputed | true |
| checks.compact_condition_eval_same_new_checkpoint | true |
| checks.compact_train_100_actual_paired_credits | true |
| checks.compact_dev_100_actual_paired_credits | true |
| checks.compact_unseen_structure_50_separate | true |
| checks.compact_train90_dev70_goal_recomputed | true |
| checks.expanded_finite_hash_bound_all_resume_state | true |
| checks.expanded_actual_finite_contiguous_updates | true |
| checks.expanded_actual_tokens_binding_digest | true |
| checks.expanded_actual_base_objective_not_chat_or_answer_only | true |
| checks.expanded_actual_LR_stable_decay | true |
| checks.expanded_actual_train_only_source_routes | true |
| checks.expanded_actual_fixed_dev80_raw_checkpoint_binding | true |
| checks.expanded_all80_individual_raw_bound_content_reviews | true |
| checks.expanded_appropriate_completion_actual_EOS | true |
| checks.expanded_same_dev256_common_byte_BPB | true |
| checks.expanded_complete_Japanese_diagnostics_RNG_isolated | true |
| checks.expanded_raw_rates_recomputed | true |
| checks.expanded_condition_eval_same_new_checkpoint | true |
| checks.expanded_train_100_actual_paired_credits | true |
| checks.expanded_dev_100_actual_paired_credits | true |
| checks.expanded_unseen_structure_50_separate | true |
| checks.expanded_train90_dev70_goal_recomputed | true |
| checks.compact_expanded_paired_fixed_IDs_bytes | true |
| checks.compact_expanded_paired_semantics | true |
| checks.compact_expanded_paired_jblimp | true |
| checks.compact_expanded_paired_jcqa | true |
| summaries.compact.BPB | 1.2688448518724071 |
| summaries.compact.rates.eos | 59 |
| summaries.compact.rates.repetition | 3 |
| summaries.compact.rates.unicode_failure | 0 |
| summaries.compact.rates.role_leak | 0 |
| summaries.compact.rates.empty | 0 |
| summaries.compact.content.grammar_score2 | 44 |
| summaries.compact.content.relevance_score2 | 4 |
| summaries.compact.content.coherence_score2 | 1 |
| summaries.compact.appropriate_EOS | 6 |
| summaries.compact.diagnostics.semantics.primary.accuracy.point | 0.4635416666666667 |
| summaries.compact.diagnostics.semantics.primary.accuracy.ci95 | [0.421875, 0.5001302083333327] |
| summaries.compact.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.compact.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.compact.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.compact.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.primary.hard_accuracy | 0.4635416666666667 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5104166666666666 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4635416666666667, 0.5572916666666666] |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.compact.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5104166666666666 |
| summaries.compact.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5104166666666666 |
| summaries.compact.diagnostics.semantics.per_token_secondary.mcc | 0.020833333333333332 |
| summaries.compact.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.compact.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.compact.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.categories.time.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.compact.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.compact.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.compact.diagnostics.jblimp.primary.accuracy.point | 0.7945619335347432 |
| summaries.compact.diagnostics.jblimp.primary.accuracy.ci95 | [0.7492447129909365, 0.8368580060422961] |
| summaries.compact.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.compact.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.compact.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.compact.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.primary.hard_accuracy | 0.7945619335347432 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7371601208459214 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6888217522658611, 0.7854984894259819] |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7371601208459214 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42434782608695654 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.compact.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.compact.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.compact.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.compact.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.compact.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.compact.diagnostics.jblimp.raw_pair_accuracy | 0.7885196374622356 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.point | 0.2966934763181412 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.ci95 | [0.26988382484361034, 0.322609472743521] |
| summaries.compact.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jcqa.primary.hard_accuracy | 0.2966934763181412 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.30205540661304736 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2752457551385165, 0.32978105451295786] |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.30205540661304736 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3018966313830916 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.mcc | 0.12822691101042694 |
| summaries.compact.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.compact.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.compact.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.compact.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.compact.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.compact.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.compact.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.compact.diagnostics.semantic_both_contexts.correct | 5 |
| summaries.compact.condition.train.correct | 75 |
| summaries.compact.condition.train.accuracy | 0.75 |
| summaries.compact.condition.train.pairs | 50 |
| summaries.compact.condition.train.both_correct | 25 |
| summaries.compact.condition.train.both_accuracy | 0.5 |
| summaries.compact.condition.dev.correct | 65 |
| summaries.compact.condition.dev.accuracy | 0.65 |
| summaries.compact.condition.dev.pairs | 50 |
| summaries.compact.condition.dev.both_correct | 16 |
| summaries.compact.condition.dev.both_accuracy | 0.32 |
| summaries.compact.unseen_structure.correct | 29 |
| summaries.compact.unseen_structure.accuracy | 0.58 |
| summaries.compact.unseen_structure.pairs | 25 |
| summaries.compact.unseen_structure.both_correct | 5 |
| summaries.compact.unseen_structure.both_accuracy | 0.2 |
| summaries.compact.known_structure.correct | 36 |
| summaries.compact.known_structure.accuracy | 0.72 |
| summaries.compact.known_structure.pairs | 25 |
| summaries.compact.known_structure.both_correct | 11 |
| summaries.compact.known_structure.both_accuracy | 0.44 |
| summaries.compact.expected_train_continuation_nll_per_token | 0.42397155702050815 |
| summaries.compact.training_seconds | 38.64743510900007 |
| summaries.compact.source_tokens.web | 0 |
| summaries.compact.source_tokens.short | 24969216 |
| summaries.compact.source_EOS.web | 0 |
| summaries.compact.source_EOS.short | 454092 |
| summaries.expanded.BPB | 1.4084090425537954 |
| summaries.expanded.rates.eos | 62 |
| summaries.expanded.rates.repetition | 7 |
| summaries.expanded.rates.unicode_failure | 0 |
| summaries.expanded.rates.role_leak | 0 |
| summaries.expanded.rates.empty | 0 |
| summaries.expanded.content.grammar_score2 | 38 |
| summaries.expanded.content.relevance_score2 | 5 |
| summaries.expanded.content.coherence_score2 | 2 |
| summaries.expanded.appropriate_EOS | 5 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.ci95 | [0.4791666666666667, 0.5677083333333334] |
| summaries.expanded.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5052083333333334 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.46875, 0.5416666666666666] |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5052083333333334 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.macro_f1 | 0.505087505087505 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.mcc | 0.01042175665801204 |
| summaries.expanded.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.expanded.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.expanded.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.categories.time.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.expanded.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.expanded.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.point | 0.7643504531722054 |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.ci95 | [0.7189577039274925, 0.8096676737160121] |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.primary.hard_accuracy | 0.7643504531722054 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7522658610271903 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7068731117824774, 0.797583081570997] |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7522658610271903 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42931034482758623 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.expanded.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.expanded.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.expanded.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.expanded.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.expanded.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.expanded.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.point | 0.24396782841823056 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.ci95 | [0.21805183199285075, 0.26899016979445933] |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jcqa.primary.hard_accuracy | 0.24396782841823056 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.28150134048257375 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.25556300268096516, 0.3092046470062556] |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.28150134048257375 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.28126840062155173 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.mcc | 0.10307770978013704 |
| summaries.expanded.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.expanded.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.expanded.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.expanded.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.expanded.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.expanded.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.expanded.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.expanded.diagnostics.semantic_both_contexts.correct | 12 |
| summaries.expanded.condition.train.correct | 68 |
| summaries.expanded.condition.train.accuracy | 0.68 |
| summaries.expanded.condition.train.pairs | 50 |
| summaries.expanded.condition.train.both_correct | 19 |
| summaries.expanded.condition.train.both_accuracy | 0.38 |
| summaries.expanded.condition.dev.correct | 61 |
| summaries.expanded.condition.dev.accuracy | 0.61 |
| summaries.expanded.condition.dev.pairs | 50 |
| summaries.expanded.condition.dev.both_correct | 14 |
| summaries.expanded.condition.dev.both_accuracy | 0.28 |
| summaries.expanded.unseen_structure.correct | 27 |
| summaries.expanded.unseen_structure.accuracy | 0.54 |
| summaries.expanded.unseen_structure.pairs | 25 |
| summaries.expanded.unseen_structure.both_correct | 5 |
| summaries.expanded.unseen_structure.both_accuracy | 0.2 |
| summaries.expanded.known_structure.correct | 34 |
| summaries.expanded.known_structure.accuracy | 0.68 |
| summaries.expanded.known_structure.pairs | 25 |
| summaries.expanded.known_structure.both_correct | 9 |
| summaries.expanded.known_structure.both_accuracy | 0.36 |
| summaries.expanded.expected_train_continuation_nll_per_token | 0.45051700545170853 |
| summaries.expanded.training_seconds | 38.66412512899842 |
| summaries.expanded.source_tokens.web | 0 |
| summaries.expanded.source_tokens.short | 24969216 |
| summaries.expanded.source_EOS.web | 0 |
| summaries.expanded.source_EOS.short | 444694 |
| comparisons.compact__expanded.quality.checks.coherence_gain_at_least8 | false |
| comparisons.compact__expanded.quality.checks.paired_CI_lower_above0 | false |
| comparisons.compact__expanded.quality.checks.EOS_nonworsening | true |
| comparisons.compact__expanded.quality.checks.repetition_nonworsening | false |
| comparisons.compact__expanded.quality.checks.no_empty_role_unicode | true |
| comparisons.compact__expanded.quality.checks.BPB_gate | false |
| comparisons.compact__expanded.quality.checks.appropriate_completion_not_punctuation | true |
| comparisons.compact__expanded.quality.passed | false |
| comparisons.compact__expanded.practical.coherence_at_least27 | false |
| comparisons.compact__expanded.practical.appropriate_at_least27 | false |
| comparisons.compact__expanded.practical.EOS_at_least37 | true |
| comparisons.compact__expanded.practical.repetition_at_most18 | true |
| comparisons.compact__expanded.original_Web_gates.EOS_at_least8_more | true |
| comparisons.compact__expanded.original_Web_gates.repetition_no_worse | true |
| comparisons.compact__expanded.original_Web_gates.no_empty_role_unicode | true |
| comparisons.compact__expanded.original_Web_gates.BPB_degradation_at_most1percent | false |
| comparisons.compact__expanded.paired_diagnostics.semantics.point | 0.0625 |
| comparisons.compact__expanded.paired_diagnostics.semantics.ci95 | [0.015625, 0.109375] |
| comparisons.compact__expanded.paired_diagnostics.semantics.units | 96 |
| comparisons.compact__expanded.paired_diagnostics.semantics.examples | 192 |
| comparisons.compact__expanded.paired_diagnostics.semantics.unit | "family/prompt" |
| comparisons.compact__expanded.paired_diagnostics.semantics.seed | 42 |
| comparisons.compact__expanded.paired_diagnostics.semantics.repetitions | 2000 |
| comparisons.compact__expanded.paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| comparisons.compact__expanded.paired_diagnostics.jblimp.point | -0.030211480362537766 |
| comparisons.compact__expanded.paired_diagnostics.jblimp.ci95 | [-0.06948640483383686, 0.00906344410876133] |
| comparisons.compact__expanded.paired_diagnostics.jblimp.units | 331 |
| comparisons.compact__expanded.paired_diagnostics.jblimp.examples | 331 |
| comparisons.compact__expanded.paired_diagnostics.jblimp.unit | "family/prompt" |
| comparisons.compact__expanded.paired_diagnostics.jblimp.seed | 42 |
| comparisons.compact__expanded.paired_diagnostics.jblimp.repetitions | 2000 |
| comparisons.compact__expanded.paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| comparisons.compact__expanded.paired_diagnostics.jcqa.point | -0.05272564789991063 |
| comparisons.compact__expanded.paired_diagnostics.jcqa.ci95 | [-0.07596067917783736, -0.029490616621983913] |
| comparisons.compact__expanded.paired_diagnostics.jcqa.units | 1119 |
| comparisons.compact__expanded.paired_diagnostics.jcqa.examples | 1119 |
| comparisons.compact__expanded.paired_diagnostics.jcqa.unit | "family/prompt" |
| comparisons.compact__expanded.paired_diagnostics.jcqa.seed | 42 |
| comparisons.compact__expanded.paired_diagnostics.jcqa.repetitions | 2000 |
| comparisons.compact__expanded.paired_diagnostics.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| comparisons.compact__expanded.eligible_for_full | false |
| condition_parent.train.summary.correct | 46 |
| condition_parent.train.summary.accuracy | 0.46 |
| condition_parent.train.summary.pairs | 50 |
| condition_parent.train.summary.both_correct | 4 |
| condition_parent.train.summary.both_accuracy | 0.08 |
| condition_parent.train.by_category.reference.correct | 14 |
| condition_parent.train.by_category.reference.accuracy | 0.7 |
| condition_parent.train.by_category.reference.pairs | 10 |
| condition_parent.train.by_category.reference.both_correct | 4 |
| condition_parent.train.by_category.reference.both_accuracy | 0.4 |
| condition_parent.train.by_category.quantity.correct | 10 |
| condition_parent.train.by_category.quantity.accuracy | 0.5 |
| condition_parent.train.by_category.quantity.pairs | 10 |
| condition_parent.train.by_category.quantity.both_correct | 0 |
| condition_parent.train.by_category.quantity.both_accuracy | 0.0 |
| condition_parent.train.by_category.negation.correct | 5 |
| condition_parent.train.by_category.negation.accuracy | 0.25 |
| condition_parent.train.by_category.negation.pairs | 10 |
| condition_parent.train.by_category.negation.both_correct | 0 |
| condition_parent.train.by_category.negation.both_accuracy | 0.0 |
| condition_parent.train.by_category.time.correct | 7 |
| condition_parent.train.by_category.time.accuracy | 0.35 |
| condition_parent.train.by_category.time.pairs | 10 |
| condition_parent.train.by_category.time.both_correct | 0 |
| condition_parent.train.by_category.time.both_accuracy | 0.0 |
| condition_parent.train.by_category.cause.correct | 10 |
| condition_parent.train.by_category.cause.accuracy | 0.5 |
| condition_parent.train.by_category.cause.pairs | 10 |
| condition_parent.train.by_category.cause.both_correct | 0 |
| condition_parent.train.by_category.cause.both_accuracy | 0.0 |
| condition_parent.dev.summary.correct | 46 |
| condition_parent.dev.summary.accuracy | 0.46 |
| condition_parent.dev.summary.pairs | 50 |
| condition_parent.dev.summary.both_correct | 5 |
| condition_parent.dev.summary.both_accuracy | 0.1 |
| condition_parent.dev.by_category.reference.correct | 11 |
| condition_parent.dev.by_category.reference.accuracy | 0.55 |
| condition_parent.dev.by_category.reference.pairs | 10 |
| condition_parent.dev.by_category.reference.both_correct | 4 |
| condition_parent.dev.by_category.reference.both_accuracy | 0.4 |
| condition_parent.dev.by_category.quantity.correct | 10 |
| condition_parent.dev.by_category.quantity.accuracy | 0.5 |
| condition_parent.dev.by_category.quantity.pairs | 10 |
| condition_parent.dev.by_category.quantity.both_correct | 0 |
| condition_parent.dev.by_category.quantity.both_accuracy | 0.0 |
| condition_parent.dev.by_category.negation.correct | 5 |
| condition_parent.dev.by_category.negation.accuracy | 0.25 |
| condition_parent.dev.by_category.negation.pairs | 10 |
| condition_parent.dev.by_category.negation.both_correct | 0 |
| condition_parent.dev.by_category.negation.both_accuracy | 0.0 |
| condition_parent.dev.by_category.time.correct | 10 |
| condition_parent.dev.by_category.time.accuracy | 0.5 |
| condition_parent.dev.by_category.time.pairs | 10 |
| condition_parent.dev.by_category.time.both_correct | 1 |
| condition_parent.dev.by_category.time.both_accuracy | 0.1 |
| condition_parent.dev.by_category.cause.correct | 10 |
| condition_parent.dev.by_category.cause.accuracy | 0.5 |
| condition_parent.dev.by_category.cause.pairs | 10 |
| condition_parent.dev.by_category.cause.both_correct | 0 |
| condition_parent.dev.by_category.cause.both_accuracy | 0.0 |
| condition_parent.dev.known_structure.correct | 24 |
| condition_parent.dev.known_structure.accuracy | 0.48 |
| condition_parent.dev.known_structure.pairs | 25 |
| condition_parent.dev.known_structure.both_correct | 4 |
| condition_parent.dev.known_structure.both_accuracy | 0.16 |
| condition_parent.dev.unseen_structure.correct | 22 |
| condition_parent.dev.unseen_structure.accuracy | 0.44 |
| condition_parent.dev.unseen_structure.pairs | 25 |
| condition_parent.dev.unseen_structure.both_correct | 1 |
| condition_parent.dev.unseen_structure.both_accuracy | 0.04 |
| scientific_tokens | 49938432 |
| verification_tokens | 262144 |
| GPU_seconds | 263.74788350799645 |
| checked_at | "2026-10-05T10:34:26.345142Z" |
| limits | "Single training seed; Codex authored synthetic examples and nonblind content scoring; dev reused for branch selection; no independent human/test evaluation" |

</details>

<details>
<summary>reports/phase6/condition_transfer_curriculum_notes.json — None</summary>

[原記録](../../reports/phase6/condition_transfer_curriculum_notes.json) ／ SHA256: `b071bbb838501ccf03cba2c26098b8e776a3e585762d74bcb1115b4f0b9638d6` ／ 17,473 bytes

| 原キー | 保存値 |
|---|---|
| rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/historical_parent-scores.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/historical_parent-scores.json) ／ SHA256: `8fca3f225b9a42086d86177a4cd0d523b0e25ef67f71170a8bfbc05968053899` ／ 1,281,695 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| ledgers.bridge.original.valid_input_tokens | 25066 |
| ledgers.bridge.original.physical_input_positions | 30368 |
| ledgers.bridge.original.scored_target_tokens | 4532 |
| ledgers.bridge.original.scored_target_bytes | 16962 |
| ledgers.bridge.BOS-only.valid_input_tokens | 4532 |
| ledgers.bridge.BOS-only.physical_input_positions | 7024 |
| ledgers.bridge.BOS-only.scored_target_tokens | 4532 |
| ledgers.bridge.BOS-only.scored_target_bytes | 16962 |
| ledgers.retention.original.valid_input_tokens | 22240 |
| ledgers.retention.original.physical_input_positions | 32384 |
| ledgers.retention.original.scored_target_tokens | 3170 |
| ledgers.retention.original.scored_target_bytes | 13220 |
| ledgers.retention.BOS-only.valid_input_tokens | 3170 |
| ledgers.retention.BOS-only.physical_input_positions | 5648 |
| ledgers.retention.BOS-only.scored_target_tokens | 3170 |
| ledgers.retention.BOS-only.scored_target_bytes | 13220 |
| checks.weights_unchanged | true |
| checks.RNG_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.CPU_FP32 | true |
| checks.CUDA_not_initialized | true |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0000.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0000.json) ／ SHA256: `8dab1965e0d1ce2cf4f561b9cd097e4d53cc8a5fec6d7cf0cd9d56224a7f8bcc` ／ 9,813 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 148 |
| physical_input_positions | 240 |
| scored_target_tokens | 148 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0016.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0016.json) ／ SHA256: `6b10a307a18d9a9f54bab811b8b1045e1b9da065d7e4bd1f9e94ce3659148ba2` ／ 9,482 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 140 |
| physical_input_positions | 208 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0032.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0032.json) ／ SHA256: `140b029e6c9fe6a84d79cf2e301f08194687b7c03270a81b4a80716624bfc3c4` ／ 10,104 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 154 |
| physical_input_positions | 240 |
| scored_target_tokens | 154 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0048.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0048.json) ／ SHA256: `d3257c65572cc80a9a13bdeacc3b17492212a34a6ad04c95aa5fe359ed9d3b2c` ／ 9,394 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 138 |
| physical_input_positions | 208 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0064.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0064.json) ／ SHA256: `7e945048c3aba520df5d9d2782c662c507aea0b4b29e0706aa70dec4a08ccf86` ／ 10,180 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 156 |
| physical_input_positions | 240 |
| scored_target_tokens | 156 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0080.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0080.json) ／ SHA256: `e305665e5494b3c723e120dcdea3e6ebee8acd7bf01bf8a47536b24f498c07b5` ／ 9,578 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 142 |
| physical_input_positions | 224 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0096.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0096.json) ／ SHA256: `e119b00558285198f1a4b86d4a44434f05e1f7406830eb622e626e7d0ca9521c` ／ 9,684 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 144 |
| physical_input_positions | 240 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0112.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0112.json) ／ SHA256: `c0839d47db65e984c8298b21d5fa04a1e49ce50254c48e0486cde5f3c3dfe44d` ／ 10,021 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 152 |
| physical_input_positions | 240 |
| scored_target_tokens | 152 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0128.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0128.json) ／ SHA256: `ab6ab8af27151aadddc2e84cd958f25516a7ddb6a4b33c76ceb7e0b670d7aaa5` ／ 9,675 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 144 |
| physical_input_positions | 224 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0144.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0144.json) ／ SHA256: `8bb29ed93ca32ed68d1c23724111579d803434d30a0bf5245b0bd6162e609ce8` ／ 9,769 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 146 |
| physical_input_positions | 240 |
| scored_target_tokens | 146 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0160.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0160.json) ／ SHA256: `637212ee5d463cf6fbcd1faf1f259640420d65b707ee045d9d891356a0989468` ／ 10,013 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 152 |
| physical_input_positions | 240 |
| scored_target_tokens | 152 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0176.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0176.json) ／ SHA256: `6d05a9c6ed659ad21dc34ce71cc0c1297df6b85e3e75b8bf947074ee068a9338` ／ 9,851 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 148 |
| physical_input_positions | 240 |
| scored_target_tokens | 148 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0192.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0192.json) ／ SHA256: `ee9b9dc621262df4d6184d9cf04779c8de2f47730e299021dc378bd2cb87029e` ／ 9,765 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 146 |
| physical_input_positions | 224 |
| scored_target_tokens | 146 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0208.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0208.json) ／ SHA256: `44ec7408b87854c061fe4bd0c77b629f7b5a831c4da13c8b3e63d76a5e59cbce` ／ 9,507 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 140 |
| physical_input_positions | 208 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0224.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0224.json) ／ SHA256: `36ee8bc7ecb1e93cf98eaba764cf95a95a14ac2e21d28487aea6036e09d1ec4b` ／ 9,665 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 144 |
| physical_input_positions | 224 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0240.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0240.json) ／ SHA256: `a8553215fa8c3020ad867c55777ead0559395f3213e5edd1b9444a9216b9613c` ／ 9,503 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 140 |
| physical_input_positions | 208 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0256.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0256.json) ／ SHA256: `a9e92620594ac9528b5b0720af86f4a1d51da153ccb04513b8afa32d5b3eb386` ／ 9,439 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 138 |
| physical_input_positions | 208 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0272.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0272.json) ／ SHA256: `9fba272441e3e7dbdc404068805ba98c05740511cde04d43a16d74b9f6c4e259` ／ 9,433 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 138 |
| physical_input_positions | 208 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0288.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0288.json) ／ SHA256: `e4efd37e92aa4f044e7a7f6f4a0a150b93ab3bdc1bda8aa764a4a64e94ab2338` ／ 9,419 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 138 |
| physical_input_positions | 208 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0304.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0304.json) ／ SHA256: `11df2fceac014912183a97a6e18d85e8e82345b702f2852ae8bb346464caf46c` ／ 9,605 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 142 |
| physical_input_positions | 208 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0320.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0320.json) ／ SHA256: `0a85859e3b3f4eb4c3d61a83b9ae4f49dc2d6b84bc691ce612c31fcd18293065` ／ 9,179 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 132 |
| physical_input_positions | 192 |
| scored_target_tokens | 132 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0336.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0336.json) ／ SHA256: `eb13733cc8617cf67466b83112be6755f559117472d5787897c14f8c616d7eb7` ／ 9,269 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 134 |
| physical_input_positions | 208 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0352.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0352.json) ／ SHA256: `75bd145e235a8dd23df0a6d44bd1720b29239f3bc19cd19d4b28327ee77b28cb` ／ 9,601 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 142 |
| physical_input_positions | 224 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0368.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0368.json) ／ SHA256: `9292e2bd74de9e4cad4207e96fa6c37adc417a213bad6b0a422b373545098bad` ／ 9,369 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 136 |
| physical_input_positions | 208 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0384.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0384.json) ／ SHA256: `1a9caf4aa6f8554eea565c69643377aadc6cf23072919609716f38060b4bbf91` ／ 9,675 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 144 |
| physical_input_positions | 224 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0400.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0400.json) ／ SHA256: `f2022068cf846ce032b89852750cabdc528ce39f8202131062d2c09a0b3e973a` ／ 9,367 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 136 |
| physical_input_positions | 224 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0416.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0416.json) ／ SHA256: `cdfc42bd13eef3f8d0f8ce829143c69a319a231c1169c3d625506660bed0bbfd` ／ 9,685 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 144 |
| physical_input_positions | 224 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0432.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0432.json) ／ SHA256: `f8b35a9d6fa45026bb9e41735bcc5632c8676a74cf2f15b7e9464f65f08e6939` ／ 9,183 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 132 |
| physical_input_positions | 208 |
| scored_target_tokens | 132 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0448.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0448.json) ／ SHA256: `15eeae6004a551cbf95dfb90a82602dcc590c866775b92dd4b3012988d1f5495` ／ 9,457 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 138 |
| physical_input_positions | 208 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0464.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0464.json) ／ SHA256: `ac1255edececbc48b4f46510cd51c44c4eb4c5c1115fa311833e0a5867abfec9` ／ 9,255 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 134 |
| physical_input_positions | 208 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0480.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0480.json) ／ SHA256: `8fa7020be5983b6e3fb8890b9040621c25d027c569a71c0828f4cd573dda38c0` ／ 9,267 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 134 |
| physical_input_positions | 208 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0496.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/BOS-only/0496.json) ／ SHA256: `fd1a3c7c8cf07d6405aef13be162a1fcbb37d1424d956d450b1f61f856d6728a` ／ 9,337 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 136 |
| physical_input_positions | 208 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0000.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0000.json) ／ SHA256: `b4fa80da8e8095203b54b64270f964b55c687639b456fa53712bd6d9f3175bfd` ／ 9,913 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 706 |
| physical_input_positions | 816 |
| scored_target_tokens | 148 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0016.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0016.json) ／ SHA256: `52c5c81be15021336a880e4577189d1849dbf51ddc7750e94cec34126329dea2` ／ 9,571 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 772 |
| physical_input_positions | 1024 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0032.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0032.json) ／ SHA256: `690cee559aed63f144011becb4045324d48cb589406ac5b8c9e202cb02ef5d05` ／ 10,197 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 708 |
| physical_input_positions | 768 |
| scored_target_tokens | 154 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0048.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0048.json) ／ SHA256: `d282467887b0ee8cb89ac83c9b4d9436d2abd605ce9b99d6309b8deef02e8185` ／ 9,484 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 766 |
| physical_input_positions | 1008 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0064.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0064.json) ／ SHA256: `f91a11d74d4ac47c38521e73cbaaced08d3cc1bc1cc51028bda05d38fa38bef3` ／ 10,275 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 718 |
| physical_input_positions | 784 |
| scored_target_tokens | 156 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0080.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0080.json) ／ SHA256: `2c97681077d65185f9bc3e4856c23b24149946094b839bce63503e4a867a26bb` ／ 9,689 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 770 |
| physical_input_positions | 1008 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0096.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0096.json) ／ SHA256: `5cb7ba6fd42f7d6ef04e225306ab46b8e0788f1787bb25d20478f0ea58d1e8eb` ／ 9,780 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 686 |
| physical_input_positions | 768 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0112.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0112.json) ／ SHA256: `bcc79183eacef3af6f23f088b440a6b73f731df3663b3f73f6294b9e9297eca9` ／ 10,124 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 800 |
| physical_input_positions | 1040 |
| scored_target_tokens | 152 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0128.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0128.json) ／ SHA256: `3f8966c65645eb10ad80126e04758f99b5206714edbdadfef05ea980c36501eb` ／ 9,794 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 690 |
| physical_input_positions | 784 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0144.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0144.json) ／ SHA256: `168914a8598699a21b44461c214868d5217060c89640ebc51f0f9af63e806606` ／ 9,860 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 786 |
| physical_input_positions | 1040 |
| scored_target_tokens | 146 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0160.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0160.json) ／ SHA256: `bd59340d0432884d4342eeda3526729d7a3b6fa6b036c0bae35b1a41fcdb43ee` ／ 10,153 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 710 |
| physical_input_positions | 800 |
| scored_target_tokens | 152 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0176.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0176.json) ／ SHA256: `dc28bce05b80b7ed6a30262cb9ce3a3a54ef320cb18a499e62725cf199892e3d` ／ 9,949 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 792 |
| physical_input_positions | 1040 |
| scored_target_tokens | 148 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0192.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0192.json) ／ SHA256: `f2a1a89888992d7c77183b3f980339828a51ed402ac96b7a7359fd759b601a13` ／ 9,859 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 700 |
| physical_input_positions | 800 |
| scored_target_tokens | 146 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0208.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0208.json) ／ SHA256: `275cd868a20ca05ec9ed41a4ad7c70f8943f79beaed25b29b2b6e2355b970203` ／ 9,609 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 784 |
| physical_input_positions | 1040 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0224.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0224.json) ／ SHA256: `eaa22e0209d113712b32ce7754495e1159f078a6045357a22a8ae1ace92d6ca6` ／ 9,775 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 702 |
| physical_input_positions | 800 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0240.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0240.json) ／ SHA256: `1fb05d043e4d4807139da51d647a7a101514aeb824959ea39fa25fc4d9130b2a` ／ 9,592 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 768 |
| physical_input_positions | 1008 |
| scored_target_tokens | 140 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0256.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0256.json) ／ SHA256: `666317570d1bd132d44c31f358e42855cc76dbdc57bcec6aa91406d69d726206` ／ 9,560 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 824 |
| physical_input_positions | 960 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0272.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0272.json) ／ SHA256: `2e2e30800c7865a1e45a49b3536b2b405d97c6a06733faa8952ad9cae4c625d6` ／ 9,525 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 822 |
| physical_input_positions | 992 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0288.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0288.json) ／ SHA256: `05ec1739b56d4c6c2966f427f9bc44fed5c2591d20f68a52ffc4c26251174a64` ／ 9,534 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 836 |
| physical_input_positions | 1008 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0304.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0304.json) ／ SHA256: `d89c46538ecdd65a0efa949967d4cc143b51e2d66b0a0f77774e8882e2514c04` ／ 9,746 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 834 |
| physical_input_positions | 1008 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0320.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0320.json) ／ SHA256: `93550838fedfa72a1ab57ab7211736826f795213b471016a031cdcd7e02a4a2a` ／ 9,282 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 818 |
| physical_input_positions | 976 |
| scored_target_tokens | 132 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0336.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0336.json) ／ SHA256: `60007fabffb50ba7bae55c6dd33701e4005dea02f4a72f1fea8a8a6e9b9f0c30` ／ 9,362 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 820 |
| physical_input_positions | 1008 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0352.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0352.json) ／ SHA256: `dbf7175d805a3501e1eb3eab475dfda5661bdab5c11251f0ebe9b3f575881a43` ／ 9,714 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 830 |
| physical_input_positions | 976 |
| scored_target_tokens | 142 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0368.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0368.json) ／ SHA256: `01c41399256f087766666c8c0edce6f452247e4f3684aab61c658ab02505a46e` ／ 9,453 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 822 |
| physical_input_positions | 1008 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0384.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0384.json) ／ SHA256: `c0d0b0df1fc8a00a7ea756058c5f06bd65e3db25290f918f07d9b481cd764597` ／ 9,793 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 842 |
| physical_input_positions | 1008 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0400.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0400.json) ／ SHA256: `f9a58f7abec38dad04092724eb3c18a9dc805365c92417afff54415c3e40677a` ／ 9,466 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 822 |
| physical_input_positions | 960 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0416.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0416.json) ／ SHA256: `219a9f543e772e0328a8f14adea157e070b8e32e06113944052861eb0f37ec15` ／ 9,810 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 842 |
| physical_input_positions | 992 |
| scored_target_tokens | 144 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0432.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0432.json) ／ SHA256: `1db9182afcf5f1b884cf1c2334f009ad4870144ac03ab60059dd0f927d8fa5c7` ／ 9,275 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 818 |
| physical_input_positions | 960 |
| scored_target_tokens | 132 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0448.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0448.json) ／ SHA256: `4ada42a40c675c76c9eb40fe1163622a1e7cbb10af729c51756c757e9993896b` ／ 9,530 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 820 |
| physical_input_positions | 992 |
| scored_target_tokens | 138 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0464.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0464.json) ／ SHA256: `86c8b4ac53182011f94e11e45b27a98318cc63086be865fb1c2f18ab3f46643b` ／ 9,350 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 816 |
| physical_input_positions | 1008 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0480.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0480.json) ／ SHA256: `999419dda266616e90515836e0530138cffabda8f49edc2f8b4c723083e081ef` ／ 9,384 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 816 |
| physical_input_positions | 976 |
| scored_target_tokens | 134 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0496.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/bridge/original/0496.json) ／ SHA256: `ac32827606888ae491a2f944aab22c51b0f2e82b7a4b5d9940de13c773c7df5d` ／ 9,456 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 826 |
| physical_input_positions | 1008 |
| scored_target_tokens | 136 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0000.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0000.json) ／ SHA256: `c64cd382624c7f9b2ee9af124abe6b844cd9179ca6d5fb8c6f960a38d64407d7` ／ 7,939 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 102 |
| physical_input_positions | 208 |
| scored_target_tokens | 102 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0016.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0016.json) ／ SHA256: `7a41a677435430391757d0589a56c5ab00cf1f7042957fe93ab3e9fd1259d1de` ／ 8,284 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 110 |
| physical_input_positions | 208 |
| scored_target_tokens | 110 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0032.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0032.json) ／ SHA256: `c556eb0f9e09ccc0f1d765cf3b7a8583267189960649252d34a456042dcd9860` ／ 6,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 78 |
| physical_input_positions | 96 |
| scored_target_tokens | 78 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0048.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0048.json) ／ SHA256: `0df563914e5794f1268df95b4113025406ff785b07937c7b91158d9b9469baba` ／ 8,116 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 224 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0064.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0064.json) ／ SHA256: `a7892d97c73a045ed8c8d2589640ec58a9a1774638b4250937561203facf454b` ／ 8,452 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 114 |
| physical_input_positions | 224 |
| scored_target_tokens | 114 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0080.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0080.json) ／ SHA256: `2e9d4d76202f73da99c8bba448eb4462fd629e2a1c9a36270195ded0c951dae6` ／ 7,065 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0096.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0096.json) ／ SHA256: `66e3cf8c61f5513fee8c5acda3bce616609d2c100191a703d06f4e9fe8b1df77` ／ 7,994 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 104 |
| physical_input_positions | 208 |
| scored_target_tokens | 104 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0112.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0112.json) ／ SHA256: `cdac4fa6dc3c7019b0171af7e3f257273e660d7be13104e7d8bc97f50f1a8105` ／ 8,217 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 108 |
| physical_input_positions | 208 |
| scored_target_tokens | 108 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0128.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0128.json) ／ SHA256: `09c6d1c1b1b8095b56bf80ccc4a386c8dcd8d5bc3f9b89d8ad4f4cc2dbe3e67b` ／ 7,072 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0144.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0144.json) ／ SHA256: `f5a8ad2a2bdc2ccf328937d8a7c25e8a5977c84cd8b7521ab3e25e072429548d` ／ 8,141 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 224 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0160.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0160.json) ／ SHA256: `593e8745e1889452ebcaf13fd33e5af999f97e404f5983aa36f91d43779d6d8e` ／ 8,551 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 116 |
| physical_input_positions | 240 |
| scored_target_tokens | 116 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0176.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0176.json) ／ SHA256: `b7e26a9398b1405dcc4b42419690600c1dfcbd5e06b9faad43c269721eb8dc49` ／ 6,920 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 76 |
| physical_input_positions | 96 |
| scored_target_tokens | 76 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0192.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0192.json) ／ SHA256: `9f062e58f6aa91a021260d0dc9a065620ea98aced95c42024c019cfb75745775` ／ 8,121 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 224 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0208.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0208.json) ／ SHA256: `bf23b41582c6f899d816750e3878ce81c43ecea97072f90df6cf22371223b11a` ／ 8,483 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 114 |
| physical_input_positions | 224 |
| scored_target_tokens | 114 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0224.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0224.json) ／ SHA256: `48f01f76d15d6e643e900d23bbeeda36e1521282980b9dd0d4c647996a6d2953` ／ 7,082 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0240.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0240.json) ／ SHA256: `c135eee80ac4c735e7ba6813611f0e765657b55419b57a66bd46f99716aaa08b` ／ 8,303 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 110 |
| physical_input_positions | 240 |
| scored_target_tokens | 110 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0256.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0256.json) ／ SHA256: `598bef904535ced071cda0c085961a0761286d6fd2288f7bbd1da64658ba55cc` ／ 8,215 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 108 |
| physical_input_positions | 224 |
| scored_target_tokens | 108 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0272.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0272.json) ／ SHA256: `7fb8364a272a9fc2b2bab1f351ed507ebed62e13fc6be4c7a0123cd156fda58b` ／ 8,367 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 112 |
| physical_input_positions | 208 |
| scored_target_tokens | 112 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0288.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0288.json) ／ SHA256: `778d48bd94ed06acfd9240eba87b507dad48afaf9346f0f46b92d3d5e6c26fcd` ／ 7,080 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0304.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0304.json) ／ SHA256: `898f67f4fc403bb383087f1a8693b251c9d078a2ec7703e61b264fcd0621eaf0` ／ 8,119 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 208 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0320.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0320.json) ／ SHA256: `f98a69df726b258dafb312390fa8e97e188d707d9b5caa34351311e340085abd` ／ 8,541 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 116 |
| physical_input_positions | 208 |
| scored_target_tokens | 116 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0336.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0336.json) ／ SHA256: `e233f27db8d07544f72e79ebf9c7eb416cbdb1b62bbf5b41446a6224c916c4d2` ／ 7,080 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0352.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0352.json) ／ SHA256: `d9b5a12910a7a35daae15208f61b3ac8e2ddcb936bc50ee4da0c0bd97005be7a` ／ 8,103 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 208 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0368.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0368.json) ／ SHA256: `2cbef3a98affdf91721bc47bb541e1871d8e24965d54189e237b635ef8c534d2` ／ 8,123 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 192 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0384.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0384.json) ／ SHA256: `acdbb6b6aca4bd30d531c1e2cae1fde70b56c0bc8a46d9200120c1b2521e54d5` ／ 6,994 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 78 |
| physical_input_positions | 96 |
| scored_target_tokens | 78 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0400.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0400.json) ／ SHA256: `b7c2cc64efaf4f83a283391dc8838aa31a9543dbdbd42f449227c663b3facdc9` ／ 8,139 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 208 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0416.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0416.json) ／ SHA256: `25a3890ac546cbb1fc743802023cad0b42d0792a183436a9548c1ea4a0e01e3f` ／ 8,153 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 106 |
| physical_input_positions | 176 |
| scored_target_tokens | 106 |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0432.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/scores/historical_parent/retention/BOS-only/0432.json) ／ SHA256: `7f3781b1b357ca5f163d45ce49f09be383e39552ccf1230b9dc9a36ab401c4a5` ／ 7,086 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| valid_input_tokens | 80 |
| physical_input_positions | 96 |
| scored_target_tokens | 80 |

</details>
