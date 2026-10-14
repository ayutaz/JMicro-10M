# 学習目的・最適化・正則化 — 4/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/base-label-smoothing-comparison-20261007/evaluation/smoothing/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/evaluation/smoothing/evaluation/result.json) ／ SHA256: `96d71baa9513c5741219529d714c3586d97e9296ab8f55b1d3321fc63e97e9b0` ／ 219,518 bytes

| 原キー | 保存値 |
|---|---|
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoint_sha256 | "5d6ae5726c63b69edb7d7f7b74c232fe1b3d2093f5297787df1ce6ed42a7869b" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 342160.5264415741 |
| body.eos_nll | 544.3450270481408 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0457113994878056 |
| body.seconds | 1.3373736609937623 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 27 |
| greedy_rates.repetition | 42 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5989583333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5989583333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6302083333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5826086956521739 |
| diagnostics.semantics.per_token_secondary.mcc | 0.16724840200141816 |
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
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7492447129909365, 0.8338368580060423] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| diagnostics.jcqa.primary.accuracy.point | 0.32082216264521896 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.2931188561215371, 0.34673815907059874] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.32082216264521896 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.306076854334227 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2801608579088472, 0.3320040214477211] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.30563002680965146 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3042124399702949 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.13181731002303418 |
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
| diagnostics.semantic_both_contexts.correct | 22 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 11957960704 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-20261007/evaluation/smoothing/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/evaluation/smoothing/evaluation/semantics.json) ／ SHA256: `345457eef5853db6ee90afdb7c746fd25771f269c99f37fb770015dbbf5c4985` ／ 205,425 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5989583333333334 |
| summary.primary.accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5989583333333334 |
| summary.per_token_secondary.accuracy.point | 0.5833333333333334 |
| summary.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6302083333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| summary.per_token_secondary.macro_f1 | 0.5826086956521739 |
| summary.per_token_secondary.mcc | 0.16724840200141816 |
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
<summary>reports/phase6/base-label-smoothing-comparison-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/job.json) ／ SHA256: `21436bae23dfa86f329ce87a038bdf4435e47dda0e4acaeedf5e3cade26d67fd` ／ 1,309 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_occupancy_seconds | 1432.7639809400134 |
| Base_complete | false |
| resident_memory_policy.visible_device_bytes | 25756696576 |
| resident_memory_policy.allocator_allowance_bytes | 23181026918 |
| resident_memory_policy.expected_worst_peak_bytes | 10756030976 |
| scientific_CE_teacher_tokens | 99900395 |
| local_update | 17680 |
| loss | 3.4299116134643555 |
| latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-label-smoothing-comparison-20261007/smoothing/checkpoint-00017698.pt" |

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/result.json) ／ SHA256: `afa08454579bf021323379a4f8ca0cb77e827ebb0eee5b0b30faf94853e40415` ／ 296,975 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| results.smoothing.training.status | "complete" |
| results.smoothing.training.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.smoothing.training.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.smoothing.training.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-label-smoothing-comparison-20261007/smoothing/checkpoint-00017698.pt" |
| results.smoothing.training.checkpoint_sha256 | "5d6ae5726c63b69edb7d7f7b74c232fe1b3d2093f5297787df1ce6ed42a7869b" |
| results.smoothing.training.scientific_CE_teacher_tokens | 100000000 |
| results.smoothing.training.counters.update | 17698 |
| results.smoothing.training.counters.supervised_tokens | 100000000 |
| results.smoothing.training.counters.CE_input_tokens | 102655467 |
| results.smoothing.training.counters.auxiliary_input_tokens | 0 |
| results.smoothing.training.counters.auxiliary_pairs | 0 |
| results.smoothing.training.counters.physical_input_tokens | 370838917 |
| results.smoothing.training.counters.original_body_bytes | 405882136 |
| results.smoothing.training.counters.token_digest | "a1ab017092f823d69e033d96868136ebeb0a55f13e2cb1cfd039e3c7d920a1c9" |
| results.smoothing.training.counters.source_teachers.web | 75000000 |
| results.smoothing.training.counters.source_teachers.textbook | 20000000 |
| results.smoothing.training.counters.source_teachers.story | 5000000 |
| results.smoothing.training.counters.source_EOS.web | 657450 |
| results.smoothing.training.counters.source_EOS.textbook | 148625 |
| results.smoothing.training.counters.source_EOS.story | 38222 |
| results.smoothing.training.sampler.kind | "bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1" |
| results.smoothing.training.sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| results.smoothing.training.sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| results.smoothing.training.sampler.binding.index_size | 12861257655 |
| results.smoothing.training.sampler.binding.index_mtime_ns | 1791234945567297288 |
| results.smoothing.training.sampler.binding.stream_size | 4000002624 |
| results.smoothing.training.sampler.binding.stream_mtime_ns | 1791234945514053852 |
| results.smoothing.training.sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| results.smoothing.training.sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| results.smoothing.training.sampler.seed | 42 |
| results.smoothing.training.sampler.goals.web | 75000000 |
| results.smoothing.training.sampler.goals.textbook | 20000000 |
| results.smoothing.training.sampler.goals.story | 5000000 |
| results.smoothing.training.sampler.consumed.web | 75000000 |
| results.smoothing.training.sampler.consumed.textbook | 20000000 |
| results.smoothing.training.sampler.consumed.story | 5000000 |
| results.smoothing.training.sampler.pending.web | [] |
| results.smoothing.training.sampler.pending.textbook | [] |
| results.smoothing.training.sampler.pending.story | [] |
| results.smoothing.training.sampler.draws | 2656558 |
| results.smoothing.training.sampler.documents_drawn | 844300 |
| results.smoothing.training.sampler.windows_emitted | 849479 |
| results.smoothing.training.sampler.auxiliary_reasons.original_sentence_or_LF_boundary | 676390 |
| results.smoothing.training.sampler.auxiliary_reasons.no_original_codec_stable_sentence_pair | 167910 |
| results.smoothing.training.parent_CE_teacher_tokens | 9978838479 |
| results.smoothing.training.Base_complete | false |
| results.smoothing.evaluation.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.smoothing.evaluation.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.smoothing.evaluation.checkpoint_sha256 | "5d6ae5726c63b69edb7d7f7b74c232fe1b3d2093f5297787df1ce6ed42a7869b" |
| results.smoothing.evaluation.body.documents | 256 |
| results.smoothing.evaluation.body.limit_documents | 256 |
| results.smoothing.evaluation.body.body_nll | 342160.5264415741 |
| results.smoothing.evaluation.body.eos_nll | 544.3450270481408 |
| results.smoothing.evaluation.body.body_bytes | 472055 |
| results.smoothing.evaluation.body.body_tokens | 122343 |
| results.smoothing.evaluation.body.bpb | 1.0457113994878056 |
| results.smoothing.evaluation.body.seconds | 1.3373736609937623 |
| results.smoothing.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| results.smoothing.evaluation.generation.max_new_tokens | 64 |
| results.smoothing.evaluation.greedy_rates.eos | 27 |
| results.smoothing.evaluation.greedy_rates.repetition | 42 |
| results.smoothing.evaluation.greedy_rates.unicode_failure | 0 |
| results.smoothing.evaluation.greedy_rates.role_leak | 0 |
| results.smoothing.evaluation.greedy_rates.empty | 0 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.point | 0.5989583333333334 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.5989583333333334 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6302083333333334] |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5826086956521739 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.16724840200141816 |
| results.smoothing.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| results.smoothing.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| results.smoothing.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| results.smoothing.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7492447129909365, 0.8338368580060423] |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| results.smoothing.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| results.smoothing.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| results.smoothing.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.smoothing.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.32082216264521896 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.2931188561215371, 0.34673815907059874] |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.32082216264521896 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.306076854334227 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2801608579088472, 0.3320040214477211] |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.30563002680965146 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3042124399702949 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.13181731002303418 |
| results.smoothing.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| results.smoothing.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| results.smoothing.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| results.smoothing.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| results.smoothing.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.smoothing.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.smoothing.evaluation.diagnostics.semantic_both_contexts.correct | 22 |
| results.smoothing.evaluation.memory.maximum_observed_allocated_bytes | 268768256 |
| results.smoothing.evaluation.memory.maximum_observed_reserved_bytes | 11957960704 |
| results.smoothing.evaluation.protected_test_used | false |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.auxiliary_input_tokens | true |
| common_CE_checks.CE.auxiliary_pairs | true |
| common_CE_checks.CE.physical_input_tokens | true |
| common_CE_checks.CE.full_sampler | true |
| scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 100000000 |
| reused_control_GPU_seconds | 0 |
| GPU_occupancy_seconds | 1432.7639809400134 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-20261007/review.json — new80_and_reused80_smoothing_comparison_reviewed</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/review.json) ／ SHA256: `9f51096eec852a5a38b3dc2a4782023ecb4236825e921a603a56769dc510c7b2` ／ 11,859 bytes

