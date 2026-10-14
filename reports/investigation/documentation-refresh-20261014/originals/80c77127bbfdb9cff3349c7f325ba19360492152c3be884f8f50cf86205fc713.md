# 実行管理・後続準備・その他 — 18/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/progress-result.json) ／ SHA256: `f53b033dde8bcd5b9ac5d8e77f22ae9df1777323c88b1a2043026c2f222bde52` ／ 625,431 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| checkpoint.binding.config_sha256 | "4f91703748a2f3f83b40ef0e291266537cc494dac0b65359c3b8eec1d86c22e9" |
| checkpoint.binding.arm | "interleaved_outcome_EOS" |
| checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoint.binding.study_kind | "original_mixed_order_fixed_conditional_outcome_EOS_v1" |
| checkpoint.binding.teacher_goals.web | 75000000 |
| checkpoint.binding.teacher_goals.story | 5000000 |
| checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoint.binding.target_rule | "conditional outcome+EOS only; original reference quotas stop input" |
| checkpoint.binding.optimizer_policy | "inherit" |
| checkpoint.binding.peak_lr | 1e-05 |
| checkpoint.updates | 3068 |
| checkpoint.additional_supervised_tokens | 91641755 |
| checkpoint.additional_input_tokens | 100532224 |
| checkpoint.actual_body_bytes | 361357103 |
| checkpoint.reference_suffix_teacher_tokens | 100000000 |
| checkpoint.actual_source_accounting.teachers.web | 75000000 |
| checkpoint.actual_source_accounting.teachers.story | 5000000 |
| checkpoint.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| checkpoint.actual_source_accounting.eos.web | 159170 |
| checkpoint.actual_source_accounting.eos.story | 38240 |
| checkpoint.actual_source_accounting.eos.ordinary_textbook | 74183 |
| checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| checkpoint.actual_source_accounting.body_bytes.web | 292149840 |
| checkpoint.actual_source_accounting.body_bytes.story | 20452979 |
| checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| checkpoint.actual_source_accounting.focus.web | 0 |
| checkpoint.actual_source_accounting.focus.story | 0 |
| checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.kind | "original-Web-retention-short-source-quotas-v1" |
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
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 159170 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 38240 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 74183 |
| checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 292149840 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 20452979 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 42739471 |
| checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "original-Web-retention-short-source-quotas-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10253920 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| checkpoint.sampler.prefix_mask_accounting.reference_policy | "interleaved" |
| checkpoint.token_digest | "d5e3ff03c09fd0e95a1a2b3e2160e24b02f007e10b564a2385c4aaed4c97dac4" |
| checkpoint.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| checkpoint.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| checkpoint.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| checkpoint.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| checkpoint.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| checkpoint.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| checkpoint.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| checkpoint.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| checkpoint.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| checkpoint.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| checkpoint.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| checkpoint.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| checkpoint.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| checkpoint.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| checkpoint.training_seconds | 168.67648764658952 |
| evaluation.binding.teacher_goals.web | 75000000 |
| evaluation.binding.teacher_goals.story | 5000000 |
| evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluation.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| evaluation.body.documents | 256 |
| evaluation.body.limit_documents | 256 |
| evaluation.body.body_nll | 318400.7202720642 |
| evaluation.body.eos_nll | 583.9714539796114 |
| evaluation.body.body_bytes | 472055 |
| evaluation.body.body_tokens | 122343 |
| evaluation.body.bpb | 0.9730966521951491 |
| evaluation.body.seconds | 1.621353958005784 |
| evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluation.generation.max_new_tokens | 64 |
| evaluation.greedy_rates.eos | 22 |
| evaluation.greedy_rates.repetition | 35 |
| evaluation.greedy_rates.unicode_failure | 0 |
| evaluation.greedy_rates.role_leak | 0 |
| evaluation.greedy_rates.empty | 0 |
| evaluation.diagnostics.semantics.primary.accuracy.point | 0.6145833333333334 |
| evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5729166666666666, 0.65625] |
| evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6145833333333334 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.59375 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5572916666666666, 0.6302083333333334] |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.59375 |
| evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.592156862745098 |
| evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.18898223650461363 |
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
| evaluation.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7280966767371602, 0.8157099697885196] |
| evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7129909365558912 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6646525679758308, 0.7643504531722054] |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7129909365558912 |
| evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41622574955908287 |
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
| evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| evaluation.diagnostics.jcqa.primary.accuracy.point | 0.353887399463807 |
| evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.3270554066130474, 0.3806970509383378] |
| evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.353887399463807 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3109919571045576 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28328865058087577, 0.3378016085790885] |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3109919571045576 |
| evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3101668649340549 |
| evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.13894601295959533 |
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
| evaluation.diagnostics.semantic_both_contexts.correct | 22 |
| evaluation.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluation.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluation.protected_test_used | false |
| bridge.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| bridge.checks.weights_unchanged | true |
| bridge.checks.no_gradients | true |
| bridge.checks.eval_mode | true |
| bridge.checks.RNG_restored | true |
| bridge.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62109375 |
| bridge.summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.765625 |
| bridge.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 35 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 10 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62109375 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| bridge.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 37 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 26 |
| bridge.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 7 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| bridge.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 49 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| bridge.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 39 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| bridge.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 10 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| bridge.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 40 |
| bridge.optimizer_updates | 0 |
| bridge.scientific_teacher_tokens | 0 |
| bridge.protected_test_used | false |
| bridge.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| retention.checks.weights_unchanged | true |
| retention.checks.no_gradients | true |
| retention.checks.eval_mode | true |
| retention.checks.RNG_restored | true |
| retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.640625 |
| retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 41 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 80 |
| retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.71875 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 31 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.64453125 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 42 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 81 |
| retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 29 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| retention.optimizer_updates | 0 |
| retention.scientific_teacher_tokens | 0 |
| retention.protected_test_used | false |
| retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/review.json — rejected_single_order_target_fourth_cell</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/review.json) ／ SHA256: `93d031d41c2af61457cd8ee7271b7b9fc757a484f8bb747a45d8fc56e5a37597` ／ 10,117 bytes

