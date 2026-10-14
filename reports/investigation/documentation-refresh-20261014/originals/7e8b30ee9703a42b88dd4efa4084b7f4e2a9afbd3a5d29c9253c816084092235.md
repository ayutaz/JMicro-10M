# 学習量・配合・学習順序 — 5/6

[分野一覧へ](03_learning.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/evaluation/story20/evaluation/semantics.json) ／ SHA256: `da5d1a05183b8b028d18a25cc7fb3d45f4317992a9d4bb44ce0a57fd670e708b` ／ 203,239 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.5677083333333334 |
| summary.primary.accuracy.ci95 | [0.53125, 0.609375] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.5677083333333334 |
| summary.per_token_secondary.accuracy.point | 0.578125 |
| summary.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.578125 |
| summary.per_token_secondary.macro_f1 | 0.5781135555977539 |
| summary.per_token_secondary.mcc | 0.15625847779496568 |
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
<summary>reports/phase6/story-weight-comparison-20261006/probe/story20/timing/latest.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/probe/story20/timing/latest.json) ／ SHA256: `3c006f959bdf731ddec5c614147de7504703822599265ac80dc19294b2a31d23` ／ 272 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/story20-content-review.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/story20-content-review.json) ／ SHA256: `0f5fc927e805d6ba7ac06112482e9cdb91d44fa852a561c9782c4f463ab9d376` ／ 743 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.1352687563443153 |
| rates.eos | 38 |
| rates.repetition | 21 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 64 |
| relevance2 | 47 |
| coherent | 15 |
| appropriate | 24 |
| new_teacher_tokens | 100000000 |
| source_teacher_tokens.web | 60000000 |
| source_teacher_tokens.textbook | 20000000 |
| source_teacher_tokens.story | 20000000 |
| notes_sha256 | "c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/story20/training/latest.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/story20/training/latest.json) ／ SHA256: `27419a46e555c9e0f516c17c96f0eabe18c06b71b53fd457dee96cf9a30dc522` ／ 277 bytes

| 原キー | 保存値 |
|---|---|
| update | 65243 |
| tokens_seen | 2137882624 |

</details>

<details>
<summary>reports/phase6/story10_100m_launch.json — None</summary>

[原記録](../../reports/phase6/story10_100m_launch.json) ／ SHA256: `96947f4c1802206fb16ecce4ad9f73b9be1ff9ff865c826b3f1d49f3a1a8f304` ／ 601 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/story10_100m_result.json — complete_pending_content_review</summary>

[原記録](../../reports/phase6/story10_100m_result.json) ／ SHA256: `3c112577231183a9d350c49868d2797db15670701e4c2de78ba815a95912bfc3` ／ 80,542 bytes

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
| trained.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-10b-100m-20261005/coherent10/checkpoint-00308228.pt" |
| trained.checkpoint_sha256 | "bb5766d3239fdd88f45e3684c670a53f8c4a14ead8bdded44ed0e47315f17234" |
| trained.update | 308228 |
| trained.tokens | 10100015104 |
| trained.additional_input_tokens | 100007936 |
| trained.training_seconds | 159.11787758699938 |
| trained.source_tokens.web | 90013696 |
| trained.source_tokens.short | 9994240 |
| trained.source_eos_teachers.web | 190484 |
| trained.source_eos_teachers.short | 110512 |
| trained.sampler.kind | "eos-pilot-mixture-v1" |
| trained.sampler.position | 3052 |
| trained.sampler.web.seed | 42 |
| trained.sampler.web.epoch | 0 |
| trained.sampler.web.position | 9853536 |
| trained.sampler.web.context | 1024 |
| trained.sampler.web.blocks | 11939276 |
| trained.sampler.short.seed | 42 |
| trained.sampler.short.epoch | 0 |
| trained.sampler.short.position | 9760 |
| trained.sampler.short.context | 1024 |
| trained.sampler.short.blocks | 24414 |
| trained.sampler.source_tokens.web | 90013696 |
| trained.sampler.source_tokens.short | 9994240 |
| trained.sampler.source_eos.web | 190484 |
| trained.sampler.source_eos.short | 110512 |
| screen_BPB | 0.9845841038494589 |
| rates.eos | 17 |
| rates.repetition | 40 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.5623697916666667, 0.6510416666666666] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5727864583333333, 0.6614583333333334] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.mcc | 0.22916666666666666 |
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
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7099697885196374 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6586102719033232, 0.7613293051359517] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7099697885196374 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41519434628975266 |
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
| diagnostics.jcqa.primary.accuracy.point | 0.34584450402144773 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.31814119749776587, 0.3726541554959786] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.34584450402144773 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30804684057217646 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.13680406871686565 |
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
| mixture.EOS_at_least8_more | true |
| mixture.repetition_no_worse | true |
| mixture.no_empty_role_unicode | true |
| mixture.BPB_degradation_at_most1percent | true |
| scientific_tokens | 100007936 |
| verification_tokens | 262144 |
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
| resume_gate.seconds | 10.76926351000111 |
| resume_gate.GPU_optimizer_updates | 8 |
| resume_gate.input_tokens | 262144 |
| resume_gate.schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| resume_gate.checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-10b-100m-20261005/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-10b-100m-20261005/resume-gate/resumed.pt"] |
| protected_test_used | false |
| GPU_seconds | 264.37010258400005 |

</details>

<details>
<summary>reports/phase6/story10_100m_review.json — passed</summary>

[原記録](../../reports/phase6/story10_100m_review.json) ／ SHA256: `6855f514ed27e72ff94b81b3b9b8f559a983aa5dccc9af1a9bd3b1e5b3a7c0c3` ／ 166,093 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-04T16:19:52.939836Z" |
| summary.grammar_score2 | 41 |
| summary.relevance_score2 | 15 |
| summary.coherence_score2 | 4 |
| summary.appropriate_EOS | 4 |
| selection.original_mixture.EOS_at_least8_more | true |
| selection.original_mixture.repetition_no_worse | true |
| selection.original_mixture.no_empty_role_unicode | true |
| selection.original_mixture.BPB_degradation_at_most1percent | true |
| selection.coherence_gain_at_least8 | false |
| selection.paired_coherence_CI_lower_above0 | true |
| selection.coherence_difference_count | 4 |
| selection.paired_CI95 | [0.0125, 0.1] |
| selection.eligible_for_full | false |
| paired_diagnostics.semantics.point | -0.005208333333333333 |
| paired_diagnostics.semantics.ci95 | [-0.036458333333333336, 0.026041666666666668] |
| paired_diagnostics.semantics.units | 96 |
| paired_diagnostics.semantics.examples | 192 |
| paired_diagnostics.semantics.unit | "family/prompt" |
| paired_diagnostics.semantics.seed | 42 |
| paired_diagnostics.semantics.repetitions | 2000 |
| paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jblimp.point | 0.00906344410876133 |
| paired_diagnostics.jblimp.ci95 | [-0.021148036253776436, 0.03927492447129909] |
| paired_diagnostics.jblimp.units | 331 |
| paired_diagnostics.jblimp.examples | 331 |
| paired_diagnostics.jblimp.unit | "family/prompt" |
| paired_diagnostics.jblimp.seed | 42 |
| paired_diagnostics.jblimp.repetitions | 2000 |
| paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jcqa.point | 0.01966041108132261 |
| paired_diagnostics.jcqa.ci95 | [-0.0008936550491510277, 0.040214477211796246] |
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
<summary>reports/phase6/story10_execution_completion.json — passed</summary>

[原記録](../../reports/phase6/story10_execution_completion.json) ／ SHA256: `4e935813e734bb1f0f42466037dbd568f64b7d6288e9f65b96380e30cb47622b` ／ 7,775 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-04T16:39:33.330611Z" |
| scope | "plan49 stages1–3:100M screen, prespecified matched lowerLR alternative, judgment/proposal;500M entry not met" |
| checks.normalLR_actual_job_complete_and_exited | true |
| checks.normalLR_source_config_and_screen_bindings | true |
| checks.normalLR_relevant_tests | true |
| checks.normalLR_actual_CUDA_save_resume | true |
| checks.normalLR_original_GPU_budget | true |
| checks.normalLR_protected_test_unused | true |
| checks.normalLR_honest_quality_scope | true |
| checks.normalLR_scientific_accounting | true |
| checks.normalLR_coherent10_common256_body_coverage | true |
| checks.normalLR_coherent10_BPB_from_actual_finite_NLL | true |
| checks.normalLR_coherent10_actual_checkpoint_hash | true |
| checks.normalLR_coherent10_equal100M_finite_updates | true |
| checks.normalLR_coherent10_fixed_fork_LR | true |
| checks.normalLR_coherent10_source_counts_no_story_wrap | true |
| checks.normalLR_coherent10_exact80_dev_requests | true |
| checks.normalLR_coherent10_all80_content_matches_actual_raw | true |
| checks.normalLR_coherent10_complete_Japanese_diagnostics | true |
| checks.lowerLR_actual_job_complete_and_exited | true |
| checks.lowerLR_source_config_and_screen_bindings | true |
| checks.lowerLR_relevant_tests | true |
| checks.lowerLR_actual_CUDA_save_resume | true |
| checks.lowerLR_original_GPU_budget | true |
| checks.lowerLR_protected_test_unused | true |
| checks.lowerLR_honest_quality_scope | true |
| checks.lowerLR_scientific_accounting | true |
| checks.lowerLR_web_common256_body_coverage | true |
| checks.lowerLR_web_BPB_from_actual_finite_NLL | true |
| checks.lowerLR_web_actual_checkpoint_hash | true |
| checks.lowerLR_web_equal100M_finite_updates | true |
| checks.lowerLR_web_fixed_fork_LR | true |
| checks.lowerLR_web_source_counts_no_story_wrap | true |
| checks.lowerLR_web_exact80_dev_requests | true |
| checks.lowerLR_web_all80_content_matches_actual_raw | true |
| checks.lowerLR_web_complete_Japanese_diagnostics | true |
| checks.lowerLR_coherent10_common256_body_coverage | true |
| checks.lowerLR_coherent10_BPB_from_actual_finite_NLL | true |
| checks.lowerLR_coherent10_actual_checkpoint_hash | true |
| checks.lowerLR_coherent10_equal100M_finite_updates | true |
| checks.lowerLR_coherent10_fixed_fork_LR | true |
| checks.lowerLR_coherent10_source_counts_no_story_wrap | true |
| checks.lowerLR_coherent10_exact80_dev_requests | true |
| checks.lowerLR_coherent10_all80_content_matches_actual_raw | true |
| checks.lowerLR_coherent10_complete_Japanese_diagnostics | true |
| checks.first_screen_failed_frozen_content_gain | true |
| checks.lowerLR_screen_failed_original_selection | true |
| checks.conditional_full_correctly_not_run | true |
| checks.no_500M_without_entry_conditions | true |
| checks.actual_UI_identity_live | true |
| checks.HTTP_UI_original_parent_restored | true |
| checks.report_exists_docs/50_story10_and_budget_execution.md | true |
| checks.report_exists_docs/51_story10_judgment_and_next_proposal.md | true |
| checks.report_exists_docs/autonomous_status.md | true |
| scientific_tokens | 300023808 |
| verification_tokens | 524288 |
| GPU_seconds | 775.5223158219997 |
| original_acceptance_gates_unchanged | true |
| original_UI.training_tokens | 10000007168 |
| original_UI.update | 305176 |
| original_UI.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| protected_test_used | false |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-10b-100m-20261005/tests.xml | "108ed0f777b7b12d59b64c1b179ace5a306d5b7bf5816652e1cca63ef1cad68d" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/tests.xml | "69c2d6525b8ccd25688dcdb54c6dbd709bcab47bab97063b2aa6f5f2d78ec207" |
| sources.docs/50_story10_and_budget_execution.md | "4df7ebd767a357943707e3965d1a5b2a98dba1bc5b176b85ba08a0325b71474d" |
| sources.docs/autonomous_status.md | "79af5fa4801c40420e264ee399941b986ac3e42787252c9af4ae2fe9b84ca778" |

</details>

<details>
<summary>reports/phase6/story10_low_lr_launch.json — None</summary>

[原記録](../../reports/phase6/story10_low_lr_launch.json) ／ SHA256: `53dfeea5c33c90c09d34c3c3df4ec5f1ed7b9671214dadcc115b804b07d24f17` ／ 618 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/story10_low_lr_result.json — complete_pending_content_review</summary>