| 原キー | 保存値 |
|---|---|
| status | "new80_and_reused80_smoothing_comparison_reviewed" |
| summaries.smoothing.BPB | 1.0457113994878056 |
| summaries.smoothing.rates.eos | 27 |
| summaries.smoothing.rates.repetition | 42 |
| summaries.smoothing.rates.unicode_failure | 0 |
| summaries.smoothing.rates.role_leak | 0 |
| summaries.smoothing.rates.empty | 0 |
| summaries.smoothing.grammar2 | 58 |
| summaries.smoothing.relevance2 | 32 |
| summaries.smoothing.coherent | 2 |
| summaries.smoothing.appropriate | 1 |
| summaries.smoothing.notes_sha256 | "d9f13ec5f234e683963dae35228b0f788eb8cae2e6e57121e78cbba16318a0eb" |
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
| strong_and_matched_quality.CE.checks.repetition_nonworsening | true |
| strong_and_matched_quality.CE.checks.no_empty_role_unicode | true |
| strong_and_matched_quality.CE.checks.BPB_gate | false |
| strong_and_matched_quality.CE.checks.appropriate_completion_not_punctuation | true |
| strong_and_matched_quality.CE.passed | false |
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
| paired_common_byte_BPB.CE.point | 0.04722423697396052 |
| paired_common_byte_BPB.CE.ci95 | [0.04534503538459256, 0.04915612009930894] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.0457113994878056 |
| paired_common_byte_BPB.CE.relative_ratio | 1.047295787814704 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "smoothing minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.smoothing.exact_content_pair_clusters | 96 |
| exact_content_semantics.smoothing.original_nominal_accuracy.point | 0.5989583333333334 |
| exact_content_semantics.smoothing.original_nominal_accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| exact_content_semantics.smoothing.original_nominal_accuracy.units | 96 |
| exact_content_semantics.smoothing.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.smoothing.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.smoothing.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.smoothing.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.smoothing.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.content_cluster_accuracy.point | 0.5989583333333334 |
| exact_content_semantics.smoothing.content_cluster_accuracy.ci95 | [0.5520833333333334, 0.6458333333333334] |
| exact_content_semantics.smoothing.content_cluster_accuracy.units | 96 |
| exact_content_semantics.smoothing.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.smoothing.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.smoothing.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.smoothing.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.smoothing.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.both_contexts_hard_correct.point | 0.22916666666666666 |
| exact_content_semantics.smoothing.both_contexts_hard_correct.ci95 | [0.14583333333333334, 0.3125] |
| exact_content_semantics.smoothing.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.smoothing.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.smoothing.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.smoothing.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.smoothing.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.smoothing.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.causality.seed | 42 |
| exact_content_semantics.smoothing.categories.causality.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.comparison.seed | 42 |
| exact_content_semantics.smoothing.categories.comparison.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.coreference.seed | 42 |
| exact_content_semantics.smoothing.categories.coreference.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.negation.seed | 42 |
| exact_content_semantics.smoothing.categories.negation.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.quantity.seed | 42 |
| exact_content_semantics.smoothing.categories.quantity.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.smoothing.categories.time.seed | 42 |
| exact_content_semantics.smoothing.categories.time.repetitions | 2000 |
| exact_content_semantics.smoothing.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | -0.026041666666666668 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.05221354166666666, 0.0] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 17698 |
| accounting.optimizer_updates | 17698 |
| accounting.CE_teacher_tokens | 100000000 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.textbook | 20000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_EOS.web | 657450 |
| accounting.source_EOS.textbook | 148625 |
| accounting.source_EOS.story | 38222 |
| accounting.CE_input_tokens | 102655467 |
| accounting.auxiliary_input_tokens | 0 |
| accounting.auxiliary_pairs | 0 |
| accounting.physical_input_tokens | 370838917 |
| accounting.original_body_bytes | 405882136 |
| history.committed_updates | 17698 |
| history.optimizer_updates | 17698 |
| history.observed_completed_attempt_updates | 17698 |
| common_CE_checks.CE.update | true |
| common_CE_checks.CE.token_digest | true |
| common_CE_checks.CE.supervised_tokens | true |
| common_CE_checks.CE.source_teachers | true |
| common_CE_checks.CE.source_EOS | true |
| common_CE_checks.CE.CE_input_tokens | true |
| common_CE_checks.CE.original_body_bytes | true |
| common_CE_checks.CE.auxiliary_input_tokens | true |
| common_CE_checks.CE.auxiliary_pairs | true |
| common_CE_checks.CE.physical_input_tokens | true |
| common_CE_checks.CE.full_sampler | true |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teachers | 100000000 |
| reused_control_GPU_seconds | 0 |
| probe_verification_updates | 44 |
| probe_verification_CE_teachers | 256032 |
| GPU_occupancy_seconds | 1432.7639809400134 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "Single learned seed, repeated nonblind DEV, same native parameters/CE input and teacher stream; weighted gold mass90M/uniform mass10M and smoothing/GPU overhead differ. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored." |

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-20261007/smoothing/train-result.json — complete</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-20261007/smoothing/train-result.json) ／ SHA256: `b0ecccaaa1f1d636338cb5a6cf436c5cd85c11c04a0b0043ccee2a6f47bc6e9f` ／ 17,874 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-label-smoothing-comparison-20261007/smoothing/checkpoint-00017698.pt" |
| checkpoint_sha256 | "5d6ae5726c63b69edb7d7f7b74c232fe1b3d2093f5297787df1ce6ed42a7869b" |
| scientific_CE_teacher_tokens | 100000000 |
| counters.update | 17698 |
| counters.supervised_tokens | 100000000 |
| counters.CE_input_tokens | 102655467 |
| counters.auxiliary_input_tokens | 0 |
| counters.auxiliary_pairs | 0 |
| counters.physical_input_tokens | 370838917 |
| counters.original_body_bytes | 405882136 |
| counters.token_digest | "a1ab017092f823d69e033d96868136ebeb0a55f13e2cb1cfd039e3c7d920a1c9" |
| counters.source_teachers.web | 75000000 |
| counters.source_teachers.textbook | 20000000 |
| counters.source_teachers.story | 5000000 |
| counters.source_EOS.web | 657450 |
| counters.source_EOS.textbook | 148625 |
| counters.source_EOS.story | 38222 |
| sampler.kind | "bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1" |
| sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| sampler.binding.index_size | 12861257655 |
| sampler.binding.index_mtime_ns | 1791234945567297288 |
| sampler.binding.stream_size | 4000002624 |
| sampler.binding.stream_mtime_ns | 1791234945514053852 |
| sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| sampler.seed | 42 |
| sampler.goals.web | 75000000 |
| sampler.goals.textbook | 20000000 |
| sampler.goals.story | 5000000 |
| sampler.consumed.web | 75000000 |
| sampler.consumed.textbook | 20000000 |
| sampler.consumed.story | 5000000 |
| sampler.pending.web | [] |
| sampler.pending.textbook | [] |
| sampler.pending.story | [] |
| sampler.draws | 2656558 |
| sampler.documents_drawn | 844300 |
| sampler.windows_emitted | 849479 |
| sampler.auxiliary_reasons.original_sentence_or_LF_boundary | 676390 |
| sampler.auxiliary_reasons.no_original_codec_stable_sentence_pair | 167910 |
| parent_CE_teacher_tokens | 9978838479 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-launcher-20261007/launcher.json) ／ SHA256: `24266404b1fdf7bf318bf36dfcb7c934f91c73ddb187ec3a99e61a8aba05451f` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-label-smoothing-comparison-launcher-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-label-smoothing-comparison-launcher-20261007/result.json) ／ SHA256: `4eb6e3fe9168aab9c18139f18c24bce5b0230777ee1db17453d4ab32a34ad5d7` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-muon-comparison-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-muon-comparison-launcher-20261007/launcher.json) ／ SHA256: `92c22c41af242346bae80fa1105273b8356a1a5cb4ac44931cf86e47f8e5c3e1` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-muon-probe-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/base-muon-probe-20261007/job.json) ／ SHA256: `97c048aef9c40c34a596f9eb06f1871e8c362a150817d00a06b733505cc569fe` ／ 473 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| scientific_teacher_positions | 0 |
| Base_complete | false |
| GPU_occupancy_seconds | 10.227059504017234 |

</details>

<details>
<summary>reports/phase6/base-muon-probe-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-muon-probe-20261007/result.json) ／ SHA256: `0fecdd30fdfec3e599f065b83409abfb53f3d45e833097b7088eeadf0f64c53f` ／ 472,615 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| passed | true |
| initial_checks.native_parent_weights | true |
| initial_checks.tied_native_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.all_parameters_once | true |
| all_resume_and_source_checks.kind | true |
| all_resume_and_source_checks.spec | true |
| all_resume_and_source_checks.binding | true |
| all_resume_and_source_checks.lineage | true |
| all_resume_and_source_checks.model_config | true |
| all_resume_and_source_checks.model | true |
| all_resume_and_source_checks.optimizer | true |
| all_resume_and_source_checks.scheduler | true |
| all_resume_and_source_checks.RNG | true |
| all_resume_and_source_checks.sampler | true |
| all_resume_and_source_checks.counters | true |
| all_resume_and_source_checks.finite_hybrid_model_buffers | true |
| all_resume_and_source_checks.history_except_timing | true |
| all_resume_and_source_checks.same_original_stream | true |
| all_resume_and_source_checks.full_sampler_matches_AdamW | true |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 11987593728 |
| capacity.context | 1024 |
| capacity.target_stride | 512 |
| capacity.batch | 48 |
| capacity.original_target_positions | 24576 |
| capacity.peak_VRAM_bytes | 10719607808 |
| capacity.CE_loss | 2.265882730484009 |
| capacity.gradient_norm | 3.153932809829712 |
| capacity.optimizer_updates | 0 |
| median_original_teachers_per_second | 37893.90946293704 |
| science_budget_seconds | 4331 |
| science_budget_eligible | true |
| total_GPU_cap_seconds | 4800 |
| GPU_occupancy_seconds | 10.227059504017234 |
| verification_updates | 47 |
| verification_original_teacher_positions | 273521 |
| capacity_forward_backward_original_positions | 24576 |
| scientific_teacher_positions | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-muon-probe-launcher-20261007/corrected-launcher.json — None</summary>

[原記録](../../reports/phase6/base-muon-probe-launcher-20261007/corrected-launcher.json) ／ SHA256: `8a21aa57232e9e8de9a0c58c0ece98af7b64a084a8805cd9072e2143117bbcee` ／ 127 bytes

| 原キー | 保存値 |
|---|---|
| reason | "Corrected CPU path API before GPU" |

</details>

<details>
<summary>reports/phase6/base-muon-probe-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-muon-probe-launcher-20261007/launcher.json) ／ SHA256: `cf1f88e9e6b88c9feb0c2277ea11260115bdfebd90a403a4c966bdf9f5370cb1` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-muon-probe-launcher-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-muon-probe-launcher-20261007/result.json) ／ SHA256: `5ba2006311d90e01dbf4b0747c15423bdfb7e33c765e8776bc9f2099f2b449ae` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-launcher-20261007/launcher.json) ／ SHA256: `03be566c55f23f9da0044ce2dec422e02d49cd6f309d0ff949806362acd8eebe` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-launcher-20261007/result.json — failed</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-launcher-20261007/result.json) ／ SHA256: `fc4cb4138496370f50055b51f215c822e963a6fe8d5968b436b3061de3970e36` ／ 153 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-probe-20261007/compiler_statistics.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-probe-20261007/compiler_statistics.json) ／ SHA256: `2dbaf75dd9907c9802220801b53ded83f03d6d0a02bca9701a695106cde26037` ／ 1,009 bytes

| 原キー | 保存値 |
|---|---|
| stats.calls_captured | "3516" |
| inductor.benchmarking.InductorBenchmarker.benchmark_gpu | "48" |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-probe-20261007/initial_checks.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-probe-20261007/initial_checks.json) ／ SHA256: `c23d6a33b3759e4a5bef1df6c3322f0883645150968806ac88686b15ceafa1e2` ／ 212 bytes

| 原キー | 保存値 |
|---|---|
| teacher_weights | true |
| teacher_eval_no_grad | true |
| teacher_tied_vocab | true |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-probe-20261007/job.json — failed</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-probe-20261007/job.json) ／ SHA256: `9b8e053676bd9f34e4324928e17ea0f87013e393b27727dc323c57f912ca7aa1` ／ 538 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| scientific_teacher_positions | 0 |
| GPU_occupancy_seconds | 66.81598484001006 |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-probe-20261007/numeric_checks.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-probe-20261007/numeric_checks.json) ／ SHA256: `8312f7b8e7d3f3d84223961e6e1572cc66f9a9a70f07e4b15fd006ec7b7191b8` ／ 822 bytes

