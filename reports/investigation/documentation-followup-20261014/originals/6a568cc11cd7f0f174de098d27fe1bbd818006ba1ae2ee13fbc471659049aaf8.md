# 構成・反復計算・容量 — 6/7

[分野一覧へ](05_architecture.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/evaluation/readout_adapter/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/evaluation/readout_adapter/evaluation/result.json) ／ SHA256: `f18b93460a0109d1362f23f999cff5bf249ed39dd89c245e413434dd02630f6a` ／ 187,627 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.policy.initialization_seed | 2026100651 |
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 337985.41487693787 |
| body.eos_nll | 517.2182487361133 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 1.0329514186604467 |
| body.seconds | 1.417319989996031 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 46 |
| greedy_rates.repetition | 24 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5364583333333334, 0.6095052083333327] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6145833333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5712418300653594 |
| diagnostics.semantics.per_token_secondary.mcc | 0.1469861839480328 |
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
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7009063444108762, 0.7946374622356491] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7492447129909365 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7734138972809668] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
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
| diagnostics.jcqa.primary.accuracy.point | 0.35031277926720283 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3243744414655943, 0.37803842716711333] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.35031277926720283 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28418230563002683, 0.3360142984807864] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30884198292554615 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.13764427437008395 |
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
| memory.maximum_observed_allocated_bytes | 236000256 |
| memory.maximum_observed_reserved_bytes | 9600761856 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/evaluation/readout_adapter/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/evaluation/readout_adapter/evaluation/semantics.json) ／ SHA256: `e4d0775058bf7c355977a5019acf0be21d7fcc1c82c244dfbb93650c0805239f` ／ 203,701 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5729166666666666 |
| summary.primary.accuracy.ci95 | [0.5364583333333334, 0.6095052083333327] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5729166666666666 |
| summary.per_token_secondary.accuracy.point | 0.5729166666666666 |
| summary.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6145833333333334] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| summary.per_token_secondary.macro_f1 | 0.5712418300653594 |
| summary.per_token_secondary.mcc | 0.1469861839480328 |
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
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/job.json) ／ SHA256: `7e0df35986835e1d2f672802197fb77d86059336c678627adb666183b21b0085` ／ 875 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 155.12132066098275 |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| loss | 0.28425660729408264 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/probe/job.json) ／ SHA256: `4bf4b7d04479fe07fe881dda5b167b244925a4ded70f11c36617ced08ff90d41` ／ 581 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 23.46177612899919 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/probe/latest.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/probe/latest.json) ／ SHA256: `7216b49977fb166d9a0b0640be51aba4f1d90301dc97d80c40316bfcfc9361a3` ／ 261 bytes

| 原キー | 保存値 |
|---|---|
| update | 323535 |
| tokens_seen | 10601594880 |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/probe/result.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/probe/result.json) ／ SHA256: `a848eab54500ef077df44a76753edbe8081ac5133ca68a9f2f9d49916c6bd8bb` ／ 78,678 bytes