| 原キー | 保存値 |
|---|---|
| status | "rejected_single_order_target_fourth_cell" |
| summaries.masked_mixed.BPB | 0.9730966521951491 |
| summaries.masked_mixed.rates.eos | 22 |
| summaries.masked_mixed.rates.repetition | 35 |
| summaries.masked_mixed.rates.unicode_failure | 0 |
| summaries.masked_mixed.rates.role_leak | 0 |
| summaries.masked_mixed.rates.empty | 0 |
| summaries.masked_mixed.grammar2 | 31 |
| summaries.masked_mixed.relevance2 | 64 |
| summaries.masked_mixed.coherent | 11 |
| summaries.masked_mixed.appropriate | 12 |
| summaries.masked_mixed.notes_sha256 | "dc9dfd4e3861267fa9b0c8b2df2cb8865aece002b6f6f2863b1e27c9d6760ca4" |
| summaries.full_mixed.BPB | 0.9748195810331843 |
| summaries.full_mixed.rates.eos | 30 |
| summaries.full_mixed.rates.repetition | 31 |
| summaries.full_mixed.rates.unicode_failure | 0 |
| summaries.full_mixed.rates.role_leak | 0 |
| summaries.full_mixed.rates.empty | 0 |
| summaries.full_mixed.grammar2 | 69 |
| summaries.full_mixed.relevance2 | 51 |
| summaries.full_mixed.coherent | 4 |
| summaries.full_mixed.appropriate | 18 |
| summaries.full_mixed.notes_sha256 | "12ff1008589c4f7de7439e99dd4e8d53aea429b2c164c898b4866b3a10431934" |
| summaries.full_staged.BPB | 1.1336128657420816 |
| summaries.full_staged.rates.eos | 76 |
| summaries.full_staged.rates.repetition | 2 |
| summaries.full_staged.rates.unicode_failure | 0 |
| summaries.full_staged.rates.role_leak | 0 |
| summaries.full_staged.rates.empty | 0 |
| summaries.full_staged.grammar2 | 65 |
| summaries.full_staged.relevance2 | 39 |
| summaries.full_staged.coherent | 23 |
| summaries.full_staged.appropriate | 26 |
| summaries.full_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| summaries.masked_staged.BPB | 1.0868123573684936 |
| summaries.masked_staged.rates.eos | 79 |
| summaries.masked_staged.rates.repetition | 1 |
| summaries.masked_staged.rates.unicode_failure | 0 |
| summaries.masked_staged.rates.role_leak | 0 |
| summaries.masked_staged.rates.empty | 0 |
| summaries.masked_staged.grammar2 | 72 |
| summaries.masked_staged.relevance2 | 53 |
| summaries.masked_staged.coherent | 35 |
| summaries.masked_staged.appropriate | 54 |
| summaries.masked_staged.notes_sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| accounting.updates | 3068 |
| accounting.actual_new_hard_teachers | 91641755 |
| accounting.original_nominal_reference_teachers | 100000000 |
| accounting.physical_input_tokens | 100532224 |
| accounting.actual_source_accounting.teachers.web | 75000000 |
| accounting.actual_source_accounting.teachers.story | 5000000 |
| accounting.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| accounting.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.actual_source_accounting.eos.web | 159170 |
| accounting.actual_source_accounting.eos.story | 38240 |
| accounting.actual_source_accounting.eos.ordinary_textbook | 74183 |
| accounting.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.actual_source_accounting.body_bytes.web | 292149840 |
| accounting.actual_source_accounting.body_bytes.story | 20452979 |
| accounting.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| accounting.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| relative_to_strong_staged.checks.coherence_gain_at_least8 | false |
| relative_to_strong_staged.checks.paired_CI_lower_above0 | false |
| relative_to_strong_staged.checks.EOS_nonworsening | false |
| relative_to_strong_staged.checks.repetition_nonworsening | false |
| relative_to_strong_staged.checks.no_empty_role_unicode | true |
| relative_to_strong_staged.checks.BPB_gate | true |
| relative_to_strong_staged.checks.appropriate_completion_not_punctuation | true |
| relative_to_strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | true |
| observed_masked_staged_comparison.checks.coherence_gain_at_least8 | false |
| observed_masked_staged_comparison.checks.paired_CI_lower_above0 | false |
| observed_masked_staged_comparison.checks.EOS_nonworsening | false |
| observed_masked_staged_comparison.checks.repetition_nonworsening | false |
| observed_masked_staged_comparison.checks.no_empty_role_unicode | true |
| observed_masked_staged_comparison.checks.BPB_gate | true |
| observed_masked_staged_comparison.checks.appropriate_completion_not_punctuation | true |
| observed_masked_staged_comparison.passed | false |
| four_cell_analysis.contrasts.order_effect_full.body_BPB_change | -0.1587932847088974 |
| four_cell_analysis.contrasts.order_effect_full.body_paired_CI95 | [-0.16429589288877466, -0.15389340970513357] |
| four_cell_analysis.contrasts.order_effect_full.coherence_count_change | -19 |
| four_cell_analysis.contrasts.order_effect_full.coherence_paired_fraction_CI95 | [-0.3375, -0.1375] |
| four_cell_analysis.contrasts.order_effect_masked.body_BPB_change | -0.11371570517334455 |
| four_cell_analysis.contrasts.order_effect_masked.body_paired_CI95 | [-0.11859395003660304, -0.10930360980970213] |
| four_cell_analysis.contrasts.order_effect_masked.coherence_count_change | -24 |
| four_cell_analysis.contrasts.order_effect_masked.coherence_paired_fraction_CI95 | [-0.425, -0.175] |
| four_cell_analysis.contrasts.target_effect_mixed.body_BPB_change | -0.0017229288380352105 |
| four_cell_analysis.contrasts.target_effect_mixed.body_paired_CI95 | [-0.001943490722199282, -0.0015048457941451575] |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_count_change | 7 |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_paired_fraction_CI95 | [0.0, 0.1875] |
| four_cell_analysis.contrasts.target_effect_staged.body_BPB_change | -0.04680050837358805 |
| four_cell_analysis.contrasts.target_effect_staged.body_paired_CI95 | [-0.04899283347501657, -0.044773117366030894] |
| four_cell_analysis.contrasts.target_effect_staged.coherence_count_change | 12 |
| four_cell_analysis.contrasts.target_effect_staged.coherence_paired_fraction_CI95 | [0.025, 0.275] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_BPB_change | 0.045077579535552845 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_paired_CI95 | [0.04310979942910883, 0.047229086453556945] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_count_change | -5 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_paired_fraction_CI95 | [-0.2, 0.0875] |
| four_cell_analysis.body_documents | 256 |
| four_cell_analysis.body_bytes | 472055 |
| four_cell_analysis.limitations | "Descriptive four-cell contrasts; repeated dev use/nonblind content/one learned seed/shared prefix. Target factor also changes hard teacher count and EOS fraction; no independent causal or human certification." |
| eligible_for_final_Base_validation | false |
| actual_science_GPU_seconds | 261.29975055900286 |
| own_probe_GPU_seconds | 17.989334398997016 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0000.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0000.json) ／ SHA256: `4fa4798205398bcd1b191c3034fa6ec9fd46f8ab173762161fdc7eec2bb49138` ／ 9,928 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0016.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0016.json) ／ SHA256: `98e0a3746cb91fd081a52250aa3cab22f59f081214a7dad59916d255852e3519` ／ 9,581 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0032.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0032.json) ／ SHA256: `9c3184cfe1418be129bbb9c53766983061f46dc33a3fe62bcad6b2bc2a41e39e` ／ 10,210 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0048.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0048.json) ／ SHA256: `25acea47d0cef2e0a83220adedea8dd3ccfd2829163395f2c33de3dad0cdebda` ／ 9,497 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0064.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0064.json) ／ SHA256: `d38dcf5d84256e89a15b0705339e7c24cf95911592d636ae4fbbddf206b396e9` ／ 10,300 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0080.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0080.json) ／ SHA256: `837378d5e3c20dabe8226a4b5ff4b82a3e0bf4dd898b5852b715ddf6b7be5cb0` ／ 9,699 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0096.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0096.json) ／ SHA256: `45355dca0ee41ad98cb8cbaaea8a6883bb3ef94e22f597f55308b741638b31b2` ／ 9,770 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0112.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0112.json) ／ SHA256: `6c09fc7277997efcda1a3bd53d00650262035dc216479a6428503e35abd3ae28` ／ 10,126 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0128.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0128.json) ／ SHA256: `64965c757d2fe189fe3af10f95bffea55a0bae95732fbd123210f604da9af431` ／ 9,804 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0144.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0144.json) ／ SHA256: `43cc79d74ed8c06250f3fd7f10a6e769b9f9020952180bc12012b2c2f0343a30` ／ 9,859 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0160.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0160.json) ／ SHA256: `c6856048eeed26e53ad60c020eaeb93a711b59f306a5e5cf3f859c2504ba967a` ／ 10,138 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0176.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0176.json) ／ SHA256: `32da9622ffb035533aebec5b01210122e13327360af82966fbd8f14fb48175bc` ／ 9,965 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0192.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0192.json) ／ SHA256: `8c11ee71308c9146450ca3c85307a6fc8cde5a65fdace7885b23ff49449ddf12` ／ 9,864 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0208.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0208.json) ／ SHA256: `5472b7c8376074bf5a7d3e38c7b83320e9b38f2b905dd1e8c76c59808ed46307` ／ 9,635 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0224.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0224.json) ／ SHA256: `145257e3d4a8e8c1763546440ec6a9925e25366aa0dd366d533361ca894702cc` ／ 9,777 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0240.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0240.json) ／ SHA256: `3102219c1a112a82e0f3443d2efbd873aa4a4ccb5195c4066d2c61b0c025e228` ／ 9,608 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0256.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0256.json) ／ SHA256: `314a141f2354889d92b38233b97bc506d37f776b778fc76371b4d669dfd292c8` ／ 9,579 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0272.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0272.json) ／ SHA256: `e1a33c7b0f2678822cf449870fcca3ec4afcfcb1330f5afefc7e9c1ea56cd78c` ／ 9,551 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0288.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0288.json) ／ SHA256: `7c96499464be212f3698518654d4378045a757f088452650699b05a30e3ca0c7` ／ 9,573 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0304.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0304.json) ／ SHA256: `ff40ead6ac7875247481b922bf1b26bf21074f220ba2929808ef1bf5e3a0df32` ／ 9,776 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0320.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0320.json) ／ SHA256: `ef3e81b348ce32eec9291efeb2d5e7df74069f5cec380bb8b8d596b66a0aad6a` ／ 9,276 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0336.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0336.json) ／ SHA256: `6378a69aedbfc661b2fed1adcbd1e53ac873916182fdbae29cf757a9c6e78455` ／ 9,380 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0352.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0352.json) ／ SHA256: `f39f65054e6c7ad5b87fa5b7daf5c2555de74bdef7d8cac0430bf82cfcbec5d0` ／ 9,744 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0368.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0368.json) ／ SHA256: `0ed99cc0833b2ca9c92b6f3c33e4d92d127b18537b2277a9b08a46fd6a15515b` ／ 9,485 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0384.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0384.json) ／ SHA256: `8b9c0a07dc0a894bcb4918efb25a9f919001e295341c1ecb1db84494c5f51869` ／ 9,835 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0400.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0400.json) ／ SHA256: `35a5323cc2c67547e44bb359dbcd83849b079914319edff390d9f1fdceca8da3` ／ 9,492 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0416.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0416.json) ／ SHA256: `83e48bbcfa618b494e898e0779aa56d6b5224a0740da3bcd0459516b5d5e86dc` ／ 9,847 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0432.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0432.json) ／ SHA256: `06e52820c78e9ea10979547f434441619e48e72f89ccf42717b3423dabde2a39` ／ 9,305 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0448.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0448.json) ／ SHA256: `bddb6ca930db5bf7028fccd413d2aef742d41c39879862c7805a04b4eaaaea59` ／ 9,548 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0464.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0464.json) ／ SHA256: `648d08f833d07ddcb816c9e54482009cbbcd27db387db132346a79b1c9c045c1` ／ 9,376 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0480.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0480.json) ／ SHA256: `ebc588a875b246a568b6e7467b8eaac2b150ed7d8927ab7b57787dfb378bb3ae` ／ 9,407 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0496.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0496.json) ／ SHA256: `443ccf3250695cd754ac31609a72e1a2edafe9c3ced868331f40250dbd1f2971` ／ 9,481 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/result.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/result.json) ／ SHA256: `70f279315656ac609f72d807e74f8a044a2f7a603acf20fb8430f42cb2c902d2` ／ 186,387 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62109375 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 45 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.765625 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 35 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 10 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.62109375 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 71 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.78125 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 37 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 26 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 7 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 45 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 43 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.63671875 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 49 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.796875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 39 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 24 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4765625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 10 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 41 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 40 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0000.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0000.json) ／ SHA256: `bf1d7770073ed4f14a35c4d35bc511a6740b915c2f1bead414a2827c35ae8eac` ／ 7,948 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0016.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0016.json) ／ SHA256: `1e46faa69b6cf675dc710b33bd6678df532524d51f0f244e43177f05a44c0ca9` ／ 8,285 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0032.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0032.json) ／ SHA256: `a6addc43b91ecfb69ddd6b6bd6c78844e4649183d12b5fe2af7fee461bd760b3` ／ 6,958 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0048.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0048.json) ／ SHA256: `37b5167707e7414ed0f45f026abeef7979e3971cf484efd6a4c048f2600025f3` ／ 8,141 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0064.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0064.json) ／ SHA256: `6cdb1e0464cf7b6be159bcaaacf78ad3283c215a61e112e76e55f50ac6a25ce4` ／ 8,482 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0080.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0080.json) ／ SHA256: `6d7ce301ecf8776296e1c4944c34a56edffbcf67dd08072284a2d0fd033f33bf` ／ 7,051 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0096.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0096.json) ／ SHA256: `7a50296c42bc4e02411e28105732e0f7087dde52729b074452ad7f4552e1241d` ／ 8,045 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0112.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0112.json) ／ SHA256: `df841f407d41fbfc8e49d8ecdd6e6929e1753b44af3134ec329003ee695340f5` ／ 8,236 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0128.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0128.json) ／ SHA256: `56d400ef3f5538d5537ea02fdac368f1664cbe6e8fc9ce94f5a189698e94013c` ／ 7,063 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0144.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0144.json) ／ SHA256: `8ea9e670fcebaf20372cd6d41ae45dca0bcf67d87b49980425aa51f7cae7a0ec` ／ 8,142 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0160.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0160.json) ／ SHA256: `9cfa5e40a125721bdd067a5636ba6111016315e0191656a27b24a4e7e7ca7aa1` ／ 8,582 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0176.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0176.json) ／ SHA256: `0e08ce7c7501fed7105df5385b6056f451c51bc0e03891b05c8c1b906728b205` ／ 6,893 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0192.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0192.json) ／ SHA256: `4dccb4f950c8c776bcf6c7e5b42c5cb0a9c9a7a6a0361779746f0317c13f9846` ／ 8,147 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0208.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0208.json) ／ SHA256: `12c76263f76f2955e679aa5ad3c584ba11fb3640109df1d1036f8aedb87966de` ／ 8,471 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0224.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0224.json) ／ SHA256: `d2e95b94a6899f2df3e0ced29d4efa1f84995525714f175ff34a62581b8c25f5` ／ 7,067 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0240.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0240.json) ／ SHA256: `b0738b7cadadf3bbacc1a99dc1bbbf94ee45e5e49d85d4b55d794c8255e4b7ed` ／ 8,328 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0256.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0256.json) ／ SHA256: `61b6c1e6dde540f09d8ca6c84d524ca913170ea440753e7d95b36beb1ac0e1ee` ／ 8,196 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0272.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0272.json) ／ SHA256: `a8a00cc7ac9d8dda3484b95d84fb656041ae3bfc0db3c51ca48a3a5b86310cc9` ／ 8,396 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0288.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0288.json) ／ SHA256: `a6cb9107493be9d67bcd8efd9f032f028800c681dada623be739f6c5e6ce3a94` ／ 7,071 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0304.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0304.json) ／ SHA256: `39e5e87487bb9db23694d1fe3f1439d25fb4206564361d15866b041abf6a55f9` ／ 8,139 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0320.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0320.json) ／ SHA256: `f070fd09881f232c6e68be1fda90c8525ebc1687fc1c0083d01bcbfe56857e8e` ／ 8,554 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0336.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0336.json) ／ SHA256: `25aa17e69791aef46ca9a714f14e0dd1e6caff9a0cd679e5452a6e289a8cace4` ／ 7,079 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0352.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0352.json) ／ SHA256: `24e06676547066245cf4d491cd9df4fb054ce41211070919da1d6e9c2c2c115b` ／ 8,128 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0368.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0368.json) ／ SHA256: `29aa54394f28c9601c0b4b6870f5682c6cd750e5eb0a0e2d57d1d16edd43e65b` ／ 8,113 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0384.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0384.json) ／ SHA256: `facde7b75d639bf73555628971df45933aa9863aa571cc531408f8531faef03f` ／ 6,992 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0400.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0400.json) ／ SHA256: `857da1f2266734c24962d371092ab27d8642990a36044e3cdf5eefedea9a9094` ／ 8,127 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0416.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0416.json) ／ SHA256: `db983e47b6de3c538ea07e5207baa69deafc3d55415c8b4d5157b14387fe400e` ／ 8,133 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0432.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0432.json) ／ SHA256: `23327f801f9dbed5d256e27c4a97b1c4a1e1fac854f6e40858bee4504e4ac79f` ／ 7,079 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0448.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0448.json) ／ SHA256: `55447ffd783ebb167c11de726e71d0f80ba8d13a24cd87bc0b84c4b4e43698d3` ／ 8,054 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0464.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0464.json) ／ SHA256: `ecdea037e61c094336961f0b919326b3d3e758af47d4478c3388c10539319c2b` ／ 8,307 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0480.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0480.json) ／ SHA256: `ffb080bcca5db6a9ce077428310383c24133792482588a2aac279f87a4e9a4e7` ／ 6,992 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0496.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0496.json) ／ SHA256: `d505fe1822d499679485464392f5aa8516e419d7c1a901ec0b3fed1b01b0cd08` ／ 8,058 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/result.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/result.json) ／ SHA256: `82a3ba72eb5470df793cdde638e0c90933635ac7d33353e359bcbcbcdcbf3b6f` ／ 183,238 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.640625 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 41 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.7109375 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 30 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 44 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 80 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 106 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.71875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 31 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 30 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.59375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.64453125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 42 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 81 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 106 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 29 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5859375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 52 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-probe-launcher-20261006/launcher.json) ／ SHA256: `1d110a18c740ddb10f221d2b8d1af34e80d7105fb5fcc1034491be849328aa51` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/interleaved-outcome-order-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/interleaved-outcome-order-probe-launcher-20261006/result.json) ／ SHA256: `110d2bda5d964e5d7bb6eff6612b5591c3ccaae50a3b9730307361950f1d8f5d` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_active_job.json — actual_terminal_fourth_cell_rejected</summary>