| 原キー | 保存値 |
|---|---|
| web.eager_losses.CE_loss | 2.8211193084716797 |
| web.eager_losses.KD_loss | 0.0 |
| web.eager_losses.combined_loss | 2.8211193084716797 |
| web.compiled_losses.CE_loss | 2.821584701538086 |
| web.compiled_losses.KD_loss | 0.0 |
| web.compiled_losses.combined_loss | 2.821584701538086 |
| web.absolute_loss_differences.CE_loss | 0.00046539306640625 |
| web.absolute_loss_differences.KD_loss | 0.0 |
| web.absolute_loss_differences.combined_loss | 0.00046539306640625 |
| web.teacher_logits.cosine | 0.9999823980469994 |
| web.teacher_logits.relative_L2 | 0.005937034763091353 |
| web.passed | false |
| web.teacher_web_logits_diagnostic_only | true |
| web.optimizer_updates | 0 |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-compile-probe-20261007/partial_histories.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-compile-probe-20261007/partial_histories.json) ／ SHA256: `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` ／ 3 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-20261007/job.json — failed</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-20261007/job.json) ／ SHA256: `fba46fc00da9027ab965ee3e2177f013a61b5ea4780cb2c7bd39c1ee085a155f` ／ 545 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| scientific_teacher_positions | 0 |
| GPU_occupancy_seconds | 7.349647694994928 |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-20261007/partial_histories.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-20261007/partial_histories.json) ／ SHA256: `15a68097ce65f81b0140152941486cae340b7a7b36ed174498fdb21f0bb80249` ／ 336,420 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-launcher-20261007/launcher.json) ／ SHA256: `fb60d21588bcaac65db8ea6eace3cd0a29e6d46e9405aa5105e95c05d48622df` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-launcher-20261007/result.json — failed</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-launcher-20261007/result.json) ／ SHA256: `f2a1390d2da6bab2751312c41f17e72ccf6041f4fd9bc4a3b2842833a79689f1` ／ 153 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-v2-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-v2-20261007/job.json) ／ SHA256: `5624edecf5e293a042162af6a1beeafbb1fa2a6d152d4bacd05a6d522a5bf55f` ／ 460 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| scientific_teacher_positions | 0 |
| GPU_occupancy_seconds | 12.28218039200874 |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-v2-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-v2-20261007/result.json) ／ SHA256: `1e2d535768db080ba3e06beb1770e16491a23df287130d22344601b33724cfca` ／ 490,407 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| passed | true |
| initial_checks.native_parent_weights | true |
| initial_checks.frozen_teacher_weights | true |
| initial_checks.teacher_eval_no_grad | true |
| initial_checks.native_tied_vocab | true |
| initial_checks.teacher_native_tied_vocab | true |
| initial_checks.parameters | true |
| initial_checks.teacher_parameters | true |
| initial_checks.student_optimizer_only | true |
| initial_checks.teacher_unchanged_after_stress | true |
| initial_checks.teacher_unchanged_continuous | true |
| initial_checks.teacher_unchanged_resumed | true |
| all_resume_and_source_checks.kind | true |
| all_resume_and_source_checks.spec | true |
| all_resume_and_source_checks.binding | true |
| all_resume_and_source_checks.lineage | true |
| all_resume_and_source_checks.model_config | true |
| all_resume_and_source_checks.model | true |
| all_resume_and_source_checks.optimizer | true |
| all_resume_and_source_checks.scheduler | true |
| all_resume_and_source_checks.RNG | true |
| all_resume_and_source_checks.sampler | true |
| all_resume_and_source_checks.counters | true |
| all_resume_and_source_checks.native_teacher_KD | true |
| all_resume_and_source_checks.finite_all_state | true |
| all_resume_and_source_checks.history_except_timing | true |
| all_resume_and_source_checks.same_original_gold_stream | true |
| all_resume_and_source_checks.full_original_sampler | true |
| all_resume_and_source_checks.short_only_teacher_positions | true |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 11987593728 |
| capacity.batch | 48 |
| capacity.context | 1024 |
| capacity.target_stride | 512 |
| capacity.diagnostic_positions | 24576 |
| capacity.peak_VRAM_bytes | 13047812096 |
| capacity.CE_loss | 2.271785020828247 |
| capacity.KD_loss | 0.3330673575401306 |
| capacity.gradient_norm | 3.97502064704895 |
| capacity.optimizer_updates | 0 |
| capacity.scientific_teachers | 0 |
| capacity.scope | "Artificial all-KD upper-bound shape on the existing originalTRAIN1024 stress window, not relabeled short-source training or new science." |
| median_original_teachers_per_second | 41557.72758192472 |
| science_budget_seconds | 4029 |
| science_budget_eligible | false |
| total_GPU_cap_seconds | 3600 |
| GPU_occupancy_seconds | 12.28218039200874 |
| verification_updates | 47 |
| verification_original_teacher_positions | 273521 |
| verification_KD_positions | 62601 |
| native_teacher_KD_state.updates | 4 |
| native_teacher_KD_state.teacher_positions | 5798 |
| native_teacher_KD_state.teacher_EOS | 46 |
| native_teacher_KD_state.teacher_valid_inputs | 5798 |
| native_teacher_KD_state.teacher_physical_inputs | 11795 |
| native_teacher_KD_state.source_positions.web | 0 |
| native_teacher_KD_state.source_positions.textbook | 4613 |
| native_teacher_KD_state.source_positions.story | 1185 |
| native_teacher_KD_state.teacher_entropy_sum | 11881.607666015625 |
| native_teacher_KD_state.teacher_gold_probability_sum | 2212.1563720703125 |
| native_teacher_KD_state.KL_sum | 3953.345572322607 |
| native_teacher_KD_state.digest | "df4e89f9c72ce39fd2317bae1ca07a1eda4744670584f097cc0e46a5851994d5" |
| scientific_teacher_positions | 0 |
| prior_probe_GPU_seconds | 7.349647694994928 |
| additional_probe_GPU_seconds | 4.932532697013812 |
| timing_teacher_equality_bool_missing_from_initial_failure | true |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-v2-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-v2-launcher-20261007/launcher.json) ／ SHA256: `afd80323ef72e5c2520f858251a3157424b16a2fb01a6ec049c398756a20c606` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-native-teacher-KD-probe-v2-launcher-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-native-teacher-KD-probe-v2-launcher-20261007/result.json) ／ SHA256: `d1ad9075a259850e8c20229a3c06efde807c02b72164bd11f66eff38ba0e6fcb` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-comparison-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-comparison-launcher-20261007/launcher.json) ／ SHA256: `aef1061b24c2cc0852991f6e3a76d76a7073f35b3d63ffb367bdaf0d886fd13c` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-20261007/capacity.json — None</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-20261007/capacity.json) ／ SHA256: `582d3cb03824c2664845965c7c30d7612ddb5a91b7092d937f05b2776c152ba7` ／ 575 bytes

| 原キー | 保存値 |
|---|---|
| CE_loss | 2.271785020828247 |
| teacher_feedback_KL | 0.6064739227294922 |
| peak_VRAM_bytes | 11034152960 |
| optimizer_updates | 0 |
| scientific_teachers | 0 |
| scope | "Original fixed TRAIN worst gold window plus original shortTRAIN8 hypothetical prefix score upper bound.8x49 exceeds actual max8x48 scoring by one position; not current-student rollout science." |

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-20261007/job.json — complete</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-20261007/job.json) ／ SHA256: `efa7ee3362e3413550ed4815f3bf3c9d7a783ad4f60ceb846c5788bcd9bcd0b4` ／ 459 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| scientific_teacher_positions | 0 |
| GPU_occupancy_seconds | 21.7514864129771 |

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-20261007/partial_histories.json — None</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-20261007/partial_histories.json) ／ SHA256: `9c57d53665996f06c2ec335e7b667ac4cc564a0f78f5f06f70c6672412d49a68` ／ 1,325,784 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-20261007/result.json) ／ SHA256: `246a1ed0dd418938c98c9df005c78577cdbc2d58ee70a8d455c210a344c9bc97` ／ 1,437,996 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| passed | true |
| initial_checks.parent_weights | true |
| initial_checks.teacher_weights | true |
| initial_checks.frozen_teacher | true |
| initial_checks.native_tied_vocab | true |
| initial_checks.teacher_tied_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.student_only_optimizer | true |
| initial_checks.teacher_unchanged_stress | true |
| initial_checks.teacher_unchanged_continuous | true |
| initial_checks.teacher_unchanged_resumed | true |
| initial_checks.teacher_unchanged_timings | true |
| all_resume_and_source_checks.kind | true |
| all_resume_and_source_checks.spec | true |
| all_resume_and_source_checks.binding | true |
| all_resume_and_source_checks.lineage | true |
| all_resume_and_source_checks.model_config | true |
| all_resume_and_source_checks.model | true |
| all_resume_and_source_checks.optimizer | true |
| all_resume_and_source_checks.scheduler | true |
| all_resume_and_source_checks.RNG | true |
| all_resume_and_source_checks.sampler | true |
| all_resume_and_source_checks.counters | true |
| all_resume_and_source_checks.on_policy_teacher | true |
| all_resume_and_source_checks.committed_all_state | true |
| all_resume_and_source_checks.history_except_timing | true |
| all_resume_and_source_checks.actual_two_rollout_batches | true |
| all_resume_and_source_checks.same_original_gold_stream | true |
| all_resume_and_source_checks.full_original_sampler | true |
| all_resume_and_source_checks.short_only_teacher | true |
| capacity.main_shape | [48, 1024] |
| capacity.auxiliary_shape | [8, 49] |
| capacity.diagnostic_gold_positions | 24576 |
| capacity.diagnostic_auxiliary_positions | 256 |
| capacity.CE_loss | 2.271785020828247 |
| capacity.teacher_feedback_KL | 0.6064739227294922 |
| capacity.gradient_norm | 4.2836527824401855 |
| capacity.peak_VRAM_bytes | 11034152960 |
| capacity.optimizer_updates | 0 |
| capacity.scientific_teachers | 0 |
| capacity.scope | "Original fixed TRAIN worst gold window plus original shortTRAIN8 hypothetical prefix score upper bound.8x49 exceeds actual max8x48 scoring by one position; not current-student rollout science." |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 11987593728 |
| median_original_teachers_per_second | 77345.84176833987 |
| postwarmup_total32_step_seconds | 3.702358888986055 |
| rollout_step_seconds | [0.6822600629820954, 0.6418070399959106] |
| science_budget_seconds | 3562 |
| science_budget_eligible | true |
| total_GPU_cap_seconds | 7200 |
| GPU_occupancy_seconds | 21.7514864129771 |
| verification_updates | 131 |
| verification_original_teacher_positions | 762296 |
| verification_distribution_positions | 1470 |
| scientific_teacher_positions | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-launcher-20261007/launcher.json — None</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-launcher-20261007/launcher.json) ／ SHA256: `8107a07a637fbfb7d4601269108796716868cfa41400b81e6f2b52169906e6b5` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-on-policy-teacher-probe-launcher-20261007/result.json — complete</summary>

[原記録](../../reports/phase6/base-on-policy-teacher-probe-launcher-20261007/result.json) ／ SHA256: `4fa21dc5f87d0891619eff8d9b9fb9723e1c0648d4f64b969c0354775ca4b0b8` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/body.json) ／ SHA256: `2fb421ea0ef6232b99444401bb201a08f0020be2ac2be7799a237691313f36df` ／ 67,404 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 356755.35076904297 |
| body.eos_nll | 1093.0935409367085 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0903161185986823 |
| body.seconds | 1.3297267500020098 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/generation.json) ／ SHA256: `de0d9bc7887b40a7b7613513fae9743178092c064b370fe7f6a75fda98f3960d` ／ 118,541 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/jblimp.json) ／ SHA256: `51bc565d31e3d5ff67cdcc7ff0407e3190166fe4aee58b1acd6717b2ddb326c8` ／ 338,617 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.8006042296072508 |
| summary.primary.accuracy.ci95 | [0.7583081570996979, 0.8429003021148036] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.8006042296072508 |
| summary.per_token_secondary.accuracy.point | 0.7492447129909365 |
| summary.per_token_secondary.accuracy.ci95 | [0.7039274924471299, 0.797583081570997] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7492447129909365 |
| summary.per_token_secondary.macro_f1 | 0.4283246977547496 |
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
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/jcqa.json) ／ SHA256: `e0deaca0cf7ac34c0b7cde15e9c9c1f7111d9d8d4742af18c2d5cc6195bbbb3e` ／ 1,639,645 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.37131367292225204 |
| summary.primary.accuracy.ci95 | [0.3418118856121537, 0.3999106344950849] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.3708668453976765 |
| summary.per_token_secondary.accuracy.point | 0.3409294012511171 |
| summary.per_token_secondary.accuracy.ci95 | [0.31322609472743523, 0.36952636282394996] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| summary.per_token_secondary.macro_f1 | 0.34038820179370183 |
| summary.per_token_secondary.mcc | 0.17712275665469462 |
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
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/result.json) ／ SHA256: `4d1a4cd1e6a312845b9c209b94a5c5176fc3cc4c12848a0ec84081af0ece7efa` ／ 216,561 bytes

