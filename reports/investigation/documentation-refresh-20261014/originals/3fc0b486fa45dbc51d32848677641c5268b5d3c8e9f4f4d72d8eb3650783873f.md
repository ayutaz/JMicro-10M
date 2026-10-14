# 学習目的・最適化・正則化 — 11/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/jcqa.json) ／ SHA256: `923fb9cf74e67278467722e16c2e9d250df368ad21c57ca672acdebb109e7747` ／ 1,641,956 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.3449508489722967 |
| summary.primary.accuracy.ci95 | [0.31724754244861486, 0.37178284182305615] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.3449508489722967 |
| summary.per_token_secondary.accuracy.point | 0.3154602323503128 |
| summary.per_token_secondary.accuracy.ci95 | [0.2877569258266309, 0.34226988382484363] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.3154602323503128 |
| summary.per_token_secondary.macro_f1 | 0.3144965134807918 |
| summary.per_token_secondary.mcc | 0.1443980005423975 |
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
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/result.json) ／ SHA256: `b911dbfce9847aca33942e1e618659ca4018df378297837a284b3ac75b4a00f2` ／ 216,623 bytes

| 原キー | 保存値 |
|---|---|
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoint_sha256 | "cf20fbbc809ec6b63a2223879ebccfa7e6693714f4114bb5cdddddd545e04476" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 327439.9063158035 |
| body.eos_nll | 490.3658225131221 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0007222231116217 |
| body.seconds | 1.2662725870031863 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 21 |
| greedy_rates.repetition | 47 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.625 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.625 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6354166666666666] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5879940241749286 |
| diagnostics.semantics.per_token_secondary.mcc | 0.17755598081359913 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7764350453172205 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7341389728096677, 0.8217522658610272] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7764350453172205 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7190332326283988 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7190332326283988 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4182776801405975 |
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
| diagnostics.jcqa.primary.accuracy.point | 0.3449508489722967 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.31724754244861486, 0.37178284182305615] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.3449508489722967 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3154602323503128 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2877569258266309, 0.34226988382484363] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3154602323503128 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3144965134807918 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.1443980005423975 |
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
| diagnostics.semantic_both_contexts.correct | 28 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 12039749632 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/evaluation/projection/evaluation/semantics.json) ／ SHA256: `45256d34825517296083ca7751deb6bda5ba7add710c90025146a0520ca5a63f` ／ 205,214 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.625 |
| summary.primary.accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.625 |
| summary.per_token_secondary.accuracy.point | 0.5885416666666666 |
| summary.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6354166666666666] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| summary.per_token_secondary.macro_f1 | 0.5879940241749286 |
| summary.per_token_secondary.mcc | 0.17755598081359913 |
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
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/job.json) ／ SHA256: `2864d7150b06f25380191cbe94c5e4457a9eecf942e7addc48ad3f321314bf60` ／ 1,340 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_occupancy_seconds | 2382.8204671700078 |
| Base_complete | false |
| resident_memory_policy.visible_device_bytes | 25756696576 |
| resident_memory_policy.allocator_allowance_bytes | 23181026918 |
| resident_memory_policy.expected_worst_peak_bytes | 19265087488 |
| scientific_CE_teacher_tokens | 99900395 |
| local_update | 17680 |
| loss | 2.5056307196617125 |
| latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-projection-comparison-20261007/projection/checkpoint-00017698.pt" |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/result.json) ／ SHA256: `2cd635d61712e60e5b29459332562910d6314a55d61da79265fc2423efda87c4` ／ 293,096 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| results.projection.training.status | "complete" |
| results.projection.training.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.projection.training.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.projection.training.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-projection-comparison-20261007/projection/checkpoint-00017698.pt" |
| results.projection.training.checkpoint_sha256 | "cf20fbbc809ec6b63a2223879ebccfa7e6693714f4114bb5cdddddd545e04476" |
| results.projection.training.scientific_CE_teacher_tokens | 100000000 |
| results.projection.training.counters.update | 17698 |
| results.projection.training.counters.supervised_tokens | 100000000 |
| results.projection.training.counters.CE_input_tokens | 102655467 |
| results.projection.training.counters.auxiliary_input_tokens | 86885793 |
| results.projection.training.counters.auxiliary_pairs | 676384 |
| results.projection.training.counters.physical_input_tokens | 683893095 |
| results.projection.training.counters.original_body_bytes | 405882136 |
| results.projection.training.counters.token_digest | "a1ab017092f823d69e033d96868136ebeb0a55f13e2cb1cfd039e3c7d920a1c9" |
| results.projection.training.counters.source_teachers.web | 75000000 |
| results.projection.training.counters.source_teachers.textbook | 20000000 |
| results.projection.training.counters.source_teachers.story | 5000000 |
| results.projection.training.counters.source_EOS.web | 657450 |
| results.projection.training.counters.source_EOS.textbook | 148625 |
| results.projection.training.counters.source_EOS.story | 38222 |
| results.projection.training.sampler.kind | "bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1" |
| results.projection.training.sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| results.projection.training.sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| results.projection.training.sampler.binding.index_size | 12861257655 |
| results.projection.training.sampler.binding.index_mtime_ns | 1791234945567297288 |
| results.projection.training.sampler.binding.stream_size | 4000002624 |
| results.projection.training.sampler.binding.stream_mtime_ns | 1791234945514053852 |
| results.projection.training.sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| results.projection.training.sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| results.projection.training.sampler.seed | 42 |
| results.projection.training.sampler.goals.web | 75000000 |
| results.projection.training.sampler.goals.textbook | 20000000 |
| results.projection.training.sampler.goals.story | 5000000 |
| results.projection.training.sampler.consumed.web | 75000000 |
| results.projection.training.sampler.consumed.textbook | 20000000 |
| results.projection.training.sampler.consumed.story | 5000000 |
| results.projection.training.sampler.pending.web | [] |
| results.projection.training.sampler.pending.textbook | [] |
| results.projection.training.sampler.pending.story | [] |
| results.projection.training.sampler.draws | 2656558 |
| results.projection.training.sampler.documents_drawn | 844300 |
| results.projection.training.sampler.windows_emitted | 849479 |
| results.projection.training.sampler.auxiliary_reasons.original_sentence_or_LF_boundary | 676390 |
| results.projection.training.sampler.auxiliary_reasons.no_original_codec_stable_sentence_pair | 167910 |
| results.projection.training.parent_CE_teacher_tokens | 9978838479 |
| results.projection.training.Base_complete | false |
| results.projection.evaluation.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.projection.evaluation.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.projection.evaluation.checkpoint_sha256 | "cf20fbbc809ec6b63a2223879ebccfa7e6693714f4114bb5cdddddd545e04476" |
| results.projection.evaluation.body.documents | 256 |
| results.projection.evaluation.body.limit_documents | 256 |
| results.projection.evaluation.body.body_nll | 327439.9063158035 |
| results.projection.evaluation.body.eos_nll | 490.3658225131221 |
| results.projection.evaluation.body.body_bytes | 472055 |
| results.projection.evaluation.body.body_tokens | 122343 |
| results.projection.evaluation.body.bpb | 1.0007222231116217 |
| results.projection.evaluation.body.seconds | 1.2662725870031863 |
| results.projection.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| results.projection.evaluation.generation.max_new_tokens | 64 |
| results.projection.evaluation.greedy_rates.eos | 21 |
| results.projection.evaluation.greedy_rates.repetition | 47 |
| results.projection.evaluation.greedy_rates.unicode_failure | 0 |
| results.projection.evaluation.greedy_rates.role_leak | 0 |
| results.projection.evaluation.greedy_rates.empty | 0 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.point | 0.625 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.625 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6354166666666666] |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5879940241749286 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.17755598081359913 |
| results.projection.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| results.projection.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| results.projection.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| results.projection.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| results.projection.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7764350453172205 |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7341389728096677, 0.8217522658610272] |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7764350453172205 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7190332326283988 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7190332326283988 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4182776801405975 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| results.projection.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| results.projection.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| results.projection.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| results.projection.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.projection.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.3449508489722967 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.31724754244861486, 0.37178284182305615] |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.3449508489722967 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3154602323503128 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2877569258266309, 0.34226988382484363] |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3154602323503128 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3144965134807918 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.1443980005423975 |
| results.projection.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| results.projection.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| results.projection.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| results.projection.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| results.projection.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.projection.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.projection.evaluation.diagnostics.semantic_both_contexts.correct | 28 |
| results.projection.evaluation.memory.maximum_observed_allocated_bytes | 268768256 |
| results.projection.evaluation.memory.maximum_observed_reserved_bytes | 12039749632 |
| results.projection.evaluation.protected_test_used | false |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.full_sampler | true |
| common_CE_checks.contrast.update | true |
| common_CE_checks.contrast.token_digest | true |
| common_CE_checks.contrast.supervised_tokens | true |
| common_CE_checks.contrast.source_teachers | true |
| common_CE_checks.contrast.source_EOS | true |
| common_CE_checks.contrast.CE_input_tokens | true |
| common_CE_checks.contrast.original_body_bytes | true |
| common_CE_checks.contrast.full_sampler | true |
| scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 200000000 |
| reused_control_GPU_seconds | 0 |
| GPU_occupancy_seconds | 2382.8204671700078 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-projection-comparison-20261007/review.json — new80_and_reused160_projection_comparison_reviewed</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-comparison-20261007/review.json) ／ SHA256: `19f42a3fb9f678740f02f9c713d5487196ba949c21abaea96e25e668743172e0` ／ 14,055 bytes

