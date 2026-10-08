# 実行管理・後続準備・その他 — 20/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/progress-result.json) ／ SHA256: `4e277c0d9e908d10463abe5d9384c5ca9d88d58b032511307eb694944561ca7a` ／ 536,527 bytes

| 原キー | 保存値 |
|---|---|
| arms.full_fresh_Adam.checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/checkpoint-00323503.pt" |
| arms.full_fresh_Adam.checkpoint.checkpoint_sha256 | "4ddcedfdc174d77890717b5910f563170cf359566c86178afcb0b2d1724cb77f" |
| arms.full_fresh_Adam.checkpoint.binding.config_sha256 | "a0772ed4fb0b1257bfb44947e42ff76267279fe8874d9c8d9ab44be407503eaf" |
| arms.full_fresh_Adam.checkpoint.binding.arm | "full_fresh_Adam" |
| arms.full_fresh_Adam.checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| arms.full_fresh_Adam.checkpoint.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| arms.full_fresh_Adam.checkpoint.binding.study_kind | "matched_fresh_Adam_rank4_frozen_backbone_Base_v1" |
| arms.full_fresh_Adam.checkpoint.binding.teacher_goals.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.binding.teacher_goals.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.binding.target_rule | "original mixed conditional outcome+EOS only" |
| arms.full_fresh_Adam.checkpoint.binding.optimizer_policy | "fresh_Adam_both_arms" |
| arms.full_fresh_Adam.checkpoint.binding.peak_lr | 1e-05 |
| arms.full_fresh_Adam.checkpoint.updates | 3068 |
| arms.full_fresh_Adam.checkpoint.additional_supervised_tokens | 91641755 |
| arms.full_fresh_Adam.checkpoint.additional_input_tokens | 100532224 |
| arms.full_fresh_Adam.checkpoint.actual_body_bytes | 361357103 |
| arms.full_fresh_Adam.checkpoint.reference_suffix_teacher_tokens | 100000000 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.teachers.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.teachers.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.eos.web | 159170 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.eos.story | 38240 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.eos.ordinary_textbook | 74183 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.body_bytes.web | 292149840 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.body_bytes.story | 20452979 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.focus.web | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.focus.story | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| arms.full_fresh_Adam.checkpoint.sampler.kind | "original-Web-retention-short-source-quotas-v1" |
| arms.full_fresh_Adam.checkpoint.sampler.goals.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.sampler.goals.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.sampler.goals.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.goals.conditional_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.context | 1024 |
| arms.full_fresh_Adam.checkpoint.sampler.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.position | 3068 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.sampler.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.sampler.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.sampler.position | 10327341 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.sampler.context | 1024 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.web.sampler.blocks | 11939276 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.genre | "story" |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.documents | 761448 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.document_position | 38243 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.story.token_offset | 87 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.genre | "textbook" |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.documents | 2942232 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.document_position | 74189 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.ordinary_textbook.token_offset | 77 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.conditional_textbook.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| arms.full_fresh_Adam.checkpoint.sampler.streams.conditional_textbook.epoch | 114 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.conditional_textbook.document_position | 871 |
| arms.full_fresh_Adam.checkpoint.sampler.streams.conditional_textbook.token_offset | 23 |
| arms.full_fresh_Adam.checkpoint.sampler.source_teachers.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.sampler.source_teachers.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.sampler.source_teachers.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.source_teachers.conditional_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.source_eos.web | 159170 |
| arms.full_fresh_Adam.checkpoint.sampler.source_eos.story | 38240 |
| arms.full_fresh_Adam.checkpoint.sampler.source_eos.ordinary_textbook | 74183 |
| arms.full_fresh_Adam.checkpoint.sampler.source_eos.conditional_textbook | 234328 |
| arms.full_fresh_Adam.checkpoint.sampler.source_tokens.web | 75183104 |
| arms.full_fresh_Adam.checkpoint.sampler.source_tokens.story | 5039104 |
| arms.full_fresh_Adam.checkpoint.sampler.source_tokens.ordinary_textbook | 10075136 |
| arms.full_fresh_Adam.checkpoint.sampler.source_tokens.conditional_textbook | 10234880 |
| arms.full_fresh_Adam.checkpoint.sampler.source_body_bytes.web | 292149840 |
| arms.full_fresh_Adam.checkpoint.sampler.source_body_bytes.story | 20452979 |
| arms.full_fresh_Adam.checkpoint.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| arms.full_fresh_Adam.checkpoint.sampler.source_body_bytes.conditional_textbook | 37865985 |
| arms.full_fresh_Adam.checkpoint.sampler.source_focus_teachers.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.source_focus_teachers.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.source_focus_teachers.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 159170 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 38240 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 74183 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 292149840 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 20452979 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 42739471 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "original-Web-retention-short-source-quotas-v1" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10253920 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| arms.full_fresh_Adam.checkpoint.sampler.prefix_mask_accounting.reference_policy | "interleaved" |
| arms.full_fresh_Adam.checkpoint.token_digest | "d5e3ff03c09fd0e95a1a2b3e2160e24b02f007e10b564a2385c4aaed4c97dac4" |
| arms.full_fresh_Adam.checkpoint.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| arms.full_fresh_Adam.checkpoint.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| arms.full_fresh_Adam.checkpoint.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.full_fresh_Adam.checkpoint.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.full_fresh_Adam.checkpoint.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| arms.full_fresh_Adam.checkpoint.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| arms.full_fresh_Adam.checkpoint.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.full_fresh_Adam.checkpoint.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.full_fresh_Adam.checkpoint.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| arms.full_fresh_Adam.checkpoint.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| arms.full_fresh_Adam.checkpoint.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.full_fresh_Adam.checkpoint.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.full_fresh_Adam.checkpoint.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| arms.full_fresh_Adam.checkpoint.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| arms.full_fresh_Adam.checkpoint.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| arms.full_fresh_Adam.checkpoint.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| arms.full_fresh_Adam.checkpoint.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| arms.full_fresh_Adam.checkpoint.training_seconds | 165.0985339851759 |
| arms.full_fresh_Adam.checkpoint.trainable_parameters | 10001152 |
| arms.full_fresh_Adam.checkpoint.native_parameters | 10001152 |
| arms.full_fresh_Adam.checkpoint.frozen_backbone_unchanged | false |
| arms.full_fresh_Adam.evaluation.binding.teacher_goals.web | 75000000 |
| arms.full_fresh_Adam.evaluation.binding.teacher_goals.story | 5000000 |
| arms.full_fresh_Adam.evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| arms.full_fresh_Adam.evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| arms.full_fresh_Adam.evaluation.checkpoint_sha256 | "4ddcedfdc174d77890717b5910f563170cf359566c86178afcb0b2d1724cb77f" |
| arms.full_fresh_Adam.evaluation.body.documents | 256 |
| arms.full_fresh_Adam.evaluation.body.limit_documents | 256 |
| arms.full_fresh_Adam.evaluation.body.body_nll | 318405.9215731621 |
| arms.full_fresh_Adam.evaluation.body.eos_nll | 583.2752591967583 |
| arms.full_fresh_Adam.evaluation.body.body_bytes | 472055 |
| arms.full_fresh_Adam.evaluation.body.body_tokens | 122343 |
| arms.full_fresh_Adam.evaluation.body.bpb | 0.9731125484176233 |
| arms.full_fresh_Adam.evaluation.body.seconds | 1.1490449440025259 |
| arms.full_fresh_Adam.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| arms.full_fresh_Adam.evaluation.generation.max_new_tokens | 64 |
| arms.full_fresh_Adam.evaluation.greedy_rates.eos | 23 |
| arms.full_fresh_Adam.evaluation.greedy_rates.repetition | 37 |
| arms.full_fresh_Adam.evaluation.greedy_rates.unicode_failure | 0 |
| arms.full_fresh_Adam.evaluation.greedy_rates.role_leak | 0 |
| arms.full_fresh_Adam.evaluation.greedy_rates.empty | 0 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5625, 0.6458333333333334] |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.625] |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5821999782395821 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.16757831697804315 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7673716012084593 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7250755287009063, 0.8126888217522659] |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7673716012084593 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7099697885196374 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6616314199395771, 0.7583081570996979] |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7099697885196374 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41519434628975266 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.full_fresh_Adam.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.353887399463807 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.3270554066130474, 0.3806970509383378] |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.353887399463807 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3109919571045576 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28328865058087577, 0.3378016085790885] |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3109919571045576 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.31023168466319423 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.13899499953659533 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.full_fresh_Adam.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.full_fresh_Adam.evaluation.diagnostics.semantic_both_contexts.correct | 21 |
| arms.full_fresh_Adam.evaluation.memory.maximum_observed_allocated_bytes | 274956288 |
| arms.full_fresh_Adam.evaluation.memory.maximum_observed_reserved_bytes | 8464105472 |
| arms.full_fresh_Adam.evaluation.protected_test_used | false |
| arms.rank4_frozen_backbone.checkpoint.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/checkpoint-00323503.pt" |
| arms.rank4_frozen_backbone.checkpoint.checkpoint_sha256 | "318fe9c57c2eafeafb78cff3920760dd651b1bdc9d94e9287a21d8024226174b" |
| arms.rank4_frozen_backbone.checkpoint.binding.config_sha256 | "a0772ed4fb0b1257bfb44947e42ff76267279fe8874d9c8d9ab44be407503eaf" |
| arms.rank4_frozen_backbone.checkpoint.binding.arm | "rank4_frozen_backbone" |
| arms.rank4_frozen_backbone.checkpoint.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| arms.rank4_frozen_backbone.checkpoint.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| arms.rank4_frozen_backbone.checkpoint.binding.study_kind | "matched_fresh_Adam_rank4_frozen_backbone_Base_v1" |
| arms.rank4_frozen_backbone.checkpoint.binding.teacher_goals.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.binding.teacher_goals.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.binding.teacher_goals.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.binding.teacher_goals.conditional_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.binding.target_rule | "original mixed conditional outcome+EOS only" |
| arms.rank4_frozen_backbone.checkpoint.binding.optimizer_policy | "fresh_Adam_both_arms" |
| arms.rank4_frozen_backbone.checkpoint.binding.peak_lr | 1e-05 |
| arms.rank4_frozen_backbone.checkpoint.updates | 3068 |
| arms.rank4_frozen_backbone.checkpoint.additional_supervised_tokens | 91641755 |
| arms.rank4_frozen_backbone.checkpoint.additional_input_tokens | 100532224 |
| arms.rank4_frozen_backbone.checkpoint.actual_body_bytes | 361357103 |
| arms.rank4_frozen_backbone.checkpoint.reference_suffix_teacher_tokens | 100000000 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.teachers.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.teachers.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.eos.web | 159170 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.eos.story | 38240 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.eos.ordinary_textbook | 74183 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.eos.conditional_textbook | 234328 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.body_bytes.web | 292149840 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.body_bytes.story | 20452979 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.focus.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.focus.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.focus.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.focus.conditional_textbook | 1407427 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.removed_prefix.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.removed_prefix.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.removed_prefix.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.actual_source_accounting.removed_prefix.conditional_textbook | 8358245 |
| arms.rank4_frozen_backbone.checkpoint.sampler.kind | "original-Web-retention-short-source-quotas-v1" |
| arms.rank4_frozen_backbone.checkpoint.sampler.goals.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.goals.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.goals.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.goals.conditional_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.context | 1024 |
| arms.rank4_frozen_backbone.checkpoint.sampler.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.position | 3068 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.sampler.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.sampler.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.sampler.position | 10327341 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.sampler.context | 1024 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.web.sampler.blocks | 11939276 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.genre | "story" |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.documents | 761448 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.document_position | 38243 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.story.token_offset | 87 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.genre | "textbook" |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.documents | 2942232 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.document_position | 74189 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.ordinary_textbook.token_offset | 77 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.conditional_textbook.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.conditional_textbook.epoch | 114 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.conditional_textbook.document_position | 871 |
| arms.rank4_frozen_backbone.checkpoint.sampler.streams.conditional_textbook.token_offset | 23 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_teachers.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_teachers.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_teachers.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_teachers.conditional_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_eos.web | 159170 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_eos.story | 38240 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_eos.ordinary_textbook | 74183 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_eos.conditional_textbook | 234328 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_tokens.web | 75183104 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_tokens.story | 5039104 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_tokens.ordinary_textbook | 10075136 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_tokens.conditional_textbook | 10234880 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_body_bytes.web | 292149840 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_body_bytes.story | 20452979 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_body_bytes.ordinary_textbook | 42739471 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_body_bytes.conditional_textbook | 37865985 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_focus_teachers.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_focus_teachers.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_focus_teachers.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.source_focus_teachers.conditional_textbook | 1407427 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.teachers.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.teachers.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.teachers.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.teachers.conditional_textbook | 1641755 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.eos.web | 159170 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.eos.story | 38240 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.eos.ordinary_textbook | 74183 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.eos.conditional_textbook | 234328 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.web | 292149840 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.story | 20452979 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.ordinary_textbook | 42739471 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.body_bytes.conditional_textbook | 6014813 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.focus.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.focus.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.focus.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.focus.conditional_textbook | 1407427 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.actual.removed_prefix.conditional_textbook | 8358245 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.kind | "original-Web-retention-short-source-quotas-v1" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.web | 75000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.story | 5000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.goals.conditional_textbook | 10000000 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.context | 1024 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.position | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.position | 10253920 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.context | 1024 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.web.sampler.blocks | 11939276 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.genre | "story" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.documents | 761448 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.document_position | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.story.token_offset | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.genre | "textbook" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.documents | 2942232 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.document_position | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.ordinary_textbook.token_offset | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.seed | 42 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.epoch | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.document_position | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.streams.conditional_textbook.token_offset | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_teachers.conditional_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_eos.conditional_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_tokens.conditional_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_body_bytes.conditional_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.web | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.story | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.ordinary_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.initial_reference.source_focus_teachers.conditional_textbook | 0 |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| arms.rank4_frozen_backbone.checkpoint.sampler.prefix_mask_accounting.reference_policy | "interleaved" |
| arms.rank4_frozen_backbone.checkpoint.token_digest | "d5e3ff03c09fd0e95a1a2b3e2160e24b02f007e10b564a2385c4aaed4c97dac4" |
| arms.rank4_frozen_backbone.checkpoint.reference_token_digest | "3ab4989ed8205f894ed55df4e26fc918a0a60835fc4705a7f827d95f33cc36e4" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.web.input | "285b95126c7ccffcfdf960ff855c447ce9bb68296bb7cd74a619eff29808f6ae" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.web.reference_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.web.masked_target | "dbd2c2d51d48e08e83243134f545268fbab66ddd526fa3f00312723debe59acd" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.web.focus | "e400d0cabaa8bb597d84b29a1b5ec4c22612cccb3883ee1857d71d3d1b2a60aa" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.story.input | "c30b3d6829177c3087783b081f61e4d62bd55cfbe78c3a973b747f6e0b6958f3" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.story.reference_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.story.masked_target | "9bd153f53fd5fda26d29c3efa300936bb475b47171a9ff5ec3f117fb152a3d3e" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.story.focus | "70f1576e7296f2604347e9e8584e3c132beef37594af8e7ea2e856cf415ca6c8" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.ordinary_textbook.input | "90324eb40ed2b7bab559b32ca5324c9dbe3b2a78f38d68bceababe0b70cf1df0" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.ordinary_textbook.reference_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.ordinary_textbook.masked_target | "5c42c19debbb2c0db5c0267f91f4f79f248289e65cd3ad5117d1729e91899461" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.ordinary_textbook.focus | "11ff893601b3eaa2ac0b43c890d57fbd6e506cbd6499245e0312f92130699412" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.conditional_textbook.input | "7cdf0453ee2a1b9c080119aa746ef4431fcab51c478fd44fe64e74b38888bd1e" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.conditional_textbook.reference_target | "c27025ad3d62d1181934b97f647f5d348f3ee7386c3e6ef6df6c06d31437b28d" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.conditional_textbook.masked_target | "81158e2896a63fa58023e009e38b0ffbbf53f23d5f0c5a434b4791739a7914e6" |
| arms.rank4_frozen_backbone.checkpoint.source_digests.conditional_textbook.focus | "2e81aad72356276a99f671d94981a473179a841263f2e36034824450f1746afa" |
| arms.rank4_frozen_backbone.checkpoint.training_seconds | 191.05161352688447 |
| arms.rank4_frozen_backbone.checkpoint.trainable_parameters | 232960 |
| arms.rank4_frozen_backbone.checkpoint.native_parameters | 10001152 |
| arms.rank4_frozen_backbone.checkpoint.frozen_backbone_unchanged | true |
| arms.rank4_frozen_backbone.evaluation.binding.teacher_goals.web | 75000000 |
| arms.rank4_frozen_backbone.evaluation.binding.teacher_goals.story | 5000000 |
| arms.rank4_frozen_backbone.evaluation.binding.teacher_goals.ordinary_textbook | 10000000 |
| arms.rank4_frozen_backbone.evaluation.binding.teacher_goals.conditional_textbook | 10000000 |
| arms.rank4_frozen_backbone.evaluation.checkpoint_sha256 | "318fe9c57c2eafeafb78cff3920760dd651b1bdc9d94e9287a21d8024226174b" |
| arms.rank4_frozen_backbone.evaluation.body.documents | 256 |
| arms.rank4_frozen_backbone.evaluation.body.limit_documents | 256 |
| arms.rank4_frozen_backbone.evaluation.body.body_nll | 318338.3824253082 |
| arms.rank4_frozen_backbone.evaluation.body.eos_nll | 583.8103364929557 |
| arms.rank4_frozen_backbone.evaluation.body.body_bytes | 472055 |
| arms.rank4_frozen_backbone.evaluation.body.body_tokens | 122343 |
| arms.rank4_frozen_backbone.evaluation.body.bpb | 0.9729061351952771 |
| arms.rank4_frozen_backbone.evaluation.body.seconds | 1.154605231975438 |
| arms.rank4_frozen_backbone.evaluation.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| arms.rank4_frozen_backbone.evaluation.generation.max_new_tokens | 64 |
| arms.rank4_frozen_backbone.evaluation.greedy_rates.eos | 13 |
| arms.rank4_frozen_backbone.evaluation.greedy_rates.repetition | 64 |
| arms.rank4_frozen_backbone.evaluation.greedy_rates.unicode_failure | 0 |
| arms.rank4_frozen_backbone.evaluation.greedy_rates.role_leak | 0 |
| arms.rank4_frozen_backbone.evaluation.greedy_rates.empty | 0 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.ci95 | [0.5625, 0.6458333333333334] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.units | 96 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.examples | 192 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.point | 0.6041666666666666 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5677083333333334, 0.6458333333333334] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.count | 192 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.6041666666666666 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6030899793276031 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.mcc | 0.20947289622255397 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.train_majority_accuracy | 0.5 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.negation.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.negation.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.quantity.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.time.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.time.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.comparison.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.coreference.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.causality.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.causality.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.ci95 | [0.7069486404833837, 0.797583081570997] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.units | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.examples | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7039274924471299 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6555891238670695, 0.7552870090634441] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.count | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7039274924471299 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41312056737588654 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.train_majority_accuracy | null |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.island effects.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.binding.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.argument structure.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.morphology.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.control/raising.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.point | 0.3342269883824844 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.ci95 | [0.3073949955317248, 0.36014298480786416] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.units | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.primary.hard_accuracy | 0.3342269883824844 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3145665773011618 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2877569258266309, 0.34137622877569257] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.count | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3145665773011618 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3136077294104208 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.mcc | 0.14336022285388283 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.categories.commonsense.seed | 42 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| arms.rank4_frozen_backbone.evaluation.diagnostics.semantic_both_contexts.correct | 21 |
| arms.rank4_frozen_backbone.evaluation.memory.maximum_observed_allocated_bytes | 236172288 |
| arms.rank4_frozen_backbone.evaluation.memory.maximum_observed_reserved_bytes | 8701083648 |
| arms.rank4_frozen_backbone.evaluation.protected_test_used | false |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone-content-notes.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone-content-notes.json) ／ SHA256: `5f27ccc46d3809ae02fd5e312c6babadb6cbc102ca6be5a55f93f6f28df986d8` ／ 27,670 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/latest.json) ／ SHA256: `8ee64b56506ac7e3218a15c3d62e737bceb972c9903642cbc647dbe3a8f9f744` ／ 297 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/review.json — fixed_rank4_and_fresh_full_control_rejected</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/review.json) ／ SHA256: `863ec1ecc2baf411299e8b542b7fc4480f740ae178a0fbc2210cc80bc3827c01` ／ 11,955 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_rank4_and_fresh_full_control_rejected" |
| summaries.full_fresh_Adam.BPB | 0.9731125484176233 |
| summaries.full_fresh_Adam.rates.eos | 23 |
| summaries.full_fresh_Adam.rates.repetition | 37 |
| summaries.full_fresh_Adam.rates.unicode_failure | 0 |
| summaries.full_fresh_Adam.rates.role_leak | 0 |
| summaries.full_fresh_Adam.rates.empty | 0 |
| summaries.full_fresh_Adam.grammar2 | 31 |
| summaries.full_fresh_Adam.relevance2 | 63 |
| summaries.full_fresh_Adam.coherent | 10 |
| summaries.full_fresh_Adam.appropriate | 11 |
| summaries.full_fresh_Adam.notes_sha256 | "aef67ea301ef9ced00b526fc09b81ce8d5c24e892f375086c5a421722708e581" |
| summaries.rank4_frozen_backbone.BPB | 0.9729061351952771 |
| summaries.rank4_frozen_backbone.rates.eos | 13 |
| summaries.rank4_frozen_backbone.rates.repetition | 64 |
| summaries.rank4_frozen_backbone.rates.unicode_failure | 0 |
| summaries.rank4_frozen_backbone.rates.role_leak | 0 |
| summaries.rank4_frozen_backbone.rates.empty | 0 |
| summaries.rank4_frozen_backbone.grammar2 | 18 |
| summaries.rank4_frozen_backbone.relevance2 | 59 |
| summaries.rank4_frozen_backbone.coherent | 3 |
| summaries.rank4_frozen_backbone.appropriate | 3 |
| summaries.rank4_frozen_backbone.notes_sha256 | "5f27ccc46d3809ae02fd5e312c6babadb6cbc102ca6be5a55f93f6f28df986d8" |
| accounting.full_fresh_Adam.updates | 3068 |
| accounting.full_fresh_Adam.actual_new_hard_teachers | 91641755 |
| accounting.full_fresh_Adam.original_nominal_reference_teachers | 100000000 |
| accounting.full_fresh_Adam.physical_input_tokens | 100532224 |
| accounting.full_fresh_Adam.actual_source_accounting.teachers.web | 75000000 |
| accounting.full_fresh_Adam.actual_source_accounting.teachers.story | 5000000 |
| accounting.full_fresh_Adam.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| accounting.full_fresh_Adam.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.full_fresh_Adam.actual_source_accounting.eos.web | 159170 |
| accounting.full_fresh_Adam.actual_source_accounting.eos.story | 38240 |
| accounting.full_fresh_Adam.actual_source_accounting.eos.ordinary_textbook | 74183 |
| accounting.full_fresh_Adam.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.full_fresh_Adam.actual_source_accounting.body_bytes.web | 292149840 |
| accounting.full_fresh_Adam.actual_source_accounting.body_bytes.story | 20452979 |
| accounting.full_fresh_Adam.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| accounting.full_fresh_Adam.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| accounting.rank4_frozen_backbone.updates | 3068 |
| accounting.rank4_frozen_backbone.actual_new_hard_teachers | 91641755 |
| accounting.rank4_frozen_backbone.original_nominal_reference_teachers | 100000000 |
| accounting.rank4_frozen_backbone.physical_input_tokens | 100532224 |
| accounting.rank4_frozen_backbone.actual_source_accounting.teachers.web | 75000000 |
| accounting.rank4_frozen_backbone.actual_source_accounting.teachers.story | 5000000 |
| accounting.rank4_frozen_backbone.actual_source_accounting.teachers.ordinary_textbook | 10000000 |
| accounting.rank4_frozen_backbone.actual_source_accounting.teachers.conditional_textbook | 1641755 |
| accounting.rank4_frozen_backbone.actual_source_accounting.eos.web | 159170 |
| accounting.rank4_frozen_backbone.actual_source_accounting.eos.story | 38240 |
| accounting.rank4_frozen_backbone.actual_source_accounting.eos.ordinary_textbook | 74183 |
| accounting.rank4_frozen_backbone.actual_source_accounting.eos.conditional_textbook | 234328 |
| accounting.rank4_frozen_backbone.actual_source_accounting.body_bytes.web | 292149840 |
| accounting.rank4_frozen_backbone.actual_source_accounting.body_bytes.story | 20452979 |
| accounting.rank4_frozen_backbone.actual_source_accounting.body_bytes.ordinary_textbook | 42739471 |
| accounting.rank4_frozen_backbone.actual_source_accounting.body_bytes.conditional_textbook | 6014813 |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.coherence_gain_at_least8 | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.paired_CI_lower_above0 | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.EOS_nonworsening | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.repetition_nonworsening | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.no_empty_role_unicode | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.BPB_gate | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.appropriate_completion_not_punctuation | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.passed | false |
| gates.full_fresh_Adam.absolute.grammar_at_least56 | false |
| gates.full_fresh_Adam.absolute.coherence_at_least27 | false |
| gates.full_fresh_Adam.absolute.appropriate_at_least27 | false |
| gates.full_fresh_Adam.absolute.EOS_at_least37 | false |
| gates.full_fresh_Adam.absolute.repetition_at_most18 | false |
| gates.full_fresh_Adam.absolute.no_empty_role_unicode | true |
| gates.full_fresh_Adam.historical_Web.EOS_at_least8_more | true |
| gates.full_fresh_Adam.historical_Web.repetition_no_worse | true |
| gates.full_fresh_Adam.historical_Web.no_empty_role_unicode | true |
| gates.full_fresh_Adam.historical_Web.BPB_degradation_at_most1percent | true |
| gates.full_fresh_Adam.eligible_for_final_Base_validation | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.coherence_gain_at_least8 | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.paired_CI_lower_above0 | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.EOS_nonworsening | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.repetition_nonworsening | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.BPB_gate | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.appropriate_completion_not_punctuation | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.passed | false |
| gates.rank4_frozen_backbone.absolute.grammar_at_least56 | false |
| gates.rank4_frozen_backbone.absolute.coherence_at_least27 | false |
| gates.rank4_frozen_backbone.absolute.appropriate_at_least27 | false |
| gates.rank4_frozen_backbone.absolute.EOS_at_least37 | false |
| gates.rank4_frozen_backbone.absolute.repetition_at_most18 | false |
| gates.rank4_frozen_backbone.absolute.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.historical_Web.EOS_at_least8_more | true |
| gates.rank4_frozen_backbone.historical_Web.repetition_no_worse | false |
| gates.rank4_frozen_backbone.historical_Web.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.historical_Web.BPB_degradation_at_most1percent | true |
| gates.rank4_frozen_backbone.eligible_for_final_Base_validation | false |
| matched_rank4_vs_full_fresh.checks.coherence_gain_at_least8 | false |
| matched_rank4_vs_full_fresh.checks.paired_CI_lower_above0 | false |
| matched_rank4_vs_full_fresh.checks.EOS_nonworsening | false |
| matched_rank4_vs_full_fresh.checks.repetition_nonworsening | false |
| matched_rank4_vs_full_fresh.checks.no_empty_role_unicode | true |
| matched_rank4_vs_full_fresh.checks.BPB_gate | true |
| matched_rank4_vs_full_fresh.checks.appropriate_completion_not_punctuation | true |
| matched_rank4_vs_full_fresh.passed | false |
| strong_historical_control_reused_unchanged.BPB | 1.1336128657420816 |
| strong_historical_control_reused_unchanged.rates.eos | 76 |
| strong_historical_control_reused_unchanged.rates.repetition | 2 |
| strong_historical_control_reused_unchanged.rates.unicode_failure | 0 |
| strong_historical_control_reused_unchanged.rates.role_leak | 0 |
| strong_historical_control_reused_unchanged.rates.empty | 0 |
| strong_historical_control_reused_unchanged.grammar2 | 65 |
| strong_historical_control_reused_unchanged.relevance2 | 39 |
| strong_historical_control_reused_unchanged.coherent | 23 |
| strong_historical_control_reused_unchanged.appropriate | 26 |
| strong_historical_control_reused_unchanged.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| eligible_recipes | [] |
| actual_science_GPU_seconds | 539.8163853790029 |
| own_probe_GPU_seconds | 58.92843314999482 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-probe-launcher-20261006/launcher.json) ／ SHA256: `97bab945c6e67ec76599c3639548bc11968b97098031b2d6124e3314016d88a4` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-probe-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-probe-launcher-20261006/result.json) ／ SHA256: `884f077d3ceacebb3073be3760e998fe1b48fddecca7f9f45f15dedaea22d570` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-train-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-train-launcher-20261006/launcher.json) ／ SHA256: `686bc539290d7a08b7d5ddea63feacaa138b05a16bfc8b790d8cd78cf3c829e6` ／ 104 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-train-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-train-launcher-20261006/result.json) ／ SHA256: `c34723bab46dd9dd8696ccf0f7105325a51cafb75d1451e08901d0d8a4acf26b` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/low_rank_base_initial_failure.json — initial_probe_setup_failure_fixed_in_v2</summary>

