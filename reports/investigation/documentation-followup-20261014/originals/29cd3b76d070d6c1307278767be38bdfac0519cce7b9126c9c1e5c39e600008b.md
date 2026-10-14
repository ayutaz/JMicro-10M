# 学習量・配合・学習順序 — 6/6

[分野一覧へ](03_learning.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/story20_low_lr_result.json — complete_pending_content_review</summary>

[原記録](../../reports/phase6/story20_low_lr_result.json) ／ SHA256: `f97c9d1ccb761945009cbaea1766f3c83732638b997e6ae16f00216d701498d2` ／ 83,033 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_content_review" |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| trained.status | "complete" |
| trained.binding.parent.update | 305176 |
| trained.binding.parent.tokens_seen | 10000007168 |
| trained.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| trained.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| trained.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| trained.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| trained.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| trained.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| trained.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| trained.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/coherent20/checkpoint-00308228.pt" |
| trained.checkpoint_sha256 | "adf0fd48524ee44e62bf9dfc8538ce9b6c5584d63eb0bb44ed211041b37188ba" |
| trained.update | 308228 |
| trained.tokens | 10100015104 |
| trained.additional_input_tokens | 100007936 |
| trained.training_seconds | 159.27653573100542 |
| trained.source_tokens.web | 80019456 |
| trained.source_tokens.short | 19988480 |
| trained.source_eos_teachers.web | 169362 |
| trained.source_eos_teachers.short | 221003 |
| trained.sampler.kind | "eos-pilot-mixture-v1" |
| trained.sampler.position | 3052 |
| trained.sampler.web.seed | 42 |
| trained.sampler.web.epoch | 0 |
| trained.sampler.web.position | 9843776 |
| trained.sampler.web.context | 1024 |
| trained.sampler.web.blocks | 11939276 |
| trained.sampler.short.seed | 42 |
| trained.sampler.short.epoch | 0 |
| trained.sampler.short.position | 19520 |
| trained.sampler.short.context | 1024 |
| trained.sampler.short.blocks | 24414 |
| trained.sampler.source_tokens.web | 80019456 |
| trained.sampler.source_tokens.short | 19988480 |
| trained.sampler.source_eos.web | 169362 |
| trained.sampler.source_eos.short | 221003 |
| rates.eos | 23 |
| rates.repetition | 22 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| screen_BPB | 0.984032484988207 |
| diagnostics.semantics.primary.accuracy.point | 0.6510416666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5989583333333334, 0.703125] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.6510416666666666 |
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
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.608855086242021 |
| diagnostics.semantics.per_token_secondary.mcc | 0.21933385865209304 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7492447129909365 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7039274924471299, 0.7945619335347432] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7492447129909365 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7643504531722054] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7613293051359517 |
| diagnostics.jcqa.primary.accuracy.point | 0.34405719392314565 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3154602323503128, 0.3708668453976765] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.34405719392314565 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3145665773011618 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2868632707774799, 0.34226988382484363] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3145665773011618 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3133467829915494 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.14338033820939985 |
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
| diagnostics.semantic_both_contexts.correct | 31 |
| mixture.EOS_at_least8_more | true |
| mixture.repetition_no_worse | true |
| mixture.no_empty_role_unicode | true |
| mixture.BPB_degradation_at_most1percent | true |
| resume_gate.passed | true |
| resume_gate.checks.model | true |
| resume_gate.checks.optimizer | true |
| resume_gate.checks.scheduler | true |
| resume_gate.checks.rng | true |
| resume_gate.checks.sampler | true |
| resume_gate.checks.tokens | true |
| resume_gate.checks.supervised_tokens | true |
| resume_gate.checks.body_bytes | true |
| resume_gate.checks.token_digest | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.model_config | true |
| resume_gate.checks.implementation_sha256 | true |
| resume_gate.checks.pilot_implementation_sha256 | true |
| resume_gate.checks.pilot_binding | true |
| resume_gate.checks.update | true |
| resume_gate.checks.lineage | true |
| resume_gate.checks.history_loss | true |
| resume_gate.checks.history_gradient_norm | true |
| resume_gate.checks.history_lr | true |
| resume_gate.checks.history_tokens_seen | true |
| resume_gate.checks.history_supervised_tokens | true |
| resume_gate.checks.history_body_bytes_seen | true |
| resume_gate.checks.history_token_digest | true |
| resume_gate.checks.finite_losses_gradients | true |
| resume_gate.checks.two_short_two_web_updates | true |
| resume_gate.binding.parent.update | 305176 |
| resume_gate.binding.parent.tokens_seen | 10000007168 |
| resume_gate.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| resume_gate.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| resume_gate.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| resume_gate.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| resume_gate.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| resume_gate.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| resume_gate.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| resume_gate.seconds | 10.854466021999542 |
| resume_gate.GPU_optimizer_updates | 8 |
| resume_gate.input_tokens | 262144 |
| resume_gate.schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| resume_gate.checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/resume-gate/resumed.pt"] |
| scientific_tokens | 100007936 |
| verification_tokens | 262144 |
| protected_test_used | false |
| GPU_seconds | 262.54340427699935 |