[原記録](../../reports/phase6/story10_low_lr_result.json) ／ SHA256: `c2ddaab87350f98f84fa80ccc38ac485c46e3e82454913b83ea434ac3a9aa0eb` ／ 165,009 bytes

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
| arms.web.status | "complete" |
| arms.web.binding.parent.update | 305176 |
| arms.web.binding.parent.tokens_seen | 10000007168 |
| arms.web.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| arms.web.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| arms.web.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| arms.web.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| arms.web.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| arms.web.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| arms.web.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| arms.web.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/web/checkpoint-00308228.pt" |
| arms.web.checkpoint_sha256 | "b746a2c0b9e0f6fa484e8cd9c974e247e8a3b9fa461cc67cde6f371b4ee4eadf" |
| arms.web.update | 308228 |
| arms.web.tokens | 10100015104 |
| arms.web.additional_input_tokens | 100007936 |
| arms.web.training_seconds | 159.38321004999852 |
| arms.web.source_tokens.web | 100007936 |
| arms.web.source_tokens.short | 0 |
| arms.web.source_eos_teachers.web | 211670 |
| arms.web.source_eos_teachers.short | 0 |
| arms.web.sampler.kind | "eos-pilot-mixture-v1" |
| arms.web.sampler.position | 3052 |
| arms.web.sampler.web.seed | 42 |
| arms.web.sampler.web.epoch | 0 |
| arms.web.sampler.web.position | 9863296 |
| arms.web.sampler.web.context | 1024 |
| arms.web.sampler.web.blocks | 11939276 |
| arms.web.sampler.short.seed | 42 |
| arms.web.sampler.short.epoch | 0 |
| arms.web.sampler.short.position | 0 |
| arms.web.sampler.short.context | 1024 |
| arms.web.sampler.short.blocks | 24414 |
| arms.web.sampler.source_tokens.web | 100007936 |
| arms.web.sampler.source_tokens.short | 0 |
| arms.web.sampler.source_eos.web | 211670 |
| arms.web.sampler.source_eos.short | 0 |
| arms.coherent10.status | "complete" |
| arms.coherent10.binding.plan_sha256 | "d91831366c5b6051e5aca47ae10712ea98ce5f39199d58b2581c6fa65575bbf3" |
| arms.coherent10.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| arms.coherent10.binding.parent.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| arms.coherent10.binding.parent.update | 305176 |
| arms.coherent10.binding.parent.tokens_seen | 10000007168 |
| arms.coherent10.binding.peak_lr | 0.0001 |
| arms.coherent10.binding.implementation.src/jmicro/model.py | "2861baaf1860174fc8f7ae5da23386ae39146b8a907077bce4958a4b6b315b3a" |
| arms.coherent10.binding.implementation.src/jmicro/shards.py | "9544c5a0c385f817f93510eaae6375e8c044286822fd86e333d2f07123b63e4c" |
| arms.coherent10.binding.implementation.src/jmicro/training.py | "d898b9ba7d15d7e24c497c5981f3fc090894833d08f202d44ef881d0bb6f5086" |
| arms.coherent10.binding.implementation.uv.lock | "29821397f48485dfa3317319da5248cb260c3963b6db4aad18276ed3ab9ce298" |
| arms.coherent10.binding.source_sha256.scripts/run_story10_low_lr.py | "5f47de181085b44bb194cb5b7ac9549008a4ead715df8007c61be73e7f336647" |
| arms.coherent10.binding.source_sha256.scripts/run_story10_low_lr.ps1 | "e14c1f44205c49db8611bad88865e8fa993a9a441ec403e04a7c82b9ab2ae85f" |
| arms.coherent10.binding.source_sha256.scripts/run_story10_comparison.py | "3f693393992fd18bde70f9a7d4ec16a85169857183c4c9bc503064b9a11a56a0" |
| arms.coherent10.binding.source_sha256.scripts/run_story10_comparison.ps1 | "f85ff6dbee30a45aa3143ac000a9db28d6ee6f17cf2424bde01babf863feb0ea" |
| arms.coherent10.binding.source_sha256.scripts/run_complete_text_comparison.py | "9d91d1d6124e62e4f40f7a99762f948186602e95cc362be10bfe03297874d8f7" |
| arms.coherent10.binding.source_sha256.scripts/run_complete_text_comparison.ps1 | "7fb1a82d9450daf7f6955d56093be61cf31c25dd479e23715372b1d8db345e5b" |
| arms.coherent10.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| arms.coherent10.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| arms.coherent10.binding.source_sha256.scripts/inspect_complete_text_data.py | "bf18510673c0c4352df911df850e3f598f921977cc34d580aa3fc87e8e8df626" |
| arms.coherent10.binding.source_sha256.scripts/prepare_story_text.py | "ecbd5d1a320d59a318b282026b36e4b7ad9284d897169f0c57e77f6dae5c90fa" |
| arms.coherent10.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| arms.coherent10.binding.source_sha256.src/jmicro/low_lr_pilot.py | "dcb6a1374c64c2852086b57a50433720b1e6b60263d5581eb742c3a1864ff64e" |
| arms.coherent10.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| arms.coherent10.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| arms.coherent10.binding.source_sha256.scripts/evaluate_japanese_base.py | "9cabf705a67181b6a45eb20c1a62b69335140f2465b24ac2066f05e51ee48d02" |
| arms.coherent10.binding.source_sha256.src/jmicro/japanese_evaluation.py | "8693e2a54e63c1b085b617b207cc5db618ae80af1eb7cb54133ba8b254da6801" |
| arms.coherent10.binding.source_sha256.src/jmicro/readiness.py | "69a92251f4a697b551b9c3cfef9e2b992e776e2047c0331f7c43ba2331d172ea" |
| arms.coherent10.binding.source_sha256.src/jmicro/evaluation_memory.py | "ba22fb7ca7ddb6633a308c2b1a32a59147ecb38e568d9f838ab032300147c6b4" |
| arms.coherent10.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| arms.coherent10.binding.source_sha256.scripts/evaluate_complete_text_full.py | "9be7d2c3dda500571f9f95215021054b48708585cead582325d63e5da289dc9b" |
| arms.coherent10.binding.source_sha256.scripts/evaluate_complete_text_full.ps1 | "ecd8c8e7341192ae32551c3309f7d20db8ac294c318c6c5e7c97dc8b34b3b3a5" |
| arms.coherent10.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| arms.coherent10.binding.source_sha256.scripts/compare_base_10b.py | "bacea1be511e08f4d005084ad309ff840bf0b32de1650c349392aaafbd218291" |
| arms.coherent10.binding.source_sha256.scripts/compare_base_5b.py | "1cf535ca7e3de85cdf5d5cf3987148b68f24602e0b10bc26ce97bca6296b14c8" |
| arms.coherent10.binding.arm | "coherent10" |
| arms.coherent10.binding.short_manifest_sha256 | "b89d692c6cb7580909b3cfa90fb8d277b3dfc606ac458724ccafd5c444d77f8d" |
| arms.coherent10.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/coherent10/checkpoint-00308228.pt" |
| arms.coherent10.checkpoint_sha256 | "f381ba389854c7540056b3f2dab78b01cd48b60d522e698fa397b6f29276cb2b" |
| arms.coherent10.update | 308228 |
| arms.coherent10.tokens | 10100015104 |
| arms.coherent10.additional_input_tokens | 100007936 |
| arms.coherent10.training_seconds | 148.28403895299925 |
| arms.coherent10.source_tokens.web | 90013696 |
| arms.coherent10.source_tokens.short | 9994240 |
| arms.coherent10.source_eos_teachers.web | 190484 |
| arms.coherent10.source_eos_teachers.short | 110512 |
| arms.coherent10.sampler.kind | "eos-pilot-mixture-v1" |
| arms.coherent10.sampler.position | 3052 |
| arms.coherent10.sampler.web.seed | 42 |
| arms.coherent10.sampler.web.epoch | 0 |
| arms.coherent10.sampler.web.position | 9853536 |
| arms.coherent10.sampler.web.context | 1024 |
| arms.coherent10.sampler.web.blocks | 11939276 |
| arms.coherent10.sampler.short.seed | 42 |
| arms.coherent10.sampler.short.epoch | 0 |
| arms.coherent10.sampler.short.position | 9760 |
| arms.coherent10.sampler.short.context | 1024 |
| arms.coherent10.sampler.short.blocks | 24414 |
| arms.coherent10.sampler.source_tokens.web | 90013696 |
| arms.coherent10.sampler.source_tokens.short | 9994240 |
| arms.coherent10.sampler.source_eos.web | 190484 |
| arms.coherent10.sampler.source_eos.short | 110512 |
| arms.coherent10.initial_state | "same final10B weights/Adam/RNG/Web cursor; explicit equal low-LR fork" |
| arms.coherent10.learning_rate_fork.parent_base_lrs | [0.002, 0.002] |
| arms.coherent10.learning_rate_fork.parent_actual_lrs | [0.0002, 0.0002] |
| arms.coherent10.learning_rate_fork.new_peak_lr | 0.0001 |
| arms.coherent10.learning_rate_fork.moments_weights_RNG_cursors_preserved | true |
| rates.web.eos | 0 |
| rates.web.repetition | 59 |
| rates.web.unicode_failure | 0 |
| rates.web.role_leak | 0 |
| rates.web.empty | 0 |
| rates.coherent10.outputs | 80 |
| rates.coherent10.eos | 16 |
| rates.coherent10.repetition | 36 |
| rates.coherent10.unicode_failure | 0 |
| rates.coherent10.role_leak | 0 |
| rates.coherent10.empty | 0 |
| BPB.web | 0.9774590515987371 |
| BPB.coherent10 | 0.9812034955039882 |
| diagnostics.web.semantics.primary.accuracy.point | 0.609375 |
| diagnostics.web.semantics.primary.accuracy.ci95 | [0.5625, 0.65625] |
| diagnostics.web.semantics.primary.accuracy.units | 96 |
| diagnostics.web.semantics.primary.accuracy.examples | 192 |
| diagnostics.web.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.web.semantics.primary.accuracy.seed | 42 |
| diagnostics.web.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.web.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.primary.hard_accuracy | 0.609375 |
| diagnostics.web.semantics.per_token_secondary.accuracy.point | 0.609375 |
| diagnostics.web.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.65625] |
| diagnostics.web.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.web.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.web.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.web.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.web.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.web.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.per_token_secondary.count | 192 |
| diagnostics.web.semantics.per_token_secondary.hard_accuracy | 0.609375 |
| diagnostics.web.semantics.per_token_secondary.macro_f1 | 0.6091099106924727 |
| diagnostics.web.semantics.per_token_secondary.mcc | 0.21904730367901812 |
| diagnostics.web.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.web.semantics.unigram_control.accuracy.point | 0.5 |
| diagnostics.web.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| diagnostics.web.semantics.unigram_control.accuracy.units | 96 |
| diagnostics.web.semantics.unigram_control.accuracy.examples | 192 |
| diagnostics.web.semantics.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.web.semantics.unigram_control.accuracy.seed | 42 |
| diagnostics.web.semantics.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.web.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.unigram_control.hard_accuracy | 0.5 |
| diagnostics.web.semantics.train_majority_accuracy | 0.5 |
| diagnostics.web.semantics.categories.negation.seed | 42 |
| diagnostics.web.semantics.categories.negation.repetitions | 2000 |
| diagnostics.web.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.categories.quantity.seed | 42 |
| diagnostics.web.semantics.categories.quantity.repetitions | 2000 |
| diagnostics.web.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.categories.time.seed | 42 |
| diagnostics.web.semantics.categories.time.repetitions | 2000 |
| diagnostics.web.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.categories.comparison.seed | 42 |
| diagnostics.web.semantics.categories.comparison.repetitions | 2000 |
| diagnostics.web.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.categories.coreference.seed | 42 |
| diagnostics.web.semantics.categories.coreference.repetitions | 2000 |
| diagnostics.web.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.categories.causality.seed | 42 |
| diagnostics.web.semantics.categories.causality.repetitions | 2000 |
| diagnostics.web.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.web.jblimp.primary.accuracy.point | 0.7371601208459214 |
| diagnostics.web.jblimp.primary.accuracy.ci95 | [0.6888217522658611, 0.7854984894259819] |
| diagnostics.web.jblimp.primary.accuracy.units | 331 |
| diagnostics.web.jblimp.primary.accuracy.examples | 331 |
| diagnostics.web.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.web.jblimp.primary.accuracy.seed | 42 |
| diagnostics.web.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.web.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.primary.hard_accuracy | 0.7371601208459214 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.point | 0.7129909365558912 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.ci95 | [0.6616314199395771, 0.7643504531722054] |
| diagnostics.web.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.web.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.web.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.per_token_secondary.count | 331 |
| diagnostics.web.jblimp.per_token_secondary.hard_accuracy | 0.7129909365558912 |
| diagnostics.web.jblimp.per_token_secondary.macro_f1 | 0.41622574955908287 |
| diagnostics.web.jblimp.per_token_secondary.mcc | 0.0 |
| diagnostics.web.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.web.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| diagnostics.web.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| diagnostics.web.jblimp.unigram_control.accuracy.units | 331 |
| diagnostics.web.jblimp.unigram_control.accuracy.examples | 331 |
| diagnostics.web.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.web.jblimp.unigram_control.accuracy.seed | 42 |
| diagnostics.web.jblimp.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.web.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| diagnostics.web.jblimp.train_majority_accuracy | null |
| diagnostics.web.jblimp.categories.island effects.seed | 42 |
| diagnostics.web.jblimp.categories.island effects.repetitions | 2000 |
| diagnostics.web.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.binding.seed | 42 |
| diagnostics.web.jblimp.categories.binding.repetitions | 2000 |
| diagnostics.web.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.argument structure.seed | 42 |
| diagnostics.web.jblimp.categories.argument structure.repetitions | 2000 |
| diagnostics.web.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.ellipsis.seed | 42 |
| diagnostics.web.jblimp.categories.ellipsis.repetitions | 2000 |
| diagnostics.web.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.verbal agreement.seed | 42 |
| diagnostics.web.jblimp.categories.verbal agreement.repetitions | 2000 |
| diagnostics.web.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.filler-gap.seed | 42 |
| diagnostics.web.jblimp.categories.filler-gap.repetitions | 2000 |
| diagnostics.web.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.morphology.seed | 42 |
| diagnostics.web.jblimp.categories.morphology.repetitions | 2000 |
| diagnostics.web.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.nominal structure.seed | 42 |
| diagnostics.web.jblimp.categories.nominal structure.repetitions | 2000 |
| diagnostics.web.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.quantifiers.seed | 42 |
| diagnostics.web.jblimp.categories.quantifiers.repetitions | 2000 |
| diagnostics.web.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.NPI licensing.seed | 42 |
| diagnostics.web.jblimp.categories.NPI licensing.repetitions | 2000 |
| diagnostics.web.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.categories.control/raising.seed | 42 |
| diagnostics.web.jblimp.categories.control/raising.repetitions | 2000 |
| diagnostics.web.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.web.jblimp.raw_pair_accuracy | 0.770392749244713 |
| diagnostics.web.jcqa.primary.accuracy.point | 0.3118856121537087 |
| diagnostics.web.jcqa.primary.accuracy.ci95 | [0.28596961572832885, 0.3386952636282395] |
| diagnostics.web.jcqa.primary.accuracy.units | 1119 |
| diagnostics.web.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.web.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.web.jcqa.primary.accuracy.seed | 42 |
| diagnostics.web.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.web.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jcqa.primary.hard_accuracy | 0.3118856121537087 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.point | 0.3092046470062556 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3351206434316354] |
| diagnostics.web.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.web.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.web.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jcqa.per_token_secondary.count | 1119 |
| diagnostics.web.jcqa.per_token_secondary.hard_accuracy | 0.3092046470062556 |
| diagnostics.web.jcqa.per_token_secondary.macro_f1 | 0.30864363095646385 |
| diagnostics.web.jcqa.per_token_secondary.mcc | 0.13706731356027757 |
| diagnostics.web.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.web.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| diagnostics.web.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| diagnostics.web.jcqa.unigram_control.accuracy.units | 1119 |
| diagnostics.web.jcqa.unigram_control.accuracy.examples | 1119 |
| diagnostics.web.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.web.jcqa.unigram_control.accuracy.seed | 42 |
| diagnostics.web.jcqa.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.web.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| diagnostics.web.jcqa.train_majority_accuracy | 0.21179624664879357 |
| diagnostics.web.jcqa.categories.commonsense.seed | 42 |
| diagnostics.web.jcqa.categories.commonsense.repetitions | 2000 |
| diagnostics.web.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.web.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.web.semantic_both_contexts.correct | 23 |
| diagnostics.coherent10.semantics.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/coherent10/evaluation/semantics.json" |
| diagnostics.coherent10.semantics.complete | true |
| diagnostics.coherent10.semantics.expected | 192 |
| diagnostics.coherent10.semantics.count | 192 |
| diagnostics.coherent10.semantics.primary.accuracy.point | 0.59375 |
| diagnostics.coherent10.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.6355468749999993] |
| diagnostics.coherent10.semantics.primary.accuracy.units | 96 |
| diagnostics.coherent10.semantics.primary.accuracy.examples | 192 |
| diagnostics.coherent10.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.semantics.primary.accuracy.seed | 42 |
| diagnostics.coherent10.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.primary.count | 192 |
| diagnostics.coherent10.semantics.primary.hard_accuracy | 0.59375 |
| diagnostics.coherent10.semantics.primary.macro_f1 | 0.5937059142702116 |
| diagnostics.coherent10.semantics.primary.mcc | 0.18754070335443587 |
| diagnostics.coherent10.semantics.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.ci95 | [0.551953125, 0.6302083333333334] |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.per_token_secondary.count | 192 |
| diagnostics.coherent10.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| diagnostics.coherent10.semantics.per_token_secondary.macro_f1 | 0.5884411884411884 |
| diagnostics.coherent10.semantics.per_token_secondary.mcc | 0.17716986318620467 |
| diagnostics.coherent10.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.semantics.unigram_control.accuracy.point | 0.5 |
| diagnostics.coherent10.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| diagnostics.coherent10.semantics.unigram_control.accuracy.units | 96 |
| diagnostics.coherent10.semantics.unigram_control.accuracy.examples | 192 |
| diagnostics.coherent10.semantics.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.semantics.unigram_control.accuracy.seed | 42 |
| diagnostics.coherent10.semantics.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.coherent10.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.unigram_control.count | 192 |
| diagnostics.coherent10.semantics.unigram_control.hard_accuracy | 0.5 |
| diagnostics.coherent10.semantics.unigram_control.macro_f1 | 0.4991304347826087 |
| diagnostics.coherent10.semantics.unigram_control.mcc | 0.0 |
| diagnostics.coherent10.semantics.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.semantics.chance | 0.5 |
| diagnostics.coherent10.semantics.above_chance_evidence | true |
| diagnostics.coherent10.semantics.train_majority_accuracy | 0.5 |
| diagnostics.coherent10.semantics.categories.negation.point | 1.0 |
| diagnostics.coherent10.semantics.categories.negation.ci95 | [1.0, 1.0] |
| diagnostics.coherent10.semantics.categories.negation.units | 16 |
| diagnostics.coherent10.semantics.categories.negation.examples | 32 |
| diagnostics.coherent10.semantics.categories.negation.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.negation.seed | 42 |
| diagnostics.coherent10.semantics.categories.negation.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.categories.quantity.point | 0.4375 |
| diagnostics.coherent10.semantics.categories.quantity.ci95 | [0.34375, 0.5] |
| diagnostics.coherent10.semantics.categories.quantity.units | 16 |
| diagnostics.coherent10.semantics.categories.quantity.examples | 32 |
| diagnostics.coherent10.semantics.categories.quantity.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.quantity.seed | 42 |
| diagnostics.coherent10.semantics.categories.quantity.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.categories.time.point | 0.5 |
| diagnostics.coherent10.semantics.categories.time.ci95 | [0.5, 0.5] |
| diagnostics.coherent10.semantics.categories.time.units | 16 |
| diagnostics.coherent10.semantics.categories.time.examples | 32 |
| diagnostics.coherent10.semantics.categories.time.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.time.seed | 42 |
| diagnostics.coherent10.semantics.categories.time.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.categories.comparison.point | 0.5 |
| diagnostics.coherent10.semantics.categories.comparison.ci95 | [0.5, 0.5] |
| diagnostics.coherent10.semantics.categories.comparison.units | 16 |
| diagnostics.coherent10.semantics.categories.comparison.examples | 32 |
| diagnostics.coherent10.semantics.categories.comparison.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.comparison.seed | 42 |
| diagnostics.coherent10.semantics.categories.comparison.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.categories.coreference.point | 0.5625 |
| diagnostics.coherent10.semantics.categories.coreference.ci95 | [0.5, 0.65625] |
| diagnostics.coherent10.semantics.categories.coreference.units | 16 |
| diagnostics.coherent10.semantics.categories.coreference.examples | 32 |
| diagnostics.coherent10.semantics.categories.coreference.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.coreference.seed | 42 |
| diagnostics.coherent10.semantics.categories.coreference.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.categories.causality.point | 0.5625 |
| diagnostics.coherent10.semantics.categories.causality.ci95 | [0.5, 0.65625] |
| diagnostics.coherent10.semantics.categories.causality.units | 16 |
| diagnostics.coherent10.semantics.categories.causality.examples | 32 |
| diagnostics.coherent10.semantics.categories.causality.unit | "family/prompt" |
| diagnostics.coherent10.semantics.categories.causality.seed | 42 |
| diagnostics.coherent10.semantics.categories.causality.repetitions | 2000 |
| diagnostics.coherent10.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.semantics.tie_examples | 0 |
| diagnostics.coherent10.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.coherent10.jblimp.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/coherent10/evaluation/jblimp.json" |
| diagnostics.coherent10.jblimp.complete | true |
| diagnostics.coherent10.jblimp.expected | 331 |
| diagnostics.coherent10.jblimp.count | 331 |
| diagnostics.coherent10.jblimp.primary.accuracy.point | 0.7552870090634441 |
| diagnostics.coherent10.jblimp.primary.accuracy.ci95 | [0.7099697885196374, 0.8006042296072508] |
| diagnostics.coherent10.jblimp.primary.accuracy.units | 331 |
| diagnostics.coherent10.jblimp.primary.accuracy.examples | 331 |
| diagnostics.coherent10.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.primary.accuracy.seed | 42 |
| diagnostics.coherent10.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.primary.count | 331 |
| diagnostics.coherent10.jblimp.primary.hard_accuracy | 0.7552870090634441 |
| diagnostics.coherent10.jblimp.primary.macro_f1 | 0.43029259896729777 |
| diagnostics.coherent10.jblimp.primary.mcc | 0.0 |
| diagnostics.coherent10.jblimp.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7643504531722054] |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.per_token_secondary.count | 331 |
| diagnostics.coherent10.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| diagnostics.coherent10.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
| diagnostics.coherent10.jblimp.per_token_secondary.mcc | 0.0 |
| diagnostics.coherent10.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.units | 331 |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.examples | 331 |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.seed | 42 |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.unigram_control.count | 331 |
| diagnostics.coherent10.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| diagnostics.coherent10.jblimp.unigram_control.macro_f1 | 0.3231083844580777 |
| diagnostics.coherent10.jblimp.unigram_control.mcc | 0.0 |
| diagnostics.coherent10.jblimp.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jblimp.chance | 0.5 |
| diagnostics.coherent10.jblimp.above_chance_evidence | true |
| diagnostics.coherent10.jblimp.train_majority_accuracy | null |
| diagnostics.coherent10.jblimp.categories.island effects.point | 0.8181818181818182 |
| diagnostics.coherent10.jblimp.categories.island effects.ci95 | [0.5454545454545454, 1.0] |
| diagnostics.coherent10.jblimp.categories.island effects.units | 11 |
| diagnostics.coherent10.jblimp.categories.island effects.examples | 11 |
| diagnostics.coherent10.jblimp.categories.island effects.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.island effects.seed | 42 |
| diagnostics.coherent10.jblimp.categories.island effects.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.binding.point | 0.23076923076923078 |
| diagnostics.coherent10.jblimp.categories.binding.ci95 | [0.0, 0.46153846153846156] |
| diagnostics.coherent10.jblimp.categories.binding.units | 13 |
| diagnostics.coherent10.jblimp.categories.binding.examples | 13 |
| diagnostics.coherent10.jblimp.categories.binding.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.binding.seed | 42 |
| diagnostics.coherent10.jblimp.categories.binding.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.argument structure.point | 0.8857142857142857 |
| diagnostics.coherent10.jblimp.categories.argument structure.ci95 | [0.8285714285714286, 0.9357142857142857] |
| diagnostics.coherent10.jblimp.categories.argument structure.units | 140 |
| diagnostics.coherent10.jblimp.categories.argument structure.examples | 140 |
| diagnostics.coherent10.jblimp.categories.argument structure.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.argument structure.seed | 42 |
| diagnostics.coherent10.jblimp.categories.argument structure.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.ellipsis.point | 0.7368421052631579 |
| diagnostics.coherent10.jblimp.categories.ellipsis.ci95 | [0.5263157894736842, 0.8960526315789402] |
| diagnostics.coherent10.jblimp.categories.ellipsis.units | 19 |
| diagnostics.coherent10.jblimp.categories.ellipsis.examples | 19 |
| diagnostics.coherent10.jblimp.categories.ellipsis.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.ellipsis.seed | 42 |
| diagnostics.coherent10.jblimp.categories.ellipsis.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.verbal agreement.point | 0.47540983606557374 |
| diagnostics.coherent10.jblimp.categories.verbal agreement.ci95 | [0.3442622950819672, 0.6065573770491803] |
| diagnostics.coherent10.jblimp.categories.verbal agreement.units | 61 |
| diagnostics.coherent10.jblimp.categories.verbal agreement.examples | 61 |
| diagnostics.coherent10.jblimp.categories.verbal agreement.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.verbal agreement.seed | 42 |
| diagnostics.coherent10.jblimp.categories.verbal agreement.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.filler-gap.point | 0.4444444444444444 |
| diagnostics.coherent10.jblimp.categories.filler-gap.ci95 | [0.1111111111111111, 0.7777777777777778] |
| diagnostics.coherent10.jblimp.categories.filler-gap.units | 9 |
| diagnostics.coherent10.jblimp.categories.filler-gap.examples | 9 |
| diagnostics.coherent10.jblimp.categories.filler-gap.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.filler-gap.seed | 42 |
| diagnostics.coherent10.jblimp.categories.filler-gap.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.morphology.point | 0.8857142857142857 |
| diagnostics.coherent10.jblimp.categories.morphology.ci95 | [0.7714285714285715, 0.9714285714285714] |
| diagnostics.coherent10.jblimp.categories.morphology.units | 35 |
| diagnostics.coherent10.jblimp.categories.morphology.examples | 35 |
| diagnostics.coherent10.jblimp.categories.morphology.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.morphology.seed | 42 |
| diagnostics.coherent10.jblimp.categories.morphology.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.nominal structure.point | 0.9565217391304348 |
| diagnostics.coherent10.jblimp.categories.nominal structure.ci95 | [0.8695652173913043, 1.0] |
| diagnostics.coherent10.jblimp.categories.nominal structure.units | 23 |
| diagnostics.coherent10.jblimp.categories.nominal structure.examples | 23 |
| diagnostics.coherent10.jblimp.categories.nominal structure.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.nominal structure.seed | 42 |
| diagnostics.coherent10.jblimp.categories.nominal structure.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.quantifiers.point | 0.8571428571428571 |
| diagnostics.coherent10.jblimp.categories.quantifiers.ci95 | [0.6428571428571429, 1.0] |
| diagnostics.coherent10.jblimp.categories.quantifiers.units | 14 |
| diagnostics.coherent10.jblimp.categories.quantifiers.examples | 14 |
| diagnostics.coherent10.jblimp.categories.quantifiers.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.quantifiers.seed | 42 |
| diagnostics.coherent10.jblimp.categories.quantifiers.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.NPI licensing.point | 0.5 |
| diagnostics.coherent10.jblimp.categories.NPI licensing.ci95 | [0.0, 1.0] |
| diagnostics.coherent10.jblimp.categories.NPI licensing.units | 4 |
| diagnostics.coherent10.jblimp.categories.NPI licensing.examples | 4 |
| diagnostics.coherent10.jblimp.categories.NPI licensing.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.NPI licensing.seed | 42 |
| diagnostics.coherent10.jblimp.categories.NPI licensing.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.categories.control/raising.point | 0.0 |
| diagnostics.coherent10.jblimp.categories.control/raising.ci95 | [0.0, 0.0] |
| diagnostics.coherent10.jblimp.categories.control/raising.units | 2 |
| diagnostics.coherent10.jblimp.categories.control/raising.examples | 2 |
| diagnostics.coherent10.jblimp.categories.control/raising.unit | "family/prompt" |
| diagnostics.coherent10.jblimp.categories.control/raising.seed | 42 |
| diagnostics.coherent10.jblimp.categories.control/raising.repetitions | 2000 |
| diagnostics.coherent10.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jblimp.tie_examples | 0 |
| diagnostics.coherent10.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.coherent10.jblimp.raw_pair_accuracy | 0.770392749244713 |
| diagnostics.coherent10.jcqa.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/coherent10/evaluation/jcqa.json" |
| diagnostics.coherent10.jcqa.complete | true |
| diagnostics.coherent10.jcqa.expected | 1119 |
| diagnostics.coherent10.jcqa.count | 1119 |
| diagnostics.coherent10.jcqa.primary.accuracy.point | 0.34226988382484363 |
| diagnostics.coherent10.jcqa.primary.accuracy.ci95 | [0.314544235924933, 0.36910187667560307] |
| diagnostics.coherent10.jcqa.primary.accuracy.units | 1119 |
| diagnostics.coherent10.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.coherent10.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jcqa.primary.accuracy.seed | 42 |
| diagnostics.coherent10.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jcqa.primary.count | 1119 |
| diagnostics.coherent10.jcqa.primary.hard_accuracy | 0.34226988382484363 |
| diagnostics.coherent10.jcqa.primary.macro_f1 | 0.3416806896824339 |
| diagnostics.coherent10.jcqa.primary.mcc | 0.17770765326762497 |
| diagnostics.coherent10.jcqa.primary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.point | 0.30831099195710454 |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.ci95 | [0.28150134048257375, 0.3342269883824844] |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jcqa.per_token_secondary.count | 1119 |
| diagnostics.coherent10.jcqa.per_token_secondary.hard_accuracy | 0.30831099195710454 |
| diagnostics.coherent10.jcqa.per_token_secondary.macro_f1 | 0.3069111560647302 |
| diagnostics.coherent10.jcqa.per_token_secondary.mcc | 0.13568851917655486 |
| diagnostics.coherent10.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.units | 1119 |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.examples | 1119 |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.seed | 42 |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.repetitions | 2000 |
| diagnostics.coherent10.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jcqa.unigram_control.count | 1119 |
| diagnostics.coherent10.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| diagnostics.coherent10.jcqa.unigram_control.macro_f1 | 0.17226221885700888 |
| diagnostics.coherent10.jcqa.unigram_control.mcc | -0.034285051798449845 |
| diagnostics.coherent10.jcqa.unigram_control.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| diagnostics.coherent10.jcqa.chance | 0.2 |
| diagnostics.coherent10.jcqa.above_chance_evidence | true |
| diagnostics.coherent10.jcqa.train_majority_accuracy | 0.21179624664879357 |
| diagnostics.coherent10.jcqa.categories.commonsense.point | 0.34226988382484363 |
| diagnostics.coherent10.jcqa.categories.commonsense.ci95 | [0.314544235924933, 0.36910187667560307] |
| diagnostics.coherent10.jcqa.categories.commonsense.units | 1119 |
| diagnostics.coherent10.jcqa.categories.commonsense.examples | 1119 |
| diagnostics.coherent10.jcqa.categories.commonsense.unit | "family/prompt" |
| diagnostics.coherent10.jcqa.categories.commonsense.seed | 42 |
| diagnostics.coherent10.jcqa.categories.commonsense.repetitions | 2000 |
| diagnostics.coherent10.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.coherent10.jcqa.tie_examples | 0 |
| diagnostics.coherent10.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| diagnostics.coherent10.semantic_both_contexts.correct | 20 |
| diagnostics.coherent10.semantic_both_contexts.total | 96 |
| diagnostics.coherent10.semantic_both_contexts.fraction | 0.20833333333333334 |
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
| resume_gate.seconds | 10.832850487999167 |
| resume_gate.GPU_optimizer_updates | 8 |
| resume_gate.input_tokens | 262144 |
| resume_gate.schedule_scope | "Real CUDA mixed routes, stable-to-decay boundary, optimizer/RNG/samplers" |
| resume_gate.checkpoints | ["/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/resume-gate/continuous.pt", "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story10-low-lr-10b-100m-20261005/resume-gate/resumed.pt"] |
| scientific_tokens | 200015872 |
| verification_tokens | 262144 |
| protected_test_used | false |
| GPU_seconds | 511.1522132379996 |