| 原キー | 保存値 |
|---|---|
| binding.parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| binding.parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| binding.checkpoint_ancestry_binding.config_sha256 | "dfd6a6aee8507dcae3f66e3309e3d2ffd4845004f053ad3f07e0eea0829daef0" |
| binding.checkpoint_ancestry_binding.source_binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| binding.checkpoint_ancestry_binding.source_binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| binding.checkpoint_ancestry_binding.source_binding.index_size | 12861257655 |
| binding.checkpoint_ancestry_binding.source_binding.index_mtime_ns | 1791234945567297288 |
| binding.checkpoint_ancestry_binding.source_binding.stream_size | 4000002624 |
| binding.checkpoint_ancestry_binding.source_binding.stream_mtime_ns | 1791234945514053852 |
| binding.checkpoint_ancestry_binding.source_binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| binding.checkpoint_ancestry_binding.source_binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| binding.checkpoint_ancestry_binding.weights_role | "scientific_fresh_teacher_decay_pilot" |
| checkpoint_sha256 | "03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 356755.35076904297 |
| body.eos_nll | 1093.0935409367085 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0903161185986823 |
| body.seconds | 1.3297267500020098 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 23 |
| greedy_rates.repetition | 27 |
| greedy_rates.unicode_failure | 1 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5625 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.515625, 0.6041666666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5727312201476336 |
| diagnostics.semantics.per_token_secondary.mcc | 0.14596008983995234 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.8006042296072508 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7583081570996979, 0.8429003021148036] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.8006042296072508 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7945619335347432 |
| diagnostics.jcqa.primary.accuracy.point | 0.37131367292225204 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3418118856121537, 0.3999106344950849] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.3708668453976765 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3409294012511171 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.31322609472743523, 0.36952636282394996] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.34038820179370183 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.17712275665469462 |
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
| diagnostics.semantic_both_contexts.correct | 16 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 10779361280 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/semantics.json) ／ SHA256: `7df21f246df075d137c4c6b3d9f6fad1e95280069c3b0cbafa976db58bb2ccb1` ／ 203,464 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5625 |
| summary.primary.accuracy.ci95 | [0.515625, 0.6041666666666666] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5625 |
| summary.per_token_secondary.accuracy.point | 0.5729166666666666 |
| summary.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| summary.per_token_secondary.macro_f1 | 0.5727312201476336 |
| summary.per_token_secondary.mcc | 0.14596008983995234 |
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
<summary>reports/phase6/base-teacher-decay-2b-20261008/job.json — complete</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/job.json) ／ SHA256: `f8429a8057c532d38d634d119af90db7e4506586000854d7d87470822fbc70e1` ／ 1,542 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 26060.094265680003 |
| prior_pilot_GPU_seconds | 1415.1338874759967 |
| cumulative_GPU_ledger_closed | true |
| Base_complete | false |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 17791499264 |
| latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-2b-20261008/latest.pt" |
| optimizer_updates | 212080 |
| scientific_cumulative_teacher_tokens | 1999868016 |
| new_scientific_teacher_tokens | 1905707821 |
| CE_loss | 2.512122392654419 |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/result.json — learning_and_native_evaluation_complete_content_pending</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/result.json) ／ SHA256: `17b32218b0fe92e3668dd2ba3a42f26f6c3543f63cbcfdc5c0c1a473a142dab0` ／ 6,632 bytes

| 原キー | 保存値 |
|---|---|
| status | "learning_and_native_evaluation_complete_content_pending" |
| binding.parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| binding.parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| binding.checkpoint_ancestry_binding.config_sha256 | "dfd6a6aee8507dcae3f66e3309e3d2ffd4845004f053ad3f07e0eea0829daef0" |
| binding.checkpoint_ancestry_binding.source_binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| binding.checkpoint_ancestry_binding.source_binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| binding.checkpoint_ancestry_binding.source_binding.index_size | 12861257655 |
| binding.checkpoint_ancestry_binding.source_binding.index_mtime_ns | 1791234945567297288 |
| binding.checkpoint_ancestry_binding.source_binding.stream_size | 4000002624 |
| binding.checkpoint_ancestry_binding.source_binding.stream_mtime_ns | 1791234945514053852 |
| binding.checkpoint_ancestry_binding.source_binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| binding.checkpoint_ancestry_binding.source_binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| binding.checkpoint_ancestry_binding.weights_role | "scientific_fresh_teacher_decay_pilot" |
| resume_gate.checks.kind | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.binding | true |
| resume_gate.checks.lineage | true |
| resume_gate.checks.model_config | true |
| resume_gate.checks.model | true |
| resume_gate.checks.optimizer | true |
| resume_gate.checks.scheduler | true |
| resume_gate.checks.RNG | true |
| resume_gate.checks.sampler | true |
| resume_gate.checks.counters | true |
| resume_gate.checks.decay | true |
| resume_gate.checks.same_learned_parent_before_first_update | true |
| resume_gate.checks.full_committed_history | true |
| resume_gate.checks.resident_peak_under90percent | true |
| resume_gate.actual_CUDA_or_CPU_updates | 8 |
| resume_gate.verification_microbatches | 8 |
| resume_gate.initial_counters.update | 10000 |
| resume_gate.initial_counters.supervised_tokens | 94160195 |
| resume_gate.initial_counters.CE_input_tokens | 96655164 |
| resume_gate.initial_counters.auxiliary_input_tokens | 0 |
| resume_gate.initial_counters.auxiliary_pairs | 0 |
| resume_gate.initial_counters.physical_input_tokens | 404673920 |
| resume_gate.initial_counters.original_body_bytes | 382169159 |
| resume_gate.initial_counters.token_digest | "26b260437b751cb63b2e2922659bbac6b6e90adc983cd578626cdb0baf9a3dc4" |
| resume_gate.initial_counters.source_teachers.web | 70620030 |
| resume_gate.initial_counters.source_teachers.textbook | 18832118 |
| resume_gate.initial_counters.source_teachers.story | 4708047 |
| resume_gate.initial_counters.source_EOS.web | 619232 |
| resume_gate.initial_counters.source_EOS.textbook | 139904 |
| resume_gate.initial_counters.source_EOS.story | 35998 |
| resume_gate.final_verification_counters.update | 10004 |
| resume_gate.final_verification_counters.supervised_tokens | 94195927 |
| resume_gate.final_verification_counters.CE_input_tokens | 96691408 |
| resume_gate.final_verification_counters.auxiliary_input_tokens | 0 |
| resume_gate.final_verification_counters.auxiliary_pairs | 0 |
| resume_gate.final_verification_counters.physical_input_tokens | 404826320 |
| resume_gate.final_verification_counters.original_body_bytes | 382314679 |
| resume_gate.final_verification_counters.token_digest | "ef3c1320b1715fd58ecb0e98d4f42a17a9a5c1659683ffc42732ece126eda415" |
| resume_gate.final_verification_counters.source_teachers.web | 70646944 |
| resume_gate.final_verification_counters.source_teachers.textbook | 18839198 |
| resume_gate.final_verification_counters.source_teachers.story | 4709785 |
| resume_gate.final_verification_counters.source_EOS.web | 619477 |
| resume_gate.final_verification_counters.source_EOS.textbook | 139960 |
| resume_gate.final_verification_counters.source_EOS.story | 36016 |
| resume_gate.verification_teacher_tokens | 71464 |
| resume_gate.verification_weights_used_for_science | false |
| resume_gate.parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| resume_gate.parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| resume_gate.peak_VRAM_bytes | 12443788800 |
| resume_gate.scope | "8 additional verification updates from exact learned parent; weights discarded" |
| candidate_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-2b-20261008/latest.pt" |
| candidate_checkpoint.sha256 | "03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442" |
| parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| control_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| control_checkpoint.sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| counters.update | 212095 |
| counters.supervised_tokens | 2000000000 |
| counters.CE_input_tokens | 2053285089 |
| counters.auxiliary_input_tokens | 0 |
| counters.auxiliary_pairs | 0 |
| counters.physical_input_tokens | 8620194616 |
| counters.original_body_bytes | 8118116484 |
| counters.token_digest | "50452c1e5fccc0928a4b1acce06171b4a869c4251c6efc645348430e6b41d51d" |
| counters.source_teachers.web | 1500000000 |
| counters.source_teachers.textbook | 400000000 |
| counters.source_teachers.story | 100000000 |
| counters.source_EOS.web | 13131989 |
| counters.source_EOS.textbook | 2967040 |
| counters.source_EOS.story | 764589 |
| stream_checks.full_counters | true |
| stream_checks.full_sampler | true |
| stream_checks.full_scheduler | true |
| scientific_cumulative_teacher_tokens | 2000000000 |
| new_scientific_teacher_tokens | 1905839805 |
| reused_control_teacher_tokens | 2000000000 |
| GPU_seconds | 26060.094265680003 |
| GPU_cap_seconds | 37536 |
| prior_pilot_GPU_seconds | 1415.1338874759967 |
| combined_GPU_seconds | 27475.228153156 |
| cumulative_GPU_ledger_closed | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-20261008/train-result.json — complete</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-20261008/train-result.json) ／ SHA256: `18400fae5e9ac30ad96677421800099913a8d0f1812a7fafbc823825c724d986` ／ 20,587 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| binding.parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| binding.checkpoint_ancestry_binding.config_sha256 | "dfd6a6aee8507dcae3f66e3309e3d2ffd4845004f053ad3f07e0eea0829daef0" |
| binding.checkpoint_ancestry_binding.source_binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| binding.checkpoint_ancestry_binding.source_binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| binding.checkpoint_ancestry_binding.source_binding.index_size | 12861257655 |
| binding.checkpoint_ancestry_binding.source_binding.index_mtime_ns | 1791234945567297288 |
| binding.checkpoint_ancestry_binding.source_binding.stream_size | 4000002624 |
| binding.checkpoint_ancestry_binding.source_binding.stream_mtime_ns | 1791234945514053852 |
| binding.checkpoint_ancestry_binding.source_binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| binding.checkpoint_ancestry_binding.source_binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| binding.checkpoint_ancestry_binding.weights_role | "scientific_fresh_teacher_decay_pilot" |
| checkpoint_ancestry_binding.config_sha256 | "dfd6a6aee8507dcae3f66e3309e3d2ffd4845004f053ad3f07e0eea0829daef0" |
| checkpoint_ancestry_binding.source_binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoint_ancestry_binding.source_binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| checkpoint_ancestry_binding.source_binding.index_size | 12861257655 |
| checkpoint_ancestry_binding.source_binding.index_mtime_ns | 1791234945567297288 |
| checkpoint_ancestry_binding.source_binding.stream_size | 4000002624 |
| checkpoint_ancestry_binding.source_binding.stream_mtime_ns | 1791234945514053852 |
| checkpoint_ancestry_binding.source_binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| checkpoint_ancestry_binding.source_binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| checkpoint_ancestry_binding.weights_role | "scientific_fresh_teacher_decay_pilot" |
| parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-2b-20261008/latest.pt" |
| checkpoint_sha256 | "03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442" |
| scientific_CE_teacher_tokens | 2000000000 |
| new_scientific_teacher_tokens | 1905839805 |
| counters.update | 212095 |
| counters.supervised_tokens | 2000000000 |
| counters.CE_input_tokens | 2053285089 |
| counters.auxiliary_input_tokens | 0 |
| counters.auxiliary_pairs | 0 |
| counters.physical_input_tokens | 8620194616 |
| counters.original_body_bytes | 8118116484 |
| counters.token_digest | "50452c1e5fccc0928a4b1acce06171b4a869c4251c6efc645348430e6b41d51d" |
| counters.source_teachers.web | 1500000000 |
| counters.source_teachers.textbook | 400000000 |
| counters.source_teachers.story | 100000000 |
| counters.source_EOS.web | 13131989 |
| counters.source_EOS.textbook | 2967040 |
| counters.source_EOS.story | 764589 |
| sampler.kind | "bounded_original_TRAIN_index_byte_draw_CE_only_genre_quota_windows_v1" |
| sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| sampler.binding.index_size | 12861257655 |
| sampler.binding.index_mtime_ns | 1791234945567297288 |
| sampler.binding.stream_size | 4000002624 |
| sampler.binding.stream_mtime_ns | 1791234945514053852 |
| sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| sampler.seed | 42 |
| sampler.goals.web | 1500000000 |
| sampler.goals.textbook | 400000000 |
| sampler.goals.story | 100000000 |
| sampler.consumed.web | 1500000000 |
| sampler.consumed.textbook | 400000000 |
| sampler.consumed.story | 100000000 |
| sampler.pending.web | [] |
| sampler.pending.textbook | [] |
| sampler.pending.story | [] |
| sampler.draws | 53281196 |
| sampler.documents_drawn | 16863621 |
| sampler.windows_emitted | 16967541 |
| sampler.auxiliary_reasons.CE_only_no_auxiliary_pair_extraction | 16863621 |
| scheduler.tokens | 2000000000 |
| spec.seed | 42 |
| spec.weight_decay.reference_teachers | 32768 |
| spec.weight_decay.parameter_scope | "same_all_native_parameters" |
| spec.residual_policy.physical_block_invocations | 1 |
| lineage.seed | 42 |
| lineage.weight_decay_policy.reference_teachers | 32768 |
| lineage.weight_decay_policy.parameter_scope | "same_all_native_parameters" |
| model_config.status | "phase5_ablation" |
| decay.policy.reference_teachers | 32768 |
| decay.policy.parameter_scope | "same_all_native_parameters" |
| decay.last_update | 212095 |
| decay.last_update_teachers | 2227 |
| stream_checks.full_counters | true |
| stream_checks.full_sampler | true |
| stream_checks.full_scheduler | true |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-launcher-20261008/result.json — complete</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-launcher-20261008/result.json) ／ SHA256: `c03e04a044ee285a886a935ce62517278fecaf6b55856b4a2493fc80773a0788` ／ 199 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-preflight-v1/config.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-preflight-v1/config.json) ／ SHA256: `c9a4c94b6412f4d207d8e808431a4778cfa518d7fe452e1bf38235c4ccdc2bf8` ／ 12,249 bytes