[原記録](../../reports/phase6/interleaved_outcome_active_job.json) ／ SHA256: `8e61c8dc32f66f412ad954201e6b45e56e569d7dfa49a897d5397d8540aef5f2` ／ 1,330 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_terminal_fourth_cell_rejected" |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 261.29975055900286 |
| actual_job.completed_updates | 3060 |
| actual_job.total_updates | 3068 |
| actual_job.actual_teachers | 91426867 |
| actual_job.reference_teachers | 99765337 |
| actual_job.loss | 2.5054211616516113 |
| completion.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved_outcome_completion.json" |
| completion.sha256 | "a34c30d48ee095f248720cebd91a2d61a07fd68c3058cddd57f0967212ea7d02" |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_completion.json — fourth_cell_complete_rejected_Base_unfinished</summary>

[原記録](../../reports/phase6/interleaved_outcome_completion.json) ／ SHA256: `a34c30d48ee095f248720cebd91a2d61a07fd68c3058cddd57f0967212ea7d02` ／ 20,747 bytes

| 原キー | 保存値 |
|---|---|
| status | "fourth_cell_complete_rejected_Base_unfinished" |
| actual_terminal_job.status | "complete" |
| actual_terminal_job.GPU_elapsed_seconds | 261.29975055900286 |
| actual_terminal_job.completed_updates | 3060 |
| actual_terminal_job.total_updates | 3068 |
| actual_terminal_job.actual_teachers | 91426867 |
| actual_terminal_job.reference_teachers | 99765337 |
| actual_terminal_job.loss | 2.5054211616516113 |
| scientific_teacher_tokens | 91641755 |
| scientific_optimizer_updates | 3068 |
| physical_input_tokens | 100532224 |
| nominal_reference_teachers | 100000000 |
| actual_source_accounting.teachers.web | 75000000 |
| actual_source_accounting.teachers.story | 5000000 |
| actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| actual_source_accounting.teachers.conditional_textbook | 1641755 |
| actual_source_accounting.eos.web | 159170 |
| actual_source_accounting.eos.story | 38240 |
| actual_source_accounting.eos.ordinary_textbook | 74183 |
| actual_source_accounting.eos.conditional_textbook | 234328 |
| actual_source_accounting.body_bytes.web | 292149840 |
| actual_source_accounting.body_bytes.story | 20452979 |
| actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| scientific_checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| scientific_checkpoint.checkpoint_sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| scientific_checkpoint.binding.config_sha256 | "4f91703748a2f3f83b40ef0e291266537cc494dac0b65359c3b8eec1d86c22e9" |
| scientific_checkpoint.binding.arm | "interleaved_outcome_EOS" |
| scientific_checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| scientific_checkpoint.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| scientific_checkpoint.binding.study_kind | "original_mixed_order_fixed_conditional_outcome_EOS_v1" |
| scientific_checkpoint.binding.teacher_goals.web | 75000000 |
| scientific_checkpoint.binding.teacher_goals.story | 5000000 |
| scientific_checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| scientific_checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| scientific_checkpoint.binding.target_rule | "conditional outcome+EOS only; original reference quotas stop input" |
| scientific_checkpoint.binding.optimizer_policy | "inherit" |
| scientific_checkpoint.binding.peak_lr | 1e-05 |
| scientific_checkpoint.updates | 3068 |
| scientific_checkpoint.additional_supervised_tokens | 91641755 |
| scientific_checkpoint.additional_input_tokens | 100532224 |
| scientific_checkpoint.actual_body_bytes | 361357103 |
| scientific_checkpoint.reference_suffix_teacher_tokens | 100000000 |
| scientific_checkpoint.actual_source_accounting.teachers.web | 75000000 |
| scientific_checkpoint.actual_source_accounting.teachers.story | 5000000 |
| scientific_checkpoint.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| scientific_checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| scientific_checkpoint.actual_source_accounting.eos.web | 159170 |
| scientific_checkpoint.actual_source_accounting.eos.story | 38240 |
| scientific_checkpoint.actual_source_accounting.eos.ordinary_textbook | 74183 |
| scientific_checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| scientific_checkpoint.actual_source_accounting.body_bytes.web | 292149840 |
| scientific_checkpoint.actual_source_accounting.body_bytes.story | 20452979 |
| scientific_checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| scientific_checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| scientific_checkpoint.actual_source_accounting.focus.web | 0 |
| scientific_checkpoint.actual_source_accounting.focus.story | 0 |
| scientific_checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| scientific_checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| scientific_checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| scientific_checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| scientific_checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| scientific_checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| scientific_checkpoint.sampler.kind | "original-Web-retention-short-source-quotas-v1" |
| scientific_checkpoint.sampler.goals.web | 75000000 |
| scientific_checkpoint.sampler.goals.story | 5000000 |
| scientific_checkpoint.sampler.goals.ordinary_textbook | 10000000 |
| scientific_checkpoint.sampler.goals.conditional_textbook | 10000000 |
| scientific_checkpoint.sampler.context | 1024 |
| scientific_checkpoint.sampler.seed | 42 |
| scientific_checkpoint.sampler.position | 3068 |
| scientific_checkpoint.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| scientific_checkpoint.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| scientific_checkpoint.sampler.streams.web.sampler.seed | 42 |
| scientific_checkpoint.sampler.streams.web.sampler.epoch | 0 |
| scientific_checkpoint.sampler.streams.web.sampler.position | 10327341 |
| scientific_checkpoint.sampler.streams.web.sampler.context | 1024 |
| scientific_checkpoint.sampler.streams.web.sampler.blocks | 11939276 |
| scientific_checkpoint.sampler.streams.story.seed | 42 |
| scientific_checkpoint.sampler.streams.story.genre | "story" |
| scientific_checkpoint.sampler.streams.story.documents | 761448 |
| scientific_checkpoint.sampler.streams.story.epoch | 0 |
| scientific_checkpoint.sampler.streams.story.document_position | 38243 |
| scientific_checkpoint.sampler.streams.story.token_offset | 87 |
| scientific_checkpoint.sampler.streams.ordinary_textbook.seed | 42 |
| scientific_checkpoint.sampler.streams.ordinary_textbook.genre | "textbook" |
| scientific_checkpoint.sampler.streams.ordinary_textbook.documents | 2942232 |
| scientific_checkpoint.sampler.streams.ordinary_textbook.epoch | 0 |
| scientific_checkpoint.sampler.streams.ordinary_textbook.document_position | 74189 |
| scientific_checkpoint.sampler.streams.ordinary_textbook.token_offset | 77 |
| scientific_checkpoint.sampler.streams.conditional_textbook.seed | 42 |
| scientific_checkpoint.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| scientific_checkpoint.sampler.streams.conditional_textbook.epoch | 114 |
| scientific_checkpoint.sampler.streams.conditional_textbook.document_position | 871 |
| scientific_checkpoint.sampler.streams.conditional_textbook.token_offset | 23 |
| scientific_checkpoint.sampler.source_teachers.web | 75000000 |
| scientific_checkpoint.sampler.source_teachers.story | 5000000 |
| scientific_checkpoint.sampler.source_teachers.ordinary_textbook | 10000000 |
| scientific_checkpoint.sampler.source_teachers.conditional_textbook | 10000000 |
| scientific_checkpoint.sampler.source_eos.web | 159170 |
| scientific_checkpoint.sampler.source_eos.story | 38240 |
| scientific_checkpoint.sampler.source_eos.ordinary_textbook | 74183 |
| scientific_checkpoint.sampler.source_eos.conditional_textbook | 234328 |
| scientific_checkpoint.sampler.source_tokens.web | 75183104 |
| scientific_checkpoint.sampler.source_tokens.story | 5039104 |
| scientific_checkpoint.sampler.source_tokens.ordinary_textbook | 10075136 |
| scientific_checkpoint.sampler.source_tokens.conditional_textbook | 10234880 |
| scientific_checkpoint.sampler.source_body_bytes.web | 292149840 |
| scientific_checkpoint.sampler.source_body_bytes.story | 20452979 |
| scientific_checkpoint.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| scientific_checkpoint.sampler.source_body_bytes.conditional_textbook | 37865985 |
| scientific_checkpoint.sampler.source_focus_teachers.web | 0 |
| scientific_checkpoint.sampler.source_focus_teachers.story | 0 |
| scientific_checkpoint.sampler.source_focus_teachers.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 75000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 5000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 10000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 159170 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 38240 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 74183 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 292149840 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 20452979 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 42739471 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "original-Web-retention-short-source-quotas-v1" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10253920 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| scientific_checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| scientific_checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| scientific_checkpoint.sampler.prefix_mask_accounting.reference_policy | "interleaved" |
| scientific_checkpoint.token_digest | "d5e3ff03c09fd0e95a1a2b3e2160e24b02f007e10b564a2385c4aaed4c97dac4" |
| scientific_checkpoint.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| scientific_checkpoint.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| scientific_checkpoint.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| scientific_checkpoint.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| scientific_checkpoint.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| scientific_checkpoint.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| scientific_checkpoint.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| scientific_checkpoint.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| scientific_checkpoint.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| scientific_checkpoint.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| scientific_checkpoint.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| scientific_checkpoint.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| scientific_checkpoint.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| scientific_checkpoint.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| scientific_checkpoint.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| scientific_checkpoint.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| scientific_checkpoint.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| scientific_checkpoint.training_seconds | 168.67648764658952 |
| new_science_GPU_seconds | 261.29975055900286 |
| own_probe_GPU_seconds | 17.989334398997016 |
| new_all_GPU_seconds | 279.2890849579999 |
| verification_optimizer_updates | 48 |
| verification_teacher_tokens | 1433919 |
| verification_input_tokens | 1572864 |
| previous_related_GPU_seconds_preserved | 2928.6630077910663 |
| related_GPU_seconds | 3207.952092749066 |
| summary.BPB | 0.9730966521951491 |
| summary.rates.eos | 22 |
| summary.rates.repetition | 35 |
| summary.rates.unicode_failure | 0 |
| summary.rates.role_leak | 0 |
| summary.rates.empty | 0 |
| summary.grammar2 | 31 |
| summary.relevance2 | 64 |
| summary.coherent | 11 |
| summary.appropriate | 12 |
| summary.notes_sha256 | "dc9dfd4e3861267fa9b0c8b2df2cb8865aece002b6f6f2863b1e27c9d6760ca4" |
| four_cell_analysis.contrasts.order_effect_full.body_BPB_change | -0.1587932847088974 |
| four_cell_analysis.contrasts.order_effect_full.body_paired_CI95 | [-0.16429589288877466, -0.15389340970513357] |
| four_cell_analysis.contrasts.order_effect_full.coherence_count_change | -19 |
| four_cell_analysis.contrasts.order_effect_full.coherence_paired_fraction_CI95 | [-0.3375, -0.1375] |
| four_cell_analysis.contrasts.order_effect_masked.body_BPB_change | -0.11371570517334455 |
| four_cell_analysis.contrasts.order_effect_masked.body_paired_CI95 | [-0.11859395003660304, -0.10930360980970213] |
| four_cell_analysis.contrasts.order_effect_masked.coherence_count_change | -24 |
| four_cell_analysis.contrasts.order_effect_masked.coherence_paired_fraction_CI95 | [-0.425, -0.175] |
| four_cell_analysis.contrasts.target_effect_mixed.body_BPB_change | -0.0017229288380352105 |
| four_cell_analysis.contrasts.target_effect_mixed.body_paired_CI95 | [-0.001943490722199282, -0.0015048457941451575] |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_count_change | 7 |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_paired_fraction_CI95 | [0.0, 0.1875] |
| four_cell_analysis.contrasts.target_effect_staged.body_BPB_change | -0.04680050837358805 |
| four_cell_analysis.contrasts.target_effect_staged.body_paired_CI95 | [-0.04899283347501657, -0.044773117366030894] |
| four_cell_analysis.contrasts.target_effect_staged.coherence_count_change | 12 |
| four_cell_analysis.contrasts.target_effect_staged.coherence_paired_fraction_CI95 | [0.025, 0.275] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_BPB_change | 0.045077579535552845 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_paired_CI95 | [0.04310979942910883, 0.047229086453556945] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_count_change | -5 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_paired_fraction_CI95 | [-0.2, 0.0875] |
| four_cell_analysis.body_documents | 256 |
| four_cell_analysis.body_bytes | 472055 |
| four_cell_analysis.limitations | "Descriptive four-cell contrasts; repeated dev use/nonblind content/one learned seed/shared prefix. Target factor also changes hard teacher count and EOS fraction; no independent causal or human certification." |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| limitations | "Nonblind Codex content scores, one learned seed, shared data and repeated dev comparisons. Masking also changes actual teacher count/EOS fraction. The four-cell observation is not an independent human/causal or capacity-limit proof." |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_order_proposal.json — defined_not_implemented_not_launched</summary>

