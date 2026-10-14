# 構成・反復計算・容量 — 3/7

[分野一覧へ](05_architecture.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/base_parallel_residual_comparison_result.json — complete</summary>

[原記録](../../reports/phase6/base_parallel_residual_comparison_result.json) ／ SHA256: `4c6f9057c685450ee32eafedcd64538676f868022a81317fb7d3d584edfe3f2a` ／ 606,836 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| results.sequential.training.status | "complete" |
| results.sequential.training.binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| results.sequential.training.binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| results.sequential.training.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.sequential.training.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.sequential.training.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| results.sequential.training.checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| results.sequential.training.scientific_CE_teacher_tokens | 2000000000 |
| results.sequential.training.counters.update | 212095 |
| results.sequential.training.counters.supervised_tokens | 2000000000 |
| results.sequential.training.counters.CE_input_tokens | 2053285089 |
| results.sequential.training.counters.auxiliary_input_tokens | 0 |
| results.sequential.training.counters.auxiliary_pairs | 0 |
| results.sequential.training.counters.physical_input_tokens | 8620194616 |
| results.sequential.training.counters.original_body_bytes | 8118116484 |
| results.sequential.training.counters.token_digest | "50452c1e5fccc0928a4b1acce06171b4a869c4251c6efc645348430e6b41d51d" |
| results.sequential.training.counters.source_teachers.web | 1500000000 |
| results.sequential.training.counters.source_teachers.textbook | 400000000 |
| results.sequential.training.counters.source_teachers.story | 100000000 |
| results.sequential.training.counters.source_EOS.web | 13131989 |
| results.sequential.training.counters.source_EOS.textbook | 2967040 |
| results.sequential.training.counters.source_EOS.story | 764589 |
| results.sequential.training.sampler.kind | "bounded_original_TRAIN_index_byte_draw_CE_only_genre_quota_windows_v1" |
| results.sequential.training.sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| results.sequential.training.sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| results.sequential.training.sampler.binding.index_size | 12861257655 |
| results.sequential.training.sampler.binding.index_mtime_ns | 1791234945567297288 |
| results.sequential.training.sampler.binding.stream_size | 4000002624 |
| results.sequential.training.sampler.binding.stream_mtime_ns | 1791234945514053852 |
| results.sequential.training.sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| results.sequential.training.sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| results.sequential.training.sampler.seed | 42 |
| results.sequential.training.sampler.goals.web | 1500000000 |
| results.sequential.training.sampler.goals.textbook | 400000000 |
| results.sequential.training.sampler.goals.story | 100000000 |
| results.sequential.training.sampler.consumed.web | 1500000000 |
| results.sequential.training.sampler.consumed.textbook | 400000000 |
| results.sequential.training.sampler.consumed.story | 100000000 |
| results.sequential.training.sampler.pending.web | [] |
| results.sequential.training.sampler.pending.textbook | [] |
| results.sequential.training.sampler.pending.story | [] |
| results.sequential.training.sampler.draws | 53281196 |
| results.sequential.training.sampler.documents_drawn | 16863621 |
| results.sequential.training.sampler.windows_emitted | 16967541 |
| results.sequential.training.sampler.auxiliary_reasons.CE_only_no_auxiliary_pair_extraction | 16863621 |
| results.sequential.training.scheduler.tokens | 2000000000 |
| results.sequential.training.spec.seed | 42 |
| results.sequential.training.spec.residual_policy.physical_block_invocations | 1 |
| results.sequential.training.lineage.seed | 42 |
| results.sequential.training.model_config.status | "phase5_ablation" |
| results.sequential.training.residual_policy.physical_block_invocations | 1 |
| results.sequential.evaluation.binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| results.sequential.evaluation.binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| results.sequential.evaluation.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.sequential.evaluation.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.sequential.evaluation.checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| results.sequential.evaluation.body.documents | 256 |
| results.sequential.evaluation.body.limit_documents | 256 |
| results.sequential.evaluation.body.body_nll | 362013.3427505493 |
| results.sequential.evaluation.body.eos_nll | 952.9294297844172 |
| results.sequential.evaluation.body.body_bytes | 472055 |
| results.sequential.evaluation.body.body_tokens | 122343 |
| results.sequential.evaluation.body.bpb | 1.1063855998175087 |
| results.sequential.evaluation.body.seconds | 1.492392722000659 |
| results.sequential.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| results.sequential.evaluation.generation.max_new_tokens | 64 |
| results.sequential.evaluation.greedy_rates.eos | 20 |
| results.sequential.evaluation.greedy_rates.repetition | 27 |
| results.sequential.evaluation.greedy_rates.unicode_failure | 0 |
| results.sequential.evaluation.greedy_rates.role_leak | 0 |
| results.sequential.evaluation.greedy_rates.empty | 0 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.53125, 0.609375] |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.567578125, 0.6510416666666666] |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6075759640277967 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.2207836961315449 |
| results.sequential.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| results.sequential.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| results.sequential.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| results.sequential.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7885196374622356 |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8308157099697885] |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7794561933534743] |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| results.sequential.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| results.sequential.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| results.sequential.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| results.sequential.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.sequential.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.3829311885612154 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.354781054512958, 0.4092940125111707] |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.38337801608579086 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3677390527256479 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3400245755138516, 0.3945598748882931] |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3681858802502234 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.36734732296171035 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.2108355764244461 |
| results.sequential.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| results.sequential.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| results.sequential.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| results.sequential.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| results.sequential.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.sequential.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.sequential.evaluation.diagnostics.semantic_both_contexts.correct | 15 |
| results.sequential.evaluation.memory.maximum_observed_allocated_bytes | 268768256 |
| results.sequential.evaluation.memory.maximum_observed_reserved_bytes | 10892607488 |
| results.sequential.evaluation.protected_test_used | false |
| results.sequential.evaluation.residual_policy.physical_block_invocations | 1 |
| results.parallel.training.status | "complete" |
| results.parallel.training.binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| results.parallel.training.binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| results.parallel.training.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.parallel.training.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.parallel.training.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| results.parallel.training.checkpoint_sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| results.parallel.training.scientific_CE_teacher_tokens | 2000000000 |
| results.parallel.training.counters.update | 212095 |
| results.parallel.training.counters.supervised_tokens | 2000000000 |
| results.parallel.training.counters.CE_input_tokens | 2053285089 |
| results.parallel.training.counters.auxiliary_input_tokens | 0 |
| results.parallel.training.counters.auxiliary_pairs | 0 |
| results.parallel.training.counters.physical_input_tokens | 8620194616 |
| results.parallel.training.counters.original_body_bytes | 8118116484 |
| results.parallel.training.counters.token_digest | "50452c1e5fccc0928a4b1acce06171b4a869c4251c6efc645348430e6b41d51d" |
| results.parallel.training.counters.source_teachers.web | 1500000000 |
| results.parallel.training.counters.source_teachers.textbook | 400000000 |
| results.parallel.training.counters.source_teachers.story | 100000000 |
| results.parallel.training.counters.source_EOS.web | 13131989 |
| results.parallel.training.counters.source_EOS.textbook | 2967040 |
| results.parallel.training.counters.source_EOS.story | 764589 |
| results.parallel.training.sampler.kind | "bounded_original_TRAIN_index_byte_draw_CE_only_genre_quota_windows_v1" |
| results.parallel.training.sampler.binding.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| results.parallel.training.sampler.binding.index_sha256 | "6b6ef7ed1553846852234c70a3d24e2ac2a5d4dfc2f84576a42bd71f16ff48c8" |
| results.parallel.training.sampler.binding.index_size | 12861257655 |
| results.parallel.training.sampler.binding.index_mtime_ns | 1791234945567297288 |
| results.parallel.training.sampler.binding.stream_size | 4000002624 |
| results.parallel.training.sampler.binding.stream_mtime_ns | 1791234945514053852 |
| results.parallel.training.sampler.binding.ready_sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| results.parallel.training.sampler.binding.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| results.parallel.training.sampler.seed | 42 |
| results.parallel.training.sampler.goals.web | 1500000000 |
| results.parallel.training.sampler.goals.textbook | 400000000 |
| results.parallel.training.sampler.goals.story | 100000000 |
| results.parallel.training.sampler.consumed.web | 1500000000 |
| results.parallel.training.sampler.consumed.textbook | 400000000 |
| results.parallel.training.sampler.consumed.story | 100000000 |
| results.parallel.training.sampler.pending.web | [] |
| results.parallel.training.sampler.pending.textbook | [] |
| results.parallel.training.sampler.pending.story | [] |
| results.parallel.training.sampler.draws | 53281196 |
| results.parallel.training.sampler.documents_drawn | 16863621 |
| results.parallel.training.sampler.windows_emitted | 16967541 |
| results.parallel.training.sampler.auxiliary_reasons.CE_only_no_auxiliary_pair_extraction | 16863621 |
| results.parallel.training.scheduler.tokens | 2000000000 |
| results.parallel.training.spec.seed | 42 |
| results.parallel.training.spec.residual_policy.physical_block_invocations | 1 |
| results.parallel.training.lineage.seed | 42 |
| results.parallel.training.model_config.status | "phase5_ablation" |
| results.parallel.training.model_config.parallel_residual_research.policy.physical_block_invocations | 1 |
| results.parallel.training.residual_policy.physical_block_invocations | 1 |
| results.parallel.evaluation.binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| results.parallel.evaluation.binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| results.parallel.evaluation.binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| results.parallel.evaluation.binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| results.parallel.evaluation.checkpoint_sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| results.parallel.evaluation.body.documents | 256 |
| results.parallel.evaluation.body.limit_documents | 256 |
| results.parallel.evaluation.body.body_nll | 360581.3127708435 |
| results.parallel.evaluation.body.eos_nll | 993.5571699440479 |
| results.parallel.evaluation.body.body_bytes | 472055 |
| results.parallel.evaluation.body.body_tokens | 122343 |
| results.parallel.evaluation.body.bpb | 1.102009028125384 |
| results.parallel.evaluation.body.seconds | 1.275821415008977 |
| results.parallel.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| results.parallel.evaluation.generation.max_new_tokens | 64 |
| results.parallel.evaluation.greedy_rates.eos | 22 |
| results.parallel.evaluation.greedy_rates.repetition | 28 |
| results.parallel.evaluation.greedy_rates.unicode_failure | 0 |
| results.parallel.evaluation.greedy_rates.role_leak | 0 |
| results.parallel.evaluation.greedy_rates.empty | 0 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.point | 0.5833333333333334 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5364583333333334, 0.6302083333333334] |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.5833333333333334 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6302083333333334] |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5821999782395821 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.16757831697804315 |
| results.parallel.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| results.parallel.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| results.parallel.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| results.parallel.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.8308157099697885 |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7914652567975831, 0.8700906344410876] |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.8308157099697885 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7734138972809668 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7734138972809668 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.43611584327086883 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| results.parallel.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| results.parallel.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| results.parallel.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| results.parallel.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.parallel.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.8036253776435045 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.34763181411974975 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.3199285075960679, 0.3744414655942806] |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.34763181411974975 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3386952636282395 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3109919571045576, 0.36639857015192134] |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3386952636282395 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3380681148429946 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.17362742844669463 |
| results.parallel.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| results.parallel.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| results.parallel.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| results.parallel.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| results.parallel.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| results.parallel.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| results.parallel.evaluation.diagnostics.semantic_both_contexts.correct | 20 |
| results.parallel.evaluation.memory.maximum_observed_allocated_bytes | 268768256 |
| results.parallel.evaluation.memory.maximum_observed_reserved_bytes | 10892607488 |
| results.parallel.evaluation.protected_test_used | false |
| results.parallel.evaluation.residual_policy.physical_block_invocations | 1 |
| common_CE_checks.full_counters | true |
| common_CE_checks.full_sampler | true |
| common_CE_checks.full_scheduler | true |
| scientific_CE_teacher_tokens | 4000000000 |
| reused_control_CE_teachers | 100000000 |
| reused_control_GPU_seconds | 0 |
| GPU_occupancy_seconds | 52093.681041047006 |
| total_GPU_seconds_including_probe | 52115.071744653 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_comparison_review.json — fresh_paired_residual2B_all160_reviewed</summary>

