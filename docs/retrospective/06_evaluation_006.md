# 評価・生成・意味診断 — 6/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/control-content-review.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/control-content-review.json) ／ SHA256: `06dbc45a8021dce32601aade8ece18b8a3e269c98faa06a37255b01c74d2d989` ／ 881 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.1435587102961566 |
| rates.eos | 44 |
| rates.repetition | 26 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 54 |
| relevance2 | 43 |
| coherent | 15 |
| appropriate | 27 |
| new_teacher_tokens | 25000000 |
| source_teacher_tokens.web | 18750000 |
| source_teacher_tokens.story | 1250000 |
| source_teacher_tokens.ordinary_textbook | 2500000 |
| source_teacher_tokens.conditional_textbook | 2500000 |
| focus_teacher_tokens | 654588 |
| weighted_teacher_mass | 25000000 |
| notes_sha256 | "790bd83a371d1cd6c273b1383da320061e3f00bd76f4e49b45455ae1a907ea70" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/control/training/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/control/training/latest.json) ／ SHA256: `50c0d406fb33bfb7008c16fd24e144c84f091cfddcdef5258977d2c8f2b95478` ／ 283 bytes

| 原キー | 保存値 |
|---|---|
| update | 62936 |
| tokens_seen | 2062286848 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/body.json) ／ SHA256: `20123a0aab5b823cbbe17deca4ddfa2e913d4bd850e4c3bd9b8e7e1176272d41` ／ 67,262 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 374176.51803684235 |
| body.eos_nll | 947.4363566637039 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1435587102961566 |
| body.seconds | 1.539865662023658 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/generation.json) ／ SHA256: `ff284ac9c24fb63beb865b413bf3bb95fca2e269adcd099f8e6b45417e0a206b` ／ 91,376 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/jblimp.json) ／ SHA256: `e74cce62311ccd492a4ae21c102fe0508655a9b91626bb445b9eb8b6e72ea7e1` ／ 338,435 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7915407854984894 |
| summary.primary.accuracy.ci95 | [0.743202416918429, 0.8338368580060423] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7915407854984894 |
| summary.per_token_secondary.accuracy.point | 0.7311178247734139 |
| summary.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7794561933534743] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| summary.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/jcqa.json) ／ SHA256: `d6d1ddfd180c181d1e016a8495337b673e83059d1d9bc8dbd32b45c51e5b2440` ／ 1,639,548 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.29848078641644327 |
| summary.primary.accuracy.ci95 | [0.2725647899910634, 0.32529043789097406] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.29848078641644327 |
| summary.per_token_secondary.accuracy.point | 0.290437890974084 |
| summary.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.290437890974084 |
| summary.per_token_secondary.macro_f1 | 0.2899833679971908 |
| summary.per_token_secondary.mcc | 0.11364311165128803 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/result.json) ／ SHA256: `1ae690ab5f027dff18dafeceefd88984efa2d62493a432a770560909964cc5a7` ／ 186,104 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 18750000 |
| binding.teacher_goals.story | 1250000 |
| binding.teacher_goals.ordinary_textbook | 2500000 |
| binding.teacher_goals.conditional_textbook | 2500000 |
| binding.loss | "normalized positive-outcome CE body+EOS" |
| binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoint_sha256 | "5f0805346dac73616e429c9cde54f9a81eaaf219ef79e11797a84c37525b8a60" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 374176.51803684235 |
| body.eos_nll | 947.4363566637039 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1435587102961566 |
| body.seconds | 1.539865662023658 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 44 |
| greedy_rates.repetition | 26 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5260416666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.4947916666666667, 0.5572916666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5260416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
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
| diagnostics.jblimp.primary.accuracy.ci95 | [0.743202416918429, 0.8338368580060423] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6797583081570997, 0.7794561933534743] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| diagnostics.jcqa.primary.accuracy.point | 0.29848078641644327 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2725647899910634, 0.32529043789097406] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.29848078641644327 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2899833679971908 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.11364311165128803 |
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
| diagnostics.semantic_both_contexts.correct | 8 |
| memory.maximum_observed_allocated_bytes | 275218432 |
| memory.maximum_observed_reserved_bytes | 13289652224 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/semantics.json) ／ SHA256: `2c68c9a6795da3cad2b688abb47fb0abb035f48287ed481cc1278f2fb4e79143` ／ 203,335 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5260416666666666 |
| summary.primary.accuracy.ci95 | [0.4947916666666667, 0.5572916666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5260416666666666 |
| summary.per_token_secondary.accuracy.point | 0.609375 |
| summary.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.609375 |
| summary.per_token_secondary.macro_f1 | 0.6091099106924727 |
| summary.per_token_secondary.mcc | 0.21904730367901812 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/body.json) ／ SHA256: `8c78cbc15dec34bd29e1bf926241f6c65dbc2022c336bdfc6c9d35827f617515` ／ 67,251 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 374712.80347824097 |
| body.eos_nll | 944.6387304514647 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.145197706486869 |
| body.seconds | 1.284524454997154 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/generation.json) ／ SHA256: `7037614ad5495e64930274d1b39a2dad9e9f0c015f526eb1021944c12a0e74b1` ／ 91,498 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/jblimp.json) ／ SHA256: `30ff7af151bb3d07ed8746423f7f573accd4b833c4d49bb43f0982260792556e` ／ 338,498 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7854984894259819 |
| summary.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7854984894259819 |
| summary.per_token_secondary.accuracy.point | 0.7280966767371602 |
| summary.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7764350453172205] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| summary.per_token_secondary.macro_f1 | 0.42132867132867136 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/jcqa.json) ／ SHA256: `bb87d6d14506aac35e007105a8c38cb619083578b3956f270bb452a54f9a74e8` ／ 1,639,715 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.2993744414655943 |
| summary.primary.accuracy.ci95 | [0.2734584450402145, 0.3261840929401251] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.2993744414655943 |
| summary.per_token_secondary.accuracy.point | 0.290437890974084 |
| summary.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.290437890974084 |
| summary.per_token_secondary.macro_f1 | 0.2900528226748983 |
| summary.per_token_secondary.mcc | 0.1136717024098022 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/result.json) ／ SHA256: `aea6c1f1ec178bd62e3e0ca2496306335e864de435e4b5bc3dc19980f3cec7a4` ／ 186,193 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 18750000 |
| binding.teacher_goals.story | 1250000 |
| binding.teacher_goals.ordinary_textbook | 2500000 |
| binding.teacher_goals.conditional_textbook | 2500000 |
| binding.loss | "normalized positive-outcome CE body+EOS" |
| binding.sampler_policy | "Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage" |
| checkpoint_sha256 | "101ab7f4c2e165d8def1aa580b826c691986add92da910ce1f92fe98a24b6db6" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 374712.80347824097 |
| body.eos_nll | 944.6387304514647 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.145197706486869 |
| body.seconds | 1.284524454997154 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 47 |
| greedy_rates.repetition | 22 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5520833333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.515625, 0.5885416666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5520833333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| diagnostics.semantics.per_token_secondary.mcc | 0.21904730367901812 |
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
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7854984894259819 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7764350453172205] |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| diagnostics.jcqa.primary.accuracy.point | 0.2993744414655943 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2734584450402145, 0.3261840929401251] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.2993744414655943 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.290437890974084 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2645218945487042, 0.31724754244861486] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.290437890974084 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2900528226748983 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.1136717024098022 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/evaluation/positive4/evaluation/semantics.json) ／ SHA256: `952822f66824199dc4799245a1b7aedb7fa58c6d663c155016bf04b389c2fcdd` ／ 203,317 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5520833333333334 |
| summary.primary.accuracy.ci95 | [0.515625, 0.5885416666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5520833333333334 |
| summary.per_token_secondary.accuracy.point | 0.609375 |
| summary.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.609375 |
| summary.per_token_secondary.macro_f1 | 0.6091099106924727 |
| summary.per_token_secondary.mcc | 0.21904730367901812 |
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
<summary>reports/phase6/condition-positive-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/job.json) ／ SHA256: `955340122ca812dd9c96e02609c0c948f016b5c93a015f75f7709516880550e6` ／ 871 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 224.40080486799707 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 24696377 |
| teacher_budget | 25000000 |
| source_teachers.web | 18521779 |
| source_teachers.story | 1234792 |
| source_teachers.ordinary_textbook | 2469974 |
| source_teachers.conditional_textbook | 2469832 |
| loss | 2.3950376510620117 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/positive4-content-review.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/positive4-content-review.json) ／ SHA256: `d5a6d7537ae412effce234476f836a1d37f03562679818276063cd223aea2124` ／ 878 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.145197706486869 |
| rates.eos | 47 |
| rates.repetition | 22 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 61 |
| relevance2 | 45 |
| coherent | 9 |
| appropriate | 24 |
| new_teacher_tokens | 25000000 |
| source_teacher_tokens.web | 18750000 |
| source_teacher_tokens.story | 1250000 |
| source_teacher_tokens.ordinary_textbook | 2500000 |
| source_teacher_tokens.conditional_textbook | 2500000 |
| focus_teacher_tokens | 654588 |
| weighted_teacher_mass | 26963764 |
| notes_sha256 | "2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/positive4/training/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/positive4/training/latest.json) ／ SHA256: `9ba1478d8075fc5154df21f6a4874900341b4ad73cbc9404060310402d0e468f` ／ 285 bytes