[原記録](../../reports/phase6/interleaved_outcome_order_proposal.json) ／ SHA256: `e5f62364090c63fdb3b8589be77cd253a9436d2c4fb4d832283cf27250071713` ／ 7,457 bytes

| 原キー | 保存値 |
|---|---|
| status | "defined_not_implemented_not_launched" |
| cells.full_targets_interleaved.cached_BPB | 0.9748195810331843 |
| cells.outcome_EOS_targets_staged.result.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/compare-result.json" |
| cells.outcome_EOS_targets_staged.result.sha256 | "f27236c59a63cdd95470c894b4774e98b65c8a39dbc6e259be85548227110811" |
| cells.outcome_EOS_targets_staged.review.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/conditional-prefix-mask-20261006/review.json" |
| cells.outcome_EOS_targets_staged.review.sha256 | "f6abb4d5ebc9f78a36c7b6e34e9f478fb2f527593f5740018cc05651eabcd574" |
| cells.outcome_EOS_targets_staged.new_run | false |
| cells.outcome_EOS_targets_interleaved.new_run | true |
| cells.outcome_EOS_targets_interleaved.still_unstarted | true |
| reference_teacher_goals.web | 75000000 |
| reference_teacher_goals.story | 5000000 |
| reference_teacher_goals.ordinary_textbook | 10000000 |
| reference_teacher_goals.conditional_textbook | 10000000 |
| original_nominal_reference_teachers | 100000000 |
| predicted_actual_hard_teachers | 91641755 |
| predicted_actual_teachers_by_source.web | 75000000 |
| predicted_actual_teachers_by_source.story | 5000000 |
| predicted_actual_teachers_by_source.ordinary_textbook | 10000000 |
| predicted_actual_teachers_by_source.conditional_textbook | 1641755 |
| accepted_data.pool.pool | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large" |
| accepted_data.pool.manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| accepted_data.positive_data.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006" |
| accepted_data.positive_data.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| accepted_data.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| accepted_data.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| accepted_data.accepted_compact_index.path | "/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large/.compact-index-8cde6396d433644b/ready.json" |
| accepted_data.accepted_compact_index.sha256 | "ac8de9b50665e8b56c6d24efdf2cc79d75ce31d9dd452c1517186cf6f18d4606" |
| CPU_preparation_ceiling_seconds | 60 |
| probe_GPU_ceiling_seconds | 120 |
| total_new_GPU_ceiling_seconds | 900 |
| failure | "End the one predeclared fourth cell on readiness/quality/budget failure. No order list, ratio, mask position, EOS weight, source text, checkpoint, LR or decoder sweep to rescue it. All old failed cells remain unadopted." |
| completion | "Actual new cell/whole scientific teacher accounting/all80/full evaluation/four-cell comparison/terminal/UI/commit. Only a qualified recipe permits independent learned seed/full dev/protected test/adoption." |
| new_teacher_tokens_so_far | 0 |
| optimizer_updates_so_far | 0 |
| GPU_seconds_so_far | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_portable.json — None</summary>