[原記録](../../reports/phase6/base_parallel_residual_comparison_review.json) ／ SHA256: `40d66a70bdf80dd03c8afb93092eb54b8f395598dcc82aa94e2894744345c2da` ／ 5,730 bytes

| 原キー | 保存値 |
|---|---|
| status | "fresh_paired_residual2B_all160_reviewed" |
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
| summaries.sequential.BPB | 1.1063855998175087 |
| summaries.sequential.rates.eos | 20 |
| summaries.sequential.rates.repetition | 27 |
| summaries.sequential.rates.unicode_failure | 0 |
| summaries.sequential.rates.role_leak | 0 |
| summaries.sequential.rates.empty | 0 |
| summaries.sequential.grammar2 | 23 |
| summaries.sequential.relevance2 | 30 |
| summaries.sequential.coherent | 3 |
| summaries.sequential.appropriate | 7 |
| summaries.sequential.notes_sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| summaries.parallel.BPB | 1.102009028125384 |
| summaries.parallel.rates.eos | 22 |
| summaries.parallel.rates.repetition | 28 |
| summaries.parallel.rates.unicode_failure | 0 |
| summaries.parallel.rates.role_leak | 0 |
| summaries.parallel.rates.empty | 0 |
| summaries.parallel.grammar2 | 20 |
| summaries.parallel.relevance2 | 38 |
| summaries.parallel.coherent | 2 |
| summaries.parallel.appropriate | 7 |
| summaries.parallel.notes_sha256 | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| summaries.cached_CE.BPB | 0.998487162513845 |
| summaries.cached_CE.rates.eos | 19 |
| summaries.cached_CE.rates.repetition | 45 |
| summaries.cached_CE.rates.unicode_failure | 0 |
| summaries.cached_CE.rates.role_leak | 0 |
| summaries.cached_CE.rates.empty | 0 |
| summaries.cached_CE.grammar2 | 44 |
| summaries.cached_CE.relevance2 | 25 |
| summaries.cached_CE.coherent | 2 |
| summaries.cached_CE.appropriate | 2 |
| summaries.cached_CE.notes_sha256 | "5a36aa6d4914260d1975974ae0fbee6c1e0024d900ea8103da970fdbc4ee9369" |
| quality_comparisons.new_sequential.checks.coherence_gain_at_least8 | false |
| quality_comparisons.new_sequential.checks.paired_CI_lower_above0 | false |
| quality_comparisons.new_sequential.checks.EOS_nonworsening | true |
| quality_comparisons.new_sequential.checks.repetition_nonworsening | false |
| quality_comparisons.new_sequential.checks.no_empty_role_unicode | true |
| quality_comparisons.new_sequential.checks.BPB_gate | true |
| quality_comparisons.new_sequential.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.new_sequential.passed | false |
| quality_comparisons.strong.checks.coherence_gain_at_least8 | false |
| quality_comparisons.strong.checks.paired_CI_lower_above0 | false |
| quality_comparisons.strong.checks.EOS_nonworsening | false |
| quality_comparisons.strong.checks.repetition_nonworsening | false |
| quality_comparisons.strong.checks.no_empty_role_unicode | true |
| quality_comparisons.strong.checks.BPB_gate | true |
| quality_comparisons.strong.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.strong.passed | false |
| quality_comparisons.cached_native.checks.coherence_gain_at_least8 | false |
| quality_comparisons.cached_native.checks.paired_CI_lower_above0 | false |
| quality_comparisons.cached_native.checks.EOS_nonworsening | true |
| quality_comparisons.cached_native.checks.repetition_nonworsening | true |
| quality_comparisons.cached_native.checks.no_empty_role_unicode | true |
| quality_comparisons.cached_native.checks.BPB_gate | false |
| quality_comparisons.cached_native.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.cached_native.passed | false |
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
| scientific_CE_teacher_tokens | 4000000000 |
| reused_control_teacher_tokens | 100000000 |
| GPU_seconds | 52093.681041047006 |
| probe_GPU_seconds | 21.390703606000898 |
| notes_sha256.sequential | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| notes_sha256.parallel | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limitations | "Single fresh training seed and repeatedly reused nonblind DEV; both exact10001152 matrices initialize identically but initial functions differ. Cached mature100M has a different learned history and is additional quality reference only. Independent learnedseed/fullDEV/protectedTEST/adoption pending." |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_first_checkpoint_verification.json — first_actual_postwarmup_CUDA_checkpoint_CPU_verified</summary>

[原記録](../../reports/phase6/base_parallel_residual_first_checkpoint_verification.json) ／ SHA256: `92d198cb22fa3338504ec2ec2b596d013182ac0ee0410728589fd8994a21bee2` ／ 1,737 bytes

| 原キー | 保存値 |
|---|---|
| status | "first_actual_postwarmup_CUDA_checkpoint_CPU_verified" |
| checks.kind | true |
| checks.spec | true |
| checks.binding | true |
| checks.lineage | true |
| checks.model_config | true |
| checks.committed_finite_state | true |
| checks.update_matches_filename | true |
| checks.postwarmup | true |
| checks.cosine_LR_exact | true |
| checks.full_sampler_load | true |
| checks.scheduler_load | true |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00002000.pt" |
| checkpoint.sha256 | "72cd25cdda716d95d7e7ff44930ad75a129654c8f6dd09300436f741642e7c2e" |
| counters.update | 2000 |
| counters.supervised_tokens | 18836429 |
| counters.CE_input_tokens | 19360716 |
| counters.auxiliary_input_tokens | 0 |
| counters.auxiliary_pairs | 0 |
| counters.physical_input_tokens | 81652400 |
| counters.original_body_bytes | 76437184 |
| counters.token_digest | "b443813c2463257fbe4ab1ce294ad26be8c43365363c2e806d74aa1a6f60e470" |
| counters.source_teachers.web | 14127234 |
| counters.source_teachers.textbook | 3767339 |
| counters.source_teachers.story | 941856 |
| counters.source_EOS.web | 123833 |
| counters.source_EOS.textbook | 27906 |
| counters.source_EOS.story | 7238 |
| scheduler.tokens | 18836429 |
| CPU_seconds | 0.9585072209993086 |
| GPU_seconds | 0 |
| scientific_training_steps_added | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_parallel_evaluation_result.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_parallel_evaluation_result.json) ／ SHA256: `07c9d0839b4e70e85758d0dcb427409affa90f10cd6bb775f50b3af0573f3213` ／ 222,526 bytes

| 原キー | 保存値 |
|---|---|
| binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoint_sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 360581.3127708435 |
| body.eos_nll | 993.5571699440479 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.102009028125384 |
| body.seconds | 1.275821415008977 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 22 |
| greedy_rates.repetition | 28 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5833333333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5364583333333334, 0.6302083333333334] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6302083333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5821999782395821 |
| diagnostics.semantics.per_token_secondary.mcc | 0.16757831697804315 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.8308157099697885 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7914652567975831, 0.8700906344410876] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.8308157099697885 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7734138972809668 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7734138972809668 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.43611584327086883 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.8036253776435045 |
| diagnostics.jcqa.primary.accuracy.point | 0.34763181411974975 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3199285075960679, 0.3744414655942806] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.34763181411974975 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3386952636282395 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3109919571045576, 0.36639857015192134] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3386952636282395 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3380681148429946 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.17362742844669463 |
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
| diagnostics.semantic_both_contexts.correct | 20 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 10892607488 |
| protected_test_used | false |
| residual_policy.physical_block_invocations | 1 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_parallel_generation.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_parallel_generation.json) ／ SHA256: `5b6b28006490aa8419016cac2df411192fb7a6bfae2a371422bba86c4d4a3b72` ／ 121,485 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_parallel_notes.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_parallel_notes.json) ／ SHA256: `51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6` ／ 16,402 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_parallel_residual_parallel_training_result.json — complete</summary>

[原記録](../../reports/phase6/base_parallel_residual_parallel_training_result.json) ／ SHA256: `ae6ceb456354523b7a26e6a9d4c9a5d632b78955d643599526745a36f73a3fad` ／ 21,511 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/parallel/checkpoint-00212095.pt" |
| checkpoint_sha256 | "c29aaba162dc99ff0056aa36a94674a10d88dc157d62fb460eaa0bd2c08ac1fb" |
| scientific_CE_teacher_tokens | 2000000000 |
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
| spec.residual_policy.physical_block_invocations | 1 |
| lineage.seed | 42 |
| model_config.status | "phase5_ablation" |
| model_config.parallel_residual_research.policy.physical_block_invocations | 1 |
| residual_policy.physical_block_invocations | 1 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_probe_completion.json — own_CUDA_complete_actual_exited_science_frozen_not_started</summary>

[原記録](../../reports/phase6/base_parallel_residual_probe_completion.json) ／ SHA256: `c94700bef4b909e9fbfeaa7ee36ac69691bee4042dfdd9faa563477f20bffb16` ／ 3,998 bytes

| 原キー | 保存値 |
|---|---|
| forecast_arm_seconds.sequential | 47779 |
| forecast_arm_seconds.parallel | 33957 |
| resume_checks.sequential.kind | true |
| resume_checks.sequential.spec | true |
| resume_checks.sequential.binding | true |
| resume_checks.sequential.lineage | true |
| resume_checks.sequential.model_config | true |
| resume_checks.sequential.model | true |
| resume_checks.sequential.optimizer | true |
| resume_checks.sequential.scheduler | true |
| resume_checks.sequential.RNG | true |
| resume_checks.sequential.sampler | true |
| resume_checks.sequential.counters | true |
| resume_checks.sequential.committed_finite_state | true |
| resume_checks.sequential.all_history_except_timing | true |
| resume_checks.parallel.kind | true |
| resume_checks.parallel.spec | true |
| resume_checks.parallel.binding | true |
| resume_checks.parallel.lineage | true |
| resume_checks.parallel.model_config | true |
| resume_checks.parallel.model | true |
| resume_checks.parallel.optimizer | true |
| resume_checks.parallel.scheduler | true |
| resume_checks.parallel.RNG | true |
| resume_checks.parallel.sampler | true |
| resume_checks.parallel.counters | true |
| resume_checks.parallel.committed_finite_state | true |
| resume_checks.parallel.all_history_except_timing | true |
| forecast_all_new_GPU_seconds | 81757.390703606 |
| ui.training_tokens | 10000007168 |
| ui.update | 305176 |
| ui.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| ui.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| ui.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| probe_GPU_seconds | 21.390703606000898 |
| original_CPU25_preserved | true |
| verification_updates | 86 |
| initial_checks.every_initial_tensor_equal | true |
| initial_checks.paired_global_RNG_equal | true |
| initial_checks.tied_heads | true |
| initial_checks.parameter_counts_exact | true |
| initial_checks.optimizers_actual_only | true |
| scientific_gold_tokens | 0 |
| capacity.sequential.passed | true |
| capacity.sequential.peak_VRAM_bytes | 17791499264 |
| capacity.sequential.context | 1024 |
| capacity.sequential.teachers | 40960 |
| capacity.sequential.physical_input_tokens | 81920 |
| capacity.sequential.loss | 8.323198318481445 |
| capacity.sequential.gradient_norm | 7.273618221282959 |
| capacity.sequential.optimizer_updates | 0 |
| capacity.sequential.weights_unchanged_by_stress | true |
| capacity.parallel.passed | true |
| capacity.parallel.peak_VRAM_bytes | 16699407360 |
| capacity.parallel.context | 1024 |
| capacity.parallel.teachers | 40960 |
| capacity.parallel.physical_input_tokens | 81920 |
| capacity.parallel.loss | 8.344459533691406 |
| capacity.parallel.gradient_norm | 6.996984004974365 |
| capacity.parallel.optimizer_updates | 0 |
| capacity.parallel.weights_unchanged_by_stress | true |
| runner_reviewer_tests | 10 |
| current_CPU_tests | 54 |
| Base_complete | false |
| validator_correction | "reports/phase6/base_parallel_residual_validator_bridge.json" |
| status | "own_CUDA_complete_actual_exited_science_frozen_not_started" |
| Base_adopted | false |
| verification_original_gold | 824014 |
| science_budget_eligible | true |
| original_stream_checks.full_counters | true |
| original_stream_checks.full_sampler | true |
| original_stream_checks.full_scheduler | true |
| current_trainer_seconds | 7.38 |
| current_trainer_tests | 13 |
| runner_reviewer_seconds | 0.87 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_proposal.json — prospective_fresh_residual_connectivity_comparison</summary>