| 原キー | 保存値 |
|---|---|
| update | 62936 |
| tokens_seen | 2062286848 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/control/timing/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/control/timing/latest.json) ／ SHA256: `a748cf986b8150e936adb884f3c171478675b407f43a83b718ca0822c6468715` ／ 278 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/job.json) ／ SHA256: `f6c949563e1d063dd7144c30294bf74caf35747a7eb7743f9f6a38cd4d644707` ／ 599 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 22.01919901598012 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/positive4/timing/latest.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/positive4/timing/latest.json) ／ SHA256: `7cc5d6c39681efde057f7f43d0469c29f42853ee3cf0ce2df909a69d0629f723` ／ 280 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/probe/result.json — actual_condition_positive_resume_and_timing_complete</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/probe/result.json) ／ SHA256: `44d77fe6cc5e1ea583dc8f460e44f01208eba8c8b537c0b14b77da8ee5c28806` ／ 145,530 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_condition_positive_resume_and_timing_complete" |
| gates.control.passed | true |
| gates.control.checks.model | true |
| gates.control.checks.optimizer | true |
| gates.control.checks.scheduler | true |
| gates.control.checks.rng | true |
| gates.control.checks.sampler | true |
| gates.control.checks.lineage | true |
| gates.control.checks.tokens | true |
| gates.control.checks.supervised_tokens | true |
| gates.control.checks.body_bytes | true |
| gates.control.checks.token_digest | true |
| gates.control.checks.focus_token_digest | true |
| gates.control.checks.focus_teacher_tokens | true |
| gates.control.checks.weighted_teacher_mass | true |
| gates.control.checks.update | true |
| gates.control.checks.spec | true |
| gates.control.checks.model_config | true |
| gates.control.checks.pilot_binding | true |
| gates.control.checks.study_binding | true |
| gates.control.checks.history_loss | true |
| gates.control.checks.history_gradient_norm | true |
| gates.control.checks.history_lr | true |
| gates.control.checks.history_token_digest | true |
| gates.control.checks.history_source_teachers | true |
| gates.control.checks.history_source_eos | true |
| gates.control.checks.history_source_input_tokens | true |
| gates.control.checks.history_source_body_bytes | true |
| gates.control.checks.history_source_focus_teachers | true |
| gates.control.checks.history_focus_token_digest | true |
| gates.control.checks.history_focus_teacher_tokens | true |
| gates.control.checks.history_weighted_teacher_mass | true |
| gates.control.checks.finite | true |
| gates.control.checks.no_reheat | true |
| gates.control.GPU_optimizer_updates | 8 |
| gates.control.verification_teacher_tokens | 259984 |
| gates.positive4.passed | true |
| gates.positive4.checks.model | true |
| gates.positive4.checks.optimizer | true |
| gates.positive4.checks.scheduler | true |
| gates.positive4.checks.rng | true |
| gates.positive4.checks.sampler | true |
| gates.positive4.checks.lineage | true |
| gates.positive4.checks.tokens | true |
| gates.positive4.checks.supervised_tokens | true |
| gates.positive4.checks.body_bytes | true |
| gates.positive4.checks.token_digest | true |
| gates.positive4.checks.focus_token_digest | true |
| gates.positive4.checks.focus_teacher_tokens | true |
| gates.positive4.checks.weighted_teacher_mass | true |
| gates.positive4.checks.update | true |
| gates.positive4.checks.spec | true |
| gates.positive4.checks.model_config | true |
| gates.positive4.checks.pilot_binding | true |
| gates.positive4.checks.study_binding | true |
| gates.positive4.checks.history_loss | true |
| gates.positive4.checks.history_gradient_norm | true |
| gates.positive4.checks.history_lr | true |
| gates.positive4.checks.history_token_digest | true |
| gates.positive4.checks.history_source_teachers | true |
| gates.positive4.checks.history_source_eos | true |
| gates.positive4.checks.history_source_input_tokens | true |
| gates.positive4.checks.history_source_body_bytes | true |
| gates.positive4.checks.history_source_focus_teachers | true |
| gates.positive4.checks.history_focus_token_digest | true |
| gates.positive4.checks.history_focus_teacher_tokens | true |
| gates.positive4.checks.history_weighted_teacher_mass | true |
| gates.positive4.checks.finite | true |
| gates.positive4.checks.no_reheat | true |
| gates.positive4.GPU_optimizer_updates | 8 |
| gates.positive4.verification_teacher_tokens | 259984 |
| timings.control.verification_teacher_tokens | 1039886 |
| timings.control.terminal_save_seconds | 0.1675578599970322 |
| timings.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/probe/control/timing/checkpoint.pt" |
| timings.control.checkpoint_sha256 | "bcb33e3e686862246e1f94811432a00a995bf8dc35233a3ace5a4b013e1cea0f" |
| timings.positive4.verification_teacher_tokens | 1039886 |
| timings.positive4.terminal_save_seconds | 0.183053562999703 |
| timings.positive4.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/condition-positive-comparison-20261006/probe/positive4/timing/checkpoint.pt" |
| timings.positive4.checkpoint_sha256 | "0b4c7fa124677427ec87d56e5b357f1e4d6c73dcf8131af90c7b006a0f1aa25e" |
| scientific_teacher_tokens | 0 |
| passed | true |
| verification_teacher_tokens | 2599740 |
| GPU_optimizer_updates | 80 |
| GPU_seconds | 22.01919901598012 |

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/progress-result.json) ／ SHA256: `0e0fc6975939207b5ab9e7a1d974d2a480df5f8087777e85d86686fbecff9679` ／ 436,896 bytes

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