[原記録](../../reports/phase6/interleaved_outcome_portable.json) ／ SHA256: `2333868a8483ec8b0c31a14c888c2784cdbab923484e5a8a6378cf1fb4aa7bbb` ／ 22,360 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/interleaved_outcome_completion.json.bytes | 20747 |
| files.reports/phase6/interleaved_outcome_completion.json.sha256 | "a34c30d48ee095f248720cebd91a2d61a07fd68c3058cddd57f0967212ea7d02" |
| files.reports/phase6/interleaved_outcome_active_job.json.bytes | 1330 |
| files.reports/phase6/source_gradient_attribution_proposal.json.bytes | 4435 |
| files.configs/phase6/interleaved_outcome_order.json.bytes | 18858 |
| files.configs/phase6/interleaved_outcome_order_probe.json.bytes | 18236 |
| files.reports/phase6/interleaved_outcome_order_proposal.json.bytes | 7457 |
| files.reports/phase6/interleaved_outcome_reference_input.json.bytes | 2649095 |
| files.scripts/record_interleaved_outcome_completion.py.bytes | 14336 |
| files.scripts/record_interleaved_outcome_completion.py.sha256 | "37299d0a4212d70c8174934b16af8fb479d09e3be87d2988f0a2544bc9de7dac" |
| files.scripts/record_interleaved_outcome_content.py.bytes | 14163 |
| files.scripts/review_interleaved_outcome_order.py.bytes | 9609 |
| files.scripts/interleaved_order_analysis.py.bytes | 2625 |
| files.tests/test_interleaved_outcome_review.py.bytes | 3295 |
| files.tests/test_interleaved_outcome_review.py.sha256 | "5419dd531cd4b4152f899371148220c6893a7826d93164ad5bef33c4aedd055e" |
| files.scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.tests/test_interleaved_outcome.py.bytes | 5013 |
| files.tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/interleaved_outcome_tests.xml.bytes | 718 |
| files.reports/phase6/interleaved_outcome_tests.xml.sha256 | "2bc59d153863f9b57babaa1fbdf88dd22637b4baee05d6d210d65ebbef985bf5" |
| files.reports/phase6/interleaved_outcome_review_tests.xml.bytes | 570 |
| files.reports/phase6/interleaved_outcome_review_tests.xml.sha256 | "fff0cef9e9a6f4a33f2ce254b56da9f7e8835bfa6bbd2915338c77e92fb36530" |
| files.reports/phase6/interleaved_outcome_review.json.bytes | 10117 |
| files.reports/phase6/interleaved-outcome-order-20261006/compare-result.json.bytes | 626133 |
| files.reports/phase6/interleaved-outcome-order-20261006/content-notes.json.bytes | 24791 |
| files.reports/phase6/interleaved-outcome-order-20261006/content-notes.json.sha256 | "dc9dfd4e3861267fa9b0c8b2df2cb8865aece002b6f6f2863b1e27c9d6760ca4" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/body.json.bytes | 66952 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/body.json.sha256 | "47af885ac930454a1f559932d174b7de453e26083fd8fd2c8baf6021333a66ab" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/generation.json.bytes | 104178 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/generation.json.sha256 | "605ebf68cb5eddd70ddffe15ca0a974f5554817808a6925d50a0d1002a2037e2" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/jblimp.json.bytes | 338208 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/jblimp.json.sha256 | "2e4c4ae525d5d6dad5817a608dc1c7216aad62047c7c0f5a77d7e693b7623eba" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/jcqa.json.bytes | 1640212 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/jcqa.json.sha256 | "0674d4d532181deb717f05af7505a98d2dc99374c89f54406c11f0052edca94f" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/result.json.bytes | 200128 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/result.json.sha256 | "d9d73a9b0651cb6b666965f9338d8203a7f06c348ef929adfd7e47a9367a6ae8" |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/semantics.json.bytes | 202758 |
| files.reports/phase6/interleaved-outcome-order-20261006/evaluation/interleaved_outcome_EOS/evaluation/semantics.json.sha256 | "2009afc1816f775f1f2899857e9e2deb73b2625553d6553f92d2f97f38bb1c24" |
| files.reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/latest.json.bytes | 297 |
| files.reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/latest.json.sha256 | "76eebb8fe5eb754f494fb4c827e91774033c468eb76c4021f294176f7711ec5a" |
| files.reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/metrics.jsonl.bytes | 11080631 |
| files.reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/metrics.jsonl.sha256 | "a22e650f9a44d6d9cb8a36704f40ec56ba971d16f9308213bcf40f936f10428a" |
| files.reports/phase6/interleaved-outcome-order-20261006/job.json.bytes | 815 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/job.json.bytes | 544 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/result.json.bytes | 241567 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json.bytes | 270 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/latest.json.sha256 | "01f95c57c65be222970611a5d04b67d781eaa85bae9e4f5e227dca29833db1f0" |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/resume-gate/result.json.bytes | 79841 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json.bytes | 268 |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/latest.json.sha256 | "38614bc57c4a10e7a669cb211c3b188812d344694241d3e4fac81c8ad4f6ec90" |
| files.reports/phase6/interleaved-outcome-order-20261006/probe/timing/metrics.jsonl.bytes | 113367 |
| files.reports/phase6/interleaved-outcome-order-20261006/progress-result.json.bytes | 625431 |
| files.reports/phase6/interleaved-outcome-order-20261006/review.json.bytes | 10117 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0000.json.bytes | 9928 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0000.json.sha256 | "4fa4798205398bcd1b191c3034fa6ec9fd46f8ab173762161fdc7eec2bb49138" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0016.json.bytes | 9581 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0016.json.sha256 | "98e0a3746cb91fd081a52250aa3cab22f59f081214a7dad59916d255852e3519" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0032.json.bytes | 10210 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0032.json.sha256 | "9c3184cfe1418be129bbb9c53766983061f46dc33a3fe62bcad6b2bc2a41e39e" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0048.json.bytes | 9497 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0048.json.sha256 | "25acea47d0cef2e0a83220adedea8dd3ccfd2829163395f2c33de3dad0cdebda" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0064.json.bytes | 10300 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0064.json.sha256 | "d38dcf5d84256e89a15b0705339e7c24cf95911592d636ae4fbbddf206b396e9" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0080.json.bytes | 9699 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0080.json.sha256 | "837378d5e3c20dabe8226a4b5ff4b82a3e0bf4dd898b5852b715ddf6b7be5cb0" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0096.json.bytes | 9770 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0096.json.sha256 | "45355dca0ee41ad98cb8cbaaea8a6883bb3ef94e22f597f55308b741638b31b2" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0112.json.bytes | 10126 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0112.json.sha256 | "6c09fc7277997efcda1a3bd53d00650262035dc216479a6428503e35abd3ae28" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0128.json.bytes | 9804 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0128.json.sha256 | "64965c757d2fe189fe3af10f95bffea55a0bae95732fbd123210f604da9af431" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0144.json.bytes | 9859 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0144.json.sha256 | "43cc79d74ed8c06250f3fd7f10a6e769b9f9020952180bc12012b2c2f0343a30" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0160.json.bytes | 10138 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0160.json.sha256 | "c6856048eeed26e53ad60c020eaeb93a711b59f306a5e5cf3f859c2504ba967a" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0176.json.bytes | 9965 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0176.json.sha256 | "32da9622ffb035533aebec5b01210122e13327360af82966fbd8f14fb48175bc" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0192.json.bytes | 9864 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0192.json.sha256 | "8c11ee71308c9146450ca3c85307a6fc8cde5a65fdace7885b23ff49449ddf12" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0208.json.bytes | 9635 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0208.json.sha256 | "5472b7c8376074bf5a7d3e38c7b83320e9b38f2b905dd1e8c76c59808ed46307" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0224.json.bytes | 9777 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0224.json.sha256 | "145257e3d4a8e8c1763546440ec6a9925e25366aa0dd366d533361ca894702cc" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0240.json.bytes | 9608 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0240.json.sha256 | "3102219c1a112a82e0f3443d2efbd873aa4a4ccb5195c4066d2c61b0c025e228" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0256.json.bytes | 9579 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0256.json.sha256 | "314a141f2354889d92b38233b97bc506d37f776b778fc76371b4d669dfd292c8" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0272.json.bytes | 9551 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0272.json.sha256 | "e1a33c7b0f2678822cf449870fcca3ec4afcfcb1330f5afefc7e9c1ea56cd78c" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0288.json.bytes | 9573 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0288.json.sha256 | "7c96499464be212f3698518654d4378045a757f088452650699b05a30e3ca0c7" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0304.json.bytes | 9776 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0304.json.sha256 | "ff40ead6ac7875247481b922bf1b26bf21074f220ba2929808ef1bf5e3a0df32" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0320.json.bytes | 9276 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0320.json.sha256 | "ef3e81b348ce32eec9291efeb2d5e7df74069f5cec380bb8b8d596b66a0aad6a" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0336.json.bytes | 9380 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0336.json.sha256 | "6378a69aedbfc661b2fed1adcbd1e53ac873916182fdbae29cf757a9c6e78455" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0352.json.bytes | 9744 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0352.json.sha256 | "f39f65054e6c7ad5b87fa5b7daf5c2555de74bdef7d8cac0430bf82cfcbec5d0" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0368.json.bytes | 9485 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0368.json.sha256 | "0ed99cc0833b2ca9c92b6f3c33e4d92d127b18537b2277a9b08a46fd6a15515b" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0384.json.bytes | 9835 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0384.json.sha256 | "8b9c0a07dc0a894bcb4918efb25a9f919001e295341c1ecb1db84494c5f51869" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0400.json.bytes | 9492 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0400.json.sha256 | "35a5323cc2c67547e44bb359dbcd83849b079914319edff390d9f1fdceca8da3" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0416.json.bytes | 9847 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0416.json.sha256 | "83e48bbcfa618b494e898e0779aa56d6b5224a0740da3bcd0459516b5d5e86dc" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0432.json.bytes | 9305 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0432.json.sha256 | "06e52820c78e9ea10979547f434441619e48e72f89ccf42717b3423dabde2a39" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0448.json.bytes | 9548 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0448.json.sha256 | "bddb6ca930db5bf7028fccd413d2aef742d41c39879862c7805a04b4eaaaea59" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0464.json.bytes | 9376 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0464.json.sha256 | "648d08f833d07ddcb816c9e54482009cbbcd27db387db132346a79b1c9c045c1" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0480.json.bytes | 9407 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0480.json.sha256 | "ebc588a875b246a568b6e7467b8eaac2b150ed7d8927ab7b57787dfb378bb3ae" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0496.json.bytes | 9481 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/0496.json.sha256 | "443ccf3250695cd754ac31609a72e1a2edafe9c3ced868331f40250dbd1f2971" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/result.json.bytes | 186387 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/bridge/interleaved_outcome_EOS/result.json.sha256 | "70f279315656ac609f72d807e74f8a044a2f7a603acf20fb8430f42cb2c902d2" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0000.json.bytes | 7948 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0000.json.sha256 | "bf1d7770073ed4f14a35c4d35bc511a6740b915c2f1bead414a2827c35ae8eac" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0016.json.bytes | 8285 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0016.json.sha256 | "1e46faa69b6cf675dc710b33bd6678df532524d51f0f244e43177f05a44c0ca9" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0032.json.bytes | 6958 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0032.json.sha256 | "a6addc43b91ecfb69ddd6b6bd6c78844e4649183d12b5fe2af7fee461bd760b3" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0048.json.bytes | 8141 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0048.json.sha256 | "37b5167707e7414ed0f45f026abeef7979e3971cf484efd6a4c048f2600025f3" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0064.json.bytes | 8482 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0064.json.sha256 | "6cdb1e0464cf7b6be159bcaaacf78ad3283c215a61e112e76e55f50ac6a25ce4" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0080.json.bytes | 7051 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0080.json.sha256 | "6d7ce301ecf8776296e1c4944c34a56edffbcf67dd08072284a2d0fd033f33bf" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0096.json.bytes | 8045 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0096.json.sha256 | "7a50296c42bc4e02411e28105732e0f7087dde52729b074452ad7f4552e1241d" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0112.json.bytes | 8236 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0112.json.sha256 | "df841f407d41fbfc8e49d8ecdd6e6929e1753b44af3134ec329003ee695340f5" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0128.json.bytes | 7063 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0128.json.sha256 | "56d400ef3f5538d5537ea02fdac368f1664cbe6e8fc9ce94f5a189698e94013c" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0144.json.bytes | 8142 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0144.json.sha256 | "8ea9e670fcebaf20372cd6d41ae45dca0bcf67d87b49980425aa51f7cae7a0ec" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0160.json.bytes | 8582 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0160.json.sha256 | "9cfa5e40a125721bdd067a5636ba6111016315e0191656a27b24a4e7e7ca7aa1" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0176.json.bytes | 6893 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0176.json.sha256 | "0e08ce7c7501fed7105df5385b6056f451c51bc0e03891b05c8c1b906728b205" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0192.json.bytes | 8147 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0192.json.sha256 | "4dccb4f950c8c776bcf6c7e5b42c5cb0a9c9a7a6a0361779746f0317c13f9846" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0208.json.bytes | 8471 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0208.json.sha256 | "12c76263f76f2955e679aa5ad3c584ba11fb3640109df1d1036f8aedb87966de" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0224.json.bytes | 7067 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0224.json.sha256 | "d2e95b94a6899f2df3e0ced29d4efa1f84995525714f175ff34a62581b8c25f5" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0240.json.bytes | 8328 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0240.json.sha256 | "b0738b7cadadf3bbacc1a99dc1bbbf94ee45e5e49d85d4b55d794c8255e4b7ed" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0256.json.bytes | 8196 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0256.json.sha256 | "61b6c1e6dde540f09d8ca6c84d524ca913170ea440753e7d95b36beb1ac0e1ee" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0272.json.bytes | 8396 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0272.json.sha256 | "a8a00cc7ac9d8dda3484b95d84fb656041ae3bfc0db3c51ca48a3a5b86310cc9" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0288.json.bytes | 7071 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0288.json.sha256 | "a6cb9107493be9d67bcd8efd9f032f028800c681dada623be739f6c5e6ce3a94" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0304.json.bytes | 8139 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0304.json.sha256 | "39e5e87487bb9db23694d1fe3f1439d25fb4206564361d15866b041abf6a55f9" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0320.json.bytes | 8554 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0320.json.sha256 | "f070fd09881f232c6e68be1fda90c8525ebc1687fc1c0083d01bcbfe56857e8e" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0336.json.bytes | 7079 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0336.json.sha256 | "25aa17e69791aef46ca9a714f14e0dd1e6caff9a0cd679e5452a6e289a8cace4" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0352.json.bytes | 8128 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0352.json.sha256 | "24e06676547066245cf4d491cd9df4fb054ce41211070919da1d6e9c2c2c115b" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0368.json.bytes | 8113 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0368.json.sha256 | "29aa54394f28c9601c0b4b6870f5682c6cd750e5eb0a0e2d57d1d16edd43e65b" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0384.json.bytes | 6992 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0384.json.sha256 | "facde7b75d639bf73555628971df45933aa9863aa571cc531408f8531faef03f" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0400.json.bytes | 8127 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0400.json.sha256 | "857da1f2266734c24962d371092ab27d8642990a36044e3cdf5eefedea9a9094" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0416.json.bytes | 8133 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0416.json.sha256 | "db983e47b6de3c538ea07e5207baa69deafc3d55415c8b4d5157b14387fe400e" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0432.json.bytes | 7079 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0432.json.sha256 | "23327f801f9dbed5d256e27c4a97b1c4a1e1fac854f6e40858bee4504e4ac79f" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0448.json.bytes | 8054 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0448.json.sha256 | "55447ffd783ebb167c11de726e71d0f80ba8d13a24cd87bc0b84c4b4e43698d3" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0464.json.bytes | 8307 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0464.json.sha256 | "ecdea037e61c094336961f0b919326b3d3e758af47d4478c3388c10539319c2b" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0480.json.bytes | 6992 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0480.json.sha256 | "ffb080bcca5db6a9ce077428310383c24133792482588a2aac279f87a4e9a4e7" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0496.json.bytes | 8058 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/0496.json.sha256 | "d505fe1822d499679485464392f5aa8516e419d7c1a901ec0b3fed1b01b0cd08" |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/result.json.bytes | 183238 |
| files.reports/phase6/interleaved-outcome-order-20261006/transfer/retention/interleaved_outcome_EOS/result.json.sha256 | "82a3ba72eb5470df793cdde638e0c90933635ac7d33353e359bcbcbcdcbf3b6f" |
| raw_bytes | 19119853 |