| 原キー | 保存値 |
|---|---|
| status | "new80_and_reused160_projection_comparison_reviewed" |
| summaries.projection.BPB | 1.0007222231116217 |
| summaries.projection.rates.eos | 21 |
| summaries.projection.rates.repetition | 47 |
| summaries.projection.rates.unicode_failure | 0 |
| summaries.projection.rates.role_leak | 0 |
| summaries.projection.rates.empty | 0 |
| summaries.projection.grammar2 | 57 |
| summaries.projection.relevance2 | 25 |
| summaries.projection.coherent | 4 |
| summaries.projection.appropriate | 3 |
| summaries.projection.notes_sha256 | "f218806173197649f51546729c7cbc91a5757328d3c7ea534d4220adcf9472b1" |
| summaries.CE.BPB | 0.998487162513845 |
| summaries.CE.rates.eos | 19 |
| summaries.CE.rates.repetition | 45 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 44 |
| summaries.CE.relevance2 | 25 |
| summaries.CE.coherent | 2 |
| summaries.CE.appropriate | 2 |
| summaries.CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
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
| strong_and_matched_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.CE.checks.EOS_nonworsening | true |
| strong_and_matched_quality.CE.checks.repetition_nonworsening | false |
| strong_and_matched_quality.CE.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.CE.checks.BPB_gate | true |
| strong_and_matched_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.CE.passed | false |
| strong_and_matched_quality.contrast.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.contrast.checks.paired_CI_lower_above0 | true |
| strong_and_matched_quality.contrast.checks.EOS_nonworsening | true |
| strong_and_matched_quality.contrast.checks.repetition_nonworsening | true |
| strong_and_matched_quality.contrast.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.contrast.checks.BPB_gate | true |
| strong_and_matched_quality.contrast.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.contrast.passed | false |
| strong_and_matched_quality.strong_staged.checks.coherence_gain_at_least8 | false |
| strong_and_matched_quality.strong_staged.checks.paired_CI_lower_above0 | false |
| strong_and_matched_quality.strong_staged.checks.EOS_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.repetition_nonworsening | false |
| strong_and_matched_quality.strong_staged.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.strong_staged.checks.BPB_gate | true |
| strong_and_matched_quality.strong_staged.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | true |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.0022350605977766573 |
| paired_common_byte_BPB.CE.ci95 | [0.0019195271648210727, 0.002551265532697412] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0022384470043157 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "projection minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| paired_common_byte_BPB.contrast.point | -0.002167795177503928 |
| paired_common_byte_BPB.contrast.ci95 | [-0.002634424532899614, -0.0017505857420847695] |
| paired_common_byte_BPB.contrast.documents | 256 |
| paired_common_byte_BPB.contrast.common_bytes | 472055 |
| paired_common_byte_BPB.contrast.control_BPB | 1.0028900182891256 |
| paired_common_byte_BPB.contrast.target_BPB | 1.0007222231116217 |
| paired_common_byte_BPB.contrast.relative_ratio | 0.9978384517365104 |
| paired_common_byte_BPB.contrast.degradation_ci_lower_above0 | false |
| paired_common_byte_BPB.contrast.seed | 42 |
| paired_common_byte_BPB.contrast.repetitions | 2000 |
| paired_common_byte_BPB.contrast.direction | "projection minus completed contrast; positive means worse" |
| paired_common_byte_BPB.contrast.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.projection.exact_content_pair_clusters | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.point | 0.625 |
| exact_content_semantics.projection.original_nominal_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.original_nominal_accuracy.units | 96 |
| exact_content_semantics.projection.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.projection.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.projection.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.content_cluster_accuracy.point | 0.625 |
| exact_content_semantics.projection.content_cluster_accuracy.ci95 | [0.5729166666666666, 0.6770833333333334] |
| exact_content_semantics.projection.content_cluster_accuracy.units | 96 |
| exact_content_semantics.projection.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.projection.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.projection.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.projection.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.projection.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.both_contexts_hard_correct.point | 0.2916666666666667 |
| exact_content_semantics.projection.both_contexts_hard_correct.ci95 | [0.20833333333333334, 0.3854166666666667] |
| exact_content_semantics.projection.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.projection.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.projection.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.projection.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.projection.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.causality.seed | 42 |
| exact_content_semantics.projection.categories.causality.repetitions | 2000 |
| exact_content_semantics.projection.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.comparison.seed | 42 |
| exact_content_semantics.projection.categories.comparison.repetitions | 2000 |
| exact_content_semantics.projection.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.coreference.seed | 42 |
| exact_content_semantics.projection.categories.coreference.repetitions | 2000 |
| exact_content_semantics.projection.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.negation.seed | 42 |
| exact_content_semantics.projection.categories.negation.repetitions | 2000 |
| exact_content_semantics.projection.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.quantity.seed | 42 |
| exact_content_semantics.projection.categories.quantity.repetitions | 2000 |
| exact_content_semantics.projection.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.projection.categories.time.seed | 42 |
| exact_content_semantics.projection.categories.time.repetitions | 2000 |
| exact_content_semantics.projection.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | 0.0 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.020833333333333332, 0.020833333333333332] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
| exact_content_semantics.paired.contrast.candidate_minus_control.point | -0.010416666666666666 |
| exact_content_semantics.paired.contrast.candidate_minus_control.ci95 | [-0.041666666666666664, 0.026041666666666668] |
| exact_content_semantics.paired.contrast.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.contrast.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.contrast.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.contrast.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.contrast.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.contrast.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.contrast.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.contrast.cases | 192 |
| exact_content_semantics.paired.contrast.new_acceptance_gate | false |
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 17698 |
| accounting.head_optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 86885793 |
| accounting.auxiliary_pairs | 676384 |
| accounting.physical_input_tokens | 683893095 |
| accounting.original_body_bytes | 405882136 |
| history.committed_updates | 17698 |
| history.head_updates | 17698 |
| history.observed_completed_attempt_updates | 17698 |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.full_sampler | true |
| common_CE_checks.contrast.update | true |
| common_CE_checks.contrast.token_digest | true |
| common_CE_checks.contrast.supervised_tokens | true |
| common_CE_checks.contrast.source_teachers | true |
| common_CE_checks.contrast.source_EOS | true |
| common_CE_checks.contrast.CE_input_tokens | true |
| common_CE_checks.contrast.original_body_bytes | true |
| common_CE_checks.contrast.full_sampler | true |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 200000000 |
| reused_control_GPU_seconds | 0 |
| probe_verification_updates | 33 |
| probe_verification_CE_teachers | 145531 |
| GPU_occupancy_seconds | 2382.8204671700078 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "Single learned seed, repeated nonblind DEV, head parameters/auxiliary compute differ. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored." |