</details>

<details>
<summary>reports/phase6/story10_low_lr_review.json — passed</summary>

[原記録](../../reports/phase6/story10_low_lr_review.json) ／ SHA256: `1a6aefb525ea8f0ec37e0c112a08cb44e78cfbd40cecf971f21eab8690aaed7d` ／ 290,894 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-04T16:33:56.243316Z" |
| selection.original_mixture.EOS_at_least8_more | true |
| selection.original_mixture.repetition_no_worse | true |
| selection.original_mixture.no_empty_role_unicode | true |
| selection.original_mixture.BPB_degradation_at_most1percent | true |
| selection.coherence_gain_at_least8 | false |
| selection.paired_coherence_CI_lower_above0 | true |
| selection.coherence_difference_count | 6 |
| selection.paired_CI95 | [0.025, 0.1375] |
| selection.eligible_for_full | false |
| summary.web.grammar_score2 | 17 |
| summary.web.relevance_score2 | 17 |
| summary.web.coherence_score2 | 0 |
| summary.web.appropriate_EOS | 0 |
| summary.coherent10.grammar_score2 | 40 |
| summary.coherent10.relevance_score2 | 10 |
| summary.coherent10.coherence_score2 | 6 |
| summary.coherent10.count | 80 |
| summary.coherent10.appropriate_EOS | 6 |
| paired_diagnostics.semantics.point | -0.015625 |
| paired_diagnostics.semantics.ci95 | [-0.046875, 0.015625] |
| paired_diagnostics.semantics.units | 96 |
| paired_diagnostics.semantics.examples | 192 |
| paired_diagnostics.semantics.unit | "family/prompt" |
| paired_diagnostics.semantics.seed | 42 |
| paired_diagnostics.semantics.repetitions | 2000 |
| paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jblimp.point | 0.01812688821752266 |
| paired_diagnostics.jblimp.ci95 | [-0.00906344410876133, 0.04229607250755287] |
| paired_diagnostics.jblimp.units | 331 |
| paired_diagnostics.jblimp.examples | 331 |
| paired_diagnostics.jblimp.unit | "family/prompt" |
| paired_diagnostics.jblimp.seed | 42 |
| paired_diagnostics.jblimp.repetitions | 2000 |
| paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jcqa.point | 0.03038427167113494 |
| paired_diagnostics.jcqa.ci95 | [0.008936550491510277, 0.050044682752457555] |
| paired_diagnostics.jcqa.units | 1119 |
| paired_diagnostics.jcqa.examples | 1119 |
| paired_diagnostics.jcqa.unit | "family/prompt" |
| paired_diagnostics.jcqa.seed | 42 |
| paired_diagnostics.jcqa.repetitions | 2000 |
| paired_diagnostics.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| scientific_tokens | 200015872 |
| verification_tokens | 262144 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/story20_budget_annotations.json — complete_320_of_320</summary>