| 原キー | 保存値 |
|---|---|
| architecture.checks.FP32_32.max_absolute_error | 0.0 |
| architecture.checks.FP32_32.absolute_tolerance | 2e-06 |
| architecture.checks.FP32_32.relative_tolerance | 2e-06 |
| architecture.checks.FP32_32.passed | true |
| architecture.checks.FP32_1024.max_absolute_error | 0.0 |
| architecture.checks.FP32_1024.absolute_tolerance | 2e-06 |
| architecture.checks.FP32_1024.relative_tolerance | 2e-06 |
| architecture.checks.FP32_1024.passed | true |
| architecture.checks.BF16_32.max_absolute_error | 0.0 |
| architecture.checks.BF16_32.absolute_tolerance | 0.0 |
| architecture.checks.BF16_32.relative_tolerance | 0.0 |
| architecture.checks.BF16_32.passed | true |
| architecture.checks.BF16_1024.max_absolute_error | 0.0 |
| architecture.checks.BF16_1024.absolute_tolerance | 0.0 |
| architecture.checks.BF16_1024.relative_tolerance | 0.0 |
| architecture.checks.BF16_1024.passed | true |
| architecture.checks.nonzero_cache1024.max_absolute_error | 1.430511474609375e-05 |
| architecture.checks.nonzero_cache1024.absolute_tolerance | 2e-05 |
| architecture.checks.nonzero_cache1024.relative_tolerance | 0.0002 |
| architecture.checks.nonzero_cache1024.passed | true |
| architecture.optimizer_updates | 0 |
| resume_gate.passed | true |
| resume_gate.checks.model | true |
| resume_gate.checks.optimizer | true |
| resume_gate.checks.scheduler | true |
| resume_gate.checks.rng | true |
| resume_gate.checks.sampler | true |
| resume_gate.checks.lineage | true |
| resume_gate.checks.tokens | true |
| resume_gate.checks.supervised_tokens | true |
| resume_gate.checks.body_bytes | true |
| resume_gate.checks.token_digest | true |
| resume_gate.checks.focus_token_digest | true |
| resume_gate.checks.focus_teacher_tokens | true |
| resume_gate.checks.weighted_teacher_mass | true |
| resume_gate.checks.update | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.model_config | true |
| resume_gate.checks.pilot_binding | true |
| resume_gate.checks.study_binding | true |
| resume_gate.checks.history_update | true |
| resume_gate.checks.history_loss | true |
| resume_gate.checks.history_gradient_norm | true |
| resume_gate.checks.history_lr | true |
| resume_gate.checks.history_tokens_seen | true |
| resume_gate.checks.history_supervised_tokens | true |
| resume_gate.checks.history_body_bytes_seen | true |
| resume_gate.checks.history_token_digest | true |
| resume_gate.checks.history_focus_token_digest | true |
| resume_gate.checks.history_focus_teacher_tokens | true |
| resume_gate.checks.history_weighted_teacher_mass | true |
| resume_gate.checks.history_outcome_weight | true |
| resume_gate.checks.history_source_teachers | true |
| resume_gate.checks.history_source_eos | true |
| resume_gate.checks.history_source_input_tokens | true |
| resume_gate.checks.history_source_body_bytes | true |
| resume_gate.checks.history_source_focus_teachers | true |
| resume_gate.checks.history_valid_input_tokens | true |
| resume_gate.checks.history_physical_input_tokens | true |
| resume_gate.checks.history_additional_teacher_tokens | true |
| resume_gate.checks.history_CE_loss | true |
| resume_gate.checks.history_parameter_penalty | true |
| resume_gate.checks.history_parameter_coefficient | true |
| resume_gate.checks.history_parameter_penalty_teacher_tokens | true |
| resume_gate.checks.history_native_optimizer_updates | true |
| resume_gate.checks.history_readout_LR | true |
| resume_gate.checks.finite | true |
| resume_gate.checks.fixed_fresh_readout_LR | true |
| resume_gate.GPU_optimizer_updates | 8 |
| resume_gate.verification_teacher_tokens | 261616 |
| timing.verification_teacher_tokens | 1046336 |
| timing.terminal_save_seconds | 0.06181667800410651 |
| timing.peak_VRAM_bytes | 2273370112 |
| timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout-adapter-comparison-v3-20261006/probe/timing.pt" |
| timing.checkpoint.sha256 | "ac14a9722a29c270b7ec03d3e39c532d3e9581f22e89af7f299e4333c83a899f" |
| passed | true |
| GPU_seconds | 23.46177612899919 |
| optimizer_updates | 40 |
| verification_teacher_tokens | 1307952 |
| scientific_teacher_tokens | 0 |
| measured_timing.steady_step_seconds | 0.1248754340049345 |
| measured_timing.teachers_per_update | 32698.0 |
| measured_timing.estimated_updates | 3059 |
| measured_timing.warmup_seconds | 0.8788038779457565 |
| measured_timing.save_seconds | 0.8654334920574911 |
| measured_timing.estimated_training_seconds | 383.7381899910979 |
| previous_failed_GPU_seconds | 0.33271518800756894 |
| estimated_science_GPU_seconds | 798.8596469884274 |
| estimated_total_GPU_seconds | 822.6541383054341 |
| within900_seconds | true |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/progress-result.json) ／ SHA256: `3e9ba2945a871b2159385d9124b187ded7e47089eb3e133191d3652cedfd042a` ／ 650,494 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.readout_adapter.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout-adapter-comparison-v3-20261006/readout_adapter/training/checkpoint-00326571.pt" |
| checkpoints.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| checkpoints.readout_adapter.binding.config_sha256 | "18cc823aeacbd431695bec1a1d445b2599db842c52b375407ebae7380ddcde81" |
| checkpoints.readout_adapter.binding.arm | "readout_adapter" |
| checkpoints.readout_adapter.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| checkpoints.readout_adapter.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| checkpoints.readout_adapter.binding.teacher_goals.web | 75000000 |
| checkpoints.readout_adapter.binding.teacher_goals.story | 5000000 |
| checkpoints.readout_adapter.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.readout_adapter.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.readout_adapter.binding.study_kind | "frozen_decoder_nonlinear_readout_Base_full100M_v1" |
| checkpoints.readout_adapter.binding.parameter_coefficient | 0.0 |
| checkpoints.readout_adapter.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.readout_adapter.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.readout_adapter.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.readout_adapter.binding.policy.kind | "frozen_native_postnorm_silu_residual_readout_v1" |
| checkpoints.readout_adapter.binding.policy.bottleneck_ratio | [3, 4] |
| checkpoints.readout_adapter.binding.policy.native_weights_frozen | true |
| checkpoints.readout_adapter.binding.policy.up_initialization | "exact_zero" |
| checkpoints.readout_adapter.binding.policy.down_initialization | "private_normal_std_0.02" |
| checkpoints.readout_adapter.binding.policy.initialization_seed | 2026100651 |
| checkpoints.readout_adapter.binding.policy.bias | false |
| checkpoints.readout_adapter.binding.policy.dropout | 0.0 |
| checkpoints.readout_adapter.binding.policy.placement | "after_final_RMSNorm_before_tied_vocabulary_matrix" |
| checkpoints.readout_adapter.binding.readout_LR | 0.0001 |
| checkpoints.readout_adapter.binding.optimizer_policy | "fresh_readout_only_native_weights_frozen" |
| checkpoints.readout_adapter.update | 326571 |
| checkpoints.readout_adapter.tokens | 10701078528 |
| checkpoints.readout_adapter.supervised_tokens | 10677786961 |
| checkpoints.readout_adapter.additional_supervised_tokens | 100000000 |
| checkpoints.readout_adapter.additional_input_tokens | 100532224 |
| checkpoints.readout_adapter.source_teachers.web | 75000000 |
| checkpoints.readout_adapter.source_teachers.story | 5000000 |
| checkpoints.readout_adapter.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.readout_adapter.source_teachers.conditional_textbook | 10000000 |
| checkpoints.readout_adapter.source_eos.web | 159447 |
| checkpoints.readout_adapter.source_eos.story | 38240 |
| checkpoints.readout_adapter.source_eos.ordinary_textbook | 74183 |
| checkpoints.readout_adapter.source_eos.conditional_textbook | 234328 |
| checkpoints.readout_adapter.source_input_tokens.web | 75183104 |
| checkpoints.readout_adapter.source_input_tokens.story | 5039104 |
| checkpoints.readout_adapter.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.readout_adapter.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.readout_adapter.source_focus_teachers.web | 0 |
| checkpoints.readout_adapter.source_focus_teachers.story | 0 |
| checkpoints.readout_adapter.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.readout_adapter.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.readout_adapter.focus_teacher_tokens | 1407427 |
| checkpoints.readout_adapter.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.readout_adapter.weighted_teacher_mass | 100000000 |
| checkpoints.readout_adapter.outcome_weight | 1 |
| checkpoints.readout_adapter.training_seconds | 77.97412706623436 |
| checkpoints.readout_adapter.completed_at | "2026-10-06T13:56:36.922115Z" |
| checkpoints.readout_adapter.parameter_coefficient | 0.0 |
| checkpoints.readout_adapter.parameter_penalty_teacher_tokens | 0 |
| checkpoints.readout_adapter.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| checkpoints.readout_adapter.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoints.readout_adapter.sampler.goals.web | 75000000 |
| checkpoints.readout_adapter.sampler.goals.story | 5000000 |
| checkpoints.readout_adapter.sampler.goals.ordinary_textbook | 10000000 |
| checkpoints.readout_adapter.sampler.goals.conditional_textbook | 10000000 |
| checkpoints.readout_adapter.sampler.context | 1024 |
| checkpoints.readout_adapter.sampler.seed | 42 |
| checkpoints.readout_adapter.sampler.position | 3068 |
| checkpoints.readout_adapter.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.readout_adapter.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.readout_adapter.sampler.streams.web.sampler.seed | 42 |
| checkpoints.readout_adapter.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.readout_adapter.sampler.streams.web.sampler.position | 10400762 |
| checkpoints.readout_adapter.sampler.streams.web.sampler.context | 1024 |
| checkpoints.readout_adapter.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.readout_adapter.sampler.streams.story.seed | 42 |
| checkpoints.readout_adapter.sampler.streams.story.genre | "story" |
| checkpoints.readout_adapter.sampler.streams.story.documents | 761448 |
| checkpoints.readout_adapter.sampler.streams.story.epoch | 0 |
| checkpoints.readout_adapter.sampler.streams.story.document_position | 38243 |
| checkpoints.readout_adapter.sampler.streams.story.token_offset | 87 |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoints.readout_adapter.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoints.readout_adapter.sampler.streams.conditional_textbook.seed | 42 |
| checkpoints.readout_adapter.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.readout_adapter.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoints.readout_adapter.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoints.readout_adapter.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoints.readout_adapter.sampler.source_teachers.web | 75000000 |
| checkpoints.readout_adapter.sampler.source_teachers.story | 5000000 |
| checkpoints.readout_adapter.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.readout_adapter.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoints.readout_adapter.sampler.source_eos.web | 159447 |
| checkpoints.readout_adapter.sampler.source_eos.story | 38240 |
| checkpoints.readout_adapter.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoints.readout_adapter.sampler.source_eos.conditional_textbook | 234328 |
| checkpoints.readout_adapter.sampler.source_tokens.web | 75183104 |
| checkpoints.readout_adapter.sampler.source_tokens.story | 5039104 |
| checkpoints.readout_adapter.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoints.readout_adapter.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoints.readout_adapter.sampler.source_body_bytes.web | 292167653 |
| checkpoints.readout_adapter.sampler.source_body_bytes.story | 20452979 |
| checkpoints.readout_adapter.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.readout_adapter.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.readout_adapter.sampler.source_focus_teachers.web | 0 |
| checkpoints.readout_adapter.sampler.source_focus_teachers.story | 0 |
| checkpoints.readout_adapter.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.readout_adapter.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.readout_adapter.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoints.readout_adapter.source_body_bytes.web | 292167653 |
| checkpoints.readout_adapter.source_body_bytes.story | 20452979 |
| checkpoints.readout_adapter.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoints.readout_adapter.source_body_bytes.conditional_textbook | 37865985 |
| checkpoints.readout_adapter.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| checkpoints.readout_adapter.native_weights_unchanged | true |
| checkpoints.readout_adapter.unique_parameters | 10099456 |
| checkpoints.readout_adapter.model_config.schema_version | 1 |
| checkpoints.readout_adapter.model_config.architecture | "decoder_only_transformer" |
| checkpoints.readout_adapter.model_config.hidden_size | 256 |
| checkpoints.readout_adapter.model_config.num_attention_heads | 4 |
| checkpoints.readout_adapter.model_config.num_key_value_heads | 2 |
| checkpoints.readout_adapter.model_config.head_dim | 64 |
| checkpoints.readout_adapter.model_config.activation | "swiglu" |
| checkpoints.readout_adapter.model_config.norm | "rmsnorm" |
| checkpoints.readout_adapter.model_config.rms_norm_eps | 1e-06 |
| checkpoints.readout_adapter.model_config.qk_norm_type | "none" |
| checkpoints.readout_adapter.model_config.qk_norm_before_rope | true |
| checkpoints.readout_adapter.model_config.attention_scale | 0.125 |
| checkpoints.readout_adapter.model_config.rope_theta | 10000 |
| checkpoints.readout_adapter.model_config.rope_layout | "half_split" |
| checkpoints.readout_adapter.model_config.rotary_dim | 64 |
| checkpoints.readout_adapter.model_config.max_position_embeddings | 1024 |
| checkpoints.readout_adapter.model_config.tie_word_embeddings | true |
| checkpoints.readout_adapter.model_config.attention_bias | false |
| checkpoints.readout_adapter.model_config.mlp_bias | false |
| checkpoints.readout_adapter.model_config.dropout | 0.0 |
| checkpoints.readout_adapter.model_config.initializer_std | 0.02 |
| checkpoints.readout_adapter.model_config.norm_initial_gain | 1.0 |
| checkpoints.readout_adapter.model_config.status | "phase5_ablation" |
| checkpoints.readout_adapter.model_config.name | "JMicro-10M-T4K-NoQKNorm" |
| checkpoints.readout_adapter.model_config.vocab_size | 4096 |
| checkpoints.readout_adapter.model_config.num_hidden_layers | 13 |
| checkpoints.readout_adapter.model_config.intermediate_size | 640 |
| checkpoints.readout_adapter.model_config.expected_parameter_count | 10001152 |
| checkpoints.readout_adapter.model_config.readout_adapter.kind | "frozen_native_postnorm_silu_residual_readout_v1" |
| checkpoints.readout_adapter.model_config.readout_adapter.bottleneck_ratio | [3, 4] |
| checkpoints.readout_adapter.model_config.readout_adapter.native_weights_frozen | true |
| checkpoints.readout_adapter.model_config.readout_adapter.up_initialization | "exact_zero" |
| checkpoints.readout_adapter.model_config.readout_adapter.down_initialization | "private_normal_std_0.02" |
| checkpoints.readout_adapter.model_config.readout_adapter.initialization_seed | 2026100651 |
| checkpoints.readout_adapter.model_config.readout_adapter.bias | false |
| checkpoints.readout_adapter.model_config.readout_adapter.dropout | 0.0 |
| checkpoints.readout_adapter.model_config.readout_adapter.placement | "after_final_RMSNorm_before_tied_vocabulary_matrix" |
| evaluations.readout_adapter.binding.teacher_goals.web | 75000000 |
| evaluations.readout_adapter.binding.teacher_goals.story | 5000000 |
| evaluations.readout_adapter.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.readout_adapter.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.readout_adapter.binding.policy.initialization_seed | 2026100651 |
| evaluations.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| evaluations.readout_adapter.body.documents | 256 |
| evaluations.readout_adapter.body.limit_documents | 256 |
| evaluations.readout_adapter.body.body_nll | 337985.41487693787 |
| evaluations.readout_adapter.body.eos_nll | 517.2182487361133 |
| evaluations.readout_adapter.body.body_bytes | 472055 |
| evaluations.readout_adapter.body.body_tokens | 122343 |
| evaluations.readout_adapter.body.bpb | 1.0329514186604467 |
| evaluations.readout_adapter.body.seconds | 1.417319989996031 |
| evaluations.readout_adapter.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.readout_adapter.generation.max_new_tokens | 64 |
| evaluations.readout_adapter.greedy_rates.eos | 46 |
| evaluations.readout_adapter.greedy_rates.repetition | 24 |
| evaluations.readout_adapter.greedy_rates.unicode_failure | 0 |
| evaluations.readout_adapter.greedy_rates.role_leak | 0 |
| evaluations.readout_adapter.greedy_rates.empty | 0 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.ci95 | [0.5364583333333334, 0.6095052083333327] |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6145833333333334] |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5712418300653594 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.mcc | 0.1469861839480328 |
| evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.readout_adapter.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.readout_adapter.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.readout_adapter.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.point | 0.7492447129909365 |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.ci95 | [0.7009063444108762, 0.7946374622356491] |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.primary.hard_accuracy | 0.7492447129909365 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7734138972809668] |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.readout_adapter.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.readout_adapter.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.point | 0.35031277926720283 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.ci95 | [0.3243744414655943, 0.37803842716711333] |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jcqa.primary.hard_accuracy | 0.35031277926720283 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28418230563002683, 0.3360142984807864] |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30884198292554615 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.mcc | 0.13764427437008395 |
| evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.readout_adapter.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.readout_adapter.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.readout_adapter.diagnostics.semantic_both_contexts.correct | 15 |
| evaluations.readout_adapter.memory.maximum_observed_allocated_bytes | 236000256 |
| evaluations.readout_adapter.memory.maximum_observed_reserved_bytes | 9600761856 |
| evaluations.readout_adapter.protected_test_used | false |
| transfer.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| transfer.readout_adapter.checks.weights_unchanged | true |
| transfer.readout_adapter.checks.no_gradients | true |
| transfer.readout_adapter.checks.eval_mode | true |
| transfer.readout_adapter.checks.RNG_restored | true |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.all128.both_correct | 62 |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 39 |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| transfer.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 63 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8125 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 40 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 54 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| transfer.readout_adapter.optimizer_updates | 0 |
| transfer.readout_adapter.scientific_teacher_tokens | 0 |
| transfer.readout_adapter.protected_test_used | false |
| transfer.readout_adapter.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| retention.readout_adapter.checks.weights_unchanged | true |
| retention.readout_adapter.checks.no_gradients | true |
| retention.readout_adapter.checks.eval_mode | true |
| retention.readout_adapter.checks.RNG_restored | true |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6484375 |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.all128.both_correct | 43 |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 28 |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 15 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.66796875 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 48 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 75 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6796875 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 51 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 72 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 33 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.readout_adapter.optimizer_updates | 0 |
| retention.readout_adapter.scientific_teacher_tokens | 0 |
| retention.readout_adapter.protected_test_used | false |
| retention.readout_adapter.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/readout_adapter/training/latest.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/readout_adapter/training/latest.json) ／ SHA256: `f29ebf0a407fdb000a1e35450f9722813db136f25077266d60e0dc9fc433747f` ／ 293 bytes

