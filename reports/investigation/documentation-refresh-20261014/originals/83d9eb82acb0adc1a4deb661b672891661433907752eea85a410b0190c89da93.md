# 評価・生成・意味診断 — 12/23

[分野一覧へ](06_evaluation.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/progress-result.json) ／ SHA256: `33a6f13b820b30fe5301aaf6833a47620dbe8e713eec95b86ac4c5f565f6515f` ／ 554,849 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/checkpoint-00323503.pt" |
| checkpoint.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checkpoint.binding.config_sha256 | "0a363551b149a330ce2a92851baa4057eeede146ef0505e384bef8931a831aab" |
| checkpoint.binding.arm | "outcome_EOS_only" |
| checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323185.pt" |
| checkpoint.binding.parent.sha256 | "ad4747898bc6492e1165edee6b870b09c8be9be944e03a9e4450fde406cb3f34" |
| checkpoint.binding.study_kind | "original_staged_suffix_conditional_prefix_mask_v1" |
| checkpoint.binding.teacher_goals.web | 75000000 |
| checkpoint.binding.teacher_goals.story | 5000000 |
| checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint.binding.target_rule | "conditional outcome+EOS only; original reference quotas stop input" |
| checkpoint.binding.optimizer_policy | "inherit" |
| checkpoint.binding.peak_lr | 1e-05 |
| checkpoint.updates | 318 |
| checkpoint.additional_supervised_tokens | 1801392 |
| checkpoint.additional_input_tokens | 10420224 |
| checkpoint.actual_body_bytes | 6695119 |
| checkpoint.reference_suffix_teacher_tokens | 10159637 |
| checkpoint.actual_source_accounting.teachers.web | 0 |
| checkpoint.actual_source_accounting.teachers.story | 0 |
| checkpoint.actual_source_accounting.teachers.ordinary_textbook | 159637 |
| checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| checkpoint.actual_source_accounting.eos.web | 0 |
| checkpoint.actual_source_accounting.eos.story | 0 |
| checkpoint.actual_source_accounting.eos.ordinary_textbook | 1202 |
| checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| checkpoint.actual_source_accounting.body_bytes.web | 0 |
| checkpoint.actual_source_accounting.body_bytes.story | 0 |
| checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| checkpoint.actual_source_accounting.focus.web | 0 |
| checkpoint.actual_source_accounting.focus.story | 0 |
| checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.kind | "same-streams-staged-source-order-v1" |
| checkpoint.sampler.goals.web | 75000000 |
| checkpoint.sampler.goals.story | 5000000 |
| checkpoint.sampler.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.context | 1024 |
| checkpoint.sampler.seed | 42 |
| checkpoint.sampler.position | 3068 |
| checkpoint.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.streams.web.sampler.seed | 42 |
| checkpoint.sampler.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.streams.web.sampler.position | 10327341 |
| checkpoint.sampler.streams.web.sampler.context | 1024 |
| checkpoint.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.streams.story.seed | 42 |
| checkpoint.sampler.streams.story.genre | "story" |
| checkpoint.sampler.streams.story.documents | 761448 |
| checkpoint.sampler.streams.story.epoch | 0 |
| checkpoint.sampler.streams.story.document_position | 38243 |
| checkpoint.sampler.streams.story.token_offset | 87 |
| checkpoint.sampler.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.streams.ordinary_textbook.document_position | 74189 |
| checkpoint.sampler.streams.ordinary_textbook.token_offset | 77 |
| checkpoint.sampler.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.streams.conditional_textbook.epoch | 114 |
| checkpoint.sampler.streams.conditional_textbook.document_position | 871 |
| checkpoint.sampler.streams.conditional_textbook.token_offset | 23 |
| checkpoint.sampler.source_teachers.web | 75000000 |
| checkpoint.sampler.source_teachers.story | 5000000 |
| checkpoint.sampler.source_teachers.ordinary_textbook | 10000000 |
| checkpoint.sampler.source_teachers.conditional_textbook | 10000000 |
| checkpoint.sampler.source_eos.web | 159170 |
| checkpoint.sampler.source_eos.story | 38240 |
| checkpoint.sampler.source_eos.ordinary_textbook | 74183 |
| checkpoint.sampler.source_eos.conditional_textbook | 234328 |
| checkpoint.sampler.source_tokens.web | 75183104 |
| checkpoint.sampler.source_tokens.story | 5039104 |
| checkpoint.sampler.source_tokens.ordinary_textbook | 10075136 |
| checkpoint.sampler.source_tokens.conditional_textbook | 10234880 |
| checkpoint.sampler.source_body_bytes.web | 292149840 |
| checkpoint.sampler.source_body_bytes.story | 20452979 |
| checkpoint.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| checkpoint.sampler.source_body_bytes.conditional_textbook | 37865985 |
| checkpoint.sampler.source_focus_teachers.web | 0 |
| checkpoint.sampler.source_focus_teachers.story | 0 |
| checkpoint.sampler.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoint.sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 159637 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 1202 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 680306 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "same-streams-staged-source-order-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 2750 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10327318 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 38243 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 87 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 72981 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 147 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 9840363 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 159170 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 38240 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 72981 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 75159552 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 5039104 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 9913344 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 292149840 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 20452979 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 42059165 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "c5731598e03dc91f7936673de06845eb53faf096030791578799fc99201f5c6f" |
| checkpoint.token_digest | "129220e93aed4e2e31b67a9daefab3af9585bc905502ec0f42a859986922a2b6" |
| checkpoint.reference_token_digest | "c5731598e03dc91f7936673de06845eb53faf096030791578799fc99201f5c6f" |
| checkpoint.training_seconds | 18.131375385826686 |
| evaluation.binding.teacher_goals.web | 75000000 |
| evaluation.binding.teacher_goals.story | 5000000 |
| evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluation.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| evaluation.body.documents | 256 |
| evaluation.body.limit_documents | 256 |
| evaluation.body.body_nll | 355608.9075078964 |
| evaluation.body.eos_nll | 263.3683707138989 |
| evaluation.body.body_bytes | 472055 |
| evaluation.body.body_tokens | 122343 |
| evaluation.body.bpb | 1.0868123573684936 |
| evaluation.body.seconds | 1.4028304950043093 |
| evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluation.generation.max_new_tokens | 64 |
| evaluation.greedy_rates.eos | 79 |
| evaluation.greedy_rates.repetition | 1 |
| evaluation.greedy_rates.unicode_failure | 0 |
| evaluation.greedy_rates.role_leak | 0 |
| evaluation.greedy_rates.empty | 0 |
| evaluation.diagnostics.semantics.primary.accuracy.point | 0.6145833333333334 |
| evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5677083333333334, 0.6614583333333334] |
| evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6145833333333334 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6145833333333334] |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5781135555977539 |
| evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.15625847779496568 |
| evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.time.seed | 42 |
| evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7583081570996979 |
| evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7129909365558912, 0.8036253776435045] |
| evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7583081570996979 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7311178247734139 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7794561933534743] |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7311178247734139 |
| evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4223385689354276 |
| evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| evaluation.diagnostics.jcqa.primary.accuracy.point | 0.291331546023235 |
| evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.26541554959785524, 0.31637622877569244] |
| evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.291331546023235 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.27658623771224305 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.3033958891867739] |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2770330652368186 |
| evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2761556488098438 |
| evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.09662606000210362 |
| evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluation.diagnostics.semantic_both_contexts.correct | 25 |
| evaluation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluation.protected_test_used | false |
| bridge.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| bridge.checks.weights_unchanged | true |
| bridge.checks.no_gradients | true |
| bridge.checks.eval_mode | true |
| bridge.checks.RNG_restored | true |
| bridge.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| bridge.summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.70703125 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 21 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.46875 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 14 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7109375 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 57 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 15 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| bridge.optimizer_updates | 0 |
| bridge.scientific_teacher_tokens | 0 |
| bridge.protected_test_used | false |
| bridge.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| retention.checks.weights_unchanged | true |
| retention.checks.no_gradients | true |
| retention.checks.eval_mode | true |
| retention.checks.RNG_restored | true |
| retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 64 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 16 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.75390625 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 57 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 49 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 15 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.74609375 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 66 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 59 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.625 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.optimizer_updates | 0 |
| retention.scientific_teacher_tokens | 0 |
| retention.protected_test_used | false |
| retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/review.json — rejected_single_prefix_mask_comparison</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/review.json) ／ SHA256: `f6abb4d5ebc9f78a36c7b6e34e9f478fb2f527593f5740018cc05651eabcd574` ／ 4,173 bytes