</details>

<details>
<summary>reports/phase6/interleaved_outcome_review.json — rejected_single_order_target_fourth_cell</summary>

[原記録](../../reports/phase6/interleaved_outcome_review.json) ／ SHA256: `93d031d41c2af61457cd8ee7271b7b9fc757a484f8bb747a45d8fc56e5a37597` ／ 10,117 bytes

| 原キー | 保存値 |
|---|---|
| status | "rejected_single_order_target_fourth_cell" |
| summaries.masked_mixed.BPB | 0.9730966521951491 |
| summaries.masked_mixed.rates.eos | 22 |
| summaries.masked_mixed.rates.repetition | 35 |
| summaries.masked_mixed.rates.unicode_failure | 0 |
| summaries.masked_mixed.rates.role_leak | 0 |
| summaries.masked_mixed.rates.empty | 0 |
| summaries.masked_mixed.grammar2 | 31 |
| summaries.masked_mixed.relevance2 | 64 |
| summaries.masked_mixed.coherent | 11 |
| summaries.masked_mixed.appropriate | 12 |
| summaries.masked_mixed.notes_sha256 | "dc9dfd4e3861267fa9b0c8b2df2cb8865aece002b6f6f2863b1e27c9d6760ca4" |
| summaries.full_mixed.BPB | 0.9748195810331843 |
| summaries.full_mixed.rates.eos | 30 |
| summaries.full_mixed.rates.repetition | 31 |
| summaries.full_mixed.rates.unicode_failure | 0 |
| summaries.full_mixed.rates.role_leak | 0 |
| summaries.full_mixed.rates.empty | 0 |
| summaries.full_mixed.grammar2 | 69 |
| summaries.full_mixed.relevance2 | 51 |
| summaries.full_mixed.coherent | 4 |
| summaries.full_mixed.appropriate | 18 |
| summaries.full_mixed.notes_sha256 | "12ff1008589c4f7de7439e99dd4e8d53aea429b2c164c898b4866b3a10431934" |
| summaries.full_staged.BPB | 1.1336128657420816 |
| summaries.full_staged.rates.eos | 76 |
| summaries.full_staged.rates.repetition | 2 |
| summaries.full_staged.rates.unicode_failure | 0 |
| summaries.full_staged.rates.role_leak | 0 |
| summaries.full_staged.rates.empty | 0 |
| summaries.full_staged.grammar2 | 65 |
| summaries.full_staged.relevance2 | 39 |
| summaries.full_staged.coherent | 23 |
| summaries.full_staged.appropriate | 26 |
| summaries.full_staged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| summaries.masked_staged.BPB | 1.0868123573684936 |
| summaries.masked_staged.rates.eos | 79 |
| summaries.masked_staged.rates.repetition | 1 |
| summaries.masked_staged.rates.unicode_failure | 0 |
| summaries.masked_staged.rates.role_leak | 0 |
| summaries.masked_staged.rates.empty | 0 |
| summaries.masked_staged.grammar2 | 72 |
| summaries.masked_staged.relevance2 | 53 |
| summaries.masked_staged.coherent | 35 |
| summaries.masked_staged.appropriate | 54 |
| summaries.masked_staged.notes_sha256 | "8f98d68db71f07c6aa3e82592e2e2aab5d81f90024e221bcdfbfc4562cef1613" |
| accounting.updates | 3068 |
| accounting.actual_new_hard_teachers | 91641755 |
| accounting.original_nominal_reference_teachers | 100000000 |
| accounting.physical_input_tokens | 100532224 |
| accounting.actual_source_accounting.teachers.web | 75000000 |
| accounting.actual_source_accounting.teachers.story | 5000000 |
| accounting.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| accounting.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.actual_source_accounting.eos.web | 159170 |
| accounting.actual_source_accounting.eos.story | 38240 |
| accounting.actual_source_accounting.eos.ordinary_textbook | 74183 |
| accounting.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.actual_source_accounting.body_bytes.web | 292149840 |
| accounting.actual_source_accounting.body_bytes.story | 20452979 |
| accounting.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| accounting.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| relative_to_strong_staged.checks.coherence_gain_at_least8 | false |
| relative_to_strong_staged.checks.paired_CI_lower_above0 | false |
| relative_to_strong_staged.checks.EOS_nonworsening | false |
| relative_to_strong_staged.checks.repetition_nonworsening | false |
| relative_to_strong_staged.checks.no_empty_role_unicode | true |
| relative_to_strong_staged.checks.BPB_gate | true |
| relative_to_strong_staged.checks.appropriate_completion_not_punctuation | true |
| relative_to_strong_staged.passed | false |
| absolute_dev_screen.grammar_at_least56 | false |
| absolute_dev_screen.coherence_at_least27 | false |
| absolute_dev_screen.appropriate_at_least27 | false |
| absolute_dev_screen.EOS_at_least37 | false |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| historical_Web.EOS_at_least8_more | true |
| historical_Web.repetition_no_worse | true |
| historical_Web.no_empty_role_unicode | true |
| historical_Web.BPB_degradation_at_most1percent | true |
| observed_masked_staged_comparison.checks.coherence_gain_at_least8 | false |
| observed_masked_staged_comparison.checks.paired_CI_lower_above0 | false |
| observed_masked_staged_comparison.checks.EOS_nonworsening | false |
| observed_masked_staged_comparison.checks.repetition_nonworsening | false |
| observed_masked_staged_comparison.checks.no_empty_role_unicode | true |
| observed_masked_staged_comparison.checks.BPB_gate | true |
| observed_masked_staged_comparison.checks.appropriate_completion_not_punctuation | true |
| observed_masked_staged_comparison.passed | false |
| four_cell_analysis.contrasts.order_effect_full.body_BPB_change | -0.1587932847088974 |
| four_cell_analysis.contrasts.order_effect_full.body_paired_CI95 | [-0.16429589288877466, -0.15389340970513357] |
| four_cell_analysis.contrasts.order_effect_full.coherence_count_change | -19 |
| four_cell_analysis.contrasts.order_effect_full.coherence_paired_fraction_CI95 | [-0.3375, -0.1375] |
| four_cell_analysis.contrasts.order_effect_masked.body_BPB_change | -0.11371570517334455 |
| four_cell_analysis.contrasts.order_effect_masked.body_paired_CI95 | [-0.11859395003660304, -0.10930360980970213] |
| four_cell_analysis.contrasts.order_effect_masked.coherence_count_change | -24 |
| four_cell_analysis.contrasts.order_effect_masked.coherence_paired_fraction_CI95 | [-0.425, -0.175] |
| four_cell_analysis.contrasts.target_effect_mixed.body_BPB_change | -0.0017229288380352105 |
| four_cell_analysis.contrasts.target_effect_mixed.body_paired_CI95 | [-0.001943490722199282, -0.0015048457941451575] |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_count_change | 7 |
| four_cell_analysis.contrasts.target_effect_mixed.coherence_paired_fraction_CI95 | [0.0, 0.1875] |
| four_cell_analysis.contrasts.target_effect_staged.body_BPB_change | -0.04680050837358805 |
| four_cell_analysis.contrasts.target_effect_staged.body_paired_CI95 | [-0.04899283347501657, -0.044773117366030894] |
| four_cell_analysis.contrasts.target_effect_staged.coherence_count_change | 12 |
| four_cell_analysis.contrasts.target_effect_staged.coherence_paired_fraction_CI95 | [0.025, 0.275] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_BPB_change | 0.045077579535552845 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.body_paired_CI95 | [0.04310979942910883, 0.047229086453556945] |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_count_change | -5 |
| four_cell_analysis.contrasts.interaction_mask_effect_mixed_minus_staged.coherence_paired_fraction_CI95 | [-0.2, 0.0875] |
| four_cell_analysis.body_documents | 256 |
| four_cell_analysis.body_bytes | 472055 |
| four_cell_analysis.limitations | "Descriptive four-cell contrasts; repeated dev use/nonblind content/one learned seed/shared prefix. Target factor also changes hard teacher count and EOS fraction; no independent causal or human certification." |
| eligible_for_final_Base_validation | false |
| actual_science_GPU_seconds | 261.29975055900286 |
| own_probe_GPU_seconds | 17.989334398997016 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/local_webui_review.json — running_local_inference_verified</summary>