</details>

<details>
<summary>reports/phase6/story20_low_lr_review.json — passed</summary>

[原記録](../../reports/phase6/story20_low_lr_review.json) ／ SHA256: `5333432e4568d191a02371bd30279605c23cc182ef82e0c7503abdd64a9a4c49` ／ 129,709 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-05T00:11:35.681533Z" |
| selection.original_mixture.EOS_at_least8_more | true |
| selection.original_mixture.repetition_no_worse | true |
| selection.original_mixture.no_empty_role_unicode | true |
| selection.original_mixture.BPB_degradation_at_most1percent | true |
| selection.coherence_gain_at_least8 | true |
| selection.paired_coherence_CI_lower_above0 | true |
| selection.coherence_difference_count | 12 |
| selection.paired_CI95 | [0.075, 0.2375] |
| selection.eligible_for_full | true |
| summary.grammar_score2 | 66 |
| summary.relevance_score2 | 15 |
| summary.coherence_score2 | 12 |
| summary.appropriate_EOS | 12 |
| paired_diagnostics.semantics.point | 0.041666666666666664 |
| paired_diagnostics.semantics.ci95 | [0.005208333333333333, 0.08333333333333333] |
| paired_diagnostics.semantics.units | 96 |
| paired_diagnostics.semantics.examples | 192 |
| paired_diagnostics.semantics.unit | "family/prompt" |
| paired_diagnostics.semantics.seed | 42 |
| paired_diagnostics.semantics.repetitions | 2000 |
| paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jblimp.point | 0.012084592145015106 |
| paired_diagnostics.jblimp.ci95 | [-0.015105740181268883, 0.03927492447129909] |
| paired_diagnostics.jblimp.units | 331 |
| paired_diagnostics.jblimp.examples | 331 |
| paired_diagnostics.jblimp.unit | "family/prompt" |
| paired_diagnostics.jblimp.seed | 42 |
| paired_diagnostics.jblimp.repetitions | 2000 |
| paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jcqa.point | 0.032171581769437 |
| paired_diagnostics.jcqa.ci95 | [0.010723860589812333, 0.05183199285075961] |
| paired_diagnostics.jcqa.units | 1119 |
| paired_diagnostics.jcqa.examples | 1119 |
| paired_diagnostics.jcqa.unit | "family/prompt" |
| paired_diagnostics.jcqa.seed | 42 |
| paired_diagnostics.jcqa.repetitions | 2000 |
| paired_diagnostics.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| scientific_tokens | 100007936 |
| verification_tokens | 262144 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/story_weight_story20_notes.json — None</summary>

[原記録](../../reports/phase6/story_weight_story20_notes.json) ／ SHA256: `c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371` ／ 16,205 bytes

| 原キー | 保存値 |
|---|---|

</details>