| 原キー | 保存値 |
|---|---|
| status | "rejected_single_prefix_mask_comparison" |
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
| summaries.outcome_EOS_only.BPB | 1.0868123573684936 |
| summaries.outcome_EOS_only.rates.outputs | 80 |
| summaries.outcome_EOS_only.rates.eos | 79 |
| summaries.outcome_EOS_only.rates.repetition | 1 |
| summaries.outcome_EOS_only.rates.unicode_failure | 0 |
| summaries.outcome_EOS_only.rates.role_leak | 0 |
| summaries.outcome_EOS_only.rates.empty | 0 |
| summaries.outcome_EOS_only.grammar2 | 72 |
| summaries.outcome_EOS_only.relevance2 | 53 |
| summaries.outcome_EOS_only.coherent | 35 |
| summaries.outcome_EOS_only.appropriate | 54 |
| summaries.outcome_EOS_only.notes_sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| summaries.outcome_EOS_only.generation_sha256 | "dd966fb8ca316e9f51ee1395b8902fccb4845f43fb940aa09a35c7ee7fd08c5a" |
| summaries.outcome_EOS_only.Japanese.semantics | 0.6145833333333334 |
| summaries.outcome_EOS_only.Japanese.jblimp | 0.7583081570996979 |
| summaries.outcome_EOS_only.Japanese.jcqa | 0.291331546023235 |
| accounting.completed_updates | 318 |
| accounting.new_actual_hard_teachers | 1801392 |
| accounting.physical_input_tokens | 10420224 |
| accounting.reference_input_teachers | 10159637 |
| accounting.actual_source_accounting.teachers.web | 0 |
| accounting.actual_source_accounting.teachers.story | 0 |
| accounting.actual_source_accounting.teachers.ordinary_textbook | 159637 |
| accounting.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.actual_source_accounting.eos.web | 0 |
| accounting.actual_source_accounting.eos.story | 0 |
| accounting.actual_source_accounting.eos.ordinary_textbook | 1202 |
| accounting.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.actual_source_accounting.body_bytes.web | 0 |
| accounting.actual_source_accounting.body_bytes.story | 0 |
| accounting.actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| accounting.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| accounting.all_original_reference_input_and_cursor_checks | true |
| accounting.matched_teacher_budget | false |
| relative_to_original_strong_staged.checks.coherence_gain_at_least8 | true |
| relative_to_original_strong_staged.checks.paired_CI_lower_above0 | true |
| relative_to_original_strong_staged.checks.EOS_nonworsening | true |
| relative_to_original_strong_staged.checks.repetition_nonworsening | true |
| relative_to_original_strong_staged.checks.no_empty_role_unicode | true |
| relative_to_original_strong_staged.checks.BPB_gate | true |
| relative_to_original_strong_staged.checks.appropriate_completion_not_punctuation | true |
| relative_to_original_strong_staged.passed | true |
| absolute_and_historical_guards.EOS_at_least8_more | true |
| absolute_and_historical_guards.repetition_no_worse | true |
| absolute_and_historical_guards.no_empty_role_unicode | true |
| absolute_and_historical_guards.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| actual_science_GPU_seconds | 50.63884665700607 |
| own_probe_GPU_seconds | 17.082726756983902 |
| matched_teacher_budget | false |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Masking changes hard teacher count and EOS target fraction, and the hypothesis follows observed failures. One suffix/nonblind80 does not isolate amount, prove the sole root cause, certify human judgement or a model capacity ceiling." |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0000.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0000.json) ／ SHA256: `a6c8716116dc1dfaf679d52b323b391807a6c4aae11dae09daaaa35faf112c70` ／ 10,069 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0016.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0016.json) ／ SHA256: `eb924750ae3363f1699fb4979dd6a2636218c0fb4422276f2946a985f3e2aaa9` ／ 9,686 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0032.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0032.json) ／ SHA256: `4d4c14c874336fdc7adb158b5eebd1c602833f648acb4859756d2a31630a4008` ／ 10,344 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0048.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0048.json) ／ SHA256: `19073ad85d45015544b3dac232e010b3cde252a9873facdc0c6ffd2152acf483` ／ 9,633 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0064.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0064.json) ／ SHA256: `9bb9f05a317902e38bcd870a57b7d5c040ca66c0fc4f107a16c61afe0cbb0313` ／ 10,417 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0080.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0080.json) ／ SHA256: `f9143ce75f289d8e1ae8dc3dd476de0df3981b305d442486dd9dac48cf9c71d0` ／ 9,834 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0096.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0096.json) ／ SHA256: `554a17e69376d77cb73e2de3b66ec8842b9c8f8c7b5725a5cb118c8797cb3ef7` ／ 9,915 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0112.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0112.json) ／ SHA256: `109229f1b4095ce2c53d9637520e4c2312a4d3cfe8618638a294c73fdc2a4214` ／ 10,263 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0128.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0128.json) ／ SHA256: `a9cb0dfeddf7837d7d0dbc72af0417407c6365bda59ee379d20172769fbe8573` ／ 9,916 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0144.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0144.json) ／ SHA256: `0fbc15a5ca9ae061ec6492e4293e60695e785992fee015e9c0850fe70ef427ae` ／ 10,008 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0160.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0160.json) ／ SHA256: `f7d6f4d64a5088735a3226c1ea1d77448ada22bacf15dc78e256e5a35f23dbc2` ／ 10,269 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0176.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0176.json) ／ SHA256: `1ed0db30d8e8c9d2c224d44f228ceb769ac4110c4c63a1a1b04073149180af97` ／ 10,074 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0192.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0192.json) ／ SHA256: `19598c70ba6dc6cee2769f4fb02300f616ed93c6973d2d680471a49693bf969a` ／ 10,016 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0208.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0208.json) ／ SHA256: `5f0c02a3eb3b6adf50a4399b1b9b5caf0110d3cf0f6fe1aa702a14e4cb8d992f` ／ 9,752 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0224.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0224.json) ／ SHA256: `1637b244fd75ed4af61963c4fda851007cdd19c70de0b24d542409781c05ff5c` ／ 9,887 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0240.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0240.json) ／ SHA256: `17985c1a3ac12a02b70da5bda1eba87d3bd766feac99a2c3a32e23184e0fe575` ／ 9,756 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0256.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0256.json) ／ SHA256: `3a0d4331628f724a8e9f2e8e77094fac8c82fa6c74cf2afe0a25767531ee1a31` ／ 9,735 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0272.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0272.json) ／ SHA256: `4acfa0abe187bff3225c108c602eadb0bed26aa38cba4effd5315c2ae7149320` ／ 9,704 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0288.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0288.json) ／ SHA256: `d7a829db0957d279f6ace92e9d6f0a8c81b7135ab919be1d4973d93dfc9a9164` ／ 9,750 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0304.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0304.json) ／ SHA256: `720fb06ae67b56ea56ae3627b2dc2bf5d55415a51756b20c5a3ffa9a4030645c` ／ 9,932 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0320.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0320.json) ／ SHA256: `7f72f8c16b5e90d402cc07ab16490d6289d3b279d4a1005f2a9bcb0f218597c2` ／ 9,450 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0336.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0336.json) ／ SHA256: `4de90cb1b5506e4fa13fa67b646844772e7bfb15ef35210c947f32bbdd392058` ／ 9,563 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0352.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0352.json) ／ SHA256: `35ecfc74abec73b6fb2714a8f6f7fe99f761e953386a0c9e5c246320427f79e2` ／ 9,922 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0368.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0368.json) ／ SHA256: `9ad4999dbf4a52a284240f32e837b2ef963a841c84e39350330009b38efbf74b` ／ 9,644 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0384.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0384.json) ／ SHA256: `4f138bdb69a1dd58c4f8f263a7e5871f4742ea46d21199c8ad9a204457f1467d` ／ 9,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0400.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0400.json) ／ SHA256: `cb04a9fce2886d8324dae4317efd5bc7c6262f25670fe05ec5d251f696881049` ／ 9,632 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0416.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0416.json) ／ SHA256: `159fbc50b649b83269473ccb9f824c077558331cc333ad6f158f258feeb8217b` ／ 10,022 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0432.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0432.json) ／ SHA256: `87cee2136a764c5ff7f990e2e314fffe9b32b4e9279008719924e1baa7d9ad95` ／ 9,486 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0448.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0448.json) ／ SHA256: `471f889ad2d56451f8ac3c89ff953127616df128ef636d7f94bfe3ef9c4df1d9` ／ 9,722 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0464.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0464.json) ／ SHA256: `0cd3c636f524d227f45e8d599fbeb27f0303704cd24ca4035e9baaff7f342ae2` ／ 9,557 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0480.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0480.json) ／ SHA256: `fe6340ccf3b1aabef01320b3ed1aaa827c02d02293d6ab1521e35adfebcacc96` ／ 9,551 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0496.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0496.json) ／ SHA256: `2a62e9c2b0471e3aeb88e45a2823650f8a7e38443be8ae19ae396dc06c5e4594` ／ 9,618 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/result.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/result.json) ／ SHA256: `27ef4a660a491cf17d429c22fe0f4812156961a943deeba044fa6760d62b4387` ／ 185,967 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7109375 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 57 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.70703125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 21 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 97 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 57 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.46875 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 14 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7109375 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 97 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9453125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 57 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 7 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 15 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 33 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0000.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0000.json) ／ SHA256: `e27ccd882a648c6551c13f9b4ccbef21ab020984e8ae2d51057e7db70831110c` ／ 8,029 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0016.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0016.json) ／ SHA256: `c02052a4cb760a8ea82b1762b385cbdbec849aade678491ac9446f6842ee0f13` ／ 8,392 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0032.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0032.json) ／ SHA256: `ef972b81c979e5977524ed3e36525816e56511455504f24a6458764ed8d1a9b8` ／ 7,064 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0048.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0048.json) ／ SHA256: `6cb82def92704d49db150ceda0dbb272aa56091d3165b8e8aeb09325d16f55eb` ／ 8,238 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0064.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0064.json) ／ SHA256: `38f915e28c1121f82c6bf896def180873c7e99dd41ac41c4dea272f8ad2c686d` ／ 8,588 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0080.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0080.json) ／ SHA256: `1d0f84d85609c6b11f212fb509e03e4cffe75735395c979a260faff918e9d8d5` ／ 7,142 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0096.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0096.json) ／ SHA256: `f5c5f91b0da962ec8dd47e5389e21b1a2e5f92a95499a245ec4c333031f915df` ／ 8,145 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0112.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0112.json) ／ SHA256: `7f7577f9e143c3d9b38a8e549649b58b190255c928429d56a2482d5f14b88f17` ／ 8,334 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0128.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0128.json) ／ SHA256: `19ae4424cadf56c9ece80a4ac5a6c29b6b92d7417586201ffcbd5560c0b0c8d1` ／ 7,151 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0144.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0144.json) ／ SHA256: `8167bca0d9a5c1d345855eb24894a9c6ea60c8a9573dcd6f848a95d4ce50d149` ／ 8,205 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0160.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0160.json) ／ SHA256: `128fef19b5b82a0ec67c5c877c78403a5d97313e0fb70fd831f22c59486d512b` ／ 8,693 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0176.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0176.json) ／ SHA256: `b3504f79dfd2a0c0a32ea800dd10206ac26aaad238591e13e0ab6454b6cda421` ／ 6,991 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0192.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0192.json) ／ SHA256: `63dd8ca20311b80ecccf15a9bb754a768d5469e59dc4f3e09b57a9466f96eb80` ／ 8,207 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0208.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0208.json) ／ SHA256: `bc6cbcb3bb9e517ecf39d495d496ccfd6c7de8350045092e5828ae5170ff5201` ／ 8,589 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0224.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0224.json) ／ SHA256: `3449a92bf375b77419ef67324ad4f701a67eef700457d8eced601a1deb5301ba` ／ 7,165 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0240.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0240.json) ／ SHA256: `52f5801b7425b7ecf9e2fd18492945123671eba10c8b7722d941bf3edbb5f6d4` ／ 8,405 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0256.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0256.json) ／ SHA256: `415428a019785da1c9a40f6503ef6fdd4fca319a364dd28dadef7e0871d70a74` ／ 8,316 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0272.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0272.json) ／ SHA256: `89100ca68b11e697b9dc48979af74b3dd522fc8b09f000620d8f14c16f8e94bd` ／ 8,521 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0288.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0288.json) ／ SHA256: `714ea97668dada7e8bde51ec34f879b12023a2e2a6c53149e1b4bd9da21e4683` ／ 7,188 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0304.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0304.json) ／ SHA256: `b7fd5116f8e05a9d4c56d3a122bff69ddab7d27234a594656a4ea5c97f87df1a` ／ 8,203 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0320.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0320.json) ／ SHA256: `35b36f1723df1d188ee8b5b7fd0b75000b6be929693aa1623b68ad39e5b2cf08` ／ 8,703 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0336.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0336.json) ／ SHA256: `c2f3a82728b7e5a7b3ae5b769f5e2f9c83fcc226a4cf11169b5fcc6646156e26` ／ 7,180 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0352.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0352.json) ／ SHA256: `4d7438ed4818240d3576a58ab5cfa2171a8cfea11a218df53f4399d5639717d5` ／ 8,220 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0368.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0368.json) ／ SHA256: `5d18f60356e9bf9ae32778c43b6e819338a64318056a1ae6591176151b19b701` ／ 8,265 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0384.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0384.json) ／ SHA256: `a9495bf0dc6fed2440becae11cfac64faf0185987b056927aa587867c1e62875` ／ 7,097 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0400.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0400.json) ／ SHA256: `e535dac1d0097de6307b6899945c1cf6431464928a4cbbd6ec8378808b3cdfcd` ／ 8,206 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0416.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0416.json) ／ SHA256: `3cffbb6d77ba5ab91d46a93c444d0eb82d0f97991f193901f909b7a897272666` ／ 8,268 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0432.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0432.json) ／ SHA256: `d5f136d88e4da0df0771da4ed82248b9fff578c57b35befecb79e2f59cf899af` ／ 7,182 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0448.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0448.json) ／ SHA256: `ec26c3bca7331ef9f9c7580f431f4dca384c46f43f9a90074b881b85f46a1682` ／ 8,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0464.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0464.json) ／ SHA256: `6d43295be0d997266234f58013b0f9f8b06ab26510093795a4ef3a9c74468aa9` ／ 8,438 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0480.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0480.json) ／ SHA256: `829b06b9f76f2431b5845a07571c91f770c8e98969c0102214a912881a2b574e` ／ 7,095 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0496.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0496.json) ／ SHA256: `bad7f1d13abdf8c4fce818f5a89e0c2e9a98bd23b1bbcd2218ca27bc1d9b81e4` ／ 8,140 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/result.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/result.json) ／ SHA256: `3256b54c76130ed6a752c9f6151f4b2e84aa9436c6c01c68ecaea927c880174f` ／ 182,522 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "bce6b3820c3430f511d2508186d0d2ee91b0a96c1b6f2304b75c63e5c8699deb" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.73828125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 64 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 48 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6015625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 16 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.75390625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 68 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 57 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8828125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 49 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 15 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 19 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.74609375 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 66 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 59 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8671875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 47 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 17 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 61 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 19 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 42 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-probe-launcher-20261006/launcher.json) ／ SHA256: `f5bbc7b820c91665b2a6c7c5e54f88538807e3e32a36fcdcbc24fd7655a463e7` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-probe-launcher-20261006/result.json) ／ SHA256: `71deae9b829df2e9eb3ca339eb3fef2fb6c13bc47a95aadd5975c121d6939e08` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-train-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-train-launcher-20261006/launcher.json) ／ SHA256: `26fcdbe5bbc253e2a317ca936be31b59a2c297365d34f5890d33ff46eaac3829` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/conditional-prefix-mask-train-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/conditional-prefix-mask-train-launcher-20261006/result.json) ／ SHA256: `8e5a85382177dbda1cadbb70536159e878e54cc7e116636a277f0698c9c06592` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_active_job.json — complete_actual_process_absent</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_active_job.json) ／ SHA256: `08ebf12da2969a5d7b29939ec7513bcc325ad83ed49c8a0c240e55f0965b7131` ／ 1,189 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_actual_process_absent" |
| terminal_job.status | "complete" |
| terminal_job.GPU_elapsed_seconds | 50.63884665700607 |
| terminal_job.completed_updates | 300 |
| terminal_job.total_updates | 318 |
| terminal_job.actual_teachers | 1710803 |
| terminal_job.reference_teachers | 9606866 |
| terminal_job.loss | 0.06465114653110504 |
| science_GPU_seconds | 50.63884665700607 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_completion.json — all80_complete_relative_generation_improved_historical_Web_retention_failed_unadopted</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_completion.json) ／ SHA256: `60d9bed29315da95b0242fd41badd69e9e3ce7358a4b78fe9af5e8efd7fde62c` ／ 6,530 bytes