| 原キー | 保存値 |
|---|---|
| update | 326571 |
| tokens_seen | 10701078528 |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/review.json — readout_adapter100M_all80_content_and_actual_architecture_reviewed</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/review.json) ／ SHA256: `dec41336c15412b5616289e5178b0f9e8283fc67ca6f19262f9ada75105a8d2a` ／ 5,586 bytes

| 原キー | 保存値 |
|---|---|
| status | "readout_adapter100M_all80_content_and_actual_architecture_reviewed" |
| summaries.readout_adapter.BPB | 1.0329514186604467 |
| summaries.readout_adapter.rates.eos | 46 |
| summaries.readout_adapter.rates.repetition | 24 |
| summaries.readout_adapter.rates.unicode_failure | 0 |
| summaries.readout_adapter.rates.role_leak | 0 |
| summaries.readout_adapter.rates.empty | 0 |
| summaries.readout_adapter.grammar2 | 46 |
| summaries.readout_adapter.relevance2 | 39 |
| summaries.readout_adapter.coherent | 7 |
| summaries.readout_adapter.appropriate | 9 |
| summaries.readout_adapter.notes_sha256 | "e73739eb226de958f00099aecf53536e90147af4684972be7bd1f5fcc8f68148" |
| summaries.native_CE.BPB | 1.0356667036495277 |
| summaries.native_CE.rates.eos | 69 |
| summaries.native_CE.rates.repetition | 6 |
| summaries.native_CE.rates.unicode_failure | 0 |
| summaries.native_CE.rates.role_leak | 0 |
| summaries.native_CE.rates.empty | 0 |
| summaries.native_CE.grammar2 | 65 |
| summaries.native_CE.relevance2 | 52 |
| summaries.native_CE.coherent | 32 |
| summaries.native_CE.appropriate | 37 |
| summaries.native_CE.notes_sha256 | "366209389693d5b382ab5a4f4001e0dd6c52fd10c33f9304672a195607b51e69" |
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
| quality_comparisons.native_CE.checks.coherence_gain_at_least8 | false |
| quality_comparisons.native_CE.checks.paired_CI_lower_above0 | false |
| quality_comparisons.native_CE.checks.EOS_nonworsening | false |
| quality_comparisons.native_CE.checks.repetition_nonworsening | false |
| quality_comparisons.native_CE.checks.no_empty_role_unicode | true |
| quality_comparisons.native_CE.checks.BPB_gate | true |
| quality_comparisons.native_CE.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.native_CE.passed | false |
| quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| quality_comparisons.strong_staged.checks.BPB_gate | true |
| quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| quality_comparisons.strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 3068 |
| accounting.teachers | 100000000 |
| accounting.physical_input_positions | 100532224 |
| accounting.parameter_penalty_teacher_tokens | 0 |
| accounting.source_teachers.web | 75000000 |
| accounting.source_teachers.story | 5000000 |
| accounting.source_teachers.ordinary_textbook | 10000000 |
| accounting.source_teachers.conditional_textbook | 10000000 |
| accounting.source_EOS.web | 159447 |
| accounting.source_EOS.story | 38240 |
| accounting.source_EOS.ordinary_textbook | 74183 |
| accounting.source_EOS.conditional_textbook | 234328 |
| scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307952 |
| new_total_GPU_seconds | 178.9158119779895 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "98,304 new nonlinear readout weights/fresh Adam vs full native Adam; native weights frozen, same parent/input/target100M and evaluators. One learned seed/nonblind repeated dev. Stock HF export pending." |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0000.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0000.json) ／ SHA256: `ad2eadffe159df224dd753908a2fa4e3a70a6df8287ed8443a6b8ea75e208792` ／ 9,977 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0016.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0016.json) ／ SHA256: `f5692df92a99a143ae5aaf912dddcc9c1707b192ab979908b6d44e8e4711ce3b` ／ 9,624 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0032.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0032.json) ／ SHA256: `58357218af7484e19ec23e5322bdacf33ad8bdcd51ddb9104f6b7bc77ef45730` ／ 10,252 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0048.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0048.json) ／ SHA256: `c9a4f0c05eb376ffbe2237b0b3cf06fedcc64f228c827ae27c3a4154fd56fa20` ／ 9,567 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0064.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0064.json) ／ SHA256: `324a117b2e2de658a8df05c804759a90dc133f1b27c7f321ad405882803dd371` ／ 10,358 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0080.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0080.json) ／ SHA256: `ff5dde764cc1e59485e5fd52640d06dd238e9992be9a66ab4dbfca195a6f333a` ／ 9,752 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0096.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0096.json) ／ SHA256: `24adee1b4dc4b8ac5fa31bc04825d6d3b4fb70af2c1559b601a6e672dc72aaa1` ／ 9,847 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0112.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0112.json) ／ SHA256: `ef6290f76b2f6b775d15bf62b36c9d90c066ebc85ba047f3af5d0f3509f31284` ／ 10,163 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0128.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0128.json) ／ SHA256: `1953524f6fe6aa3a567490ed17624c64c85725026675e619855a7eef5e878775` ／ 9,852 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0144.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0144.json) ／ SHA256: `f7e6b7e34772f1e943d7f43ea1aba27a52001b7697031b4d57fa8e16b375f20e` ／ 9,933 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0160.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0160.json) ／ SHA256: `21183cc0cdf39a67230d4ef433b1a8bde0e523bc3cf94c4f4da6c39583291af0` ／ 10,174 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0176.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0176.json) ／ SHA256: `7041e0f2f50a5e548da9b07cbe6dd895cb7b13d07a096346713a897d94be4bc6` ／ 10,002 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0192.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0192.json) ／ SHA256: `771126af20db7b313b8aa3e378ba5cdeef34e8d2c5af5c54059285e1406cbb14` ／ 9,935 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0208.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0208.json) ／ SHA256: `120033bc53b7b173b97cc4113d7f56e172becf72c10f41d78f6e137e3bb485e9` ／ 9,671 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0224.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0224.json) ／ SHA256: `c2fe2cffe78bbc9d7e52cdd4729e047de8b084c73f23a5a73cd13592579f8620` ／ 9,852 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0240.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0240.json) ／ SHA256: `d25fa3fb00e668aacaab39d0be092ff2697f8902f0359c8ec9fd08150cb207b5` ／ 9,652 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0256.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0256.json) ／ SHA256: `b6bb366eac113e4be0558a1b326783825a75b6d199c6c188ea7a3008db63515e` ／ 9,696 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0272.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0272.json) ／ SHA256: `448c6b73f593bf35dedcc4c3c401697c1e06712647ba7bade1ae96772c112555` ／ 9,667 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0288.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0288.json) ／ SHA256: `841589c787f6bde0577bcb757117ae93fd9ad1f5d5445a153033f9071707b509` ／ 9,687 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0304.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0304.json) ／ SHA256: `5b8731953a5a8f2876c10c003c46ca140721f21fd3f276ad852edfb5d290bb0f` ／ 9,885 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0320.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0320.json) ／ SHA256: `fa066fdd65ab5814df93e76f7ff00900977759995bbc0833d6e5913243f1c8c0` ／ 9,374 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0336.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0336.json) ／ SHA256: `63c006dba3464f7a384a31dbe11851292911ef4ac3758ebe4370adc996afd1c1` ／ 9,495 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0352.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0352.json) ／ SHA256: `cab769cb25e4f5f23300de465d180afc84681cdb70ef06ea9afb7a488e2fdd36` ／ 9,833 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0368.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0368.json) ／ SHA256: `4d8e9f5e60f32aba25c69b31daab933a669db90eb0024c763680d05b6c1d600f` ／ 9,614 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0384.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0384.json) ／ SHA256: `d71339cb1244150f0db9a36c21c0bdfbc1e514d4fe82d904cc2e7a24cb16c871` ／ 9,931 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0400.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0400.json) ／ SHA256: `0702fd19bc60268512bc0d52dc5034f7e6520cf2536ad333aafdd9b8409d8c25` ／ 9,596 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0416.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0416.json) ／ SHA256: `38b6e0b04a598173dac5e6f7dbb416d9ff9c52bb8947d86ca7fc9f52e5e40c7e` ／ 9,963 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0432.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0432.json) ／ SHA256: `cd599f061ab9fff6e4790677f44c9609c051c56576a2e008b470b469bfd9c344` ／ 9,407 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0448.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0448.json) ／ SHA256: `e9d5afa3c1c9e347b0a2873321a69f0f8952f48535336804cc2f371c0b126cd6` ／ 9,645 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0464.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0464.json) ／ SHA256: `dc3d449264c56043e2955a1fa6914048319b6e7ddee8c2f7de80bd95853ad7bf` ／ 9,461 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0480.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0480.json) ／ SHA256: `3d0a97e269e0c5312cecccb82af719da9bf6cc8ece02323ac4d44ca71c250d62` ／ 9,479 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0496.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/0496.json) ／ SHA256: `0011aaeefc12e7cee0896b3d5d5ace096afc595fbdc987accc2ba03cf70e0fc6` ／ 9,570 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/result.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/bridge/readout_adapter/result.json) ／ SHA256: `98a3e6af084b34ed1ad8cf2fde6cb23aafa46680e7b6cc5048a778aece496e70` ／ 186,258 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.72265625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 62 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 39 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 63 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 40 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 54 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0000.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0000.json) ／ SHA256: `dd0b1b7d643712aa2a26fe4f641859f4f54b6278a22aa96571f8aac94babee4f` ／ 8,010 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0016.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0016.json) ／ SHA256: `7e71f54d5eac32b81e9f848713e297eec58ec709a4036d53a904510e5b236a14` ／ 8,350 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0032.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0032.json) ／ SHA256: `bc7bac34ebb629efa8a870baae016fbc72de10c37eeed1a8a0ec0128c37c90ea` ／ 7,024 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0048.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0048.json) ／ SHA256: `a1fb7d56d37c1c17247802feafd605edec3e4c3f2fd6207bbe3fe19e6c8eec00` ／ 8,179 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0064.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0064.json) ／ SHA256: `789e751223d19957a118d5c97ddea84269931ef76922a097fc80ed314eb86029` ／ 8,541 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0080.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0080.json) ／ SHA256: `cccd0203401da1accf4eb46fcdc0253ac66943b818911d86dd2047495bc456bf` ／ 7,117 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0096.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0096.json) ／ SHA256: `4448606e6d1b3f2a5cf73631ba6ffe4592662929ea3bdd4bf9b1647e0571ade7` ／ 8,104 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0112.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0112.json) ／ SHA256: `e585231b1db1f5356279398b721bfba07e2a23177aadc28f4d9954f45d7b72e7` ／ 8,280 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0128.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0128.json) ／ SHA256: `ea916452f70ef336c970f7ab7970d46675bed9edd7948dcd7db37887071d2ae7` ／ 7,124 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0144.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0144.json) ／ SHA256: `38984756d9542e798d21e6f6f063a0fca762308b061749ecb1a58732bde4a415` ／ 8,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0160.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0160.json) ／ SHA256: `e6aa9db64749e7d9b82358d238dec538693dc4a0bd3414a3d7924d9a8ae24a0e` ／ 8,624 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0176.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0176.json) ／ SHA256: `f363b0db366284533eb05370a8ea6368b9485b37bcca770c0a1de2f4c4fb43d8` ／ 6,959 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0192.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0192.json) ／ SHA256: `f8ef19c1a610bb6b94d6406954c1846d6a48dec11aebda5c26c7c3a8370559ae` ／ 8,196 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0208.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0208.json) ／ SHA256: `d1c60dac8b3a58317da5605ae765151d827fb238d97a4fd379a039fd6ba4bc82` ／ 8,547 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0224.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0224.json) ／ SHA256: `4fcc6b7775ec9463177adf9bb2da8b1401de84596b38d26db714350a63a8457f` ／ 7,124 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0240.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0240.json) ／ SHA256: `69edf55c4fd86bb839cdb3bedb045bb2cc19cf75b76d15ded9dd0f335a596dd9` ／ 8,345 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0256.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0256.json) ／ SHA256: `406618ab7ef6435bda32418bcf23694b67147a3d87da6fcf870f899cf4177289` ／ 8,289 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0272.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0272.json) ／ SHA256: `a470e5be69f9589ece6afba512df3fb395251f1ecbc812d82d9cbc8a12837cc1` ／ 8,472 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0288.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0288.json) ／ SHA256: `0f42e038a64b01cc6245648a66be9fd26ce35941f3d7aa0a68b40803aa398aa5` ／ 7,149 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0304.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0304.json) ／ SHA256: `8df2874b7b866fd0819ea941bfc95ca444f040170a6c438642d2a39eb5bd6030` ／ 8,195 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0320.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0320.json) ／ SHA256: `07ce6c1ae521424a46b0bd76ffddd762716fb705a35b883a18c78cb60a8a63a8` ／ 8,642 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0336.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0336.json) ／ SHA256: `a1ec14a0df0af01c3ea5f5925e112b54d8e35b9a6da8057d32447d9924e7270b` ／ 7,140 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0352.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0352.json) ／ SHA256: `f6beaa89b1d16811098395419039edc9f4ade121395a21f571da39df3086a290` ／ 8,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0368.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0368.json) ／ SHA256: `9c0b5ce99d69a7c37088f209394b1d929c4170792cd6d734150ca8339f1050bb` ／ 8,220 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0384.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0384.json) ／ SHA256: `dd6a221614d7527555a61197f60b67c5a58f7306d771c6819d06c9db286d10ff` ／ 7,067 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0400.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0400.json) ／ SHA256: `921b8c3fd39308aad9ef7bb9ba9e45d2fc6d936e948003446990f00d638ef5fa` ／ 8,201 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0416.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0416.json) ／ SHA256: `ac5f2a9e3c34aadf8a99b5d76960fbcf48123da7b7f9758b8a20560e68ddc5f4` ／ 8,216 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0432.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0432.json) ／ SHA256: `623240bfef3ea8b5dd66f2ac9ee997ebfbeda18e9bd5da6eace1393fe5b33b7b` ／ 7,146 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0448.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0448.json) ／ SHA256: `ae1874b63f9d57eb4c92eae8640942462854d638906f65e9a13bffa8bf8069d6` ／ 8,102 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0464.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0464.json) ／ SHA256: `79a658dc9643de49cb51d14082439839661a9223cca1343d5b27b1ce1eef2545` ／ 8,392 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0480.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0480.json) ／ SHA256: `cbb97c3f25893e3bfa9604049f89546f018bc0cb93b9beaca892dff3f06a0fa9` ／ 7,057 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0496.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/0496.json) ／ SHA256: `e8529261a037bb8d31003f5edd792f58837c04b70d386f8375d03f76026225f9` ／ 8,112 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |

