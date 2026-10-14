# 学習目的・最適化・正則化 — 1/17

[分野一覧へ](04_objectives.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/anchored_context_outcome/training/latest.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/anchored_context_outcome/training/latest.json) ／ SHA256: `abc223d96898ae13e67ac9278260db677b2b7e5678922fa6cc527b6a34db3541` ／ 308 bytes

| 原キー | 保存値 |
|---|---|
| update | 323503 |
| tokens_seen | 10600546304 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/compare-result.json — positive_anchor100M_and_cached_strong_stagedCE_complete</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/compare-result.json) ／ SHA256: `5a0f5b651736355e9976fbe24f129801dcfd4e3578b84a9322b309954f444481` ／ 1,979,584 bytes

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
| status | "positive_anchor100M_and_cached_strong_stagedCE_complete" |
| scientific_teacher_tokens | 100000000 |
| total_comparison_teachers | 200000000 |
| reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| previous_related_study_GPU_seconds | 1734.8376444790629 |
| mechanism_comparison_teacher_tokens | 200000000 |
| reference_input_tokens | 25133056 |
| ranking_exposure.updates | 3068 |
| ranking_exposure.valid_input_tokens | 1022980 |
| ranking_exposure.physical_input_positions | 6283264 |
| ranking_exposure.gold_body_scored_bytes | 315047 |
| ranking_exposure.foil_body_scored_bytes | 315047 |
| new_original_corpus_tokens | 0 |
| positive_anchor_body_teacher_tokens | 73725 |
| combined_hard_teacher_positions | 100073725 |
| Base_adopted | false |
| protected_test_used | false |
| GPU_seconds | 523.4998286040209 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/content-packets/anchored_context_outcome.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/content-packets/anchored_context_outcome.json) ／ SHA256: `2d1684d500e0188e36b343fcdfe1f316e38bc5a1eada36985e08907490871676` ／ 110,256 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/body.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/body.json) ／ SHA256: `0f29fe8ddeba0ff6055fba2afd763c562eb3b647a5f09f9bbba7d5b44f837ea6` ／ 70,680 bytes

| 原キー | 保存値 |
|---|---|
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 323885.3029294014 |
| body.eos_nll | 478.9777773749083 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9898586401014015 |
| body.seconds | 1.2865901720069814 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/generation.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/generation.json) ／ SHA256: `3f13654ce98fcbea4c72ef6dd541010f7dc20000cb531ffb5036f63ab4dc2f1a` ／ 97,154 bytes

| 原キー | 保存値 |
|---|---|
| max_new_tokens | 64 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/jblimp.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/jblimp.json) ／ SHA256: `01d06d944f860b157496b5b0fb6c174ed4db619e59b988a7b1cfe54e6438b61c` ／ 341,873 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.7643504531722054 |
| summary.primary.accuracy.ci95 | [0.7190332326283988, 0.8096676737160121] |
| summary.primary.accuracy.units | 331 |
| summary.primary.accuracy.examples | 331 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.7643504531722054 |
| summary.per_token_secondary.accuracy.point | 0.7039274924471299 |
| summary.per_token_secondary.accuracy.ci95 | [0.6555891238670695, 0.7552870090634441] |
| summary.per_token_secondary.accuracy.units | 331 |
| summary.per_token_secondary.accuracy.examples | 331 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 331 |
| summary.per_token_secondary.hard_accuracy | 0.7039274924471299 |
| summary.per_token_secondary.macro_f1 | 0.41312056737588654 |
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
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/jcqa.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/jcqa.json) ／ SHA256: `2dc6b21a4b4fcea8926e67aae7e7323f08746e7471ead281821a42a8c99766d0` ／ 1,644,683 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.3494191242180518 |
| summary.primary.accuracy.ci95 | [0.32171581769436997, 0.3762287756925827] |
| summary.primary.accuracy.units | 1119 |
| summary.primary.accuracy.examples | 1119 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.3494191242180518 |
| summary.per_token_secondary.accuracy.point | 0.3333333333333333 |
| summary.per_token_secondary.accuracy.ci95 | [0.30650134048257377, 0.3610366398570152] |
| summary.per_token_secondary.accuracy.units | 1119 |
| summary.per_token_secondary.accuracy.examples | 1119 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 1119 |
| summary.per_token_secondary.hard_accuracy | 0.3333333333333333 |
| summary.per_token_secondary.macro_f1 | 0.3329130501779027 |
| summary.per_token_secondary.mcc | 0.16745826052541415 |
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
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/result.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/result.json) ／ SHA256: `e77bc57b3b185ac4e271a1098e3f6167123a473d16bc2e76d1e68e053621c88e` ／ 195,768 bytes