| 原キー | 保存値 |
|---|---|
| status | "all80_complete_relative_generation_improved_historical_Web_retention_failed_unadopted" |
| actual_terminal_job.status | "complete" |
| actual_terminal_job.GPU_elapsed_seconds | 50.63884665700607 |
| actual_terminal_job.completed_updates | 300 |
| actual_terminal_job.total_updates | 318 |
| actual_terminal_job.actual_teachers | 1710803 |
| actual_terminal_job.reference_teachers | 9606866 |
| actual_terminal_job.loss | 0.06465114653110504 |
| actual_scientific_process_absent | true |
| scientific_optimizer_updates | 318 |
| scientific_actual_hard_teacher_tokens | 1801392 |
| reference_suffix_teacher_tokens | 10159637 |
| physical_input_tokens | 10420224 |
| actual_source_accounting.teachers.web | 0 |
| actual_source_accounting.teachers.story | 0 |
| actual_source_accounting.teachers.ordinary_textbook | 159637 |
| actual_source_accounting.teachers.conditional_textbook | 1641755 |
| actual_source_accounting.eos.web | 0 |
| actual_source_accounting.eos.story | 0 |
| actual_source_accounting.eos.ordinary_textbook | 1202 |
| actual_source_accounting.eos.conditional_textbook | 234328 |
| actual_source_accounting.body_bytes.web | 0 |
| actual_source_accounting.body_bytes.story | 0 |
| actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| probe_optimizer_updates | 48 |
| probe_teacher_tokens | 653485 |
| science_GPU_seconds | 50.63884665700607 |
| probe_GPU_seconds | 17.082726756983902 |
| total_new_GPU_seconds | 67.72157341398997 |
| GPU_ceiling_seconds | 600 |
| previous_related_GPU_seconds_preserved | 2858.847923864086 |
| related_GPU_seconds | 2926.569497278076 |
| matched_teacher_budget | false |
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
| summaries.outcome_EOS_only.BPB | 1.0868123573684936 |
| summaries.outcome_EOS_only.rates.outputs | 80 |
| summaries.outcome_EOS_only.rates.eos | 79 |
| summaries.outcome_EOS_only.rates.repetition | 1 |
| summaries.outcome_EOS_only.rates.unicode_failure | 0 |
| summaries.outcome_EOS_only.rates.role_leak | 0 |
| summaries.outcome_EOS_only.rates.empty | 0 |
| summaries.outcome_EOS_only.grammar2 | 72 |
| summaries.outcome_EOS_only.relevance2 | 53 |
| summaries.outcome_EOS_only.coherent | 35 |
| summaries.outcome_EOS_only.appropriate | 54 |
| summaries.outcome_EOS_only.notes_sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| summaries.outcome_EOS_only.generation_sha256 | "dd966fb8ca316e9f51ee1395b8902fccb4845f43fb940aa09a35c7ee7fd08c5a" |
| summaries.outcome_EOS_only.Japanese.semantics | 0.6145833333333334 |
| summaries.outcome_EOS_only.Japanese.jblimp | 0.7583081570996979 |
| summaries.outcome_EOS_only.Japanese.jcqa | 0.291331546023235 |
| generation_relative_guards.checks.coherence_gain_at_least8 | true |
| generation_relative_guards.checks.paired_CI_lower_above0 | true |
| generation_relative_guards.checks.EOS_nonworsening | true |
| generation_relative_guards.checks.repetition_nonworsening | true |
| generation_relative_guards.checks.no_empty_role_unicode | true |
| generation_relative_guards.checks.BPB_gate | true |
| generation_relative_guards.checks.appropriate_completion_not_punctuation | true |
| generation_relative_guards.passed | true |
| historical_retention_guards.EOS_at_least8_more | true |
| historical_retention_guards.repetition_no_worse | true |
| historical_retention_guards.no_empty_role_unicode | true |
| historical_retention_guards.BPB_degradation_at_most1percent | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| CPU_completion_seconds | 0.13052477600285783 |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_portable.json — None</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_portable.json) ／ SHA256: `1f78f97459004bccfa9bf9ba439f7897cf6d3ae4881f1e6e1d26262a9e2e135d` ／ 21,936 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/conditional_prefix_mask_completion.json.bytes | 6530 |
| files.reports/phase6/conditional_prefix_mask_completion.json.sha256 | "60d9bed29315da95b0242fd41badd69e9e3ce7358a4b78fe9af5e8efd7fde62c" |
| files.reports/phase6/shared_prefix_web_loss_proposal.json.bytes | 4124 |
| files.reports/phase6/shared_prefix_web_loss_proposal.json.sha256 | "0d02c9d77781623a17c67e67f26e6ff052506b65880ff99cf9bca2526a8bd857" |
| files.configs/phase6/conditional_prefix_mask.json.bytes | 18078 |
| files.configs/phase6/conditional_prefix_mask_probe.json.bytes | 17454 |
| files.reports/phase6/conditional_prefix_mask_proposal.json.bytes | 6313 |
| files.reports/phase6/conditional_prefix_mask_reference_input.json.bytes | 416371 |
| files.reports/phase6/conditional_prefix_mask_active_job.json.bytes | 1189 |
| files.reports/phase6/conditional_prefix_mask_review.json.bytes | 4173 |
| files.reports/phase6/conditional_prefix_mask_tests.xml.bytes | 703 |
| files.reports/phase6/conditional_prefix_mask_tests.xml.sha256 | "3dd7ff7170b72e7e421c01daed7868fe60f374166b447908fc64b79be9b0f090" |
| files.reports/phase6/conditional_prefix_mask_tests_initial_failure.xml.bytes | 2467 |
| files.reports/phase6/conditional_prefix_mask_tests_initial_failure.xml.sha256 | "8697dc4fc87c25769fc09c5aaf2263dbc98f12058ea5e428ef9a5ddc8edebd69" |
| files.reports/phase6/conditional_prefix_mask_review_tests.xml.bytes | 426 |
| files.reports/phase6/conditional_prefix_mask_review_tests.xml.sha256 | "70824f61d9f743916de21b00c064c86714ffd9deec84b7e3b663e687a5ab7cd5" |
| files.scripts/review_conditional_prefix_mask.py.bytes | 8799 |
| files.tests/test_conditional_prefix_mask_review.py.bytes | 2400 |
| files.tests/test_conditional_prefix_mask_review.py.sha256 | "95dd22f1041ae69a597d9e9cac676ccf71059f84c7ca7f80b04a3e960e09cfd1" |
| files.scripts/record_conditional_prefix_mask_completion.py.bytes | 13563 |
| files.scripts/record_conditional_prefix_mask_completion.py.sha256 | "9db34cc2b062ba6e102e833ae9e7c1325288b3f9d1ad6de0e749338e220387ca" |
| files.scripts/record_conditional_prefix_mask_content.py.bytes | 13872 |
| files.scripts/record_conditional_prefix_mask_preparation.py.bytes | 7094 |
| files.scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.scripts/run_conditional_prefix_mask.py.bytes | 24674 |
| files.scripts/run_conditional_prefix_mask.ps1.bytes | 3109 |
| files.tests/test_conditional_prefix_mask.py.bytes | 5430 |
| files.tests/test_conditional_prefix_mask.py.sha256 | "6063bdac436aaea64860228e4c8af1945c93639ea8706758685688bf95158fd0" |
| files.reports/phase6/conditional_prefix_mask_preparation.json.bytes | 5637 |
| files.reports/phase6/conditional_prefix_mask_preparation_portable.json.bytes | 3511 |
| files.reports/phase6/conditional-prefix-mask-20261006/compare-result.json.bytes | 555424 |
| files.reports/phase6/conditional-prefix-mask-20261006/content-notes.json.bytes | 24260 |
| files.reports/phase6/conditional-prefix-mask-20261006/content-notes.json.sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/body.json.bytes | 67183 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/body.json.sha256 | "897e349c27f891502ddbddbfe3a68c7cc4b64e568a4ba53baa9992e129ec2628" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json.bytes | 50283 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/generation.json.sha256 | "dd966fb8ca316e9f51ee1395b8902fccb4845f43fb940aa09a35c7ee7fd08c5a" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jblimp.json.bytes | 338266 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jblimp.json.sha256 | "e3d3130476757fd5189831eac9203c0d96ffc99035066f7f35c0ce4ed5162af0" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jcqa.json.bytes | 1641835 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/jcqa.json.sha256 | "e15b8a078132d84c7203afe0314e5dc17d41dad03bc9a2da1336dd72d49f3c46" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/result.json.bytes | 140105 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/result.json.sha256 | "cf853457f80a95ae6e4eb5164b7b0c2f7c70ae217aeca6e9fa8638694dc57ded" |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/semantics.json.bytes | 202951 |
| files.reports/phase6/conditional-prefix-mask-20261006/evaluation/outcome_EOS_only/evaluation/semantics.json.sha256 | "4b7571f44a05e4799dc6ca30d86b5aa27eaadcf75dfc88dbddc89b0d0aecbccc" |
| files.reports/phase6/conditional-prefix-mask-20261006/job.json.bytes | 802 |
| files.reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/latest.json.bytes | 288 |
| files.reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/latest.json.sha256 | "5adae3a062451d6e77c90991552a392d873cfb8e3cf852556325c39d39e90d37" |
| files.reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/metrics.jsonl.bytes | 831350 |
| files.reports/phase6/conditional-prefix-mask-20261006/outcome_EOS_only/training/metrics.jsonl.sha256 | "997dacf16b3e8401c77d82475931a49a6e061185774ee5cadec94e35e7c13647" |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/job.json.bytes | 542 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/result.json.bytes | 179337 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json.bytes | 268 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/latest.json.sha256 | "f59cf223dad31bd609b3fa583bccad26df932c065c769fd1776ce58d1398dba6" |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/resume-gate/result.json.bytes | 58834 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json.bytes | 266 |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/latest.json.sha256 | "f30b45ad19decd079082b1779bde955715a99d3e9fdaf3e6ef4f2fbe9c1cc36d" |
| files.reports/phase6/conditional-prefix-mask-20261006/probe/timing/metrics.jsonl.bytes | 82582 |
| files.reports/phase6/conditional-prefix-mask-20261006/progress-result.json.bytes | 554849 |
| files.reports/phase6/conditional-prefix-mask-20261006/review.json.bytes | 4173 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0000.json.bytes | 10069 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0000.json.sha256 | "a6c8716116dc1dfaf679d52b323b391807a6c4aae11dae09daaaa35faf112c70" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0016.json.bytes | 9686 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0016.json.sha256 | "eb924750ae3363f1699fb4979dd6a2636218c0fb4422276f2946a985f3e2aaa9" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0032.json.bytes | 10344 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0032.json.sha256 | "4d4c14c874336fdc7adb158b5eebd1c602833f648acb4859756d2a31630a4008" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0048.json.bytes | 9633 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0048.json.sha256 | "19073ad85d45015544b3dac232e010b3cde252a9873facdc0c6ffd2152acf483" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0064.json.bytes | 10417 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0064.json.sha256 | "9bb9f05a317902e38bcd870a57b7d5c040ca66c0fc4f107a16c61afe0cbb0313" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0080.json.bytes | 9834 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0080.json.sha256 | "f9143ce75f289d8e1ae8dc3dd476de0df3981b305d442486dd9dac48cf9c71d0" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0096.json.bytes | 9915 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0096.json.sha256 | "554a17e69376d77cb73e2de3b66ec8842b9c8f8c7b5725a5cb118c8797cb3ef7" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0112.json.bytes | 10263 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0112.json.sha256 | "109229f1b4095ce2c53d9637520e4c2312a4d3cfe8618638a294c73fdc2a4214" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0128.json.bytes | 9916 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0128.json.sha256 | "a9cb0dfeddf7837d7d0dbc72af0417407c6365bda59ee379d20172769fbe8573" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0144.json.bytes | 10008 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0144.json.sha256 | "0fbc15a5ca9ae061ec6492e4293e60695e785992fee015e9c0850fe70ef427ae" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0160.json.bytes | 10269 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0160.json.sha256 | "f7d6f4d64a5088735a3226c1ea1d77448ada22bacf15dc78e256e5a35f23dbc2" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0176.json.bytes | 10074 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0176.json.sha256 | "1ed0db30d8e8c9d2c224d44f228ceb769ac4110c4c63a1a1b04073149180af97" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0192.json.bytes | 10016 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0192.json.sha256 | "19598c70ba6dc6cee2769f4fb02300f616ed93c6973d2d680471a49693bf969a" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0208.json.bytes | 9752 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0208.json.sha256 | "5f0c02a3eb3b6adf50a4399b1b9b5caf0110d3cf0f6fe1aa702a14e4cb8d992f" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0224.json.bytes | 9887 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0224.json.sha256 | "1637b244fd75ed4af61963c4fda851007cdd19c70de0b24d542409781c05ff5c" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0240.json.bytes | 9756 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0240.json.sha256 | "17985c1a3ac12a02b70da5bda1eba87d3bd766feac99a2c3a32e23184e0fe575" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0256.json.bytes | 9735 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0256.json.sha256 | "3a0d4331628f724a8e9f2e8e77094fac8c82fa6c74cf2afe0a25767531ee1a31" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0272.json.bytes | 9704 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0272.json.sha256 | "4acfa0abe187bff3225c108c602eadb0bed26aa38cba4effd5315c2ae7149320" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0288.json.bytes | 9750 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0288.json.sha256 | "d7a829db0957d279f6ace92e9d6f0a8c81b7135ab919be1d4973d93dfc9a9164" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0304.json.bytes | 9932 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0304.json.sha256 | "720fb06ae67b56ea56ae3627b2dc2bf5d55415a51756b20c5a3ffa9a4030645c" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0320.json.bytes | 9450 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0320.json.sha256 | "7f72f8c16b5e90d402cc07ab16490d6289d3b279d4a1005f2a9bcb0f218597c2" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0336.json.bytes | 9563 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0336.json.sha256 | "4de90cb1b5506e4fa13fa67b646844772e7bfb15ef35210c947f32bbdd392058" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0352.json.bytes | 9922 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0352.json.sha256 | "35ecfc74abec73b6fb2714a8f6f7fe99f761e953386a0c9e5c246320427f79e2" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0368.json.bytes | 9644 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0368.json.sha256 | "9ad4999dbf4a52a284240f32e837b2ef963a841c84e39350330009b38efbf74b" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0384.json.bytes | 9989 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0384.json.sha256 | "4f138bdb69a1dd58c4f8f263a7e5871f4742ea46d21199c8ad9a204457f1467d" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0400.json.bytes | 9632 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0400.json.sha256 | "cb04a9fce2886d8324dae4317efd5bc7c6262f25670fe05ec5d251f696881049" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0416.json.bytes | 10022 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0416.json.sha256 | "159fbc50b649b83269473ccb9f824c077558331cc333ad6f158f258feeb8217b" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0432.json.bytes | 9486 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0432.json.sha256 | "87cee2136a764c5ff7f990e2e314fffe9b32b4e9279008719924e1baa7d9ad95" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0448.json.bytes | 9722 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0448.json.sha256 | "471f889ad2d56451f8ac3c89ff953127616df128ef636d7f94bfe3ef9c4df1d9" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0464.json.bytes | 9557 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0464.json.sha256 | "0cd3c636f524d227f45e8d599fbeb27f0303704cd24ca4035e9baaff7f342ae2" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0480.json.bytes | 9551 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0480.json.sha256 | "fe6340ccf3b1aabef01320b3ed1aaa827c02d02293d6ab1521e35adfebcacc96" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0496.json.bytes | 9618 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/0496.json.sha256 | "2a62e9c2b0471e3aeb88e45a2823650f8a7e38443be8ae19ae396dc06c5e4594" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/result.json.bytes | 185967 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/bridge/outcome_EOS_only/result.json.sha256 | "27ef4a660a491cf17d429c22fe0f4812156961a943deeba044fa6760d62b4387" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0000.json.bytes | 8029 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0000.json.sha256 | "e27ccd882a648c6551c13f9b4ccbef21ab020984e8ae2d51057e7db70831110c" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0016.json.bytes | 8392 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0016.json.sha256 | "c02052a4cb760a8ea82b1762b385cbdbec849aade678491ac9446f6842ee0f13" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0032.json.bytes | 7064 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0032.json.sha256 | "ef972b81c979e5977524ed3e36525816e56511455504f24a6458764ed8d1a9b8" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0048.json.bytes | 8238 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0048.json.sha256 | "6cb82def92704d49db150ceda0dbb272aa56091d3165b8e8aeb09325d16f55eb" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0064.json.bytes | 8588 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0064.json.sha256 | "38f915e28c1121f82c6bf896def180873c7e99dd41ac41c4dea272f8ad2c686d" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0080.json.bytes | 7142 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0080.json.sha256 | "1d0f84d85609c6b11f212fb509e03e4cffe75735395c979a260faff918e9d8d5" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0096.json.bytes | 8145 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0096.json.sha256 | "f5c5f91b0da962ec8dd47e5389e21b1a2e5f92a95499a245ec4c333031f915df" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0112.json.bytes | 8334 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0112.json.sha256 | "7f7577f9e143c3d9b38a8e549649b58b190255c928429d56a2482d5f14b88f17" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0128.json.bytes | 7151 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0128.json.sha256 | "19ae4424cadf56c9ece80a4ac5a6c29b6b92d7417586201ffcbd5560c0b0c8d1" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0144.json.bytes | 8205 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0144.json.sha256 | "8167bca0d9a5c1d345855eb24894a9c6ea60c8a9573dcd6f848a95d4ce50d149" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0160.json.bytes | 8693 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0160.json.sha256 | "128fef19b5b82a0ec67c5c877c78403a5d97313e0fb70fd831f22c59486d512b" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0176.json.bytes | 6991 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0176.json.sha256 | "b3504f79dfd2a0c0a32ea800dd10206ac26aaad238591e13e0ab6454b6cda421" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0192.json.bytes | 8207 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0192.json.sha256 | "63dd8ca20311b80ecccf15a9bb754a768d5469e59dc4f3e09b57a9466f96eb80" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0208.json.bytes | 8589 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0208.json.sha256 | "bc6cbcb3bb9e517ecf39d495d496ccfd6c7de8350045092e5828ae5170ff5201" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0224.json.bytes | 7165 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0224.json.sha256 | "3449a92bf375b77419ef67324ad4f701a67eef700457d8eced601a1deb5301ba" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0240.json.bytes | 8405 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0240.json.sha256 | "52f5801b7425b7ecf9e2fd18492945123671eba10c8b7722d941bf3edbb5f6d4" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0256.json.bytes | 8316 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0256.json.sha256 | "415428a019785da1c9a40f6503ef6fdd4fca319a364dd28dadef7e0871d70a74" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0272.json.bytes | 8521 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0272.json.sha256 | "89100ca68b11e697b9dc48979af74b3dd522fc8b09f000620d8f14c16f8e94bd" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0288.json.bytes | 7188 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0288.json.sha256 | "714ea97668dada7e8bde51ec34f879b12023a2e2a6c53149e1b4bd9da21e4683" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0304.json.bytes | 8203 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0304.json.sha256 | "b7fd5116f8e05a9d4c56d3a122bff69ddab7d27234a594656a4ea5c97f87df1a" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0320.json.bytes | 8703 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0320.json.sha256 | "35b36f1723df1d188ee8b5b7fd0b75000b6be929693aa1623b68ad39e5b2cf08" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0336.json.bytes | 7180 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0336.json.sha256 | "c2f3a82728b7e5a7b3ae5b769f5e2f9c83fcc226a4cf11169b5fcc6646156e26" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0352.json.bytes | 8220 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0352.json.sha256 | "4d7438ed4818240d3576a58ab5cfa2171a8cfea11a218df53f4399d5639717d5" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0368.json.bytes | 8265 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0368.json.sha256 | "5d18f60356e9bf9ae32778c43b6e819338a64318056a1ae6591176151b19b701" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0384.json.bytes | 7097 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0384.json.sha256 | "a9495bf0dc6fed2440becae11cfac64faf0185987b056927aa587867c1e62875" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0400.json.bytes | 8206 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0400.json.sha256 | "e535dac1d0097de6307b6899945c1cf6431464928a4cbbd6ec8378808b3cdfcd" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0416.json.bytes | 8268 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0416.json.sha256 | "3cffbb6d77ba5ab91d46a93c444d0eb82d0f97991f193901f909b7a897272666" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0432.json.bytes | 7182 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0432.json.sha256 | "d5f136d88e4da0df0771da4ed82248b9fff578c57b35befecb79e2f59cf899af" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0448.json.bytes | 8138 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0448.json.sha256 | "ec26c3bca7331ef9f9c7580f431f4dca384c46f43f9a90074b881b85f46a1682" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0464.json.bytes | 8438 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0464.json.sha256 | "6d43295be0d997266234f58013b0f9f8b06ab26510093795a4ef3a9c74468aa9" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0480.json.bytes | 7095 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0480.json.sha256 | "829b06b9f76f2431b5845a07571c91f770c8e98969c0102214a912881a2b574e" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0496.json.bytes | 8140 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/0496.json.sha256 | "bad7f1d13abdf8c4fce818f5a89e0c2e9a98bd23b1bbcd2218ca27bc1d9b81e4" |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/result.json.bytes | 182522 |
| files.reports/phase6/conditional-prefix-mask-20261006/transfer/retention/outcome_EOS_only/result.json.sha256 | "3256b54c76130ed6a752c9f6151f4b2e84aa9436c6c01c68ecaea927c880174f" |
| raw_bytes | 6247536 |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_proposal.json — defined_not_implemented_not_launched</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_proposal.json) ／ SHA256: `623c059d986b585df5bd51114eeab73473a285f6f0b7856edff967b47f45e54d` ／ 6,313 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_not_implemented_not_launched" |
| reason | "Fixed L2 improved Web loss but not all generation guards; both new CE and L2 outputs reproduce conditional light/person/record phrasing on unrelated natural prefixes. Previous positive-weight/ranking/anchor/KL comparisons still learned hard CE on those setup tokens. This tests target selection, not another parameter coefficient or source variant." |
| selected_shared_checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323185.pt" |
| selected_shared_checkpoint.sha256 | "ad4747898bc6492e1165edee6b870b09c8be9be944e03a9e4450fde406cb3f34" |
| first_original_conditional_update | 323190 |
| shared_update | 323185 |
| original_control_notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source_order_condition_notes.json" |
| original_control_notes.sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| accepted_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006" |
| accepted_source.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| source_summary.documents | 2048 |
| source_summary.EOS_positions | 2048 |
| remaining_reference_teacher_quotas.web | 0 |
| remaining_reference_teacher_quotas.story | 0 |
| remaining_reference_teacher_quotas.ordinary_textbook | 159637 |
| remaining_reference_teacher_quotas.conditional_textbook | 10000000 |
| KL_teacher | 0 |
| new_source_documents | 0 |
| new_tokenizer | 0 |
| CPU_preparation_ceiling_seconds | 30 |
| probe_GPU_ceiling_seconds | 120 |
| total_new_GPU_ceiling_seconds | 600 |
| failure | "End this single target-mask comparison after failure; no prefix/outcome/EOS weight, source, mask position, checkpoint, input budget, ratio or decoder sweep to rescue it." |
| limits | "Hypothesis chosen after the observed failure. Template repetition and one selected suffix do not prove the sole cause of quality issues, source-wide quality or a model capacity ceiling. Masking also changes hard-teacher count and EOS fraction; hold physical input fixed and label the changed budgets." |
| completion | "Actual finite suffix/matched original reference input ledger/full evaluation/all80 review/decision/UI/commit. Only a qualified pilot allows independent learned recipe seed/full dev/protected test/adoption." |
| scientific_teacher_tokens_so_far | 0 |
| GPU_seconds_so_far | 0 |
| optimizer_updates_so_far | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_reference_input.json — all318_original_reference_inputs_targets_source_cursors_match</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_reference_input.json) ／ SHA256: `863f7cc8a0d25de94b6d4a280beced4f8dad931f5e28ed59a1aabf5975f0b668` ／ 416,371 bytes