[原記録](../../reports/phase6/base_parallel_residual_proposal.json) ／ SHA256: `e92e2ad165be53feb7dce8b56fa90fe301c7fc5007ac217a00544cbb11ccdc86` ／ 10,204 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_fresh_residual_connectivity_comparison" |
| source_limitation | "NeoX describes mainly distributed communication efficiency and comparable early losses. This single4090 RMSNorm/SwiGLU/GQA adaptation preserves native initialization; it is not a faithful20B reproduction or Japanese quality/speed proof." |
| variants.sequential.status | "phase5_ablation" |
| variants.parallel.status | "phase5_ablation" |
| variants.parallel.parallel_residual_research.policy.physical_block_invocations | 1 |
| policy.physical_block_invocations | 1 |
| physical_and_logical_blocks | 13 |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_gold_total | 4000000000 |
| new_unique_corpus_tokens | 0 |
| sampler | "Original full TRAIN body/EOS1024/512 windows with CEOnlyOriginalSampler; keep accepted binding/stat, no full13GB corpus scan" |
| optimizer.seed | 42 |
| resource.CPU_preparation_cap_seconds | 30 |
| resource.own_probe_GPU_cap_seconds | 180 |
| resource.total_GPU_cap_seconds | 86400 |
| resource.capacity_shape | [80, 1024] |
| resource.checkpoint_updates | 2000 |
| resource.heartbeat_updates | 20 |
| failure | "Close this exact parallel connectivity/init/source/LR/batch/backend/decoder/token/GPU-cap recipe if finite, budget or quality gates fail; no tied-norm/gain/layer-count/seed/parent/timing-window rescue or automatic extension." |
| limitations | "One initialization/training seed and reused nonblind DEV. Same raw matrices differ in initial function, and same teacher counts differ in gradient dynamics. No prior evidence proves sequential FFN dependence causes repetition or that2B suffices." |
| references.base_output_mixture_comparison_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_output_mixture_comparison_completion.json" |
| references.base_output_mixture_comparison_completion.json.sha256 | "f1ad9f9ac838998de62b8bd0be29f58e697cd5a2b0c05b82835deb45d0350c61" |
| references.base_capacity_reference_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_capacity_reference_synthesis.json" |
| references.base_capacity_reference_synthesis.json.sha256 | "ba603b7bd2d90b54300eee86815f6ed7fa10cf1c250e38420b1998ac5c52fe14" |
| references.base_relu_squared_probe_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_relu_squared_probe_completion.json" |
| references.base_relu_squared_probe_completion.json.sha256 | "2a53bebec5a10a01071678fabd6d67ee690fa11d60d726e69adf51de7d6667da" |
| references.base_failure_route_synthesis.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_failure_route_synthesis.json" |
| references.base_failure_route_synthesis.json.sha256 | "2384411b47272b53b9e4eda981a69ff67e335069ca125a43e551c892515826b2" |
| CPU_preparation_seconds | 1.0721340519994556 |
| new_GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| GPU_workflow_implemented | false |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_rating_reuse.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_rating_reuse.json) ／ SHA256: `b4d78ed14f4d03b56e362feac74cfdfaa9eef9e056aa1d2d5aa798831bd4f3ef` ／ 9,326 bytes

| 原キー | 保存値 |
|---|---|
| arms.sequential.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_sequential_notes.json" |
| arms.sequential.notes.sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| arms.parallel.notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_parallel_notes.json" |
| arms.parallel.notes.sha256 | "51543a2299e79f01b339fef4af36676aac44c9498c0cbd4d222bd8a8d06c47b6" |
| historical_notes_changed | false |
| GPU_seconds | 0 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_sequential_evaluation_result.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_sequential_evaluation_result.json) ／ SHA256: `8ca51cf98d9b787619bd08805f6745c736bb1aa3d565f9dad4b1a13dd69fe2bb` ／ 222,049 bytes

| 原キー | 保存値 |
|---|---|
| binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 362013.3427505493 |
| body.eos_nll | 952.9294297844172 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.1063855998175087 |
| body.seconds | 1.492392722000659 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 20 |
| greedy_rates.repetition | 27 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.53125, 0.609375] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.609375 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.567578125, 0.6510416666666666] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6075759640277967 |
| diagnostics.semantics.per_token_secondary.mcc | 0.2207836961315449 |
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
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8308157099697885] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7885196374622356 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6858006042296072, 0.7794561933534743] |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.770392749244713 |
| diagnostics.jcqa.primary.accuracy.point | 0.3829311885612154 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.354781054512958, 0.4092940125111707] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.38337801608579086 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3677390527256479 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.3400245755138516, 0.3945598748882931] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3681858802502234 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.36734732296171035 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.2108355764244461 |
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
| diagnostics.semantic_both_contexts.correct | 15 |
| memory.maximum_observed_allocated_bytes | 268768256 |
| memory.maximum_observed_reserved_bytes | 10892607488 |
| protected_test_used | false |
| residual_policy.physical_block_invocations | 1 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_sequential_generation.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_sequential_generation.json) ／ SHA256: `79256b59752c3002cf6f6e6d0f25fa01c8cbf336ba6d8eac51e427976b68104f` ／ 121,207 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_sequential_notes.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_sequential_notes.json) ／ SHA256: `4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7` ／ 16,178 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_parallel_residual_sequential_training_result.json — complete</summary>

[原記録](../../reports/phase6/base_parallel_residual_sequential_training_result.json) ／ SHA256: `a55959a821d9880609be22576b86d1f7f9ee7c373fb98378eb3de6a2ffc36b54` ／ 21,097 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.sources.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| binding.sources.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| binding.sources.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.sources.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-parallel-residual-comparison-20261007/sequential/checkpoint-00212095.pt" |
| checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| scientific_CE_teacher_tokens | 2000000000 |
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
| spec.residual_policy.physical_block_invocations | 1 |
| lineage.seed | 42 |
| model_config.status | "phase5_ablation" |
| residual_policy.physical_block_invocations | 1 |

</details>

<details>
<summary>reports/phase6/base_parallel_residual_validator_bridge.json — None</summary>

[原記録](../../reports/phase6/base_parallel_residual_validator_bridge.json) ／ SHA256: `2396055b52eb341be341766047c63bfc9b27bace0fd6e3b64de63f4def7d4d70` ／ 2,837 bytes

| 原キー | 保存値 |
|---|---|
| correction | "Align committed-state cosine arithmetic with unchanged TargetPositionSchedule.value. Exact equality remains required; no tolerance, training update, LR, optimizer, sampler, model, budget or quality change." |
| current_references.trainer_test_source.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/tests/test_base_parallel_residual_trainer.py" |
| current_references.trainer_test_source.sha256 | "162fd92c0a293f6b9b5e8294e05a704e237c7bfc85ce5869bf9af4a7ce97b83c" |
| current_references.trainer_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_cosine_tests.xml" |
| current_references.trainer_tests.sha256 | "309e338660c04a523ef5c30e580fd8c5cac9b4b909b19d7b3dbeed697e5cee95" |
| current_references.initial_failed_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_cosine_initial_tests.xml" |
| current_references.initial_failed_tests.sha256 | "edd6b67d4fbe62f4350a1f953ec5218c3fe24d2934d04b3cb7c8b3598686ab2c" |
| current_trainer_tests | 13 |
| current_total_model_trainer_evaluation_tests | 27 |
| actual_postwarmup_CPU_gold_each | 10000 |
| actual_CPU_postwarmup_save_resume_both | true |
| GPU_training_updates_changed | false |
| GPU_training_recipe_changed | false |
| additional_GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_recurrent_compute_novelty_review.json — recurrent_compute_candidate_declined_after_prior_route_and_primary_source_review</summary>

[原記録](../../reports/phase6/base_recurrent_compute_novelty_review.json) ／ SHA256: `92f60482d9c00878132db5c542a7062b5e0fd99e058f2cb57478759f749a62f0` ／ 8,949 bytes