| 原キー | 保存値 |
|---|---|
| pilot_completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_teacher_decay_pilot_completion.json" |
| pilot_completion.sha256 | "4d40b8ca019cb25e9af01958603b12b7122f4b1752fd22c5b85bf7efa149d728" |
| parent_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-pilot-20261008/latest.pt" |
| parent_checkpoint.sha256 | "b7b9808a70ac4e6ca1bfe3751b70fcfa12c292c216ef512b00588a5e75f649ad" |
| parent_counters.update | 10000 |
| parent_counters.supervised_tokens | 94160195 |
| parent_counters.CE_input_tokens | 96655164 |
| parent_counters.auxiliary_input_tokens | 0 |
| parent_counters.auxiliary_pairs | 0 |
| parent_counters.physical_input_tokens | 404673920 |
| parent_counters.original_body_bytes | 382169159 |
| parent_counters.token_digest | "26b260437b751cb63b2e2922659bbac6b6e90adc983cd578626cdb0baf9a3dc4" |
| parent_counters.source_teachers.web | 70620030 |
| parent_counters.source_teachers.textbook | 18832118 |
| parent_counters.source_teachers.story | 4708047 |
| parent_counters.source_EOS.web | 619232 |
| parent_counters.source_EOS.textbook | 139904 |
| parent_counters.source_EOS.story | 35998 |
| checkpoint_binding.config_sha256 | "dfd6a6aee8507dcae3f66e3309e3d2ffd4845004f053ad3f07e0eea0829daef0" |
| checkpoint_binding.source_binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoint_binding.source_binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| checkpoint_binding.source_binding.index_size | 12861257655 |
| checkpoint_binding.source_binding.index_mtime_ns | 1791234945567297288 |
| checkpoint_binding.source_binding.stream_size | 4000002624 |
| checkpoint_binding.source_binding.stream_mtime_ns | 1791234945514053852 |
| checkpoint_binding.source_binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| checkpoint_binding.source_binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| checkpoint_binding.weights_role | "scientific_fresh_teacher_decay_pilot" |
| source_sha256.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| source_sha256.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.scripts/run_base_teacher_decay_pilot.py | "b6f715a3502074e05f005afbeadade509f46ea40bdc1dc660b3658b0269f8dd6" |
| source_sha256.scripts/run_base_teacher_decay_pilot.ps1 | "b04ce0b2a4cdad441556b4d962a4525a5d305a8db8cf2f180d2ddde9cd792020" |
| source_sha256.scripts/base_teacher_decay_trainer.py | "a90a8487ccb73a797d31df29dbaa53b8cf8e85beb3ad4db83ea2a9e4053e5122" |
| source_sha256.tests/test_base_teacher_decay.py | "e30ba067bf794844dc1b4345c265afa0929391d26e625f538a0b60987b29533b" |
| source_sha256.scripts/inspect_base_teacher_decay.py | "2e37fd8b4890a9ac0978457e04432b9e8ffb64e11950ba6b3ecf5999c88fe2d4" |
| source_sha256.scripts/review_base_teacher_decay_pilot.py | "9f9de0db1018c088576900dd073c46580afaf33ae7620ddc0dd77a619979e0db" |
| source_sha256.scripts/review_eos_5b_finish.py | "483d0bd97ebc5130fd7fe3104cfd5f4f4ee8c688b5bd2c8a03108018395eba46" |
| source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| source_sha256.scripts/run_base_teacher_decay_2b.py | "1b623e7872e6c6d2d50d7cb7372de7689508444667c505b17b965c4455bab800" |
| source_sha256.scripts/run_base_teacher_decay_2b.ps1 | "8e7fa1b7e5dfbd4351d19ac981e5b529052c413659ce9858d4b3b01ced654858" |
| source_sha256.scripts/base_teacher_decay_2b_protocol.py | "fdbd649b0133396e5dadc49fbd8baaaec677cbb8db849fcda132395d29ac4e75" |
| source_sha256.scripts/review_base_teacher_decay_2b.py | "d668fc6fd4bc9bdc04e7e40c23bb2c56fcb534bff8f58914bb543f719ca0148a" |
| source_sha256.tests/test_base_teacher_decay_2b.py | "cf43e1b384362ec67ae55785386079cbfcdc368827e3f7cfa21848fe2831c9a0" |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_teacher_decay_2b_tests.xml" |
| CPU_tests.sha256 | "3003a94ba7af591c63d2d14022dbed64c37dea3bcf671b479991543796c67e5d" |
| quality_references.strong_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_order_condition_notes.json" |
| quality_references.strong_notes.sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| quality_references.cached_control_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural_context_contrast_CE_notes.json" |
| quality_references.cached_control_notes.sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| initial_teacher_tokens | 94160195 |
| final_teacher_tokens | 2000000000 |
| new_teacher_tokens | 1905839805 |
| decay_policy.reference_teachers | 32768 |
| decay_policy.parameter_scope | "same_all_native_parameters" |
| GPU_cap_seconds | 37536 |
| prior_pilot_GPU_seconds | 1415.1338874759967 |
| maximum_combined_GPU_seconds | 38951.133887476 |
| expected_worst_peak_bytes | 17791499264 |
| checkpoint_every_updates | 1000 |
| heartbeat_every_updates | 20 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| control_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| control_checkpoint.sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| control_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_sequential_notes.json" |
| control_notes.sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-2b-preflight-v1/failure.json — preflight_failed_before_GPU_then_repaired</summary>

[原記録](../../reports/phase6/base-teacher-decay-2b-preflight-v1/failure.json) ／ SHA256: `5522a54e7a72d4617ecbedb09d5ea384d141994599a1cc69bf0fee014fdcec61` ／ 437 bytes

| 原キー | 保存値 |
|---|---|
| reason | "CPU_tests XML was passed to read_json after successful SHA validation; JSONDecodeError. No science/UI stop/GPU occurred." |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| repair | "Validate frozen reference bytes separately from JSON parsing; keep actual7 CPU checks and scientific recipe/budget unchanged." |
| status | "preflight_failed_before_GPU_then_repaired" |

</details>

<details>
<summary>reports/phase6/base-teacher-decay-launcher-20261008/launcher.json — None</summary>

[原記録](../../reports/phase6/base-teacher-decay-launcher-20261008/launcher.json) ／ SHA256: `1d509d5bef56be727f52baf822f2b894aaad0be694aab0786b50d2a63b31b2c6` ／ 77 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base-teacher-decay-launcher-20261008/result.json — complete</summary>

[原記録](../../reports/phase6/base-teacher-decay-launcher-20261008/result.json) ／ SHA256: `767b2d29f12e358fc8902d7634e37503be09143895066b30e53889d53929d3d2` ／ 199 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base_ademamix_active_job.json — own_probe_complete_scientific100M_active</summary>

[原記録](../../reports/phase6/base_ademamix_active_job.json) ／ SHA256: `f1cf0c2eb8da0b07a2e0a93f416a83f9d42489e31b224d733859568e645e90d5` ／ 4,491 bytes

| 原キー | 保存値 |
|---|---|
| status | "own_probe_complete_scientific100M_active" |
| probe_initial_checks.native_parent_weights | true |
| probe_initial_checks.candidate_control_initial_weights | true |
| probe_initial_checks.global_RNG_equal | true |
| probe_initial_checks.tied_native_vocab | true |
| probe_initial_checks.exact10M_parameters | true |
| probe_initial_checks.all_parameters_once | true |
| probe_initial_checks.fresh_optimizer_empty | true |
| probe_initial_checks.sampler_full_initial_state_equal | true |
| all_resume_and_source_checks.kind | true |
| all_resume_and_source_checks.spec | true |
| all_resume_and_source_checks.binding | true |
| all_resume_and_source_checks.lineage | true |
| all_resume_and_source_checks.model_config | true |
| all_resume_and_source_checks.model | true |
| all_resume_and_source_checks.optimizer | true |
| all_resume_and_source_checks.scheduler | true |
| all_resume_and_source_checks.RNG | true |
| all_resume_and_source_checks.sampler | true |
| all_resume_and_source_checks.counters | true |
| all_resume_and_source_checks.finite_model_and_three_moments | true |
| all_resume_and_source_checks.all_history_except_timing | true |
| all_resume_and_source_checks.same_original_source_digest_masks_EOS | true |
| all_resume_and_source_checks.full_sampler_matches_AdamW | true |
| all_resume_and_source_checks.initial_actual_CE_equal | true |
| capacity.batch | 48 |
| capacity.context | 1024 |
| capacity.teacher_stride | 512 |
| capacity.backward_original_positions | 24576 |
| capacity.peak_VRAM_bytes | 10745063424 |
| capacity.loss | 2.2704575061798096 |
| capacity.gradient_norm | 3.172720432281494 |
| capacity.optimizer_updates | 0 |
| capacity.weights_unchanged | true |
| capacity.optimizer_steps_unchanged | true |
| GPU_probe_seconds | 9.068181484999968 |
| verification_updates | 47 |
| verification_original_gold | 273521 |
| scientific_GPU_cap_seconds | 3199 |
| total_GPU_cap_seconds | 4800 |
| scientific_job_observed.status | "running" |
| scientific_job_observed.pid | 1816 |
| scientific_job_observed.boot_id | "4052bfc5-3850-44e4-9123-d34a9e19f36e" |
| scientific_job_observed.start_ticks | "100189" |
| scientific_job_observed.started_at | "2026-10-07T07:24:00.121495Z" |
| scientific_job_observed.config_sha256 | "e980082d37b82bd13f1ff92376fecd4f706868da4dc5765c4a5249a518b033de" |
| scientific_job_observed.GPU_occupancy_seconds | 59.719619719999855 |
| scientific_job_observed.restart_command | "scripts/run_base_ademamix.ps1 -Worker; inspect PID/boot/start and valid completed checkpoint first; same cumulative budget" |
| scientific_job_observed.Base_complete | false |
| scientific_job_observed.Chat_started | false |
| scientific_job_observed.quantization_started | false |
| scientific_job_observed.memory_policy.torch_version | "2.14.1+cu130" |
| scientific_job_observed.memory_policy.device | "NVIDIA GeForce RTX 4090" |
| scientific_job_observed.memory_policy.visible_device_bytes | 25756696576 |
| scientific_job_observed.memory_policy.process_fraction | 0.8999999999844701 |
| scientific_job_observed.memory_policy.allocator_allowance_bytes | 23181026918 |
| scientific_job_observed.memory_policy.expected_worst_peak_bytes | 10745063424 |
| scientific_job_observed.stage | "ademamix-training" |
| scientific_job_observed.heartbeat_at | "2026-10-07T07:25:01.120840Z" |
| scientific_job_observed.completed_updates | 540 |
| scientific_job_observed.original_teachers | 3056829 |
| scientific_job_observed.CE_loss | 2.7199888229370117 |
| scientific_job_observed.latest_checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-ademamix-comparison-20261007/ademamix/checkpoint-00000500.pt" |
| CPU_checks.optimizer_trainer | 16 |
| CPU_checks.workflow | 12 |
| initial_CPU_failure | "Budget test fixture2.6seconds/100000gold incorrectly expected3500; corrected fixture to2.0seconds. Original prospective formula/caps/quality thresholds unchanged; run forecast now uses identical direct probe arithmetic." |
| new_unique_dataset_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| old_FFN_and_MHA_caps_remain_closed | true |