| 原キー | 保存値 |
|---|---|
| status | "all318_original_reference_inputs_targets_source_cursors_match" |
| original_reference_suffix_teacher_tokens | 10159637 |
| actual_masked_suffix_teacher_tokens | 1801392 |
| original_reference_token_digest | "c5731598e03dc91f7936673de06845eb53faf096030791578799fc99201f5c6f" |
| actual_source_accounting.teachers.web | 0 |
| actual_source_accounting.teachers.story | 0 |
| actual_source_accounting.teachers.ordinary_textbook | 159637 |
| actual_source_accounting.teachers.conditional_textbook | 1641755 |
| actual_source_accounting.eos.web | 0 |
| actual_source_accounting.eos.story | 0 |
| actual_source_accounting.eos.ordinary_textbook | 1202 |
| actual_source_accounting.eos.conditional_textbook | 234328 |
| actual_source_accounting.body_bytes.web | 0 |
| actual_source_accounting.body_bytes.story | 0 |
| actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| terminal_reference_sampler.kind | "same-streams-staged-source-order-v1" |
| terminal_reference_sampler.goals.web | 75000000 |
| terminal_reference_sampler.goals.story | 5000000 |
| terminal_reference_sampler.goals.ordinary_textbook | 10000000 |
| terminal_reference_sampler.goals.conditional_textbook | 10000000 |
| terminal_reference_sampler.context | 1024 |
| terminal_reference_sampler.seed | 42 |
| terminal_reference_sampler.position | 3068 |
| terminal_reference_sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| terminal_reference_sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| terminal_reference_sampler.streams.web.sampler.seed | 42 |
| terminal_reference_sampler.streams.web.sampler.epoch | 0 |
| terminal_reference_sampler.streams.web.sampler.position | 10327341 |
| terminal_reference_sampler.streams.web.sampler.context | 1024 |
| terminal_reference_sampler.streams.web.sampler.blocks | 11939276 |
| terminal_reference_sampler.streams.story.seed | 42 |
| terminal_reference_sampler.streams.story.genre | "story" |
| terminal_reference_sampler.streams.story.documents | 761448 |
| terminal_reference_sampler.streams.story.epoch | 0 |
| terminal_reference_sampler.streams.story.document_position | 38243 |
| terminal_reference_sampler.streams.story.token_offset | 87 |
| terminal_reference_sampler.streams.ordinary_textbook.seed | 42 |
| terminal_reference_sampler.streams.ordinary_textbook.genre | "textbook" |
| terminal_reference_sampler.streams.ordinary_textbook.documents | 2942232 |
| terminal_reference_sampler.streams.ordinary_textbook.epoch | 0 |
| terminal_reference_sampler.streams.ordinary_textbook.document_position | 74189 |
| terminal_reference_sampler.streams.ordinary_textbook.token_offset | 77 |
| terminal_reference_sampler.streams.conditional_textbook.seed | 42 |
| terminal_reference_sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| terminal_reference_sampler.streams.conditional_textbook.epoch | 114 |
| terminal_reference_sampler.streams.conditional_textbook.document_position | 871 |
| terminal_reference_sampler.streams.conditional_textbook.token_offset | 23 |
| terminal_reference_sampler.source_teachers.web | 75000000 |
| terminal_reference_sampler.source_teachers.story | 5000000 |
| terminal_reference_sampler.source_teachers.ordinary_textbook | 10000000 |
| terminal_reference_sampler.source_teachers.conditional_textbook | 10000000 |
| terminal_reference_sampler.source_eos.web | 159170 |
| terminal_reference_sampler.source_eos.story | 38240 |
| terminal_reference_sampler.source_eos.ordinary_textbook | 74183 |
| terminal_reference_sampler.source_eos.conditional_textbook | 234328 |
| terminal_reference_sampler.source_tokens.web | 75183104 |
| terminal_reference_sampler.source_tokens.story | 5039104 |
| terminal_reference_sampler.source_tokens.ordinary_textbook | 10075136 |
| terminal_reference_sampler.source_tokens.conditional_textbook | 10234880 |
| terminal_reference_sampler.source_body_bytes.web | 292149840 |
| terminal_reference_sampler.source_body_bytes.story | 20452979 |
| terminal_reference_sampler.source_body_bytes.ordinary_textbook | 42739471 |
| terminal_reference_sampler.source_body_bytes.conditional_textbook | 37865985 |
| terminal_reference_sampler.source_focus_teachers.web | 0 |
| terminal_reference_sampler.source_focus_teachers.story | 0 |
| terminal_reference_sampler.source_focus_teachers.ordinary_textbook | 0 |
| terminal_reference_sampler.source_focus_teachers.conditional_textbook | 1407427 |
| terminal_reference_sampler.source_order | ["web", "story", "ordinary_textbook", "conditional_textbook"] |
| physical_input_tokens | 10420224 |
| masked_teacher_budget_matches_control | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/conditional_prefix_mask_review.json — rejected_single_prefix_mask_comparison</summary>