| 原キー | 保存値 |
|---|---|
| status | "recurrent_compute_candidate_declined_after_prior_route_and_primary_source_review" |
| decision | "Do not implement or launch the proposed full-stack recurrence or damped layer-reuse variant. Prior gated immediate sharing already tested26 invocations; changing visit order, gate initialization or residual scaling would reopen its closed recipe rather than establish a clean independent route." |
| decision_scope | "Conservative project scope decision; whole-stack recurrence and damped Euler are mathematically different from the old gated model. Their Japanese10M performance was not measured, and a universal recurrence failure is not claimed." |
| historical_sharing.physical_blocks | 13 |
| historical_sharing.original_gold_tokens | 100000000 |
| historical_sharing.candidate.BPB | 1.0359260398203731 |
| historical_sharing.candidate.rates.eos | 73 |
| historical_sharing.candidate.rates.repetition | 7 |
| historical_sharing.candidate.rates.unicode_failure | 0 |
| historical_sharing.candidate.rates.role_leak | 0 |
| historical_sharing.candidate.rates.empty | 0 |
| historical_sharing.candidate.grammar2 | 68 |
| historical_sharing.candidate.relevance2 | 53 |
| historical_sharing.candidate.coherent | 30 |
| historical_sharing.candidate.appropriate | 36 |
| historical_sharing.candidate.notes_sha256 | "40040c25ee7f83f4a59a9b6549f1c205cfa10e93525ed6d445ee5345c1201519" |
| historical_sharing.matched_control.BPB | 1.0356667036495277 |
| historical_sharing.matched_control.rates.eos | 69 |
| historical_sharing.matched_control.rates.repetition | 6 |
| historical_sharing.matched_control.rates.unicode_failure | 0 |
| historical_sharing.matched_control.rates.role_leak | 0 |
| historical_sharing.matched_control.rates.empty | 0 |
| historical_sharing.matched_control.grammar2 | 65 |
| historical_sharing.matched_control.relevance2 | 52 |
| historical_sharing.matched_control.coherent | 32 |
| historical_sharing.matched_control.appropriate | 37 |
| historical_sharing.matched_control.notes_sha256 | "366209389693d5b382ab5a4f4001e0dd6c52fd10c33f9304672a195607b51e69" |
| historical_sharing.quality_comparisons.native_CE.checks.coherence_gain_at_least8 | false |
| historical_sharing.quality_comparisons.native_CE.checks.paired_CI_lower_above0 | false |
| historical_sharing.quality_comparisons.native_CE.checks.EOS_nonworsening | true |
| historical_sharing.quality_comparisons.native_CE.checks.repetition_nonworsening | false |
| historical_sharing.quality_comparisons.native_CE.checks.no_empty_role_unicode | true |
| historical_sharing.quality_comparisons.native_CE.checks.BPB_gate | true |
| historical_sharing.quality_comparisons.native_CE.checks.appropriate_completion_not_punctuation | true |
| historical_sharing.quality_comparisons.native_CE.passed | false |
| historical_sharing.quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| historical_sharing.quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| historical_sharing.quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| historical_sharing.quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| historical_sharing.quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| historical_sharing.quality_comparisons.strong_staged.checks.BPB_gate | true |
| historical_sharing.quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| historical_sharing.quality_comparisons.strong_staged.passed | false |
| historical_sharing.absolute_dev_screen.grammar_at_least56 | true |
| historical_sharing.absolute_dev_screen.coherence_at_least27 | true |
| historical_sharing.absolute_dev_screen.appropriate_at_least27 | true |
| historical_sharing.absolute_dev_screen.EOS_at_least37 | true |
| historical_sharing.absolute_dev_screen.repetition_at_most18 | true |
| historical_sharing.absolute_dev_screen.no_empty_role_unicode | true |
| historical_sharing.original_Web.EOS_at_least8_more | true |
| historical_sharing.original_Web.repetition_no_worse | true |
| historical_sharing.original_Web.no_empty_role_unicode | true |
| historical_sharing.original_Web.BPB_degradation_at_most1percent | false |
| historical_sharing.eligible_for_final_Base_validation | false |
| novelty_search.first_pattern_limitation | "A loop/recurrent-depth keyword search missed the earlier gated immediate sharing; direct inspection of gated_shared_model/proposal/review found the overlap. Never interpret absence of one keyword as absence of a tested mechanism." |
| next_bounded_research.limitations | "Primer combines squared ReLU with QKV depthwise convolution; its speed or quality gains are not evidence for the isolated activation versus SwiGLU or Japanese10M. No convolution or MHA allocation rescue is proposed." |
| next_bounded_research.completion_condition | "Inspect primary FFN definition/ablation and existing fresh control/budget evidence, then select or decline one exact comparison before implementing any GPU workflow. If selected, freeze token/source/LR/seed/budget and require actual CUDA/resume/timing before learning." |
| references.reports/phase6/gated_shared_comparison_completion.json.path | "reports/phase6/gated_shared_comparison_completion.json" |
| references.reports/phase6/gated_shared_comparison_completion.json.sha256 | "9ef8553215231de40e7d9c541aa7d2c50507fae28c50cbb514bf288274d21647" |
| references.reports/phase6/base_completed_objective_studies_v3_20261007.json.path | "reports/phase6/base_completed_objective_studies_v3_20261007.json" |
| references.reports/phase6/base_completed_objective_studies_v3_20261007.json.sha256 | "716b4ef75300e630d76467e75146734777dfd31c8023fb2449548ffb0f1f7252" |
| new_GPU_seconds | 0 |
| new_scientific_gold_tokens | 0 |
| new_unique_dataset_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_relu_squared_probe_completion.json — actual_FFN_probe_complete_science_closed_budget_exceeded</summary>

[原記録](../../reports/phase6/base_relu_squared_probe_completion.json) ／ SHA256: `2a53bebec5a10a01071678fabd6d67ee690fa11d60d726e69adf51de7d6667da` ／ 6,681 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_FFN_probe_complete_science_closed_budget_exceeded" |
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_relu_squared_CPU_tests.xml" |
| CPU_tests.sha256 | "a6a267ffa25123825cfc813da27a0074994babb8f0fe43c410f9037d0d682454" |
| initial_failed_CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_relu_squared_tests_initial.xml" |
| initial_failed_CPU_tests.sha256 | "9e16ab4f4b72257135d2d2d1fe5b24b57706d02f4d153028c18dcfa5365fb35d" |
| initial_test_failure_fixed_without_numeric_or_quality_threshold_change | true |
| initial_GPU_checks.non_FFN_tensors_equal | true |
| initial_GPU_checks.paired_global_RNG_equal | true |
| initial_GPU_checks.tied_heads | true |
| initial_GPU_checks.parameter_counts_exact | true |
| initial_GPU_checks.optimizers_actual_only | true |
| all_resume_checks.SwiGLU.kind | true |
| all_resume_checks.SwiGLU.spec | true |
| all_resume_checks.SwiGLU.binding | true |
| all_resume_checks.SwiGLU.lineage | true |
| all_resume_checks.SwiGLU.model_config | true |
| all_resume_checks.SwiGLU.model | true |
| all_resume_checks.SwiGLU.optimizer | true |
| all_resume_checks.SwiGLU.scheduler | true |
| all_resume_checks.SwiGLU.RNG | true |
| all_resume_checks.SwiGLU.sampler | true |
| all_resume_checks.SwiGLU.counters | true |
| all_resume_checks.SwiGLU.committed_finite_state | true |
| all_resume_checks.SwiGLU.all_history_except_timing | true |
| all_resume_checks.ReLU_squared.kind | true |
| all_resume_checks.ReLU_squared.spec | true |
| all_resume_checks.ReLU_squared.binding | true |
| all_resume_checks.ReLU_squared.lineage | true |
| all_resume_checks.ReLU_squared.model_config | true |
| all_resume_checks.ReLU_squared.model | true |
| all_resume_checks.ReLU_squared.optimizer | true |
| all_resume_checks.ReLU_squared.scheduler | true |
| all_resume_checks.ReLU_squared.RNG | true |
| all_resume_checks.ReLU_squared.sampler | true |
| all_resume_checks.ReLU_squared.counters | true |
| all_resume_checks.ReLU_squared.committed_finite_state | true |
| all_resume_checks.ReLU_squared.all_history_except_timing | true |
| capacity.SwiGLU.passed | true |
| capacity.SwiGLU.peak_VRAM_bytes | 17791499264 |
| capacity.SwiGLU.context | 1024 |
| capacity.SwiGLU.teachers | 40960 |
| capacity.SwiGLU.physical_input_tokens | 81920 |
| capacity.SwiGLU.loss | 8.323198318481445 |
| capacity.SwiGLU.gradient_norm | 7.273618221282959 |
| capacity.SwiGLU.optimizer_updates | 0 |
| capacity.SwiGLU.weights_unchanged_by_stress | true |
| capacity.ReLU_squared.passed | true |
| capacity.ReLU_squared.peak_VRAM_bytes | 19971449856 |
| capacity.ReLU_squared.context | 1024 |
| capacity.ReLU_squared.teachers | 40960 |
| capacity.ReLU_squared.physical_input_tokens | 81920 |
| capacity.ReLU_squared.loss | 8.299936294555664 |
| capacity.ReLU_squared.gradient_norm | 5.175074100494385 |
| capacity.ReLU_squared.optimizer_updates | 0 |
| capacity.ReLU_squared.weights_unchanged_by_stress | true |
| GPU_seconds | 22.554600659001153 |
| verification_updates | 86 |
| verification_original_gold | 824014 |
| stress_optimizer_updates | 0 |
| scientific_gold_tokens | 0 |
| new_unique_dataset_tokens | 0 |
| forecast_all_new_GPU_seconds | 15027.554600659001 |
| fixed_all_new_GPU_cap_seconds | 14400 |
| science_budget_eligible | false |
| fixed300M_per_arm_FFN_protocol_closed | true |
| no_cap_increase_or_teacher_batch_rescue | true |
| timing_breakdown.SwiGLU.total_step_seconds | 5.518083155999193 |
| timing_breakdown.SwiGLU.sampler_wait_seconds | 1.7945518241322134 |
| timing_breakdown.SwiGLU.remaining_step_seconds | 3.7235313318669796 |
| timing_breakdown.SwiGLU.step_timing_excludes_no_wait_for_budget | true |
| timing_breakdown.SwiGLU.forecast_cap_seconds | 7886 |
| timing_breakdown.SwiGLU.original_gold_per_second | 55828.44464115667 |
| timing_breakdown.ReLU_squared.total_step_seconds | 4.912113096070243 |
| timing_breakdown.ReLU_squared.sampler_wait_seconds | 0.18653339994489215 |
| timing_breakdown.ReLU_squared.remaining_step_seconds | 4.725579696125351 |
| timing_breakdown.ReLU_squared.step_timing_excludes_no_wait_for_budget | true |
| timing_breakdown.ReLU_squared.forecast_cap_seconds | 7119 |
| timing_breakdown.ReLU_squared.original_gold_per_second | 62715.57555269991 |
| timing_limitation | "SwiGLU always measured first and ReLU_squared second on identical source batches; no randomized/interleaved order or cold-cache control. Sampler waiting differs strongly. The12percent wall-throughput difference does not prove architectural acceleration. Remaining-step time includes collation/transfers/optimizer/CPU and is not a pure GPU profiler measurement." |
| original_UI.API.training_tokens | 10000007168 |
| original_UI.API.update | 305176 |
| original_UI.API.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.API.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.API.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 1170170 |
| archive.uncompressed_text_bytes | 4205593 |
| native_checkpoints_preserved | true |
| old_MHA_budget_failure_and_science0_preserved | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_relu_squared_probe_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/base_relu_squared_probe_evidence_manifest.json) ／ SHA256: `519495db4e5830d58325b4e95888a0d1d129c43e5e85f6fdfa96b9b41d9dcf7e` ／ 10,703 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_relu_squared_proposal.json — prospective_fresh_equal_parameter_FFN_comparison</summary>