[原記録](../../reports/phase6/low_rank_base_initial_failure.json) ／ SHA256: `67fab37b23cb1add849416b5a5d18cbd48e19cf2cc428bff7247cd37a300e04d` ／ 1,058 bytes

| 原キー | 保存値 |
|---|---|
| old_job.status | "failed_or_interrupted" |
| old_job.GPU_elapsed_seconds | 0.0 |
| GPU_seconds | 0.0 |
| scientific_teacher_tokens | 0 |
| status | "initial_probe_setup_failure_fixed_in_v2" |
| optimizer_updates | 0 |

</details>

<details>
<summary>reports/phase6/low_rank_base_proposal.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_proposal.json) ／ SHA256: `1171227c42435683d058a83f772e9993a43fd5ae9a67588c0f76bfefc8490e75` ／ 3,174 bytes

| 原キー | 保存値 |
|---|---|
| hypothesis | "Restrict the learned update subspace rather than adding an L2 penalty or altering data/loss/order. Frozen W0 does not guarantee preserved active-model Web quality." |
| distinct_from_failed_branches | ["full-model L2 displacement anchor", "full-model weight averaging", "Web logit KL", "packing isolation", "sequence unlikelihood"] |
| input_target_budget | "Each3068 updates/100532224 input/91641755 actual masked teachers; same original100M reference quota ledger. Not100M actual teachers." |
| CPU_preparation_ceiling_seconds | 30 |
| probe_GPU_ceiling_seconds | 240 |
| total_new_GPU_ceiling_seconds | 1800 |
| GPU_seconds_so_far | 0 |
| new_teacher_tokens_so_far | 0 |
| completion | "Both actual endpoints and all160 raw-bound content reviews; unchanged strong/absolute/historical-Web gates, exact terminal identity and UI restoration. Only a qualified recipe may enter independent learned seed/full-dev/protected-test/adoption." |
| failure_policy | "End fixed rank4 comparison; no rank/module/scale/LR/source/mask/decoder/checkpoint salvage sweep." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_completion.json — fixed_rank4_and_fresh_full_control_rejected</summary>