[原記録](../../reports/phase6/story20_budget_annotations.json) ／ SHA256: `6efbb487824aee0238fdd910130c7a9428e25e3f7eba2e0802cae252c7f9e588` ／ 71,661 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_320_of_320" |
| generation_sha256.coherent20.intermediate100M | "d40a1ee97fb7321813d879f2fdc731c78b9c5b534a48a7baaa5b12a7791778fc" |
| generation_sha256.coherent20.result | "e2532f17497c9243ca4eade7227c74fcc563cdb327e3ca7aaa80854c7ae9c0a4" |

</details>

<details>
<summary>reports/phase6/story20_budget_annotations_coherent20_intermediate100M.json — complete_80_of_80</summary>

[原記録](../../reports/phase6/story20_budget_annotations_coherent20_intermediate100M.json) ／ SHA256: `21785a45c791030f13eb83be99d1cba69170e0a03d269d5e0a82d0acd4c0107b` ／ 15,737 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_80_of_80" |
| checkpoint_role | "intermediate100M" |

</details>

<details>
<summary>reports/phase6/story20_budget_annotations_coherent20_result.json — complete_80_of_80</summary>

[原記録](../../reports/phase6/story20_budget_annotations_coherent20_result.json) ／ SHA256: `97a3eda41299a2bc01752c580dce2c94bf34f1d3e1a51fd7f832bd704dbab987` ／ 16,527 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_80_of_80" |
| checkpoint_role | "result" |

</details>

<details>
<summary>reports/phase6/story20_budget_annotations_web_intermediate100M.json — complete_80_of_80</summary>

[原記録](../../reports/phase6/story20_budget_annotations_web_intermediate100M.json) ／ SHA256: `11a423a75ccd8e39de8389c66ec72417893e3ff3356e87d4620c2ba5833f2795` ／ 15,426 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_80_of_80" |
| checkpoint_role | "intermediate100M" |

</details>

<details>
<summary>reports/phase6/story20_budget_annotations_web_result.json — complete_80_of_80</summary>

[原記録](../../reports/phase6/story20_budget_annotations_web_result.json) ／ SHA256: `910daece59e722a004db9ce43460350edd4c032b42d4b92e4d9614f5a648929d` ／ 15,559 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_80_of_80" |
| checkpoint_role | "result" |

</details>

<details>
<summary>reports/phase6/story20_budget_data_launch.json — None</summary>

[原記録](../../reports/phase6/story20_budget_data_launch.json) ／ SHA256: `65c6247b89b2c62b6a08b54d324da3cb24720515c38f282a6eacee7cd3d229d4` ／ 446 bytes

| 原キー | 保存値 |
|---|---|
| scope | "conditional public train-only story preparation; UI retained" |

</details>

<details>
<summary>reports/phase6/story20_budget_full_launch.json — launched</summary>

[原記録](../../reports/phase6/story20_budget_full_launch.json) ／ SHA256: `158d06a9b5eb9d1d760b1fb69fec25f6fc0ae4e458f4f5ace773f90f10d4e7c0` ／ 963 bytes

| 原キー | 保存値 |
|---|---|
| status | "launched" |
| additional_training_tokens | 0 |
| gpu_budget_seconds | 3000 |

</details>

<details>
<summary>reports/phase6/story20_budget_full_progress.json — partial_web_full_complete_candidate_in_progress</summary>

[原記録](../../reports/phase6/story20_budget_full_progress.json) ／ SHA256: `7d9eba53ce616d8da3e2e300f0d28f889bb17bcb8b17bb36fd2bf565b713ef81` ／ 1,676 bytes

| 原キー | 保存値 |
|---|---|
| status | "partial_web_full_complete_candidate_in_progress" |
| additional_training_tokens | 0 |
| web.full_BPB | 0.9404477181826103 |
| web.documents | 89416 |
| web.body_bytes | 164344743 |
| web.body_tokens | 42003934 |
| web.fixed80.eos | 0 |
| web.fixed80.repetition | 62 |
| web.fixed80.unicode_failure | 0 |
| web.fixed80.role_leak | 0 |
| web.fixed80.empty | 0 |
| web.all400.EOS | 10 |
| web.all400.repetition | 128 |
| web.all400.unicode_failure | 0 |
| web.all400.role_leak | 0 |
| web.all400.empty | 0 |
| web.long.128.natural_eos | 0 |
| web.long.128.raw_utf8_failure | 0 |
| web.long.512.natural_eos | 0 |
| web.long.512.raw_utf8_failure | 0 |
| candidate500M_passes_acceptance | null |

</details>

<details>
<summary>reports/phase6/story20_budget_full_result.json — complete</summary>

[原記録](../../reports/phase6/story20_budget_full_result.json) ／ SHA256: `ab3fb2bdf011cdeabf50ef9f68a3948ba4a874411c80b05c8ae356110ec053cf` ／ 7,214 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.scripts/evaluate_story20_budget_full.py | "4c24be96499730c5f89091fbfab14fa394dbf3d49cfc050b4a4fdf6f14ee77bc" |
| binding.source_sha256.scripts/evaluate_story20_budget_full.ps1 | "91084d52fed005faf5fb54d4ea91f817ea7f3fe6e8152cf92b9d186709810316" |
| summary.web.training_input_tokens | 10500014080 |
| summary.web.full_dev_BPB | 0.9404477181826103 |
| summary.web.fixed80.eos | 0 |
| summary.web.fixed80.repetition | 62 |
| summary.web.fixed80.unicode_failure | 0 |
| summary.web.fixed80.role_leak | 0 |
| summary.web.fixed80.empty | 0 |
| summary.web.all400.eos | 10 |
| summary.web.all400.repetition | 128 |
| summary.web.all400.unicode_failure | 0 |
| summary.web.all400.role_leak | 0 |
| summary.web.all400.empty | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.repetition | 62 |
| summary.web.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.repetition | 62 |
| summary.web.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed42.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed42.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed43.eos | 4 |
| summary.web.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed44.eos | 4 |
| summary.web.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| summary.coherent20.label | "coherent20" |
| summary.coherent20.training_input_tokens | 10500014080 |
| summary.coherent20.full_dev_BPB | 0.9487982354210883 |
| summary.coherent20.fixed80.outputs | 80 |
| summary.coherent20.fixed80.eos | 37 |
| summary.coherent20.fixed80.repetition | 18 |
| summary.coherent20.fixed80.unicode_failure | 0 |
| summary.coherent20.fixed80.role_leak | 0 |
| summary.coherent20.fixed80.empty | 0 |
| summary.coherent20.all400.outputs | 400 |
| summary.coherent20.all400.eos | 179 |
| summary.coherent20.all400.repetition | 36 |
| summary.coherent20.all400.unicode_failure | 0 |
| summary.coherent20.all400.role_leak | 0 |
| summary.coherent20.all400.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.eos | 37 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.repetition | 18 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.eos | 37 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.repetition | 18 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.eos | 39 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.eos | 37 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.eos | 29 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| parent.training_input_tokens | 10000007168 |
| parent.full_dev_BPB | 0.9540184727984398 |
| parent.fixed80.eos | 0 |
| parent.fixed80.repetition | 53 |
| parent.fixed80.unicode_failure | 0 |
| parent.fixed80.role_leak | 0 |
| parent.fixed80.empty | 0 |
| parent.all400.eos | 9 |
| parent.all400.repetition | 112 |
| parent.all400.unicode_failure | 0 |
| parent.all400.role_leak | 0 |
| parent.all400.empty | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed42.eos | 4 |
| parent.generation_groups.sampling-suppressed1-seed42.repetition | 3 |
| parent.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed44.eos | 3 |
| parent.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| parent.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| long_generation.web.conditions.128.natural_eos | 0 |
| long_generation.web.conditions.128.raw_utf8_failure | 0 |
| long_generation.web.conditions.512.natural_eos | 0 |
| long_generation.web.conditions.512.raw_utf8_failure | 0 |
| long_generation.coherent20.complete | true |
| long_generation.coherent20.conditions.128.count | 20 |
| long_generation.coherent20.conditions.128.expected | 20 |
| long_generation.coherent20.conditions.128.natural_eos | 12 |
| long_generation.coherent20.conditions.128.mean_char4_repeat | 0.3513307720872196 |
| long_generation.coherent20.conditions.128.same_sentence_repeat | 6 |
| long_generation.coherent20.conditions.128.raw_utf8_failure | 0 |
| long_generation.coherent20.conditions.512.count | 20 |
| long_generation.coherent20.conditions.512.expected | 20 |
| long_generation.coherent20.conditions.512.natural_eos | 12 |
| long_generation.coherent20.conditions.512.mean_char4_repeat | 0.42203450003921655 |
| long_generation.coherent20.conditions.512.same_sentence_repeat | 6 |
| long_generation.coherent20.conditions.512.raw_utf8_failure | 0 |
| checks.mixture.EOS_at_least8_more | true |
| checks.mixture.repetition_no_worse | true |
| checks.mixture.no_empty_role_unicode | true |
| checks.mixture.BPB_degradation_at_most1percent | true |
| checks.mixture.no_punctuation_only_stops | true |
| checks.parent_growth.full_BPB_no_major_regression | true |
| checks.parent_growth.fixed_repetition_not8_worse | true |
| checks.parent_growth.raw_unicode_empty_role_zero_all400 | true |
| candidate_passes_all_full_conditions | true |
| additional_training_tokens | 0 |
| protected_test_used | false |
| GPU_seconds | 1925.8684119710015 |