| 原キー | 保存値 |
|---|---|
| binding.teacher_goals.web | 75000000 |
| binding.teacher_goals.story | 5000000 |
| binding.teacher_goals.ordinary_textbook | 10000000 |
| binding.teacher_goals.conditional_textbook | 10000000 |
| binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| binding.sampler_policy | "Same full parent/main100M CE/Web KL/TRAIN pair windows as ranking control; one positive nonEOS CE anchor, no extra input/corpus/reset/reheat." |
| binding.positive_anchor_policy.update | "Ranking and positive anchor combined in one backward; ordinaryCE,WebKL,combined pair gradients precede one clip/Adam/scheduler update." |
| binding.ranking_policy.families_per_update | 2 |
| binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| binding.KL_policy.every_completed_update | 1 |
| binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoint_sha256 | "7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662" |
| body.documents | 256 |
| body.limit_documents | 256 |
| body.body_nll | 323885.3029294014 |
| body.eos_nll | 478.9777773749083 |
| body.body_bytes | 472055 |
| body.body_tokens | 122343 |
| body.bpb | 0.9898586401014015 |
| body.seconds | 1.2865901720069814 |
| body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| generation.max_new_tokens | 64 |
| greedy_rates.eos | 40 |
| greedy_rates.repetition | 28 |
| greedy_rates.unicode_failure | 0 |
| greedy_rates.role_leak | 0 |
| greedy_rates.empty | 0 |
| diagnostics.semantics.primary.accuracy.point | 0.671875 |
| diagnostics.semantics.primary.accuracy.ci95 | [0.6197916666666666, 0.7188802083333327] |
| diagnostics.semantics.primary.accuracy.units | 96 |
| diagnostics.semantics.primary.accuracy.examples | 192 |
| diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.primary.accuracy.seed | 42 |
| diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.primary.hard_accuracy | 0.671875 |
| diagnostics.semantics.per_token_secondary.accuracy.point | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5729166666666666, 0.65625] |
| diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.semantics.per_token_secondary.count | 192 |
| diagnostics.semantics.per_token_secondary.hard_accuracy | 0.6145833333333334 |
| diagnostics.semantics.per_token_secondary.macro_f1 | 0.6142065819485174 |
| diagnostics.semantics.per_token_secondary.mcc | 0.22961557339788813 |
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
| diagnostics.jblimp.primary.accuracy.point | 0.7643504531722054 |
| diagnostics.jblimp.primary.accuracy.ci95 | [0.7190332326283988, 0.8096676737160121] |
| diagnostics.jblimp.primary.accuracy.units | 331 |
| diagnostics.jblimp.primary.accuracy.examples | 331 |
| diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.primary.accuracy.seed | 42 |
| diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.primary.hard_accuracy | 0.7643504531722054 |
| diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7039274924471299 |
| diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6555891238670695, 0.7552870090634441] |
| diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jblimp.per_token_secondary.count | 331 |
| diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7039274924471299 |
| diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41312056737588654 |
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
| diagnostics.jblimp.raw_pair_accuracy | 0.7643504531722054 |
| diagnostics.jcqa.primary.accuracy.point | 0.3494191242180518 |
| diagnostics.jcqa.primary.accuracy.ci95 | [0.32171581769436997, 0.3762287756925827] |
| diagnostics.jcqa.primary.accuracy.units | 1119 |
| diagnostics.jcqa.primary.accuracy.examples | 1119 |
| diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.primary.accuracy.seed | 42 |
| diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.primary.hard_accuracy | 0.3494191242180518 |
| diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3333333333333333 |
| diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.30650134048257377, 0.3610366398570152] |
| diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| diagnostics.jcqa.per_token_secondary.count | 1119 |
| diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3333333333333333 |
| diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3329130501779027 |
| diagnostics.jcqa.per_token_secondary.mcc | 0.16745826052541415 |
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
| diagnostics.semantic_both_contexts.correct | 33 |
| memory.maximum_observed_allocated_bytes | 348777472 |
| memory.maximum_observed_reserved_bytes | 12694061056 |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/evaluation/anchored_context_outcome/evaluation/semantics.json) ／ SHA256: `d476feea469cb552a94966458933942f0e4106246b4b5ee0d2692d3affc1e49f` ／ 206,629 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.671875 |
| summary.primary.accuracy.ci95 | [0.6197916666666666, 0.7188802083333327] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.671875 |
| summary.per_token_secondary.accuracy.point | 0.6145833333333334 |
| summary.per_token_secondary.accuracy.ci95 | [0.5729166666666666, 0.65625] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.6145833333333334 |
| summary.per_token_secondary.macro_f1 | 0.6142065819485174 |
| summary.per_token_secondary.mcc | 0.22961557339788813 |
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
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/job.json) ／ SHA256: `41950afad23eba7a94eb72db80230020c6335b7f78889afba2b451db3716838f` ／ 932 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 523.4998286040209 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99767422 |
| teacher_budget | 100000000 |
| source_teachers.web | 75000000 |
| source_teachers.story | 5000000 |
| source_teachers.ordinary_textbook | 10000000 |
| source_teachers.conditional_textbook | 9767422 |
| loss | 0.6452912576496601 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/probe/initial-parent-preservation.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/probe/initial-parent-preservation.json) ／ SHA256: `7e3baba2df7953d4543f1aa8dfb9201879154985b785d86eb0d487734d738771` ／ 266 bytes