[原記録](../../reports/phase6/conditional_prefix_mask_review.json) ／ SHA256: `f6abb4d5ebc9f78a36c7b6e34e9f478fb2f527593f5740018cc05651eabcd574` ／ 4,173 bytes

| 原キー | 保存値 |
|---|---|
| status | "rejected_single_prefix_mask_comparison" |
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
| summaries.outcome_EOS_only.BPB | 1.0868123573684936 |
| summaries.outcome_EOS_only.rates.outputs | 80 |
| summaries.outcome_EOS_only.rates.eos | 79 |
| summaries.outcome_EOS_only.rates.repetition | 1 |
| summaries.outcome_EOS_only.rates.unicode_failure | 0 |
| summaries.outcome_EOS_only.rates.role_leak | 0 |
| summaries.outcome_EOS_only.rates.empty | 0 |
| summaries.outcome_EOS_only.grammar2 | 72 |
| summaries.outcome_EOS_only.relevance2 | 53 |
| summaries.outcome_EOS_only.coherent | 35 |
| summaries.outcome_EOS_only.appropriate | 54 |
| summaries.outcome_EOS_only.notes_sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| summaries.outcome_EOS_only.generation_sha256 | "dd966fb8ca316e9f51ee1395b8902fccb4845f43fb940aa09a35c7ee7fd08c5a" |
| summaries.outcome_EOS_only.Japanese.semantics | 0.6145833333333334 |
| summaries.outcome_EOS_only.Japanese.jblimp | 0.7583081570996979 |
| summaries.outcome_EOS_only.Japanese.jcqa | 0.291331546023235 |
| accounting.completed_updates | 318 |
| accounting.new_actual_hard_teachers | 1801392 |
| accounting.physical_input_tokens | 10420224 |
| accounting.reference_input_teachers | 10159637 |
| accounting.actual_source_accounting.teachers.web | 0 |
| accounting.actual_source_accounting.teachers.story | 0 |
| accounting.actual_source_accounting.teachers.ordinary_textbook | 159637 |
| accounting.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.actual_source_accounting.eos.web | 0 |
| accounting.actual_source_accounting.eos.story | 0 |
| accounting.actual_source_accounting.eos.ordinary_textbook | 1202 |
| accounting.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.actual_source_accounting.body_bytes.web | 0 |
| accounting.actual_source_accounting.body_bytes.story | 0 |
| accounting.actual_source_accounting.body_bytes.ordinary_textbook | 680306 |
| accounting.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| accounting.all_original_reference_input_and_cursor_checks | true |
| accounting.matched_teacher_budget | false |
| relative_to_original_strong_staged.checks.coherence_gain_at_least8 | true |
| relative_to_original_strong_staged.checks.paired_CI_lower_above0 | true |
| relative_to_original_strong_staged.checks.EOS_nonworsening | true |
| relative_to_original_strong_staged.checks.repetition_nonworsening | true |
| relative_to_original_strong_staged.checks.no_empty_role_unicode | true |
| relative_to_original_strong_staged.checks.BPB_gate | true |
| relative_to_original_strong_staged.checks.appropriate_completion_not_punctuation | true |
| relative_to_original_strong_staged.passed | true |
| absolute_and_historical_guards.EOS_at_least8_more | true |
| absolute_and_historical_guards.repetition_no_worse | true |
| absolute_and_historical_guards.no_empty_role_unicode | true |
| absolute_and_historical_guards.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation | false |
| actual_science_GPU_seconds | 50.63884665700607 |
| own_probe_GPU_seconds | 17.082726756983902 |
| matched_teacher_budget | false |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Masking changes hard teacher count and EOS target fraction, and the hypothesis follows observed failures. One suffix/nonblind80 does not isolate amount, prove the sole root cause, certify human judgement or a model capacity ceiling." |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/body.json) ／ SHA256: `f99de04f3e4bb62fc18c49c8e2c6297bd07f3b47c655f23ccf632b6b7cd964bf` ／ 69,913 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 323411.1250305176 |
| body.eos_nll | 517.7313129939139 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9884094570544709 |
| body.seconds | 1.2839610580122098 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/generation.json) ／ SHA256: `f90cd1667c20f38eb2ddae5dfafcba6a19a245db946f6413c4f147a009a2f04b` ／ 99,822 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/jblimp.json) ／ SHA256: `d23a1f4805c010e249b4ba1c0b14152fc1acebff99abf318321c198db6693b5b` ／ 341,173 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7522658610271903 |
| summary.primary.accuracy.ci95 | [0.7069486404833837, 0.797583081570997] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7522658610271903 |
| summary.per_token_secondary.accuracy.point | 0.7220543806646526 |
| summary.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| summary.per_token_secondary.macro_f1 | 0.4192982456140351 |
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
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/jcqa.json) ／ SHA256: `8b06c7526d73c92630875450feea2807b8b2d536702aa97e26984b722842385c` ／ 1,644,265 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.33958891867739055 |
| summary.primary.accuracy.ci95 | [0.3118856121537087, 0.3672922252010724] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.33958891867739055 |
| summary.per_token_secondary.accuracy.point | 0.32082216264521896 |
| summary.per_token_secondary.accuracy.ci95 | [0.2931188561215371, 0.3485254691689008] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.32082216264521896 |
| summary.per_token_secondary.macro_f1 | 0.3202529966325722 |
| summary.per_token_secondary.mcc | 0.15168655619820284 |
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
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/result.json) ／ SHA256: `84c7eeaa4197640b4d06ae5996f82af9552268214ec16054e218ef8f36f7799e` ／ 198,004 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus." |
| binding.ranking_policy.families_per_update | 2 |
| binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| binding.KL_policy.every_completed_update | 1 |
| binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 323411.1250305176 |
| body.eos_nll | 517.7313129939139 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9884094570544709 |
| body.seconds | 1.2839610580122098 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 41 |
| greedy_rates.repetition | 21 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.59375 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.546875, 0.640625] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.59375 |
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
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.5882624392627378 |
| diagnostics.semantics.per_token_secondary.mcc | 0.17732400774015752 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7069486404833837, 0.797583081570997] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.3118856121537087, 0.3672922252010724] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32082216264521896 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2931188561215371, 0.3485254691689008] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32082216264521896 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3202529966325722 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.15168655619820284 |
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
| diagnostics.semantic_both_contexts.correct | 21 |
| memory.maximum_observed_allocated_bytes | 348777472 |
| memory.maximum_observed_reserved_bytes | 12694061056 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/evaluation/context_outcome_ranking/evaluation/semantics.json) ／ SHA256: `9d17316f1a7ee48c2f9d5eb6593cab3292f0a9b39e697d55bc3c3245873582fc` ／ 206,014 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.59375 |
| summary.primary.accuracy.ci95 | [0.546875, 0.640625] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.59375 |
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
| summary.per_token_secondary.macro_f1 | 0.5882624392627378 |
| summary.per_token_secondary.mcc | 0.17732400774015752 |
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
<summary>reports/phase6/context-prior-diagnostic-20261006/bridge-prepared.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/bridge-prepared.json) ／ SHA256: `4e9c11d18395b03aeeb8a9ac7caec86f8ef6f59ca598ca00bf14bac447f85823` ／ 930,998 bytes