</details>

<details>
<summary>reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/result.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-comparison-v3-20261006/transfer/retention/readout_adapter/result.json) ／ SHA256: `29d542b2034807498340802106236dbb81fbf9ef8c961ce94a743901e08db721` ／ 182,875 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6484375 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 43 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 28 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 15 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.66796875 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 48 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 75 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 33 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6796875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 51 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 72 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 33 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-20261006/launcher.json) ／ SHA256: `6a82b166df181751e7c9723d99b54c809743946c2fcd7e56176a456cf3599050` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-20261006/result.json — failed</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-20261006/result.json) ／ SHA256: `da04fbfc4f03492f4f3c3daa6352568f70ea329fd6cbe2d07bde69f85b7ce022` ／ 176 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-v2-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-v2-20261006/launcher.json) ／ SHA256: `a45541d4872a2121caab00cea7ff3f0693879ed50fea2ef74a1c9bfaaa536868` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-v2-20261006/result.json — failed</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-v2-20261006/result.json) ／ SHA256: `00edf7dddf824d4284b4f8769c5bf6657014951c54b2f15c306ee277163798ad` ／ 176 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-v3-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-v3-20261006/launcher.json) ／ SHA256: `82c1c44180209bcf08359323ac5ed7ad37e33e29ba782aeeda1e7e297e5c84ec` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/readout-adapter-probe-launcher-v3-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/readout-adapter-probe-launcher-v3-20261006/result.json) ／ SHA256: `36a2a63085a6f07d24221a39ec28aee1c8251c67f5d2cc73015ad8cbfac8d77d` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/readout-adapter-science-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/readout-adapter-science-launcher-20261006/launcher.json) ／ SHA256: `a1008932e1027897be9df805eb56edd095ecdc363b989ded30d15eb0107ae1f3` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/readout-adapter-science-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/readout-adapter-science-launcher-20261006/result.json) ／ SHA256: `f781872083c7296cdb598ac0a04a7298b6d88128775437ed42b9783f857640c9` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/readout_adapter_comparison_completion.json — readout_adapter_comparison_completion</summary>