[原記録](../../reports/phase6/base_relu_squared_proposal.json) ／ SHA256: `329fc5e41e8150e6187f9b0172d765345cfbfed23d5210fa133d67d60c69a10d` ／ 7,731 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_fresh_equal_parameter_FFN_comparison" |
| variants.SwiGLU.status | "phase5_ablation" |
| physical_blocks | 13 |
| paired_initialization | "Fresh seed42 native scaffold; identical non-FFN weights. Replace candidate FFNs with independently seeded fresh normal(.02) matrices in a CPU fork_rng, preserving scaffold RNG. No learned parent or probe weights." |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_gold_across_arms | 600000000 |
| new_unique_dataset_tokens | 0 |
| sampler | "CEOnlyOriginalSampler, original full-unit1024/512 windows and body+EOS once" |
| optimizer.seed | 42 |
| resource.CPU_preparation_cap_seconds | 30 |
| resource.probe_GPU_cap_seconds | 180 |
| resource.total_GPU_cap_seconds | 14400 |
| resource.warmup_updates | 3 |
| resource.timed_updates | 32 |
| failure | "One exact two-projection960 architecture. No activation/gain/norm/bias/convolution/width/LR/source/Tokenizer/seed/checkpoint/batch/precision/backend/cap rescue or automatic extension. No positive claim from train loss, random weights or timing." |
| limitations | "Changes FFN function and latent width jointly while exactly matching parameters. Fresh300M is an initial research comparison, not sufficient training assumed or proof of10M capacity. One seed and reused nonblind DEV cannot establish final quality." |
| references.base_kv_allocation_probe_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_kv_allocation_probe_completion.json" |
| references.base_kv_allocation_probe_completion.json.sha256 | "3c5bdaf0f6918eaeef7409396e5773a35efe2836c7a4a78eaa11180bd3a3f57e" |
| references.base_kv_allocation_bucketed_completion.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_kv_allocation_bucketed_completion.json" |
| references.base_kv_allocation_bucketed_completion.json.sha256 | "604dc6d65f15ffe2b7b78e3783cf6538b85799bc85134c1facb0c5fb26f613da" |
| references.base_completed_objective_studies_v3_20261007.json.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_completed_objective_studies_v3_20261007.json" |
| references.base_completed_objective_studies_v3_20261007.json.sha256 | "716b4ef75300e630d76467e75146734777dfd31c8023fb2449548ffb0f1f7252" |
| CPU_preparation_seconds | 1.011478709988296 |
| implementation.GPU_workflow | false |
| new_GPU_seconds | 0 |
| scientific_gold_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_counterfactual.json — all96_GPU_complete_CPU_summary_pending</summary>

[原記録](../../reports/phase6/base_residual_boundary_counterfactual.json) ／ SHA256: `6824507ad4118098b5e29eea2fbecf6c388732477210956136e922e30fe2d821` ／ 404,725 bytes

| 原キー | 保存値 |
|---|---|
| status | "all96_GPU_complete_CPU_summary_pending" |
| checks.weights_unchanged | true |
| checks.RNG_unchanged | true |
| checks.eval_mode_unchanged | true |
| checks.all96_next_token_only | true |
| GPU_seconds | 2.3952718090004055 |
| GPU_cap_seconds | 30 |
| cumulative_GPU_ledger_closed | true |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_counterfactual_completion.json — complete</summary>

[原記録](../../reports/phase6/base_residual_boundary_counterfactual_completion.json) ／ SHA256: `74d671fc00bfaf933d045c86bad55b86b596041b7d7db24c16c19775627eea47` ／ 19,791 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 2.3952718090004055 |
| GPU_cap_seconds | 30 |
| checks.weights_unchanged | true |
| checks.RNG_unchanged | true |
| checks.eval_mode_unchanged | true |
| checks.all96_next_token_only | true |
| identical_original_counterfactual_prediction_checks | 31 |
| summaries.all.median_EOS_probability_difference | 0.8986915070563555 |
| summaries.all.mean_EOS_probability_difference | 0.586995554729981 |
| summaries.all.median_no_trailing_LF_EOS_probability | 0.05019144341349602 |
| summaries.all.median_one_LF_EOS_probability | 0.9548971951007843 |
| summaries.all.no_trailing_LF_EOS_rank1 | 0 |
| summaries.all.one_LF_EOS_rank1 | 24 |
| summaries.TRAIN.median_EOS_probability_difference | 0.927004024386406 |
| summaries.TRAIN.mean_EOS_probability_difference | 0.829160287801642 |
| summaries.TRAIN.median_no_trailing_LF_EOS_probability | 0.05140066333115101 |
| summaries.TRAIN.median_one_LF_EOS_probability | 0.9736657738685608 |
| summaries.TRAIN.no_trailing_LF_EOS_rank1 | 0 |
| summaries.TRAIN.one_LF_EOS_rank1 | 15 |
| summaries.DEV.median_EOS_probability_difference | 0.16867672548050905 |
| summaries.DEV.mean_EOS_probability_difference | 0.34483082165832 |
| summaries.DEV.median_no_trailing_LF_EOS_probability | 0.0477202907204628 |
| summaries.DEV.median_one_LF_EOS_probability | 0.3135595843195915 |
| summaries.DEV.no_trailing_LF_EOS_rank1 | 0 |
| summaries.DEV.one_LF_EOS_rank1 | 9 |
| restored_UI_model.training_tokens | 10000007168 |
| restored_UI_model.update | 305176 |
| restored_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| restored_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| interpretation | "Same-body trailing LF changes measured next-token EOS preference within these frozen weights; a positive screen establishes local marker sensitivity only. No new free-generation or Base-quality improvement measured. Original DEV/test bytes and all quality gates unchanged." |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_counterfactual_job.json — complete</summary>

[原記録](../../reports/phase6/base_residual_boundary_counterfactual_job.json) ／ SHA256: `777aa024bf997fa78237a8a250e89299b331fabca0eafe258299763ee5d5a651` ／ 646 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 2.3952718090004055 |
| cumulative_GPU_ledger_closed | true |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_counterfactual_proposal.json — prospective_read_only_counterfactual_defined_not_implemented_or_started</summary>

[原記録](../../reports/phase6/base_residual_boundary_counterfactual_proposal.json) ／ SHA256: `1b52d6e2a0450e6055dfb408f24aaefd85fe924713b8ca6266ca097a764d2398` ／ 3,266 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_read_only_counterfactual_defined_not_implemented_or_started" |
| parent_checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| CPU_preparation_budget_seconds | 30 |
| GPU_budget_seconds | 30 |
| completion | "Implement missing typed command and durable launcher first; protocol fixtures for LF-only edits/context/original bytes. Actual exited&lt;=30seconds job, all96 next-token records, unchanged weights/RNG/eval-mode, closed PID/boot/start GPU ledger, original idle10B UI restored, CPU paired summary and local commit. Preserve any failure and do not sweep markers or normalize DEV to pass a gate." |
| interpretation | "A positive result establishes a local ending-marker sensitivity of the frozen model, not that stripping/appending LF improves general free generation, causes the full TRAIN/DEV gap, resolves repetition, or qualifies Base. A negative result leaves source/topic/completion differences unresolved. Any later learning comparison needs its own source/quantity/budget/quality protocol." |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_format_observation.json — CPU_observation_complete_counterfactual_GPU_unstarted</summary>

[原記録](../../reports/phase6/base_residual_boundary_format_observation.json) ／ SHA256: `fdbb7bf47440f858b33c4aa5262aad3fa663d23df3fbee5d5b7b13dba6ac8754` ／ 15,270 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_observation_complete_counterfactual_GPU_unstarted" |
| CPU_seconds | 0.024218104997999035 |
| completion_sha256 | "dc429db88a26fc4801b5ede3fa713201fe996fdc6a4d877b1b13403e06e7178f" |
| groups.TRAIN.documents | 16 |
| groups.TRAIN.real_EOS_by_ending.False.observations | 1 |
| groups.TRAIN.real_EOS_by_ending.False.rank1 | 0 |
| groups.TRAIN.real_EOS_by_ending.False.median_probability | 0.0573916882276535 |
| groups.TRAIN.real_EOS_by_ending.True.observations | 10 |
| groups.TRAIN.real_EOS_by_ending.True.rank1 | 10 |
| groups.TRAIN.real_EOS_by_ending.True.median_probability | 0.9783100485801697 |
| groups.DEV.documents | 16 |
| groups.DEV.real_EOS_by_ending.False.observations | 5 |
| groups.DEV.real_EOS_by_ending.False.rank1 | 0 |
| groups.DEV.real_EOS_by_ending.False.median_probability | 0.04713575169444084 |
| groups.DEV.real_EOS_by_ending.True.observations | 0 |
| groups.DEV.real_EOS_by_ending.True.rank1 | 0 |
| groups.DEV.real_EOS_by_ending.True.median_probability | null |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| GPU_seconds | 0 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_boundary_stop_path_analysis.json — CPU_derivation_from_existing_uncached_next_token_queries</summary>

[原記録](../../reports/phase6/base_residual_boundary_stop_path_analysis.json) ／ SHA256: `464b3989679c9e3891737b7df7f02831dff02e0f7ebfbb88276db7f5ef9381f2` ／ 7,400 bytes

| 原キー | 保存値 |
|---|---|
| interpretation | "Compose two already-observed uncached next-token argmax events where the second exact context equals the first plus token18. This is not a new cached generation measurement. A learned LF then EOS path exists for21/32 (TRAIN15/16,DEV6/16), so low immediate EOS probability before LF is not by itself a broken stop mechanism or a reason to normalize DEV/test or start an LF-only learning rescue. Semantic failure remains unresolved." |
| Base_complete | false |
| new_GPU_queries | 0 |
| uncached_two_step_LF_EOS.TRAIN | 15 |
| uncached_two_step_LF_EOS.DEV | 6 |
| uncached_two_step_LF_EOS.all | 21 |
| status | "CPU_derivation_from_existing_uncached_next_token_queries" |
| all32_appended_LF_exact_token18 | true |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control.json — complete</summary>

[原記録](../../reports/phase6/base_residual_capacity_control.json) ／ SHA256: `0e789ffc64df5694d530eff36ec1907bad0eaebe72847a4e0d2b76147a7dac41` ／ 101,377 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| resume_gate.checks.kind | true |
| resume_gate.checks.model_config | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.binding | true |
| resume_gate.checks.model | true |
| resume_gate.checks.optimizer | true |
| resume_gate.checks.scheduler | true |
| resume_gate.checks.RNG | true |
| resume_gate.checks.cursor | true |
| resume_gate.checks.counters | true |
| resume_gate.checks.history | true |
| resume_gate.checks.finite | true |
| resume_gate.passed | true |
| resume_gate.verification_updates | 8 |
| resume_gate.verification_teacher_tokens | 80992 |
| counters.update | 25 |
| counters.supervised_tokens | 252176 |
| counters.EOS_targets | 2000 |
| counters.completed_original_body_bytes | 1081117 |
| counters.CE_input_tokens | 252176 |
| counters.physical_input_tokens | 636000 |
| counters.source_teacher_tokens.web | 128856 |
| counters.source_teacher_tokens.textbook | 76700 |
| counters.source_teacher_tokens.story | 46620 |
| counters.token_digest | "a731ea9cd1ea219051bdc9fffddeaa84f274ffb3bbc1c8b43e125610529b21ad" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-capacity-control-r2-20261008/latest.pt" |
| checkpoint.sha256 | "f17a18e8594253b46b54970821c28132c76592ea2dd9dba9904ba037ee63154d" |
| teacher_measured_at_update | 25 |
| capacity_control_passed | true |
| completion_reason | "all6_conditioned_original_targets_and_cached_suffix_EOS_exact" |
| GPU_seconds | 18.944145809990005 |
| GPU_cap_seconds | 300 |
| cumulative_GPU_ledger_closed | true |
| prior_GPU_seconds | 3.1996772790007526 |
| this_process_GPU_seconds | 15.744468530989252 |
| scientific_Base_teacher_tokens | 0 |
| diagnostic_learning_teacher_tokens | 252176 |
| unique_original_teacher_tokens | 756 |
| probe_weights_discarded_for_adoption | true |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| limits | "Positive learning control on six consumed TRAIN units only; neither Base quality nor generalization." |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control_completion.json — complete</summary>

