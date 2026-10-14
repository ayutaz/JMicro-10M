# 実行管理・後続準備・その他 — 19/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/compare-result.json — two_arm_GPU_complete_pending_all160_content_review</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/compare-result.json) ／ SHA256: `6d4248efd068a273c9b1ca34f5df288e307c1cd4cf295e4c982f742ce7c8a0e2` ／ 537,102 bytes

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
| scientific_teacher_tokens | 183283510 |
| scientific_optimizer_updates | 6136 |
| status | "two_arm_GPU_complete_pending_all160_content_review" |
| GPU_seconds | 539.8163853790029 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam-content-notes.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam-content-notes.json) ／ SHA256: `aef67ea301ef9ced00b526fc09b81ce8d5c24e892f375086c5a421722708e581` ／ 62,238 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/full_fresh_Adam/training/latest.json) ／ SHA256: `aa8ec2224d672e13a0fc56b707e312b504b19946795798e9900fb94cd653f67c` ／ 291 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/job.json) ／ SHA256: `96cd14adc2ac407a08d14aff49dc9d972dc26108f215707419af5fec69131632` ／ 749 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 539.8163853790029 |
| completed_updates | 3060 |
| total_updates | 3068 |
| actual_teachers | 91426867 |
| loss | 2.561180353164673 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/full_fresh_Adam/timing/latest.json) ／ SHA256: `f1a8c47952d8fd21d3623be16390b352df72283195d9d2e74d88b5767d8f0983` ／ 286 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/job.json) ／ SHA256: `d41f8427d65ea7dd89887769029b13d6260c6cceb8bba6fa233999d9cb6e3985` ／ 573 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 58.92843314999482 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/progress-result.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/progress-result.json) ／ SHA256: `f9ef6a9bde7c83d2b0d717169b4a1058a3d897bfaef6738b1f8644cb4a6b8796` ／ 549,063 bytes

| 原キー | 保存値 |
|---|---|
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

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json — None</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/rank4_frozen_backbone/timing/latest.json) ／ SHA256: `9f4d3d5355c8e20cc4eba80a2e0cc1e6478a9f52eaf5c830760a783b2522a891` ／ 292 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>

<details>
<summary>reports/phase6/low-rank-base-comparison-v2-20261006/probe/result.json — own_two_arm_CUDA_probe_complete</summary>

[原記録](../../reports/phase6/low-rank-base-comparison-v2-20261006/probe/result.json) ／ SHA256: `05f864752f66504342f9a790eb01712300a5eaa15bf9e8b8fab41f7e3027db13` ／ 549,578 bytes

| 原キー | 保存値 |
|---|---|
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
| GPU_optimizer_updates | 96 |
| verification_teacher_tokens | 2867838 |
| scientific_teacher_tokens | 0 |
| passed | true |
| status | "own_two_arm_CUDA_probe_complete" |
| GPU_seconds | 58.92843314999482 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |

</details>