</details>

<details>
<summary>reports/phase6/natural-context-contrast-projection-evidence-20261007/manifest.json — None</summary>

[原記録](../../reports/phase6/natural-context-contrast-projection-evidence-20261007/manifest.json) ／ SHA256: `c82eb2f686431e13def12b1d1f5017b4ecd84719c231761fa4552e1fac0f8019` ／ 5,698 bytes

| 原キー | 保存値 |
|---|---|
| entries.configs/phase6/natural_context_contrast_projection_comparison.json.bytes | 7106 |
| entries.configs/phase6/natural_context_contrast_projection_probe.json.bytes | 4645 |
| entries.configs/phase6/natural_context_contrast_projection_probe_initial_mask_preflight.json.bytes | 4645 |
| entries.configs/phase6/natural_context_contrast_projection_probe_initial_preflight.json.bytes | 4645 |
| entries.reports/phase6/natural-context-contrast-projection-initial-preflight-20261007/natural_context_contrast_projection.py.bytes | 9368 |
| entries.reports/phase6/natural-context-contrast-projection-initial-preflight-20261007/probe_initial_mask.py.bytes | 17702 |
| entries.reports/phase6/natural-context-contrast-projection-initial-preflight-20261007/probe_natural_context_contrast_projection.py.bytes | 17700 |
| entries.reports/phase6/natural-context-contrast-projection-initial-preflight-20261007/test_natural_context_contrast_projection.py.sha256 | "539df8a03538a530dbaab3325977daac14c5bb053dfbfbe88a281725e8a2b77e" |
| entries.reports/phase6/natural-context-contrast-projection-initial-preflight-20261007/test_natural_context_contrast_projection.py.bytes | 5323 |
| entries.reports/phase6/natural-context-contrast-projection-probe-20261007/job.json.bytes | 704 |
| entries.reports/phase6/natural-context-contrast-projection-probe-20261007/result.json.bytes | 286023 |
| entries.reports/phase6/natural_context_contrast_projection_proposal.json.bytes | 4847 |
| entries.reports/phase6/natural_context_contrast_projection_run_tests.xml.sha256 | "6b396eee034b7aaec8d565d41eddbff12ff2bb7fee3984c55b8c08e0cf3ce271" |
| entries.reports/phase6/natural_context_contrast_projection_run_tests.xml.bytes | 576 |
| entries.reports/phase6/natural_context_contrast_projection_tests.xml.sha256 | "b8826c608660a0a9bc8dd08e3b99c4029657c4af12a84b3e89dc61c933f6cf27" |
| entries.reports/phase6/natural_context_contrast_projection_tests.xml.bytes | 1301 |
| entries.reports/phase6/natural_context_contrast_projection_tests_initial_fixture_failure.xml.sha256 | "61630b27acaa7c5260473a13828564881561887a39fee73c8f5125bcd00f9d50" |
| entries.reports/phase6/natural_context_contrast_projection_tests_initial_fixture_failure.xml.bytes | 4396 |
| entries.scripts/natural_context_contrast_corpus.py.bytes | 16493 |
| entries.scripts/natural_context_contrast_memory.py.bytes | 4117 |
| entries.scripts/natural_context_contrast_projection.py.bytes | 9393 |
| entries.scripts/natural_context_contrast_trainer.py.bytes | 12633 |
| entries.scripts/phase6_performance.py.bytes | 30565 |
| entries.scripts/probe_natural_context_contrast_projection.ps1.bytes | 2562 |
| entries.scripts/probe_natural_context_contrast_projection.py.bytes | 17680 |
| entries.scripts/run_natural_context_contrast_projection.ps1.bytes | 2618 |
| entries.scripts/run_natural_context_contrast_projection.py.bytes | 16650 |
| entries.src/jmicro/model.py.bytes | 11578 |
| entries.src/jmicro/phase5.py.bytes | 8823 |
| entries.src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| entries.src/jmicro/tokenizer.py.bytes | 6567 |
| entries.src/jmicro/training.py.bytes | 35671 |
| entries.tests/test_natural_context_contrast_corpus.py.sha256 | "25faf4393c32ca6d0901663dd67124c3c630e2b5835d20f9e94b1db49cb9fbc6" |
| entries.tests/test_natural_context_contrast_corpus.py.bytes | 6805 |
| entries.tests/test_natural_context_contrast_projection.py.sha256 | "96519a93edea2fdb49db23e4ebc3be6b593356d1fc42f5366c8c4cae65c05877" |
| entries.tests/test_natural_context_contrast_projection.py.bytes | 5626 |
| entries.tests/test_natural_context_contrast_projection_run.py.sha256 | "40d335e819ac51eb88dd5b6eebcebfb700633bb1dbdbc8b70dafb886e5f201d4" |
| entries.tests/test_natural_context_contrast_projection_run.py.bytes | 1981 |
| entries.uv.lock.bytes | 510441 |
| teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_CE_completion.json — CE_100M_evaluation_and_all80_content_complete_contrast_live</summary>

[原記録](../../reports/phase6/natural_context_contrast_CE_completion.json) ／ SHA256: `9039e82b17bedab5f1f0814248f2517b9b4c4417337cc0bf8cb394675c486269` ／ 3,539 bytes