[原記録](../../reports/phase6/base_residual_capacity_control_completion.json) ／ SHA256: `da3dc20412249f95d9fceac815d9793df9832ad400bd447a2b5d37ff9dd81a82` ／ 4,774 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| prior_failed_process_exited | true |
| GPU_seconds | 18.944145809990005 |
| GPU_cap_seconds | 300 |
| first_failed_gate_GPU_seconds | 3.1996772790007526 |
| repaired_process_GPU_seconds | 15.744468530989252 |
| verification_updates | 16 |
| verification_teacher_tokens | 161984 |
| original_unique_teacher_tokens | 756 |
| diagnostic_learning_teacher_tokens | 252176 |
| completed_updates | 25 |
| initial_full_teacher_correct | 422 |
| initial_conditioned_teacher_correct | 352 |
| final_full_teacher_correct | 751 |
| full_teacher_argmax_theoretical_upper_bound | 751 |
| final_conditioned_teacher_correct | 612 |
| conditioned_teacher_targets | 612 |
| capacity_control_passed | true |
| content_reading_notes | "All six originals reproduced, including awkward source wording and source factual claims; exact memorization is neither correctness of those claims nor quality on new prompts. Source roughness was retained, not edited away." |
| counters.update | 25 |
| counters.supervised_tokens | 252176 |
| counters.EOS_targets | 2000 |
| counters.completed_original_body_bytes | 1081117 |
| counters.CE_input_tokens | 252176 |
| counters.physical_input_tokens | 636000 |
| counters.source_teacher_tokens.web | 128856 |
| counters.source_teacher_tokens.textbook | 76700 |
| counters.source_teacher_tokens.story | 46620 |
| counters.token_digest | "a731ea9cd1ea219051bdc9fffddeaa84f274ffb3bbc1c8b43e125610529b21ad" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-capacity-control-r2-20261008/latest.pt" |
| checkpoint.sha256 | "f17a18e8594253b46b54970821c28132c76592ea2dd9dba9904ba037ee63154d" |
| restored_UI_model.training_tokens | 10000007168 |
| restored_UI_model.update | 305176 |
| restored_UI_model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| restored_UI_model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| restored_UI_model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_Base_teacher_tokens | 0 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| conclusion | "The corrected current sequential2B learning/evaluation path can memorize these six already-seen TRAIN units and stop at original EOS. An end-to-end inability to learn these examples is unsupported. This does not establish generalization, explain corpus-wide repetition, validate all data quality or qualify Base." |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control_gate.json — None</summary>

[原記録](../../reports/phase6/base_residual_capacity_control_gate.json) ／ SHA256: `03f80ebaa18f16ae04f6680b5613e98ce6472446dcd0fbd49dead7cfdfe30237` ／ 44,974 bytes

| 原キー | 保存値 |
|---|---|
| checks.kind | true |
| checks.model_config | true |
| checks.spec | true |
| checks.binding | true |
| checks.model | true |
| checks.optimizer | true |
| checks.scheduler | true |
| checks.RNG | true |
| checks.cursor | true |
| checks.counters | true |
| checks.history | true |
| checks.finite | true |
| passed | true |
| verification_updates | 8 |
| verification_teacher_tokens | 80992 |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control_job.json — complete</summary>

[原記録](../../reports/phase6/base_residual_capacity_control_job.json) ／ SHA256: `92fcaa7550c885af1aa67342bae794a56e7a7fb4dfa8792385308a1fa4b3dd7d` ／ 1,172 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 18.944145809990005 |
| cumulative_GPU_ledger_closed | true |
| counters.update | 25 |
| counters.supervised_tokens | 252176 |
| counters.EOS_targets | 2000 |
| counters.completed_original_body_bytes | 1081117 |
| counters.CE_input_tokens | 252176 |
| counters.physical_input_tokens | 636000 |
| counters.source_teacher_tokens.web | 128856 |
| counters.source_teacher_tokens.textbook | 76700 |
| counters.source_teacher_tokens.story | 46620 |
| counters.token_digest | "a731ea9cd1ea219051bdc9fffddeaa84f274ffb3bbc1c8b43e125610529b21ad" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-capacity-control-r2-20261008/latest.pt" |
| capacity_control_passed | true |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control_proposal.json — defined_capacity_control_not_implemented_or_started</summary>

[原記録](../../reports/phase6/base_residual_capacity_control_proposal.json) ／ SHA256: `524c4001bd53d999f96562e59074459a3041261980f7be460c1f7c9337ee5fc3` ／ 4,373 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_capacity_control_not_implemented_or_started" |
| references.six_inference_completion | "reports/phase6/base_residual_seen_train_diagnostic_completion.json" |
| parent_checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| maximum_capacity_control_original_teacher_tokens | 3000000 |
| maximum_cumulative_GPU_seconds | 300 |
| maximum_CPU_preparation_seconds | 30 |
| capacity_completion_condition | "Actual exited process within300seconds; complete committed-update learning/accounting and saved state. Pass only if finite training and all six complete original targets are teacher-argmax-correct, and cached BF16/math greedy continuation from each fixed prefix exactly reproduces its original suffix plus real EOS. No quality-score replacement, no early guessed EOS, no selection of easier units." |
| capacity_early_stop | "Evaluate complete six-target teacher accuracy every25 completed updates. Only if100%, measure all six original cached continuations; stop early only if all six exactly match including actual EOS. Otherwise continue until original-teacher3M or GPU300seconds, preserve a negative result without parameter or cap rescue." |
| decode_cap | "For this memorization control only, fixed each original suffix token count+8, context&lt;1024; larger than64 for long articles because exact original EOS must be reachable. The completed6-inference/DEV80 decoder remains unchanged. This long-cap control is never used to claim Base-quality gains." |
| interpretation | "A pass proves this fixed path can learn these six examples, not generalization or a solution for Base. A bounded failure is not proof that10M is incapable; inspect actual training/evaluation behavior, do not automatically extend or sweep. Earlier capacity and trainfit evidence used other checkpoints/data/trainers, and is retained." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_control_protocol_correction.json — prospective_pre_GPU_structural_protocol_correction</summary>

[原記録](../../reports/phase6/base_residual_capacity_control_protocol_correction.json) ／ SHA256: `f59530f78a13192ebac9490d234b2fa1bad96d74934ebe182d1cfb5994b0abce` ／ 5,699 bytes

| 原キー | 保存値 |
|---|---|
| status | "prospective_pre_GPU_structural_protocol_correction" |
| references.six_inference_completion | "reports/phase6/base_residual_seen_train_diagnostic_completion.json" |
| parent_checkpoint_sha256 | "a1d29762321f1a9df088ced78d5b67fb174f59e1dd10fd4520bf769ed78c5f51" |
| maximum_capacity_control_original_teacher_tokens | 3000000 |
| maximum_cumulative_GPU_seconds | 300 |
| maximum_CPU_preparation_seconds | 30 |
| capacity_completion_condition | "All six fixed24-token-prefix-conditioned teacher suffixes100% argmax correct and all six cached BF16/math greedy original suffixes plus real EOS exactly reproduced. Entire original body/EOS still trained and full-target accuracy still reported." |
| capacity_early_stop | "Check every25 completed updates; only conditioned suffix100% triggers six cached decodes. No cap/LR/selection rescue." |
| decode_cap | "For this memorization control only, fixed each original suffix token count+8, context&lt;1024; larger than64 for long articles because exact original EOS must be reachable. The completed6-inference/DEV80 decoder remains unchanged. This long-cap control is never used to claim Base-quality gains." |
| interpretation | "A pass proves this fixed path can learn these six examples, not generalization or a solution for Base. A bounded failure is not proof that10M is incapable; inspect actual training/evaluation behavior, do not automatically extend or sweep. Earlier capacity and trainfit evidence used other checkpoints/data/trainers, and is retained." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |
| maximum_possible_full_teacher_argmax_correct | 751 |
| reason | "Identical BOS history has six distinct first-token targets. Full teacher100% is impossible. Before any CUDA/learning, correct the diagnostic criterion to exact original suffix after the existing fixed24-token prefix; train on unchanged full originals and retain all full-target scores. This changes no Base gates, source, optimizer, budget or decoder." |
| GPU_learning_started | false |
| GPU_seconds | 0 |
| diagnostic_learning_teacher_tokens | 0 |

</details>

<details>
<summary>reports/phase6/base_residual_capacity_pre_condition_fixture_config.json — None</summary>

[原記録](../../reports/phase6/base_residual_capacity_pre_condition_fixture_config.json) ／ SHA256: `e391509d481e4bd36ec4c1750b6a387101832223486dfc87f2333c91cbf50fb6` ／ 5,050 bytes

| 原キー | 保存値 |
|---|---|
| CPU_tests.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_residual_capacity_runner_tests.xml" |
| CPU_tests.sha256 | "fe734f7de969b214e3e70e0fe0c6c796f681b117b46deb1ba90d00a658105c36" |
| source_sha256.tests/test_base_parallel_residual_run.py | "f11e036a7cd1bebf7fdedf8bc43456a602f4e354ef09d610811ecbf7dd2d994c" |
| source_sha256.scripts/base_native_teacher_KD_trainer.py | "644cd0b0ec57df31d927918e8be9adb04e4cbd24a54c900b4374fbad14ef2033" |
| source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.tests/test_base_residual_seen_train.py | "72f4e61d5765a6a6514cb22396a5a41e916459fd92084f93c1c290be1ab8679d" |
| source_sha256.scripts/run_base_residual_capacity.py | "0cd62511fd36b52b425cf2ff0ca175bcb7d40a55264ed112a0259006bc934887" |
| source_sha256.scripts/run_base_residual_capacity.ps1 | "2f2d6aecb358da6720dc0a920b5a0366a1a26572ef5a44f1a9b4f840489efa55" |
| source_sha256.tests/test_base_residual_capacity.py | "3048d46e782c08ab2f5a456b8fdff684968c43d28deea628c69408a07cc514da" |
| max_teacher_tokens | 3000000 |
| GPU_budget_seconds | 300 |
| checkpoint_every_updates | 25 |
| tokenizer | "artifacts/phase2/4096/tokenizer.model" |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_consumed_unit_provenance.json — CPU_consumed_index_provenance_complete</summary>

[原記録](../../reports/phase6/base_residual_consumed_unit_provenance.json) ／ SHA256: `fb94d12c397b7884d21a500a7796a064e7ea69b9389411e0f03eeca6f271870d` ／ 575,236 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_consumed_index_provenance_complete" |
| CPU_seconds | 0.19876069600286428 |
| actual_completed_updates | 8 |
| teacher_tokens_by_source.web | 59121 |
| teacher_tokens_by_source.textbook | 15831 |
| teacher_tokens_by_source.story | 3982 |
| teacher_tokens_by_source_and_unit_kind.web:original-whole | 10908 |
| teacher_tokens_by_source_and_unit_kind.textbook:intact-paragraph-first32 | 15831 |
| teacher_tokens_by_source_and_unit_kind.story:original-whole | 3982 |
| teacher_tokens_by_source_and_unit_kind.web:intact-paragraph-first32 | 48213 |
| Web_teachers | 59121 |
| Web_paragraph_unit_teachers | 48213 |
| Web_paragraph_unit_teacher_fraction | 0.8154970315116457 |
| Web_noninitial_source_slice_teachers | 43508 |
| Web_noninitial_source_slice_teacher_fraction | 0.7359144804722518 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| GPU_seconds | 0 |
| Base_complete | false |
| interpretation | "Metadata enrichment of the already-bound initial actual updates, not a global corpus/near-duplicate/content audit. Paragraph-unit prevalence and omitted context do not themselves establish a cause of poor generation. Original source offsets enable a separate bounded same-target context diagnostic without rescanning the corpus." |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_comparison_completion.json — fixed_dropout100M_complete_rejected_Base_incomplete</summary>