[原記録](../../reports/phase6/local_webui_review.json) ／ SHA256: `e66bf75dac568befba16f95a0e06fafa62cf9aff0e238c8e7039fffaa865ad5f` ／ 3,540 bytes

| 原キー | 保存値 |
|---|---|
| tests.passed | 11 |
| tests.xml_sha256 | "26748cbea1ef169e874d98ede535978788846c7f2108a62a2d4cfbc562519df7" |
| tests.failed | 0 |
| source_sha256.tests/test_webui.py | "774507a642e3f1853acc12dd53e605e0d0fa2e41dac9070b42344c2a7f719cb2" |
| checks.same_seed_ids_equal | true |
| checks.windows_linux_sources_match | true |
| checks.greedy_matches_accepted_evaluation | true |
| checks.disconnect_releases_and_regenerates | true |
| checks.duplicate_preserves_active_record | true |
| checks.start_stop_scripts_verified | true |
| checks.browser_generation | true |
| checks.mobile_no_horizontal_overflow | true |
| checks.checkpoint_tokenizer_sha_verified | true |
| checks.windows_http_access | true |
| checks.duplicate_start_rejected | true |
| checks.actual_gpu_generation | true |
| checks.browser_manual_stop | true |
| status | "running_local_inference_verified" |
| scope | "User requested current-model local Web UI; no training or later experiments" |
| additional_training_tokens | 0 |
| checked_at | "2026-10-04T12:31:33.3837066Z" |
| browser.checked_at | "2026-10-04T12:31:09.628457Z" |
| browser.status | "passed" |
| browser.generation.status | "生成量の上限で停止" |
| model.training_tokens | 10000007168 |
| model.update | 305176 |
| model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-20261006/probe/job.json — failed_or_interrupted</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-20261006/probe/job.json) ／ SHA256: `656385de8b6d546ea6fb14bdc960e4612409efc0685b3a6f6d575e06013edd31` ／ 533 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed_or_interrupted" |
| GPU_elapsed_seconds | 0.0 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-probe-launcher-20261006/launcher.json) ／ SHA256: `073172f762861ba202b331ff18c05f338cb3bb75feb90372cf6cce37fb0ec960` ／ 105 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-probe-launcher-20261006/result.json — failed</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-probe-launcher-20261006/result.json) ／ SHA256: `29841bf5e38ea8f94cda361331e4d7225a1b28e55174b2782f40815a37d82447` ／ 176 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>