| 原キー | 保存値 |
|---|---|
| historical_Web_BPB_guard_passed | false |
| status | "CE_100M_evaluation_and_all80_content_complete_contrast_live" |
| scientific_CE_teacher_tokens | 100000000 |
| Base_complete | false |
| content_notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| archive.bytes | 2664967.0 |
| CE_eligible_for_final_Base_validation | false |
| historical_Web_BPB_limit | 0.9812859519097707 |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| Base_adopted | false |
| summary.BPB | 0.998487162513845 |
| summary.rates.eos | 19 |
| summary.rates.repetition | 45 |
| summary.rates.unicode_failure | 0 |
| summary.rates.role_leak | 0 |
| summary.rates.empty | 0 |
| summary.grammar2 | 44 |
| summary.relevance2 | 25 |
| summary.coherent | 2 |
| summary.appropriate | 2 |
| summary.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summary.scope | "one_arm_content_only_comparison_and_final_validation_pending" |
| summary.Base_complete | false |
| summary.scientific_CE_teacher_tokens | 100000000 |
| live_contrast_snapshot.CE_teacher_tokens | 12868737 |
| live_contrast_snapshot.loss | 2.6185899496078493 |
| live_contrast_snapshot.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/contrast/checkpoint-00002250.pt" |
| source_EOS.web | 657450 |
| source_EOS.textbook | 148625 |
| source_EOS.story | 38222 |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| protected_test_used | false |
| CE_updates | 17698 |
| whole_scientific_comparison_complete | false |
| source_teachers.web | 75000000 |
| source_teachers.textbook | 20000000 |
| source_teachers.story | 5000000 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_CE_content_review.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_CE_content_review.json) ／ SHA256: `4b354506ff0c9f2968fdd4fdb29bb0ee1a29049f7418ed71b61906efb8e78d21` ／ 753 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 0.998487162513845 |
| rates.eos | 19 |
| rates.repetition | 45 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 44 |
| relevance2 | 25 |
| coherent | 2 |
| appropriate | 2 |
| notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| scope | "one_arm_content_only_comparison_and_final_validation_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_CE_notes.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_CE_notes.json) ／ SHA256: `5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369` ／ 21,013 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/natural_context_contrast_CE_semantic_clusters.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_CE_semantic_clusters.json) ／ SHA256: `f37f81388ed8047c61f688897f5a9a36eeb1cd7d138c7dd4dc73a4e079d76543` ／ 5,017 bytes

| 原キー | 保存値 |
|---|---|
| reference.checkpoint_sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| reference.DEV_selection.dev_bytes_sha256 | "bc676ad2b955a238b60cc3a2cfccbe4b5e7b793640212980f72716ed3a6a14a2" |
| summary.exact_content_pair_clusters | 96 |
| summary.original_nominal_accuracy.point | 0.625 |
| summary.original_nominal_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| summary.original_nominal_accuracy.units | 96 |
| summary.original_nominal_accuracy.examples | 192 |
| summary.original_nominal_accuracy.unit | "family/prompt" |
| summary.original_nominal_accuracy.seed | 42 |
| summary.original_nominal_accuracy.repetitions | 2000 |
| summary.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.content_cluster_accuracy.point | 0.625 |
| summary.content_cluster_accuracy.ci95 | [0.578125, 0.6770833333333334] |
| summary.content_cluster_accuracy.units | 96 |
| summary.content_cluster_accuracy.examples | 192 |
| summary.content_cluster_accuracy.unit | "family/prompt" |
| summary.content_cluster_accuracy.seed | 42 |
| summary.content_cluster_accuracy.repetitions | 2000 |
| summary.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.both_contexts_hard_correct.point | 0.2708333333333333 |
| summary.both_contexts_hard_correct.ci95 | [0.1875, 0.3645833333333333] |
| summary.both_contexts_hard_correct.units | 96 |
| summary.both_contexts_hard_correct.examples | 96 |
| summary.both_contexts_hard_correct.unit | "family/prompt" |
| summary.both_contexts_hard_correct.seed | 42 |
| summary.both_contexts_hard_correct.repetitions | 2000 |
| summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.causality.seed | 42 |
| summary.categories.causality.repetitions | 2000 |
| summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.comparison.seed | 42 |
| summary.categories.comparison.repetitions | 2000 |
| summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.coreference.seed | 42 |
| summary.categories.coreference.repetitions | 2000 |
| summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.negation.seed | 42 |
| summary.categories.negation.repetitions | 2000 |
| summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.quantity.seed | 42 |
| summary.categories.quantity.repetitions | 2000 |
| summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.time.seed | 42 |
| summary.categories.time.repetitions | 2000 |
| summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| scientific_config_sha256 | "70b87bf762f3225fd83f40d3bde301c13e5a4b4243372e541af1a1e38e88bc29" |
| new_GPU_seconds | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| limitations | "All original case weights retained; exact aliases are clustered, not counted as independent cases. Other template correlations remain. CIs describe this constructed DEV packet, not natural Japanese population accuracy. No protected TEST source file is opened by this supplement." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_comparison_completion.json — comparison_complete_fixed_recipes_rejected</summary>

[原記録](../../reports/phase6/natural_context_contrast_comparison_completion.json) ／ SHA256: `a07acf8bb9ebfbe120af9ea903aae65477b535c5992bad4176d246a71c2c608f` ／ 6,633 bytes

| 原キー | 保存値 |
|---|---|
| scientific_CE_teacher_tokens | 200000000 |
| Base_complete | false |
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
| summaries.CE.BPB | 0.998487162513845 |
| summaries.CE.rates.eos | 19 |
| summaries.CE.rates.repetition | 45 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 44 |
| summaries.CE.relevance2 | 25 |
| summaries.CE.coherent | 2 |
| summaries.CE.appropriate | 2 |
| summaries.CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| ui_identity.status | "running" |
| ui_identity.additional_training_tokens | 0 |
| ui_identity.model.training_tokens | 10000007168 |
| ui_identity.model.update | 305176 |
| ui_identity.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_identity.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_identity.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| Base_adopted | false |
| GPU_budget_seconds | 5229 |
| ui_model.training_tokens | 10000007168 |
| ui_model.update | 305176 |
| ui_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| status | "comparison_complete_fixed_recipes_rejected" |
| review.reports/phase6/natural_context_contrast_paired_semantic_clusters.json | "a99480a471ffb781bafd2242ec3c06871abc37669ee28e8142c5d392dfbb4f2a" |
| CE_teacher_tokens_per_arm | 100000000 |
| protected_test_used | false |
| GPU_occupancy_seconds | 3762.997766413988 |
| paired_semantic_difference.point | 0.010416666666666666 |
| paired_semantic_difference.ci95 | [-0.020833333333333332, 0.041666666666666664] |
| paired_semantic_difference.units | 96 |
| paired_semantic_difference.examples | 192 |
| paired_semantic_difference.unit | "family/prompt" |
| paired_semantic_difference.seed | 42 |
| paired_semantic_difference.repetitions | 2000 |
| paired_semantic_difference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| common_CE_checks.token_digest | true |
| common_CE_checks.supervised_tokens | true |
| common_CE_checks.source_teachers | true |
| common_CE_checks.source_EOS | true |
| common_CE_checks.CE_input_tokens | true |
| common_CE_checks.original_body_bytes | true |
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | true |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
| archive.bytes | 3303099 |
| eligible_for_final_Base_validation.CE | false |
| eligible_for_final_Base_validation.contrast | false |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_comparison_review.json — all160_context_comparison_reviewed</summary>