</details>

<details>
<summary>reports/phase6/condition-positive-comparison-20261006/review.json — same_input_positive_CE_actual50M_all160_evidence_complete</summary>

[原記録](../../reports/phase6/condition-positive-comparison-20261006/review.json) ／ SHA256: `c9062ff59ff032a18abc05163f85b3e53d8d2b0a79ef5fd028630c2a565d14ea` ／ 4,263 bytes

| 原キー | 保存値 |
|---|---|
| status | "same_input_positive_CE_actual50M_all160_evidence_complete" |
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
| summaries.positive4.BPB | 1.145197706486869 |
| summaries.positive4.rates.eos | 47 |
| summaries.positive4.rates.repetition | 22 |
| summaries.positive4.rates.unicode_failure | 0 |
| summaries.positive4.rates.role_leak | 0 |
| summaries.positive4.rates.empty | 0 |
| summaries.positive4.grammar2 | 61 |
| summaries.positive4.relevance2 | 45 |
| summaries.positive4.coherent | 9 |
| summaries.positive4.appropriate | 24 |
| summaries.positive4.new_teacher_tokens | 25000000 |
| summaries.positive4.source_teacher_tokens.web | 18750000 |
| summaries.positive4.source_teacher_tokens.story | 1250000 |
| summaries.positive4.source_teacher_tokens.ordinary_textbook | 2500000 |
| summaries.positive4.source_teacher_tokens.conditional_textbook | 2500000 |
| summaries.positive4.focus_teacher_tokens | 654588 |
| summaries.positive4.weighted_teacher_mass | 26963764 |
| summaries.positive4.notes_sha256 | "2d3d01ac393fa966b600f3dc991b609a0798358aa474faaf3b2b023fc2c2337e" |
| summaries.positive4.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
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
| absolute_dev_screen.positive4.grammar_at_least56 | true |
| absolute_dev_screen.positive4.coherence_at_least27 | false |
| absolute_dev_screen.positive4.appropriate_at_least27 | false |
| absolute_dev_screen.positive4.EOS_at_least37 | true |
| absolute_dev_screen.positive4.repetition_at_most18 | false |
| absolute_dev_screen.positive4.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.positive4.EOS_at_least8_more | true |
| original_Web.positive4.repetition_no_worse | true |
| original_Web.positive4.no_empty_role_unicode | true |
| original_Web.positive4.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.positive4 | false |
| new_scientific_teacher_tokens | 50000000 |
| verification_teacher_tokens | 2599740 |
| GPU_seconds | 224.40080486799707 |
| verification_GPU_seconds | 22.01919901598012 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/condition-relation-comparison-20261006/annotations.json — None</summary>