[原記録](../../reports/phase6/low_rank_base_v2_completion.json) ／ SHA256: `be0f34b5cef57216180654ff2fb511bb2096a8ebfc808f822bf89852661a6119` ／ 7,746 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_rank4_and_fresh_full_control_rejected" |
| actual_terminal_job.status | "complete" |
| actual_terminal_job.GPU_elapsed_seconds | 539.8163853790029 |
| actual_terminal_job.completed_updates | 3060 |
| actual_terminal_job.total_updates | 3068 |
| actual_terminal_job.actual_teachers | 91426867 |
| actual_terminal_job.loss | 2.561180353164673 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| scientific_teacher_tokens | 183283510 |
| teacher_tokens_per_arm | 91641755 |
| nominal_reference_teacher_tokens_per_arm | 100000000 |
| physical_input_tokens | 201064448 |
| scientific_optimizer_updates | 6136 |
| verification_teacher_tokens | 2867838 |
| verification_optimizer_updates | 96 |
| scientific_GPU_seconds | 539.8163853790029 |
| probe_GPU_seconds | 58.92843314999482 |
| total_new_GPU_seconds | 598.7448185289977 |
| GPU_ceiling_seconds | 1800 |
| previous_related_GPU_seconds_preserved | 3250.1644225021005 |
| related_GPU_seconds | 3848.909241031098 |
| summaries.full_fresh_Adam.BPB | 0.9731125484176233 |
| summaries.full_fresh_Adam.rates.eos | 23 |
| summaries.full_fresh_Adam.rates.repetition | 37 |
| summaries.full_fresh_Adam.rates.unicode_failure | 0 |
| summaries.full_fresh_Adam.rates.role_leak | 0 |
| summaries.full_fresh_Adam.rates.empty | 0 |
| summaries.full_fresh_Adam.grammar2 | 31 |
| summaries.full_fresh_Adam.relevance2 | 63 |
| summaries.full_fresh_Adam.coherent | 10 |
| summaries.full_fresh_Adam.appropriate | 11 |
| summaries.full_fresh_Adam.notes_sha256 | "aef67ea301ef9ced00b526fc09b81ce8d5c24e892f375086c5a421722708e581" |
| summaries.rank4_frozen_backbone.BPB | 0.9729061351952771 |
| summaries.rank4_frozen_backbone.rates.eos | 13 |
| summaries.rank4_frozen_backbone.rates.repetition | 64 |
| summaries.rank4_frozen_backbone.rates.unicode_failure | 0 |
| summaries.rank4_frozen_backbone.rates.role_leak | 0 |
| summaries.rank4_frozen_backbone.rates.empty | 0 |
| summaries.rank4_frozen_backbone.grammar2 | 18 |
| summaries.rank4_frozen_backbone.relevance2 | 59 |
| summaries.rank4_frozen_backbone.coherent | 3 |
| summaries.rank4_frozen_backbone.appropriate | 3 |
| summaries.rank4_frozen_backbone.notes_sha256 | "5f27ccc46d3809ae02fd5e312c6babadb6cbc102ca6be5a55f93f6f28df986d8" |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.coherence_gain_at_least8 | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.paired_CI_lower_above0 | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.EOS_nonworsening | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.repetition_nonworsening | false |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.no_empty_role_unicode | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.BPB_gate | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.checks.appropriate_completion_not_punctuation | true |
| gates.full_fresh_Adam.relative_to_unchanged_strong.passed | false |
| gates.full_fresh_Adam.absolute.grammar_at_least56 | false |
| gates.full_fresh_Adam.absolute.coherence_at_least27 | false |
| gates.full_fresh_Adam.absolute.appropriate_at_least27 | false |
| gates.full_fresh_Adam.absolute.EOS_at_least37 | false |
| gates.full_fresh_Adam.absolute.repetition_at_most18 | false |
| gates.full_fresh_Adam.absolute.no_empty_role_unicode | true |
| gates.full_fresh_Adam.historical_Web.EOS_at_least8_more | true |
| gates.full_fresh_Adam.historical_Web.repetition_no_worse | true |
| gates.full_fresh_Adam.historical_Web.no_empty_role_unicode | true |
| gates.full_fresh_Adam.historical_Web.BPB_degradation_at_most1percent | true |
| gates.full_fresh_Adam.eligible_for_final_Base_validation | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.coherence_gain_at_least8 | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.paired_CI_lower_above0 | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.EOS_nonworsening | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.repetition_nonworsening | false |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.BPB_gate | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.checks.appropriate_completion_not_punctuation | true |
| gates.rank4_frozen_backbone.relative_to_unchanged_strong.passed | false |
| gates.rank4_frozen_backbone.absolute.grammar_at_least56 | false |
| gates.rank4_frozen_backbone.absolute.coherence_at_least27 | false |
| gates.rank4_frozen_backbone.absolute.appropriate_at_least27 | false |
| gates.rank4_frozen_backbone.absolute.EOS_at_least37 | false |
| gates.rank4_frozen_backbone.absolute.repetition_at_most18 | false |
| gates.rank4_frozen_backbone.absolute.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.historical_Web.EOS_at_least8_more | true |
| gates.rank4_frozen_backbone.historical_Web.repetition_no_worse | false |
| gates.rank4_frozen_backbone.historical_Web.no_empty_role_unicode | true |
| gates.rank4_frozen_backbone.historical_Web.BPB_degradation_at_most1percent | true |
| gates.rank4_frozen_backbone.eligible_for_final_Base_validation | false |
| matched_rank4_vs_full_fresh.checks.coherence_gain_at_least8 | false |
| matched_rank4_vs_full_fresh.checks.paired_CI_lower_above0 | false |
| matched_rank4_vs_full_fresh.checks.EOS_nonworsening | false |
| matched_rank4_vs_full_fresh.checks.repetition_nonworsening | false |
| matched_rank4_vs_full_fresh.checks.no_empty_role_unicode | true |
| matched_rank4_vs_full_fresh.checks.BPB_gate | true |
| matched_rank4_vs_full_fresh.checks.appropriate_completion_not_punctuation | true |
| matched_rank4_vs_full_fresh.passed | false |
| eligible_recipes | [] |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_completion_portable.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_v2_completion_portable.json) ／ SHA256: `e149e31f67c66fcdda8633e2f92ed156afb15b3b1f91941db8054a3febe8fb9f` ／ 49,263 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/low_rank_base_v2_completion.json.bytes | 7746 |
| files.reports/phase6/low_rank_base_v2_completion.json.sha256 | "be0f34b5cef57216180654ff2fb511bb2096a8ebfc808f822bf89852661a6119" |
| files.configs/phase6/low_rank_base_v2_comparison.json.bytes | 19756 |
| files.configs/phase6/low_rank_base_v2_probe.json.bytes | 18828 |
| files.reports/phase6/low_rank_base_v2_proposal.json.bytes | 3174 |
| files.reports/phase6/low_rank_base_tests.xml.bytes | 818 |
| files.reports/phase6/low_rank_base_tests.xml.sha256 | "2bcbb25dd4caae60332c675759e6be648e61c984c1156f82bd24d0274201c58f" |
| files.scripts/record_low_rank_base_completion.py.bytes | 7788 |
| files.scripts/record_low_rank_base_completion.py.sha256 | "65f5881c4d8dc5b7cb4aafe9cb88d9a0eba12064f78fb4b57e8e1127560fcf78" |
| files.scripts/record_low_rank_base_content.py.bytes | 3750 |
| files.scripts/review_low_rank_base_comparison.py.bytes | 7871 |
| files.reports/phase6/low_rank_base_initial_failure.json.bytes | 1058 |
| files.reports/phase6/low_rank_base_initial_failure.json.sha256 | "67fab37b23cb1add849416b5a5d18cbd48e19cf2cc428bff7247cd37a300e04d" |
| files.scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.tests/test_low_rank_base.py.bytes | 3982 |
| files.tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/compare-result.json.bytes | 537102 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/body.json.bytes | 66967 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/generation.json.bytes | 103672 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/jblimp.json.bytes | 338101 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/jcqa.json.bytes | 1640058 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/result.json.bytes | 199540 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/full_fresh_Adam/evaluation/semantics.json.bytes | 202724 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/body.json.bytes | 66954 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/generation.json.bytes | 112634 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/jblimp.json.bytes | 338242 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/jcqa.json.bytes | 1640738 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/result.json.bytes | 209649 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/evaluation/rank4_frozen_backbone/evaluation/semantics.json.bytes | 202824 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/latest.json.bytes | 291 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/latest.json.sha256 | "aa8ec2224d672e13a0fc56b707e312b504b19946795798e9900fb94cd653f67c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/metrics.jsonl.bytes | 11359893 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam-content-notes.json.bytes | 62238 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam-content-notes.json.sha256 | "aef67ea301ef9ced00b526fc09b81ce8d5c24e892f375086c5a421722708e581" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam-observations.tsv.bytes | 11332 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/job.json.bytes | 749 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json.bytes | 288 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json.sha256 | "8a7a5fa8afab1cc49670dd01e1663b346a7789364ed554469394dd8402a72ad9" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/result.json.bytes | 81889 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json.bytes | 286 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json.sha256 | "f1a8c47952d8fd21d3623be16390b352df72283195d9d2e74d88b5767d8f0983" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/metrics.jsonl.bytes | 116227 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/job.json.bytes | 573 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/progress-result.json.bytes | 549063 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json.bytes | 294 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json.sha256 | "d9a94f389888c22dec301452605e4cd993c37a28703aed29bd59fd4902c2da28" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/result.json.bytes | 81981 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json.bytes | 292 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json.sha256 | "9f4d3d5355c8e20cc4eba80a2e0cc1e6478a9f52eaf5c830760a783b2522a891" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/metrics.jsonl.bytes | 116436 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/result.json.bytes | 549578 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/configs/phase6/low_rank_base_v2_probe.json.bytes | 18828 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_low_rank_base.py.bytes | 3982 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/progress-result.json.bytes | 536527 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/latest.json.bytes | 297 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/latest.json.sha256 | "8ee64b56506ac7e3218a15c3d62e737bceb972c9903642cbc647dbe3a8f9f744" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone/training/metrics.jsonl.bytes | 11376825 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone-content-notes.json.bytes | 27670 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone-content-notes.json.sha256 | "5f27ccc46d3809ae02fd5e312c6babadb6cbc102ca6be5a55f93f6f28df986d8" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/rank4_frozen_backbone-observations.tsv.bytes | 11079 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/review.json.bytes | 11955 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/configs/phase6/low_rank_base_v2_comparison.json.bytes | 19756 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_low_rank_base.py.bytes | 3982 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |
| raw_bytes | 32682714 |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_launch.json — fixed_rank4_Base_launch</summary>