[原記録](../../reports/phase6/natural_context_contrast_comparison_review.json) ／ SHA256: `d034f4f5c20d67c6d94e5052f569670fce2fd5e166fd0d625b16c1def003c674` ／ 7,099 bytes

| 原キー | 保存値 |
|---|---|
| status | "all160_context_comparison_reviewed" |
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
| summaries.CE.BPB | 0.998487162513845 |
| summaries.CE.rates.eos | 19 |
| summaries.CE.rates.repetition | 45 |
| summaries.CE.rates.unicode_failure | 0 |
| summaries.CE.rates.role_leak | 0 |
| summaries.CE.rates.empty | 0 |
| summaries.CE.grammar2 | 44 |
| summaries.CE.relevance2 | 25 |
| summaries.CE.coherent | 2 |
| summaries.CE.appropriate | 2 |
| summaries.CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| summaries.contrast.BPB | 1.0028900182891256 |
| summaries.contrast.rates.eos | 6 |
| summaries.contrast.rates.repetition | 53 |
| summaries.contrast.rates.unicode_failure | 0 |
| summaries.contrast.rates.role_leak | 0 |
| summaries.contrast.rates.empty | 0 |
| summaries.contrast.grammar2 | 48 |
| summaries.contrast.relevance2 | 26 |
| summaries.contrast.coherent | 0 |
| summaries.contrast.appropriate | 3 |
| summaries.contrast.notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| strong_relative_quality.CE.checks.coherence_gain_at_least8 | false |
| strong_relative_quality.CE.checks.paired_CI_lower_above0 | false |
| strong_relative_quality.CE.checks.EOS_nonworsening | false |
| strong_relative_quality.CE.checks.repetition_nonworsening | false |
| strong_relative_quality.CE.checks.no_empty_role_unicode | true |
| strong_relative_quality.CE.checks.BPB_gate | true |
| strong_relative_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_relative_quality.CE.passed | false |
| strong_relative_quality.contrast.checks.coherence_gain_at_least8 | false |
| strong_relative_quality.contrast.checks.paired_CI_lower_above0 | false |
| strong_relative_quality.contrast.checks.EOS_nonworsening | false |
| strong_relative_quality.contrast.checks.repetition_nonworsening | false |
| strong_relative_quality.contrast.checks.no_empty_role_unicode | true |
| strong_relative_quality.contrast.checks.BPB_gate | true |
| strong_relative_quality.contrast.checks.appropriate_completion_not_punctuation | true |
| strong_relative_quality.contrast.passed | false |
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | true |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
| absolute_dev_screen.CE.grammar_at_least56 | false |
| absolute_dev_screen.CE.coherence_at_least27 | false |
| absolute_dev_screen.CE.appropriate_at_least27 | false |
| absolute_dev_screen.CE.EOS_at_least37 | false |
| absolute_dev_screen.CE.repetition_at_most18 | false |
| absolute_dev_screen.CE.no_empty_role_unicode | true |
| absolute_dev_screen.contrast.grammar_at_least56 | false |
| absolute_dev_screen.contrast.coherence_at_least27 | false |
| absolute_dev_screen.contrast.appropriate_at_least27 | false |
| absolute_dev_screen.contrast.EOS_at_least37 | false |
| absolute_dev_screen.contrast.repetition_at_most18 | false |
| absolute_dev_screen.contrast.no_empty_role_unicode | true |
| historical_Web.CE.EOS_at_least8_more | true |
| historical_Web.CE.repetition_no_worse | true |
| historical_Web.CE.no_empty_role_unicode | true |
| historical_Web.CE.BPB_degradation_at_most1percent | false |
| historical_Web.contrast.EOS_at_least8_more | false |
| historical_Web.contrast.repetition_no_worse | true |
| historical_Web.contrast.no_empty_role_unicode | true |
| historical_Web.contrast.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.CE | false |
| eligible_for_final_Base_validation.contrast | false |
| accounting.CE.completed_updates | 17698 |
| accounting.CE.CE_teacher_tokens | 100000000 |
| accounting.CE.auxiliary_input_tokens | 0 |
| accounting.CE.auxiliary_pairs | 0 |
| accounting.CE.CE_input_tokens | 102655467 |
| accounting.CE.physical_input_tokens | 370838917 |
| accounting.CE.source_teachers.web | 75000000 |
| accounting.CE.source_teachers.textbook | 20000000 |
| accounting.CE.source_teachers.story | 5000000 |
| accounting.CE.source_EOS.web | 657450 |
| accounting.CE.source_EOS.textbook | 148625 |
| accounting.CE.source_EOS.story | 38222 |
| accounting.CE.original_body_bytes | 405882136 |
| accounting.contrast.completed_updates | 17698 |
| accounting.contrast.CE_teacher_tokens | 100000000 |
| accounting.contrast.auxiliary_input_tokens | 86885793 |
| accounting.contrast.auxiliary_pairs | 676384 |
| accounting.contrast.CE_input_tokens | 102655467 |
| accounting.contrast.physical_input_tokens | 683893095 |
| accounting.contrast.source_teachers.web | 75000000 |
| accounting.contrast.source_teachers.textbook | 20000000 |
| accounting.contrast.source_teachers.story | 5000000 |
| accounting.contrast.source_EOS.web | 657450 |
| accounting.contrast.source_EOS.textbook | 148625 |
| accounting.contrast.source_EOS.story | 38222 |
| accounting.contrast.original_body_bytes | 405882136 |
| common_CE_checks.token_digest | true |
| common_CE_checks.supervised_tokens | true |
| common_CE_checks.source_teachers | true |
| common_CE_checks.source_EOS | true |
| common_CE_checks.CE_input_tokens | true |
| common_CE_checks.original_body_bytes | true |
| scientific_CE_teacher_tokens | 200000000 |
| probe_updates_separate | 112 |
| GPU_occupancy_seconds | 3762.997766413988 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "One learned seed and repeated nonblind DEV; source draws are exposure, not unique supply. The evaluator marks no protected TEST cases evaluated; its task loader may decode the suite JSON. Diagnostic CUDA resume updates and auxiliary input are separate from scientific CE teachers." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_contrast_content_review.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_contrast_content_review.json) ／ SHA256: `462948e714351a500915180a817e8a35b4237c5d031ff4d08665623f78165a39` ／ 772 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.0028900182891256 |
| rates.eos | 6 |
| rates.repetition | 53 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 48 |
| relevance2 | 26 |
| coherent | 0 |
| appropriate | 3 |
| notes_sha256 | "fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47" |
| scope | "one_arm_content_only_comparison_and_final_validation_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_contrast_notes.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_contrast_notes.json) ／ SHA256: `fef5cfb13fa427cd31feac7218a65f0ceaa7431abef4b297d877e8454c87fe47` ／ 20,780 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/natural_context_contrast_contrast_semantic_clusters.json — None</summary>

[原記録](../../reports/phase6/natural_context_contrast_contrast_semantic_clusters.json) ／ SHA256: `24377c4d678f3ba639d9ed67583966a2b10cb45327b7ed7060d0bed9d77c7c10` ／ 5,040 bytes