| 原キー | 保存値 |
|---|---|
| parent_sampler_lineage | true |
| frozen_teacher_weights | true |
| frozen_teacher_eval_no_grad | true |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/probe/job.json) ／ SHA256: `8c7fa903e4f7025667fd00b1a049d2311d053375c9f65f3e23dd42a07feefc2f` ／ 605 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 31.25854540299042 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/probe/result.json — actual_positive_anchor_full_resume_timing_complete</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/probe/result.json) ／ SHA256: `3894168df298b8d8f626dc167c1ffdb2808fc7356ef7e7e8f5129d70b361165d` ／ 124,339 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_positive_anchor_full_resume_timing_complete" |
| passed | true |
| gate.passed | true |
| gate.checks.model | true |
| gate.checks.optimizer | true |
| gate.checks.scheduler | true |
| gate.checks.rng | true |
| gate.checks.sampler | true |
| gate.checks.lineage | true |
| gate.checks.tokens | true |
| gate.checks.supervised_tokens | true |
| gate.checks.body_bytes | true |
| gate.checks.token_digest | true |
| gate.checks.focus_token_digest | true |
| gate.checks.focus_teacher_tokens | true |
| gate.checks.weighted_teacher_mass | true |
| gate.checks.update | true |
| gate.checks.spec | true |
| gate.checks.model_config | true |
| gate.checks.pilot_binding | true |
| gate.checks.study_binding | true |
| gate.checks.KL_state | true |
| gate.checks.ranking_state | true |
| gate.checks.positive_anchor_state | true |
| gate.checks.history_loss | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_lr | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.history_ordinary_CE_loss | true |
| gate.checks.history_reference_KL_loss | true |
| gate.checks.history_reference_non_EOS_teacher_probability_mass | true |
| gate.checks.history_reference_input_tokens | true |
| gate.checks.history_reference_soft_target_body_positions | true |
| gate.checks.history_reference_ignored_positions | true |
| gate.checks.history_reference_digest | true |
| gate.checks.history_combined_student_physical_input_tokens | true |
| gate.checks.history_positive_anchor_loss | true |
| gate.checks.history_combined_pair_loss | true |
| gate.checks.history_positive_anchor_body_teacher_tokens | true |
| gate.checks.history_combined_hard_teacher_positions | true |
| gate.checks.history_ranking_loss | true |
| gate.checks.history_ranking_family_indices | true |
| gate.checks.history_ranking_digest | true |
| gate.checks.history_ranking_relational_choice_labels | true |
| gate.checks.history_ranking_valid_input_tokens | true |
| gate.checks.history_ranking_physical_input_positions | true |
| gate.checks.history_ranking_gold_body_scored_positions | true |
| gate.checks.history_ranking_foil_body_scored_positions | true |
| gate.checks.history_ranking_gold_body_scored_bytes | true |
| gate.checks.history_ranking_foil_body_scored_bytes | true |
| gate.checks.history_combined_student_valid_input_tokens | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.verification_reference_non_EOS_teacher_probability_mass | 65163.615234375 |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 261602 |
| gate.verification_reference_input_tokens | 65536 |
| gate.verification_reference_soft_positions | 65276 |
| gate.verification_ranking.updates | 8 |
| gate.verification_ranking.families_seen | 16 |
| gate.verification_ranking.relational_choice_labels | 32 |
| gate.verification_ranking.valid_input_tokens | 2768 |
| gate.verification_ranking.physical_input_positions | 16384 |
| gate.verification_ranking.gold_body_scored_positions | 186 |
| gate.verification_ranking.foil_body_scored_positions | 186 |
| gate.verification_ranking.gold_body_scored_bytes | 834 |
| gate.verification_ranking.foil_body_scored_bytes | 834 |
| gate.verification_positive_anchor_teacher_tokens | 186 |
| timing.verification_teacher_tokens | 1046365 |
| timing.terminal_save_seconds | 0.16856681401259266 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/anchored-context-outcome-comparison-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "c5220ef9c26ccb9a5fe88db6437981984cc6d81632bc647fc3c44e43953b11e6" |
| timing.reference_non_EOS_teacher_probability_mass | 260614.552734375 |
| timing.reference_input_tokens | 262144 |
| timing.verification_ranking.updates | 32 |
| timing.verification_ranking.families_seen | 64 |
| timing.verification_ranking.relational_choice_labels | 128 |
| timing.verification_ranking.valid_input_tokens | 10608 |
| timing.verification_ranking.physical_input_positions | 65536 |
| timing.verification_ranking.gold_body_scored_positions | 747 |
| timing.verification_ranking.foil_body_scored_positions | 747 |
| timing.verification_ranking.gold_body_scored_bytes | 3188 |
| timing.verification_ranking.foil_body_scored_bytes | 3188 |
| timing.positive_anchor_teacher_tokens | 747 |
| verification_teacher_tokens | 1307967 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| initial_parent_preservation.parent_sampler_lineage | true |
| initial_parent_preservation.frozen_teacher_weights | true |
| initial_parent_preservation.frozen_teacher_eval_no_grad | true |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| verification_ranking.updates | 40 |
| verification_ranking.families_seen | 80 |
| verification_ranking.relational_choice_labels | 160 |
| verification_ranking.valid_input_tokens | 13376 |
| verification_ranking.physical_input_positions | 81920 |
| verification_ranking.gold_body_scored_positions | 933 |
| verification_ranking.foil_body_scored_positions | 933 |
| verification_ranking.gold_body_scored_bytes | 4022 |
| verification_ranking.foil_body_scored_bytes | 4022 |
| verification_positive_anchor_teacher_tokens | 933 |
| GPU_seconds | 31.25854540299042 |

</details>

<details>
<summary>reports/phase6/anchored-context-outcome-comparison-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/anchored-context-outcome-comparison-20261006/probe/timing/latest.json) ／ SHA256: `f66feef962f96734d4574402435004fcd3428ace87534434bdbf4c7eae463c0c` ／ 278 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>