[原記録](../../reports/phase6/base_residual_dropout_comparison_completion.json) ／ SHA256: `2b9bc2aa77b9077b478ee025ea476433347fa539bfc177246a3dfe0a3e515c84` ／ 13,260 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_dropout100M_complete_rejected_Base_incomplete" |
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-dropout-comparison-20261007/dropout/checkpoint-00017698.pt" |
| checkpoint.sha256 | "803127cef3b486b113baf7bf5fb4ba6f440cf25fbe33677423ce8d6c068b67ba" |
| GPU_occupancy_seconds | 1467.6673003619944 |
| GPU_budget_seconds | 3965 |
| new_scientific_CE_teacher_tokens | 100000000 |
| reused_control_CE_teacher_tokens | 100000000 |
| reused_control_GPU_seconds | 0 |
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
| summaries.dropout.BPB | 1.023868636287589 |
| summaries.dropout.rates.eos | 13 |
| summaries.dropout.rates.repetition | 43 |
| summaries.dropout.rates.unicode_failure | 0 |
| summaries.dropout.rates.role_leak | 0 |
| summaries.dropout.rates.empty | 0 |
| summaries.dropout.grammar2 | 55 |
| summaries.dropout.relevance2 | 21 |
| summaries.dropout.coherent | 1 |
| summaries.dropout.appropriate | 1 |
| summaries.dropout.notes_sha256 | "e12d8867a788ab3a1fe60d4b845a9a4e243b2b5519b3332a27ec45eccd2c84a4" |
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
| strong_and_matched_quality.CE.checks.EOS_nonworsening | false |
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
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.025381473773744036 |
| paired_common_byte_BPB.CE.ci95 | [0.023991309983611684, 0.026814997117567702] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.023868636287589 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0254199299967386 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "dropout minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.dropout.exact_content_pair_clusters | 96 |
| exact_content_semantics.dropout.original_nominal_accuracy.point | 0.6041666666666666 |
| exact_content_semantics.dropout.original_nominal_accuracy.ci95 | [0.546875, 0.6614583333333334] |
| exact_content_semantics.dropout.original_nominal_accuracy.units | 96 |
| exact_content_semantics.dropout.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.dropout.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.dropout.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.dropout.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.dropout.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.content_cluster_accuracy.point | 0.6041666666666666 |
| exact_content_semantics.dropout.content_cluster_accuracy.ci95 | [0.546875, 0.6614583333333334] |
| exact_content_semantics.dropout.content_cluster_accuracy.units | 96 |
| exact_content_semantics.dropout.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.dropout.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.dropout.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.dropout.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.dropout.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.both_contexts_hard_correct.point | 0.2916666666666667 |
| exact_content_semantics.dropout.both_contexts_hard_correct.ci95 | [0.20833333333333334, 0.3854166666666667] |
| exact_content_semantics.dropout.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.dropout.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.dropout.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.dropout.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.dropout.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.dropout.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.causality.seed | 42 |
| exact_content_semantics.dropout.categories.causality.repetitions | 2000 |
| exact_content_semantics.dropout.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.comparison.seed | 42 |
| exact_content_semantics.dropout.categories.comparison.repetitions | 2000 |
| exact_content_semantics.dropout.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.coreference.seed | 42 |
| exact_content_semantics.dropout.categories.coreference.repetitions | 2000 |
| exact_content_semantics.dropout.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.negation.seed | 42 |
| exact_content_semantics.dropout.categories.negation.repetitions | 2000 |
| exact_content_semantics.dropout.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.quantity.seed | 42 |
| exact_content_semantics.dropout.categories.quantity.repetitions | 2000 |
| exact_content_semantics.dropout.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.time.seed | 42 |
| exact_content_semantics.dropout.categories.time.repetitions | 2000 |
| exact_content_semantics.dropout.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | -0.020833333333333332 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.07291666666666667, 0.03125] |
| exact_content_semantics.paired.CE.candidate_minus_control.units | 96 |
| exact_content_semantics.paired.CE.candidate_minus_control.examples | 192 |
| exact_content_semantics.paired.CE.candidate_minus_control.unit | "family/prompt" |
| exact_content_semantics.paired.CE.candidate_minus_control.seed | 42 |
| exact_content_semantics.paired.CE.candidate_minus_control.repetitions | 2000 |
| exact_content_semantics.paired.CE.candidate_minus_control.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.exact_content_pair_clusters | 96 |
| exact_content_semantics.paired.CE.cases | 192 |
| exact_content_semantics.paired.CE.new_acceptance_gate | false |
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
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| fixed_recipe_closed | true |
| UI_restored.model.training_tokens | 10000007168 |
| UI_restored.model.update | 305176 |
| UI_restored.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI_restored.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI_restored.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| archive.bytes | 103603956 |
| archive.compressed_bundle.bytes | 49205820 |
| archive.compressed_bundle.lossless | true |
| archive.compressed_bundle.compression_CPU_wall_seconds | 1.4044143990031444 |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_comparison_review.json — new80_and_reused80_dropout_comparison_reviewed</summary>

[原記録](../../reports/phase6/base_residual_dropout_comparison_review.json) ／ SHA256: `14cefdcd35658501fb85531ce29d9a1b49b728018f96a2287ba83a15a9979579` ／ 11,683 bytes

| 原キー | 保存値 |
|---|---|
| status | "new80_and_reused80_dropout_comparison_reviewed" |
| summaries.dropout.BPB | 1.023868636287589 |
| summaries.dropout.rates.eos | 13 |
| summaries.dropout.rates.repetition | 43 |
| summaries.dropout.rates.unicode_failure | 0 |
| summaries.dropout.rates.role_leak | 0 |
| summaries.dropout.rates.empty | 0 |
| summaries.dropout.grammar2 | 55 |
| summaries.dropout.relevance2 | 21 |
| summaries.dropout.coherent | 1 |
| summaries.dropout.appropriate | 1 |
| summaries.dropout.notes_sha256 | "e12d8867a788ab3a1fe60d4b845a9a4e243b2b5519b3332a27ec45eccd2c84a4" |
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
| strong_and_matched_quality.CE.checks.EOS_nonworsening | false |
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
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | false |
| paired_common_byte_BPB.CE.point | 0.025381473773744036 |
| paired_common_byte_BPB.CE.ci95 | [0.023991309983611684, 0.026814997117567702] |
| paired_common_byte_BPB.CE.documents | 256 |
| paired_common_byte_BPB.CE.common_bytes | 472055 |
| paired_common_byte_BPB.CE.control_BPB | 0.998487162513845 |
| paired_common_byte_BPB.CE.target_BPB | 1.023868636287589 |
| paired_common_byte_BPB.CE.relative_ratio | 1.0254199299967386 |
| paired_common_byte_BPB.CE.degradation_ci_lower_above0 | true |
| paired_common_byte_BPB.CE.seed | 42 |
| paired_common_byte_BPB.CE.repetitions | 2000 |
| paired_common_byte_BPB.CE.direction | "dropout minus completed CE; positive means worse" |
| paired_common_byte_BPB.CE.note | "Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit" |
| exact_content_semantics.dropout.exact_content_pair_clusters | 96 |
| exact_content_semantics.dropout.original_nominal_accuracy.point | 0.6041666666666666 |
| exact_content_semantics.dropout.original_nominal_accuracy.ci95 | [0.546875, 0.6614583333333334] |
| exact_content_semantics.dropout.original_nominal_accuracy.units | 96 |
| exact_content_semantics.dropout.original_nominal_accuracy.examples | 192 |
| exact_content_semantics.dropout.original_nominal_accuracy.unit | "family/prompt" |
| exact_content_semantics.dropout.original_nominal_accuracy.seed | 42 |
| exact_content_semantics.dropout.original_nominal_accuracy.repetitions | 2000 |
| exact_content_semantics.dropout.original_nominal_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.content_cluster_accuracy.point | 0.6041666666666666 |
| exact_content_semantics.dropout.content_cluster_accuracy.ci95 | [0.546875, 0.6614583333333334] |
| exact_content_semantics.dropout.content_cluster_accuracy.units | 96 |
| exact_content_semantics.dropout.content_cluster_accuracy.examples | 192 |
| exact_content_semantics.dropout.content_cluster_accuracy.unit | "family/prompt" |
| exact_content_semantics.dropout.content_cluster_accuracy.seed | 42 |
| exact_content_semantics.dropout.content_cluster_accuracy.repetitions | 2000 |
| exact_content_semantics.dropout.content_cluster_accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.both_contexts_hard_correct.point | 0.2916666666666667 |
| exact_content_semantics.dropout.both_contexts_hard_correct.ci95 | [0.20833333333333334, 0.3854166666666667] |
| exact_content_semantics.dropout.both_contexts_hard_correct.units | 96 |
| exact_content_semantics.dropout.both_contexts_hard_correct.examples | 96 |
| exact_content_semantics.dropout.both_contexts_hard_correct.unit | "family/prompt" |
| exact_content_semantics.dropout.both_contexts_hard_correct.seed | 42 |
| exact_content_semantics.dropout.both_contexts_hard_correct.repetitions | 2000 |
| exact_content_semantics.dropout.both_contexts_hard_correct.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.causality.seed | 42 |
| exact_content_semantics.dropout.categories.causality.repetitions | 2000 |
| exact_content_semantics.dropout.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.comparison.seed | 42 |
| exact_content_semantics.dropout.categories.comparison.repetitions | 2000 |
| exact_content_semantics.dropout.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.coreference.seed | 42 |
| exact_content_semantics.dropout.categories.coreference.repetitions | 2000 |
| exact_content_semantics.dropout.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.negation.seed | 42 |
| exact_content_semantics.dropout.categories.negation.repetitions | 2000 |
| exact_content_semantics.dropout.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.quantity.seed | 42 |
| exact_content_semantics.dropout.categories.quantity.repetitions | 2000 |
| exact_content_semantics.dropout.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.dropout.categories.time.seed | 42 |
| exact_content_semantics.dropout.categories.time.repetitions | 2000 |
| exact_content_semantics.dropout.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| exact_content_semantics.paired.CE.candidate_minus_control.point | -0.020833333333333332 |
| exact_content_semantics.paired.CE.candidate_minus_control.ci95 | [-0.07291666666666667, 0.03125] |
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
| probe_verification_CE_teachers | 220036 |
| GPU_occupancy_seconds | 1467.6673003619944 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| final_seed_full_dev_test_adoption_pending | true |
| limitations | "Single learned seed, repeated nonblind DEV, same native parameters/CE input and teacher stream; training dropout/GPU overhead differs. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored." |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_comparison_start.json — actual_scientific_dropout_training_alive</summary>

[原記録](../../reports/phase6/base_residual_dropout_comparison_start.json) ／ SHA256: `93ea9d4786e02d96bdf738fa3160a5677bb8649e15c28a3e7596c234a307499f` ／ 2,208 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_scientific_dropout_training_alive" |
| scientific_CE_teacher_tokens_at_check | 3394390 |
| completed_updates_at_check | 600 |
| finite_loss_at_check | 3.037971258163452 |
| scientific_teacher_goal | 100000000 |
| GPU_budget_seconds | 3965 |
| forecast_training_seconds | 2243.2025923009955 |
| source_teacher_goals.web | 75000000 |
| source_teacher_goals.textbook | 20000000 |
| source_teacher_goals.story | 5000000 |
| reused_control_CE_teachers | 100000000 |
| reused_control_GPU_seconds | 0 |
| artifacts.checkpoints | "dropout/checkpoint-xxxxxxxx.pt" |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_content_review.json — None</summary>