| 原キー | 保存値 |
|---|---|
| reference.checkpoint_sha256 | "b3c88153624b9d9c1e9114314c7c19f7feeaf5e4c51650b3e78f0dd40c407707" |
| reference.DEV_selection.dev_bytes_sha256 | "bc676ad2b955a238b60cc3a2cfccbe4b5e7b793640212980f72716ed3a6a14a2" |
| summary.exact_content_pair_clusters | 96 |
| summary.original_nominal_accuracy.point | 0.6354166666666666 |
| summary.original_nominal_accuracy.ci95 | [0.5833333333333334, 0.6875] |
| summary.original_nominal_accuracy.units | 96 |
| summary.original_nominal_accuracy.examples | 192 |
| summary.original_nominal_accuracy.unit | "family/prompt" |
| summary.original_nominal_accuracy.seed | 42 |
| summary.original_nominal_accuracy.repetitions | 2000 |
| summary.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.content_cluster_accuracy.point | 0.6354166666666666 |
| summary.content_cluster_accuracy.ci95 | [0.5833333333333334, 0.6875] |
| summary.content_cluster_accuracy.units | 96 |
| summary.content_cluster_accuracy.examples | 192 |
| summary.content_cluster_accuracy.unit | "family/prompt" |
| summary.content_cluster_accuracy.seed | 42 |
| summary.content_cluster_accuracy.repetitions | 2000 |
| summary.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.both_contexts_hard_correct.point | 0.3125 |
| summary.both_contexts_hard_correct.ci95 | [0.21875, 0.40625] |
| summary.both_contexts_hard_correct.units | 96 |
| summary.both_contexts_hard_correct.examples | 96 |
| summary.both_contexts_hard_correct.unit | "family/prompt" |
| summary.both_contexts_hard_correct.seed | 42 |
| summary.both_contexts_hard_correct.repetitions | 2000 |
| summary.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.causality.seed | 42 |
| summary.categories.causality.repetitions | 2000 |
| summary.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.comparison.seed | 42 |
| summary.categories.comparison.repetitions | 2000 |
| summary.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.coreference.seed | 42 |
| summary.categories.coreference.repetitions | 2000 |
| summary.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.negation.seed | 42 |
| summary.categories.negation.repetitions | 2000 |
| summary.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.quantity.seed | 42 |
| summary.categories.quantity.repetitions | 2000 |
| summary.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.categories.time.seed | 42 |
| summary.categories.time.repetitions | 2000 |
| summary.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| scientific_config_sha256 | "70b87bf762f3225fd83f40d3bde301c13e5a4b4243372e541af1a1e38e88bc29" |
| new_GPU_seconds | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| limitations | "All original case weights retained; exact aliases are clustered, not counted as independent cases. Other template correlations remain. CIs describe this constructed DEV packet, not natural Japanese population accuracy. No protected TEST source file is opened by this supplement." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_dev_transfer_completion.json — readonly_DEV64_representation_transfer_complete</summary>

[原記録](../../reports/phase6/natural_context_contrast_dev_transfer_completion.json) ／ SHA256: `a229fc52e2064f56d067148e6fb7deaf608e15e0dd2a4691142756612cdeb7e3` ／ 17,440 bytes

| 原キー | 保存値 |
|---|---|
| Base_adopted | false |
| Base_complete | false |
| ui_model.training_tokens | 10000007168 |
| ui_model.update | 305176 |
| ui_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| protected_test_used | false |
| GPU_seconds | 1.501790620997781 |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| CPU_preparation_seconds | 0.30937964702025056 |
| CPU_tests | 4 |
| status | "readonly_DEV64_representation_transfer_complete" |
| archive.bytes | 1408455.0 |
| GPU_limit_seconds | 60 |
| paired.CE_minus_original.point | 0.0078125 |
| paired.CE_minus_original.CI95 | [-0.015625, 0.03125] |
| paired.CE_minus_original.document_units | 64 |
| paired.CE_minus_original.directions_correlated | true |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | -0.5 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired.contrast_minus_CE.point | 0.109375 |
| paired.contrast_minus_CE.CI95 | [0.0390625, 0.1953125] |
| paired.contrast_minus_CE.document_units | 64 |
| paired.contrast_minus_CE.directions_correlated | true |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 1.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired.contrast_minus_original.point | 0.1171875 |
| paired.contrast_minus_original.CI95 | [0.046875, 0.1953125] |
| paired.contrast_minus_original.document_units | 64 |
| paired.contrast_minus_original.directions_correlated | true |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| ui_identity.status | "running" |
| ui_identity.additional_training_tokens | 0 |
| ui_identity.model.training_tokens | 10000007168 |
| ui_identity.model.update | 305176 |
| ui_identity.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_identity.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_identity.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_dev_transfer_proposal.json — readonly_DEV_transfer_diagnostic_proposed_commands_not_implemented</summary>

[原記録](../../reports/phase6/natural_context_contrast_dev_transfer_proposal.json) ／ SHA256: `092606705f03759fa385afe4bd5754eb42247922a145e6e86f7546cbfd115f85` ／ 2,785 bytes

| 原キー | 保存値 |
|---|---|
| new_scientific_teacher_tokens | 0 |
| Base_adopted | false |
| additional_raw_data_download_bytes | 0 |
| status | "readonly_DEV_transfer_diagnostic_proposed_commands_not_implemented" |
| checkpoint_source | "Original10B parent410f975d… and exact CE f691a758… / contrast b3c88153… terminal checkpoints from completed frozen comparison; no outcome-based checkpoint selection." |
| GPU_diagnostic_budget_seconds | 60 |
| completion | "All three fixed models scored on exact same64 heldout pairs; finite saved outputs, accumulated GPU seconds and actual terminal process. Interpret discrimination transfer separately from generation coherence and next-token likelihood; preserve rejected Base decisions. This one-shot diagnostic ends after its bounded result; no coefficient/LR/source/epoch rescue or repeat to obtain favorable result." |
| protected_test_used | false |
| limitations | "Retrospective diagnostic choice after a failed experiment; no preregistered adoption gate. Structured document retrieval cannot establish coherent Japanese generation or Base completion." |
| reason | "TRAIN endpoint contrast loss1.6211 to0.3759 and positive-minus-distractor cosine0.3060 to0.6587 accompany no meaningful natural-generation gain. Sampled TRAIN endpoints differ; heldout representation transfer is unmeasured, and cached decode/shift evidence already exists." |
| Base_complete | false |
| CPU_preparation_budget_seconds | 30 |
| optimizer_updates | 0 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_dev_transfer_review.json — all_three_fixed_DEV64_retrieval_models_reviewed</summary>

[原記録](../../reports/phase6/natural_context_contrast_dev_transfer_review.json) ／ SHA256: `32c309825a5944068a4937777de182f4c03f49b23a93406751e95295270ac2b0` ／ 16,215 bytes