</details>

<details>
<summary>reports/phase6/story20_budget_full_review.json — passed</summary>

[原記録](../../reports/phase6/story20_budget_full_review.json) ／ SHA256: `04c8280a3ac871f58711ebcf9bc723b97e5fc9163ad0e9c4175d16fe7e965172` ／ 8,806 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-05T02:14:40.904493Z" |
| checks.actual_full_job_complete_exited | true |
| checks.full_config_screen_review_binding | true |
| checks.screen_was_eligible | true |
| checks.full_budget_zero_learning_and_honest_scope | true |
| checks.web_actual_checkpoint_and_full_binding | true |
| checks.web_full_common89416_complete_coverage | true |
| checks.web_actual_BPB_from_finite_NLL | true |
| checks.web_same_parent_body_scoring_protocol | true |
| checks.web_parent_aligned_documents_and400_requests | true |
| checks.web_actual_raw400_ID_flags | true |
| checks.web_fixed80_match_primary_IDs | true |
| checks.web_long_binding_requests_and_complete | true |
| checks.web_long_raw_text_stops_UTF8_and_metrics | true |
| checks.web_long128_summary_from_rows | true |
| checks.web_long512_summary_from_rows | true |
| checks.web_long_saved_summary_binding | true |
| checks.coherent20_actual_checkpoint_and_full_binding | true |
| checks.coherent20_full_common89416_complete_coverage | true |
| checks.coherent20_actual_BPB_from_finite_NLL | true |
| checks.coherent20_same_parent_body_scoring_protocol | true |
| checks.coherent20_parent_aligned_documents_and400_requests | true |
| checks.coherent20_actual_raw400_ID_flags | true |
| checks.coherent20_fixed80_match_primary_IDs | true |
| checks.coherent20_long_binding_requests_and_complete | true |
| checks.coherent20_long_raw_text_stops_UTF8_and_metrics | true |
| checks.coherent20_long128_summary_from_rows | true |
| checks.coherent20_long512_summary_from_rows | true |
| checks.coherent20_long_saved_summary_binding | true |
| checks.same_full_document_and_generation_requests_between_arms | true |
| checks.actual_summaries_original_gates_recomputed | true |
| summary.web.training_input_tokens | 10500014080 |
| summary.web.full_dev_BPB | 0.9404477181826103 |
| summary.web.fixed80.eos | 0 |
| summary.web.fixed80.repetition | 62 |
| summary.web.fixed80.unicode_failure | 0 |
| summary.web.fixed80.role_leak | 0 |
| summary.web.fixed80.empty | 0 |
| summary.web.all400.eos | 10 |
| summary.web.all400.repetition | 128 |
| summary.web.all400.unicode_failure | 0 |
| summary.web.all400.role_leak | 0 |
| summary.web.all400.empty | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.repetition | 62 |
| summary.web.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.repetition | 62 |
| summary.web.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed42.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed42.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed43.eos | 4 |
| summary.web.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed44.eos | 4 |
| summary.web.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| summary.coherent20.label | "coherent20" |
| summary.coherent20.training_input_tokens | 10500014080 |
| summary.coherent20.full_dev_BPB | 0.9487982354210883 |
| summary.coherent20.fixed80.outputs | 80 |
| summary.coherent20.fixed80.eos | 37 |
| summary.coherent20.fixed80.repetition | 18 |
| summary.coherent20.fixed80.unicode_failure | 0 |
| summary.coherent20.fixed80.role_leak | 0 |
| summary.coherent20.fixed80.empty | 0 |
| summary.coherent20.all400.outputs | 400 |
| summary.coherent20.all400.eos | 179 |
| summary.coherent20.all400.repetition | 36 |
| summary.coherent20.all400.unicode_failure | 0 |
| summary.coherent20.all400.role_leak | 0 |
| summary.coherent20.all400.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.eos | 37 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.repetition | 18 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.eos | 37 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.repetition | 18 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.eos | 39 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.eos | 37 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.eos | 29 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| parent.training_input_tokens | 10000007168 |
| parent.full_dev_BPB | 0.9540184727984398 |
| parent.fixed80.eos | 0 |
| parent.fixed80.repetition | 53 |
| parent.fixed80.unicode_failure | 0 |
| parent.fixed80.role_leak | 0 |
| parent.fixed80.empty | 0 |
| parent.all400.eos | 9 |
| parent.all400.repetition | 112 |
| parent.all400.unicode_failure | 0 |
| parent.all400.role_leak | 0 |
| parent.all400.empty | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed42.eos | 4 |
| parent.generation_groups.sampling-suppressed1-seed42.repetition | 3 |
| parent.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed44.eos | 3 |
| parent.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| parent.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| adoption_checks.mixture.EOS_at_least8_more | true |
| adoption_checks.mixture.repetition_no_worse | true |
| adoption_checks.mixture.no_empty_role_unicode | true |
| adoption_checks.mixture.BPB_degradation_at_most1percent | true |
| adoption_checks.mixture.no_punctuation_only_stops | true |
| adoption_checks.parent_growth.full_BPB_no_major_regression | true |
| adoption_checks.parent_growth.fixed_repetition_not8_worse | true |
| adoption_checks.parent_growth.raw_unicode_empty_role_zero_all400 | true |
| candidate_passes_all_full_conditions | true |
| long_generation.web.conditions.128.natural_eos | 0 |
| long_generation.web.conditions.128.raw_utf8_failure | 0 |
| long_generation.web.conditions.512.natural_eos | 0 |
| long_generation.web.conditions.512.raw_utf8_failure | 0 |
| long_generation.coherent20.complete | true |
| long_generation.coherent20.conditions.128.count | 20 |
| long_generation.coherent20.conditions.128.expected | 20 |
| long_generation.coherent20.conditions.128.natural_eos | 12 |
| long_generation.coherent20.conditions.128.mean_char4_repeat | 0.3513307720872196 |
| long_generation.coherent20.conditions.128.same_sentence_repeat | 6 |
| long_generation.coherent20.conditions.128.raw_utf8_failure | 0 |
| long_generation.coherent20.conditions.512.count | 20 |
| long_generation.coherent20.conditions.512.expected | 20 |
| long_generation.coherent20.conditions.512.natural_eos | 12 |
| long_generation.coherent20.conditions.512.mean_char4_repeat | 0.42203450003921655 |
| long_generation.coherent20.conditions.512.same_sentence_repeat | 6 |
| long_generation.coherent20.conditions.512.raw_utf8_failure | 0 |
| additional_training_tokens | 0 |
| protected_test_used | false |
| GPU_seconds | 1925.8684119710015 |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/coherent20-full.json | "65b1e23a790b6c59c0838fcadcb9aae8e99565c7fd10327dd1ea7ae535e0e471" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/coherent20/long-generation.json | "5a59775b69ccd4068a098f447591097abc73760bfa9a73bc747bc31cda5b2882" |

</details>

<details>
<summary>reports/phase6/story20_budget_launch.json — None</summary>

[原記録](../../reports/phase6/story20_budget_launch.json) ／ SHA256: `6a0dbbe970ef28f941a8ccac0a41bf12f63f61f08d037e5c1903bf4dcf3278d5` ／ 534 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/story20_budget_pool_content_review.json — None</summary>

[原記録](../../reports/phase6/story20_budget_pool_content_review.json) ／ SHA256: `0f09145e94e02043f400bba1e0825fd137d7cebeaa063e7744c10b411fa7878d` ／ 6,826 bytes

| 原キー | 保存値 |
|---|---|
| accepted_for_experiment | true |
| samples_sha256 | "be643b3d6aa671fef448b88b99061bee2d3f116a16b5f0452981513aabbed516" |
| reviewed_samples | 40 |
| sample_policy | "First ten accepted stories per pinned train file, four files; not random and not corpus prevalence" |
| totals.tokens | 59963449 |
| totals.documents | 662857 |
| totals.body_bytes | 236846913 |
| target_tokens | 120000000 |
| planned_story_input_tokens | 99975168 |
| repetition_policy | "Explicit deterministic BlockSampler epoch reuse if source exhausted; not new unique data" |
| known_limits | ["Independent human blind review not performed", "Overlap with general Web and benchmarks beyond exact checks unknown", "Public synthetic stories are not factual reference data", "Heuristic resolved-end filtering does not prove semantic resolution"] |

</details>

<details>
<summary>reports/phase6/story20_budget_pool_ready.json — ready_pending_content_inspection</summary>

[原記録](../../reports/phase6/story20_budget_pool_ready.json) ／ SHA256: `572cd8e003acfa5bb6e6ce7c395189af4143bbc19a678bbf2249b9807ea199dd` ／ 2,590 bytes

| 原キー | 保存値 |
|---|---|
| status | "ready_pending_content_inspection" |
| binding.source.official_validation_or_test_downloaded | false |
| binding.target_tokens | 120000000 |
| totals.tokens | 59963449 |
| totals.documents | 662857 |
| totals.body_bytes | 236846913 |
| parent_documents | 125613 |
| body_tokens_mean | 88.46211928062915 |
| target_tokens | 120000000 |
| planned500M_story_tokens | 99975168 |
| repetition_policy | "Explicit deterministic BlockSampler epoch reuse if source exhausted; not new unique data" |
| seconds | 194.53356156800146 |

</details>

<details>
<summary>reports/phase6/story20_budget_result.json — complete_primary_and_conditional_full_reviewed</summary>