</details>

<details>
<summary>reports/phase6/base_ademamix_comparison_completion.json — AdEMAMix100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_ademamix_comparison_completion.json) ／ SHA256: `dfb2fabb821a3a181ebdcb63807a06e8630bbd9448ca77d8994c1163206c8302` ／ 5,917 bytes

| 原キー | 保存値 |
|---|---|
| status | "AdEMAMix100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_updates | 17698 |
| GPU_occupancy_seconds | 1866.8568215459998 |
| GPU_cap_seconds | 3199 |
| probe_GPU_seconds | 9.068181484999968 |
| total_GPU_seconds_including_probe | 1875.9250030309997 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-ademamix-comparison-20261007/ademamix/checkpoint-00017698.pt" |
| checkpoint_sha256 | "a96c73161e006a64a48477eed32fc990a2664a4f3f1f844fc3ebbe63c63d88e6" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_ademamix_notes.json" |
| notes.sha256 | "2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73" |
| reused_control_GPU_seconds | 0 |
| summaries.ademamix.BPB | 1.0756096504846635 |
| summaries.ademamix.rates.eos | 13 |
| summaries.ademamix.rates.repetition | 46 |
| summaries.ademamix.rates.unicode_failure | 0 |
| summaries.ademamix.rates.role_leak | 0 |
| summaries.ademamix.rates.empty | 0 |
| summaries.ademamix.grammar2 | 18 |
| summaries.ademamix.relevance2 | 23 |
| summaries.ademamix.coherent | 1 |
| summaries.ademamix.appropriate | 3 |
| summaries.ademamix.notes_sha256 | "2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73" |
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
| eligible_for_final_Base_validation | false |
| fixed_AdEMAMix_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 107102576 |
| archive.compressed_bundle.bytes | 45755220 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_ademamix_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_ademamix_comparison_evidence_manifest.json) ／ SHA256: `095680340dc20014a4a8b9dc6fe8deaae29f1452b2977496efb0dd2cbebcd84b` ／ 14,104 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_ademamix_comparison_review.json — AdEMAMix_native100M_and_all80_reviewed</summary>

[原記録](../../reports/phase6/base_ademamix_comparison_review.json) ／ SHA256: `e9a01c191f5f410ee38778f841323d8b3ba6f73a8b6c13fc70c37e3a55092369` ／ 4,383 bytes

| 原キー | 保存値 |
|---|---|
| status | "AdEMAMix_native100M_and_all80_reviewed" |
| summaries.ademamix.BPB | 1.0756096504846635 |
| summaries.ademamix.rates.eos | 13 |
| summaries.ademamix.rates.repetition | 46 |
| summaries.ademamix.rates.unicode_failure | 0 |
| summaries.ademamix.rates.role_leak | 0 |
| summaries.ademamix.rates.empty | 0 |
| summaries.ademamix.grammar2 | 18 |
| summaries.ademamix.relevance2 | 23 |
| summaries.ademamix.coherent | 1 |
| summaries.ademamix.appropriate | 3 |
| summaries.ademamix.notes_sha256 | "2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73" |
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
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | false |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
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
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| scientific_CE_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| GPU_seconds | 1866.8568215459998 |
| probe_GPU_seconds | 9.068181484999968 |
| notes_sha256 | "2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single seed and mature-parent optimizer transition; repeated nonblind DEV; heuristic update RMS and compute differ. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required." |

</details>

<details>
<summary>reports/phase6/base_ademamix_notes.json — None</summary>

[原記録](../../reports/phase6/base_ademamix_notes.json) ／ SHA256: `2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73` ／ 20,106 bytes

| 原キー | 保存値 |
|---|---|
| limitations | "Repeated fixed DEV and subjective Codex review; no independent human or blind evaluation. Exact historical id/prefix/text/stop matches retain the prospectively fixed first-reference scores." |

</details>

<details>
<summary>reports/phase6/base_ademamix_proposal.json — prospective_new_dual_gradient_EMA_comparison</summary>

[原記録](../../reports/phase6/base_ademamix_proposal.json) ／ SHA256: `b6869908e6a1ac4156993f30f7980c27b75a40b67dbd0d52394c19d59075a750` ／ 6,458 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_new_dual_gradient_EMA_comparison" |
| evidence_scope | "Paper section3/Algorithm1/A.1 and official implementation specify corrected fast EMA, uncorrected slow EMA and second-moment denominator. Other models/data report slower forgetting. This does not prove Japanese10M improvement or2x GPU speed." |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| optimizer.alpha_warmup_updates | 1000 |
| optimizer.beta3_half_life_warmup_updates | 1000 |
| optimizer.slow_EMA_bias_correction | false |
| optimizer.fast_EMA_bias_correction | true |
| seed | 42 |
| original_gold_tokens | 100000000 |
| new_unique_dataset_tokens | 0 |
| accepted_data_rescan | false |
| resource.CPU_proposal_cap_seconds | 30 |
| resource.probe_GPU_cap_seconds | 180 |
| resource.total_GPU_cap_seconds | 4800 |
| resource.warmup_updates | 3 |
| resource.timed_updates | 32 |
| failure | "One exact recipe; no alpha/beta/warmup/LR/WD/parent/data/teacher/batch/precision/backend/decoder/cap rescue, automatic extension or reopening closed FFN/MHA." |
| limitations | "One conservative-LR mature-parent transition, one seed/repeated nonblind DEV. Slow memory changes direction and magnitude; not isolated equal-norm updates or causal forgetting proof. No new source/data, Chat or quantization." |
| historical_evidence.base_completed_objective_studies_v3_20261007.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_completed_objective_studies_v3_20261007.json" |
| historical_evidence.base_completed_objective_studies_v3_20261007.json.sha256 | "716b4ef75300e630d76467e75146734777dfd31c8023fb2449548ffb0f1f7252" |
| historical_evidence.base_muon_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_muon_comparison_completion.json" |
| historical_evidence.base_muon_comparison_completion.json.sha256 | "cfa43645b777d9dd5e685cfbce25e4175278c5aeec9d91a2033a3ba82e94cbad" |
| historical_evidence.base_sam_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sam_comparison_completion.json" |
| historical_evidence.base_sam_comparison_completion.json.sha256 | "2f31f34c1235d3f13589e54c44fe695e748d63a11af1103c249de2fd44e28693" |
| historical_evidence.base_storage_reader_completion_20261007.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_storage_reader_completion_20261007.json" |
| historical_evidence.base_storage_reader_completion_20261007.json.sha256 | "1820f5391a56a1bbf5d73e6e1f4bb45626a0357a061e77a371d348841a220046" |
| new_GPU_seconds | 0 |
| new_scientific_gold_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_ademamix_rating_reuse.json — None</summary>

[原記録](../../reports/phase6/base_ademamix_rating_reuse.json) ／ SHA256: `6bde5a49c5d6172b759e1af209b6196edc287d6c135f5437c59ef959de1393df` ／ 6,419 bytes

| 原キー | 保存値 |
|---|---|
| candidate_notes_sha256 | "2bac110624e58a0cf8cbb0a8cfdd7e917b8b74cbd3ffbb7ada19a9916f717d73" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| scope | "Exact textual rating lineage after all80 reading, not independent human/blind or new quality evaluation." |

</details>

<details>
<summary>reports/phase6/base_completed_objective_studies_20261007.json — five_completed_same_gold_objective_conditions_quality_rejected</summary>

[原記録](../../reports/phase6/base_completed_objective_studies_20261007.json) ／ SHA256: `6fcf7bc7b038e5a33f39d77b6c8bf3c8f1798362bb702ea83cccbfa341b4ee9a` ／ 8,898 bytes

| 原キー | 保存値 |
|---|---|
| status | "five_completed_same_gold_objective_conditions_quality_rejected" |
| cached_CE.BPB | 0.998487162513845 |
| cached_CE.rates.eos | 19 |
| cached_CE.rates.repetition | 45 |
| cached_CE.rates.unicode_failure | 0 |
| cached_CE.rates.role_leak | 0 |
| cached_CE.rates.empty | 0 |
| cached_CE.grammar2 | 44 |
| cached_CE.relevance2 | 25 |
| cached_CE.coherent | 2 |
| cached_CE.appropriate | 2 |
| cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| strong_staged.BPB | 1.1336128657420816 |
| strong_staged.rates.eos | 76 |
| strong_staged.rates.repetition | 2 |
| strong_staged.rates.unicode_failure | 0 |
| strong_staged.rates.role_leak | 0 |
| strong_staged.rates.empty | 0 |
| strong_staged.grammar2 | 65 |
| strong_staged.relevance2 | 39 |
| strong_staged.coherent | 23 |
| strong_staged.appropriate | 26 |
| strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| native_KD_matched_effect.EOS | [19, 46] |
| native_KD_matched_effect.repetition | [45, 25] |
| native_KD_matched_effect.coherent | [2, 5] |
| native_KD_matched_effect.appropriate | [2, 7] |
| native_KD_matched_effect.paired_coherence_CI95 | [-0.0125, 0.1] |
| native_KD_matched_effect.coherence_improvement_proven | false |
| new_unique_dataset_tokens | 0 |
| dataset_scope | "Same accepted2B pool and matched original100M hard-gold stream per condition;500M counts repeated learning exposure, not new unique data. SAM second-pass, middle and entropy positions, on-policy sampled-context KL and dense short25M KL are separately defined compute/supervision, not interchangeable new hard labels." |
| current_condition_closed | true |
| old_dense_KD3600_budget_failure_preserved | true |
| old_compiler_numeric_failure_preserved | true |
| new_GPU_seconds | 0 |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_completed_objective_studies_v2_20261007.json — six_completed_same_gold_objective_conditions_quality_rejected</summary>

[原記録](../../reports/phase6/base_completed_objective_studies_v2_20261007.json) ／ SHA256: `37335ff5e0c06335569336c7c3dfbef7ccd71d6321a0c891e6e753f254f03771` ／ 12,121 bytes

| 原キー | 保存値 |
|---|---|
| status | "six_completed_same_gold_objective_conditions_quality_rejected" |
| cached_CE.BPB | 0.998487162513845 |
| cached_CE.rates.eos | 19 |
| cached_CE.rates.repetition | 45 |
| cached_CE.rates.unicode_failure | 0 |
| cached_CE.rates.role_leak | 0 |
| cached_CE.rates.empty | 0 |
| cached_CE.grammar2 | 44 |
| cached_CE.relevance2 | 25 |
| cached_CE.coherent | 2 |
| cached_CE.appropriate | 2 |
| cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| strong_staged.BPB | 1.1336128657420816 |
| strong_staged.rates.eos | 76 |
| strong_staged.rates.repetition | 2 |
| strong_staged.rates.unicode_failure | 0 |
| strong_staged.rates.role_leak | 0 |
| strong_staged.rates.empty | 0 |
| strong_staged.grammar2 | 65 |
| strong_staged.relevance2 | 39 |
| strong_staged.coherent | 23 |
| strong_staged.appropriate | 26 |
| strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| new_unique_dataset_tokens | 0 |
| dataset_scope | "Same matched100M stream repeated in six conditions; separately defined auxiliary positions are not interchangeable new corpus or hard labels." |
| old_resource_failures_preserved | true |
| output_KD_stop_and_repetition_effect_preserved | true |
| new_GPU_seconds | 0 |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_completed_objective_studies_v3_20261007.json — seven_completed_same_gold_conditions_quality_rejected</summary>

[原記録](../../reports/phase6/base_completed_objective_studies_v3_20261007.json) ／ SHA256: `716b4ef75300e630d76467e75146734777dfd31c8023fb2449548ffb0f1f7252` ／ 13,709 bytes