| 原キー | 保存値 |
|---|---|
| secondary | ["mean_token_log_likelihood", "mean_byte_log_likelihood"] |
| label_scope | "Logical consequences of declared local states. Device settings are definitions, not external fact claims. These source-transfer probes are separate from originaldev/test." |

</details>

<details>
<summary>reports/phase6/context-prior-diagnostic-20261006/conditional_KL-scores.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/conditional_KL-scores.json) ／ SHA256: `5702df10bb43e27848538bfed71fafc767f416f7a90d53ba20e8b6b285b6783e` ／ 1,295,251 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/eos_decoupled_web_kl/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
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
<summary>reports/phase6/context-prior-diagnostic-20261006/gold_body_replay-scores.json — None</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/gold_body_replay-scores.json) ／ SHA256: `3b3ba615cbfaf33af1c2cf575124e52264ddb8941435d8db8c395a15cebe4d88` ／ 1,293,366 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/hard-body-web-replay-comparison-20261006/hard_body_web_replay/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "c03d1d4a0071af756bc39591e0e457daac411e72c847437f8a1d6ba674e99235" |
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
<summary>reports/phase6/context-prior-diagnostic-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/context-prior-diagnostic-20261006/job.json) ／ SHA256: `c2023f584b39553fe56c54f3211e2a686c98b949e79f5b1464d124076bbdaea7` ／ 2,229 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| CPU_budget_seconds | 180 |
| CPU_elapsed_seconds | 16.773451183980796 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| source_sha256.tests/test_context_prior_analysis.py | "c7e8f06ff97aa140aca29a715c4ddc0ea14ebd000904ed14a57a4d83ebe3098f" |
| source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |

</details>