[原記録](../../reports/phase6/story20_budget_result.json) ／ SHA256: `a5b1f5e2878a4a635f210091e7e17b49609ccb3d8e2707a761dcd19fde501ffb` ／ 8,221 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_primary_and_conditional_full_reviewed" |
| scientific_tokens | 1000013824 |
| verification_tokens | 262144 |
| GPU_seconds | 1878.7058998310022 |
| arms.web.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| arms.web.checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| arms.web.update | 320435 |
| arms.web.tokens | 10500014080 |
| arms.web.additional_input_tokens | 500006912 |
| arms.web.source_tokens.web | 500006912 |
| arms.web.source_tokens.short | 0 |
| arms.web.training_seconds | 747.3961857169998 |
| arms.coherent20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/coherent20/checkpoint-00320435.pt" |
| arms.coherent20.checkpoint_sha256 | "f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac" |
| arms.coherent20.update | 320435 |
| arms.coherent20.tokens | 10500014080 |
| arms.coherent20.additional_input_tokens | 500006912 |
| arms.coherent20.source_tokens.web | 400031744 |
| arms.coherent20.source_tokens.short | 99975168 |
| arms.coherent20.training_seconds | 735.2801723750017 |
| BPB.web.intermediate100M | 0.9786423269745784 |
| BPB.web.result | 0.9715702494156145 |
| BPB.coherent20.intermediate100M | 0.985129409148557 |
| BPB.coherent20.result | 0.9799114534563707 |
| rates.web.intermediate100M.eos | 0 |
| rates.web.intermediate100M.repetition | 55 |
| rates.web.intermediate100M.unicode_failure | 0 |
| rates.web.intermediate100M.role_leak | 0 |
| rates.web.intermediate100M.empty | 0 |
| rates.web.result.eos | 0 |
| rates.web.result.repetition | 62 |
| rates.web.result.unicode_failure | 0 |
| rates.web.result.role_leak | 0 |
| rates.web.result.empty | 0 |
| rates.coherent20.intermediate100M.outputs | 80 |
| rates.coherent20.intermediate100M.eos | 22 |
| rates.coherent20.intermediate100M.repetition | 29 |
| rates.coherent20.intermediate100M.unicode_failure | 0 |
| rates.coherent20.intermediate100M.role_leak | 0 |
| rates.coherent20.intermediate100M.empty | 0 |
| rates.coherent20.result.outputs | 80 |
| rates.coherent20.result.eos | 37 |
| rates.coherent20.result.repetition | 18 |
| rates.coherent20.result.unicode_failure | 0 |
| rates.coherent20.result.role_leak | 0 |
| rates.coherent20.result.empty | 0 |
| diagnostics.web.intermediate100M.semantic_both_contexts.correct | 23 |
| diagnostics.web.result.semantic_both_contexts.correct | 21 |
| diagnostics.coherent20.intermediate100M.semantics | 0.6302083333333334 |
| diagnostics.coherent20.intermediate100M.jblimp_SLOR | 0.7552870090634441 |
| diagnostics.coherent20.intermediate100M.jcqa | 0.3386952636282395 |
| diagnostics.coherent20.intermediate100M.semantic_both_contexts.correct | 27 |
| diagnostics.coherent20.intermediate100M.semantic_both_contexts.total | 96 |
| diagnostics.coherent20.intermediate100M.semantic_both_contexts.fraction | 0.28125 |
| diagnostics.coherent20.intermediate100M.complete_tasks.semantics | true |
| diagnostics.coherent20.intermediate100M.complete_tasks.jcqa | true |
| diagnostics.coherent20.intermediate100M.complete_tasks.jblimp | true |
| diagnostics.coherent20.result.semantics | 0.6197916666666666 |
| diagnostics.coherent20.result.jblimp_SLOR | 0.7854984894259819 |
| diagnostics.coherent20.result.jcqa | 0.3351206434316354 |
| diagnostics.coherent20.result.semantic_both_contexts.correct | 25 |
| diagnostics.coherent20.result.semantic_both_contexts.total | 96 |
| diagnostics.coherent20.result.semantic_both_contexts.fraction | 0.2604166666666667 |
| diagnostics.coherent20.result.complete_tasks.semantics | true |
| diagnostics.coherent20.result.complete_tasks.jcqa | true |
| diagnostics.coherent20.result.complete_tasks.jblimp | true |
| protected_test_used | false |
| content_review_status | "complete_320_of_320" |
| original_UI.training_tokens | 10000007168 |
| original_UI.update | 305176 |
| original_UI.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| primary_review.eligible_for_full | true |
| primary_review.checks_passed | 37 |
| primary_review.summary.web.intermediate100M.grammar_score2 | 2 |
| primary_review.summary.web.intermediate100M.relevance_score2 | 9 |
| primary_review.summary.web.intermediate100M.coherence_score2 | 0 |
| primary_review.summary.web.intermediate100M.appropriate_EOS | 0 |
| primary_review.summary.web.result.grammar_score2 | 4 |
| primary_review.summary.web.result.relevance_score2 | 8 |
| primary_review.summary.web.result.coherence_score2 | 0 |
| primary_review.summary.web.result.appropriate_EOS | 0 |
| primary_review.summary.coherent20.intermediate100M.grammar_score2 | 27 |
| primary_review.summary.coherent20.intermediate100M.relevance_score2 | 15 |
| primary_review.summary.coherent20.intermediate100M.coherence_score2 | 9 |
| primary_review.summary.coherent20.intermediate100M.count | 80 |
| primary_review.summary.coherent20.intermediate100M.appropriate_EOS | 9 |
| primary_review.summary.coherent20.intermediate100M.epoch | 0 |
| primary_review.summary.coherent20.intermediate100M.position | 19520 |
| primary_review.summary.coherent20.result.grammar_score2 | 38 |
| primary_review.summary.coherent20.result.relevance_score2 | 26 |
| primary_review.summary.coherent20.result.coherence_score2 | 19 |
| primary_review.summary.coherent20.result.count | 80 |
| primary_review.summary.coherent20.result.appropriate_EOS | 19 |
| primary_review.summary.coherent20.result.epoch | 1 |
| primary_review.summary.coherent20.result.position | 39074 |
| primary_review.selection.intermediate100M.original_mixture.EOS_at_least8_more | true |
| primary_review.selection.intermediate100M.original_mixture.repetition_no_worse | true |
| primary_review.selection.intermediate100M.original_mixture.no_empty_role_unicode | true |
| primary_review.selection.intermediate100M.original_mixture.BPB_degradation_at_most1percent | true |
| primary_review.selection.intermediate100M.coherence_gain_at_least8 | true |
| primary_review.selection.intermediate100M.paired_coherence_CI_lower_above0 | true |
| primary_review.selection.intermediate100M.coherence_difference_count | 9 |
| primary_review.selection.intermediate100M.paired_CI95 | [0.05, 0.1875] |
| primary_review.selection.intermediate100M.eligible_for_full | true |
| primary_review.selection.result.original_mixture.EOS_at_least8_more | true |
| primary_review.selection.result.original_mixture.repetition_no_worse | true |
| primary_review.selection.result.original_mixture.no_empty_role_unicode | true |
| primary_review.selection.result.original_mixture.BPB_degradation_at_most1percent | true |
| primary_review.selection.result.coherence_gain_at_least8 | true |
| primary_review.selection.result.paired_coherence_CI_lower_above0 | true |
| primary_review.selection.result.coherence_difference_count | 19 |
| primary_review.selection.result.paired_CI95 | [0.15, 0.3375] |
| primary_review.selection.result.eligible_for_full | true |
| source_result_status | "complete_pending_content_review" |
| full_review.checks_passed | 30 |
| full_review.candidate_passes_all_full_conditions | true |
| full_review.GPU_seconds | 1925.8684119710015 |
| final_original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| final_original_UI.training_tokens | 10000007168 |

</details>

<details>
<summary>reports/phase6/story20_budget_review.json — passed</summary>

[原記録](../../reports/phase6/story20_budget_review.json) ／ SHA256: `b78385bd235d7a9281a5b6b4283902078e5abd8db743076aa886ecf88fed0465` ／ 643,386 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-05T01:41:26.724622Z" |
| checks.actual_mixed_CUDA_save_resume | true |
| checks.paired500M_scientific_tokens | true |
| checks.web_15259_contiguous_finite_updates | true |
| checks.web_intermediate100M_generation_hash_and_exact80_IDs | true |
| checks.web_intermediate100M_all80_individual_content_notes | true |
| checks.web_intermediate100M_actual_checkpoint_hash | true |
| checks.web_intermediate100M_finite_full_state_counters | true |
| checks.web_intermediate100M_common_schedule_and_source_counts | true |
| checks.web_intermediate100M_actual_epoch_reuse_disclosed | true |
| checks.web_intermediate100M_common256_actual_finite_BPB | true |
| checks.web_intermediate100M_complete_Japanese_tasks_RNG_isolated | true |
| checks.web_result_generation_hash_and_exact80_IDs | true |
| checks.web_result_all80_individual_content_notes | true |
| checks.web_result_actual_checkpoint_hash | true |
| checks.web_result_finite_full_state_counters | true |
| checks.web_result_common_schedule_and_source_counts | true |
| checks.web_result_actual_epoch_reuse_disclosed | true |
| checks.web_result_common256_actual_finite_BPB | true |
| checks.web_result_complete_Japanese_tasks_RNG_isolated | true |
| checks.coherent20_15259_contiguous_finite_updates | true |
| checks.coherent20_intermediate100M_generation_hash_and_exact80_IDs | true |
| checks.coherent20_intermediate100M_all80_individual_content_notes | true |
| checks.coherent20_intermediate100M_actual_checkpoint_hash | true |
| checks.coherent20_intermediate100M_finite_full_state_counters | true |
| checks.coherent20_intermediate100M_common_schedule_and_source_counts | true |
| checks.coherent20_intermediate100M_actual_epoch_reuse_disclosed | true |
| checks.coherent20_intermediate100M_common256_actual_finite_BPB | true |
| checks.coherent20_intermediate100M_complete_Japanese_tasks_RNG_isolated | true |
| checks.coherent20_result_generation_hash_and_exact80_IDs | true |
| checks.coherent20_result_all80_individual_content_notes | true |
| checks.coherent20_result_actual_checkpoint_hash | true |
| checks.coherent20_result_finite_full_state_counters | true |
| checks.coherent20_result_common_schedule_and_source_counts | true |
| checks.coherent20_result_actual_epoch_reuse_disclosed | true |
| checks.coherent20_result_common256_actual_finite_BPB | true |
| checks.coherent20_result_complete_Japanese_tasks_RNG_isolated | true |
| checks.no_protected_test | true |
| summary.web.intermediate100M.grammar_score2 | 2 |
| summary.web.intermediate100M.relevance_score2 | 9 |
| summary.web.intermediate100M.coherence_score2 | 0 |
| summary.web.intermediate100M.appropriate_EOS | 0 |
| summary.web.result.grammar_score2 | 4 |
| summary.web.result.relevance_score2 | 8 |
| summary.web.result.coherence_score2 | 0 |
| summary.web.result.appropriate_EOS | 0 |
| summary.coherent20.intermediate100M.grammar_score2 | 27 |
| summary.coherent20.intermediate100M.relevance_score2 | 15 |
| summary.coherent20.intermediate100M.coherence_score2 | 9 |
| summary.coherent20.intermediate100M.count | 80 |
| summary.coherent20.intermediate100M.appropriate_EOS | 9 |
| summary.coherent20.intermediate100M.epoch | 0 |
| summary.coherent20.intermediate100M.position | 19520 |
| summary.coherent20.result.grammar_score2 | 38 |
| summary.coherent20.result.relevance_score2 | 26 |
| summary.coherent20.result.coherence_score2 | 19 |
| summary.coherent20.result.count | 80 |
| summary.coherent20.result.appropriate_EOS | 19 |
| summary.coherent20.result.epoch | 1 |
| summary.coherent20.result.position | 39074 |
| selection.intermediate100M.original_mixture.EOS_at_least8_more | true |
| selection.intermediate100M.original_mixture.repetition_no_worse | true |
| selection.intermediate100M.original_mixture.no_empty_role_unicode | true |
| selection.intermediate100M.original_mixture.BPB_degradation_at_most1percent | true |
| selection.intermediate100M.coherence_gain_at_least8 | true |
| selection.intermediate100M.paired_coherence_CI_lower_above0 | true |
| selection.intermediate100M.coherence_difference_count | 9 |
| selection.intermediate100M.paired_CI95 | [0.05, 0.1875] |
| selection.intermediate100M.eligible_for_full | true |
| selection.result.original_mixture.EOS_at_least8_more | true |
| selection.result.original_mixture.repetition_no_worse | true |
| selection.result.original_mixture.no_empty_role_unicode | true |
| selection.result.original_mixture.BPB_degradation_at_most1percent | true |
| selection.result.coherence_gain_at_least8 | true |
| selection.result.paired_coherence_CI_lower_above0 | true |
| selection.result.coherence_difference_count | 19 |
| selection.result.paired_CI95 | [0.15, 0.3375] |
| selection.result.eligible_for_full | true |
| eligible_for_full | true |
| paired_diagnostics.intermediate100M.semantics.point | 0.020833333333333332 |
| paired_diagnostics.intermediate100M.semantics.ci95 | [-0.015625, 0.057291666666666664] |
| paired_diagnostics.intermediate100M.semantics.units | 96 |
| paired_diagnostics.intermediate100M.semantics.examples | 192 |
| paired_diagnostics.intermediate100M.semantics.unit | "family/prompt" |
| paired_diagnostics.intermediate100M.semantics.seed | 42 |
| paired_diagnostics.intermediate100M.semantics.repetitions | 2000 |
| paired_diagnostics.intermediate100M.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.intermediate100M.jblimp.point | 0.00906344410876133 |
| paired_diagnostics.intermediate100M.jblimp.ci95 | [-0.021148036253776436, 0.03927492447129909] |
| paired_diagnostics.intermediate100M.jblimp.units | 331 |
| paired_diagnostics.intermediate100M.jblimp.examples | 331 |
| paired_diagnostics.intermediate100M.jblimp.unit | "family/prompt" |
| paired_diagnostics.intermediate100M.jblimp.seed | 42 |
| paired_diagnostics.intermediate100M.jblimp.repetitions | 2000 |
| paired_diagnostics.intermediate100M.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.intermediate100M.jcqa.point | 0.025022341376228777 |
| paired_diagnostics.intermediate100M.jcqa.ci95 | [0.002680965147453083, 0.045576407506702415] |
| paired_diagnostics.intermediate100M.jcqa.units | 1119 |
| paired_diagnostics.intermediate100M.jcqa.examples | 1119 |
| paired_diagnostics.intermediate100M.jcqa.unit | "family/prompt" |
| paired_diagnostics.intermediate100M.jcqa.seed | 42 |
| paired_diagnostics.intermediate100M.jcqa.repetitions | 2000 |
| paired_diagnostics.intermediate100M.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.result.semantics.point | 0.015625 |
| paired_diagnostics.result.semantics.ci95 | [-0.020833333333333332, 0.052083333333333336] |
| paired_diagnostics.result.semantics.units | 96 |
| paired_diagnostics.result.semantics.examples | 192 |
| paired_diagnostics.result.semantics.unit | "family/prompt" |
| paired_diagnostics.result.semantics.seed | 42 |
| paired_diagnostics.result.semantics.repetitions | 2000 |
| paired_diagnostics.result.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.result.jblimp.point | 0.030211480362537766 |
| paired_diagnostics.result.jblimp.ci95 | [-0.0030211480362537764, 0.0634441087613293] |
| paired_diagnostics.result.jblimp.units | 331 |
| paired_diagnostics.result.jblimp.examples | 331 |
| paired_diagnostics.result.jblimp.unit | "family/prompt" |
| paired_diagnostics.result.jblimp.seed | 42 |
| paired_diagnostics.result.jblimp.repetitions | 2000 |
| paired_diagnostics.result.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.result.jcqa.point | 0.01966041108132261 |
| paired_diagnostics.result.jcqa.ci95 | [-2.234137622877442e-05, 0.040214477211796246] |
| paired_diagnostics.result.jcqa.units | 1119 |
| paired_diagnostics.result.jcqa.examples | 1119 |
| paired_diagnostics.result.jcqa.unit | "family/prompt" |
| paired_diagnostics.result.jcqa.seed | 42 |
| paired_diagnostics.result.jcqa.repetitions | 2000 |
| paired_diagnostics.result.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.web.semantics.seed | 42 |
| within_arm_100M_to500M.web.semantics.repetitions | 2000 |
| within_arm_100M_to500M.web.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.web.jblimp.seed | 42 |
| within_arm_100M_to500M.web.jblimp.repetitions | 2000 |
| within_arm_100M_to500M.web.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.web.jcqa.seed | 42 |
| within_arm_100M_to500M.web.jcqa.repetitions | 2000 |
| within_arm_100M_to500M.web.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.web.coherence.point | 0.0 |
| within_arm_100M_to500M.web.coherence.ci95 | [0.0, 0.0] |
| within_arm_100M_to500M.web.coherence.units | 80 |
| within_arm_100M_to500M.web.coherence.examples | 80 |
| within_arm_100M_to500M.web.coherence.unit | "family/prompt" |
| within_arm_100M_to500M.web.coherence.seed | 42 |
| within_arm_100M_to500M.web.coherence.repetitions | 2000 |
| within_arm_100M_to500M.web.coherence.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.coherent20.semantics.point | -0.010416666666666666 |
| within_arm_100M_to500M.coherent20.semantics.ci95 | [-0.036458333333333336, 0.010416666666666666] |
| within_arm_100M_to500M.coherent20.semantics.units | 96 |
| within_arm_100M_to500M.coherent20.semantics.examples | 192 |
| within_arm_100M_to500M.coherent20.semantics.unit | "family/prompt" |
| within_arm_100M_to500M.coherent20.semantics.seed | 42 |
| within_arm_100M_to500M.coherent20.semantics.repetitions | 2000 |
| within_arm_100M_to500M.coherent20.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.coherent20.jblimp.point | 0.030211480362537766 |
| within_arm_100M_to500M.coherent20.jblimp.ci95 | [0.0030211480362537764, 0.06042296072507553] |
| within_arm_100M_to500M.coherent20.jblimp.units | 331 |
| within_arm_100M_to500M.coherent20.jblimp.examples | 331 |
| within_arm_100M_to500M.coherent20.jblimp.unit | "family/prompt" |
| within_arm_100M_to500M.coherent20.jblimp.seed | 42 |
| within_arm_100M_to500M.coherent20.jblimp.repetitions | 2000 |
| within_arm_100M_to500M.coherent20.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.coherent20.jcqa.point | -0.0035746201966041107 |
| within_arm_100M_to500M.coherent20.jcqa.ci95 | [-0.017873100983020553, 0.010723860589812333] |
| within_arm_100M_to500M.coherent20.jcqa.units | 1119 |
| within_arm_100M_to500M.coherent20.jcqa.examples | 1119 |
| within_arm_100M_to500M.coherent20.jcqa.unit | "family/prompt" |
| within_arm_100M_to500M.coherent20.jcqa.seed | 42 |
| within_arm_100M_to500M.coherent20.jcqa.repetitions | 2000 |
| within_arm_100M_to500M.coherent20.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| within_arm_100M_to500M.coherent20.coherence.point | 0.125 |
| within_arm_100M_to500M.coherent20.coherence.ci95 | [0.0375, 0.2125] |
| within_arm_100M_to500M.coherent20.coherence.units | 80 |
| within_arm_100M_to500M.coherent20.coherence.examples | 80 |
| within_arm_100M_to500M.coherent20.coherence.unit | "family/prompt" |
| within_arm_100M_to500M.coherent20.coherence.seed | 42 |
| within_arm_100M_to500M.coherent20.coherence.repetitions | 2000 |
| within_arm_100M_to500M.coherent20.coherence.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| scientific_tokens | 1000013824 |
| verification_tokens | 262144 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/story20_budget_story_training.json — complete</summary>