| 原キー | 保存値 |
|---|---|
| status | "seven_completed_same_gold_conditions_quality_rejected" |
| cached_CE.BPB | 0.998487162513845 |
| cached_CE.rates.eos | 19 |
| cached_CE.rates.repetition | 45 |
| cached_CE.rates.unicode_failure | 0 |
| cached_CE.rates.role_leak | 0 |
| cached_CE.rates.empty | 0 |
| cached_CE.grammar2 | 44 |
| cached_CE.relevance2 | 25 |
| cached_CE.coherent | 2 |
| cached_CE.appropriate | 2 |
| cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| strong_staged.BPB | 1.1336128657420816 |
| strong_staged.rates.eos | 76 |
| strong_staged.rates.repetition | 2 |
| strong_staged.rates.unicode_failure | 0 |
| strong_staged.rates.role_leak | 0 |
| strong_staged.rates.empty | 0 |
| strong_staged.grammar2 | 65 |
| strong_staged.relevance2 | 39 |
| strong_staged.coherent | 23 |
| strong_staged.appropriate | 26 |
| strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| new_unique_dataset_tokens | 0 |
| dataset_scope | "Same matched100M stream used in seven conditions; separate auxiliary positions and linked evaluations are not new unique corpus or additional hard labels." |
| old_resource_failures_preserved | true |
| output_KD_stop_and_repetition_effect_preserved | true |
| new_GPU_seconds | 0 |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_comparison_completion.json — confidence100M_review_complete_rejected</summary>

[原記録](../../reports/phase6/base_confidence_penalty_comparison_completion.json) ／ SHA256: `9b60041cb33f9d1ee1c84e16d66e7a8bae0727868cbe73460778247834692d6d` ／ 5,878 bytes

| 原キー | 保存値 |
|---|---|
| status | "confidence100M_review_complete_rejected" |
| scientific_CE_teacher_tokens | 100000000 |
| scientific_updates | 17698 |
| scientific_confidence_positions | 100000000 |
| confidence_penalty.updates | 17698 |
| GPU_occupancy_seconds | 1485.7340487600013 |
| GPU_cap_seconds | 3916 |
| probe_GPU_seconds | 9.44069278097595 |
| total_GPU_seconds_including_probe | 1495.1747415409773 |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-confidence-penalty-comparison-20261007/confidence_penalty/checkpoint-00017698.pt" |
| checkpoint_sha256 | "f541c96d0f941aaf05dcfb48554fd905206aafa900686b3900833821a7c47fc1" |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_confidence_penalty_notes.json" |
| notes.sha256 | "bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82" |
| reused_control_GPU_seconds | 0 |
| summaries.confidence_penalty.BPB | 1.0066673599304765 |
| summaries.confidence_penalty.rates.eos | 16 |
| summaries.confidence_penalty.rates.repetition | 50 |
| summaries.confidence_penalty.rates.unicode_failure | 0 |
| summaries.confidence_penalty.rates.role_leak | 0 |
| summaries.confidence_penalty.rates.empty | 0 |
| summaries.confidence_penalty.grammar2 | 33 |
| summaries.confidence_penalty.relevance2 | 28 |
| summaries.confidence_penalty.coherent | 1 |
| summaries.confidence_penalty.appropriate | 2 |
| summaries.confidence_penalty.notes_sha256 | "bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82" |
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
| eligible_for_final_Base_validation | false |
| fixed_confidence_condition_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 102986654 |
| archive.compressed_bundle.bytes | 45925354 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| final_seed_full_dev_test_adoption_pending | true |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_comparison_evidence_manifest.json) ／ SHA256: `0e81c0a2caa38dbc7286f4f73a66c34801433fa8d951efb61256527e76e1aa18` ／ 10,374 bytes

| 原キー | 保存値 |
|---|---|
| full_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_comparison_review.json — confidence_penalty_native100M_and_all80_reviewed</summary>

[原記録](../../reports/phase6/base_confidence_penalty_comparison_review.json) ／ SHA256: `d3c81695c97340feff659d4f00447d0b85eedb0175bcefb6959bcd7915176e22` ／ 4,568 bytes

| 原キー | 保存値 |
|---|---|
| status | "confidence_penalty_native100M_and_all80_reviewed" |
| summaries.confidence_penalty.BPB | 1.0066673599304765 |
| summaries.confidence_penalty.rates.eos | 16 |
| summaries.confidence_penalty.rates.repetition | 50 |
| summaries.confidence_penalty.rates.unicode_failure | 0 |
| summaries.confidence_penalty.rates.role_leak | 0 |
| summaries.confidence_penalty.rates.empty | 0 |
| summaries.confidence_penalty.grammar2 | 33 |
| summaries.confidence_penalty.relevance2 | 28 |
| summaries.confidence_penalty.coherent | 1 |
| summaries.confidence_penalty.appropriate | 2 |
| summaries.confidence_penalty.notes_sha256 | "bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82" |
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
| matched_objective_quality.checks.coherence_gain_at_least8 | false |
| matched_objective_quality.checks.paired_CI_lower_above0 | false |
| matched_objective_quality.checks.EOS_nonworsening | false |
| matched_objective_quality.checks.repetition_nonworsening | false |
| matched_objective_quality.checks.no_empty_role_unicode | true |
| matched_objective_quality.checks.BPB_gate | false |
| matched_objective_quality.checks.appropriate_completion_not_punctuation | true |
| matched_objective_quality.passed | false |
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
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| scientific_CE_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| GPU_seconds | 1485.7340487600013 |
| probe_GPU_seconds | 9.44069278097595 |
| confidence_penalty.updates | 17698 |
| scientific_confidence_positions | 100000000 |
| notes_sha256 | "bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single seed and mature-parent confidence-loss transition; repeated nonblind DEV; prediction entropy regularization differs; same hard gold and native head. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required." |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_notes.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_notes.json) ／ SHA256: `bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82` ／ 18,688 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_probe_launch.json — actual_confidence_CUDA_gate_passed_native100M_science_live</summary>

[原記録](../../reports/phase6/base_confidence_penalty_probe_launch.json) ／ SHA256: `33ca3175c194402976f438afca2823f9f82495b96f0f05fb111c16d8ed6598a6` ／ 4,113 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_confidence_CUDA_gate_passed_native100M_science_live" |
| scientific_actual_identity.pid | 729058 |
| scientific_actual_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| scientific_actual_identity.start_ticks | "22794332" |
| scientific_config_sha256 | "a9035f846eedbb8355e362d0b944ce24c81410d883290e0fffb42b72ba9df069" |
| probe_GPU_seconds | 9.44069278097595 |
| scientific_GPU_cap_seconds | 3916 |
| total_GPU_cap_seconds | 4800 |
| initial_checks.native_parent_weights | true |
| initial_checks.tied_native_vocab | true |
| initial_checks.native_parameters | true |
| initial_checks.all_parameters_once | true |
| resume_and_source_checks.kind | true |
| resume_and_source_checks.spec | true |
| resume_and_source_checks.binding | true |
| resume_and_source_checks.lineage | true |
| resume_and_source_checks.model_config | true |
| resume_and_source_checks.model | true |
| resume_and_source_checks.optimizer | true |
| resume_and_source_checks.scheduler | true |
| resume_and_source_checks.RNG | true |
| resume_and_source_checks.sampler | true |
| resume_and_source_checks.counters | true |
| resume_and_source_checks.confidence_penalty | true |
| resume_and_source_checks.finite_hybrid_model_buffers | true |
| resume_and_source_checks.history_except_timing | true |
| resume_and_source_checks.same_original_stream | true |
| resume_and_source_checks.full_sampler_matches_AdamW | true |
| capacity.context | 1024 |
| capacity.target_stride | 512 |
| capacity.batch | 48 |
| capacity.original_target_positions | 24576 |
| capacity.confidence_positions | 24576 |
| capacity.peak_VRAM_bytes | 11913217024 |
| capacity.optimizer_updates | 0 |
| capacity.unchanged_weights | true |
| capacity.CE_loss | 2.2709779739379883 |
| capacity.confidence_KL_loss | 5.815214157104492 |
| capacity.prediction_entropy | 2.502552032470703 |
| capacity.combined_loss | 2.852499485015869 |
| capacity.gradient_norm | 3.103583574295044 |
| capacity.decoder_forwards | 1 |
| verification_updates | 47 |
| verification_original_teacher_positions | 273521 |
| verification_confidence_positions | 250313 |
| exact_planned_completed_updates | 17698 |
| scientific_original_teacher_positions | 100000000 |
| scientific_confidence_positions | 100000000 |
| cached_control_GPU_repeated | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_probe_launch_archive.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_probe_launch_archive.json) ／ SHA256: `ac1c0d8fbefef5e4d5856289e4e41bd6b4ab2114f7ecb96a7218fc9f909f6d08` ／ 341 bytes

| 原キー | 保存値 |
|---|---|
| archive.bytes | 160911 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_probe_launch_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_probe_launch_evidence_manifest.json) ／ SHA256: `bac739aad61025d92eb52cbd032ec387fd7562fc99773ef388a43fd447d2ccf7` ／ 3,844 bytes

| 原キー | 保存値 |
|---|---|
| probe_checkpoints_preserved_native | true |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_proposal.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_proposal.json) ／ SHA256: `5f3101313e1c1cc2c0e7cf3a1d8ff438316892100e0886028f96dfbd902f2276` ／ 6,356 bytes

| 原キー | 保存値 |
|---|---|
| references.base_failure_route_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_failure_route_synthesis.json" |
| references.base_failure_route_synthesis.json.sha256 | "2384411b47272b53b9e4eda981a69ff67e335069ca125a43e551c892515826b2" |
| references.base_recent_objective_failure_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_recent_objective_failure_synthesis.json" |
| references.base_recent_objective_failure_synthesis.json.sha256 | "fac67855f7e041d18aaf9d8055a9829587a72a61f7d14019704c8c404ceb4133" |
| references.base_middle_supervision_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_middle_supervision_comparison_completion.json" |
| references.base_middle_supervision_comparison_completion.json.sha256 | "4829d93b24a02a3ded203258887a06934d067f285ee9a4326333dfc1ef8a1975" |
| references.base_label_smoothing_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_label_smoothing_comparison_completion.json" |
| references.base_label_smoothing_comparison_completion.json.sha256 | "9a5904a9db1398667e24aec1f578c0aa6587c3ee107dd789638f33ff4aeee6c5" |
| references.base_sam_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_sam_comparison_completion.json" |
| references.base_sam_comparison_completion.json.sha256 | "2f31f34c1235d3f13589e54c44fe695e748d63a11af1103c249de2fd44e28693" |
| references.base_on_policy_teacher_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_on_policy_teacher_comparison_completion.json" |
| references.base_on_policy_teacher_comparison_completion.json.sha256 | "022131b4a404867cc07ec69876ea069dfed03c91cafc8f96a33b1d96d834bfa5" |
| literature_limit | "Pereyra et al.2017 sections3/3.2 motivate negative entropy and reversed uniform KL; Penn Treebank language-model experiments are not Japanese10M continuation evidence or an exact reproduction. Coefficient0.1 is one fixed conservative exploratory choice, not an asserted literature optimum. Calibration has not been proven the cause; at a saturated delta the entropy-only gradient also vanishes." |
| recipe.loss | "original_mean_CE_plus_0.1_times_log_vocab_minus_mean_prediction_entropy" |
| seed | 42 |
| original_teachers | 100000000 |
| new_unique_dataset_tokens | 0 |
| control_reused_GPU_seconds | 0 |
| total_GPU_cap_seconds | 4800 |
| probe_GPU_cap_seconds | 180 |
| CPU_checks.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_confidence_penalty_trainer_tests.xml" |
| CPU_checks.sha256 | "9a72813cf3c179175d3690401ab49e62fb1b6e6090ae0f4082b793362bc15ca8" |
| acceptance | "Independent analytic CE/KL/logit-gradient/sign/mask/bounds/shift tests; native final CE/gradient parity; full state and original source/save-resume. Actual CUDA4 vs2+2 and all48x1024 finite backward/memory;32 actual postwarmup times, exact17698-update mean forecast*1.3+900 plus actual probe&lt;=4800. Reuse cachedCE and require fullstream/sampler; commonDEV256/Japanese192,331,1119/all80 and unchanged matched/strong/absolute/historicalWeb gates. Only a qualified candidate gets independent trainedseed/fullDEV/protected finalTEST/adoption." |
| failure | "Close this fixed condition on numeric/state/stream/budget or quality failure. No coefficient/temperature/annealing/threshold/LR/parent/data/batch/decoder/cap rescue or automatic extension." |
| limitations | "One conservative-LR mature-parent transition and repeatedly used nonblind DEV. Entropy regularization can worsen hard-gold prediction and EOS. Failure does not prove all entropy objectives, different data or learning amounts ineffective." |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_rating_reuse.json — None</summary>