[原記録](../../reports/phase6/readout_adapter_comparison_completion.json) ／ SHA256: `59ad7cc3eca2b0d7493d7ff7e700a2faea59ceb098fc78c6f3393834d0bf2d31` ／ 704,384 bytes

| 原キー | 保存値 |
|---|---|
| status | "readout_adapter_comparison_completion" |
| CPU_preparation_seconds | 0.05737043500994332 |
| verification_GPU_seconds | 23.79449131700676 |
| verification_teacher_tokens | 1307952 |
| scientific_GPU_seconds | 155.12132066098275 |
| new_source_CE_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 155.12132066098275 |
| actual_job.teachers | 99767422 |
| actual_job.teacher_budget | 100000000 |
| actual_job.loss | 0.28425660729408264 |
| actual_job.source_teachers.web | 75000000 |
| actual_job.source_teachers.story | 5000000 |
| actual_job.source_teachers.ordinary_textbook | 10000000 |
| actual_job.source_teachers.conditional_textbook | 9767422 |
| actual_result.checkpoints.readout_adapter.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout-adapter-comparison-v3-20261006/readout_adapter/training/checkpoint-00326571.pt" |
| actual_result.checkpoints.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| actual_result.checkpoints.readout_adapter.binding.config_sha256 | "18cc823aeacbd431695bec1a1d445b2599db842c52b375407ebae7380ddcde81" |
| actual_result.checkpoints.readout_adapter.binding.arm | "readout_adapter" |
| actual_result.checkpoints.readout_adapter.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/historical-parent-condition-comparison-v3-20261006/historical_parent/training/checkpoint-00323503.pt" |
| actual_result.checkpoints.readout_adapter.binding.parent.sha256 | "6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0" |
| actual_result.checkpoints.readout_adapter.binding.teacher_goals.web | 75000000 |
| actual_result.checkpoints.readout_adapter.binding.teacher_goals.story | 5000000 |
| actual_result.checkpoints.readout_adapter.binding.teacher_goals.ordinary_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.binding.teacher_goals.conditional_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.binding.study_kind | "frozen_decoder_nonlinear_readout_Base_full100M_v1" |
| actual_result.checkpoints.readout_adapter.binding.parameter_coefficient | 0.0 |
| actual_result.checkpoints.readout_adapter.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| actual_result.checkpoints.readout_adapter.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_result.checkpoints.readout_adapter.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| actual_result.checkpoints.readout_adapter.binding.policy.kind | "frozen_native_postnorm_silu_residual_readout_v1" |
| actual_result.checkpoints.readout_adapter.binding.policy.bottleneck_ratio | [3, 4] |
| actual_result.checkpoints.readout_adapter.binding.policy.native_weights_frozen | true |
| actual_result.checkpoints.readout_adapter.binding.policy.up_initialization | "exact_zero" |
| actual_result.checkpoints.readout_adapter.binding.policy.down_initialization | "private_normal_std_0.02" |
| actual_result.checkpoints.readout_adapter.binding.policy.initialization_seed | 2026100651 |
| actual_result.checkpoints.readout_adapter.binding.policy.bias | false |
| actual_result.checkpoints.readout_adapter.binding.policy.dropout | 0.0 |
| actual_result.checkpoints.readout_adapter.binding.policy.placement | "after_final_RMSNorm_before_tied_vocabulary_matrix" |
| actual_result.checkpoints.readout_adapter.binding.readout_LR | 0.0001 |
| actual_result.checkpoints.readout_adapter.binding.optimizer_policy | "fresh_readout_only_native_weights_frozen" |
| actual_result.checkpoints.readout_adapter.update | 326571 |
| actual_result.checkpoints.readout_adapter.tokens | 10701078528 |
| actual_result.checkpoints.readout_adapter.supervised_tokens | 10677786961 |
| actual_result.checkpoints.readout_adapter.additional_supervised_tokens | 100000000 |
| actual_result.checkpoints.readout_adapter.additional_input_tokens | 100532224 |
| actual_result.checkpoints.readout_adapter.source_teachers.web | 75000000 |
| actual_result.checkpoints.readout_adapter.source_teachers.story | 5000000 |
| actual_result.checkpoints.readout_adapter.source_teachers.ordinary_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.source_teachers.conditional_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.source_eos.web | 159447 |
| actual_result.checkpoints.readout_adapter.source_eos.story | 38240 |
| actual_result.checkpoints.readout_adapter.source_eos.ordinary_textbook | 74183 |
| actual_result.checkpoints.readout_adapter.source_eos.conditional_textbook | 234328 |
| actual_result.checkpoints.readout_adapter.source_input_tokens.web | 75183104 |
| actual_result.checkpoints.readout_adapter.source_input_tokens.story | 5039104 |
| actual_result.checkpoints.readout_adapter.source_input_tokens.ordinary_textbook | 10075136 |
| actual_result.checkpoints.readout_adapter.source_input_tokens.conditional_textbook | 10234880 |
| actual_result.checkpoints.readout_adapter.source_focus_teachers.web | 0 |
| actual_result.checkpoints.readout_adapter.source_focus_teachers.story | 0 |
| actual_result.checkpoints.readout_adapter.source_focus_teachers.ordinary_textbook | 0 |
| actual_result.checkpoints.readout_adapter.source_focus_teachers.conditional_textbook | 1407427 |
| actual_result.checkpoints.readout_adapter.focus_teacher_tokens | 1407427 |
| actual_result.checkpoints.readout_adapter.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| actual_result.checkpoints.readout_adapter.weighted_teacher_mass | 100000000 |
| actual_result.checkpoints.readout_adapter.outcome_weight | 1 |
| actual_result.checkpoints.readout_adapter.training_seconds | 77.97412706623436 |
| actual_result.checkpoints.readout_adapter.completed_at | "2026-10-06T13:56:36.922115Z" |
| actual_result.checkpoints.readout_adapter.parameter_coefficient | 0.0 |
| actual_result.checkpoints.readout_adapter.parameter_penalty_teacher_tokens | 0 |
| actual_result.checkpoints.readout_adapter.anchor_initial_digest | "13062d26f17738fac26ba94cd97e5d42229641da7c224a3d9888917fb9b1e8ce" |
| actual_result.checkpoints.readout_adapter.sampler.kind | "same-streams-staged-source-order-v1" |
| actual_result.checkpoints.readout_adapter.sampler.goals.web | 75000000 |
| actual_result.checkpoints.readout_adapter.sampler.goals.story | 5000000 |
| actual_result.checkpoints.readout_adapter.sampler.goals.ordinary_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.sampler.goals.conditional_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.sampler.context | 1024 |
| actual_result.checkpoints.readout_adapter.sampler.seed | 42 |
| actual_result.checkpoints.readout_adapter.sampler.position | 3068 |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.sampler.seed | 42 |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.sampler.epoch | 0 |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.sampler.position | 10400762 |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.sampler.context | 1024 |
| actual_result.checkpoints.readout_adapter.sampler.streams.web.sampler.blocks | 11939276 |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.seed | 42 |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.genre | "story" |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.documents | 761448 |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.epoch | 0 |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.document_position | 38243 |
| actual_result.checkpoints.readout_adapter.sampler.streams.story.token_offset | 87 |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.seed | 42 |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.genre | "textbook" |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.documents | 2942232 |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.epoch | 0 |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.document_position | 74189 |
| actual_result.checkpoints.readout_adapter.sampler.streams.ordinary_textbook.token_offset | 77 |
| actual_result.checkpoints.readout_adapter.sampler.streams.conditional_textbook.seed | 42 |
| actual_result.checkpoints.readout_adapter.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| actual_result.checkpoints.readout_adapter.sampler.streams.conditional_textbook.epoch | 114 |
| actual_result.checkpoints.readout_adapter.sampler.streams.conditional_textbook.document_position | 871 |
| actual_result.checkpoints.readout_adapter.sampler.streams.conditional_textbook.token_offset | 23 |
| actual_result.checkpoints.readout_adapter.sampler.source_teachers.web | 75000000 |
| actual_result.checkpoints.readout_adapter.sampler.source_teachers.story | 5000000 |
| actual_result.checkpoints.readout_adapter.sampler.source_teachers.ordinary_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.sampler.source_teachers.conditional_textbook | 10000000 |
| actual_result.checkpoints.readout_adapter.sampler.source_eos.web | 159447 |
| actual_result.checkpoints.readout_adapter.sampler.source_eos.story | 38240 |
| actual_result.checkpoints.readout_adapter.sampler.source_eos.ordinary_textbook | 74183 |
| actual_result.checkpoints.readout_adapter.sampler.source_eos.conditional_textbook | 234328 |
| actual_result.checkpoints.readout_adapter.sampler.source_tokens.web | 75183104 |
| actual_result.checkpoints.readout_adapter.sampler.source_tokens.story | 5039104 |
| actual_result.checkpoints.readout_adapter.sampler.source_tokens.ordinary_textbook | 10075136 |
| actual_result.checkpoints.readout_adapter.sampler.source_tokens.conditional_textbook | 10234880 |
| actual_result.checkpoints.readout_adapter.sampler.source_body_bytes.web | 292167653 |
| actual_result.checkpoints.readout_adapter.sampler.source_body_bytes.story | 20452979 |
| actual_result.checkpoints.readout_adapter.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| actual_result.checkpoints.readout_adapter.sampler.source_body_bytes.conditional_textbook | 37865985 |
| actual_result.checkpoints.readout_adapter.sampler.source_focus_teachers.web | 0 |
| actual_result.checkpoints.readout_adapter.sampler.source_focus_teachers.story | 0 |
| actual_result.checkpoints.readout_adapter.sampler.source_focus_teachers.ordinary_textbook | 0 |
| actual_result.checkpoints.readout_adapter.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| actual_result.checkpoints.readout_adapter.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| actual_result.checkpoints.readout_adapter.source_body_bytes.web | 292167653 |
| actual_result.checkpoints.readout_adapter.source_body_bytes.story | 20452979 |
| actual_result.checkpoints.readout_adapter.source_body_bytes.ordinary_textbook | 42739471 |
| actual_result.checkpoints.readout_adapter.source_body_bytes.conditional_textbook | 37865985 |
| actual_result.checkpoints.readout_adapter.token_digest | "066655c59038b4f3e18a144c50707944fce1ceeee6408d2c771d23195d0f34ce" |
| actual_result.checkpoints.readout_adapter.native_weights_unchanged | true |
| actual_result.checkpoints.readout_adapter.unique_parameters | 10099456 |
| actual_result.checkpoints.readout_adapter.model_config.schema_version | 1 |
| actual_result.checkpoints.readout_adapter.model_config.architecture | "decoder_only_transformer" |
| actual_result.checkpoints.readout_adapter.model_config.hidden_size | 256 |
| actual_result.checkpoints.readout_adapter.model_config.num_attention_heads | 4 |
| actual_result.checkpoints.readout_adapter.model_config.num_key_value_heads | 2 |
| actual_result.checkpoints.readout_adapter.model_config.head_dim | 64 |
| actual_result.checkpoints.readout_adapter.model_config.activation | "swiglu" |
| actual_result.checkpoints.readout_adapter.model_config.norm | "rmsnorm" |
| actual_result.checkpoints.readout_adapter.model_config.rms_norm_eps | 1e-06 |
| actual_result.checkpoints.readout_adapter.model_config.qk_norm_type | "none" |
| actual_result.checkpoints.readout_adapter.model_config.qk_norm_before_rope | true |
| actual_result.checkpoints.readout_adapter.model_config.attention_scale | 0.125 |
| actual_result.checkpoints.readout_adapter.model_config.rope_theta | 10000 |
| actual_result.checkpoints.readout_adapter.model_config.rope_layout | "half_split" |
| actual_result.checkpoints.readout_adapter.model_config.rotary_dim | 64 |
| actual_result.checkpoints.readout_adapter.model_config.max_position_embeddings | 1024 |
| actual_result.checkpoints.readout_adapter.model_config.tie_word_embeddings | true |
| actual_result.checkpoints.readout_adapter.model_config.attention_bias | false |
| actual_result.checkpoints.readout_adapter.model_config.mlp_bias | false |
| actual_result.checkpoints.readout_adapter.model_config.dropout | 0.0 |
| actual_result.checkpoints.readout_adapter.model_config.initializer_std | 0.02 |
| actual_result.checkpoints.readout_adapter.model_config.norm_initial_gain | 1.0 |
| actual_result.checkpoints.readout_adapter.model_config.status | "phase5_ablation" |
| actual_result.checkpoints.readout_adapter.model_config.name | "JMicro-10M-T4K-NoQKNorm" |
| actual_result.checkpoints.readout_adapter.model_config.vocab_size | 4096 |
| actual_result.checkpoints.readout_adapter.model_config.num_hidden_layers | 13 |
| actual_result.checkpoints.readout_adapter.model_config.intermediate_size | 640 |
| actual_result.checkpoints.readout_adapter.model_config.expected_parameter_count | 10001152 |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.kind | "frozen_native_postnorm_silu_residual_readout_v1" |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.bottleneck_ratio | [3, 4] |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.native_weights_frozen | true |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.up_initialization | "exact_zero" |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.down_initialization | "private_normal_std_0.02" |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.initialization_seed | 2026100651 |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.bias | false |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.dropout | 0.0 |
| actual_result.checkpoints.readout_adapter.model_config.readout_adapter.placement | "after_final_RMSNorm_before_tied_vocabulary_matrix" |
| actual_result.evaluations.readout_adapter.binding.teacher_goals.web | 75000000 |
| actual_result.evaluations.readout_adapter.binding.teacher_goals.story | 5000000 |
| actual_result.evaluations.readout_adapter.binding.teacher_goals.ordinary_textbook | 10000000 |
| actual_result.evaluations.readout_adapter.binding.teacher_goals.conditional_textbook | 10000000 |
| actual_result.evaluations.readout_adapter.binding.policy.initialization_seed | 2026100651 |
| actual_result.evaluations.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| actual_result.evaluations.readout_adapter.body.documents | 256 |
| actual_result.evaluations.readout_adapter.body.limit_documents | 256 |
| actual_result.evaluations.readout_adapter.body.body_nll | 337985.41487693787 |
| actual_result.evaluations.readout_adapter.body.eos_nll | 517.2182487361133 |
| actual_result.evaluations.readout_adapter.body.body_bytes | 472055 |
| actual_result.evaluations.readout_adapter.body.body_tokens | 122343 |
| actual_result.evaluations.readout_adapter.body.bpb | 1.0329514186604467 |
| actual_result.evaluations.readout_adapter.body.seconds | 1.417319989996031 |
| actual_result.evaluations.readout_adapter.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| actual_result.evaluations.readout_adapter.generation.max_new_tokens | 64 |
| actual_result.evaluations.readout_adapter.greedy_rates.eos | 46 |
| actual_result.evaluations.readout_adapter.greedy_rates.repetition | 24 |
| actual_result.evaluations.readout_adapter.greedy_rates.unicode_failure | 0 |
| actual_result.evaluations.readout_adapter.greedy_rates.role_leak | 0 |
| actual_result.evaluations.readout_adapter.greedy_rates.empty | 0 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.ci95 | [0.5364583333333334, 0.6095052083333327] |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.units | 96 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.examples | 192 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6145833333333334] |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.count | 192 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5712418300653594 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.mcc | 0.1469861839480328 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.train_majority_accuracy | 0.5 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.negation.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.negation.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.quantity.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.time.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.time.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.comparison.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.coreference.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.causality.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.causality.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.point | 0.7492447129909365 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.ci95 | [0.7009063444108762, 0.7946374622356491] |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.units | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.examples | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.primary.hard_accuracy | 0.7492447129909365 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.7734138972809668] |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.count | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.train_majority_accuracy | null |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.binding.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.readout_adapter.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.point | 0.35031277926720283 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.ci95 | [0.3243744414655943, 0.37803842716711333] |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.units | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.primary.hard_accuracy | 0.35031277926720283 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28418230563002683, 0.3360142984807864] |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.count | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30884198292554615 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.mcc | 0.13764427437008395 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.seed | 42 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.readout_adapter.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.readout_adapter.diagnostics.semantic_both_contexts.correct | 15 |
| actual_result.evaluations.readout_adapter.memory.maximum_observed_allocated_bytes | 236000256 |
| actual_result.evaluations.readout_adapter.memory.maximum_observed_reserved_bytes | 9600761856 |
| actual_result.evaluations.readout_adapter.protected_test_used | false |
| actual_result.transfer.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| actual_result.transfer.readout_adapter.checks.weights_unchanged | true |
| actual_result.transfer.readout_adapter.checks.no_gradients | true |
| actual_result.transfer.readout_adapter.checks.eval_mode | true |
| actual_result.transfer.readout_adapter.checks.RNG_restored | true |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.72265625 |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.all128.both_correct | 62 |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8046875 |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 39 |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.640625 |
| actual_result.transfer.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.72265625 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 63 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 59 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 107 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8125 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 40 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 44 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 70 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 54 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 37 |
| actual_result.transfer.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 45 |
| actual_result.transfer.readout_adapter.optimizer_updates | 0 |
| actual_result.transfer.readout_adapter.scientific_teacher_tokens | 0 |
| actual_result.transfer.readout_adapter.protected_test_used | false |
| actual_result.transfer.readout_adapter.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.retention.readout_adapter.checkpoint_sha256 | "a51065b1a2a44fe47a7cd38730f4643276aa1c6125c52abaeb4ef1377ac13bba" |
| actual_result.retention.readout_adapter.checks.weights_unchanged | true |
| actual_result.retention.readout_adapter.checks.no_gradients | true |
| actual_result.retention.readout_adapter.checks.eval_mode | true |
| actual_result.retention.readout_adapter.checks.RNG_restored | true |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6484375 |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.all128.both_correct | 43 |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 28 |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| actual_result.retention.readout_adapter.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 15 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.66796875 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 48 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 75 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.75 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 33 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 15 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6796875 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 51 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 72 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 33 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 55 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.609375 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 18 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| actual_result.retention.readout_adapter.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| actual_result.retention.readout_adapter.optimizer_updates | 0 |
| actual_result.retention.readout_adapter.scientific_teacher_tokens | 0 |
| actual_result.retention.readout_adapter.protected_test_used | false |
| actual_result.retention.readout_adapter.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.status | "readout_adapter100M_GPU_complete_pending_all80_content" |
| actual_result.GPU_seconds | 155.12132066098275 |
| actual_result.scientific_teacher_tokens | 100000000 |
| actual_result.reused_control_teacher_tokens | 100000000 |
| actual_result.all_scientific_input_streams_match | true |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| total_new_GPU_seconds | 178.9158119779895 |
| actual_review.status | "readout_adapter100M_all80_content_and_actual_architecture_reviewed" |
| actual_review.summaries.readout_adapter.BPB | 1.0329514186604467 |
| actual_review.summaries.readout_adapter.rates.eos | 46 |
| actual_review.summaries.readout_adapter.rates.repetition | 24 |
| actual_review.summaries.readout_adapter.rates.unicode_failure | 0 |
| actual_review.summaries.readout_adapter.rates.role_leak | 0 |
| actual_review.summaries.readout_adapter.rates.empty | 0 |
| actual_review.summaries.readout_adapter.grammar2 | 46 |
| actual_review.summaries.readout_adapter.relevance2 | 39 |
| actual_review.summaries.readout_adapter.coherent | 7 |
| actual_review.summaries.readout_adapter.appropriate | 9 |
| actual_review.summaries.readout_adapter.notes_sha256 | "e73739eb226de958f00099aecf53536e90147af4684972be7bd1f5fcc8f68148" |
| actual_review.summaries.native_CE.BPB | 1.0356667036495277 |
| actual_review.summaries.native_CE.rates.eos | 69 |
| actual_review.summaries.native_CE.rates.repetition | 6 |
| actual_review.summaries.native_CE.rates.unicode_failure | 0 |
| actual_review.summaries.native_CE.rates.role_leak | 0 |
| actual_review.summaries.native_CE.rates.empty | 0 |
| actual_review.summaries.native_CE.grammar2 | 65 |
| actual_review.summaries.native_CE.relevance2 | 52 |
| actual_review.summaries.native_CE.coherent | 32 |
| actual_review.summaries.native_CE.appropriate | 37 |
| actual_review.summaries.native_CE.notes_sha256 | "366209389693d5b382ab5a4f4001e0dd6c52fd10c33f9304672a195607b51e69" |
| actual_review.summaries.strong_staged.BPB | 1.1336128657420816 |
| actual_review.summaries.strong_staged.rates.eos | 76 |
| actual_review.summaries.strong_staged.rates.repetition | 2 |
| actual_review.summaries.strong_staged.rates.unicode_failure | 0 |
| actual_review.summaries.strong_staged.rates.role_leak | 0 |
| actual_review.summaries.strong_staged.rates.empty | 0 |
| actual_review.summaries.strong_staged.grammar2 | 65 |
| actual_review.summaries.strong_staged.relevance2 | 39 |
| actual_review.summaries.strong_staged.coherent | 23 |
| actual_review.summaries.strong_staged.appropriate | 26 |
| actual_review.summaries.strong_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| actual_review.quality_comparisons.native_CE.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparisons.native_CE.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparisons.native_CE.checks.EOS_nonworsening | false |
| actual_review.quality_comparisons.native_CE.checks.repetition_nonworsening | false |
| actual_review.quality_comparisons.native_CE.checks.no_empty_role_unicode | true |
| actual_review.quality_comparisons.native_CE.checks.BPB_gate | true |
| actual_review.quality_comparisons.native_CE.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparisons.native_CE.passed | false |
| actual_review.quality_comparisons.strong_staged.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparisons.strong_staged.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparisons.strong_staged.checks.EOS_nonworsening | false |
| actual_review.quality_comparisons.strong_staged.checks.repetition_nonworsening | false |
| actual_review.quality_comparisons.strong_staged.checks.no_empty_role_unicode | true |
| actual_review.quality_comparisons.strong_staged.checks.BPB_gate | true |
| actual_review.quality_comparisons.strong_staged.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparisons.strong_staged.passed | false |
| actual_review.absolute_dev_screen.grammar_at_least56 | false |
| actual_review.absolute_dev_screen.coherence_at_least27 | false |
| actual_review.absolute_dev_screen.appropriate_at_least27 | false |
| actual_review.absolute_dev_screen.EOS_at_least37 | true |
| actual_review.absolute_dev_screen.repetition_at_most18 | false |
| actual_review.absolute_dev_screen.no_empty_role_unicode | true |
| actual_review.original_Web.EOS_at_least8_more | true |
| actual_review.original_Web.repetition_no_worse | true |
| actual_review.original_Web.no_empty_role_unicode | true |
| actual_review.original_Web.BPB_degradation_at_most1percent | false |
| actual_review.eligible_for_final_Base_validation | false |
| actual_review.accounting.completed_updates | 3068 |
| actual_review.accounting.teachers | 100000000 |
| actual_review.accounting.physical_input_positions | 100532224 |
| actual_review.accounting.parameter_penalty_teacher_tokens | 0 |
| actual_review.accounting.source_teachers.web | 75000000 |
| actual_review.accounting.source_teachers.story | 5000000 |
| actual_review.accounting.source_teachers.ordinary_textbook | 10000000 |
| actual_review.accounting.source_teachers.conditional_textbook | 10000000 |
| actual_review.accounting.source_EOS.web | 159447 |
| actual_review.accounting.source_EOS.story | 38240 |
| actual_review.accounting.source_EOS.ordinary_textbook | 74183 |
| actual_review.accounting.source_EOS.conditional_textbook | 234328 |
| actual_review.scientific_teacher_tokens | 100000000 |
| actual_review.reused_control_teacher_tokens | 100000000 |
| actual_review.verification_teacher_tokens | 1307952 |
| actual_review.new_total_GPU_seconds | 178.9158119779895 |
| actual_review.Base_complete | false |
| actual_review.Base_adopted | false |
| actual_review.protected_test_used | false |
| actual_review.limitations | "98,304 new nonlinear readout weights/fresh Adam vs full native Adam; native weights frozen, same parent/input/target100M and evaluators. One learned seed/nonblind repeated dev. Stock HF export pending." |
| eligible_for_final_Base_validation | false |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/readout-adapter-comparison-v3-20261006/content-notes.json" |
| notes.sha256 | "e73739eb226de958f00099aecf53536e90147af4684972be7bd1f5fcc8f68148" |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>