[原記録](../../reports/phase6/story20_budget_story_training.json) ／ SHA256: `b172a11446fcddad0305dbc8e8a92d8b8c3d80986f383b350f4d8e6f7e12099a` ／ 1,454 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/coherent20/checkpoint-00320435.pt" |
| checkpoint_sha256 | "f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac" |
| update | 320435 |
| tokens | 10500014080 |
| additional_input_tokens | 500006912 |
| source_tokens.web | 400031744 |
| source_tokens.short | 99975168 |
| source_eos_teachers.web | 846893 |
| source_eos_teachers.short | 1105092 |
| training_seconds | 735.2801723750017 |
| checkpoint_role | "result" |
| parent.update | 305176 |
| parent.tokens_seen | 10000007168 |
| scientific_config_sha256 | "bca826c47b66c3707588ff058381e1e95eef093c171f3c8cc72b9d2d771262d1" |

</details>

<details>
<summary>reports/phase6/story20_budget_web_training.json — complete</summary>

[原記録](../../reports/phase6/story20_budget_web_training.json) ／ SHA256: `5a7341fcda8a32dd191ead5fc9511b3e21a1b3ea77a18009fa892d1e6f97ef82` ／ 1,339 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint_sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| update | 320435 |
| tokens | 10500014080 |
| additional_input_tokens | 500006912 |
| source_tokens.web | 500006912 |
| source_tokens.short | 0 |
| source_eos_teachers.web | 1058482 |
| source_eos_teachers.short | 0 |
| training_seconds | 747.3961857169998 |
| checkpoint_role | "result" |
| parent.update | 305176 |
| parent.tokens_seen | 10000007168 |
| scientific_config_sha256 | "bca826c47b66c3707588ff058381e1e95eef093c171f3c8cc72b9d2d771262d1" |

</details>

<details>
<summary>reports/phase6/story20_content_categories.json — complete</summary>

[原記録](../../reports/phase6/story20_content_categories.json) ／ SHA256: `92aa55dfefef2beb893ee8163be174314b308e807e8ae472c002c144cd6698f6` ／ 18,044 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| interpretation | "Descriptive counts only, not a new selection gate or independent human judgment" |
| within_story100M_to500M.EOS_gained | 18 |
| within_story100M_to500M.EOS_lost | 3 |
| within_story100M_to500M.coherence_gained | 12 |
| within_story100M_to500M.coherence_lost | 2 |
| within_story100M_to500M.coherence_loss_ids | ["base-010", "base-037"] |
| within_story100M_to500M.appropriate_share_of_actual_stops100M | 0.4090909090909091 |
| within_story100M_to500M.appropriate_share_of_actual_stops500M | 0.5135135135135135 |
| within_story100M_to500M.interpretation | "Paired descriptive transitions; net coherence gain10, not every prefix improves" |

</details>

<details>
<summary>reports/phase6/story20_execution_completion.json — passed</summary>

[原記録](../../reports/phase6/story20_execution_completion.json) ／ SHA256: `d85e7686044627d23a4b0ad561232e3c48cbf0c01dd3d52334c76790db3cf67b` ／ 13,301 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| scope | "Plan52 actual stages1–4 including entered paired500M branch" |
| checked_at | "2026-10-05T02:20:25.655161Z" |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/screen-job.json_actual_complete_exited | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/screen-job.json_budget | true |
| checks.100M_actual_config_result_content_binding | true |
| checks.20_relevant_tests | true |
| checks.100M_actual25_CUDA_resume_checks | true |
| checks.100M_actual_saved_finite_state | true |
| checks.100M_counters_full_resume_state | true |
| checks.100M_contiguous_finite_schedule_and_counts | true |
| checks.100M_same_input_as_normalLR20 | true |
| checks.100M_common256_complete_BPB_protocol | true |
| checks.100M_complete_Japanese_tasks_and_saved_control | true |
| checks.100M_exact_dev80_prefixes | true |
| checks.100M_all80_content_bound | true |
| checks.100M_original_selection_recomputed | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/full/full-job.json_actual_complete_exited | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/full/full-job.json_budget | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/full_30_actual_checks_bound | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/web-full.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/web/long-generation.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/coherent20-full.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/coherent20/long-generation.json | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/full_original_gates_no_learning | true |
| checks.reports/phase6/story20-low-lr-10b-100m-20261005/full_entry_pass | true |
| checks.pool_actual_builder_complete_exited | true |
| checks.pool_actual_source_exhaustion_counts | true |
| checks.pool40_inspection_bound_and_reuse_disclosed | true |
| checks.new_pool_stream_index_tokenbyte_hashes | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/screen-job.json_actual_complete_exited | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/screen-job.json_budget | true |
| checks.26_relevant_budget_tests | true |
| checks.500M_primary_all_checks_bound | true |
| checks.paired500M_actual_scientific_and_resume_counts | true |
| checks.web_intermediate100M_80_raw_ratings_bound | true |
| checks.web_intermediate100M_complete_Japanese_diagnostics | true |
| checks.web_result_80_raw_ratings_bound | true |
| checks.web_result_complete_Japanese_diagnostics | true |
| checks.coherent20_intermediate100M_80_raw_ratings_bound | true |
| checks.coherent20_intermediate100M_complete_Japanese_diagnostics | true |
| checks.coherent20_result_80_raw_ratings_bound | true |
| checks.coherent20_result_complete_Japanese_diagnostics | true |
| checks.intermediate100M_original_selection_recomputed | true |
| checks.result_original_selection_recomputed | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/full/full-job.json_actual_complete_exited | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/full/full-job.json_budget | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/full_30_actual_checks_bound | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/web-full.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/web/long-generation.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/coherent20-full.json | true |
| checks.full_source_/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/full/coherent20/long-generation.json | true |
| checks.reports/phase6/story20-low-lr-10b-500m-20261005/full_original_gates_no_learning | true |
| checks.500M_full_separate_frozen_plan_and_sources | true |
| checks.500M_full_saved_source_scripts/evaluate_story20_budget_full.py | true |
| checks.500M_full_saved_source_scripts/evaluate_story20_budget_full.ps1 | true |
| checks.500M_full_saved_source_scripts/review_story20_execution.py | true |
| checks.stage4_actual_decision_and_next_proposal | true |
| checks.actual_original_UI_identity_live | true |
| checks.HTTP_original10B_UI_restored | true |
| checks.delivery_AGENTS.md | true |
| checks.delivery_README.md | true |
| checks.delivery_docs/autonomous_status.md | true |
| checks.delivery_docs/15_project_roadmap.md | true |
| checks.delivery_docs/windows_handoff.md | true |
| checks.delivery_docs/52_story20_low_lr_execution.md | true |
| checks.delivery_docs/53_story20_low_lr_judgment.md | true |
| sources./home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards/ready.json | "572cd8e003acfa5bb6e6ce7c395189af4143bbc19a678bbf2249b9807ea199dd" |
| sources./home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards/content-review.json | "0f09145e94e02043f400bba1e0825fd137d7cebeaa063e7744c10b411fa7878d" |
| sources./home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards/manifest.json | "213e11ddad72763ca5d1cb08b7a2c2a98a65989fe03dc194465d9ec4beec0921" |
| sources./home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards/samples.json | "be643b3d6aa671fef448b88b99061bee2d3f116a16b5f0452981513aabbed516" |
| sources./home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/job.json | "a38c5d1eb60850ae5382b02ae44f2f0cc2ff778ca41af323a6b8f7d80d7ddc5d" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/intermediate100M/coherent20/evaluation/result.json | "1f1aa0e6a88cf8e86e450f3a423fbdc019b6eec75fe04378b65eaa76a0a71afd" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/intermediate100M/coherent20/evaluation/generation.json | "d40a1ee97fb7321813d879f2fdc731c78b9c5b534a48a7baaa5b12a7791778fc" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/result/coherent20/evaluation/result.json | "338fa68df832a8fddfa63c6038c1b8f9c840ccbd9d8ee508c617494f4498a455" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/result/coherent20/evaluation/generation.json | "e2532f17497c9243ca4eade7227c74fcc563cdb327e3ca7aaa80854c7ae9c0a4" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/docs/autonomous_status.md | "ec9c89d56b7e76c496c85f90599a5295a173d1d0b0ec04e23133433d39acb44c" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/tests.xml | "179367c2e9b66a4e7c4c3cb9b8b7051efc32c4dee125ffdbd7240b1cd99911df" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/tests.xml | "025a90697cb8d71cd9021f926498f854490adff4f38728bc3372d02fb42a96c0" |
| scientific_tokens | 1100021760 |
| verification_tokens | 524288 |
| GPU_seconds | 6007.147478496008 |
| candidate500M_passes_acceptance | true |
| protected_test_used | false |
| original_UI.training_tokens | 10000007168 |
| original_UI.update | 305176 |
| original_UI.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/story20_judgment.json — None</summary>

[原記録](../../reports/phase6/story20_judgment.json) ／ SHA256: `282a3823c7dcce4355a4dc86e219801aeeca95c03a95d460a6811be5cd82881d` ／ 3,227 bytes

| 原キー | 保存値 |
|---|---|
| stage4_status | "complete" |
| scope | "Plan52 actual stages1-4 including conditional paired500M and full/long" |
| candidate500M_passes_acceptance | true |
| adoption | "Accepted by unchanged comparison gates as a research candidate; Base and Chat quality targets remain unmet" |
| checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/coherent20/checkpoint-00320435.pt" |
| checkpoint_sha256 | "f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac" |
| model_training_input_tokens | 10500014080 |
| scientific_tokens | 1100021760 |
| verification_tokens | 524288 |
| GPU_seconds | 6007.147478496008 |
| protected_test_used | false |
| next_proposal.comparison.learning_tokens | 500006912 |
| next_proposal.comparison.stable_updates | 14500 |
| next_proposal.comparison.decay_updates | 759 |
| next_proposal.comparison.interpretation | "New data composition as a whole; pool size, content and reuse change together, not a pure quality-only or unique-volume-only intervention" |
| next_proposal.budgets.scientific_tokens | 500006912 |
| next_proposal.budgets.primary_GPU_seconds | 1800 |
| next_proposal.budgets.conditional_new_candidate_full_GPU_seconds | 1800 |
| next_proposal.budgets.actual_config_and_data_must_be_frozen_before_execution | true |
| next_proposal.budgets.CPU_preparation_and_content_review | "Separate, bounded to required data; failure to secure intended amount/content stops before GPU" |
| next_proposal.completion_condition | "40 reproducibly random training texts reviewed and actual sources/amount/reuse disclosed; all80 generations graded; unchanged original gates and at least8 more coherent outputs versus current19/80 with paired95% lower&gt;0, EOS/repetition non-regression; eligible new-candidate full/long only, report/adopt-or-reject and stop; no automatic1B/20B/Chat/test/publication" |
| limitations | ["One training seed and repeatedly used dev", "Codex content scoring is not independent human blind", "Full corpus independent audit and broad duplicate/benchmark contamination checks remain incomplete", "Current source synthetic and source40 sample non-random", "100M intermediate and500M final are different phases of one common LR schedule"] |