| 原キー | 保存値 |
|---|---|
| status | "all_three_fixed_DEV64_retrieval_models_reviewed" |
| GPU_occupancy_seconds | 1.501790620997781 |
| paired_document_differences.CE_minus_original.point | 0.0078125 |
| paired_document_differences.CE_minus_original.CI95 | [-0.015625, 0.03125] |
| paired_document_differences.CE_minus_original.document_units | 64 |
| paired_document_differences.CE_minus_original.directions_correlated | true |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | -0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.CE_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired_document_differences.contrast_minus_CE.point | 0.109375 |
| paired_document_differences.contrast_minus_CE.CI95 | [0.0390625, 0.1953125] |
| paired_document_differences.contrast_minus_CE.document_units | 64 |
| paired_document_differences.contrast_minus_CE.directions_correlated | true |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 1.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.contrast_minus_CE.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| paired_document_differences.contrast_minus_original.point | 0.1171875 |
| paired_document_differences.contrast_minus_original.CI95 | [0.046875, 0.1953125] |
| paired_document_differences.contrast_minus_original.document_units | 64 |
| paired_document_differences.contrast_minus_original.directions_correlated | true |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 0.5 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 0.0 |
| paired_document_differences.contrast_minus_original.case_difference.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 0.0 |
| conclusion | "Contrast transfers some observed document-pair discrimination to this fixed DEV packet. Original failed generation and retention outcomes remain unchanged; retrieval does not certify appropriate next-token continuation, semantic reasoning or Base quality." |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| one_shot_diagnostic_closed | true |
| limitations | "Retrospective diagnostic, fixed64 documents and unknown near-family correlations. Bootstrap resamples document pairs, not128 independent directions, and is not an independent seed or natural-Japanese population guarantee. Variance is retained from actual scoring; matrices do not reconstruct feature coordinates." |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_likelihood_transfer_completion.json — all9_readonly_suffix_likelihood_sections_complete</summary>

[原記録](../../reports/phase6/natural_context_contrast_likelihood_transfer_completion.json) ／ SHA256: `2f9d08f99d4aebe8545abe301d5c6e0c91847dfcb2b04b4b97d1d8722ae1d8a1` ／ 26,245 bytes