[原記録](../../reports/phase6/low_rank_base_v2_launch.json) ／ SHA256: `47b1b7c190472dcae87d5c63c6abf5197c22aaa1470ccc0dddeb16a932b15dfb` ／ 1,723 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_rank4_Base_launch" |
| actual_scientific_teacher_tokens_per_arm | 91641755 |
| nominal_reference_teachers_per_arm | 100000000 |
| new_scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| GPU_ceiling_seconds | 1800 |
| probe_ceiling_seconds | 240 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| actual_job.status | "setup" |
| actual_job.GPU_elapsed_seconds | 27.601280468981713 |
| actual_job.completed_updates | 320 |
| actual_job.total_updates | 3068 |
| actual_job.actual_teachers | 9560645 |
| actual_job.loss | 2.5379979610443115 |
| verification_GPU_seconds | 58.92843314999482 |
| remaining_science_GPU_ceiling_seconds | 1741.0715668500052 |
| estimated_GPU_seconds_with_margin | 1144.749499059093 |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_launch_portable.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_v2_launch_portable.json) ／ SHA256: `e96156570fe50482afa0f06bb5dbd580865184719e388dc5d8d57bb1955f45a8` ／ 1,909 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/low_rank_base_v2_launch.json.bytes | 1723 |
| files.configs/phase6/low_rank_base_v2_comparison.json.bytes | 19756 |
| files.reports/phase6/low_rank_base_v2_proposal.json.bytes | 3174 |
| files.reports/phase6/low_rank_base_tests.xml.bytes | 818 |
| files.reports/phase6/low_rank_base_tests.xml.sha256 | "2bcbb25dd4caae60332c675759e6be648e61c984c1156f82bd24d0274201c58f" |
| files.scripts/record_low_rank_base_milestone.py.bytes | 8024 |
| files.scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.tests/test_low_rank_base.py.bytes | 3982 |
| files.tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/job.json.bytes | 605 |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_probe.json — fixed_rank4_Base_probe</summary>