</details>

<details>
<summary>reports/phase6/story20_low_lr_annotations.json — None</summary>

[原記録](../../reports/phase6/story20_low_lr_annotations.json) ／ SHA256: `1464bbc690dea9103f1bd0a9ae30791ff294ce28d19e1a1dba374087ff5a6880` ／ 14,025 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/story20_low_lr_full_launch.json — None</summary>

[原記録](../../reports/phase6/story20_low_lr_full_launch.json) ／ SHA256: `3cc22df5ff1c2f6b8bbaf17fb3370107a1edd6da5b43e0047ea996e9f430e8d7` ／ 650 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/story20_low_lr_full_result.json — complete</summary>

[原記録](../../reports/phase6/story20_low_lr_full_result.json) ／ SHA256: `c8b85a98d3af98764aa11c06e57459548fbc3add04b3b3375385bee7bf59c132` ／ 10,032 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| summary.web.training_input_tokens | 10100015104 |
| summary.web.full_dev_BPB | 0.9459608210110293 |
| summary.web.fixed80.eos | 0 |
| summary.web.fixed80.repetition | 59 |
| summary.web.fixed80.unicode_failure | 0 |
| summary.web.fixed80.role_leak | 0 |
| summary.web.fixed80.empty | 0 |
| summary.web.all400.eos | 6 |
| summary.web.all400.repetition | 126 |
| summary.web.all400.unicode_failure | 0 |
| summary.web.all400.role_leak | 0 |
| summary.web.all400.empty | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.repetition | 59 |
| summary.web.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.repetition | 59 |
| summary.web.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed42.eos | 3 |
| summary.web.generation_groups.sampling-suppressed1-seed42.repetition | 5 |
| summary.web.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed44.eos | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| summary.coherent20.label | "coherent20" |
| summary.coherent20.training_input_tokens | 10100015104 |
| summary.coherent20.full_dev_BPB | 0.9520806696198469 |
| summary.coherent20.fixed80.outputs | 80 |
| summary.coherent20.fixed80.eos | 23 |
| summary.coherent20.fixed80.repetition | 22 |
| summary.coherent20.fixed80.unicode_failure | 0 |
| summary.coherent20.fixed80.role_leak | 0 |
| summary.coherent20.fixed80.empty | 0 |
| summary.coherent20.all400.outputs | 400 |
| summary.coherent20.all400.eos | 127 |
| summary.coherent20.all400.repetition | 45 |
| summary.coherent20.all400.unicode_failure | 0 |
| summary.coherent20.all400.role_leak | 0 |
| summary.coherent20.all400.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.eos | 23 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.repetition | 22 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.eos | 23 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.repetition | 22 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.eos | 28 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.eos | 22 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.repetition | 1 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.eos | 31 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| parent.training_input_tokens | 10000007168 |
| parent.full_dev_BPB | 0.9540184727984398 |
| parent.fixed80.eos | 0 |
| parent.fixed80.repetition | 53 |
| parent.fixed80.unicode_failure | 0 |
| parent.fixed80.role_leak | 0 |
| parent.fixed80.empty | 0 |
| parent.all400.eos | 9 |
| parent.all400.repetition | 112 |
| parent.all400.unicode_failure | 0 |
| parent.all400.role_leak | 0 |
| parent.all400.empty | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed42.eos | 4 |
| parent.generation_groups.sampling-suppressed1-seed42.repetition | 3 |
| parent.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed44.eos | 3 |
| parent.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| parent.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| long_generation.web.conditions.128.natural_eos | 0 |
| long_generation.web.conditions.128.raw_utf8_failure | 0 |
| long_generation.web.conditions.512.natural_eos | 0 |
| long_generation.web.conditions.512.raw_utf8_failure | 0 |
| long_generation.coherent20.complete | true |
| long_generation.coherent20.conditions.128.count | 20 |
| long_generation.coherent20.conditions.128.expected | 20 |
| long_generation.coherent20.conditions.128.natural_eos | 9 |
| long_generation.coherent20.conditions.128.mean_char4_repeat | 0.473526548453593 |
| long_generation.coherent20.conditions.128.same_sentence_repeat | 8 |
| long_generation.coherent20.conditions.128.raw_utf8_failure | 0 |
| long_generation.coherent20.conditions.512.count | 20 |
| long_generation.coherent20.conditions.512.expected | 20 |
| long_generation.coherent20.conditions.512.natural_eos | 9 |
| long_generation.coherent20.conditions.512.mean_char4_repeat | 0.585896771817001 |
| long_generation.coherent20.conditions.512.same_sentence_repeat | 8 |
| long_generation.coherent20.conditions.512.raw_utf8_failure | 0 |
| checks.mixture.EOS_at_least8_more | true |
| checks.mixture.repetition_no_worse | true |
| checks.mixture.no_empty_role_unicode | true |
| checks.mixture.BPB_degradation_at_most1percent | true |
| checks.mixture.no_punctuation_only_stops | true |
| checks.parent_growth.full_BPB_no_major_regression | true |
| checks.parent_growth.fixed_repetition_not8_worse | true |
| checks.parent_growth.raw_unicode_empty_role_zero_all400 | true |
| candidate_passes_all_full_conditions | true |
| additional_training_tokens | 0 |
| protected_test_used | false |
| GPU_seconds | 1940.0297624170053 |

</details>

<details>
<summary>reports/phase6/story20_low_lr_full_review.json — passed</summary>

[原記録](../../reports/phase6/story20_low_lr_full_review.json) ／ SHA256: `0e36ec61bed46884879b836f822f58360f8e65826107e89ca83e2788508736f0` ／ 8,801 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checked_at | "2026-10-05T00:45:12.818871Z" |
| checks.actual_full_job_complete_exited | true |
| checks.full_config_screen_review_binding | true |
| checks.screen_was_eligible | true |
| checks.full_budget_zero_learning_and_honest_scope | true |
| checks.web_actual_checkpoint_and_full_binding | true |
| checks.web_full_common89416_complete_coverage | true |
| checks.web_actual_BPB_from_finite_NLL | true |
| checks.web_same_parent_body_scoring_protocol | true |
| checks.web_parent_aligned_documents_and400_requests | true |
| checks.web_actual_raw400_ID_flags | true |
| checks.web_fixed80_match_primary_IDs | true |
| checks.web_long_binding_requests_and_complete | true |
| checks.web_long_raw_text_stops_UTF8_and_metrics | true |
| checks.web_long128_summary_from_rows | true |
| checks.web_long512_summary_from_rows | true |
| checks.web_long_saved_summary_binding | true |
| checks.coherent20_actual_checkpoint_and_full_binding | true |
| checks.coherent20_full_common89416_complete_coverage | true |
| checks.coherent20_actual_BPB_from_finite_NLL | true |
| checks.coherent20_same_parent_body_scoring_protocol | true |
| checks.coherent20_parent_aligned_documents_and400_requests | true |
| checks.coherent20_actual_raw400_ID_flags | true |
| checks.coherent20_fixed80_match_primary_IDs | true |
| checks.coherent20_long_binding_requests_and_complete | true |
| checks.coherent20_long_raw_text_stops_UTF8_and_metrics | true |
| checks.coherent20_long128_summary_from_rows | true |
| checks.coherent20_long512_summary_from_rows | true |
| checks.coherent20_long_saved_summary_binding | true |
| checks.same_full_document_and_generation_requests_between_arms | true |
| checks.actual_summaries_original_gates_recomputed | true |
| summary.web.training_input_tokens | 10100015104 |
| summary.web.full_dev_BPB | 0.9459608210110293 |
| summary.web.fixed80.eos | 0 |
| summary.web.fixed80.repetition | 59 |
| summary.web.fixed80.unicode_failure | 0 |
| summary.web.fixed80.role_leak | 0 |
| summary.web.fixed80.empty | 0 |
| summary.web.all400.eos | 6 |
| summary.web.all400.repetition | 126 |
| summary.web.all400.unicode_failure | 0 |
| summary.web.all400.role_leak | 0 |
| summary.web.all400.empty | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.repetition | 59 |
| summary.web.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.web.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.repetition | 59 |
| summary.web.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.web.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed42.eos | 3 |
| summary.web.generation_groups.sampling-suppressed1-seed42.repetition | 5 |
| summary.web.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| summary.web.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.web.generation_groups.sampling-suppressed1-seed44.eos | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| summary.web.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.web.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| summary.coherent20.label | "coherent20" |
| summary.coherent20.training_input_tokens | 10100015104 |
| summary.coherent20.full_dev_BPB | 0.9520806696198469 |
| summary.coherent20.fixed80.outputs | 80 |
| summary.coherent20.fixed80.eos | 23 |
| summary.coherent20.fixed80.repetition | 22 |
| summary.coherent20.fixed80.unicode_failure | 0 |
| summary.coherent20.fixed80.role_leak | 0 |
| summary.coherent20.fixed80.empty | 0 |
| summary.coherent20.all400.outputs | 400 |
| summary.coherent20.all400.eos | 127 |
| summary.coherent20.all400.repetition | 45 |
| summary.coherent20.all400.unicode_failure | 0 |
| summary.coherent20.all400.role_leak | 0 |
| summary.coherent20.all400.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.eos | 23 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.repetition | 22 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.eos | 23 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.repetition | 22 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.eos | 28 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.eos | 22 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.repetition | 1 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.eos | 31 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.repetition | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| summary.coherent20.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| parent.training_input_tokens | 10000007168 |
| parent.full_dev_BPB | 0.9540184727984398 |
| parent.fixed80.eos | 0 |
| parent.fixed80.repetition | 53 |
| parent.fixed80.unicode_failure | 0 |
| parent.fixed80.role_leak | 0 |
| parent.fixed80.empty | 0 |
| parent.all400.eos | 9 |
| parent.all400.repetition | 112 |
| parent.all400.unicode_failure | 0 |
| parent.all400.role_leak | 0 |
| parent.all400.empty | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed1-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed1-seed42.empty | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.outputs | 80 |
| parent.generation_groups.greedy-suppressed0-seed42.eos | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.repetition | 53 |
| parent.generation_groups.greedy-suppressed0-seed42.unicode_failure | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.role_leak | 0 |
| parent.generation_groups.greedy-suppressed0-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed42.eos | 4 |
| parent.generation_groups.sampling-suppressed1-seed42.repetition | 3 |
| parent.generation_groups.sampling-suppressed1-seed42.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed42.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed43.eos | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.repetition | 2 |
| parent.generation_groups.sampling-suppressed1-seed43.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed43.empty | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.outputs | 80 |
| parent.generation_groups.sampling-suppressed1-seed44.eos | 3 |
| parent.generation_groups.sampling-suppressed1-seed44.repetition | 1 |
| parent.generation_groups.sampling-suppressed1-seed44.unicode_failure | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.role_leak | 0 |
| parent.generation_groups.sampling-suppressed1-seed44.empty | 0 |
| adoption_checks.mixture.EOS_at_least8_more | true |
| adoption_checks.mixture.repetition_no_worse | true |
| adoption_checks.mixture.no_empty_role_unicode | true |
| adoption_checks.mixture.BPB_degradation_at_most1percent | true |
| adoption_checks.mixture.no_punctuation_only_stops | true |
| adoption_checks.parent_growth.full_BPB_no_major_regression | true |
| adoption_checks.parent_growth.fixed_repetition_not8_worse | true |
| adoption_checks.parent_growth.raw_unicode_empty_role_zero_all400 | true |
| candidate_passes_all_full_conditions | true |
| long_generation.web.conditions.128.natural_eos | 0 |
| long_generation.web.conditions.128.raw_utf8_failure | 0 |
| long_generation.web.conditions.512.natural_eos | 0 |
| long_generation.web.conditions.512.raw_utf8_failure | 0 |
| long_generation.coherent20.complete | true |
| long_generation.coherent20.conditions.128.count | 20 |
| long_generation.coherent20.conditions.128.expected | 20 |
| long_generation.coherent20.conditions.128.natural_eos | 9 |
| long_generation.coherent20.conditions.128.mean_char4_repeat | 0.473526548453593 |
| long_generation.coherent20.conditions.128.same_sentence_repeat | 8 |
| long_generation.coherent20.conditions.128.raw_utf8_failure | 0 |
| long_generation.coherent20.conditions.512.count | 20 |
| long_generation.coherent20.conditions.512.expected | 20 |
| long_generation.coherent20.conditions.512.natural_eos | 9 |
| long_generation.coherent20.conditions.512.mean_char4_repeat | 0.585896771817001 |
| long_generation.coherent20.conditions.512.same_sentence_repeat | 8 |
| long_generation.coherent20.conditions.512.raw_utf8_failure | 0 |
| additional_training_tokens | 0 |
| protected_test_used | false |
| GPU_seconds | 1940.0297624170053 |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/coherent20-full.json | "579bbcd54df59db0efdf6f90ee580cc12ca035c10b3ff5f7e393c98f0c1dcdb2" |
| sources./home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-100m-20261005/full/coherent20/long-generation.json | "d8b81d88b0daafb4137f42c95b2c3f65c0a9a3e4707af5c85d415ef4364c4274" |

</details>

<details>
<summary>reports/phase6/story20_low_lr_launch.json — None</summary>

[原記録](../../reports/phase6/story20_low_lr_launch.json) ／ SHA256: `d8b51ef181658a1735d6e0dfde1e466357dd4a57f5595478ce3fffa8731783bc` ／ 534 bytes

| 原キー | 保存値 |
|---|---|

</details>