[原記録](../../reports/phase6/base_residual_dropout_content_review.json) ／ SHA256: `feeb63c6ac7cc613eadff4e1c12fc673cff54f12b2063d5681537b0ef0981d1e` ／ 733 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.023868636287589 |
| rates.eos | 13 |
| rates.repetition | 43 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 55 |
| relevance2 | 21 |
| coherent | 1 |
| appropriate | 1 |
| notes_sha256 | "e12d8867a788ab3a1fe60d4b845a9a4e243b2b5519b3332a27ec45eccd2c84a4" |
| scope | "new80_content_only_final_comparison_pending" |
| Base_complete | false |
| scientific_CE_teacher_tokens | 100000000 |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_launcher_result.json — complete</summary>

[原記録](../../reports/phase6/base_residual_dropout_launcher_result.json) ／ SHA256: `3542db959b2752ddc700023c399abe2b1d21eaaaefcc15afea2483d6e3bce16d` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_notes.json — None</summary>

[原記録](../../reports/phase6/base_residual_dropout_notes.json) ／ SHA256: `e12d8867a788ab3a1fe60d4b845a9a4e243b2b5519b3332a27ec45eccd2c84a4` ／ 21,850 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/base_residual_dropout_probe_completion.json — actual_training_only_dropout_probe_passed_science_ready</summary>

[原記録](../../reports/phase6/base_residual_dropout_probe_completion.json) ／ SHA256: `eb468f6f7f6bd2abc6c3cc1436d534dc1e0dee1a4a15b7f390da04f569cfeca4` ／ 4,436 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_training_only_dropout_probe_passed_science_ready" |
| CPU_protocol_checks | 5 |
| CPU_protocol_seconds | 2.96 |
| CPU_run_checks | 3 |
| CPU_run_seconds | 1.32 |
| GPU_seconds | 9.546564576012315 |
| GPU_limit_seconds | 180 |
| initial_checks.native_weights | true |
| initial_checks.native_parameters | true |
| initial_checks.native_tied | true |
| initial_checks.initialization_RNG | true |
| initial_checks.training_sites | true |
| initial_checks.native_logits | true |
| initial_checks.inference_RNG_unchanged | true |
| initial_checks.training_masks_active | true |
| resume_checks.kind | true |
| resume_checks.spec | true |
| resume_checks.binding | true |
| resume_checks.lineage | true |
| resume_checks.model_config | true |
| resume_checks.model | true |
| resume_checks.optimizer | true |
| resume_checks.scheduler | true |
| resume_checks.RNG | true |
| resume_checks.sampler | true |
| resume_checks.counters | true |
| resume_checks.finite | true |
| resume_checks.all_history_except_timing | true |
| verification_updates | 44 |
| verification_CE_teacher_tokens | 220036 |
| capacity.16.passed | true |
| capacity.16.peak_VRAM_bytes | 3837475840 |
| capacity.16.context | 1024 |
| capacity.16.loss | 3.281668186187744 |
| capacity.16.gradient_norm | 20.508241653442383 |
| capacity.16.optimizer_updates | 0 |
| capacity.16.teachers | 8192 |
| capacity.16.physical_input_tokens | 16384 |
| capacity.32.passed | true |
| capacity.32.peak_VRAM_bytes | 7465794560 |
| capacity.32.context | 1024 |
| capacity.32.loss | 2.949056386947632 |
| capacity.32.gradient_norm | 5.2433600425720215 |
| capacity.32.optimizer_updates | 0 |
| capacity.32.teachers | 16384 |
| capacity.32.physical_input_tokens | 32768 |
| capacity.48.passed | true |
| capacity.48.peak_VRAM_bytes | 11095129088 |
| capacity.48.context | 1024 |
| capacity.48.loss | 3.3149211406707764 |
| capacity.48.gradient_norm | 8.63879108428955 |
| capacity.48.optimizer_updates | 0 |
| capacity.48.teachers | 24576 |
| capacity.48.physical_input_tokens | 49152 |
| capacity.64.passed | true |
| capacity.64.peak_VRAM_bytes | 14724463616 |
| capacity.64.context | 1024 |
| capacity.64.loss | 3.2554516792297363 |
| capacity.64.gradient_norm | 7.758731842041016 |
| capacity.64.optimizer_updates | 0 |
| capacity.64.teachers | 32768 |
| capacity.64.physical_input_tokens | 65536 |
| timings.16.median_CE_targets_per_second | 16206.0068359375 |
| timings.16.samples | [15497.996148400767, 11631.452093649006, 23097.42484752375, 22154.06492544513, 16206.00718977863] |
| timings.32.median_CE_targets_per_second | 23900.125 |
| timings.32.samples | [28210.169912812737, 23739.40237930112, 23900.12461117922, 26022.526978348345, 20387.039875750263] |
| timings.48.median_CE_targets_per_second | 44579.12109375 |
| timings.48.samples | [91192.06810471634, 75541.42894832653, 32353.501048220878, 44579.12258045542, 38576.80553432277] |
| timings.64.median_CE_targets_per_second | 58060.19140625 |
| timings.64.samples | [62936.584301387426, 99567.88568774423, 58060.192246067476, 43969.88793905881, 41783.34958864278] |
| measured_fastest_resident_batch | 64 |
| matched_scientific_batch | 48 |
| scientific_CE_teacher_tokens | 0 |
| archive.bytes | 716702 |
| UI_restored_before_science.actual_ps_checked_before_scientific_launch | true |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_proposal.json — single_training_only_dropout_hypothesis_before_GPU</summary>

[原記録](../../reports/phase6/base_residual_dropout_proposal.json) ／ SHA256: `782f8179915c876ffdfee42ef2948115e7a5ceb4e0cd77b5c37ca3388311de35` ／ 3,038 bytes

| 原キー | 保存値 |
|---|---|
| status | "single_training_only_dropout_hypothesis_before_GPU" |
| CPU_protocol_limit_seconds | 30 |
| GPU_probe_limit_seconds | 180 |
| scientific_teacher_tokens_proposed | 100000000 |
| hypothesis | "Previously learned original TRAIN targets can fit substantially better without held-out generation transfer. Training-only embedding/residual dropout may reduce co-adaptation and transfer better into the same native predictive vocabulary distribution; success in this Japanese10M setting is unproven." |
| primary_limitation | "General supervised dropout research; not evidence that Japanese10M Base generation or EOS will improve." |
| comparison_completion | "Actual exact100M completed native full-state; same full CE accounting/digest/cursor as cached CE; full Japanese/DEV256 common-byte BPB/new generation80 individual notes, reused CE80 and original strong/Web retention/absolute gates; actual process ended, restored original UI, evidence and commit." |
| probe_completion | "CPU tests then actual finite CUDA/BF16, initial native evaluation/RNG equivalence, training stochastic masks, continuous4 versus2-save-resume2 all state/history, longest1024 window resident capacity and measured source speed. Discard all probe weights." |
| budget_policy | "Freeze scientific GPU budget only after actual matched batch48 throughput and worst-context capacity, with checkpoint/evaluation allowance. Implement persistent scientific command/reviewer first." |
| failed_condition_policy | "Close fixed probability/sites if qualification fails. No probability/sites/LR/source/epoch/head sweep or automatic extension." |
| Base_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/base_residual_dropout_review_initial_API_failure.json — CPU_ad_hoc_cached_API_preflight_failure_preserved</summary>

[原記録](../../reports/phase6/base_residual_dropout_review_initial_API_failure.json) ／ SHA256: `bafada7cd04eee404c86f6954653b2b592ee84fb91b565263e0e2992cb714965` ／ 620 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_ad_hoc_cached_API_preflight_failure_preserved" |
| reason | "Preparation-only caller looked for top-level point in semantic paired result; helper returns candidate_minus_control containing point/ci95." |
| GPU_seconds | 0 |
| new_teacher_tokens | 0 |
| scientific_source_changed | false |
| repair | "Read candidate_minus_control in the ad-hoc caller. The reviewer already saves the complete nested return without this mistaken indexing." |

</details>

<details>
<summary>reports/phase6/base_residual_failure_pair_diagnostic.json — all80_paired_existing_generation_failures_classified</summary>

[原記録](../../reports/phase6/base_residual_failure_pair_diagnostic.json) ／ SHA256: `c594226cbc1439521c3898d22d9e27b4cf931c0a5f38b25f3ccc8d11753db85b` ／ 150,102 bytes

| 原キー | 保存値 |
|---|---|
| status | "all80_paired_existing_generation_failures_classified" |
| inputs.strong_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_order_condition_notes.json" |
| inputs.strong_notes.sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| inputs.sequential_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_sequential_notes.json" |
| inputs.sequential_notes.sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |
| CPU_seconds | 0.012416926998412237 |
| GPU_seconds | 0 |
| generated_tokens | 0 |
| scientific_teacher_tokens | 0 |
| optimizer_updates | 0 |
| summaries.strong.eos | 76 |
| summaries.strong.grammar2 | 65 |
| summaries.strong.coherence2 | 23 |
| summaries.strong.appropriate | 26 |
| summaries.strong.nonprogressive_repetition | 6 |
| summaries.strong.automatic_repetition | 2 |
| summaries.sequential.eos | 20 |
| summaries.sequential.grammar2 | 23 |
| summaries.sequential.coherence2 | 3 |
| summaries.sequential.appropriate | 7 |
| summaries.sequential.nonprogressive_repetition | 64 |
| summaries.sequential.automatic_repetition | 27 |
| classification_definitions.nonprogressive_repetition | "Same event, phrase or explanatory relation repeated without new progression; semantic paraphrases count. A repeated condition followed by its justified outcome or one echo before genuine new information alone does not count. Diagnostic observation, not a replacement for the original automatic repetition metric." |
| acceptance_criteria_changed | false |
| model_history.strong.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| model_history.strong.tokens | 10600546304 |
| model_history.strong.binding.teacher_goals.web | 75000000 |
| model_history.strong.binding.teacher_goals.story | 5000000 |
| model_history.strong.binding.teacher_goals.ordinary_textbook | 10000000 |
| model_history.strong.binding.teacher_goals.conditional_textbook | 10000000 |
| model_history.strong.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| model_history.strong.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| model_history.sequential.training_seed | 42 |
| limitations | "Posthoc nonblind descriptive labels from already-reused DEV. Manual repetition is not an independent ground-truth detector benchmark. Maintained does not mean overall coherent, and unresolved does not assert a literal contradiction. Training histories differ, so this is not a causal architecture or quantity comparison. No score/gate replacement." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_scored | false |

</details>

<details>
<summary>reports/phase6/base_residual_failure_pair_notes.json — None</summary>

[原記録](../../reports/phase6/base_residual_failure_pair_notes.json) ／ SHA256: `26f9e48b581990c3e69f5fe391e96547c7edf3ac127cbbbff53af95fc90c8be9` ／ 25,896 bytes

| 原キー | 保存値 |
|---|---|
| definitions.nonprogressive_repetition | "Same event, phrase or explanatory relation repeated without new progression; semantic paraphrases count. A repeated condition followed by its justified outcome or one echo before genuine new information alone does not count. Diagnostic observation, not a replacement for the original automatic repetition metric." |
| inputs.strong_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_order_condition_notes.json" |
| inputs.strong_notes.sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| inputs.sequential_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base_parallel_residual_sequential_notes.json" |
| inputs.sequential_notes.sha256 | "4a65fa58b63910688b3e3b09165b9b7906e522c0b7dde54d67c2eb0ee85be1a7" |

</details>