[原記録](../../reports/phase6/low_rank_base_v2_probe.json) ／ SHA256: `3b45bc5243a28a7fdca0e2eb8b297e1d64d80ee6d9e06646c676b4e9d8bf23f7` ／ 551,714 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_rank4_Base_probe" |
| actual_scientific_teacher_tokens_per_arm | 91641755 |
| nominal_reference_teachers_per_arm | 100000000 |
| new_scientific_teacher_tokens | 0 |
| GPU_seconds | 58.92843314999482 |
| GPU_ceiling_seconds | 1800 |
| probe_ceiling_seconds | 240 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| verification_teacher_tokens | 2867838 |
| GPU_optimizer_updates | 96 |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| arms.full_fresh_Adam.initial_checks.model | true |
| arms.full_fresh_Adam.initial_checks.fresh_Adam | true |
| arms.full_fresh_Adam.initial_checks.scheduler | true |
| arms.full_fresh_Adam.initial_checks.RNG | true |
| arms.full_fresh_Adam.initial_checks.native_count | true |
| arms.full_fresh_Adam.initial_checks.trainable_count | true |
| arms.full_fresh_Adam.initial_checks.actual_Web_cursor | true |
| arms.full_fresh_Adam.initial_checks.actual_parent_sampler_lineage | true |
| arms.full_fresh_Adam.initial_checks.actual_LR | true |
| arms.full_fresh_Adam.gate.passed | true |
| arms.full_fresh_Adam.gate.checks.version | true |
| arms.full_fresh_Adam.gate.checks.spec | true |
| arms.full_fresh_Adam.gate.checks.model_config | true |
| arms.full_fresh_Adam.gate.checks.model | true |
| arms.full_fresh_Adam.gate.checks.unmerged_training_model | true |
| arms.full_fresh_Adam.gate.checks.optimizer | true |
| arms.full_fresh_Adam.gate.checks.scheduler | true |
| arms.full_fresh_Adam.gate.checks.rng | true |
| arms.full_fresh_Adam.gate.checks.sampler | true |
| arms.full_fresh_Adam.gate.checks.update | true |
| arms.full_fresh_Adam.gate.checks.tokens | true |
| arms.full_fresh_Adam.gate.checks.supervised_tokens | true |
| arms.full_fresh_Adam.gate.checks.body_bytes | true |
| arms.full_fresh_Adam.gate.checks.token_digest | true |
| arms.full_fresh_Adam.gate.checks.focus_token_digest | true |
| arms.full_fresh_Adam.gate.checks.focus_teacher_tokens | true |
| arms.full_fresh_Adam.gate.checks.weighted_teacher_mass | true |
| arms.full_fresh_Adam.gate.checks.shard_manifest_sha256 | true |
| arms.full_fresh_Adam.gate.checks.implementation_sha256 | true |
| arms.full_fresh_Adam.gate.checks.study_implementation_sha256 | true |
| arms.full_fresh_Adam.gate.checks.study_binding | true |
| arms.full_fresh_Adam.gate.checks.pilot_binding | true |
| arms.full_fresh_Adam.gate.checks.lineage | true |
| arms.full_fresh_Adam.gate.checks.branch_updates | true |
| arms.full_fresh_Adam.gate.checks.branch_tokens | true |
| arms.full_fresh_Adam.gate.checks.merged_for_native_evaluation | true |
| arms.full_fresh_Adam.gate.checks.native_parameters | true |
| arms.full_fresh_Adam.gate.checks.trainable_parameters | true |
| arms.full_fresh_Adam.gate.checks.history_supervised_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_actual_source_eos | true |
| arms.full_fresh_Adam.gate.checks.history_tokens_seen | true |
| arms.full_fresh_Adam.gate.checks.history_source_input_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_gradient_norm | true |
| arms.full_fresh_Adam.gate.checks.history_additional_teacher_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_loss | true |
| arms.full_fresh_Adam.gate.checks.history_actual_source_body_bytes | true |
| arms.full_fresh_Adam.gate.checks.history_weighted_teacher_mass | true |
| arms.full_fresh_Adam.gate.checks.history_outcome_weight | true |
| arms.full_fresh_Adam.gate.checks.history_source_body_bytes | true |
| arms.full_fresh_Adam.gate.checks.history_token_digest | true |
| arms.full_fresh_Adam.gate.checks.history_removed_prefix_targets | true |
| arms.full_fresh_Adam.gate.checks.history_body_bytes_seen | true |
| arms.full_fresh_Adam.gate.checks.history_reference_suffix_teacher_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_trainable_parameters | true |
| arms.full_fresh_Adam.gate.checks.history_valid_input_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_reference_token_digest | true |
| arms.full_fresh_Adam.gate.checks.history_actual_source_teachers | true |
| arms.full_fresh_Adam.gate.checks.history_source_teachers | true |
| arms.full_fresh_Adam.gate.checks.history_source_focus_teachers | true |
| arms.full_fresh_Adam.gate.checks.history_focus_teacher_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_source_eos | true |
| arms.full_fresh_Adam.gate.checks.history_focus_token_digest | true |
| arms.full_fresh_Adam.gate.checks.history_physical_input_tokens | true |
| arms.full_fresh_Adam.gate.checks.history_native_parameters | true |
| arms.full_fresh_Adam.gate.checks.history_source_digests | true |
| arms.full_fresh_Adam.gate.checks.history_update | true |
| arms.full_fresh_Adam.gate.checks.history_actual_source_routes | true |
| arms.full_fresh_Adam.gate.checks.history_arm | true |
| arms.full_fresh_Adam.gate.checks.history_lr | true |
| arms.full_fresh_Adam.gate.checks.finite | true |
| arms.full_fresh_Adam.gate.checks.no_reheat | true |
| arms.full_fresh_Adam.gate.checks.mixed_sources_present | true |
| arms.full_fresh_Adam.gate.checks.actual_conditional_mask_active | true |
| arms.full_fresh_Adam.gate.GPU_optimizer_updates | 16 |
| arms.full_fresh_Adam.gate.verification_teacher_tokens | 478390 |
| arms.full_fresh_Adam.timing.terminal_save_seconds | 0.26101426500827074 |
| arms.full_fresh_Adam.timing.verification_teacher_tokens | 955529 |
| arms.full_fresh_Adam.timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/checkpoint.pt" |
| arms.full_fresh_Adam.timing.checkpoint.sha256 | "4a7d0be2250304987a458f1956f7b9f63a077dd3cf24d1ed01d34d444dcc9ee6" |
| arms.full_fresh_Adam.timing.peak_VRAM_bytes | 6149106176 |
| arms.rank4_frozen_backbone.initial_checks.model | true |
| arms.rank4_frozen_backbone.initial_checks.fresh_Adam | true |
| arms.rank4_frozen_backbone.initial_checks.scheduler | true |
| arms.rank4_frozen_backbone.initial_checks.RNG | true |
| arms.rank4_frozen_backbone.initial_checks.native_count | true |
| arms.rank4_frozen_backbone.initial_checks.trainable_count | true |
| arms.rank4_frozen_backbone.initial_checks.actual_Web_cursor | true |
| arms.rank4_frozen_backbone.initial_checks.actual_parent_sampler_lineage | true |
| arms.rank4_frozen_backbone.initial_checks.actual_LR | true |
| arms.rank4_frozen_backbone.gate.passed | true |
| arms.rank4_frozen_backbone.gate.checks.version | true |
| arms.rank4_frozen_backbone.gate.checks.spec | true |
| arms.rank4_frozen_backbone.gate.checks.model_config | true |
| arms.rank4_frozen_backbone.gate.checks.model | true |
| arms.rank4_frozen_backbone.gate.checks.unmerged_training_model | true |
| arms.rank4_frozen_backbone.gate.checks.optimizer | true |
| arms.rank4_frozen_backbone.gate.checks.scheduler | true |
| arms.rank4_frozen_backbone.gate.checks.rng | true |
| arms.rank4_frozen_backbone.gate.checks.sampler | true |
| arms.rank4_frozen_backbone.gate.checks.update | true |
| arms.rank4_frozen_backbone.gate.checks.tokens | true |
| arms.rank4_frozen_backbone.gate.checks.supervised_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.body_bytes | true |
| arms.rank4_frozen_backbone.gate.checks.token_digest | true |
| arms.rank4_frozen_backbone.gate.checks.focus_token_digest | true |
| arms.rank4_frozen_backbone.gate.checks.focus_teacher_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.weighted_teacher_mass | true |
| arms.rank4_frozen_backbone.gate.checks.shard_manifest_sha256 | true |
| arms.rank4_frozen_backbone.gate.checks.implementation_sha256 | true |
| arms.rank4_frozen_backbone.gate.checks.study_implementation_sha256 | true |
| arms.rank4_frozen_backbone.gate.checks.study_binding | true |
| arms.rank4_frozen_backbone.gate.checks.pilot_binding | true |
| arms.rank4_frozen_backbone.gate.checks.lineage | true |
| arms.rank4_frozen_backbone.gate.checks.branch_updates | true |
| arms.rank4_frozen_backbone.gate.checks.branch_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.merged_for_native_evaluation | true |
| arms.rank4_frozen_backbone.gate.checks.native_parameters | true |
| arms.rank4_frozen_backbone.gate.checks.trainable_parameters | true |
| arms.rank4_frozen_backbone.gate.checks.history_supervised_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_actual_source_eos | true |
| arms.rank4_frozen_backbone.gate.checks.history_tokens_seen | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_input_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_gradient_norm | true |
| arms.rank4_frozen_backbone.gate.checks.history_additional_teacher_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_loss | true |
| arms.rank4_frozen_backbone.gate.checks.history_actual_source_body_bytes | true |
| arms.rank4_frozen_backbone.gate.checks.history_weighted_teacher_mass | true |
| arms.rank4_frozen_backbone.gate.checks.history_outcome_weight | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_body_bytes | true |
| arms.rank4_frozen_backbone.gate.checks.history_token_digest | true |
| arms.rank4_frozen_backbone.gate.checks.history_removed_prefix_targets | true |
| arms.rank4_frozen_backbone.gate.checks.history_body_bytes_seen | true |
| arms.rank4_frozen_backbone.gate.checks.history_reference_suffix_teacher_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_trainable_parameters | true |
| arms.rank4_frozen_backbone.gate.checks.history_valid_input_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_reference_token_digest | true |
| arms.rank4_frozen_backbone.gate.checks.history_actual_source_teachers | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_teachers | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_focus_teachers | true |
| arms.rank4_frozen_backbone.gate.checks.history_focus_teacher_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_eos | true |
| arms.rank4_frozen_backbone.gate.checks.history_focus_token_digest | true |
| arms.rank4_frozen_backbone.gate.checks.history_physical_input_tokens | true |
| arms.rank4_frozen_backbone.gate.checks.history_native_parameters | true |
| arms.rank4_frozen_backbone.gate.checks.history_source_digests | true |
| arms.rank4_frozen_backbone.gate.checks.history_update | true |
| arms.rank4_frozen_backbone.gate.checks.history_actual_source_routes | true |
| arms.rank4_frozen_backbone.gate.checks.history_arm | true |
| arms.rank4_frozen_backbone.gate.checks.history_lr | true |
| arms.rank4_frozen_backbone.gate.checks.finite | true |
| arms.rank4_frozen_backbone.gate.checks.no_reheat | true |
| arms.rank4_frozen_backbone.gate.checks.mixed_sources_present | true |
| arms.rank4_frozen_backbone.gate.checks.actual_conditional_mask_active | true |
| arms.rank4_frozen_backbone.gate.GPU_optimizer_updates | 16 |
| arms.rank4_frozen_backbone.gate.verification_teacher_tokens | 478390 |
| arms.rank4_frozen_backbone.timing.terminal_save_seconds | 0.20526182500179857 |
| arms.rank4_frozen_backbone.timing.verification_teacher_tokens | 955529 |
| arms.rank4_frozen_backbone.timing.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/checkpoint.pt" |
| arms.rank4_frozen_backbone.timing.checkpoint.sha256 | "60583f591f5cb455f9e91dc299fa21d5603be062e45d3ca6066e2e0a3e775477" |
| arms.rank4_frozen_backbone.timing.peak_VRAM_bytes | 6149106176 |
| measured_timings.full_fresh_Adam.steady_step_seconds | 0.12237645400455222 |
| measured_timings.full_fresh_Adam.estimated_updates | 3068 |
| measured_timings.full_fresh_Adam.warmup_seconds | 0.7698920789989643 |
| measured_timings.full_fresh_Adam.save_seconds | 3.6541997101157904 |
| measured_timings.full_fresh_Adam.estimated_training_seconds | 379.87505267508095 |
| measured_timings.rank4_frozen_backbone.steady_step_seconds | 0.061413364004692994 |
| measured_timings.rank4_frozen_backbone.estimated_updates | 3068 |
| measured_timings.rank4_frozen_backbone.warmup_seconds | 1.7193110539519694 |
| measured_timings.rank4_frozen_backbone.save_seconds | 2.87366555002518 |
| measured_timings.rank4_frozen_backbone.estimated_training_seconds | 193.00917737037526 |
| estimated_science_GPU_seconds_with_margin | 1144.749499059093 |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_probe_portable.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_v2_probe_portable.json) ／ SHA256: `b26e4070325f937e329b2e7b8070d534e6bb834186e322ddb39e7de55e225626` ／ 23,983 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/low_rank_base_v2_probe.json.bytes | 551714 |
| files.configs/phase6/low_rank_base_v2_probe.json.bytes | 18828 |
| files.reports/phase6/low_rank_base_v2_proposal.json.bytes | 3174 |
| files.reports/phase6/low_rank_base_tests.xml.bytes | 818 |
| files.reports/phase6/low_rank_base_tests.xml.sha256 | "2bcbb25dd4caae60332c675759e6be648e61c984c1156f82bd24d0274201c58f" |
| files.scripts/record_low_rank_base_milestone.py.bytes | 8024 |
| files.scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.tests/test_low_rank_base.py.bytes | 3982 |
| files.tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json.bytes | 288 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/latest.json.sha256 | "8a7a5fa8afab1cc49670dd01e1663b346a7789364ed554469394dd8402a72ad9" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/resume-gate/result.json.bytes | 81889 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json.bytes | 286 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json.sha256 | "f1a8c47952d8fd21d3623be16390b352df72283195d9d2e74d88b5767d8f0983" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/metrics.jsonl.bytes | 116227 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/job.json.bytes | 573 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/progress-result.json.bytes | 549063 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json.bytes | 294 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/latest.json.sha256 | "d9a94f389888c22dec301452605e4cd993c37a28703aed29bd59fd4902c2da28" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/resume-gate/result.json.bytes | 81981 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json.bytes | 292 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json.sha256 | "9f4d3d5355c8e20cc4eba80a2e0cc1e6478a9f52eaf5c830760a783b2522a891" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/metrics.jsonl.bytes | 116436 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/result.json.bytes | 549578 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/configs/phase6/low_rank_base_v2_probe.json.bytes | 18828 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/audit_base_parent_baselines.py.bytes | 10171 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/cached_three_source_index.py.bytes | 3702 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_loss.py.bytes | 1721 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_loss.py.sha256 | "85ef2ba6f3815eacbbe4f7178bca235f2240662b55581fbbf0f925d38879b349" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_positive_trainer.py.bytes | 17219 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_relation_language.py.bytes | 13080 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/condition_transfer_curriculum.py.bytes | 17562 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/conditional_prefix_mask_trainer.py.bytes | 9918 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/diagnose_mature_base_distribution.py.bytes | 13137 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/evaluate_japanese_base.py.bytes | 23943 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/historical_parent_condition_trainer.py.bytes | 5114 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/inspect_complete_text_data.py.bytes | 3834 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/interleaved_outcome_trainer.py.bytes | 8012 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/mature_condition_trainer.py.bytes | 6925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/original_web_retention_trainer.py.bytes | 2925 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/phase6_performance.py.bytes | 30565 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_coherent_text.py.bytes | 8227 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_coherent_text.py.sha256 | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.bytes | 7698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_positive_teachers.py.sha256 | "7ab8cd6680e0ab909a5340a9450ba98cc0647be0adc706e8b6cc852cf04ab57c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_relation_inputs.py.bytes | 2883 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_relation_language.py.bytes | 9494 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_transfer_curriculum.py.bytes | 14907 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_condition_transfer_inputs.py.bytes | 3845 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/prepare_story_text.py.bytes | 10281 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_diversity_comparison.py.bytes | 12116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_positive_comparison.py.bytes | 12940 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_relation_comparison.py.bytes | 15550 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_source_learning.py.bytes | 14551 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_source_ranking.py.bytes | 5436 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_condition_transfer_comparison.py.bytes | 13454 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_historical_parent_condition_comparison_v3.py.bytes | 14814 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_mature_base_condition_comparison.py.bytes | 12993 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_original_web_retention_comparison.py.bytes | 14711 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_source_order_condition_comparison.py.bytes | 15634 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/review_source_order_condition_comparison_v2.py.bytes | 15640 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_complete_text_comparison.ps1.bytes | 898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_complete_text_comparison.py.bytes | 19516 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_diversity_comparison.ps1.bytes | 2658 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_diversity_comparison.py.bytes | 23265 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_positive_comparison.ps1.bytes | 2666 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_positive_comparison.py.bytes | 27001 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_relation_comparison.ps1.bytes | 3117 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_relation_comparison.py.bytes | 26879 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_learning.ps1.bytes | 3106 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_learning.py.bytes | 25539 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_ranking.ps1.bytes | 2541 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_source_ranking.py.bytes | 20218 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_transfer_comparison.ps1.bytes | 3116 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_condition_transfer_comparison.py.bytes | 25898 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_complete_100m.py.bytes | 17731 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_complete_100m.py.sha256 | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_short_pilot.py.bytes | 27331 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_eos_short_pilot.py.sha256 | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.ps1.bytes | 3176 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_historical_parent_condition_comparison_v3.py.bytes | 30882 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_interleaved_outcome_order.ps1.bytes | 3123 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_interleaved_outcome_order.py.bytes | 27212 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_mature_base_condition_comparison.ps1.bytes | 3109 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_mature_base_condition_comparison.py.bytes | 25251 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_original_web_retention_comparison.ps1.bytes | 3146 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_original_web_retention_comparison.py.bytes | 26346 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison.ps1.bytes | 3126 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison.py.bytes | 29698 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.ps1.bytes | 3221 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_source_order_condition_comparison_v2.py.bytes | 28951 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/run_story_weight_comparison.py.bytes | 24337 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_budget_evidence.py.bytes | 4931 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_budget_evidence.py.sha256 | "a4dcbf2c65f3e96d437ff151cb6d7381b8d4d3100ff56666db4cb699dc499e4c" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/source_order_condition_trainer.py.bytes | 3178 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/story_weight_trainer.py.bytes | 14130 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/scripts/textbook_quantity_trainer.py.bytes | 4021 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/coherent_units.py.bytes | 3942 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/coherent_units.py.sha256 | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/eos_pilot.py.bytes | 8774 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/eos_pilot.py.sha256 | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/evaluation_memory.py.bytes | 1060 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/japanese_evaluation.py.bytes | 10087 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/low_lr_pilot.py.bytes | 1320 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/model.py.bytes | 11578 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/readiness.py.bytes | 3643 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/shards.py.bytes | 6231 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/tokenizer.py.bytes | 6567 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/tokenizer.py.sha256 | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/src/jmicro/training.py.bytes | 35671 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_base_parent_baselines.py.bytes | 1335 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_base_parent_baselines.py.sha256 | "8f481bc8aed9ad30089ef08aae49bd966a209833fe8d3ca2548249ff763f8f0f" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.bytes | 1996 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_comparison_v3.py.sha256 | "b5a7f57ae0335855929fba132b77199fc30413e01ec6b5d578ac9d1cf9ce27b8" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_condition.py.bytes | 1239 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_historical_parent_condition.py.sha256 | "18f3bf7443c80fdd1b0c9a474f1c4caf855ef67c11f6115bab1f49d0bef442c9" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_interleaved_outcome.py.bytes | 5013 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_interleaved_outcome.py.sha256 | "d43291a8ce81854b1bd5a73122aa7d1312ba583f20e4ae4f64582844999df09e" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_low_rank_base.py.bytes | 3982 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_budget_v2.py.bytes | 2794 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_budget_v2.py.sha256 | "1d797ef6d41a0f4da77b88cf4076ec3ec6267246d9a562d564cb8e9987d58117" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_comparison.py.bytes | 2734 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_comparison.py.sha256 | "a53ecfb4811256bc5d40de9227de4b42b56467efc56f2f63bb780dfec8388563" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_condition.py.bytes | 3190 |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/probe/source/tests/test_source_order_condition.py.sha256 | "358621d322be46b1e2520da76c09490384f33ca7c49d3cac3ff15523613f87f7" |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_proposal.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_v2_proposal.json) ／ SHA256: `f235c0414bfecfb4034608eed92d6f8d8cc8fd4fbefed9e5c93b6d5accd374dd` ／ 3,174 bytes

| 原キー | 保存値 |
|---|---|
| hypothesis | "Restrict the learned update subspace rather than adding an L2 penalty or altering data/loss/order. Frozen W0 does not guarantee preserved active-model Web quality." |
| distinct_from_failed_branches | ["full-model L2 displacement anchor", "full-model weight averaging", "Web logit KL", "packing isolation", "sequence unlikelihood"] |
| input_target_budget | "Each3068 updates/100532224 input/91641755 actual masked teachers; same original100M reference quota ledger. Not100M actual teachers." |
| CPU_preparation_ceiling_seconds | 30 |
| probe_GPU_ceiling_seconds | 240 |
| total_new_GPU_ceiling_seconds | 1800 |
| GPU_seconds_so_far | 0 |
| new_teacher_tokens_so_far | 0 |
| completion | "Both actual endpoints and all160 raw-bound content reviews; unchanged strong/absolute/historical-Web gates, exact terminal identity and UI restoration. Only a qualified recipe may enter independent learned seed/full-dev/protected-test/adoption." |
| failure_policy | "End fixed rank4 comparison; no rank/module/scale/LR/source/mask/decoder/checkpoint salvage sweep." |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>
