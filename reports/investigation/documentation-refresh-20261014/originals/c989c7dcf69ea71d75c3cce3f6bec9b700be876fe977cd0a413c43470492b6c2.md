# 学習目的・最適化・正則化 — 2/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/progress-result.json) ／ SHA256: `a6ed6eb2964b11160f95381c508b0f46439d8035f28a123dc9bd44c6789d7ffb` ／ 1,978,327 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt" |
| checkpoints.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| checkpoints.control.binding.config_sha256 | "03b4ad47fa42b9a669c4588e736648e6339c93b9eb0cf3d08aac22a46cf90a88" |
| checkpoints.control.binding.arm | "source_order" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.control.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.control.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 1e-05 |
| checkpoints.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.control.binding.study_kind | "historical_parent_source_order_100M" |
| checkpoints.control.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| checkpoints.control.binding.outcome_weight | 1 |
| checkpoints.control.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.control.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.control.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.control.update | 323503 |
| checkpoints.control.tokens | 10600546304 |
| checkpoints.control.supervised_tokens | 10577786961 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100532224 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.control.source_teachers.conditional_textbook | 10000000 |
| checkpoints.control.source_eos.web | 159170 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.ordinary_textbook | 74183 |
| checkpoints.control.source_eos.conditional_textbook | 234328 |
| checkpoints.control.source_input_tokens.web | 75183104 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.control.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.control.source_focus_teachers.web | 0 |
| checkpoints.control.source_focus_teachers.story | 0 |
| checkpoints.control.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.control.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.control.focus_teacher_tokens | 1407427 |
| checkpoints.control.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.control.weighted_teacher_mass | 100000000 |
| checkpoints.control.outcome_weight | 1 |
| checkpoints.control.training_seconds | 163.39403466315707 |
| checkpoints.control.completed_at | "2026-10-06T06:25:12.649548Z" |
| checkpoints.anchored_context_outcome.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/anchored-context-outcome-comparison-20261006/anchored_context_outcome/training/checkpoint-00323503.pt" |
| checkpoints.anchored_context_outcome.checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| checkpoints.anchored_context_outcome.binding.config_sha256 | "10a398a2533ba51b9522e37f7ed764fdb0d4050fea680d5cba1be8ec40f91d24" |
| checkpoints.anchored_context_outcome.binding.arm | "anchored_context_outcome" |
| checkpoints.anchored_context_outcome.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.anchored_context_outcome.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.anchored_context_outcome.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.anchored_context_outcome.binding.teacher_goals.web | 75000000 |
| checkpoints.anchored_context_outcome.binding.teacher_goals.story | 5000000 |
| checkpoints.anchored_context_outcome.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.anchored_context_outcome.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.anchored_context_outcome.binding.optimizer_policy | "inherit" |
| checkpoints.anchored_context_outcome.binding.peak_lr | 1e-05 |
| checkpoints.anchored_context_outcome.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.anchored_context_outcome.binding.study_kind | "historical_parent_staged_CE_conditional_Web_KL_train_anchored_outcome_ranking_100M" |
| checkpoints.anchored_context_outcome.binding.sampler_policy | "Same full parent/main100M CE/Web KL/TRAIN pair windows as ranking control; one positive nonEOS CE anchor, no extra input/corpus/reset/reheat." |
| checkpoints.anchored_context_outcome.binding.outcome_weight | 1 |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.kind | "train_gold_outcome_non_EOS_positive_CE_anchor_v1" |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.gold_rows | "For each existing4-row family: branch0-candidate0 and branch1-candidate1 only." |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.objective | "Sum gold-body conditional nonEOS token NLL divided by actual positive body token count." |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.vocabulary | "Remove EOS3 only; retain all other vocabulary IDs. Prefix/padding ignored; complete body labels&gt;=8." |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.exposure | "Reuse the existing8x256 paired logits/input/labels, no extra forward/data/window; gold positions become separately counted hard teachers." |
| checkpoints.anchored_context_outcome.binding.positive_anchor_policy.update | "Ranking and positive anchor combined in one backward; ordinaryCE,WebKL,combined pair gradients precede one clip/Adam/scheduler update." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| checkpoints.anchored_context_outcome.binding.ranking_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.binding.ranking_policy.temperature | 1.0 |
| checkpoints.anchored_context_outcome.binding.ranking_policy.families_per_update | 2 |
| checkpoints.anchored_context_outcome.binding.ranking_policy.candidate_rows_per_family | 4 |
| checkpoints.anchored_context_outcome.binding.ranking_policy.context | 256 |
| checkpoints.anchored_context_outcome.binding.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| checkpoints.anchored_context_outcome.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| checkpoints.anchored_context_outcome.binding.ranking_inputs.path | "/home/aihub_ubuntu/jmicro-data/phase6/context-outcome-ranking-20261006/manifest.json" |
| checkpoints.anchored_context_outcome.binding.ranking_inputs.sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.anchored_context_outcome.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.anchored_context_outcome.binding.KL_policy.direction | "parent_to_student" |
| checkpoints.anchored_context_outcome.binding.KL_policy.temperature | 1.0 |
| checkpoints.anchored_context_outcome.binding.KL_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.binding.KL_policy.every_completed_update | 1 |
| checkpoints.anchored_context_outcome.binding.KL_policy.reference_context | 1024 |
| checkpoints.anchored_context_outcome.binding.KL_policy.reference_batch | 8 |
| checkpoints.anchored_context_outcome.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.anchored_context_outcome.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.anchored_context_outcome.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.anchored_context_outcome.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| checkpoints.anchored_context_outcome.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.anchored_context_outcome.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.anchored_context_outcome.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.anchored_context_outcome.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.anchored_context_outcome.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.anchored_context_outcome.update | 323503 |
| checkpoints.anchored_context_outcome.tokens | 10600546304 |
| checkpoints.anchored_context_outcome.supervised_tokens | 10577786961 |
| checkpoints.anchored_context_outcome.additional_supervised_tokens | 100000000 |
| checkpoints.anchored_context_outcome.additional_input_tokens | 100532224 |
| checkpoints.anchored_context_outcome.source_teachers.web | 75000000 |
| checkpoints.anchored_context_outcome.source_teachers.story | 5000000 |
| checkpoints.anchored_context_outcome.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.anchored_context_outcome.source_teachers.conditional_textbook | 10000000 |
| checkpoints.anchored_context_outcome.source_eos.web | 159170 |
| checkpoints.anchored_context_outcome.source_eos.story | 38240 |
| checkpoints.anchored_context_outcome.source_eos.ordinary_textbook | 74183 |
| checkpoints.anchored_context_outcome.source_eos.conditional_textbook | 234328 |
| checkpoints.anchored_context_outcome.source_input_tokens.web | 75183104 |
| checkpoints.anchored_context_outcome.source_input_tokens.story | 5039104 |
| checkpoints.anchored_context_outcome.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.anchored_context_outcome.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.anchored_context_outcome.source_focus_teachers.web | 0 |
| checkpoints.anchored_context_outcome.source_focus_teachers.story | 0 |
| checkpoints.anchored_context_outcome.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.anchored_context_outcome.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.anchored_context_outcome.focus_teacher_tokens | 1407427 |
| checkpoints.anchored_context_outcome.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.anchored_context_outcome.weighted_teacher_mass | 100000000 |
| checkpoints.anchored_context_outcome.outcome_weight | 1 |
| checkpoints.anchored_context_outcome.training_seconds | 440.8266774234653 |
| checkpoints.anchored_context_outcome.completed_at | "2026-10-06T08:54:29.087545Z" |
| checkpoints.anchored_context_outcome.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| checkpoints.anchored_context_outcome.reference_replay.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.anchored_context_outcome.reference_replay.batch | 8 |
| checkpoints.anchored_context_outcome.reference_replay.context | 1024 |
| checkpoints.anchored_context_outcome.reference_replay.initial_cursor.seed | 42 |
| checkpoints.anchored_context_outcome.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.anchored_context_outcome.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.anchored_context_outcome.reference_replay.initial_cursor.context | 1024 |
| checkpoints.anchored_context_outcome.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.anchored_context_outcome.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.anchored_context_outcome.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.anchored_context_outcome.reference_replay.stream.sampler.seed | 42 |
| checkpoints.anchored_context_outcome.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.anchored_context_outcome.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.anchored_context_outcome.reference_replay.stream.sampler.context | 1024 |
| checkpoints.anchored_context_outcome.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.anchored_context_outcome.reference_replay.updates | 3068 |
| checkpoints.anchored_context_outcome.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.anchored_context_outcome.reference_replay.body_positions | 25026383 |
| checkpoints.anchored_context_outcome.reference_replay.ignored_positions | 106673 |
| checkpoints.anchored_context_outcome.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.anchored_context_outcome.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.anchored_context_outcome.reference_input_tokens | 25133056 |
| checkpoints.anchored_context_outcome.reference_soft_target_body_positions | 25026383 |
| checkpoints.anchored_context_outcome.main_and_Web_reference_physical_input_tokens | 125665280 |
| checkpoints.anchored_context_outcome.combined_student_physical_input_tokens | 131948544 |
| checkpoints.anchored_context_outcome.combined_student_valid_input_tokens | 126688260 |
| checkpoints.anchored_context_outcome.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| checkpoints.anchored_context_outcome.ranking_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.ranking_policy.temperature | 1.0 |
| checkpoints.anchored_context_outcome.ranking_policy.families_per_update | 2 |
| checkpoints.anchored_context_outcome.ranking_policy.candidate_rows_per_family | 4 |
| checkpoints.anchored_context_outcome.ranking_policy.context | 256 |
| checkpoints.anchored_context_outcome.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| checkpoints.anchored_context_outcome.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| checkpoints.anchored_context_outcome.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| checkpoints.anchored_context_outcome.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| checkpoints.anchored_context_outcome.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| checkpoints.anchored_context_outcome.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| checkpoints.anchored_context_outcome.ranking_input_binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.anchored_context_outcome.ranking_input_binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| checkpoints.anchored_context_outcome.ranking_input_binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.anchored_context_outcome.ranking_input_binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| checkpoints.anchored_context_outcome.ranking_input_binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| checkpoints.anchored_context_outcome.ranking_input_binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| checkpoints.anchored_context_outcome.ranking_input_binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checkpoints.anchored_context_outcome.ranking_input_binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| checkpoints.anchored_context_outcome.ranking_sampler.kind | "train_family_outcome_ranking_sampler_v1" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checkpoints.anchored_context_outcome.ranking_sampler.binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| checkpoints.anchored_context_outcome.ranking_sampler.seed | 42 |
| checkpoints.anchored_context_outcome.ranking_sampler.families_per_update | 2 |
| checkpoints.anchored_context_outcome.ranking_sampler.context | 256 |
| checkpoints.anchored_context_outcome.ranking_sampler.epoch | 5 |
| checkpoints.anchored_context_outcome.ranking_sampler.position | 1016 |
| checkpoints.anchored_context_outcome.ranking_sampler.updates | 3068 |
| checkpoints.anchored_context_outcome.ranking_sampler.families_seen | 6136 |
| checkpoints.anchored_context_outcome.ranking_sampler.relational_choice_labels | 12272 |
| checkpoints.anchored_context_outcome.ranking_sampler.valid_input_tokens | 1022980 |
| checkpoints.anchored_context_outcome.ranking_sampler.physical_input_positions | 6283264 |
| checkpoints.anchored_context_outcome.ranking_sampler.gold_body_scored_positions | 73725 |
| checkpoints.anchored_context_outcome.ranking_sampler.foil_body_scored_positions | 73725 |
| checkpoints.anchored_context_outcome.ranking_sampler.gold_body_scored_bytes | 315047 |
| checkpoints.anchored_context_outcome.ranking_sampler.foil_body_scored_bytes | 315047 |
| checkpoints.anchored_context_outcome.ranking_sampler.digest | "f5fda5bbab96066a63a036f6f33fd98998a0f043c83503b6cd07fd0a0ed23cbe" |
| checkpoints.anchored_context_outcome.ranking_exposure.updates | 3068 |
| checkpoints.anchored_context_outcome.ranking_exposure.families_seen | 6136 |
| checkpoints.anchored_context_outcome.ranking_exposure.relational_choice_labels | 12272 |
| checkpoints.anchored_context_outcome.ranking_exposure.valid_input_tokens | 1022980 |
| checkpoints.anchored_context_outcome.ranking_exposure.physical_input_positions | 6283264 |
| checkpoints.anchored_context_outcome.ranking_exposure.gold_body_scored_positions | 73725 |
| checkpoints.anchored_context_outcome.ranking_exposure.foil_body_scored_positions | 73725 |
| checkpoints.anchored_context_outcome.ranking_exposure.gold_body_scored_bytes | 315047 |
| checkpoints.anchored_context_outcome.ranking_exposure.foil_body_scored_bytes | 315047 |
| checkpoints.anchored_context_outcome.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.anchored_context_outcome.KL_policy.direction | "parent_to_student" |
| checkpoints.anchored_context_outcome.KL_policy.temperature | 1.0 |
| checkpoints.anchored_context_outcome.KL_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.KL_policy.every_completed_update | 1 |
| checkpoints.anchored_context_outcome.KL_policy.reference_context | 1024 |
| checkpoints.anchored_context_outcome.KL_policy.reference_batch | 8 |
| checkpoints.anchored_context_outcome.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.anchored_context_outcome.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.anchored_context_outcome.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.anchored_context_outcome.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| checkpoints.anchored_context_outcome.positive_anchor_policy.kind | "train_gold_outcome_non_EOS_positive_CE_anchor_v1" |
| checkpoints.anchored_context_outcome.positive_anchor_policy.coefficient | 1.0 |
| checkpoints.anchored_context_outcome.positive_anchor_policy.gold_rows | "For each existing4-row family: branch0-candidate0 and branch1-candidate1 only." |
| checkpoints.anchored_context_outcome.positive_anchor_policy.objective | "Sum gold-body conditional nonEOS token NLL divided by actual positive body token count." |
| checkpoints.anchored_context_outcome.positive_anchor_policy.vocabulary | "Remove EOS3 only; retain all other vocabulary IDs. Prefix/padding ignored; complete body labels&gt;=8." |
| checkpoints.anchored_context_outcome.positive_anchor_policy.exposure | "Reuse the existing8x256 paired logits/input/labels, no extra forward/data/window; gold positions become separately counted hard teachers." |
| checkpoints.anchored_context_outcome.positive_anchor_policy.update | "Ranking and positive anchor combined in one backward; ordinaryCE,WebKL,combined pair gradients precede one clip/Adam/scheduler update." |
| checkpoints.anchored_context_outcome.positive_anchor_body_teacher_tokens | 73725 |
| checkpoints.anchored_context_outcome.combined_hard_teacher_positions | 100073725 |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.control.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.control.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.control.binding.sampler_policy | "Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding." |
| evaluations.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 370922.2019701004 |
| evaluations.control.body.eos_nll | 404.9141170345247 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1336128657420816 |
| evaluations.control.body.seconds | 1.6409143939963542 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 76 |
| evaluations.control.greedy_rates.repetition | 2 |
| evaluations.control.greedy_rates.unicode_failure | 0 |
| evaluations.control.greedy_rates.role_leak | 0 |
| evaluations.control.greedy_rates.empty | 0 |
| evaluations.control.diagnostics.semantics.primary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6041666666666666] |
| evaluations.control.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.primary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.4791666666666667, 0.5208333333333334] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.0 |
| evaluations.control.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.control.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.control.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7371601208459214, 0.8277945619335347] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.743202416918429 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7008308157099699, 0.7915407854984894] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.743202416918429 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42634315424610053 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.control.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.control.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.control.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.7824773413897281 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.26541554959785524 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.2386058981233244, 0.291331546023235] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.26541554959785524 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.26630920464700625 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.24037086684539768, 0.2931188561215371] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.26630920464700625 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.26555235832138696 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.08306759781336262 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.control.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.control.diagnostics.semantic_both_contexts.correct | 14 |
| evaluations.control.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.control.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.control.protected_test_used | false |
| evaluations.anchored_context_outcome.binding.teacher_goals.web | 75000000 |
| evaluations.anchored_context_outcome.binding.teacher_goals.story | 5000000 |
| evaluations.anchored_context_outcome.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.anchored_context_outcome.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.anchored_context_outcome.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.anchored_context_outcome.binding.sampler_policy | "Same full parent/main100M CE/Web KL/TRAIN pair windows as ranking control; one positive nonEOS CE anchor, no extra input/corpus/reset/reheat." |
| evaluations.anchored_context_outcome.binding.positive_anchor_policy.update | "Ranking and positive anchor combined in one backward; ordinaryCE,WebKL,combined pair gradients precede one clip/Adam/scheduler update." |
| evaluations.anchored_context_outcome.binding.ranking_policy.families_per_update | 2 |
| evaluations.anchored_context_outcome.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| evaluations.anchored_context_outcome.binding.KL_policy.every_completed_update | 1 |
| evaluations.anchored_context_outcome.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| evaluations.anchored_context_outcome.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.anchored_context_outcome.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.anchored_context_outcome.checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| evaluations.anchored_context_outcome.body.documents | 256 |
| evaluations.anchored_context_outcome.body.limit_documents | 256 |
| evaluations.anchored_context_outcome.body.body_nll | 323885.3029294014 |
| evaluations.anchored_context_outcome.body.eos_nll | 478.9777773749083 |
| evaluations.anchored_context_outcome.body.body_bytes | 472055 |
| evaluations.anchored_context_outcome.body.body_tokens | 122343 |
| evaluations.anchored_context_outcome.body.bpb | 0.9898586401014015 |
| evaluations.anchored_context_outcome.body.seconds | 1.2865901720069814 |
| evaluations.anchored_context_outcome.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.anchored_context_outcome.generation.max_new_tokens | 64 |
| evaluations.anchored_context_outcome.greedy_rates.eos | 40 |
| evaluations.anchored_context_outcome.greedy_rates.repetition | 28 |
| evaluations.anchored_context_outcome.greedy_rates.unicode_failure | 0 |
| evaluations.anchored_context_outcome.greedy_rates.role_leak | 0 |
| evaluations.anchored_context_outcome.greedy_rates.empty | 0 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.point | 0.671875 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.ci95 | [0.6197916666666666, 0.7188802083333327] |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.primary.hard_accuracy | 0.671875 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.point | 0.6145833333333334 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5729166666666666, 0.65625] |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.6145833333333334 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.macro_f1 | 0.6142065819485174 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.mcc | 0.22961557339788813 |
| evaluations.anchored_context_outcome.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.anchored_context_outcome.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.point | 0.7643504531722054 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.ci95 | [0.7190332326283988, 0.8096676737160121] |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.primary.hard_accuracy | 0.7643504531722054 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7039274924471299 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6555891238670695, 0.7552870090634441] |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7039274924471299 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41312056737588654 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.anchored_context_outcome.diagnostics.jblimp.raw_pair_accuracy | 0.7643504531722054 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.point | 0.3494191242180518 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.ci95 | [0.32171581769436997, 0.3762287756925827] |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.primary.hard_accuracy | 0.3494191242180518 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3333333333333333 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.30650134048257377, 0.3610366398570152] |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3333333333333333 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3329130501779027 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.mcc | 0.16745826052541415 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.anchored_context_outcome.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.anchored_context_outcome.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.anchored_context_outcome.diagnostics.semantic_both_contexts.correct | 33 |
| evaluations.anchored_context_outcome.memory.maximum_observed_allocated_bytes | 348777472 |
| evaluations.anchored_context_outcome.memory.maximum_observed_reserved_bytes | 12694061056 |
| evaluations.anchored_context_outcome.protected_test_used | false |
| mechanism_cached.checkpoints.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context-outcome-ranking-comparison-20261006/context_outcome_ranking/training/checkpoint-00323503.pt" |
| mechanism_cached.checkpoints.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| mechanism_cached.checkpoints.binding.config_sha256 | "8de26074f0701ec1894fc239430179eaaa3e8096f5828359083da12377ef01b4" |
| mechanism_cached.checkpoints.binding.arm | "context_outcome_ranking" |
| mechanism_cached.checkpoints.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.checkpoints.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.checkpoints.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| mechanism_cached.checkpoints.binding.teacher_goals.web | 75000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.story | 5000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.ordinary_textbook | 10000000 |
| mechanism_cached.checkpoints.binding.teacher_goals.conditional_textbook | 10000000 |
| mechanism_cached.checkpoints.binding.optimizer_policy | "inherit" |
| mechanism_cached.checkpoints.binding.peak_lr | 1e-05 |
| mechanism_cached.checkpoints.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| mechanism_cached.checkpoints.binding.study_kind | "historical_parent_staged_CE_conditional_Web_KL_train_outcome_ranking_100M" |
| mechanism_cached.checkpoints.binding.sampler_policy | "Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus." |
| mechanism_cached.checkpoints.binding.outcome_weight | 1 |
| mechanism_cached.checkpoints.binding.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| mechanism_cached.checkpoints.binding.ranking_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.binding.ranking_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.binding.ranking_policy.families_per_update | 2 |
| mechanism_cached.checkpoints.binding.ranking_policy.candidate_rows_per_family | 4 |
| mechanism_cached.checkpoints.binding.ranking_policy.context | 256 |
| mechanism_cached.checkpoints.binding.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| mechanism_cached.checkpoints.binding.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| mechanism_cached.checkpoints.binding.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| mechanism_cached.checkpoints.binding.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| mechanism_cached.checkpoints.binding.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| mechanism_cached.checkpoints.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| mechanism_cached.checkpoints.binding.ranking_inputs.path | "/home/aihub_ubuntu/jmicro-data/phase6/context-outcome-ranking-20261006/manifest.json" |
| mechanism_cached.checkpoints.binding.ranking_inputs.sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| mechanism_cached.checkpoints.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| mechanism_cached.checkpoints.binding.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.binding.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.binding.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| mechanism_cached.checkpoints.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.checkpoints.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| mechanism_cached.checkpoints.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.checkpoints.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.checkpoints.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| mechanism_cached.checkpoints.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| mechanism_cached.checkpoints.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| mechanism_cached.checkpoints.update | 323503 |
| mechanism_cached.checkpoints.tokens | 10600546304 |
| mechanism_cached.checkpoints.supervised_tokens | 10577786961 |
| mechanism_cached.checkpoints.additional_supervised_tokens | 100000000 |
| mechanism_cached.checkpoints.additional_input_tokens | 100532224 |
| mechanism_cached.checkpoints.source_teachers.web | 75000000 |
| mechanism_cached.checkpoints.source_teachers.story | 5000000 |
| mechanism_cached.checkpoints.source_teachers.ordinary_textbook | 10000000 |
| mechanism_cached.checkpoints.source_teachers.conditional_textbook | 10000000 |
| mechanism_cached.checkpoints.source_eos.web | 159170 |
| mechanism_cached.checkpoints.source_eos.story | 38240 |
| mechanism_cached.checkpoints.source_eos.ordinary_textbook | 74183 |
| mechanism_cached.checkpoints.source_eos.conditional_textbook | 234328 |
| mechanism_cached.checkpoints.source_input_tokens.web | 75183104 |
| mechanism_cached.checkpoints.source_input_tokens.story | 5039104 |
| mechanism_cached.checkpoints.source_input_tokens.ordinary_textbook | 10075136 |
| mechanism_cached.checkpoints.source_input_tokens.conditional_textbook | 10234880 |
| mechanism_cached.checkpoints.source_focus_teachers.web | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.story | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.ordinary_textbook | 0 |
| mechanism_cached.checkpoints.source_focus_teachers.conditional_textbook | 1407427 |
| mechanism_cached.checkpoints.focus_teacher_tokens | 1407427 |
| mechanism_cached.checkpoints.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| mechanism_cached.checkpoints.weighted_teacher_mass | 100000000 |
| mechanism_cached.checkpoints.outcome_weight | 1 |
| mechanism_cached.checkpoints.training_seconds | 441.0778062947211 |
| mechanism_cached.checkpoints.completed_at | "2026-10-06T08:28:04.933673Z" |
| mechanism_cached.checkpoints.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| mechanism_cached.checkpoints.reference_replay.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| mechanism_cached.checkpoints.reference_replay.batch | 8 |
| mechanism_cached.checkpoints.reference_replay.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.seed | 42 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.epoch | 0 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.position | 10253920 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.initial_cursor.blocks | 11939276 |
| mechanism_cached.checkpoints.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| mechanism_cached.checkpoints.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.seed | 42 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.epoch | 0 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.position | 10278464 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.context | 1024 |
| mechanism_cached.checkpoints.reference_replay.stream.sampler.blocks | 11939276 |
| mechanism_cached.checkpoints.reference_replay.updates | 3068 |
| mechanism_cached.checkpoints.reference_replay.physical_input_tokens | 25133056 |
| mechanism_cached.checkpoints.reference_replay.body_positions | 25026383 |
| mechanism_cached.checkpoints.reference_replay.ignored_positions | 106673 |
| mechanism_cached.checkpoints.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| mechanism_cached.checkpoints.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| mechanism_cached.checkpoints.reference_input_tokens | 25133056 |
| mechanism_cached.checkpoints.reference_soft_target_body_positions | 25026383 |
| mechanism_cached.checkpoints.main_and_Web_reference_physical_input_tokens | 125665280 |
| mechanism_cached.checkpoints.combined_student_physical_input_tokens | 131948544 |
| mechanism_cached.checkpoints.combined_student_valid_input_tokens | 126688260 |
| mechanism_cached.checkpoints.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| mechanism_cached.checkpoints.ranking_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.ranking_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.ranking_policy.families_per_update | 2 |
| mechanism_cached.checkpoints.ranking_policy.candidate_rows_per_family | 4 |
| mechanism_cached.checkpoints.ranking_policy.context | 256 |
| mechanism_cached.checkpoints.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| mechanism_cached.checkpoints.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| mechanism_cached.checkpoints.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| mechanism_cached.checkpoints.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| mechanism_cached.checkpoints.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| mechanism_cached.checkpoints.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| mechanism_cached.checkpoints.ranking_input_binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| mechanism_cached.checkpoints.ranking_input_binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| mechanism_cached.checkpoints.ranking_input_binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| mechanism_cached.checkpoints.ranking_input_binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| mechanism_cached.checkpoints.ranking_input_binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| mechanism_cached.checkpoints.ranking_input_binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| mechanism_cached.checkpoints.ranking_input_binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| mechanism_cached.checkpoints.ranking_input_binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| mechanism_cached.checkpoints.ranking_sampler.kind | "train_family_outcome_ranking_sampler_v1" |
| mechanism_cached.checkpoints.ranking_sampler.binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| mechanism_cached.checkpoints.ranking_sampler.binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| mechanism_cached.checkpoints.ranking_sampler.binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| mechanism_cached.checkpoints.ranking_sampler.binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| mechanism_cached.checkpoints.ranking_sampler.binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| mechanism_cached.checkpoints.ranking_sampler.binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| mechanism_cached.checkpoints.ranking_sampler.binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| mechanism_cached.checkpoints.ranking_sampler.binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| mechanism_cached.checkpoints.ranking_sampler.seed | 42 |
| mechanism_cached.checkpoints.ranking_sampler.families_per_update | 2 |
| mechanism_cached.checkpoints.ranking_sampler.context | 256 |
| mechanism_cached.checkpoints.ranking_sampler.epoch | 5 |
| mechanism_cached.checkpoints.ranking_sampler.position | 1016 |
| mechanism_cached.checkpoints.ranking_sampler.updates | 3068 |
| mechanism_cached.checkpoints.ranking_sampler.families_seen | 6136 |
| mechanism_cached.checkpoints.ranking_sampler.relational_choice_labels | 12272 |
| mechanism_cached.checkpoints.ranking_sampler.valid_input_tokens | 1022980 |
| mechanism_cached.checkpoints.ranking_sampler.physical_input_positions | 6283264 |
| mechanism_cached.checkpoints.ranking_sampler.gold_body_scored_positions | 73725 |
| mechanism_cached.checkpoints.ranking_sampler.foil_body_scored_positions | 73725 |
| mechanism_cached.checkpoints.ranking_sampler.gold_body_scored_bytes | 315047 |
| mechanism_cached.checkpoints.ranking_sampler.foil_body_scored_bytes | 315047 |
| mechanism_cached.checkpoints.ranking_sampler.digest | "f5fda5bbab96066a63a036f6f33fd98998a0f043c83503b6cd07fd0a0ed23cbe" |
| mechanism_cached.checkpoints.ranking_exposure.updates | 3068 |
| mechanism_cached.checkpoints.ranking_exposure.families_seen | 6136 |
| mechanism_cached.checkpoints.ranking_exposure.relational_choice_labels | 12272 |
| mechanism_cached.checkpoints.ranking_exposure.valid_input_tokens | 1022980 |
| mechanism_cached.checkpoints.ranking_exposure.physical_input_positions | 6283264 |
| mechanism_cached.checkpoints.ranking_exposure.gold_body_scored_positions | 73725 |
| mechanism_cached.checkpoints.ranking_exposure.foil_body_scored_positions | 73725 |
| mechanism_cached.checkpoints.ranking_exposure.gold_body_scored_bytes | 315047 |
| mechanism_cached.checkpoints.ranking_exposure.foil_body_scored_bytes | 315047 |
| mechanism_cached.checkpoints.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| mechanism_cached.checkpoints.KL_policy.direction | "parent_to_student" |
| mechanism_cached.checkpoints.KL_policy.temperature | 1.0 |
| mechanism_cached.checkpoints.KL_policy.coefficient | 1.0 |
| mechanism_cached.checkpoints.KL_policy.every_completed_update | 1 |
| mechanism_cached.checkpoints.KL_policy.reference_context | 1024 |
| mechanism_cached.checkpoints.KL_policy.reference_batch | 8 |
| mechanism_cached.checkpoints.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| mechanism_cached.checkpoints.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.checkpoints.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| mechanism_cached.checkpoints.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| mechanism_cached.evaluations.binding.teacher_goals.web | 75000000 |
| mechanism_cached.evaluations.binding.teacher_goals.story | 5000000 |
| mechanism_cached.evaluations.binding.teacher_goals.ordinary_textbook | 10000000 |
| mechanism_cached.evaluations.binding.teacher_goals.conditional_textbook | 10000000 |
| mechanism_cached.evaluations.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| mechanism_cached.evaluations.binding.sampler_policy | "Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus." |
| mechanism_cached.evaluations.binding.ranking_policy.families_per_update | 2 |
| mechanism_cached.evaluations.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| mechanism_cached.evaluations.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.evaluations.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.evaluations.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.evaluations.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.evaluations.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| mechanism_cached.evaluations.body.documents | 256 |
| mechanism_cached.evaluations.body.limit_documents | 256 |
| mechanism_cached.evaluations.body.body_nll | 323411.1250305176 |
| mechanism_cached.evaluations.body.eos_nll | 517.7313129939139 |
| mechanism_cached.evaluations.body.body_bytes | 472055 |
| mechanism_cached.evaluations.body.body_tokens | 122343 |
| mechanism_cached.evaluations.body.bpb | 0.9884094570544709 |
| mechanism_cached.evaluations.body.seconds | 1.2839610580122098 |
| mechanism_cached.evaluations.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| mechanism_cached.evaluations.generation.max_new_tokens | 64 |
| mechanism_cached.evaluations.greedy_rates.eos | 41 |
| mechanism_cached.evaluations.greedy_rates.repetition | 21 |
| mechanism_cached.evaluations.greedy_rates.unicode_failure | 0 |
| mechanism_cached.evaluations.greedy_rates.role_leak | 0 |
| mechanism_cached.evaluations.greedy_rates.empty | 0 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.point | 0.59375 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.ci95 | [0.546875, 0.640625] |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6354166666666666] |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.count | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5882624392627378 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.mcc | 0.17732400774015752 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.train_majority_accuracy | 0.5 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.ci95 | [0.7069486404833837, 0.797583081570997] |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.count | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| mechanism_cached.evaluations.diagnostics.jblimp.train_majority_accuracy | null |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.ci95 | [0.3118856121537087, 0.3672922252010724] |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32082216264521896 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2931188561215371, 0.3485254691689008] |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.count | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32082216264521896 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3202529966325722 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.mcc | 0.15168655619820284 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| mechanism_cached.evaluations.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| mechanism_cached.evaluations.diagnostics.semantic_both_contexts.correct | 21 |
| mechanism_cached.evaluations.memory.maximum_observed_allocated_bytes | 348777472 |
| mechanism_cached.evaluations.memory.maximum_observed_reserved_bytes | 12694061056 |
| mechanism_cached.evaluations.protected_test_used | false |
| mechanism_cached.transfer.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| mechanism_cached.transfer.checks.weights_unchanged | true |
| mechanism_cached.transfer.checks.no_gradients | true |
| mechanism_cached.transfer.checks.eval_mode | true |
| mechanism_cached.transfer.checks.RNG_restored | true |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7578125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.both_correct | 86 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7578125 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 86 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 86 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| mechanism_cached.transfer.optimizer_updates | 0 |
| mechanism_cached.transfer.scientific_teacher_tokens | 0 |
| mechanism_cached.transfer.protected_test_used | false |
| mechanism_cached.transfer.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| mechanism_cached.retention.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| mechanism_cached.retention.checks.weights_unchanged | true |
| mechanism_cached.retention.checks.no_gradients | true |
| mechanism_cached.retention.checks.eval_mode | true |
| mechanism_cached.retention.checks.RNG_restored | true |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.78125 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 53 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 27 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7734375 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 38 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 53 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 27 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 27 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.78125 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 40 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 53 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 27 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 29 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| mechanism_cached.retention.optimizer_updates | 0 |
| mechanism_cached.retention.scientific_teacher_tokens | 0 |
| mechanism_cached.retention.protected_test_used | false |
| mechanism_cached.retention.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| transfer.control.checks.weights_unchanged | true |
| transfer.control.checks.no_gradients | true |
| transfer.control.checks.eval_mode | true |
| transfer.control.checks.RNG_restored | true |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 59 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer.control.optimizer_updates | 0 |
| transfer.control.scientific_teacher_tokens | 0 |
| transfer.control.protected_test_used | false |
| transfer.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| transfer.anchored_context_outcome.checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| transfer.anchored_context_outcome.checks.weights_unchanged | true |
| transfer.anchored_context_outcome.checks.no_gradients | true |
| transfer.anchored_context_outcome.checks.eval_mode | true |
| transfer.anchored_context_outcome.checks.RNG_restored | true |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.70703125 |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.all128.both_correct | 79 |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.421875 |
| transfer.anchored_context_outcome.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 16 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.703125 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 79 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 96 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4140625 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 16 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.70703125 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 79 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 96 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.421875 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 22 |
| transfer.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| transfer.anchored_context_outcome.optimizer_updates | 0 |
| transfer.anchored_context_outcome.scientific_teacher_tokens | 0 |
| transfer.anchored_context_outcome.protected_test_used | false |
| transfer.anchored_context_outcome.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.control.checkpoint_sha256 | "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae" |
| retention.control.checks.weights_unchanged | true |
| retention.control.checks.no_gradients | true |
| retention.control.checks.eval_mode | true |
| retention.control.checks.RNG_restored | true |
| retention.control.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention.control.summary.aggregate.sum_log_likelihood.all128.both_correct | 36 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention.control.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.control.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 42 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention.control.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention.control.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention.control.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention.control.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention.control.optimizer_updates | 0 |
| retention.control.scientific_teacher_tokens | 0 |
| retention.control.protected_test_used | false |
| retention.control.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.anchored_context_outcome.checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| retention.anchored_context_outcome.checks.weights_unchanged | true |
| retention.anchored_context_outcome.checks.no_gradients | true |
| retention.anchored_context_outcome.checks.eval_mode | true |
| retention.anchored_context_outcome.checks.RNG_restored | true |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.80078125 |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 54 |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6796875 |
| retention.anchored_context_outcome.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 26 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7890625 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 42 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 54 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 10 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.65625 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 26 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| retention.anchored_context_outcome.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.80078125 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 45 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 54 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 10 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6796875 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 26 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| retention.anchored_context_outcome.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention.anchored_context_outcome.optimizer_updates | 0 |
| retention.anchored_context_outcome.scientific_teacher_tokens | 0 |
| retention.anchored_context_outcome.protected_test_used | false |
| retention.anchored_context_outcome.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/review.json — positive_anchor100M_all80_and_strong_stagedCE_reviewed</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/review.json) ／ SHA256: `df57f485609d317f1d9e941d2b138eebb137831311f1548d8d8c15f572b6c040` ／ 15,775 bytes