| 原キー | 保存値 |
|---|---|
| Base_complete | false |
| Base_adopted | false |
| paired_contrast_minus_CE.matched.point_BPB | 0.0054906949912326315 |
| paired_contrast_minus_CE.matched.CI95_BPB | [0.003822604251162451, 0.007581448655016614] |
| paired_contrast_minus_CE.matched.unit | "64 paired documents, byte-weighted ratio" |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | -1.04046630859375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 4.900390625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 9.03778076171875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 8.80419921875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 1.146240234375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 4.08984375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 2.904266357421875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 2.2198486328125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 0.1170654296875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 9.00872802734375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 2.06024169921875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 22.08349609375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 5.6912841796875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | -0.93438720703125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 5.686767578125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 6.74322509765625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | -0.471405029296875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 3.456512451171875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 4.037109375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 3.18341064453125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 0.01666259765625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.925384521484375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 1.94586181640625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | -0.087615966796875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | -0.920806884765625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 1.9630126953125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 1.39141845703125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 1.255767822265625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.963836669921875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 1.98907470703125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 6.60919189453125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 11.12677001953125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 3.11322021484375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 1.20123291015625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 3.6268310546875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 3.5775146484375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 2.30615234375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 4.82427978515625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 0.5948486328125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | -0.6519775390625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 1.1778564453125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 9.194580078125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | -4.06475830078125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 3.982208251953125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 1.9127197265625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | -1.07501220703125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | -3.8057861328125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 10.87884521484375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 1.6943359375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 9.9490966796875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 33.552978515625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 2.6510009765625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | -0.8653564453125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 6.2178955078125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 7.630950927734375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 5.8505859375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 3.55615234375 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 4.25390625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | -3.32098388671875 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 2.48876953125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 5.5338134765625 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 4.7022705078125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 1.96533203125 |
| paired_contrast_minus_CE.matched.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | -0.842254638671875 |
| paired_contrast_minus_CE.cyclic.point_BPB | 0.006096397486108837 |
| paired_contrast_minus_CE.cyclic.CI95_BPB | [0.004189200838098615, 0.008573287511042582] |
| paired_contrast_minus_CE.cyclic.unit | "64 paired documents, byte-weighted ratio" |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 2.407470703125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 2.85382080078125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 11.1805419921875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 6.7191162109375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 1.3533935546875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 2.754150390625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 2.647003173828125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | 0.31939697265625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 1.36114501953125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 5.99853515625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 2.933349609375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 26.0830078125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 4.97674560546875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 0.22271728515625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | -0.3668212890625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 14.0235595703125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 3.1346435546875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 2.95770263671875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 3.958740234375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 2.7908935546875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | -1.343017578125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 1.271087646484375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | -0.670654296875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 3.36419677734375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | -2.61468505859375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 2.723388671875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 1.21307373046875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 6.33447265625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 1.011077880859375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | -0.0804443359375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 4.19073486328125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 8.599609375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 1.8538818359375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 4.8050537109375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 7.2735595703125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 4.02325439453125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 4.84576416015625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 3.87200927734375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 3.123565673828125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 1.2880859375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 2.264404296875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 4.61376953125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 1.911865234375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 4.16717529296875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 2.0615234375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 1.94537353515625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | -1.5970458984375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 8.5374755859375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 9.033935546875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 4.42242431640625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 42.640869140625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 3.76666259765625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | -0.05889892578125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 4.8497314453125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | -3.466705322265625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 8.1688232421875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 0.9228515625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 5.60595703125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 0.2503662109375 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 5.5994873046875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 0.89434814453125 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 8.10748291015625 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 3.9910888671875 |
| paired_contrast_minus_CE.cyclic.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | -3.647613525390625 |
| paired_contrast_minus_CE.BOS_only.point_BPB | 0.006510482251951778 |
| paired_contrast_minus_CE.BOS_only.CI95_BPB | [0.004820018635551494, 0.008639528432890706] |
| paired_contrast_minus_CE.BOS_only.unit | "64 paired documents, byte-weighted ratio" |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | -0.976226806640625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | 5.37335205078125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 9.23333740234375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | 2.4935302734375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 3.9581298828125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | 0.55712890625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | 4.900787353515625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | -1.3712158203125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 2.562286376953125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | 9.2520751953125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 3.5682373046875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 21.9788818359375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | 3.64044189453125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 4.59051513671875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | 3.21112060546875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 5.816162109375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 3.02685546875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | 4.239227294921875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | 8.9180908203125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | 3.03314208984375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | 0.23162841796875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 4.958770751953125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | 2.8966064453125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | -0.689300537109375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | -1.64398193359375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | -0.45660400390625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | 5.50360107421875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 2.162353515625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 25.2694091796875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | 1.00537109375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | 2.86895751953125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | 4.90313720703125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | 3.798095703125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 6.063720703125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 6.70745849609375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 4.61041259765625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | -3.21429443359375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | 6.04754638671875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 1.309356689453125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 0.86431884765625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 1.376678466796875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | 7.7789306640625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 1.94598388671875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 4.98876953125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 3.816162109375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 0.9111328125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | -0.93035888671875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | 5.519775390625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 3.0831298828125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | 9.06048583984375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 26.922607421875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | -2.76361083984375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 2.52734375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | 7.0614013671875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | 2.6932373046875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 5.9703369140625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | 6.630859375 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 5.83935546875 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 2.478515625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 2.158447265625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | 1.034423828125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 8.28277587890625 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 2.43017578125 |
| paired_contrast_minus_CE.BOS_only.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | 6.588531494140625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.point_BPB | 0.0006057024948762055 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.CI95_BPB | [-0.0005691477410176404, 0.0017613417870157044] |
| paired_contrast_minus_CE.cyclic_context_benefit_change.unit | "64 paired documents, byte-weighted ratio" |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30006 | 3.44793701171875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30072 | -2.04656982421875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30077 | 2.14276123046875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30093 | -2.0850830078125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30125 | 0.2071533203125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30129 | -1.335693359375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30136 | -0.25726318359375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30147 | -1.90045166015625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30167 | 1.24407958984375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30174 | -3.01019287109375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30207 | 0.87310791015625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30219 | 3.99951171875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30220 | -0.71453857421875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30233 | 1.1571044921875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30256 | -6.0535888671875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30268 | 7.28033447265625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30271 | 3.606048583984375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30350 | -0.498809814453125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30352 | -0.078369140625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30361 | -0.39251708984375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30384 | -1.35968017578125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30387 | 0.345703125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30411 | -2.61651611328125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30436 | 3.451812744140625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30441 | -1.693878173828125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30444 | 0.7603759765625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30461 | -0.1783447265625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30464 | 5.078704833984375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30473 | 0.0472412109375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30571 | -2.06951904296875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30590 | -2.41845703125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30613 | -2.52716064453125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30617 | -1.25933837890625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30632 | 3.60382080078125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30633 | 3.646728515625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30657 | 0.44573974609375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30663 | 2.53961181640625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30760 | -0.9522705078125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30774 | 2.528717041015625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30809 | 1.9400634765625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30824 | 1.0865478515625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30827 | -4.580810546875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30832 | 5.97662353515625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30850 | 0.184967041015625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30910 | 0.1488037109375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30913 | 3.0203857421875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30926 | 2.208740234375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30936 | -2.34136962890625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30966 | 7.339599609375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30982 | -5.52667236328125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:30987 | 9.087890625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31014 | 1.11566162109375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31046 | 0.80645751953125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31068 | -1.3681640625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31100 | -11.09765625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31109 | 2.3182373046875 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31161 | -2.63330078125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31181 | 1.35205078125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31240 | 3.57135009765625 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31260 | 3.1107177734375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31318 | -4.63946533203125 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31325 | 3.40521240234375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31328 | 2.0257568359375 |
| paired_contrast_minus_CE.cyclic_context_benefit_change.raw_delta_nll.fineweb2_edu_ja:train-00000-of-00283.parquet:31360 | -2.80535888671875 |
| optimizer_updates | 0 |
| archive.bytes | 1277484.0 |
| ui_identity.status | "running" |
| ui_identity.additional_training_tokens | 0 |
| ui_identity.model.training_tokens | 10000007168 |
| ui_identity.model.update | 305176 |
| ui_identity.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_identity.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_identity.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| GPU_limit_seconds | 60 |
| ui_model.training_tokens | 10000007168 |
| ui_model.update | 305176 |
| ui_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| summaries.original.matched.BPB | 0.9813161982241746 |
| summaries.original.matched.body_nll | 43199.963470458984 |
| summaries.original.matched.body_bytes | 63511 |
| summaries.original.matched.body_tokens | 16509 |
| summaries.original.cyclic.BPB | 1.1185374089198517 |
| summaries.original.cyclic.body_nll | 49240.780181884766 |
| summaries.original.cyclic.body_bytes | 63511 |
| summaries.original.cyclic.body_tokens | 16509 |
| summaries.original.BOS_only.BPB | 1.0669981454132147 |
| summaries.original.BOS_only.body_nll | 46971.894470214844 |
| summaries.original.BOS_only.body_bytes | 63511 |
| summaries.original.BOS_only.body_tokens | 16509 |
| summaries.CE.matched.BPB | 0.9950548595583135 |
| summaries.CE.matched.body_nll | 43804.77328491211 |
| summaries.CE.matched.body_bytes | 63511 |
| summaries.CE.matched.body_tokens | 16509 |
| summaries.CE.cyclic.BPB | 1.1326447534847175 |
| summaries.CE.cyclic.body_nll | 49861.82034301758 |
| summaries.CE.cyclic.body_bytes | 63511 |
| summaries.CE.cyclic.body_tokens | 16509 |
| summaries.CE.BOS_only.BPB | 1.085956374305155 |
| summaries.CE.BOS_only.body_nll | 47806.48254394531 |
| summaries.CE.BOS_only.body_bytes | 63511 |
| summaries.CE.BOS_only.body_tokens | 16509 |
| summaries.contrast.matched.BPB | 1.000545554549546 |
| summaries.contrast.matched.body_nll | 44046.487243652344 |
| summaries.contrast.matched.body_bytes | 63511 |
| summaries.contrast.matched.body_tokens | 16509 |
| summaries.contrast.cyclic.BPB | 1.1387411509708263 |
| summaries.contrast.cyclic.body_nll | 50130.198822021484 |
| summaries.contrast.cyclic.body_bytes | 63511 |
| summaries.contrast.cyclic.body_tokens | 16509 |
| summaries.contrast.BOS_only.BPB | 1.0924668565571067 |
| summaries.contrast.BOS_only.body_nll | 48093.09005737305 |
| summaries.contrast.BOS_only.body_bytes | 63511 |
| summaries.contrast.BOS_only.body_tokens | 16509 |
| status | "all9_readonly_suffix_likelihood_sections_complete" |
| common_suffix_bytes_per_section | 63511 |
| GPU_seconds | 2.1220142460078932 |
| new_teacher_tokens | 0 |
| CPU_preparation_seconds | 0.02817891602171585 |
| protected_test_used | false |
| CPU_tests | 3 |
| common_suffix_tokens_per_section | 16509 |
| CPU_test_seconds | 0.81 |

</details>

<details>
<summary>reports/phase6/natural_context_contrast_likelihood_transfer_proposal.json — conditional_likelihood_transfer_diagnostic_defined_not_implemented</summary>

[原記録](../../reports/phase6/natural_context_contrast_likelihood_transfer_proposal.json) ／ SHA256: `85d13902a1d4f1af1d6c08b6b38449c356e6bae48fc6eafb93ccdfdd998fa325` ／ 2,845 bytes

| 原キー | 保存値 |
|---|---|
| completion | "All3 models x3 context views x64 complete paired records; finite NLL/common suffix-byte BPB, matched-minus-other-prefix and matched-minus-BOS differences, all target counts, config/checkpoint/input source hashes, actual terminal identity and cumulative GPU budget. Preserve all prior rejected Base decisions. Close the one-shot diagnostic after result, with no automatic training or favorable repeated attempts." |
| CPU_preparation_seconds_limit | 30 |
| Base_adopted | false |
| GPU_seconds_limit | 60 |
| optimizer_updates | 0 |
| Base_complete | false |
| status | "conditional_likelihood_transfer_diagnostic_defined_not_implemented" |
| limitations | "Retrospective original DEV article association and lexical topic overlap are not factual reasoning or free-generation coherence. Structured retrieval success and teacher-forced improvement cannot replace unchanged Base gates or independent learned seed/full dev/protected test/adoption." |
| reason | "Frozen DEV64 representation retrieval improved after contrast but all80 free generation worsened. Distinguish whether source association gains reach the next-token output distribution before selecting any new learning objective." |
| protected_test_used | false |
| new_teacher_tokens | 0 |

</details>