[原記録](../../reports/phase6/base_confidence_penalty_rating_reuse.json) ／ SHA256: `5cee84e3f8692be5013650b9c049b623fcaea861d8e957b3df4a167bb615f168` ／ 16,013 bytes

| 原キー | 保存値 |
|---|---|
| candidate_notes_sha256 | "bdfba89dc6e344e0fc63c93e15cf64233f7775d40bf15046394d9e1236f00b82" |
| historical_notes_changed | false |
| GPU_seconds | 0 |
| scope | "Mechanical exact id/prefix/text/stop and score audit after current80 reading; not new human or blind ratings." |

</details>

<details>
<summary>reports/phase6/base_confidence_penalty_science_launch_snapshot.json — running</summary>

[原記録](../../reports/phase6/base_confidence_penalty_science_launch_snapshot.json) ／ SHA256: `99334311a8e3b30fbc7dc48b97e3ddb05b73a155448c3a535320a8e0ef957934` ／ 1,008 bytes

| 原キー | 保存値 |
|---|---|
| status | "running" |
| GPU_occupancy_seconds | 21.09037987299962 |
| Base_complete | false |
| memory_policy.visible_device_bytes | 25756696576 |
| memory_policy.allocator_allowance_bytes | 23181026918 |
| memory_policy.expected_worst_peak_bytes | 11913217024 |
| completed_updates | 220 |
| original_teachers | 1242231 |
| CE_loss | 2.55314302444458 |

</details>

<details>
<summary>reports/phase6/base_current_objective_evidence.json — four_actual_quality_rejections_and_one_never_trained_KD_effect_distinguished</summary>

[原記録](../../reports/phase6/base_current_objective_evidence.json) ／ SHA256: `1c313018ffdfd5147cc30f53b2af4de48dca740302d8dbd043b2c7c5234d2267` ／ 9,216 bytes

| 原キー | 保存値 |
|---|---|
| status | "four_actual_quality_rejections_and_one_never_trained_KD_effect_distinguished" |
| cached_control.BPB | 0.998487162513845 |
| cached_control.rates.eos | 19 |
| cached_control.rates.repetition | 45 |
| cached_control.rates.unicode_failure | 0 |
| cached_control.rates.role_leak | 0 |
| cached_control.rates.empty | 0 |
| cached_control.grammar2 | 44 |
| cached_control.relevance2 | 25 |
| cached_control.coherent | 2 |
| cached_control.appropriate | 2 |
| cached_control.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| untrained_native_KD.completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_native_teacher_KD_probe_completion.json" |
| untrained_native_KD.completion.sha256 | "2672f10105a206c9965fdeda98d260444487dec643c58c04957db247d6662dbe" |
| untrained_native_KD.scientific_gold_positions | 0 |
| untrained_native_KD.old3600_budget_closed | true |
| untrained_native_KD.exact17698_mean32_forecast_seconds | 4489 |
| untrained_native_KD.mean32_step_seconds | 0.15595599255902926 |
| untrained_native_KD.actual_old_probe_seconds | 12.28218039200874 |
| GPU_seconds | 0 |
| CPU_seconds | 0.0063947449962142855 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_embedding_gradient_completion.json — readonly_tied_gradient_diagnostic_complete_screen_not_passed</summary>

[原記録](../../reports/phase6/base_embedding_gradient_completion.json) ／ SHA256: `1fd5cae17e1116c87c52db5f68dd3b85d76e538c9268ae17b872801ec2923cf7` ／ 22,787 bytes

| 原キー | 保存値 |
|---|---|
| status | "readonly_tied_gradient_diagnostic_complete_screen_not_passed" |
| actual_endpoints.parent.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| actual_endpoints.parent.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| actual_endpoints.parent.sources.web.EOS_input_norm | 0.0 |
| actual_endpoints.parent.sources.web.EOS_output_norm | 0.23293847177678895 |
| actual_endpoints.parent.sources.web.teachers | 849 |
| actual_endpoints.parent.sources.web.documents | 8 |
| actual_endpoints.parent.sources.textbook.EOS_input_norm | 0.0 |
| actual_endpoints.parent.sources.textbook.EOS_output_norm | 0.1934559040218081 |
| actual_endpoints.parent.sources.textbook.teachers | 856 |
| actual_endpoints.parent.sources.textbook.documents | 8 |
| actual_endpoints.parent.sources.story.EOS_input_norm | 0.0 |
| actual_endpoints.parent.sources.story.EOS_output_norm | 0.2093909763187799 |
| actual_endpoints.parent.sources.story.teachers | 827 |
| actual_endpoints.parent.sources.story.documents | 8 |
| actual_endpoints.parent.native_checks.weights_unchanged | true |
| actual_endpoints.parent.native_checks.native_tied | true |
| actual_endpoints.parent.native_checks.RNG_unchanged | true |
| actual_endpoints.parent.native_checks.no_accumulated_grads | true |
| actual_endpoints.parent.native_checks.all_fixed_rows_measured | true |
| actual_endpoints.parent.screen.passed | false |
| actual_endpoints.CE100M.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| actual_endpoints.CE100M.checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| actual_endpoints.CE100M.sources.web.EOS_input_norm | 0.0 |
| actual_endpoints.CE100M.sources.web.EOS_output_norm | 0.03588022623771083 |
| actual_endpoints.CE100M.sources.web.teachers | 849 |
| actual_endpoints.CE100M.sources.web.documents | 8 |
| actual_endpoints.CE100M.sources.textbook.EOS_input_norm | 0.0 |
| actual_endpoints.CE100M.sources.textbook.EOS_output_norm | 0.026375805830898345 |
| actual_endpoints.CE100M.sources.textbook.teachers | 856 |
| actual_endpoints.CE100M.sources.textbook.documents | 8 |
| actual_endpoints.CE100M.sources.story.EOS_input_norm | 0.0 |
| actual_endpoints.CE100M.sources.story.EOS_output_norm | 0.03746095435634992 |
| actual_endpoints.CE100M.sources.story.teachers | 827 |
| actual_endpoints.CE100M.sources.story.documents | 8 |
| actual_endpoints.CE100M.native_checks.weights_unchanged | true |
| actual_endpoints.CE100M.native_checks.native_tied | true |
| actual_endpoints.CE100M.native_checks.RNG_unchanged | true |
| actual_endpoints.CE100M.native_checks.no_accumulated_grads | true |
| actual_endpoints.CE100M.native_checks.all_fixed_rows_measured | true |
| actual_endpoints.CE100M.screen.passed | false |
| GPU_occupancy_seconds | 2.030721627001185 |
| GPU_limit_seconds | 180 |
| scientific_CE_teacher_tokens | 0 |
| optimizer_updates | 0 |
| new_original_training_tokens | 0 |
| fixed_diagnostic_closed | true |
| no_projection_or_untying_training_from_this_hypothesis | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 824456 |
| archive.compressed_bundle.bytes | 256763 |
| interpretation | "Global input/output path cosines in the fixed source aggregates lie near zero. Negative dots for many individual vocabulary rows do not establish dominant global cancellation; cancellation ratio alone also falls below1 for orthogonal gradients. This local TRAIN sample does not prove that tying cannot matter elsewhere or that any architecture is sufficient." |

</details>

<details>
<summary>reports/phase6/base_embedding_gradient_launcher_result.json — complete</summary>

[原記録](../../reports/phase6/base_embedding_gradient_launcher_result.json) ／ SHA256: `13838bb224f80d27326406e3b3b0b1e0209bf0704287312cd1af9f14772534ec` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base_embedding_gradient_payload.json — None</summary>

[原記録](../../reports/phase6/base_embedding_gradient_payload.json) ／ SHA256: `4b592ba9e5ec64a664b249b07ade7dd4763db1e3e93a14c2a421a4efa2f23671` ／ 87,081 bytes

| 原キー | 保存値 |
|---|---|
| seed | 2026100741 |

</details>

<details>
<summary>reports/phase6/base_embedding_gradient_result.json — complete</summary>

[原記録](../../reports/phase6/base_embedding_gradient_result.json) ／ SHA256: `29241c5f960770bb765b4c792c923e9c0882e2de953fc06da8228db7895e1f8f` ／ 21,017 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| endpoints.parent.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| endpoints.parent.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| endpoints.parent.sources.web.EOS_input_norm | 0.0 |
| endpoints.parent.sources.web.EOS_output_norm | 0.23293847177678895 |
| endpoints.parent.sources.web.teachers | 849 |
| endpoints.parent.sources.web.documents | 8 |
| endpoints.parent.sources.textbook.EOS_input_norm | 0.0 |
| endpoints.parent.sources.textbook.EOS_output_norm | 0.1934559040218081 |
| endpoints.parent.sources.textbook.teachers | 856 |
| endpoints.parent.sources.textbook.documents | 8 |
| endpoints.parent.sources.story.EOS_input_norm | 0.0 |
| endpoints.parent.sources.story.EOS_output_norm | 0.2093909763187799 |
| endpoints.parent.sources.story.teachers | 827 |
| endpoints.parent.sources.story.documents | 8 |
| endpoints.parent.native_checks.weights_unchanged | true |
| endpoints.parent.native_checks.native_tied | true |
| endpoints.parent.native_checks.RNG_unchanged | true |
| endpoints.parent.native_checks.no_accumulated_grads | true |
| endpoints.parent.native_checks.all_fixed_rows_measured | true |
| endpoints.parent.screen.passed | false |
| endpoints.CE100M.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/natural-context-contrast-comparison-20261007/CE/checkpoint-00017698.pt" |
| endpoints.CE100M.checkpoint.sha256 | "f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967" |
| endpoints.CE100M.sources.web.EOS_input_norm | 0.0 |
| endpoints.CE100M.sources.web.EOS_output_norm | 0.03588022623771083 |
| endpoints.CE100M.sources.web.teachers | 849 |
| endpoints.CE100M.sources.web.documents | 8 |
| endpoints.CE100M.sources.textbook.EOS_input_norm | 0.0 |
| endpoints.CE100M.sources.textbook.EOS_output_norm | 0.026375805830898345 |
| endpoints.CE100M.sources.textbook.teachers | 856 |
| endpoints.CE100M.sources.textbook.documents | 8 |
| endpoints.CE100M.sources.story.EOS_input_norm | 0.0 |
| endpoints.CE100M.sources.story.EOS_output_norm | 0.03746095435634992 |
| endpoints.CE100M.sources.story.teachers | 827 |
| endpoints.CE100M.sources.story.documents | 8 |
| endpoints.CE100M.native_checks.weights_unchanged | true |
| endpoints.CE100M.native_checks.native_tied | true |
| endpoints.CE100M.native_checks.RNG_unchanged | true |
| endpoints.CE100M.native_checks.no_accumulated_grads | true |
| endpoints.CE100M.native_checks.all_fixed_rows_measured | true |
| endpoints.CE100M.screen.passed | false |
| GPU_occupancy_seconds | 2.030721627001185 |
| peak_allocated_bytes | 540574208 |
| optimizer_updates | 0 |
| scientific_CE_teachers | 0 |
| new_original_training_tokens | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| fixed_diagnostic_closed | true |
| limitations | "Only8 distinct TRAIN families per source, index-byte biased first/last windows, two reused endpoints. Gradient-path statistics are local teacher-forcing diagnostics, not causal proof, independent generation generalization or new Base-quality evidence. Both forwards use FP32 math, not the scientific BF16 flash path." |

</details>