| 原キー | 保存値 |
|---|---|
| status | "positive_anchor100M_all80_and_strong_stagedCE_reviewed" |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | false |
| mechanism_comparison.checks.repetition_nonworsening | false |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
| mechanism_summary.BPB | 0.9884094570544709 |
| mechanism_summary.rates.eos | 41 |
| mechanism_summary.rates.repetition | 21 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 37 |
| mechanism_summary.relevance2 | 41 |
| mechanism_summary.coherent | 2 |
| mechanism_summary.appropriate | 22 |
| mechanism_summary.notes_sha256 | "e03024c23b3a5e2fb5e27ce6490db590e8eab6ef0d9c2942a1df785acbea8d76" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| previous_related_study_GPU_seconds | 1734.8376444790629 |
| summaries.control.BPB | 1.1336128657420816 |
| summaries.control.rates.eos | 76 |
| summaries.control.rates.repetition | 2 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 65 |
| summaries.control.relevance2 | 39 |
| summaries.control.coherent | 23 |
| summaries.control.appropriate | 26 |
| summaries.control.notes_sha256 | "6b143e08096a1ee2365a643c008d5c009d2c2ff48dd1d42a9749ac5301766d2d" |
| summaries.control.additional_teacher_tokens | 100000000 |
| summaries.anchored_context_outcome.BPB | 0.9898586401014015 |
| summaries.anchored_context_outcome.rates.eos | 40 |
| summaries.anchored_context_outcome.rates.repetition | 28 |
| summaries.anchored_context_outcome.rates.unicode_failure | 0 |
| summaries.anchored_context_outcome.rates.role_leak | 0 |
| summaries.anchored_context_outcome.rates.empty | 0 |
| summaries.anchored_context_outcome.grammar2 | 34 |
| summaries.anchored_context_outcome.relevance2 | 70 |
| summaries.anchored_context_outcome.coherent | 5 |
| summaries.anchored_context_outcome.appropriate | 16 |
| summaries.anchored_context_outcome.notes_sha256 | "cb5970e6f45d834687451e466f062e9f2b99c7990f638aaaba8b03037d1b0256" |
| summaries.anchored_context_outcome.additional_teacher_tokens | 100000000 |
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
| absolute_dev_screen.EOS_at_least37 | true |
| absolute_dev_screen.repetition_at_most18 | false |
| absolute_dev_screen.no_empty_role_unicode | true |
| original_Web.EOS_at_least8_more | true |
| original_Web.repetition_no_worse | true |
| original_Web.no_empty_role_unicode | true |
| original_Web.BPB_degradation_at_most1percent | false |
| retained_source_checks.all_four_source_cursors_and_accounting_equal | true |
| retained_source_checks.original_Web_cursor_retained | true |
| retained_source_checks.Web_blocks_consumed | 73421 |
| reference_accounting.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| reference_accounting.frozen_parent_teacher_digest_verified | true |
| reference_accounting.reference_input_tokens | 25133056 |
| reference_accounting.main_ordinary_CE_teacher_tokens | 100000000 |
| reference_accounting.main_and_Web_reference_physical_input_tokens | 125665280 |
| reference_accounting.newly_prepared_source_tokens | 0 |
| ranking_accounting.ranking_exposure.updates | 3068 |
| ranking_accounting.ranking_exposure.valid_input_tokens | 1022980 |
| ranking_accounting.ranking_exposure.physical_input_positions | 6283264 |
| ranking_accounting.ranking_exposure.gold_body_scored_bytes | 315047 |
| ranking_accounting.ranking_exposure.foil_body_scored_bytes | 315047 |
| ranking_accounting.combined_student_physical_input_tokens | 131948544 |
| ranking_accounting.combined_student_valid_input_tokens | 126688260 |
| ranking_accounting.ranking_ordinary_CE_teacher_tokens | 0 |
| ranking_accounting.new_original_corpus_tokens | 0 |
| positive_anchor_accounting.positive_anchor_body_teacher_tokens | 73725 |
| positive_anchor_accounting.combined_hard_teacher_positions | 100073725 |
| positive_anchor_accounting.foil_hard_teacher_positions | 0 |
| positive_anchor_accounting.new_original_corpus_tokens | 0 |
| positive_anchor_accounting.all_completed_positive_teacher_and_loss_rows_verified | true |
| eligible_for_final_Base_validation | false |
| transfer_aggregates.control.sum_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.sum_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.both_correct | 59 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 49 |
| transfer_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.40625 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 8 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 36 |
| transfer_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.6640625 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 62 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 46 |
| transfer_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 85 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.8984375 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 51 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 13 |
| transfer_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4296875 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 33 |
| transfer_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 21 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.all128.accuracy | 0.70703125 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.all128.both_correct | 79 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.structural_holdout.accuracy | 0.421875 |
| transfer_aggregates.anchored_context_outcome.sum_log_likelihood.structural_holdout.both_correct | 16 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.accuracy | 0.703125 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.both_correct | 79 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.aligned_context_margin_shift | 96 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.accuracy | 0.4140625 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.both_correct | 16 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.accuracy | 0.70703125 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.both_correct | 79 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 96 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.accuracy | 0.421875 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 22 |
| transfer_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| retention_aggregates.control.sum_log_likelihood.all128.accuracy | 0.62890625 |
| retention_aggregates.control.sum_log_likelihood.all128.both_correct | 36 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| retention_aggregates.control.sum_log_likelihood.lexical_holdout.both_correct | 25 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.sum_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_token_log_likelihood.all128.accuracy | 0.65234375 |
| retention_aggregates.control.mean_token_log_likelihood.all128.both_correct | 42 |
| retention_aggregates.control.mean_token_log_likelihood.all128.same_unique_candidate | 83 |
| retention_aggregates.control.mean_token_log_likelihood.all128.aligned_context_margin_shift | 99 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.accuracy | 0.734375 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.both_correct | 30 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| retention_aggregates.control.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 53 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 49 |
| retention_aggregates.control.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.accuracy | 0.65625 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.both_correct | 43 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.same_unique_candidate | 82 |
| retention_aggregates.control.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 100 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.75 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.both_correct | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 32 |
| retention_aggregates.control.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5625 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.both_correct | 11 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 50 |
| retention_aggregates.control.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 46 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.all128.accuracy | 0.80078125 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.lexical_holdout.both_correct | 54 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.structural_holdout.accuracy | 0.6796875 |
| retention_aggregates.anchored_context_outcome.sum_log_likelihood.structural_holdout.both_correct | 26 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.accuracy | 0.7890625 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.same_unique_candidate | 42 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.both_correct | 54 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 10 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.accuracy | 0.65625 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.both_correct | 26 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 32 |
| retention_aggregates.anchored_context_outcome.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.accuracy | 0.80078125 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.same_unique_candidate | 45 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 108 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.921875 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.both_correct | 54 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 10 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 60 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6796875 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.both_correct | 26 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 35 |
| retention_aggregates.anchored_context_outcome.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 48 |
| verification_ranking_exposure.updates | 40 |
| verification_ranking_exposure.families_seen | 80 |
| verification_ranking_exposure.relational_choice_labels | 160 |
| verification_ranking_exposure.valid_input_tokens | 13376 |
| verification_ranking_exposure.physical_input_positions | 81920 |
| verification_ranking_exposure.gold_body_scored_positions | 933 |
| verification_ranking_exposure.foil_body_scored_positions | 933 |
| verification_ranking_exposure.gold_body_scored_bytes | 4022 |
| verification_ranking_exposure.foil_body_scored_bytes | 4022 |
| verification_positive_anchor_teacher_tokens | 933 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 523.4998286040209 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| verification_GPU_seconds | 31.25854540299042 |
| prior_probe_GPU_seconds | 0.0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "One100M mainCE with same parent/Adam/scheduler/RNG/LR/source quotas/order and same conditional parent Web KL windows. Pair exposure is identical to the completed ranking mechanism control but adds positive hard teachers. Strong stagedCE remains the quality control. No equality of supervision/time is claimed. No new corpus. Shared-generator local probes/nonblind repeated dev/one learned seed; independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0000.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0000.json) ／ SHA256: `56d3fb429bad5e91040cd1e84e86932e3bdbda89689c39736dd08fe9b3ec0f9a` ／ 10,075 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0016.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0016.json) ／ SHA256: `8c74bd2fa61ada126932c790dfd5e21996e2b1960cc68925ac637264ed899dd5` ／ 9,719 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0032.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0032.json) ／ SHA256: `07ba715fac186501df0d37e22c716110efd2359def7787bb3875b33636a244a7` ／ 10,354 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0048.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0048.json) ／ SHA256: `4357671b1b12eb138d5682e08e12d1bb0459db0f848f2f3ac65ee48a25af3ef2` ／ 9,647 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0064.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0064.json) ／ SHA256: `c7a1ccc5a3259a0baca60302faff9182118e5eae279182085d015bd312bb6402` ／ 10,418 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0080.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0080.json) ／ SHA256: `311c2b2858a284593e7b8155ff3a385826707d53dd3326b8e8c37da03f572c75` ／ 9,817 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0096.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0096.json) ／ SHA256: `d05f5644e0a5fecf5919f5b4fadd994b60b215ff775a7dc094168778eecfe1d7` ／ 9,913 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0112.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0112.json) ／ SHA256: `120d1422c4bdf2e1c36131e0bb5867614a70788032d65b8af3ee322ef062c2c1` ／ 10,265 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0128.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0128.json) ／ SHA256: `aad2836c7f72e9bc06bfc875d0a2c022a3803f491060805c36936b792fe617d7` ／ 9,934 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0144.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0144.json) ／ SHA256: `2f3f61e42288fd0aec417371433b2ca0fbc71515712014a7ec3ca5ef958f373e` ／ 10,001 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0160.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0160.json) ／ SHA256: `1a7dccc7c5ec243484ef8486de02dea4b1ddffd01092e8354fc1771bffa030a7` ／ 10,244 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0176.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0176.json) ／ SHA256: `ffd54773ff5b2c70c024dfaf330dcf93a2607fecf18cbfcd6c8c4fe04ac92170` ／ 10,097 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0192.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0192.json) ／ SHA256: `7ff5d06e600b79b687c07bcdbe9c6540ce13bf85701bf2b2c664c63abba55b9e` ／ 10,026 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0208.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0208.json) ／ SHA256: `a220f433c2fa86d0a9884e1ad3d11beecb4077673a0784ef8a71a35ccbc86b96` ／ 9,732 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0224.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0224.json) ／ SHA256: `9899833818f0e8cf90b1ecc69dfc6d5c0db335d4dd97ed0656b10468c5f28e88` ／ 9,930 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0240.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0240.json) ／ SHA256: `d2e82a0e961293d206d9d4ef256d9c00d328b4de68b801d163e1af028d0aa4fe` ／ 9,742 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0256.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0256.json) ／ SHA256: `79caf416ac9cdfb7054cb9942ac05b8f7721bdcfac4f58fa61df6a6799b47eca` ／ 9,726 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0272.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0272.json) ／ SHA256: `cf09265a66251181a3f67602bf9ad50045647e998c6280ee22057d503220ae50` ／ 9,699 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0288.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0288.json) ／ SHA256: `5883618fa2ac60da5131f7b79d4680c1029756fdb2035b92170375a50927c078` ／ 9,727 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0304.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0304.json) ／ SHA256: `09a4638a631b586722c585774ec68847bc7c65b4b7c7bbdb72996ac71697ef7a` ／ 9,925 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0320.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0320.json) ／ SHA256: `a3bea5389da62f4f706df6294cb8e1a12c56ddf80347404b3b5c15b63a212b7f` ／ 9,450 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0336.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0336.json) ／ SHA256: `393bdc46c1282866e82389047d7baa54a9014563929856879ca55fe36cdb32c4` ／ 9,543 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0352.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0352.json) ／ SHA256: `b752e32ac3b5f55c48e1488e583db66442854df1facb5e70979ee7111cde03a8` ／ 9,903 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0368.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0368.json) ／ SHA256: `49fbdc5005ca43ecf3adcc5995db5b22d5709551a886dba3e0566b245812df84` ／ 9,639 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0384.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0384.json) ／ SHA256: `a7fc5966f0b3bf4cba64635888116d746786e467483e3c3112bc7a38703d5cc4` ／ 9,998 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0400.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0400.json) ／ SHA256: `4282943d3ae646912219de2986550daac4811fa4c7342537132076d903b86d08` ／ 9,645 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0416.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0416.json) ／ SHA256: `0ec2d99aaa182f61661537a347add79aad1f58bc6d17ffb68442f4a53ae394f3` ／ 9,993 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0432.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0432.json) ／ SHA256: `babfd763429d35719a0bc613ccd97d6449aa0c468adb626dfc1cddbbae94cd28` ／ 9,437 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0448.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0448.json) ／ SHA256: `3dc26d69db516092cf1f04914e281464054bc448df4030a5689a9b891e178ba6` ／ 9,727 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0464.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0464.json) ／ SHA256: `5ad6299a17460e0c81861f5aac70f432e5252afdf69f790c2cf7086c68fb7b67` ／ 9,520 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0480.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0480.json) ／ SHA256: `f085c9836ed679e2d5963622d80f15e1c34a5ad1e09a707c557bf7497ae6f812` ／ 9,538 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0496.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/0496.json) ／ SHA256: `dadba733952d7a6ba79147058550d8f1e51d94c10e6ddb135e7f88b2c94ae0e4` ／ 9,590 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/result.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/bridge/anchored_context_outcome/result.json) ／ SHA256: `a58dc6bccc2f0850d8eec122ea9804c442ad079fc1e428b72578ce7925f3d3db` ／ 185,495 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.70703125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 79 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.421875 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 16 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.703125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 79 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 96 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.4140625 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 16 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.70703125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 79 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 23 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 96 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.421875 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 16 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 22 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 32 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0000.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0000.json) ／ SHA256: `5190057a813a4372472a78562d2a81e18866b029641a0bd552bf2dbcc9680b6f` ／ 8,023 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0016.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0016.json) ／ SHA256: `dec457c8258ce222783633e480e51f386f91cef642c632e8d51902c06acfb84a` ／ 8,332 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0032.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0032.json) ／ SHA256: `96e34a5cb25949a0cf09df050acbfa913ca45671bef7af359bf42e77d7ff699a` ／ 7,032 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0048.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0048.json) ／ SHA256: `e77b4259e9772f973229033e5e8c43c1df938b8c7a05b9c627b87d67a24dd61f` ／ 8,211 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0064.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0064.json) ／ SHA256: `1428d4bef54ede54f6954ef9d1203c5009c9df1bb4da0672d94177f3a127642a` ／ 8,570 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0080.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0080.json) ／ SHA256: `0465eda840e7effb6fd205b5aed36ba14db4616511b30ae4af8151219626cb74` ／ 7,154 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0096.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0096.json) ／ SHA256: `270d3990fdd8855066deb7f00610a69c9cbbbf9cffe6ade9ab4a2e6b6e968012` ／ 8,131 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0112.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0112.json) ／ SHA256: `164cb9d91c1ed9266d7c6a37d476d49e011223bcb036ead018044609fcaaacf5` ／ 8,311 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0128.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0128.json) ／ SHA256: `82b88c4eb7a2b6134ea97227b018094c7b63c5a4cf77c151cd2d47ae0e30289b` ／ 7,107 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0144.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0144.json) ／ SHA256: `77c85246ccfe27cabf8eafdf2e694f5474ba019db473a1ea82ff14753956020c` ／ 8,220 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0160.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0160.json) ／ SHA256: `949e2899ebb65b2573fa7615de863c5bf9394f24f722c637a1df32e7f47ea1b1` ／ 8,666 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0176.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0176.json) ／ SHA256: `95f71ec1849ffabbd57dd1fd12366ed6c8f2aa39ced7260c53d561039d645ba7` ／ 6,987 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0192.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0192.json) ／ SHA256: `5cc58df7cc370900fa09eaee59dcd9108911fadac54e741f942c1d2e2f776e46` ／ 8,227 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0208.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/transfer/retention/anchored_context_outcome/0208.json) ／ SHA256: `ec64bed6c7bf3fe1832383562a16d8f50a357f4b00b88460d4112cfc51e6b32c` ／ 8,541 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |

</details>