[原記録](../../reports/phase6/condition-relation-comparison-20261006/annotations.json) ／ SHA256: `22a31080c24d49c804e2f00d54fd39bc7b76e6269aad06ddaa3fb3b06f969bac` ／ 38,718 bytes

| 原キー | 保存値 |
|---|---|
| control_notes.reviewer | "Codex nonblind; all80 individually read" |
| control_notes.independent_human_blind | false |
| control_notes.generation_sha256 | "f4a01f16fda39a368f5160c2ac938d168b7df4cea5f46fc5f11eb49627555913" |
| control_notes.rubric_consistency_reuse.keys | ["id", "prefix", "text", "stop_reason"] |
| control_notes.rubric_consistency_reuse.all_current_outputs_individually_read | true |
| control_notes.rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |
| relation_notes.reviewer | "Codex nonblind; all80 individually read" |
| relation_notes.independent_human_blind | false |
| relation_notes.generation_sha256 | "76297e0d8604bee0732b8c4509345f4947749d2635570c3d200520251a09877a" |
| relation_notes.rubric_consistency_reuse.keys | ["id", "prefix", "text", "stop_reason"] |
| relation_notes.rubric_consistency_reuse.all_current_outputs_individually_read | true |
| relation_notes.rubric_consistency_reuse.limitations | "Nonblind Codex judgments; no independent human evaluation. Fantasy, personification and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone does not certify completion." |

</details>
